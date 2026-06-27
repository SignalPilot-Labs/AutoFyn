"""Shared subprocess helpers for the sandbox.

Generic command execution, git/gh wrappers with retry, and the fail-fast
helper that raises HTTP 500. Used by repo operations and any other module
that needs to run subprocesses.
"""

import asyncio
import json
import logging
import os
import subprocess

from aiohttp import web

from constants import (
    RETRY_BASE_DELAY_SEC,
    RETRY_MAX_ATTEMPTS,
    RETRY_TRANSIENT_PATTERNS,
    SANDBOX_LOST_MSG,
    SANDBOX_LOST_PATTERN,
    SECRET_REDACT_MASK,
    STDERR_DISPLAY_LIMIT,
)
from models import CmdResult

log = logging.getLogger("sandbox.subprocess")

_SECRET_ENV_KEYS: tuple[str, ...] = ("GIT_TOKEN", "GH_TOKEN")


def scrub_secrets(text: str) -> str:
    """Replace git/gh token values with a redaction mask.

    Reads os.environ at call time so it picks up tokens injected via
    POST /env after server startup.
    """
    scrubbed = text
    for key in _SECRET_ENV_KEYS:
        value = os.environ.get(key)
        if value:
            scrubbed = scrubbed.replace(value, SECRET_REDACT_MASK)
    return scrubbed


async def _exec(
    args: list[str], cwd: str, timeout: int, env: dict[str, str] | None,
) -> CmdResult:
    """Spawn a subprocess and capture its output.

    `env` fully replaces the child environment when not None (callers that
    want an overlay must pass {**os.environ, ...}). A spawn-time OSError
    (e.g. ESTALE — a stale handle on `cwd` after a remote sandbox's overlay
    vanished) is turned into a failed CmdResult rather than propagated, so
    the OS message lands in stderr and the fail() handler can classify it
    into a clean error instead of crashing the request with a raw traceback.
    """
    proc: asyncio.subprocess.Process | None = None
    try:
        proc = await asyncio.create_subprocess_exec(
            *args, cwd=cwd, env=env,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        return CmdResult(
            stdout=(stdout or b"").decode(),
            stderr=(stderr or b"").decode(),
            exit_code=proc.returncode if proc.returncode is not None else -1,
        )
    except asyncio.TimeoutError:
        if proc:
            proc.kill()
            await proc.wait()
        return CmdResult(stdout="", stderr="timed out", exit_code=-1)
    except OSError as exc:
        return CmdResult(stdout="", stderr=str(exc), exit_code=-1)


async def run_cmd(args: list[str], cwd: str, timeout: int) -> CmdResult:
    """Run a subprocess inheriting the sandbox process env."""
    return await _exec(args, cwd, timeout, None)


async def run_with_retry(cmd: list[str], cwd: str, timeout: int) -> CmdResult:
    """Run a command with exponential backoff on transient failures."""
    result = CmdResult(stdout="", stderr="", exit_code=-1)
    for attempt in range(RETRY_MAX_ATTEMPTS):
        result = await run_cmd(cmd, cwd, timeout)
        if result.exit_code == 0:
            return result
        if not any(p in result.stderr.lower() for p in RETRY_TRANSIENT_PATTERNS):
            return result
        if attempt < RETRY_MAX_ATTEMPTS - 1:
            delay = RETRY_BASE_DELAY_SEC * (2 ** attempt)
            log.warning(
                "%s: transient error, retry %d/%d in %.0fs",
                cmd[0], attempt + 1, RETRY_MAX_ATTEMPTS, delay,
            )
            await asyncio.sleep(delay)
    return result


async def git(args: list[str], timeout: int, cwd: str) -> CmdResult:
    """Run `git <args>` with retry on transient network errors."""
    return await run_with_retry(["git"] + args, cwd, timeout)


async def gh(args: list[str], timeout: int, cwd: str) -> CmdResult:
    """Run `gh <args>` with retry on transient network errors."""
    return await run_with_retry(["gh"] + args, cwd, timeout)


async def git_indexed(
    args: list[str], timeout: int, cwd: str, index_file: str,
) -> CmdResult:
    """Run `git <args>` with GIT_INDEX_FILE pointed at a throwaway index.

    Used by the live diff to stage the working tree (`git add -A`) into a
    disposable index so untracked files appear in `git diff --cached`
    without ever mutating the repo's real index. No retry — these are local
    diff/index ops, not network operations, and a non-zero exit (e.g. diff
    exit code 1 = "differences found") must be returned to the caller, not
    retried.
    """
    env = {**os.environ, "GIT_INDEX_FILE": index_file}
    return await _exec(["git"] + args, cwd, timeout, env)


def _raise_sandbox_lost(label: str, stderr: str) -> None:
    """Raise a distinct 503 when the sandbox filesystem has vanished.

    A stale-handle failure means the remote sandbox's overlay is gone (the
    Slurm job died, e.g. on a network drop), so retrying or reporting a
    generic command error is misleading. Surface a clear, actionable cause
    that maps to "resume to reallocate" instead of a raw OSError traceback.
    """
    log.error("%s failed — sandbox lost: %s", label, stderr)
    body = json.dumps({
        "error": SANDBOX_LOST_MSG,
        "sandbox_lost": True,
        "label": label,
        "stderr": stderr,
    })
    raise web.HTTPServiceUnavailable(text=body, content_type="application/json")


def fail(result: CmdResult, label: str) -> None:
    """Raise an HTTP error if the command failed.

    A vanished sandbox filesystem (stale handle) raises a distinct 503 with
    a clear cause; every other failure raises 500. Stderr goes into the JSON
    body (not the HTTP reason header) because aiohttp rejects reason values
    containing newlines.
    """
    if result.exit_code == 0:
        return
    stderr = scrub_secrets(result.stderr.strip())[:STDERR_DISPLAY_LIMIT]
    if SANDBOX_LOST_PATTERN in stderr.lower():
        _raise_sandbox_lost(label, stderr)
    log.error("%s failed (exit=%d): %s", label, result.exit_code, stderr)
    body = json.dumps({
        "error": f"{label} failed",
        "exit_code": result.exit_code,
        "stderr": stderr,
    })
    raise web.HTTPInternalServerError(
        text=body,
        content_type="application/json",
    )
