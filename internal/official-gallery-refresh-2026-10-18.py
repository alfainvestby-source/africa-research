#!/usr/bin/env python3
"""Replace watermark-risk portal/agent photos with official/developer gallery pulls.

Does NOT strip watermarks. Prefer project_site / developer URLs from dossiers.
Marks Hauzisha CDN rows as watermark_risk in manifests.
"""
from __future__ import annotations

import csv
import hashlib
import io
import re
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup
from PIL import Image

STORE = Path("/cursor/stores/self")
PROJECTS = STORE / "docs" / "projects"
MEDIA = STORE / "media" / "projects"
SEED = STORE / "docs" / "db" / "seed"
TODAY = date.today().isoformat()
UA = "Mozilla/5.0 (compatible; CursorOfficialGallery/0.1)"

WATERMARK_HOST_SUBSTR = (
    "hauzisha",
    "new-hauzisha-pull",
    "b-cdn.net/developers",  # hauzisha CDN path pattern often
)

# Prefer these source host patterns when refreshing
OFFICIAL_SCORE_KEYS = ("official", "developer", "project_site", "microsite")

SKIP_SUBSTR = (
    "favicon", "sprite", "1x1", "pixel.gif", "tracking", "gravatar",
    "emoji", "wp-includes", "/icons/", "data:image", ".svg", "spinner",
    "placeholder", "loading.gif", "badge", "logo",
)
WP_SIZE_RE = re.compile(r"-\d{2,4}x\d{2,4}(?=\.(?:jpe?g|png|webp|gif)$)", re.I)

# Explicit official seed URLs (from dossiers + public search) for high-watermark projects
FORCE_OFFICIAL = {
    "rhapta-one": [
        "https://commercialpropertykenya.com/properties/rhapta-one-residency-apartment-in-westlands/",
        "https://oaklaneproperties.co.ke/properties/rhapta-one-residency-modern-1-2-bedroom-apartments-for-sale-in-westlands-nairobi/",
    ],
    "auris-residence": [
        "https://jafugroupkenya.com/",
        "https://commercialpropertykenya.com/properties/auris-residence-westlands-1-2-bedrooms/",
        "https://nairobirealestate.co.ke/properties/auris-residence-westlands-apartments",
        "https://gna.co.ke/project/auris-residence-westlands-studios-1-and-2-bedrooms/",
    ],
    "berkeley-homes": [
        "https://berkelyresidence.com/",
        "https://nefroonhomes.com/projects/berkeley-homes-2957aa6f",
        "https://commercialpropertykenya.com/properties/berkeley-homes-in-kileleshwa/",
        "https://oaklaneproperties.co.ke/properties/berkely-apartments-kilelewshwa/",
    ],
    "pandora-residences": [
        "https://pandora.co.ke/",
        "https://nairobirealestate.co.ke/properties/pandora-residence",
    ],
    "aya-luxury-residence": [
        "https://whitehorserealestate.ke/",
        "https://aad.ke/aad-real-estate-unveils-aya-luxury-residence-project-at-sankara-hotel/",
        "https://gna.co.ke/project/aya-residence-kileleshwa-apartments-duplexes-triplex-villas/",
    ],
    "only-you": ["https://onlyounairobi.com/"],
    "libra-residences": [
        "https://www.glbcgroup.co.ke/portfolio/libra-residences/",
        "https://www.glbcgroup.co.ke/projects/",
    ],
    "diplomat-residencies": ["https://diplomat.wonderpropertykenya.com/"],
    "gaia-brookside": [
        "https://www.wonderpropertykenya.com/projects/gaia",
        "https://www.wonderpropertykenya.com/",
    ],
    "237-lulu": [
        "https://mividahomes.com/developments/237-lulu/",
        "https://gardencityliving.co.ke/237-lulu/",
    ],
    "hephe-palace": ["https://www.hephepalace.ke/"],
    "montbleu": ["https://www.montbleu.co.ke/"],
    "highpoint-336": [
        "https://www.highpointresidencesltd.com/",
        "https://nairobirealestate.co.ke/properties/highpoint-336-residencies",
    ],
    "serene-manor": [
        "https://jafugroupkenya.com/",
        "https://nairobirealestate.co.ke/properties/serene-manor-apartments-kilimani",
    ],
    "citrine-heights": [
        "https://jafugroupkenya.com/",
        "https://commercialpropertykenya.com/properties/citrine-heights-westlands-nairobi/",
    ],
}


