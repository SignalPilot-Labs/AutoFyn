## imo-2026-03

Problem is near-closed. Answer c(n) = 2^n/D, D = 2^{n+1}−1. Two crux gaps remain, one per side;
each has a genuinely-new framing this round. The two live slugs sit on opposite sides of the
problem (upper polytope vs lower interleaving) — maximally far apart, no shared wall. I put up:
(1) ADVANCE upper-vertex-reduction with the 1-homogeneity σ-face spine; (2) ADVANCE
direct-constructive with the T-parity generalized-interleaving a=0 closer; (3) FOLD
upper-general-cascade (its B2-small residual is now subsumed by the σ-face reduction — no build).

---

upper-vertex-reduction: advance
Target: The whole XY upper bound O ≤ c(n) for all n — i.e. A ≤ 1/D on the entire Case-B hard
  regime (p = n+1 pieces, all > 1/D, all gaps > 1/D, Σ = 1), completing the upper half of
  c(n) = 2^n/D. (Lower half imported from direct-constructive; Case A + Reductions 1–2 certified.)
Technique: 1-homogeneity scaling reduction of f to the σ-face, then σ-face casework closed by
  certified IH-reducible except a single flat-residual cascade. Replaces the open (V)
  vertex-attainment claim entirely — no convexity/PL assumption is used anywhere.
Skeleton:
  1. f(b) = min over ≤ q−1 XY strategies of A(b) is 1-homogeneous: f(λb) = λ f(b) — because
     scaling all pieces by λ scales every cut position and every final length by λ, hence scales
     A by λ, for every fixed strategy; the min over strategies commutes with the scalar λ. (One-line,
     new structural fact; verify: strategy set is scale-invariant since gap/positivity constraints
     rescale.) Watch: the DOMAIN K_q is not scale-invariant (its σ-constraint Σ ≤ (2^q−1)/D and the
     absolute floor b_q ≥ 1/D are not homogeneous) — the homogeneity is of f as a function on the
     positive cone; step 2 uses it only to push the max onto the σ-face.
  2. Max of f on K_q migrates strictly onto the σ-face {Σ b_i = (2^q−1)/D} — because for any b in K_q
     with Σ b_i = s < (2^q−1)/D, the rescaled b' = b·(2^q−1)/(Ds) has f(b') = ((2^q−1)/(Ds))·f(b) >
     f(b), and b' still satisfies gap/floor constraints (gaps and floor scale UP by a factor >1, so
     stay ≥ 1/D). Hence sup_{K_q} f = sup_{σ-face ∩ K_q} f. This is the substitute for (V): it needs
     NO vertex-attainment, NO PL-ness, NO convexity — only monotone scaling. (V) is now bypassed, not
     proved.
  3. On the σ-face, split by (b_1, b_2) tiers:
     (a) b_1 > 2^{q-1}/D: IH-reducible halve-branch → valid IH(q−1) instance. [CERTIFIED import]
     (b) b_2 > 2^{q-2}/D (and b_1 ≤ 2^{q-1}/D): IH-reducible cut-at-b_2 branch → IH(q−1). [CERTIFIED]
     (c) flat residual: b_1 ≤ 2^{q-1}/D AND b_2 ≤ 2^{q-2}/D. THIS is the single open step (step 4).
  4. Flat-residual cascade (q ≥ 5): XY forces A < 1/D with q−1 cuts. [OPEN — the sole gap]
  5. Induction on q: base q ≤ 4 certified (IH-reducible ∪ IH4-flat, `lemmas/IH4-flat.md`); step
     (a)/(b) drop to IH(q−1); step (c) closed by step 4 ⟹ IH(q) all q ⟹ upper bound for all n.
