# Lemma: Parity lower bound at integer-valued arrangement vertices

**Status:** CERTIFIED (round 5, proof-reviewer). Proved in `approaches/cell-complex-l3.md` §D2 (specializes the certified `lemma-grid-parity.md` to arrangement vertices of the level-`n` dyadic). Reviewer confirmed the parity computation against the n=3, n=4 vertex enumerations (5 and 12 distinct min multisets respectively, all matching the pair-excess binary form).

## Statement

At an **integer-valued arrangement vertex** of the level-`n` dyadic's hyperplane arrangement (the `2n+1` sub-pieces are nonneg integers summing to `D(n)`, which is ODD), the advantage sum `A` is an **odd nonneg integer**, hence `A ≥ 1` (integer scale), i.e. `A ≥ α(n) = 1/D(n)` real. **Equality `A = 1`** iff the **pair-excess binary form**:

- **(non-degenerate, odd piece-count `2n+1`)** all pair-excesses `e_i = p_{2i−1} − p_{2i} = 0` (so `p_{2i−1} = p_{2i}` for `i = 1, …, n` — `n` equal pairs) AND the leftover `ℓ = p_{2n+1} = 1`; OR
- **(one-excess degenerate, even piece-count `2n`)** exactly one pair-excess `e_j = 1`, all other `e_i = 0`, and `ℓ = 0` (so the odd-multiplicity values are a consecutive pair `{a, a+1}` for some integer `a ≥ 1`, the larger at the odd rank).

Equivalently: at an integer-valued vertex, the values of ODD multiplicity are either `{1}` (non-degenerate) or a consecutive pair `{a, a+1}` (one-excess degenerate).

## Proof

The pieces are nonneg integers summing to `D(n)` (odd). The pair-sum `p_{2i−1} + p_{2i}` is an integer, and `e_i = p_{2i−1} − p_{2i} = (p_{2i−1} + p_{2i}) − 2 p_{2i} ≡ p_{2i−1} + p_{2i} (mod 2)`. Summing: `Σ e_i ≡ Σ (p_{2i−1} + p_{2i}) (mod 2) ≡ Σ p_i ≡ D(n) ≡ 1 (mod 2)`. (For odd piece-count, the leftover `ℓ = p_{2n+1} ≥ 1` is added; the parity of `Σ e_i + ℓ ≡ D(n) ≡ 1` is still odd.) But `A = Σ e_i + ℓ` (pair-excess decomposition, `lemma-pair-excess-decomposition.md`), so `A ≡ 1 (mod 2)`: `A` is odd. As `A ≥ 0` (real identity), `A ≥ 1`. ∎

Equality `A = 1` forces `Σ e_i + ℓ = 1` with nonneg integer `e_i, ℓ`, giving exactly the binary forms above.

## Reusability

Specializes the certified integer-grid parity theorem (`lemma-grid-parity.md`) to arrangement vertices of the level-`n` dyadic. A necessary component of any structural proof of `L(n)` for general `n` (combined with the vertex-principle and a structural theorem that fractional vertices have `A > α(n)·D(n)` — the latter is the open D3 conjecture of `cell-complex-l3`). The equality characterization matches the verified equality loci at `n = 1, 2, 3, 4`.

## Scope

- **Integer-valued arrangement vertices only** (pieces are nonneg integers). Does NOT cover fractional vertices (the D3 conjecture that fractional vertices have `A > 1` is OPEN).
- The `a = 2^j` refinement (the smaller value of the consecutive pair is a power of two) is EMPIRICAL (census), NOT claimed here — the parity theorem allows any `a ≥ 1`.
- Does NOT by itself prove `L(n)` for general `n` over reals; it is one input to the structural route.
