#!/usr/bin/env python3
"""Rapid-fire photo collector. Per-project hard timeout 60s; resume via manifests."""
from __future__ import annotations

import csv
import hashlib
import io
import multiprocessing as mp
import os
import re
import signal
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError as FutTimeout
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup
from PIL import Image

STORE = Path("/cursor/stores/self")
PROJECTS_DOC = STORE / "docs" / "projects"
MEDIA_ROOT = STORE / "media" / "projects"
TODAY = date.today().isoformat()
UA = "Mozilla/5.0 (compatible; CursorPhotoCollector/0.2)"
MAX_PER_PROJECT = 35
MIN_EDGE = 400
PAGE_TIMEOUT = 8
IMG_TIMEOUT = 8
MAX_PAGES = 5
MAX_DOWNLOADS = 45
PROJECT_HARD_TIMEOUT = 60  # kill if stuck > 1 min
SLEEP = 0.05

SKIP_SUBSTR = (
    "favicon", "sprite", "1x1", "pixel.gif", "tracking", "gravatar",
    "emoji", "wp-includes", "/icons/", "data:image", ".svg", "spinner",
    "placeholder", "loading.gif", "badge",
)
WP_SIZE_RE = re.compile(r"-\d{2,4}x\d{2,4}(?=\.(?:jpe?g|png|webp|gif)$)", re.I)


def officialish(publisher: str, stype: str) -> int:
    blob = f"{publisher} {stype}".lower()
    if any(k in blob for k in ("official", "project_site", "developer", "nema", "esia", "eia")):
        return 5
    if "marketing" in blob or "related_party" in blob or "brochure" in blob:
        return 4
    if "agent" in blob:
        return 3
    return 2


def categorize(url: str, alt: str = "") -> str:
    blob = f"{url} {alt}".lower()
    if any(k in blob for k in ("floorplan", "floor-plan", "site-plan", "layout", "typology")):
        return "plans"
    if any(k in blob for k in ("progress", "construction", "crane")):
        return "progress"
    if any(k in blob for k in ("pool", "gym", "lobby", "amenit", "garden", "rooftop")):
        return "amenities"
    if any(k in blob for k in ("interior", "living", "bedroom", "kitchen", "showhouse", "show-house")):
        return "interior"
    if any(k in blob for k in ("exterior", "facade", "tower", "render", "elevation", "aerial")):
        return "exterior"
    return "other"


def parse_dossier_sources(md_path: Path) -> list[dict]:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    sources, seen = [], set()
    for m in re.finditer(
        r"^\|\s*\d+\s*\|\s*(https?://[^|\s]+)\s*\|\s*([^|]*)\|\s*([^|]*)\|",
        text,
        re.M,
    ):
        url = m.group(1).strip().split()[0].rstrip(")")
        if not url.startswith("http") or url.lower().endswith(".pdf"):
            continue
        if url in seen:
            continue
        seen.add(url)
        pub, st = m.group(2).strip(), m.group(3).strip()
        sources.append({"url": url, "publisher": pub, "type": st, "confidence": officialish(pub, st)})
    return sources


def fetch(url: str, timeout: int = PAGE_TIMEOUT) -> tuple[bytes | None, str | None]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            # hard cap body size 8MB
            data = resp.read(8_000_000)
            return data, resp.headers.get_content_type()
    except Exception as e:
        return None, str(e)[:120]


def absolutize(base: str, src: str) -> str | None:
    if not src or src.startswith("data:"):
        return None
    return urllib.parse.urljoin(base, src.strip().strip("\"'"))


def pick_srcset(srcset: str, base: str) -> str | None:
    best_url, best_w = None, -1
    for part in srcset.split(","):
        bits = part.strip().split()
        if not bits:
            continue
        u = absolutize(base, bits[0])
        w = 0
        if len(bits) > 1 and bits[1].endswith("w"):
            try:
                w = int(bits[1][:-1])
            except ValueError:
                pass
        if u and w >= best_w:
            best_w, best_url = w, u
    return best_url


def upgrade_wp(url: str) -> list[str]:
    out = [url]
    path = urllib.parse.urlparse(url).path
    if WP_SIZE_RE.search(path):
        out.insert(0, WP_SIZE_RE.sub("", url))
    if "-scaled." in path:
        out.insert(0, url.replace("-scaled.", "."))
    return out


