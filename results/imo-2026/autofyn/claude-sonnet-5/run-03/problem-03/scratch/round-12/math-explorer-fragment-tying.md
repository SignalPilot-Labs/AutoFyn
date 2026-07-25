# Math-explorer report — lens: fragment-vs-fragment tying / region-boundary monotonicity (round 12)

Problem: imo-2026-03. Scouting only, for `approaches/global-lp-vertex-sufficiency.md`
("Existence Theorem," Σ-shape part of the candidate set `Q`). No proof attempted.

## 1. Exactly what is open, stated precisely

Setup (all imported, certified): reduction to
`c(n) = max_p V(p)` over the balanced region `B(n)` (`k=n+1` pieces,
`p_1<1/2`, every gap `>γ(n)=1/(2^{n+1}-1)`), where `V(p)` is the certified
**Finite-Cell Affine-Vertex Reduction Theorem**'s value: `V(p^*) = V(q^*)`
for some `q^*` in the finite candidate set
`Q = {solutions of (k-1)-subsets of L set to 0}`, where `L` is a finite list
of affine functionals split into two disjoint groups:

- **Region functionals** (the `n+2` inequalities defining `B(n)`'s closure:
  `p_1≤1/2`, the `n` gap inequalities, `p_k≥0`). The candidates drawn only
  from `(k-1)`-subsets of this group are `Q_region ⊂ Q`, and — per rounds
  10/11 — **`Q_region` is fully classified (exact vertex count/coordinates,
  all `n≥2`) and fully closed (`V(q)≤c(n)` exactly at every `q∈Q_region`,
  via the Boundary Continuity Theorem plus exact `k`-Anchor-Merge
  evaluation)**.
- **Σ-shape functionals** (validity boundaries `x_σ(p)_a=0`, between-branch
  ties `f_σ(p)=f_τ(p)`, and — new round 11 — within-branch rank-pinning
  ties `y_σ(p)_a=y_σ(p)_b`), coming from the finite but uncharacterized
  shape set `Σ(n,k)` of the Global Vertex Lemma. **The candidates drawn
  from `(k-1)`-subsets involving at least one Σ-shape functional are
  entirely unaddressed.** This is the only piece of `Q` left; closing it
  (or proving the true maximizer `p*` never lands there) is exactly what
  remains of the Existence Theorem.

So concretely, two live routes to close this residual, both flagged by
round 11's builder as next targets:

**(A) Fragment-vs-fragment tying** = a *construction*-side target: exhibit,
for every `n` and every `p∈B(n)`, an explicit legal response (a member of
`Σ(n,k)`, i.e. a specific cut-allocation + pin assignment) achieving
`OddSum ≤ c(n)`, where the tying mechanism pairs two **fragments of
different split pieces** to each other (`x_a = x_b` for some tie value not
required to equal any whole untouched piece's value), as opposed to the
round-11 refuted family which always ties a fragment to a *whole untouched
piece's* value. This is a genuinely different, more flexible construction
family (see §2 for why it evades the round-11 Mass-Constraint obstruction
in principle, and §3 for a numeric stress-test of whether it evades it in
practice).

**(B) Region-boundary monotonicity** = a *reduction*-side target,
completely different in character: prove that for every interior point
`p∈B(n)` (not already on `∂B(n)`), there is *some* direction `d` pointing
toward the boundary `∂B(n)` (i.e. increasing one of the slack quantities
`1/2-p_1`, `p_i-p_{i+1}-γ(n)`, `p_k` toward `0`... more precisely
*decreasing* one of them toward `0`) along which `V` is **weakly
non-decreasing**. If true for every interior `p`, the maximizer `p*` of
`V` over the closed region can always be pushed to `∂B(n)` without
lowering `V`, which — combined with the already-certified Boundary
Continuity Theorem (Section 4.2) — would force `p*` into the closure of
`∂B(n)`, i.e. into `Q_region`'s territory, **entirely bypassing the need
to classify `Σ(n,k)`.** This is Opening 2 from round 11's dispatch; it has
not been attempted by any approach yet.

## 2. Why (A) is not obviously refuted by the Mass-Constraint Theorem

The certified Mass-Constraint Theorem
(`lemmas/rank-pinning-lemma-and-mass-constraint-theorem.md`) shows: if
every split piece's fragments are matched **against a whole untouched
piece's value** (the General Multi-Piece Subset-Tie family), then the
split pieces' total mass `Π=Σp_{i_a}` must satisfy `Π≥1/2` (sum the
legality constraints `T_a≤p_{i_a}` and use `ΣT_a=1-Π`). Combined with the
top-piece bound `p_1(e_0)<3/(2(n+1))` at the closed vertex `e_0`, this
forces `s>(n+1)/3` split pieces — unbounded in `n`.

