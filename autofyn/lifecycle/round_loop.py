"""Round loop — Python drives a fresh orchestrator session per round.

This is the real long-running thing. The Claude SDK session only lives
for one round. When a round ends, Python reads `/tmp/memory/rounds.json` for the
summary, commits with `[Round N] <summary>`, pushes, and decides whether
to start another round.

Round terminal states and what the loop does with them:

    complete      : read metadata, commit, push, loop again
    ended         : orchestrator called end_session — commit, push, stop
    paused        : await resume/stop on the user inbox
    stopped       : user stopped — tear down
    session_error : API/SDK error — retry up to 3× with exponential backoff (2/4/8s)
    error         : log and tear down
"""

import logging
from typing import Any

from lifecycle.bootstrap import BootstrapResult
from lifecycle.credentials import acquire_and_inject, report_round_outcome
from lifecycle.round_handlers import (
    handle_complete_or_ended,
    handle_paused,
    handle_session_error,
    handle_stopped,
)
from memory.metadata import MetadataStore
from user.inbox import UserInbox
from prompts.orchestrator import RoundContext, build_initial_prompt, build_round_system_prompt
from prompts.subagent import build_agent_defs
from sandbox_client.client import SandboxClient
from agent_session.runner import RoundRunner
from agent_session.time_lock import TimeLock
from utils import db
from utils.constants import STUCK_RECOVERY_REPORT_NAME
from utils.db_reconcile import reconcile_orphaned_agent_calls
from db.constants import (
    RUN_STATUS_ERROR,
    RUN_STATUS_PAUSED,
    RUN_STATUS_STOPPED,
)
from memory.archiver import RoundArchiver
from utils.models import RoundResult, RunContext

log = logging.getLogger("lifecycle.round_loop")


# ── Per-round preparation helpers ────────────────────────────────────


async def _build_round_context(
    round_number: int,
    bootstrap: BootstrapResult,
    host_mounts: list[dict[str, str]] | None,
    user_env_keys: list[str],
    disabled_subagents: list[str],
) -> tuple[RoundContext, list[str]]:
    """Drain inbox, load prior metadata/reports/user activity, build the
    RoundContext. Returns (round_context, prior_reports) — prior_reports is
    also needed by _build_initial_prompt for the stuck-recovery check."""
    run = bootstrap.run
    time_lock = bootstrap.time_lock
    metadata_store = bootstrap.metadata
    reports = bootstrap.reports
    inbox = bootstrap.inbox

    prior_metadata = await metadata_store.load()
    prior_reports = (
        await reports.list_round(round_number - 1) if round_number > 1 else []
    )
    # Drain in-memory inbox so buffered messages don't re-deliver
    # via send_message at the next subagent boundary. The DB is now
    # the source of truth for the full user activity timeline.
    inbox.take_pending_messages()
    user_activity = await db.get_user_activity(run.run_id)

    round_context = RoundContext(
        round_number=round_number,
        duration_minutes=run.duration_minutes,
        time_remaining_minutes=time_lock.remaining_minutes(),
        metadata=prior_metadata,
        previous_round_reports=prior_reports,
        user_activity=user_activity,
        host_mounts=host_mounts,
        user_env_keys=user_env_keys,
        base_branch=run.base_branch,
        disabled_subagents=disabled_subagents,
        subagent_specs=bootstrap.subagent_config.specs,
        repo_prompt_bodies=bootstrap.subagent_config.bodies,
        sandbox_resources=bootstrap.sandbox_resources,
    )
    return round_context, prior_reports


def _build_round_options(
    round_number: int,
    bootstrap: BootstrapResult,
    round_context: RoundContext,
    host_mounts: list[dict[str, str]] | None,
    user_env_keys: list[str],
    disabled_subagents: list[str],
) -> dict[str, Any]:
    """Build the per-round SDK options dict (base options + agents +
    system_prompt). No I/O."""
    tool_call_timeout_sec = bootstrap.run_config.tool_call_timeout_sec
    system_prompt = build_round_system_prompt(round_context, tool_call_timeout_sec)

    options = dict(bootstrap.base_session_options)
    options["agents"] = build_agent_defs(
        round_number=round_number,
        host_mounts=host_mounts,
        user_env_keys=user_env_keys,
        user_model=options["model"],
        tool_call_timeout_sec=tool_call_timeout_sec,
        base_branch=bootstrap.run.base_branch,
        disabled_subagents=disabled_subagents,
        subagent_specs=round_context.subagent_specs,
        repo_prompt_bodies=round_context.repo_prompt_bodies,
        sandbox_resources=round_context.sandbox_resources,
    )
    options["system_prompt"] = {
        "type": system_prompt["type"],
        "preset": system_prompt["preset"],
        "append": system_prompt.get("append", ""),
    }
    return options


def _build_initial_prompt(
    round_number: int,
    bootstrap: BootstrapResult,
    time_lock: TimeLock,
    prior_reports: list[str],
) -> str:
    """Compute stuck-recovery flag and build the round's initial prompt."""
    prior_round_had_stuck_recovery = STUCK_RECOVERY_REPORT_NAME in prior_reports
    return build_initial_prompt(
        round_number,
        bootstrap.task,
        time_lock.grace_round_used,
        prior_round_had_stuck_recovery,
    )


