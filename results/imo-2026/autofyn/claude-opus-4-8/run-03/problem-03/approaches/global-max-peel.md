## Status
partial

## Approaches tried
- **global-max-peel** (round 3, this file) — unified LOWER-bound induction organized around
  the exact peel-current-max identity S(B) = b_(1) − S(B∖{b_(1)}) and the block/XOR
  decomposition. Outcome: the peel identity is proven and shown to reduce the whole lower
  bound to the single inequality Σ_odd(B) ≥ 2^n (equivalently S(B) ≥ 1). The genuinely new
  deliverable is a **single unconditional inequality — "h ≥ 1 ⟹ S(B) ≥ 1"** — that merges
  the field's entire Case 1 (top piece uncut) together with a large part of Case 2 into ONE
  argument requiring no induction. Base case n = 1 is fully closed. The residual is a strictly
  smaller obligation than the field's Case 2: only the sub-case c_n ≥ 1 AND h < 1 (small top
  shard) remains, and there the binding gap is a budget-cap bound on the layer-cake overlap W
  — the same shared crux the whole field sits on. **Honest verdict:** the global-max/peel
  framing does *not* escape the crux (as the outliner flagged it might not); its value is a
  cleaner, smaller, unconditional reduction of it. Upper bound not attempted (out of scope
  this round).

## Current best
The lower bound c(n) ≥ 2^n/D_n is reduced to the clean statement
  **G(n): every ≤ n-cut refinement B of P_n = {2^0, 2^1, …, 2^n} has S(B) ≥ 1**,
and G(n) is proven **completely for the entire "high-band" regime h ≥ 1** (Lemma H below,
unconditional — no induction, no IH), which subsumes all of the field's Case 1 plus every
Case 2 with a large surviving top shard. Base case n = 1 is fully proven (both c_n = 0 and
c_n = 1). The single remaining obligation for the lower bound is:

> **(GAP-LB)** In the induction step, sub-case c_n ≥ 1 and h < 1 (the top block 2^n is cut and
> its largest shard q_1 satisfies q_1 < 2^{n-1}+1): with S(Rest) ≥ 1 available by the
> induction hypothesis G(n−1), prove S(B) = h + S_low(B_n) + S(Rest) − 2W ≥ 1, where the only
> missing ingredient is an upper bound on the overlap W = meas{t : N_{B_n}(t) odd and
> N_{Rest}(t) odd} strictly better than the trivial W ≤ min(S_low(B_n), S(Rest)). This is the
> same "budget-cap on W" gap the two live approaches (induction-peel A2, alternating-sum G1)
> also carry.

The upper bound c(n) ≤ 2^n/D_n (that XY can hold Liu Bang to exactly this against every A) is
entirely open in this approach.

## Full proof
Not present — Status is partial (GAP-LB open; upper bound not attempted).

---

# Work: unified peel-current-max lower bound

