# Round 13 — Plateau check + fresh-framing scout (IMO-2026-03)

## 1. PLATEAU CHECK: is GT(m) general-m secretly the same obstruction as the Σ-shape closure?

**Verdict: no — they are structurally different obstructions, not one gap in two languages, but there IS a real surface-level similarity worth naming so the field doesn't fool itself twice.**

### Stating both in a common formal language

- **Gap 1 (lower bound, `self-similar-induction-on-n`).** GT(m): for every
  finite multiset $D=(a_1\ge\cdots\ge a_k)$ of positive reals, $k\le m+1$,
  $\max(D)\le2^m$, $\mathrm{sum}(D)<3\cdot2^{m-1}$:
  $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\min(\mathrm{sum}(D),2^m)$. Proved
  $m=0,1,2,3$ by a case split on $p=\#\{a_i>2^{m-1}\}\in\{0,1,2\}$, with the
  $p=0$ residual further split by $r=\#\{a_i>2^{m-2}\}\in\{0,1,2\}$. The
  file's own "Honest scope: $m\ge4$" section (lines 3143–3167 of
  `approaches/self-similar-induction-on-n.md`) states explicitly: past
  $m=4$ the $r=0$ residual becomes feasible for the first time (Feasibility
  Lemma: infeasible $m\le3$, feasible $m\ge4$) and needs *one further*
  threshold split (against $2^{m-3}$), whose own all-tiny residual becomes
  feasible only from some larger $m$, recursively — "a genuine, self-similar
  infinite-descent structure... not completed this round." This is exactly
  the same phenomenon already named by an earlier math-explorer at line 394
  of the same file, for a *different* sub-target (`Theorem 2'`'s window):
  "an unbounded-depth self-similar recursion."

- **Gap 2 (upper bound, `global-lp-vertex-sufficiency`).** The Existence
  Theorem's candidate vertex set $Q$ splits into $Q_{\text{region}}$ (fully
  closed, round 10–12) and a $\Sigma$-shape part: $(k-1)$-subsets of the
  candidate functional list $L$ that include validity-boundary functionals
  $x_\sigma(p)\ge0$ or branch-comparison functionals $f_\sigma(p)-f_\tau(p)$,
  arising from case splits in how the *response* to a cut-position $p$
  compares across different combinatorial "shapes" $\sigma$ of split-piece
  assignment. No bound on $|\Sigma(n,k)|$ as $n\to\infty$ is known (flagged
  unchanged since round 9); this is explicitly called "a combinatorial
  classification problem" (`approaches/global-lp-vertex-sufficiency.md`
  §4.4, lines 1052–1056).

### Are they the same object?

Both are "a case-split tree whose branch count is not known to stay bounded
as a parameter grows." That surface pattern is genuinely common — but the
underlying objects, growth mechanisms, and difficulty profiles differ in
ways that matter:

- **Different index and different geometry.** Gap 1's parameter is a single
  scalar $m$ (recursion depth along one integer), and its branches are
  determined by comparing a *fixed* multiset $D$'s elements against a
  *single* dyadic threshold ladder $2^{m-1},2^{m-2},2^{m-3},\dots$ — a
  totally ordered, one-dimensional descent. Gap 2's parameter is $n$ (the
  ambient simplex dimension), and its branches are combinatorial shapes
  $\sigma$ — subsets/assignments of $\{1,\dots,n+1\}$ pieces to split
  groups, an object living in a space that grows combinatorially
  (potentially exponentially) with $n$, not linearly.
- **Gap 1's depth is explicitly computable and small.** The Feasibility
  Lemma gives an exact closed-form threshold: the $j$-th level's "all below
  $2^{m-j}$" sub-case becomes feasible exactly when $(m+1)2^{m-j}\ge2^m$,
  i.e. $j\le\log_2(m+1)$. So the case-tree depth needed for a fixed $m$ is
  $O(\log m)$, not unbounded in any troubling sense — this looks like
  exactly the kind of "growing tower of ad hoc case splits" that a **single
  cleverer strong induction** (strengthening the hypothesis to directly
  track the "count-cap slack" the file's own diagnosis names, rather than
  re-deriving feasibility case-by-case) can plausibly collapse into one
  uniform argument. This is a concrete, promising next target — see below.
- **Gap 2's depth has no known formula at all.** There is no analogue of
  the Feasibility Lemma for $\Sigma(n,k)$: nobody has produced a formula
  bounding $|\Sigma(n,k)|$, nor evidence it grows sub-exponentially. It is
  an open enumeration problem over a much richer combinatorial space
  (assignments of pieces to groups), not a numeric threshold check on one
  multiset.
