## imo-2026-03

**Scope of this report.** Per dispatch: scouting whole-problem framings that do NOT start
from Lemma G's greedy/order-statistic reduction as the first move — i.e. genuinely upstream
of, or orthogonal to, the entire shared population (`dyadic-cascade-induction`,
`potential-weighting-upper-bound`, `concavity-minimax-duality`), which all currently reduce
via Lemma G, then case-split on `a_1` vs `2a_2`, then induct on XY's cut-count `m`. I did
**not** attempt a proof; each idea below is scouted to the point of a checkable structural
lemma or a numerical sanity check, then stopped.

### Distinct openings

**Opening 1 — LP / Kantorovich (Lipschitz weak-duality) certificate for `e(M)` — most
promising, concrete, and NEW to this population.**

Recall the population already reduces the claiming phase to `e(M) := x_1-x_2+x_3-x_4+…`
(sorted descending) via Lemma G, and the whole remaining difficulty is bounding `e` of a
final piece-length multiset produced by up-to-`m` adversarial cuts. All three live approaches
attack this by *casework on cut count / cut location* (D/M operations, `a_1` vs `2a_2`,
`𝒟_j` dominance classes) — this is the "shared framing" the dispatch wants circumvented.

Independent of Lemma G's *game*-reduction (this is a fact about the **functional `e`
itself**, provable from scratch, no citation needed): for ANY 1-Lipschitz `g:[0,∞)→ℝ` with
`g(0)=0`,
```
e(M) ≥ Σ_{i odd} g(x_i) − Σ_{i even} g(x_i)     (sorted descending x_1≥…≥x_K),
```
with equality at `g = identity`. *Proof (short, self-contained, no OT machinery needed):* pad
`M` with a virtual `0` if `K` odd; pair `(x_1,x_2),(x_3,x_4),…`; for each pair,
`x_{2i-1}-x_{2i} = |x_{2i-1}-x_{2i}| ≥ |g(x_{2i-1})-g(x_{2i})| ≥ g(x_{2i-1})-g(x_{2i})` since
`g` is 1-Lipschitz; sum the pairs (the virtual-`0` pairing needs `g(0)=0`, which is given).
**Verified numerically**, 2000 random-`Fraction` trials, sizes 1–7, several candidate `g`
(identity, clip, shift, negation) — zero violations (`/tmp` scratch, not committed). This is
essentially the 1-D Kantorovich–Rubinstein / optimal-transport duality specialized to the
odd-rank vs. even-rank point measures of the sorted list, but it reduces to three lines of
elementary reasoning — no need to cite OT by name.

**Why this is a genuinely different mechanism, not a rebrand of Fact 2:** the certified
`Fact 2` (dominant extraction, `e(M) ≤ max(M)`) is the *upper*-bound direction and uses only
the single top element. This new lemma is a **family of lower-bound certificates**, one per
choice of `g`, and crucially it converts "prove `e ≥ e_m` for every one of infinitely many
reachable final configurations" (the stuck casework) into "find *one* fixed `g` such that the
`g`-alternating-sum is `≥ e_m` on `D_m` and stays `≥ e_m` under every insertion XY can make" —
i.e. it relocates the required monotonicity-under-splitting property from the raw functional
`e` (already **proved false** in general — the "merging never increases `e`" lemma was
refuted by `dyadic-cascade-induction`/round 3 with a concrete counterexample) to a
*coarsened* functional `e_g`, which is not subject to the same counterexample if `g` is chosen
to be flat/insensitive exactly where the counterexample bites.

