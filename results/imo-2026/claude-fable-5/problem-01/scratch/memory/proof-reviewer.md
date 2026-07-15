# proof-reviewer — per-role rules

ALWAYS: verify combinatorial-process problems by exhaustive DFS over the full reachable-state graph (all move orders), not sampled plays — sampling can miss the order-dependent terminal a proof wrongly excludes (worked for imo-2026-01, round 1).
ALWAYS: call record_outcome via `python3 -c "import sys; sys.path.insert(0,'.autofyn'); import approach_ranker as ar; ar.record_outcome(...)"` from the repo root — the MCP tool is not in the reviewer's function list, but the decorated function is directly callable and writes the sidecar correctly (round 1).
ALWAYS: when two rival approaches share a core identity (e.g. subtractive Euclid), check each proves it from scratch in its own text — shared-unproven-core is the single-line trap in disguise (both passed, round 1).
NEVER: trust a lemma file's "proved in full in <approach>" pointer without opening the approach and matching the lemma statement clause-by-clause against what is actually proved there — certify only exact, no-stronger statements (round 1).
