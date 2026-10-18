#!/usr/bin/env python3
"""Conservative duplicate / relist detection across seeded properties + lead lists.

No auto-merge. No invented facts. Soft signals only for unit-mix/price.
"""
from __future__ import annotations

import csv
import math
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path

STORE = Path("/cursor/stores/self")
SEED = STORE / "docs" / "db" / "seed"
INTERNAL = STORE / "internal"
DOCS_DB = STORE / "docs" / "db"

# Known anti-merge / sibling pairs (external_id or slug tokens) — false_positive unless stronger evidence
KNOWN_DISTINCT = [
    # (a_tokens, b_tokens, reason)
    ({"porini"}, {"jabali"}, "Same precinct family (Rendeavour/Tatu) — different products"),
    ({"luna", "oak"}, {"brookside", "oak"}, "Oak Group siblings — different plots"),
    ({"galaxy"}, {"ankori"}, "Both Rhapta corridor — different projects"),
    ({"sunpark"}, {"sunpark"}, "Phase I Ready vs II research — check phase label"),  # handled specially
    ({"marina", "bay"}, {"marina", "bay"}, "Phase 1 Ready vs Phase 2 — check phase"),
    ({"alina", "valley"}, {"alina", "harbour"}, "Wonder Alina family — different products"),
    ({"alina", "valley"}, {"alina", "ridge"}, "Wonder Alina family — different products"),
    ({"gaia"}, {"diplomat"}, "Wonder siblings — different streets"),
    ({"gaia"}, {"alina"}, "Wonder siblings — different streets"),
    ({"diplomat"}, {"alina"}, "Wonder siblings — different streets"),
    ({"golfscape"}, {"highpoint", "336"}, "Highpoint is Golfscape marketing partner ≠ Highpoint 336 project"),
    ({"capricorn"}, {"staroot", "residency"}, "Capricorn ≠ Staroot Residency"),
    ({"sensei"}, {"benford"}, "Sensei ≠ Benford Greenwood"),
    ({"sensei"}, {"greenwood"}, "Sensei ≠ Benford Greenwood"),
    ({"atreus"}, {"gaia"}, "Different Brookside streets/developers"),
    ({"atreus"}, {"brookside", "oak"}, "Different Brookside products"),
    ({"atreus"}, {"lesto"}, "Lesto Residences Ojijo ≠ Atreus"),
    ({"hephe"}, {"karura"}, "≠ Karura Forest Views Block alias"),
    ({"lulu", "237"}, {"amaiza"}, "≠ Amaiya Mi Vida"),
    ({"lulu", "237"}, {"amaiya"}, "≠ Amaiya Mi Vida"),
    ({"grand", "premier"}, {"rosewood"}, "Whitehorse siblings — different sites"),
    ({"only", "you"}, {"libra"}, "GLBC mkt on Only You ≠ Libra primary merge"),
    ({"montbleu"}, {"marina"}, "M-Group mkt on Montbleu ≠ Marina Bay 2 primary"),
]

STOP = {
    "the", "and", "of", "at", "in", "on", "a", "an", "for", "to", "by",
    "residences", "residence", "residential", "apartments", "apartment",
    "homes", "home", "estate", "project", "development", "phase", "ph",
    "towers", "tower", "suites", "suite", "limited", "ltd", "company", "co",
}


def norm_text(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9\s]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def tokens(s: str) -> set[str]:
    return {t for t in norm_text(s).split() if t and t not in STOP and len(t) > 1}


def fuzzy(a: str, b: str) -> float:
    a, b = norm_text(a), norm_text(b)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    # contain
    if a in b or b in a:
        return 0.92
    return SequenceMatcher(None, a, b).ratio()


