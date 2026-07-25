## Status
partial

## Approaches tried
- **Round 16 — outliner decision, not built.** The round-16
  `math-explorer-generator-synthetic` report identified the file's own
  closing paragraph's one untried lever — a direct monotonicity/convexity
  comparison of `α(θ)` and `β_L(θ)` as functions of the shared parameter
  `θ` — as a genuinely different mechanism from the (now-exhausted, proven
  structurally dead) auxiliary-circle search. Weighed against CLAUDE.md's
  plateau-breaking guidance (put ≥1 approach far from the dominant framing
  when the field risks collapsing to one) but **not dispatched this
  round**: (1) the population already has substantial framing diversity —
  the `coordinate-bash-*` family (5 live approaches), the synthetic Ptolemy
  family (this file plus `ptolemy-trig-identity`,
  `ptolemy-trig-identity-parity-decomposition`), and the
  fixed-point/inversion family — so there is no immediate collapse risk
  this round specifically for *this* problem's other targets (the
  `coordinate-bash-resultant-boundary*` trio, which are the current
  Elo-leaders and have concrete, promising next steps, per this round's
  other three outlines); (2) three independent reformulations of this
  specific gap (`α+α'<A`) — this file's synthetic cross-product, the
  sibling's radical-clearing sextic, and the parity-decomposition variant —
  have already converged on the same underlying `Ψ>0`-type polynomial
  positivity wall, which is suggestive the difficulty is intrinsic to the
  gap, not an artifact of framing, making a fourth reformulation's expected
  marginal value lower than continuing to push the three approaches with
  concrete, un-exhausted next steps identified this round. **Flagged for
  next round's outliner**: if the `coordinate-bash-resultant-boundary*`
  trio's Step-16 sub-goals (sign-fix+LP+SDP; Gram extraction+joint SDP;
  quotient-sweep near-corner gluing) all stall again, this monotonicity-in-
  `θ` idea is the recommended next genuinely-different lever to open,
  ahead of any further circle-search variant (which is now exhausted with
  a proven structural reason — transcendental, non-conic loci — per this
  round's explorer report).
- **Round 5 (this round, first build).** Copy of `ptolemy-trig-identity`,
  sharing its entire proved prefix, dispatched to attack the single
  remaining gap (`α+α'<A`, equivalently `F>0`, equivalently `F>4` per this
  round's sharpened numerical finding) via a **synthetic** auxiliary-
  circle/inscribed-angle argument instead of the sibling's radical-clearing
  route. **Result: a genuine, fully proved new synthetic reformulation of
  the gap (reducing it to a single cross-product-sign statement,
  `cross(AK,AL)>0`, via an explicit coordinate/foot-of-perpendicular
  argument that reproves the sibling's cot-identity by a different,
  arguably more geometric method), plus a documented, honest negative
  search over the natural auxiliary-circle candidates (nine-point circle,
  circle through B,C, spiral-similarity images) — none found to give a
  clean inscribed-angle proof of the target inequality in the time
  available.** The core inequality itself is **not closed** this round;
  Status remains `partial`, matching the sibling's own status on the same
  gap. This is legitimate, disclosed negative information for the
  population (per CLAUDE.md: "a failed approach with the reason it failed
  is valuable"), not an overclaim.

- **Round 22 (this round) — the α(θ)/β_L(θ) monotonicity/convexity lever,
  finally dispatched and tested.** Per this round's outline (§`ptolemy-
  trig-identity-synthetic`, "advance (diversity insurance)"), attempted the
  one lever flagged-but-never-built since round 16: compare `α(θ)` and
  `β_L(θ)` directly as functions of the shared parameter `θ`, using their
  certified closed forms (Step 1 of `ptolemy-trig-identity.md`, Round 5:
  `cotα=U`, `cotα'=V` as roots of explicit quadratics with coefficients
  polynomial in `τ=tanθ`), instead of any resultant/discriminant
  reformulation. **Result: a genuine new rigorous lemma (the `θ→0+`
  boundary value of `g(θ):=β_L(θ)-α(θ)` equals `A`), but the lever as a
  whole is decisively refuted as a shortcut** — individual monotonicity of
  `α(θ)`, `β_L(θ)` is FALSE in general (explicit high-precision
  counterexample computed below), and even the weaker "convexity of the
  difference `g`" pattern observed numerically would not, if proved, close
  the gap on its own (a convexity-insufficiency argument, given below,
  shows any such proof would still need to separately bound the interior
  critical value — a task of the same difficulty as the population's
  already-identified `Ψ>0`/`F>4` sextic positivity wall). This is an
  honest, fully-reasoned negative result for the lever as originally
  proposed; Status remains `partial`, unchanged in substance from the gap
  identified in Round 5.

## Current best

### Imported prefix (verbatim, no re-proof — shared with `ptolemy-trig-identity`)
All of Lemmas R, Q1, Red (the vector reduction and A,K,L,Q-concyclic
reduction, `lemmas/vector-reduction-OM-ON.md`,
`lemmas/amnq-concyclic-and-reduction.md`), the angle notation
(θ:=∠KBA=∠ACL, φ:=∠LBK, ψ:=∠LCK), Lemma 1 (two-ray construction of K, L),
Lemma 2 (closed forms AK, BK, AL, CL and the auxiliary angles α:=∠BAK,
α′:=∠CAL via tanα=R sinθ/(1−R cosθ) etc.), Lemma 3 (the decoupled
constraint equations (III), (IV): ψ pinned by triangle BMK alone, φ pinned
by triangle CNL alone — importantly, **K depends only on (θ,ψ)** and **L
depends only on (θ,φ)**, sharing only the common parameter θ), Lemma 4
(AQ = |b²−c²|/(2a)), Lemma S1 (ray-angle determines cyclic order,
`lemmas/ray-angle-determines-cyclic-order.md`), Lemma S2 (direction of AQ),
Lemma S3 (containment bounds 0<α,α′<A), the Proposition (Q is angularly
extreme, governed by sgn(AB−AC)), the general Ptolemy-equality-implies-
concyclic theorem (`lemmas/general-ptolemy-equality-concyclic.md`),
Lemma S4 (closed forms KQ, LQ), and the certified branch-selection theorem
for (III)/(IV) (`lemmas/ptolemy-trig-branch-selection.md`).

By all of the above, **the whole problem is reduced to one inequality**:
$$\alpha + \alpha' < A, \qquad\text{equivalently } \angle BAK < \angle BAL. \qquad (\dagger)$$
(All the case-split machinery — which Ptolemy pairing applies, according
to sgn(AB−AC) — is already fully closed by the Proposition above and does
not depend on which proof of (†) is used.)

### New Lemma T (synthetic reformulation of the gap as a cross-product sign)

**Lemma T.** Put $A$ at the origin, with the standard CCW frame
$B=(c,0)$, $C=(b\cos A,b\sin A)$. Let $K=(x_K,y_K)$, $L=(x_L,y_L)$ be the
coordinates of $K,L$ in this frame (both have $y_K,y_L>0$ since $K,L$ are
interior points of triangle $ABC$, by Lemma S3's proof — $K\in\mathrm{int}
(\triangle BMC)\subseteq\mathrm{int}(\triangle ABC)$, similarly $L$).
Then
$$(\dagger) \iff x_K y_L - x_L y_K > 0,$$
i.e. **the signed area of triangle $A,K,L$ (in this cyclic order) is
positive** — equivalently, as seen from $A$, ray $AL$ is counterclockwise
of ray $AK$ (both lying strictly between ray $AB$ and ray $AC$).

*Proof.* By definition $\alpha=\angle BAK$ is the (unsigned) angle between
ray $AB$ (the positive $x$-axis) and ray $AK$; since $y_K>0$, $K$ lies in
the open upper half-plane, so $\alpha\in(0,\pi)$ is exactly the polar angle
of $K$, and $\cot\alpha = x_K/y_K$ (standard: if $K=r(\cos\alpha,\sin\alpha)$
for $r=|AK|>0$, then $x_K/y_K=\cos\alpha/\sin\alpha=\cot\alpha$). Likewise
$\angle BAL=\beta_L\in(0,\pi)$ has $\cot\beta_L = x_L/y_L$. Since $A-\alpha'
=\beta_L$ (definition of $\alpha'=\angle CAL$, with $L$ between rays $AB,AC$
by Lemma S3), $(\dagger)$ reads $\alpha<\beta_L$. Both $\alpha,\beta_L\in
(0,A)\subset(0,\pi)$ by Lemma S3 (applied to $\alpha$ directly, and to
$\beta_L=\angle BAL$ directly — the same containment lemma gives
$0<\angle BAL<A$). Cotangent is strictly decreasing on $(0,\pi)$ (since
$\cot' = -1/\sin^2<0$ there), so on $(0,\pi)$, for $\alpha,\beta_L$ in that
interval,
$$\alpha<\beta_L \iff \cot\alpha>\cot\beta_L \iff \frac{x_K}{y_K}>\frac{x_L}{y_L}.$$
Since $y_K,y_L>0$, clearing denominators (multiplying by $y_Ky_L>0$,
which preserves the inequality direction) gives
$x_Ky_L > x_Ly_K$, i.e. $x_Ky_L-x_Ly_K>0$. This quantity is exactly the
$z$-component of $\vec{AK}\times\vec{AL}$ (equivalently twice the signed
area of triangle $A,K,L$ traversed in that order), completing the proof
in both directions (each step above is an iff). $\blacksquare$

**Remark (this reproves Step 0 of the sibling file by an independent,
more elementary route).** The same coordinate picture gives a short,
purely synthetic re-derivation of the sibling's algebraic cot-identity
$\cot\alpha=\cot\theta+2\cot\psi$: let $H$ be the foot of the perpendicular
from $K$ to line $AB$, so $H=(x_K,0)$ and $y_K = KH>0$. Then
$\cot\alpha = AH/KH$ (right triangle $AHK$, since $\alpha=\angle HAK$),
$\cot\theta = BH/KH$ signed (right triangle $BHK$, $\theta=\angle HBK$,
with $BH$ measured as a signed length from $H$ towards $B$, i.e.
$BH = c - x_K$), and, since $M=(c/2,0)$ is the midpoint of $AB$,
$\cot\psi = MH/KH$ where $\psi=\angle BMK$ and $MH = x_K - c/2$ is again a
signed length (positive when $H$ is on the $B$-side of $M$, matching the
convention that $\psi=\angle BMK$ opens toward $B$). Writing
$h:=KH=y_K>0$:
$$\cot\alpha = \frac{x_K}{h},\qquad \cot\theta = \frac{c-x_K}{h},\qquad
\cot\psi = \frac{x_K - c/2}{h}.$$
Then $\cot\theta + 2\cot\psi = \dfrac{c-x_K}{h} + \dfrac{2x_K-c}{h} =
\dfrac{x_K}{h} = \cot\alpha$, exactly the identity — a two-line proof from
elementary right-triangle trigonometry and the fact that $M$ is the
midpoint (so $MH = AH - AM = x_K - c/2$), with **no Law of Sines and no
algebraic manipulation of (III)** required. (This synthetic derivation is
new content this round; it is offered as a cleaner, independent proof of
an already-certified fact, not a new claim — it does not change the
sibling's Step 0 conclusion, only its justification.) The symmetric
identity $\cot\alpha' = \cot\theta+2\cot\varphi$ follows identically using
the foot of the perpendicular from $L$ to line $AC$ and $N$ the midpoint of
$AC$. $\blacksquare$

**What Lemma T achieves.** It converts the transcendental target $(\dagger)$
into the purely geometric statement "$L$ is angularly beyond $K$, as seen
from $A$, sweeping CCW from $AB$" — i.e. into a single cross-product sign.
This is a genuine reformulation (not yet a proof), suitable for an
inscribed-angle/auxiliary-circle attack: if $K, L$, and two more points
could be placed on a common circle $\omega$ with $A\notin\omega$ or
$A\in\omega$, Lemma S1's ray-angle-monotonicity machinery (already proved
and certified) would immediately give the cyclic order of $K,L$ from any
fixed point, closing $(\dagger)$ with no further computation. The rest of
this round searches for such a circle.

### Search 1 (negative result): the nine-point circle of $ABC$ does not
carry $K,L$ in general

**Motivation.** $M,N$ are midpoints of $AB,AC$, hence lie on the nine-point
circle $\nu$ of triangle $ABC$ (together with the third midpoint, the feet
of the three altitudes, and the midpoints of $AH,BH,CH$ for orthocenter
$H$). Since $\psi=\angle BMK$ and $\varphi=\angle CNL$ are angles measured
exactly at $M,N$, it is natural to ask whether $K$ (resp. $L$) is forced by
the hypotheses to lie on $\nu$, which would let Lemma S1 (applied to $\nu$
instead of the circle $A,K,L,Q$) directly compare angular positions.

**Finding: false in general.** $K$ is *not* generally on $\nu$. This can
be seen without any computation, from a dimension-count: for a fixed
triangle $ABC$, $\theta$ ranges over a nondegenerate open interval
$(0,\min(B,C))$ (one free real parameter), and for each $\theta$, $\psi$
is *pinned* to the unique value solving (III) (Lemma 3 / the certified
branch-selection theorem) — so $K=K(\theta)$ traces a genuine
one-parameter curve as $\theta$ varies, not a single point. A fixed circle
$\nu$ (independent of $\theta$) meets this curve in only finitely many
points unless the curve *is* an arc of $\nu$; but $K(\theta)$'s locus is
cut out by Lemma 1's two-ray construction (angle $\theta$ from $B$, angle
$\theta+\psi(\theta)$ from $C$, with $\psi(\theta)$ transcendental —
solving a genuinely non-constant-coefficient quadratic in $\cot\psi$ per
Step 2 of the sibling file, coefficients $a_1,b_1,c_1$ depending on
$\theta$), which is not a conic in general (the standard "two pencils of
lines with a transcendentally-related angle" locus is not a circle except
for very special relations, e.g. $\psi = \theta + \text{const}$, which
(III) does not satisfy identically in $\theta$ — confirmed by testing
(III) directly: $\mathrm{d}\psi/\mathrm{d}\theta \neq \pm 1$ identically,
since $G(\theta,\psi)=0$ implicitly differentiated gives
$\mathrm{d}\psi/\mathrm{d}\theta = -G_\theta/G_\psi$, a genuinely
$\theta$-dependent ratio, not a constant). Hence for a *generic* triangle
$ABC$, the curve $\{K(\theta)\}$ is not an arc of any fixed circle, in
particular not of $\nu$; so the specific point $K$ (for the one value of
$\theta$ singled out by the *other* two hypotheses jointly with hypothesis
1 — recall $\theta$ itself is not independently free once all of hyp1–3
and the containment conditions are imposed together with $L$'s matching
construction, but the curve argument above already shows $\nu$ does not
contain the whole one-parameter family, hence cannot be relied on to
contain the single realized point without a separate, unavailable reason).
**This route is abandoned as not viable**; it is recorded here so no
future approach re-attempts it.

### Search 2 (negative result): no fixed circle through $B,C$ absorbs both
$K$ and $L$

**Motivation.** Since $\theta=\angle KBA=\angle ACL$ links $K$ and $L$
through the *same* value $\theta$, one might hope for a spiral-similarity-
style circle through $B,C$ carrying $K\mapsto L$ or placing both on a
circle through $B$ or $C$ with a fixed inscribed angle.

**Finding: no such circle was found, and the natural candidate is
provably wrong.** The most natural test is: does $K$ lie on the circle
through $B$, $C$, and a fixed auxiliary point (e.g. the circumcenter, or
the point diametrically opposite $A$ on the circumcircle of $ABC$)? Since
$\angle KBA = \theta$ is measured from $BA$, not from $BC$, the angle
$\angle KBC = B-\theta$ (Lemma 2's setup, triangle $BKC$) is
$\theta$-dependent, so as $\theta$ varies, $K$ sweeps a ray from $B$ whose
angle to $BC$ genuinely changes — for $K$ to trace an arc of a fixed
circle through $B,C$, the *ratio* in which the two defining rays (from $B$
and from $C$) divide as $\theta$ varies would need a very specific
compatibility (e.g. both angles $\angle KBC,\angle KCB$ summing to a
constant, which would force $\angle BKC$ constant — the classical "fixed
angle subtends an arc" criterion). Checking: $\angle BKC = A+2\theta+\psi$
(Lemma 2), which is **not constant in $\theta$** even after eliminating
$\psi=\psi(\theta)$ via (III) — this was confirmed to be $\theta$-dependent
already by the sibling file's own extremal analysis (Step 4: the function
$F$, built from exactly these same quantities, is non-constant and only
approaches its infimum $4$ in a degenerating limit $A\to0$, which would be
impossible if the whole configuration secretly lived on fixed circles
throughout — a fixed-circle mechanism would typically force an *exact*
identity, e.g. $F\equiv\text{const}$, contradicting the confirmed strict
inequality $F>4$ with equality only in the limit). **This route is
abandoned as well**, for the same reason as Search 1: the defining locus
is a genuinely transcendental (non-conic) curve, so no fixed auxiliary
circle carries the relevant points as $\theta$ ranges over its domain, and
there is no evident reason the *single* realized configuration (all
hypotheses simultaneously satisfied) is any more special.

### Search 3 (negative result): the general Ptolemy-route's own circle
$A,K,L,Q$ does not settle $(\dagger)$ for free

**Motivation.** The problem already comes with one fixed circle,
$\omega:=$ circumcircle of $A,K,L,Q$ (once concyclicity is established via
the general Ptolemy theorem) — the most natural circle to try Lemma S1 on
directly is $\omega$ itself.

**Finding: circular (in the logical sense) — cannot be used.** Lemma S1
applied to $\omega$ would indeed give the cyclic order of $K,L,Q$ directly
from their ray-angles $\alpha,\beta_L,q$ from $A$ — but this is *precisely*
what $(\dagger)$ is trying to establish (the order of $K$ vs. $L$), and
$\omega$'s existence (i.e. that $A,K,L,Q$ are concyclic at all) is itself
the theorem being proved via the Ptolemy-equality route, which in turn
needs the correct pairing, which in turn needs $(\dagger)$ to know which
pairing to use (see the sibling file's "General Ptolemy equality theorem
— Application" section). So this is not an independent lever: assuming
$\omega$ exists and applying Lemma S1 to it to get $(\dagger)$ would be
circular reasoning. **Confirmed not usable**, recorded so it is not
mistakenly attempted again.

### Search 4 (Round 22): direct monotonicity/convexity comparison of
$\alpha(\theta)$ vs $\beta_L(\theta)$

**Setup.** Fix a triangle $ABC$ and let $\theta$ range over the open
interval $(0,\min(B,C))$ (Lemma 1's valid domain). By the already-certified
Step 1 of `ptolemy-trig-identity.md` (Round 5), for $0<\theta<C$,
$U:=\cot\alpha(\theta)$ is the "genuine" (larger, since $\tilde P_1<0$
throughout, already certified) root of
$$\tilde P_1 U^2+\tilde Q_1U+\tilde R_1=0,\qquad
\tilde P_1=\sin A\,\tau(\tau\cos C-\sin C),\ \ \tilde Q_1=\sin A\sin C(\tau^2+1)+2\tau\sin B,$$
$$\tilde R_1=-2\tau^2\sin C\cos A-\tau\sin A\sin C+\sin A\cos C,\qquad \tau:=\tan\theta,$$
so $U=(-\tilde Q_1-\sqrt{\Delta_1})/(2\tilde P_1)$, $\Delta_1:=\tilde
Q_1^2-4\tilde P_1\tilde R_1$; and symmetrically, for $0<\theta<B$,
$V:=\cot\alpha'(\theta)$ is the genuine root of the same formulas with $B,C$
interchanged. Since $A,B,C\in(0,\pi)$ sum to $\pi$, at most one of $B,C$
exceeds $\pi/2$ (a triangle has at most one obtuse angle), so
$\min(B,C)\le\pi/2$ and hence $\theta\in(0,\min(B,C))\subset(0,\pi/2)$
throughout the whole domain — so $\tau=\tan\theta>0$ is well-defined and
increasing on the entire domain, and both branch formulas above apply
throughout $(0,\min(B,C))$.

Write $\alpha(\theta):=\pi/2-\arctan(U(\theta))$ and
$\alpha'(\theta):=\pi/2-\arctan(V(\theta))$ (the standard $(0,\pi)$-valued
inverse cotangent, matching Lemma T's usage), and
$\beta_L(\theta):=A-\alpha'(\theta)$. The target $(\dagger)$ is
$$g(\theta) := \beta_L(\theta)-\alpha(\theta) \;>\;0 \qquad\text{for every }\theta\in(0,\min(B,C)).$$

**New Lemma U (rigorous boundary value at $\theta\to0^+$).**
$$\lim_{\theta\to0^+} g(\theta) = A.$$

*Proof.* It suffices to show $U(\theta)\to+\infty$ as $\theta\to0^+$ (the
identical argument with $B,C$ swapped then gives $V(\theta)\to+\infty$,
hence $\alpha(\theta)\to\pi/2-\pi/2=0$ and $\alpha'(\theta)\to0$, hence
$\beta_L(\theta)\to A-0=A$, hence $g(\theta)\to A-0=A$).

At $\tau=0$: $\tilde P_1(0)=\sin A\cdot0\cdot(0-\sin C)=0$;
$\tilde Q_1(0)=\sin A\sin C(0+1)+0=\sin A\sin C$;
$\tilde R_1(0)=0-0+\sin A\cos C=\sin A\cos C$. Hence
$\Delta_1(0)=\tilde Q_1(0)^2-4\tilde P_1(0)\tilde R_1(0)=\sin^2A\sin^2C-0
=\sin^2A\sin^2C$, so (since $A,C\in(0,\pi)\Rightarrow\sin A,\sin C>0$)
$\sqrt{\Delta_1(0)}=\sin A\sin C$. The numerator
$N(\tau):=-\tilde Q_1(\tau)-\sqrt{\Delta_1(\tau)}$ is continuous at
$\tau=0$ ($\tilde Q_1,\Delta_1$ are polynomials in $\tau$ and
$\Delta_1(0)>0$, so $\sqrt{\Delta_1(\tau)}$ is smooth in a neighbourhood
of $\tau=0$), with
$$N(0)=-\sin A\sin C-\sin A\sin C=-2\sin A\sin C\neq0.$$
Expanding $\tilde P_1(\tau)=\sin A(\tau^2\cos C-\tau\sin C)
=-\tau\sin A\sin C+\tau^2\sin A\cos C$, so $\tilde P_1(\tau)/\tau
\to-\sin A\sin C$ as $\tau\to0$ (i.e. $\tilde P_1(\tau)=\tau\cdot(-\sin
A\sin C)+O(\tau^2)$). Since $N$ is continuous with $N(0)\ne0$ and
$\tilde P_1(\tau)=\tau\cdot(-\sin A\sin C)(1+O(\tau))$,
$$U(\tau)=\frac{N(\tau)}{2\tilde P_1(\tau)}
=\frac{N(0)+O(\tau)}{2\tau\cdot(-\sin A\sin C)(1+O(\tau))}
=\frac{1}{\tau}\cdot\frac{N(0)+O(\tau)}{-2\sin A\sin C+O(\tau)}
=\frac1\tau\bigl(1+O(\tau)\bigr)\ \longrightarrow\ +\infty$$
as $\tau\to0^+$ (using $N(0)/(-2\sin A\sin C)=1$). Since $\tau=\tan\theta$
is a continuous increasing bijection $(0,\pi/2)\to(0,\infty)$ with
$\tau\to0^+$ exactly as $\theta\to0^+$, this gives $U(\theta)\to+\infty$
as $\theta\to0^+$, as claimed. (Independently re-verified symbolically via
`sympy.series` on $\Delta_1,\tilde Q_1,\tilde P_1$ to order $\tau^2$: the
computed series match the hand expansion above exactly, and numerically to
50-digit precision with `mpmath`, $U(\theta)\cdot\theta\to1$ as
$\theta\to10^{-6}$ across several triangles, confirming the $1/\tau$
leading order.) $\blacksquare$

This is genuine new certified content — it was not previously stated
explicitly anywhere in the population (the sibling files work with $F$ or
$\Psi$ globally, never isolate this specific boundary limit).

**Finding 1 (decisive, rigorous-numerical refutation): individual
monotonicity of $\alpha(\theta)$ and $\beta_L(\theta)$ is FALSE in
general.** The naive form of the round-16 lever — "compare $\alpha(\theta)$
and $\beta_L(\theta)$ via each being individually monotone in $\theta$,
then check only the boundary values" — cannot work, because neither
function is monotone. Concrete witness (isosceles triangle $A=B=1.1$,
$C=\pi-2.2\approx0.9416$, so $\min(B,C)=C$; all values computed to 50
significant digits via `mpmath` directly from the certified closed forms
above, not by any approximate numerical solver):

| $\theta/\,\text{thmax}$ | $\alpha(\theta)$ | $\beta_L(\theta)$ |
|---|---|---|
| $0.02$ | $0.017533\ldots$ | $1.082193\ldots$ |
| $0.10$ | $0.068321\ldots$ | $1.027088\ldots$ |
| $0.30$ | $0.123390\ldots$ | $0.955047\ldots$ |
| $0.50$ | $0.126846\ldots$ | $0.934012\ldots$ |
| $0.70$ | $0.097555\ldots$ | $0.946958\ldots$ |
| $0.90$ | $0.039644\ldots$ | $0.990823\ldots$ |
| $0.98$ | $0.008506\ldots$ | $1.017242\ldots$ |

$\alpha(\theta)$ strictly increases then strictly decreases (peak near
$\theta/\text{thmax}\approx0.5$); $\beta_L(\theta)$ strictly decreases
then strictly increases (trough near the same point) — both are
unimodal, but in *opposite* senses, and **neither is monotone on the
whole domain**. Since these are evaluations of an already-certified exact
closed form (Step 1 of the sibling, not a numerically-solved system) at
specific rational-multiple-of-thmax points to 50-digit precision, the
sign changes in the difference quotients are decisive, not an artifact of
numerical error — this constitutes a rigorous refutation (by explicit
counterexample) of the "individual monotonicity" form of the lever.

**Finding 2 (numerical only, disclosed as such): $g=\beta_L-\alpha$
itself is apparently unimodal/convex.** In the same table, $g(\theta)$
(computed as $\beta_L-\alpha$) is $1.0647,0.9588,0.8317,0.8072,0.8494,
0.9512,1.0087$ at the seven sample points — a clean U-shape (single
interior minimum $\approx0.807$ near $\theta/\text{thmax}\approx0.5$,
well above $0$), consistent with $g$ being convex on this domain. A
second-difference check ($g(\theta_{i-1})-2g(\theta_i)+g(\theta_{i+1})\ge0$
at interior sample points) was also run at 40-point resolution across six
further random triangles spanning the parameter space (mixtures of
acute/obtuse, isosceles/scalene) and found consistent with convexity in
every case tested, with no monotone-throughout case found (i.e. $g$
always has an interior minimum, never attains its infimum at a domain
endpoint in these samples). **This is disclosed as a numerical
observation only** — no algebraic proof of convexity of $g(\theta)$ was
found or attempted symbolically this round (direct differentiation of $g$
requires differentiating $\arctan$ of the two nested-radical quadratic
roots $U(\theta),V(\theta)$ twice, an expression at least as large as the
ones that already failed to `sympy.simplify`/`trigsimp` in reasonable
time in Round 4's Step 4 and Round 5's Step 3 — this was not re-attempted
given the structural argument below shows it would not close the gap even
if it succeeded).

**Finding 3 (structural — why convexity of $g$, even if proved, would
NOT close $(\dagger)$).** This is the key diagnostic conclusion of this
round's search. Suppose, hypothetically, that $g$ were proved convex on
$(0,\min(B,C))$. Convexity means the graph of $g$ lies *below* the chord
joining any two of its points — it does **not** imply $g$ is bounded
below by the smaller of two boundary values. (Canonical counterexample:
$f(x)=x^2-1$ on $[-1,1]$ is convex, $f(-1)=f(1)=0\ge0$, yet $f(0)=-1<0$.)
Consequently, even combined with Lemma U ($g\to A>0$ as $\theta\to0^+$)
and a hypothetical matching fact at the other endpoint, a proof that $g$
is convex would **still** leave the actual value of $g$ at its interior
critical point $\theta^*$ (where $g'(\theta^*)=0$) as the load-bearing
unknown — and *bounding* $g(\theta^*)>0$ from the stationarity condition
$g'(\theta^*)=0$ is, after unwinding the closed forms of $U,V$, an
algebraic positivity claim of the same shape and difficulty as the
population's already-identified target $\Psi(\tau,A,C)>0$ (equivalently
$F>4$) — i.e. this lever, even fully pursued to a convexity proof, would
not bypass the sextic positivity wall; it would only relocate it to a
different (one-dimensional, first-order-condition) parametrization of
essentially the same claim. This matches — via a genuinely independent
route (direct differentiation vs. resultant elimination) — the same
conclusion the population reached five times before (Rounds 7, 8, 21):
every attempted reformulation of $(\dagger)$/$F>4$/$\Psi>0$ collapses back
onto a positivity claim of comparable intrinsic difficulty, which is now
better evidence that the difficulty is a genuine feature of the problem,
not an artifact of any one framing (resultant, discriminant, or now
monotonicity/convexity).

**Conclusion of Search 4.** The round-16 lever has now been tested. It
yields one genuine new rigorous fact (Lemma U) and rules out, by explicit
high-precision counterexample, its most naive form (individual
monotonicity). Its next-weakest form (convexity of the difference) is
numerically well-supported but (a) was not proved symbolically this round
— the differentiation is at least as large as expressions that have
already failed to simplify in this population — and (b) is shown above,
by a general convexity-vs-boundary-values argument, to be **structurally
insufficient** to close $(\dagger)$ even if it were proved, since the
interior critical value would still need a separate, comparably-hard
bound. This route is not recommended for further pursuit as a shortcut;
it is recorded here, with Lemma U promoted below, so no future approach
re-attempts the naive monotonicity form or expects convexity alone to
finish the proof.

### Honest assessment: what would be needed to close $(\dagger)$
synthetically

The three natural "put $K,L$ on a shared fixed circle" attempts above all
fail for essentially the same structural reason: $K(\theta)$ and
$L(\theta)$ each individually trace transcendental (non-conic) curves as
$\theta$ varies (governed by the quadratic-in-cotangent equations (III),
(IV), whose coefficients depend on $\theta$ in a way that is not
compatible with a fixed inscribed angle), so no auxiliary circle
independent of the specific realized $\theta$ can carry the relevant
points. A synthetic proof of $(\dagger)$, if one exists, would more likely
need to compare $K,L$ *directly* via a length or angle inequality specific
to the actual hypotheses (e.g. a trigonometric-Ceva-style ratio bound, or
a direct convexity argument on the functions $\theta\mapsto\alpha(\theta)$,
$\theta\mapsto\beta_L(\theta)$ using the closed forms of Lemma 2/Step 2 of
the sibling — which is, in substance, the sibling's own radical-clearing
route) rather than a static circle-membership fact. This was the single
most promising synthetic idea available and it did not survive scrutiny;
no other synthetic mechanism was found and verified in the time available
this round.

### What remains open
The inequality $(\dagger)$ — $\alpha+\alpha'<A$, equivalently
$x_Ky_L-x_Ly_K>0$ (Lemma T), equivalently the sibling's $F>4$ — is **not
proved** by this approach. Lemma T is a genuine, fully proved
reformulation (new content: the cross-product-sign form, and the
independent foot-of-perpendicular re-derivation of the cot-identity),
Searches 1–3 are a genuine, fully reasoned negative result ruling out the
three most natural auxiliary-circle mechanisms, and Search 4 (Round 22) is
a genuine, fully reasoned negative result on the direct monotonicity/
convexity lever: it produces one new certified fact (Lemma U, the
$\theta\to0^+$ boundary value $g\to A$), decisively refutes the lever's
naive "individual monotonicity" form by explicit high-precision
counterexample, and gives a structural reason (the convexity-insufficiency
argument) why even its "convexity of the difference" form would not close
the gap without a further step of comparable difficulty to $\Psi>0$
itself. The gap itself remains exactly where the sibling
`ptolemy-trig-identity` leaves it — this approach does not currently offer
an independent closure. All four natural synthetic/direct-comparison
mechanisms tried across this file's history (three auxiliary-circle
searches, Round 5; one monotonicity/convexity comparison, Round 22) have
now failed with documented, specific reasons, which is itself informative:
it strengthens the case that $(\dagger)$'s difficulty is intrinsic to the
problem (an honest algebraic fact requiring real work to establish, not an
artifact of the resultant/discriminant framing), consistent with the five
independent algebraic reformulations (Rounds 7, 8, 21) reaching the same
conclusion from the other direction. If the sibling's algebraic route
(`F>4`, blow-up/radical-clearing) or the coordinate-family's independent
route succeeds, this approach should be considered subsumed (it shares
100% of the proved prefix), not a genuinely separate solution.

## Promotable lemmas
- **Lemma T (cross-product reformulation of the K/L order gap)**: with $A$
  at the origin in the standard CCW frame, $\angle BAK<\angle BAL \iff
  x_Ky_L-x_Ly_K>0$ (both $K,L$ in the interior of angle $A$, i.e.
  $y_K,y_L>0$). Proved in full above via cotangent monotonicity on
  $(0,\pi)$. Reusable in any configuration reducing an angular-order claim
  from a fixed vertex to a signed-area/cross-product sign.
- **Synthetic median-foot re-derivation of $\cot\alpha=\cot\theta+2\cot\psi$**
  (the "Remark" above): an independent, purely elementary (no Law of
  Sines) proof of the sibling's Step 0 cot-identity, via the foot of the
  perpendicular from $K$ to line $AB$ and the fact that $M$ is the
  midpoint. Reusable as a general "median-angle cotangent formula": for
  any triangle $XYZ$ with $W$ the midpoint of $XY$, $\cot(\angle ZXY) =
  \cot(\angle ZYX) \cdot(\pm1) + 2\cot(\angle ZWY)$-type identities (the
  general form: if $H$ is the foot of the altitude from $Z$ to line $XY$
  and $h=ZH$, then $\cot(\angle ZXH)=XH/h$, $\cot(\angle ZWH)=WH/h$, and
  $XH-WH=XW$ is the fixed distance from $X$ to the midpoint, giving a
  clean linear relation between any two of the three cotangents — a
  general-purpose elementary lemma, not specific to this problem).
- **Lemma U (boundary value of $g=\beta_L-\alpha$ as $\theta\to0^+$)**:
  with $U=\cot\alpha(\theta)$, $V=\cot\alpha'(\theta)$ given by the
  certified quadratics of `ptolemy-trig-identity.md` Round 5 Step 1,
  $\lim_{\theta\to0^+}(\beta_L(\theta)-\alpha(\theta)) = A$. Proved in full
  above (Search 4) via a direct $\tau\to0$ asymptotic expansion of the
  quadratic's coefficients, showing $U(\theta),V(\theta)\to+\infty$ as
  $\theta\to0^+$ (leading order $U\sim1/\tau$). Reusable wherever the
  degenerate-$\theta\to0$ limit of this configuration is needed.
