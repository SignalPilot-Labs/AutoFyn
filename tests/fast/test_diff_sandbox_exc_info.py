"""Regression tests for missing exc_info=True in diff endpoint exception handlers.

When the sandbox diff operation raises, log.warning must include exc_info=True
so the full stack trace is captured. Without it, only the exception message is
logged, making diagnosis of sandbox connectivity issues impossible.

Fixes:
- endpoints/diff.py — diff_repo sandbox path
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI, HTTPException
from fastapi.routing import APIRoute

from endpoints.diff import register_diff_routes


def _make_server(client: MagicMock) -> MagicMock:
    """Create a minimal AgentServer stand-in."""
    pool = MagicMock()
    pool.get_client = MagicMock(return_value=client)
    server = MagicMock()
    server.pool = MagicMock(return_value=pool)
    return server


class TestDiffRepoSandboxExcInfo:
    """diff_repo must call log.warning with exc_info=True when sandbox fails."""

    @pytest.mark.asyncio
    async def test_sandbox_diff_logs_exc_info_on_failure(self) -> None:
        """When client.repo.diff() raises, log.warning includes exc_info=True."""
        client = MagicMock()
        client.repo.diff = AsyncMock(side_effect=RuntimeError("connection refused"))

        app = FastAPI()
        server = _make_server(client)
        register_diff_routes(app, server)

        # Get the registered route handler directly.
        route = next(r for r in app.routes if isinstance(r, APIRoute) and r.path == "/diff/repo")
        handler = route.endpoint

        with patch("endpoints.diff.log") as mock_log:
            with pytest.raises(HTTPException) as exc_info:
                await handler(
                    run_id="run-1",
                    branch="main",
                    base="main",
                    repo="org/repo",
                    token="tok",
                    source="sandbox",
                )

        assert exc_info.value.status_code == 502
        mock_log.warning.assert_called_once()
        call_kwargs = mock_log.warning.call_args[1]
        assert call_kwargs.get("exc_info") is True, (
            "log.warning must be called with exc_info=True to preserve the stack trace"
        )
