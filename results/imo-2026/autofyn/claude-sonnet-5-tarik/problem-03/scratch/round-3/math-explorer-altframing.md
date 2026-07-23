## imo-2026-03 (lens: genuinely different top-level framing — is there a route around
local smoothing/casework, e.g. minimax duality / LP / probabilistic / continued fractions?)

### Verdict up front
The field has **not** truly collapsed to one framing — `dyadic-cascade-induction` and
`elementary-exchange-smoothing` both do explicit local casework near the dyadic point, but
they differ in *how* they organize that casework (exhaustive sign-regime algebra vs.
concave-gradient-hull certificate). Genuinely orthogonal to both: I found and numerically
stress-tested a **global-concavity route** that, if it can be made rigorous, replaces
`dyadic-cascade-induction`'s entire Case (i)/(ii) exhaustive casework with one convexity
lemma + `elementary-exchange-smoothing`'s already-proven local certificate. This is the
headline finding below. `concavity-minimax-duality.md`'s existing sketch of this idea is
flagged in its own text as "highest-risk/undeveloped" — I re-examined it and its literal
Step-3 argument is actually **unsound as written**, but the underlying *conclusion*
(concavity of the value function `g`) held up in every numerical test I ran at `n=2`. So:
not dead, but needs a real fix, not the argument currently on file.

### Distinct openings

**1. (Most promising, genuinely new work this round) Global concavity of `g` + import
`elementary-exchange-smoothing`'s local certificate ⟹ bypass all Case (i)/(ii) casework
for the upper bound at n=2.**

Definition: `g(a) := ` XY's best-response value (the *true* game value, min over all of
XY's legal responses) as a function of LB's sorted opening `a=(a_1≥…≥a_k≥0)`, `Σa_i=1`.
`elementary-exchange-smoothing` Step C already rigorously proves (via a finite-min-of-3-
affine-functions + gradient-hull certificate `λ=(2/7,1/7,4/7)`) that `(4/7,2/7,1/7)` is a
**strict LOCAL maximizer** of `g`, in an honest open neighborhood inside the sorted
simplex domain — a real, certified, non-numerical result, conditional only on the (still
open) fact `g(4/7,2/7,1/7)=1/7`.

**Standard fact of convex analysis** (not in `knowledge_base.md` under this name, but a
direct consequence of the definition of concavity): *if `g` is concave on a convex domain,
any strict local maximum is automatically the unique GLOBAL maximum* — a concave function
cannot have two distinct local maxima that aren't both global. So **if `g`'s global
concavity over the whole sorted-simplex domain can be proved**, `elementary-exchange-
smoothing`'s existing local certificate immediately promotes to a complete, casework-free
proof that `(4/7,2/7,1/7)` is the unique maximizer of `g` over the ENTIRE domain — i.e. the
**entire upper-bound direction at n=2, done in one shot**, with `dyadic-cascade-induction`'s
four-sign-regime hand computation becoming unnecessary (though still valuable as an
independent cross-check).

*Numerical stress test (this round, not done previously in this population).* I implemented
a randomized strategy-space search for `g(a)` at `n=2` (candidate cuts: bisect / tie-to-
existing-value / random, up to 2 cuts, thousands of trials per point — reproduces the known
exact value `g(4/7,2/7,1/7)=4/7` to full float precision as a sanity check) and tested the
concavity inequality `g(midpoint) ≥ (g(p1)+g(p2))/2` on:
- 5 hand-picked pairs spanning Case (i), Case (ii), and points straddling their shared
  boundary, all near and far from the dyadic point — **0/5 violations**.
- 25 uniformly-random pairs drawn from the full sorted simplex — **0/25 violations**.
- 4 targeted boundary-crossing pairs (crossing `a_1=2a_2`, crossing `a_2=2a_3`, and a pair
  approaching the degenerate `a_3→0` edge) — **0/4 violations**.
This is **strong numerical evidence** (conjecture, not proof) that `g` is genuinely concave
on the whole domain at `n=2`, not merely piecewise-concave within each hand-derived regime.

