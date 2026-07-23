## Status
partial

## Approaches tried
- **upper-vertex-reduction** (round 7) — PARTIAL. Recast IH(q) as "f ≤ 1/D on the compact polytope K_q",
  proved f continuous with the min attained (Berge; §A), proved every vertex satisfies f ≤ 1/D
  (Lemma VertexFace), and reduced IH(q) to the single statement **(V): f attains its max on K_q at a
  vertex**. (V) was the blocking gap; the outline's PL-marginal justification for (V) is FALSE
  (partial-minimisation preserves PL only under joint convexity; A = μ{N odd} is non-convex). Honest
  partial.
- **upper-vertex-reduction** (round 8, THIS ROUND) — PARTIAL, spine rebuilt, gap shrunk cleanly.
  **Replaced (V) entirely** with a rigorous **1-homogeneity + σ-face migration** reduction (no
  vertex-attainment, no PL, no convexity): (i) proved f(λb) = λ f(b) on the positive hard-regime cone
  (Lemma f-homogeneous); (ii) proved that any K_q point below the σ-face rescales UP onto the σ-face
  with f weakly larger, so max_{K_q} f = max_{σ-face ∩ K_q} f (Lemma σ-migration). This validly
  bypasses the false-marginal-PL trap. On the σ-face I closed tiers (a) b_1 large and (b) b_2 large via
  certified IH-reducible → IH(q−1), and I NEWLY closed two sub-slices of the flat residual:
  **c1** (b_1 ≥ S/2) by generalized GreedyCascade (A = 2b_1 − S ≤ 1/D) and **c2a** (b_2 ≥ (S−b_1)/2) by
  a new [halve b_1; greedy-cascade b_2] strategy (A = 2b_2 − (S−b_1) ≤ 1/D, using b_2 ≤ 2^{q−2}/D).
  **Sole open gap:** the flat residual sub-slice **c2b** = {b_1 < S/2 AND b_2 < (S−b_1)/2}, q ≥ 5 — the
  bulk of the flat residual. A three-level extension FAILS (the level-3 greedy value 2b_3 − s_3 is
  unbounded because b_3 is not dyadically bounded; verified numerically, worst fixed-strategy A ≈ 4 vs
  optimum ≈ 0.16). Honestly the crux is still an adaptive cascade with no closed form; min-A optimum is
  ≈ 0.16–0.47 ≪ 1 (large margin), so a strategy exists but its uniform construction is unproven.

## Current best
**The whole Case-B hard-regime upper bound for all n reduces — with NO vertex-attainment, NO PL, NO
convexity — to a single explicit combinatorial slice, and everything except that slice is proven.**

Precisely (all imports certified):

- **Setup.** After the certified reductions (Reduction 1: Case B ⟹ p = n+1; Reduction 2 + Lemma H peel
  the easy sub-cases), the open upper-bound core is **IH(q)** for all q ≥ 2:
  *for q pieces b_1 ≥ … ≥ b_q with b_q ≥ 1/D, all consecutive gaps ≥ 1/D, and S = Σ b_i ≤ (2^q−1)/D,
  XY forces A = μ(⊕_i [0,b_i]) ≤ 1/D using ≤ q−1 cuts.* (D = 2^{n+1}−1; A by Lemma X; IH(q≤4)
  certified.) IH(q) ⟺ f ≤ 1/D on K_q, where f(b) = min over ≤ q−1 XY cut-strategies of A and
  K_q = {b : b_i − b_{i+1} ≥ 1/D, b_q ≥ 1/D, Σ b_i ≤ (2^q−1)/D}.

