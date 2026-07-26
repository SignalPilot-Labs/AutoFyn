# proof-outliner per-role rules

ALWAYS: verify the core load-bearing facts numerically before writing the skeleton — a 20-line python check on the create-move + obstruction across both unit-fraction and non-unit-fraction θ (including NON-integer-degree θ like 180/7, 180/11) catches framing flaws that explorers disagree on. (Round 1: confirmed θ=36°=180/5 WINS, disproving the defense explorer's "3-smooth only" claim; confirmed create-move works for all N up to 99.)

NEVER: import a defense explorer's subgroup invariant ("keep group ⊆ ℤ/p") that constrains the SPLIT point γ — it fails because Mulan picks γ outside the current group. The correct mod-θ invariant constrains the COORDINATES (angles) to be nonzero mod θ, not γ. (Round 1: defense explorer's broken invariant led it to the WRONG "3-smooth only" answer.)

ALWAYS: distinguish "integer-grid evidence" from "the answer." On the integer-degree grid, divisors of 180 win and non-divisors lose — this is CONSISTENT with the unit-fraction answer (integer divisors ARE 180/N for N|180), not a contradiction. Non-integer θ=180/7 can't be tested on the integer grid; test it on a scaled grid. (Round 1: a "non-divisor loses" reading would have wrongly excluded θ=180/7.)

NEVER: trust shallow/coarse game-tree "no win" results — they miss off-grid winning split points (e.g. the θ=60 win from {36,72,72} needs α=24). Use full least-fixpoint attractor computation or analytic argument instead.

ALWAYS: when the dispatch flags an explorer disagreement, reconcile it against the actual problem with a computation before trusting either side. (Round 1: dispatch's "consolidated conjecture = unit fraction" was correct; both the constructive and retrieval explorers agreed; only the defense explorer dissented, and it was wrong.)
