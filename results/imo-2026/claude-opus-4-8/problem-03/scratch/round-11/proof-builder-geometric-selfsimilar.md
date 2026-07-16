# Build report — geometric-selfsimilar (Round 11)

**Status: partial.** Solid new progress on the upper bound; general-m hard case remains an honest open gap.

## Spec concerns
None with the outline's arithmetic. The reviewer-confirmed Σ′ correction (condition (2) is
`p₂ < τ/2 = 2^{m−2}t`, giving `Σ′ = Σ−2p₂ > (2^{m−1}−1)t` for all m) is correct and I re-verified it
symbolically (identity `2^m − 2^{m−1} − 1 = 2^{m−1} − 1`). The Σ′-size was never the blocker. The concern
is that the outliner's *further* claim — that the subproblem inherits gap condition (2′) at threshold t
or falls into an easy MK case — is **FALSE** (see below). So the proposed threshold-invariant induction
does not close as specified; I record this as a rigorous negative result, not a papered-over gap.

## What I proved this round (rigorous, certifiable)

1. **Lemma MK: μ(k pieces, k−1 cuts) ≤ min(pieces).** Full induction proof written to
   `results/imo-2026-03/lemmas/MK.md` (halve largest into invisible pair, recurse; bases k=1,2).
   Verified 0/4000. This is the uniform easy-case tool T4 lacked.

2. **Corollary MK.1 (easy cases, all m).** `δ ≤ t` → MK on X, `A ≤ δ ≤ t`. `d_j ≤ t` → one pairing
   `p_j@p_{j+1}` + MK on the m−1 effective pieces, `A ≤ min ≤ d_j ≤ t`. Budget exactly m−1. Verified 0/4000.

3. **Case A.A at arbitrary threshold t (all m).** For `q₁ > Σ/2` under (I) `q₁ < 2^{m−1}t` and (III)
   `Σ ≥ (2^m−1)t`: subtract-all chain gives `A = 2q₁ − Σ < 2·2^{m−1}t − (2^m−1)t = t`. Verified 0
   violations (m=3,4,5 gap configs). Threshold-invariant form of certified Case A.A.

4. **Clean reduction (all m):** the residual gap case splits exhaustively into
   (a) `p₁>Σ/2` [Case A.A, CLOSED], (b) `p₁≤Σ/2` & (`δ≤t` or `d_j≤t`) [MK, CLOSED],
   (c) `p₁≤Σ/2`, all `d_j>t`, `δ>t` [PURE HARD CASE]. So the ENTIRE remaining UB = case (c). Case (c) is
   closed for m≤3 (Cor R4.1) and m=4 (T4 — its Cases 1/2/3 are exactly Cor MK.1). m≥5 open.

## The open gap (honest)

**The naive threshold-invariant induction is REFUTED.** After the universal `p₁@p₂` move, the
subproblem `Y' = {d₁,p₃,…,p_m}` does NOT inherit condition (2′) `2nd(Y') < 2^{m−3}t`:

| m | hard configs | inherit (I')&(II')&(III') | easy-MK escape | NEITHER |
|---|---|---|---|---|
| 5 (MAX=20) | 898 | 88 | 454 | **356** |
| 6 (MAX=14) | 2120 | 236 | 594 | **1290** |

Yet `μ(Y', m−2) ≤ t` still holds — e.g. `X={8,4,3,2,1}`, `t=18/31`, `Y'={4,3,2,1}`: neither escape holds,
but `μ({4,3,2,1},3)=0` (via `{4,3,2,1}→{2,2,2,2,1,1}` all equal pairs). The subproblem closes through the
full strategy space, not through self-similar gap conditions. So `{(I'),(II'),(III')}` is the **wrong
invariant**; (III') (Σ′-size) is fine, (II') inheritance is the false step. Closing m≥5 needs a
weaker-but-recursable invariant or a direct hard-case strategy. (T) is numerically TRUE (0 violations,
true optimal μ, m=5, 2722 configs, worst 0.795), just not analytically proven for m≥5.

## Files written
- `results/imo-2026-03/lemmas/MK.md` (NEW — for certification)
- `results/imo-2026-03/approaches/geometric-selfsimilar.md` (Status partial; R11 in Approaches tried +
  Current best; new proof section "R11: reduction to the PURE HARD CASE"; Promotable lemmas MK + Case A.A-at-t)

## For the reviewer
- Certify **Lemma MK** (`lemmas/MK.md`) — clean, verifiable, unblocks the uniform easy-case handling.
- Optionally record the threshold-invariant Case A.A corollary into `gap-caseAA-subtract-chain.md`.
- The m≥5 hard case (c) stays the single open UB gap; the naive condition-inheritance route is now
  certified-dead (do not re-dispatch it). Next attack should target case (c) directly.
