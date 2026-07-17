# outline-reviewer — per-role rules

ALWAYS: check that results/<id>/approaches/.ranking.json exists before assuming approaches are registered — round 1 can autocommit without registering, so "existing" slugs may need register_approach too (round 3)
ALWAYS: call the ranker via `python3 -c "import sys; sys.path.insert(0,'.autofyn'); import approach_ranker as ar; ..."` from /home/agentuser/repo when MCP tools are not exposed in the tool list — the @mcp.tool functions are plain callables (round 3)
ALWAYS: cross-check V_n-style set definitions against how lemmas quantify over them — imo-2026-06 outlines defined V_n with an "m > a_n" bound that made the valid-below-are-terms lemma vacuous as written; a separate unbounded constraint set W_n is needed (round 3)
NEVER: spend more than ~2 min on empirical verification — one sympy script over 2-3 seed values of a_1 with 80 terms suffices to sanity-check a structural claim like SCPL (round 3)
