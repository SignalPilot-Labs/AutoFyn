"""Dashboard utility functions — agent HTTP proxy, ORM helpers, DB access helpers."""

import json
import logging
import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from datetime import date, datetime
from typing import Any

import httpx
from cryptography.fernet import InvalidToken
from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession

from common import crypto
from backend.constants import (
    AGENT_API_URL,
    AGENT_TIMEOUT_SHORT,
    MASK_PREFIX_CLAUDE_TOKEN,
    SECRET_KEYS,
    SIGNAL_AGENT_PATHS,
)
from db.connection import get_session_factory
from db.constants import (
    CLAUDE_TOKEN_INDEX_KEY,
    CLAUDE_TOKENS_KEY,
    DISABLED_SUBAGENTS_KEY_PREFIX,
    HOST_MOUNTS_KEY_PREFIX,
    MASTER_KEY_PATH,
    PROVIDER_ANTHROPIC,
    REMOTE_MOUNTS_KEY_PREFIX,
)
from common.models import Token, parse_token_pool
from db.models import AuditLog, ControlSignal, Run, Setting


class CredentialDecryptionError(Exception):
    """Raised when a stored credential cannot be decrypted.

    Distinguishes 'credential set but broken' from 'credential not configured'.
    """

_AGENT_INTERNAL_SECRET = os.environ["AGENT_INTERNAL_SECRET"]
if not _AGENT_INTERNAL_SECRET:
    raise RuntimeError("AGENT_INTERNAL_SECRET is empty — dashboard cannot start")

log = logging.getLogger("backend.utils")


def _decrypt_json(setting: Setting, error_label: str) -> Any:
    """Decrypt an encrypted setting value and parse it as JSON.

    Raises CredentialDecryptionError on either decrypt failure (InvalidToken)
    or JSON parse failure (JSONDecodeError/TypeError), with error_label
    identifying the offending setting in the message.
    """
    try:
        plain = crypto.decrypt(setting.value, MASTER_KEY_PATH)
    except InvalidToken as e:
        raise CredentialDecryptionError(
            f"Stored credential '{error_label}' exists but cannot be decrypted — master key may have changed"
        ) from e
    try:
        return json.loads(plain)
    except (json.JSONDecodeError, TypeError) as e:
        raise CredentialDecryptionError(
            f"Stored credential '{error_label}' exists but cannot be parsed — data may be corrupted"
        ) from e


# ---------------------------------------------------------------------------
# Session helper
# ---------------------------------------------------------------------------

@asynccontextmanager
async def session() -> AsyncGenerator[AsyncSession]:
    """Yield an async DB session."""
    async with get_session_factory()() as s:
        yield s


# ---------------------------------------------------------------------------
# ORM helpers
# ---------------------------------------------------------------------------

def model_to_dict(obj) -> dict:
    """Convert an ORM model instance to a JSON-safe dict."""
    d = {c.key: getattr(obj, c.key) for c in obj.__table__.columns}
    for key, val in d.items():
        if isinstance(val, (datetime, date)):
            d[key] = val.isoformat()
    return d


# ---------------------------------------------------------------------------
# Control signals
# ---------------------------------------------------------------------------

async def send_control_signal(
    run_id: str,
    signal: str,
    valid_statuses: set[str],
    payload: str | None,
    extra_body: dict[str, Any] | None,
) -> dict:
    """Validate run status, log to DB, and forward to agent EventBus."""
    async with session() as s:
        run = await s.get(Run, run_id)
        if not run:
            raise HTTPException(status_code=404, detail="Run not found")
        if run.status not in valid_statuses:
            raise HTTPException(
                status_code=409,
                detail=f"Cannot send '{signal}' to run with status '{run.status}'",
            )
        s.add(ControlSignal(run_id=run_id, signal=signal, payload=payload))
        if signal == "inject" and payload:
            s.add(AuditLog(
                run_id=run_id,
                event_type="prompt_injected",
                details={"prompt": payload},
            ))
        await s.commit()

    agent_path = SIGNAL_AGENT_PATHS.get(signal)
    if agent_path:
        if signal == "inject":
            json_body: dict[str, Any] | None = {"payload": payload}
        elif extra_body is not None:
            json_body = extra_body
        else:
            json_body = None
        params = {"run_id": run_id}
        await agent_request("POST", agent_path, AGENT_TIMEOUT_SHORT, json_body, params, None, extra_headers=None)

    return {"ok": True, "signal": signal, "run_id": run_id}


