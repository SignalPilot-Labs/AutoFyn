"""Session utility functions — serialization, agent parsing, summarization.

After SSE consolidation, all event data flows through the SessionEventLog.
No HTTP POSTs to the agent — the sandbox never initiates outbound connections.
"""

import json
import logging
from typing import Any

from claude_agent_sdk import (
    AssistantMessage,
    ResultMessage,
    TextBlock,
    ThinkingBlock,
    ToolUseBlock,
)
from claude_agent_sdk.types import (
    AgentDefinition,
    RateLimitEvent,
    StreamEvent,
)

from constants import (
    INPUT_CONTENT_MAX_LEN,
    INPUT_SUMMARY_MAX_LEN,
    SUBAGENT_RUNS_IN_BACKGROUND,
    SUMMARY_CONTENT_KEYS,
    SUMMARY_ELLIPSIS,
    SUMMARY_MAX_DEPTH,
    SUMMARY_MAX_ITEMS,
    SUMMARY_TRUNCATED_KEY,
)
from models import TruncationReport

log = logging.getLogger("sandbox.session_utils")


def parse_agents(raw: dict[str, dict]) -> dict[str, AgentDefinition]:
    """Convert plain dicts from the agent into AgentDefinition dataclasses.

    Pins every subagent to synchronous dispatch: the orchestrator must have the
    subagent's report in hand before it can end its turn.
    """
    return {
        name: AgentDefinition(
            description=defn["description"],
            prompt=defn["prompt"],
            model=defn.get("model"),
            tools=defn.get("tools"),
            background=SUBAGENT_RUNS_IN_BACKGROUND,
        )
        for name, defn in raw.items()
    }


def _clamp(val: Any, key: str, depth: int, report: TruncationReport) -> Any:
    """Clamp strings in val to their per-key limit, recursing into containers.

    Sets report.truncated whenever a value is dropped or shortened, so callers
    know a payload was clamped without re-serializing the original to compare.
    Never changes a value's type — consumers read these payloads by shape.
    """
    if isinstance(val, str):
        limit = (
            INPUT_CONTENT_MAX_LEN if key in SUMMARY_CONTENT_KEYS else INPUT_SUMMARY_MAX_LEN
        )
        if len(val) <= limit:
            return val
        report.truncated = True
        return val[:limit] + SUMMARY_ELLIPSIS
    if depth >= SUMMARY_MAX_DEPTH:
        if isinstance(val, dict) and val:
            report.truncated = True
            return {}
        if isinstance(val, list) and val:
            report.truncated = True
            return []
        return val
    if isinstance(val, dict):
        if len(val) > SUMMARY_MAX_ITEMS:
            report.truncated = True
        return {
            k: _clamp(v, k, depth + 1, report)
            for k, v in list(val.items())[:SUMMARY_MAX_ITEMS]
        }
    if isinstance(val, list):
        if len(val) > SUMMARY_MAX_ITEMS:
            report.truncated = True
        return [_clamp(v, key, depth + 1, report) for v in val[:SUMMARY_MAX_ITEMS]]
    return val


def summarize(data: Any) -> dict:
    """Truncate large values in tool input/output for event log storage.

    Drops any incoming SUMMARY_TRUNCATED_KEY so the flag is always ours.
    """
    report = TruncationReport()
    if not isinstance(data, dict):
        raw = json.dumps(data, default=str)
        if len(raw) > INPUT_SUMMARY_MAX_LEN:
            raw = raw[:INPUT_SUMMARY_MAX_LEN] + SUMMARY_ELLIPSIS
        return {"_raw": raw}
    payload = {k: v for k, v in data.items() if k != SUMMARY_TRUNCATED_KEY}
    if len(payload) != len(data) or len(payload) > SUMMARY_MAX_ITEMS:
        report.truncated = True
    summarized = {
        key: _clamp(val, key, 1, report)
        for key, val in list(payload.items())[:SUMMARY_MAX_ITEMS]
    }
    if report.truncated:
        summarized[SUMMARY_TRUNCATED_KEY] = True
    return summarized


def serialize_message(message: object) -> dict | None:
    """Convert SDK message to a JSON-serializable event dict."""
    if isinstance(message, StreamEvent):
        # Always None in practice — subagent partials don't surface — but pass
        # the SDK's field through rather than assert what it can never carry.
        return {
            "event": "stream_event",
            "data": {
                "event": message.event or {},
                "parent_tool_use_id": message.parent_tool_use_id,
            },
        }
    if isinstance(message, AssistantMessage):
        blocks = []
        for block in message.content:
            if isinstance(block, TextBlock):
                blocks.append({"type": "text", "text": block.text})
            elif isinstance(block, ThinkingBlock):
                blocks.append({"type": "thinking", "thinking": block.thinking})
            elif isinstance(block, ToolUseBlock):
                blocks.append(
                    {
                        "type": "tool_use",
                        "id": block.id,
                        "name": block.name,
                        "input": block.input,
                    }
                )
        return {
            "event": "assistant_message",
            "data": {
                "content": blocks,
                "usage": message.usage,
                "parent_tool_use_id": message.parent_tool_use_id,
            },
        }
    if isinstance(message, RateLimitEvent):
        info = message.rate_limit_info
        return {
            "event": "rate_limit",
            "data": {
                "status": info.status,
                "resets_at": info.resets_at,
                "utilization": info.utilization,
            },
        }
    if isinstance(message, ResultMessage):
        return {
            "event": "result",
            "data": {
                "session_id": message.session_id,
                "total_cost_usd": message.total_cost_usd,
                "num_turns": message.num_turns,
                "usage": message.usage,
                # Full-session usage per model, subagent turns included —
                # the only place the CLI reports subagent tokens at all.
                "model_usage": message.model_usage,
            },
        }
    return None
