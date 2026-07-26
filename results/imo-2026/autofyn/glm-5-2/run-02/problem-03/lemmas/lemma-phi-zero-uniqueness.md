# Lemma: Φ=0 uniqueness (halving-defect fixed point)

**Status:** CERTIFIED (round 5, proof-reviewer). Proved in `approaches/dyadic-halving-induction.md` §1. Reviewer re-derived the telescoping identity for `n = 1, …, 5`.

## Statement

For a sorted-desc config `P = (p_1, …, p_{n+1})` with `Σ p_i = 1`, define the **halving defect**

```
Φ(P) = Σ_{i=1}^{n} |p_i − 2 p_{i+1}|.
```

Then `Φ(P) = 0` iff `P` is the order-`n` dyadic `(1, 2, 4, …, 2^n)/D(n)`, `D(n) = 2^{n+1} − 1`.

## Proof

`Φ(P) = 0` means `p_i = 2 p_{i+1}` for every `i = 1, …, n`. Telescoping: `p_1 = 2 p_2 = 4 p_3 = … = 2^n p_{n+1}`, i.e. `p_i = 2^{n+1−i} p_{n+1}`. The sum constraint `Σ_{i=1}^{n+1} p_i = 1` gives `p_{n+1} · (1 + 2 + … + 2^n) = p_{n+1} · D(n) = 1`, hence `p_{n+1} = 1/D(n)` and `p_i = 2^{n+1−i}/D(n)`. This is exactly the order-`n` dyadic. Conversely, the dyadic has `p_i = 2 p_{i+1}` at every level (`2^{n+1−i} = 2 · 2^{n−i}`), so `Φ = 0`. ∎

## Reusability

The fixed-point uniqueness of the halving operator: the dyadic is the unique config where every halving step is exact. The 2-adic structure (`D(n+1) = 2 D(n) + 1`, the irreducible `+1`) is the signature. Useful as a structural-identity input for any approach framing the upper bound via halving-defect / 2-adic invariants.

## Scope

- All `n ≥ 1`; a structural-identity lemma (no strategy, just the fixed-point characterization).
- Does NOT by itself prove `cap ≤ α(n)` for non-dyadic configs (the strict-decrease conjecture `Φ > 0 ⟹ cap < α(n)` is FALSE — see `lemma-ridge-falsification.md`; the dyadic is NOT an isolated strict global max of `cap`).
- Records the structural fact, not a regime-N closure.
