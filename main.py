"""Vercel & ASGI FastAPI entrypoint for the Comprehensive FMC650 MCP Server."""
from fmc650_mcp_server.api import app

__all__ = ["app"]
