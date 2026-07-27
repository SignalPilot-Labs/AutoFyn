# Proof review — IMO 2026 P3 (`imo-2026-03`)

Candidate answer: c(n) = 2^n/(2^{n+1}−1) = 2^n/S_n, equivalently minimax alternating sum D* = 1/S_n.
Recorded Status in results file: `partial`. Builder honestly lists two open gaps (general lower-bound Case B; general upper bound). This review verifies the parts claimed rigorous and assesses the open gaps.

---

## 1. Verification of parts claimed "fully proved"

### Lemma A (greedy alternating pick is optimal for both) — CORRECT
The exchange argument checks out. I re-derived the algebra independently.
For j = 2k+1 (odd), after removing v_{2k+1} the sorted remainder is
v_1,…,v_{2k}, v_{2k+2},…,v_m, whose even positions (2,4,6,…, reindexed)
are {v_2,v_4,…,v_{2k}} ∪ {v_{2k+3}, v_{2k+5}, …} (the shift by one index
after the gap is exactly what the builder writes). Then
  payoff(1) − payoff(j) = (v_1−v_2)+(v_3−v_4)+…+(v_{2k−1}−v_{2k}) ≥ 0
by monotonicity. Even case j=2k gives the identical telescoping. The SPE
framing (induction fixes greedy play in the subgame for both movers) is
standard and valid; base m≤2 immediate. The corollary (LB gets (1+D)/2) is
then just total = 1. Solid. This is the correct reduction framework.

### L(1) lower bound — CORRECT
G_1=(1,2), one cut. Cut 2 → (a,2−a): sorted a,1,2−a (for a≥1), D = a−1+(2−a)=1.
Cut 1 → (a,1−a): sorted 2,a,1−a, D = 3−2a > 1 (since a<1). Verified by
brute force over a-grid: min D = 1 exactly. Correct, equality at halving.

### Case A general lower bound — CORRECT
If XY spends 0 cuts on 2^n, then b_1 = 2^n alone at position 1 (all other
pieces ≤ 2^{n−1}). D = 2^n − D_tail, D_tail ≤ (total tail mass) = 2^n−1,
so D ≥ 1. The parity bookkeeping (D_tail = odd-tail-position sum −
even-tail-position sum ≤ odd sum ≤ full sum) is right. Does not even need
the inductive hypothesis, as the builder notes. Correct.

### U(1) upper bound — BOUND CORRECT, but PROOF HAS A BOUNDARY GAP
This is the one place I flag a hidden gap in a "proved" part.

Builder's Case 2 (1/2 ≤ L < 2/3): "shave sliver t off L with
0 < t ≤ min(R, 2L−1)". At L = 1/2 EXACTLY, 2L−1 = 0, so no valid t>0
exists, and moreover the assumed sorted order (L−t, R, t) requires
L−t ≥ R, i.e. t ≤ 2L−1, which at L=1/2 forces t ≤ 0. So the strategy
literally breaks at L = 1/2, a legal LB configuration (cut at the midpoint:
two equal halves).

The BOUND is still true there (I verified): XY cuts one 1/2-piece into
(1/3, 1/6), giving pieces {1/2, 1/3, 1/6}, sorted 1/2, 1/3, 1/6, D = 1/3
exactly; or finer shaves drive D → 0. The true sorted order at L=1/2 is
(R, L−t, t) = (1/2, 1/2−t, t), giving D = 1−2L+2t = 2t, arbitrarily small.
So U(1) holds, but the written case split misses the single boundary point
L = 1/2 (a different sorted order applies). One-line fix: add the boundary
case explicitly. Not fatal — the n=1 result c(1)=2/3 stands (independently
re-verified: worst-case over a fine L-grid gives max XY-achievable D ≈ 0.332
≤ 1/3, attained at L=2/3 geometric).

### Numerical re-confirmation of the conjecture (independent)
- n=1,2,3,4 lower bound on geometric: random XY (≤n cuts) never drives D below
  1 (scaled); n=1,2,3 hit exactly 1, n=4 stays ≥ 1.04. Conjectured floor not
  contradicted.
- n=2 upper bound: over 40 random LB partitions, XY always achieves D ≤ 1/7,
  ratio (XY-optimal D)/(1/7) never exceeds 1, equality only at geometric.
  Conjectured ceiling not contradicted.
So the answer c(n)=2^n/(2^{n+1}−1) is not refuted; it remains the strong
favorite.

---

## 2. Assessment of the two open gaps

### Gap (a): general lower-bound Case B (interleaving of fragments of 2^n
with refined tail). 
The builder's "bold merge inequality" D(merge) ≥ ΣF − ΣT is indeed FALSE
(I reproduce the builder's counterexample: F={5,5,5,5}, T={4,4,4,4}:
merge sorted 5,5,5,5,4,4,4,4 → D=0 < 4=ΣF−ΣT). So a pure mass-counting
merge bound cannot work.

Is the sketched approach salvageable? PARTIALLY. The defect is that it
ignores the *internal alternating structure* of the refined tail T (which by
induction has its own D ≥ 1, not just total mass 2^n−1). The right lemma
must use both (i) the inductive "+1 gap" structure of T (L(n−1) on the tail
as a standalone game) AND (ii) the cut budget ≤ n (the counterexample with
ΣF=ΣT+1 needs more than n cuts to realize as a refinement of G_n).

Most promising concrete direction — the rank-function / integral identity
the builder himself flagged but did not close:
  D = ∫_0^{b_1} 1_{r(t) odd} dt,   r(t) = #{pieces of size ≥ t}.
A single cut of a piece of size s into (m, M) (m ≤ M) changes r by +1 on
(0, m] and 0 elsewhere, so it flips the parity of r on (0, m]. Thus
  ΔD = m − 2·O(m),   O(m) = |{t ∈ (0,m] : r(t) odd}|,
