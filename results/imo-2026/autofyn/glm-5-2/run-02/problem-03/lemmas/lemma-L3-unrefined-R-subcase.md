# Lemma: L(3) unrefined-R sub-case (reals)

**Status:** CERTIFIED (round 4; RE-WORKED round 5 — m_1-split fix, now self-rigorous for BOTH branches). Proved in `approaches/pairing-partner.md` §B (Branch 1, round 4) + §B' (Branch 2, round 5). Reviewer re-derived the closed form `A = 7 − 2(s_3+s_5)` (Branch 1) and the Branch 2 reduction `A = 4 − A_rest, A_rest = 2·oddsum(rest5) − 11` with exact-rational python (39,980 grid + 500k random configs in Branch 2, 0 violations `A < 1`, min `A → 1` as `m_1 → 4⁻`).

> **⚠ ROUND-5 RE-WORK (by proof-reviewer):** the round-4 proof's setup `s_1 = a_1` (via `b_1 ≤ σ ≤ 4`) is valid ONLY under `m_1 ≥ a_1 = 4` (i.e. `σ ≤ 4`). It does NOT cover the ~50% of configs with `m_1 < 4` (`σ > 4`, where `a_1 = 4` is the global rank-1 piece, not `m_1`). The round-5 **m_1-split** fixes this: Branch 1 (`m_1 ≥ 4`) = the round-4 casework, correctly scoped; Branch 2 (`m_1 < 4`) = a NEW 6-piece casework reducing to `oddsum(rest5) ≥ 4`, proved in full in `approaches/pairing-partner.md` §B'. The RESULT `A ≥ 1/15` is unchanged; the lemma is now self-rigorous (no longer reliant on the cell-complex L(3) certification, which still stands independently as a cross-check).

## Statement

For Liu's level-3 dyadic config `Liu = (1, 2, 4, 8)/15`, suppose Xiang's three marks **all land in the largest piece `M = 8/15`** (so `R' = R = (1, 2, 4)/15` is **unrefined**, superincreasing structure intact). Then for every real such response,

`A ≥ 1/15 = α(3)`,

