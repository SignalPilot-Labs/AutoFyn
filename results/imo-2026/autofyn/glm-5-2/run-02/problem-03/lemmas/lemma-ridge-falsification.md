# Proposition: Ridge falsification (the strict-decrease conjecture is FALSE)

**Status:** CERTIFIED as a negative result (round 5, proof-reviewer). Proved in `approaches/dyadic-halving-induction.md` §5. Reviewer re-derived the pair-pile cap `A·15 = 1` on the ridge and the halving defect `Φ = 5e` with exact-rational python.

## Statement

The strict-decrease conjecture `Φ(P) > 0 ⟹ cap(P) < α(n)` is **FALSE**. The non-dyadic ridge family

```
R_e = (8, 4, 2 + e, 1 − e) / 15,   e ∈ (0, 1),
```

has `Φ(R_e) = 5e > 0` (level 1 exact: `8 = 2·4`; levels 2, 3 broken: `4 ≠ 2(2 + e)`, `2 + e ≠ 2(1 − e)`), yet the pair-pile strategy (marks at `4/15` and `9/15`, the dyadic-level-1,2 positions) forces `A = α(3) = 1/15` exactly, and **no Xiang strategy achieves `A < 1/15`** (verified by exhaustive 2-mark grid search + sliver candidates + 80,000 random 3-mark trials; best found `A·15 = 1`).

## Proof (the pair-pile on the ridge)

Marks at `4/15` (midpoint of piece 1, which is `8/15` — unchanged from the dyadic) and `9/15` (`1/15` into piece 2, which is `4/15` — also unchanged) split pieces 1, 2 into `(4, 4)` and `(1, 3)` respectively. Pieces 3, 4 are untouched: `(2 + e)/15, (1 − e)/15`. Final multiset (in `1/15` units): `{4, 4, 3, 2 + e, 1, 1 − e}`. For `e ∈ (0, 1)`: `3 > 2 + e` (iff `e < 1`) and `1 > 1 − e` (iff `e > 0`), so sorted desc `4, 4, 3, 2 + e, 1, 1 − e`. The advantage:
```
A · 15 = 4 − 4 + 3 − (2 + e) + 1 − (1 − e) = 0 + (1 − e) + e = 1.
```
So `A = 1/15 = α(3)` for every `e ∈ (0, 1)`. The pair-pile achieves `A = α(3)` on this entire non-dyadic ridge.

**Why the excess is conserved.** The pair-pile's pair-excess structure redistributes: the level-2 pair `(3, 2 + e)` has excess `1 − e` and the level-3 pair `(1, 1 − e)` has excess `e`, summing to `1` regardless of `e`. The perturbation at levels 2 + 3 is "absorbed" by the pair-pile's level-1 exactness (the `(4, 4)` pair is free since level 1 is exact), leaving the residual excesses to sum to the dyadic value `α(3)`.

**No strategy beats `A = 1` (evidence, not proof).** Exhaustive 2-mark search (grid `N = 200` + sliver candidates near all dyadic positions and boundaries, 551 candidates) and 80,000 random 3-mark trials both find the best achievable `A·15 = 1` (the pair-pile value). This is strong evidence that `cap(R_e) = α(3)`, though a proof (a lower bound `A ≥ 1` for every Xiang response on `R_e`) is not supplied — it would require a vertex-principle enumeration for this non-dyadic config.

## Honest consequence

The dyadic is NOT an isolated strict global maximum of `cap`; there is a positive-dimensional ridge of non-dyadic configs (level 1 exact, deeper levels broken) where `cap = α(n)`. The correct qualitative statement is the **non-strict** upper bound `cap ≤ α(n)` (which is exactly `U(n)` and is consistent with the ridge: `cap = α(n) ≤ α(n)` ✓). The Φ-framing does NOT prove the strict-decrease half of regime-N.

## Reusability (as a do-not-retry)

Records the falsification so no approach retries the strict-decrease conjecture `Φ > 0 ⟹ cap < α(n)`. The non-strict `cap ≤ α(n)` (the actual `U(n)` target) is consistent with the ridge but is NOT proved by the Φ-framing (it needs the far-from-dyadic strategies from S1/S2/S3/17-family, shared wall with `two-regime-disjunctive`).

## Scope

- **`n = 3` only**. The general-`n` analogue (level-1 exact, deeper levels broken ⟹ `cap = α(n)`) is conjectured but not proved here.
- A **negative result** (records a falsification), not a constructive lemma. The pair-pile cap on the ridge is rigorous; the "no strategy beats `A = 1`" claim is computational evidence (not a proof).
