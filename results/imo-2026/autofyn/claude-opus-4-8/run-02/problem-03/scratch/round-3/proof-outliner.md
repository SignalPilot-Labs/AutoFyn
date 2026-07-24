## imo-2026-03

Two gaps remain, both narrowed to a single residual; the run is one step from `solved` on
each bound. The field puts up the two lead approaches, each REVISED with a concrete new
mechanism for its gap (kept far apart: GAP-L closes by an **integer-value-at-the-minimizer
parity** argument; GAP-U closes by an **amortized multi-peel phase** argument), plus an
explicit retirement decision on the diversity hedge.

Shared certified imports (free to all approaches, in `lemmas/`): `endgame-greedy` (Lemma 0),
`layer-cake-alt-sum` (`f=M`, Lemma 1/L), matching form (Lemma 2), single-cut action (Lemma 3),
`top-band-decoupling` (Lemmas A,B: `f(P)=u+f(Q)`), `integer-parity-alt-sum` (Lemma D: integer
pieces ⇒ `f≡Σ mod 2`; Lemma E: `f≥0`), `alt-sum-two-max-minus-total` (Lemma 5: `f≥2a₁−Σ`),
`cut-and-pair-reduction` (Lemma 4/H: `g_b(P) ≤ g_{b-1}(R)`, dominant dichotomy). Reduction
(certified): `c(n)=2^n/D_n ⇔ V_n := max_LB min_XY f = 1` (scaled), `D_n = 2^{n+1}−1`.

---

### self-similar-recursion: revise
Target: Prove `c(n) = 2^n/(2^{n+1}−1)` end to end. This approach owns the **lower bound**
`V_n ≥ 1` (i.e. GAP-L: every `≤n`-cut refinement `P` of `W_n={2^0,…,2^n}` has `f(P) ≥ 1`),
and imports the upper bound once the sibling closes GAP-U.

**Re-plan of GAP-L residual (non-integer cut positions).** Drop the "perturb non-integer
vertices toward integer ones" plan (dead: huge positive-measure non-integer flats already sit
exactly at `f=1`, so there is no strict improvement to chase). Replace it with the
**chamber-value / monochromatic-parity** reframing from the lowerbound explorer, confirmed by
hand-algebra (n=2) and by my scan (min `f=1`; the achievable values at the minimizer are exactly
the positive **signed sums of the original dyadic pieces** `{2^0,…,2^n}`, i.e. `{1,3,5,7,…}`).

Technique: piecewise-affine descent to a "monochromatic" configuration, then close by the
**already-certified parity mechanism applied to the VALUE** (not to the pieces) — the value at
the minimizer is an integer combination of the original integer pieces even though the cut
positions are irrational.

Skeleton:
  1. Reduce to (LBL): `f(P) ≥ 1` for every `≤n`-cut refinement `P` of `W_n`. — certified reduction.
  2. `f` is continuous, piecewise-affine on the compact cut polytope; min attained (Weierstrass).
     Within a **sort-chamber** (fixed descending order, hence fixed sign vector `σ`), `f = Σ σ_i a_i`
     is affine, and moving any single cut offset has `∂f/∂offset ∈ {−2,0,+2}`. — certified (Section 4).
  3. **Conservation-telescoping identity (chamber value).** Group the signed sum by original
     piece: the sub-pieces of piece `2^k` have signed contribution `= Σ(± over its sub-pieces)`.
     If within the chamber every sub-piece of `2^k` carries the **same** sign `ε_k∈{+1,−1}`
     ("monochromatic" piece), that contribution telescopes by conservation `Σ(sub-pieces)=2^k`
     to exactly `ε_k·2^k`, independent of the (possibly irrational) offsets. So on a fully
     monochromatic chamber, `f = Σ_{k=0}^n ε_k 2^k` — an **integer**.
  4. **Descent to a monochromatic (or degenerate) minimizer** (THE GAP, see below). Push offsets
     down the `{−2,0,+2}` gradient to walls; a piece with mixed-sign sub-pieces is not at a local
     min (an interior offset of it has gradient `±2`, so `f` strictly decreases until a wall).
     Walls are: (i) a cut degenerates (offset hits a piece/adjacent-cut boundary) → strictly
     fewer effective cuts → induction on the cut budget (base: uncut `W_n`, `f=f(W_n)≥1`); or
     (ii) a rank tie with another piece's sub-piece → `f` continuous across it, so a min on the
     wall is a min of an adjacent chamber; iterate. Conclusion: the minimum is attained at a
     configuration that is monochromatic or has strictly fewer cuts.
  5. **Close by parity + nonnegativity.** At a monochromatic minimizer, `f = Σ_k ε_k 2^k ∈ ℤ`.
     Its parity is `ε_0·2^0 ≡ 1 (mod 2)` (all higher terms even), so `f` is an **odd integer**;
     by Lemma E `f ≥ 0`. An odd integer `≥0` is `≥1`. Hence `f ≥ 1`. Moreover `f≥0` forces
     `ε_n=+1` (else `f ≤ −2^n + (2^n−1) = −1 < 0`), and the minimal positive value `Σ ε_k 2^k`
     with `ε_n=+1` is `2^n − (2^n−1) = 1` (all lower signs `−`), matching the flats exactly.

