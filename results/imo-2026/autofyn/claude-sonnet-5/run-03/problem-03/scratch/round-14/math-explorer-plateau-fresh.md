## imo-2026-03

### Plateau check (lens 1)

**Verdict: a partial, targeted plateau-break is warranted — not a full reset, but the outliner should put ≥1 genuinely different-mechanism approach on the table this round, aimed specifically at the shared obstruction identified below.**

The two remaining live gaps are:
- **Lower bound**: `GT(m)` for `m≥4` (`self-similar-induction-on-n`), needed to
  extend the fully-closed Branch-I.A-restricted window from `ℓ=1..4` to
  general `ℓ`. Narrowed (round 13) to two precisely-stated sub-cases (`q=1`
  excess case; the `GT(k-1)`-mirror small-sum case), but the underlying
  **mechanism** — peel the running max, compare to a threshold
  (`2^{m-1}`, then `μ=max(S)`), recurse — has been the *same* mechanism
  since round 3/4 (when the "three-way case split," Case A/B/middle-regime,
  was first identified). Ten rounds later the core difficulty is unchanged:
  the middle regime's case count grows with `m` (nested trichotomies,
  vertex-enumeration attempts in rounds 10–11 only closed `m=3,4` by hand
  and admit the vertex list is not proved exhaustive for general `m`).
- **Upper bound**: the `Σ`-shape residual of the candidate vertex set `Q`
  (`global-lp-vertex-sufficiency`), needed after `Q_region` was fully closed
  (round 10). The **mechanism** — Global Vertex Lemma → finite hyperplane
  arrangement `L` → candidate set `Q` as `(k-1)`-subset solutions — has been
  unchanged since round 9. Rounds 11–13 only ruled out *bypass* mechanisms
  (bounded-`s_0` constructions, region-boundary monotonicity, exchange
  arguments both region- and response-side) without ever attacking the core
  difficulty: no bound on `|Σ(n,k)|` as a function of `n` has been derived
  in 5 rounds.

**Are they secretly the same obstruction? Yes, structurally.** Both gaps are,
underneath the different notation, the identical phenomenon: *a
combinatorially-described family of extremal candidates (case-splits of a
top-piece refinement on the lower-bound side; vertex-solutions of a growing
affine-functional list on the upper-bound side) whose count is not bounded
uniformly in the problem's size parameter (`m` resp. `n`), and every attempt
so far to avoid enumerating it (case-split induction on one side,
exchange/monotonicity arguments on the other) has been tried and killed*.
This is exactly CLAUDE.md's "stuck shared gap" trigger, even though it
manifests as two syntactically different open statements — they are the
same wall (unbounded case-growth resisting a uniform argument) hit from the
lower- and upper-bound sides of the *same* certified reduction
(`lemmas/reduction-to-multiset-minimax.md`). The steady round-by-round
narrowing reported in `current.md` is real (not stalled optics), but it has
all been *narrowing the search for a bypass*, never a reduction of the
core combinatorial-growth difficulty itself. That is the sign to try, not
another bypass on the same architecture, but a genuinely different
mechanism that doesn't require enumerating cases/vertices at all.

### Fresh framing (lens 2): proposed plateau-break approach

**None of the crux corpus's combinatorics `games-and-strategy` cruxes
(`aimo-0019`, `aimo-0066`, `aimo-0077`, `aimo-0115`, `aimo-0117`, `aimo-0196`,
`aimo-0225`, `aimo-0236`, `aimo-0262`, `aimo-0445`, `aimo-0461`, `aimo-0521`,
`aimo-0560`, `aimo-0596`, `aimo-0631`, `aimo-0653`, `aimo-0663`, `aimo-0746`,
`aimo-0766`, `aimo-0854`) is a genuine structural match** — none involves a
two-phase "partition then refine" value-optimization with an OddSum-type
alternating-rank objective. The closest in *flavor* (not mechanism to copy
wholesale, since none directly transfers) are `aimo-0236` (two 2-adic-
valuation potential/monovariant arguments driving an adversarial token
game — nu_2(x) as the invariant carried across turns) and `aimo-0117`
(assigning played values as an explicit dyadic/geometric sequence in a
two-box adversarial value game, structurally close to our own
`LB`-partition). Both are useful as *inspiration for a discharging-style
invariant*, not as a citable solution — this problem's objective (OddSum on
sorted refinements under a cut budget) has no exact match in the sampled
corpus. `generating-functions` (12 cruxes) and `linear-algebra-method` (16
cruxes) in combinatorics were checked by subtopic count and are too thin/
generic here to be worth a full read given time budget; flag them as
unexplored, not ruled out.

