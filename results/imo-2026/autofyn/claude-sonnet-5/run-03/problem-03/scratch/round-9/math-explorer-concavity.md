## imo-2026-03 (lens: Existence Theorem / concavity-of-V(p) obstruction)

### Precise restatement of the object

By the certified Reduction Lemma, for fixed `n`, `k≤n+1`:
`c(n) = max_p V(p)`, `V(p) := min over legal XY responses (cut-allocation m
with Σm_i≤n, then split each p_i into m_i+1 positive fragments) of
OddSum(resulting multiset)`, `p` ranging over the simplex `{p_i>0, Σp_i=1}`.
The Existence Theorem (the sole open sub-problem of the upper-bound
direction) is: `V(p)≤c(n)` for every `p` in the "balanced region"
(`k=n+1`, `p_1<1/2`, every consecutive gap `>γ(n)=1/(2^{n+1}-1)`).

"Concavity" as the round-8 approach wanted it: `V` concave on the balanced
region's polytope, which (combined with the already-certified Global
Vertex Lemma — `V` is a min, over a finite `p`-independent set `Σ(n,k)` of
combinatorial "shapes," of affine-in-`p` candidate formulas restricted to
each shape's validity region) would let the max of `V` reduce to
finitely many extremal/boundary configurations, exactly mirroring how
Theorem 3 and Theorem B closed lower-dimensional analogues.

### Why the classical LP-RHS-convexity fact does not transfer (confirmed)

The standard fact is: `val(b) = min{c^T x : Ax=b, x≥0}` is convex in `b`
when `c` is *fixed*, via LP duality (`val(b)=max{y^Tb : A^Ty≤c}`, a sup of
linear functions of `b`). Here, for a *fixed* cut-allocation/shape, the
objective `OddSum` is a fixed linear functional only *after* the sort
order is pinned — but `p` enters not just the constraint RHS
(`Σ fragments of piece i = p_i`) but the objective itself directly:
untouched pieces `p_j` are literal entries of the multiset being
OddSum'd, and after solving for the "free block" (Global Vertex Lemma),
its value is itself an affine function of the *other* `p_j`'s. So the
"cost vector is `p`-independent" hypothesis genuinely fails; only
piecewise-linearity (constant within a fixed optimal basis/shape) survives
from parametric-LP theory, not global convexity/concavity across
basis/shape changes. This diagnosis (already in the certified lemma file)
is correct and I could not find a variant of the classical theorem
covering "parameter enters both objective and RHS linearly" that
salvages global concavity.

### NEW: concavity is numerically FALSE (round-8's "no violation" finding was an artifact of weak testing)

I built an independently-implemented, higher-fidelity `V(p)` computation
(exhaustive enumeration of all cut-allocations `m` with `Σm_i≤n`, each
continuous split optimized via multi-restart Nelder-Mead **and**
cross-checked with `scipy.optimize.differential_evolution`, both giving
identical results to 4+ decimals) and swept a straight line through the
balanced region at `n=2` (`k=3`): fix the ratio `p_2:p_3` and vary `p_1`
from 0.15 to 0.49.

Result: `V` along this line is **not concave** — it has multiple genuine
"dip" (locally convex) segments, e.g. at `p=(0.5146,0.3154,0.17)`,
`(0.5022,0.3078,0.19)`, `(0.4898,0.3002,0.21)`:
`V=0.51460, 0.50220, 0.51020` respectively (reproduced identically by two
independent optimizers). The midpoint value `0.50220` is **below** the
average of the endpoints `(0.51460+0.51020)/2=0.51240` by a margin of
`≈0.0102` — far outside any plausible numerical-noise band (both
optimizers agree to 4 decimals, and increasing restarts from 10→30
changed nothing). Several other segments along the same sweep show the
same pattern (second differences alternate sign: `+0.0204` at `p_1=0.19`,
`+0.0202` at `p_1=0.27`, `+0.0206` at `p_1=0.39`, etc.) — a genuine
up-down-up oscillation, not a single valley.

**Diagnosis of the mechanism**: at all three points above the *same*
cut-allocation shape wins (`m=(1,0,0)`, i.e. split only the top piece
into 2 fragments, using only 1 of the 2 available cuts) — yet `V` is
still non-affine across them. This means the optimal **pin value** for
the free fragment (in the Global Vertex Lemma's sense — the split
fragment is pinned to `0`, `p_2`, or `p_3`) itself switches as `p_1`
varies (since `p_2=0.62(1-p_1)` and `p_3=0.38(1-p_1)` move at different
rates), so even within one combinatorial shape-class `m` there are
multiple genuinely different affine sub-branches (different pin
choices), and switching between them, combined with which branches are
*valid* (nonnegative fragments) at each `p`, produces exactly the
non-concave dip the round-8 file worried was possible in the
"validity gap" between the true `V` and its naive concave relaxation
`V̂`. **This is a clean, reproducible, exact-optimizer-cross-checked
counterexample to global concavity of `V(p)`** — concavity should be
abandoned as a target, not merely left open.