def is_watermark_host(url: str) -> bool:
    low = (url or "").lower()
    return any(h in low for h in WATERMARK_HOST_SUBSTR)


def parse_dossier_official(md_path: Path) -> list[str]:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    out, seen = [], set()
    for m in re.finditer(
        r"^\|\s*\d+\s*\|\s*(https?://[^|\s]+)\s*\|\s*([^|]*)\|\s*([^|]*)\|",
        text,
        re.M,
    ):
        url = m.group(1).strip().split()[0].rstrip(")")
        if not url.startswith("http") or url.lower().endswith(".pdf"):
            continue
        pub, st = m.group(2).strip(), m.group(3).strip()
        blob = f"{pub} {st}".lower()
        if any(k in blob for k in OFFICIAL_SCORE_KEYS) or "project" in st.lower():
            if "hauzisha" in blob or "hauzisha" in url.lower():
                continue
            if url not in seen:
                seen.add(url)
                out.append(url)
    return out


def fetch(url: str, timeout: int = 12) -> tuple[bytes | None, str | None]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read(8_000_000), resp.headers.get_content_type()
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


def extract_images(page_url: str, html: bytes) -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    found, seen = [], set()

    def add(u: str | None):
        if not u:
            return
        low = u.lower()
        if any(s in low for s in SKIP_SUBSTR):
            return
        if is_watermark_host(u):
            return
        path = low.split("?")[0]
        if not any(path.endswith(e) for e in (".jpg", ".jpeg", ".png", ".webp", ".gif")):
            if not re.search(r"/uploads/|/image|/img|/photo|/media|/wp-content/", low):
                return
        for cand in upgrade_wp(u):
            if cand not in seen:
                seen.add(cand)
                found.append(cand)

    for meta in soup.find_all("meta", property=re.compile(r"og:image", re.I)):
        add(absolutize(page_url, meta.get("content") or ""))
    for img in soup.find_all("img"):
        srcset = img.get("srcset") or img.get("data-srcset") or ""
        if srcset:
            add(pick_srcset(srcset, page_url))
        for attr in ("src", "data-src", "data-lazy-src", "data-original", "data-large_image"):
            if img.get(attr):
                add(absolutize(page_url, img.get(attr)))
    return found


def categorize(url: str) -> str:
    blob = url.lower()
    if any(k in blob for k in ("floorplan", "floor-plan", "site-plan", "layout")):
        return "plans"
    if any(k in blob for k in ("progress", "construction", "crane")):
        return "progress"
    if any(k in blob for k in ("pool", "gym", "lobby", "amenit", "garden", "rooftop")):
        return "amenities"
    if any(k in blob for k in ("interior", "living", "bedroom", "kitchen")):
        return "interior"
    if any(k in blob for k in ("exterior", "facade", "tower", "render", "elevation")):
        return "exterior"
    return "other"


