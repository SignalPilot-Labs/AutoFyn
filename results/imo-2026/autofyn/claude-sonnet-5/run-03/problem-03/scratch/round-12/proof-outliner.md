# proof-outliner report — round 12, imo-2026-03

## Field this round

Revised (concrete Round-12 target sections appended, existing content
untouched): `global-lp-vertex-sufficiency`, `self-similar-induction-on-n`,
`greedy-reduction-geometric`, `lp-duality-split-polytope`.

Opened new (plateau-break, per CLAUDE.md's mandatory rule): 
`structured-randomization-upper-bound` — a genuinely different mechanism
(probabilistic/expectation argument) for the upper-bound direction, far
from the vertex/tie/affine-cell lineage. Status `unsolved`; the naive
i.i.d.-uniform form is already refuted (numerically, decisively) and
recorded so nobody re-pays that cost; the file specifies a concrete
structured-randomization design (randomize the discrete tie-target choice
of an already-certified deterministic family, not the continuous
breakpoints) and mandates a numeric sanity-check *before* any proof
attempt, per the plateau-check explorer's explicit instruction.

Untouched (deprioritized, no new lead found): `universal-halving-adversary`,
`dyadic-potential-invariant`, `layer-cake-parity-reframing`.

## Why this shape, and the plateau-break rationale

The plateau-check explorer's finding is confirmed by direct file
inspection: `global-lp-vertex-sufficiency`, `lp-duality-split-polytope`,
and `self-similar-induction-on-n` all now explicitly build on
finite-hyperplane-arrangement / cell-wise-affine / vertex-attainment
machinery descended from the retired `dyadic-potential-invariant`'s Vertex
Pinning Lemma, and `greedy-reduction-geometric`'s remaining Level-Absorption
gap (Theorem N) was proved this round to be symbol-for-symbol identical to
`self-similar-induction-on-n`'s Branch-I.A-restricted window. Per CLAUDE.md:
"if the shared gap is wrong they all die together (the single-gap trap)"
and "put ≥1 approach on the table that attacks the problem from a
genuinely different framing, far from the current field." The plateau-check
explorer tried three candidate fresh framings and found two are dead ends
already paid for (layer-cake/generating-function reframing — proved
non-additive; raw game-tree backward induction — provably equivalent in
content to the certified multiset reduction, no new attack surface) and one
is genuinely untried and not yet refuted in its structured form
(probabilistic/randomized-construction upper bound). That is the basis for
opening `structured-randomization-upper-bound`.

At the same time, the shared-top-only and fragment-tying explorers both
found the vertex/LP-polytope lineage still has concrete, buildable,
non-exhausted next steps — narrowing rather than abandoning it is correct
this round; CLAUDE.md's rule is to add a genuinely different approach to
the table, not to abandon a productive lineage prematurely. Hence: 4
existing approaches get sharpened, concrete targets; 1 new approach opens
a different framing; 2 stay deprioritized per the dispatch instruction.

## Per-approach detail

### `greedy-reduction-geometric` (revise)
**Target:** Theorem N's residual is now known, symbol-for-symbol, to be
the same object as `self-similar-induction-on-n`'s Branch-I.A-restricted
window:
$$c_1\in[2^{\ell-1},2^{\ell-1}+1-\varepsilon),\ \max(C\setminus\{c_1\})<2^{\ell-1},\
\mathrm{sum}(C)=2^\ell+\varepsilon,\ |C|\le\ell+1,\quad \ell=m-1,$$
target $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell$. Recommended next
step: attack via route (a) (self-referential strong induction on $\ell$
mirroring round 8's Branch-II mechanism — see below), coordinating with
the sibling approach so the two files don't duplicate proof effort on what
is now one shared object. Appended as "## Round 12 target" in
`approaches/greedy-reduction-geometric.md`.

### `self-similar-induction-on-n` (revise)
**Target 1 (primary):** the same shared window as above, owner of Theorem
W (left-endpoint exact value), Lemma TPI (gap (b)(i) closed). Concrete next
step, route (a): strong induction on $\ell$, same three-way dichotomy used
for the window applied to the reduced gap-(a) target
($\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$), two branches close
by already-certified analogues, third recurses to a smaller $\ell$ down to
exact base cases $\ell=2,3$. Flagged caution: the recursion's cap
$\max(D)<2^{\ell-1}$ is weaker than the window's own hypothesis
$\max(C)\le2^{\ell-1}-\varepsilon'$, so the induction hypothesis may need
strengthening before it closes — verify in exact `Fraction` arithmetic,
not float optimization (naive numerical search, both gradient- and
box-vertex-based, provably fails to find Theorem W's own value here because
the true extremal structure is an internally tied pair, not a box corner).
Route (b) (exchange-smoothing toward the tied-pair family, via
`aimo-0146`/`aimo-0119`) is a strong alternative/complement if route (a)
stalls.
**Target 2:** import the Rank-Pinning Lemma *technique* (not the literal
lemma — objects differ) into the Middle-Regime Vertex Reduction Theorem to
upgrade the numerically-found $m=3,4,5$ vertex closures to proved-exhaustive,
by enlarging the candidate functional list with pairwise differences among
$B/S$'s own free coordinates and $\Gamma_{m-2}$'s elements. Real, citable,
non-numerical progress even though it doesn't close the middle regime in
general. Appended as "## Round 12 targets" in
`approaches/self-similar-induction-on-n.md`.

### `global-lp-vertex-sufficiency` (revise)
**Primary target: Region-Boundary Monotonicity (Opening 2)** — a reduction-
side mechanism that would close the Existence Theorem *without* ever
classifying $\Sigma(n,k)$. Concrete buildable step: on a fixed cell $C$ of
the $L$-arrangement, $V=f_{\sigma(C)}$ is affine (already certified via
this round's Rank-Pinning Lemma fix), so $V$ is exactly linear along any
line staying in $C$ — trivially monotonic in one of $\pm d$ per cell. The
actual open step: a *consistent* choice of direction sign valid before
knowing which cell $p$ sits in, or a monotonicity-preserving extension of
the certified Lemma 4.2 continuity technique across cell-crossings.
Crux moves `aimo-0146` and `aimo-0287` are adaptable playbooks for the
"which direction is safe" argument (not citable results — reprove from
scratch). **Secondary/deprioritized: fragment-vs-fragment tying (Opening
1)** — structurally not ruled out by the Mass-Constraint Theorem (which
only covers tie-to-whole-untouched-piece constructions), but this round's
numeric stress test at the hard vertex $e_0$ gives a soft negative signal
(minimal clearing $s$ still appears to grow with $n$). Worth at most one
more focused, *proved* (not searched) attempt if the primary target stalls.
Appended as "## Round 12 target" in
`approaches/global-lp-vertex-sufficiency.md`.

### `lp-duality-split-polytope` (revise)
No direct transfer exists from this file's own tooling into the shared
lower-bound window (objects are dual: this file's machinery is explicit
upper-bound constructions at a fixed partition, the window is a
lower-bound universal-response claim). Redirected to
`global-lp-vertex-sufficiency`'s Opening 1 (fragment-vs-fragment tying),
which fits this file's strength (explicit, proved — not searched —
constructions): construct and prove exactly a fragment-vs-fragment tying
response at the already-characterized hard vertex $e_0$, generalizing the
certified Singleton-Interleaving Lemma to chain-tie fragments from
different split pieces. Framed as the one focused attempt the
fragment-tying explorer recommends before treating this construction
family as also insufficient; a further negative result here is legitimate,
citable content (reinforcing that no bounded-family construction suffices,
strengthening the case for `global-lp-vertex-sufficiency`'s reduction-side
route). Appended as "## Round 12 target" in
`approaches/lp-duality-split-polytope.md`.

### `structured-randomization-upper-bound` (new, opened this round)
Plateau-break approach per CLAUDE.md's mandatory rule — see rationale
above. Status `unsolved`, naive i.i.d. form pre-refuted and recorded (do
not retry), a concrete structured-randomization design specified
(randomize the discrete tie-target choice of an already-certified
deterministic family, e.g. Theorem 12's construction, rather than
continuous breakpoints), and a mandatory numeric sanity-check step defined
before any proof attempt is permitted — matching the plateau-check
explorer's explicit instruction not to skip straight to a written proof
on an untested random-construction family. New file:
`approaches/structured-randomization-upper-bound.md`.

### Untouched: `universal-halving-adversary`, `dyadic-potential-invariant`,
`layer-cake-parity-reframing`
No new lead found for any of these this round; left as-is per the
dispatch instruction (do not touch without a genuinely new lead).
`layer-cake-parity-reframing` was explicitly re-checked by the
plateau-check explorer this round and confirmed still a paid-for dead end
(Coupling Obstruction), not worth reopening without a new idea.

## Recommended build set

All four revised approaches have concrete, non-duplicated next targets
ready to build; the new approach's first step is scouting/design +
numeric sanity-check work squarely inside what a proof-builder can do
(design the construction, compute the expectation exactly, compare to
$c(n)$) even though it may not yield a proof this round.

**build set: global-lp-vertex-sufficiency, self-similar-induction-on-n, greedy-reduction-geometric, lp-duality-split-polytope, structured-randomization-upper-bound**
