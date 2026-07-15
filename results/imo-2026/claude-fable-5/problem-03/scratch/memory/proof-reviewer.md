# proof-reviewer — per-role rules

ALWAYS: re-implement UB/LB constructions independently in exact rationals (fractions.Fraction) rather than rerunning the builder's script — float pigeonhole interval indexing (int(s*D)) can misclassify boundary sums (round 1, imo-2026-03).
ALWAYS: audit mark-count ledgers branch by branch (leftover nonempty / leftover empty / one side empty from the start) — the ≤ n budget is where realization lemmas silently overspend (round 1).
ALWAYS: check claiming-phase lemmas by brute-force game tree with ties AND zeros included — zero-length pieces from endpoint marks are the classic skipped case (round 1).
NEVER: assume two approaches with the same core mechanism share a verdict — verify each file's own write-up (self-similar-induction's Lemma R differed materially from the merge process and needed its own check, round 1).
ALWAYS: call record_outcome by importing .autofyn/approach_ranker.py and calling the function directly (it is an MCP tool, no CLI; cwd is repo root so sys.path.insert(0,'.autofyn') works) (round 1).
