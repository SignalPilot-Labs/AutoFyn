# orbit-recurrence-limit-at-infinity (IMO 2026 P5)

**Statement.** Under the master bound (★) of this problem, suppose `g(b)=β>0` for some `b>0`. Then `lim_{a→∞} g(a) = β`, with the quantitative bound `|g(a)−β| ≤ 9β²/(16a)` for `a≥b`. Consequently every positive value of `g` equals `β`.

**Proof.** By orbit-invariance (`g(fⁿ(b))=g(b)`), the orbit `b_m:=b+mβ=f^m(b)` carries `g(b_m)=β` for all `m≥0`. For `a≥b`, by 1-D pigeonhole / nearest-lattice-point, choose `m≥0` with `|a−b_m|≤β/2` (the lattice `b+mβ` covers `[b,∞)` with spacing `β`). Apply (★) with `x=a, y=b_m`:
```
|g(a)−β|·(2a+2b_m+g(a)+β)  ≤  (a−b_m−β)².
```
Set `e:=a−b_m`, `|e|≤β/2`: RHS `=(e−β)²≤(3β/2)²=9β²/4`. LHS factor: `b_m=a−e≥a−β/2`, so `2a+2b_m+g(a)+β ≥ 2a+2(a−β/2)+0+β = 4a` (using `g(a)≥0`). Hence `|g(a)−β|·4a ≤ 9β²/4`, i.e. `|g(a)−β| ≤ 9β²/(16a)→0`.

For the consequence: if `g(y₀)=δ>0`, the orbit `y₀+nδ→∞` carries `g=δ` (invariance); the limit forces `δ=β`. ∎

**Certified:** round 1, proof-reviewer. Used in `lipschitz-connectedness` §3–§4 to reduce the value set of `g` to `{0,β}`.
