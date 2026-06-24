"""Integration test for the sandbox /health resources contract.

Pins the producer/consumer seam end to end: the real sandbox /health
handler must emit a `resources` object whose shape the agent's
SandboxClient.resources() parser consumes without drift. A plain unit
test mocks one side; this runs the actual handler over HTTP and rebuilds
the agent's SandboxResources from the live payload, so a future change to
the /health JSON shape fails here instead of at runtime on a real run.
"""

import os
from dataclasses import asdict

import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient

from config.constants import SandboxResources
from sandbox.api.health import register as register_health
from sandbox.sdk.manager import SessionManager

# The /health resources probe reads os.sched_getaffinity, which is
# Linux-only (the sandbox always runs on Linux). Skip the whole module on
# other platforms — there is nothing to probe to assert against.
pytestmark = pytest.mark.skipif(
    not hasattr(os, "sched_getaffinity"),
    reason="sched_getaffinity is Linux-only; the sandbox always runs on Linux",
)


@pytest.fixture
def health_app() -> web.Application:
    """Build a minimal aiohttp app with the real /health handler."""
    app = web.Application()
    app["sessions"] = SessionManager()
    register_health(app)
    return app


@pytest.fixture
async def client(health_app: web.Application, aiohttp_client) -> TestClient:
    """Create a test client for the health endpoint."""
    return await aiohttp_client(health_app)


def _parse_resources(payload: dict) -> SandboxResources:
    """Mirror agent SandboxClient.resources() — the consumer side.

    Kept in lockstep with autofyn/sandbox_client/client.py::resources so a
    drift in either the handler's output or the parser is caught here.
    """
    res = payload["resources"]
    return SandboxResources(
        kind=res["kind"],
        cpu_count=res["cpu_count"],
        mem_limit_bytes=res["mem_limit_bytes"],
    )


class TestHealthResourcesContract:
    """The real /health handler emits a parseable resources object."""

    @pytest.mark.asyncio
    async def test_health_includes_resources(self, client: TestClient) -> None:
        resp = await client.get("/health")
        assert resp.status == 200
        data = await resp.json()
        assert "resources" in data
        assert set(data["resources"]) == {"kind", "cpu_count", "mem_limit_bytes"}

    @pytest.mark.asyncio
    async def test_resources_round_trip_to_agent_model(self, client: TestClient) -> None:
        """The live payload parses into the agent's SandboxResources cleanly."""
        resp = await client.get("/health")
        data = await resp.json()

        resources = _parse_resources(data)
        # The probe ran on this Linux CI host: a real CPU count, and a
        # memory limit that is either a positive cgroup ceiling or None.
        assert resources.cpu_count >= 1
        assert resources.mem_limit_bytes is None or resources.mem_limit_bytes > 0
        # asdict round-trips back to exactly the emitted JSON shape.
        assert asdict(resources) == data["resources"]

    @pytest.mark.asyncio
    async def test_resources_cached_across_requests(self, client: TestClient) -> None:
        """Two calls return identical resources — the probe is cached once."""
        first = (await (await client.get("/health")).json())["resources"]
        second = (await (await client.get("/health")).json())["resources"]
        assert first == second