async def _finalize_round(
    result: RoundResult,
    terminal: str | None,
    round_number: int,
    archiver: RoundArchiver,
    rid: str,
) -> tuple[bool, str | None]:
    """Decide retry, archive the round, and return (retry, terminal).

    retry is True only for a session_error round that has not hit max retries
    (terminal is None) — the caller decrements round_number and continues WITHOUT
    archiving. Otherwise the round is archived (failures logged with exc_info) and
    (False, terminal) is returned."""
    # Session-error retries must not inflate round_number or create
    # junk archive directories. Decrement and retry the same round.
    # When terminal is set (max retries exceeded), fall through to
    # archive so the error round is preserved for resume inspection.
    if result.status == "session_error" and terminal is None:
        return True, None

    # Archive after outcome handling so the persisted rounds.json
    # reflects record_round(N) from _commit_and_push_round — file
    # and metadata snapshots stay consistent on resume.
    try:
        await archiver.archive_round(round_number)
    except Exception as exc:
        log.warning(
            "[%s] archive_round(%d) failed: %s",
            rid,
            round_number,
            exc,
            exc_info=True,
        )
    return False, terminal


# ── Main round loop ──────────────────────────────────────────────────


async def run_rounds(
    sandbox: SandboxClient,
    bootstrap: BootstrapResult,
    host_mounts: list[dict[str, str]] | None,
    user_env_keys: list[str],
    disabled_subagents: list[str],
) -> str:
    """Run rounds until the orchestrator or user says stop.

    Returns the terminal run status: "completed", "stopped", or "error".
    """
    run = bootstrap.run
    time_lock = bootstrap.time_lock
    archiver = bootstrap.archiver
    rid = run.run_id[:8]

    runner = RoundRunner(sandbox, run, bootstrap.inbox, time_lock, bootstrap.run_config)
    metadata_for_commit = bootstrap.metadata
    consecutive_session_errors = 0

    # Fresh run: 0 → first round is 1. Resumed run: starting_round is
    # the highest archived round; we pick up at starting_round + 1.
    round_number = bootstrap.starting_round
    while True:
        round_number += 1
        log.info("[%s] ── Round %d begin ──", rid, round_number)

        await bootstrap.reports.ensure_round_directory(round_number)

        round_context, prior_reports = await _build_round_context(
            round_number, bootstrap, host_mounts, user_env_keys, disabled_subagents
        )
        options = _build_round_options(
            round_number, bootstrap, round_context, host_mounts, user_env_keys,
            disabled_subagents,
        )
        initial_prompt = _build_initial_prompt(
            round_number, bootstrap, time_lock, prior_reports
        )

        cred_id = await acquire_and_inject(sandbox, run.run_id)
        result = await runner.run(options, initial_prompt, round_number)
        await report_round_outcome(run.run_id, cred_id)
        await reconcile_orphaned_agent_calls(run.run_id)

        terminal, consecutive_session_errors = await _handle_round_outcome(
            result=result,
            round_number=round_number,
            sandbox=sandbox,
            run=run,
            inbox=bootstrap.inbox,
            time_lock=time_lock,
            metadata_store=metadata_for_commit,
            consecutive_session_errors=consecutive_session_errors,
            max_rounds=bootstrap.run_config.max_rounds,
        )

        retry, terminal = await _finalize_round(
            result, terminal, round_number, archiver, rid
        )
        if retry:
            round_number -= 1
            continue
        if terminal is not None:
            return terminal


# ── Outcome handling ─────────────────────────────────────────────────


async def _handle_round_outcome(
    result: RoundResult,
    round_number: int,
    sandbox: SandboxClient,
    run: RunContext,
    inbox: UserInbox,
    time_lock: TimeLock,
    metadata_store: MetadataStore,
    consecutive_session_errors: int,
    max_rounds: int,
) -> tuple[str | None, int]:
    """Apply the round result. Returns (terminal status or None, error counter)."""
    rid = run.run_id[:8]

    if result.status == RUN_STATUS_ERROR:
        log.error("[%s] Round %d errored: %s", rid, round_number, result.error)
        return RUN_STATUS_ERROR, 0

    if result.status == "session_error":
        return await handle_session_error(
            result, round_number, run, consecutive_session_errors
        )

    # Any non-error round resets the counter.
    consecutive_session_errors = 0

    if result.status == RUN_STATUS_STOPPED:
        await handle_stopped(
            round_number, sandbox, run, metadata_store, result,
        )
        return RUN_STATUS_STOPPED, 0

    if result.status == RUN_STATUS_PAUSED:
        terminal = await handle_paused(round_number, run, inbox)
        return terminal, 0

    # status in ("complete", "ended")
    terminal = await handle_complete_or_ended(
        result, round_number, sandbox, run, metadata_store,
        time_lock, inbox, max_rounds,
    )
    return terminal, 0