# ---------------------------------------------------------------------------
# Settings data access
# ---------------------------------------------------------------------------

async def upsert_setting(s: AsyncSession, key: str, value: str, encrypted: bool) -> None:
    """Upsert a single setting."""
    await s.execute(
        pg_insert(Setting)
        .values(key=key, value=value, encrypted=encrypted)
        .on_conflict_do_update(index_elements=["key"], set_={"value": value, "encrypted": encrypted, "updated_at": func.now()})
    )


async def get_repo_list(s: AsyncSession) -> list[str]:
    """Read the repos JSON array from settings."""
    setting = await s.get(Setting, "repos")
    if not setting:
        return []
    try:
        return json.loads(setting.value)
    except (json.JSONDecodeError, TypeError) as e:
        log.error("Repo list setting contains invalid JSON: %s", e, exc_info=True)
        raise CredentialDecryptionError(
            "Repo list setting contains invalid JSON — data may be corrupted"
        ) from e


async def save_repo_list(s: AsyncSession, repos: list[str]) -> None:
    """Write the repos JSON array to settings."""
    await upsert_setting(s, "repos", json.dumps(repos), False)


async def ensure_repo_in_list(s: AsyncSession, repo: str) -> None:
    """Add repo to the list if not already present."""
    repos = await get_repo_list(s)
    if repo not in repos:
        repos.append(repo)
        await save_repo_list(s, repos)


async def read_credentials(repo: str | None, sandbox_id: str | None) -> dict:
    """Read and decrypt stored credentials. Picks next Claude token round-robin.

    When sandbox_id is provided, loads remote mounts from
    ``remote_mounts:{repo}:{sandbox_id}`` instead of local Docker mounts
    from ``host_mounts:{repo}``.
    """
    creds: dict[str, Any] = {}
    async with session() as s:
        for key in ("git_token", "github_repo"):
            setting = await s.get(Setting, key)
            if not setting:
                continue
            if setting.encrypted:
                try:
                    creds[key] = crypto.decrypt(setting.value, MASTER_KEY_PATH)
                except InvalidToken as e:
                    raise CredentialDecryptionError(
                        f"Stored credential '{key}' exists but cannot be decrypted — master key may have changed"
                    ) from e
            else:
                creds[key] = setting.value

        if repo:
            env_key = f"env_vars:{repo}"
            env_setting = await s.get(Setting, env_key)
            if env_setting:
                creds["env"] = _decrypt_json(env_setting, env_key)

            mounts_key = (
                f"{REMOTE_MOUNTS_KEY_PREFIX}{repo}:{sandbox_id}"
                if sandbox_id
                else f"{HOST_MOUNTS_KEY_PREFIX}{repo}"
            )
            mounts_setting = await s.get(Setting, mounts_key)
            if mounts_setting:
                try:
                    creds["host_mounts"] = json.loads(mounts_setting.value)
                except (json.JSONDecodeError, TypeError) as e:
                    raise CredentialDecryptionError(
                        f"Stored config '{mounts_key}' exists but cannot be parsed — data may be corrupted"
                    ) from e

            mcp_key = f"mcp_servers:{repo}"
            mcp_setting = await s.get(Setting, mcp_key)
            if mcp_setting:
                creds["mcp_servers"] = _decrypt_json(mcp_setting, mcp_key)

            disabled_key = f"{DISABLED_SUBAGENTS_KEY_PREFIX}{repo}"
            disabled_setting = await s.get(Setting, disabled_key)
            if disabled_setting:
                try:
                    creds["disabled_subagents"] = json.loads(disabled_setting.value)
                except (json.JSONDecodeError, TypeError) as e:
                    raise CredentialDecryptionError(
                        f"Stored config '{disabled_key}' exists but cannot be parsed — data may be corrupted"
                    ) from e

    return creds


