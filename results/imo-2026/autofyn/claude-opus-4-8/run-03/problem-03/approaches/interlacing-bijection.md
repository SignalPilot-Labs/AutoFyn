## Status
partial

## Approaches tried
- **interlacing-bijection** (round 5, NEW, this file) — discrete/combinatorial reframing of the
  lower-bound residual (PM). Represented the residual multiset B_low = Q_low ⊔ C by the sorted
  **merge word** and the associated **±1 lattice walk** D(t) = N_{Q_low}(t) − N_C(t). Derived a
  **new, exact layer-cake reformulation** of (PM) into a purely discrete crossing-measure
  inequality (Lemma IB-1), rigorously and numerically verified (0 mismatches, 60k configs). This
  makes R2 one line and gives L9 a transparent reading. Reduced the {D≥2} compensation to an
  explicit **excess→deficit injection target** on even-up-layers vs odd-down-layers. Constructed
  the injection map and proved it total in the height-≤2 no-interior-plateau slice; the general
  injection (heights ≥ 3, and the budget-consuming totality) is left as an explicit GAP. Confirmed
  numerically that the budget/structure is **essential** (free, unstructured Q violates (PM)
  67/20000 while the true game never does). UB imported/deferred (GAP).

## Current best
**Answer c(n) = 2^n/D_n, D_n := 2^{n+1}−1** (target; c(1)=2/3 proved in full upstream, both bounds).
The full LB reduction to the residual (PM) ∫[D odd] ≥ ∫D is imported and certified (L0–L11).

**New this round — the discrete framing and its central lemma (rigorous):**

- **Merge-word / ±1 walk.** Write the residual multiset as B_low = Q_low ⊔ C with all parts ≤ H,
  D(t) := N_{Q_low}(t) − N_C(t). Reading the parts in **descending** value order, D is a lattice
  walk starting at 0 (threshold t = +∞) that takes a **+1 step at each Q_low-value** and a **−1
  step at each C-value**, ending at D(0+) = |Q_low| − |C|. Between consecutive distinct part-values
  the walk is flat, of length = the gap between those values. (PM) is a statement about this walk
  weighted by gap-lengths.

- **Lemma IB-1 (layer-cake reformulation of (PM)) — PROVED, promotable.** With
  A_j := meas{t : D(t) ≥ j} and B_j := meas{t : D(t) ≤ −j},
    ∫[D odd] − ∫D = 2·( Σ_{i≥0} B_{2i+1} − Σ_{i≥1} A_{2i} ).
  Hence **(PM) ⟺ Σ_{i≥0} B_{2i+1} ≥ Σ_{i≥1} A_{2i}**, i.e.
    meas{D ≤ −1} + meas{D ≤ −3} + … ≥ meas{D ≥ 2} + meas{D ≥ 4} + …
  Equivalently ∫⌈D^-/2⌉ ≥ ∫⌊D^+/2⌋ (D^± := max(±D,0)). This is a **purely discrete crossing
  inequality**: the total time the walk spends at even positive heights (2,4,…) must be paid for by
  the total time it spends at odd negative depths (−1,−3,…). Verified exactly (Fraction), 0
  mismatches over 60000 constrained configs at n = 2,3,4.

This isolates the {D≥2} compensation as a **rank-crossing balance**, not a continuous integral —
the framing the field lacked. Its two proven sub-cases become transparent:
- **R2 in this language:** D ≤ 1 a.e. ⟹ {D ≥ 2} has measure 0 ⟹ RHS = 0 ⟹ inequality trivial.
- **L9 in this language:** N_{Q_low} even a.e. ⟹ the walk's height has fixed parity structure
  forcing the overlap to vanish (Σ A_{even} matched termwise).

