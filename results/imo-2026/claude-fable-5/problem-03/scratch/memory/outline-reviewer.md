# Per-role rules: outline-reviewer

ALWAYS: invoke the ranker by importing /home/agentuser/repo/.autofyn/approach_ranker.py in python3 (functions register_approach/update_ranking are plain callables despite @mcp.tool) — there is no MCP tool surface in this environment (round 1).
ALWAYS: numerically stress-test any "exhaustion / case-selection covers everything" claim in an upper-bound outline with a hand-built config — round 1 found a real hole in self-similar-induction's k-selection at n=3, q=(0.35,0.245,0.235,0.17), fixable only by cascade-like moves (round 1).
NEVER: accept "vertex replies have sizes in ½ℤ"-style integrality claims without checking equipartition vertices (k≥3 equal sub-pieces give denominators ≥3) (round 1, exact-value-function E3).
ALWAYS: for imo-2026-03, remember the lower bound is zero-slack — grid check at n=2 gives min Odd exactly 4/7, so any lossy estimate in a lower-bound outline is fatal (round 1).
