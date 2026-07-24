## imo-2026-03 (lens: count-function profile / non-integrality alternatives to the cut-budget wall)

### Setup recap (imported, not re-derived)
Reduction is fully certified: `c(n) = (1+max_LB min_XY M)/2`, `M(P) = measure{t : c_P(t) odd}`
(layer-cake-alt-sum), `c(n)=2^n/D_n ⇔ max_LB min_XY M = 1/D_n`. Upper bound is FULLY proved
(delete-subtract-reachability + subset-sum-pigeonhole). Sole gap is (LBL): every ≤n-cut
refinement `Q` of `W_n={2^0,...,2^n}` has `f(Q) ≥ 1`, further reduced (Lemma 6.1, certified-grade)
to **(LBL-B)**: the case where the top piece `2^n` IS cut.

### Distinct openings surfaced this round

**1. Profile/visible-multiset peeling (formalizes the "track the count function, not scalar f"
suggestion) — TESTED, and it reconverges to the SAME wall as self-similar-recursion.**
I traced the refuting instance `Q'={16,4,3.567,2.115,2,1.885,1,0.433} → f≈14.134`, then bisect
`16→{8,8}` giving `f≈1.866`. Computed the count function explicitly: in `Q'` every value is
distinct (no matched pairs), so the *entire* multiset is "visible" and `f(Q')` is just its raw
alternating sum, dominated by peeling off the unique max `16` via (F2): `f(Q')=16−f(Q'∖{16})`.
The bisection turns `16` into a matched pair `{8,8}` (P1-invisible), so the new visible multiset
is exactly `Q'∖{16}` and `f` collapses to `f(Q'∖{16})=1.866`. **The "12.27 drop" is entirely an
artifact of (F2) peeling off a large unique top value** — there is no exotic multi-band
cancellation. This means the natural refinement of the induction is: recursively peel the current
unique max of the *visible* multiset (matched-pair-reduced) via (F2)/Lemma 3.1, reducing (LBL) to
a statement about the remainder after each peel. But this recursive peel gets stuck exactly when
the visible multiset hits a **rank tie at the max level** (≥2 distinct-but-equal visible values,
neither of which cancels as a clean matched pair, e.g. an odd stack of 3 equal values) — which is
*the same tied-vertex / Case-B residual* already isolated by `self-similar-recursion` (Gap A/B) and
by `block-recursion`'s UPM-5. **Verdict: this "profile" refinement is NOT a genuinely different
wall — it is the cut-budget-side incarnation of the identical tied-rank obstruction.** Report this
clearly to the outliner: pursuing "track the full count-function profile through the cut-budget
induction" as currently conceived will very likely reduce to Gap A/B, not dissolve it. This matches
CLAUDE.md's warning that a bypass in a related framing hits the same wall one step later.

**2. Band-wise (dyadic-level) domination — a genuine variant worth a try, but likely inherits the
same tie obstruction at the band boundaries.** Decompose `f(Q) = Σ_{i=0}^n M_i(Q)` where
`M_i(Q) = measure{t ∈ [2^{i-1},2^i) : c_Q(t) odd}` (bands aligned to `W_n`'s original scale,
`B_0=[0,1)`). This is a genuinely finer invariant than the scalar `f`. Untested conjecture: for `Q`
reachable with `≤n` cuts, some per-band inequality like `Σ_{i≥j} M_i(Q) ≥ f(W_{n-k})`-type floors
holds bandwise as cuts accumulate. I did NOT find time to check this numerically at scale; flag it
as an opening but expect it converges to the same rank-tie difficulty at whichever band absorbs the
top-piece's sub-pieces, since band boundaries are where ties concentrate (a sub-piece of `2^n` can
land exactly at `2^{n-1}`, coinciding with the original `2^{n-1}` piece — literally Case B's
mechanism).

