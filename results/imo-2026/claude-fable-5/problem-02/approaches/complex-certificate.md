# Approach: complex-certificate

## Status
solved

## Approaches tried
- (round 1, outline) Raw complex encoding H₁ = H₂ = 0 via Im(·) = 0 — **abandoned before
  building**, per outline-reviewer: plain ideal membership over the Im-variety is FALSE
  (mirror components on which OM ≠ ON). Recorded so no one retries it.
- (round 1, build) **Branch-pinned trig-resolved encoding + explicit polynomial
  certificate** — **worked.** All configuration hypotheses are consumed in deriving two
  polynomial relations ℓ_K = 0, ℓ_L = 0 (one per side) by law-of-sines bookkeeping in
  genuine triangles (every angle an angle of an actual triangle, so every sine is
  positive and no mod-π ambiguity ever arises); the goal then follows from an
  **unconditional algebraic identity** 2 sin A · G = α·ℓ_K + β·ℓ_L, displayed in full and
  verified by three coefficient identities, each checked line by line by product-to-sum
  tables. Numeric validation of the whole chain: `/tmp/round-1/scratch/build_cc_1.py`
  (valid configuration reconstructed from scratch, all five hypothesis conditions and
  OM = ON confirmed to 1e-13); symbolic verification of every displayed identity:
  `/tmp/round-1/scratch/build_cc_2.py`, `build_cc_5.py`–`build_cc_10.py`.

## Current best
Complete proof below. No open gaps.

## Full proof

**Problem.** Let $ABC$ be a triangle, $M$, $N$ the midpoints of $AB$, $AC$. Points $K$,
$L$ are chosen inside triangles $BMC$, $BNC$ respectively, such that $K$ lies inside
angle $LBA$, $L$ lies inside angle $ACK$, and
$$\angle KBA = \angle ACL,\qquad \angle LBK = \angle LNC,\qquad \angle LCK = \angle BMK.$$
Let $O$ be the circumcentre of triangle $AKL$. Prove $OM = ON$.

Throughout, $b = CA$, $c = AB$, $A$ also denotes the angle $\angle BAC \in (0,\pi)$, and
all named angles are **unsigned angles in $(0,\pi)$** (as in the problem statement). Set
$$\varphi := \angle KBA = \angle ACL,\qquad
\psi := \angle LBK = \angle LNC,\qquad
\chi := \angle LCK = \angle BMK,$$
$$u := \angle KAB, \qquad v := \angle LAC .$$

The proof has six parts:

- **Part 0** — configuration facts (all interiority hypotheses are consumed here);
- **Part 1** — the unconditional reduction $OM = ON \iff OB^2 - OC^2 = \tfrac{c^2-b^2}{2}$;
- **Part 2** — the law-of-sines encoding of the hypotheses;
- **Part 3** — elimination of $\chi$ and $\psi$: the two side-relations $\ell_K = 0$, $\ell_L = 0$;
- **Part 4** — $A$, $K$, $L$ are not collinear;
- **Part 5** — coordinates, the circumcentre, and the reduction of the goal to one trig polynomial $G = 0$;
- **Part 6** — the certificate: the identity $2\sin A\cdot G = \alpha\,\ell_K + \beta\,\ell_L$, verified in full.

---

### Part 0. Configuration facts

**(0a) $K, L$ lie in the interior of triangle $ABC$.**
Since $B, M, C$ lie in the (convex) closed triangle $ABC$, the closed triangle $BMC$ is
contained in the closed triangle $ABC$. The boundary of $ABC$ is contained in the three
lines $AB$, $BC$, $CA$. The open triangle $\mathrm{int}(BMC)$ is disjoint from line
$AB$ (which contains its edge $BM$: the interior of a triangle lies strictly on one side
of each edge line) and from line $BC$ (its edge $BC$). Finally, the closed triangle
$BMC$ meets line $CA$ only in the single point $C$: the vertices $B$ and $M$ lie
strictly on the same side of line $CA$ (every point of segment $AB$ other than $A$
does), so by convexity any point of triangle $BMC$ on line $CA$ lies on the edge...
more directly: a point of the convex hull of $\{B, M, C\}$ lying on line $CA$ must have
zero total weight on $B$ and $M$ (their signed distances to the line have the same
strict sign), hence equals $C$. Since the vertex $C$ is not an interior point,
$\mathrm{int}(BMC)$ is disjoint from all three lines, hence from $\partial(ABC)$, so
$\mathrm{int}(BMC)\subseteq \mathrm{int}(ABC)$. Thus $K \in \mathrm{int}(ABC)$.
The same argument with $N$ in place of $M$ (edge $NC$ on line $CA$, edge $BC$ on line
$BC$, and triangle $BNC$ meeting line $AB$ only at $B$) gives
$\mathrm{int}(BNC) \subseteq \mathrm{int}(ABC)$, so $L \in \mathrm{int}(ABC)$.

