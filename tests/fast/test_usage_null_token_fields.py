"""Regression test: null token fields in a usage payload must not crash.

OpenRouter (GPT-5.6) sends cache_creation_input_tokens / cache_read_input_tokens
as null for token kinds the model lacks (GPT has no prompt caching). The old
`usage.get(key, 0)` only defaulted on an ABSENT key, so a present-but-null value
returned None and `int + None` raised "unsupported operand type(s) for +: 'int'
and 'NoneType'" on the first round of any OpenRouter run. `usage.get(key) or 0`
now treats absent and null alike as zero (the correct semantic — zero tokens of
that kind).
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from tests.fast.conftest import _make_dispatcher


class TestUsageNullTokenFields:
    """_accumulate_usage must coerce null token counts to 0 without crashing."""

    @pytest.mark.asyncio
    async def test_null_cache_fields_do_not_crash(self) -> None:
        """OpenRouter-style usage with null cache fields accumulates as zeros."""
        dispatcher, _ = _make_dispatcher()
        run = dispatcher._run

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher._accumulate_usage(
                {
                    "usage": {
                        "input_tokens": 1200,
                        "output_tokens": 300,
                        "cache_creation_input_tokens": None,
                        "cache_read_input_tokens": None,
                    }
                }
            )

        assert run.total_input_tokens == 1200
        assert run.total_output_tokens == 300
        assert run.cache_creation_input_tokens == 0
        assert run.cache_read_input_tokens == 0
        assert dispatcher._latest_context_tokens == 1200

    @pytest.mark.asyncio
    async def test_all_null_token_fields_do_not_crash(self) -> None:
        """Every token field null accumulates to zero, no exception."""
        dispatcher, _ = _make_dispatcher()
        run = dispatcher._run

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher._accumulate_usage(
                {
                    "usage": {
                        "input_tokens": None,
                        "output_tokens": None,
                        "cache_creation_input_tokens": None,
                        "cache_read_input_tokens": None,
                    }
                }
            )

        assert run.total_input_tokens == 0
        assert run.total_output_tokens == 0
        assert run.cache_creation_input_tokens == 0
        assert run.cache_read_input_tokens == 0
        assert dispatcher._latest_context_tokens == 0
