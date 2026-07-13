"""Per-round credential acquisition: pick a healthy credential, inject it, park if none.

Provider-aware: the run's model determines its provider (Claude → anthropic,
GPT-5.6 → openrouter), the broker rotates only over that provider's tokens, and
the injected env differs per provider (native OAuth token vs. OpenRouter gateway
routing). A run is single-provider, so there is no cross-provider env to clear.
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
from common.broker import CredentialBroker, WaitDirective, credential_id
from common.constants import (
    ENV_ANTHROPIC_API_KEY,
    ENV_ANTHROPIC_AUTH_TOKEN,
    ENV_ANTHROPIC_BASE_URL,
    ENV_CLAUDE_OAUTH_TOKEN,
    OPENROUTER_BASE_URL,
    PROVIDER_ANTHROPIC,
    PROVIDER_OPENROUTER,
    openrouter_model_env,
    provider_for_model,
    rotation_key_for,
)
from common.models import Token
from utils import db
from utils.db_logging import log_audit

log = logging.getLogger("lifecycle.credentials")


def _provider_env(provider: str, model: str, value: str) -> dict[str, str]:
    """Build the SDK credential env for a leased token, per provider.

    Fails loudly on an unknown provider rather than injecting a partial env
    that would silently route to the wrong place.
    """
    if provider == PROVIDER_ANTHROPIC:
        return {ENV_CLAUDE_OAUTH_TOKEN: value}
    if provider == PROVIDER_OPENROUTER:
        # Point the SDK at OpenRouter, auth with the OpenRouter key, and blank
        # ANTHROPIC_API_KEY so it never falls back to a native Anthropic key
        # that would bypass the gateway. Model overrides route the SDK tiers.
        return {
            ENV_ANTHROPIC_BASE_URL: OPENROUTER_BASE_URL,
            ENV_ANTHROPIC_AUTH_TOKEN: value,
            ENV_ANTHROPIC_API_KEY: "",
            **openrouter_model_env(model),
        }
    raise ValueError(f"cannot build credential env for unknown provider '{provider}'")


async def acquire_and_inject(sandbox: SandboxClient, run_id: str, model: str) -> str:
    """Acquire a healthy credential for the run's provider and inject it.

    The run's model fixes its provider; the broker rotates only over tokens of
    that provider. Parks the run (status rate_limited) until a credential is
    free, then injects the provider-specific env and returns its credential_id
    so the caller can report exhaustion.
    """
    provider = provider_for_model(model)
    parked = False
    while True:
        async with get_session_factory()() as s:
            broker = CredentialBroker(s)
            pool = await broker.read_pool()
            tokens: list[Token] = [t for t in pool if t.provider == provider]
            if not tokens:
                raise RuntimeError(f"no {provider} credentials configured")
            ids = [credential_id(t.provider, t.value) for t in tokens]
            rotation_key = rotation_key_for(provider, CLAUDE_TOKEN_INDEX_KEY)
            result = await broker.acquire(provider, ids, rotation_key)
            await s.commit()

        if not isinstance(result, WaitDirective):
            if parked:
                await db.update_run_status(run_id, RUN_STATUS_RUNNING)
            await sandbox.env.set(_provider_env(provider, model, tokens[result.index].value))
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
