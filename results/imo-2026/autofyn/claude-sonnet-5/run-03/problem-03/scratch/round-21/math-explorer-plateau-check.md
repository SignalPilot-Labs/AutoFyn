# Round 21 — Plateau check + fresh-framing scout, imo-2026-03

## Part 1: Is this a genuine plateau, or two approaches still converging?

**Verdict: not a dead plateau this round.** The two live approaches are working
on *different* sub-problems with distinct, concrete, non-overlapping next
steps — they are not repeatedly hitting the same wall.

- **`self-similar-induction-on-n`** (Elo 1613, stale flag set, 20 rounds
  expanded). Round 20 closed the cross-gap/same-parity configuration the
  round-20 outline-reviewer flagged (General Pairwise Reduction Lemma +
  Finite Reduction Theorem, certified). What remains is now **precisely
  named**: the **General Cardinality-Constrained Half-Sum Lemma** — for
  $k\ge2$, $R$ with $\max(R)\le2^{k-1}$, $|R|\le k+1$,
  $\mathrm{sum}(R)=S\in[2^k,2^k+1)$: $\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge
  (S+2^k)/2$ — verified numerically to $k=6$ but **not proved**; round 19
  diagnosed *why* the natural one-parameter induction on $k$ fails (the
  recursive residual after peeling keeps the *original* cap $2^{k-1}$
  rather than shrinking to $2^{k-2}$, so it's a smaller instance of the
  *same* excess-1 phenomenon — a genuinely two-parameter family is needed).
  This is a sharp, well-defined next step, not vague casting-about.

- **`global-lp-vertex-sufficiency`** (Elo 1597, stale flag set, 13
  rounds). Round 20 fully closed the $n=2$ Existence Theorem (both
  directions) and refuted both natural $n=3$ 2-cut/6-fragment pairings
  (with an exact LP worst-case, not just sampling). The open core is
  named in `current.md`'s "Current best" §2: the **$\Sigma$-shape part of
  the finite candidate set at $n\ge3$** — a combinatorial classification
  problem (no known bound on $|\Sigma(n,k)|$), separate from the "large
  gaps everywhere" case which several named-tool construction families
  (chain-tie, twin-anchor, perfect-tie) have already been shown, in three
  independent lines of evidence, *not* to suffice at $e_0$.

These are genuinely different sub-problems (a *finite-k algebraic
inequality* vs. a *combinatorial classification of tie-patterns at
$n\ge3$*), each narrowed by real, independently-reviewed content every
round for the last several rounds. No orchestrator or reviewer note in
`current.md` (rounds 16–20) flags "field collapsed to one framing" —
that flag has only ever been raised for constructive upper-bound
*families* at $e_0$ (rounds 12/15/16/17/18), which is exactly why
`lp-duality-split-polytope` was later redirected to necessity-conjecture
work and then went dormant (round 18, `dead-end`, light/optional dispatch
only). **No new approach is strictly required this round** on plateau
grounds alone. That said, 20 rounds without a full close, plus one
approach already dormant, means it is worth banking a genuinely distant
framing now rather than waiting for an actual stall.

## Part 2: A genuinely different framing, scouted from the crux corpus

Both live approaches build on the same certified reduction chain: Reduction
Lemma → OddSum/AltSum on a multiset → peel-the-max induction
(`self-similar-induction-on-n`) or LP-vertex/shape enumeration
(`global-lp-vertex-sufficiency`). `lp-duality-split-polytope`'s own past
work (Mass-Constraint / Integer-AltSum-Lower-Bound theorems) is *counting*-flavored
but still worked entirely through explicit named constructions at $e_0$,
never through an actual LP dual certificate. I queried
`past_crux_moves_database.json` (combinatorics domain, subtopics
`games-and-strategy`, `linear-algebra-method`, `probabilistic-method`,
plus keyword search for `majoriz`/`exchange`/`duality`/`potential
function`/`vertex` across all domains) for machinery none of the three
approaches has used. Two candidates stand out as genuinely far from the
current field's machinery:

### (A) Double-counting / fooling-set argument for the general-$k$ GCH bound
`aimo-0129` (a partition/dissection problem, `double-counting` subtopic)
proves a lower bound on partition size not by casework on the partition's
shape, but by **exhibiting a "fooling set"** — a family of cells no two of
which can lie in a single piece of *any* legal partition — turning an
optimization lower bound into a pure counting statement. This is
structurally unlike anything tried on the open GCH($k$) core: all 20
rounds of `self-similar-induction-on-n` attack
$\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ by peeling/induction on the
*value* structure of $R$ (chains, blocks, rank-parity perturbation). A
fooling-set-style argument would instead try to exhibit, for every
candidate integer multiplicity vector, a small family of "witness"
sub-constraints (e.g. specific pairs of Γ-levels plus specific $R$-values)
such that no feasible $R$ can violate all of them simultaneously —
converting the still-open general-$k$ closure from an algebraic
optimization into a combinatorial covering/counting problem. This is
worth a scouting build only if a concrete fooling-set family can be
written down for $k=3,4$ by hand first (cheap-kill before investment).

