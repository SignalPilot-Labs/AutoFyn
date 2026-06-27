"""Regression: subagent assistant text must not leak into the main feed.

Assistant messages from a subagent carry a non-null parent_tool_use_id (the
parent Agent/SendMessage tool call they run inside). Their prose is
intermediate narration whose final form is already captured by the
SubagentStop hook (subagent_complete.final_text) and shown as the Agent
Summary. The dispatcher must therefore suppress llm_text/llm_thinking audit
events for subagent messages while still logging them for the orchestrator
(parent_tool_use_id is None).

Before the fix, subagent text was logged with agent_role="worker" and
rendered inline in the main feed, "breaking" the log — most visibly when a
SendMessage resumed a subagent.
"""

from unittest.mock import AsyncMock, patch

import pytest

from agent_session.stream import StreamDispatcher
from agent_session.tracker import SubagentTracker
from utils.models import RunContext
from utils.run_config import RunAgentConfig

_DEFAULT_RUN_CONFIG = RunAgentConfig(
    max_rounds=128,
    tool_call_timeout_sec=3600,
    session_idle_timeout_sec=120,
    subagent_idle_kill_sec=600,
)

_RUN_ID = "abcd1234-0000-0000-0000-000000000000"


def _make_run() -> RunContext:
    """Create a minimal RunContext for the dispatcher."""
    return RunContext(
        run_id=_RUN_ID,
        agent_role="worker",
        github_repo="org/repo",
        branch_name="fix/test",
        base_branch="main",
        duration_minutes=60,
        total_cost=0,
        total_input_tokens=0,
        total_output_tokens=0,
        cache_creation_input_tokens=0,
        cache_read_input_tokens=0,
    )


def _make_dispatcher() -> StreamDispatcher:
    """Create a StreamDispatcher for testing."""
    return StreamDispatcher(
        run=_make_run(),
        round_number=1,
        tracker=SubagentTracker(_DEFAULT_RUN_CONFIG),
    )


def _assistant_event(text: str, parent_tool_use_id: str | None) -> dict:
    """Build an assistant_message stream event with one text block."""
    return {
        "event": "assistant_message",
        "data": {
            "content": [{"type": "text", "text": text}],
            "usage": None,
            "parent_tool_use_id": parent_tool_use_id,
        },
    }


class TestSubagentTextNotLogged:
    """Subagent assistant text is suppressed; orchestrator text is logged."""

    @pytest.mark.asyncio
    async def test_subagent_text_is_not_logged(self) -> None:
        """A message with parent_tool_use_id set must emit no llm_text audit."""
        dispatcher = _make_dispatcher()
        event = _assistant_event("subagent narration", parent_tool_use_id="toolu_123")

        with patch(
            "agent_session.stream.log_audit", new_callable=AsyncMock
        ) as mock_audit:
            signal = await dispatcher.dispatch(event)

        assert signal.kind == "continue"
        mock_audit.assert_not_called()

    @pytest.mark.asyncio
    async def test_orchestrator_text_is_logged(self) -> None:
        """A message with parent_tool_use_id None must emit an llm_text audit."""
        dispatcher = _make_dispatcher()
        event = _assistant_event("orchestrator narration", parent_tool_use_id=None)

        with patch(
            "agent_session.stream.log_audit", new_callable=AsyncMock
        ) as mock_audit:
            signal = await dispatcher.dispatch(event)

        assert signal.kind == "continue"
        mock_audit.assert_called_once_with(
            _RUN_ID,
            "llm_text",
            {"text": "orchestrator narration", "agent_role": "worker"},
        )

    @pytest.mark.asyncio
    async def test_subagent_thinking_is_not_logged(self) -> None:
        """Subagent thinking blocks are suppressed like text blocks."""
        dispatcher = _make_dispatcher()
        event = {
            "event": "assistant_message",
            "data": {
                "content": [{"type": "thinking", "thinking": "subagent thoughts"}],
                "usage": None,
                "parent_tool_use_id": "toolu_456",
            },
        }

        with patch(
            "agent_session.stream.log_audit", new_callable=AsyncMock
        ) as mock_audit:
            signal = await dispatcher.dispatch(event)

        assert signal.kind == "continue"
        mock_audit.assert_not_called()