- **No literal reduction found.** Attempting to state Gap 2's obstruction
  in Gap 1's language (a bound on OddSum of a peeled dyadic multiset) does
  not work: Gap 2 is not about peeling a fixed multiset against $\Gamma_m$
  at all — it is about classifying vertices of a polytope over the
  simplex, a different mathematical object (continuous $p\in\mathbb
  R^{n+1}$, not a discrete multiset $D$ with $\max(D)\le2^m$). Conversely,
  Gap 1 has no analogue of "$V(p)\le c(n)$ for all $p$"; it's a bound for
  one instance $D$ per recursive call. No isomorphism or literal reduction
  presents itself in either direction.

**Conclusion:** these are two independent obstructions that happen to share
a *rhetorical* pattern ("self-similar / unbounded case-split," flagged by
name in both files) but not a shared underlying combinatorial object. This
is **not** a single-gap trap in the sense round 12's shared vertex/tie/cell
machinery was (three approaches literally invoking the same lemma chain).
It is closer to "two different approaches independently ran into the
generic difficulty of induction case-explosion" — worth naming so future
rounds don't assume closing one automatically closes the other, but not a
reason to treat the two gaps as one target or to expect one closure to
carry across.

**Actionable point for gap 1:** given the depth is provably $O(\log m)$ and
the recursion is fully explicit/mechanical (dyadic thresholds, closed-form
feasibility), the right next move is very likely a **strengthened induction
hypothesis** — e.g. induct on $m$ with a hypothesis parametrized by both $m$
and the "excess piece-count slack" $j$ the file's own diagnosis names,
proving a single uniform lemma $\mathrm{GT}(m,j)$ by induction on $m+j$ or
similar, rather than continuing to hand-enumerate $p,r,s,\dots$ levels one
at a time. This should be dispatched as a concrete outline target next
round, not treated as equivalent in difficulty to the Σ-shape classification.

## 2. FRESH FRAMING: is a genuinely new top-level route to the whole problem warranted?

### Crux corpus search (combinatorics: games-and-strategy, invariants-and-monovariants, processes-and-algorithms, extremal-principle; also number_theory games-and-strategy)

Searched by keyword across `technique`/`how_used` for: alternating-claim
games, greedy pick-the-largest-remaining mechanics, stick/interval/segment
cutting, dyadic/geometric sequences in adversarial settings, sorted-order
extremal arguments, draft/auction mechanics, odd/even-indexed sums. Found
40 `games-and-strategy` cruxes total (both domains) plus broader hits.
**No crux directly matches this problem's actual mechanism** (two-phase:
first player marks $\le n$ cut points, second player marks $\le n$ more,
then players alternately claim whole pieces greedy-optimally — a
"mark-then-claim" game, not a live alternating-move game on a shared
board). The closest flavor-matches, none load-bearing for this problem's
actual difficulty:
- `aimo-0585` (algebra/sequences-and-recurrences): bounding a **greedy**
  running sum against an adversarially-ordered pool by comparing the
  actual pick to a hypothetical opposite-sign alternative — same genre as
  this problem's already-certified Greedy-Optimality Lemma
  (`lemmas/greedy-optimality-oddsum.md`), not new.
- `aimo-0117` (games-and-strategy): "assign played values as a two-sided
  geometric (dyadic) sequence so the largest strictly exceeds the sum of
  all others" — same dyadic-domination flavor as $\Gamma_m=\{2^m,\dots,1\}$
  already central to every live approach; not a new idea, confirms the
  existing framing is the natural one for this problem shape.
- `aimo-0718` (invariants-and-monovariants): pigeonhole a greedy actor
  against an $r$-blocking adversary via the $r+1$ smallest objects — a
  different flavor (blocking, not cutting) with no clear adaptation.
- No crux in the corpus addresses a two-phase "alternately mark cut points,
  then alternately claim resulting pieces" structure, nor a closed form of
  shape $2^n/(2^{n+1}-1)$ arising from an OddSum-of-sorted-multiset
  identity. This is consistent with the problem being contest-fresh
  (2026) and structurally somewhat novel — the reduction to
  $\max_p\min_{\text{response}}\mathrm{OddSum}$ (already proved, certified
  `lemmas/reduction-to-multiset-minimax.md`) is itself the field's own
  discovery, not adapted from a corpus crux.

### Independent top-level alternatives considered

