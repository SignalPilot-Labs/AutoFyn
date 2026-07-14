"""Per-round credential acquisition: pick a healthy credential, inject it, park if none.

The run's model decides which tokens are eligible (a Claude run can only use
Anthropic tokens, a GPT-5.6 run only OpenRouter tokens), and the broker rotates
over that eligible set. The provider is a property of the selected token, so the
injected env is built from the selection — native OAuth token for Anthropic, or
OpenRouter gateway routing — not from a provider locked onto the run.
See docs/providers.md.
"""

import asyncio
import logging
from datetime import datetime, timezone

from db.connection import get_session_factory
from db.constants import (
    CLAUDE_TOKEN_INDEX_KEY,
    CREDENTIAL_WAIT_POLL_SECONDS,
    RUN_STATUS_RATE_LIMITED,
    RUN_STATUS_RUNNING,
)
from db.models import Run
from sandbox_client.client import SandboxClient
from common.broker import AllRateLimited, CredentialBroker
from common.constants import (
    ENV_ANTHROPIC_API_KEY,
    ENV_ANTHROPIC_AUTH_TOKEN,
    ENV_ANTHROPIC_BASE_URL,
    ENV_CLAUDE_OAUTH_TOKEN,
    OPENROUTER_BASE_URL,
    PROVIDER_ANTHROPIC,
    PROVIDER_OPENROUTER,
    openrouter_model_env,
    rotation_key_for,
)
from common.models import Token
from utils import db
from utils.db_logging import log_audit

log = logging.getLogger("lifecycle.credentials")


def _provider_env(token: Token, model: str) -> dict[str, str]:
    """Build the SDK credential env for the selected token, keyed on its provider.

    Fails loudly on an unknown provider rather than injecting a partial env
    that would silently route to the wrong place.
    """
    if token.provider == PROVIDER_ANTHROPIC:
        return {ENV_CLAUDE_OAUTH_TOKEN: token.value}
    if token.provider == PROVIDER_OPENROUTER:
        # Point the SDK at OpenRouter, auth with the OpenRouter key, and blank
        # ANTHROPIC_API_KEY so it never falls back to a native Anthropic key
        # that would bypass the gateway. Model overrides route the SDK tiers.
        return {
            ENV_ANTHROPIC_BASE_URL: OPENROUTER_BASE_URL,
            ENV_ANTHROPIC_AUTH_TOKEN: token.value,
            ENV_ANTHROPIC_API_KEY: "",
            **openrouter_model_env(model),
        }
    raise ValueError(f"cannot build credential env for unknown provider '{token.provider}'")


async def acquire_and_inject(sandbox: SandboxClient, run_id: str, model: str, provider: str) -> str:
    """Acquire a healthy credential for the run's provider and inject it.

    The run's provider decides the eligible token set; the broker rotates over
    that set and returns the selected token, whose provider drives the injected
    env (model supplies the OpenRouter tier overrides). Parks the run (status
    rate_limited) until a credential is free, then returns its credential_id so
    the caller can report exhaustion.
    """
    rotation_key = rotation_key_for(provider, CLAUDE_TOKEN_INDEX_KEY)
    parked = False
    while True:
        async with get_session_factory()() as s:
            broker = CredentialBroker(s)
            eligible: list[Token] = [
                t for t in await broker.read_pool() if t.provider == provider
            ]
            if not eligible:
                raise RuntimeError(f"no {provider} credentials configured")
            result = await broker.acquire(eligible, rotation_key)
            await s.commit()

        if not isinstance(result, AllRateLimited):
            if parked:
                await db.update_run_status(run_id, RUN_STATUS_RUNNING)
            await sandbox.env.set(_provider_env(result.token, model))
            return result.credential_id

        if not parked:
            parked = True
            await db.update_run_status(run_id, RUN_STATUS_RATE_LIMITED)
            await log_audit(run_id, "credentials_exhausted_waiting", {
                "wait_until": result.wait_until.isoformat(),
                "reason": result.reason,
            })
        log.info("[%s] all %s credentials rate-limited, waiting", run_id[:8], provider)
        await asyncio.sleep(CREDENTIAL_WAIT_POLL_SECONDS)


async def report_round_outcome(run_id: str, cred_id: str) -> None:
    """Cool down this round's credential if the round hit a rate limit.

    The runner persists rate_limit_resets_at on the run when a round is rate
    limited. This consumes and clears that timestamp in one transaction so it
    is a per-round signal: a later round that hits no limit reads None and
    cools down nothing, never poisoning an innocent credential.
    """
    async with get_session_factory()() as s:
        run = await s.get(Run, run_id)
        if run is None or not run.rate_limit_resets_at:
            return
        reset_dt = datetime.fromtimestamp(run.rate_limit_resets_at, tz=timezone.utc)
        run.rate_limit_resets_at = None
        if reset_dt > datetime.now(timezone.utc):
            await CredentialBroker(s).report_exhausted(cred_id, reset_dt)
        await s.commit()
