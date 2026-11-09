#!/usr/bin/env python3
"""Single Authoritative .cfg Validation, Preset Generation & Compilation Engine for FMC650.

Enforces 100% of the structural, XML, and hexadecimal rules documented in
`re/cfgs/FMC650_CFG_Save_Failure_Debugging_Report.md` so no human or AI agent can
produce a .cfg file that fails Teltonika Configurator's "Save to device" check:

1. Anchor-Set Invariance:
   The parameter ID set is copied from a real vendor-exported reference .cfg
   (e.g. `4.43.1.0` with 11,688 IDs for FW `03.01.01.Rev.15`, or `4.41.0.0` with
   7,963 IDs for FW `01.02.10`) and verified invariant on write via `cfg_tool.write_cfg`.
2. Manual CAN Requests (`17000..17699`) Hex & Offset Protection:
   - `+0` (`17000, 17010, ..., 17690`, `Req ID`): MUST be an exact 8-character hex
     string (default `'00000000'`), never `'0'` or `''`. (`+1` is `RTR`).
   - `+2` (`17002, 17012, ..., 17692`, `Payload`): MUST be an exact 16-character hex
     string (default `'0000000000000000'`), never `'0'`, `'00000000'`, or `''`.
3. Manual CAN I/O Reception `CanId` (`47002..47292`, `90002..90492`) Decimal UInt32 Guard:
   - Stored in `.cfg` as a decimal `UInt32` (`0..4294967295`, e.g. `'419360512'` for
     `0x18FEEF00`). If an agent supplies a hex string, validation fails with the exact
     decimal `UInt32` value to use.
4. Strict `<CollectionConfiguration>` Enum Membership (81 XML Tables):
   - Rejects `PID 47500 = '0'` (`Tachograph Data -> Timestamp -> Priority` uses
     `TimestampCollection = {'1': 'Low', '2': 'High', '3': 'Panic'}`).
   - Enforces all 5 `<Operand>` collections (`OperandCollection`, `OperandCollectionKLN`,
     `OperandCollectionKLNTimestamp`, `OperandCollectionLimited`, `OperandCollection_ainps`).
5. Authoritative Compiler XML Precedence:
   - Definitions in `generated_FMC650_spec1_cfg4.43.1.0.xml` never inherit conflicting
     constraints from secondary FMB family XMLs in `fmx65_03.01.01.Rev.15_schema.json`.

Usage:
  # 1. Custom PID=value edits on any reference .cfg:
  python make_cfg.py <reference.cfg> <out.cfg> [id=value ...]

  # 2. Generate Fleet Telematics v1.2 fleet preset profiles:
  python make_cfg.py --preset all
  python make_cfg.py --preset p2_production
"""
from __future__ import annotations

from functools import lru_cache
import json
import os
from pathlib import Path
import re
import sys
from typing import Any
import xml.etree.ElementTree as ET

TOOLS_DIR = Path(__file__).resolve().parent
RE_ROOT = TOOLS_DIR.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import cfg_tool  # noqa: E402

DEFAULT_SCHEMA = str(RE_ROOT / "re" / "fmx65_03.01.01.Rev.15_schema.json")
DEFAULT_XML = str(RE_ROOT / "re" / "generated_FMC650_spec1_cfg4.43.1.0.xml")
CFGS_DIR = (RE_ROOT / "cfgs") if (RE_ROOT / "cfgs").exists() else (RE_ROOT / "re" / "cfgs")
EXPORT_DIR = Path(os.environ["FMC650_EXPORT_DIR"]) if os.environ.get("FMC650_EXPORT_DIR") else None
ANCHOR_REV15_PATH = CFGS_DIR / "device_export_original.cfg"
ANCHOR_F15_PATH = CFGS_DIR / "FMC650_FLEET_P2_PRODUCTION_v1.2_fw010210.cfg"

NUMERIC_TYPES = {"Byte", "Int32", "UInt16", "UInt32", "Float", "Double", "LLS"}
NON_PARAM_RULE_TAGS = {"If", "NoAction"}

STD_IO_OFFSETS = {
    "Priority": 0,
    "Operand": 1,
    "HighLevel": 2,
    "LowLevel": 3,
    "EventOnly": 4,
    "AverageConstant": 5,
    "AveragingConstant": 5,
}
MCAN_IO_OFFSETS = {
    "CanType": 0,
    "DataMask": 1,
    "CanId": 2,
    "CanSrc": 3,
    "Operand": 4,
}

# Manual CAN Request parameter ID sets (17000..17699, 70 slots spaced by 10)
MCAN_REQ_ID_PIDS: frozenset[int] = frozenset(range(17000, 17700, 10))
MCAN_REQ_PAYLOAD_PIDS: frozenset[int] = frozenset(range(17002, 17700, 10))