def extract_images(page_url: str, html: bytes) -> list[tuple[str, str]]:
    soup = BeautifulSoup(html, "lxml")
    found, seen = [], set()

    def add(u: str | None, alt: str = ""):
        if not u:
            return
        low = u.lower()
        if any(s in low for s in SKIP_SUBSTR):
            return
        path = low.split("?")[0]
        if not any(path.endswith(e) for e in (".jpg", ".jpeg", ".png", ".webp", ".gif")):
            if not re.search(r"/uploads/|/image|/img|/photo|/media/", low):
                return
        for cand in upgrade_wp(u):
            if cand not in seen:
                seen.add(cand)
                found.append((cand, alt))

    for meta in soup.find_all("meta", property=re.compile(r"og:image", re.I)):
        add(absolutize(page_url, meta.get("content") or ""))
    for img in soup.find_all("img"):
        alt = img.get("alt") or ""
        srcset = img.get("srcset") or img.get("data-srcset") or ""
        if srcset:
            add(pick_srcset(srcset, page_url), alt)
        for attr in ("src", "data-src", "data-lazy-src", "data-original", "data-large_image"):
            if img.get(attr):
                add(absolutize(page_url, img.get(attr)), alt)
    return found


def image_dims(data: bytes) -> tuple[int, int]:
    try:
        with Image.open(io.BytesIO(data)) as im:
            return im.size
    except Exception:
        return 0, 0


def ext_for(url: str, ctype: str | None, data: bytes) -> str:
    path = urllib.parse.urlparse(url).path.lower()
    for e in (".jpg", ".jpeg", ".png", ".webp", ".gif"):
        if path.endswith(e):
            return ".jpg" if e == ".jpeg" else e
    if ctype:
        if "png" in ctype:
            return ".png"
        if "webp" in ctype:
            return ".webp"
        if "gif" in ctype:
            return ".gif"
    if data[:8].startswith(b"\x89PNG"):
        return ".png"
    if data[:4] == b"RIFF" and b"WEBP" in data[:16]:
        return ".webp"
    return ".jpg"


def download_one(url: str, meta: dict) -> dict | None:
    data, ctype = fetch(url, timeout=IMG_TIMEOUT)
    if data is None or len(data) < 2500:
        return None
    if ctype and not str(ctype).startswith("image"):
        if not (data[:2] == b"\xff\xd8" or data[:8].startswith(b"\x89PNG") or b"WEBP" in data[:16]):
            return None
    w, h = image_dims(data)
    if max(w, h) and max(w, h) < MIN_EDGE:
        return None
    return {
        **meta,
        "data": data,
        "ctype": ctype,
        "width": w,
        "height": h,
        "bytes": len(data),
        "content_hash": hashlib.sha256(data).hexdigest(),
        "category": categorize(url, meta.get("alt") or ""),
    }


def collect_project(slug: str) -> dict:
    # per-process hard timeout via alarm (Unix)
    def _timeout_handler(signum, frame):
        raise TimeoutError(f"project hard timeout {PROJECT_HARD_TIMEOUT}s")

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(PROJECT_HARD_TIMEOUT)
    try:
        return _collect_project_inner(slug)
    finally:
        signal.alarm(0)


def _collect_project_inner(slug: str) -> dict:
    md = PROJECTS_DOC / f"{slug}.md"
    sources = parse_dossier_sources(md)
    sources.sort(key=lambda s: -s["confidence"])
    sources = sources[:MAX_PAGES]

    out_dir = MEDIA_ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    candidates, page_errors = [], []
    for src in sources:
        time.sleep(SLEEP)
        body, ctype = fetch(src["url"])
        if body is None:
            page_errors.append(f"{src['url'][:80]}::{ctype}")
            continue
        if ctype and str(ctype).startswith("image/"):
            candidates.append({**src, "source_url": src["url"], "page_url": src["url"], "alt": ""})
            continue
        for iu, alt in extract_images(src["url"], body):
            candidates.append(
                {
                    "source_url": iu,
                    "page_url": src["url"],
                    "alt": alt,
                    "confidence": src["confidence"],
                    "publisher": src["publisher"],
                }
            )

    by_url = {}
    for c in candidates:
        by_url.setdefault(c["source_url"], c)
    ordered = sorted(
        by_url.items(),
        key=lambda kv: (-kv[1]["confidence"], 0 if "-scaled" not in kv[0] else 1, -len(kv[0])),
    )[:MAX_DOWNLOADS]

    downloaded = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(download_one, url, meta) for url, meta in ordered]
        try:
            for fut in as_completed(futs, timeout=PROJECT_HARD_TIMEOUT - 5):
                try:
                    item = fut.result(timeout=IMG_TIMEOUT + 2)
                except Exception:
                    item = None
                if item:
                    downloaded.append(item)
        except FutTimeout:
            pass

    best = {}
    for d in downloaded:
        prev = best.get(d["content_hash"])
        score = (d["confidence"], d["width"] * d["height"], d["bytes"])
        if prev is None or score > (prev["confidence"], prev["width"] * prev["height"], prev["bytes"]):
            best[d["content_hash"]] = d

    ranked = sorted(
        best.values(),
        key=lambda d: (d["confidence"], d["width"] * d["height"], d["bytes"]),
        reverse=True,
    )[:MAX_PER_PROJECT]

    rows, counters = [], {}
    for d in ranked:
        cat = d["category"]
        counters[cat] = counters.get(cat, 0) + 1
        cat_dir = out_dir / cat
        cat_dir.mkdir(parents=True, exist_ok=True)
        ext = ext_for(d["source_url"], d.get("ctype"), d["data"])
        fname = f"{counters[cat]:02d}-{d['content_hash'][:10]}{ext}"
        rel = f"{cat}/{fname}"
        (cat_dir / fname).write_bytes(d["data"])
        rows.append(
            {
                "filename": rel,
                "source_url": d["source_url"],
                "page_url": d["page_url"],
                "width": d["width"],
                "height": d["height"],
                "bytes": d["bytes"],
                "content_hash": d["content_hash"],
                "category": cat,
                "accessed_at": TODAY,
                "confidence": d["confidence"],
                "publisher": d.get("publisher") or "",
                "notes": "",
            }
        )

    fields = [
        "filename", "source_url", "page_url", "width", "height", "bytes",
        "content_hash", "category", "accessed_at", "confidence", "publisher", "notes",
    ]
    with (out_dir / "manifest.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    return {
        "slug": slug,
        "sources_tried": len(sources),
        "candidates": len(by_url),
        "downloaded_ok": len(downloaded),
        "unique_hashes": len(best),
        "kept": len(ranked),
        "page_errors": page_errors[:3],
        "gap": len(ranked) < 8,
    }