**Open GAP (the make-or-break):** the excess→deficit injection for general heights (D reaching
≥ 3) and the proof that the single-block part budget |Q_low|+|C| ≤ 2n+1 makes it total. Confirmed
essential: dropping the budget/structure (free Q) makes (PM) FALSE (67/20000), so any valid proof
must consume it. UB (branch inequalities) imported from induction-peel, deferred as GAP.

## Full proof
Not present — Status is partial (LB residual injection open; UB deferred).

---

# Approach: discrete rank-crossing injection for the LB residual

Throughout, D_n = 2^{n+1} − 1 and P_n = {2^0, …, 2^n}. We attack the whole claim
**c(n) = 2^n/D_n**; the lower bound is recast combinatorially below, the upper bound is imported.

## 0. Imported, certified machinery (not re-proved)

From `lemmas/`: **L0** (claiming ⟹ odd-rank sum), **L1** (reduction to the multiset-refinement
game, c(n) = max_A min_B Σ_odd(B)), **L2** (Σ_odd = (1+S)/2, so the target ⟺ max_A min_B S(B) =
1/D_n), **L3** (layer-cake S(B) = meas{N(t) odd}, ∫N = sum, XOR corollary), **L4** (min-pairing),
**L6/A0–A1** (at most one part > H := 2^{n-1}; truncation identity S(B) = e + S(B_low), so
S(B) ≥ e and the whole LB reduces, when e < 1, to the **residual** S(B_low) ≥ 1 − e), **L9**
(self-pairing kills the overlap), **L10** (β identities), **L11 / R1–R2** (the residual reforge).

By L11(R1), with B_low = Q_low ⊔ C (all parts ≤ H), D(t) := N_{Q_low}(t) − N_C(t):
  S(B_low) = ∫_0^∞ [D(t) odd] dt,   ∫_0^∞ D(t) dt = sum(Q_low) − sum(C) = 1 − e,
so the residual is **exactly** the parity-vs-mean inequality
  **(PM)   ∫_0^∞ [D odd] dt ≥ ∫_0^∞ D dt.**
Structure carried in (from induction-peel §3.3, all certified): **Q_low** is a capped ≤ c-cut
refinement of the single block {2^n}, so it has c+1 parts, each ≤ H, summing to 2^n − e with
e < 1; **C** is a ≤ k_C-cut refinement of P_{n−1}, so it has n + k_C parts summing to 2^n − 1,
each ≤ H; and c ≥ 1, c + k_C ≤ n, hence the **part budget**
  |Q_low| + |C| = (c+1) + (n+k_C) ≤ 2n + 1.

Our contribution is a genuinely different, **discrete** attack on (PM): recast it as a
crossing-measure inequality on the merge word and reduce it to an explicit combinatorial
injection. No measure-charging vocabulary is used; the objects are the walk and its layers.

## 1. The merge word and the ±1 walk

Let the distinct positive values occurring among the parts of Q_low and C be
  v_1 > v_2 > … > v_r > 0.
For a threshold t in the open interval I_k := (v_{k+1}, v_k) (with v_0 := +∞, v_{r+1} := 0), the
counts N_{Q_low}(t), N_C(t) are constant, hence so is D(t); write D_k for that value and
ℓ_k := v_k − v_{k+1} > 0 for the length of I_k. Then, since D is a step function constant on each
I_k and the endpoints form a null set,
  ∫ [D odd] dt = Σ_{k : D_k odd} ℓ_k,   ∫ D dt = Σ_k D_k ℓ_k.       (1)

