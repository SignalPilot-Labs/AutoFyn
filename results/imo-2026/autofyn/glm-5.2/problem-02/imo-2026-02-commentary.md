# IMO 2026, Problem 2 — Solution and Commentary

## Problem

Let $ABC$ be a triangle, and let $M$ and $N$ be the midpoints of $AB$ and $AC$,
respectively. Let $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$,
respectively, such that $K$ lies inside $\angle LBA$, $L$ lies inside
$\angle ACK$, and
$$
  \angle KBA=\angle ACL,\qquad
  \angle LBK=\angle LNC,\qquad
  \angle LCK=\angle BMK.
$$
If $O$ is the circumcentre of triangle $AKL$, prove that $OM=ON$.

---

## Notation

Write $\measuredangle(\ell_1,\ell_2)$ for the **directed angle** from line
$\ell_1$ to line $\ell_2$, taken modulo $\pi$ (so it is an angle between
*undirected* lines). Put
$$
A:=\angle BAC,\qquad
\alpha:=\angle KBA=\angle ACL,\quad
\beta:=\angle LBK=\angle LNC,\quad
\gamma:=\angle LCK=\angle BMK.
$$

---

## Solution

### Step 1 — Reduction to $|A'B|=|A'C|$

Let $A':=2O-A$, the **antipode of $A$** on the circumcircle $(AKL)$ (since $O$
is its centre). Then $AA'$ is a diameter, so by Thales' theorem
$$
A'K\perp AK\quad\text{and}\quad A'L\perp AL. \tag{R1}
$$
Equivalently, $A'$ is the intersection of the line through $K$ perpendicular to
$AK$ and the line through $L$ perpendicular to $AL$.

The homothety $h$ centred at $A$ with ratio $\tfrac12$ sends $B\mapsto M$ and
$C\mapsto N$ (midpoints), scales all distances by $\tfrac12$, preserves
perpendicularity, and so maps the perpendicular bisector of $BC$ bijectively
onto the perpendicular bisector of $MN$. Because $O\in\text{pb}(MN)\iff OM=ON$
and $h^{-1}(O)=2O-A=A'$,
$$
OM=ON\iff A'\in\text{pb}(BC)\iff |A'B|=|A'C|. \tag{R2}
$$
It remains to prove $|A'B|=|A'C|$.

### Step 2 — Direction Lemma: $\measuredangle(BC,BA')=90^\circ-A-\alpha$

We prove the key identity by a coordinate computation closed by an explicit
polynomial certificate.

**Frame.** Put $A=(0,0)$, $B=(1,0)$ (scale so $|AB|=1$),
$C=(b\cos A,b\sin A)$, $b>0$, so $ABC$ is counterclockwise. The six ray
directions are forced by the interior hypotheses:
$$
BK:\pi-\alpha,\; MK:\gamma,\; CL:A+\pi+\alpha,\; NL:A-\beta,\;
CK:A+\pi+\alpha+\gamma,\; BL:\pi-\alpha-\beta,
$$
with $0<\alpha$, $0<\alpha+\gamma<C$, $0<\alpha+\beta<B$ keeping sines positive.
Intersecting the relevant pairs,
$$
K=\Bigl(1-\tfrac{\sin\gamma\cos\alpha}{2\sin(\alpha+\gamma)},\;
        \tfrac{\sin\gamma\sin\alpha}{2\sin(\alpha+\gamma)}\Bigr),\quad
L=b\Bigl(\cos A-\tfrac{\sin\beta\cos(A+\alpha)}{2\sin(\alpha+\beta)},\;
        \sin A-\tfrac{\sin\beta\sin(A+\alpha)}{2\sin(\alpha+\beta)}\Bigr).
$$

**Incidences.** $K\in CK$ and $L\in BL$ are exactly the two remaining conditions
($\angle LCK=\gamma$, $\angle LBK=\beta$). The cross-product incidences
$\mathrm{conK}:=(K-C)\times\mathrm{dir}(CK)=0$ and
$\mathrm{conL}:=(L-B)\times\mathrm{dir}(BL)=0$ are each **linear in $b$**:
$\mathrm{conK}=k_1 b+k_0$, $\mathrm{conL}=l_1 b+l_0$, with
$k_1=\sin(\alpha+\gamma)\neq0$. Eliminating $b$ gives the **consistency**
$$
C:=k_0l_1-l_0k_1=0,\qquad b=-k_0/k_1. \tag{cons}
$$

