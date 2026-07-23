# Build report — trig-lawofsines — imo-2026-02 (round 1)

Status: **partial**

## Closures achieved this round
1. **Closing relations E2′, E3′ derived in closed form** (the outline-reviewer's
   flagged under-specified piece). Each comes from equating two Law-of-Sines
   expressions for the cevian length (`△BCK` vs `△BMK` for `BK`, giving γ; mirror
   for β). Result:
   - E3′: `sinγ·sinC·sin(A+2θ+γ) = 2 sinA·sin(θ+γ)·sin(C−θ−γ)`.
   - E2′: `sinβ·sinB·sin(A+2θ+β) = 2 sinA·sin(θ+β)·sin(B−θ−β)`.
   They DECOUPLE: E3′ fixes γ(θ) from the K-side alone, E2′ fixes β(θ) from the
   L-side alone. Verified exact against a numeric fsolve/brentq solver: all three
   angle conditions reproduced (1e-6) and `OM=ON` to <1e-13 for many θ on scalene
   triangles.
2. **Full parametrization + cevian formulas** proved and verified (ray directions
   fixed by the "inside ∠LBA / inside ∠ACK" containment; BK, BL by Law of Sines
   in △BCK, △BCL).
3. **Clean reduction** `OM=ON ⇔ (T): 2(|u|²v₂−|v|²u₂)=D(1−2A_x)` using
   `pow(X)=|X−O|²−R²` and the circumcentre formula — a single scalar identity,
   avoids computing O fully (only needs O·(C−B), obtained from the 2×2 perp-
   bisector system). Verified numerically.
4. **Structural simplification:** E3′ (and E2′) is LINEAR in (cos2γ, sin2γ), so the
   physical branch has a closed form.

## Remaining gap
- **Final identity (T) on the physical branch.** CAS ideal-membership
  (`numer(T) ∈ ⟨E3′,E2′,pyth⟩`?) returns FALSE — not because T is false, but
  because {E3′, unit circle} has a spurious second root γ+π (E3′ depends only on
  2γ) and T vanishes only at the physical γ∈(0,C−θ). So ideal membership is the
  wrong (too-strong) test. Closing requires substituting the explicit physical
  linear solution for (cos2γ,sin2γ) — determinate once the branch sign is fixed by
  0<γ<C−θ — or a saturation/sign argument. Believed routine; not finished in
  budget. T and OM=ON numerically certified to machine precision over the whole
  family and several triangles.

## Spec concerns
- None with the problem statement. The 1-parameter DOF and the physical
  branch-selection (via the containment inequalities) are real and must be honored
  by any CAS route: **do NOT use plain Groebner ideal membership** — it admits the
  γ↦γ+π spurious branch and reports false negatives. Next round should substitute
  the closed-form branch (linear-in-cos2γ solution) rather than test membership.

## Handoff / recommendation
The route is one determinate substitution away from complete. Recommend: solve the
linear-in-(cos2γ,sin2γ) form of E3′ for the physical (cos2γ,sin2γ) [rational in
θ,B,C once the sign is chosen], same for β, substitute into (T), and simplify to 0
— a single-variable-in-θ identity check over a symbolic triangle. Numerics leave
no doubt the result is 0.
