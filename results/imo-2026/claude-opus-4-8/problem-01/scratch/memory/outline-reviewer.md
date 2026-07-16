# outline-reviewer role memory

ALWAYS: call the ranker tools (register_approach/update_ranking/copy_approach) by
importing .autofyn/approach_ranker.py in a python3 script (sys.path.insert
'.autofyn'; import approach_ranker) — it is an MCP server with no CLI, and these
tools are not in the Bash-agent function schema (round 1).
ALWAYS: run a quick random simulation for combinatorial-process IMO problems to
confirm the invariant/monovariant before ranking — cheap and catches wrong
formulas (confirmed IMO-2026-P1 M=prod p^{gcd v_p}, exactly-one survivor, round 1).
NOTE: for imo-2026-01, omega-count and valuation-gcd share the SAME termination
monovariant (sum Omega + count); product-count (lex on board product) is the real
termination hedge. Watch that shared-monovariant risk if it ever fails (round 1).