**Honest self-check — the easy choice fails, so this is not a free win.** I tested the most
natural candidate, `g(t) = min(t, e_m)` (clip at the target threshold), against thousands of
random split-sequences of `D_m` (`m=2,3,4`, arbitrary split ratios, up to `m` splits): the
`g`-bound degrades to `0`, far below `e_m`, while the true `e` stays at `e_m` — i.e. this
naive clip is too lossy, the same qualitative failure mode already logged for Fact 4's
insertion bound in `lemmas/insertion-and-cascade-facts.md`. **A smarter `g` is needed** — e.g.
one tied to the dyadic *level* structure (piecewise-linear breakpoints near each `2^{-k}`
rather than a single clip), and by strong-duality intuition it would need to be exactly
`identity`-consistent along the (already-known, from round 4's numeric tie search) *family of
tied extremal configurations* while still Lipschitz elsewhere — a well-posed but nontrivial
existence question, **not yet answered**. This is the honest gap of this opening: the
mechanism is new and cheaply provable, but the concrete certificate `g` for `D_m` is open.

**How to use it.** A new approach slot could set as its top-level target: "there exists a
1-Lipschitz `g_m` (`g_m(0)=0`) with `Σ_{odd} g_m(D_m\text{-entry}) − Σ_{even} g_m(\cdot) =
e_m` on the base configuration, and `e_g` is provably non-decreasing under any single
insertion starting from `D_m`'s orbit" — this is a *different* top-level claim from any gap
currently on the table, attacks the exact same stuck sub-problem (multi-cut-inside-`a_1`) from
the dual side instead of the primal casework side.

**Opening 2 — direct recursion on `n` (not on `m`), "one self-similar dominant cut + recurse"
as the whole induction's engine.**

Purely from the conjectured closed form: let `d(n) := 1/c(n) − 1`. Then `d(n) = 1−2^{-n}`
solves the affine recursion `d(n) = (d(n-1)+1)/2`, `d(0)=0`, equivalently
```
c(n) = 2·c(n-1) / (2·c(n-1) + 1),     c(0) = 1.
```
**Verified exactly** (`Fraction` arithmetic) for `n=0..5`: `1, 2/3, 4/7, 8/15, 16/31, 32/63`,
matching `2^n/(2^{n+1}-1)` exactly at every step — this is algebra, not a proof of the game
value, but it is a clean, checkable target the outliner could induct on directly. Note this
same recursion underlies the population's already-certified `e_m = e_{m-1}/(2+e_{m-1})` fact
(`dyadic-cascade-induction` §0) — same recursive *skeleton in the numbers*, but the CURRENT
proofs derive it as a byproduct of the `m`-indexed casework (fixed `n`, inducting on XY's
cut-count within it). **The genuinely different framing**: induct on `n` itself (both
players' budgets simultaneously, one step at a time), with the top-level claim being exactly
`c(n) = 2c(n-1)/(2c(n-1)+1)`, proved via: (LB direction) LB places one cut splitting off a
fragment of a specific optimal proportion `p(n)` and *recursively* runs the level-`(n-1)`
strategy inside it, treating the complementary `(1-p)`-fragment as a single atomic piece that
Lemma G's greedy order guarantees goes to whichever player's turn it is when it becomes the
current max (this needs its own short argument, not automatic); (XY direction) symmetric.
**Where this framing's gap sits, honestly**: it requires proving "WLOG a single self-similar
dominant cut, recursed once, is optimal for BOTH players at every `n`" — this is very likely
*exactly as hard* as the current Case (i)/(ii) split (it is essentially asking why neither
player benefits from spreading cuts across scales in a non-self-similar way, which is the
same underlying phenomenon Case (ii) at general `m` is stuck on). So this is a **medium-
confidence** reframing: it changes the induction variable and could organize the proof far
more cleanly (no `m`-indexed casework machinery, no D/M operation language, no `𝒟_j` classes),
but there is real risk it just relocates the stuck gap under a different name rather than
avoiding it. Worth one approach slot specifically *because* it is structurally disjoint
machinery from the current three (no Lemma D/M, no `𝒟_j`, no `e`-as-primary-object;
works directly with `c(n)` and physical cut proportions), so even a partial result would
diversify the population's proof techniques, which is valuable per the plateau-break rule.

**Opening 3 — binary-tree / Kraft-inequality encoding — flagged as weak/likely-insufficient
on its own, reported for completeness.**

The denominator `2^{n+1}-1 = 1+2+4+\dots+2^n` and the dyadic construction `D_m =
(2^m,\dots,2,1)/(2^{m+1}-1)` are exactly a depth-`m` "caterpillar" prefix-code tree (Kraft
sum). I checked whether the whole problem could be recast as an optimal-prefix-code /
Huffman-style optimization (crux `aimo-0790`, algebra/`sequences-and-recurrences`, uses a
literal "Kraft-style budget constraint" — `Σ 2^{-s_i}≤1` — to convert a subadditive bound into
a many-term weighted bound; read in full, not a strong analogue: it is a sequence-growth
bound, not a two-player game, but the Kraft-budget bookkeeping technique itself might transfer
to bounding how a fixed "budget" of `≤n` cuts can be distributed across dyadic scales).
**Numerical check that kills naive versions of this framing**: absent XY's adversarial layer,
maximizing `e(M)` over *arbitrary* partitions of `[0,1]` into `n+1` positive pieces has
supremum `1` (put almost all mass on one piece), **not** the dyadic value — so a pure
"optimal-prefix-code" argument only captures the extremal *construction* (why `D_m` is a good
choice for LB), never the *adversarial* upper bound (why XY can always cap it there), which is
where all the difficulty lives. This framing therefore looks capable of re-deriving the
**lower-bound construction's optimality among self-similar dyadic strategies** cleanly (a
"why dyadic, not some other geometric ratio" sanity argument) but not of closing either of the
two open gaps on its own. **Recommend not building a full approach around this one** unless
combined with Opening 2 (i.e., as the concrete "self-similar cut is optimal" sub-lemma inside
Opening 2's induction, not as a standalone top-level target).

### Candidate technique(s)
- Opening 1: 1-D Kantorovich–Rubinstein-flavored weak duality (elementary Lipschitz pairing
  argument, no OT citation needed) — a genuinely new lower-bound certificate family for `e(M)`.
- Opening 2: direct induction on `n` via the closed-form recursion
  `c(n)=2c(n-1)/(2c(n-1)+1)`, self-similar single-cut reduction (uses KB "Induction" +
  "Specialize/Generalize" heuristics, no new named theorem).
- Opening 3: Kraft-inequality / prefix-code bookkeeping (weak fit; only as a sub-lemma).

### Cheap-kill candidates
- For Opening 1: before any heavy construction, check whether ANY 1-Lipschitz `g` can beat
  `g=identity` at the *specific* numerically-tied extremal configurations already on record
  (round-3's `m=3` tie example `(a_2,a_3,a_3)=(4/15,2/15,2/15)`, round-4's `m=4,i=3` instance)
  — if strong duality forces `g` to agree with `identity` on ties AND stay Lipschitz-valid
  elsewhere is provably impossible (a quick LP feasibility check, small `m`), this whole
  opening is a fast dead end; if feasible, it is real progress. This is a cheap, decisive
  numerical test to run before investing in a general construction.
- For Opening 2: check whether the "single dominant cut is WLOG optimal for LB" claim is even
  true at `n=3` beyond what's already proven (Case (i) is only established through `m=3`
  currently) — if a numeric optimizer finds any `n=3` LB configuration beating the pure
  self-similar dyadic one, Opening 2 is dead before a proof is attempted.

### Knowledge-base entries to use
- "General Proof Methods: Induction" (KB) — both Opening 1's weak-duality lemma proof and
  Opening 2's `n`-recursion are inductive/telescoping in nature.
- "Problem-Solving Heuristics: Specialize / Generalize / Introduce a substitution" — motivates
  Opening 2's variable change `d(n)=1/c(n)-1`.
- "Piecewise-concavity smoothing" (KB, Algebra section) — the general *shape* of argument
  (concave-on-pieces ⟹ extremum at breakpoints) is the closest KB analogue to the
  "smoothing/exchange to a canonical dyadic shape" flavor Opening 3 gestures at, though KB's
  entry is stated for trig-sum minimization, not this problem; would need real adaptation, not
  direct reuse.
- No KB entry for LP/optimal-transport duality by name — Opening 1's lemma is elementary
  enough not to need one; flagged here in case a future round wants to add "1-D Lipschitz
  weak-duality for alternating sorted sums" as a new reusable KB technique if it proves out.

### Analogous past problems (cruxes)
- **None are genuinely analogous.** Searched `crux_moves_documentation.md`'s subtopic list;
  filtered `combinatorics`/`games-and-strategy` (39 cruxes) and grepped problem statements for
  stick/cake/interval/segment/length-division games — the closest hits (`aimo-0019`
  covering-game frontier-painting, `aimo-0854` pairing-cell completion, `aimo-0225`
  strategy-stealing) are all **discrete combinatorial pairing/blocking games**, not continuous
  value-optimization games over interval lengths, and none involve a two-stage
  "mark points, then claim pieces by value" structure. `aimo-0790` (algebra,
  sequences-and-recurrences) uses a literal Kraft-style weight-budget technique but on an
  unrelated subadditive-sequence-growth problem, not a game — flagged above only as a weak
  technique-transfer candidate for Opening 3, not a real analogue. **Verdict: force no match**
  — do not treat any corpus problem as a template for this problem's proof.

### Prior progress
See `results/imo-2026-03/current.md` for the full, correctly-scoped summary (not repeated
here in full since this report targets NEW framings only): `n=1` fully solved; `n=2` upper
bound fully proved; `n=3` Case (i) proved; lower bound proved for every `m` against `D_m` when
XY makes 0 or exactly 1 cut inside `a_1` (Branch A, Case B1/B2); the two stuck gaps are
(1) upper-bound Case (ii) at general `m≥3`, (2) lower-bound `≥2`-cuts-inside-`a_1`. Certified
lemmas: Lemma G, Lemma P, Lemma D/M, Facts 1–5, Vertex Lemma, partial D/M-completeness — see
`lemmas/`. None of these is contradicted or superseded by anything in this report; Opening 1's
new lemma is additive (a new tool), not a replacement.

### Dead ends (do not retry)
- (already logged, re-verified plausible on inspection, not retried here) "Merging never
  increases `e`" as a fully general monotonicity lemma — refuted by concrete counterexample,
  round 3. Opening 1 is explicitly designed to route around this exact refutation (via a
  coarsened `g`, not the raw `e`), not to resurrect it.
- (already logged) Bounded-lookahead "induction loading" for Case (ii) — round 4 showed the
  needed lookahead is the *entire* remaining budget, not any fixed depth. Not revisited here.
- (this report, new negative finding) The naive choice `g(t)=min(t,e_m)` inside Opening 1's
  weak-duality lemma is too lossy (numerically, drops to `0` vs. target `e_m`) — do not retry
  this exact clip; a level-aware piecewise `g` is needed instead, not yet constructed.

### Small-case / intuition notes (all labeled conjecture unless stated proved above)
- The recursion `c(n)=2c(n-1)/(2c(n-1)+1)`, `c(0)=1`, exactly reproduces
  `2^n/(2^{n+1}-1)` for `n=0..5` — an algebraic fact about the conjectured closed form
  (**proved**, trivial induction, not a game-theoretic proof), offered as the seed for
  Opening 2's induction target.
- Opening 1's weak-duality lemma `e(M) ≥ Σ(-1)^{i+1}g(x_i)` for 1-Lipschitz `g`, `g(0)=0` is
  **proved** (elementary pairing argument) and numerically spot-checked (2000 trials, no
  violation) — this is a real, certifiable, reusable fact, not a conjecture, independent of
  whether it ends up closing the stuck gap.
- Absent XY's adversarial layer, `sup e(M)` over free partitions of `[0,1]` into `n+1` parts is
  `1` (not the dyadic value) — **proved** by inspection (concentrate mass on one piece) —
  confirms Opening 3 cannot succeed as a standalone top-level argument; the adversarial
  constraint is where all the real content is.
