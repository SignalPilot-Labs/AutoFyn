# Lemma: Pair-excess decomposition of the advantage sum (reals, identity)

**Status:** CERTIFIED (round 5, proof-reviewer). Proved in `approaches/cell-complex-l3.md` §D1 (one-line regrouping, real-valued, no integrality).

## Statement

For `2n + 1` real sub-pieces `p_1 ≥ p_2 ≥ … ≥ p_{2n+1}` (sorted desc), the advantage sum

```
A = Σ_{i=1}^{2n+1} (−1)^{i+1} p_i = Σ_{i=1}^{n} (p_{2i−1} − p_{2i}) + p_{2n+1}.
```

Equivalently, defining pair-excesses `e_i := p_{2i−1} − p_{2i} ≥ 0` (by sorted order) and the leftover `ℓ := p_{2n+1} ≥ 0` (the smallest piece):

```
A = Σ_{i=1}^{n} e_i + ℓ,   with `e_i ≥ 0`, `ℓ ≥ 0` (real).
```

## Proof

Regroup the alternating sum: `(p_1 − p_2) + (p_3 − p_4) + … + (p_{2n−1} − p_{2n}) + p_{2n+1}`. ∎ (one-line identity; no integrality.)

## Reusability

Gives the trivial `A ≥ 0` for reals. The base identity on which the grid-parity lower bound (the certified `lemma-grid-parity.md`, specialized to integer-valued arrangement vertices in `lemma-parity-integer-vertices.md`) and the equality-vertex characterization rest. The structural input for any approach decomposing `A` into pair-excess + leftover.

## Scope

- Real-valued identity; holds for ALL `n ≥ 1` and ALL sorted-desc partitions (no integrality, no dyadic assumption).
- Gives only `A ≥ 0`; the target `A ≥ α(n)` needs additional structure (grid-parity on integer vertices, or the vertex-principle enumeration on a fixed `n`).
