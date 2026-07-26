# Lemma: Ridge reproduction (all n ≥ 2) — pair-pile reproduces on R_e

**Status:** CERTIFIED (round 6, reviewer APPROVE). Proved in `approaches/self-reproducing-invariant.md` §2.1. Reviewer (round 6) independently verified the algebra for n=3,4 and several e ∈ (0,1).

## Statement

For every `n ≥ 2` and `e ∈ (0, 1)`, the **ridge** config

```
R_e^{(n)} = (2^n, 2^{n−1}, …, 4, 2+e, 1−e) / D(n)
```

(the level-`n` dyadic with the bottom two pieces `(2, 1)` perturbed by compensating `(+e, −e)`) satisfies: the pair-pile strategy (certified `lemma-pair-pile-dyadic-cap.md`, applied to the top `n−1` unchanged pieces) yields final advantage `A = α(n)·D(n) = 1` (integer scale), i.e. `A = α(n)` real. Hence `cap(R_e^{(n)}) = α(n)` and `Liu = f(n)`.

The pair-pile invariant **reproduces** on the ridge: the perturbation shifts the active pair-excess from `1` to `1−e` and the bottom pair-excess from `0` to `e`, which **compensate** (`(1−e) + e = 1`).

## Proof

The pair-pile touches pieces of dyadic size `2^k` for `k = 2, …, n` (all but the bottom two). On `R_e^{(n)}`, the top `n−1` pieces are unchanged (dyadic), so the same pair-pile marks apply: bisect each `2^k` (`k ≥ 3`) into `(2^{k−1}, 2^{k−1})` (excess `0`), split the size-`4` piece into `(1, 3)`. The bottom two `(2+e, 1−e)` are untouched.

Final multiset (in `1/D(n)` units): `{2^{n−1}, 2^{n−1}, …, 4, 4, 3, 2+e, 1, 1−e}`. For `e ∈ (0,1)`: `3 > 2+e` (iff `e<1`) and `1 > 1−e` (iff `e>0`), so sorted descending the perturbed pieces sit between `3` and `1`: `…, 3, 2+e, 1, 1−e`.

Pair-excesses: each bisected pair `(2^k, 2^k)` → excess `0`; pair `(3, 2+e)` → excess `1−e`; pair `(1, 1−e)` → excess `e`. Sum: `A = 0 + … + 0 + (1−e) + e = 1`. ∎

## Reusability

Generalizes the certified n=3 ridge-falsification (`lemma-ridge-falsification.md`, which records that the strict-decrease `Φ>0⟹cap<α` is FALSE) to a **positive** all-n result: the pair-pile reproduces on `R_e^{(n)`, giving `cap = α(n)` (non-strict). The ridge is a non-dyadic config in the **equality locus `E_n`** (pair-pile gives exactly `α(n)`), so the dyadic is NOT an isolated point of `E_n`; `E_n` is positive-dimensional. Structural input to any upper-bound approach using the pair-pile / self-reproducing-invariant framing (`self-reproducing-invariant`).

## Scope

- `n ≥ 2`, `e ∈ (0, 1)` only (the ridge family).
- Does NOT prove `cap ≤ α(n)` for ALL non-dyadic configs — only that the pair-pile attains `α(n)` on the ridge (equality, not strict-decrease).
- The far-from-dyadic closure (balanced, extreme-dominant, moderate-dominant) is OPEN (owned by `two-regime-disjunctive` for n=3; open for general n).
