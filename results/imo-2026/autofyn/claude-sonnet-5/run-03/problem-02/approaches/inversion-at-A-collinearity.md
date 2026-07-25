## Status
partial

## Approaches tried

### Round 8 (this round) — new approach, built to the fail-fast checkpoint

**Setup (imported from `fixed-point-concyclic`, no new construction).** Place
$A=0$ in the complex plane (the standing convention of the whole population,
`lemmas/vector-reduction-OM-ON.md`). Let $Q$ be the fixed point of
`lemmas/amnq-concyclic-and-reduction.md` (reflection of $A$ in the
perpendicular bisector of $MN$), and let $K,L\in\mathbb C$ be the two
hypothesis-determined points, all distinct from $A=0$ (a standing
non-degeneracy assumption of the whole population — $K,L\ne A$ since $K,L$
lie on lines through $B,C$ distinct from $A$, and $Q\ne A$ outside the
already-resolved isosceles case, `lemmas/isosceles-case-symmetry.md`). The
shared reduction target of the population is: $A,K,L,Q$ concyclic $\implies$
$OM=ON$ (`lemmas/amnq-concyclic-and-reduction.md`), and `fixed-point-
concyclic` has reduced "$A,K,L,Q$ concyclic" to the single scalar condition
$\chi\in\mathbb R$ where
$$\chi = \chi(A,K,L,Q) = \frac{(A-L)(K-Q)}{(A-Q)(K-L)} = \frac{-L(K-Q)}{-Q(K-L)} = \frac{L(K-Q)}{Q(K-L)}$$
(using $A=0$; this is exactly the quantity called $\chi_{\text{direct}}$ in
`lemmas/bilinear-chi-cramer-formula.md`, and shown there to equal $-D_0/D_1$
in closed, radical-free form via Theorem 6/7's Cramer's-rule machinery).

**Step 1 — set up the inversion.** Let $\iota$ be the inversion centered at
$A=0$ with radius $1$, realized (for computational convenience) as the
holomorphic Möbius map $\iota(z) = 1/z$ on $\mathbb C\setminus\{0\}$. (This
differs from the literal geometric inversion $z\mapsto 1/\bar z$ by
post-composition with complex conjugation; since both concyclicity and
collinearity of a point triple are invariant under conjugation — conjugation
is a reflection, an isometry, hence preserves both generalized-circle
membership and the vanishing of the relevant determinant — the choice
between $1/z$ and $1/\bar z$ does not affect any conclusion below, and we use
$1/z$ throughout for cleaner algebra.) Define $K^*=1/K$, $L^*=1/L$,
$Q^*=1/Q$, all well defined by the non-degeneracy noted above.

**Step 2 — prove, from scratch, that $A,K,L,Q$ concyclic $\iff K^*,L^*,Q^*$
collinear.** ($A,K,L$ are never collinear — they are the vertices of the
triangle $AKL$ with circumcenter $O$, given non-degenerate throughout the
whole population — so "$A,K,L,Q$ concyclic" is unambiguous, not conflated
with the collinear alternative.) We give a direct algebraic proof, not a
citation of "inversion sends circles to lines" as a black box.

The general equation of a circle through the origin in $\mathbb C$ is
$$z\bar z + \bar p\,z + p\,\bar z = 0 \qquad (p\in\mathbb C,\ p\ne 0),$$
since this is $|z|^2 + 2\,\mathrm{Re}(\bar p z) = 0$, a circle of center
$-p$ and radius $|p|$ (any circle through $0$ has this center-radius shape
with $|{-p}|=|p|$ equal to the radius, so every such circle is captured, and
conversely every equation of this form with $p\ne0$ is a genuine circle
through $0$ of positive radius). $K,L$ determine $p$ uniquely (two real
linear equations $\bar p K+p\bar K=-K\bar K$, $\bar p L+p\bar L=-L\bar L$ in
the two real unknowns $\mathrm{Re}(p),\mathrm{Im}(p)$, solvable uniquely
whenever $K,L$ are not both real multiples of a common direction from $0$
together with $0$ itself — i.e. whenever $A=0,K,L$ are not collinear, which
holds by the non-degeneracy above).

A point $W\ne0$ lies on this circle iff $W\bar W+\bar pW+p\bar W=0$; dividing
by $W\bar W\ne0$,
$$1+\bar p\cdot\frac1{\bar W}+p\cdot\frac1W=0,\qquad\text{i.e.}\qquad
1+p\,W^*+\bar p\,\overline{W^*}=0,\qquad W^*:=1/W.$$
This is $p\,W^*+\bar p\,\overline{W^*}=-1$, i.e. $2\,\mathrm{Re}(p\,W^*)=-1$
— a genuine real-affine-linear equation in $W^*\in\mathbb C\cong\mathbb R^2$
(since $p\ne0$, this is not the trivial equation $0=-1$, and its solution
set is exactly a line, the set of points whose projection onto the direction
$p$ is the fixed value $-1/(2|p|)$).