Key lemmas (claim + mechanism):
  - 1-homogeneity of f — because a fixed strategy's final multiset is a positively-homogeneous
    (degree-1) function of the piece vector, and A of a sorted multiset is degree-1 in the values;
    min over a scale-invariant strategy family preserves degree-1. (Certifiable, one line; this is
    the round's promotable new lemma — propose `lemmas/f-homogeneous.md`.)
  - σ-face migration — because f homogeneous + rescaling to the σ-face strictly increases the scalar
    factor (2^q−1)/(Ds) > 1 while keeping gaps ≥ 1/D and floor ≥ 1/D (both scale up). Kills (V).
  - Flat-residual cascade bound (THE HARD STEP, q ≥ 5, b_1 < 2^{q-1}/D exactly the residual regime):
    XY applies an alternating pair-cancel cascade — halve b_1 (creates {b_1/2,b_1/2}, XOR-null by
    Lemma X), then pair-cancel cuts (cut b_{2i} at b_{2i+1}, creating a copy of b_{2i+1} that
    XOR-cancels the intact b_{2i+1}, leaving singleton b_{2i}−b_{2i+1}), and one final asymmetric
    split (b_last at δ). By Lemma X, A = alternating sum of the SURVIVING SINGLETONS only. The
    load-bearing inequality the builder must prove: **the alternating sum of the surviving singletons
    < 1/D**, derived from the flat-residual constraints b_1 ≤ 2^{q-1}/D, b_2 ≤ 2^{q-2}/D,
    Σ = (2^q−1)/D, all gaps > 1/D. IH4-flat (certified) is exactly this bound for q=4 with singletons
    {b_2−b_3, b_4−δ, δ}; the q=5 target (D=31): b_1 ≤ 16/31, b_2 ≤ 8/31, Σ=1, and a 4-cut cascade
    must leave singletons summing (alternately) to < 1/31. Two tools available to the builder:
      (i) generalized IH-flat cascade (the pair-cancel pattern above), generalizing IH4-flat's proof
          directly — the natural induction on the flat-residual structure; OR
      (ii) `lemmas/GreedyCascade.md` (certified): if a_1 ≥ 1/2 the greedy n-cut cascade gives exactly
          A = 2a_1 − 1 ≤ 1/D (closed form). This covers the a_1 ∈ [1/2, c(n)] slice of the flat
          residual; the genuinely-open slice is b_1 < 1/2 where halving/greedy under-cancels (the r6
          fixed-point obstruction lives here).
Open gaps: ONLY step 4 (the q ≥ 5 flat-residual cascade, restricted to b_1 < 1/2). Everything else
  is certified imports (IH-reducible, IH4-flat, GreedyCascade, VertexFace, X, H, Reductions 1–2) plus
  the two new one-line lemmas (homogeneity, migration).
Cases to cover: σ-face tiers (a) b_1 large, (b) b_2 large, (c) flat residual — (a),(b) certified;
  only (c) open. Within (c): the b_1 ≥ 1/2 sub-slice via GreedyCascade, the b_1 < 1/2 sub-slice via
  the cascade (the real work).
Watch out for:
  - Do NOT claim f homogeneous on K_q as a set — K_q is not scale-invariant; homogeneity is on the
    cone, used only to push the max to the σ-face. State it as f(λb)=λf(b) for b in the positive
    hard-regime cone.
  - The migration argument REPLACES (V); do not resurrect the vertex-attainment claim or any PL/
    convexity argument (refuted r3/r6/r7). If a reviewer asks "where is (V)?" the answer is: not
    needed — homogeneity + monotone rescaling is strictly weaker and suffices.
  - The cascade must respect the cut budget q−1: count cuts explicitly (halve b_1 = 1, each
    pair-cancel = 1, final split = 1). For q=5 that is 4 cuts = q−1. Verify the pairing uses exactly
    q−1 cuts and leaves the right singleton count.
  - The surviving-singleton alternating sum can FAIL to be < 1/D if the singletons cluster (each
    b_{2i}−b_{2i+1} > 1/D by the gap condition, so their alternating sum is delicate) — this is why
    the bound is the crux, not a formality. The final asymmetric δ-split (as in IH4-flat's two
    sub-cases) is what tunes the last singleton below 1/D; keep it.
  - Numerics support the conclusion (explorer V-route §1: geometric vertex = 1/D, all interior < 1/D,
    q=3,4,5) but the cascade bound is the honest open lemma.

---

direct-constructive: advance
Target: The whole LB lower bound O ≥ c(n) for all n against every XY play — completing the lower
  half. Everything is closed EXCEPT the stray regime's augmented a=0 closer (§4.4.4); this advance
  fills that single gap, which then closes L2 and the entire problem's lower bound.
Technique: T-parity + generalized interleaving — a genuinely-different framing from the certified
  DyadicLower (no receiver/donor, no flat-move monovariant, no cross-group transfer). Organize by
  parity of the total piece count T = |F| + |G|; prove A > 1 by vertex-ordering enumeration + a
  parity-counting bound forcing stray G-sub-pieces onto odd ranks.
Skeleton:
  1. Setup (certified, §4.4.1–4.4.3): stray config = F (k_n+1 R_n-fragments, ΣF=2^n, budget
     k_n+s ≤ n) ∪ G (n+s non-R_n pieces, ΣG=2^n−1, each ≤ 2^{n-1}, s ≥ 1 stray sub-pieces > 0).
     Target A ≥ 1 ⟺ E ≤ ΣG (†). Reduced to the augmented a=0 minimiser (all pieces ≤ 2^{n-1}).
  2. Split on parity of T = (k_n+1)+(n+s):
     Case A (T odd — the tight case, A → 1): prove A ≥ 1 + 2·Σ(s smallest G-pieces) > 1.
     Case B (T even — the slack case): prove A ≥ 2 by pigeonhole on the large F-pieces.
  3. Count bound (T odd): #odd ranks − |F| = (T+1)/2 − (k_n+1) = (n+s−k_n)/2 ≥ s (using budget
     k_n ≤ n−s), so ≥ s G-pieces are FORCED onto odd ranks. [structural, extends certified Count Lemma]
  4. Vertex-ordering enumeration (Case A): for every valid sorted-order cell, the affine formula for
     A gives a lower bound > 1, using (a) a=0 ⟹ all pieces < 2^{n-1}, (b) ΣF=2^n, ΣG=2^n−1, (c) the
     dyadic structure of G. [THE HARD STEP — the builder fills this]
  5. Case B (T even): budget k_n+s ≤ n with s ≥ 1 forces k_n ≤ n−1, so |F|=k_n+1 pieces summing to
     2^n each < 2^{n-1} makes the top two F-pieces large (pigeonhole f_1,f_2 > 2^n/(k_n+1)); the
     bracket structure of the sorted alternating sum then gives A ≥ 2. [secondary, easier]
  6. Combine with certified confined (s=0, DyadicLower-confined) and the certified a=1 / top-gap
     branches ⟹ GDL(n) for all s ⟹ L2 closed ⟹ lower bound for all n.
