# proof-builder report — labeling-duality — round 1

Status: partial (not solved).

## What was done
1. Fully verified (not just asserted) the σ-invariance of the hypothesis
   system: rewriting ∠KBA=∠ACL as ∠KBM=∠LCN (ray BA=ray BM, ray CA=ray CN
   since M∈AB, N∈AC), then checking σ:B↔C,K↔L,M↔N fixes condition (1′) and
   swaps conditions (2)↔(3) exactly (using symmetry of angle notation
   ∠XYZ=∠ZYX). Also confirmed the containment/interiority hypotheses are
   syntactically self-dual under σ.
2. Derived a NEW, much cleaner reduction of OM=ON, replacing the outline's
   messy Cramer's-rule / cross-product expansion of the circumcenter. Using
   the classical median-length (Apollonius) identity `OZ² = (OX²+OY²)/2 −
   XY²/4` (proved from scratch via the parallelogram law) applied twice with
   O = circumcenter(AKL) (so OA=OK=OL=R), the whole problem OM=ON reduces
   to a single scalar identity:
   `pow_Γ(B) − pow_Γ(C) = (AB² − AC²)/2`, where Γ = circumcircle(AKL).
   This equivalence is fully proved (no gaps) and is a strictly sharper
   target than the original outline's plan.
3. Verified this reduction numerically to 1e-10 on the explorer's concrete
   example (A=(0,3), B=(-2,0), C=(3,0), θ=25°, solved via fsolve) — both
   OM=ON and the power identity check out.
4. Attempted to close the remaining identity via secant lines through B, C
   to circle Γ (using known points A, K, L on Γ) — did not find a full
   synthetic closure in the time budget. This is now the honest, sole
   remaining gap: express pow_Γ(B), pow_Γ(C) via the three angle hypotheses.
5. Cross-checked the outline's original Cramer's-rule vector route and
   showed it's equivalent to but strictly messier than the power-of-a-point
   target (TI); recommended future rounds drop it and work with (TI)
   directly.

## Key output for other approaches / next round
The reduction `OM=ON ⟺ pow_Γ(B) − pow_Γ(C) = (AB²−AC²)/2` (Γ=circumcircle
AKL) is fully proved and promotable as a shared lemma — any approach
(coordinate, synthetic, complex-number) attacking this problem should target
this single scalar power-of-a-point identity rather than OM=ON directly, and
should also import the median-length (Apollonius) lemma rather than
re-deriving it.

File written: `/home/agentuser/repo/results/imo-2026-02/approaches/labeling-duality.md`
(Status: partial).
