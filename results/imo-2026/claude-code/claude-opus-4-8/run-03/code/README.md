# Verification certificates — "Prove OM = ON" (ISL-2021-G8-type problem)

Triangle `ABC`, midpoints `M,N` of `AB,AC`; interior points `K,L` with
`∠KBA=∠ACL=:β`, `∠LBK=∠LNC`, `∠LCK=∠BMK`. `O`=circumcentre of `AKL`.
Claim: `OM = ON`.

Requires: `python3` with `numpy`, `scipy`, `sympy`, `mpmath`.
Run any file with `python3 <file>.py`.

## The proof and where each step is certified

**Reduction.** `A* := 2O − A` (antipode of A on ⊙AKL). Since `M=(A+B)/2`,
`N=(A+C)/2`, we get `OM=½·A*B`, `ON=½·A*C`, so `OM=ON ⇔ A*B=A*C`
(A* on ⊥bisector of BC). A* lies on ⊥AK-at-K and ⊥AL-at-L (Thales).

**Key Lemma.** ⊥AK-at-K meets the ⊥bisector of BC at signed height
`½·BC·cot(∠A+β)` — depends only on ∠A, β, BC, hence symmetric in B↔C.
Same for L ⇒ both perpendiculars meet on the ⊥bisector ⇒ A* is there.

| Script | What it certifies |
|---|---|
| `explore.py`        | Sets up config, solves for K,L numerically; identifies the valid branch (K∈△BMC, L∈△BNC); confirms `OM=ON` (~1e-15). |
| `explore5.py`       | **Reduction:** `A*B=A*C` and A* on ⊥bisector, across 3 triangles. |
| `verify_lemma.py`   | **Key closed form:** `Φ(K)=Φ(L)=½cot(∠A+β)` across 5 triangles × 4 β. |
| `angles.py`         | Confirms median relation (a) `cotμ=cotβ+2cotδ` and constraint `ε=β+δ`. |
| `sanity.py`         | Confirms the symbolic building blocks: `cotδ`, `cotε` formulas, AK-equality. |
| `prove_target.py`   | **Crux (symbolic):** cleared hypothesis `cotε=cot(β+δ)` ≡ `(★)`, ratio = **1** exactly. |
| `target2.py`        | `(★)`'s root in μ equals the configuration's μ (⇒ hypothesis ⇔ (★)). |
| `finalcheck.py`     | **End-to-end:** OM=ON, A*B=A*C, height=½BC·cot(A+β), height-formula — all ~1e-13, 4 triangles × 3 β. |

Decisive certificates: **`finalcheck.py`** (whole chain, numeric) and
**`prove_target.py`** (crux identity, symbolic/exact).

## Exploration scaffold (kept for provenance)
`explore2/3/4/6/7/8.py` — concyclicity/collinearity/spiral-similarity searches,
second-intersection probing, the `Φ(K) = −Ψ(K)/(8Δ(K))` derivation, isogonality
tests. `sym1/sym2.py`, `ratio.py`, `prove_lemma.py`, `target.py`, `check_spade.py`,
`star_spade.py` — intermediate symbolic attempts (note: `(♠)` in `star_spade.py`
was a discarded hand-derivation with a sign slip; the crux uses `(★)` via
`prove_target.py`, not `(♠)`).