**(0b) Basic angle facts.** Since $K \in \mathrm{int}(ABC)$, $K$ lies on none of the
lines $AB$, $BC$, $CA$; likewise $L$. By the crossbar theorem, for an interior point $K$
the ray $AK$ meets segment $BC$, hence lies strictly inside angle $BAC$, so
$$\angle BAC = \angle BAK + \angle KAC, \qquad\text{i.e.}\qquad 0 < u < A,\quad \angle KAC = A - u > 0,$$
and likewise $0 < v < A$, $\angle LAB = A - v$. Similarly $0 < \varphi = \angle KBA < \angle B$
(interior point seen from vertex $B$) and $0 < \varphi = \angle ACL < \angle C$; in
particular $\varphi \in (0,\pi)$ and $\sin\varphi > 0$. Since $K \notin$ line $AB$ and
$M \in$ line $AB$ with $M \ne K$, the angle $\chi = \angle BMK$ is a genuine angle in
$(0,\pi)$, so $\sin\chi > 0$ and $\chi > 0$; likewise $\psi = \angle LNC \in (0,\pi)$,
$\psi > 0$.

**(0c) Ray identifications at the midpoints.** $M$ is the midpoint of $AB$, so $M$ lies
strictly between $B$ and $A$; hence ray $BM$ = ray $BA$ and
$\angle KBM = \angle KBA = \varphi$. Likewise $N$ lies strictly between $C$ and $A$, so
ray $CN$ = ray $CA$ and $\angle LCN = \angle LCA = \varphi$.

**(0d) Angle additivity from the two interiority hypotheses.** "$K$ lies inside angle
$LBA$" means ray $BK$ lies strictly inside angle $LBA$, so
$$\angle ABL = \angle ABK + \angle KBL = \varphi + \psi .$$
"$L$ lies inside angle $ACK$" means ray $CL$ lies strictly inside angle $ACK$, so
$$\angle ACK = \angle ACL + \angle LCK = \varphi + \chi .$$
*These two lines and the positivity facts of (0b) are the only places the interiority
hypotheses are used; everything after this point is unconditional algebra on genuine
triangles.*

---

### Part 1. Reduction: $OM = ON \iff OB^2 - OC^2 = \tfrac{c^2 - b^2}{2}$

**Median-length formula.** For any points $O, P, Q$ with $S$ the midpoint of $PQ$:
writing vectors from $O$, $\;4\,OS^2 = |\,\vec{OP}+\vec{OQ}\,|^2 = OP^2 + OQ^2 + 2\,\vec{OP}\cdot\vec{OQ}$
and $PQ^2 = OP^2 + OQ^2 - 2\,\vec{OP}\cdot\vec{OQ}$; adding,
$4\,OS^2 = 2\,OP^2 + 2\,OQ^2 - PQ^2$.

Applying this to $S = M$ (midpoint of $AB$) and $S = N$ (midpoint of $AC$):
$$4\,OM^2 = 2\,OA^2 + 2\,OB^2 - c^2, \qquad 4\,ON^2 = 2\,OA^2 + 2\,OC^2 - b^2 .$$
Subtracting, $4(OM^2 - ON^2) = 2(OB^2 - OC^2) - (c^2 - b^2)$. Hence
$$OM = ON \iff OB^2 - OC^2 = \frac{c^2 - b^2}{2}. \tag{1}$$
(This step is unconditional; it does not even use that $O$ is the circumcentre.)

---

### Part 2. The hypotheses as law-of-sines relations

Each relation below is the law of sines in a genuine (nondegenerate) triangle; by (0b),
$K \notin$ lines $AB, CA$ and $L \notin$ lines $AB, CA$, so all six triangles used are
nondegenerate, all their angles lie in $(0,\pi)$, and every sine below is **positive**.
When a triangle has angles $\theta_1, \theta_2$ at two vertices, the sine of the third
angle is $\sin(\pi - \theta_1 - \theta_2) = \sin(\theta_1 + \theta_2)$.

**Triangle $ABK$** (angles $u$ at $A$, $\varphi$ at $B$):
$$AK = \frac{c\,\sin\varphi}{\sin(\varphi + u)}, \qquad
BK = \frac{c\,\sin u}{\sin(\varphi + u)}. \tag{E1}$$

