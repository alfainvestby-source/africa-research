#!/usr/bin/env python3
"""Derive + harvest high-confidence property card facets (no invented facts).

Adds/backfills on properties.csv:
  property_type, beds_min, beds_max, size_sqm_min, size_sqm_max,
  hero_price_qualifier, hero_price_min, hero_price_max, hero_price_currency,
  deposit_pct, deposit_meets_must_have, summary, map_tier, street_label

Also writes:
  property_utility_chips.csv
  media_assets.csv + property_media.csv (from existing manifests)
  appends geo_pins for area-only props via Nominatim (geocode conf 2–3)
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date
from pathlib import Path

STORE = Path("/cursor/stores/self")
SEED = STORE / "docs" / "db" / "seed"
PROJECTS = STORE / "docs" / "projects"
MEDIA = STORE / "media" / "projects"
TODAY = date.today().isoformat()
UA = "KenyaOffPlanResearch/0.1 (cursor-agent; geo-enrichment; contact: research)"

UTILITY_FEATURES = {
    "backup_generator",
    "borehole",
    "rooftop_solar",
    "solar_water_heating",
    "wifi",
    "internet_cable",
    "fibre",
    "parking",
    "gated_security",
    "cctv",
    "electric_fence",
}


def read_csv(name: str) -> list[dict]:
    path = SEED / name
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(name: str, rows: list[dict], fieldnames: list[str]) -> None:
    path = SEED / name
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})


def parse_street(md: str) -> str:
    for pat in (
        r"\|\s*`geography\.street`\s*\|[^|]*\|\s*\*?\*?([^*|\n]+?)\*?\*?\s*\|",
        r"\|\s*`geography\.neighbourhood_street`\s*\|[^|]*\|\s*\*?\*?([^*|\n]+?)\*?\*?\s*\|",
    ):
        m = re.search(pat, md)
        if m:
            raw = m.group(1).strip()
            raw = re.sub(r"\*+", "", raw)
            raw = re.sub(r"\s+", " ", raw)
            # take primary street phrase before parenthetical soft notes when long
            if " — " in raw:
                raw = raw.split(" — ")[0].strip()
            return raw[:160]
    return ""


def parse_summary_bits(md: str, name: str) -> str:
    """One factual line from dossier intro — never invent marketing."""
    # first non-empty paragraph after H1
    lines = md.splitlines()
    past_title = False
    chunk = []
    for line in lines:
        if line.startswith("# "):
            past_title = True
            continue
        if not past_title:
            continue
        if line.startswith("---") or line.startswith("##"):
            if chunk:
                break
            continue
        if line.startswith("**Not in seed") or line.startswith("**Seeded"):
            continue
        if line.startswith("**Method") or line.startswith("Live research"):
            continue
        if line.startswith("|") or line.startswith("- [") or line.startswith("```"):
            if chunk:
                break
            continue
        if line.strip():
            chunk.append(line.strip())
            if len(" ".join(chunk)) > 80:
                break
    text = " ".join(chunk)
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > 220:
        text = text[:217].rsplit(" ", 1)[0] + "…"
    return text


def infer_property_type(unit_rows: list[dict], notes: str) -> str:
    blob = " ".join(
        (u.get("label") or "") + " " + (u.get("notes") or "") for u in unit_rows
    ).lower()
    blob += " " + (notes or "").lower()
    hits = []
    if any(k in blob for k in ("villa",)):
        hits.append("villa")
    if any(k in blob for k in ("townhouse", "town house")):
        hits.append("townhouse")
    if any(k in blob for k in ("maisonette",)):
        hits.append("maisonette")
    if any(k in blob for k in ("penthouse",)):
        hits.append("penthouse")
    if any(k in blob for k in ("studio", "bedroom", "br ", " br", "apartment", "residences", "tower")):
        hits.append("apartment")
    hits = list(dict.fromkeys(hits))
    if not hits:
        return "apartment"  # Kenya UC corpus default when typologies are residential flats
    if len(hits) == 1:
        return hits[0]
    if set(hits) <= {"apartment", "penthouse", "studio"} or (
        "apartment" in hits and "penthouse" in hits and len(hits) <= 2
    ):
        return "apartment"
    return "mixed"


def hero_from_prices(rows: list[dict]) -> tuple[str, str, str, str]:
    """Return qualifier, min, max, currency."""
    if not rows:
        return "POA", "", "", "KES"
    ndi = any(str(r.get("needs_developer_input", "")).lower() in ("true", "1", "yes") for r in rows)
    currency = "KES"
    amounts = []
    for r in rows:
        cur = (r.get("currency") or "KES").strip() or "KES"
        a = (r.get("amount") or "").strip().replace(",", "")
        if not a:
            continue
        try:
            amounts.append((float(a), cur))
        except ValueError:
            continue
    if amounts:
        # prefer majority currency
        from collections import Counter
        currency = Counter(c for _, c in amounts).most_common(1)[0][0]
        amts = [a for a, c in amounts if c == currency]
    else:
        amts = []
    if ndi:
        return "POA", "", "", currency
    if len(amts) >= 2 and min(amts) != max(amts):
        return "range", str(int(min(amts))), str(int(max(amts))), currency
    if len(amts) == 1 or (len(amts) >= 2 and min(amts) == max(amts)):
        return "from", str(int(amts[0])), str(int(amts[0])), currency
    return "POA", "", "", currency


def beds_sizes(unit_rows: list[dict]):
    beds, sizes = [], []
    for u in unit_rows:
        b = (u.get("bedrooms") or "").strip()
        if b != "":
            try:
                beds.append(int(float(b)))
            except ValueError:
                pass
        s = (u.get("size_sqm") or "").strip()
        if s:
            try:
                sizes.append(float(s))
            except ValueError:
                pass
    bmin = str(min(beds)) if beds else ""
    bmax = str(max(beds)) if beds else ""
    smin = str(int(min(sizes))) if sizes else ""
    smax = str(int(max(sizes))) if sizes else ""
    return bmin, bmax, smin, smax


def deposit_for(rows: list[dict]) -> tuple[str, str]:
    """Only when deposit_pct meets_must_have."""
    cands = [
        r
        for r in rows
        if r.get("element") == "deposit_pct"
        and str(r.get("meets_must_have", "")).lower() in ("true", "1", "yes")
    ]
    if not cands:
        return "", "false"
    # prefer canonical / highest confidence
    def score(r):
        can = 1 if str(r.get("is_canonical", "")).lower() in ("true", "1") else 0
        try:
            conf = int(r.get("confidence") or 0)
        except ValueError:
            conf = 0
        return (can, conf)

    best = sorted(cands, key=score, reverse=True)[0]
    val = (best.get("value_numeric") or "").strip()
    if not val:
        m = re.search(r"(\d+(?:\.\d+)?)\s*%", best.get("value_text") or "")
        val = m.group(1) if m else ""
    return val, "true"


def map_tier(prop: dict, pin_rows: list[dict]) -> str:
    lat = (prop.get("lat") or "").strip()
    lng = (prop.get("lng") or "").strip()
    if lat and lng:
        return "exact"
    if pin_rows:
        max_conf = 0
        for p in pin_rows:
            try:
                max_conf = max(max_conf, int(float(p.get("confidence") or 0)))
            except ValueError:
                pass
        if max_conf >= 4:
            return "exact"
        return "approximate"
    if (prop.get("geo_neighbourhood_id") or "").strip():
        return "area"
    return "unknown"


def nominatim(query: str) -> tuple[float, float, str] | None:
    params = urllib.parse.urlencode({"q": query, "format": "json", "limit": 1})
    url = f"https://nominatim.openstreetmap.org/search?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print("geocode fail", query, e)
        return None
    if not data:
        return None
    hit = data[0]
    return float(hit["lat"]), float(hit["lon"]), hit.get("display_name", "")


def build_geocode_query(street: str, nb_name: str, city_name: str, country: str = "Kenya") -> str:
    parts = []
    if street:
        # simplify: first street-like token before / or (
        s = street.split("(")[0].split(";")[0].strip()
        s = re.split(r"\s*/\s*", s)[0].strip()
        # drop leading soft words
        s = re.sub(r"^(End of|Junction of|Access via)\s+", "", s, flags=re.I)
        parts.append(s)
    if nb_name:
        parts.append(nb_name)
    if city_name:
        parts.append(city_name)
    parts.append(country)
    return ", ".join(p for p in parts if p)


def seed_media_from_manifests(props: list[dict]) -> tuple[list[dict], list[dict]]:
    assets, links = [], []
    for prop in props:
        slug = prop["slug"]
        manifest = MEDIA / slug / "manifest.csv"
        if not manifest.exists():
            continue
        with manifest.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        # pick hero: first exterior else first row
        sorted_rows = sorted(
            rows,
            key=lambda r: (
                0 if (r.get("category") or "") == "exterior" else 1,
                int(r.get("sort_order") or r.get("index") or 9999) if str(r.get("sort_order") or r.get("index") or "").isdigit() else 9999,
            ),
        )
        for i, r in enumerate(sorted_rows[:40]):
            local = r.get("local_path") or r.get("path") or r.get("filename") or ""
            if local and not local.startswith("/"):
                # relative to project folder
                local_full = str(MEDIA / slug / local)
            elif local:
                local_full = local
            else:
                # try category/filename pattern
                cat = r.get("category") or "other"
                fn = r.get("filename") or r.get("file") or ""
                if not fn:
                    continue
                local_full = str(MEDIA / slug / cat / fn)
            aid = f"media-{slug}-{i+1:03d}"
            ch = r.get("content_hash") or r.get("sha256") or ""
            assets.append(
                {
                    "id": aid,
                    "local_path": local_full,
                    "source_url": r.get("source_url") or r.get("url") or "",
                    "category": r.get("category") or "other",
                    "width_px": r.get("width_px") or r.get("width") or "",
                    "height_px": r.get("height_px") or r.get("height") or "",
                    "bytes": r.get("bytes") or "",
                    "content_hash": ch,
                    "page_url": r.get("page_url") or "",
                    "confidence": r.get("confidence") or "3",
                    "accessed_at": r.get("accessed_at") or TODAY,
                    "notes": f"seeded from manifest {slug}",
                }
            )
            role = "hero" if i == 0 else "gallery"
            links.append(
                {
                    "id": f"pm-{slug}-{i+1:03d}",
                    "property_id": prop["id"],
                    "media_asset_id": aid,
                    "role": role,
                    "sort_order": str(i),
                    "category_override": "",
                }
            )
    return assets, links


def main() -> None:
    props = read_csv("properties.csv")
    places = {r["id"]: r for r in read_csv("geo_places.csv")}
    developers = {r["id"]: r for r in read_csv("developers.csv")}
    ut_by = defaultdict(list)
    for r in read_csv("unit_types.csv"):
        ut_by[r["property_id"]].append(r)
    pr_by = defaultdict(list)
    for r in read_csv("price_observations.csv"):
        pr_by[r["property_id"]].append(r)
    pay_by = defaultdict(list)
    for r in read_csv("payment_plan_claims.csv"):
        pay_by[r["property_id"]].append(r)
    pin_by = defaultdict(list)
    for r in read_csv("geo_pins.csv"):
        pin_by[r["property_id"]].append(r)
    feat_by = defaultdict(list)
    for r in read_csv("property_features.csv"):
        feat_by[r["property_id"]].append(r)

    # --- derive card fields ---
    new_props = []
    for p in props:
        pid = p["id"]
        units = ut_by[pid]
        prices = pr_by[pid]
        pays = pay_by[pid]
        pins = pin_by[pid]
        dossier = PROJECTS / f"{p['slug']}.md"
        md = dossier.read_text(encoding="utf-8", errors="replace") if dossier.exists() else ""

        street = parse_street(md)
        summary = parse_summary_bits(md, p["canonical_name"])
        if not summary:
            nb = places.get(p.get("geo_neighbourhood_id") or "", {}).get("name") or ""
            city = places.get(p.get("geo_city_id") or "", {}).get("name") or ""
            ic = p.get("inventory_class") or ""
            summary = f"{p['canonical_name']} — {nb}, {city} ({ic}).".strip(" —.")

        bmin, bmax, smin, smax = beds_sizes(units)
        qual, pmin, pmax, cur = hero_from_prices(prices)
        dep, dep_mh = deposit_for(pays)
        ptype = infer_property_type(units, p.get("notes") or "")
        tier = map_tier(p, pins)

        out = dict(p)
        out.update(
            {
                "property_type": ptype,
                "beds_min": bmin,
                "beds_max": bmax,
                "size_sqm_min": smin,
                "size_sqm_max": smax,
                "hero_price_qualifier": qual,
                "hero_price_min": pmin,
                "hero_price_max": pmax,
                "hero_price_currency": cur or p.get("currency_default") or "KES",
                "deposit_pct": dep,
                "deposit_meets_must_have": dep_mh,
                "summary": summary,
                "map_tier": tier,
                "street_label": street,
            }
        )
        new_props.append(out)

    prop_fields = [
        "id",
        "external_id",
        "slug",
        "canonical_name",
        "status_label",
        "inventory_class",
        "property_type",
        "beds_min",
        "beds_max",
        "size_sqm_min",
        "size_sqm_max",
        "hero_price_qualifier",
        "hero_price_min",
        "hero_price_max",
        "hero_price_currency",
        "deposit_pct",
        "deposit_meets_must_have",
        "summary",
        "map_tier",
        "street_label",
        "primary_developer_id",
        "geo_city_id",
        "geo_neighbourhood_id",
        "geo_master_community_id",
        "lat",
        "lng",
        "currency_default",
        "research_cycle",
        "last_verified_at",
        "notes",
    ]
    write_csv("properties.csv", new_props, prop_fields)
    print("properties.csv updated", len(new_props))

    # --- utility chips ---
    chip_rows = []
    for p in new_props:
        for fr in feat_by[p["id"]]:
            fid = (fr.get("feature_id") or "").strip()
            if fid in UTILITY_FEATURES or fid.startswith("solar") or fid in {
                "backup_generator",
                "borehole",
                "parking",
                "gated_security",
                "cctv",
            }:
                chip_rows.append(
                    {
                        "id": f"chip-{p['slug']}-{fid}",
                        "property_id": p["id"],
                        "external_id": p["external_id"],
                        "feature_id": fid,
                        "label": fr.get("raw_text") or fid,
                        "confidence": fr.get("confidence") or "",
                        "is_canonical": fr.get("is_canonical") or "",
                        "publisher_class": fr.get("publisher_class") or "",
                    }
                )
    # dedupe id
    seen = set()
    uniq = []
    for r in chip_rows:
        if r["id"] in seen:
            continue
        seen.add(r["id"])
        uniq.append(r)
    write_csv(
        "property_utility_chips.csv",
        uniq,
        [
            "id",
            "property_id",
            "external_id",
            "feature_id",
            "label",
            "confidence",
            "is_canonical",
            "publisher_class",
        ],
    )
    print("utility chips", len(uniq), "props", len({r['property_id'] for r in uniq}))

    # --- media seed from existing manifests ---
    assets, links = seed_media_from_manifests(new_props)
    write_csv(
        "media_assets.csv",
        assets,
        [
            "id",
            "local_path",
            "source_url",
            "category",
            "width_px",
            "height_px",
            "bytes",
            "content_hash",
            "page_url",
            "confidence",
            "accessed_at",
            "notes",
        ],
    )
    write_csv(
        "property_media.csv",
        links,
        ["id", "property_id", "media_asset_id", "role", "sort_order", "category_override"],
    )
    print("media assets", len(assets), "links", len(links), "props", len({l['property_id'] for l in links}))

    # --- geocode missing ---
    existing_pins = read_csv("geo_pins.csv")
    have_pin = {r["property_id"] for r in existing_pins}
    new_pins = []
    for p in new_props:
        has_ll = bool((p.get("lat") or "").strip() and (p.get("lng") or "").strip())
        if has_ll or p["id"] in have_pin:
            continue
        nb = places.get(p.get("geo_neighbourhood_id") or "", {}).get("name") or ""
        city = places.get(p.get("geo_city_id") or "", {}).get("name") or ""
        street = p.get("street_label") or ""
        query = build_geocode_query(street, nb, city)
        print("geocode", p["external_id"], "→", query)
        time.sleep(1.1)  # Nominatim policy
        hit = nominatim(query)
        if not hit and street:
            # fallback neighbourhood+city only
            time.sleep(1.1)
            query2 = build_geocode_query("", nb, city)
            print("  fallback", query2)
            hit = nominatim(query2)
            query = query2
        if not hit:
            print("  MISS", p["external_id"])
            continue
        lat, lng, display = hit
        conf = 3 if street else 2
        pin_id = f"pin-{p['slug']}-geocode"
        new_pins.append(
            {
                "id": pin_id,
                "property_id": p["id"],
                "external_id": p["external_id"],
                "lat": f"{lat:.6f}",
                "lng": f"{lng:.6f}",
                "geo_method": "geocode",
                "confidence": str(conf),
                "is_recommended": "true",
                "needs_verification": "true",
                "source_url": "https://nominatim.openstreetmap.org/search",
                "source_query": query,
                "provider": "nominatim",
                "accessed_at": TODAY,
                "notes": f"Approximate; display={display[:120]}",
            }
        )
        # bump map_tier on property
        p["map_tier"] = "approximate"

    if new_pins:
        pin_fields = list(existing_pins[0].keys()) if existing_pins else list(new_pins[0].keys())
        write_csv("geo_pins.csv", existing_pins + new_pins, pin_fields)
        write_csv("properties.csv", new_props, prop_fields)
        print("new geo_pins", len(new_pins))
    else:
        print("no new geo_pins")

    # coverage snapshot
    n = len(new_props)
    def pct(pred):
        return sum(1 for p in new_props if pred(p))

    print("--- coverage ---")
    print("property_type", pct(lambda p: p.get("property_type")), "/", n)
    print("beds range", pct(lambda p: p.get("beds_min") != ""), "/", n)
    print("size range", pct(lambda p: p.get("size_sqm_min") != ""), "/", n)
    print("hero qualifier", pct(lambda p: p.get("hero_price_qualifier") != ""), "/", n)
    print("deposit must-have", pct(lambda p: p.get("deposit_meets_must_have") == "true"), "/", n)
    print("summary", pct(lambda p: bool(p.get("summary"))), "/", n)
    print("street", pct(lambda p: bool(p.get("street_label"))), "/", n)
    print("map exact", pct(lambda p: p.get("map_tier") == "exact"), "approx", pct(lambda p: p.get("map_tier") == "approximate"), "area", pct(lambda p: p.get("map_tier") == "area"))


if __name__ == "__main__":
    main()