**Why the existing `concavity-minimax-duality.md` Step 3 argument for this is unsound as
written (important correction, not a full retraction of the idea):** it claims "`g` is the
pointwise infimum of finitely many combinatorial-pattern functions, each affine on its own
domain, hence `g` is concave" — citing "infimum of affine functions is concave." This
standard fact requires each function in the family to be affine **on the whole domain** (or
at least defined and dominating `g` everywhere); here, each *named* XY strategy (e.g.
"bisect `a_1`") is only affine within the sub-region where the sorted order it assumes
actually holds — outside that region the same concrete cutting rule gives a *different*
affine formula (because the final sorted order changes), so each strategy's own value
function, tracked honestly across the whole domain, is **piecewise-affine, not affine**. A
pointwise min of piecewise-affine (not affine) functions is piecewise-affine but is **not
automatically concave globally** — this is exactly why, e.g., `dyadic-cascade-induction`'s
Case (i) and Case (ii) needed genuinely different formulas and four separate sign sub-
regimes even just within Case (ii). So the literal Step 3 text should be treated as a
**disproven justification**, even though the numerical evidence above suggests its
*conclusion* survives. **This is the real open gap for this opening**: find the correct
argument for global concavity (candidates: an exchange/rearrangement argument showing any
two "adjacent-regime" affine pieces of `g` meet with a concave kink, i.e. the piece on the
side of larger `a_1` always has smaller slope — this is a checkable, finite, cell-by-cell
condition, structurally similar to what `dyadic-cascade-induction`'s own case analysis
already computed piece-by-piece but never assembled into a global concavity statement).
Also drop that file's invocation of Sion's minimax theorem — **it's a red herring**: this
is a *sequential* (Stackelberg: LB commits, then XY responds with full information) game,
not a simultaneous-move matrix game, so there is no min/max order to swap; `c(n) =
max_a min_{XY} L` is already exactly the quantity defined by the problem statement, no
minimax theorem needed to justify its existence (ordinary compactness of the simplex +
upper semicontinuity of `g`, noted in passing in that file, suffices).

**Caveat — this does NOT sidestep the shared lower-bound gap.** Even a fully rigorous
global-concavity + local-certificate argument only proves `g(a) ≤ g(4/7,2/7,1/7)` for all
`a` — it still needs `g(4/7,2/7,1/7) = 1/7` exactly as an independent input (the same "does
the dyadic point resist every XY response" fact that is the shared open gap flagged in
`current.md` and in the parallel lower-bound explorer's report this round). So this opening
replaces/streamlines the **upper-bound casework only**; it is a genuinely different
top-level strategy for that half, not a full solve.

**n≥3 check — inconclusive, flagged honestly.** I ran the same concavity test at `n=3`
(dyadic point `(8,4,2,1)/15` vs. `(0.4,0.3,0.2,0.1)`, 3 cuts allowed) and found a small,
*reproducible across 3 different random seeds* apparent violation (`g(mid)≈0.5083 <
avg≈0.5167`). I do **not** trust this as a real violation — the search space at `n=3` (up to
3 sequential cuts, each with many candidate tie-targets) is much larger and my randomized
sampler under-samples it; since `g_numeric` is a min over a *finite sample* of strategies, it
is always an over-estimate of the true `g`, and an apparent "violation" could equally be an
under-sampling artifact at the midpoint's less-round-number coordinates (matches to
non-round fractions are less likely to be hit by a value-matching heuristic sampler) rather
than a real failure of concavity. **Flag as: needs a more careful (non-random,
vertex-enumeration-based) check before either believing or discarding global concavity at
`n≥3`** — do not treat this as either confirmation or refutation.

**2. Dominance/superincreasing induction (found independently by the parallel lower-bound
explorer this round, `/tmp/round-3/math-explorer-lowerbound.md`) — genuinely complementary,
not overlapping with opening 1.** `D_n=(2^n,…,2,1)` is superincreasing (`2^k > 2^k-1`), which
forces a real two-sided case split ("XY cuts `a_1`" vs. "XY leaves `a_1` alone") for the
*lower-bound* direction specifically, and that explorer numerically confirmed "leave `a_1`
alone" is a badly suboptimal branch for XY (best found `e≈2/7`, far from target `1/7`). This
is a different half of the problem (lower bound, not upper bound) from opening 1 above, and
the two combine naturally: opening 1 (global concavity) attacks "no other `a` beats the
dyadic point," while the dominance lemma attacks "no XY response beats `1/7` at the dyadic
point itself" — together they would close n=2 fully, and the recursive peel-off-`a_1`
structure in both suggests a **joint induction on n proving both halves together** (also
flagged independently by that explorer) is probably the cleanest eventual framing, rather
than "prove upper bound for all n" and "prove lower bound for all n" as two separate,
unrelated inductions.

