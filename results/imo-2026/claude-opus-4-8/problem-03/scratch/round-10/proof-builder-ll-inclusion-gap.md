# Build report — ll-inclusion-gap (Round 10)

**Slug:** ll-inclusion-gap (imo-2026-03, LB INC branch, refined-R closure)
**Status:** partial (unchanged; genuine advance + a rigorous negative result)

## What I built
Attempted the refined-R **{Claim_R, T_R} mutual induction** (Gen-Decomp descent) the outline asked for.
In building it I established, rigorously, that **it does not close G-INC-2** — the class is not
descent-closed. I also fully closed a residual and pinned the true bottleneck.

### Positive, rigorous
- **G-INC-2e (equal-split thin edge) CLOSED for `n ≤ 6`** (Step 22). Mechanism: equal-pair-removal →
  L1 (any Q with a repeated value); `h̄=0` (`deficit_top ≥ 1`); and the **rigorous vacuousness** of the
  all-distinct `h̄≥2, q₁>q₂` edge — `ΣQ_lo < (m−1)2^{m−2}` forces `q₁+q₂ > 2^{m−2}(9−m)`, while
  distinct parts `≤ 2^{m−1}` give `q₁+q₂ < 2^m`; `2^{m−2}(9−m) ≥ 2^m ⟺ m ≤ 5`. So empty for `m ≤ 5`
  (`n ≤ 6`). This tightens round 9's "closed except thin edge" to a proof for `n ≤ 6`.
- **h=2 inductive-step arithmetic written** (Step 20), rigorous *conditional on* the sub-instance being
  in-class — exactly the anchor's 2a/2b-i/2b-ii routing, ε' via T_{R_lo} never Claim at ε<0.

### Rigorous NEGATIVE result (the honest core of the round)
- **{Claim_R, T_R} is OBSTRUCTED** (Step 21). The refined-R class is not closed under `n→n−2` descent:
  - **O1** `h_{R_lo}` parity breaks for lower-band cuts at `k₀∈{n−4,n−3}` — witness `{1,2,2,2,8,16,32}`
    (`h_R=2` even, but `h_{R_lo}=1` odd), so Gen-Decomp cannot be re-applied. **Corrects the explorers'
    claim "h_{R_lo}=2 always."** Even lower-band cuts do not self-sustain.
  - **O2** the anchor's `h=0` bound `deficit_top ≥ 2^{n−2}` fails for general R (`= q₁−q₂`, can be <1).
  - **O3** top-piece cuts give `R_lo = G_{n−3}∪{a}`, not a refinement; and the structure-free abstract
    Claim_R is **FALSE** (budget-enforced, ΣR=2^ℓ−1: `R={1,3,3}`, `Q={1,7/2,7/2}` give `A(R)=A(Q)=1`;
    `{1,3,3}` is not a cut of `{1,2,4}`). So Claim_R needs the exact refinement structure the descent
    destroys.
  Conclusion: Gen-Decomp gives the descent *identity* but not a descent-*closed class*; the route the
  R10 outline hoped to revive cannot close G-INC-2. Future work needs a descent-closed structured class
  (none known) or a direct `A(R)` evaluation per cut type (outline's fallback, not done here).

### G-INC-2nt / a<1
- `n=4` base **verified** 0-violation (123 budget-valid configs, min margin 1); general + `a<1` OPEN,
  obstructed by O1–O3. Not a proof (continuum in `a`).

## Numerics (all bounded <60s, joint budget c_Q+c_R≤n enforced)
- Class-closure O1: enumerated all `k₀ ≤ n−3` lower-band cuts at n=6; `k₀∈{2,3}` give odd `h_{R_lo}`.
- G-INC-2nt n=4: 123 configs, 0 viol, margin 1.
- G-INC-2e vacuousness: m=3,4,5 vacuous; m=6 first feasible (arithmetic + confirms).
- Abstract Claim_R (drop refinement): with joint budget + ΣR=2^ℓ−1, 12 viol at ℓ=3, all non-refinements
  at margin 0 → refinement structure is necessary.

## Promotable lemmas proposed
- **#11 G-INC-2e vacuousness** (fully proven, m≤5): closes equal-split for n≤6.
- **#12 Refined-R descent non-closure** (rigorous negative result O1/O2/O3): documents the obstruction so
  future rounds don't retry the clean {Claim_R,T_R} induction; reusable by ll-dyadic-symdiff's INC import.

## Spec concerns:
The R10 outline + both explorers overclaimed the {Claim_R,T_R} induction as a clean build ("h_{R_lo}=2
always", "descent clean", "closes G-INC-2nt(a≥1)+G-INC-2lb"). This is FALSE (O1 verified). The real
bottleneck is G-INC-2nt via a **non-inductive** attack (direct A(R)), not the mutual induction. Also the
outline said "This closes G-INC-2lb" — it does not; lb funnels into nt and inherits the obstruction. The
outliner should redirect: put an explorer on the direct-A(R)-per-cut-type route, and treat the
{Claim_R,T_R} revival as CLOSED-negative (do not re-dispatch it).
