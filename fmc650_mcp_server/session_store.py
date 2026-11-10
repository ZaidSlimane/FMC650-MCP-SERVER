"""SQLite Session & Conversation Store for the Comprehensive FMC650 MCP Server."""
from __future__ import annotations

from contextlib import closing
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sqlite3
import tempfile
from typing import Any, Dict, List, Optional
import uuid

SERVER_ROOT = Path(os.environ.get("FMC650_SERVER_ROOT") or Path(__file__).resolve().parents[1]).resolve()
if os.environ.get("VERCEL"):
    DEFAULT_DB_PATH = Path(tempfile.gettempdir()) / "fmc650_mcp" / "conversations_test.db"
else:
    DEFAULT_DB_PATH = SERVER_ROOT / "graph-db" / "data" / "conversations_test.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS conversations (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    context TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS messages (
    id TEXT PRIMARY KEY,
    conversation_id TEXT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    metadata TEXT,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS workflow_contexts (
    conversation_id TEXT PRIMARY KEY REFERENCES conversations(id) ON DELETE CASCADE,
    state TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_messages_conversation ON messages(conversation_id, created_at);
"""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _connect() -> sqlite3.Connection:
    path = Path(os.environ.get("CONVERSATIONS_DB_PATH") or DEFAULT_DB_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    return conn


def _message_dict(row: sqlite3.Row) -> Dict[str, Any]:
    msg = dict(row)
    msg["metadata"] = json.loads(msg["metadata"]) if msg.get("metadata") else None
    return msg


def create_conversation(title: str, context: str = "FMC650 MCP Server") -> Dict[str, Any]:
    now = _now()
    first = next((line.strip() for line in (title or "").splitlines() if line.strip()), "") or "FMC650 Engineering Session"
    conversation = {
        "id": uuid.uuid4().hex,
        "title": first if len(first) <= 80 else first[:79].rstrip() + "…",
        "context": context or "FMC650 MCP Server",
        "created_at": now,
        "updated_at": now,
    }
    with closing(_connect()) as conn, conn:
        conn.execute(
            "INSERT INTO conversations (id, title, context, created_at, updated_at) "
            "VALUES (:id, :title, :context, :created_at, :updated_at)",
            conversation,
        )
    return conversation


def list_conversations() -> List[Dict[str, Any]]:
    with closing(_connect()) as conn:
        rows = conn.execute("SELECT * FROM conversations ORDER BY updated_at DESC").fetchall()
    return [dict(r) for r in rows]


def get_conversation(conversation_id: str) -> Optional[Dict[str, Any]]:
    with closing(_connect()) as conn:
        row = conn.execute("SELECT * FROM conversations WHERE id = ?", (conversation_id,)).fetchone()
        if row is None:
            return None
        messages = conn.execute(
            "SELECT * FROM messages WHERE conversation_id = ? ORDER BY created_at, rowid",
            (conversation_id,),
        ).fetchall()
    return {**dict(row), "messages": [_message_dict(m) for m in messages]}


def add_message(
    conversation_id: str,
    role: str,
    content: str,
    metadata: Optional[Dict[str, Any]] = None,
) -> Optional[Dict[str, Any]]:
    now = _now()
    message = {
        "id": uuid.uuid4().hex,
        "conversation_id": conversation_id,
        "role": role,
        "content": content,
        "metadata": json.dumps(metadata, ensure_ascii=False) if metadata is not None else None,
        "created_at": now,
    }
    with closing(_connect()) as conn, conn:
        updated = conn.execute(
            "UPDATE conversations SET updated_at = ? WHERE id = ?",
            (now, conversation_id),
        )
        if updated.rowcount == 0:
            return None
        conn.execute(
            "INSERT INTO messages (id, conversation_id, role, content, metadata, created_at) "
            "VALUES (:id, :conversation_id, :role, :content, :metadata, :created_at)",
            message,
        )
    return {**message, "metadata": metadata}


def delete_conversation(conversation_id: str) -> bool:
    with closing(_connect()) as conn, conn:
        deleted = conn.execute("DELETE FROM conversations WHERE id = ?", (conversation_id,))
    return deleted.rowcount > 0