with equality iff the small `M`-sub-pieces realize `{m_2, m_3, m_4} = {2/15, 1/15, 1/15}` (the staircase equality case) or the degenerate limit `{2/15, 2/15, 0}` (a mark at `M`'s boundary).

## Proof (sketch; full proof in `approaches/pairing-partner.md` §B)

Work in `1/15` units (stick totals `15`, `M = 8`, `R = (4, 2, 1)`, superincreasing). Three marks in `M` split it into `m_1 ≥ m_2 ≥ m_3 ≥ m_4`, `Σ m_i = 8`. The proof now splits into two branches by the **m_1-split**:

- **Branch 1 (`m_1 ≥ 4 = a_1`):** `σ = m_2 + m_3 + m_4 = 8 − m_1 ≤ 4 = a_1`, so `m_2 ≤ σ ≤ 4 = a_1`, hence `s_1 = a_1 = 4` in the merge of `{m_2, m_3, m_4}` with `R`. The closed form below and the 3-case casework apply. (This is the round-4 proof, correctly scoped.)
- **Branch 2 (`m_1 < 4`):** `a_1 = 4` is the global rank-1 piece (Liu's, `+4`); all `m_i < 4`. The rest `rest = {m_1, m_2, m_3, m_4, 2, 1}` occupies ranks 2–7; `A = 4 − A_rest` with `A_rest = t_1 − t_2 + t_3 − t_4 + t_5 − t_6` (sorted `t`'s). With `rest_total = 11`, `A = 15 − 2·oddsum(rest)`, so `A ≥ 1 ⟺ oddsum(rest) ≤ 7 ⟺ evensum(rest) ≥ 4`. Removing `t_1 = m_1` (since `m_1 ≥ 2 = a_2` and `m_1 ≥ m_i`), `evensum(rest) = oddsum(rest5)` where `rest5 = {m_2, m_3, m_4, 2, 1}`. Target: `oddsum(rest5) ≥ 4`. Proved by a 6-case casework on `m_2` vs `2` and `m_3` vs `1` (see `approaches/pairing-partner.md` §B'); the impossible sub-case (`m_2 < 2, m_3 < 1, m_4 < 1`) is ruled out by `m_2 + m_3 + m_4 = 8 − m_1 > 4` forcing `m_2 > 2`. Each sub-case closes with `oddsum(rest5) ≥ 4`, strict except in the limit `m_1 → 4⁻`. ∎ (Branch 2)

**Branch 1 detail:** Let `σ = m_2 + m_3 + m_4 = 8 − m_1 ≤ 4 = a_1`, and `b_i := m_{i+1}` (so `b_1 ≥ b_2 ≥ b_3`, `Σ b_i = σ ≤ 4`).

Merge `{b_1, b_2, b_3}` with `R = {4, 2, 1}` and sort descending: `s_1 ≥ … ≥ s_6`. Since `b_1 ≤ σ ≤ 4 = a_1`, `s_1 = 4`. The global advantage is

`A = m_1 − s_1 + s_2 − s_3 + s_4 − s_5 + s_6`.

Using `Σ s_i = σ + 7` and `s_1 = 4`:

`A = (8 − σ) − 4 + (σ + 3 − s_3 − s_5) − (s_3 + s_5) = 7 − 2(s_3 + s_5)`.

So `A ≥ 1 ⟺ s_3 + s_5 ≤ 3 = a_2 + a_3`. Equivalently (with `t_i := s_{i+1}`, the sorted-desc list of `{b_1, b_2, b_3, 2, 1}`): `t_2 + t_4 ≤ 3`.

**3-case casework on `t_2`:**

- **Case I (`t_2 > 2`):** at least two of `{b_1, b_2, b_3}` exceed `2` (the `R`-pieces `2, 1` do not strictly exceed `2`), so `σ > 4`. **Impossible** (contradicts `σ ≤ 4`).
- **Case II (`t_2 = 2`):** forces `b_3 ≤ 1` (else `σ > 4`), so among `{b_3, 1}` at least two pieces `≤ 1`, giving `t_4 ≤ 1`. Hence `t_2 + t_4 ≤ 3`. ✓
- **Case III (`t_2 < 2`):** `b_1 < 2`, so `t_1 = 2`, `t_2 = b_1`. Three sub-cases by `b_2, b_3` vs `1`:
  - IIIa (`b_2 ≥ 1 ≥ b_3`): `t_4 = 1`, `t_2 + t_4 = b_1 + 1 < 3`. ✓
  - IIIb (`b_2 ≥ b_3 ≥ 1`): `t_4 = b_3`, `t_2 + t_4 = b_1 + b_3 = σ − b_2 ≤ 4 − b_2 ≤ 3` (strict — equality forces `b_1 = b_3 = 1.5`, contradicting `b_2 ≥ b_3`). ✓
  - IIIc (`b_3 ≤ b_2 ≤ 1`): `t_4 = b_2`, `t_2 + t_4 = b_1 + b_2 < 2 + 1 = 3`. ✓

Equality: Case II with `t_4 = 1`, `b_1 = 2`, `σ = 4` (`m_1 = 4`), giving `{m_2, m_3, m_4} = {2, 1, 1}` (staircase) or `{2, 2, 0}` (degenerate). ∎

## Reusability

The first real-valued `k ≥ 2` foothold on G1 (Lemma L general-n), independent of the cell-complex route. The closed form `A = (target formula in rank-index sums)` + casework pattern is a template for `L(n)` at small `n` via the superincreasing lever. Provides corroboration for any approach targeting `L(3)`.

## Scope

- **n = 3 only**, and **only the `k = n+1` (unrefined-R) sub-case** (all marks in `M`), now covering BOTH `m_1 ≥ a_1` (Branch 1) and `m_1 < a_1` (Branch 2) disjointly and exhaustively.
- Does NOT cover the `R`-refined sub-cases (`k ≤ n`, some marks in `R`) — OPEN over reals.
- Does NOT lift to general `n` (the general-`n` Hall matchings (H1) and (H2) are verified conjectures, OPEN).
- The full `L(3)` over reals (all `k`, all `R`-refinements) is closed by the sibling `cell-complex-l3` vertex enumeration (CERTIFIED); this lemma is now a SELF-RIGOROUS independent parallel foothold (no longer reliant on the cell-complex certification).