where r is the pre-cut rank function. XY minimises D by cutting where more
than half of (0, m] is currently odd. For the geometric config, r_0(t) is a
step function with steps at 2^0,2^1,…,2^n, and the parity of r_0 alternates
in dyadic bands. A viable invariant to target:

  CONJECTURED LEMMA (the next builder should prove this): For G_n and any
  refinement by ≤ n cuts, at the moment XY makes the k-th cut (1 ≤ k ≤ n)
  on a piece of size 2^j producing fragments (m, M) with m ≤ M, the parity
  flip on (0, m] can reduce D by at most ... such that after all n cuts,
  D ≥ 1. Equivalently: define a potential Φ ≥ D − 1 that is non-decreasing
  under cuts while ≤ n cuts remain in budget; show Φ_final ≥ 0.

The equality case (full halving) shows the bound is exactly tight, so any
proof must pin down that the n-cut budget is precisely what stops XY one
unit short of D = 0 (with 2 cuts on G_1=(1,2) XY reaches D=0; verified).
This is a real, hard, but NOT hopeless combinatorial-continuous lemma; the
integral identity is the right tool. ROUTE: back to builder with this
specific lemma as the target.

### Gap (b): general upper bound.
This is the more worrying gap. The builder tried four natural approaches and
all failed: myopic greedy (fails on 36/400 for n=2, 67/400 for n=3 — I
confirm the failure instance (0.4,0.35,0.25): greedy-halve gives 0.25 >
1/7), naive induction (does not decrement n, the "UB-2 obstacle" — correct:
the sorted order is global), and Hall/equal-pairing (leftover exceeds 1/S_n
on random configs for n≥3 — I confirm this is a real obstruction, not a
sampling artefact).

Is the approach salvageable? The reduction framework (Lemma A) is definitely
right, so this is NOT a RETHINK of the whole problem. But the upper bound
genuinely lacks a worked-out strategy, and the most promising remaining
route — the majorisation/smoothing conjecture ("f(C) = XY-optimal D is
Schur-maximised uniquely at the geometric config") — is unproved and may be
hard; numerics support it (n=2,3 ratios ≤ 1) but a smoothing monotonicity
for a min-of-piecewise-linear function is delicate and not obviously true.

Concrete guidance for the next builder — two parallelisable attacks:

  (UB-i) Direct XY strategy via the integral identity (mirror of the lower
  bound). To prove D ≤ 1/S_n for arbitrary LB partition C, exhibit a
  deterministic XY rule that, cut by cut, drives D down to ≤ 1/S_n. The
  rank-function view suggests: XY should cut so as to flip parity on the
  longest possible odd-band, i.e. shave the largest piece down to the
  second-largest. Formalise a greedy-on-rank strategy (NOT greedy-on-D,
  which fails) and prove it hits 1/S_n. The right invariant is on r(t), not
  on D directly.

  (UB-ii) Prove the smoothing lemma directly: show that for any LB partition
  C = (c_1 ≥ … ≥ c_{n+1}), replacing the two smallest pieces c_n, c_{n+1}
  by their "geometric step" (merging and re-splitting toward ratio 2:1, or
  similar) does not decrease f(C) = XY-optimal D. Iterating reaches the
  geometric config; combined with the lower bound this gives the upper
  bound. This needs a local monotonicity computation; start by proving it
  for n=2 (3 pieces) where it is a 2-variable inequality and verifiable.

Either attack, if it lands, reduces the upper bound to the lower bound (or
to a direct computation), so the lower-bound Case B lemma remains the
load-bearing crux for BOTH directions.

---

## 3. Overclaim check
No overclaim: the file is marked `partial`, the gaps are explicitly named,
and the conjecture is clearly separated from proved results. The only
blemish is the unstated boundary gap in U(1) (L=1/2), but it is fixable and
the result is correct. I do NOT downgrade the overall status for this
alone, but the builder must add the boundary case on revision.

---

## Scores
- Correctness: 7/10. All "proved" parts correct except the U(1) boundary
  gap (fixable). The open gaps are honestly flagged.
- Completeness / rigor: 5/10. Two large gaps (general Case B lower bound;
  general upper bound) remain open. The n=1 case is essentially complete
  modulo the one boundary line.
- Progress: 7/10. The reduction (Lemma A) is the right framework and is
  solid; geometric construction + Case A + exhaustive small-n verification
  constitute real, reusable progress. Far more than a blank start.

## True Status: partial
The proof is not solved: both the general lower bound (Case B interleaving)
and the general upper bound (XY strategy or majorisation) are open, as the
builder admits. The approach is correct and salvageable, not wrong.

## Verdict: CHANGES REQUESTED

Routing guidance for the next round:
1. (Lower bound) Hand the builder the rank-function identity
   D = ∫ 1_{r(t) odd} dt and the parity-flip formula ΔD = m − 2·O(m) for a
   cut (m,M). Task: prove the "potential Φ ≥ D−1 non-decreasing under ≤ n
   cuts on G_n" lemma (Gap (a)). This is the single load-bearing lemma for
   the whole problem — it likely proves BOTH bounds if the upper bound is
   reduced to it.
2. (Upper bound) Pursue either (UB-i) a rank-greedy XY strategy, or (UB-ii)
   a local smoothing monotonicity starting with the n=2 three-piece case.
   If the majorisation conjecture proves out of reach, a direct rank-based
   XY strategy is the fallback.
3. (Easy fix) Add the U(1) boundary case L = 1/2 explicitly (cut one
   half into (1/3, 1/6), D = 1/3) so the n=1 proof is genuinely complete.

Do NOT mark `solved` until both the general lower-bound Case B and the
general upper bound are proved.