Key lemmas (claim + mechanism):
  - **Chamber-telescoping**: on a monochromatic sort-chamber `f = Σ_k ε_k 2^k`, `ε_k∈{±1}` —
    because each original piece's sub-pieces sum to `2^k` (conservation) and share one sign, so
    their signed total is `±2^k`, independent of where the (real) cuts fall. This is why
    non-integer cut positions do **not** break the argument: the *value* is always an integer
    combination of the *original* dyadic pieces.
  - **Odd-value floor**: `Σ_k ε_k 2^k ≡ 1 (mod 2)` and `≥0` (Lemma E) ⇒ `≥1` — the certified
    parity mechanism (Lemma D) re-used at the level of the chamber value, not the pieces
    (parity of the pieces is irrelevant; parity of the value is what closes it).

Open gaps:
  - **(THE GAP) Step 4**: rigorously prove the descent terminates at a monochromatic-or-degenerate
    configuration — specifically, that iterating "decrease `f` along a `±2` gradient to a wall,
    cross rank-ties by continuity, and induct down on cut budget at degeneracies" cannot cycle
    and must reach a chamber where every original piece is monochromatic. This is a finite
    descent/well-foundedness argument (each degeneracy strictly drops the cut count; ties permute
    a finite rank order). This is the single honest residual — but it is now a clean combinatorial
    descent, NOT a mysterious non-integer inequality.
Cases to cover: monochromatic minimizer (Step 5, done modulo the gap); degenerate/fewer-cut
  minimizer (induction on budget, base uncut `W_n`); `u≥1` regime already closed by Corollary C
  (`f=u+f(Q)≥u≥1`) as an independent shortcut.
Watch out for:
  - A rank tie can occur between sub-pieces of DIFFERENT original pieces (not just a bisection's
    two halves); the descent must handle inter-piece ties, not only intra-piece ones. Do NOT
    assume ties only merge a piece's own halves.
  - Ensure "monochromatic" is defined per original piece (all its sub-pieces one sign), not per
    chamber globally; a chamber can be monochromatic for some pieces and mixed for others — the
    descent must remove EVERY mixed piece.
  - Do NOT reintroduce parity of the pieces or any integer-cut assumption (provably useless,
    `d=3` counterexample). Parity is applied only to the final integer VALUE `Σ ε_k 2^k`.
  - Do NOT invoke any blanket "cutting a non-top piece never helps" domination (FALSE, 28k
    counterexamples); only Lemma A's top-band localization is a licensed structural fact.

---

### alternating-sum-threshold-potential: revise
Target: Prove `c(n) = 2^n/(2^{n+1}−1)` end to end. This approach owns the **upper bound**
`V_n ≤ 1` (GAP-U: for every LB marking `P_0`, `≤n+1` pieces, XY forces `f ≤ 1`), via Invariant
(I) `g_b(P) ≤ s/D_b`, and imports the lower bound once the sibling closes GAP-L.

**Re-plan of GAP-U middle regime (M)** `f(P)>s/D_b` AND `max(a₁,2a₂)<(2^b/D_b)s`. The one-shot
geometric step (H) provably cannot fire here (no single cut removes the `≈½`-fraction). Replace
the lock-step "one cut ⇒ budget −1" accounting with a **telescoped multi-peel phase** on the
*effective top* (the largest piece not already cancelled by an invisible matched pair), per the
upperbound explorer.

Technique: strong induction on `b` with a **variable-length phase**: instead of `g_b ≤ g_{b−1}(R)`,
prove `g_b(P) ≤ g_{b−k}(R_k)` for an adaptively chosen `k∈{1,…,m−1}`, where `R_k` results from
`k` iterated effective-top peels (each a bisect-top OR top-match chosen by a refined rule), and
show some `k` achieves the cumulative mass-removal fraction `1 − D_{b−k}/D_b`, closing via IH at
`b−k` (legitimate: `|R_k| = m−k ≤ (b−k)+1`).