Key lemmas (claim + mechanism):
  - Sub-lemma L2-a0 (T-odd interleaving lower bound, THE HARD STEP): for T odd and any valid
    augmented a=0 config, A(F∪G) ≥ 1 + 2·Σ(s smallest G-pieces) > 1 — because the ≥ s forced
    odd-rank G-pieces (step 3) each contribute a positive value, and in the minimizing ordering
    A = ΣF − ΣG + 2·Σ(G at odd ranks) = 1 + 2·Σ(G at odd ranks). Mechanism to prove per-cell: for
    each sorted-order type, write A as an affine function of (F,G) and bound below by 1 using the
    three constraint families. Certified anchor: n=3, s=1 (T=7, the ONLY valid parity for n=3) has a
    COMPLETE finite vertex enumeration in explorer-lower-a0 §(i) — every ordering gives A =
    (function of F > 1) + 2t. n=4,5: 0 violations over 10^4–10^5 configs.
  - Pair-contribution comparison (alternative tool for the builder, explorer Opening 2): for the s=1
    stray cut of R_0=1 into {1−t, t}, all other G-pieces ≥ 2 > 1−t force the pair to the BOTTOM two
    ranks in every ordering, so A_stray = A_confined_vertex + 2t ≥ 1 + 2t. Clean for R_0; needs the
    per-cell enumeration for stray cuts of R_j (j > 0) and for s ≥ 2.
  - T-even pigeonhole bound — because reduced F-budget forces two large F-pieces whose bracket
    contribution alone exceeds 1.
