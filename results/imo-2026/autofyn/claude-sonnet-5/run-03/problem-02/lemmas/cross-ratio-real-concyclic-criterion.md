## Lemma (Real cross ratio ⟺ concyclic or collinear)
For four points $z_1,z_2,z_3,z_4\in\mathbb C$, no three collinear, define
$$\chi(z_1,z_2,z_3,z_4) := \frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)}.$$
Then $z_1,z_2,z_3,z_4$ are concyclic **or** collinear iff $\chi\in\mathbb R$.

## Proof
The map $f(z) = \dfrac{z-z_3}{z-z_4}\cdot\dfrac{z_2-z_4}{z_2-z_3}$ is a
Möbius transformation (composition of a translation, a reciprocal, and
scalings — each of which sends the set of generalized circles, i.e. circles
and lines, to itself: this is the standard fact that $1/z$ sends
circles/lines through 0 to lines and circles/lines avoiding 0 to circles,
computed directly from $w=1/z=\bar z/|z|^2$; affine maps preserve circles
and lines trivially). By construction $f(z_3)=0$, $f(z_4)=\infty$,
$f(z_2)=1$. Since $0,1,\infty\in\mathbb R\cup\{\infty\}$ (a generalized
circle) and $f$ is a bijection of the extended plane sending generalized
circles to generalized circles, the unique generalized circle through
$z_2,z_3,z_4$ is sent by $f$ exactly onto $\mathbb R\cup\{\infty\}$. Hence
$z_1$ lies on that generalized circle iff $f(z_1)=\chi(z_1,z_2,z_3,z_4)\in
\mathbb R\cup\{\infty\}$, i.e. (since $z_1\ne z_4$, so $f(z_1)\ne\infty$)
iff $\chi\in\mathbb R$. ∎

## Notes
- Standard tool (cross-ratio / Möbius geometry); stated and proved here in
  full so it can be cited by name without external reference.
- To conclude concyclic (not merely concyclic-or-collinear) in an
  application, the collinear alternative must be excluded separately
  (e.g. by a nondegeneracy argument specific to the configuration).

## Addendum (round 8): inversion at one of the four points reproduces the
identical cross-ratio, not merely an equivalent reformulation
Let `z_1=A` and place `A=0` (WLOG, by translation). Let `K^*:=1/K,L^*:=1/L,
Q^*:=1/Q` be the images of `z_2=K,z_3=L,z_4=Q` under inversion `z\mapsto1/z`
centered at `A`. Then `A,K,L,Q` concyclic (or collinear) `\iff K^*,L^*,Q^*`
collinear, and moreover the ratio realizing that collinearity is **exactly**
the cross ratio above:
$$\rho:=\frac{Q^*-K^*}{L^*-K^*} = \chi(A,K,L,Q) = \frac{L(K-Q)}{Q(K-L)}
\qquad(\text{using }A=0).$$
*Proof.* `Q^*-K^*=1/Q-1/K=(K-Q)/(QK)`, `L^*-K^*=1/L-1/K=(K-L)/(LK)`, so
`\rho=[(K-Q)/(QK)]/[(K-L)/(LK)]=L(K-Q)/(Q(K-L))`, which is exactly
`\chi(A,K,L,Q)` with `A=0` (direct substitution into the cross-ratio
definition above: `(z_1-z_3)(z_2-z_4)/[(z_1-z_4)(z_2-z_3)]` with
`z_1=A=0,z_2=K,z_3=L,z_4=Q` gives `(-L)(K-Q)/[(-Q)(K-L)]=L(K-Q)/(Q(K-L))`).
Both sides are the identical rational function of `K,L,Q` — not merely
proportional or Möbius-equivalent — so choosing to invert at one of the
four points and test collinearity of the images adds **no** new algebraic
leverage over directly testing `\chi\in\mathbb R`: it is a re-narration of
the same target, term for term.
**Consequence for search strategy**: any future approach considering
"invert at a distinguished point, then test collinearity" for a
concyclicity-through-that-point target should expect this identity to hold
in general (not just for this problem's specific points), since the
Möbius map used in the main proof above, restricted to sending the
inversion pole to `\infty`, differs from `z\mapsto1/z` only by an affine
post-composition that does not change realness of the image of the fourth
point.

## Independent verification (addendum)
Independently re-verified by proof-reviewer (round 8): `sympy.simplify(rho -
chi)` with `K,L,Q` as free symbols gives `0` — confirmed as a literal
algebraic identity, not merely a numerical coincidence. No gap found.

## Source
Derived and proved in full in
`results/imo-2026-02/approaches/fixed-point-concyclic.md` (round 2, Step 3).
Independently re-verified by proof-reviewer (round 2): the Möbius-map
argument is the standard textbook proof and contains no gap.

## Status
Certified — general-purpose tool, reusable for any geometry problem
requiring a complex-number concyclicity criterion.