def token_jaccard(a: str, b: str) -> float:
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def haversine_m(lat1, lng1, lat2, lng2) -> float:
    r = 6371000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dl = math.radians(lng2 - lng1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@dataclass
class Entity:
    kind: str  # property | hauzisha_lead | block_lead | nairobi_csv
    id: str
    name: str
    aliases: list[str] = field(default_factory=list)
    developer: str = ""
    developer_id: str = ""
    neighbourhood: str = ""
    street: str = ""
    city: str = ""
    area_text: str = ""
    lat: float | None = None
    lng: float | None = None
    beds_min: str = ""
    beds_max: str = ""
    beds_card: str = ""
    inventory_class: str = ""
    url: str = ""
    external_id: str = ""
    notes: str = ""
    price_min: str = ""
    price_max: str = ""


def load_properties() -> list[Entity]:
    props = read_csv(SEED / "properties.csv")
    places = {r["id"]: r for r in read_csv(SEED / "geo_places.csv")}
    devs = {r["id"]: r for r in read_csv(SEED / "developers.csv")}
    aliases = defaultdict(list)
    for r in read_csv(SEED / "property_aliases.csv"):
        aliases[r["property_id"]].append(r["alias"])
    pin_by = defaultdict(list)
    for r in read_csv(SEED / "geo_pins.csv"):
        pin_by[r["property_id"]].append(r)

    out = []
    for p in props:
        lat = lng = None
        if (p.get("lat") or "").strip() and (p.get("lng") or "").strip():
            try:
                lat, lng = float(p["lat"]), float(p["lng"])
            except ValueError:
                pass
        if lat is None:
            for pin in pin_by[p["id"]]:
                if str(pin.get("is_recommended")).lower() in ("true", "1"):
                    try:
                        lat, lng = float(pin["lat"]), float(pin["lng"])
                        break
                    except ValueError:
                        pass
        nb = places.get(p.get("geo_neighbourhood_id") or "", {}).get("name", "")
        city = places.get(p.get("geo_city_id") or "", {}).get("name", "")
        did = p.get("primary_developer_id") or ""
        dname = ""
        if did and did in devs:
            dname = devs[did].get("legal_name") or ""
        out.append(
            Entity(
                kind="property",
                id=p["id"],
                name=p["canonical_name"],
                aliases=aliases.get(p["id"], []),
                developer=dname,
                developer_id=did,
                neighbourhood=nb,
                street=p.get("street_label") or "",
                city=city,
                area_text=" ".join(x for x in [p.get("street_label") or "", nb, city] if x),
                lat=lat,
                lng=lng,
                beds_min=p.get("beds_min") or "",
                beds_max=p.get("beds_max") or "",
                inventory_class=p.get("inventory_class") or "",
                external_id=p.get("external_id") or "",
                notes=p.get("notes") or "",
                price_min=p.get("hero_price_min") or "",
                price_max=p.get("hero_price_max") or "",
            )
        )
    return out


def load_hauzisha_leads() -> list[Entity]:
    rows = read_csv(SEED / "listings_hauzisha_inventory_leads.csv")
    out = []
    for i, r in enumerate(rows):
        name = (r.get("development_name") or "").strip()
        if not name:
            continue
        out.append(
            Entity(
                kind="hauzisha_lead",
                id=f"hz-lead-{i+1:03d}",
                name=name,
                developer=r.get("developer_name") or "",
                area_text=r.get("area") or "",
                neighbourhood=r.get("area") or "",
                beds_card=r.get("beds_card") or "",
                inventory_class=r.get("inventory_class") or "",
                url=r.get("developer_hauzisha_url") or "",
                notes=(r.get("hauzisha_status_tag") or "") + " | " + (r.get("notes") or ""),
            )
        )
    return out


def load_block_leads() -> list[Entity]:
    rows = read_csv(INTERNAL / "block-ke-offplan-developments.csv")
    out = []
    for i, r in enumerate(rows):
        name = (r.get("Title") or "").strip()
        if not name:
            continue
        out.append(
            Entity(
                kind="block_lead",
                id=f"block-lead-{i+1:03d}",
                name=name,
                url=r.get("URL") or "",
                notes=f"completion={r.get('Completion') or ''}; listings={r.get('Listings') or ''}",
            )
        )
    return out


def load_nairobi_csv() -> list[Entity]:
    rows = read_csv(INTERNAL / "nairobi_off_plan_projects.csv")
    out = []
    for r in rows:
        lat = lng = None
        try:
            if r.get("lat"):
                lat = float(r["lat"])
            if r.get("lng"):
                lng = float(r["lng"])
        except ValueError:
            pass
        out.append(
            Entity(
                kind="nairobi_csv",
                id=f"csv-{r.get('external_id') or r.get('name')}",
                name=r.get("name") or "",
                external_id=r.get("external_id") or "",
                area_text=r.get("location") or "",
                neighbourhood=r.get("location") or "",
                lat=lat,
                lng=lng,
                notes=f"stage={r.get('stage')}; completion={r.get('completion')}; developer_csv={r.get('developer') or r.get('Developer') or ''}",
                price_min=r.get("price_from_kes") or "",
            )
        )
    return out


def best_name_score(a: Entity, b: Entity) -> tuple[float, str]:
    names_a = [a.name] + a.aliases
    names_b = [b.name] + b.aliases
    best, why = 0.0, ""
    for na in names_a:
        for nb in names_b:
            f = fuzzy(na, nb)
            j = token_jaccard(na, nb)
            score = max(f, j * 0.95 + 0.05 * f)
            # boost if distinctive token shared (non-stop)
            shared = tokens(na) & tokens(nb)
            if len(shared) >= 2:
                score = max(score, 0.85 + 0.05 * min(3, len(shared)))
            if score > best:
                best = score
                why = f"name '{na}' ~ '{nb}' ({score:.2f})"
    return best, why


def developer_score(a: Entity, b: Entity) -> tuple[float, str]:
    da, db = a.developer, b.developer
    if a.developer_id and b.developer_id and a.developer_id == b.developer_id:
        return 1.0, f"same developer_id {a.developer_id}"
    if not da or not db:
        return 0.0, ""
    f = fuzzy(da, db)
    if f >= 0.85:
        return f, f"developer '{da}' ~ '{db}' ({f:.2f})"
    # token overlap on developer
    j = token_jaccard(da, db)
    if j >= 0.5:
        return j, f"developer tokens overlap ({j:.2f})"
    return 0.0, ""


def place_score(a: Entity, b: Entity) -> tuple[float, str]:
    reasons = []
    score = 0.0
    # neighbourhood
    for na, nb in (
        (a.neighbourhood, b.neighbourhood),
        (a.neighbourhood, b.area_text),
        (a.area_text, b.neighbourhood),
        (a.area_text, b.area_text),
    ):
        if na and nb and fuzzy(na, nb) >= 0.8:
            score = max(score, 0.55)
            reasons.append(f"area/nbhd '{na}'~'{nb}'")
            break
    # street
    if a.street and b.street and fuzzy(a.street, b.street) >= 0.75:
        score = max(score, 0.75)
        reasons.append(f"street '{a.street[:40]}'~'{b.street[:40]}'")
    elif a.street and b.area_text and any(t in norm_text(b.area_text) for t in tokens(a.street) if len(t) > 4):
        score = max(score, 0.45)
        reasons.append("street token in lead area")
    # geo
    if a.lat is not None and b.lat is not None and a.lng is not None and b.lng is not None:
        d = haversine_m(a.lat, a.lng, b.lat, b.lng)
        if d <= 150:
            score = max(score, 0.9)
            reasons.append(f"geo {d:.0f}m")
        elif d <= 400:
            score = max(score, 0.7)
            reasons.append(f"geo {d:.0f}m")
        elif d <= 1200:
            score = max(score, 0.4)
            reasons.append(f"geo {d:.0f}m (soft)")
        elif d > 5000:
            # far apart — penalty applied by caller
            reasons.append(f"geo FAR {d/1000:.1f}km")
            return -0.5, "; ".join(reasons)
    return score, "; ".join(reasons)


def soft_fingerprint(a: Entity, b: Entity) -> tuple[float, str]:
    """Beds/price soft only — never decisive alone."""
    reasons = []
    score = 0.0
    # beds card vs beds range
    if a.beds_card and (b.beds_min or b.beds_max):
        card = a.beds_card.lower()
        ok = True
        if b.beds_min and b.beds_min != "0" and f"{b.beds_min}br" not in card.replace(" ", "") and b.beds_min not in card:
            # allow studio
            if not (b.beds_min == "0" and "studio" in card):
                ok = False
        if ok and b.beds_max and f"{b.beds_max}" in card:
            score = 0.25
            reasons.append("beds_card overlaps seeded beds")
    if a.beds_min and b.beds_min and a.beds_min == b.beds_min and a.beds_max and b.beds_max and a.beds_max == b.beds_max:
        score = max(score, 0.3)
        reasons.append(f"beds range {a.beds_min}-{a.beds_max}")
    return score, "; ".join(reasons)


def phase_labels(name: str) -> set[str]:
    n = norm_text(name)
    labs = set()
    if re.search(r"\b(ii|2|phase 2|ph ?2|phase ii)\b", n):
        labs.add("phase2")
    if re.search(r"\b(i|1|phase 1|ph ?1|phase i)\b", n) and "ii" not in n and "phase 2" not in n:
        labs.add("phase1")
    return labs


def known_distinct(a: Entity, b: Entity) -> str | None:
    na = norm_text(a.name + " " + " ".join(a.aliases))
    nb = norm_text(b.name + " " + " ".join(b.aliases))
    ta, tb = tokens(a.name), tokens(b.name)
    # special phase siblings with same stem
    stem_a = re.sub(r"\b(phase|ph|ii|i|2|1)\b", "", na).strip()
    stem_b = re.sub(r"\b(phase|ph|ii|i|2|1)\b", "", nb).strip()
    if fuzzy(stem_a, stem_b) >= 0.9:
        pa, pb = phase_labels(a.name), phase_labels(b.name)
        if pa and pb and pa != pb:
            return "Same brand stem different phase labels"
    for tok_a, tok_b, reason in KNOWN_DISTINCT:
        if tok_a <= ta and tok_b <= tb:
            return reason
        if tok_b <= ta and tok_a <= tb:
            return reason
        # also check substrings for multiword
        if all(t in na for t in tok_a) and all(t in nb for t in tok_b):
            return reason
        if all(t in nb for t in tok_a) and all(t in na for t in tok_b):
            return reason
    return None


def classify(score: float, name_s: float, reasons: list[str], distinct: str | None, a: Entity, b: Entity) -> tuple[str, str]:
    """Return recommended_action, confidence_label."""
    if distinct:
        # phase case
        if "phase" in distinct.lower():
            return "related_phase", "medium"
        return "false_positive", "high"

    # both properties in seed with high name — likely already distinct researched entities
    if a.kind == "property" and b.kind == "property":
        if name_s >= 0.95 and score >= 0.75:
            return "needs_human", "high"  # two seeded rows almost same name — critical
        if name_s >= 0.8 and score >= 0.65:
            return "needs_human", "medium"
        if "Wonder" in (a.developer + b.developer) or "Elegant" in (a.developer + b.developer) or "Whitehorse" in (a.developer + b.developer):
            if name_s < 0.85:
                return "false_positive", "medium"
        if score < 0.7:
            return "false_positive", "medium"
        return "needs_human", "low"

    # lead ↔ property
    if name_s >= 0.93 and score >= 0.8:
        return "same_property", "high"
    if name_s >= 0.88 and score >= 0.7:
        return "same_property", "medium"
    if name_s >= 0.8 and score >= 0.6:
        return "needs_human", "medium"
    if "phase" in norm_text(a.name) or "phase" in norm_text(b.name):
        if name_s >= 0.75:
            return "related_phase", "medium"
    if score >= 0.55 and name_s >= 0.7:
        return "needs_human", "low"
    return "false_positive", "low"


def score_pair(a: Entity, b: Entity) -> dict | None:
    if a.id == b.id:
        return None
    # skip comparing two different lead kinds with weak names early
    name_s, name_why = best_name_score(a, b)
    if name_s < 0.55 and not (a.lat and b.lat):
        return None

    reasons = [name_why] if name_why else []
    total = name_s * 0.55

    d_s, d_why = developer_score(a, b)
    if d_s:
        total += d_s * 0.2
        reasons.append(d_why)

    p_s, p_why = place_score(a, b)
    if p_s < 0:
        total += p_s * 0.3  # far geo penalty
        reasons.append(p_why)
    elif p_s:
        total += p_s * 0.2
        reasons.append(p_why)

    f_s, f_why = soft_fingerprint(a, b)
    if f_s:
        total += f_s * 0.05
        reasons.append(f_why)

    # URL / external id
    if a.external_id and b.external_id and a.external_id == b.external_id:
        total += 0.35
        reasons.append(f"same external_id {a.external_id}")
    if a.url and b.url and norm_text(a.url) == norm_text(b.url):
        total += 0.2
        reasons.append("same url")

    # Cap
    total = max(0.0, min(1.0, total))

    distinct = known_distinct(a, b)
    if distinct and name_s < 0.95:
        action, conf = "false_positive", "high"
        reasons.append(f"ANTI-MERGE: {distinct}")
        # still emit if someone might confuse them (shared developer/area)
        if d_s < 0.5 and p_s <= 0 and name_s < 0.7:
            return None
    else:
        action, conf = classify(total, name_s, reasons, distinct, a, b)
        if distinct and "phase" in distinct.lower():
            action, conf = "related_phase", "medium"
            reasons.append(f"PHASE: {distinct}")

    # drop noise
    if action == "false_positive" and conf == "low" and total < 0.65:
        return None
    if total < 0.58 and action == "false_positive":
        return None
    if name_s < 0.62 and action != "false_positive" and "geo" not in " ".join(reasons):
        return None

    return {
        "left_kind": a.kind,
        "left_id": a.id,
        "left_name": a.name,
        "left_external_id": a.external_id,
        "left_developer": a.developer,
        "right_kind": b.kind,
        "right_id": b.id,
        "right_name": b.name,
        "right_external_id": b.external_id,
        "right_developer": b.developer,
        "score": round(total, 3),
        "name_score": round(name_s, 3),
        "match_reasons": " | ".join(r for r in reasons if r),
        "recommended_action": action,
        "confidence": conf,
        "cluster_key": "",
    }


def cluster_pairs(pairs: list[dict]) -> list[dict]:
    """Union-find on same_property / needs_human high among property+lead."""
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for p in pairs:
        if p["recommended_action"] in ("same_property", "needs_human", "related_phase") and p["confidence"] in ("high", "medium"):
            union(f"{p['left_kind']}:{p['left_id']}", f"{p['right_kind']}:{p['right_id']}")

    for p in pairs:
        la = find(f"{p['left_kind']}:{p['left_id']}")
        lb = find(f"{p['right_kind']}:{p['right_id']}")
        # only assign cluster if connected
        if la == lb and p["recommended_action"] != "false_positive":
            p["cluster_key"] = la
        else:
            p["cluster_key"] = ""
    return pairs


def main():
    props = load_properties()
    hz = load_hauzisha_leads()
    block = load_block_leads()
    nbo = load_nairobi_csv()

    print(f"loaded properties={len(props)} hauzisha={len(hz)} block={len(block)} nairobi_csv={len(nbo)}")

    pairs: list[dict] = []

    # 1) property ↔ property
    for i in range(len(props)):
        for j in range(i + 1, len(props)):
            r = score_pair(props[i], props[j])
            if r:
                pairs.append(r)

    # 2) property ↔ hauzisha
    for p in props:
        for h in hz:
            r = score_pair(p, h)
            if r:
                pairs.append(r)

    # 3) property ↔ block (low trust — needs_human max unless very strong name)
    for p in props:
        for b in block:
            r = score_pair(p, b)
            if not r:
                continue
            if r["recommended_action"] == "same_property":
                r["recommended_action"] = "needs_human"
                r["match_reasons"] += " | Block.ke low-trust — do not auto-link"
                r["confidence"] = "medium" if r["confidence"] == "high" else r["confidence"]
            pairs.append(r)

    # 4) property ↔ nairobi CSV (should mostly match by external_id)
    for p in props:
        for c in nbo:
            r = score_pair(p, c)
            if r:
                pairs.append(r)

    # 5) hauzisha ↔ hauzisha (duplicate leads / relists within portal export)
    for i in range(len(hz)):
        for j in range(i + 1, len(hz)):
            r = score_pair(hz[i], hz[j])
            if r and r["name_score"] >= 0.8:
                if r["recommended_action"] == "same_property":
                    r["recommended_action"] = "needs_human"
                    r["match_reasons"] += " | possible portal relist / duplicate lead row"
                pairs.append(r)

    pairs.sort(key=lambda x: (-x["score"], x["recommended_action"]))
    pairs = cluster_pairs(pairs)

    # write CSV
    csv_path = SEED / "duplicate_candidates.csv"
    fields = [
        "left_kind", "left_id", "left_external_id", "left_name", "left_developer",
        "right_kind", "right_id", "right_external_id", "right_name", "right_developer",
        "score", "name_score", "match_reasons", "recommended_action", "confidence", "cluster_key",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(pairs)
    print(f"wrote {csv_path} rows={len(pairs)}")

    # counts
    from collections import Counter
    actions = Counter(p["recommended_action"] for p in pairs)
    kinds = Counter(f"{p['left_kind']}↔{p['right_kind']}" for p in pairs)
    clusters = {p["cluster_key"] for p in pairs if p["cluster_key"]}
    print("actions", dict(actions))
    print("kinds", dict(kinds))
    print("clusters", len(clusters))

    # write markdown summary path used by caller
    summary_path = INTERNAL / "_dup_detect_summary.json"
    import json
    summary_path.write_text(json.dumps({
        "n_pairs": len(pairs),
        "actions": dict(actions),
        "kinds": dict(kinds),
        "n_clusters": len(clusters),
        "top": pairs[:40],
    }, indent=2))
    print("summary", summary_path)


if __name__ == "__main__":
    main()