# ---------------------------------------------------------------------------
# Token pool CRUD
# ---------------------------------------------------------------------------

async def read_token_pool(s: AsyncSession, for_update: bool) -> list[Token]:
    """Read the decrypted token pool.

    When for_update=True, acquires a row-level lock (SELECT ... FOR UPDATE)
    to prevent concurrent read-modify-write races during pool mutations.
    Pass for_update=True in any caller that modifies the pool after reading.
    """
    if for_update:
        stmt = select(Setting).where(Setting.key == CLAUDE_TOKENS_KEY).with_for_update()
        result = await s.execute(stmt)
        pool = result.scalar_one_or_none()
    else:
        pool = await s.get(Setting, CLAUDE_TOKENS_KEY)
    if pool:
        return parse_token_pool(_decrypt_json(pool, "Token pool"))
    return []


async def _write_token_pool(s: AsyncSession, tokens: list[Token]) -> None:
    """Encrypt and write the token pool."""
    encrypted = crypto.encrypt(json.dumps([t.model_dump() for t in tokens]), MASTER_KEY_PATH)
    await upsert_setting(s, CLAUDE_TOKENS_KEY, encrypted, True)


async def add_token_to_pool(raw_token: str, label: str | None, provider: str) -> dict:
    """Add a credential to the pool. Rejects duplicate values."""
    async with session() as s:
        tokens = await read_token_pool(s, for_update=True)
        if any(t.value == raw_token for t in tokens):
            raise ValueError("This token is already in the pool")
        tokens.append(Token(provider=provider, value=raw_token, label=label))
        await _write_token_pool(s, tokens)
        await s.commit()
    return {"ok": True, "count": len(tokens)}


async def rename_token_in_pool(index: int, label: str | None) -> dict:
    """Rename a token's label by index. Never touches the value or provider."""
    async with session() as s:
        tokens = await read_token_pool(s, for_update=True)
        if index < 0 or index >= len(tokens):
            raise ValueError(f"Index {index} out of range (pool has {len(tokens)} tokens)")
        existing = tokens[index]
        tokens[index] = Token(provider=existing.provider, value=existing.value, label=label)
        await _write_token_pool(s, tokens)
        await s.commit()
    return {"ok": True, "index": index}


async def list_pool_tokens() -> list[dict]:
    """List all tokens in the pool (value masked, provider and label as-is)."""
    async with session() as s:
        tokens = await read_token_pool(s, for_update=False)
        idx_row = await s.get(Setting, CLAUDE_TOKEN_INDEX_KEY)
        idx_value: str | None = idx_row.value if idx_row else None
    if not tokens:
        return []
    has_used = idx_value is not None
    active_idx = (int(idx_value) - 1) % len(tokens) if has_used else -1
    return [
        {
            "index": i,
            "provider": t.provider,
            "masked": crypto.mask(t.value, prefix_len=MASK_PREFIX_CLAUDE_TOKEN),
            "label": t.label,
            "active": has_used and i == active_idx,
        }
        for i, t in enumerate(tokens)
    ]