# The 26 native TrailerCAN (ISO 11992-2 / WABCO TEBS E) parameter base IDs + 103020 (Vehicle ABS Status)
TRAILERCAN_40_TABLE_IDS: tuple[int, ...] = (
    103000, 103060, 103110, 103120, 103130, 103200, 103300, 103310,
    103220, 103080, 103210, 103270, 103280, 104570, 104230, 104590,
    103140, 103150, 103160, 103170, 103180, 103190, 103090, 103040,
    103050, 104580,
)
TRAILERCAN_EXTRA_IDS: tuple[int, ...] = (103020,)


def _strip_ns(tag: str) -> str:
    return tag.split("}", 1)[-1] if "}" in tag else tag


@lru_cache(maxsize=4)
def load_xml_constraints(xml_path: str = DEFAULT_XML) -> tuple[dict[str, dict[str, str]], dict[int, dict[str, Any]]]:
    """Parse CollectionConfiguration tables, ParameterId definitions, IOItem blocks, and List/Geozone ranges."""
    collections: dict[str, dict[str, str]] = {}
    xml_params: dict[int, dict[str, Any]] = {}
    if not xml_path or not os.path.exists(xml_path):
        return collections, xml_params

    root = ET.parse(xml_path).getroot()

    for el in root.iter():
        if _strip_ns(el.tag) == "CollectionConfiguration":
            cname = el.attrib.get("Name", "")
            items: dict[str, str] = {}
            for child in el:
                if _strip_ns(child.tag) == "CollectionItem":
                    v = child.attrib.get("Value")
                    t = child.attrib.get("Text", "")
                    if v is not None:
                        items[v] = t
            if cname:
                collections[cname] = items

    for el in root.iter():
        tag = _strip_ns(el.tag)
        if tag in NON_PARAM_RULE_TAGS:
            continue

        pid_str = el.attrib.get("ParameterId")
        if pid_str and pid_str.isdigit():
            pid = int(pid_str)
            existing = xml_params.get(pid)
            if existing is None:
                xml_params[pid] = {
                    "tag": tag,
                    "name": el.attrib.get("Label") or el.attrib.get("Name") or tag,
                    "attrib": dict(el.attrib),
                }
            else:
                for k, v in el.attrib.items():
                    existing["attrib"].setdefault(k, v)
                if existing["name"] == existing["tag"] and (el.attrib.get("Label") or el.attrib.get("Name")):
                    existing["name"] = el.attrib.get("Label") or el.attrib.get("Name")

        elif tag == "IOItem":
            io_id_str = el.attrib.get("IoId")
            if io_id_str and io_id_str.isdigit():
                io_id = int(io_id_str)
                io_name = el.attrib.get("Name", f"IO_{io_id}")
                child_tags = {_strip_ns(c.tag) for c in el}
                is_mcan = "CanType" in child_tags
                for c in el:
                    ctag = _strip_ns(c.tag)
                    if "Offset" in c.attrib:
                        off = int(c.attrib["Offset"])
                    elif is_mcan and ctag in MCAN_IO_OFFSETS:
                        off = MCAN_IO_OFFSETS[ctag]
                    elif ctag in STD_IO_OFFSETS:
                        off = STD_IO_OFFSETS[ctag]
                    else:
                        continue
                    xml_params[io_id + off] = {
                        "tag": f"IOItem.{ctag}",
                        "name": f"{io_name} -> {ctag}",
                        "attrib": dict(c.attrib),
                        "io_id": io_id,
                        "io_name": io_name,
                        "is_mcan": is_mcan,
                    }

    return collections, xml_params


@lru_cache(maxsize=4)
def load_schema_data(schema_path: str = DEFAULT_SCHEMA) -> dict[str, Any]:
    """Load and cache the full schema JSON dictionary."""
    if not schema_path or not os.path.exists(schema_path):
        return {}
    with open(schema_path, encoding="utf-8") as fh:
        return json.load(fh)


@lru_cache(maxsize=4)
def load_schema_map(schema_path: str = DEFAULT_SCHEMA) -> dict[int, dict[str, Any]]:
    """Load and cache the parameter schema JSON indexed by integer PID."""
    data = load_schema_data(schema_path)
    raw_params = data.get("params", {})
    if isinstance(raw_params, list):
        return {int(p["id"]): p for p in raw_params if isinstance(p, dict) and "id" in p}
    return {int(k): v for k, v in raw_params.items() if str(k).isdigit()}


