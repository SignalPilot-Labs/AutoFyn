# master-bound (IMO 2026 P5)

**Statement.** For `f:R_{>0}→R_{>0}` satisfying `sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x·f(y))` for all `x,y>0`, with `g:=f−id`, the original double inequality is equivalent to
```
(★)   |g(x) − g(y)| · (2x + 2y + g(x) + g(y))  ≤  (x − y − g(y))²   for all x,y > 0.
```
The factor `2x+2y+g(x)+g(y) = x+f(x)+y+f(y)` is unconditionally strictly positive (before any use of `g≥0`).

**Proof.** Set `L:=2(x²+f(y)²)−(f(x)+y)²`, `R:=(f(x)+y)²−4x·f(y)` (both `≥0` are exactly the two given inequalities). Direct expansion (completing squares) gives
```
(I)   L + R = 2(x − f(y))²,
(II)  L − R = 2(g(y)−g(x))·(x+f(y)+f(x)+y) = 2(g(y)−g(x))·(2x+2y+g(x)+g(y)).
```
For reals `a,b`: `a,b≥0 ⇔ a+b≥0 ∧ |a−b|≤a+b` (backward: `−(a+b)≤a−b≤a+b` ⟹ `−2a≤0, −2b≤0`). Apply with `a=L, b=R`: (◆) ⇔ `L+R≥0 ∧ |L−R|≤L+R`. Since `L+R=2(x−f(y))²≥0` always, (◆) ⇔ `|L−R|≤L+R`, i.e. (★) after dividing by 2. ∎

**Note.** The factor `2x+2y+g(x)+g(y)` is the amplifying linear mechanism: along forward orbits it grows linearly in `n,m` while the RHS stays bounded — this is what makes the constancy-of-`g` kill work (contrast `cross-inequalities`, which lack this factor and are strictly weaker).

**Certified:** round 1, proof-reviewer. sorry-free; shared by `diagonal-diophantine-kill` and `lipschitz-connectedness`.
