# Scouting report: global potential / bijective framing (round 6)

**Lens assignment:** find a framing that treats the WHOLE final cut multiset
$S$ at once, never decomposed into "ladder's top piece $F$ vs rescaled tail
$G$" — the decomposition every approach (1–5) has independently used and
that has produced the same wall for 4 straight rounds: an induction needing
an *upper* bound on a reduced sub-instance, but only a *lower* bound is
provable.

## Terrain summary

The reduction chain everyone shares (all certified, not in dispute):
$$c(n)=\max_{\text{Liu's config}}\min_{\text{Xiang's response}} \Phi(S),\qquad
\Phi(S)=\tfrac12(\mathrm{Total}(S)+A(S)),\qquad
A(S)=\int_0^\infty \mathbb 1[N_S(x)\text{ odd}]\,dx.$$
($A(S)$ = alternating sum in descending order; `integral-alternating-sum-formula`,
`odd-run-reduction-lemma`, `vertex-minimum-theorem`.)

**Key realization: $A(S)$ is already a global, non-decomposed potential.**
It is a single integral over the whole multiset with no reference to "which
generation" a piece came from. The top/tail split that every approach hits
is *not* forced by this formula — it is introduced later, when people fix
Liu's ladder and write $S=F\cup G$ ($F$=Liu's own ladder pieces or a
partial ladder, $G$=Xiang's refinement) so they can compute $N_S=N_F+N_G$
piecewise. That splitting choice, not the potential itself, is the source
of the plateau. So a "global potential" in the literal sense (idea 1) has
already been used maximally — `dyadic-band-occupancy` (round 5) pushed the
coarsest version of this (band/mass counts only) and *proved it insufficient*
(`band-invariance-conjecture-refuted-dead-end`): fine within-band position
matters, so no purely-count-based global potential can close the gap without
smuggling back in positional (i.e. effectively top/tail-shaped) information.
**Verdict on idea 1: not fresh — already tried and shown too coarse.** Any
revival needs to encode position, at which point it risks re-deriving the
same split.

## Most promising fresh lead: LP duality / certificate (idea 3)

`vertex-minimum-theorem` + `odd-run-reduction-lemma` already reduce the
*entire* problem (for fixed $n$ and fixed Liu config) to: a polytope $P$
(Xiang's legal responses, cut-budget $\le n$, ordering constraints) plus a
piecewise-linear objective $\Phi$, whose min over $P$ is attained at a
vertex. Every approach since round 3 has stayed on the **primal** side:
enumerate/characterize vertices, or induct by peeling off the top piece.
Nobody has tried the **dual** side: exhibit an explicit nonnegative
combination of $P$'s defining constraints (piece orderings $L_i\ge L_{i+1}\ge0$,
$\sum L_i=1$, and the finitely many "which points got marked" incidence
constraints) that *directly* certifies $\Phi(S)\ge a_n\cdot\mathrm{Total}(S)$
for every $S\in P$ — a Positivstellensatz/LP-duality certificate, in the
spirit of the `linear-algebra-method`/SOS crux entries (e.g. aimo-0071,
aimo-0195, aimo-0284: rewrite a bound as an explicit nonnegative combination
of simple inequalities rather than casework). This would sidestep the
induction entirely: no "upper bound on a smaller instance" is ever needed,
because a dual certificate proves the global inequality in one shot, over
the whole multiset, for every $n$ at once if the certificate's shape is
found parametrically (e.g. coefficients following the same $2^{n+1-i}/(2^{n+1}-1)$
ladder weights). This is a **genuinely different framing** from every live
approach and directly targets why the induction is stuck (it needs
something induction structurally cannot supply).

Risk: nobody has constructed even a single candidate certificate yet, so
this is unstarted territory, not a partial result — a full round would be
needed just to find the certificate's shape for $n=2$ (already fully known
both directions) as a template, then conjecture the general-$n$ form.

## Idea 2: bijective/exchange argument, ratio $2^n:(2^n-1)$ directly

