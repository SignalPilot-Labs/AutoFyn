## Status
unsolved

## Target
Prove OM = ON for the configuration of IMO 2026 P2.

## Outline (Cartesian + tangent-parametrization + resultant elimination)

This is the guaranteed-existence analytic route. No inspiration required: a
finite algebraic computation either verifies the identity or it does not.

**Coordinate choice.** A = (0,0), B = (2,0), C = (2p, 2q) with q > 0 and
(p,q) generic (scalene allowed; the isosceles special case p=0, q=1 is the
already-verified base case). Then M = midpoint(AB) = (1,0),
N = midpoint(AC) = (p,q). The line MN has direction (p−1, q); its perpendicular
bisector is the target line O must lie on.

**Parametrization of K and L by angle tangents.** Let
  tα = tan α,  tβ = tan β,  tγ = tan γ
where α=∠KBA=∠ACL, β=∠LBK=∠LNC, γ=∠LCK=∠BMK (the angle alphabet). Build K, L
*from* (tα, tβ, tγ) by ray intersection (this bakes in conditions (i)-(iii) by
construction, so the only remaining equations are the two midpoint-angle
conditions):
  - K = (ray from B making angle α with BA) ∩ (ray from M making angle γ with MB).
    BA is the negative x-direction from B=(2,0); MB is the negative x-direction
    from M=(1,0). Both rays go up-and-left from B and up-right? — careful with
    orientation; K is inside △BMC, so K is below line BC and above line AB.
    Explicitly: line from B at angle α above BA: parametric form
       B + s·(−cos α, sin α),  s > 0.
    line from M at angle γ above MB (MB points in −x): M + u·(−cos γ, sin γ)? No,
    MK goes up-and-right toward C side, so M + u·(cos γ, sin γ) with appropriate
    sign. [GAP-1: get the ray directions exactly right — orientation bug here
    silently inverts the variety, a recorded dead end.]
  - L = (ray from C making angle α with CA) ∩ (ray from N making angle β with NC).
    CA direction from C = (−2p,−2q)/|CA| = (−p,−q)/√(p²+q²); NC direction from
    N=(p,q) toward C=(2p,2q) is (p,q) (positive). L is inside △BNC.
  Solve the two 2×2 linear systems (rays are lines) to express K=(Kx,Ky),
  L=(Lx,Ly) as rational functions of (p,q,tα,tβ,tγ). [GAP-2: write these
  rational expressions; they are large but finite.]

**Two residual equations.** The parametrization built K,L from α,β,γ, using
conditions (i)-(iii) at B and C and M and N. Wait — (iii) ∠LCK=∠BMK=γ uses γ
at BOTH C and M, so the construction above already imposed (iii) at M. The two
conditions NOT yet imposed are the *other* occurrences:
  (i) at C:  ∠ACL = α  — imposed (L built from C-ray at angle α).
  (ii) at B: ∠LBK = β  — NOT yet imposed (L was built from C and N; need L to
    also lie on the ray from B at angle β past BK).
  (ii) at N: ∠LNC = β  — imposed (L built from N-ray at angle β).
  (iii) at C: ∠LCK = γ — NOT yet imposed (L was built from C at angle α; need
    the angle from CL to CK to be γ).
So the two residual equations are:
  E1: ∠(CL, CK) = γ   (the angle at C between the CL-ray and the CK-ray is γ)
  E2: ∠(LB, LK) = β   (the angle at B is β — wait, (ii) is ∠LBK = β, i.e. angle
     at B in triangle LBK, which is ∠(BL, BK).)
[GAP-3: write E1, E2 as polynomial equations in (tα,tβ,tγ,p,q) by taking the
tangent of both sides: tan(angle(PQ,PR)) = cross/dot, clear denominators.]
After clearing denominators E1, E2 are two polynomial equations n1=0, n2=0 in
the variables (tβ, tγ) (with tα, p, q as parameters) — note E1 involves only γ
at C plus the geometry; E2 involves β at B. Degree: each is moderate (≤ 4).

**Circumcenter as a linear solve.** With A=(0,0), the circumcenter O of △AKL
satisfies (equidistant from A and K, and from A and L):
  2 O·K = |K|²,   2 O·L = |L|²,
