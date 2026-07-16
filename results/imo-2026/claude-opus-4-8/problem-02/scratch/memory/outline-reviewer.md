# outline-reviewer role memory

ALWAYS: invoke the ranker (register_approach/copy_approach/update_ranking) by `import sys; sys.path.insert(0,'.autofyn'); import approach_ranker as r` and calling the functions in a python3 -c — it is an MCP server (`mcp.run()`), there is no argparse CLI (round 1).
ALWAYS: for geometry approaches, re-verify each approach's claimed reformulation numerically before ranking — results/<id>/verify_config.py gives find_KL_for_alpha/circumcenter helpers; caught a wrong circumcenter-formula denominator sign and an over-optimistic "linear conjugate solve" (actually degree-2) this way (round 1).

ALWAYS: for imo-2026-02 complex §3, sanity-check the interior-positivity mechanisms by algebraic reduction, not just numerics: Im((2k-b)/b)>0 collapses to Im(k·b̄)>0 = "K on C-side of line AB", and line BM IS line AB (M=midpoint AB, so B,M,A collinear) — so the outline's "K on C-side of BM" is literally K∈int(BMC). Confirmed the midpoint factors 2l-c, 2k-b are correct by evaluating C2,C3 directly and getting real-positive (round 2).
