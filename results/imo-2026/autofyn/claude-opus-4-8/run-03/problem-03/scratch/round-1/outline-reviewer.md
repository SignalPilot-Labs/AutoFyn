# Outline review — imo-2026-03 (round 1)

Answer under review: **c(n) = 2^n/(2^{n+1}−1)**. This is a find-all/compute problem: BOTH a lower bound (LB strategy) and an upper bound (XY strategy) are required.

## Numeric verification I ran (foundation is solid)
- **L0 (greedy claim lemma).** Full minimax vs odd-rank sum over 2000 random multisets (up to 7 pieces): 0 mismatches. Confirmed — in the alternating claim game with no cross-piece synergy, "take largest" is optimal for both players and LB's total = odd-rank sum. L1 (order irrelevance) then follows and the reduction to the multiset game is legitimate.
- **Lower bound.** LB = dyadic G_n, 200k random XY refinements (≤ n cuts) for n=1,2,3: min odd-rank sum = exactly 2^n/D_n (0.66667, 0.57143, 0.53333), never below. The superincreasing → small-parts-to-even-ranks mechanism is well supported.
- **Upper bound (dyadic is optimal for LB).** Sampled 300 random LB partitions per n; the best LB value found stayed ≤ 2^n/D_n (n=2: 0.5653, n=3: 0.5329). No partition beats dyadic. Answer confirmed.

So the shared L0/L1 foundation and the target value are on solid ground for all three approaches, and the lower-bound mechanism (identical in spirit across all three) is credible.

## Adversarial finding on the upper bound (affects explicit-certificate)
I tested the explicit-certificate Lemma F(a) claim "XY concentrates cuts on the largest part, never spreads — spreading is suboptimal for XY." **It is false.** For LB = {0.428, 0.410, 0.162} at n=2, concentrating both cuts on the largest part bottoms out at 0.5717 (ABOVE target 4/7 = 0.5714), while XY's true optimum (a sliver off the top + a bisect of the middle part, reorganizing ranks) reaches 0.5101. So concentrate-only does NOT even hold this LB partition to the bound; XY must spread/sliver. A proof built on "concentrate don't spread" would be wrong. The outliner flagged this as an unproven obligation; my check upgrades it to "the stated mechanism is refuted — it must be replaced, not merely proven."

## Verdicts

### induction-peel — APPROVE
- Technique viable for both bounds. Self-similarity checked: R = G_n \ {g*} = ((2^n−1)/D_n)·G_{n−1} exactly (parts 2^j/D_n, j=0..n−1) — the recursion is real, not wishful.
- Lower-bound Lemma A (superincreasing forces sub-pieces of g* / small parts to even ranks; IH on scaled rest) has a stated mechanism that matches the numerics.
- Upper-bound Lemma B (match-vs-bisect min over the peeled top, homogeneous recursion, equalization pins dyadic) is the hard gap but the mechanism is specified and the min-over-two-tactics is correctly identified as essential (the {0.9,0.1} warning is right — match-only gives 0.9). Homogeneity/scaling caveat is correctly noted.
- Builder must: (1) write the L0 exchange argument rigorously; (2) make the rank-interleaving in Lemma A precise (case split on how many of XY's cuts land on g*); (3) prove Lemma B's min caps LB for EVERY partition and that equalization forces the geometric ratio — do not assume the maximizing profile is dyadic, derive it. Verify the two scalar recurrences reproduce 2^n/(2^{n+1}−1).

### alternating-sum-potential — APPROVE
- L2 identity (LB = (1+S)/2, S = Σ(−1)^{i+1}p_(i)) is elementary and correct; target reduces cleanly to S = 1/D_n = smallest dyadic part. Elegant, genuinely distinct route (global monovariant, no induction on n).
- Lower-bound Lemma C (reserve S ≥ 1/D_n) mechanism is credible and matches numerics.
- Upper-bound Lemma D is the risk: the "each cut halves the reserve" contraction must be an EXACT per-cut inequality on a genuinely monovariant Φ, not a hand-wave "S contracts." The outliner names this obligation honestly. Builder must exhibit the concrete per-cut inequality and handle bisect-vs-match, small-part cuts, and parity (m = k + #cuts) of the final count.
- Note: this approach shares the match/bisect intuition with induction-peel on the upper bound; the divergence (global reserve vs recursion on n) is real but the two are the closer pair. Acceptable diversity.

### explicit-certificate — CHANGES REQUESTED (kept in population, not built this round)
- Lower-bound Lemma E (Hall/marriage injection of small parts into even ranks) is sound and matches the observed invariance — good, and a genuine third route on the lower bound.
- Upper-bound Lemma F is broken as written: F(a) "concentrate don't spread" is **refuted** by my test above. The majorization/Schur-convexity cap (F(c)) is also the vaguest mechanism in the field — "Schur-convex functional maximized at the geometric profile" is asserted, not derived. Before this is built, F must be re-planned around a CORRECT XY strategy (one that permits spreading/slivering), and the majorization functional written explicitly with its monotonicity proven.
- Kept registered as a diversity hedge (the Hall lower bound and an order-statistics upper bound are a distinct framing), but it should be revised by the outliner before consuming a builder.

## Diversity assessment (for the orchestrator)
Good spread on the upper-bound crux: recursion-on-n (peel), global monovariant (potential), explicit majorization (certificate). All three share ONE lower-bound idea (superincreasing → small parts to even ranks) and the L0/L1 foundation — but the lower bound is numerically nailed and low-risk, so a shared lower-bound framing is acceptable. The real crux, the upper bound, is attacked three genuinely different ways. Watch that induction-peel and alternating-sum-potential don't collapse into the same match/bisect wall; if both stall there for 2–3 rounds, put a fourth approach on the table that attacks the upper bound without the match/bisect primitive.

## Ranking (this round)
induction-peel (1531) > alternating-sum-potential (1500) > explicit-certificate (1469). Peel leads on the strongest, best-specified two-sided recursion; potential is a close, elegant second whose upper-bound contraction is unproven; certificate trails because its upper-bound mechanism is refuted and needs re-planning.

build set: induction-peel, alternating-sum-potential
