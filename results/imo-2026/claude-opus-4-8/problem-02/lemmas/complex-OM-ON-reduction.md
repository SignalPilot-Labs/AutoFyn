# Lemma (certified, round 1) — complex-frame reduction of OM=ON

Source approach: `complex-swap-symmetry` (its "L1"). Certified by proof-reviewer
(algebra re-derived symbolically, sympy: identity reduces to 0).

Normalise by an orientation-preserving similarity so that `B=−1, C=1` on the real axis
and `A=a` (non-real, `a≠±1`). Then `M=(a−1)/2`, `N=(a+1)/2`, `N−M=1`. Let `O` be the
circumcentre of `AKL`.

> **OM=ON ⟺ O+Ō=(a+ā)/2 ⟺ Re(O)=Re(a)/2.**

*Proof.* For any `Z`, `|O−Z|²=(O−Z)(Ō−Z̄)`. Expanding,
`|O−M|²−|O−N|²=O(N̄−M̄)+Ō(N−M)+(|M|²−|N|²)`. With `N−M=1` (real, so `N̄−M̄=1`) and
`|M|²−|N|²=[(a−1)(ā−1)−(a+1)(ā+1)]/4=−(a+ā)/2`, this equals `O+Ō−(a+ā)/2`, which
vanishes iff `O+Ō=(a+ā)/2`, i.e. `Re(O)=Re(a)/2`. ∎

Verification (reviewer): symbolic expansion of `|O−M|²−|O−N|²−(O+Ō−(a+ā)/2)=0`.

Status: gap-free, correct. CERTIFIED.

NOTE — the companion "L2" (sign-correct reality encoding of E1,E2,E3 as w1,w2,w3∈ℝ₊)
from the same approach is NOT certified: its handedness/sign determination rests on
"what the numeric solver returns" and is numerically pinned, not derived from scratch.
It must be given a rigorous directed-angle derivation before it can be cached.