async def remove_token_from_pool(index: int) -> dict:
    """Remove a token by index. Adjusts round-robin index to avoid skipping."""
    async with session() as s:
        tokens = await read_token_pool(s, for_update=True)
        if index < 0 or index >= len(tokens):
            raise ValueError(f"Index {index} out of range (pool has {len(tokens)} tokens)")
        tokens.pop(index)
        if tokens:
            await _write_token_pool(s, tokens)
        else:
            pool_row = await s.get(Setting, CLAUDE_TOKENS_KEY)
            if pool_row:
                await s.delete(pool_row)
        # Adjust round-robin index
        idx_row = await s.get(Setting, CLAUDE_TOKEN_INDEX_KEY)
        if idx_row and tokens:
            current = int(idx_row.value)
            if index < current:
                await upsert_setting(s, CLAUDE_TOKEN_INDEX_KEY, str(current - 1), False)
            elif current >= len(tokens):
                await upsert_setting(s, CLAUDE_TOKEN_INDEX_KEY, str(0), False)
        elif idx_row and not tokens:
            await s.delete(idx_row)
        await s.commit()
    return {"ok": True, "count": len(tokens)}


# ---------------------------------------------------------------------------
# Agent HTTP proxy
# ---------------------------------------------------------------------------


async def agent_request(
    method: str,
    path: str,
    timeout: int,
    json_body: dict | None,
    params: dict | None,
    fallback: Any,
    *,
    extra_headers: dict[str, str] | None,
) -> Any:
    """Make an HTTP request to the agent container.

    On success returns the JSON response. On connection failure:
    - If fallback is provided, returns it silently.
    - Otherwise raises HTTP 502.
    Preserves 409 conflict errors from the agent.
    extra_headers are merged after X-Internal-Secret so they cannot overwrite it.
    """
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            headers: dict[str, str] = {"X-Internal-Secret": _AGENT_INTERNAL_SECRET} if _AGENT_INTERNAL_SECRET else {}
            if extra_headers:
                for key, value in extra_headers.items():
                    if key != "X-Internal-Secret":
                        headers[key] = value
            res = await client.request(
                method, f"{AGENT_API_URL}{path}", json=json_body, params=params, headers=headers,
            )
            if res.status_code >= 400:
                log.warning("Agent returned %d for %s %s", res.status_code, method, path)
                try:
                    detail = res.json().get("detail", f"Agent error {res.status_code}")
                except Exception:
                    detail = f"Agent error {res.status_code}"
                # Preserve client-meaningful status codes; wrap others as 502
                if res.status_code in (404, 409, 422, 429, 503):
                    raise HTTPException(status_code=res.status_code, detail=detail)
                raise HTTPException(status_code=502, detail=detail)
            return res.json()
    except HTTPException:
        raise
    except Exception as e:
        log.error("Agent request failed: %s %s — %s", method, path, e, exc_info=True)
        if fallback is not None:
            return fallback
        raise HTTPException(status_code=502, detail="Agent service unavailable")


# ---------------------------------------------------------------------------
# Startup
# ---------------------------------------------------------------------------

async def autofill_settings(master_key_path: str) -> None:
    """Import env vars into settings DB if settings are empty (first-boot autofill)."""
    async with session() as s:
        result = await s.execute(select(func.count()).select_from(Setting))
        if result.scalar_one() > 0:
            return

        env_mappings = {
            "git_token": "GIT_TOKEN",
            "max_budget_usd": "MAX_BUDGET_USD",
        }

        for key, env_var in env_mappings.items():
            val = os.environ.get(env_var)
            if not val:
                continue
            is_secret = key in SECRET_KEYS
            stored_val = crypto.encrypt(val, master_key_path) if is_secret else val
            await upsert_setting(s, key, stored_val, is_secret)

        claude_token = os.environ.get("CLAUDE_CODE_OAUTH_TOKEN")
        if claude_token:
            pool = json.dumps([Token(provider=PROVIDER_ANTHROPIC, value=claude_token, label=None).model_dump()])
            encrypted = crypto.encrypt(pool, master_key_path)
            await upsert_setting(s, CLAUDE_TOKENS_KEY, encrypted, True)

        await s.commit()


