# Partial D/M-completeness — g(A,m) = h(A,m) modulo the "all-cycles" tie-dependency case

**Certified by:** proof-reviewer, round 4, from approach `concavity-minimax-duality`
(round-4 builder, §8). Independently re-derived and checked (via an independent
topological-sort/DAG argument reproducing the same "all-cycles" obstruction, and via exact
`Fraction` reachability/BFS spot checks) by the reviewer.

**Depends on:** the already-certified `lemmas/dm-operation-reformulation.md` (Lemma D/M,
in particular its single-operation identities for `D(x)` and `M(x,y)`, proved for *any*
current piece regardless of its depth in a larger cut-forest) and `lemmas/vertex-lemma.md`
(the single-cut piecewise-linearity Lemma and its joint-optimum Corollary).

## Statement

Fix a starting multiset `A` and a cut budget `m`. Let `g(A,m)` be the true minimum of `e`
over Xiang-Yu's entire physical strategy space (≤m cuts), and `h(A,m)` the minimum of `e`
over all legal length-≤m D/M operation sequences starting at `A` (Lemma D/M already gives
`g(A,m) ≤ h(A,m)`, i.e. D/M sequences are *achievable*). Then:

```
g(A,m) = h(A,m),
```

**provided** the global minimizer's "tie-dependency graph" is not a nonempty union of
disjoint directed cycles. This condition holds automatically — and hence `g=h` unconditionally
— whenever, at every stage of peeling the minimizer's genuine cuts one at a time, some
not-yet-peeled cut is a self-bisection or a tie to an untouched original piece of `A` (i.e.
whenever the unresolved cuts are not *all* simultaneously "cross-ties" — cuts that tie
exclusively to values produced by other, still-unresolved cuts — arranged in a closed
dependency cycle).

**Open case, precisely isolated (not closed by this lemma):** the "all-cycles" configuration
itself — every unresolved genuine cut is cross-tie type, and the tie-dependency graph among
them is a nonempty union of directed cycles. No example of this configuration actually arising
for any `A,m` is known to occur, but none is ruled out either.

## Proof sketch (full detail in `concavity-minimax-duality.md` §8)

1. **Existence of a global minimizer** (Step 8.1): the strategy space for ≤m cuts decomposes
   into finitely many combinatorial "shapes" (cut-forest topologies), each a compact polytope
   of cut positions on which `e(final)` is continuous (piecewise-linear, by the Vertex Lemma).
   A continuous function on a compact set attains its minimum; taking the min over finitely
   many shapes, `g(A,m)` is attained at a concrete configuration `FINAL`.
2. **Vertex classification** (Step 8.2): applying the Vertex Lemma's Corollary at `FINAL`,
   every genuine cut of `FINAL`'s forest is, when every other cut is held fixed, a
   self-bisection, a tie (to a background piece or another cut's output), or degenerate
   (droppable, reducing to a strictly-fewer-genuine-cuts configuration with the same `e`).
3. **Peeling / topological argument** (Steps 8.3–8.4): define a dependency graph on the
   genuine cuts (edge `c→c'` when `c` ties to a value produced by `c'`; self-bisections and
   ties-to-untouched-originals have no outgoing edge). A cut with in-degree 0 (nothing ties to
   its own output) can always be safely "peeled" — undone via Lemma D/M's single-operation
   identity, appending the corresponding `D`/`M` operation to a shorter legal sequence
   constructed by strong induction on the number of genuine cuts. Since every out-degree in
   this graph is `≤1`, and any node with out-degree 0 exists whenever at least one bisection
   or tie-to-original occurs, the *only* way every node can have in-degree `≥1` (blocking all
   peeling) is if the graph is a disjoint union of directed cycles (a standard finite-graph
   fact: total in-degree = total out-degree = (number of out-degree-1 nodes) ≤ (total nodes),
   with equality — forcing *every* node to have in-degree exactly 1 too — only when every node
   has out-degree exactly 1, i.e. no bisections/original-ties exist at all). This matches an
   independent topological-sort argument: a valid temporal ordering of the cuts (as a D/M
   sequence) exists iff the dependency graph is a DAG, and a graph with out-degree ≤1
   everywhere is a DAG iff it has no directed cycle.
4. When peeling succeeds at every stage (no all-cycles obstruction), the induction terminates
   with a witnessed legal D/M sequence realizing `e(FINAL) = g(A,m)`, giving `h(A,m) ≥
   g(A,m)`; combined with the already-certified reverse inequality, `g(A,m)=h(A,m)`.

## Verification

Independently re-derived by the reviewer via a from-scratch topological-sort/DAG argument
(reproducing the identical "union of directed cycles is the only obstruction to an in-degree-0
node" conclusion via a direct in-degree/out-degree counting argument, not merely re-reading
the proof). The claim that no all-cycles configuration is known to arise for the specific
family `A=D_m` is corroborated (not proved) by `dyadic-cascade-induction`'s independent
exhaustive/broad numeric search (`m=2` exhaustive, `m=3,4` broad random) over the *true*
physical strategy space finding no violation of the target `e_m`.

## Reusable by

Any approach that needs the *true* value `g(A,m)` (not merely an achievable upper bound
`h(A,m)`) to equal the D/M-search value — in particular useful for a *lower-bound* argument
phrased in D/M language. **Not currently needed by `dyadic-cascade-induction`**, whose round-4
fix to its own §5.2' Step 0 sidesteps the D/M formalism entirely in favor of direct physical
reasoning (case-split by count of cuts landing inside `a_1`'s descendant fragments) — the two
fixes are independent and complementary, not competing, and do not contradict each other.
Most directly useful to `potential-weighting-upper-bound`'s D/M-policy search (if it is ever
adapted to argue a *lower* bound within the D/M framework) or any future approach that wants
to reason about XY's worst case purely via D/M operations.