(Caveat: this refutes concavity as literally stated over the *whole*
balanced region on this one segment at `n=2`; it does not by itself rule
out a *weaker*, still-useful property — see next section.)

### Alternative that could still finish the Existence Theorem without concavity

The Global Vertex Lemma already gives: `V(p) = min_{σ∈Σ, valid at p}
f_σ(p)` with `Σ` finite and each `f_σ` affine, and validity `x_σ(p)≥0` an
affine (half-space) condition. **Key point I want to flag for the
outliner**: concavity was never actually *necessary* — what is needed is
just that `V` is *piecewise affine with finitely many convex pieces* on
the balanced region, because a genuinely affine function's max over a
convex polytope is always attained at a vertex, regardless of whether the
overall piecewise function is globally concave, convex, or neither.

Concretely: let `L` be the finite list of affine functionals on `p`-space
consisting of (a) every component of every `x_σ(p)`, `σ∈Σ` (the validity
boundaries) and (b) every pairwise difference `f_σ(p)-f_τ(p)`, `σ,τ∈Σ`
(the branch-comparison boundaries), together with the balanced region's
own defining inequalities (`p_1=1/2`, each gap `=γ(n)`). This is a
**finite hyperplane arrangement** in `p`-space. On each open cell of the
induced polyhedral subdivision, every functional in `L` has constant
sign, so: (i) which `σ`'s are valid is locally constant, and (ii) which
valid `σ` wins all pairwise comparisons is locally constant — hence `V`
equals a *single fixed affine formula* on the whole (open, hence by
continuity closed) cell. Therefore `V` restricted to each cell (a convex
polytope) is genuinely affine, so its max over `cell ∩ balanced-region`
is attained at a vertex of that intersection — a vertex of the whole
arrangement. Since the arrangement is finite, this gives a **finite
candidate set of extremal `p*`'s, without ever needing concavity** — a
strictly weaker and (now, given the numeric refutation above) strictly
*correct* substitute for the round-8 target. This is essentially the
same "vertex of a finite arrangement" philosophy the project has already
used one level down (fragment-space, in the Vertex Pinning /
Single/Two-Piece Vertex Lemmas), just applied one level up in `p`-space.
The catch, honestly: `|Σ(n,k)|` and hence the number of hyperplanes/cells
could be combinatorially large, so this converts the problem into "a
finite but possibly huge case check" rather than an immediately tractable
closed form — real combinatorial work (bounding/classifying which
comparisons can actually be tight simultaneously, or which cells actually
intersect the balanced region) is still needed to make this practical,
but it is a mathematically complete, correct route that does not depend
on the (now-refuted) concavity claim.

**Quasi-concavity / Sion's minimax theorem**: I looked at whether a
weaker property suffices. Quasi-concavity of `V` (convex superlevel
sets) would *not* by itself give a vertex-of-arrangement reduction the
way full concavity or the piecewise-affine argument above does — a
quasi-concave function on a polytope can still attain its max in a face's
relative interior, not just at vertices, so it doesn't obviously shortcut
anything here; not pursued further. Sion's minimax theorem (swap of
`min`/`max` for a bifunction quasi-concave-usc in one variable,
quasi-convex-lsc in the other, on convex compact sets) does not obviously
apply either: for a fixed cut-allocation shape, `OddSum` as a function of
the continuous fragment values is only affine *within* a fixed sort-order
region (neither convex nor concave once sort order can change across the
domain), so the "bifunction" here fails the quasi-convexity-in-response
hypothesis globally, and I did not find a way to restrict to a
subdomain where it would hold without reintroducing exactly the
same validity/branch-switching structure driving the concavity failure.
I do not recommend pursuing Sion's theorem further without a much more
specific reformulation than what's on the table. Danskin's theorem
(envelope theorem for `max` of a parametrized differentiable family) is
the wrong shape too — it gives *directional derivatives* of a value
function, useful for local sensitivity, not a global finite-vertex
reduction; not clearly useful here either given `V` is already known to
be non-smooth (Lipschitz only) at branch-switch boundaries.

### Knowledge-base entries relevant

- **"Piecewise-concavity smoothing"** (Algebra & Polynomials section):
  the general pattern "partition the domain by the zeros of finitely many
  named linear/simple functions; the function is then concave/affine on
  each piece; a extremum of the whole piecewise function occurs at a
  breakpoint or an endpoint of a piece" is exactly the same *shape* of
  argument as the hyperplane-arrangement idea above (there it's zeros of
  sinusoid arguments driving a *min* to a breakpoint; here it's the
  finite hyperplane arrangement from `Σ(n,k)` driving a *max* to a
  vertex). Worth citing by name as the template/precedent for this style
  of finite-piece extremal reduction, even though the concrete mechanics
  differ (that entry is about a 1-D circle parametrization; this is a
  `k-1`-dimensional polytope).
