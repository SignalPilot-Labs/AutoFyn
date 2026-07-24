# Lens: literature + alternative technique (round 3, imo-2026-03)

## Read

`current.md`, all four `approaches/*.md`, all lemma files (titles only), and
`crux_moves_documentation.md`, then queried `past_crux_moves_database.json`
(2434 cruxes) directly by domain/subtopic and by keyword.

## The shared wall, restated precisely

All three live approaches (`greedy-halving-adversary`,
`self-similar-potential-certificate`, and implicitly
`smoothing-compactness-certificate`'s attempted generalization) reduce the
game, via the certified `claiming-subgame-reduction` + integral/
alternating-sum machinery, to: does Xiang Yu's mixing of fragments of the
ladder's top piece $p_1$ into the tail's refinement (any split $c\ge1$ of his
$n$ cuts) ever push $A(S)$ below $a_n=1/(2^{n+1}-1)$? Both approaches that
tried to prove "no" via **mass accounting** (dropping a cross term
$2\int_0^r u'v\,dx$, or bounding a single-insertion shift by the inserted
mass) found the resulting bound is *provably* too weak — it degrades to
something below 0, useless. This is a genuine, reviewer-verified negative
result, not just fatigue: **any purely mass/measure-based certificate for
this cross-term is a dead end**, confirmed independently twice. The missing
ingredient, as both approaches now agree, is *rank/position*, not mass: which
fragment lands at which parity-rank relative to the tail's pieces.

## Corpus search and what it turns up

Queried `combinatorics/games-and-strategy` (39 cruxes),
`combinatorics/extremal-principle` (166), `combinatorics/processes-and-
algorithms` (48), `number_theory/games-and-strategy` (1 crux), plus keyword
sweeps for `superincreasing`, `geometric`/`dyadic`/`doubling`, `exchange
argument`, `matching`, `strategy-stealing`, `exponential potential`,
`unpaired`/`floating element`/`deficit`.

Three genuinely different-technique candidates stand out, in decreasing order
of how directly they map onto the located obstruction:

### 1. Exchange argument on the extremal (minimizing) final configuration itself — most promising

Several cruxes (`aimo-0119`, `aimo-0425`, `aimo-0146`) solve "minimize/
maximize a weighted or bounded quantity over a constrained combinatorial
space" not by an integral/measure identity but by:
- **fixing an extremal object** (here: a hypothetical Xiang-Yu response that
  achieves the true minimum of $A(S)$ against the ladder, tie-broken however
  needed to make it unique/canonical — this always exists since the
  feasible set is finite-dimensional and compact for fixed $n$),
- proving a **local swap/transfer is never strictly improving** for the
  adversary at that optimum (e.g. `aimo-0119`: "moving a card from the
  heaviest box to the lightest is non-improving at the minimizing partition"
  ⟹ direct algebraic inequality on the box sums; `aimo-0425`: "swapping the
  heaviest item of the top pile against the lightest of the bottom pile
  cannot shrink the spread at the minimizer" ⟹ pins down the spread
  numerically), and
- reading off the *structural* consequence of that non-improvement directly
  (not via mass bookkeeping — via the specific *values* being swapped).

**Why this is a different technique, not a bypass of the same wall**: the
existing three approaches all try to write $A(S)$ as an explicit *formula*
(via Lemma 2's integral, or a decomposition like Lemma 8) and then bound the
formula — this forces the cross term to be estimated abstractly, which is
exactly where they get stuck (the bound is measure-only and blind to rank).
An exchange argument instead never writes down a formula for $A(S)$ at all:
it fixes the hypothetical worst Xiang-Yu response $X^*$ for the ladder,
assumes for contradiction $A(X^*) < a_n$, and derives a contradiction by
exhibiting **one legal single-cut perturbation of $X^*$** (move a cut
point, or re-pair a fragment of $p_1$ against a different tail piece) that
would *strictly lower* $A$ further, or by showing $X^*$ must already have a
specific rigid shape (e.g. "every non-$p_1$ original piece $p_i$ is
paired almost-exactly against a fragment of $p_1$, in a very specific
nesting order dictated by the superincreasing gaps $p_i - \sum_{j>i}p_j$")
— which the ladder's exact superincreasing gaps ($p_i = 2p_{i+1}+\cdots$,
each with a residual of exactly $1/(2^{n+1}-1)$ baked in) can then be shown
to be unrealizable with only $n$ cuts. This targets the *rank* structure
directly (which fragment sits where in sorted order) rather than trying to
bound a rank-blind integral — i.e. it attacks the interleaving obstruction
head-on instead of trying to out-estimate it.

**Concrete new angle not yet tried**: none of the three approaches has fixed
"the worst Xiang-Yu response" as an extremal object and interrogated *its*
local optimality conditions. All three instead work forward from an
arbitrary/generic Xiang-Yu response and try to bound $A$ uniformly. Flip the
direction: **assume a minimizing response exists (finite feasible set argument
+ compactness), derive its first-order/exchange conditions, and show those
conditions force it back onto (or above) the untouched-top-piece case ($c=0$,
already fully closed) or an already-excluded degenerate shape.** This is
structurally how `smoothing-compactness-certificate` succeeded at $n=2$ (six
templates + LP contradiction is *already* a crude, ad hoc version of exactly
this idea — a finite check over configuration classes) — but that approach
enumerates a fixed number of templates by hand, which doesn't scale to
general $n$. A *formal* exchange lemma (swap-two-fragments-strictly-improves
unless already at the ladder's own pairing pattern) is the natural way to
turn the $n=2$ template trick into an $n$-uniform argument, and it is a
technique never invoked by name in any of the three approach files.

### 2. Deferred-commitment / adaptive invariant strategy (from `aimo-0117`) — instructive but likely not directly transferable

`aimo-0117` (a dyadic stick/box game, `combinatorics/games-and-strategy`) is
strikingly close in *flavor*: one player writes only powers of $2$ (an
explicit superincreasing/geometric ladder), and proves a domination result
not via a potential-function computation but via an **invariant maintained
move-by-move**: "the current largest power of two always sits in my
protected box," proved by induction on turns, with the player's *response
rule* depending on whether the opponent just touched the currently-largest
element. The mechanism ("the max always strictly exceeds the sum of
everything smaller, so wherever it sits decides the outcome, and I can always
force it back to my side") is exactly our ladder's superincreasing property,
used as a *live, per-move invariant* rather than a post-hoc sum computation.

**Caveat, honestly reported**: this technique is turn-by-turn reactive
(Jesse sees Tjeerd's move before his own next move), but in imo-2026-03 both
marking phases are single *batch* submissions — Xiang Yu sees all of Liu
Bang's points at once and then commits all $\le n$ of his own points in one
shot; there is no alternation during the marking phase for an adaptive
invariant to react within. So this crux does **not** transfer literally. What
*is* transferable is the underlying idea of proving a dominance property by
an **induction on the number of cuts placed so far, treating Xiang Yu's
batch of $n$ cuts as if placed one at a time in some order chosen for the
proof's convenience**, and showing the "top-of-ladder dominance" invariant
survives each individual cut regardless of where it lands. This reframes the
problem as an induction on *Xiang Yu's cut count* rather than on $n$ (the
game size) or on mass — a genuinely different induction variable from what
any of the three approaches currently use. Concretely: show that after each
of Xiang Yu's $\le n$ cuts (processed in an order fixed by the prover, e.g.
largest-remaining-Liu-Bang-piece-cut first), the *current* partial multiset's
$A$-value stays $\ge a_n$ minus a term that shrinks to $0$ as cuts run out —
an induction on "cuts remaining" rather than trying to handle the whole final
multiset at once. This is worth a dedicated outline attempt.

### 3. Floating/handoff element for the residual (from `aimo-0596`)

`aimo-0596`'s pairing-game solution controls the *identity* of the single
unpaired card via a "floating element" that gets handed off dynamically
during the pairing process (whenever the opponent grabs the current floater,
the responder promotes a fresh floater). This is structurally close to our
own certified `leftover-formula` (Lemma 3: $A(S)$ equals exactly the one
unpaired element in a near-perfect pairing), but `aimo-0596` shows how to
**control which element is forced to be the leftover** via an active
handoff invariant, rather than computing the leftover after the fact. This
suggests reframing the open gap as: "show that no matter how Xiang Yu tries
to pair up the ladder's $n+1$ pieces (plus his own fragments) using his $n$
cuts, the *floating*/unpaired residual is forced (by a handoff argument, not
a counting argument) to be at least the smallest ladder piece
$p_{n+1}=1/(2^{n+1}-1)=a_n$." This is a genuinely different proof route from
the "compute $A(S)$ via an integral and bound the cross term" route the
current approaches use — it stays entirely in the "pairing game" language
already present in Lemma 3, just pushed further (an active/constructive
argument for *why* the leftover can't be smaller, rather than a passive
formula for what it equals once fixed). It is close in spirit to the
"resource deficit of exactly one" observation already recorded in
`greedy-halving-adversary` (Liu Bang's $n+1$ pieces vs Xiang Yu's $n$ cuts is
one cut short of a perfect pairing) but has not been developed into an actual
handoff/matching-game argument — only stated as a headcount fact.

### Weaker/rejected leads
- `aimo-0264`'s exponential-potential-tower technique (base chosen so one
  exponent increment beats a fixed number of duplicate copies) is a genuinely
  different *kind* of potential (multiplicative/exponential rather than
  additive), matching CLAUDE.md's suggestion to consider a non-mass
  potential. But its use case (proving a string-rewriting process
  terminates) doesn't map onto a minimax inequality the way exchange
  arguments do; the "dominance" fact it encodes is already exactly what
  certified Lemma 7 (dominant-element-removal) captures for our problem. Not
  a new angle beyond what's already proven.
- `aimo-0779` (digit game with an involution-pairing response) is the same
  "pairing/leftover" family as `aimo-0596`, weaker instructively (no dynamic
  handoff — its pairing is static per case).
- Strategy-stealing (`aimo-0225`, `aimo-0663`'s shadow-game coupling) doesn't
  obviously apply: our game isn't symmetric between the two players (Liu
  Bang commits first and claims first; there's no obvious "if Xiang Yu had a
  winning response, Liu Bang could reuse it" argument since the two players'
  objectives and move structures aren't dual to each other in the needed
  way).

## Recommendation for next round's outliner

Put up (at least) one new approach slug built on **Lead 1 (exchange argument
on the extremal Xiang-Yu response)**, framed as: fix a minimizer $X^*$ of
$A(\text{final multiset})$ over all legal $\le n$-cut Xiang-Yu responses to
the ladder (exists by finiteness/compactness of the piece-count-bounded
configuration space for fixed $n$), and derive a **local-swap optimality
condition** on $X^*$ — e.g. "no two fragments (one from $p_1$'s split, one
from the tail's refinement) can be exchanged/re-paired to strictly lower
$A$" — then show this condition forces $X^*$'s structure to coincide with
(or be dominated by) the already-solved $c=0$ untouched-top-piece case, using
the ladder's *exact* superincreasing gaps ($p_i - \sum_{j>i}p_j =
1/(2^{n+1}-1)$ at every level, not just the top) as the quantity the swap
argument pins down. This is far from the current field: it never computes
$A(S)$ via an integral/alternating-sum formula at all, so it cannot inherit
the same "mass bound is too weak" failure mode that has now killed the
approach twice from two independent directions. **Lead 2** (induction on
Xiang-Yu's cut count, processed one at a time, tracking a live "ladder-top
dominance" invariant) is a good second/complementary slug if the outliner
wants a second genuinely different framing — it changes the induction
variable itself (cuts-remaining rather than $n$ or mass), which is the kind
of far-apart diversification CLAUDE.md's plateau rule calls for.
