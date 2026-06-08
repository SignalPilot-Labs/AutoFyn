"""Regression tests for DockerLocalBackend stale-container reconcile.

A sandbox container that dies uncleanly (Docker crash, host reboot, OOM kill)
leaves its name claimed. The next start with the same name must reclaim it,
but must never remove a still-running container. These tests pin both halves.
"""

import os
from unittest.mock import AsyncMock, MagicMock, patch

import docker.errors
import pytest

from sandbox_client.backends.local_backend import DockerLocalBackend
from sandbox_client.models import SandboxStartError


def _make_backend() -> DockerLocalBackend:
    """Instantiate DockerLocalBackend with mocked Docker."""
    with patch("sandbox_client.backends.local_backend.docker.from_env", return_value=MagicMock()):
        with patch("sandbox_client.backends.local_backend.sandbox_config", return_value={"vm_timeout_sec": 30, "health_timeout_sec": 5}):
            with patch.dict(os.environ, {"AF_IMAGE_TAG": "test", "SANDBOX_INTERNAL_SECRET": "test-sandbox-secret"}):
                return DockerLocalBackend()


def _container_with_status(status: str) -> MagicMock:
    """Build a mock container reporting the given status."""
    container = MagicMock()
    container.status = status
    container.remove = MagicMock()
    return container


class TestReconcileStaleContainer:
    """Pre-flight reconcile of a name-colliding leftover container."""

    @pytest.mark.asyncio
    async def test_no_existing_container_is_noop(self) -> None:
        """Reconcile does nothing when no container holds the name."""
        backend = _make_backend()
        backend._docker.containers.get = MagicMock(
            side_effect=docker.errors.NotFound("missing")
        )

        await backend._reconcile_stale_container("autofyn-sandbox-key")

    @pytest.mark.asyncio
    async def test_exited_container_is_removed(self) -> None:
        """An exited leftover is force-removed so its name is freed."""
        backend = _make_backend()
        stale = _container_with_status("exited")
        backend._docker.containers.get = MagicMock(return_value=stale)

        await backend._reconcile_stale_container("autofyn-sandbox-key")

        stale.remove.assert_called_once_with(force=True)

    @pytest.mark.asyncio
    async def test_created_container_is_removed(self) -> None:
        """A created-but-never-started leftover is also removed."""
        backend = _make_backend()
        stale = _container_with_status("created")
        backend._docker.containers.get = MagicMock(return_value=stale)

        await backend._reconcile_stale_container("autofyn-sandbox-key")

        stale.remove.assert_called_once_with(force=True)

    @pytest.mark.asyncio
    async def test_running_container_is_not_removed(self) -> None:
        """A live container holding the name fails loud, never removed."""
        backend = _make_backend()
        live = _container_with_status("running")
        backend._docker.containers.get = MagicMock(return_value=live)

        with pytest.raises(SandboxStartError, match="refusing to remove a live container"):
            await backend._reconcile_stale_container("autofyn-sandbox-key")

        live.remove.assert_not_called()

    @pytest.mark.asyncio
    async def test_paused_container_is_not_removed(self) -> None:
        """A paused container is treated as live and never removed."""
        backend = _make_backend()
        live = _container_with_status("paused")
        backend._docker.containers.get = MagicMock(return_value=live)

        with pytest.raises(SandboxStartError):
            await backend._reconcile_stale_container("autofyn-sandbox-key")

        live.remove.assert_not_called()

    @pytest.mark.asyncio
    async def test_create_reconciles_before_run(self) -> None:
        """create() invokes reconcile before launching the start command."""
        backend = _make_backend()

        with patch.object(backend, "_reconcile_stale_container", new=AsyncMock()) as recon:
            with patch(
                "sandbox_client.backends.local_backend.asyncio.create_subprocess_shell",
                new=AsyncMock(side_effect=RuntimeError("stop after reconcile")),
            ):
                with pytest.raises(RuntimeError, match="stop after reconcile"):
                    await backend.create("key", None, "docker run ...")

        recon.assert_awaited_once_with("autofyn-sandbox-key")
