# proof-builder — global-lp-vertex-sufficiency — round 20

File updated: `results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md`
(Status: `partial`, unchanged at the top level — general n remains open —
but two sub-results were fully closed/refuted this round; see below.)

## Task (a): n=2 achievability closure — DONE, fully rigorous, no numerics in the proof

Rewrote Section 10.6 with a complete, gap-free, hand-checked casework
proof (not a grid search) that all ten n=2 response shapes at
p*=(4/7,2/7,1/7) satisfy OddSum >= c(2)=4/7:

- Writing t=1/7 (p1=4t,p2=2t,p3=t), three shapes ((0,2,0),(0,0,2),(0,1,1))
  reduce to a **trivial nonnegativity bound**: the untouched largest
  piece is always the overall rank-1 element, so OddSum = c(2) + (sum of
  nonnegative rank-2/rank-4 terms) >= c(2) immediately.
- The other three ((2,0,0),(1,1,0),(1,0,1)) reduce to a clean identity
  OddSum >= M1+m1 = c(2), where M1,m1 are a canonical max/min split of
  the piece being doubly-split (or the two singly-split pieces' max
  fragments), proved via a short (2-3 sub-case) exhaustive order
  analysis in each case.

I did **not** just copy the explorer's numbers: I independently
re-derived the exact minimizing structure from scratch (the M1+m1
identity is new content this round, not in the explorer's report, which
only reported the numeric vertex values) and cross-checked all six exact
minima against my own independent brute-force exact-`Fraction` grid
search (matches the explorer's reported values digit-for-digit: 4/7,
5/7, 9/14, 4/7, 4/7, 9/14) plus a second independent sanity check
(200,000-trial-per-shape random exact-`Fraction` sampling of the true
domain, zero violations, observed minima matching the proved bounds
exactly). Combined with the already-certified `<=c(2)` witness, this
gives **V(p*)=c(2) exactly, both directions fully proved** — proposed
for certification as the completed n=2 Existence Theorem (Section 10.6,
Promotable lemmas round 20).

## Task (b): n=3 2-cut/6-fragment construction — REFUTED (both natural pairings), honest negative report

Confirmed the outline-reviewer's finding that the outline's primary
p2,p3-tied construction is infeasible (r<0) on a large sub-region of
B(3) (re-verified the flagged point exactly: p2+p3=0.5001>p1=0.365).

Per the dispatch, ran the mandatory LP-style exact worst-case check
(not random sampling) on the recommended alternative (p3,p4-tied
pairing) **before any proof investment**, and found it **also fails**,
broadly:

- Derived the closed form: whenever feasible, OddSum(M') = 1-p1
  identically throughout B(3) (proved the "r'>p2" branch is vacuous
  under B(3)'s own hypothesis p1<1/2 — an exact algebraic fact, not
  numeric).
- This is the *same* value/failure-condition as the already-refuted
  p2,p3-pairing (fails whenever p1<7/15).
- Ran an exact LP (by hand, via cost/constraint-ratio analysis, not
  scipy/sampling) to find the true worst case: feasibility requires
  5g1+6g2+3g3>1; minimizing p1 subject to this and the region's gap
  constraints gives inf p1 = 16/45 ≈ 0.3556 (verified in Fraction
  arithmetic), well below 7/15=21/45, giving a genuine
  sup(OddSum-c(3)) = 1/9 > 0 on an **open sub-region**, not a thin
  sliver.
- Produced an explicit exact-rational counterexample fully inside B(3):
  p=(12821/36000, 2077/7200, 61/288, 1723/12000), OddSum(M')=23179/36000
  ≈ 0.6439 > c(3)=8/15≈0.5333.
- Cross-checked with broad random exact-`Fraction` sampling (433
  feasible points out of 200,000 raw draws; 269/433≈62% violate c(3)),
  consistent with (and stronger than) the explorer's originally-reported
  22% figure (differing sampling distributions, not a bug).

**Self-caught bug, corrected before write-up**: my first derivation of
the p4-from-sum-constraint substitution had a transposed-coefficient
error (4p4+3g1+2g2+g3=1 instead of the correct 4p4+g1+2g2+3g3=1),
caught by my own branch-vs-direct-computation sanity check (40/48
mismatches on the buggy version) before it reached the file. Flagged
explicitly in the write-up (Section 11.3's self-correction note) so no
future round repeats it.

**Net conclusion for (b), reported honestly**: both natural
fragment-to-untouched-piece pairings of the 2-cut/6-fragment
single-piece-split-of-p1 construction are now refuted for the whole of
B(3) — infeasibility (p2,p3-pairing) and value-failure (p3,p4-pairing)
are shown to be *decoupled* obstructions, so swapping the pairing does
not fix the underlying problem. This is a genuine, precisely-scoped
negative result (not written up as a general-purpose lemma, per
established discipline for negative findings), closing off this whole
construction family and leaving two concrete open paths for the next
round: (i) a two-witness case split (main witness for p1 gtrsim 7/15,
a structurally different patch witness for the now-known-substantial
corner p1 in (16/45, 7/15)), or (ii) an entirely different n=3
construction not of this "split p1 into 3, tie 2 fragments" shape.

## Status / Promotable lemmas

Status stays `partial` for the overall approach (n>=3 remains open).
Two items proposed for reviewer certification (not self-certified):
1. **n=2 Achievability Theorem** (Section 10.6 rewrite + Promotable
   lemmas round 20) — completes the full n=2 Existence Theorem
   (V(p)<=c(2) for all p in B(2), and V(p*)=c(2) exactly at the
   witness), both directions fully proved, no gaps.
2. The n=3 negative fact about the p3,p4-pairing's closed-form value
   (OddSum(M')=1-p1 whenever feasible) is recorded as a precise closed
   result but explicitly **not** proposed as a standalone reusable
   lemma (negative/scoping in nature).

All exact-Fraction verification scripts referenced are in `/tmp/` on
this machine (not committed): `/tmp/verify_n2_6shapes.py`,
`/tmp/verify_200_bound.py`, `/tmp/verify_110_101.py`,
`/tmp/verify_020_002.py`, `/tmp/n3_altpairing2.py`,
`/tmp/n3_symbolic2.py`, `/tmp/n3_verify_formula2.py`,
`/tmp/n3_counterex.py`.