def run_one_subprocess(slug: str, q: mp.Queue):
    try:
        r = collect_project(slug)
        q.put(r)
    except Exception as e:
        q.put({"slug": slug, "kept": 0, "error": str(e)[:200], "gap": True})


def collect_with_kill(slug: str) -> dict:
    """Hard kill child after PROJECT_HARD_TIMEOUT+5s."""
    q: mp.Queue = mp.Queue()
    p = mp.Process(target=run_one_subprocess, args=(slug, q))
    p.start()
    p.join(PROJECT_HARD_TIMEOUT + 5)
    if p.is_alive():
        p.terminate()
        p.join(3)
        if p.is_alive():
            p.kill()
            p.join(2)
        # write empty/partial gap manifest if none
        out = MEDIA_ROOT / slug
        out.mkdir(parents=True, exist_ok=True)
        man = out / "manifest.csv"
        if not man.exists():
            with man.open("w", newline="", encoding="utf-8") as f:
                f.write(
                    "filename,source_url,page_url,width,height,bytes,content_hash,"
                    "category,accessed_at,confidence,publisher,notes\n"
                )
        return {"slug": slug, "kept": 0, "error": f"KILLED after {PROJECT_HARD_TIMEOUT}s", "gap": True}
    try:
        return q.get_nowait()
    except Exception:
        return {"slug": slug, "kept": 0, "error": "no-result", "gap": True}


def main():
    slugs = sorted(p.stem for p in PROJECTS_DOC.glob("*.md"))
    MEDIA_ROOT.mkdir(parents=True, exist_ok=True)
    results = []
    print(f"Rapid-fire collect {len(slugs)} projects (hard {PROJECT_HARD_TIMEOUT}s/project)…", flush=True)
    for i, slug in enumerate(slugs, 1):
        man = MEDIA_ROOT / slug / "manifest.csv"
        if man.exists() and man.stat().st_size > 80:
            n = max(0, sum(1 for _ in man.open()) - 1)
            if n > 0:
                print(f"[{i}/{len(slugs)}] {slug} SKIP ({n})", flush=True)
                results.append({"slug": slug, "kept": n, "gap": n < 8, "skipped": True})
                continue
        print(f"[{i}/{len(slugs)}] {slug} …", flush=True)
        t0 = time.time()
        r = collect_with_kill(slug)
        r["elapsed_s"] = round(time.time() - t0, 1)
        results.append(r)
        print(
            f"  -> kept={r.get('kept')} {r.get('elapsed_s')}s "
            f"err={r.get('error') or (r.get('page_errors') or '')}",
            flush=True,
        )

    summary = MEDIA_ROOT / "_collection-summary.csv"
    fields = ["slug", "kept", "candidates", "downloaded_ok", "gap", "error", "elapsed_s", "skipped"]
    with summary.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in results:
            w.writerow(r)
    total = sum(int(r.get("kept") or 0) for r in results)
    gaps = [r["slug"] for r in results if r.get("gap")]
    print(f"DONE total_images={total} projects={len(results)} gaps={gaps}", flush=True)


if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    main()
