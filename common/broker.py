"""Health-aware credential selection: round-robin over credentials not cooling down."""

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.constants import (
    CLAUDE_TOKENS_KEY,
    CREDENTIAL_DEFAULT_COOLDOWN_SECONDS,
    MASTER_KEY_PATH,
)
from db.models import CredentialHealth, Setting
from common import crypto


@dataclass(frozen=True)
class Lease:
    """A selected credential: which one, and its pool index."""

    credential_id: str
    index: int


@dataclass(frozen=True)
class WaitDirective:
    """Every credential is cooling down; retry after wait_until."""

    wait_until: datetime
    reason: str


def credential_id(provider: str, material: str) -> str:
    """Stable id for a credential: provider + hash of its material."""
    digest = hashlib.sha256(material.encode()).hexdigest()[:16]
    return f"{provider}:{digest}"


def _now() -> datetime:
    return datetime.now(timezone.utc)


async def read_claude_tokens(s: AsyncSession) -> list[str]:
    """Read and decrypt the Claude token pool (read-only, no lock)."""
    row = await s.get(Setting, CLAUDE_TOKENS_KEY)
    if row is None:
        return []
    return json.loads(crypto.decrypt(row.value, MASTER_KEY_PATH))


def _as_utc(dt: datetime) -> datetime:
    """Normalize a stored datetime to UTC-aware (some backends drop tzinfo)."""
    return dt if dt.tzinfo is not None else dt.replace(tzinfo=timezone.utc)


async def _cooldowns(s: AsyncSession, ids: list[str]) -> dict[str, datetime]:
    """Map credential_id -> cooldown_until for ids that are currently cooling down."""
    rows = (
        (
            await s.execute(
                select(CredentialHealth).where(CredentialHealth.credential_id.in_(ids))
            )
        )
        .scalars()
        .all()
    )
    return {
        r.credential_id: _as_utc(r.cooldown_until)
        for r in rows
        if r.cooldown_until is not None
    }


async def _read_cursor(s: AsyncSession, cursor_key: str) -> int:
    row = await s.get(Setting, cursor_key)
    return int(row.value) if row is not None else 0


async def _write_cursor(s: AsyncSession, cursor_key: str, value: int) -> None:
    row = await s.get(Setting, cursor_key)
    if row is None:
        s.add(Setting(key=cursor_key, value=str(value), encrypted=False))
    else:
        row.value = str(value)


async def acquire(
    s: AsyncSession,
    provider: str,
    ids: list[str],
    cursor_key: str,
) -> Lease | WaitDirective:
    """Pick the next credential round-robin over the ids not cooling down.

    Advances the cursor_key cursor; returns a WaitDirective when all cool down.
    """
    if not ids:
        raise ValueError(f"no credentials for provider '{provider}'")

    now = _now()
    cooldowns = await _cooldowns(s, ids)
    available = [i for i, cid in enumerate(ids) if cooldowns.get(cid, now) <= now]
    if not available:
        return WaitDirective(
            wait_until=min(cooldowns.values()), reason="all credentials rate-limited"
        )

    start = await _read_cursor(s, cursor_key) % len(ids)
    picked = min(available, key=lambda i: (i - start) % len(ids))
    await _write_cursor(s, cursor_key, (picked + 1) % len(ids))
    return Lease(credential_id=ids[picked], index=picked)


async def report_exhausted(
    s: AsyncSession,
    cid: str,
    reset_at: datetime | None,
) -> None:
    """Mark a credential rate-limited until reset_at (default cooldown if None).

    Recovery is automatic: once cooldown_until passes, acquire selects it again.
    """
    cooldown = reset_at or (
        _now() + timedelta(seconds=CREDENTIAL_DEFAULT_COOLDOWN_SECONDS)
    )
    row = await s.get(CredentialHealth, cid)
    if row is None:
        s.add(CredentialHealth(credential_id=cid, cooldown_until=cooldown))
    else:
        row.cooldown_until = cooldown