Numeric grounding: ladder denominator is $2^{n+1}-1=2\cdot 2^n-1$, and
$c(n)=2^n/(2^{n+1}-1)$, Xiang's share $=(2^n-1)/(2^{n+1}-1)$ — i.e. Liu's
share is exactly one more "unit" out of $2\cdot(\text{Xiang's units})+1$.
This $2^{n+1}-1$ (a Mersenne-type count) is suggestive of a binary/dyadic
encoding, matching crux techniques like `aimo-0596` (F_2^k
involution/XOR-pairing take-turns argument) and `aimo-0915` ("pair elements
into complementary constant-sum pairs so any equal split balances the
total" — combinatorics/bijections-and-encoding). A candidate shape: find an
explicit injection from Xiang's claimed pieces (or their mass) into a
canonical set of "shadow" fragments of Liu's claimed pieces, pairing each
Xiang fragment with a Liu fragment of exactly twice its size (mirroring the
ladder's own doubling ratio $p_i=2p_{i+1}$), so that summing the pairing
directly forces $\Phi\ge 2\cdot(\mathrm{Total}-\Phi)$-ish inequalities minus
a bounded leftover — reproducing $2^n:(2^n-1)$ as a telescoping/geometric
series rather than an induction on sub-instances.

**Caveat:** this is *unexplored* but unlike idea 3 it isn't obviously
targeting the specific failure mode (upper-bound-needed-but-not-available);
`exchange-argument-extremal-response` already tried an exchange/swap
argument but at the LP-vertex level (swapping which vertex is the
minimizer), not a piece-to-piece bijection on the final multiset — so a
literal bijective map on pieces is still a genuinely different avenue from
that approach, just riskier/less targeted than idea 3. Worth a 1-round
scouting build to see if the doubling structure of the ladder ($p_i=2p_{i+1}$,
`ladder-self-similarity-constant`) admits an explicit pairing; if it doesn't
cleanly emerge for $n=2$ (fully solved, so testable in an afternoon) it
should be dropped fast.

## Idea 4: crux corpus leads

Searched `combinatorics` × `games-and-strategy`, `bijections-and-encoding`,
`linear-algebra-method`, `inequalities-SOS-and-convexity` subtopics (per
`crux_moves_documentation.md`). No exact analog to a stick-cutting
alternating-claim game exists in the corpus, but concrete transplantable
moves:
- **aimo-0596** (misère take-turns, XOR/F_2 pairing): "seed the responder
  with one full pair up front so whatever the final invariant lands on is
  already held" — a template for a *global* pairing invariant maintained
  across the whole claiming phase, not a per-generation split.
- **aimo-0915** (bijections): "pair elements into complementary
  constant-sum pairs so any equal-count split automatically balances the
  total" — closest structural template for idea 2's pairing.
- **aimo-0560** (games-and-strategy, "surrogate adversary" — replace the
  real adversary with a strictly stronger one whose reply is pointwise at
  least as damaging): already effectively used in spirit by the
  rescaled-ladder/cascading-halving results, but could be reapplied at the
  *whole-multiset* level (one canonical global surrogate for Xiang Yu,
  proved dominant over all of $P$ at once via a single argument) instead of
  per-generation, which is the top/tail-free version of achievability work
  already done.
- **aimo-0071 / aimo-0195 / aimo-0284** (SOS/AM-GM/Cauchy-Schwarz):
  templates for turning "the true minimum" into "an explicit nonnegative
  decomposition" — relevant machinery for idea 3's certificate search, not
  a direct analog.

## Recommendation

Rank for round 6: **(3) LP-duality/certificate first** (most directly
targets the diagnosed failure mode — the induction's missing upper bound —
and reuses already-certified machinery `vertex-minimum-theorem` +
`odd-run-reduction-lemma` as its starting point, so it is a genuinely new
framing built on existing certified facts, not from scratch). **(2)
Bijective pairing on final pieces second** as a lower-cost, higher-risk
parallel scout (quick to falsify on the fully-solved $n=2$ case). Idea (1),
literal global mass/count potential, should NOT be re-opened — it is
already shown too coarse by `dyadic-band-occupancy`'s certified negative
result this round.
