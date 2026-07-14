"""Regression test: the SDK transport buffer must be raised above its default.

The CLI inlines a finished subagent's transcript into the Task result's
`toolUseResult` field, and carries it twice — `output` and `result` are the
same string. A 21-minute proof-outliner produced 603 kB, doubled to a
1,228,989-byte NDJSON frame, against the SDK's 1 MB default. The framer's
guard raises out of the read generator, so the reader task dies permanently:
the subprocess keeps emitting and nobody is listening, and the round is lost.

summarize() cannot prevent this. It runs in a PreToolUse hook, on our side of
the wire, after the SDK has already framed and parsed the line. The overflow
happens in the transport before any hook exists — our largest *logged* payload
that round was 12 kB while the wire carried 1.2 MB.

So the fix is the transport's own documented knob, and what this test pins is
that we pass it at all: the field defaulted to None, which is exactly how the
1 MB default reached production unnoticed.
"""

from __future__ import annotations

from constants import SDK_MAX_BUFFER_BYTES

# The frame that killed session f264a6ef9806 (run d13d3c89, round 1).
OBSERVED_OVERFLOW_BYTES = 1_228_989

# The SDK's _DEFAULT_MAX_BUFFER_SIZE — what we get by leaving the field unset.
SDK_DEFAULT_BUFFER_BYTES = 1024 * 1024


class TestSdkBufferSizeConfigured:
    """The session must configure a transport buffer that fits real payloads."""

    def test_buffer_exceeds_sdk_default(self) -> None:
        """Leaving max_buffer_size unset is the bug — the default is too small."""
        assert SDK_MAX_BUFFER_BYTES > SDK_DEFAULT_BUFFER_BYTES

    def test_buffer_fits_the_frame_that_broke_production(self) -> None:
        """The observed 1.21 MB Task result must parse rather than kill the reader."""
        assert SDK_MAX_BUFFER_BYTES > OBSERVED_OVERFLOW_BYTES

    def test_buffer_has_headroom_beyond_the_observed_frame(self) -> None:
        """Sizing to the one observed sample would re-break on a longer subagent.

        That frame came from a single 21-minute subagent, and the payload scales
        with transcript length — doubled, since output and result duplicate it.
        A ceiling only a little above the sample is a ceiling waiting to be hit
        by the next agent that thinks for longer.
        """
        assert SDK_MAX_BUFFER_BYTES >= 2 * OBSERVED_OVERFLOW_BYTES

    def test_session_passes_the_buffer_to_the_sdk(self) -> None:
        """The constant must actually reach ClaudeAgentOptions.

        A constant nobody passes is precisely the state that shipped: the
        transport reads options.max_buffer_size, and ours was None.
        """
        from sdk.session import Session

        session = Session(
            "test-session",
            {
                "run_id": "test-run",
                "model": "claude-fable-5",
                "effort": "high",
                "system_prompt": "sys",
                "disallowed_tools": [],
                "cwd": "/home/agentuser/repo",
                "add_dirs": [],
                "setting_sources": [],
                "max_budget_usd": 10,
                "github_repo": "owner/repo",
                "branch_name": "test-branch",
                "initial_prompt": "go",
            },
        )

        options = session._build_options()

        assert options.max_buffer_size == SDK_MAX_BUFFER_BYTES