def synthesize_param_row(
    pid: int,
    schema_map: dict[int, dict[str, Any]] | None = None,
    xml_path: str = DEFAULT_XML,
) -> dict[str, Any] | None:
    """Return the schema row for pid, or synthesize one from XML constraints for valid IOItem child offsets."""
    smap = schema_map if schema_map is not None else load_schema_map()
    row = smap.get(int(pid))
    if row is not None:
        return row
    _, xml_params = load_xml_constraints(xml_path)
    xmeta = xml_params.get(int(pid))
    if xmeta is not None:
        attr = xmeta.get("attrib", {})
        return {
            "id": int(pid),
            "name": xmeta.get("name", f"Parameter {pid}"),
            "label": xmeta.get("name", f"Parameter {pid}"),
            "type": attr.get("ParameterType", "Byte"),
            "default": attr.get("Default", ""),
            "min": int(attr["Min"]) if attr.get("Min", "").lstrip("-").isdigit() else None,
            "max": int(attr["Max"]) if attr.get("Max", "").lstrip("-").isdigit() else None,
            "collection": attr.get("Collection"),
            "validate": attr.get("Validate"),
            "max_length": int(attr["TextMaxLength"]) if attr.get("TextMaxLength", "").isdigit() else None,
        }
    return None


def _check_validate_expression(
    pid: int,
    raw: str,
    label: str,
    validate_expr: str,
    xml_default: str | None = None,
) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    """Check Length(...), Hex, and Regex(...) rules in a Validate attribute."""
    fails: list[tuple[str, str]] = []
    warns: list[tuple[str, str]] = []

    # Dedicated guard for Manual CAN Request Req ID (17000..17690) and Payload (17002..17692)
    if pid in MCAN_REQ_ID_PIDS:
        if len(raw) != 8 or not re.fullmatch(r"[0-9A-Fa-f]{8}", raw):
            fails.append((
                "FAIL",
                f"id {pid} ({label}): '{raw}' violates Length(0,8); Length(8,8); Hex — "
                f"Manual CAN Request Req ID (+0) in .cfg MUST be an exact 8-character hex string "
                f"(default '00000000', never '0' or ''; +1={pid + 1} is RTR).",
            ))
        return fails, warns

    if pid in MCAN_REQ_PAYLOAD_PIDS:
        if len(raw) != 16 or not re.fullmatch(r"[0-9A-Fa-f]{16}", raw):
            fails.append((
                "FAIL",
                f"id {pid} ({label}): '{raw}' violates Length(0,16); Length(8,16); Hex — "
                f"Manual CAN Request 8-byte Payload (+2) in .cfg MUST be an exact 16-character hex string "
                f"(default '0000000000000000', never '0' or 8-char '00000000').",
            ))
        return fails, warns

    if not validate_expr:
        return fails, warns

    if validate_expr.startswith("Regex") and f"({raw})" not in validate_expr:
        pat = validate_expr[len("Regex"):]
        try:
            if not re.fullmatch(pat, raw):
                fails.append(("FAIL", f"id {pid} ({label}): '{raw}' fails regex {pat}"))
        except re.error:
            warns.append(("WARN", f"id {pid} ({label}): unparseable regex {pat}"))

    # Parse all Length(...) clauses, including multi-arg Length(0,2,4,6,8,10,12,14,16,18,20)
    raw_len_groups = re.findall(r"Length\(\s*([0-9,\s]+)\s*\)", validate_expr)
    if raw_len_groups:
        parsed_groups = [
            [int(tok.strip()) for tok in grp.split(",") if tok.strip().isdigit()]
            for grp in raw_len_groups
        ]
        # Multi-value discrete length list e.g. Length(0,2,4,6,8,10,12,14,16,18,20)
        if len(parsed_groups) == 1 and len(parsed_groups[0]) > 2:
            allowed_lens = set(parsed_groups[0])
            if len(raw) not in allowed_lens:
                fails.append((
                    "FAIL",
                    f"id {pid} ({label}): length {len(raw)} of '{raw}' violates {validate_expr} "
                    f"(allowed lengths: {sorted(allowed_lens)})",
                ))
        else:
            two_arg = [(g[0], g[1]) for g in parsed_groups if len(g) == 2]
            if two_arg:
                eff_min = max(a for a, _ in two_arg)
                eff_max = min(b for _, b in two_arg)
                allows_empty = (xml_default == "") and any(a == 0 for a, _ in two_arg)
                if not ((allows_empty and len(raw) == 0) or (eff_min <= len(raw) <= eff_max)):
                    fails.append((
                        "FAIL",
                        f"id {pid} ({label}): length {len(raw)} of '{raw}' violates {validate_expr} "
                        f"(required {eff_min}..{eff_max} chars"
                        f"{' or empty string' if allows_empty else ''})",
                    ))

    tokens = [t.strip() for t in validate_expr.split(";")]
    if "Hex" in tokens:
        if not re.fullmatch(r"[0-9A-Fa-f]*", raw):
            fails.append(("FAIL", f"id {pid} ({label}): '{raw}' is not valid hexadecimal ({validate_expr})"))

    return fails, warns


