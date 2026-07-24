# O-free reformulation of a "circumcenter dot direction" target

**Statement.** Let A, K, L be non-collinear points with circumcenter O, and
let B, C be any two further points. Write `det(u,v) = u_x v_y − u_y v_x` and
`D = det(K−A, L−A) ≠ 0` (nonzero since A,K,L non-collinear). Define
```
α = det(C−B, L−A)/D,   β = det(K−A, C−B)/D
```
(the unique scalars with `C − B = α(K−A) + β(L−A)`). Then
```
O·(C−B) = ½·[α(|K|² − |A|²) + β(|L|² − |A|²)].
```

**Proof.** Since O is the circumcenter of A,K,L: `|O−A|² = |O−K|²` expands
to `2O·(K−A) = |K|² − |A|²`; likewise `2O·(L−A) = |L|² − |A|²`. Since
`K−A, L−A` are linearly independent (A,K,L non-collinear), they form a basis
and Cramer's rule gives the stated α, β with `C−B = α(K−A)+β(L−A)`
uniquely. By linearity of the dot product,
`O·(C−B) = αO·(K−A) + βO·(L−A) = ½[α(|K|²−|A|²) + β(|L|²−|A|²)]`. ∎

**Status.** Fully proved, general vector-geometry fact independent of this
problem's specific hypotheses (i)-(iii). Verified by inspection (elementary
linear algebra, no computational check needed beyond the derivation itself).
Certified for shared reuse — replaces a rational (division-heavy)
circumcenter coordinate formula with a linear expression in K, L when the
target is "P·(C−B) = const" for P a circumcenter.