Skeleton:
  1. Setup: `g_b(P) = min over ≤b cuts of f`; target Invariant (I) `g_b(P) ≤ s/D_b`; base `b=0`,
     STOP rule, one-cut recursion (★), geometric step under (H). — all certified (Lemma 4/H).
  2. In regime (M): define the **effective top** = largest piece not in an invisible matched
     pair. Iterate: at each step recompute the effective residual (subtract invisible pairs) and
     choose bisect-top (`remove a₁`) vs top-match (`remove 2a₂`) at THAT level — the mass removed
     at step `j` is `r_j := max(a₁^{(j)}, 2a₂^{(j)})` of the current effective residual.
  3. **Phase mass-removal bound (THE GAP).** Show: there exists `k∈{1,…,m−1}` with
     `Σ_{j=1}^k r_j ≥ (1 − D_{b−k}/D_b)·s`, using the standing hypothesis `f(P) > s/D_b`.
     Note `1 − D_{b−k}/D_b = 2^{b−k+1}(2^k−1)/D_b`. Then `Σ(R_k) = s − Σ r_j ≤ (D_{b−k}/D_b)s`,
     and by (★) applied `k` times + IH at `b−k`: `g_b(P) ≤ g_{b−k}(R_k) ≤ Σ(R_k)/D_{b−k} ≤ s/D_b`.
  4. Termination of the phase: each peel drops the piece count by 1, so after `≤ m−1 ≤ b` peels
     only the base case (`≤1` effective piece, STOP) remains — the phase is bounded by `m`, not
     forced to spend the full budget `b`. Combine with STOP (fires the moment `f ≤ s/D_b`).

Key lemmas (claim + mechanism):
  - **Effective-top peel step**: one cut on the effective top (bisect-top or top-match) removes
    mass `r_j=max(a₁,2a₂)` of the effective residual and drops its piece count by 1, leaving `f`
    controlled by `f(R_j)` — because the created equal pair matches at cost 0 (Lemma 4, upper
    direction). Do NOT peel the *physical* max blindly (overshoots, recorded dead end
    `[0.385,…]→0.153`); always recompute the effective residual first.
  - **`f>s/D_b` ⇒ top-heaviness**: the phase floor uses that a large potential forces the top
    pieces to carry a large mass fraction. Mechanism to make rigorous: `f = Σ_j(a_{2j-1}−a_{2j})`
    (adjacent-gap form, Lemma 2); `f > s/D_b` bounds the gaps from below, which lower-bounds the
    cumulative `Σ r_j` of the successive effective tops. THIS is the load-bearing inequality to
    nail — the link from "potential above target" to "peeling removes mass fast enough."

Open gaps:
  - **(THE GAP) Step 3**: prove the phase mass-removal inequality — that `f(P)>s/D_b` guarantees
    some `k≤m−1` with `Σ_{j≤k} r_j ≥ (1−D_{b−k}/D_b)s`. Recommended attack: strengthen the IH to
    a **two-parameter** invariant tracking both `s` and the piece count `m` (crux `aimo-0236`:
    a two-phase invariant, stronger before / weaker after each peel, self-restoring within a
    bounded phase), and/or a **discharging** argument (crux `aimo-0558`: charge each gentle cut
    to a distinct piece it eventually cancels). Note pure bisect-top for all `k` provably
    UNDERSHOOTS the fraction on balanced inputs (equal pieces: `bs/(b+1) < (D_b−1)/D_b s`), so the
    rule MUST mix in top-match — but balanced inputs have small `f` and are killed by STOP, so
    the hypothesis `f>s/D_b` is exactly what excludes the bad case; the proof must USE it.
Cases to cover: STOP fires (`f≤s/D_b`, done, 0 cuts); (H) fires at level `b` (certified geometric
  step); regime (M) (the phase argument above); phase reaches base (`≤1` effective piece).
Watch out for:
  - Mass conservation on every cut: `Σ(new pieces)=Σ(old)`. The "top-match to a deeper piece
    `a_k`, `k>2`" move silently drops mass if coded as delete-and-replace — the mass-conserving
    single-step version is provably too weak alone; only the multi-cut phase works. Validate
    `Σ` before trusting any lemma step.
  - The phase length `k` is adaptive (config-dependent), bounded by `m−1`, NOT fixed at `b`.
    A fixed number of peels overshoots or undershoots — the count must be chosen by when the
    cumulative fraction is met or the base is hit.
  - Do NOT retry the one-shot dual-price / LP certificate for either bound (proven dead, round 2).

---

### game-value-recursion: retire (do not build)
Recommendation to the reviewer: **retire from the active build set** (keep the file as a dormant
population member; do not delete). Rationale: (i) it has closed **no** gap in 2 rounds (Elo 1484,
below both leaders); (ii) its only open item (Case B / budget non-fungibility) is the SAME
GAP-L wall the two revises now attack with concrete new mechanisms, reached from a different
direction but stalled at the identical step — so it adds no independent shot on goal; (iii) its
Case A is redundant with the certified `alt-sum-two-max-minus-total`. Diversity is now carried
where it pays: the two REVISES use genuinely different closing mechanisms per gap (integer-value
parity for L; amortized phase for U), which is the productive form of breadth for this
two-gap-isolated endgame. If the GAP-L descent (Step 4 above) stalls next round, reconsider
reviving game-value-recursion to carry the monochromatic-parity idea in claiming-game language
as an independent second attack. `majorization-smoothing` likewise stays dormant (one-shot
certificate provably fails; no live route).

---

**build set: self-similar-recursion, alternating-sum-threshold-potential**
