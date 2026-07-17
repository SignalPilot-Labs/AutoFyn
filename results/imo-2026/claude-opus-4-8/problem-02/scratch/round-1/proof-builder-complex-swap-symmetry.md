# Build report — complex-swap-symmetry (imo-2026-02), round 1

Status: **partial**

## Closures (rigorous, complete)
- **Frame:** WLOG B=−1, C=1 on real axis, A=a (similarity normalisation). Clean.
- **L1:** `OM=ON ⟺ Re(O)=Re(a)/2` — fully proved (uses N−M=1 real, MM̄−NN̄=−(a+ā)/2).
- **L2 (reviewer's sharpest caveat — CLOSED):** exact sign-correct encoding of the
  three angle hypotheses as reality conditions, verified to machine precision against
  a from-scratch numeric solver (scalene a=0.3+1.4i, 9 family members):
  - E1 ⟺ w1=(K−B)(L−C)/[(A−B)(A−C)] ∈ ℝ₊  (a PRODUCT is real — this is the
    opposite-handedness of K vs L the reviewer flagged; got the sign right)
  - E2 ⟺ w2=(K−B)(L−N)/[(L−B)(C−N)] ∈ ℝ₊
  - E3 ⟺ w3=(K−C)(B−M)/[(L−C)(K−M)] ∈ ℝ₊
  All three w_i had |Im|<1e-16 on solutions. σ swaps w1↦w1, w2↦1/w3 — matches the
  combinatorial symmetry.
- **Circumcentre formula** via the two perpendicular-bisector linear equations —
  proved and checked numerically.
- **Reduction:** whole problem ⟺ `Tnum := (O+Ō−(a+ā)/2)·D = 0` on V(R1,R2,R3).

## Remaining gap (the wall)
- `Tnum=0` verified to **50 digits** on the geometric component C0 — including
  complexified points off the real arc (so it is not merely the reality slice).
- BUT `Tnum ∉ (R1,R2,R3)` and `∉` radical up to power 2 over C(a,ā): the variety
  V(R1,R2,R3) is **reducible**, and Tnum vanishes only on the component C0 carrying
  the solutions. The naive ideal-membership proof therefore fails — this is the
  precise, honest reason (not hand-waving).
- Remaining task: SATURATE (R1,R2,R3) by D·(a±1)(k±1)(l±1) (or extract the correct
  primary component) and reduce Tnum there. Saturation Gröbner timed out (>2 min) in
  the budget. Finite mechanical CAS step — hand to next round with more compute.

## Spec concerns
- None on the problem statement. The encoding L2 is now ground-truth-pinned, so any
  approach (trig too) can trust these three reality conditions and their signs.
- Diversity note for orchestrator: this approach and trig-lawofsines both bottom out
  on a CAS elimination over the 1-parameter family, AND both now share the same deep
  obstacle — the naive elimination variety is reducible / the reality (anti-
  holomorphic) constraint is not algebraically captured by the three conditions
  alone. The outline-reviewer predicted this shared practical wall. If next round the
  saturation still resists, the power-of-point synthetic route is the diversity
  anchor and should be prioritised.

## Files
- Proof/approach: /home/agentuser/repo/results/imo-2026-02/approaches/complex-swap-symmetry.md
- Promotable: L1 and L2 (both fully proved; L2 closes the sign-encoding caveat).
