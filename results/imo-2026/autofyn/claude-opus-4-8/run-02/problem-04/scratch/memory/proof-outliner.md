# proof-outliner role memory

ALWAYS: do NOT call register_approach — it is the outline-reviewer's gate (seeds only approved
  lines); the dispatch prompt may say "register" but the ranker code + role prompt say the
  outliner does not register (because register_approach docstring reserves it for the reviewer,
  round 1).
ALWAYS: numerically test the load-bearing lemma before outlining — for imo-2026-04 a quick
  random-move sim confirmed the residue-invariant necessity (0 forced-loss events) and turned a
  "hard open gap" flagged by explorers into an essentially-complete argument (round 1).