Open gaps: step 4 (Case-A T-odd per-cell vertex enumeration for general n; n=3 finite case done) and
  the T-even pigeonhole finish (step 5). All setup, reformulation (†), confined case, a=1 / top-gap
  branches, and Count Lemma are certified.
Cases to cover: T odd (steps 3–4) and T even (step 5) — jointly exhaustive; for n=3 only T=7 (odd)
  occurs, so the T-odd formula covers everything there. Within T-odd: enumerate the sorted-order cell
  types (the explorer lists 5 for n=3; general n needs the cell-type taxonomy).
Watch out for:
  - The identity A = 1 + 2·Σ(G at odd ranks) is NOT a general identity — it requires ALL F-pieces at
    odd ranks, which holds in the minimizing construction but NOT in an arbitrary ordering. The lower
    bound over ALL orderings therefore CANNOT just cite the identity; the builder must do genuine
    per-cell vertex enumeration (this is the real work, and where a hand-wave would hide a gap).
  - The infimum 1 is NOT attained for s ≥ 1 (min A = 1 + 2t → 1 as t → 0, recovering the confined
    interleaving). State A > 1 strictly, not A ≥ 1 with a claimed minimizer.
  - Pointwise A_stray ≥ A_confined is FALSE (716/17980 violations, r7) — the comparison is per
    ordering-TYPE, not pointwise in F. Do not route through a monotone stray↔confined swap.
  - Dead ends (do not retry): receiver-existence (false at clustered configs), flat-move monovariant
    with cross-group transfers (blocked by fixed group sums), relaxed (†) with arbitrary G (false,
    min A ≈ 0.08). This framing must avoid all of them (it does — no donor/receiver, no monovariant).

---

upper-general-cascade: FOLD (subsumed — no build this round)
Rationale: The σ-face reduction (upper-vertex-reduction, above) now covers the WHOLE Case-B hard
  regime. On the σ-face at q = n+1 (Σ = 1 = (2^q−1)/D exactly), every config is either b_1 > 2^{q-1}/D
  (IH-reducible, certified), b_2 > 2^{q-2}/D (IH-reducible, certified), or the flat residual.
  upper-general-cascade's only open residual was B2-small (a_1 < 1/2). Since 1/2 < c(n) = 2^{q-1}/D
  (verified: c(n) = 0.571,0.533,0.516,… for n=2,3,4; the flat b_1 threshold is exactly c(n)), every
  B2-small config has b_1 < 1/2 < 2^{q-1}/D, so it is NOT in the b_1-large branch; it splits between
  the b_2-large branch (certified IH-reducible) and the flat residual (owned by upper-vertex-reduction
  step 4). Hence B2-small owns NO region outside the σ-face reduction — a separate build would
  duplicate the flat-residual cascade. FOLD it: its certified lemmas (GreedyCascade, IH-reducible,
  IH4-flat) remain in the shared cache and are imported by upper-vertex-reduction as tools; no new
  work is assigned to this slug. Do NOT dispatch a builder for it.

---

Diversity note: the field has two live whole-problem attempts on opposite sides (upper polytope σ-face
vs lower T-parity interleaving); they share no wall (distinct gaps, distinct machinery), so they will
not die together. Each carries a genuinely-new framing delivered this round. For a near-closed problem
this is adequate breadth; no new far-apart approach is opened (opening one now would waste a build when
both remaining gaps have fresh, promising mechanisms). If BOTH gaps stall next round, reframe — but not
before.

build set: upper-vertex-reduction, direct-constructive