**Triangle $MBK$** (angles $\varphi$ at $B$ by (0c), $\chi$ at $M$; $MB = c/2$):
$$BK = \frac{(c/2)\,\sin\chi}{\sin(\varphi + \chi)}. \tag{E3'}$$
Equating the two expressions for $BK$ and clearing the (positive) denominators:
$$2\,\sin u\,\sin(\varphi + \chi) = \sin\chi\,\sin(\varphi + u). \tag{E3}$$

**Triangle $ACK$** (angles $A - u$ at $A$ by (0b), $\varphi + \chi$ at $C$ by (0d)):
$$AK = \frac{b\,\sin(\varphi + \chi)}{\sin(\varphi + \chi + A - u)}. \tag{E5}$$

**Triangle $ACL$** (angles $v$ at $A$, $\varphi$ at $C$):
$$AL = \frac{b\,\sin\varphi}{\sin(\varphi + v)}, \qquad
CL = \frac{b\,\sin v}{\sin(\varphi + v)}. \tag{E2}$$

**Triangle $NCL$** (angles $\varphi$ at $C$ by (0c), $\psi$ at $N$; $NC = b/2$):
equating with (E2)'s $CL$:
$$2\,\sin v\,\sin(\varphi + \psi) = \sin\psi\,\sin(\varphi + v). \tag{E4}$$

**Triangle $ABL$** (angles $A - v$ at $A$, $\varphi + \psi$ at $B$ by (0d)):
$$AL = \frac{c\,\sin(\varphi + \psi)}{\sin(\varphi + \psi + A - v)}. \tag{E6}$$

---

### Part 3. Eliminating $\chi$ and $\psi$: the side relations

**K-side.** From (E3), expanding $\sin(\varphi+\chi) = \sin\varphi\cos\chi + \cos\varphi\sin\chi$
and using $\sin(\varphi+u) - 2\sin u\cos\varphi = \sin\varphi\cos u - \cos\varphi\sin u = \sin(\varphi - u)$:
$$\sin\chi\,\sin(\varphi - u) = 2\,\sin u\,\sin\varphi\,\cos\chi .$$
Since $\sin\chi > 0$ and $2\sin u \sin\varphi > 0$ (Part 0), we may write
$$(\cos\chi,\ \sin\chi) = r\,\bigl(\sin(\varphi - u),\ 2\sin u \sin\varphi\bigr),
\qquad r := \frac{\sin\chi}{2\sin u\,\sin\varphi} > 0. \tag{2}$$
(No branch ambiguity: $\sin \chi>0$ pins the sign of $r$, and $(2)$ reproduces both
$\cos\chi$ and $\sin\chi$ exactly.) Consequently
$$\sin(\varphi + \chi) = \sin\varphi\cos\chi + \cos\varphi\sin\chi
= r\,\sin\varphi\,\bigl[\sin(\varphi - u) + 2\sin u\cos\varphi\bigr]
= r\,\sin\varphi\,\sin(\varphi + u), \tag{3}$$
$$\cos(\varphi + \chi) = \cos\varphi\cos\chi - \sin\varphi\sin\chi
= r\,\bigl[\cos\varphi\,\sin(\varphi - u) - 2\sin u\,\sin^2\varphi\bigr]. \tag{4}$$

Now equate (E1) and (E5) (both equal $AK$) and clear denominators:
$$c\,\sin\varphi\,\sin(\varphi + \chi + A - u) = b\,\sin(\varphi + \chi)\,\sin(\varphi + u).$$
Expand $\sin(\varphi+\chi+A-u) = \sin(\varphi+\chi)\cos(A-u) + \cos(\varphi+\chi)\sin(A-u)$
and substitute (3), (4); every term acquires the factor $r$, and dividing by
$r\,\sin\varphi > 0$ leaves
$$c\,\Bigl[\sin\varphi\,\sin(\varphi+u)\cos(A-u) + \cos\varphi\,\sin(\varphi-u)\sin(A-u)
- 2\sin^2\!\varphi\,\sin u\,\sin(A-u)\Bigr] = b\,\sin^2(\varphi+u). \tag{5}$$

**Bracket identity.** The bracket in (5) equals $\cos A - \cos(\varphi+u)\cos(A+\varphi-u)$.
*Verification by product-to-sum (each row is the standard expansion
$2\sin X\sin Y = \cos(X-Y)-\cos(X+Y)$, $2\sin X\cos Y = \sin(X+Y)+\sin(X-Y)$,
$2\cos X\cos Y = \cos(X-Y)+\cos(X+Y)$, applied twice); we list the five summands of
(bracket) $-\ \bigl[\cos A - \cos(\varphi+u)\cos(A+\varphi-u)\bigr]$ in Fourier form:*

| term | Fourier expansion |
|---|---|
| $\sin\varphi\,\sin(\varphi{+}u)\cos(A{-}u)$ | $\tfrac14\cos A - \tfrac14\cos(A{+}2\varphi) + \tfrac14\cos(A{-}2u) - \tfrac14\cos(2\varphi{+}2u{-}A)$ |
| $\cos\varphi\,\sin(\varphi{-}u)\sin(A{-}u)$ | $\tfrac14\cos A + \tfrac14\cos(A{-}2\varphi) - \tfrac14\cos(A{-}2u) - \tfrac14\cos(A{+}2\varphi{-}2u)$ |
| $-2\sin^2\!\varphi\,\sin u\,\sin(A{-}u)$ | $\tfrac12\cos A - \tfrac14\cos(A{-}2\varphi) - \tfrac14\cos(A{+}2\varphi) - \tfrac12\cos(A{-}2u) + \tfrac14\cos(2\varphi{+}2u{-}A) + \tfrac14\cos(A{+}2\varphi{-}2u)$ |
| $-\cos A$ | $-\cos A$ |
| $+\cos(\varphi{+}u)\cos(A{+}\varphi{-}u)$ | $\tfrac12\cos(A{+}2\varphi) + \tfrac12\cos(A{-}2u)$ |

Summing each column of Fourier modes gives $0$ (e.g. the $\cos A$ modes:
$\tfrac14+\tfrac14+\tfrac12-1 = 0$; the $\cos(A{+}2\varphi)$ modes:
$-\tfrac14-\tfrac14+\tfrac12 = 0$; the $\cos(A{-}2u)$ modes:
$\tfrac14-\tfrac14-\tfrac12+\tfrac12=0$; the $\cos(2\varphi{+}2u{-}A)$ modes:
$-\tfrac14+\tfrac14 = 0$; the $\cos(A{-}2\varphi)$ modes: $\tfrac14 - \tfrac14 = 0$;
the $\cos(A{+}2\varphi{-}2u)$ modes: $-\tfrac14+\tfrac14 = 0$). ∎ (bracket identity)

Therefore, defining
$$P_u := \cos A - \cos(\varphi+u)\cos(A+\varphi-u), \qquad Q_u := \sin^2(\varphi+u),$$
equation (5) becomes the **K-side relation**
$$\boxed{\ \ell_K := b\,Q_u - c\,P_u = 0.\ } \tag{K}$$

**L-side.** The L-side computation is *literally the same computation* with the
substitutions $u \to v$, $\chi \to \psi$, $b \leftrightarrow c$: (E4) has the same shape
as (E3), and equating (E2) with (E6) has the same shape as equating (E1) with (E5) with
$b$ and $c$ exchanged. Hence, with
$$P_v := \cos A - \cos(\varphi+v)\cos(A+\varphi-v), \qquad Q_v := \sin^2(\varphi+v),$$
$$\boxed{\ \ell_L := c\,Q_v - b\,P_v = 0.\ } \tag{L}$$

---

### Part 4. $A$, $K$, $L$ are not collinear

Suppose, for contradiction, that $A, K, L$ are collinear. Since $K, L \in \mathrm{int}(ABC)$
and $K, L \neq A$, both lie on one ray $\ell$ from $A$ through the interior of the
triangle; write $\ell = \{A + t\,\hat\ell : t > 0\}$ and $K = A + t_K\hat\ell$,
$L = A + t_L\hat\ell$ with $t_K, t_L > 0$.

**Monotonicity claim.** For $X(t) = A + t\hat\ell$ ($t>0$), the function
$t \mapsto \angle ABX(t)$ is strictly increasing, and so is $t \mapsto \angle ACX(t)$.

*Proof.* Take coordinates with $A$ at the origin and $B = (c, 0)$; since $\ell$ enters
the interior, $\hat\ell = (\cos\theta, \sin\theta)$ with $\sin\theta > 0$ (orient the
$C$-side up), where $\theta\in(0,A)$. The angle at $B$ between ray $BA$ (direction $(-1,0)$)
and ray $BX$ (direction $X(t) - B = (t\cos\theta - c,\ t\sin\theta)$) has
$$\cos\angle ABX = \frac{c - t\cos\theta}{|X-B|}, \qquad
\sin\angle ABX = \frac{t\sin\theta}{|X-B|} > 0,$$
so
$$\cot\angle ABX = \frac{c - t\cos\theta}{t\,\sin\theta}
= \frac{1}{\sin\theta}\Bigl(\frac{c}{t} - \cos\theta\Bigr),$$
which is strictly decreasing in $t$; since $\cot$ is strictly decreasing on $(0,\pi)$,
$\angle ABX(t)$ is strictly increasing. The statement at $C$ is the same computation in
coordinates with $A$ at the origin and $C$ on the positive axis of the frame: there
$\hat\ell$ makes angle $\theta' = A - \theta \in (0, A)$ with ray $AC$, $\sin\theta' > 0$,
and $\cot\angle ACX = \frac{1}{\sin\theta'}\bigl(\frac{b}{t} - \cos\theta'\bigr)$,
strictly decreasing. ∎

Now, by (0d) and (0b), $\angle ABL = \varphi + \psi > \varphi = \angle ABK$ (as $\psi > 0$),
so by the claim applied at $B$: $t_L > t_K$. But also
$\angle ACK = \varphi + \chi > \varphi = \angle ACL$ (as $\chi > 0$), so by the claim
applied at $C$: $t_K > t_L$. Contradiction. Hence $A, K, L$ are not collinear, and the
circumcircle $\omega$ and circumcentre $O$ of triangle $AKL$ exist and are unique. ∎

**Consequence.** The rays $AK$ and $AL$ are distinct. Ray $AK$ makes angle $u$ with ray
$AB$; ray $AL$ makes angle $A - v$ with ray $AB$; both $u, A-v \in (0, A)$. Distinctness
means $u \neq A - v$; since $|(A - v) - u| < A < \pi$,
$$\sin(A - u - v) \neq 0. \tag{6}$$

---

### Part 5. Coordinates, the circumcentre, and the goal polynomial $G$

Place $A = (0,0)$, $B = (c, 0)$, $C = (b\cos A,\ b\sin A)$ (so $C$ is in the upper half
plane; $K$ and $L$, being interior, are as well). By Part 0,
$$K = AK\,(\cos u,\ \sin u), \qquad L = AL\,\bigl(\cos(A-v),\ \sin(A-v)\bigr).$$

Since $A = 0 \in \omega$, the circle $\omega$ has equation $|z|^2 = 2\langle O, z\rangle$
($z \in \mathbb{R}^2$), and for any point $P$,
$$\mathrm{pow}(P, \omega) = |P - O|^2 - |O|^2 = |P|^2 - 2\langle O, P\rangle .$$
With $R_\omega = OA = |O|$, we get $OB^2 - OC^2 = \mathrm{pow}(B,\omega) - \mathrm{pow}(C,\omega)
= (c^2 - b^2) - 2\langle O,\ B - C\rangle$. By (1),
$$OM = ON \iff 2\,\langle O,\ B - C\rangle = \frac{c^2 - b^2}{2}. \tag{7}$$

Write $(X, Y) := 2O$. Since $K, L \in \omega$: $|K|^2 = 2\langle O, K\rangle$ and
$|L|^2 = 2\langle O, L\rangle$; dividing by $AK > 0$ resp. $AL > 0$:
$$X\cos u + Y \sin u = AK, \qquad X\cos(A-v) + Y\sin(A-v) = AL. \tag{8}$$
The determinant of this linear system is
$\cos u\,\sin(A-v) - \sin u\,\cos(A-v) = \sin(A - u - v) \ne 0$ by (6), so Cramer's rule gives
$$X = \frac{AK\,\sin(A-v) - AL\,\sin u}{\sin(A-u-v)}, \qquad
Y = \frac{AL\,\cos u - AK\,\cos(A-v)}{\sin(A-u-v)}.$$

Since $B - C = (c - b\cos A,\ -b\sin A)$, condition (7) reads
$X(c - b\cos A) - Y\, b \sin A = \tfrac{c^2-b^2}{2}$, i.e.
$$AK\bigl[(c - b\cos A)\sin(A-v) + b\sin A\cos(A-v)\bigr]
- AL\bigl[(c - b\cos A)\sin u + b \sin A\cos u\bigr]
= \frac{c^2-b^2}{2}\,\sin(A-u-v).$$
Using $\sin A\cos(A-v) - \cos A\sin(A-v) = \sin v$ and
$\sin A \cos u - \cos A \sin u = \sin(A - u)$, the brackets simplify:
$$(c - b\cos A)\sin(A-v) + b \sin A \cos(A - v) = c\,\sin(A - v) + b\,\sin v,$$
$$(c - b\cos A)\sin u + b\sin A \cos u = c\,\sin u + b\,\sin(A - u).$$
So (7) is equivalent to
$$AK\,\bigl[c\sin(A-v) + b\sin v\bigr] - AL\,\bigl[c\sin u + b\sin(A-u)\bigr]
= \frac{c^2-b^2}{2}\,\sin(A-u-v). \tag{G0}$$

Finally substitute $AK = \dfrac{c\sin\varphi}{\sin(\varphi+u)}$,
$AL = \dfrac{b\sin\varphi}{\sin(\varphi+v)}$ from (E1), (E2) and multiply by
$\sin(\varphi+u)\sin(\varphi+v) > 0$: **(G0), hence $OM = ON$, is equivalent to $G = 0$,**
where
$$G := c\,\sin\varphi\,\sin(\varphi+v)\bigl[c\sin(A-v) + b\sin v\bigr]
- b\,\sin\varphi\,\sin(\varphi+u)\bigl[c\sin u + b\sin(A-u)\bigr]
- \frac{c^2-b^2}{2}\,\sin(A-u-v)\,\sin(\varphi+u)\,\sin(\varphi+v). \tag{9}$$

---

### Part 6. The certificate

**Claim (certificate identity).** With $P_u, Q_u, P_v, Q_v, \ell_K, \ell_L$ as in
Part 3 and $G$ as in (9), the following holds **identically in the six free real
variables $u, v, \varphi, A, b, c$** (no constraints assumed):
$$2\,\sin A\cdot G \;=\; \alpha\,\ell_K \;+\; \beta\,\ell_L, \tag{10}$$
where
$$\alpha := -\Bigl[\,b\,(\sin^2\varphi + \sin^2 v) + c\,\sin(\varphi+v)\,\sin(A - \varphi - v)\,\Bigr],$$
$$\beta := \;\;\;\, c\,(\sin^2\varphi + \sin^2 u) + b\,\sin(\varphi+u)\,\sin(A - \varphi - u).$$

**Why the claim finishes the proof.** By Part 3, the hypotheses force
$\ell_K = \ell_L = 0$. Hence $2\sin A \cdot G = 0$; since $A \in (0,\pi)$ is an angle of
triangle $ABC$, $\sin A \neq 0$, so $G = 0$; by Part 5 this is equivalent to (7), and by
Part 1 to $OM = ON$. $\blacksquare$ (modulo the claim)

**Proof of the claim.** Both sides of (10) are quadratic forms in $(b, c)$ whose
coefficients are trigonometric polynomials in $(u, v, \varphi, A)$; it suffices to match
the coefficients of $b^2$, $bc$, $c^2$. Collecting them from (9) and from
$\alpha \ell_K + \beta \ell_L$ (recall $\ell_K = b\,Q_u - c\,P_u$,
$\ell_L = c\,Q_v - b\,P_v$), the claim is equivalent to the three identities:

**(Id-$b^2$)** $\;2\sin A\Bigl[-\sin\varphi\,\sin(\varphi{+}u)\sin(A{-}u) + \tfrac12\sin(A{-}u{-}v)\sin(\varphi{+}u)\sin(\varphi{+}v)\Bigr]
= -(\sin^2\varphi + \sin^2 v)\,\sin^2(\varphi{+}u) - \sin(\varphi{+}u)\,\sin(A{-}\varphi{-}u)\,P_v .$

**(Id-$bc$)** $\;2\sin A\,\sin\varphi\bigl[\sin v\,\sin(\varphi{+}v) - \sin u\,\sin(\varphi{+}u)\bigr]
= (\sin^2\varphi + \sin^2 v)\,P_u - \sin(\varphi{+}v)\sin(A{-}\varphi{-}v)\,\sin^2(\varphi{+}u)
+ \sin(\varphi{+}u)\sin(A{-}\varphi{-}u)\,\sin^2(\varphi{+}v) - (\sin^2\varphi + \sin^2 u)\,P_v .$

**(Id-$c^2$)** $\;2\sin A\Bigl[\sin\varphi\,\sin(\varphi{+}v)\sin(A{-}v) - \tfrac12\sin(A{-}u{-}v)\sin(\varphi{+}u)\sin(\varphi{+}v)\Bigr]
= \sin(\varphi{+}v)\,\sin(A{-}\varphi{-}v)\,P_u + (\sin^2\varphi + \sin^2 u)\,\sin^2(\varphi{+}v) .$

*(Bookkeeping check for the coefficient collection: e.g. the $b^2$-terms of
$\alpha\ell_K$ come from the $b$-part of $\alpha$ times the $b$-part of $\ell_K$:
$-(\sin^2\varphi+\sin^2v)\cdot Q_u$; those of $\beta\ell_L$ from
$b\sin(\varphi{+}u)\sin(A{-}\varphi{-}u)\cdot(-b\,P_v)$; similarly for $bc$ and $c^2$.)*

**(Id-$c^2$) follows from (Id-$b^2$).** Swap $u \leftrightarrow v$ in (Id-$b^2$) and
multiply by $-1$: the left side becomes
$2\sin A[\sin\varphi\sin(\varphi{+}v)\sin(A{-}v) - \tfrac12\sin(A{-}u{-}v)\sin(\varphi{+}u)\sin(\varphi{+}v)]$
(note $\sin(A{-}v{-}u) = \sin(A{-}u{-}v)$), and the right side becomes
$(\sin^2\varphi+\sin^2u)\sin^2(\varphi{+}v) + \sin(\varphi{+}v)\sin(A{-}\varphi{-}v)P_u$ —
exactly (Id-$c^2$). So only (Id-$b^2$) and (Id-$bc$) need verification.

**Verification of (Id-$b^2$).** Every term on both sides carries the factor
$\sin(\varphi+u)$ (for the $P_v$-term this is explicit; for the left side, both bracket
terms contain it). Dividing (Id-$b^2$) by it and moving everything to one side, it is
equivalent to $T_1 + T_2 + T_3 + T_4 + T_5 = 0$ with the Fourier (product-to-sum)
expansions:

| term | Fourier expansion |
|---|---|
| $T_1 = \sin A\,\sin(\varphi{+}v)\,\sin(A{-}u{-}v)$ | $\tfrac14\sin(\varphi{-}u) - \tfrac14\sin(2A{+}\varphi{-}u) + \tfrac14\sin(\varphi{+}u{+}2v) - \tfrac14\sin(\varphi{+}u{+}2v{-}2A)$ |
| $T_2 = -2\sin A\,\sin\varphi\,\sin(A{-}u)$ | $-\tfrac12\sin(\varphi{-}u) - \tfrac12\sin(\varphi{+}u) + \tfrac12\sin(\varphi{+}u{-}2A) + \tfrac12\sin(2A{+}\varphi{-}u)$ |
| $T_3 = (\sin^2\varphi + \sin^2 v)\,\sin(\varphi{+}u)$ | $\tfrac14\sin(\varphi{-}u) + \sin(\varphi{+}u) - \tfrac14\sin(3\varphi{+}u) - \tfrac14\sin(\varphi{+}u{-}2v) - \tfrac14\sin(\varphi{+}u{+}2v)$ |
| $T_4 = \sin(A{-}\varphi{-}u)\,\cos A$ | $-\tfrac12\sin(\varphi{+}u) - \tfrac12\sin(\varphi{+}u{-}2A)$ |
| $T_5 = -\sin(A{-}\varphi{-}u)\,\cos(\varphi{+}v)\,\cos(A{+}\varphi{-}v)$ | $\tfrac14\sin(3\varphi{+}u) - \tfrac14\sin(2A{+}\varphi{-}u) + \tfrac14\sin(\varphi{+}u{-}2v) + \tfrac14\sin(\varphi{+}u{+}2v{-}2A)$ |

*(Here $T_4 + T_5 = \sin(A-\varphi-u)\,P_v$ after sign transport; each row is two
applications of the standard product-to-sum formulas; note
$\sin(\varphi+u-2A) = -\sin(2A - \varphi - u)$ etc., all rows written with a consistent
sign convention $\sin(-X) = -\sin X$.)*

Column-wise cancellation of the Fourier modes:
$\sin(\varphi{-}u)$: $\tfrac14 - \tfrac12 + \tfrac14 = 0$;
$\sin(2A{+}\varphi{-}u)$: $-\tfrac14 + \tfrac12 - \tfrac14 = 0$;
$\sin(\varphi{+}u{+}2v)$: $\tfrac14 - \tfrac14 = 0$;
$\sin(\varphi{+}u{+}2v{-}2A)$: $-\tfrac14 + \tfrac14 = 0$;
$\sin(\varphi{+}u)$: $-\tfrac12 + 1 - \tfrac12 = 0$;
$\sin(\varphi{+}u{-}2A)$: $\tfrac12 - \tfrac12 = 0$;
$\sin(3\varphi{+}u)$: $-\tfrac14 + \tfrac14 = 0$;
$\sin(\varphi{+}u{-}2v)$: $-\tfrac14 + \tfrac14 = 0$.
All modes cancel, so (Id-$b^2$) holds. ∎

**Verification of (Id-$bc$).** Moving everything to one side, (Id-$bc$) is equivalent
to $S_1 + \cdots + S_6 = 0$ with:

| term | Fourier expansion |
|---|---|
| $S_1 = 2\sin A\sin\varphi\,\sin v\,\sin(\varphi{+}v)$ | $\tfrac14\cos(A{-}2\varphi) - \tfrac14\cos(A{+}2\varphi) + \tfrac14\cos(A{-}2v) - \tfrac14\cos(A{+}2v) - \tfrac14\cos(2\varphi{+}2v{-}A) + \tfrac14\cos(A{+}2\varphi{+}2v)$ |
| $S_2 = -2\sin A\sin\varphi\,\sin u\,\sin(\varphi{+}u)$ | $-\tfrac14\cos(A{-}2\varphi) + \tfrac14\cos(A{+}2\varphi) - \tfrac14\cos(A{-}2u) + \tfrac14\cos(A{+}2u) + \tfrac14\cos(2\varphi{+}2u{-}A) - \tfrac14\cos(A{+}2\varphi{+}2u)$ |
| $S_3 = -(\sin^2\varphi + \sin^2 v)\,P_u$ | $-\tfrac98\cos A + \tfrac14\cos(A{-}2\varphi) + \tfrac34\cos(A{+}2\varphi) - \tfrac18\cos(A{+}4\varphi) + \tfrac12\cos(A{-}2u) + \tfrac14\cos(A{-}2v) + \tfrac14\cos(A{+}2v) - \tfrac18\cos(2\varphi{+}2u{-}A) - \tfrac18\cos(2u{+}2v{-}A) - \tfrac18\cos(A{+}2\varphi{-}2u) - \tfrac18\cos(A{+}2\varphi{-}2v) - \tfrac18\cos(A{+}2\varphi{+}2v) - \tfrac18\cos(A{-}2u{+}2v)$ |
| $S_4 = \sin(\varphi{+}v)\sin(A{-}\varphi{-}v)\sin^2(\varphi{+}u)$ | $-\tfrac14\cos A + \tfrac18\cos(2\varphi{+}2u{-}A) + \tfrac14\cos(2\varphi{+}2v{-}A) + \tfrac18\cos(A{+}2\varphi{+}2u) - \tfrac18\cos(A{+}2u{-}2v) - \tfrac18\cos(4\varphi{+}2u{+}2v{-}A)$ |
| $S_5 = -\sin(\varphi{+}u)\sin(A{-}\varphi{-}u)\sin^2(\varphi{+}v)$ | $\tfrac14\cos A - \tfrac14\cos(2\varphi{+}2u{-}A) - \tfrac18\cos(2\varphi{+}2v{-}A) - \tfrac18\cos(A{+}2\varphi{+}2v) + \tfrac18\cos(A{-}2u{+}2v) + \tfrac18\cos(4\varphi{+}2u{+}2v{-}A)$ |
| $S_6 = (\sin^2\varphi + \sin^2 u)\,P_v$ | $\tfrac98\cos A - \tfrac14\cos(A{-}2\varphi) - \tfrac34\cos(A{+}2\varphi) + \tfrac18\cos(A{+}4\varphi) - \tfrac14\cos(A{-}2u) - \tfrac14\cos(A{+}2u) - \tfrac12\cos(A{-}2v) + \tfrac18\cos(2\varphi{+}2v{-}A) + \tfrac18\cos(2u{+}2v{-}A) + \tfrac18\cos(A{+}2\varphi{-}2u) + \tfrac18\cos(A{+}2\varphi{-}2v) + \tfrac18\cos(A{+}2\varphi{+}2u) + \tfrac18\cos(A{+}2u{-}2v)$ |

Column-wise cancellation of all Fourier modes (each mode listed with its total):
$\cos A$: $-\tfrac98 - \tfrac14 + \tfrac14 + \tfrac98 = 0$;
$\cos(A{-}2\varphi)$: $\tfrac14 - \tfrac14 + \tfrac14 - \tfrac14 = 0$;
$\cos(A{+}2\varphi)$: $-\tfrac14 + \tfrac14 + \tfrac34 - \tfrac34 = 0$;
$\cos(A{+}4\varphi)$: $-\tfrac18 + \tfrac18 = 0$;
$\cos(A{-}2u)$: $-\tfrac14 + \tfrac12 - \tfrac14 = 0$;
$\cos(A{+}2u)$: $\tfrac14 - \tfrac14 = 0$;
$\cos(A{-}2v)$: $\tfrac14 + \tfrac14 - \tfrac12 = 0$;
$\cos(A{+}2v)$: $-\tfrac14 + \tfrac14 = 0$;
$\cos(2\varphi{+}2u{-}A)$: $\tfrac14 - \tfrac18 + \tfrac18 - \tfrac14 = 0$;
$\cos(2\varphi{+}2v{-}A)$: $-\tfrac14 + \tfrac14 - \tfrac18 + \tfrac18 = 0$;
$\cos(A{+}2\varphi{+}2u)$: $-\tfrac14 + \tfrac18 + \tfrac18 = 0$;
$\cos(A{+}2\varphi{+}2v)$: $\tfrac14 - \tfrac18 - \tfrac18 = 0$;
$\cos(A{+}2\varphi{-}2u)$: $-\tfrac18 + \tfrac18 = 0$;
$\cos(A{+}2\varphi{-}2v)$: $-\tfrac18 + \tfrac18 = 0$;
$\cos(2u{+}2v{-}A)$: $-\tfrac18 + \tfrac18 = 0$;
$\cos(A{-}2u{+}2v)$: $-\tfrac18 + \tfrac18 = 0$;
$\cos(A{+}2u{-}2v)$: $-\tfrac18 + \tfrac18 = 0$;
$\cos(4\varphi{+}2u{+}2v{-}A)$: $-\tfrac18 + \tfrac18 = 0$.
All modes cancel, so (Id-$bc$) holds. ∎

This proves the certificate identity (10), and with it the theorem:

$$\boxed{OM = ON.}$$
$\blacksquare$

---

### Remarks on rigor and tooling

- **Named tools used:** law of sines (in six explicitly nondegenerate triangles), the
  median-length formula (proved inline in Part 1 by the parallelogram law / vector
  expansion), the crossbar theorem (Part 0b, for angle additivity at $A$), Cramer's rule
  (Part 5), and the standard product-to-sum identities (Parts 3 and 6). No knowledge-base
  entry is contradicted; the median-formula reduction matches the shared reduction
  recorded in `results/imo-2026-02/current.md`.
- **Where the configuration hypotheses are consumed:** entirely in Part 0 (interiority
  $\Rightarrow$ positivity of all sines and the two angle additivities
  $\angle ACK = \varphi + \chi$, $\angle ABL = \varphi + \psi$) and Part 4 (strictness
  $\chi, \psi > 0$ for non-collinearity). After Part 3 the argument is a *branch-free
  algebraic identity*: the certificate (10) holds for all real values of the variables,
  which is exactly the reviewer-predicted resolution of the mirror-branch obstruction —
  the mirror components of the naive $\operatorname{Im}(\cdot) = 0$ encoding do not
  satisfy the branch-pinned relations (K), (L) with these *unsigned-angle* derivations.
- **Machine assistance:** the certificate cofactors $\alpha, \beta$ were *found* by a
  sympy linear solve (`/tmp/round-1/scratch/build_cc_4.py`) and every displayed identity
  re-verified symbolically (`build_cc_2.py`, `build_cc_5.py`–`build_cc_10.py`) and
  numerically on a genuine configuration (`build_cc_1.py`); but the written proof stands
  on its own — each identity is displayed with its full Fourier expansion table and the
  mode-by-mode cancellation, checkable by hand.

## Promotable lemmas

- **Median-formula reduction** (`OM = ON ⟺ OB² − OC² = (c²−b²)/2 ⟺ pow(B,ω) − pow(C,ω) = (c²−b²)/2` for any circle ω through A with centre O) — proved in full in Parts 1 and 5 (equations (1), (7)); shared with all approaches, worth certifying as `lemmas/median-reduction.md`.
- **Non-collinearity of A, K, L** from the sector hypotheses (Part 4, self-contained: the cot-monotonicity argument) — reusable by every other approach, worth certifying as `lemmas/AKL-noncollinear.md`.
- **Side relations** ℓ_K = 0, ℓ_L = 0 (Part 3: `b sin²(φ+u) = c[cos A − cos(φ+u)cos(A+φ−u)]` and its b↔c, u→v mirror, where u = ∠KAB, v = ∠LAC, φ = ∠KBA = ∠ACL) — the complete branch-free encoding of the hypotheses after eliminating χ, ψ; equivalent content to secant-trig-identity's E-system after elimination, worth certifying as `lemmas/side-relations.md`.
- **Certificate identity** (10) with cofactors α, β (Part 6) — the load-bearing identity; if secant-trig-identity reaches the same elimination, it can import this instead of re-deriving.