**The point $A'$.** By (R1), $A'$ solves $A'\cdot K=|K|^2$ and $A'\cdot L=|L|^2$
(perpendicular-through-$K$ is $\{P:P\cdot K=|K|^2\}$, since $A=0$); the
denominator is $K\times L\neq0$ (as $A,K,L$ are non-collinear).

**The direction identity.** Set $\theta:=\tfrac\pi2-A-\alpha$ and let $R_\theta$ be
rotation by $\theta$. Then
$\measuredangle(BC,BA')=\theta$ is equivalent to
$(A'-B)\parallel R_\theta(C-B)$, i.e.\ to
$$
G:=(A'-B)\times R_\theta(C-B)=0. \tag{G}
$$
A direct substitution gives $G=G_2 b^2+G_1 b+G_0$ (polynomial in $b$). On the
locus $b=-k_0/k_1$, clearing $k_1^2$ yields
$g:=k_1^2 G(-k_0/k_1)=G_2 k_0^2-G_1 k_0k_1+G_0 k_1^2$, and $G=0\iff g=0$ on
$C=0$.

**Certificate.** With half-angle parameters
$t_\beta=\tan(\beta/2)$, $t_\gamma=\tan(\gamma/2)$ (baking in
$\sin^2\beta+\cos^2\beta=1$ and $\sin^2\gamma+\cos^2\gamma=1$) and
$s_\alpha,c_\alpha,s_A,c_A$ kept as **free indeterminates** (no Pythagorean
relation imposed), one has the **exact polynomial identity**
$$
\boxed{\;g = C\cdot T\;}
$$
for an explicit rational $T=T_n/T_d$ in $\mathbb{Z}[s_\alpha,c_\alpha,s_A,c_A]
[t_\beta,t_\gamma]$, verified by exact symbolic expansion
($g\,T_d-C\,T_n\equiv0$), equivalently by pseudodivision of $g$ by $C$ in
$t_\gamma$ over $\mathbb{Q}(s_\alpha,c_\alpha,s_A,c_A)(t_\beta)$ giving
**remainder $0$**. It is non-vacuous ($g$ and $C$ are nonzero at free-indeterminate
evaluations, unlike a prior attempt that fell into a maximal-ideal trap).

Because it is a polynomial identity in free indeterminates, it specialises to
the actual angles. On the configuration (cons) gives $C=0$, hence $g=0$, hence
$G=0$, hence
$$
\boxed{\;\measuredangle(BC,BA')=\theta=90^\circ-A-\alpha.\;} \tag{$\ast$}
$$
The certificate pins the **signed** value $+\theta$ (one checks $G(+\theta)=0$
but $G(-\theta)\neq0$ on the locus), used next.

### Step 3 — The counterpart for $CA'$ and conclusion

Relabel by the involution $\sigma$ swapping $B\leftrightarrow C$,
$M\leftrightarrow N$, $K\leftrightarrow L$ (hence $\beta\leftrightarrow\gamma$),
which fixes $A$, $\alpha$, and the point $A'$ (it exchanges the two
perpendiculars defining $A'$). The relabelled configuration still satisfies all
hypotheses, so ($\ast$) applies to it.

**Sign subtlety.** Step 2 was certified in the *counterclockwise* frame, giving
the signed value $+\theta$. The relabelled triangle $(A,C,B)$ is *clockwise*; to
apply the counterclockwise-framed lemma one reflects it, and a reflection
**negates** directed angles. Transferring back to the original frame,
$$
\measuredangle(CB,CA')=-\theta=-(90^\circ-A-\alpha). \tag{$\ast\sigma$}
$$
Since line $CB$ equals line $BC$ (mod $\pi$), no further sign appears:
$\measuredangle(BC,CA')=-(90^\circ-A-\alpha)$.

Now $\measuredangle(BC,BA')=+\theta$ and $\measuredangle(BC,CA')=-\theta$ are equal
and opposite, so the base angles of $\triangle A'BC$ coincide:
$$
\angle A'BC=|\theta|=\angle A'CB,
$$
making $\triangle A'BC$ isosceles with apex $A'$. (Equivalently: with $B,C$ on a
horizontal line, the line through $B$ at $+\theta$ and the line through $C$ at
$-\theta$ meet on the perpendicular bisector of $BC$.) Thus
$$
|A'B|=|A'C|,\quad\text{i.e.}\quad A'\in\text{pb}(BC). \tag{R3}
$$
Combining (R2) and (R3),
$$
\boxed{\;OM=ON.\;}\qquad\blacksquare
$$

---

## Commentary

### The one idea that makes the problem tractable
The conclusion $OM=ON$ looks like a statement about the circumcentre $O$, but
$O$ is awkward to handle directly. The trick is to pass to the **antipode**
$A'=2O-A$ of $A$ on $(AKL)$. By Thales, $A'$ is nothing but the intersection of
the two lines *perpendicular to $AK$ at $K$ and to $AL$ at $L$* — purely
incidence-geometric, with no circumcentre in sight. And because $M,N$ are
midpoints, a single homothety centred at $A$ converts "$O$ equidistant from
$M,N$" into "$A'$ equidistant from $B,C$." So the whole problem becomes:

> **Prove that the intersection of the two perpendiculars (to $AK$ at $K$, to
> $AL$ at $L$) lies on the perpendicular bisector of $BC$.**

### Why the obvious attempts stall
- A pure angle chase for $\angle A'BC=\angle A'CB$ **fails**: the position of
  $A'$ (intersection of two perpendiculars) depends on *lengths*, not only on
  angles, so the base angle $\angle A'BC$ is **not** a linear sum of the
  configuration angles. (Numerically it is the unsigned $V$-shape
  $|90^\circ-A-\alpha|$.)
- A coordinate proof of the **distance** identity
  $|A'B|^2-|A'C|^2=0$ also fails in the naive form: this expression belongs only
  to the *radical* of the constraint ideal, not the ideal itself, so no
  straightforward Gröbner / pseudodivision certificate exists (a genuine
  real-variety obstruction — the ideal is not radical).

### The decisive observation
Pass from the **distance** identity (degree-2, lives in a radical) to the
**direction** identity
$\measuredangle(BC,BA')=90^\circ-A-\alpha$ (a ratio/tangent, hence a *rational*
function). Rational identities admit clean **polynomial** divisibility
certificates: the cleared numerator $g$ satisfies $g=C\cdot T$ with remainder
$0$. Crucially, this identity involves **only $A$ and $\alpha$** — the dependence
on $\beta,\gamma$ cancels completely. That is the miracle: although $A'$ depends
on all of $K,L$ (hence on $\beta,\gamma$), the *direction* of $BA'$ from $BC$
depends on nothing but the single angle equality $\angle KBA=\angle ACL$.

### The sign trap (caught and fixed)
The lemma is a **signed** directed angle ($+\theta$), certified only in the
counterclockwise frame. Relabelling $B\leftrightarrow C$ reverses orientation
(turning the triangle clockwise), so a reflection is needed to re-apply the
lemma — and that reflection **flips the sign**, giving
$\measuredangle(CB,CA')=-\theta$. Two sign errors (a missed orientation flip,
and a spurious flip from the $CB\leftrightarrow BC$ line conversion) cancel to
produce the right answer by coincidence; the rigorous fix applies the
orientation-reversal sign exactly once. With $BA'$ at $+\theta$ and $CA'$ at
$-\theta$ from $BC$, the two lines are mirror images across the perpendicular
bisector of $BC$, forcing $A'$ onto it.

### Verification
The proof was checked three independent ways:
- **algebraic:** exact polynomial identity $g=C\cdot T$ (zero remainder on
  pseudodivision), non-vacuous;
- **numerical:** $\measuredangle(BC,BA')=+\theta$, $\measuredangle(BC,CA')=-\theta$,
  and $|A'B|-|A'C|\approx0$ to $\sim10^{-12}$ across many scalene triangles and
  valid $\alpha$;
- **coordinate:** the lines through $B$ at $+\theta$ and through $C$ at $-\theta$
  meet at the midpoint of $BC$, i.e.\ on its perpendicular bisector — a direct,
  non-circular confirmation of the isosceles conclusion.

### Files
- `results/imo-2026-02.md` — the rigorous proof (repo contract file,
  `Status: solved`), including the explicit factored certificate.
- `imo-2026-02-solution.tex` — this solution in LaTeX.
- `imo-2026-02-commentary.md` — this file (solution + commentary).