def refresh_slug(slug: str) -> dict:
    md = PROJECTS / f"{slug}.md"
    urls = []
    if md.exists():
        urls.extend(parse_dossier_official(md))
    urls.extend(FORCE_OFFICIAL.get(slug, []))
    # dedupe preserve order
    seen_u, page_urls = set(), []
    for u in urls:
        if u not in seen_u and "hauzisha" not in u.lower():
            seen_u.add(u)
            page_urls.append(u)

    out_dir = MEDIA / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    clean_dir = out_dir / "official_clean"
    clean_dir.mkdir(exist_ok=True)

    # Mark existing hauzisha rows
    man_path = out_dir / "manifest.csv"
    existing = []
    if man_path.exists():
        with man_path.open(newline="", encoding="utf-8") as f:
            existing = list(csv.DictReader(f))
    wm_count = 0
    for r in existing:
        if is_watermark_host(r.get("source_url") or "") or is_watermark_host(r.get("page_url") or ""):
            r["notes"] = ((r.get("notes") or "") + " | watermark_risk=hauzisha").strip(" |")
            r["watermark_risk"] = "true"
            wm_count += 1
        else:
            r["watermark_risk"] = r.get("watermark_risk") or "false"

    candidates = []
    page_errors = []
    for page in page_urls[:6]:
        data, ctype = fetch(page)
        if not data or (ctype and "html" not in ctype and "text" not in ctype):
            page_errors.append(f"{page}::{ctype}")
            continue
        for img_url in extract_images(page, data)[:40]:
            candidates.append((img_url, page))
        time.sleep(0.2)

    # download clean
    kept_rows = []
    hashes = set()
    # keep existing non-watermark hashes
    for r in existing:
        if r.get("watermark_risk") == "true":
            continue
        h = r.get("content_hash") or ""
        if h:
            hashes.add(h)

    downloaded = 0
    for img_url, page in candidates:
        if downloaded >= 35:
            break
        if is_watermark_host(img_url):
            continue
        blob, err = fetch(img_url, timeout=10)
        if not blob or len(blob) < 8000:
            continue
        try:
            with Image.open(io.BytesIO(blob)) as im:
                w, h = im.size
                if min(w, h) < 400:
                    continue
                fmt = (im.format or "JPEG").upper()
        except Exception:
            continue
        digest = hashlib.sha256(blob).hexdigest()
        if digest in hashes:
            continue
        hashes.add(digest)
        cat = categorize(img_url)
        ext = ".jpg" if fmt in ("JPEG", "JPG") else (".png" if fmt == "PNG" else ".webp")
        # save under official_clean and also category for compatibility
        cat_dir = out_dir / cat
        cat_dir.mkdir(exist_ok=True)
        n = 1 + sum(1 for p in cat_dir.glob("*") if p.is_file())
        fname = f"{n:02d}-{digest[:10]}{ext}"
        rel = f"{cat}/{fname}"
        (cat_dir / fname).write_bytes(blob)
        try:
            (clean_dir / fname).write_bytes(blob)
        except OSError as e:
            print(f"  warn clean_dir write {fname}: {e}", flush=True)
        kept_rows.append(
            {
                "filename": rel,
                "source_url": img_url,
                "page_url": page,
                "width": w,
                "height": h,
                "bytes": len(blob),
                "content_hash": digest,
                "category": cat,
                "accessed_at": TODAY,
                "confidence": "4",
                "publisher": "official_refresh",
                "notes": "official_clean_refresh_2026-10-18",
                "watermark_risk": "false",
            }
        )
        downloaded += 1

    # rewrite manifest: non-wm existing + new clean (cap 40, prefer clean)
    non_wm = [r for r in existing if r.get("watermark_risk") != "true"]
    wm_rows = [r for r in existing if r.get("watermark_risk") == "true"]
    # put clean first
    merged = kept_rows + non_wm
    # dedupe by hash
    seen_h, final = set(), []
    for r in merged:
        h = r.get("content_hash") or ""
        if h and h in seen_h:
            continue
        if h:
            seen_h.add(h)
        final.append(r)
        if len(final) >= 40:
            break
    # append wm rows at end with risk flag but exclude from public preference (still keep for Admin evidence, capped)
    for r in wm_rows[:5]:
        h = r.get("content_hash") or ""
        if h and h in seen_h:
            continue
        if h:
            seen_h.add(h)
        final.append(r)

    fields = [
        "filename", "source_url", "page_url", "width", "height", "bytes",
        "content_hash", "category", "accessed_at", "confidence", "publisher",
        "notes", "watermark_risk",
    ]
    with man_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in final:
            w.writerow({k: r.get(k, "") for k in fields})

    return {
        "slug": slug,
        "official_pages": len(page_urls),
        "new_clean": len(kept_rows),
        "wm_flagged": wm_count,
        "manifest_rows": len(final),
        "page_errors": page_errors[:3],
    }


