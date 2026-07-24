# Outline review — imo-2026-03 (round 1)

## Foundations tested (all shared across the three approaches)

I verified the load-bearing shared claims computationally before judging:

1. **Lemma 0 (endgame/greedy) — CONFIRMED.** For a fixed piece multiset, the
   alternating-claim game value to the first mover = sum of odd-ranked pieces
   (sorted descending). Brute-force game tree vs odd-rank-sum agreed on 3000
   random multisets (0 mismatches). This is sound; it may be cached at
   `lemmas/endgame-greedy.md` once a builder writes the induction+monotonicity proof.

2. **Answer c(n)=2^n/(2^{n+1}-1) — CONFIRMED at n=1,2.** Exact maximin grid search
   (LB maximin over cuts, XY minimin over cuts) gives 2/3 at n=1 and 4/7 at n=2,
   with the maximum attained exactly at the dyadic marking {1/7,2/7,4/7}. Dyadic
   LB lower bound gives 8/15 at n=3 too. The conjectured answer and the dyadic LB
   construction are correct.

3. **Layer-cake identity (potential approach) — CONFIRMED exactly.**
   A = sum(-1)^{i+1} a_i = measure{t : #{pieces > t} odd}, on 5000 random
   normalized multisets (0 mismatches). Hence LB total = (1+A)/2 = (1+M)/2 is a
   correct reformulation, and the claim reduces to M* = 1/D_n.

## Two shared mechanisms are flawed AS STATED — both approaches must heed

These are the substantive issues. Neither is fatal (both sit in flagged open
gaps, and the target bound is TRUE), but the mechanisms as written are wrong.

- **A. "A cut in a non-max piece never helps XY / only raises Odd" is FALSE as a
  blanket lemma.** 28,487 counterexamples in 20k random configs: cutting a
  non-maximal piece can strictly DECREASE the odd-rank-sum (help XY). This blanket
  claim appears in `self-similar-recursion` (key lemma "worst XY response = all
  cuts into the largest piece", gap G3) and in `majorization-smoothing` (smoothing
  lemma step 2, "splitting a NON-maximal piece never decreases Odd"). It must NOT
  be used in full generality.
  HOWEVER, restricted to XY responding to the **dyadic config W_n**, the claim
  holds: I checked that XY's global optimal response and XY's response confined to
  cutting only the largest piece coincide, both equal to 2^n/D_n, for n=1,2,3. So
  the LOWER-bound use (XY minimizing against the fixed dyadic config) is salvageable
  — but the builder must prove it *for the dyadic structure specifically*, not cite
  the false general lemma.

- **B. The upper-bound XY strategy "repeatedly bisect the current max n times" does
  NOT achieve the cap.** Against LB = [~1, ~0] at n=2, blind bisection yields
  {0.5,0.25,0.25}+eps with odd-sum 0.75 >> 4/7. XY over-cuts: the correct XY play
  is to split the big piece ONCE into halves (making c(t) even, M=0) and STOP.
  The optimal-XY maximin value is 4/7, so the cap is true, but the naive recipe is
  not it. All three approaches invoke a "clone the leader / bisect the max" UB rule
  — the two sorted-vector approaches must make it ADAPTIVE with an explicit stopping
  rule (don't create a new large odd piece). The **potential approach handles this
  most naturally** ("make c(t) even on as much of [0,1] as possible", with early
  stopping already listed), which is why it ranks first.

## Per-approach verdicts

### alternating-sum-threshold-potential — APPROVE (rank 1)
Genuinely distinct framing (threshold integral / parity measure, not the sorted
vector). Both foundational identities (Lemma 0 payoff, layer-cake A=M) are verified
exactly. Its UB mechanism ("make c(t) even, stop when done") is the most robust of
the three and correctly handles the degenerate LB=[~1] case that breaks blind
bisection. Cruxes remain (G2 LB "dyadic gaps cap destroyable odd-measure at
1-1/D_n"; G3 UB residual <= 1/D_n weighting inequality for ALL markings) but they
are honestly flagged with a stated mechanism. Fix the off-by-one in step 2 as noted.
Build.

### self-similar-recursion — APPROVE with required corrections (rank 2)
Technique (strong two-sided induction on n via the self-similar dyadic
decomposition w_n=2w_{n-1}) is sound and the cleanest structural route. Required
corrections for the builder: (i) G3 — do NOT cite the false blanket exchange
lemma; restrict "XY best cuts the largest piece" to the dyadic config and prove it
there (verified true for n<=3). (ii) G2 UB — the "clone the leader / bisect max"
recursion must incorporate the adaptive stopping rule from finding B, or the
recursion caps the wrong quantity; the maximin confirms the cap is 2^n/D_n, so the
correct residual bookkeeping exists. Build.

### majorization-smoothing — APPROVE, highest risk (rank 3)
Legitimate but the most delicate route; it self-flags the correct danger ("Odd is
NOT monotone under general majorization — stay on the cut path"). Two concerns:
(i) the smoothing lemma's step-2 wording restates the false blanket claim A —
reword to the dyadic-restricted / directed form; (ii) shares the same bisection UB
mechanism (finding B) with self-similar, and shares the same LB exchange — so it
risks stalling on the same wall as self-similar. Build this round for diversity,
but if it and self-similar both bottom out on the identical UB bisection gap next
round, drop one and ask the outliner for a genuinely different UB attack.

## Field diversity note (for the orchestrator)
LB direction: all three share the (correct, forced) dyadic construction and the
same restricted exchange — that convergence is fine, the construction is optimal.
UB direction is the real shared wall: all three lean on a "bisect the max" intuition
and the two sorted-vector approaches share it almost verbatim. The potential
approach is the outlier that sidesteps it. If the UB cruxes plateau across the field
for 2+ rounds, next round should seed one approach with a non-bisection UB strategy
(e.g., XY equalizing/matching LB's pieces directly, or a direct optimal-response
characterization from the maximin structure).

build set: alternating-sum-threshold-potential, self-similar-recursion, majorization-smoothing
