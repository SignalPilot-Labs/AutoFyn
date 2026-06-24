"""Regression tests for sandbox-lost (stale handle) classification.

When a remote sandbox's overlay vanishes (Slurm job died on a network
drop), git commands fail with ESTALE. Two things must hold:

1. A spawn-time OSError from create_subprocess_exec becomes a failed
   CmdResult, not an unhandled exception that crashes the request with a
   raw traceback.
2. fail() classifies a stale-handle stderr as a distinct 503 with a clear
   "resume to reallocate" message, not a generic 500.
"""

from unittest.mock import patch

import pytest
from aiohttp import web

from constants import SANDBOX_LOST_MSG
from models import CmdResult
from shared.subprocess import fail, run_cmd


class TestSubprocessSandboxLost:
    """Spawn OSError is captured and stale handles classify as 503."""

    @pytest.mark.asyncio
    async def test_spawn_oserror_becomes_failed_cmdresult(self) -> None:
        """A stale-handle OSError at spawn time returns a failed CmdResult."""
        err = OSError(116, "Stale file handle")

        async def fake_create_subprocess(*args, **kwargs):  # type: ignore[no-untyped-def]
            raise err

        with patch("asyncio.create_subprocess_exec", side_effect=fake_create_subprocess):
            result = await run_cmd(["git", "status"], "/home/agentuser/repo", 5)

        assert result.exit_code == -1
        assert "stale file handle" in result.stderr.lower()

    def test_fail_classifies_stale_handle_as_503(self) -> None:
        """fail() raises 503 with the sandbox-lost message on a stale handle."""
        result = CmdResult(
            stdout="",
            stderr="[Errno 116] Stale file handle: '/home/agentuser/repo'",
            exit_code=-1,
        )

        with pytest.raises(web.HTTPServiceUnavailable) as exc_info:
            fail(result, "git branch --show-current")

        body = exc_info.value.body
        assert body is not None
        assert SANDBOX_LOST_MSG in body.decode()

    def test_fail_other_error_stays_500(self) -> None:
        """A non-stale-handle failure still raises 500, not 503."""
        result = CmdResult(stdout="", stderr="fatal: not a git repository", exit_code=128)

        with pytest.raises(web.HTTPInternalServerError):
            fail(result, "git status")

    def test_fail_noop_on_success(self) -> None:
        """fail() does nothing for a successful command."""
        fail(CmdResult(stdout="ok", stderr="", exit_code=0), "git status")