- **"Extreme value theorem / Lagrange multipliers on a compact manifold"**
  (Linear Algebra section): already the tool underlying the existence-of-
  maximizer step (Section 3 of the certified lemma); not directly useful
  for locating the maximizer since `V` is non-smooth.
- No entry in `knowledge_base.md` states Sion's minimax theorem, Danskin's
  theorem, or general parametric-LP value-function theory by name; these
  are not currently knowledge-base tools for this project (confirmed by
  grep).

### Crux corpus check

Per `crux_moves_documentation.md`, filtered `domain=combinatorics` for
techniques mentioning polytope/vertex/linear-programming/minimax/convex
keywords (26 hits) and separately scanned `games-and-strategy` broadly
(consistent with round 6's finding). None are genuine analogues: the
hits are extremal-principle arguments about discrete point configurations
(convex position, convex hull vertices of a finite point set), not a
continuous parametric-LP/minimax value function with the parameter
entering both objective and constraints. This reconfirms round 6's
"NEVER assume a crux subtopic match implies a usable analogue" finding —
**no crux corpus match found** for this specific obstruction; do not
force one.

### Summary for the outliner

- Distinct openings: (1) the finite-hyperplane-arrangement /
  vertex-of-cells argument above, a complete and correct (if
  combinatorially heavy) substitute for concavity, ready to be developed
  as the approach's actual next section; (2) treat the numeric
  counterexample as settling that concavity itself is a dead end — do not
  spend another round trying to prove it; (3) if the arrangement approach
  proves too large to make concrete, consider whether a *local* version
  suffices (e.g. only need `V≤c(n)` on the finitely many "survivor"
  configurations already located by `universal-halving-adversary` and
  `lp-duality-split-polytope`'s triangular family, i.e. maybe the true
  global maximizer of `V` over the balanced region is actually attained
  exactly at one of these already-catalogued families, checkable directly
  without a full arrangement enumeration).
- Candidate technique(s): finite hyperplane-arrangement / piecewise-affine
  vertex reduction (new, not concavity); NOT quasi-concavity, NOT Sion's
  minimax (both checked and found unpromising as stated).
- Cheap-kill candidates: none beyond what's already used; the region is
  already reduced to a compact polytope with a known finite branch
  structure — the remaining work is genuinely combinatorial (bounding
  `|Σ(n,k)|`/cell count or finding structure that prunes most cells), not
  a parity/pigeonhole shortcut.
- Knowledge-base entries to use: "Piecewise-concavity smoothing" (as a
  structural template/precedent, not a literal citation), "Extreme value
  theorem ... on a compact manifold" (already used for existence).
- Analogous past problems (cruxes): none genuinely analogous found (26
  loosely keyword-matched combinatorics cruxes checked, all about discrete
  point-set convex position/extremal principle, not continuous parametric
  LP/minimax) — consistent with round 6's finding, do not force a match.
- Prior progress: Global Vertex Lemma (certified) + Lipschitz continuity
  (certified) + existence-of-maximizer (certified), all from
  `lemmas/global-vertex-lemma-and-lipschitz-continuity.md`; these are all
  reused unchanged by the arrangement-based alternative above (it builds
  directly on the Global Vertex Lemma's finite `Σ(n,k)` and affine
  branches — no new prerequisite machinery needed to start).
- Dead ends (do not retry): global concavity of `V(p)` — now numerically
  **refuted** (not just "unresolved"), with a reproducible, two-optimizer
  cross-checked counterexample at `n=2` (`p=(0.5146,0.3154,0.17)` vs.
  midpoint `(0.5022,0.3078,0.19)` vs. `(0.4898,0.3002,0.21)`, deficit
  `≈0.0102`, well outside noise). Round 8's "no violation in 15 trials"
  finding was a false negative caused by a much coarser proxy for `V`
  (best-of-many-random-splits, few restarts) evaluated only at randomly
  chosen deep-interior points that happened to stay within a single
  affine chamber — the same "weak/coarse test gives false reassurance"
  failure mode flagged repeatedly in `/tmp/memory/math-explorer.md`
  (rounds 1, 8). Do not revisit concavity as a target; do not trust
  small/coarse numeric concavity checks on `V(p)` in general — sweeps
  crossing branch/validity boundaries (not just random interior pairs)
  are needed to detect the real (kinked) structure.
- Small-case / intuition notes (conjecture only): `V(p)`'s branch
  structure is much finer than the raw cut-allocation `m` — even fixing
  `m`, the optimal *pin choice* for a free fragment can switch as `p`
  varies continuously, producing multiple genuine kinks per shape-class;
  the true maximum of `V` over the balanced region is very likely
  attained at a boundary/breakpoint configuration (consistent with the
  general "extremal-at-breakpoint" pattern seen throughout this project's
  other closed sub-theorems), but *which* breakpoint requires the
  arrangement-level analysis above, not a concavity shortcut.
