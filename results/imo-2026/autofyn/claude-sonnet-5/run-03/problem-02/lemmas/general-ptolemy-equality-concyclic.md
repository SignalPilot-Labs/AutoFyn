## Lemma (Ptolemy equality ⟹ concyclic)
Let W, X, Y, Z be four pairwise distinct points in the plane, no three
collinear, viewed as complex numbers w, x, y, z. If
$$WY\cdot XZ = WX\cdot YZ + XY\cdot WZ,$$
then W, X, Y, Z are concyclic.

## Proof
The algebraic identity
$$(w-y)(x-z) = (w-x)(y-z) + (x-y)(w-z) \qquad (\star)$$
holds for all complex w,x,y,z (direct expansion; independently re-verified
by symbolic expansion, both sides equal $wx-wz-xy+yz$). Taking absolute
values and applying the triangle inequality $|u+v|\le|u|+|v|$ with
$u=(w-x)(y-z)$, $v=(x-y)(w-z)$ gives Ptolemy's inequality
$WY\cdot XZ \le WX\cdot YZ + XY\cdot WZ$ for **any** four points.

Equality forces $|u+v|=|u|+|v|$. Since $W\ne X$, $Y\ne Z$ (pairwise
distinct), $u\ne0$; likewise $v\ne0$ (using $X\ne Y$, $W\ne Z$). The
equality case of the triangle inequality for nonzero complex numbers is that
$v/u\in\mathbb R_{>0}$ (standard: $|u+v|^2=|u|^2+|v|^2+2\langle u,v\rangle
\le(|u|+|v|)^2$ by Cauchy–Schwarz, equality iff $u,v$ are positively
proportional). Write $v/u=t>0$. From $(\star)$,
$(w-y)(x-z)=u+v=u(1+t)$, so the cross ratio
$$\chi=\frac{(w-y)(x-z)}{(w-z)(x-y)}=\frac{u(1+t)}{-v}=-\frac{1+t}{t}\in\mathbb R.$$
By the standard cross-ratio criterion for concyclicity (four pairwise
distinct, not-three-collinear points are concyclic iff their cross ratio is
real — see the companion certified lemma
`cross-ratio-real-concyclic-criterion.md`), W, X, Y, Z are concyclic. ∎

## Notes
- Applying the theorem to a specific quadruple requires identifying the
  correct assignment of (W,X,Y,Z) to the four points so that the diagonal
  product WY·XZ matches the target's left-hand side and the two side
  products match the right-hand side's two terms — this bookkeeping is
  external to the lemma itself and must be redone per application.
- Removes the need for a separate synthetic "cyclic order" lemma:
  concyclicity does not depend on the order the four points are listed in.

## Source
Derived in `results/imo-2026-02/approaches/ptolemy-trig-identity.md`
(round 2). Independently re-verified by proof-reviewer (round 2): the
identity $(\star)$ checked by symbolic expansion (sympy), the triangle-
inequality equality-case argument and cross-ratio computation checked by
hand — no gap found.

## Status
Certified — general-purpose tool, reusable in any problem requiring a
Ptolemy-equality-based concyclicity proof, independent of the rest of this
approach.
