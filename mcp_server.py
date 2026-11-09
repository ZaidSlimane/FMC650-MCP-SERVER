"""Root Entrypoint for the Comprehensive FMC650 MCP Server (`fmc650-comprehensive-mcp`).

Usage:
    python mcp_server.py
    python -m fmc650_mcp_server.server
"""
from __future__ import annotations

from fmc650_mcp_server.server import main, mcp  # noqa: F401

if __name__ == "__main__":
    main()
