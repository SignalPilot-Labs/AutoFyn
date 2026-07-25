## imo-2026-03

Lens: fresh top-level framing for the upper-bound Existence Theorem (V(p) <= c(n)
on the balanced region), explicitly avoiding the vertex/tie/polytope family and
the mechanisms already killed (majorization, structured randomization,
region-boundary path monotonicity, 4 bounded tie-topologies, global
convexity/concavity LP-duality certificates).

### Opening 1 — Reciprocal/potential functional-equation induction on n (PRIMARY)

**The observation (verified exactly, trivial algebra — see check below).**
$c(n)=2^n/(2^{n+1}-1)$ satisfies the clean recursion
$$\frac1{c(n)} \;=\; \frac1{c(n-1)} \;+\; \frac1{2^n},\qquad c(0)=1.$$
Equivalently $c(n)=1/\bigl(2-2^{-n}\bigr)$, and $c(n)$ solves the
self-consistency equation $c(n) = \tfrac12 + c(n)\cdot 2^{-(n+1)}$ — i.e.
$c(n)$ is a **fixed point of a contraction that "peels off mass $1/2$, then
folds the remaining $1/2$-scaled recursive value back in with weight
$2^{-(n+1)}$."** This has the shape of resistors combining in series
(reciprocal-additive), or of a self-similar renewal equation, not of a
per-$p$ hyperplane-arrangement vertex condition.