Hence: $K,L,Q$ all lie on the circle through $A=0$ determined by $p$ $\iff$
$K^*,L^*,Q^*$ all lie on the line $\{w:2\,\mathrm{Re}(pw)=-1\}$ (same $p$).
Since $p$ is uniquely determined by $K,L$ (shown above) on both sides of the
equivalence — the circle through $A,K,L$ is unique, and so is the line
through $K^*,L^*$ (as $K^*\ne L^*$, since $K\ne L$) — this is precisely the
statement
$$A,K,L,Q\text{ concyclic} \iff K^*,L^*,Q^*\text{ collinear}.$$
This closes Step 2 rigorously, with no appeal to inversion theory as an
external black box: the whole equivalence is an elementary computation.
(Equivalently, in determinant form: three points $x,y,z\in\mathbb C$ are
collinear iff $\det\begin{pmatrix}x&\bar x&1\\y&\bar y&1\\z&\bar z&1\end{pmatrix}=0$,
which for $x=K^*,y=L^*,z=Q^*$ is algebraically the same vanishing condition
derived above, just packaged as a $3\times3$ determinant instead of a real
part; we do not need this repackaging separately since the derivation above
already produces the equivalent real-linear equation directly.)

**Step 3 — compute the collinearity condition explicitly and compare it to
the existing target.** Collinearity of $K^*,L^*,Q^*$ is equivalent to the
ratio
$$\rho := \frac{Q^*-K^*}{L^*-K^*}$$
being real (three points $x,y,z$ with $x\ne y$ are collinear iff
$(z-x)/(y-x)\in\mathbb R$ — elementary: this ratio is real iff $z-x$ and
$y-x$ point along the same line through $0$, iff $x,y,z$ are collinear).

We compute $\rho$ explicitly, substituting $K^*=1/K,L^*=1/L,Q^*=1/Q$:
$$Q^*-K^*=\frac1Q-\frac1K=\frac{K-Q}{QK},\qquad
L^*-K^*=\frac1L-\frac1K=\frac{K-L}{LK},$$
$$\rho=\frac{(K-Q)/(QK)}{(K-L)/(LK)}=\frac{K-Q}{QK}\cdot\frac{LK}{K-L}
=\frac{L(K-Q)}{Q(K-L)}.$$

This was independently re-verified symbolically (own `sympy` session, this
round): with $K,L,Q$ treated as free symbolic (formal, non-conjugate)
variables, `sympy.simplify` confirms
$$\rho \;-\; \chi \;=\; \frac{L(K-Q)}{Q(K-L)} \;-\; \frac{L(K-Q)}{Q(K-L)} \;=\;0$$
identically — i.e. $\rho$ and $\chi$ (as defined in the setup above, imported
verbatim from `fixed-point-concyclic`) are not merely numerically equal on
some sample or Möbius-equivalent up to a substitution: **they are the
identical rational function of $K,L,Q$**, term for term.

**Conclusion — the fail-fast trigger is met, honestly and unambiguously.**
The outline's own instruction (per `/tmp/round-8/proof-outliner.md` and
`/tmp/round-8/outline-reviewer.md`) was: abandon quickly if Step 5's
determinant does not visibly simplify relative to the existing realness
target, rather than re-deriving the same difficulty in new coordinates.
Step 3 shows something stronger than "does not simplify" — it shows the
**post-inversion collinearity condition is, symbol for symbol, the same
rational expression** as the cross-ratio $\chi$ already being worked with by
`fixed-point-concyclic`, which in turn (via the already-certified Theorem
6/7, `lemmas/bilinear-chi-cramer-formula.md`) equals $-D_0/D_1$ and reduces
(via the already-derived, certified factorization of
$\sigma(D_0)D_1-D_0\sigma(D_1)$, §6.4 of `fixed-point-concyclic.md`) to the
identical scalar condition $\mathrm{Rem}(h_1,h_2,h_3,B,\bar B,C,\bar C)=0$.

There is no algebraic distance whatsoever between "$K^*,L^*,Q^*$ collinear"
and "$\chi\in\mathbb R$": they are literally the same statement about the
same expression $\rho=\chi$, merely re-narrated in inverted-image language.
Passing to a determinant-of-homogeneous-coordinates packaging (Step 2's
parenthetical remark) does not change this, since that determinant reduces,
by the identical algebra of Step 2, to the same real-affine equation that
Step 3 already shows is $\rho\in\mathbb R\iff\chi\in\mathbb R$ with $\rho=\chi$
identically.

