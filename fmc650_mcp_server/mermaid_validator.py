"""Deterministic Mermaid Diagram Validator & Auto-Repairer."""
from __future__ import annotations

import re
from typing import List, Tuple

ALLOWED_HEADERS = (
    "flowchart TD",
    "flowchart LR",
    "graph TD",
    "graph LR",
    "sequenceDiagram",
    "stateDiagram-v2",
    "stateDiagram",
    "classDiagram",
    "erDiagram",
    "xychart-beta",
)


def validate_and_repair_mermaid(code: str) -> Tuple[bool, str, List[str]]:
    """Validate and auto-repair Mermaid diagram code.

    Returns:
        (is_valid, repaired_code, warnings_or_errors)
    """
    notes: List[str] = []
    if not code or not code.strip():
        return False, "", ["Mermaid diagram code is empty."]

    cleaned = code.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:mermaid)?\s*\r?\n", "", cleaned)
        cleaned = re.sub(r"\r?\n```\s*$", "", cleaned)

    if re.search(r"<br\s*/?>", cleaned, flags=re.IGNORECASE):
        cleaned = re.sub(r"<br\s*/?>", " - ", cleaned, flags=re.IGNORECASE)
        notes.append("Replaced raw <br/> HTML tags with ' - '.")

    if re.search(r"</?[a-zA-Z][^>]*>", cleaned):
        cleaned = re.sub(r"</?[a-zA-Z][^>]*>", "", cleaned)
        notes.append("Stripped unsupported raw HTML tags from Mermaid code.")

    lines = [ln.rstrip() for ln in cleaned.splitlines() if ln.strip()]
    if not lines:
        return False, "", ["Mermaid diagram has no non-empty lines."]

    first = lines[0].strip()
    if first in ("flowchart TB", "flowchart BT", "graph TB", "graph BT"):
        lines[0] = "flowchart TD"
        first = "flowchart TD"
        notes.append("Normalized flowchart TB/BT header to 'flowchart TD'.")

    if not any(first.startswith(h) for h in ALLOWED_HEADERS):
        return (
            False,
            "\n".join(lines),
            [f"Unsupported Mermaid diagram header '{first}'. Allowed: {ALLOWED_HEADERS}."],
        )

    def _quote_bracket_label(match: re.Match) -> str:
        node_id = match.group(1)
        label = match.group(2)
        if label.startswith('"') and label.endswith('"'):
            return match.group(0)
        if any(ch in label for ch in ("(", ")", ":", "/", "[", "]")):
            safe_label = label.replace('"', "'")
            notes.append(f"Auto-quoted special characters in node label for '{node_id}'.")
            return f'{node_id}["{safe_label}"]'
        return match.group(0)

    repaired_lines: List[str] = [lines[0]]
    block_balance = 0
    for ln in lines[1:]:
        stripped = ln.strip()
        if re.match(r"^(?:subgraph|rect|alt|opt|loop|par|critical)\b", stripped):
            block_balance += 1
        elif stripped == "end":
            block_balance -= 1

        if first.startswith(("flowchart", "graph")):
            ln = re.sub(r"\b([A-Za-z0-9_]+)\[([^\]\"\n]+)\]", _quote_bracket_label, ln)
        repaired_lines.append(ln)

    while block_balance > 0:
        repaired_lines.append("    end")
        block_balance -= 1
        notes.append("Appended missing 'end' to balance block structure.")

    if block_balance < 0:
        return False, "\n".join(repaired_lines), ["Unbalanced 'end' statements in Mermaid diagram."]

    if len(repaired_lines) < 2:
        return False, "\n".join(repaired_lines), ["Mermaid diagram contains only a header with no body."]

    return True, "\n".join(repaired_lines), notes
