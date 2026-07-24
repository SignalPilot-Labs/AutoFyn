## Statement

For the $n=4$ ladder with units normalized so $\pi=(\pi_1,\pi_2,\pi_3,\pi_4)
=(8,4,2,1)$ (total $15$), consider any legal response using exactly $3$
cuts distributed among the four pieces as one of the $20$ maximal
compositions identified in `rank-pigeonhole-budget.md` §7.16 (i.e. every
composition $(c_1,c_2,c_3,c_4)$ with $\sum c_i=3$, each piece split into
$c_i+1$ nonnegative fragments summing to $\pi_i$). Let $U$ be the
resulting multiset of $7$ fragments. Then
$$A(U)\ge1,$$
with equality attained (e.g. by the fragmentation $\{4,4,2,2,2,1\}$,
realizable within the budget of every one of the $20$ shapes). Combined
with the certified Index-Chain Identity (`rank-pigeonhole-budget.md`
§7.11: $\mathrm{MinFloor}(\ell)\equiv(\star_{\ell-1})$), this is exactly
$(\star_3)=\mathrm{MinFloor}(4)$, fully closed both directions.

## Proof

See `results/imo-2026-03/approaches/rank-pigeonhole-budget.md`, §7.16–
7.18.5. Summary of the full case coverage (all $20$ maximal shapes):

- $14$ shapes closed directly in round 28 (§7.16) via `odd-run-reduction-
  lemma` and elementary peeling — each has an unconditionally dominant or
  forced value collapsing the multiset quickly.
- Shape $(2,0,1,0)$ closed in round 29 (§7.17) via the certified
  **Pair-Insertion Ordering Lemma** (`lemmas/pair-insertion-ordering-
  lemma.md`).
- Shapes $(2,0,0,1)$, $(1,1,0,1)$, $(1,1,1,0)$ closed in round 30 (§7.18)
  via the Forced-Dominance Fact, `sharp-dominant-removal-identity`
  peeling, and the Pair-Insertion Ordering Lemma.
- Shapes $(1,2,0,0)$ and $(2,1,0,0)$ — the two shapes with **two
  independently-split "conservation groups"** ($\pi_1$'s triple/pair and
  $\pi_2$'s pair/triple respectively, with neither group's top
  unconditionally dominating the other's) — closed in round 31 (§7.18.4)
  by direct citation of the certified `vertex-minimum-theorem` (parts
  2–3): each shape's residual $3$-free-parameter polytope has a
  *complete, exhaustively-justified* finite family of candidate vertices
  (every triple of the shape's legal type-(I) "fragment $=0$" / type-(II)
  "two values tied" hyperplanes — $18$ hyperplanes / $36$ feasible
  vertices for $(2,1,0,0)$, $21$ hyperplanes / $27$ feasible vertices for
  $(1,2,0,0)$), each solved and filtered for feasibility in exact
  rational arithmetic, and each evaluated by direct sorting. All $63$
  vertices (across both shapes) give $A(U)\ge1$, with equality at the
  vertices matching $\{4,4,2,2,2,1\}$. Full vertex tables (all values
  exact rationals, independently hand-verifiable by sorting and
  alternating-summing) are given in §7.18.4.

## Certification note (proof-reviewer, round 31)

**Certified.** Independently re-derived the complete hyperplane families
for both shapes from scratch (from the shapes' own defining constraints,
not copied from the builder's list) and solved all $\binom{18}3=816$
(resp. $\binom{21}3=1330$) triples in exact `Fraction`/`sympy` rational
arithmetic: got an exact match to the file's counts — 18 hyperplanes / 36
feasible vertices for $(2,1,0,0)$, 21 hyperplanes / 27 feasible vertices
for $(1,2,0,0)$ — and the same minimum value $A(U)=1$ in both cases,
matching every tight row in the file's tables. Beyond the vertex-only
re-derivation, ran a 2,000,000-trial continuum (non-vertex-restricted)
random search over the full feasible region of each shape's free
parameters: no interior point beats $A(U)=1$ (observed minima
$\approx1.0000006$ and $\approx1.0000151$, consistent with a true
infimum of exactly $1$ attained only at the boundary vertices) — this
independently corroborates that restricting to the finite vertex family
(licensed by the already-certified `vertex-minimum-theorem`) is itself
valid for these two shapes, not merely that the claimed vertex list is
internally consistent. No gap found in the hyperplane-completeness
argument, the feasibility filtering, or the vertex evaluations.
Certified correct and complete for both shapes.

## Origin

`results/imo-2026-03/approaches/rank-pigeonhole-budget.md`, round 31,
§7.18.4–7.18.5.