- **The spine (this round, proved in §A–§E below).**
  1. f is continuous on the compact K_q and the min is attained (certified f-continuous-attained; §A).
  2. **f is 1-homogeneous:** f(λb) = λ f(b) for λ > 0 on the positive cone (Lemma f-homogeneous; §B).
  3. **σ-face migration:** every K_q point with Σ b_i < S := (2^q−1)/D rescales up to a σ-face point
     with f weakly larger, so **max_{K_q} f = max_{σ-face ∩ K_q} f** (Lemma σ-migration; §C). *This
     replaces the round-7 open (V).*
  4. On the σ-face (Σ = S) split by (b_1, b_2) tiers (§D):
     (a) b_1 > 2^{q-1}/D → IH-reducible halve-branch → IH(q−1). [certified]
     (b) b_2 > 2^{q-2}/D (and b_1 ≤ 2^{q-1}/D) → IH-reducible cut-at-b_2 branch → IH(q−1). [certified]
     (c) flat residual: b_1 ≤ 2^{q-1}/D AND b_2 ≤ 2^{q-2}/D.
  5. Flat residual (§E) split by dominance:
     (c1) b_1 ≥ S/2 → generalized GreedyCascade → A = 2b_1 − S ≤ 1/D. [PROVED §E1]
     (c2a) b_1 < S/2 AND b_2 ≥ (S−b_1)/2 → [halve b_1; greedy b_2] → A = 2b_2 − (S−b_1) ≤ 1/D.
           [PROVED §E2, new this round]
     (c2b) b_1 < S/2 AND b_2 < (S−b_1)/2 → **OPEN (q ≥ 5)**; for q = 4 covered by certified IH4-flat.

- **THE SOLE GAP (c2b).** In the flat residual with both top pieces non-dominant, no proven uniform
  XY strategy is known for q ≥ 5. The optimum is adaptive (min-A ≈ 0.16–0.47 ≪ 1 numerically, so XY
  CAN force A well below 1/D, but the construction has no closed form and the naive multi-level cascade
  overshoots). **This is the blocking gap; Status is partial.** No overclaim.

## Detailed development

Throughout D = 2^{n+1}−1, c(n) = 2^n/D, S := (2^q−1)/D. By Lemma G1 (certified) LB collects the
odd-ranked pieces; by Lemma R (certified) O = (1+A)/2 with A = μ{t : N(t) odd} the sorted alternating
sum, evaluated by Lemma X (certified) as A = μ(⊕_i [0,ℓ_i]). The XY-goal O ≤ c(n) ⟺ **A ≤ 1/D**.
Reduction 1 (certified) confines Case B to p = n+1 pieces; write q = n+1 (XY has q−1 = n cuts). All of
§A–§E work at the general induction level q (fixed D), with base cases IH(q ≤ 4) certified.

### §A. f is continuous on K_q and the min is attained (certified import)

This is the certified Lemma **f-continuous-attained**. There are finitely many combinatorial cut
patterns; for each, the admissible cut positions form a compact set varying continuously in b, and
A(b, positions) is jointly continuous; by the Berge Maximum Theorem the pattern-value is continuous
with the min attained (Weierstrass), and f is the minimum of finitely many continuous functions, hence
continuous with its value attained. In particular f attains a maximum on the compact K_q, and IH(q) is
the statement that this maximum is ≤ 1/D. ∎ (imported)

### §B. Lemma f-homogeneous: f(λb) = λ f(b)

*Lemma (f-homogeneous).* For every b in the positive cone {b_1 ≥ … ≥ b_q > 0} and every λ > 0,
f(λb) = λ f(b).

*Proof.* Parametrise an XY strategy on a piece vector by (P, φ), where P is a combinatorial cut pattern
(which piece each of the ≤ q−1 cuts acts on, in order) and φ assigns to each cut a *fraction*
ρ ∈ (0,1) determining its position: a cut on a current part of length L is placed at absolute position
ρL, splitting it into (ρL, (1−ρ)L). This parametrisation is **scale-free**: the admissible set of
(P, φ) — patterns and fractions in (0,1) — does not depend on the piece vector.

Fix a strategy (P, φ). Run it on b and on λb simultaneously. By induction on the number of cuts
executed, every current part when running on λb equals λ times the corresponding current part when
running on b: the initial parts are b_i vs λb_i; and a cut with fraction ρ sends a part x to (ρx,
(1−ρ)x), so if the two runs have parts x and λx, the resulting parts are (ρx,(1−ρ)x) and
(ρ·λx,(1−ρ)·λx) = λ·(ρx,(1−ρ)x). Hence the final multiset of parts on λb is exactly λ times (each
length) the final multiset on b.

