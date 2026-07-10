"""Per-round credential acquisition: pick a healthy credential, inject it, park if none."""

import asyncio
import logging
from datetime import datetime, timezone

from db.connection import get_session_factory
from db.constants import (
    CLAUDE_TOKEN_INDEX_KEY,
    CREDENTIAL_WAIT_POLL_SECONDS,
    PROVIDER_ANTHROPIC,
    RUN_STATUS_RATE_LIMITED,
    RUN_STATUS_RUNNING,
)
from db.models import Run
from sandbox_client.client import SandboxClient
from common.broker import CredentialBroker, WaitDirective, credential_id
from utils import db
from utils.constants import ENV_KEY_CLAUDE_TOKEN
from utils.db_logging import log_audit

log = logging.getLogger("lifecycle.credentials")


async def acquire_and_inject(sandbox: SandboxClient, run_id: str) -> str:
    """Acquire a healthy credential for this round and inject it into the sandbox.

    Parks the run (status rate_limited) until a credential is free, then injects
    the token and returns its credential_id so the caller can report exhaustion.
    """
    parked = False
    while True:
        async with get_session_factory()() as s:
            broker = CredentialBroker(s)
            tokens = await broker.read_claude_tokens()
            if not tokens:
                raise RuntimeError("no Claude credentials configured")
            ids = [credential_id(PROVIDER_ANTHROPIC, t) for t in tokens]
            result = await broker.acquire(PROVIDER_ANTHROPIC, ids, CLAUDE_TOKEN_INDEX_KEY)
            await s.commit()

        if not isinstance(result, WaitDirective):
            if parked:
                await db.update_run_status(run_id, RUN_STATUS_RUNNING)
            await sandbox.env.set({ENV_KEY_CLAUDE_TOKEN: tokens[result.index]})
            return result.credential_id

        if not parked:
            parked = True
            await db.update_run_status(run_id, RUN_STATUS_RATE_LIMITED)
            await log_audit(run_id, "credentials_exhausted_waiting", {
                "wait_until": result.wait_until.isoformat(),
                "reason": result.reason,
            })
        log.info("[%s] all credentials rate-limited, waiting", run_id[:8])
        await asyncio.sleep(CREDENTIAL_WAIT_POLL_SECONDS)


async def report_round_outcome(run_id: str, cred_id: str) -> None:
    """Cool down this round's credential if the round hit a rate limit.

    The runner persists rate_limit_resets_at on the run; a future value means
    the credential is rate-limited until then.
    """
    async with get_session_factory()() as s:
        run = await s.get(Run, run_id)
        if run is None or not run.rate_limit_resets_at:
            return
        reset_dt = datetime.fromtimestamp(run.rate_limit_resets_at, tz=timezone.utc)
        if reset_dt <= datetime.now(timezone.utc):
            return
        await CredentialBroker(s).report_exhausted(cred_id, reset_dt)
        await s.commit()
