"""Script-Backed .cfg Creation, Diffing & XML Validation Engine for FMC650 MCP Server.

Wraps `fmc650-reverse-engineered/tools/cfg_tool.py` and `make_cfg.py` with
secret masking, profile diffing, XML enum decoding, and deterministic gzipped
`.cfg` compilation.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import sys
from typing import Any, Dict, List, Optional, Tuple

from fmc650_mcp_server.schemas import CompiledCfgArtifact

SERVER_ROOT = Path(os.environ.get("FMC650_SERVER_ROOT") or Path(__file__).resolve().parents[1]).resolve()
RE_ROOT = SERVER_ROOT / "fmc650-reverse-engineered"
RE_TOOLS_DIR = RE_ROOT / "tools"
RE_CFGS_DIR = (RE_ROOT / "cfgs") if (RE_ROOT / "cfgs").exists() else (RE_ROOT / "re" / "cfgs")
RE_DIR = RE_ROOT / "re"
GENERATED_CFGS_DIR = Path(
    os.environ.get("FMC650_GENERATED_CFGS_DIR") or (Path(__file__).resolve().parent / "generated_cfgs")
).resolve()


def _rel_path(path: Path) -> str:
    """Return a clean repository-relative POSIX path without leaking host filesystem paths."""
    try:
        return path.resolve().relative_to(SERVER_ROOT).as_posix()
    except ValueError:
        return path.name

if str(RE_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(RE_TOOLS_DIR))

import cfg_tool  # type: ignore  # noqa: E402
import make_cfg  # type: ignore  # noqa: E402

DEFAULT_XML_PATH = str(RE_DIR / "generated_FMC650_spec1_cfg4.43.1.0.xml")
DEFAULT_SCHEMA_PATH = str(RE_DIR / "fmx65_03.01.01.Rev.15_schema.json")

# Secret credential PIDs that must be masked when inspecting .cfg files
SECRET_CREDENTIAL_PIDS = {10, 11, 12, 2002, 2003, 2005, 2006, 2008, 13004}


class CfgCreatorEngine:
    """First-class .cfg inspection, diffing, validation, and compilation engine."""

    def __init__(
        self,
        xml_path: str = DEFAULT_XML_PATH,
        schema_path: str = DEFAULT_SCHEMA_PATH,
    ):
        self.xml_path = xml_path
        self.schema_path = schema_path
        GENERATED_CFGS_DIR.mkdir(parents=True, exist_ok=True)
        self.collections, self.xml_params = make_cfg.load_xml_constraints(self.xml_path)
        self.schema_data: Dict[str, Any] = make_cfg.load_schema_data(self.schema_path)
        self.schema_int_map: Dict[int, Dict[str, Any]] = make_cfg.load_schema_map(self.schema_path)
        self.schema_params: Dict[str, Dict[str, Any]] = {str(k): v for k, v in self.schema_int_map.items()}

    def _resolve_profile_path(self, profile_name_or_path: str) -> Path:
        """Resolve a .cfg profile name or path across cfgs/, re/, and generated_cfgs/."""
        cand = Path(profile_name_or_path)
        if cand.is_file():
            return cand

        base = os.path.basename(profile_name_or_path)
        base_with_ext = base if base.endswith(".cfg") else f"{base}.cfg"

        search_dirs = [RE_CFGS_DIR, RE_DIR, RE_ROOT, GENERATED_CFGS_DIR]
        for d in search_dirs:
            for candidate_name in (base, base_with_ext):
                p = d / candidate_name
                if p.is_file():
                    return p

        lower_q = profile_name_or_path.lower()
        for d in search_dirs:
            if not d.is_dir():
                continue
            for cfg_file in sorted(d.glob("*.cfg")):
                if lower_q in cfg_file.name.lower():
                    return cfg_file

        raise FileNotFoundError(f"Could not find .cfg profile matching '{profile_name_or_path}'.")

    @staticmethod
    def _read_cfg_file(path: Path) -> Tuple[Dict[str, str], Dict[int, str], bytes]:
        """Delegate .cfg reading to cfg_tool.read_cfg and normalize parameter keys to int."""
        header, raw_params, raw_bytes = cfg_tool.read_cfg(path)
        params: Dict[int, str] = {int(k): v for k, v in raw_params.items() if str(k).isdigit()}
        return header, params, raw_bytes

    def list_profiles(self) -> List[Dict[str, Any]]:
        """List all available .cfg profiles in cfgs/, re/, and generated_cfgs/."""
        results: List[Dict[str, Any]] = []
        seen_paths = set()
        for folder in (RE_CFGS_DIR, RE_DIR, RE_ROOT, GENERATED_CFGS_DIR):
            if not folder.is_dir():
                continue
            for p in sorted(folder.glob("*.cfg")):
                if p.resolve() in seen_paths:
                    continue
                seen_paths.add(p.resolve())
                try:
                    header, params, raw_bytes = self._read_cfg_file(p)
                    results.append({
                        "filename": p.name,
                        "path": _rel_path(p),
                        "size_bytes": len(raw_bytes),
                        "is_gzipped": raw_bytes[:2] == b"\x1f\x8b",
                        "sha256": hashlib.sha256(raw_bytes).hexdigest(),
                        "parameter_count": len(params),
                        "header": header,
                    })
                except Exception as exc:
                    results.append({
                        "filename": p.name,
                        "path": _rel_path(p),
                        "error": str(exc),
                    })
        return results

    def inspect_profile(
        self,
        profile_name_or_path: str = "FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg",
        pids: Optional[List[int]] = None,
        filter_non_default: bool = False,
    ) -> Dict[str, Any]:
        """Inspect a .cfg profile with secret blinding, XML enum decoding, and factory default diffing."""
        path = self._resolve_profile_path(profile_name_or_path)
        header, params, raw_bytes = self._read_cfg_file(path)

        factory_params: Dict[int, str] = {}
        factory_path = RE_CFGS_DIR / "device_export_original.cfg"
        if factory_path.is_file():
            _, factory_params, _ = self._read_cfg_file(factory_path)

        target_pids = pids if pids is not None else sorted(params.keys())
        items: List[Dict[str, Any]] = []

        for pid in target_pids:
            val = params.get(pid)
            f_val = factory_params.get(pid)
            if filter_non_default and pids is None and val == f_val:
                continue

            is_secret = pid in SECRET_CREDENTIAL_PIDS
            masked_val = "[REDACTED_SECRET]" if (is_secret and val) else val
            xmeta = self.xml_params.get(pid, {})
            attr = xmeta.get("attrib", {})
            coll_name = attr.get("Collection")
            enum_map = self.collections.get(coll_name, {}) if coll_name else {}
            decoded_enum = enum_map.get(str(val)) if (val is not None and not is_secret) else None
            row = make_cfg.synthesize_param_row(pid, schema_map=self.schema_int_map, xml_path=self.xml_path) or {}

            items.append({
                "pid": pid,
                "name": xmeta.get("name") or row.get("label") or row.get("name") or f"PID_{pid}",
                "value": masked_val,
                "factory_default": "[REDACTED_SECRET]" if (is_secret and f_val) else f_val,
                "is_modified_from_factory": val != f_val,
                "decoded_enum": decoded_enum,
                "xml_type": attr.get("ParameterType") or row.get("type"),
                "xml_collection": coll_name,
                "xml_validate": attr.get("Validate") or row.get("validate"),
            })

        return {
            "filename": path.name,
            "path": _rel_path(path),
            "sha256": hashlib.sha256(raw_bytes).hexdigest(),
            "header": header,
            "total_parameters": len(params),
            "returned_count": len(items),
            "parameters": items if len(items) <= 250 else items[:250],
            "truncated": len(items) > 250,
        }

    def diff_profiles(self, profile_a: str, profile_b: str) -> Dict[str, Any]:
        """Compute a structured parameter-by-parameter diff between two .cfg profiles."""
        path_a = self._resolve_profile_path(profile_a)
        path_b = self._resolve_profile_path(profile_b)
        header_a, params_a, _ = self._read_cfg_file(path_a)
        header_b, params_b, _ = self._read_cfg_file(path_b)

        all_pids = sorted(set(params_a.keys()) | set(params_b.keys()))
        differences: List[Dict[str, Any]] = []

        for pid in all_pids:
            va = params_a.get(pid)
            vb = params_b.get(pid)
            if va == vb:
                continue

            is_secret = pid in SECRET_CREDENTIAL_PIDS
            masked_a = "[REDACTED_SECRET]" if (is_secret and va) else va
            masked_b = "[REDACTED_SECRET]" if (is_secret and vb) else vb

            xmeta = self.xml_params.get(pid, {})
            attr = xmeta.get("attrib", {})
            coll_name = attr.get("Collection")
            enum_map = self.collections.get(coll_name, {}) if coll_name else {}
            srow = self.schema_int_map.get(pid, {})

            differences.append({
                "pid": pid,
                "name": xmeta.get("name") or srow.get("label") or srow.get("name") or f"PID_{pid}",
                "value_in_a": masked_a,
                "enum_in_a": enum_map.get(str(va)) if (va is not None and not is_secret) else None,
                "value_in_b": masked_b,
                "enum_in_b": enum_map.get(str(vb)) if (vb is not None and not is_secret) else None,
            })

        return {
            "profile_a": path_a.name,
            "profile_b": path_b.name,
            "header_a": header_a,
            "header_b": header_b,
            "total_differences": len(differences),
            "differences": differences[:300],
            "truncated": len(differences) > 300,
        }

    def validate_edits(
        self,
        base_profile: str,
        proposed_edits: Dict[int, str],
    ) -> Dict[str, Any]:
        """Delegate batch edit validation to make_cfg.validate_cfg_edits with secret masking."""
        path = self._resolve_profile_path(base_profile)
        header, anchor_params, _ = self._read_cfg_file(path)
        report = make_cfg.validate_cfg_edits(
            base_params=anchor_params,
            header=header,
            edits=proposed_edits,
            schema_map=self.schema_int_map,
            xml_path=self.xml_path,
            base_name=path.name,
        )
        for item in report["details"]:
            pid = int(item["pid"])
            if pid in SECRET_CREDENTIAL_PIDS:
                if "current_in_anchor" in item:
                    item["current_in_anchor"] = "[REDACTED_SECRET]"
                item["proposed"] = "[REDACTED_SECRET]"
        return report

    def create_cfg(
        self,
        base_profile: str,
        proposed_edits: Dict[int, str],
        output_filename: Optional[str] = None,
    ) -> CompiledCfgArtifact:
        """Delegate validation and deterministic gzip .cfg compilation to make_cfg.compile_cfg."""
        path = self._resolve_profile_path(base_profile)
        out_path: Optional[Path] = None
        if output_filename:
            safe_name = os.path.basename(output_filename)
            if not safe_name.endswith(".cfg"):
                safe_name += ".cfg"
            out_path = GENERATED_CFGS_DIR / safe_name

        res = make_cfg.compile_cfg(
            ref_path=path,
            out_path=out_path,
            edits=proposed_edits,
            schema_path=self.schema_path,
            xml_path=self.xml_path,
        )
        val_report = res["validation_report"]
        sanitized_edits = {
            str(k): ("[REDACTED_SECRET]" if int(k) in SECRET_CREDENTIAL_PIDS else str(v))
            for k, v in proposed_edits.items()
        }

        return CompiledCfgArtifact(
            base_profile=path.name,
            output_path=res["output_path"],
            sha256=res["sha256"],
            total_parameters=res["total_parameters"],
            modified_count=res["modified_count"],
            validation_passed=val_report["validation_passed"],
            validation_errors=val_report["errors"],
            applied_edits=sanitized_edits,
        )