- **Direct strong induction on $n$ with an explicit potential.** This *is*
  `self-similar-induction-on-n`'s framing already (12 rounds deep, closest
  to done). A genuinely different potential function (e.g. tracking
  $\sum p_i^2$ or an entropy-like $-\sum p_i\log p_i$ instead of OddSum
  directly) was considered: no natural monovariant of this kind interacts
  cleanly with the *sorted-then-alternate-sum* structure of OddSum, which
  is inherently combinatorial (depends on rank order and parity, not on
  smooth functionals of $p$) — a genuine obstruction to any classical
  smoothing/entropy argument, consistent with round 9's retirement of
  concavity as a route (`global-lp-vertex-sufficiency`, "Concavity was
  retired, genuine counterexample").
- **Probabilistic/entropy argument.** Already tried and killed this round
  (`structured-randomization-upper-bound`, Expectation Obstruction
  Theorem) for the upper-bound direction specifically. No analogous attempt
  exists yet for the *lower*-bound direction (can LB's strategy be shown to
  guarantee $c(n)$ via a probabilistic argument over XY's possible
  responses, rather than exact peeling?) — this is a genuinely unexplored
  corner, but the Expectation Obstruction Theorem's mechanism (any
  $n$-independent mediocre-candidate mass fails past a threshold) plausibly
  generalizes to rule this out too, since OddSum's rank-dependence is the
  same obstruction regardless of which side randomizes. Not recommended as
  a fresh open unless someone finds a genuinely concentrating (not
  averaging) probabilistic construction — the theorem's own scope note
  already flags this as the only surviving randomized possibility, and it
  is speculative, not diagnosed as promising.
- **Bijective/generating-function argument for $c(n)=2^n/(2^{n+1}-1)$
  directly.** The denominator $2^{n+1}-1=\sum_{i=0}^n2^i$ and numerator
  $2^n$ strongly suggest LB's geometric partition $\Gamma_n=\{2^n,\dots,
  2,1\}$ (already the field's central object) *is* the generating-function
  witness — $c(n)$ is just $2^n/\mathrm{sum}(\Gamma_n\cup\{1\})$-shaped
  book-keeping already fully derived and certified
  (`lemmas/reduction-to-multiset-minimax.md`,
  `lemmas/top-duplication-witness-theorem.md`). There is no additional
  bijective structure left to mine here — the "generating function" *is*
  the dyadic multiset already in use by all four live approaches. Not a
  fresh opening; would duplicate existing certified work.

### Assessment

No genuinely new top-level framing was found that (a) isn't already what
one of the four live approaches is doing, or (b) isn't already
diagnosed/killed (randomization, concavity). The crux corpus, searched
broadly across games-and-strategy, invariants-and-monovariants, and
processes-and-algorithms in both `combinatorics` and `number_theory`,
contains nothing load-bearing for this problem's specific two-phase
mark-then-claim / sorted-alternate-sum structure that hasn't already been
independently discovered by the existing lines of work.

## Recommendation for round 13's outliner

**Stay focused — do not open a new top-level approach this round.** The
field is close (window closed $\ell=1$–$4$; two well-diagnosed remaining
gaps) and this round's search found no fresh framing worth the diversity
cost, nor evidence the two remaining gaps are secretly one (so closing gap
1 will not silently unlock gap 2 or vice versa — both still need direct
work). Concretely for the build set:
1. Push `self-similar-induction-on-n` to attempt the **strengthened
   induction hypothesis** for GT($m$) at general $m$ (parametrize by the
   "count-cap slack" $j$ the file's own diagnosis names; induct on $m+j$ or
   similar) rather than continuing ad hoc level-by-level case splits — this
   is a concrete, well-scoped target with a real chance of closing gap 1
   in full generality this round or next.
2. Push `global-lp-vertex-sufficiency` to keep narrowing the $\Sigma$-shape
   gap; per its own file, the most promising sub-target is a
   $p$-dependent boundary-endpoint argument or further constraining where
   $p^*$ can land, since bounded-construction search (the $e_0$
   Mass-Constraint route) is now independently ruled out by both this
   approach and `lp-duality-split-polytope`.
3. Optionally, as a *cheap* diversity hedge (not a full new approach): task
   one explorer next round with checking whether Gap 1's now-understood
   $O(\log m)$ case-depth structure suggests an analogous **explicit depth
   bound** technique could be transplanted to bound $|\Sigma(n,k)|$ for Gap
   2 — i.e., not "these are the same gap" but "the technique that will
   likely close gap 1 (a slack-parametrized strengthened induction) might,
   after gap 1 closes, suggest a matching move for gap 2." This is
   speculative and should not gate the round.
