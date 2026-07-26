# Lemma: analytic-target-line

**Statement.** With `A` at the origin, `B=(b,0)`, `C=(u,v)`, `M=(b/2,0)`, `N=(u/2,v/2)`, and `O` the circumcentre of the non-degenerate `△AKL` (so `det(K,L)=kx·ly−ky·lx≠0`):
```
OM = ON  ⟺  O·(C−B) = (|C|²−|B|²)/4  ⟺  Q(kx,ky,lx,ly)=0,
```
where the cleared target is
```
Q := 2·(|K|²·ly − |L|²·ky)·(u−b) + 2·(kx·|L|² − lx·|K|²)·v − det(K,L)·(|C|²−|B|²).
```

**Proof.** The circumcentre `O=(ox,oy)` of `△AKL` (with `A=0`) satisfies the perpendicular-bisector equations `2·O·K=|K|²`, `2·O·L=|L|²`. Cramer's rule (denominator `det(K,L)≠0`):
```
2·det(K,L)·ox = |K|²·ly − |L|²·ky,   2·det(K,L)·oy = kx·|L|² − lx·|K|².   (1)
```
Using `M=B/2`, `N=C/2`:
```
OM² − ON² = 2·O·(N−M) + |M|² − |N|² = O·(C−B) + (|B|²−|C|²)/4,
```
so `OM=ON ⟺ O·(C−B)=(|C|²−|B|²)/4`. Multiplying by `2·det(K,L)` (nonzero) and substituting (1) yields the cleared polynomial `Q` above. ∎

**Source.** `analytic-branch-cert` Section 2; re-verified in `analytic-resultant-cert` §2. Reviewer-certified round 2.