**Concrete new approach to open as a population member (genuinely distinct
mechanism, not a relabeling):** a **discharging / charge-conservation
argument directly on the cut-sequence**, bypassing the multiset-minimax
`OddSum` abstraction's case-split/vertex machinery entirely. Idea: assign
each *final* piece of value `v` sitting at "scale" `s` (defined via its
value relative to the nearest power-of-two threshold it was cut from,
i.e. its position in the induced dyadic hierarchy of the construction) a
charge `w(v,s)`, chosen so that (a) the total charge over any legal
refinement is an *invariant* (conserved exactly under every single-cut
move, provable by a local, one-cut computation — no global case split
needed), and (b) `OddSum(refinement) ≥` (resp. `≤`) a simple function of
total charge, closing both directions from one identity instead of two
separate induction architectures. This is structurally different from
every approach in the current population: `self-similar-induction-on-n`
and `greedy-reduction-geometric` both recurse via peeling-the-max
case-splits; `global-lp-vertex-sufficiency` and `lp-duality-split-polytope`
both work via LP/vertex geometry; `universal-halving-adversary` searches a
named-tool family; `dyadic-potential-invariant` and
`layer-cake-parity-reframing` already tried single-cut-local invariants
and were refuted for the *specific* invariants they tried (Cut-Reallocation
Exchange Lemma, majorization, per-cut-additive layer-cake) — but a
charge/discharging argument (assign charge *by scale/rank*, not by raw
value or by naive per-cut additivity) is a different member of this same
general family that has not been tried; it should be attempted with
**mandatory early numerical falsification** (as `dyadic-potential-invariant`
and `layer-cake-parity-reframing` correctly did) before any proof
investment, since this family already has two documented dead ends and the
prior on a third naive variant working is low — the goal is to find a
charge assignment general enough to survive where those two did not (in
particular, avoid strict per-cut additivity, which layer-cake already
proved fails via a sign-flipping counterexample; a scale/rank-dependent
weight, not a value-dependent one, is the untried degree of freedom).

### Candidate technique(s)
- Existing (2 stuck architectures): peel-max case-split induction
  (`self-similar-induction-on-n`); LP/hyperplane-arrangement vertex
  enumeration (`global-lp-vertex-sufficiency`).
- Proposed fresh: discharging / rank-scaled charge-conservation invariant
  (see above) — combinatorics KB entry "Invariants & monovariants."

### Cheap-kill candidates
- Before investing in the discharging approach: a fast numerical check
  (Nelder-Mead + exact-Fraction spot check) of whether a rank-scaled charge
  `w(v,s) = v · 2^{-|log2(v) - s|}`-style weight (or similar) is exactly
  conserved under a single cut — if it fails even at `n=2,3` by a
  non-noise margin (as the two prior invariant attempts did), kill it
  immediately rather than developing further, per the discipline the
  population has already established for this failure mode.
- For `GT(m)`, `m≥4`: check whether the `q=1, e≥1` sub-case (round 13's
  first open sub-case) admits a direct small-`m` counterexample search
  (`m=4,5`) before more induction machinery is built — a quick way to
  confirm the sub-case is genuinely hard, not just unattempted.

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics section) — for the proposed
  discharging approach.