**Why this happens (a structural, not merely coincidental, explanation).**
This is not an accident of this particular problem's numbers: the proof of
`lemmas/cross-ratio-real-concyclic-criterion.md` already constructs, for the
general four-point cross ratio, a Möbius map $f$ sending three of the four
points to $0,1,\infty$ and testing whether the fourth lands in $\mathbb R$.
Choosing $A$ (rather than $L$) as the point sent to $\infty$ is exactly the
map $z\mapsto 1/z$ up to an affine post-composition (which does not affect
realness of the image of the fourth point, since affine maps with real
coefficients preserve $\mathbb R\cup\{\infty\}$ setwise, and any Möbius map
sending $A\mapsto\infty$ differs from $1/z$ only by such a post-composition
composed with a pre-translation, both of which cancel out of the specific
ratio $\rho=\chi$ computed above). In other words: "cross-ratio realness"
*is* "inverted-image collinearity" for a four-point configuration containing
the inversion's center as one of the four points — they are two names for
the same classical fact, not two different facts that happen to coincide
numerically here. The outline's own honest caveat ("not known to be easier
... classically equivalent formulations of the same fact") is hereby
confirmed to be not just plausible but **exactly and provably true**, with
the equivalence made fully explicit and symbolic rather than left as an
unverified worry.

**Fail-fast invoked.** Per the outline-reviewer's explicit instruction, this
approach is stopped here, honestly reported as a negative result: inversion
at $A$ does not produce a new or simpler target. It reproduces, verbatim, the
existing $\chi\in\mathbb R$ (equivalently $\mathrm{Rem}=0$) target already
under active investigation by `fixed-point-concyclic`, contributing no new
leverage on the population's central remaining gap. No further effort was
sunk into re-deriving `fixed-point-concyclic`'s open items (the Gröbner-basis
non-membership result, the numerical Rem≈0 evidence, etc.) in this new
language, since doing so would be exactly the "re-deriving the same
difficulty in new coordinates" the outline warned against.

## Current best

A complete, rigorous proof that "inversion at $A$, collinearity of
$K^*,L^*,Q^*$" is the **identical** algebraic condition (the same rational
function $\rho=\chi$ of $K,L,Q$, not merely an equivalent-in-difficulty
reformulation) as the cross-ratio realness condition $\chi\in\mathbb R$
already isolated by `fixed-point-concyclic`'s Theorem 6/7 and reduced there
to $\mathrm{Rem}(h_1,h_2,h_3,B,\bar B,C,\bar C)=0$. This is an honest,
completed negative result, established (not merely conjectured) this round:
the approach does not reduce the problem's difficulty and should not be
pursued further as an independent route. It does, however, retroactively
strengthen confidence in `fixed-point-concyclic`'s own formulation: since the
$\chi\in\mathbb R$ target is *provably* the unique natural "linearize
concyclicity through $A$" target (any inversion-at-$A$ approach collapses to
it), the population's open gap ($\mathrm{Rem}=0$) is confirmed to be the
essentially unique bottleneck of this entire family of routes, not an
artifact of one particular choice of algebraic packaging. The remaining gap
for the whole problem is therefore exactly `fixed-point-concyclic`'s open
item: proving $\mathrm{Rem}(h_1,h_2,h_3,B,\bar B,C,\bar C)=0$ on the true
geometric (positivity/branch-selected) locus, which this approach does not
attempt to close (that task belongs to `fixed-point-concyclic`, not to this
now-exhausted reformulation).

## Full proof
Not applicable — Status is `partial` (this approach establishes a rigorous
equivalence/negative result about a reformulation, not a proof of the
problem's conclusion $OM=ON$).

## Promotable lemmas

**Lemma (concyclic-through-a-point ⟺ inverted images collinear, with
explicit closed form).** Let $A,K,L,Q\in\mathbb C$ with $A,K,L$ not
collinear and $K,L,Q\ne A$. Placing $A=0$ WLOG (translate), define
$K^*=1/K,L^*=1/L,Q^*=1/Q$. Then $A,K,L,Q$ are concyclic iff $K^*,L^*,Q^*$
are collinear, and moreover the collinearity ratio equals the cross ratio
exactly:
$$\frac{Q^*-K^*}{L^*-K^*} = \frac{(A-L)(K-Q)}{(A-Q)(K-L)} = \chi(A,K,L,Q).$$
Proved in full above (Steps 2–3), independent of any specific geometric
configuration — a general fact about four points in the plane, one of which
is the inversion pole. Reusable by any future approach considering an
inversion-based reformulation of a concyclicity-through-a-fixed-point
target: it shows in advance that such a reformulation adds no new
information beyond the cross-ratio-realness form already covered by
`lemmas/cross-ratio-real-concyclic-criterion.md`, and pins down the exact
identity ($\rho=\chi$, not just $\rho\Leftrightarrow\chi$) so this need not
be re-derived. Not filed as a separate `lemmas/` entry since it is a direct,
easily-restated corollary of the already-certified
`lemmas/cross-ratio-real-concyclic-criterion.md` (choosing the base point of
that lemma's Möbius map to be the inversion pole) — the reviewer may
certify it as a short addendum/corollary to that existing lemma file if
useful for future search, rather than as a wholly new file.
