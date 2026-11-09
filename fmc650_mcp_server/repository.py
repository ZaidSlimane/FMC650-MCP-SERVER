"""Unified Knowledge, Diagnostic Playbook, XML, Graph, Flespi & Wialon Repository for FMC650 MCP Server.

Indexes 100% of data assets under `FMC650 MCP Server/`:
1. Tier 1: Compiled Configurator XML (`generated_FMC650_spec1_cfg4.43.1.0.xml`) & Merged Schema (`fmx65_03.01.01.Rev.15_schema.json`)
2. Tier 2: `.cfg` Creator Engine & Reference/Production `.cfg` Profiles (`CfgCreatorEngine`)
3. Tier 3: Knowledge Graphs (`graph_v3.json` and `graph.json`)
4. Tier 4: Flespi & Wialon Mappings (`flespi-parameters/`, `wialon-parameters/FMC650_00_UNIFIED_PARAMS.md`, `FMC650_TEST_TR84_UNIT_PROFILE.json`)
5. Tier 5: Subject-Indexed Diagnostic Playbooks (`diagnostic/00..06_*.md`) & `debugging-sessions/`
6. Tier 6: All 10 Official Teltonika Documentation Categories under `teltonika-docs/`
"""
from __future__ import annotations

import gzip
import json
from pathlib import Path
import re
from typing import Any, Dict, List, Optional, Set, Tuple
import networkx as nx

from fmc650_mcp_server.cfg_creator import (
    CfgCreatorEngine,
    SECRET_CREDENTIAL_PIDS,
    SERVER_ROOT,
)

ALL_KNOWLEDGE_DIRS = [
    "diagnostic",
    "debugging-sessions",
    "flespi-parameters",
    "wialon-parameters",
    "fmc650-reverse-engineered",
    "teltonika-docs",
    "teltonika-docs/Certification",
    "teltonika-docs/Configuration",
    "teltonika-docs/Data_Sending_Parameters_ID",
    "teltonika-docs/Firmware_Changelog",
    "teltonika-docs/manual",
    "teltonika-docs/Memberships",
    "teltonika-docs/Nomenclature_Classification_Codes",
    "teltonika-docs/Product_Change_Notifications",
    "teltonika-docs/Promotional_Material",
    "teltonika-docs/Tachograph_Solution",
]

TOP_LEVEL_SCAN_DIRS = [
    "diagnostic",
    "debugging-sessions",
    "flespi-parameters",
    "wialon-parameters",
    "fmc650-reverse-engineered",
    "teltonika-docs",
]

STOPWORDS: Set[str] = {
    "what", "which", "where", "when", "why", "how", "who", "whom", "whose",
    "does", "do", "did", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "can", "could", "should", "would", "will", "shall",
    "control", "controls", "controlled", "controlling", "configure", "configures",
    "configured", "configuration", "parameter", "parameters", "param", "params",
    "parametre", "parametres", "paramètre", "paramètres", "setting", "settings",
    "vehicle", "vehicule", "véhicule", "truck", "camion", "fmc650", "fmc",
    "teltonika", "device", "tracker", "explain", "explique", "expliquer",
    "simplement", "simply", "tell", "about", "give", "list", "show", "find",
    "the", "for", "and", "with", "from", "into", "onto", "that", "this",
    "these", "those", "all", "any", "some", "dans", "quel", "quelle",
    "quels", "quelles", "sont", "les", "des", "aux", "pour", "comment",
    "pourquoi", "est", "sur", "une", "par", "avec", "sans", "plus", "moins",
}

BILINGUAL_SYNONYMS: Dict[str, List[str]] = {
    "weight": ["weight", "load", "axle", "cargo", "trailer", "gross", "139", "13657", "89"],
    "weights": ["weight", "load", "axle", "cargo", "trailer", "gross", "139", "13657", "89"],
    "poids": ["weight", "load", "axle", "cargo", "trailer", "gross", "139", "13657"],
    "masse": ["weight", "load", "axle", "cargo", "139"],
    "load": ["load", "weight", "axle", "cargo", "13657"],
    "charge": ["load", "weight", "axle", "cargo", "13657"],
    "axle": ["axle", "load", "weight", "bogie", "89", "90", "91", "92", "13657"],
    "axles": ["axle", "load", "weight", "bogie", "89", "90", "91", "92", "13657"],
    "axels": ["axle", "load", "weight", "bogie", "89", "90", "91", "92", "13657"],
    "essieu": ["axle", "load", "weight", "bogie", "13657"],
    "essieux": ["axle", "load", "weight", "bogie", "13657"],
    "bogie": ["bogie", "tridem", "trailer", "airbag", "port 42", "13657", "wabco"],
    "tridem": ["bogie", "tridem", "trailer", "13657", "wabco"],
    "wabco": ["wabco", "tebs", "trailercan", "13657", "13810", "iso 11992", "can2"],
    "tabs": ["wabco", "tebs", "trailercan", "13657", "can2"],
    "tebs": ["wabco", "tebs", "trailercan", "13657", "13810", "can2"],
    "sitrak": ["sitrak", "sinotruk", "c7h", "traxon", "mc13", "can1", "139"],
    "c7h": ["sitrak", "sinotruk", "c7h", "6x4", "6x2", "ecas", "leaf", "spring"],
    "incline": ["incline", "slope", "hill", "pente", "incliné", "brake-bind", "levelling", "accelerometer", "fleet_weight_stable"],
    "inclined": ["incline", "slope", "hill", "pente", "incliné", "brake-bind", "levelling", "accelerometer", "fleet_weight_stable"],
    "inlined": ["incline", "slope", "inline", "uneven", "calibration", "13663", "13664", "fleet_weight_stable"],
    "slope": ["incline", "slope", "hill", "pente", "brake-bind", "levelling", "fleet_weight_stable"],
    "pente": ["incline", "slope", "hill", "pente", "brake-bind", "levelling", "fleet_weight_stable"],
    "silent": ["silent", "normal", "206", "208", "locked", "request", "pgn 59904", "pgn 65258"],
    "mode": ["mode", "silent", "normal", "206", "208"],
    "ignition": ["ignition", "101", "50000", "239", "din1"],
    "allumage": ["ignition", "101", "50000", "239"],
    "contact": ["ignition", "101", "50000", "239"],
    "movement": ["movement", "accelerometer", "100", "240"],
    "mouvement": ["movement", "accelerometer", "100", "240"],
    "sleep": ["sleep", "deep", "102", "103", "200"],
    "veille": ["sleep", "deep", "102", "103", "200"],
    "speed": ["speed", "overspeeding", "11100", "80", "24"],
    "vitesse": ["speed", "overspeeding", "11100", "80", "24"],
    "overspeed": ["overspeeding", "11100", "11101", "11102", "11103", "11104"],
    "overspeeding": ["overspeeding", "11100", "11101", "11102", "11103", "11104"],
    "survitesse": ["overspeeding", "11100", "11101", "11102", "11103", "11104"],
    "fuel": ["fuel", "lls", "adblue", "87", "86", "135"],
    "carburant": ["fuel", "lls", "adblue", "87", "86", "135"],
    "gasoil": ["fuel", "lls", "87"],
    "tachograph": ["tachograph", "tacho", "ddd", "k-line", "47500", "200", "209"],
    "chronotachygraphe": ["tachograph", "tacho", "ddd", "k-line", "47500"],
    "tachygraphe": ["tachograph", "tacho", "ddd", "k-line", "47500"],
    "tacho": ["tachograph", "tacho", "ddd", "k-line", "47500"],
    "odometer": ["odometer", "mileage", "216"],
    "odomètre": ["odometer", "mileage", "216"],
    "kilometrage": ["odometer", "mileage", "216"],
    "kilométrage": ["odometer", "mileage", "216"],
    "fraud": ["fraud", "theft", "loss", "fleet_fraud_alert", "fleet_trailer_loss_delta", "13810"],
    "theft": ["fraud", "theft", "loss", "fleet_fraud_alert", "fleet_trailer_loss_delta", "13810"],
    "vol": ["fraud", "theft", "loss", "fleet_fraud_alert", "fleet_trailer_loss_delta", "13810"],
}

