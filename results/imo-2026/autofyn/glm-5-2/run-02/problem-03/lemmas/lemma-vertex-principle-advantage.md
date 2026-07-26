# Lemma: Vertex-principle for the advantage sum

**Status:** CERTIFIED (round 4, proof-reviewer). Proved in `approaches/cell-complex-l3.md` (Lemmas 1–4); the `n=3` instance verified by exhaustive exact-rational enumeration (`/tmp/round-4/cell_vertex_exhaustive.py`: 65520 triples, 11523 feasible vertices, 0 violations, min `A = 1/15`).

## Statement

For Liu's level-`n` dyadic config (pieces `(1, 2, 4, …, 2^n)/D(n)`, `D(n) = 2^{n+1}−1`), parametrize Xiang's `≤ n` marks by a vector `x ∈ [0,1]^n` (unused marks placed at an endpoint; coincident marks / marks at Liu marks handled by continuous extension). Let

`A(x) = Σ_{i=1}^{M} (−1)^{i+1} p_i`,   `p_1 ≥ … ≥ p_M` the final sub-pieces sorted descending.

Then:

1. **Continuity.** `A` is continuous on all of `[0,1]^n`, including the coincidence / Liu-mark-boundary locus. *(Mechanism: a vanishing sub-piece has length `→ 0`, is the smallest (rank `M`), contributes `(−1)^{M+1}·0 = 0`; removing it decreases `M` by `1` and preserves the signs of all larger sub-pieces — their ranks shift by at most `1` but their relative rank-parity is unchanged because the removed piece was below them.)*

2. **Piecewise-linearity.** Within each open cell of the natural hyperplane arrangement `H` (piece-equality `s_a = s_b` plus piece-zero `s_a = 0` hyperplanes, intersected with the sum-constraints `Σ (sub-pieces of Liu piece j) = L_j`), the sorted order of the `M` sub-pieces is constant, so `A` is an affine function of `x` (each sub-piece length is affine in `x`).

3. **Cell closures are polytopes with arrangement-vertices.** The closure of each cell (intersected with `[0,1]^n`) is a compact polytope whose vertices are arrangement vertices — points where `n` independent hyperplanes of `H` are simultaneously active (on top of the `n+1` sum-constraints, giving full rank).

4. **Vertex-principle.** *If `A ≥ α(n) = 1/D(n)` at every arrangement vertex (using the continuous extension `A(vertex) = alt-sum of the distinct-cut pieces), then `A ≥ α(n)` everywhere on `[0,1]^n`.*

   *Proof.* `A` is continuous (1) and affine on each cell (2). Each cell's closure is a compact polytope with arrangement-vertices (3). A linear (affine) function on a compact polytope attains its minimum at a vertex of the polytope (standard: the sub-level set of an affine function is a face; the minimum, if attained, is attained on a face, inductively on a vertex). So `min_{cl(C)} A = min_{vertices v of cl(C)} A(v) ≥ α(n)`. Since `[0,1]^n = ∪_C cl(C)` (a finite union over all cells), `A ≥ α(n)` everywhere. ∎

## Remark on the flat-facet concern

The minimizer of `A` may be a positive-dimensional flat polytope (a facet interior, not a unique vertex) — verified at `n=3` (the pair-pile / mirror flat region: shifting all Xiang marks by a common offset preserves `A = 1/15`). The vertex-principle still applies: an affine function equal to its cell-minimum on a positive-dimensional face is constant on that face, and the face's vertices are arrangement vertices attaining the same minimum. The flat-facet analysis is therefore needed only to *characterize equality* (which configurations attain `A = α(n)`), NOT to establish the bound. The bound follows from the vertex check alone; tightness is supplied separately (e.g. the certified mirror config).

## Reusability

Reduces the real-valued lower bound `L(n)` (against Liu's level-`n` dyadic, for every real Xiang response `A ≥ α(n)`) to a **finite, exact-rational vertex enumeration** at each fixed `n`. The arrangement grows exponentially in `n` (`~n! · 2^n` sort-pattern regions), so direct enumeration is feasible only for small `n` (verified `n = 3`: 11523 vertices in seconds). The general-`n` lift requires a structural theorem (not supplied by this lemma); the lemma is the per-`n` certificate technique, independent of the `−2T` / Hall decomposition field.

## Scope

- Applies for every fixed `n` (the vertex-principle Lemmas 1–4 are general-`n`).
- The `n = 3` enumeration is a complete proof of `L(3)` over reals (the first real-`n ≥ 3` lower-bound foothold).
- Does NOT close `c(3) = f(3)` (the upper bound / regime-`N` for `n = 3` is owned by `two-regime-disjunctive`, open).
- Does NOT lift to general `n` (the inductive lift is a separate GAP).
