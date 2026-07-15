# outline-reviewer — per-role rules

ALWAYS: call the ranker by importing /home/agentuser/repo/.autofyn/approach_ranker.py in a python3 heredoc and calling the tool functions directly (register_approach/update_ranking) — the MCP tools are not exposed as native tool calls in this container (round 1).
ALWAYS: computationally test the outline's monovariant/invariant claims with a random-play simulator before approving — a 2-minute script verified W-descent, lex-descent, uniqueness, and join-depth bounds in one shot (round 1).
NEVER: approve a confluence/Newman-style outline whose overlapping-join lemma is "both sides reach the unique small-board terminal" without a first, independent proof of that uniqueness — it is circular; and note that "prove the 3-entry case by its own induction" usually re-encounters the same overlapping case (round 1).
ALWAYS: when two approved approaches share one core identity, check the field has a third registered approach independent of it before accepting the shared risk (single-line-trap audit) (round 1).