**This argument is structural to the "tie against a whole untouched
piece" mechanism specifically**: the `1-Π` term comes directly from
`ΣT_a=Σ_{m∈U}p_m`, i.e. from every unit of untouched mass being
literally consumed as a tie target. A fragment-vs-fragment tie `x_a=x_b`
between two split pieces `i_a,i_b` places **no such constraint on
untouched mass at all** — the tied value `x` can be any amount up to
`min(p_{i_a},p_{i_b})`, freely chosen, not forced to equal a specific
untouched piece's value. So the Mass-Constraint Theorem's proof does not
transfer, and in principle a small, fixed number of split pieces could
supply arbitrarily many internal ties among themselves without consuming
untouched mass at all. This is exactly why round 11 flagged fragment-vs-
fragment tying as "not covered" and "the most promising open lead" —
worth taking seriously, not dismissing by analogy.

## 3. Numerical stress test (exact-`e_0` target, unconstrained numeric search)

To check whether this extra flexibility is *actually* enough to give
bounded-`s_0` sufficiency, I ran an **unconstrained** numeric search (not
assuming any specific tying pattern — Nelder–Mead over raw fragment
proportions, softmax-parametrized for positivity) at the exact,
already-classified hard vertex `e_0` (Section 4.1/4.3 of
`global-lp-vertex-sufficiency.md`; `V(e_0)=c(n)` exactly, proved). Exact
`Fraction` arithmetic was used to compute `e_0`'s coordinates and `c(n)`
(`γ(n)=1/(2^{n+1}-1)`, `p_i(e_0)` an arithmetic progression from
`p_1(e_0)`), and the search's objective was evaluated on the resulting
floats. Splitting the **top `s` pieces** into `2` fragments each (using
only `s≤n` cuts, well inside budget), best-of-many-restarts:

| n | c(n) | s=2 | s=3 | s=4 | s=5 | s=6 | s=7 |
|---|---|---|---|---|---|---|---|
| 6 | 0.503937 | 0.511811 (no) | **0.503937 (tight, matches proved V(e0)=c(n))** | 0.503937 | 0.503937 | 0.500062 (yes) | — |
| 8 | 0.500978 | 0.503914 (no) | 0.501957 (no) | 0.501957 (no) | 0.500506–0.500979 (borderline, noisy) | 0.500133–0.501328 (noisy) | 0.500896–0.50 (noisy) |

(`n=8`'s `s=5,6,7` rows are reported as ranges because two independent runs
with different restart counts disagreed on whether the threshold is
crossed at `s=5` vs. needing `s≥6` — the true minimum is close enough to
`c(8)` that Nelder–Mead's local convergence is unreliable at this
precision; **this numeric harness is not able to certify an exact minimal
`s`**, only to give qualitative signal.)

**What this does and does not show.**
- It **confirms the harness is correct**: at `n=6`, the unconstrained
  search's best value with `s=3` split pieces matches the already-*proved*
  exact value `V(e_0)=c(6)=64/127` to 6 decimal places, exactly as
  expected from the certified theorem — a useful sanity check, not a new
  result.
- It gives a **soft negative signal for bounded-`s_0` sufficiency in
  general**, including via fragment-vs-fragment mechanisms: the smallest
  `s` at which the *unconstrained* search (which is free to discover
  fragment-vs-fragment ties, tie-to-untouched-piece ties, or any other
  pattern the optimizer likes) first clears `c(n)` **grows with `n`**
  (`3` at `n=6`, evidently `≥5` at `n=8`, not resolved cleanly by `n=10`
  in the time budget) at a rate that looks broadly consistent with — not
  contradicting — the `~(n+1)/3` to `~(n+1)/2` growth the Mass-Constraint
  Theorem already proved for the narrower tie-to-whole-piece family. This
  is **not a proof** (Nelder–Mead is a local numerical optimizer, not
  exhaustive over `Σ(n,k)`, and "split the top `s` pieces" is one natural
  but unproved-optimal choice of which pieces to split), but it means
  fragment-vs-fragment tying should **not** be assumed to rescue
  bounded-`s_0` sufficiency without further evidence — the flexibility
  argument in §2 is a real structural fact but does not, by itself,
  translate into a working bounded construction at the specific point
  `e_0` where the mass-constraint family already fails hardest.
- I did **not** find, in this budget, an exact rational witness of a
  fragment-vs-fragment construction beating `c(n)` with `s` bounded
  independent of `n` — nor did I find a proof that none exists. This
  remains genuinely open in both directions.

## 4. Crux corpus scouting (LP-vertex / extremal-point techniques)

The corpus (`crux_moves_documentation.md`, `past_crux_moves_database.json`)
has no problem shaped like this one (a two-phase minimax game with a
sort-and-sum objective), so nothing is a direct transplant. The closest
load-bearing moves, worth adapting rather than citing:

- **`aimo-0146`** (combinatorics, `extremal-principle` /
  `invariants-and-monovariants`): "Maximize a fixed weighted sum of a
  sorted nonnegative integer sequence under a sum constraint by
  exchange-smoothing weight toward the higher-coefficient position," and
  "verify a functional is monotone under a local edge-rerouting move by
  checking it never decreases a specific quantity." This is the same
  shape as target (B) above (`OddSum` is exactly a fixed-weight sum of a
  sorted sequence, weight `1` on odd ranks, `0` on even) — the technique
  to adapt is proving a **local exchange move** (shifting mass between two
  adjacent pieces) never decreases `OddSum`, which is precisely what
  region-boundary monotonicity needs, just applied to the *outer*
  `p`-level sum rather than the inner fragment-level one this project has
  mostly worked with so far.
- **`aimo-0287`** (algebra, `extremal-principle` /
  `symmetric-functions-and-substitution`): "Test a single boundary
  exchange (drop one element, add an adjacent one)... push exactly the two
  boundary coordinates toward each other by half the surplus, dispose of
  the exceptional configuration where the optimum has no interior
  boundary." This is a template for exactly the kind of "move `p_1,p_2`
  toward each other along the region-boundary direction, handle the
  degenerate case separately" argument (B) would need — a concrete
  playbook, not a citable result (the objective and constraints differ,
  so every step must be reproven from scratch per `CLAUDE.md`).
- Nothing in the corpus addresses a genuinely non-concave, piecewise-affine
  value function's boundary behavior directly — this project's own
  Rank-Pinning/Finite-Cell machinery is already more specialized than
  anything retrievable here. No further corpus lead found for the
  Σ-classification side (unbounded-piece constructions / compactness);
  this looks like an area where the project's own machinery (Lipschitz
  continuity, Small-Mass Insertion Lemma) is already the right toolkit,
  not something to import.

## 5. Terrain summary and recommended next step

Three live threads for `global-lp-vertex-sufficiency`'s Existence Theorem,
in order of how promising this scouting found them:

1. **Region-boundary monotonicity (Opening 2, target (B) above) — most
   promising, not yet attempted.** Concrete mechanism to try: use the
   *already-proved* Finite-Cell structure itself. On any fixed cell `C` of
   the `L`-arrangement, `V=f_{\sigma(C)}` is affine (certified, Lemma 4.1).
   Fix `p∈C∩B(n)` and a line `p(t)=p+t\cdot d` for a boundary-normal
   direction `d` (e.g. `d` moves mass from `p_2` into `p_1`, decreasing the
   `p_1<1/2` slack, or moves mass between two adjacent pieces to shrink one
   gap toward `γ(n)`). Since `f_{\sigma(C)}` is affine, `V` is *exactly
   linear* in `t` while `p(t)` stays in `C` — hence trivially monotonic
   (weakly) in **one** of the two directions `±d`. The gap not yet closed:
   proving that a *consistent* choice of which direction (`+d` or `-d`) to
   use can be made *before* knowing which cell `p` sits in (or handling the
   cell-crossings along the chosen line via the certified Lemma-4.2-style
   continuity mechanism, extended to a *monotonicity*-preserving version —
   this is a new argument, not automatic from continuity alone: continuity
   only says the two affine pieces agree at the crossing point, not that
   both are simultaneously non-decreasing through it). This is a smaller,
   sharper target than classifying all of `Σ(n,k)` and reuses proved
   machinery (Lemma 4.1, Lemma 4.2's density/continuity technique, and the
   `aimo-0146`/`aimo-0287` exchange-argument templates from §4) — the
   single most concrete, buildable next step.
2. **Fragment-vs-fragment tying (Opening 1 continuation, target (A)) —
   structurally not ruled out, but this round's numeric stress-test gives
   a soft negative signal (§3): the unconstrained numeric optimum at the
   hardest known point `e_0` still seems to need growing `s`, similar to
   the already-refuted family. Worth at most one more focused attempt (a
   specific fragment-vs-fragment construction proved, not searched, e.g.
   generalizing the certified Singleton-Interleaving Lemma to tie
   `2`,`3`,... fragments from *different* split pieces to each other in a
   chain) before treating it as likely also insufficient for bounded `s_0`.
3. **Unbounded-piece / limiting constructions** (this round's third
   mandated scouting direction) — no concrete mechanism found. A
   compactness/limiting argument (`s\to\infty` as `n\to\infty`, in the
   spirit of the Mass-Constraint Theorem's own asymptotic `s/(n+1)\to1/2`
   finding) would need to characterize the *limit shape* of the optimal
   response, which is exactly as hard as classifying `Σ(n,k)` in the
   limit — no shortcut identified. Not recommended as the next dispatch
   target; deprioritize below (1) and (2).

**Bottom line for next round's outliner:** dispatch a builder at Opening 2
(region-boundary monotonicity) as the primary new target for
`global-lp-vertex-sufficiency` — it is the only one of the three
candidates with a concrete, already-partially-proved mechanism (cell-wise
affineness) to build from, and if it succeeds it would close the Existence
Theorem outright without needing any bound on `|Σ(n,k)|`. Keep fragment-
vs-fragment tying (Opening 1) as a secondary, lower-priority target given
this round's soft negative numeric signal.