The score A is the alternating sum of the sorted-descending distinct surviving lengths (equivalently
A = μ(⊕_part [0, part]) by Lemma X); scaling every length by λ scales every sorted length by λ, scales
the measure of ⊕_part [0, λ·part] = λ·(⊕_part [0,part]) by λ, so
A(λb, (P,φ)) = λ·A(b, (P,φ)) for every fixed strategy.

Therefore
  f(λb) = min_{(P,φ)} A(λb,(P,φ)) = min_{(P,φ)} λ·A(b,(P,φ)) = λ·min_{(P,φ)} A(b,(P,φ)) = λ f(b),
using λ > 0 (so min commutes with multiplication by λ) and that the strategy set is the same for b and
λb. ∎

*(Watch: this is homogeneity on the positive CONE, not on K_q as a set — K_q's constraints Σ ≤ S and
b_q ≥ 1/D are not scale-invariant. Homogeneity is used only in §C to push the max onto the σ-face.)*

### §C. Lemma σ-migration: the max of f migrates onto the σ-face

*Lemma (σ-migration).* Let S = (2^q−1)/D and let the σ-face be
Φ := {b ∈ K_q : Σ b_i = S}. Then max_{K_q} f = max_{Φ} f.

*Proof.* Since Φ ⊆ K_q, max_Φ f ≤ max_{K_q} f. For the reverse, take any b ∈ K_q with
s := Σ b_i. By definition of K_q, s ≤ S. If s = S then b ∈ Φ. If s < S, set the scale factor
c := S/s > 1 and b' := c·b. We check b' ∈ Φ:
  - *ordering:* c > 0 preserves b'_1 ≥ … ≥ b'_q;
  - *gaps:* b'_i − b'_{i+1} = c(b_i − b_{i+1}) ≥ c·(1/D) > 1/D ≥ 1/D ✓ (gaps scale UP);
  - *floor:* b'_q = c·b_q ≥ c·(1/D) > 1/D ≥ 1/D ✓ (floor scales UP);
  - *sum:* Σ b'_i = c·s = S ✓, so b' lies on the σ-face.
