## Status
solved

## Approaches tried
- `diagonal-diophantine-kill` — `(L+R, L−R)` sign-decomposition → master bound `(★)` → two-forward-orbit Diophantine kill (Kronecker density for irrational displacement ratios; exact-zero Frobenius lattice point for rational ratios); `d₁=0` edge case closed by maximal-zero-interval + boundary-perturbation reduction. **APPROVE — solved.**
- `lipschitz-connectedness` — same master bound `(★)`; limit-at-infinity `g(a)→β` via Dirichlet nearest-integer (bound `9β²/(16a)`); value set reduced to `{0,β}`; continuity-at-nonzero gap closed by showing both level sets are OPEN (via `O(h²)` at zeros and quadratic-sign `Q(0)=−4βb<0` at β-points) + connectedness. **APPROVE — solved.**
- `swap-cross-inequalities` — derives cross-inequalities `2xf(y)≤y²+f(x)²`, `2yf(x)≤x²+f(y)²` non-circularly (universal QM≥AM on the swapped pair, not the swapped hypothesis). Dead-ended: orbit amplification is asymptotically AM-GM-level (perfect-square leading term `(nd₁−md₂)²`); local two-sided bound squeezes only at zeros of g. **CHANGES REQUESTED — partial, dead-end on forcing; Lemma 1 certified as a reusable derived inequality.**

## Current best
The problem is **solved**. Two independent complete proofs (approaches 1 and 2) establish that every admissible `f : R_{>0}→R_{>0}` is `f(x)=x+c` with `c≥0`.

