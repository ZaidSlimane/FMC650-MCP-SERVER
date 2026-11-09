#!/usr/bin/env python3
"""Read, write, and verify Teltonika .cfg configuration files for FMX6 (FMC650/FMX65).

Single source of truth for the .cfg binary/text container format:
- Container: deterministic single gzip member (mtime=0) wrapping a UTF-8 parameter stream (or plain UTF-8 text).
- Text grammar (verified byte-exact on re/cfgs/device_export_original.cfg):
    ConfigurationVersion:<v>;HwVersion:<hw>;Title:<title>;FmType:<fm>;SpecId:<n>;
    <id>:<value>;<id>:<value>;...
- Continuation rule: a new parameter starts only at `^\\d+:` whose integer ID is strictly
  greater than the previous ID; any semicolon-separated token without that shape is
  preserved as part of the previous value (e.g. PID 181334 value `0;10:FMC650DEMO`).

Usage:
  cfg_tool.py read   <file.cfg> <out.json>     # decompress + parse to JSON
  cfg_tool.py write  <in.json>  <out.cfg>      # rebuild deterministic gzip .cfg
  cfg_tool.py verify <file.cfg>                # parse -> rebuild text -> verify invariance
"""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any

HEADER_KEYS: tuple[str, ...] = (
    "ConfigurationVersion",
    "HwVersion",
    "Title",
    "FmType",
    "SpecId",
)
HEADER_RE = re.compile(r"^(" + "|".join(HEADER_KEYS) + r"):")
PARAM_RE = re.compile(r"^(\d+):(.*)$", re.S)


def parse_text(text: str) -> tuple[dict[str, str], dict[str, str]]:
    """Parse a decompressed .cfg text stream into (header_dict, params_str_key_dict)."""
    header: dict[str, str] = {}
    params: dict[str, str] = {}
    pos = 0
    for part in re.split(r";", text):
        if PARAM_RE.match(part):
            break
        if ":" in part:
            k, v = part.split(":", 1)
            if HEADER_RE.match(part):
                header[k] = v
            pos += len(part) + 1
    body = text[pos:]
    last: int | None = None
    for chunk in body.split(";"):
        m = PARAM_RE.match(chunk)
        if m and (last is None or int(m.group(1)) > last):
            last = int(m.group(1))
            params[m.group(1)] = m.group(2)
        elif chunk and last is not None:
            params[str(last)] += ";" + chunk
    return header, params


def build_text(header: dict[str, str], params: dict[Any, Any]) -> str:
    """Serialize header and parameter map into the canonical Teltonika .cfg text stream."""
    str_params = {str(k): str(v) for k, v in params.items()}
    head = "".join(f"{k}:{header[k]};" for k in HEADER_KEYS if k in header)
    body = "".join(f"{k}:{str_params[k]};" for k in sorted(str_params, key=int))
    return head + body


def read_cfg(path: str | Path) -> tuple[dict[str, str], dict[str, str], bytes]:
    """Read a gzip-compressed or plain-text .cfg file and return (header, params, raw_bytes)."""
    file_path = Path(path)
    raw_bytes = file_path.read_bytes()
    if raw_bytes[:2] == b"\x1f\x8b":
        text = gzip.decompress(raw_bytes).decode("utf-8")
    else:
        text = raw_bytes.decode("utf-8-sig")
    header, params = parse_text(text)
    return header, params, raw_bytes


def write_cfg(
    path: str | Path,
    header: dict[str, str],
    params: dict[Any, Any],
    reference_keys: set[int] | None = None,
) -> tuple[bytes, str]:
    """Build .cfg text, assert round-trip & anchor-set invariance, and write deterministic gzip (mtime=0)."""
    new_text = build_text(header, params)
    gen_header, gen_params = parse_text(new_text)

    expected_keys = reference_keys if reference_keys is not None else {int(k) for k in params}
    actual_keys = {int(k) for k in gen_params}
    if actual_keys != expected_keys:
        raise ValueError(
            f"Parameter key-set drift detected ({len(actual_keys)} vs {len(expected_keys)} IDs) — refusing to write."
        )
    if build_text(gen_header, gen_params) != new_text:
        raise ValueError("Round-trip .cfg text serialization drift detected — refusing to write.")

    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as fh:
        with gzip.GzipFile(fileobj=fh, mode="wb", mtime=0) as gz:
            gz.write(new_text.encode("utf-8"))

    gz_bytes = out_path.read_bytes()
    sha256_hex = hashlib.sha256(gz_bytes).hexdigest()
    return gz_bytes, sha256_hex


def verify_cfg(path: str | Path) -> dict[str, Any]:
    """Verify round-trip text identity and container metadata of a .cfg file."""
    header, params, raw_bytes = read_cfg(path)
    text = (
        gzip.decompress(raw_bytes).decode("utf-8")
        if raw_bytes[:2] == b"\x1f\x8b"
        else raw_bytes.decode("utf-8-sig")
    )
    rebuilt = build_text(header, params)
    return {
        "text_identical": rebuilt == text,
        "sha256_original": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "sha256_rebuilt": hashlib.sha256(rebuilt.encode("utf-8")).hexdigest(),
        "is_gzipped": raw_bytes[:2] == b"\x1f\x8b",
        "gzip_header_os_byte": raw_bytes[9] if len(raw_bytes) > 9 else None,
        "gzip_xfl": raw_bytes[8] if len(raw_bytes) > 8 else None,
        "parameter_count": len(params),
        "header": header,
    }


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "read":
        header, params, raw_bytes = read_cfg(sys.argv[2])
        text = (
            gzip.decompress(raw_bytes).decode("utf-8")
            if raw_bytes[:2] == b"\x1f\x8b"
            else raw_bytes.decode("utf-8-sig")
        )
        with open(sys.argv[3], "w", encoding="utf-8") as fh:
            json.dump(
                {
                    "header": header,
                    "params": params,
                    "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                },
                fh,
                indent=1,
            )
        print(f"params={len(params)} header={header}")
    elif cmd == "write":
        with open(sys.argv[2], encoding="utf-8") as fh:
            data = json.load(fh)
        gz_bytes, _ = write_cfg(sys.argv[3], data["header"], data["params"])
        print(f"wrote {sys.argv[3]} ({len(gz_bytes)} B gzip)")
    elif cmd == "verify":
        info = verify_cfg(sys.argv[2])
        print("text_identical:", info["text_identical"])
        print("sha256_original:", info["sha256_original"])
        print("sha256_rebuilt :", info["sha256_rebuilt"])
        print("gzip_header_os_byte:", info["gzip_header_os_byte"], "xfl:", info["gzip_xfl"])
    else:
        sys.exit(f"Unknown command {cmd!r}. Expected: read | write | verify")


if __name__ == "__main__":
    main()
