# outline-reviewer — per-role rules

ALWAYS: Verify the shared reduction yourself (line by line + a quick sympy simulation) before letting multiple approaches build on it — for imo-2026-06 the sorted-valid-set identity checked out and that verification let me cut the hedge approach with confidence (round 1).
NEVER: Let a "greedy would have chosen a cheaper candidate" argument pass once "sequence = sorted valid set" is established — the greedy has no freedom; such dynamic arguments are vacuous and must be recast as static statements about the valid set (crt-window lead 3(a), round 1).
ALWAYS: Call the ranker via `cd /home/agentuser/repo/.autofyn && python3 -c "import approach_ranker as ar; ..."` — the tools are plain functions in .autofyn/approach_ranker.py, not bound MCP tools (round 1).
NEVER: Register a RETHINK-cut approach in the ranker — finite-state-window-pullback was cut and left out so junk stays out of the pool (round 1).
