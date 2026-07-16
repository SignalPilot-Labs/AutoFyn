# Build report — ll-inclusion-gap (imo-2026-03), Round 8

**Status: partial** (this round's target achieved; two rival non-anchor pieces remain open).

## What I built this round

**Primary target CLOSED: `T(ℓ)` for ALL `ℓ`, hence `G-INC-1 = Claim(n,0)` for ALL `n`.**
This kills the shared LB anchor crux (`T(ℓ) = GAP-A = B2*`) that stood open 3+ rounds.

Concretely, I extended the round-7 single-claim two-step induction into a **mutual strong induction on
the pair `{Claim(n,ε), T(n)}`**:

- **New Step 12b** — the inductive step for `T(n)` (`n ≥ 3`). It mirrors `Claim(n,ε)`'s Step 12 with:
  - Reduction (ΣP-free top-band decomposition) to `deficit_top + M ≥ 1 − τ`, `τ = 2^n−ΣP ∈ (0,1)`.
  - `h ≥ 4` **IMPOSSIBLE** (four parts `≥ 2^{n−2}` sum to `2^n > ΣP`), so only `h ∈ {0,2}`.
  - `h = 0`: `deficit_top = 2^{n−2} ≥ 2 ≥ 1 > 1 − τ`.
  - `h = 2`: `a = 2^{n−1}−q₁ ≥ 0`, `b = q₂−2^{n−2} ≥ 0`, `deficit_top = a+b`, `ΣP_lo = 2^{n−2}+ε'`,
    `ε' = a−b−τ`. Sub-case 2a (`a+b ≥ 1−τ`) direct; **2b-i** (`ε' ∈ [0,1)`) invokes `Claim(n−2,ε')` →
    `1+2b+τ ≥ 1−τ`; **2b-ii** (`ε' ∈ (−1,0)`) invokes `T(n−2)` → `1+2a−τ ≥ 1−τ`.
  - Critical bound `ε' > −1` in 2b-ii from `a ≥ 0`, `b < 1−τ`. Verified exact.
- **Step 13 rewritten** as a single strong induction on `P(n) = [Claim(n,·) ∧ T(n)]`, bases `P(1),P(2)`
  (Step 11 certified), each step reaching only to `n−2`. Both parity chains `P(1)→P(3)→⋯` and
  `P(2)→P(4)→⋯` grounded; dependency chain written out explicitly.
- **Consequence:** `A(Q∪G_{n−1}) = A(G_{n−1}) − A(Q) ≥ 1` in the INC branch for the anchor, every `n`.

**Secondary write-up: the flagged `h = 0` sub-case of `Claim(n,ε)`'s Step 12** — added explicitly
(`deficit_top = 2^{n−2} ≥ 1 ≥ 1−ε`; reachable `n ≥ 5`, e.g. `Q = {13/2,13/2,6,6,4,3}` at `n=5`). Also
added a nonvacuity remark in Step 12's sub-case 2b (empty `Q_lo` boundary, e.g. `Q = {2^{n−1},2^{n−1}}`,
lands in 2a, never recurses).

## Rigor / correctness checks

- All arithmetic derived from scratch: `deficit_top = a+b`, `ΣP_lo = 2^{n−2}+ε'`, the A-form conversion
  `A(P_lo) ≤ A(G_{n−3}) − 1 − ε'` from `O_{P_lo} ≤ O_{G_{n−3}}` (via `2O_{G_{n−3}} = A(G_{n−3}) +
  2^{n−2} − 1`), and both target inequalities `1+2b+τ ≥ 1−τ`, `1+2a−τ ≥ 1−τ`.
- **Never** invokes `Claim` at negative `ε` (certified-FALSE, `Q_lo = {1.9,1.5}`): 2b-ii calls `T(n−2)`,
  whose target is the ε-free `O_P ≤ O_{G_{ℓ−1}}` on the sum-window.
- Bases cited from Step 11 (certified), not re-proved.
- Numeric re-check this round (bounded <20s, joint cut budget `|P| ≤ ℓ+1` enforced, 1/4 grid):
  `T(2)`: 5 configs, 0 violations, maxO=2=O_G; `T(3)`: 172 configs, 0 violations, maxO=5=O_G (tight).
  Consistent with the proof and prior `ℓ=4` checks.

## Remaining gaps (honest)

The slug's target is the **full lower bound** `c(n)`; that needs INC (all R) AND GAP (all R). Closed
now: INC anchor `R = G_{n−1}`, all `n`; GAP Case-1 (`max(Q) > 2^{n−1}`, `b ≥ 1`). Still OPEN:

- **G-INC-2** (INC, refined R): `S_R` lacks dyadic band structure; SET IDENTITY/top-band decomposition
  are `G_{n−1}`-specific (no known analogue). Vacuous `n=3`, first nontrivial `n=4`. The refinedR
  explorer confirmed it is genuinely separate (tight `R={4,4,4,2,1},Q={5,5,4,2}`, `S_Q=[2,4)⊄S_{G₃}`).
  Not attempted this round (T(ℓ) was the priority; no room left).
- **G-GAP** (non-containment, `0 < b < 1` / interior miss): the alignment-cost bound. This is
  `ll-dyadic-symdiff`'s native territory (rival route), not pushed here.

I did NOT push G-INC-2 this round — the mutual-induction write-up and its verification consumed the
budget, and the outline-reviewer ranked T(ℓ) as the priority with G-INC-2 as "only if room after".
Not overclaimed: G-INC-2 remains a plan, not a proof.

## Promotable lemmas (for the reviewer to certify)

1. **`T(ℓ)` for all `ℓ`** (Step 12b): INC `P`, `|P| ≤ ℓ+1`, `ΣP ∈ (2^ℓ−1,2^ℓ)` ⟹ `O_P ≤ O_{G_{ℓ−1}}`.
   The `ε<0` companion; proved by mutual induction with `Claim`. Rigorous, general `ℓ`.
2. **`G-INC-1 = Claim(n,0)` for all `n`** (Step 13, upgrade of round-7 lemma 6 from `n≤4` to all `n`).
   Both are reusable by `ll-dyadic-symdiff` (its Sub-3b INC sub-case is exactly G-INC-1).

## Spec concerns

None. The dispatch's "close T(ℓ) for all ℓ by mutual induction" is exactly what the certified machinery
supports; the case split cycles (verified well-founded), all bases certified, arithmetic exact. One
note for the orchestrator: with the anchor INC branch now complete for all `n`, the remaining LB work
(G-INC-2 + G-GAP) is the genuinely new frontier — the plateau-risk is now on those two, not on T(ℓ).
