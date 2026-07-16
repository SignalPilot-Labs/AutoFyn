# Build report — ll-inclusion-gap, round 9 (G-INC-2)

Status: **partial** (honest). Target was G-INC-2 (refined-R INC branch). Real, rigorous progress on the
equal-split top cut; new promotable tools; lower-band / non-equal top cut left open with mechanism.

## Spec concern (outline was wrong on one point)
The outline's **step-1 cheap-kill is self-contradictory**: it requires `f⁺ ≥ f⁻` (⟹ `A(R) ≥ A(G_{n−1})`)
AND `f⁺ = 0` (⟹ `S_R ⊆ S_{G_{n−1})}` ⟹ `A(R) ≤ A(G_{n−1})`); together these force *no cut*, so it is
vacuous. Fixed in Step 15: the correct cheap-kill needs `S_Q ⊆ S_{G_{n−1}}` (NOT automatic from
`S_Q ⊆ S_R` — the tight n=4 pair has `S_Q ⊄ S_{G_3}`) AND `A(R) ≥ A(G_{n−1})`, then certified G-INC-1
gives it. Narrow but honest.

## What is now rigorous (in the approach file)
- **Gen-Decomp (Step 16, promotable):** refined-R top-band decomposition
  `A(R)−A(Q) = deficit_top + (A(R_lo)−A(Q_lo))`, both ≥0, with the clean descent `S_{Q_lo} ⊆ S_{R_lo}` —
  **no SET IDENTITY** (the anchor tool with no refined-R analogue). This is the correct engine.
- **Lemma L1 (Step 17, promotable, FULLY PROVEN):** `S_P⊆S_{G_{m−1}}`, `|P|≤m−1` ⟹ `A(P)≤A(G_{m−1})−1`,
  by a clean `m→m−2` **budget** induction (no ε, no T-companion). The strict `−1` is forced by the
  budget — exactly the reviewer's diagnosis. Tight (`P=G_{m−1}∖{1}`), 0-violation m=2..6.
- **Equal-split top cut (Step 18):** proved `S_R = S_{G_{n−2}}` exactly (verified n=4..9); reduced to
  large-pair count `g∈{0,2}` (`g≥4` impossible, `W>ΣQ`); closed `g=2` via L1, and `g=0` when `h̄=0` or
  the two largest parts are equal. Handles the reviewer's **multi-part `−1`** worry: the `−1` is L1's
  budget deficit, valid for any number of parts (not just 2). This is the case the Parity-Condition does
  NOT fire (h can be odd) — closed except one edge.

## Reviewer's required gaps — status
1. **Step-2 well-foundedness (lower-band ↔ top-piece mutual recursion):** made the dependency EXPLICIT
   (Step 19) — a lower-band cut at level `n` descends to a top cut at level `n−2`; Gen-Decomp supplies
   the descent identity, but the cross-position recursion + unpinned `ΣQ_lo` are NOT closed. Honest open
   gap G-INC-2lb.
2. **Step-3 multi-part `−1`:** CLOSED via L1 (the `−1` = budget deficit, any part count). The band-width
   arithmetic `maxgap = 2^{n−3} ≤ A(G_{n−2})−1` is subsumed: `S_R = S_{G_{n−2}}` makes it an anchor
   statement, and L1 gives the exact `−1` without band-by-band bookkeeping.
3. **Step-4 a<1 sub-case:** NOT closed; flagged with the rest of the non-equal top cut (G-INC-2nt).

## Honest open gaps (in file)
- G-INC-2e: equal-split edge `g=0, h̄≥2, q₁>q₂` (non-near-tight; numerics comfortable).
- G-INC-2lb: lower-band cut cross-position recursion / unpinned `ΣQ_lo`.
- G-INC-2nt: non-equal top cut, incl. `a<1`.
- (G-GAP unchanged; ll-dyadic-symdiff territory.)

## Numerics (bounded <20s, joint cut budget enforced)
- `S_R = S_{G_{n−2}}` for equal-split: exact set equality n=4..9. ✓
- Equal-split max A(Q): n=4→2, n=5→4, n=6→10 = `A(G_{n−2})−1` (tight). ✓
- L1 max A(P): tight at `A(G_{m−1})−1`, 0 violations m=2..6. ✓
- g∈{0,2} confirmed analytically (`g≥4 ⟹ W>ΣQ`). ✓

## Suggestion for next round
Gen-Decomp gives the refined-R descent identity the reviewer said was missing (why refined-r-alt-tail was
cut). An ε/τ `{Claim_R, T_R}` over the joint cut-position family may now be viable — worth an explorer
scout. That would close G-INC-2lb + G-INC-2nt together and likely the equal-split edge.
