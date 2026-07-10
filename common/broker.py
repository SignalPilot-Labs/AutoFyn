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
from common.models import parse_token_pool


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


def _as_utc(dt: datetime) -> datetime:
    """Normalize a stored datetime to UTC-aware (some backends drop tzinfo)."""
    return dt if dt.tzinfo is not None else dt.replace(tzinfo=timezone.utc)


class CredentialBroker:
    """Selects healthy credentials and records rate-limit cooldowns.

    Bound to one session; all queries run on it. The caller commits.
    Selection is round-robin over the credentials not currently cooling down,
    bookmarked by a per-provider rotation index in the settings table.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._s = session

    async def read_claude_tokens(self) -> list[str]:
        """Read and decrypt the Claude token pool values (read-only, no lock)."""
        row = await self._s.get(Setting, CLAUDE_TOKENS_KEY)
        if row is None:
            return []
        pool = parse_token_pool(json.loads(crypto.decrypt(row.value, MASTER_KEY_PATH)))
        return [t.value for t in pool]

    async def acquire(
        self, provider: str, ids: list[str], rotation_key: str
    ) -> Lease | WaitDirective:
        """Pick the next credential round-robin over the ids not cooling down.

        Advances the rotation bookmark; returns a WaitDirective when all cool down.
        """
        if not ids:
            raise ValueError(f"no credentials for provider '{provider}'")

        now = _now()
        cooldowns = await self._cooldowns(ids)
        available = [i for i, cid in enumerate(ids) if cooldowns.get(cid, now) <= now]
        if not available:
            return WaitDirective(
                wait_until=min(cooldowns.values()), reason="all credentials rate-limited"
            )

        start = await self._read_rotation(rotation_key) % len(ids)
        picked = min(available, key=lambda i: (i - start) % len(ids))
        await self._write_rotation(rotation_key, (picked + 1) % len(ids))
        return Lease(credential_id=ids[picked], index=picked)

    async def report_exhausted(self, cid: str, reset_at: datetime | None) -> None:
        """Mark a credential rate-limited until reset_at (default cooldown if None).

        Recovery is automatic: once cooldown_until passes, acquire selects it again.
        """
        cooldown = reset_at or (
            _now() + timedelta(seconds=CREDENTIAL_DEFAULT_COOLDOWN_SECONDS)
        )
        row = await self._s.get(CredentialHealth, cid)
        if row is None:
            self._s.add(CredentialHealth(credential_id=cid, cooldown_until=cooldown))
        else:
            row.cooldown_until = cooldown

    async def _cooldowns(self, ids: list[str]) -> dict[str, datetime]:
        """Map credential_id -> cooldown_until for ids currently cooling down."""
        rows = (
            (
                await self._s.execute(
                    select(CredentialHealth).where(
                        CredentialHealth.credential_id.in_(ids)
                    )
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

    async def _read_rotation(self, rotation_key: str) -> int:
        row = await self._s.get(Setting, rotation_key)
        return int(row.value) if row is not None else 0

    async def _write_rotation(self, rotation_key: str, value: int) -> None:
        row = await self._s.get(Setting, rotation_key)
        if row is None:
            self._s.add(Setting(key=rotation_key, value=str(value), encrypted=False))
        else:
            row.value = str(value)
