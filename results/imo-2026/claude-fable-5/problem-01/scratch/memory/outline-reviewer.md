# outline-reviewer — per-role rules

ALWAYS: run your own quick numerical check (random runs + exhaustive small-case branch) instead of trusting explorer-reported test counts — an exhaustive 3-board confluence check took seconds and turned "explorer says 200 tests" into independent evidence (round 1).
ALWAYS: when an outline proposes "prove uniqueness of terminals by induction" as a mechanism for local confluence, check for circularity — the induction step of terminal-uniqueness typically IS local confluence; require the builder to exhibit explicit joining sequences or an independent pin on the terminal state (round 1).