- "Pigeonhole / extremal principle" — potentially for bounding `|Σ(n,k)|`
  if a combinatorial-classification attack on the upper-bound gap is
  pursued instead/additionally.
- No geometry/NT entries apply.

### Analogous past problems (cruxes)
- `aimo-0236` (combinatorics, games-and-strategy) — 2-adic-valuation
  potential/monovariant argument in an adversarial token game. Same
  *flavor* (dyadic potential surviving adversarial play) as the proposed
  discharging approach, but the game structure (tokens on a line, +a moves)
  is not analogous enough to transfer any step directly — inspiration only.
- `aimo-0117` (combinatorics/games, no crux subtopic tag surfaced but
  thematically close) — explicit dyadic/geometric sequence of played
  values in a two-box value-comparison game; structurally reminiscent of
  `LB`'s geometric partition `p_i=2^{n+1-i}/(2^{n+1}-1)`, but the box-filling
  mechanics differ enough that no crux move transfers as-is.
- No genuinely matching crux found for the core two-phase
  partition-then-refine-under-budget game with an alternating-rank
  (OddSum) objective; report this honestly rather than force a weak match.

### Prior progress
See `current.md` for the full, accurate state: Branch-I.A-restricted window
fully closed at `ℓ=1..4`; `Q_region` fully closed for the upper bound; both
remaining gaps (`GT(m)` for `m≥4`; `Σ`-shape classification) are real,
precisely stated, and (per this report) share one underlying obstruction.

### Dead ends (do not retry)
- Cut-Reallocation Exchange Lemma (literal or region-restricted) —
  `dyadic-potential-invariant` rounds 3–4, exact counterexamples both times.
- Majorization/Schur-monotonicity of OddSum — `dyadic-potential-invariant`
  round 6, proved false in general (OddSum is neither Schur-convex nor
  Schur-concave).
- Per-cut-additive layer-cake/threshold decomposition —
  `layer-cake-parity-reframing` round 4, proved false by an exact
  sign-flipping counterexample (a cut's marginal AltSum contribution is not
  independent of other cuts).
- Structured-randomization / expectation-over-discrete-scheme for the
  upper bound — `structured-randomization-upper-bound`, proved structurally
  incapable in general (Expectation Obstruction Theorem).
- Exchange-argument class (region-side and response-side, single-choice and
  existential) for the boundary-endpoint bypass of `Σ`-classification —
  `global-lp-vertex-sufficiency` rounds 12–13, refuted at `n=3` in both
  forms.
- Bounded-`s_0` named-construction families (Subset-Tie, Multi-Piece
  Subset-Tie, transplanted `k`-Anchor-Merge) for the upper bound at `e_0` —
  `global-lp-vertex-sufficiency`/`lp-duality-split-polytope` rounds 10–12,
  all refuted (Mass-Constraint Theorem, Perfect-Tie-Family Characterization,
  exact transplant refutation).

### Small-case / intuition notes
- (Conjecture, strongly evidenced, not proved) `c(n)=2^n/(2^{n+1}-1)`,
  attained by `LB`'s geometric partition; `c(0)=1`, `c(1)=2/3` proved.
- (Conjecture) The middle-regime vertex enumeration for `GT(m)` is exact at
  `m=3,4` (hand-verified) and has strict slack at `m=5` (33 > 32) — no
  counterexample found at any tested `m`, consistent with `GT(m)` being
  true for all `m`, but the general argument is missing.
- (Conjecture) No fixed named-tool/bounded-`s_0` construction family closes
  the upper bound at `e_0` for all `n` — three independent negative results
  now converge on this (Mass-Constraint, Perfect-Tie-Family, exchange
  refutations), reinforcing that only a genuinely `p`-dependent or
  invariant-based argument (not a fixed finite construction) can close the
  upper bound — this is additional, convergent evidence (not proof) that
  the discharging/invariant framing proposed above targets the right kind
  of mechanism, even though its specific naive variants have twice failed.
