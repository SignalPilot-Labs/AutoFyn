# Lemma: Grid equality-case classification (necessary condition, grid-only)

**Status:** CERTIFIED (round 4, proof-reviewer) as a corollary of the certified integer-grid parity theorem (`lemmas/lemma-grid-parity.md`). Proved in `approaches/two-regime-disjunctive.md` §5c.1.

## Statement

At Liu's **level-`n` dyadic config** (pieces `(1, 2, 4, …, 2^n)/D(n)`, `D(n) = 2^{n+1}−1` odd), for any Xiang refinement whose combined marks are at multiples of `1/D(n)` (so every final piece is a positive multiple of `1/D(n)`), with `M` final pieces (scaled integers `q_1 ≥ … ≥ q_M`, `Σ q_i = D(n)`):

`A·D(n) = 1`   (i.e. `A = α(n) = 1/D(n)`)

**iff** one of:

- **(odd `M = 2m+1`)** every pair-excess `e_i := q_{2i−1} − q_{2i} = 0` (so `q_{2i−1} = q_{2i}` for `i = 1, …, m` — all pieces pair up equally) **and** the leftover smallest piece `q_{2m+1} = 1`. (Equivalently: the only odd-multiplicity value is `{1}`.)
- **(even `M = 2m`)** exactly one pair-excess `e_i = 1` (so `q_{2i−1} = q_{2i} + 1` for one `i`, and `q_{2j−1} = q_{2j}` for all `j ≠ i`) and all other pair-excesses `0`. (Equivalently: the odd-multiplicity values are a single consecutive pair `{a, a+1}` for some integer `a ≥ 1`.)

## Proof

Direct from the certified integer-grid parity theorem: `A* := A·D(n) = Σ_{i=1}^{⌊M/2⌋} e_i + [q_M if M odd]`, each `e_i ≥ 0`, `Σ e_i ≡ D(n) ≡ 1 (mod 2)`, hence `A*` is a non-negative odd integer `≥ 1`. Equality `A* = 1`:

- Even `M = 2m`: `A* = Σ e_i`, non-negative odd, `= 1` iff exactly one `e_i = 1` and the rest `0`. The lone `e_i = 1` gives `q_{2i−1} = q_{2i} + 1` (consecutive odd-mult values `{q_{2i}, q_{2i}+1}`); the other `e_j = 0` give `q_{2j−1} = q_{2j}` (even-mult).
- Odd `M = 2m+1`: `A* = Σ e_i + q_{2m+1}`, both non-negative, `q_{2m+1} ≥ 1`. `A* = 1` iff `Σ e_i = 0` (all pairs equal) and `q_{2m+1} = 1` (the single odd-mult value is `1`). ∎

## Honest scope (empirical refinement NOT claimed)

This is a **necessary condition** on equality, derived from parity alone. The corpus-compute census further observed that the *achievable* odd-multiplicity leftovers (with `≤ n` Xiang marks) are exactly `{1}` (mirror family) and `{2^j, 2^j+1}` for `j = 0, …, n−1` (pair-pile family) — i.e. the smaller consecutive value is always a power of two. The parity theorem **does NOT force `a = 2^j`**: it permits any `a ≥ 1`. The "`a = 2^j`" refinement is a statement about which strategies Xiang can realize, witnessed **empirically** by the census (the pair-pile gives `{2, 3}`; the mirror gives `{1}`; the other `{2^j, 2^j+1}` minimizers are observed but not explicitly constructed here). **NOT claimed as proved.**

## Reusability

A clean necessary-condition characterization of the equality case on the grid. Combined with the certified pair-pile (an explicit construction attaining `A = α(n)`), this gives `min_{grid-aligned Xiang} A = α(n)` at the dyadic, with the structural condition above on the equality case. Reusable as the grid-side equality characterization for any approach that needs to identify the dyadic extremal structure.

## Scope

- **Grid-only** (`1/D(n)`-grid-aligned marks); does NOT lift to reals (per the grid-parity lemma's own caveat: a finer odd grid `1/(K·D(n))` gives only the weaker `A ≥ 1/(K·D(n))`; arbitrary real marks can produce sub-`1/D(n)` smallest pieces).
- A **necessary** condition on equality; not sufficient (achievable equality cases are a strategy-existence question).
- The `a = 2^j` refinement is empirical, not certified by this lemma.
