# proof-builder report: structured-randomization-upper-bound (round 12)

## Outcome: unsolved, but a genuine, general negative result established

This was the approach's first build. Per the round's mandate (plateau
break, test a *structured* discrete randomization of an already-certified
deterministic construction family's tie-target choice, not the
already-refuted naive i.i.d. baseline), I ran two concrete structured
schemes and then diagnosed *why* both fail, in a way that generalizes.

**Scheme 1 — random-matching $k$-Anchor-Merge** (randomize which disjoint
pairs of pieces get tied, applying the certified General $k$-Anchor-Merge
Lemma). Tested at the documented $n=6$ "large-gaps-everywhere" survivor
point from `global-lp-vertex-sufficiency.md`. Result: $\mathbb E
[\mathrm{OddSum}]\approx0.55$–$0.58$ for $k=1,2,3$, far above
$c(6)\approx0.5039$ — decisively worse even than the best deterministic
pairing (found by exhaustive search, $\approx0.504$–$0.508$, itself already
insufficient). Random matchings are much worse on average than the best
one; randomizing the pairing throws away exactly the signal.

**Scheme 2 — random-index Generalized Subset-Tie** (Theorem 12, randomize
which piece $i$ gets split and tied against a subset of the rest).
Uncovered a genuine side-finding first: the *minimum* over all $7$ choices
of $i$ (using exact or greedy subset-sum) beats $c(6)$ robustly at this
survivor point and its perturbations ($1376/1376$ perturbed trials) —
initially looked like it might refute the survivor outright via Theorem
12's full any-index freedom (round 8 only tested $i=1$). Verified this is
*not* a rounding artifact of the quoted 4-decimal point (checked via
perturbation), but a broad sweep ($3000$ trials/$n$, $n=2,\dots,9$) shows
this min-over-index family fails broadly (100% at $n=2$), so it's not a
general closure — flagged as a lead for the deterministic approaches, not
pursued further here. Crucially, the **expectation** (uniform average over
$i$) fails even at the one point where the minimum succeeds
($\mathbb E\approx0.507>c(6)$): a couple of mediocre indices outvote the
excellent one.

**Main deliverable: Expectation Obstruction Theorem.** Formalized why both
failures are instances of one general phenomenon. Using the universal fact
$\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$ (elementary telescoping-sum proof,
included) and $c(n)=\tfrac12+\tfrac1{2(2^{n+1}-1)}\to\tfrac12$, any
structured-randomization scheme that puts a *fixed* (n-independent)
positive probability mass $\varepsilon$ on candidates with
$\mathrm{OddSum}\ge\tfrac12+\delta$ (fixed $\delta$) has
$\mathbb E[\mathrm{OddSum}]\ge\tfrac12+\varepsilon\delta$, which exceeds
$c(n)$ once $n$ passes an explicit threshold
($2^{n+1}-1>1/(2\delta\varepsilon)$) — matching both numerical failures
quantitatively. Scope is stated honestly: this doesn't rule out a
distribution that concentrates $1-o(2^{-n})$ mass on already-near-optimal
candidates, but building such a distribution requires solving the same
combinatorial-optimum question the deterministic approaches are already
attacking, defeating the point of randomizing.

## Status
Left `unsolved` (no proof, and the approach's core mechanism is now shown
structurally incapable of working via any "fixed-mediocre-mass" scheme, for
large $n$). This is an honest, precisely-scoped negative result per
CLAUDE.md's norms — not a forced or fake proof. Did **not** self-certify
anything into `lemmas/`; the Expectation Obstruction Theorem and the
min-over-index by-product are left in the approach file for the
proof-reviewer to check and, if it agrees, certify.

## For the orchestrator / next round
- This approach's own direction (expectation over discrete structured
  randomization) is a documented dead end for the reason above; recommend
  not re-dispatching further variants of "randomize a discrete tie choice
  and average" without a genuinely concentrating (not fixed-mass) design.
- The min-over-index Theorem-12-any-$i$ by-product (deterministic, not
  probabilistic) is flagged as a possibly-useful widening for
  `global-lp-vertex-sufficiency` / `universal-halving-adversary` — not
  claimed as a result of this approach, offered as a lead only.