**3. Probabilistic / generating-function / continued-fraction reframings — searched, no
traction found.** I scanned the crux corpus's `probabilistic-method` and
`generating-functions` subtopics (combinatorics domain) and found no crux whose mechanism
transfers to a deterministic, full-information, sequential two-player cutting game — those
techniques are for existence-by-counting or algebraic-encoding problems, not adversarial
optimization with full information, so there's no natural role for randomness or formal
power series here (nothing to "generate" — the state space at each `n` is a finite
combinatorial casework, not an infinite series). The recursion `e_n=e_{n-1}/(2+e_{n-1})`
does look continued-fraction-shaped, but unrolling it algebraically (already done in
`current.md`) already gives the closed form `e_n=1/(2^{n+1}-1)` directly — I could not find
any KB entry or crux move that uses a continued-fraction/Stern-Brocot argument to *prove*
(rather than just state) that a recursively-defined adversarial game value equals such a
closed form; this looks like a description of the answer's shape, not an independent proof
technique. Not recommending it as a route — flagging only so a future round doesn't spend a
cycle chasing it without cause.

### Candidate technique(s)
Global concavity of the Stackelberg value function `g(a)` (opening 1) + the already-
certified local gradient-hull certificate — needs a *correct* concavity proof, not the
flawed "infimum of affine functions" argument currently in `concavity-minimax-duality.md`.
Complementary: dominance/superincreasing lock-in (opening 2, from the parallel explorer) for
the lower-bound half.

### Cheap-kill candidates
- **A fast numerical gate before investing in opening 1**: before any round spends real
  effort trying to prove global concavity rigorously, run a denser/adversarial (not just
  random) numerical search for a genuine concavity violation at `n=2` — e.g. explicitly
  search over pairs straddling every named sign-sub-regime boundary from
  `dyadic-cascade-induction`'s own case table (the four regimes: `a_2≥2a_3`/`u≤a_3`,
  `a_2≥2a_3`/`u>a_3`, `a_2<2a_3`/`u≤a_3`, `a_2<2a_3`/`u>a_3`) with points close to each
  boundary on both sides. If a real violation turns up, opening 1 is dead immediately and
  no proof effort should be spent on it — this is a single bounded computation, cheap
  relative to attempting the concavity proof itself.
- No parity/pigeonhole cheap kill applies (continuous optimization, not discrete counting).

### Knowledge-base entries to use
- **"Piecewise-concavity smoothing"** (KB Algebra & Polynomials) — the named entry both
  `elementary-exchange-smoothing` and `concavity-minimax-duality` already invoke; it is
  stated for a *different* concrete setting (sums of `|sinusoid|` terms on a circle), so it
  must be genuinely re-derived/adapted for this problem's min-of-affine-on-cells structure,
  not cited as a black box — its literal minimum-at-breakpoint conclusion doesn't
  automatically give *global* concavity across the cell boundaries here (that's exactly
  opening 1's open gap).
- **General Proof Methods: Induction** — for opening 2's joint two-direction induction.
- No KB entry directly addresses LP/minimax duality for sequential (Stackelberg) games; do
  not force-fit Sion's minimax theorem or von Neumann duality onto this problem (see "Dead
  ends" — the game is sequential with full information, not simultaneous).

### Analogous past problems (cruxes)
Searched broadly per dispatch: `combinatorics/games-and-strategy` (39 cruxes, all read),
`combinatorics/linear-algebra-method`, `combinatorics/generating-functions`,
`combinatorics/probabilistic-method`, `algebra/inequalities-SOS-and-convexity`, plus a
keyword scan for `minimax`/`duality`/`zero-sum`/`von Neumann`/`saddle` across all 2434
cruxes and an `alternat*`/`take turns`/`claim the largest` keyword scan.
- **No crux in the corpus matches this problem's actual mechanism** (a continuous,
  sequential, full-information cutting-and-claiming game solved via a global concavity /
  variational argument). The `games-and-strategy` subtopic is entirely **discrete** pairing/
  invariant/parity/strategy-stealing arguments (mirroring, blocking, parity invariants on
  cell counts) — none transfer to a continuous optimization-over-a-simplex setting.
  No minimax/LP-duality crux exists in the corpus at all (the keyword scan returned only
  unrelated "zero-sum integer triple" number-theory hits).