def check_value(
    pid: int | str,
    raw: Any,
    row: dict[str, Any] | None = None,
    xml_path: str = DEFAULT_XML,
) -> list[tuple[str, str]]:
    """Validate a single (pid, value) edit against the authoritative compiled XML and schema JSON."""
    pid_int = int(pid)
    raw_str = str(raw)
    notes: list[tuple[str, str]] = []

    collections, xml_params = load_xml_constraints(xml_path)
    xinfo = xml_params.get(pid_int)
    if row is None:
        row = synthesize_param_row(pid_int, xml_path=xml_path)
    if not row and not xinfo:
        return [("FAIL", f"id {pid_int} is not in the schema or XML — refusing (anchor-set violation)")]

    row = row or {}
    xatt = xinfo["attrib"] if xinfo else {}
    has_xml_def = xinfo is not None

    # Authoritative XML attributes take strict precedence; do not inherit conflicting
    # constraints from secondary FMB XMLs in `row` when `has_xml_def` is True.
    typ = xatt.get("ParameterType") or ("" if has_xml_def else (row.get("type") or ""))
    label = (xinfo["name"] if xinfo else None) or row.get("label") or row.get("name") or "(unlabeled)"
    lo = xatt.get("Min") if has_xml_def else (xatt.get("Min") if xatt.get("Min") not in (None, "") else row.get("min"))
    hi = xatt.get("Max") if has_xml_def else (xatt.get("Max") if xatt.get("Max") not in (None, "") else row.get("max"))
    col_name = xatt.get("Collection") if has_xml_def else (xatt.get("Collection") or row.get("collection"))
    val_expr = xatt.get("Validate") if has_xml_def else (xatt.get("Validate") or row.get("validate") or "")
    val_expr = val_expr or ""
    max_len = (
        xatt.get("TextMaxLength")
        if has_xml_def
        else (xatt.get("TextMaxLength") if xatt.get("TextMaxLength") not in (None, "") else row.get("max_length"))
    )
    xml_default = xatt.get("Default") if has_xml_def else row.get("default")

    # If the parameter is not in the compiled FMC650 XML (`has_xml_def` is False) and the value
    # matches the factory .cfg export value (`cfg_value`) or default, accept it without false positives.
    if not has_xml_def and raw_str in {str(row.get("cfg_value", "")), str(row.get("default", ""))}:
        return [("OK", f"id {pid_int} ({label}): factory default {raw_str!r} preserved")]

    # 1. XML CollectionConfiguration enum check (catches e.g. PID 47500 TimestampCollection={'1','2','3'})
    if col_name and col_name in collections:
        allowed = collections[col_name]
        if allowed and raw_str not in allowed:
            pos_ints = [int(k) for k in allowed if k.isdigit() and int(k) > 0]
            is_bitmask_coll = (
                pid_int in (100, 101, 109, 157, 12454)
                or (xinfo is not None and xinfo.get("tag") == "Collection")
                or "bitmask" in col_name.lower()
            ) and bool(pos_ints)
            bitmask_max = max(63, sum(pos_ints), (1 << (len(pos_ints) + 1)) - 1) if is_bitmask_coll else 0
            is_xml_default = xml_default is not None and raw_str == str(xml_default)

            if not (is_xml_default or (is_bitmask_coll and raw_str.isdigit() and 0 <= int(raw_str) <= bitmask_max)):
                allowed_str = ", ".join(f"'{k}' ({v})" for k, v in sorted(allowed.items()))
                extra_hint = ""
                if pid_int == 47500 and raw_str == "0":
                    extra_hint = (
                        " — Tachograph Timestamp Priority (PID 47500) cannot be '0' (None); "
                        "use '1' (Low), '2' (High), or '3' (Panic)."
                    )
                return [(
                    "FAIL",
                    f"id {pid_int} ({label}): '{raw_str}' is not in XML Collection '{col_name}' "
                    f"(allowed: {allowed_str}){extra_hint}",
                )]

    # 2. Manual CAN I/O Reception CanId (+2 in 47000..47290, 90000..90490) Decimal UInt32 Guard
    is_mcan_canid = bool(xinfo and xinfo.get("is_mcan") and xinfo.get("tag") == "IOItem.CanId")
    if is_mcan_canid:
        if not raw_str.isdigit():
            hex_cand = raw_str[2:] if raw_str.lower().startswith("0x") else raw_str
            dec_hint = ""
            if re.fullmatch(r"[0-9A-Fa-f]{1,8}", hex_cand):
                dec_hint = f" (for hex 0x{hex_cand.upper()}, pass decimal '{int(hex_cand, 16)}')"
            return [(
                "FAIL",
                f"id {pid_int} ({label}): '{raw_str}' is not a decimal UInt32 — "
                f"Manual CAN IOItem CanId (+2) is stored as a decimal integer in .cfg{dec_hint}",
            )]

    # 3. Numeric type and range checks
    if typ in NUMERIC_TYPES:
        if raw_str == "" and xml_default == "":
            return [("OK", f"id {pid_int} ({label}): {row.get('cfg_value', '')!r} -> '' (XML empty default)")]
        try:
            v = float(raw_str)
        except ValueError:
            return [("FAIL", f"id {pid_int} ({label}): '{raw_str}' is not a {typ}")]
        if typ in ("Byte", "Int32", "UInt16", "UInt32") and "." in raw_str:
            return [("FAIL", f"id {pid_int} ({label}): '{raw_str}' must be an integer")]
        # Collection-backed parameters (e.g. PID 205/207 can_bus_speed with 500/1000 kbps)
        # or explicit Max > 255 expand the upper bound of Byte/UInt16.
        coll_max = (
            max((float(k) for k in collections.get(col_name, {}) if k.lstrip("-").isdigit()), default=0.0)
            if col_name
            else 0.0
        )
        effective_byte_max = max(255.0, float(hi) if hi not in (None, "") else 0.0, coll_max)
        if typ == "Byte" and not (0 <= v <= effective_byte_max):
            return [("FAIL", f"id {pid_int} ({label}): {raw_str} outside Byte range (0..{int(effective_byte_max)})")]
        if typ == "UInt16" and not (0 <= v <= max(65535.0, float(hi) if hi not in (None, "") else 0.0)):
            return [("FAIL", f"id {pid_int} ({label}): {raw_str} outside UInt16 range (0..65535)")]
        if typ == "UInt32" and not (0 <= v <= max(4294967295.0, float(hi) if hi not in (None, "") else 0.0)):
            return [("FAIL", f"id {pid_int} ({label}): {raw_str} outside UInt32 range (0..4294967295)")]
        if lo not in (None, "") and float(lo) > v:
            return [("FAIL", f"id {pid_int} ({label}): {raw_str} < min {lo}")]
        if hi not in (None, "") and float(hi) < v:
            return [("FAIL", f"id {pid_int} ({label}): {raw_str} > max {hi}")]

    # 4. String length & Validate (Regex / Length(...) / Hex) checks
    if typ == "String" or (val_expr and not is_mcan_canid) or pid_int in (MCAN_REQ_ID_PIDS | MCAN_REQ_PAYLOAD_PIDS):
        if max_len not in (None, "") and len(raw_str) > int(max_len):
            return [("FAIL", f"id {pid_int} ({label}): longer than {max_len} chars")]
        fails, warns = _check_validate_expression(
            pid_int, raw_str, label, val_expr, xml_default=str(xml_default) if xml_default is not None else None
        )
        if fails:
            return fails
        notes.extend(warns)
    elif not typ and not col_name:
        notes.append(("WARN", f"id {pid_int} ({label}): row has no encoded type"))

    if not any((lo, hi, val_expr, col_name, max_len, row.get("default"), typ)):
        notes.append(("WARN", f"id {pid_int} ({label}): row has NO encoded constraint — device-side validation unknown"))
    else:
        notes.append(("OK", f"id {pid_int} ({label}): {row.get('cfg_value', '')!r} -> {raw_str!r}"))
    return notes