def reseed_media_csvs() -> tuple[int, int]:
    props = list(csv.DictReader((SEED / "properties.csv").open()))
    assets, links = [], []
    for prop in props:
        slug = prop["slug"]
        man = MEDIA / slug / "manifest.csv"
        if not man.exists():
            continue
        with man.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        # prefer non-watermark for hero
        rows_sorted = sorted(
            rows,
            key=lambda r: (
                0 if str(r.get("watermark_risk", "")).lower() in ("", "false", "0") else 1,
                0 if (r.get("publisher") or "") == "official_refresh" else 1,
                0 if (r.get("category") or "") == "exterior" else 1,
                r.get("filename") or "",
            ),
        )
        for i, r in enumerate(rows_sorted[:40]):
            fn = r.get("filename") or ""
            if not fn:
                continue
            aid = f"media-{slug}-{i+1:03d}"
            assets.append(
                {
                    "id": aid,
                    "local_path": str(MEDIA / slug / fn),
                    "source_url": r.get("source_url") or "",
                    "category": r.get("category") or "other",
                    "width_px": r.get("width") or "",
                    "height_px": r.get("height") or "",
                    "bytes": r.get("bytes") or "",
                    "content_hash": r.get("content_hash") or "",
                    "page_url": r.get("page_url") or "",
                    "confidence": r.get("confidence") or "3",
                    "accessed_at": r.get("accessed_at") or TODAY,
                    "notes": r.get("notes") or "",
                    "watermark_risk": r.get("watermark_risk") or "false",
                }
            )
            links.append(
                {
                    "id": f"pm-{slug}-{i+1:03d}",
                    "property_id": prop["id"],
                    "media_asset_id": aid,
                    "role": "hero" if i == 0 else "gallery",
                    "sort_order": str(i),
                    "category_override": "",
                    "watermark_risk": r.get("watermark_risk") or "false",
                }
            )

    def write(name, rows, fields):
        with (SEED / name).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)

    write(
        "media_assets.csv",
        assets,
        [
            "id", "local_path", "source_url", "category", "width_px", "height_px",
            "bytes", "content_hash", "page_url", "confidence", "accessed_at",
            "notes", "watermark_risk",
        ],
    )
    write(
        "property_media.csv",
        links,
        [
            "id", "property_id", "media_asset_id", "role", "sort_order",
            "category_override", "watermark_risk",
        ],
    )
    return len(assets), len({a["local_path"].split("/projects/")[1].split("/")[0] for a in assets if "/projects/" in a["local_path"]})


def main():
    # Always flag hauzisha across all manifests first
    flagged_projects = []
    for man in MEDIA.glob("*/manifest.csv"):
        slug = man.parent.name
        with man.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        changed = False
        for r in rows:
            if is_watermark_host(r.get("source_url") or "") or is_watermark_host(r.get("page_url") or ""):
                if str(r.get("watermark_risk", "")).lower() != "true":
                    r["watermark_risk"] = "true"
                    r["notes"] = ((r.get("notes") or "") + " | watermark_risk=hauzisha").strip(" |")
                    changed = True
            else:
                r.setdefault("watermark_risk", "false")
        if changed:
            fields = list(rows[0].keys())
            if "watermark_risk" not in fields:
                fields.append("watermark_risk")
            with man.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
                w.writeheader()
                w.writerows(rows)
            flagged_projects.append(slug)

    targets = sorted(set(FORCE_OFFICIAL) | set(flagged_projects))
    print(f"Refreshing {len(targets)} projects for official clean galleries…", flush=True)
    results = []
    for i, slug in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {slug} …", flush=True)
        r = refresh_slug(slug)
        results.append(r)
        print(
            f"  -> new_clean={r['new_clean']} wm_flagged={r['wm_flagged']} "
            f"pages={r['official_pages']} errs={r['page_errors']}",
            flush=True,
        )

    n_assets, n_props = reseed_media_csvs()
    print(f"Reseeded media_assets={n_assets} props={n_props}", flush=True)

    out = STORE / "internal" / "official-gallery-refresh-results-2026-10-18.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        fields = ["slug", "official_pages", "new_clean", "wm_flagged", "manifest_rows", "page_errors"]
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in results:
            w.writerow({**r, "page_errors": "|".join(r.get("page_errors") or [])})
    print("wrote", out)


if __name__ == "__main__":
    main()