### (B) Explicit LP-duality certificate (not a construction family) — revives `lp-duality-split-polytope`
Every upper-bound attempt at $e_0$ / $n\ge3$ so far (chain-tie,
twin-anchor, perfect-tie, Multi-Piece Necessity, aimo-0091/aimo-0178
double-counting transplants) has been a *primal* argument: propose an
explicit response construction and show it beats $c(n)$. None of the 20
rounds has formulated the adversary's (XY's) minimization as a literal
linear program and exhibited a **dual-feasible certificate** — a set of
nonnegative multipliers on the piece-sum-equality and ordering
constraints whose weighted combination directly certifies
$V(p)\ge c(n)$ (or $\mathrm{AltSum}\ge1$) without naming any single
witness response. This is the standard LP-duality move (cf. this repo's
own framing name, `lp-duality-split-polytope` — but its 13 rounds of work
were all primal constructions plus a shadow-price *heuristic*, never an
actual dual LP solve with an explicit certificate vector). Concretely:
take the already-certified affine-in-$p$ formula family $\Sigma(n,k)$ from
`global-lp-vertex-sufficiency` §1 (finite candidate shapes, explicit
linear formulas) and, instead of enumerating/bounding each shape, set up
the dual of "minimize OddSum over the polytope of feasible fragment
values" and solve for multipliers symbolically in $k$ using `sympy`/
`scipy.optimize.linprog`'s dual output at several $k$, then guess-and-prove
the general pattern. This is a genuinely different mechanism (a
certificate you verify by weighted summation, not a construction you
verify by direct evaluation) and would attack the same open target as
both `self-similar-induction-on-n`'s general-$k$ closure *and*
`global-lp-vertex-sufficiency`'s $\Sigma$-shape classification from one
level up, potentially subsuming both.

### Ruled out (already tried, don't re-suggest)
- **Majorization / Schur-convexity of OddSum in $R$'s sorted coordinates**
  — `dyadic-potential-invariant` proved this **false in general** (round
  6, certified counterexample, $N\ge3$). Do not revisit as stated.
- **Reciprocal-recursion potential $1/V(p)=1/V(p')+2^{-n}$** —
  `reciprocal-potential-induction-on-n` cleanly refuted (round 16,
  two independently-natural reduction maps both fail exactly, plus a
  structural reason: a whole continuum of AP partitions sits at the
  universal floor $1/2$). Dead as stated.
- **Fixed-formula neighbor-discharging / rank-shift transfer** —
  `discharging-neighbor-transfer` fixed its labeling bug (round 16) but
  is explicitly recommended retired (reduces to the same stuck
  $\mathrm{GT}(m)$ recursion with strictly less machinery).
- **Structured/i.i.d. randomization for the upper bound** —
  `structured-randomization-upper-bound`'s Expectation Obstruction
  Theorem (round 12, certified) shows the core mechanism is structurally
  incapable of closing the upper bound for large $n$ except via a design
  that defeats the point. Dead as stated (a genuinely different
  probabilistic mechanism, not this one, would be needed).
- **aimo-0091/aimo-0178 double-counting transplant to $s\ge n-1$** —
  checked and refuted structurally by `lp-duality-split-polytope` round
  18 (no parity-upgrade analogue; no symmetry group on $e_0$'s AP
  coordinates).

## Recommendation for the orchestrator

Keep both live approaches building on their own named next steps (no
shared-wall plateau to break). If a third slot is wanted this round to
hedge against 20-rounds-no-close, open it on **(B) LP-duality certificate**
rather than (A): it directly reuses the already-certified $\Sigma(n,k)$
shape enumeration from `global-lp-vertex-sufficiency` (so it isn't
starting from zero) while introducing a genuinely new mechanism (a dual
certificate, verified by summation, rather than a primal construction,
verified by evaluation) that is far from both live approaches' machinery
and has literally never been attempted in 20 rounds despite the
approach's name. Mandatory cheap-kill before any proof investment: solve
the LP dual numerically (`scipy.optimize.linprog`) at one small concrete
$(n,k)$ instance already in the corpus (e.g. $e_0$ at $n=6$, where
`lp-duality-split-polytope`'s Chain-Correction Floor Theorem already gives
the exact primal optimum $1/2$) and check the dual objective matches
before writing any general symbolic claim.