def validate_cfg_edits(
    base_params: dict[Any, str],
    header: dict[str, str],
    edits: dict[Any, Any],
    schema_map: dict[int, dict[str, Any]] | None = None,
    xml_path: str = DEFAULT_XML,
    base_name: str = "reference.cfg",
) -> dict[str, Any]:
    """Validate a dictionary of {pid: value} edits against a base .cfg anchor set and XML/schema constraints."""
    smap = schema_map if schema_map is not None else load_schema_map()
    anchor_int_map: dict[int, str] = {int(k): str(v) for k, v in base_params.items() if str(k).isdigit()}

    errors: list[str] = []
    warnings: list[str] = []
    details: list[dict[str, Any]] = []

    for raw_pid, raw_val in sorted(edits.items(), key=lambda x: int(x[0])):
        pid = int(raw_pid)
        val_str = str(raw_val)

        if pid not in anchor_int_map:
            msg = (
                f"id {pid}: absent from reference .cfg anchor '{base_name}' "
                f"(ConfigurationVersion={header.get('ConfigurationVersion')}) — anchor-set violation"
            )
            errors.append(msg)
            details.append({"pid": pid, "proposed": val_str, "status": "FAIL", "messages": [msg]})
            continue

        row = synthesize_param_row(pid, schema_map=smap, xml_path=xml_path)
        issues = check_value(pid, val_str, row=row, xml_path=xml_path)
        pid_errors: list[str] = []
        pid_warns: list[str] = []
        for level, msg in issues:
            if level == "FAIL" or "anchor-set violation" in msg:
                pid_errors.append(msg)
                errors.append(msg)
            else:
                pid_warns.append(msg)
                warnings.append(msg)

        details.append({
            "pid": pid,
            "current_in_anchor": anchor_int_map.get(pid),
            "proposed": val_str,
            "status": "FAIL" if pid_errors else "PASS",
            "messages": pid_errors + pid_warns,
        })

    return {
        "base_profile": base_name,
        "header": header,
        "total_anchor_parameters": len(anchor_int_map),
        "validation_passed": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "details": details,
    }