- Best remaining analogies are the ones the parallel lower-bound explorer already reported:
  **`aimo-0117`** and **`aimo-0401`** (both: dyadic/superincreasing-sequence dominance
  locking the rank of the top element) — genuinely useful for opening 2, not for opening 1.
  I independently confirm these are the best matches after my own broader scan; nothing else
  in the corpus is closer.
- Checked `aimo-0717` (a real IMO-style strip-cutting-into-pieces problem, `2n-1` pieces via
  Eulerian-cycle counting) as a plausible "stick-cutting" analogy — **not actually
  analogous**: it's a deterministic reconstruction/counting problem (minimum pieces to
  reassemble a permuted strip), not an adversarial two-player value game; the technique
  (Eulerian-cycle edge counting) does not transfer.

### Prior progress
See `current.md` (read in full) — `dyadic-cascade-induction` and `elementary-exchange-
smoothing` both fully close the n=2 upper bound's Case (i)/(ii) via local casework;
`elementary-exchange-smoothing`'s Step C (gradient-hull certificate, `λ=(2/7,1/7,4/7)`) is
the exact tool opening 1 above proposes to *globalize* rather than re-derive.
`concavity-minimax-duality` remains unbuilt (Status: unsolved, deprioritized) — its Step 3
sketch is the seed of opening 1 but is unsound as literally written (see above).

### Dead ends (do not retry)
- **`concavity-minimax-duality.md`'s literal Step 3 justification** ("min of finitely many
  affine-on-their-own-domain functions is concave") — logically incomplete/likely false as a
  general principle; do not cite it as-is. The numerically-supported *conclusion*
  (concavity of `g`) may still be true and worth pursuing (opening 1), but needs a different
  proof.
- **Sion's minimax theorem / LP duality framing** in that same file — a red herring for this
  specific game, which is sequential/Stackelberg with full information, not a simultaneous
  zero-sum matrix game; no order-of-quantifiers swap is needed or applicable.
- **Strategy-stealing from the proved upper bound to the lower bound** — independently
  re-confirmed as a non-sequitur by the parallel lower-bound explorer this round (the upper
  bound is a sufficiency statement over ALL LB openings; it says nothing about the specific
  dyadic opening's resistance). Do not retry.
- **Probabilistic-method / generating-function reframings** — scanned, no applicable
  mechanism found in the corpus or in the problem's own structure; not worth a dedicated
  round.
- **Continued-fraction "slick" proof of the closed form** — the recursion shape is
  suggestive but I found no proof technique (in KB or corpus) that uses continued-fraction
  structure to *establish* rather than *describe* such a recursion's closed form; treat as
  unpromising unless someone finds a concrete mechanism, not as a next-round target.

### Small-case / intuition notes (conjecture, numerically checked, not proof)
- **n=2: global concavity of `g` over the whole sorted-simplex domain is well-supported
  numerically** (0 violations across ~34 varied test pairs spanning both Cases and their
  shared boundary) — a genuinely new empirical finding this round, not previously checked
  by either sibling approach (both only checked *local* concavity/local casework, never
  tested concavity claims that cross their own Case (i)/(ii) boundary). If provable, this
  would let the upper-bound proof at `n=2` collapse from four hand-solved sign regimes to
  one convexity lemma plus the already-certified local certificate.
- **n=3: inconclusive** — a small, seed-reproducible apparent concavity violation was found,
  but is most plausibly a numerical search-quality artifact (larger, under-sampled strategy
  space) rather than a genuine failure; **do not conclude concavity fails at n≥3** without a
  more careful (non-random) check first.
- Both findings above are new numerical exploration this round, not merely a repeat of prior
  rounds' spot-checks.
