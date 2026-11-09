#!/usr/bin/env python3
"""Merge vendor-generator definitions into the static schema and recompute coverage.

Input:  the vendor-compiled configuration document
        (generated_FMC650_spec1_cfg4.43.1.0.xml, produced by driving the vendor
        Configuration.Generator through tools/ximgen), the parsed cfg json, and
        the static schema built by build_schema.py as <out_prefix>_schema.json.
Output: <out_prefix>_schema.json, <out_prefix>_parameters.csv,
        <out_prefix>_report.json, <out_prefix>_gaps.json
        (the curated artifacts use out_prefix = fmx65_03.01.01.Rev.15).
"""
import csv, glob, json, os, sys
import xml.etree.ElementTree as ET

gen_xml, cfg_path, schema_path, out_prefix = sys.argv[1:5]
cfg = json.load(open(cfg_path))
cfg_ids = {int(k) for k in cfg}
old = json.load(open(schema_path))
recs = {int(p["id"]): p for p in old["params"]}
ambiguous = {int(p["id"]) for p in old["params"] if p.get("ambiguous")}


def norm(v):
    return v.strip() if isinstance(v, str) else v


root = ET.parse(gen_xml).getroot()
gen_count = 0
for el in root.iter():
    pid = norm(el.get("ParameterId"))
    if not pid or not pid.isdigit():
        continue
    pid = int(pid)
    rec = {
        "element": el.tag,
        "type": norm(el.get("ParameterType")) or norm(el.get("ListType")),
        "label": norm(el.get("Label")) or norm(el.get("GroupName")) or norm(el.get("Name")),
        "default": norm(el.get("Default")),
        "min": norm(el.get("Min")),
        "max": norm(el.get("Max")),
        "units": norm(el.get("Units")),
        "collection": norm(el.get("Collection")),
        "validate": norm(el.get("Validate")),
        "max_length": norm(el.get("TextMaxLength")),
        "increment": norm(el.get("Increment")),
        "source": "generator:FMC650:1",
        "origin": el.tag,
        "branch": "generated_FMC650_spec1_cfg4.43.1.0.xml",
    }
    rec = {k: v for k, v in rec.items() if v not in (None, "")}
    prev = recs.get(pid)
    if prev and prev.get("label") and rec.get("label") and prev["label"] != rec["label"]:
        ambiguous.add(pid)
    if prev:
        # inherit fields the compiled document omits (e.g. Collection has no
        # ParameterType) instead of regressing them to empty
        for k in ("type", "collection", "min", "max", "units", "validate",
                  "max_length", "default", "label", "path"):
            if k not in rec and prev.get(k):
                rec[k] = prev[k]
        rec["static_source"] = prev.get("static_source") or prev.get("source")
    rec["id"] = pid
    recs[pid] = rec
    gen_count += 1

# ---- IOItem blocks: id = IoId + order, order 0..4 ------------------------
# Evidence: IoId bases are spaced 10 apart (50000, 50010, ...); the cfg shows hits
# at offsets 0..4 for every item and 5..9 only for the next base's block. Bases come
# from the generated document *and* every vendor XML (2,445 unique), because the
# compiler only emits the subset visible for this hardware.
#
# Attribution rule: fill only ids that no stronger mechanism claims. A literal
# ParameterId in the vendor XML (or a generator-document element) outranks a
# block-formula claim — e.g. id 48100 is `<NumberInput ParameterId="48100"
# Label="Default data request period" Max="300">` in FMB640.BaseExtension.xml even
# though an `IoId="48100"` exists elsewhere; overwriting it as an IOItem would
# replace vendor metadata with a coincidental block match.
io_bases = {}
io_children_meta = {}
STD_IO_OFFSETS = {
    "Priority": 0, "Operand": 1, "HighLevel": 2, "LowLevel": 3,
    "EventOnly": 4, "AverageConstant": 5, "AveragingConstant": 5,
    "SendSmsTo": 6, "SmsText": 7,
}
MCAN_IO_OFFSETS = {
    "CanType": 0, "DataMask": 1, "CanId": 2, "CanSrc": 3, "Operand": 4,
}
# 1. Authoritative compiler-generated XML (generated_FMC650_spec1_cfg4.43.1.0.xml) wins first
for io in root.iter("IOItem"):
    b = norm(io.get("IoId"))
    if b and b.isdigit():
        base_int = int(b)
        io_bases.setdefault(base_int, (norm(io.get("Name")), norm(io.get("Units")), "generated_FMC650_spec1_cfg4.43.1.0.xml"))
        child_tags = {c.tag for c in io}
        is_mcan = "CanType" in child_tags
        for c in io:
            if "Offset" in c.attrib:
                off = int(c.attrib["Offset"])
            elif is_mcan and c.tag in MCAN_IO_OFFSETS:
                off = MCAN_IO_OFFSETS[c.tag]
            elif c.tag in STD_IO_OFFSETS:
                off = STD_IO_OFFSETS[c.tag]
            else:
                continue
            io_children_meta.setdefault(base_int + off, {
                "field_tag": c.tag,
                "type": norm(c.get("ParameterType")),
                "default": norm(c.get("Default")),
                "min": norm(c.get("Min")),
                "max": norm(c.get("Max")),
                "collection": norm(c.get("Collection")),
                "validate": norm(c.get("Validate")),
                "max_length": norm(c.get("TextMaxLength")),
            })
