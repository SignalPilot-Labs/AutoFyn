## Status
unsolved

## Approaches tried
(none yet — new approach, round 1)

## Current best
**Setup**: same as `resonance-lattice-invariant.md`.

**Sufficiency**: shared (chain lemma S1 + universal boundary identity S2) — reuse the
certified version once available in `lemmas/`.

**Necessity — THIS APPROACH'S DISTINCT MECHANISM: formal combinatorial-game-theory
Win/Loss (N-position/P-position) labeling of the full state space, adapted from the
crux `aimo-0225`** (games-and-strategy: isosceles counter/triangle game on an n-gon,
where states (a,a,b) are Win/Loss depending on the 2-adic valuation of |a−b|, proved by
backward induction plus a symmetry/strategy-stealing step for non-isosceles states).
This is a genuinely different framing from the residue-lattice and topological-cell
approaches: instead of exhibiting an explicit preserved quantity, it defines Win/Loss
recursively over the (continuum) state space and reasons about the STRUCTURE of the
Win region via closure/openness, matching how the θ=60° depth-4 branching example
(found by the game-strategy explorer) genuinely requires multi-step game-tree lookahead,
not a one-shot invariant.

**Formal setup.** Let S = {(X,Y,Z) ∈ (0,180)^3 : X+Y+Z=180} (the open 2-simplex of
triangles). Define W ⊆ S ("Mulan wins from here in finitely many moves") by: (X,Y,Z) ∈ W
iff X=θ or Y=θ or Z=θ (already won), OR there exists a legal move (apex + a1 ∈ (0,apex))
such that BOTH resulting children lie in W ∪ {already-won}. L = S \ W ("Shan-Yu survives
forever from here"). The problem reduces to: **is L empty (Mulan always wins, for the
given θ) or nonempty (Shan-Yu has a starting point in L)?**

Key Lemma N1 (closure/topological structure of W): W is defined by an increasing union
W = ∪_{k≥0} W_k where W_0 = {angle=θ} and W_{k+1} = W_k ∪ {states with a move forcing
both children into W_k}. Show each W_k is a **relatively open subset of S** union a
boundary piece equal to a finite union of affine hyperplane-segments (angle = mθ for
integer m), by induction on k: W_0 is a union of 3 hyperplane pieces (closed, measure
zero in S); the "exists a1 forcing both children into W_k" condition, for W_k closed of
this hyperplane-union form, is itself (by direct computation of the forcing equations,
shared with `algebraic-independence-generic.md`'s Lemma N1) again a union of finitely
many hyperplane pieces of the form {some affine combination of X,Y,Z equals an integer
multiple of θ}. This gives an **explicit inductive description of W as a countable union
of hyperplane-segments of the form {angle ≡ 0 mod θ in a suitable derived sense}**,
never containing any 2-dimensional open subset of S, UNLESS at some stage the recursive
hyperplane condition degenerates to "all of S" — the same collapse condition as Lemma S2
/ N1 elsewhere, occurring exactly at θ=180/n.

Key Lemma N2 (Shan-Yu's escape when L ≠ ∅): if the hyperplane-union description of W
from N1 never equals all of S (i.e. θ ≠ 180/n for any n), then S \ W = L is nonempty and
in fact **open and dense** (complement of a countable union of proper affine hyperplane
pieces, each nowhere dense) — so Shan-Yu can start at ANY point of this dense open set
(e.g. take a generic rational-coordinate-free point, or explicitly the point with X0/θ
irrational as in the other approach) and, being in L, by definition of L he has, for
EVERY move Mulan makes, at least one child also in L (else the state would be forced
into W_k for some k, contradicting L = S\W being exactly the non-W states) — giving an
explicit inductive escape rule: "always keep the child that is in L", which is guaranteed
to exist at every step by the very definition of L as a complement of W. This turns the
topological claim into Shan-Yu's actual strategy, closing necessity IF Lemma N1's
hyperplane-collapse classification is fully nailed down.

**Where this differs from the other two necessity approaches**: this one does not try
to name an explicit preserved invariant a priori; instead it treats Win/Loss as the
primary object and derives the invariant (the hyperplane-union structure) as a
CONSEQUENCE of the backward-induction definition — closer to the aimo-0225 template.
The risk/gap is that "W_k is always a finite union of hyperplane pieces, closed under
one more inductive step" must be verified in full generality (all six apex/labelling
cases, at every level k), which is a genuinely inductive symbolic-algebra task, not just
a one-level check as done by the round-1 explorers.

## Full proof
(none yet — Status is unsolved)
