#!/usr/bin/env python3
"""Extract the FMC650/FMX6 parameter-id schema from the vendor Configurator XML.

Honest scope: this script collects what the vendor XML states *statically* and
what its documented generator nodes imply arithmetically. It does NOT reimplement
the Configurator's runtime property generation, so a large part of the cfg id
universe remains unattributed; the report says exactly how much.

Evidence for the generator formula (CIL of
Configuration.Generator.Utilities.PropertyIdCalulator.CalculatePropertyId):
    id = startId + offsetMultiplier * blockIndex + orderId

Usage: build_schema.py <brand_xml_dir> <parsed_cfg.json> <out_prefix>
"""
import glob
import json
import os
import sys
import xml.etree.ElementTree as ET

TYPE_TAGS = {
    "NumberInput": "Int32", "TextBox": "String", "Collection": "Byte",
    "DropDownList": "Byte", "List": "String", "Geozones": "group", "Polygon": "group",
}


def norm(v):
    return v.strip() if isinstance(v, str) else v


def load(path):
    with open(path, "rb") as fh:
        return ET.fromstring(fh.read().decode("utf-8-sig"))


def describe(el):
    rec = {
        "element": el.tag,
        "type": norm(el.get("ParameterType")) or TYPE_TAGS.get(el.tag),
        "label": norm(el.get("Label")) or norm(el.get("GroupName")) or norm(el.get("Name")),
        "default": norm(el.get("Default")),
        "min": norm(el.get("Min")),
        "max": norm(el.get("Max")),
        "units": norm(el.get("Units")),
        "collection": norm(el.get("Collection")),
        "validate": norm(el.get("Validate")),
        "max_length": norm(el.get("TextMaxLength")),
        "increment": norm(el.get("Increment")),
    }
    return {k: v for k, v in rec.items() if v not in (None, "")}


def main():
    brand, cfg_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
    cfg = json.load(open(cfg_path))
    cfg_ids = {int(k) for k in cfg}

    recs = {}          # id -> record, first writer wins
    ambiguous = set()  # ids claimed by more than one branch/definition

    def add(pid, rec, branch):
        pid = int(pid)
        if pid in recs:
            if recs[pid].get("label") != rec.get("label"):
                ambiguous.add(pid)
            return
        rec["id"] = pid
        rec["branch"] = branch
        recs[pid] = rec

    # ---- 1. explicit ParameterId in every vendor XML file -------------------
    files = sorted(glob.glob(os.path.join(brand, "*.xml")))
    files = [f for f in files if not f.endswith(("Schemas.xml",))]
    for f in files:
        base = os.path.basename(f)
        try:
            root = load(f)
        except Exception:
            continue
        for el in root.iter():
            pid = norm(el.get("ParameterId"))
            if pid and pid.isdigit():
                r = describe(el)
                r["source"] = "xml:ParameterId"
                r["origin"] = el.tag
                add(pid, r, base)

    # ---- 2. list ranges ----------------------------------------------------
    lists_root = load(os.path.join(brand, "FMB640.Lists.xml"))
    list_defs = []
    for lc in lists_root.iter("ListConfiguration"):
        list_defs.append({
            "name": norm(lc.get("Name")),
            "start": int(lc.get("StartId")),
            "count": int(lc.get("NumberOfItems")),
            "type": norm(lc.get("ListType")),
            "default": norm(lc.get("Default")),
            "validate": norm(lc.get("Validate")),
            "max_length": norm(lc.get("TextMaxLength")),
            "mask": norm(lc.get("Mask")),
        })
    # group variants sharing a start id -> report candidate semantics instead of
    # silently choosing one
    by_start = {}
    for d in list_defs:
        by_start.setdefault(d["start"], []).append(d)
    for start, defs in by_start.items():
        span = max(d["count"] for d in defs)
        present = [i for i in range(start, start + span) if i in cfg_ids]
        if not present:
            continue
        names = sorted({d["name"] for d in defs})
        meta = min(defs, key=lambda d: abs(d["count"] - len(present)))
        for i in present:
            add(i, {
                "source": "xml:ListConfiguration",
                "type": meta["type"],
                "label": f"list entry {i - start + 1} (candidates: {', '.join(names[:4])})",
                "default": meta["default"],
                "validate": meta["validate"],
                "max_length": meta["max_length"],
                "collection": meta["name"],
                "path": f"List start={start}",
                "origin": "ListConfiguration",
            }, "FMB640.Lists.xml")

    # ---- 3. geozone / polygon arithmetic ----------------------------------
    for f in files:
        base = os.path.basename(f)
        try:
            root = load(f)
        except Exception:
            continue
        for gz in root.iter("Geozones"):
            start, off = int(gz.get("StartId")), int(gz.get("Offset"))
            children = [c for c in gz]
            for z in range(int(gz.get("Count"))):
                for order, child in enumerate(children):
                    pid = start + off * z + order
                    if pid not in cfg_ids:
                        continue
                    r = describe(child)
                    r["source"] = "xml:Geozones"
                    r["label"] = f"{norm(child.get('Label')) or child.tag} (zone {z + 1})"
                    r["path"] = "Geofencing / Geozones"
                    r["origin"] = "Geozones"
                    add(pid, r, base)
        for pg in root.iter("Polygon"):
            start, off = int(pg.get("StartId")), int(pg.get("Offset"))
            pts = int(pg.get("PointsCount"))
            z = 0
            while start + off * z in cfg_ids and z < 500:
                for i in range(pts * 2):
                    pid = start + off * z + i
                    if pid not in cfg_ids:
                        continue
                    add(pid, {
                        "source": "xml:Polygon",
                        "type": "Double",
                        "label": f"polygon {z + 1} point {i // 2 + 1} "
                                 f"{'longitude' if i % 2 == 0 else 'latitude'}",
                        "increment": norm(pg.get("Increment")),
                        "path": "Geofencing / Polygon",
                        "origin": "Polygon",
                    }, base)
                z += 1

    # ---- 4. report ---------------------------------------------------------
    mapped = cfg_ids & set(recs)
    report = {
        "cfg_params": len(cfg_ids),
        "schema_ids": len(recs),
        "cfg_covered": len(mapped),
        "cfg_unknown": len(cfg_ids - set(recs)),
        "schema_only": len(set(recs) - cfg_ids),
        "coverage_pct": round(100.0 * len(mapped) / len(cfg_ids), 2),
        "ambiguous_ids": len(ambiguous & cfg_ids),
        "by_source": {},
    }
    for pid in mapped:
        s = recs[pid]["source"]
        report["by_source"][s] = report["by_source"].get(s, 0) + 1

    rows = []
    for pid in sorted(recs):
        r = dict(recs[pid])
        r["in_cfg"] = pid in cfg_ids
        r["cfg_value"] = cfg.get(str(pid))
        r["ambiguous"] = pid in ambiguous
        rows.append(r)
    json.dump({"report": report, "params": rows}, open(out + "_schema.json", "w"), indent=1)
    json.dump(report, open(out + "_report.json", "w"), indent=1)
    unknown = sorted(cfg_ids - set(recs))
    gaps = []
    if unknown:
        s = p = unknown[0]
        for x in unknown[1:]:
            if x - p <= 1:
                p = x
            else:
                gaps.append((s, p, p - s + 1)); s = p = x
        gaps.append((s, p, p - s + 1))
    json.dump(gaps, open(out + "_gaps.json", "w"), indent=1)
    print(json.dumps(report, indent=2))
    print("largest unknown gaps:", sorted(gaps, key=lambda g: -g[2])[:12])


if __name__ == "__main__":
    main()