def compile_cfg(
    ref_path: str | Path,
    out_path: str | Path | None,
    edits: dict[Any, Any],
    schema_path: str = DEFAULT_SCHEMA,
    xml_path: str = DEFAULT_XML,
) -> dict[str, Any]:
    """Read reference .cfg, validate edits, and if valid and out_path is set, write deterministic gzip .cfg."""
    ref_file = Path(ref_path)
    header, base_params, _ = cfg_tool.read_cfg(ref_file)
    smap = load_schema_map(schema_path)
    val_report = validate_cfg_edits(
        base_params=base_params,
        header=header,
        edits=edits,
        schema_map=smap,
        xml_path=xml_path,
        base_name=ref_file.name,
    )

    if not val_report["validation_passed"]:
        return {
            "validation_report": val_report,
            "output_path": None,
            "sha256": None,
            "size_bytes": 0,
            "modified_count": 0,
            "total_parameters": len(base_params),
        }

    new_params = dict(base_params)
    modified_count = 0
    for raw_pid, raw_val in edits.items():
        k_str = str(int(raw_pid))
        v_str = str(raw_val)
        if new_params.get(k_str) != v_str:
            modified_count += 1
        new_params[k_str] = v_str

    out_path_str: str | None = None
    sha256_hex: str | None = None
    size_bytes = 0
    if out_path is not None:
        gz_bytes, sha256_hex = cfg_tool.write_cfg(
            out_path,
            header,
            new_params,
            reference_keys={int(k) for k in base_params},
        )
        out_path_str = str(out_path)
        size_bytes = len(gz_bytes)

    return {
        "validation_report": val_report,
        "output_path": out_path_str,
        "sha256": sha256_hex,
        "size_bytes": size_bytes,
        "modified_count": modified_count,
        "total_parameters": len(new_params),
    }


# ---------------------------------------------------------------------------
# Built-in Fleet Telematics v1.2 Preset Profile Builders
# ---------------------------------------------------------------------------

def set_io_block(
    edits: dict[str, str],
    base_params: dict[str, str],
    io_id: int,
    priority: str,
    operand: str | None = None,
    high_level: str | None = None,
    low_level: str | None = None,
    event_only: str | None = None,
    averaging: str | None = None,
) -> None:
    """Set fields of a standard 6-field IOItem block (only touching PIDs present in base_params)."""
    if str(io_id) in base_params:
        edits[str(io_id)] = str(priority)
    if operand is not None and str(io_id + 1) in base_params:
        edits[str(io_id + 1)] = str(operand)
    if high_level is not None and str(io_id + 2) in base_params:
        edits[str(io_id + 2)] = str(high_level)
    if low_level is not None and str(io_id + 3) in base_params:
        edits[str(io_id + 3)] = str(low_level)
    if event_only is not None and str(io_id + 4) in base_params:
        edits[str(io_id + 4)] = str(event_only)
    if averaging is not None and str(io_id + 5) in base_params:
        edits[str(io_id + 5)] = str(averaging)


def apply_optimizations_and_40_params(
    edits: dict[str, str],
    base_params: dict[str, str],
    enable_trailercan: bool = True,
) -> None:
    """Apply Network/Packet/Queue Optimizations + the 40 Weight/TrailerCAN parameters."""
    edits["1000"] = "120"  # Open Link Timeout = 120 s
    edits["1001"] = "5"    # Response Timeout = 5 s (prevents Wialon lag from blocking Flespi)
    edits["1002"] = "1"    # Sort By = 1 (Oldest First / FIFO)
    edits["1006"] = "0"    # Save records to = 0 (Internal memory)

    for io_id in (45290, 45300, 45310, 45320, 45330):
        set_io_block(edits, base_params, io_id, priority="1", operand="3", high_level="0", low_level="0", event_only="0")

    set_io_block(edits, base_params, 46530, priority="2", operand="3", high_level="0", low_level="0", event_only="0")

    for io_id in (45860, 48940, 90750, 90760, 90770, 90780):
        set_io_block(edits, base_params, io_id, priority="0", operand="3", high_level="0", low_level="0", event_only="0")

    if "330" in base_params:
        edits["330"] = "2" if enable_trailercan else "0"
    for io_id in TRAILERCAN_40_TABLE_IDS + TRAILERCAN_EXTRA_IDS:
        set_io_block(
            edits, base_params, io_id,
            priority="1" if enable_trailercan else "0",
            operand="3", high_level="0", low_level="0", event_only="0",
        )

    for io_id in (180510, 180520):
        set_io_block(edits, base_params, io_id, priority="0", operand="3", high_level="0", low_level="0", event_only="0")


