# proof-outliner — per-role rules

ALWAYS: numerically stress-test a proposed adversary strategy family before enshrining it in a skeleton (the "obvious" halve+match family for imo-2026-03 provably fails on deficient configs; a 5-minute random search found the counterexample and the cascade fix, round 1).
ALWAYS: check whether per-position bounds are actually true before using them as a lemma — for sorted-piece games only aggregate bounds may hold (p_{2i} ≤ 2^{n−i}/D was false; only the summed defect bound is true, round 1).
ALWAYS: for alternating-claiming games, reduce via (i) claiming value = Odd(multiset), (ii) layer-cake identity Odd − Even = measure{N(x) odd}, (iii) strip-equal-pairs invariance — these three lemmas made all rival routes expressible in one language (round 1).
NEVER: give an inductive approach a lossy estimate when the extremal configuration meets the induction threshold with equality — the geometric config has zero slack, so any inequality slack breaks the step (round 1).