a 2×2 linear system in (Ox, Oy) with coefficient matrix [[2Kx, 2Ky],[2Lx, 2Ly]]
(ROWS are K and L — a recorded transpose bug; verify |OK|=|OL|=|OA| on output).
Solve:
  Ox = (|K|²·Ly − |L|²·Ky) / (2·(Kx·Ly − Lx·Ky)),
  Oy = (|L|²·Kx − |K|²·Lx) / (2·(Kx·Ly − Lx·Ky)).
[GAP-4: write O explicitly; this is mechanical.]

**Target.** OM² − ON² = (Ox−1)² + Oy² − (Ox−p)² − (Oy−q)²
           = 2(p−1)·Ox + 2q·Oy + 1 − p² − q².
Let T = 2(p−1)·Ox + 2q·Oy + 1 − p² − q² (a linear function of O, hence a
rational function of (p,q,tα,tβ,tγ)). Clear its denominator and call the
numerator N_T. The goal is N_T ≡ 0 mod (n1, n2) (i.e. on the solution curve).

**Elimination (the crux).** [GAP-5 — the load-bearing step:]
  Compute the resultant R = Res(n1, n2; tγ) (eliminate tγ, treating tα, tβ, p, q
  as parameters) — or eliminate the pair (tβ,tγ) by a bivariate resultant /
  multivariate Groebner with an elimination order.
  Then show that N_T lies in the ideal (n1, n2) by reducing N_T modulo a
  Groebner basis of (n1, n2) and obtaining remainder 0.
Already done for (p,q)=(0,1) (right-isosceles): the 268-term numerator reduces
to 0 in a 2-polynomial Groebner basis (lex on (tγ,tβ,tα)). The general-(p,q)
case is the gap.

Strategy to make the general elimination tractable (avoiding the recorded 9-min
timeout on naive 5-var lex Groebner):
  (a) Specialize tα to several numeric values (matching the numeric explorer's
      α ∈ {0.15, 0.25, ..., 0.90}) and verify remainder 0 for each — this proves
      the identity for infinitely-many-α *if* we also argue the remainder is
      polynomial in tα of bounded degree. [GAP-5a: bound the degree in tα and
      interpolate.]
  (b) OR: treat (p,q) as concrete generic values (e.g. p=0.25, q=1.3 — the test
      triangle of the analytic explorer) and run the 3-var (tα,tβ,tγ) Groebner
      reduction; if remainder 0, repeat for 2-3 more (p,q) and interpolate in
      (p,q) (the identity is polynomial in p,q of bounded degree). [GAP-5b.]
  (c) OR: full 5-var elimination via a careful lex/graded order with
      factorizing-Groebner; feasible if (a)/(b) bound the degrees first.

Mechanism (one-line reason it should work): the conclusion is an algebraic
identity on the 1-parameter solution curve, so it MUST reduce to 0 modulo the
ideal of that curve; the only question is whether the computation terminates in
the time budget. The isosceles-special-case success is strong evidence.

## Gaps
- GAP-1: correct ray orientations in the K,L parametrization (dead end recorded
  for the wrong orientation).
- GAP-2: explicit rational expressions for K, L.
- GAP-3: polynomial equations n1, n2 for the two residual angle conditions.
- GAP-4: explicit O (circumcenter) formulas.
- GAP-5 (THE crux): the general-(p,q) elimination showing N_T ∈ (n1, n2). Use
  the degree-bounding + interpolation sub-strategy (GAP-5a or GAP-5b) to make
  it tractable; full 5-var Groebner is a last resort and likely times out.

## Cases to cover
- Isosceles case (p=0, q=1): ALREADY PROVED (record as a certified lemma).
- General scalene (p,q): the gap.

## Watch out for
- Orientation of angle tangents (recorded dead end: equating oriented cross/dot
  as 3 equations in (kx,ky,lx,ly) gives the WRONG variety — must use the
  parametric construction that fixes orientation).
- Circumcenter linear-system transpose bug (rows are K, L).
- Naive 5-var lex Groebner times out at 9 min just on setup — do NOT attempt;
  use degree-bounding + interpolation or resultant elimination.
- Verify each intermediate numerically before trusting the symbolic reduction.
- A successful analytic proof is fully rigorous but UGLY; acceptable — the
  reviewer's bar is "no gaps, every theorem named", not "elegant".