FRONTMATTER_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n", re.DOTALL)


def _normalize_element_label(label: str) -> str:
    """Normalize an XML/Schema/AVL element label so 'Axle 1 Load -> Priority' matches 'Axle 1 load'."""
    s = label.lower().strip()
    if "->" in s:
        s = s.split("->", 1)[0].strip()
    s = re.sub(r"\s*\(field\s*\d+\)\s*$", "", s)
    s = re.sub(r"\s*:\s*(priority|operand|high\s*level|low\s*level|event\s*only|averaging\s*constant)\s*$", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s


class FMC650KnowledgeRepository:
    """In-memory singleton repository unifying XML, .cfg, Graphs, Flespi/Wialon, Diagnostic Playbooks, and Docs."""

    _instance: Optional["FMC650KnowledgeRepository"] = None

    @classmethod
    def get_instance(cls) -> "FMC650KnowledgeRepository":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.knowledge_root: Path = SERVER_ROOT
        self.cfg_engine = CfgCreatorEngine()
        self.collections = self.cfg_engine.collections
        self.xml_params = self.cfg_engine.xml_params
        self.schema_params = self.cfg_engine.schema_params
        self.io_bases: Dict[str, str] = self.cfg_engine.schema_data.get("io_bases", {})

        # Load Graph v3 and Graph v1
        self.graph_v3 = self._load_graph(
            self.knowledge_root / "graph-db" / "graph-v3" / "graph_v3.json"
        )
        self.graph_v1 = self._load_graph(
            self.knowledge_root / "graph-db" / "graph-v1" / "graph.json"
        )
        self.cfg_pid_avl_collisions: Set[int] = set()
        for src, _, edge in self.graph_v3.edges(data=True):
            if edge.get("relation") == "COLLIDES_INTEGER_ID_WITH" and str(src).startswith("cfg_pid:"):
                try:
                    self.cfg_pid_avl_collisions.add(int(str(src).split(":", 1)[1]))
                except ValueError:
                    continue

        # Build valid PID set across XML, schema.json, and reference .cfg
        self.all_valid_pids: Set[int] = set(self.xml_params.keys()) | {
            int(k) for k in self.schema_params.keys() if str(k).isdigit()
        }
        ref_cfg_path = self.cfg_engine._resolve_profile_path("device_export_original.cfg")
        self.factory_defaults: Dict[int, str] = {}
        if ref_cfg_path.is_file():
            _, self.factory_defaults, _ = self.cfg_engine._read_cfg_file(ref_cfg_path)
            self.all_valid_pids |= set(self.factory_defaults.keys())

        # Index all documentation files across the server root
        self.doc_files: List[Path] = self._discover_all_docs()

        # Index Wialon TR84 Unit Profile sensors (146 sensors) & Unified Flespi/Wialon table (1,161 params)
        self.wialon_tr84_sensors: List[Dict[str, Any]] = []
        self.wialon_sensors_by_id: Dict[int, Dict[str, Any]] = {}
        self.wialon_sensors_by_param: Dict[str, List[Dict[str, Any]]] = {}
        self._load_wialon_tr84_profile()

        # Index Flespi & Wialon mappings (strictly separating Configuration PIDs from Telemetry AVL IDs)
        self.flespi_wialon_by_pid: Dict[int, Dict[str, Any]] = {}
        self.flespi_wialon_by_avl: Dict[int, Dict[str, Any]] = {}
        self.flespi_wialon_by_key: Dict[str, Dict[str, Any]] = {}
        self.avl_by_norm_name: Dict[str, Dict[str, Any]] = {}
        self._index_telematics_mappings()
        self._index_unified_wialon_markdown()

    @staticmethod
    def _load_graph(path: Path) -> nx.MultiDiGraph:
        gz_path = path.with_name(path.name + ".gz")
        if path.is_file():
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        elif gz_path.is_file():
            with gzip.open(gz_path, "rt", encoding="utf-8") as f:
                data = json.load(f)
        else:
            return nx.MultiDiGraph()
        edge_key = "links" if "links" in data else "edges"
        return nx.node_link_graph(data, edges=edge_key)

    def _discover_all_docs(self) -> List[Path]:
        """Collect all readable documentation/data files across `FMC650 MCP Server/`."""
        docs: List[Path] = []
        allowed_exts = {".md", ".txt", ".csv", ".json", ".wlp"}
        for dname in TOP_LEVEL_SCAN_DIRS:
            folder = self.knowledge_root / dname
            if not folder.is_dir():
                continue
            for p in sorted(folder.rglob("*")):
                if not p.is_file():
                    continue
                if any(part in {"__pycache__", ".git", ".venv", "node_modules", "bin", "obj"} for part in p.parts):
                    continue
                if p.name == "fmx65_03.01.01.Rev.15_schema.json":
                    continue
                if p.suffix.lower() in allowed_exts:
                    docs.append(p)
        return docs

    def _load_wialon_tr84_profile(self) -> None:
        """Load the 146 Wialon sensors from `wialon-parameters/FMC650_TEST_TR84_UNIT_PROFILE.json`."""
        profile_path = self.knowledge_root / "wialon-parameters" / "FMC650_TEST_TR84_UNIT_PROFILE.json"
        if not profile_path.is_file():
            return
        try:
            data = json.loads(profile_path.read_text(encoding="utf-8", errors="replace"))
            for s in data.get("sensors", []):
                sid = int(s.get("id", 0))
                param_expr = str(s.get("p", "")).strip()
                entry = {
                    "sensor_id": sid,
                    "name": s.get("n"),
                    "type": s.get("t"),
                    "description": s.get("d"),
                    "unit": s.get("m"),
                    "parameter_expression": param_expr,
                    "calculation_table": s.get("tbl", []),
                }
                self.wialon_tr84_sensors.append(entry)
                if sid:
                    self.wialon_sensors_by_id[sid] = entry
                for tok in re.findall(r"[a-zA-Z0-9_]+", param_expr):
                    self.wialon_sensors_by_param.setdefault(tok.lower(), []).append(entry)
        except Exception:
            pass

    def _index_unified_wialon_markdown(self) -> None:
        """Parse `wialon-parameters/FMC650_00_UNIFIED_PARAMS.md` to enrich Path A / Path B keys & descriptions."""
        md_path = self.knowledge_root / "wialon-parameters" / "FMC650_00_UNIFIED_PARAMS.md"
        if not md_path.is_file():
            return
        try:
            for line in md_path.read_text(encoding="utf-8", errors="replace").splitlines():
                if not line.startswith("|") or "---" in line or "Flespi Parameter" in line:
                    continue
                parts = [c.strip() for c in line.strip("|").split("|")]
                if len(parts) < 8 or not parts[0].isdigit():
                    continue
                flespi_param = parts[1].strip("` ")
                val_type = parts[2].strip("` ")
                avl_str = parts[4].replace("`", "").strip()
                stream_key = parts[5].strip("` ")
                direct_keys = [k.strip("` ") for k in parts[6].split(",")]
                desc = parts[7].strip()

                avl_ids = [int(x) for x in re.findall(r"\b\d+\b", avl_str)]
                wialon_sensors = self.wialon_sensors_by_param.get(stream_key.lower(), [])

                info = {
                    "flespi_key": flespi_param,
                    "type": val_type,
                    "avl_ids": avl_ids,
                    "avl_id": avl_ids[0] if avl_ids else None,
                    "wialon_stream_key_path_a": stream_key,
                    "wialon_direct_keys_path_b": direct_keys,
                    "wialon_key": f"{stream_key} (Path A) / {', '.join(direct_keys[:2])} (Path B)",
                    "description": desc,
                    "wialon_tr84_sensors": wialon_sensors,
                    "source": "wialon-parameters/FMC650_00_UNIFIED_PARAMS.md",
                }
                self.flespi_wialon_by_key[flespi_param.lower()] = info
                self.flespi_wialon_by_key[stream_key.lower()] = info
                for aid in avl_ids:
                    if aid in self.flespi_wialon_by_avl:
                        existing = self.flespi_wialon_by_avl[aid]
                        existing.setdefault("wialon_stream_key_path_a", stream_key)
                        existing.setdefault("wialon_tr84_sensors", wialon_sensors)
                        existing.setdefault("description", desc)
                    else:
                        self.flespi_wialon_by_avl[aid] = info
        except Exception:
            pass

        # Also index all custom fleet_* and vhc_* Wialon sensors directly into flespi_wialon_by_key
        for param_key, sensors in self.wialon_sensors_by_param.items():
            if param_key not in self.flespi_wialon_by_key:
                self.flespi_wialon_by_key[param_key] = {
                    "flespi_key": param_key.replace("_", "."),
                    "wialon_stream_key_path_a": param_key,
                    "wialon_key": param_key,
                    "wialon_tr84_sensors": sensors,
                    "source": "wialon-parameters/FMC650_TEST_TR84_UNIT_PROFILE.json (Flespi tidj Weight Plugin)",
                }

    def _index_telematics_mappings(self) -> None:
        """Index Flespi & Wialon mappings from Graph v3 (`AvlTelemetryElement` & `GOVERNS_TELEMETRY`) + seeded tables."""
        for nid, ndata in self.graph_v3.nodes(data=True):
            if ndata.get("type") != "AvlTelemetryElement" or not str(nid).startswith("avl_id:"):
                continue
            try:
                aid = int(str(nid).split("avl_id:")[-1])
            except ValueError:
                continue

            el_name = str(ndata.get("name") or f"AVL {aid}")
            flespi_keys: List[str] = []
            wialon_keys: List[str] = []
            mapping_evidence: List[Dict[str, Any]] = []
            for _, tgt, edata in self.graph_v3.out_edges(nid, data=True):
                rel = edata.get("relation", "")
                stgt = str(tgt)
                if rel == "DECODED_AS_FLESPI_PARAM" and stgt.startswith("flespi_param:"):
                    fk = stgt.split("flespi_param:", 1)[1]
                    if fk not in flespi_keys:
                        flespi_keys.append(fk)
                    mapping_evidence.append(self._mapping_edge_evidence(rel, stgt, edata))
                elif rel in ("DIRECT_MAPS_TO_WIALON_IO", "STREAMS_TO_WIALON_KEY"):
                    wk = stgt.split(":")[-1]
                    if wk not in wialon_keys:
                        wialon_keys.append(wk)
                    mapping_evidence.append(self._mapping_edge_evidence(rel, stgt, edata))

            if not wialon_keys:
                wialon_keys.append(f"io_{aid}")

            el_lower = el_name.lower()
            if any(w in el_lower for w in ("weight", "load", "axle", "cargo")):
                preferred_fk = [k for k in flespi_keys if any(w in k for w in ("weight", "axle", "cargo", "load"))]
                if preferred_fk:
                    flespi_keys = preferred_fk

            entry = {
                "avl_id": aid,
                "name": el_name,
                "flespi_key": ", ".join(flespi_keys[:3]) if flespi_keys else None,
                "flespi_keys": flespi_keys,
                "wialon_key": ", ".join(wialon_keys[:2]),
                "wialon_keys": wialon_keys,
                "mapping_evidence": mapping_evidence,
                "source": "Graph v3 + flespi-parameters/02_FMC650_Telemetry_AVL_ID_to_Flespi_Parameters_Mapping.md",
            }
            self.flespi_wialon_by_avl[aid] = entry
            norm = _normalize_element_label(el_name)
            if norm:
                self.avl_by_norm_name.setdefault(norm, entry)
            for fk in flespi_keys:
                self.flespi_wialon_by_key.setdefault(fk.lower(), entry)
            for wk in wialon_keys:
                self.flespi_wialon_by_key.setdefault(wk.lower(), entry)

        for u, v, edata in self.graph_v3.edges(data=True):
            if edata.get("relation") != "GOVERNS_TELEMETRY":
                continue
            su, sv = str(u), str(v)
            if not sv.startswith("avl_id:"):
                continue
            try:
                aid = int(sv.split("avl_id:")[-1])
            except ValueError:
                continue
            avl_entry = self.flespi_wialon_by_avl.get(aid)
            if not avl_entry:
                continue
            if su.startswith("cfg_pid:"):
                try:
                    pid = int(su.split("cfg_pid:")[-1])
                    pid_entry = dict(avl_entry)
                    pid_entry["configuration_pid"] = pid
                    pid_entry["configuration_mapping_evidence"] = self._mapping_edge_evidence(
                        "GOVERNS_TELEMETRY", sv, edata
                    )
                    self.flespi_wialon_by_pid[pid] = pid_entry
                except ValueError:
                    pass
            elif su.startswith("cfg_ioblock:"):
                try:
                    base_pid = int(su.split("cfg_ioblock:")[-1])
                    for off in range(10):
                        if (base_pid + off) in self.all_valid_pids:
                            pid_entry = dict(avl_entry)
                            pid_entry["configuration_io_block"] = base_pid
                            pid_entry["configuration_mapping_evidence"] = self._mapping_edge_evidence(
                                "GOVERNS_TELEMETRY", sv, edata
                            )
                            self.flespi_wialon_by_pid.setdefault(base_pid + off, pid_entry)
                except ValueError:
                    pass

        # Seed authoritative FMS J1939 Axle 1..15 weight (PID 46100..46240 -> AVL ID 89..103)
        for axle_idx in range(1, 16):
            base_pid = 46090 + axle_idx * 10
            aid = 88 + axle_idx
            entry = self.flespi_wialon_by_avl.get(aid) or {
                "avl_id": aid,
                "name": f"Axle weight {axle_idx} (FMS J1939 PGN 65258)",
                "flespi_key": f"can.axle.weight.{axle_idx}",
                "flespi_keys": [f"can.axle.weight.{axle_idx}", "can.axle.weight"],
                "wialon_stream_key_path_a": f"can_axle_weight_{axle_idx}",
                "wialon_key": f"can_axle_weight_{axle_idx} / io_{aid}",
                "wialon_keys": [f"can_axle_weight_{axle_idx}", f"io_{aid}"],
                "source": "teltonika-docs/Data_Sending_Parameters_ID/02_fms-elements/fms-elements.md",
            }
            self.flespi_wialon_by_avl[aid] = entry
            for off in range(6):
                if (base_pid + off) in self.all_valid_pids:
                    self.flespi_wialon_by_pid[base_pid + off] = entry

        # FMS J1939 Combined vehicle weight (PID 46530..46534 -> AVL ID 139 -> total.vehicle.weight)
        fms_gcvw_entry = self.flespi_wialon_by_avl.get(139) or {
            "avl_id": 139,
            "name": "Gross Combination Vehicle Weight (FMS J1939 PGN 65134)",
            "flespi_key": "total.vehicle.weight",
            "flespi_keys": ["total.vehicle.weight"],
            "wialon_stream_key_path_a": "total_vhc_weight",
            "wialon_key": "total_vhc_weight / io_139",
            "wialon_keys": ["total_vhc_weight", "io_139"],
            "wialon_tr84_sensors": self.wialon_sensors_by_param.get("total_vhc_weight", []),
            "source": "teltonika-docs/Data_Sending_Parameters_ID/02_fms-elements/fms-elements.md",
        }
        self.flespi_wialon_by_avl[139] = fms_gcvw_entry
        for off in range(6):
            if (46530 + off) in self.all_valid_pids:
                self.flespi_wialon_by_pid[46530 + off] = fms_gcvw_entry

        # EV FMS Gross Combination Vehicle Weight (PID 90780..90784 -> AVL ID 10899)
        ev_gcvw_entry = {
            "avl_id": 10899,
            "name": "Gross Combination Vehicle Weight (EV FMS)",
            "flespi_key": "can.gross.combination.vehicle.weight",
            "flespi_keys": ["can.gross.combination.vehicle.weight", "total.vehicle.weight"],
            "wialon_stream_key_path_a": "can_gross_combination_vhc_weight",
            "wialon_key": "can_gross_combination_vhc_weight / io_10899",
            "wialon_keys": ["can_gross_combination_vhc_weight", "io_10899"],
            "source": "teltonika-docs/Data_Sending_Parameters_ID/14_ev-fms-elements/ev-fms-elements.md",
        }
        self.flespi_wialon_by_avl[10899] = ev_gcvw_entry
        for off in range(6):
            if (90780 + off) in self.all_valid_pids:
                self.flespi_wialon_by_pid[90780 + off] = ev_gcvw_entry

        # TrailerCAN WABCO TEBS E Weight & Pneumatic Blocks
        trailer_weight_blocks = [
            ([103060, 104670, 106280], 13657, "Axle Load Sum (#1/#2/#3) — WABCO TEBS E Port 42 Bogie Sum", "trailer.axle.load.sum", "trailer_axle_load_sum"),
            ([103110, 104720, 106330], 13662, "Axle Load Measured By Towed Vehicle (#1/#2/#3)", "trailer.towing.vehicle.axle.load", "trailer_towing_vhc_axle_load"),
            ([103120, 104730, 106340], 13663, "Axle Load Measured By External Scale (#1/#2/#3)", "trailer.scale.axle.load", "trailer_scale_axle_load"),
            ([103130], 13664, "Axle Load Calibration Data Load Level", "trailer.calibration.load.level.state.enum", "trailer_calibration_load_lvl_state_enum"),
            ([104590], 13810, "Pneumatic Supply Pressure (kPa)", "trailer.pneumatic.supply.pressure", "trailer_pneumatic_supply_press"),
            ([104230], 13774, "Vehicle Pneumatic Supply Status", "trailer.pneumatic.supply.state.enum", "trailer_pneumatic_supply_st_enum"),
            ([180510], 13413, "EBS Weight Load (Apache RS232)", "trailer.axle.load.sum", "trailer_axle_load_sum"),
        ]
        for base_list, aid, el_title, fk, wk_a in trailer_weight_blocks:
            tw_entry = {
                "avl_id": aid,
                "name": el_title,
                "flespi_key": fk,
                "flespi_keys": [fk] if fk else [],
                "wialon_stream_key_path_a": wk_a,
                "wialon_key": f"{wk_a} (Path A) / io_{aid} (Path B)",
                "wialon_keys": [wk_a, f"io_{aid}"],
                "wialon_tr84_sensors": self.wialon_sensors_by_param.get(wk_a.lower(), []),
                "source": "flespi-parameters/03_Complete_re_IOItem_Blocks_1357_Catalog.md + diagnostic/04_WABCO_TEBS_E_Bogie_Physics_and_Trailer_Parameters.md",
            }
            self.flespi_wialon_by_avl[aid] = tw_entry
            for bpid in base_list:
                for off in range(6):
                    if (bpid + off) in self.all_valid_pids:
                        self.flespi_wialon_by_pid[bpid + off] = tw_entry

        # Link remaining IO Configuration PIDs (>= 10000) to AVL Telemetry Elements
        for pid in self.all_valid_pids:
            if pid < 10000 or pid in self.flespi_wialon_by_pid:
                continue
            xname = self.xml_params.get(pid, {}).get("name")
            sname = self.schema_params.get(str(pid), {}).get("label") or self.schema_params.get(str(pid), {}).get("name")
            for raw_label in (xname, sname):
                if not raw_label:
                    continue
                norm = _normalize_element_label(raw_label)
                if norm and norm in self.avl_by_norm_name:
                    self.flespi_wialon_by_pid[pid] = self.avl_by_norm_name[norm]
                    break
                m_ax_w = re.match(r"^axle\s+(\d+)\s+weight$", norm)
                if m_ax_w:
                    reordered = f"axle weight {m_ax_w.group(1)}"
                    if reordered in self.avl_by_norm_name:
                        self.flespi_wialon_by_pid[pid] = self.avl_by_norm_name[reordered]
                        break
                alt_norm = norm.replace("weight", "load") if "weight" in norm else norm.replace("load", "weight")
                if alt_norm and alt_norm in self.avl_by_norm_name:
                    self.flespi_wialon_by_pid[pid] = self.avl_by_norm_name[alt_norm]
                    break

        # Manual CAN 00..69 (17000..17695 -> AVL 145..214) and Timestamp (47500 -> AVL 405)
        for idx in range(70):
            base_pid = 17000 + idx * 10
            avl_id = 145 + idx
            entry = {
                "pid_block": f"{base_pid}..{base_pid + 5}",
                "avl_id": avl_id,
                "name": f"Manual CAN {idx:02d}",
                "flespi_key": f"manual.can.{idx}",
                "flespi_keys": [f"manual.can.{idx}"],
                "wialon_key": f"io_{avl_id}",
                "wialon_keys": [f"io_{avl_id}"],
                "source": "flespi-parameters/02_FMC650_Telemetry_AVL_ID_to_Flespi_Parameters_Mapping.md",
            }
            for off in range(6):
                self.flespi_wialon_by_pid[base_pid + off] = entry
            self.flespi_wialon_by_avl[avl_id] = entry
            self.flespi_wialon_by_key[f"manual.can.{idx}"] = entry
            self.flespi_wialon_by_key[f"io_{avl_id}"] = entry

        ts_entry = {
            "pid_block": "47500..47509",
            "avl_id": 405,
            "name": "Timestamp (High-Resolution Sub-Second Event Timestamp)",
            "flespi_key": "timestamp",
            "flespi_keys": ["timestamp"],
            "wialon_key": "io_405",
            "wialon_keys": ["io_405"],
            "source": "flespi-parameters/02_FMC650_Telemetry_AVL_ID_to_Flespi_Parameters_Mapping.md",
        }
        for off in range(10):
            if (47500 + off) in self.all_valid_pids:
                self.flespi_wialon_by_pid[47500 + off] = ts_entry
        self.flespi_wialon_by_avl[405] = ts_entry
        self.flespi_wialon_by_key["timestamp"] = ts_entry
        self.flespi_wialon_by_key["io_405"] = ts_entry

    @staticmethod
    def _mapping_edge_evidence(relation: str, target: str, edge: Dict[str, Any]) -> Dict[str, Any]:
        """Return the assertion citation and confidence without implying verification."""
        return {
            "relation": relation,
            "target": target,
            "source_file": edge.get("source_file"),
            "source_location": edge.get("source_location"),
            "confidence": edge.get("confidence"),
            "confidence_score": edge.get("confidence_score"),
            "verification_status": edge.get("verification_status"),
            "rationale": edge.get("rationale") or edge.get("notes"),
            "legacy_provenance": edge.get("legacy_provenance"),
        }

    def reconcile_parameter(self, pid: int) -> Dict[str, Any]:
        """Reconcile a PID across Tier 1 XML, Tier 2 .cfg default, Tier 3 Graph/schema, and Tier 4 Flespi/Wialon."""
        xmeta = self.xml_params.get(pid, {})
        xattr = xmeta.get("attrib", {})
        srow = self.schema_params.get(str(pid), {})

        xml_name = xmeta.get("name")
        schema_name = srow.get("label") or srow.get("name")
        io_base_label = self.io_bases.get(str((pid // 10) * 10))
        canonical_name = xml_name or schema_name or f"Parameter {pid}"

        dirty_doc_conflict: Optional[str] = None
        if 17000 <= pid <= 17695:
            slot = (pid - 17000) // 10
            dirty_doc_conflict = (
                f"Raw Markdown manuals mislabeled PID {pid} as 'Manual CAN {slot:02d}', "
                f"whereas authoritative FMC650 compiler XML defines 17000..17695 as Manual CAN Request #{slot} "
                f"('{xml_name}', Validate='{xattr.get('Validate')}')."
            )
        elif 47500 <= pid <= 47509:
            dirty_doc_conflict = (
                f"Raw Markdown manuals mislabeled PID {pid} under 'ISF Ignition Status (47500)', "
                f"whereas authoritative FMC650 compiler XML defines 47500..47509 as Tachograph Data -> "
                f"'{xml_name}' (Collection='{xattr.get('Collection')}', where '0' is illegal on 47500)."
            )
        elif xml_name and schema_name and xml_name != schema_name and not xml_name.endswith(f"-> {schema_name}"):
            dirty_doc_conflict = (
                f"Schema JSON labeled PID {pid} as '{schema_name}', "
                f"whereas authoritative FMC650 compiler XML defines it as '{xml_name}'."
            )
        elif io_base_label and xml_name and "->" in xml_name and not xml_name.startswith(io_base_label):
            dirty_doc_conflict = (
                f"Secondary io_bases table labeled base {(pid // 10) * 10} as '{io_base_label}', "
                f"whereas authoritative FMC650 compiler XML defines PID {pid} as '{xml_name}'."
            )

        coll_name = xattr.get("Collection")
        enum_values = self.collections.get(coll_name, {}) if coll_name else (srow.get("values") or {})
        param_type = xattr.get("ParameterType") or srow.get("type") or ("Byte (Enum)" if coll_name else "Unknown")
        if pid in (205, 207) and xattr.get("Max") == "1000":
            param_type = "UInt16 (XML quirk: declared Byte with Min=50..Max=1000)"

        min_val = xattr.get("Min") if "Min" in xattr else srow.get("min")
        max_val = xattr.get("Max") if "Max" in xattr else srow.get("max")
        validate_expr = xattr.get("Validate") or srow.get("validate")
        default_val = xattr.get("Default") if "Default" in xattr else srow.get("default")
        factory_cfg_val = self.factory_defaults.get(pid)
        if pid in SECRET_CREDENTIAL_PIDS and factory_cfg_val:
            factory_cfg_val = "[REDACTED_SECRET]"

        avl_id: Optional[str] = None
        collides_with_avl_id: Optional[str] = None
        io_block_id: Optional[int] = xmeta.get("io_id")
        graph_edges: List[Dict[str, str]] = []
        for nid in (
            f"cfg_def:spec:1:schema:4.43.1.0:hw:FMC650_1:pid:{pid}",
            f"cfg_pid:{pid}",
            f"cfg_ioblock:{(pid // 10) * 10}" if pid >= 10000 else f"cfg_ioblock:{pid}",
        ):
            if self.graph_v3.has_node(nid):
                for _, tgt, edata in self.graph_v3.out_edges(nid, data=True):
                    rel = edata.get("relation", "RELATED_TO")
                    stgt = str(tgt)
                    graph_edges.append({"relation": rel, "target": stgt})
                    if rel == "GOVERNS_TELEMETRY" and stgt.startswith("avl_id:"):
                        avl_id = stgt.split("avl_id:")[-1]
                    elif rel == "COLLIDES_INTEGER_ID_WITH" and stgt.startswith("avl_id:"):
                        collides_with_avl_id = stgt.split("avl_id:")[-1]
                    elif rel == "PART_OF_IO_BLOCK" and stgt.startswith("cfg_ioblock:"):
                        try:
                            io_block_id = int(stgt.split(":")[-1])
                        except ValueError:
                            pass

        fw_map = self.flespi_wialon_by_pid.get(pid)
        if not fw_map and io_block_id:
            fw_map = self.flespi_wialon_by_pid.get(io_block_id)
        if fw_map and fw_map.get("avl_id"):
            avl_id = str(fw_map["avl_id"])

        return {
            "pid": pid,
            "canonical_name": canonical_name,
            "xml_name": xml_name,
            "schema_json_name": schema_name,
            "dirty_doc_conflict": dirty_doc_conflict,
            "parameter_type": param_type,
            "min": min_val,
            "max": max_val,
            "validate_rule": validate_expr,
            "collection_name": coll_name,
            "enum_values": enum_values,
            "xml_default": default_val,
            "factory_cfg_default": factory_cfg_val,
            "io_block_id": io_block_id,
            "avl_id": avl_id,
            "collides_with_avl_id": collides_with_avl_id,
            "ui_section": " > ".join(srow.get("section", [])) if srow.get("section") else None,
            "flespi_wialon_mapping": fw_map,
            "graph_edges": graph_edges[:15],
            "present_in_4_43_1_0_anchor": pid in self.factory_defaults,
        }

    @staticmethod
    def _mask_secrets_in_text(text: str) -> str:
        """Mask any raw SECRET_CREDENTIAL_PIDS assignments in documentation snippets."""
        def _repl(m: re.Match) -> str:
            p = int(m.group(1))
            if p in SECRET_CREDENTIAL_PIDS:
                return f"{p}:[REDACTED_SECRET]"
            return m.group(0)
        return re.sub(r"\b(\d{2,5}):([^\s,;]+)", _repl, text)

    @staticmethod
    def _search_term_pattern(term: str) -> re.Pattern[str]:
        """Match ordinary terms literally and compact alphanumeric IDs across separators."""
        lowered = term.lower()
        parts = re.findall(r"[a-z]+|\d+", lowered)
        compact = re.sub(r"[^a-z0-9]", "", lowered)
        if len(parts) > 1 and "".join(parts) == compact:
            pattern = r"[ \t:=_.-]*".join(re.escape(part) for part in parts)
            return re.compile(pattern, flags=re.IGNORECASE)
        return re.compile(re.escape(term), flags=re.IGNORECASE)

    def _build_evidence_snippets(
        self,
        lines: List[str],
        terms: List[str],
        max_snippets: int = 3,
        radius: int = 2,
        max_chars: int = 1400,
    ) -> List[Dict[str, Any]]:
        """Build short line-numbered excerpts around actual body matches."""
        patterns = [(term, self._search_term_pattern(term)) for term in dict.fromkeys(terms)]
        candidates: List[Tuple[int, int]] = []
        for index, line in enumerate(lines):
            score = sum(1 for _, pattern in patterns if pattern.search(line))
            if score:
                candidates.append((score, index))
        candidates.sort(key=lambda item: (-item[0], item[1]))

        snippets: List[Dict[str, Any]] = []
        used_lines: Set[int] = set()
        line_budget = max(80, max_chars // (2 * radius + 1) - 12)

        def clip_line(line: str) -> str:
            if len(line) <= line_budget:
                return line
            match_starts = [m.start() for _, pattern in patterns if (m := pattern.search(line))]
            start = max(0, (min(match_starts) if match_starts else 0) - line_budget // 4)
            end = min(len(line), start + line_budget)
            prefix = "…" if start else ""
            suffix = "…" if end < len(line) else ""
            return prefix + line[start:end] + suffix

        for score, index in candidates:
            start = max(0, index - radius)
            end = min(len(lines), index + radius + 1)
            if any(line_num in used_lines for line_num in range(start, end)):
                continue
            excerpt = "\n".join(
                f"{line_num + 1}: {clip_line(lines[line_num])}"
                for line_num in range(start, end)
            )
            snippets.append({
                "start_line": start + 1,
                "end_line": end,
                "match_score": score,
                "text": self._mask_secrets_in_text(excerpt)[:max_chars],
            })
            used_lines.update(range(start, end))
            if len(snippets) >= max_snippets:
                break
        return snippets

    def search_all_knowledge(
        self,
        query: str,
        domains: Optional[List[str]] = None,
        top_k: int = 12,
        require_body_match: bool = False,
    ) -> Dict[str, Any]:
        """Search across all server knowledge directories (including `diagnostic/` and `teltonika-docs/`)."""
        raw_words = [w.lower() for w in re.findall(r"[\w.-]+", query) if len(w) > 1]
        meaningful_words = [w for w in raw_words if w not in STOPWORDS]
        if not meaningful_words:
            meaningful_words = raw_words

        expanded_words = list(dict.fromkeys(meaningful_words))
        for w in meaningful_words:
            for syn in BILINGUAL_SYNONYMS.get(w, []):
                if syn not in expanded_words:
                    expanded_words.append(syn)

        domain_filter = {d.lower() for d in domains} if domains else None
        scored_hits: List[Tuple[float, Dict[str, Any]]] = []

        for doc_path in self.doc_files:
            rel_path = str(doc_path.relative_to(self.knowledge_root)).replace("\\", "/")
            parts = rel_path.split("/")
            top_dir = parts[0]
            sub_dir = parts[1] if len(parts) > 1 else ""
            if domain_filter:
                if top_dir.lower() not in domain_filter and sub_dir.lower() not in domain_filter and f"{top_dir}/{sub_dir}".lower() not in domain_filter:
                    continue

            try:
                raw_text = doc_path.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            body = FRONTMATTER_RE.sub("", raw_text)
            term_patterns = [(w, self._search_term_pattern(w)) for w in expanded_words]
            body_matched_terms = [w for w, pattern in term_patterns if pattern.search(body)]
            path_matched_terms = [w for w, pattern in term_patterns if pattern.search(rel_path)]
            matched_terms = [w for w in expanded_words if w in body_matched_terms or w in path_matched_terms]
            if not matched_terms or (require_body_match and not body_matched_terms):
                continue

            score = 0.0
            for w in body_matched_terms:
                is_primary = w in meaningful_words
                score += 5.0 if is_primary else 2.0
            for w in path_matched_terms:
                if w not in body_matched_terms:
                    is_primary = w in meaningful_words
                    score += 1.5 if is_primary else 0.5

            # Boost diagnostic playbooks & authoritative mapping docs
            if top_dir == "diagnostic":
                score += 4.5
            elif top_dir in ("flespi-parameters", "wialon-parameters") or sub_dir in ("Configuration", "Data_Sending_Parameters_ID"):
                score += 2.5
            elif top_dir == "debugging-sessions" and any(k in meaningful_words for k in ("save", "failed", "cfg", "17000", "47500", "debug", "ignition", "flapping")):
                score += 3.5

            evidence_snippets = self._build_evidence_snippets(body.splitlines(), body_matched_terms)
            match_type = "content" if body_matched_terms else "path_only"
            snippet = "\n\n".join(s["text"] for s in evidence_snippets)
            if match_type == "path_only":
                snippet = "Filename matched; no matching text was found in the document body."
            scored_hits.append((
                score,
                {
                    "path": rel_path,
                    "directory": f"{top_dir}/{sub_dir}" if top_dir == "teltonika-docs" and sub_dir else top_dir,
                    "score": round(score, 2),
                    "matched_terms": matched_terms,
                    "body_matched_terms": body_matched_terms,
                    "path_matched_terms": path_matched_terms,
                    "match_type": match_type,
                    "snippet": snippet,
                    "evidence_snippets": evidence_snippets,
                },
            ))

        scored_hits.sort(key=lambda item: item[0], reverse=True)
        top_results = [item[1] for item in scored_hits[:top_k]]

        reconciled_pids: Dict[int, Dict[str, Any]] = {}
        for tok in re.findall(r"\b(\d{3,6})\b", query):
            p = int(tok)
            if p in self.all_valid_pids:
                reconciled_pids[p] = self.reconcile_parameter(p)

        return {
            "query": query,
            "expanded_terms": expanded_words,
            "total_matching_files": len(scored_hits),
            "results": top_results,
            "reconciled_query_pids": reconciled_pids,
        }

    def search_debugging_sessions(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """Find historical session analyses and return line-numbered evidence from matching files."""
        limit = max(1, min(int(top_k), 10))
        search = self.search_all_knowledge(
            query=query,
            domains=["debugging-sessions"],
            top_k=limit,
            require_body_match=True,
        )
        results: List[Dict[str, Any]] = []

        for hit in search.get("results", []):
            path = str(hit.get("path", ""))
            doc_path = (self.knowledge_root / path).resolve()
            if not str(doc_path).startswith(str(self.knowledge_root.resolve())) or not doc_path.is_file():
                continue
            results.append({
                "path": path,
                "evidence_type": "raw_session_log" if doc_path.suffix.lower() == ".txt" else "session_analysis",
                "match_type": "content",
                "score": hit.get("score"),
                "matched_terms": hit.get("body_matched_terms", []),
                "evidence_snippets": hit.get("evidence_snippets", []),
            })

        return {
            "query": query,
            "evidence_scope": "Historical FMC650 observations; findings describe these recorded cases and may not generalize to every device or firmware.",
            "total_matching_files": search.get("total_matching_files", 0),
            "results": results,
            "reconciled_query_pids": search.get("reconciled_query_pids", {}),
        }

    def get_full_document_section(
        self,
        doc_path: str,
        heading_or_line_range: Optional[str] = None,
        offset: int = 0,
        max_chars: int = 12000,
    ) -> Dict[str, Any]:
        """Read a document section from `FMC650 MCP Server/` with safe pagination and secret masking."""
        safe_max = min(max(500, max_chars), 12000)
        safe_offset = max(0, int(offset))
        cand = (self.knowledge_root / doc_path).resolve()
        if not str(cand).startswith(str(self.knowledge_root.resolve())) or not cand.is_file():
            # Also try under teltonika-docs/<doc_path>
            cand_td = (self.knowledge_root / "teltonika-docs" / doc_path).resolve()
            if str(cand_td).startswith(str(self.knowledge_root.resolve())) and cand_td.is_file():
                cand = cand_td
            else:
                matches = [p for p in self.doc_files if doc_path.lower() in str(p).replace("\\", "/").lower()]
                if not matches:
                    return {"error": f"Document '{doc_path}' not found in FMC650 MCP Server."}
                cand = matches[0]

        raw_text = cand.read_text(encoding="utf-8", errors="replace")
        target_text = raw_text

        if heading_or_line_range:
            m_lines = re.match(r"^L?(\d+)\s*-\s*L?(\d+)$", heading_or_line_range.strip(), flags=re.IGNORECASE)
            if m_lines:
                start_l, end_l = int(m_lines.group(1)), int(m_lines.group(2))
                all_lines = raw_text.splitlines()
                if start_l < 1 or end_l < start_l or end_l > len(all_lines):
                    return {
                        "error": f"Invalid line range '{heading_or_line_range}' for a {len(all_lines)}-line document.",
                        "path": str(cand.relative_to(self.knowledge_root)).replace("\\", "/"),
                        "total_lines": len(all_lines),
                    }
                target_text = "\n".join(all_lines[start_l - 1:end_l])
            else:
                sections = re.split(r"(?=^#{1,3}\s+)", raw_text, flags=re.MULTILINE)
                hq = heading_or_line_range.lower()
                matched_secs = [s for s in sections if hq in s.splitlines()[0].lower()] if sections else []
                if matched_secs:
                    target_text = "\n".join(matched_secs)
                else:
                    headings = [
                        section.splitlines()[0].strip()
                        for section in sections
                        if section.splitlines() and re.match(r"^#{1,3}\s+", section.splitlines()[0])
                    ]
                    return {
                        "error": f"Heading '{heading_or_line_range}' was not found in the document.",
                        "path": str(cand.relative_to(self.knowledge_root)).replace("\\", "/"),
                        "available_headings": headings[:40],
                    }

        masked = self._mask_secrets_in_text(target_text)
        total_len = len(masked)
        sliced = masked[safe_offset: safe_offset + safe_max]
        next_offset = (safe_offset + safe_max) if (safe_offset + safe_max) < total_len else None

        return {
            "path": str(cand.relative_to(self.knowledge_root)).replace("\\", "/"),
            "total_chars": total_len,
            "offset": safe_offset,
            "returned_chars": len(sliced),
            "has_more": next_offset is not None,
            "next_offset": next_offset,
            "content": sliced,
        }

    def list_io_block_siblings(
        self,
        io_block_or_pid: int,
        profile_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Return all sibling parameters of an IO block using XML io_id grouping and current .cfg values."""
        xmeta = self.xml_params.get(io_block_or_pid, {})
        base_io_id = xmeta.get("io_id")
        if base_io_id is None:
            cand_10 = (io_block_or_pid // 10) * 10
            if cand_10 in self.xml_params and self.xml_params[cand_10].get("io_id") == cand_10:
                base_io_id = cand_10
            else:
                base_io_id = io_block_or_pid

        sibling_pids = sorted(
            p for p, info in self.xml_params.items() if info.get("io_id") == base_io_id
        )
        if not sibling_pids:
            sibling_pids = [p for p in range(base_io_id, base_io_id + 10) if p in self.all_valid_pids]

        cfg_values: Dict[int, Any] = {}
        if profile_name:
            try:
                inspected = self.cfg_engine.inspect_profile(profile_name, pids=sibling_pids)
                cfg_values = {item["pid"]: item["value"] for item in inspected.get("parameters", [])}
            except Exception:
                pass

        siblings = []
        for spid in sibling_pids:
            rec = self.reconcile_parameter(spid)
            if spid in cfg_values:
                rec["profile_value"] = cfg_values[spid]
            siblings.append(rec)

        return {
            "requested_pid": io_block_or_pid,
            "io_block_base_id": base_io_id,
            "io_block_name": self.xml_params.get(base_io_id, {}).get("io_name") or self.io_bases.get(str(base_io_id), f"IO_{base_io_id}"),
            "sibling_count": len(siblings),
            "siblings": siblings,
        }
