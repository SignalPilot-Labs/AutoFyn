# outline-reviewer per-role rules

ALWAYS: call the ranker by importing `/home/agentuser/repo/.autofyn/approach_ranker.py` directly in python3 (`import approach_ranker as ar; ar.register_approach(...)`) — the MCP decorators return plain functions, and no MCP tool surface is exposed to this role (round 1).
ALWAYS: re-verify the outliner's "sympy-verified" identities yourself in one batch script before approving — cheap (seconds) and it anchors the verdict to evidence, not trust (round 1).