def apply_fms_and_safety_v12(edits: dict[str, str], base_params: dict[str, str]) -> None:
    """Apply Guide v1.2 FMS & DOUT settings while preserving 17000..17699, 47500, and CAN0..CAN23."""
    edits["11003"] = "1"    # Green Driving Output Control -> 1 = None (never DOUT 2)
    edits["11103"] = "1"    # Overspeeding Output Control -> 1 = None (never DOUT 2)
    edits["13002"] = "720"  # FOTA WEB Period -> 720 min

    for io_id in (46100, 46110, 46120, 46130):
        set_io_block(edits, base_params, io_id, priority="1", operand="3", high_level="0", low_level="0", event_only="0")

    for io_id in (46790, 46800, 46880, 46900):
        set_io_block(edits, base_params, io_id, priority="1", event_only="0")

    set_io_block(edits, base_params, 50000, priority="2", event_only="0")
    set_io_block(edits, base_params, 50010, priority="2", event_only="0")
    set_io_block(edits, base_params, 50020, priority="1", event_only="0")
    set_io_block(edits, base_params, 50040, priority="1", event_only="0")
    set_io_block(edits, base_params, 50050, priority="2", event_only="0")
    set_io_block(edits, base_params, 50140, priority="1", event_only="0")
    set_io_block(edits, base_params, 50160, priority="1", event_only="0")
    set_io_block(edits, base_params, 50170, priority="1", event_only="0")


def apply_acquisition_p2(edits: dict[str, str]) -> None:
    """§5.2 P2 — Production Data Acquisition settings."""
    edits.update({
        "10000": "60", "10004": "1", "10005": "300",
        "10050": "20", "10051": "100", "10052": "10", "10053": "10", "10054": "1", "10055": "60",
        "10100": "300", "10104": "1", "10105": "900",
        "10150": "60", "10151": "250", "10152": "15", "10153": "15", "10154": "1", "10155": "120",
        "10200": "300", "10204": "1", "10205": "900",
        "10250": "60", "10251": "250", "10252": "15", "10253": "15", "10254": "1", "10255": "120",
    })


def apply_acquisition_p1(edits: dict[str, str]) -> None:
    """§5.1 P1 — Pilote Haute Résolution Data Acquisition settings."""
    edits.update({
        "10000": "15", "10004": "1", "10005": "30",
        "10050": "10", "10051": "50", "10052": "5", "10053": "5", "10054": "1", "10055": "30",
        "10100": "300", "10104": "1", "10105": "900",
        "10150": "60", "10151": "250", "10152": "15", "10153": "15", "10154": "1", "10155": "120",
        "10200": "300", "10204": "1", "10205": "900",
        "10250": "60", "10251": "250", "10252": "15", "10253": "15", "10254": "1", "10255": "120",
    })