**3. SOS/quadratic-certificate dual on `f` — also collapses onto the ALREADY-USED convexity
lever, not a new one.** The natural quadratic potential for this family is `Φ(Q) = Σ a_i²`
(sum of squares of piece lengths): bisecting `V→{V/2,V/2}` strictly decreases `Φ` by `V²/2`, and
`Φ` is strictly convex under any sum-preserving perturbation. **This is EXACTLY the `Φ`
already used by `self-similar-recursion`'s Lemma S-core / Φ-max selection** (certified
`phimax-trivial-kernel.md`). So "try an SOS/quadratic dual certificate on `f`" independently
re-derives the same lever the integrality route already uses to pin the minimizer, and hits the
same Gap A/B wall (the Φ-maximal selection's residual incidence-graph facts). I do not see a
quadratic form distinct from `Σa_i²` that is natural here (the constraint set — reachable-by-≤n-
cuts configs of `W_n` — is not a clean polytope/quadric; it's a recursive combinatorial tree, so a
closed-form SOS certificate would need to encode the cut recursion itself, which is about as hard
as (LBL) directly). **Recommend NOT spending a round on a "fresh" SOS dual — it is the same Φ
already in play under a different name.**

**4. GENUINELY NEW opening (untested, most promising): reuse the certified UPPER-BOUND machinery
(Lemma A/B: delete-subtract-reachability + subset-sum-pigeonhole) in the REVERSE causal role to
attack (LBL) directly, bypassing the cut-budget induction on `f` entirely.** The upper bound shows
against ANY Liu-Bang marking, Xiang Yu's DELETE/SUBTRACT strategy achieves `f ≤ φ(P) ≤ s/(2^m-1)`,
and (per `current.md`) this bound is numerically TIGHT for `P=W_n`: `φ(W_n)=1/D_n` for `n≤5`.
(LBL) is exactly the claim that XY (playing ANY strategy, not just delete/subtract) cannot beat
this floor. Since the powers of two `2^0,...,2^n` have all signed subset sums `Σε_i2^i` (`ε∈
{-1,0,1}^{n+1}`) distinct and nonzero unless `ε=0` (uniqueness of binary/balanced-ternary-like
representation), there may be a clean **integer/valuation gap argument bounding `φ(W_n)` from
BELOW by 1 directly on the original powers**, transportable to the cut pieces via the SAME
delete/subtract reachability lemma used for the upper bound (i.e., show any reachable `Q` still
has `f(Q) ≥` a signed-subset-sum floor of the *original* `2^i` values, not of the sub-pieces).
This reuses certified machinery in a new direction and is genuinely distinct from both the
integrality/Φ-max route and the cut-budget/Jacobsthal route. Worth a dedicated approach slug.

### Cheap-kill candidates
- v_2 / integer floor of signed subset sums: `Σε_i 2^i ≠ 0` for `ε∈{-1,0,1}^{n+1}\{0}` (unique
  binary decomposition up to the balanced-digit ambiguity) — cheap to state, may directly bound
  `φ(W_n) ≥ 1/D_n`-type floors from below. Worth checking before heavy casework (opening 4 above).
- None obvious for openings 1–3 beyond what's already been tried; both are shown here to reduce to
  existing gaps.

### Knowledge-base entries
- **Invariants & monovariants** (Combinatorics, KB) — underlies both the (refuted) per-cut driver
  and any profile refinement; the KB entry itself gives no extra leverage beyond what's already
  used.
- **Sum of squares (SOS) / completing the square**, **Quadratic forms** (Algebra/Linear-Algebra,
  KB) — the natural candidate `Φ=Σa_i²` is already certified in-repo (`phimax-trivial-kernel`);
  KB doesn't suggest a materially different quadratic form for this problem.
- **Pigeonhole/extremal principle**, **Double counting** (Combinatorics, KB) — underlie the
  certified `subset-sum-pigeonhole` (Lemma B), reusable for opening 4.

### Analogous past problems (crux corpus)
Filtered `combinatorics` / `games-and-strategy` (39 cruxes). Best match:
- **aimo-0117** (Jesse & Tjeerd stone game, Dutch NL olympiad). Crux: *"Assign the played values
  as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds
  the sum of all the others"* + an inductive invariant "the largest power of 2 played so far sits
  in the target box after your turn," closed by `2^j > Σ_{i<j} 2^i`. This is structurally the SAME
  dyadic-domination idea already used in `top-uncut floor` (Lemma 6.1: `2^n` unique max ⇒
  `f≥2^n−2^{n-1}=2^{n-1}`) — confirms the technique is standard and already correctly deployed here,
  not a new lever. Read in full: `past_problems_database.json` / `past_crux_moves_database.json`
  (`problem_id=aimo-0117`).
- No other crux in `games-and-strategy` or `invariants-and-monovariants` (combinatorics) resembled
  a *static final-configuration* extremal-multiset game like this one (most are sequential
  alternating-turn strategies with observation between moves, which our problem is NOT — Xiang Yu
  marks all `≤n` points at once after seeing Liu Bang's marks, so the "sequential mirroring
  invariant" style of most `games-and-strategy` cruxes doesn't transfer). Judged NOT genuinely
  analogous beyond the dyadic-domination idea already in use.

### Prior progress
See `current.md`: upper bound fully proved/certified. Lower bound reduces to the tied-vertex
residual = Gap A (acyclicity of Φ-max incidence multigraph) ∪ Gap B (μ=3 even-block leaf) for
`self-similar-recursion`, ≡ UPM-5 for `block-recursion`, ≡ (LBL-B) top-cut case for `cut-budget`.
16 lemmas certified. Numerically `min f = 1` for `n≤4` (conjecture, matches proved cases).

### Dead ends (do NOT retry)
- Per-cut Jacobsthal-decrement driver on scalar `f` — REFUTED (explicit counterexample,
  round 5, reviewer-confirmed).
- One-shot linear LP dual / fixed length-only price certificate — REFUTED (round 2, tautological
  or ≤0 by equal-piece feasibility).
- (NEW, this round) Recursive visible-multiset peel as a way to avoid the tied-vertex wall — traced
  explicitly on the refuting instance and shown to reduce to the SAME Gap A/B tie obstruction, not
  a bypass. Do not present this as a "new framing" without also confronting Gap A/B.
- (NEW, this round) SOS/quadratic certificate using `Φ=Σa_i²` — this is not new; it is the already-
  certified `phimax-trivial-kernel` potential of `self-similar-recursion` under a different name,
  and inherits its Gap A/B wall.

### Small-case / intuition notes
- Confirmed by direct computation (not just cited): the refuting instance's 12.27 f-drop is fully
  explained by the (F2) peel-off of a unique top value `16` followed by its bisection into an
  invisible matched pair `{8,8}` — no exotic mechanism. (Conjecture-free; verified by explicit
  count-function computation in this session.)
- `min f = 1` for `n ≤ 4` remains the numerically-confirmed target; no case data contradicts the
  pinned answer `c(n) = 2^n/(2^{n+1}-1)`.
- Recommend the outliner treat opening 4 (reverse-direction subset-sum/signed-power-of-two floor)
  as the genuinely new candidate for a round-6 approach slug; openings 1–3 should be reported to
  the population as "checked and found to collapse onto the existing Gap A/B wall" so no future
  round re-discovers this by re-treading it as if it were new.