# 2. Secondary Brand.dll XMLs fill only IoId bases absent from the compiled FMC650 document
if len(sys.argv) > 5 and sys.argv[5]:
    for f in sorted(glob.glob(os.path.join(sys.argv[5], "*.xml"))):
        try:
            r = ET.parse(f).getroot()
        except Exception:
            continue
        for e in r.iter("IOItem"):
            b = norm(e.get("IoId"))
            if b and b.isdigit():
                io_bases.setdefault(int(b), (norm(e.get("Name")), norm(e.get("Units")), "vendor IOItem"))

io_added = 0
for base, (name, units, branch_src) in io_bases.items():
    name = name or f"IO {base}"
    for order in range(6):
        pid = base + order
        if pid not in cfg_ids:
            continue
        if pid in recs:   # an existing literal/generator definition outranks the block formula
            continue
        cmeta = io_children_meta.get(pid, {})
        field_tag = cmeta.get("field_tag")
        rec = {
            "element": "IOItem",
            "label": name if order == 0 else (f"{name} ({field_tag})" if field_tag else f"{name} (field {order + 1})"),
            "units": units if order in (0, 2, 3) else None,
            "type": cmeta.get("type"),
            "default": cmeta.get("default"),
            "min": cmeta.get("min"),
            "max": cmeta.get("max"),
            "collection": cmeta.get("collection"),
            "validate": cmeta.get("validate"),
            "max_length": cmeta.get("max_length"),
            "source": "generator:IOItem",
            "origin": "IOItem",
            "branch": branch_src,
            "path": f"IOItem block {base}",
        }
        rec = {k: v for k, v in rec.items() if v not in (None, "")}
        prev = recs.get(pid)
        if prev:
            rec["static_source"] = prev.get("static_source") or prev.get("source")
        rec["id"] = pid
        recs[pid] = rec
        io_added += 1

rows = []
for pid in sorted(recs):
    r = dict(recs[pid])
    r["in_cfg"] = pid in cfg_ids
    r["cfg_value"] = cfg.get(str(pid))
    r["ambiguous"] = pid in ambiguous
    rows.append(r)

mapped = cfg_ids & set(recs)
by_source = {}
for pid in mapped:
    s = recs[pid].get("source", "?")
    by_source[s] = by_source.get(s, 0) + 1

report = {
    "cfg_params": len(cfg_ids),
    "schema_ids": len(recs),
    "cfg_covered": len(mapped),
    "cfg_unknown": len(cfg_ids - set(recs)),
    "schema_only": len(set(recs) - cfg_ids),
    "coverage_pct": round(100.0 * len(mapped) / len(cfg_ids), 2),
    "ambiguous_ids": len(ambiguous & cfg_ids),
    "generator_definitions": gen_count,
    "ioitem_definitions": io_added,
    "by_source": by_source,
}
json.dump({"report": report, "params": rows}, open(out_prefix + "_schema.json", "w"), indent=1)
json.dump(report, open(out_prefix + "_report.json", "w"), indent=1)

fields = ["id","in_cfg","cfg_value","source","element","type","label","default","min","max",
          "units","collection","validate","max_length","increment","path","origin","branch",
          "ambiguous","static_source"]
with open(out_prefix + "_parameters.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\r\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

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
json.dump(gaps, open(out_prefix + "_gaps.json", "w"), indent=1)
print(json.dumps(report, indent=2))