**Why this is a genuinely different top-level framing.** Every live approach
(global-lp-vertex-sufficiency, lp-duality-split-polytope,
self-similar-induction-on-n's stuck $j\ge2$/GT(m) machinery) works by fixing
$n$ and classifying/bounding *over all $p$ at that fixed $n$* (vertex
enumeration, $\Sigma$-shape classification, tie-topology construction). This
opening instead targets an **induction directly on $n$ at the level of the
value function itself**: conjecture and attempt to prove a genuine
**recursive inequality on $V$**, not just on the closed form $c(n)$ — e.g.
something in the shape
$$V_n(p) \;\le\; \Bigl(\tfrac1{V_{n-1}(p')} + 2^{-n}\Bigr)^{-1}$$
for a *canonically reduced* $(p',n-1)$-instance obtained by LB "spending"
one unit of structure (e.g. peeling the top piece's optimal fragment at
scale $1/2$ and rescaling the rest). If provable, downward induction on $n$
closes the Existence Theorem **without ever touching $\Sigma(n,k)$ or the
tie-topology zoo** — the obstruction moves from "classify all vertices of an
exponentially large candidate set" to "prove one reciprocal-recursive
inequality relating consecutive $n$." This is architecturally closer to a
renewal-equation / potential-function argument (cf. resistor networks,
continued fractions) than to LP duality, and it has not been tried by any
approach so far (all of self-similar-induction-on-n's induction is on a
different variable — depth of the *peeling* within a fixed $n$, not on $n$
itself with a reciprocal-additive recursion).

**Cheap first test (recommended for next round).** The recursion is exactly
true for $c(n)=\sup_pV(p)$ (verified below), so the real open question is
whether $V(p)$ itself — not just its supremum — obeys a matching *pointwise*
inequality along some natural reduction map $p\mapsto p'$. Concretely: take
one of the already-catalogued "hard" $n=3$ balanced-region points from
`global-lp-vertex-sufficiency.md` (Sections 4.6–4.7, the points with logged
excess $\approx0.0098,0.0013,0.0098$ against every tried construction), and
for a **natural reduction candidate** (e.g. bisect the top piece into two
equal halves, treat one half plus the rest as a rescaled $(n-1)$-piece
instance $p'$) check numerically whether
$1/V(p) \ge 1/V(p') + 2^{-n}$ (the inequality direction needed for an upper
bound via the recursion) holds. If it holds at these hard points but fails
generically elsewhere, that pins down exactly which reduction map is the
right one — a sharp, checkable target before any proof investment.

**My own gut-check (this round, exact arithmetic).** I verified the
closed-form recursion itself exactly with `Fraction` arithmetic for
$n=0,\dots,7$:
```
n=1: 1/c(1)=3/2,  1/c(0)+1/2 = 3/2   (match)
n=2: 1/c(2)=7/4,  1/c(1)+1/4 = 7/4   (match)
n=3: 1/c(3)=15/8, 1/c(2)+1/8 = 15/8  (match)
... holds exactly for all n=0..7
```
This is only a fact about the *supremum* $c(n)$, i.e. **conjecture-level
motivation, not yet evidence about $V(p)$ pointwise** — I did not have
budget this round to build a from-scratch $V(p)$ solver (the existing
approaches' own scripts are the appropriate reference; several already
compute $V(p)$ numerically via exhaustive cut-allocation enumeration, e.g.
`global-lp-vertex-sufficiency.md` Sections 4.6–4.7's own methodology) to
test the pointwise inequality — flagged as the concrete next step, not
claimed as verified.

### Opening 2 — Full two-phase strategy-stealing / exchange argument (bypass the $p$-then-response reduction entirely)

**Why genuinely different.** Every current approach works inside the
*already-reduced* two-level optimization $c(n)=\max_p\min_{\text{response}}
\mathrm{OddSum}$ (the certified Reduction Lemma,
`lemmas/reduction-to-multiset-minimax.md`). This opening proposes instead
to attack the **original alternating-claim game directly**, using a
strategy-stealing/exchange argument across *both* players' moves
simultaneously — i.e. show that for any LB partition $p$ that would beat
$c(n)$, there is an explicit **move-by-move re-pairing** of the actual
claiming sequence (not a static response construction) that provably caps
LB's total, using an interchange argument in the spirit of classical
strategy-stealing proofs (cf. crux corpus `games-and-strategy` entries,
though none matched closely — see below). This sidesteps the entire
"characterize the extremal $p^*$" problem that both remaining approaches
are stuck on, since it never needs to enumerate or bound a candidate set at
all. **Risk, stated honestly:** this is speculative and more of an
architectural suggestion than a validated lead — I did not find a concrete
mechanism this round, only the observation that no approach has tried
working with the *original* (non-reduced) two-phase game since round 1's
initial reduction was proved. Worth a dedicated round if Opening 1 stalls.

**Cheap first test.** Before any proof effort: pick a small hard instance
(e.g. $n=3$, $k=4$ pieces near a catalogued hard point) and hand-trace the
actual claiming game turn-by-turn under LB's candidate partition and XY's
numerically-optimal response, looking for a natural "exchange" (swap which
piece LB claims at step $2$ with which piece XY claims at step $3$, etc.)
that provably doesn't hurt XY — if no such local exchange is visible even
by inspection at one hard instance, this framing is likely a dead end and
should be deprioritized quickly.

### Opening 3 — Layer-cake/threshold-sweep as an interval/matroid extremal problem (considered, NOT recommended as primary)

The layer-cake identity $\mathrm{OddSum}-\mathrm{EvenSum}=\int
\mathbb 1[N(t)\text{ odd}]\,dt$ (certified,
`lemmas/layer-cake-identity-and-coupling-obstruction.md`) is still
available and was flagged in round 4 as a genuinely different
per-piece-additive reformulation. However: (a) `layer-cake-parity-reframing`
was formally retired (round 7) as subsumed by
self-similar-induction-on-n's own AltSum machinery; (b) the round-7
structural diagnostic (Rule 68 in run_state.md) found that **every**
per-cut/per-piece-additive mechanism tried so far bottlenecks on the same
wall; (c) `discharging-neighbor-transfer` (round 15, a direct attempt at a
threshold/weight-based additive argument) was found to reduce to the exact
same stuck GT(m) recursion. A fresh attempt to reinterpret the threshold
sweep as an **interval scheduling / matroid-intersection** problem (rather
than a per-cut charge) is *conceivably* different in kind (global rank
structure via a totally-unimodular constraint matrix, not a local charge),
but I could not find a concrete formulation this round, and the strong
prior (three independent approaches hitting the identical wall) makes this
a low-priority lead unless someone finds a genuinely non-additive way to
use the identity. **Recommendation: do not pursue as a top-level opening
next round unless Openings 1–2 both stall.**

### Candidate technique(s)
- Opening 1: renewal-equation / reciprocal-additive potential-function
  induction on $n$ (new to this project; related in spirit to resistor-network
  series-combination and continued-fraction recursions, not cited from the
  knowledge base directly — no current KB entry matches this exact
  technique, see below).
- Opening 2: strategy-stealing/interchange argument on the full two-phase
  game (classical game-theory technique, not yet tried here since round 1's
  reduction).

### Cheap-kill candidates
- Opening 1: test the pointwise reciprocal-recursion inequality
  $1/V(p)\ge 1/V(p')+2^{-n}$ at the already-catalogued $n=3,4$ hard points
  (from `global-lp-vertex-sufficiency.md` Sections 4.6–4.7) under a few
  natural reduction maps $p\mapsto p'$ (bisect top piece; peel and rescale
  tail) — cheap, no proof investment, decides viability in one round.
- Opening 2: hand-trace one hard instance's actual claiming sequence,
  looking for a visible local exchange — if none is apparent by inspection,
  drop quickly.
- Opening 3: none obvious beyond what's already been tried and failed
  (deprioritized).

### Knowledge-base entries to use
- `knowledge_base.md` was skimmed; no entry names a reciprocal-recursion /
  renewal-equation technique or a strategy-stealing exchange argument
  specific to alternating-claim games — both openings would be genuinely
  new tool imports, not reuses of a named KB entry. The certified
  project-internal lemmas most relevant if Opening 1 is pursued:
  `lemmas/reduction-to-multiset-minimax.md` (the two-level structure being
  bypassed/refactored), `lemmas/twin-anchor-floor-theorem.md` and
  `lemmas/top-duplication-witness-theorem.md` (exact known values of $V$ at
  specific points, useful as base cases / sanity checks for any recursive
  inequality).

### Analogous past problems (cruxes)
Searched `past_crux_moves_database.json` filtered to `domain=combinatorics`,
`subtopic` in {`games-and-strategy`, `extremal-principle`,
`generating-functions`, `telescoping-and-summation`}, keyword-matched against
alternating-claim/split/reciprocal/geometric-series themes (91 candidate
hits out of 223 in those subtopics). **None are genuinely analogous** to
either fresh opening:
- `aimo-0117` (dyadic/geometric power-of-two sequence where the top value
  exceeds the sum of the rest) is structurally close to the *already-known*
  extremal geometric partition (LB's construction), not to a new upper-bound
  mechanism — already fully absorbed into this project's existing
  machinery (the Doubling Lemma family), not a fresh lead.
- `aimo-0122` ("reciprocal-sum equation at a maximum-degree vertex forces
  equality") uses reciprocal sums but in an unrelated graph-degree
  equality-case context — not a genuine analogue to the $1/c(n)$ recursion
  found here.
- No crux entry in the corpus implements a renewal/resistor-style
  reciprocal-additive induction on a game value, and no entry implements a
  strategy-stealing exchange argument on a *claim-from-a-continuum* game
  (all `games-and-strategy` cruxes found were discrete board/pairing games,
  consistent with round 6's prior finding that this subtopic doesn't match
  the continuous split-then-claim structure here). **Report: no strong
  crux match for either fresh opening — both are genuine reconnaissance,
  not adaptations.**

### Prior progress
See `current.md`: lower bound essentially closed except a width-1 window in
GT(m) and a $k=2$ Level-Absorption base case; upper bound's sole remaining
obstruction is the Existence Theorem's $\Sigma$-shape residual (branch-
comparison-boundary and within-branch-tie candidates), now confirmed dead
for 4 bounded tie-topology families and for global convexity/concavity
certificates (round 15).

### Dead ends (do not retry)
Per dispatch: majorization/Schur monotonicity (round 6), structured
randomization/expectation (round 12, Expectation Obstruction Theorem),
region-boundary path monotonicity (round 12/13, all 4 exchange-mechanism
variants), 4 bounded tie-topology families — cyclic, linear-chain,
descending-chain, star/tree (rounds 13–15), global convexity/concavity
LP-duality certificates (round 9 and round 15's 2-fragment counterexample).
Additionally (my own finding this round): layer-cake/threshold-additive
reframings are a *soft* dead end — not formally refuted as a class, but
three independent attempts (layer-cake-parity-reframing, retired round 7;
self-similar-induction's own AltSum machinery; discharging-neighbor-transfer,
round 15) all converge on the same GT(m) obstruction, so a fourth
threshold-additive attempt is low-value unless it finds a non-additive
(matroid/interval-scheduling) formulation, which I could not construct this
round.

### Small-case / intuition notes
The reciprocal recursion $1/c(n)=1/c(n-1)+2^{-n}$ is an **exact, proved**
algebraic fact about the closed form (trivial from the formula, verified
with exact `Fraction` arithmetic $n=0,\dots,7$ this round) — not a
conjecture about $V(p)$ itself. Whether $V(p)$ obeys a matching *pointwise*
inequality under some canonical reduction map is entirely open and
untested; this is the concrete, falsifiable next step for Opening 1, stated
precisely enough to cheap-kill in one round of numeric testing against the
already-catalogued hard $n=3,4$ points before any proof investment.
