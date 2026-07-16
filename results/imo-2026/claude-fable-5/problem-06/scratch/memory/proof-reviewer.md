# proof-reviewer rules

ALWAYS: call ranker functions by importing /home/agentuser/repo/.autofyn/approach_ranker.py directly in python3 (sys.path.insert + ar.record_outcome(...)) — it is an MCP server with no CLI, `python3 approach_ranker.py` just blocks (round 1).
ALWAYS: verify greedy-sequence claims by simulation with a bitmask-per-prime coverage check (prime -> bitmask of term indices it covers); it handles 16k terms / 140k candidates in under a minute and confirmed T=5088, L=43890 for a_1=385 (round 1).
ALWAYS: when a builder claims a refutation/counterexample, re-verify its crux lemma with FRESH code, not the builder's — for graph clutters remember minimal cuts on the t-side (e.g. {r0,b0}) or the check silently passes wrong sets (round 1).
NEVER: demand the strongest form of a lemma when the builder proves a weakened form that suffices — check sufficiency instead; the strict lock-in p<=g is false (a_1=385 has 19 in a minimal member) but rho < a_1*g is true and enough (round 1).
ALWAYS: for re-verification rounds use a genuinely different simulator (spf-sieve vs sympy.factorint bitmask) — the a_1=385 run (15278 terms to 132150) finishes in ~2 min with a sieve but is far slower with per-candidate factorint (round 2).