def generate_all_fleet_profiles(preset_filter: str = "all") -> list[dict[str, Any]]:
    """Build and strictly validate the Fleet Telematics v1.2 .cfg profiles using compile_cfg."""
    rev15_path = ANCHOR_REV15_PATH if ANCHOR_REV15_PATH.exists() else (CFGS_DIR / "device_export_original.cfg")
    _, rev15_base, _ = cfg_tool.read_cfg(rev15_path)
    CFGS_DIR.mkdir(parents=True, exist_ok=True)

    profiles_spec: list[tuple[str, str, Path, dict[str, str]]] = []

    edits_p2: dict[str, str] = {}
    apply_optimizations_and_40_params(edits_p2, rev15_base, enable_trailercan=True)
    apply_fms_and_safety_v12(edits_p2, rev15_base)
    apply_acquisition_p2(edits_p2)
    profiles_spec.append(("p2_production", "FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg", rev15_path, edits_p2))

    edits_surgical: dict[str, str] = {}
    apply_optimizations_and_40_params(edits_surgical, rev15_base, enable_trailercan=True)
    profiles_spec.append(("p2_surgical", "FMC650_FLEET_P2_SURGICAL_rev15.cfg", rev15_path, edits_surgical))

    edits_p1: dict[str, str] = {}
    apply_optimizations_and_40_params(edits_p1, rev15_base, enable_trailercan=True)
    apply_fms_and_safety_v12(edits_p1, rev15_base)
    apply_acquisition_p1(edits_p1)
    profiles_spec.append(("p1_pilote_hr", "FMC650_FLEET_P1_PILOTE_HR_v1.2_rev15.cfg", rev15_path, edits_p1))

    edits_p0: dict[str, str] = {}
    apply_optimizations_and_40_params(edits_p0, rev15_base, enable_trailercan=False)
    apply_fms_and_safety_v12(edits_p0, rev15_base)
    apply_acquisition_p2(edits_p0)
    profiles_spec.append(("p0_decouverte", "FMC650_FLEET_P0_DECOUVERTE_v1.2_rev15.cfg", rev15_path, edits_p0))

    fw010210_fallback = CFGS_DIR / "FMC650_FLEET_P2_PRODUCTION_v1.2_fw010210.cfg"
    f15_anchor = ANCHOR_F15_PATH if ANCHOR_F15_PATH.exists() else (fw010210_fallback if fw010210_fallback.exists() else None)
    if f15_anchor is not None:
        _, f15_base, _ = cfg_tool.read_cfg(f15_anchor)
        edits_fw010210: dict[str, str] = {}
        apply_optimizations_and_40_params(edits_fw010210, f15_base, enable_trailercan=True)
        apply_fms_and_safety_v12(edits_fw010210, f15_base)
        apply_acquisition_p2(edits_fw010210)
        profiles_spec.append(("p2_fw010210", "FMC650_FLEET_P2_PRODUCTION_v1.2_fw010210.cfg", f15_anchor, edits_fw010210))

    results: list[dict[str, Any]] = []
    filt = preset_filter.lower().strip()
    for key, filename, anchor_path, edits in profiles_spec:
        if filt not in ("all", key, filename.lower()):
            continue
        out_cfg_path = CFGS_DIR / filename
        res = compile_cfg(anchor_path, out_cfg_path, edits)
        if not res["validation_report"]["validation_passed"]:
            raise RuntimeError(
                f"Validation errors in {filename}:\n" + "\n".join(res["validation_report"]["errors"])
            )
        if EXPORT_DIR is not None and EXPORT_DIR.exists() and (EXPORT_DIR / filename) != anchor_path:
            dl_path = EXPORT_DIR / filename
            dl_path.write_bytes(out_cfg_path.read_bytes())

        ver = res["validation_report"]["header"].get("ConfigurationVersion")
        print(
            f"[OK] {filename}: {res['modified_count']} params modified from base "
            f"(0 XML/Hex/Collection errors), {res['total_parameters']} total IDs, "
            f"ver={ver}, size={res['size_bytes']} B"
        )
        results.append(res)
    return results


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)

    if "--preset" in args:
        idx = args.index("--preset")
        preset_name = args[idx + 1] if idx + 1 < len(args) else "all"
        generate_all_fleet_profiles(preset_name)
        return

    edits: dict[int, str] = {}
    rest: list[str] = []
    schema_path = DEFAULT_SCHEMA
    xml_path = DEFAULT_XML
    i = 0
    while i < len(args):
        if args[i] == "--schema":
            schema_path = args[i + 1]
            i += 2
        elif args[i] == "--xml":
            xml_path = args[i + 1]
            i += 2
        elif "=" in args[i]:
            pid, _, v = args[i].partition("=")
            if not pid.isdigit():
                sys.exit(f"bad arg {args[i]!r}: expected id=value")
            edits[int(pid)] = v
            i += 1
        else:
            rest.append(args[i])
            i += 1

    if len(rest) < 2:
        sys.exit("Usage: make_cfg.py <reference.cfg> <out.cfg> [id=value ...] | make_cfg.py --preset all")
    ref_path, out_path = rest[0], rest[1]

    smap = load_schema_map(schema_path)
    header, params, _ = cfg_tool.read_cfg(ref_path)
    ref_ids = {int(k) for k in params}
    print(f"reference: {len(ref_ids)} params, header {header}")

    fails: list[int] = []
    for pid, v in sorted(edits.items()):
        if pid not in ref_ids:
            print(
                f"  [FAIL] id {pid}: not present in reference .cfg ({len(ref_ids)} params, "
                f"ConfigurationVersion={header.get('ConfigurationVersion')})"
            )
            fails.append(pid)
            continue
        row = synthesize_param_row(pid, schema_map=smap, xml_path=xml_path)
        for level, msg in check_value(pid, v, row, xml_path=xml_path):
            print(f"  [{level}] {msg}")
            if level == "FAIL":
                fails.append(pid)
    if fails:
        sys.exit(f"\nrefused (validation): ids {sorted(set(fails))}")

    res = compile_cfg(ref_path, out_path, edits, schema_path=schema_path, xml_path=xml_path)
    print(
        f"\n{out_path}: {res['total_parameters']} params, {res['size_bytes']} B gzip "
        f"({res['modified_count']} edited, sha256={res['sha256']})"
    )


if __name__ == "__main__":
    main()