Key shared machinery: diagonal collapse (`f(f(y))=2f(y)−y`, `g:=f−id ≥ 0`, `g` constant on forward orbits, `fⁿ(y)=y+n·g(y)`); the `(L+R, L−R)` identities; the master bound `(★)` `|g(x)−g(y)|·(2x+2y+g(x)+g(y)) ≤ (x−y−g(y))²`. The amplifying linear factor `2x+2y+...` in `(★)` (vs the cross-inequalities' lack thereof — approach 3) is what makes the constancy-of-`g` kill work.

## Full proof

Let `f:R_{>0}→R_{>0}` satisfy, for all `x,y>0`,
```
        ⎛ x² + f(y)² ⎞                 ⎽⎺
   √    ⎜ ─────────── ⎟   ≥   (f(x)+y)/2   ≥   √(x·f(y)).            (◆)
        ⎝     2       ⎠
```
We prove the answer is exactly `f(x)=x+c` for a constant `c≥0`.

### 1. Diagonal collapse (C1)+(C2)

Specialize `x=f(y)` (legitimate: `f(y)>0`). Then `(x,f(y))=(f(y),f(y))` is equal, so QM=AM=GM all equal `f(y)`, and (◆) reads `f(y) ≥ (f(f(y))+y)/2 ≥ f(y)`, forcing
```
(C1)   f(f(y)) = 2 f(y) − y     for all y > 0.
```
Define the displacement `g(y):=f(y)−y`. Since `f(t)=t+g(t)`, (C1) gives `f(y)+g(f(y)) = y+2g(y)`, i.e. `(y+g(y))+g(f(y))=y+2g(y)`, hence `g(f(y))=g(y)`: **`g` is invariant along each forward orbit.** Inducting, `fⁿ(y)=y+n·g(y)` for all `n≥0`. If `g(y)<0`, the iterate `fⁿ(y)=y+n·g(y)→−∞` leaves `R_{>0}` — contradiction. Therefore
```
(C2)   g(y) ≥ 0     for all y > 0   (hence f(y) ≥ y).
```

### 2. The master bound (★)

Both sides of each inequality in (◆) are nonnegative; squaring is legitimate. Set
```
L := 2(x²+f(y)²) − (f(x)+y)² ≥ 0,     R := (f(x)+y)² − 4x·f(y) ≥ 0
```
(Nonnegativity is exactly the two given inequalities). Direct expansion (completing squares) gives the two identities
```
(I)   L + R = 2(x − f(y))² = 2(x − y − g(y))²,
(II)  L − R = 2(g(y) − g(x))·(x + f(y) + f(x) + y) = 2(g(y)−g(x))·(2x+2y+g(x)+g(y)).
```
The factor `2x+2y+g(x)+g(y)=x+f(x)+y+f(y)>0` unconditionally (each summand positive).

For real `a,b`: `a,b≥0 ⇔ a+b≥0 ∧ |a−b|≤a+b`. Apply with `a=L, b=R`: (◆) ⇔ `L+R≥0 ∧ |L−R|≤L+R`. Since `L+R=2(x−f(y))²≥0` always, (◆) ⇔
```
(★)   |g(x) − g(y)|·(2x + 2y + g(x) + g(y))  ≤  (x − y − g(y))²   for all x,y > 0.
```

### 3. Constancy of g (necessity): two routes

**Route A — Diophantine kill (`diagonal-diophantine-kill`).** Suppose `g` is not constant; pick `a,b` with `0 ≤ d₁:=g(a) < d₂:=g(b)`. By orbit-invariance, the orbits `a+nd₁` (carrying `g=d₁`) and `b+md₂` (carrying `g=d₂`) are admissible for all `n,m≥0`. Substituting into (★):
```
(d₂−d₁)·(2a+2b+d₁+d₂+2nd₁+2md₂)  ≤  (a−b+nd₁−(m+1)d₂)².   (★★★)
```
The LHS → +∞ as `n,m→∞` (since `d₁,d₂>0`); the RHS is `(a−b+u_{n,m})²` with `u_{n,m}=nd₁−(m+1)d₂`.

- *Irrational `d₁/d₂∉Q`.* By Kronecker/Weyl equidistribution (1-D), `{nα−m : n,m∈Z_{≥0}}` is dense in R with arbitrarily large witnesses (irrational `α>0`): choose `k` large with `{kα}` near `{T}`, set `n=k, m=⌊kα⌋−⌊T⌋→∞`. With `α=d₁/d₂`, `T=(b−a)/d₂+1`, get a sequence `(n_j,m_j)→∞` with `u_{n_j,m_j}→b−a`, so RHS→0 while LHS→+∞ — contradiction.
- *Rational `d₁/d₂=p/q` (lowest, `p<q, p≥1`).* Set `n=kq, m=kp−1` (`m≥0` for `k≥1`). Then `u_{n,m}=k(qd₁−pd₂)=0`, RHS=`(a−b)²` constant; LHS→+∞ as `k→∞` — contradiction.
- *Edge `d₁=0<d₂`.* Lemma: `g(a)=0 ⇒ g(x)→0` as `x→a` (set `y=a` in ★: `g(x)(2x+2a+g(x))≤(x−a)²`; for `|x−a|<a/2` the factor `≥3a`, so `g(x)≤(x−a)²/(3a)`). If every neighbourhood of `a` contains a point with `g>0`, pick `x_n→a` with `0<g(x_n)→0<d₂` and reduce to the main kill with `d₁=g(x_n)>0`. Otherwise `g≡0` on a maximal open interval `I_max=(α,β)`. The right endpoint `β` is finite (else the orbit `b+nd₂→∞` of a `d₂`-point enters `(α,∞)` where `g=0`, contradicting invariance `g=d₂`); `g(β)=0` (let `y∈(α,β), x=β` in ★, `y→β⁻`: `g(β)(4β+g(β))≤0`); and `g` is not identically zero on any `(β,β+ε)` (maximality). So points `x_n→β⁺` with `0<g(x_n)→0<d₂` exist, reducing again to the main kill — contradiction.

All three sub-cases impossible, so `g` is constant: `g≡c, c≥0` (by (C2)).

**Route B — Lipschitz/connectedness (`lipschitz-connectedness`).** Same (C1)+(C2) and (★). If `g` has no positive value, `g≡0`. Else pick `b` with `β:=g(b)>0`; orbit `b_m=b+mβ` carries `g=β`. For `a≥b`, pick `m` with `|a−b_m|≤β/2` (1-D pigeonhole); (★) with `x=a, y=b_m` gives `|g(a)−β|·4a ≤ 9β²/4`, i.e. `|g(a)−β|≤9β²/(16a)→0`. Hence `g(a)→β`. If `g(y₀)=δ>0`, the orbit `y₀+nδ→∞` (carrying `g=δ`) forces `δ=β` by the limit; so the value set of `g` lies in `{0,β}`. Now both level sets `Z={g=0}` and `P={g=β}` are open: at `a∈Z`, ★ gives `g(a+h)≤h²/(3a)<β` for small `h`, forcing `g(a+h)=0`; at `b∈P`, supposing `g(b+h)=0` gives `h²−4βh−4βb≥0`, but `Q(0)=−4βb<0` and `Q` is negative on the open interval `(2β−2√(β²+βb), 2β+2√(β²+βb))⊇(-b,b)`-around-0 (the lower endpoint exceeds `−b`), forcing `g(b+h)=β` on a neighbourhood. `Z∪P=(0,∞)` with both open; by connectedness of `(0,∞)` and `P` nonempty, `Z=∅`, so `g≡β`. Both branches give `f(x)=x+c, c≥0`.

### 4. Construction (sufficiency) and codomain

For `f(x)=x+c` with `c≥0`: the middle term `(f(x)+y)/2=(x+y+c)/2=AM(x,y+c)`; the outer bound `√((x²+(y+c)²)/2)=QM(x,y+c)≥AM(x,y+c)`; the inner bound `√(x(y+c))=GM(x,y+c)≤AM(x,y+c)` — both by the classical QM-AM-GM chain, valid for the positive pair `(x,y+c)` (since `x>0, y+c>0`). Direct expansion also gives `L=R=(x−y−c)²≥0`. The codomain `f:R_{>0}→R_{>0}` forces `c≥0` (if `c<0`, `x+c<0` for `x∈(0,−c)⊂R_{>0}`).

### 5. Conclusion

Necessity (§3) + sufficiency (§4) give the full characterization:
```
   f(x) = x + c,    c ∈ R,  c ≥ 0.     ∎
```

## Notes
- Approach `swap-cross-inequalities` contributes the certified derived lemma `2xf(y)≤y²+f(x)²`, `2yf(x)≤x²+f(y)²` (non-circularly proven) but is too weak to force constancy of `g`; it is subsumed by the master-bound routes above.
