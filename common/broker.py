"""Health-aware credential selection: round-robin over credentials not cooling down."""

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.constants import (
    CLAUDE_TOKENS_KEY,
    CREDENTIAL_DEFAULT_COOLDOWN_SECONDS,
    MASTER_KEY_PATH,
)
from db.models import CredentialHealth, Setting
from common import crypto
from common.models import Token, parse_token_pool


@dataclass(frozen=True)
class SelectedCredential:
    """The credential the broker picked this round.

    Carries the token itself, so the caller reads the provider (and value) off
    the selection instead of re-deriving it from the run's model. The provider
    is a property of the chosen credential, not a lock on the run.
    """

    credential_id: str
    index: int
    token: Token


@dataclass(frozen=True)
class AllRateLimited:
    """Every eligible credential is cooling down; retry after wait_until."""

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
    Selection is round-robin over the tokens not currently cooling down,
    bookmarked by a rotation index in the settings table. The caller passes the
    eligible token set and its rotation key, so the broker is provider-agnostic.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._s = session

    async def read_pool(self) -> list[Token]:
        """Read and decrypt the credential pool (read-only, no lock)."""
        row = await self._s.get(Setting, CLAUDE_TOKENS_KEY)
        if row is None:
            return []
        return parse_token_pool(json.loads(crypto.decrypt(row.value, MASTER_KEY_PATH)))

    async def acquire(
        self, tokens: list[Token], rotation_key: str
    ) -> SelectedCredential | AllRateLimited:
        """Pick the next credential round-robin over ``tokens`` not cooling down.

        Advances the rotation bookmark; returns AllRateLimited when all cool down.
        The returned SelectedCredential carries the chosen Token, so the caller
        reads its provider off the selection rather than the run's model.

        Concurrent runs share one rotation bookmark, so the whole selection is a
        read-modify-write on that row. We lock it FOR UPDATE first: that serializes
        overlapping acquires through this row, so two runs can never read the same
        start, pick the same index, and both write start+1 (which would hand the
        same credential out twice and stall the rotation).
        """
        if not tokens:
            raise ValueError("no credentials to select from")

        ids = [credential_id(t.provider, t.value) for t in tokens]
        start = await self._read_rotation_for_update(rotation_key) % len(ids)

        now = _now()
        cooldowns = await self._cooldowns(ids)
        available = [i for i, cid in enumerate(ids) if cooldowns.get(cid, now) <= now]
        if not available:
            return AllRateLimited(
                wait_until=min(cooldowns[cid] for cid in ids),
                reason="all credentials rate-limited",
            )

        picked = min(available, key=lambda i: (i - start) % len(ids))
        await self._write_rotation(rotation_key, (picked + 1) % len(ids))
        return SelectedCredential(
            credential_id=ids[picked], index=picked, token=tokens[picked]
        )

    async def report_exhausted(self, cid: str, reset_at: datetime | None) -> None:
        """Mark a credential rate-limited until reset_at (default cooldown if None).

        Recovery is automatic: once cooldown_until passes, acquire selects it again.

        Concurrent runs can cool the same credential at once, so this is an atomic
        upsert that never shortens an existing cooldown (keeps the later reset).
        A plain get-then-add would race two runs into a duplicate-key insert, and
        a plain assignment could clobber a longer cooldown with a shorter one.
        """
        cooldown = reset_at if reset_at is not None else (
            _now() + timedelta(seconds=CREDENTIAL_DEFAULT_COOLDOWN_SECONDS)
        )
        stmt = pg_insert(CredentialHealth).values(
            credential_id=cid, cooldown_until=cooldown
        )
        await self._s.execute(
            stmt.on_conflict_do_update(
                index_elements=["credential_id"],
                set_={
                    "cooldown_until": func.greatest(
                        CredentialHealth.cooldown_until, stmt.excluded.cooldown_until
                    )
                },
            )
        )

    async def _cooldowns(self, ids: list[str]) -> dict[str, datetime]:
        """Map credential_id -> cooldown_until, restricted to the given ids.

        acquire relies on this restriction: AllRateLimited.wait_until is the min
        over these values, so it must never include cooldowns for other ids.
        """
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

    async def _read_rotation_for_update(self, rotation_key: str) -> int:
        """Read the rotation bookmark, locking its row so overlapping acquires serialize."""
        row = (
            await self._s.execute(
                select(Setting).where(Setting.key == rotation_key).with_for_update()
            )
        ).scalar_one_or_none()
        return int(row.value) if row is not None else 0

    async def _write_rotation(self, rotation_key: str, value: int) -> None:
        row = await self._s.get(Setting, rotation_key)
        if row is None:
            self._s.add(Setting(key=rotation_key, value=str(value), encrypted=False))
        else:
            row.value = str(value)