Throughout, D_n := 2^{n+1} − 1 and P_n := {2^0, 2^1, …, 2^n} (a multiset with Σ = D_n).
For a finite multiset X of positive reals, sorted x_(1) ≥ x_(2) ≥ … , define the **potential**
S(X) := Σ_i (−1)^{i+1} x_(i) = x_(1) − x_(2) + x_(3) − …, and Σ_odd(X) := x_(1)+x_(3)+x_(5)+… .
We use, as black boxes, the certified project lemmas:
L0 (claim value = odd-rank sum), L1 (reduction to the multiset-refinement game
c(n) = max_A min_B Σ_odd(B)), L2 (Σ_odd = (Σ + S)/2, hence with Σ=1 the target
c(n)=2^n/D_n ⟺ max_A min_B S(B) = 1/D_n), L3 (layer-cake identity
S(X) = meas{t>0 : N_X(t) odd}, N_X(t) = #{parts of X exceeding t}, and its XOR corollary),
and L4 (min-pairing). See `results/imo-2026-03/lemmas/`.

## §1. What the lower bound requires

By L1–L2, to prove the lower bound c(n) ≥ 2^n/D_n it suffices to exhibit **one** choice of A
for which min_B S(B) ≥ 1/D_n. Take A = D_n^{-1}·P_n (Liu Bang cuts [0,1] at the n dyadic
points that produce interval lengths 2^0/D_n, …, 2^n/D_n; these are n cut points, legal). Any
Xiang-Yu response is a ≤ n-split refinement of A. Because S is homogeneous of degree 1
(S(λX) = λ S(X), immediate from the definition), min_B S(B) ≥ 1/D_n for this scaled A is
equivalent, after multiplying through by D_n, to the following statement about the **unscaled**
set P_n:

> **G(n).** Every multiset B obtained from P_n = {2^0, …, 2^n} by at most n split operations
> (each replacing one current part x by two positive parts summing to x) satisfies S(B) ≥ 1.

Indeed, if G(n) holds then for the scaled A, S(B_scaled) = S(B_unscaled)/D_n ≥ 1/D_n, whence
by L2 (with Σ = 1) Σ_odd(B_scaled) = (1 + S)/2 ≥ (1 + 1/D_n)/2 = (D_n+1)/(2D_n) = 2^n/D_n =
c(n). So **G(n) ⟹ lower bound.** The rest of this document works toward G(n).

**Block structure.** A ≤ n-split refinement B of P_n partitions into blocks
B = B_0 ⊔ B_1 ⊔ … ⊔ B_n, where block B_j is the refinement of the original part 2^j; it sums
to 2^j and consists of 1 + c_j parts, where c_j ≥ 0 is the number of splits spent inside it
and c := Σ_j c_j ≤ n. Every part of B_j is ≤ 2^j.

## §2. The peel-current-max identity and its meaning

**Lemma P (peel-max).** For any finite multiset X with global maximum m = x_(1),
S(X) = m − S(X ∖ {m}).

*Proof.* Write X sorted x_(1) ≥ x_(2) ≥ … . Then X ∖ {m} sorted is x_(2) ≥ x_(3) ≥ … , and
S(X ∖ {m}) = Σ_{i≥2} (−1)^{(i−1)+1} x_(i) = Σ_{i≥2} (−1)^{i} x_(i). Hence
m − S(X∖{m}) = x_(1) − Σ_{i≥2}(−1)^{i} x_(i) = x_(1) + Σ_{i≥2}(−1)^{i+1} x_(i)
= Σ_{i≥1}(−1)^{i+1} x_(i) = S(X). No strict-max hypothesis is needed: sorting is stable, so
ties among the parts do not affect the argument. ∎

**Consequence (equivalent form of G(n)).** By L2 applied to B (with Σ = D_n),
Σ_odd(B) = (D_n + S(B))/2, so S(B) ≥ 1 ⟺ Σ_odd(B) ≥ (D_n+1)/2 = 2^n. Thus:

> **G(n) ⟺ Σ_odd(B) ≥ 2^n for every ≤ n-cut refinement B of P_n.**

Lemma P re-expresses the per-step obligation cleanly: peeling m = b_(1) off B, S(B) ≥ 1 is
exactly S(B ∖ {m}) ≤ m − 1. We record this because it is the honest organizing identity of
this approach — but we also flag, up front, that this identity is by itself only a *cosmetic*
reduction: unwinding S(B∖{m}) ≤ m−1 via L2 gives back Σ_odd(B) ≥ 2^n, i.e. G(n) again. The
content must come from the block/superincreasing structure, developed next. This is stated
plainly here (per the outliner's caveat: "if the induction is forced back into a case split on
m's origin it has bought nothing — report that honestly"). The genuine gain of this approach
is §4's *unconditional* Lemma H, which is what merges the field's two cases.

## §3. Block/XOR decomposition and band confinement of the overlap

Split B into its top block and the rest:
  B = B_n ⊔ Rest,  Rest := B_0 ⊔ … ⊔ B_{n−1}.
Rest is a ≤ (c − c_n)-cut refinement of {2^0, …, 2^{n−1}} = P_{n−1}, with total mass
Σ Rest = 2^n − 1, and **every part of Rest is ≤ 2^{n−1}.**

By the XOR corollary of L3 (N_B = N_{B_n} + N_{Rest}, so N_B(t) is odd iff exactly one of
N_{B_n}(t), N_{Rest}(t) is odd):
  (XOR)  S(B) = S(B_n) + S(Rest) − 2W,  W := meas{ t : N_{B_n}(t) odd AND N_{Rest}(t) odd }.

**Band confinement of W (structural fact, from the explorer, made precise here).** Every part
of Rest is ≤ 2^{n−1}, so for t ≥ 2^{n−1} no part of Rest exceeds t, i.e. N_{Rest}(t) = 0
(even). Hence the integrand of W vanishes for t ≥ 2^{n−1}: **W is confined to the low band
t < 2^{n−1}.** Consequently, writing
  S_low(B_n) := meas{ t < 2^{n−1} : N_{B_n}(t) odd },
we have W ≤ S_low(B_n) and W ≤ meas{t : N_{Rest}(t) odd} = S(Rest); therefore
  (†)  W ≤ min( S_low(B_n), S(Rest) ).
Also all of S(Rest)'s odd region lies in t < 2^{n−1} (parts of Rest ≤ 2^{n−1}).

**The high-band term h.** At most one part of B_n can exceed 2^{n−1} (two such parts would sum
> 2^n = Σ B_n). Hence for t ≥ 2^{n−1}, N_{B_n}(t) ∈ {0,1}, and it equals 1 exactly on
[2^{n−1}, q_1) where q_1 := max(B_n). So the measure of B_n's odd region **above** 2^{n−1} is
  h := max( q_1 − 2^{n−1}, 0 ),
and S(B_n) = h + S_low(B_n) (high band + low band). Substituting into (XOR):
  (‡)  S(B) = h + S_low(B_n) + S(Rest) − 2W,  with W confined to t < 2^{n−1}.

*(All of (XOR), (†), (‡), the band confinement, and the "at most one part > 2^{n−1}" claim
were verified numerically: 0 discrepancies over 80 000 random Case-B refinements, n = 1..4.)*

## §4. Main Lemma: the unified high-band inequality (unconditional)

**Lemma H.** If h ≥ 1 then S(B) ≥ 1. This needs no induction hypothesis.

*Proof.* By (†), W ≤ min(S_low(B_n), S(Rest)), so
  S_low(B_n) + S(Rest) − 2W ≥ S_low(B_n) + S(Rest) − 2·min(S_low(B_n), S(Rest))
                             = | S_low(B_n) − S(Rest) | ≥ 0.
Plugging into (‡): S(B) = h + [S_low(B_n) + S(Rest) − 2W] ≥ h + 0 = h ≥ 1. ∎

**Corollary H1 (subsumes the field's Case 1 — top piece uncut).** If c_n = 0, then B_n =
{2^n}, so q_1 = 2^n and h = 2^n − 2^{n−1} = 2^{n−1} ≥ 1 (for n ≥ 1). By Lemma H, S(B) ≥ 1.

So the entire "top piece survives uncut" case — which both live approaches prove as a separate
Case 1 — is a *single instance* of the unconditional Lemma H, together with every Case-2
configuration in which the largest surviving shard of the top block is ≥ 2^{n−1} + 1. This is
the concrete unification this approach delivers: **one inequality, no case split on the origin
of the max, no induction.** (Numerically, Lemma H's hypothesis-conclusion pair was checked
directly: over the 80 000 trials no configuration with h ≥ 1 ever had S(B) < 1.)

## §5. Base case n = 1 (complete)

Refinements of P_1 = {1, 2} with ≤ 1 cut. Either c_1 = 0 (top block uncut): Corollary H1 gives
S ≥ 1. Or c_1 = 1: the part 2 is split into q_1 ≥ 2 − q_1 with q_1 ∈ [1, 2), and Rest = {1}
(no budget left). Sorted B = {q_1, 1, 2 − q_1} (since 2 − q_1 ≤ 1 ≤ q_1), so
S(B) = q_1 − 1 + (2 − q_1) = 1 ≥ 1. (If q_1 = 1, B = {1,1,1}, S = 1 as well.) Hence G(1) holds:
every ≤ 1-cut refinement of {1,2} has S ≥ 1, with equality achievable. ∎ (base case)

## §6. Induction step and the residual gap

Assume G(n−1): every ≤ (n−1)-cut refinement of P_{n−1} has S ≥ 1. Let B be a ≤ n-cut
refinement of P_n; decompose as in §3.

- **If c_n = 0:** Corollary H1 gives S(B) ≥ 1. (No IH needed.)
- **If c_n ≥ 1:** then Rest uses ≤ n − c_n ≤ n − 1 cuts, so by the induction hypothesis
  **S(Rest) ≥ 1**. Two sub-cases on the high-band term:
  - **h ≥ 1:** Lemma H gives S(B) ≥ 1 (again unconditional; the IH is not even needed).
  - **h < 1** (i.e. q_1 < 2^{n−1} + 1, the top block is cut into small shards): here
    S(Rest) ≥ 1 is available, and (‡) reads S(B) = h + S_low(B_n) + S(Rest) − 2W. **This is
    the one place the argument does not close.** The trivial bound (†) W ≤ min(S_low(B_n),
    S(Rest)) yields only S(B) ≥ h + |S_low(B_n) − S(Rest)|, which is not ≥ 1 in general
    (numerics: |S_low(B_n) − S(Rest)| can be < 1 while a *smaller* actual W keeps
    S(B) = 1 exactly). What is needed is a genuine upper bound on the overlap W driven by the
    **cut budget** on Rest — each of the ≤ n − 1 cuts on Rest adds at most one interval to
    Rest's odd region, capping how much of B_n's low-band odd region W can cover. Establishing
    W ≤ (h + S_low(B_n) + S(Rest) − 1)/2 = (S(B_n)+S(Rest)−1)/2 closes it. This is exactly
    **GAP-LB**, and it coincides with the shared crux of the field (induction-peel Sub-claim
    A2 / alternating-sum G1).

**Status of the induction:** complete except for the single sub-case (c_n ≥ 1, h < 1). Under
the trivial-W bound the induction goes through in every other configuration, and Lemma H
disposes of the whole h ≥ 1 world (including all uncut-top configurations) unconditionally.

## §7. Honest assessment (as required by the dispatch)

- **Which bound:** LOWER bound only, c(n) ≥ 2^n/D_n, and even that is proven only *modulo*
  GAP-LB (fully for n = 1, and for all n in the regime h ≥ 1).
- **What is genuinely new / the unification claim:** Lemma H is an *unconditional* inequality
  that merges the entire "top piece uncut" case with a large part of the "top piece cut" case
  into one line, with no induction and no case split on where the global max lives. This is a
  strictly cleaner and smaller reduction than the field's Case 1 / Case 2 dichotomy: after
  Lemma H, the ONLY residual is the low-band overlap bound in the single sub-case c_n ≥ 1,
  h < 1.
- **What it did NOT buy (reported honestly):** the peel-current-max identity (Lemma P) is,
  by itself, cosmetic — it re-expresses G(n) as Σ_odd(B) ≥ 2^n, the same inequality. Peeling
  by the *global* max does not make the residual multiset a refinement of a superincreasing
  set (the max wanders between blocks when the top is shredded), so the promised
  "single-argument-for-both-cases via peeling" does not by itself close Case 2; the real
  content lives in §3–§4's block/XOR/band decomposition, and the binding low-band overlap
  bound is the field's shared crux. Global-max peeling does **not** escape it.
- **Upper bound:** not attempted here; remains open (the full problem needs
  c(n) ≤ 2^n/D_n via a Xiang-Yu strategy against arbitrary A).

## Promotable lemmas
- **Lemma P (peel-max identity).** For any finite multiset X with max m: S(X) = m − S(X∖{m}).
  Proven in full in §2 (stable-sort reindexing; no strict-max needed). Reusable everywhere.
- **Lemma H (unconditional high-band inequality).** For a ≤ n-cut refinement B of P_n with top
  block B_n and Rest = B∖B_n (all parts ≤ 2^{n−1}), writing q_1 = max(B_n) and
  h = max(q_1 − 2^{n−1}, 0): if h ≥ 1 then S(B) ≥ 1 — with no induction hypothesis. Proven in
  full in §4 from the XOR decomposition (L3 corollary) and the band confinement of the overlap
  W. In particular this covers every configuration with the top part uncut (Corollary H1),
  giving a one-line, induction-free proof of the field's entire "Case 1". Reusable by
  induction-peel (its Sub-claim A2 high-band sub-case) and alternating-sum-potential (G1).
- **Band-confinement fact.** For B = B_n ⊔ Rest a ≤ n-cut refinement of P_n, the layer-cake
  overlap W = meas{t : N_{B_n}(t) odd ∧ N_{Rest}(t) odd} is confined to t < 2^{n−1}, and at
  most one part of B_n exceeds 2^{n−1}, so S(B) = h + S_low(B_n) + S(Rest) − 2W with W
  confined to the low band (identity (‡), §3). Proven in full, numerically verified. This is
  the exact structural isolation both live approaches want.