Thus b' ∈ Φ ⊆ K_q. By Lemma f-homogeneous (§B), applicable since b lies in the positive cone
(b_q ≥ 1/D > 0), f(b') = c·f(b). As c > 1 and f(b) ≥ 0 (A is a measure, so A ≥ 0, hence f ≥ 0),
f(b') = c f(b) ≥ f(b).

Hence every b ∈ K_q is weakly dominated in f-value by a point of Φ. Taking suprema (both attained by
§A, f continuous on compacta), max_{K_q} f ≤ max_Φ f. Combined with the reverse inequality,
max_{K_q} f = max_Φ f. ∎

*Consequence (replaces (V)).* IH(q) ⟺ f ≤ 1/D on K_q ⟺ **f ≤ 1/D on the σ-face Φ**. No
vertex-attainment, no piecewise-linearity, and no convexity of f is used — only 1-homogeneity and
monotone rescaling. The round-7 open statement (V) is bypassed, not proved.

### §D. σ-face tiers (a),(b): reduction to IH(q−1) via certified IH-reducible

Work on Φ, so Σ b_i = S = (2^q−1)/D. Recall certified **IH-reducible**: if
S − max(b_1, 2b_2) < (2^{q−1}−1)/D, one pair-cancelling cut drops the position to a valid IH(q−1)
instance, whence IH(q−1) gives A ≤ 1/D with ≤ q−1 cuts. Since S − max(b_1,2b_2) = min(S−b_1, S−2b_2):

- **Tier (a): b_1 > 2^{q-1}/D.** Then S − b_1 < (2^q−1)/D − 2^{q-1}/D = (2^{q-1}−1)/D, so the
  hypothesis of IH-reducible holds (halve-b_1 branch). By IH(q−1), A ≤ 1/D. [certified]
- **Tier (b): b_2 > 2^{q-2}/D (and b_1 ≤ 2^{q-1}/D).** Then 2b_2 > 2^{q-1}/D, so
  S − 2b_2 < (2^q−1)/D − 2^{q-1}/D = (2^{q-1}−1)/D, again satisfying IH-reducible (cut-at-b_2 branch).
  By IH(q−1), A ≤ 1/D. [certified]

The complement is the **flat residual (c):** b_1 ≤ 2^{q-1}/D AND b_2 ≤ 2^{q-2}/D (with Σ = S). Note the
threshold algebra: on Φ, b_1 ≤ 2^{q-1}/D ⟺ S − b_1 ≥ (2^{q-1}−1)/D, and b_2 ≤ 2^{q-2}/D ⟺
S − 2b_2 ≥ (2^{q-1}−1)/D; so (c) is exactly the complement of IH-reducible's hypothesis. Tiers (a),(b)
and (c) are jointly exhaustive and pairwise disjoint by construction.

### §E. Flat residual (c): dominance split

Assume b ∈ Φ flat: Σ = S = (2^q−1)/D, b_1 ≤ 2^{q-1}/D, b_2 ≤ 2^{q-2}/D, gaps ≥ 1/D, b_q ≥ 1/D.

#### §E1. Sub-slice c1: b_1 ≥ S/2 (generalized GreedyCascade) — CLOSED

*Claim.* If b_1 ≥ S/2, then XY forces A = 2b_1 − S ≤ 1/D with ≤ q−1 cuts.

*Proof.* This is GreedyCascade with total mass S in place of 1 (the certified proof used Σ = 1 only via
the identity r_p = 2b_1 − Σ and the legality bound b_1 ≥ Σ/2; both are stated in terms of the actual
total, so the argument is verbatim with Σ = S). Explicitly: set r_1 = b_1; for j = 1,…,q−1 cut the
running leftover r_j at position b_{j+1}, giving a fragment of length b_{j+1} and leftover
r_{j+1} = r_j − b_{j+1}. Then r_j = b_1 − (b_2+…+b_j), and legality (0 < b_{j+1} ≤ r_j) holds because
b_1 ≥ S/2 ≥ S − b_1 = b_2+…+b_q ≥ b_2+…+b_{j+1}. Each length b_2,…,b_q appears exactly twice (once
intact, once as a fragment of b_1), so by Lemma X those pairs cancel and only the final leftover
r_q = b_1 − (b_2+…+b_q) = b_1 − (S − b_1) = 2b_1 − S survives: A = μ([0, 2b_1 − S]) = 2b_1 − S. Uses
q−1 cuts. Finally, using the flat bound b_1 ≤ 2^{q-1}/D = (S + 1/D)/2 (indeed
(S + 1/D)/2 = ((2^q−1)+1)/(2D) = 2^q/(2D) = 2^{q-1}/D):
  A = 2b_1 − S ≤ 2·2^{q-1}/D − S = 2^q/D − (2^q−1)/D = 1/D.
And A = 2b_1 − S ≥ 0. Hence 0 ≤ A ≤ 1/D. ∎

#### §E2. Sub-slice c2a: b_1 < S/2 AND b_2 ≥ (S−b_1)/2 — CLOSED (new this round)

*Claim.* If b_1 < S/2 and b_2 ≥ (S−b_1)/2, then XY forces A = 2b_2 − (S−b_1) ≤ 1/D with ≤ q−1 cuts.

*Proof.* XY plays the following q−1 cuts.
  (1) **Halve b_1** into (b_1/2, b_1/2). By Lemma X this pair XOR-cancels, contributing nothing to A.
      (1 cut.)
  (2) **Greedy-cascade b_2 through b_3,…,b_q** (as in §E1, but with b_2 as the cascaded piece over the
      sub-multiset {b_2,…,b_q} of total mass s' := S − b_1): set r_1 = b_2; for j = 2,…,q−1 cut the
      running leftover at b_{j+1}, producing fragment b_{j+1} and leftover r = b_2 − (b_3+…+b_{j+1}).
      This uses q−2 cuts.

  *Legality.* At each step need the leftover ≥ the next piece: b_2 − (b_3+…+b_j) ≥ b_{j+1}, i.e.
  b_2 ≥ b_3+…+b_{j+1}. Since b_2 ≥ (S−b_1)/2 = s'/2 and s' = b_2 + (b_3+…+b_q), the condition
  b_2 ≥ s'/2 gives b_2 ≥ b_3+…+b_q ≥ b_3+…+b_{j+1}. ✓

  *Final multiset.* b_1's two halves cancel; each of b_3,…,b_q appears twice (intact + fragment of b_2)
  and cancels by Lemma X; the only survivor is the final leftover
  r_q = b_2 − (b_3+…+b_q) = b_2 − (s' − b_2) = 2b_2 − s' = 2b_2 − (S − b_1) ≥ 0 (by b_2 ≥ s'/2). Hence
  A = μ([0, 2b_2 − (S−b_1)]) = 2b_2 − (S − b_1). Total cuts = 1 + (q−2) = q−1. ✓

  *Bound.* Using the flat bound b_2 ≤ 2^{q-2}/D and S = (2^q−1)/D:
    A = 2b_2 − S + b_1 ≤ 2·2^{q-2}/D − (2^q−1)/D + b_1 = 2^{q-1}/D − (2^q−1)/D + b_1
      = b_1 − (2^{q-1}−1)/D ≤ 2^{q-1}/D − (2^{q-1}−1)/D = 1/D,
  the last step by the flat bound b_1 ≤ 2^{q-1}/D. And A ≥ 0. Hence 0 ≤ A ≤ 1/D. ∎

*(Both §E1 and §E2 verified numerically: over configs biased to their slivers, max A ≈ 0.64 (c1) and
≈ 0.45 (c2a) at q = 5, both ≤ 1/D in scaled units. They are however *thin* slivers of the flat
residual — b_1 ≥ S/2 requires b_1 ∈ [S/2, (S+1/D)/2], a window of width 1/(2D); the bulk of the flat
residual lies in c2b below.)*

#### §E3. Sub-slice c2b: b_1 < S/2 AND b_2 < (S−b_1)/2 — OPEN for q ≥ 5

This is the sole remaining gap. Structurally: both top pieces are *non-dominant* — b_1 is less than
half the total, and b_2 is less than half the remaining total after removing b_1. For q = 4 the
certified **IH4-flat** lemma settles the entire flat residual (its 3-cut singleton strategy plus the
δ-split), so c2b is closed at q = 4. For q ≥ 5 it is open, for the following honest reasons.

- *The two-level cascade does not extend to level 3.* The natural continuation — halve b_1, halve b_2,
  then greedy-cascade b_3 — gives A = 2b_3 − (S − b_1 − b_2), which the flat constraints do NOT bound
  by 1/D: the value bound in §E1/§E2 used the *dyadic* caps b_1 ≤ 2^{q-1}/D and b_2 ≤ 2^{q-2}/D, but
  b_3 is only constrained by b_3 < b_2 ≤ 2^{q-2}/D, not by 2^{q-3}/D. Numerically this fixed
  "halve-until-dominant" strategy overshoots badly (worst A ≈ 4.0 at q = 5, vs the true optimum
  ≈ 0.16). So no uniform ≥3-level greedy cascade closes c2b.

- *The fixed-point obstruction (recorded r6) recurs here.* After halving b_1, the active sub-multiset
  {b_2,…,b_q} has sum S − b_1 ≥ (2^{q-1}−1)/D (equality of the flat boundary), i.e. it sits AT or ABOVE
  the IH(q−1) sum boundary, so it is not a valid IH(q−1) instance; the geometric config
  (2^{q-1},…,2,1)/D is the exact fixed point of the halve-largest recursion. (The geometric config
  itself is not in c2b — it has b_1 = 2^{q-1}/D ≥ S/2, so it is closed by c1/§E1 with A = 1/D exactly.)

- *A strategy provably exists but is adaptive.* An exact min-A search (bounded, exact evaluator by
  Lemma X, ≤ 200 samples per config, respecting the no-large-grid rule) over flat-residual configs at
  q = 5,6,7 gives min A ≈ 0.16–0.47 ≪ 1 in scaled units (1/D scaled = 1), with the geometric vertex the
  unique config attaining exactly 1 (and it lives in c1). So XY *can* force A well below 1/D throughout
  c2b — the target is true with wide margin — but the optimal cut pattern varies with b (adaptive
  δ-splits, no single combinatorial template), and no uniform construction with a clean proof is known.
  This is the same adaptive fragment-cascade wall flagged since r6/r7.

**Honest verdict.** The spine is now clean and correct: IH(q) for all q reduces — with no
vertex/PL/convexity assumption — to bounding f on the σ-face, and the σ-face casework closes every tier
except the single explicit slice c2b (q ≥ 5). c2b remains the blocking gap. Status: **partial**.

### §F. Machine checks (support only; §B–§E2 stand without them)

- f-homogeneous: for a fixed strategy at q = 4, A(λb) = λ·A(b) to machine precision across random λ and
  strategies (also independently verified by the outline-reviewer).
- σ-migration: rescaling an interior K_q point up to the σ-face weakly increases f (verified).
- §E1 (c1): worst A ≈ 0.643 ≤ 1 over 118 sliver configs at q = 5.
- §E2 (c2a): worst A ≈ 0.449 ≤ 1 over 282 sliver configs at q = 5.
- §E3 (c2b): "halve-until-dominant" fixed strategy overshoots (worst A ≈ 4.0), but exact min-A ≈ 0.16
  at the same config — confirming c2b's optimum is ≪ 1 but adaptive.

## Full proof
Not present — Status is partial. IH(q) for q ≥ 5 is reduced (with NO vertex/PL/convexity assumption) to
the single flat-residual slice c2b = {b_1 < S/2, b_2 < (S−b_1)/2}; c2b is NOT proven for q ≥ 5 and is
the open gap.

## Promotable lemmas

- **Lemma f-homogeneous (proved in full, §B).** *For the min-over-≤(q−1)-cut-strategies value
  f(b) = min A, and any λ > 0, f(λb) = λ f(b) on the positive cone {b_1 ≥ … ≥ b_q > 0}* — because a
  fixed strategy (cut pattern + fractional positions) scales every final part length by λ, hence scales
  A by λ, and the strategy set is scale-free, so the min scales by λ. Pure structural fact; no numerics.
- **Lemma σ-migration (proved in full, §C).** *With S = (2^q−1)/D and Φ = {b ∈ K_q : Σ b_i = S},
  max_{K_q} f = max_Φ f* — because any K_q point with Σ < S rescales UP by S/(Σ) > 1 onto Φ (gaps and
  floor scale up, staying ≥ 1/D) with f weakly larger by f-homogeneous. **Validly replaces the round-7
  open statement (V)**: reduces IH(q) to bounding f on the σ-face, with NO vertex-attainment, NO
  piecewise-linearity, NO convexity. Derived from f-homogeneous + certified f-continuous-attained.
- **Lemma TwoLevelCascade (proved in full, §E1–§E2).** *In the flat residual on the σ-face
  (Σ = (2^q−1)/D, b_1 ≤ 2^{q-1}/D, b_2 ≤ 2^{q-2}/D, gaps ≥ 1/D): if b_1 ≥ S/2 then XY forces
  A = 2b_1 − S ≤ 1/D (generalized GreedyCascade); if b_1 < S/2 and b_2 ≥ (S−b_1)/2 then XY forces
  A = 2b_2 − (S−b_1) ≤ 1/D via [halve b_1; greedy-cascade b_2].* Closes the two "dominant-top-piece"
  sub-slices of the flat residual for all q with explicit ≤ (q−1)-cut strategies. Derived from certified
  Lemmas X, G1, R (and generalizes certified GreedyCascade to arbitrary total mass S). The residual
  c2b = {b_1 < S/2, b_2 < (S−b_1)/2} (q ≥ 5) remains open.
- **Lemma VertexFace, Lemma f-continuous-attained** — already certified (round 7), unchanged; VertexFace
  is no longer on the critical path (the σ-migration spine bypasses it) but remains a valid boundary fact.
