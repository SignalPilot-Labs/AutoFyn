# Lemma: Superincreasing-R identity

**Status:** CERTIFIED (round 4; CORRECTED round 5 — false corollary REMOVED). Proved in `approaches/pairing-partner.md` §A (round 4) / §0 (round 5). Reviewer re-derived the identity with exact-rational python (100000 random configs, 0 violations).

> **⚠ ROUND-5 CORRECTION (by proof-reviewer):** the round-4 "Corollary (obstruction bound)" section claimed `Σ_{MM} m_even ≤ σ = M − m_1 ≤ M/2 = a_1`. This is **FALSE for `k ≥ 2`** (the step `m_1 ≥ M/2` holds only when `k + 1 = 2`, i.e. `k = 1`; for `k + 1 ≥ 3` pieces summing to `M`, the largest satisfies `m_1 ≥ M/(k+1)`, which can be strictly below `M/2`). Counterexample at `n = 2` (level-3 dyadic, `M = 8`, `a_1 = 4`): `m = (3, 3, 1, 1)` has `m_1 = 3 < 4 = M/2`, so `σ = 5 > 4 = a_1`. The corollary is therefore **INVALID in the very sub-case (`k ≥ 2`) it targeted and is DELETED from this lemma**. The IDENTITY below is unaffected. (A scoped bound `σ ≤ a_1` does hold under the Branch-1 hypothesis `m_1 ≥ a_1` of the `pairing-partner` round-5 build; that scoped bound is NOT a general lemma and is not certified here.)

## Statement

In the level-`(n+1)` dyadic's `M ⊎ R` self-similar decomposition (`M = 2^{n+1}/D(n+1)`, `R = (1, 2, 4, …, 2^n)/D(n+1)`), the unrefined `R`-pieces

`a_j = 2^{n+1−j} / D(n+1)`,   `j = 1, …, n+1`   (`a_1 = 2^n/D(n+1) > a_2 = 2^{n−1}/D(n+1) > … > a_{n+1} = 1/D(n+1)`)

are **pairwise distinct and superincreasing**: for every `j`,

`a_j − Σ_{l > j} a_l = 1/D(n+1) = α(n+1) > 0`,   hence   `a_j > Σ_{l > j} a_l`.

*Proof.* `a_j = 2^{n+1−j}/D(n+1)` and `Σ_{l > j} a_l = (2^{n+1−j} − 1)/D(n+1)`, so `a_j − Σ_{l>j} a_l = 1/D(n+1)`. ∎

(This is the per-piece form of the certified dyadic-dominance identity `M − total(R) = α(n+1)` — the `j = 1` case is `a_1 − total(R\{a_1}) = α(n+1)`.)

## Reusability

Provides the structural input to any Hall-matching attack on the residual `(Match) Σ_{MM} m_even ≤ Σ_{RR} r_odd` (the open handle of G1, localized by the certified `e_M ≤ o_R` reduction + self-compensation lemma). The superincreasing gap `a_j − Σ_{l>j} a_l = α(n+1)` is the candidate Hall witness (each `MM` smaller half sits below a distinct dyadic level of `R`, so a distinct `RR` larger half dominates it). The identity does NOT by itself close the `(Match)` (no magnitude bound on `Σ_{MM} m_even` follows from the identity alone for `k ≥ 2`); the full Hall matching is a CONJECTURE for general `n` (verified `n = 1..5`, OPEN).

## Scope

- General `n` (the identity holds for all `n`).
- The identity is a structural input, NOT a matching — does not close G1 alone.
- The general-`n` Hall matching on rank indices is a verified conjecture (OPEN), not certified by this lemma.
- **Do NOT cite the deleted obstruction-bound corollary** `σ ≤ M/2 = a_1` — it is false for `k ≥ 2`.
