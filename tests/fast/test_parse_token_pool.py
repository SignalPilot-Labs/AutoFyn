"""Tests for parse_token_pool: legacy string entries upgrade, new dict entries keep labels.

The pool schema changed from list[str] to list[Token]. parse_token_pool must read
both: bare strings (pre-migration) become label-less Tokens, dict entries round-trip.
"""

from __future__ import annotations

from common.models import Token, parse_token_pool


class TestParseTokenPool:
    """parse_token_pool normalizes decrypted pools to list[Token]."""

    def test_legacy_string_entries_become_labelless_tokens(self) -> None:
        """Pre-migration bare-string entries upgrade to Tokens with label=None."""
        result = parse_token_pool(["sk-ant-a", "sk-ant-b"])

        assert result == [
            Token(value="sk-ant-a", label=None),
            Token(value="sk-ant-b", label=None),
        ]

    def test_dict_entries_preserve_label(self) -> None:
        """New-shape dict entries round-trip value and label."""
        result = parse_token_pool(
            [{"value": "sk-ant-a", "label": "work"}, {"value": "sk-ant-b", "label": None}]
        )

        assert result == [
            Token(value="sk-ant-a", label="work"),
            Token(value="sk-ant-b", label=None),
        ]

    def test_mixed_legacy_and_new_entries(self) -> None:
        """A pool mid-migration may hold both shapes at once."""
        result = parse_token_pool(["sk-ant-a", {"value": "sk-ant-b", "label": "spare"}])

        assert result == [
            Token(value="sk-ant-a", label=None),
            Token(value="sk-ant-b", label="spare"),
        ]

    def test_empty_pool(self) -> None:
        """An empty decrypted pool yields an empty list."""
        assert parse_token_pool([]) == []
