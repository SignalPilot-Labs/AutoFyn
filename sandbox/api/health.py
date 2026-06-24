"""Health check HTTP handler for the sandbox."""

from dataclasses import asdict

from aiohttp import web

from config.constants import SandboxResources
from constants import SANDBOX_IMAGE_TAG, SANDBOX_PROTOCOL_VERSION
from sdk.manager import SessionManager
from shared.resources import probe_resources

# The allocation is fixed for the sandbox's lifetime, so probe once and
# cache — but lazily, on first request, not at import (the probe reads
# Linux-only syscalls and must not run when this module is merely imported
# on another platform, e.g. during host-side tests).
_resources: SandboxResources | None = None


def _cached_resources() -> SandboxResources:
    """Return the probed allocation, computing it once on first call."""
    global _resources
    if _resources is None:
        _resources = probe_resources()
    return _resources


async def handle_health(request: web.Request) -> web.Response:
    """Return health status with active session count and protocol info."""
    sessions: SessionManager = request.app["sessions"]
    return web.json_response({
        "status": "healthy",
        "active_sessions": sessions.active_count(),
        "protocol_version": SANDBOX_PROTOCOL_VERSION,
        "image_tag": SANDBOX_IMAGE_TAG,
        "resources": asdict(_cached_resources()),
    })


async def handle_heartbeat(request: web.Request) -> web.Response:
    """Acknowledge a heartbeat ping from the connector."""
    return web.json_response({"ok": True})


def register(app: web.Application) -> None:
    """Attach /health and /heartbeat routes to the aiohttp app."""
    app.router.add_get("/health", handle_health)
    app.router.add_get("/heartbeat", handle_heartbeat)