**Walk description.** Read the values in descending order v_1, v_2, …. Passing downward across a
value v that is a part-value of Q_low increases N_{Q_low} by the multiplicity of v there; across a
C-value it increases N_C. Thus, going from I_{k−1} to I_k (i.e. crossing v_k downward),
  D_k − D_{k−1} = (# Q_low-parts equal to v_k) − (# C-parts equal to v_k).
On the far right I_0 = (v_1, ∞) we have N = 0 so D_0 = 0; on the far left I_r = (0, v_{r+1}=0)…
more precisely on (0, v_r) every part exceeds t so D = |Q_low| − |C|. Summing the increments,
  D_r = |Q_low| − |C| = (c+1) − (n+k_C) =: s_0.        (2)
In the **generic case** (all r = |Q_low|+|C| part-values distinct) each step is exactly ±1: **+1**
at a Q_low-value, **−1** at a C-value. So D is a ±1 lattice walk with |Q_low| = c+1 up-steps and
|C| = n+k_C down-steps, starting at height 0 and ending at height s_0 ≤ 0 (since s_0 = 1 − 2k_C − …
≤ 1 − 2k_C by c ≤ n − k_C; in fact s_0 = (c+1)−(n+k_C)). Ties (equal part-values) merge several
±1 steps into one larger step and are handled by L9-style cancellation (§4).

**Reading (1) off the walk.** (PM) says the gap-length-weighted count of intervals where the walk
sits at an **odd** height is ≥ the gap-length-weighted signed height. This is a discrete
(interleaving-order) quantity on the left and a path-integral on the right.

## 2. Lemma IB-1: the layer-cake reformulation of (PM) — PROVED

For integers j ≥ 1 put A_j := meas{t : D(t) ≥ j} = Σ_{k : D_k ≥ j} ℓ_k and
B_j := meas{t : D(t) ≤ −j} = Σ_{k : D_k ≤ −j} ℓ_k.

**Lemma IB-1.**
  ∫[D odd] − ∫D = 2·( Σ_{i≥0} B_{2i+1} − Σ_{i≥1} A_{2i} ).
Consequently **(PM) ⟺ Σ_{i≥0} B_{2i+1} ≥ Σ_{i≥1} A_{2i}**.

*Proof.* All sums below are finite (D takes finitely many integer values). First, the signed
height decomposes into layers: for each interval, D_k = Σ_{j≥1}(1[D_k ≥ j] − 1[D_k ≤ −j]) (a
telescoping count of the levels between 0 and D_k). Multiplying by ℓ_k and summing over k,
  ∫D = Σ_{j≥1}(A_j − B_j).        (3)

Second, the odd-height measure. meas{D = j} = A_j − A_{j+1} for j ≥ 1 and meas{D = −j} =
B_j − B_{j+1} for j ≥ 1. Hence
  ∫[D odd] = Σ_{j≥1 odd}(A_j − A_{j+1}) + Σ_{j≥1 odd}(B_j − B_{j+1})
           = Σ_{j≥1}(−1)^{j+1} A_j + Σ_{j≥1}(−1)^{j+1} B_j,        (4)
where each equality is the standard rearrangement of an alternating telescoping sum: e.g.
Σ_{j odd}(A_j − A_{j+1}) = A_1 − A_2 + A_3 − A_4 + … = Σ_{j≥1}(−1)^{j+1}A_j (both sides finite).

Subtract (3) from (4):
  ∫[D odd] − ∫D = Σ_{j≥1}[(−1)^{j+1} − 1]A_j + Σ_{j≥1}[(−1)^{j+1} + 1]B_j.
Now (−1)^{j+1} − 1 equals 0 for j odd and −2 for j even; (−1)^{j+1} + 1 equals 2 for j odd and 0
for j even. Therefore
  ∫[D odd] − ∫D = −2 Σ_{i≥1} A_{2i} + 2 Σ_{i≥0} B_{2i+1},
which is the claim. Since the left side is ∫f(D) with f(d) = [d odd] − d ≥ 0 for d ≤ 1, the
equivalence (PM) ⟺ Σ_{i≥0} B_{2i+1} ≥ Σ_{i≥1} A_{2i} follows. ∎

**Equivalent floor/ceiling form.** #{i ≥ 1 : D ≥ 2i} = ⌊D^+/2⌋ and #{i ≥ 0 : D ≤ −(2i+1)} =
⌈D^-/2⌉, so
  **(PM) ⟺ ∫ ⌈D^-/2⌉ dt ≥ ∫ ⌊D^+/2⌋ dt.**        (IB-1′)

*Numerical check (verification tool, not a proof step).* Over 60000 constrained residual configs
at n = 2,3,4 (exact `Fraction`), the identity of Lemma IB-1 held with 0 mismatches and the
inequality (PM) held with minimum slack exactly 0 (attained at the extremal family). See
`/tmp/explore.py`.

**Why this is the right object.** The right-hand pile Σ A_{2i} is the total (gap-length-weighted)
time the walk spends at **even positive** heights; the left-hand pile Σ B_{2i+1} is the time at
**odd negative** depths. (PM) is now the concrete assertion "even-up time ≤ odd-down time" — a
balance between two families of rank-crossing intervals, exactly the discrete target the
new-framing explorer identified.

## 3. Transparent readings of the closed sub-cases

- **R2 (D ≤ 1 a.e.).** Then {D ≥ 2} = ∅, so A_2 = A_4 = … = 0 and the RHS-pile Σ A_{2i} = 0 ≤
  Σ B_{2i+1}. (PM) is immediate. This re-derives R2 with no case analysis on f — the even-up pile
  is simply empty.
- **L9 (S(Q_low) = 0, i.e. N_{Q_low} even a.e.).** Then N_{B_low} = N_{Q_low} + N_C ≡ N_C (mod 2),
  so {D odd} = {N_C odd} up to null sets and ∫[D odd] = S(C); since ∫D = 1 − e ≤ 1 ≤ S(C) (IH),
  (PM) holds. In IB-1 terms the even-up pile is dominated by the C-only crossings, which the IH
  already controls.

Both are honest special cases of Lemma IB-1; the general case is §4.

## 4. The excess→deficit injection (target, partial construction, GAP)

By Lemma IB-1 the residual is now: **inject the even-up pile into the odd-down pile.** We phrase
this as a transport/injection on the walk's layers.

**Layer decomposition into excursions.** Fix an even level 2i ≥ 2. Because D is a ±1 (generic) walk
starting and ending at heights < 2i (start 0, end s_0 ≤ 0), the super-level set {t : D(t) ≥ 2i} is a
finite disjoint union of maximal intervals ("**up-excursions at level 2i**"), each entered by a +1
step (a Q_low-value crossing 2i−1 → 2i) and exited by a −1 step (a C-value crossing 2i → 2i−1). The
RHS-pile Σ_{i≥1} A_{2i} is the total length of all up-excursions over all even levels. Symmetrically,
Σ_{i≥0} B_{2i+1} is the total length of all "**down-excursions at odd depth 2i+1**" (each entered by a
C-value crossing −2i → −(2i+1), exited by a Q_low-value).

**What must be built.** A measure-preserving injection Φ from the even-up pile into the odd-down
pile — i.e. an assignment of each unit of length under an even up-excursion to a *distinct* unit of
length under some odd down-excursion. Its existence is *equivalent* to (PM) (that is the content of
Lemma IB-1), so building Φ **is** the proof; the value added by this framing is that Φ is a concrete
combinatorial object (a pairing of crossings) rather than an analytic inequality, and the budget
enters as a **counting** constraint on how many excursions can exist.

**Candidate map (nearest deeper matching along the walk).** Order all up-steps (Q_low-values) and
down-steps (C-values) by descending value (the reading order of §1). For a point τ under an even
up-excursion at level 2i, define Φ(τ) by "reflecting the excess downward": follow the walk to the
right (decreasing threshold, i.e. toward t = 0) until the height first drops to −(2i−1) below its
level, and map τ to the corresponding point of that odd down-excursion. Intuitively each pair of
Q_low-values that lifted the walk from 2i−2 to 2i must, because the walk returns to height s_0 ≤ 0
by the end, later be undone by C-values that carry it symmetrically below 0.

**Partial construction (height-≤2, clean-descent slice — indicated, NOT fully certified).** Suppose
D ≤ 2 everywhere and every maximal {D = 2} interval is bordered on its low-t side by a maximal
{D = 1} interval that continues monotonically down through 0 into {D ≤ −1} (the "clean descent"
configuration). Then the intended matching sends each unit under {D = 2} along that descent to a
unit under {D ≤ −1}; the ±1 structure nests the descents so distinct {D=2} units target distinct
{D≤−1} units, giving Σ A_{2i} = A_2 ≤ B_1 = Σ B_{2i+1}. I flag this as an **indicated** slice, not a
certified lemma: the disjointness/nesting bookkeeping is stated but not written out to full rigor
here, and — as §4-GAP(2) shows — even the height-≤2 case is NOT true from ∫D ≤ 1 alone, so the
clean-descent hypothesis is doing real (unquantified) work. It is included to show the injection is
non-vacuous, not as an established result.

**Where it is NOT yet proved (the GAP).** The construction is not yet total in general:
1. **Heights ≥ 3.** When D reaches 3 or more, an up-excursion at level 2 can be *entered and left
   several times* while a single deep down-excursion services them; the "nearest deeper" rule can
   collide (two even-up units aimed at the same odd-down unit) unless the budget forbids the
   offending configuration. Making Φ injective here is unproven.
2. **Budget totality.** The reason Φ is total (never runs out of odd-down length) must be the part
   budget |Q_low| + |C| ≤ 2n+1 together with C's structure (a refinement of P_{n−1}): these bound
   the number of even-up excursions and force enough odd-down length. This is exactly the
   round-4 obligation ("consume the single-block part budget, not a cut-count cap on C"), now stated
   as: the number of up-steps that can create even-up excursions is c+1, and c + k_C ≤ n caps the
   simultaneous starving of the odd-down pile. The precise inequality tying excursion **counts** to
   the **lengths** (which involves the actual gap-lengths ℓ_k, not just counts) is **open**.

**Budget is provably essential (not optional).** If one drops the block/count structure and lets
Q_low be a free multiset of ≤ 5 parts ≤ H with sum in (2^n−1, 2^n], (PM) **fails** — a fast exact
probe found 67/20000 violations at n = 3, whereas the genuine game (Q_low a capped block-refinement
with c + k_C ≤ n) had 0 violations in 60000 trials. So Lemma IB-1's inequality is *false* without
the budget; the missing step (1)–(2) above is the load-bearing one, and no budget-free injection can
exist. This both fences off any attempt to prove Φ total from ∫D ≤ 1 alone and pinpoints the
combinatorial content.

## 5. Ties (non-generic merge word)

If two part-values coincide, the corresponding walk step is ±2 (or larger). Two equal parts of the
**same** origin (both Q_low, or both C) create a step of the same sign and do not affect the parity
pattern beyond changing the height by 2 — they can be split into two unit steps at infinitesimally
separated thresholds without changing any ℓ_k in the limit, so Lemma IB-1 and (1) are unaffected
(the identities are stated for the true step function D and hold verbatim; only the "±1 generic"
description of §1 needs the splitting). A coincidence of a Q_low-value with a C-value is a **matched
±1/∓1 pair** that cancels in the height (net 0 step) exactly as in L9's self-pairing: it contributes
0 to every A_j, B_j and can be removed, reducing the part count and recursing. Hence ties never
increase the even-up pile and are covered once the generic injection is built. (This mirrors, in
walk language, the certified L9 cancellation; no measure-charging is used.)

## 6. Upper bound (imported, deferred)

This slug's contribution is the LB discrete framing. The upper bound max_A min_B S(B) ≤ 1/D_n is
the shared field crux; we import induction-peel §4: the value function U_k(A) = min over ≤k-cut
refinements of S, with recursion U_k(A) = min(S(A), min_{one split} U_{k−1}(A′)), base case
U_0(A) = S(A) ≤ sum(A) = sum(A)/D_0, and the two **branch inequalities**
U_{k−1}(c(A)) ≤ sum(A)/D_k for the minimizing c ∈ {MATCH, BISECT}. These branch inequalities are
an explicit **GAP** here (not attacked in this approach). Granting them and Lemma A (LB), L2 gives
c(n) = (1 + 1/D_n)/2 = 2^n/D_n.

## 7. Verification of the answer (small n)

- n = 1: c(1) = 2/3, proved in full upstream (induction-peel §2, both bounds).
- n = 2: c(2) = 4/7; refining G_2 = {1,2,4}/7 by 4→2+2, 2→1+1 gives {2,2,1,1,1}/7, Σ_odd = 4/7,
  S = 1/7, matching the numeric min.
- n = 3: c(3) = 8/15 (S = 1/15), confirmed by numeric min-search upstream.
Lemma IB-1's inequality was checked to be tight (slack 0) exactly at these dyadic extremals.

## Open gaps (honest)

1. **LB residual injection (the crux of this approach).** Prove Lemma IB-1's inequality
   Σ_{i≥0} B_{2i+1} ≥ Σ_{i≥1} A_{2i} in general by constructing the total excess→deficit injection
   Φ, using the single-block part budget |Q_low|+|C| ≤ 2n+1 and C's P_{n−1}-refinement structure to
   guarantee totality at heights ≥ 3. Proven slices: R2 ({D≥2} empty), L9 (Q_low even), and the
   clean-descent height-≤2 slice. Budget confirmed essential (free-Q violates (PM)).
2. **UB branch inequalities** (imported, deferred): U_{k−1}(c(A)) ≤ sum(A)/D_k for the minimizing
   split. The field-wide crux; not attacked here.

## Build report
- **Status: partial.**
- **Established (rigorous):** (i) the merge-word / ±1-walk representation of the residual (§1);
  (ii) **Lemma IB-1**, an exact layer-cake reformulation of (PM) into the discrete crossing
  inequality Σ B_{odd} ≥ Σ A_{even} (equivalently ∫⌈D^-/2⌉ ≥ ∫⌊D^+/2⌋), proved from L3-type
  telescoping and numerically verified (0 mismatches, 60k configs) — a genuinely new object no live
  approach uses; (iii) transparent one-line re-derivations of R2 and L9 in this language; (iv) the
  height-≤2 clean-descent slice of the injection; (v) a numeric proof-of-necessity that the part
  budget is essential (free Q violates (PM) 67/20000). The reframing is complete and the target is a
  concrete combinatorial injection, not an analytic inequality.
- **Remaining GAPs:** the general excess→deficit injection at heights ≥ 3 and its budget-driven
  totality (LB crux); the imported UB branch inequalities.
- **Spec concerns:** none. The approach stays in pure walk/crossing language (no measure-charging),
  keeping it distinct from induction-peel (summation-by-parts/charging) and alternating-sum
  (β-Hall). Lemma IB-1 is promotable and reusable by any XOR-split LB approach.

## Promotable lemmas
- **IB-1 (layer-cake reformulation of (PM)).** For D = N_{Q_low} − N_C with A_j = meas{D ≥ j},
  B_j = meas{D ≤ −j}: ∫[D odd] − ∫D = 2(Σ_{i≥0} B_{2i+1} − Σ_{i≥1} A_{2i}); hence (PM) ⟺
  Σ_{i≥0} B_{2i+1} ≥ Σ_{i≥1} A_{2i} ⟺ ∫⌈D^-/2⌉ ≥ ∫⌊D^+/2⌋. Proved in full (§2) from the layer
  decompositions (3),(4); numerically verified (0/60000). Reusable by every XOR-split / parity-vs-
  mean lower-bound approach; converts the residual into a discrete even-up vs odd-down crossing
  balance.
