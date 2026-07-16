## imo-2026-05

Fresh run, round 1. Population empty (nothing to sample/advance). Opening 3 new rival approaches
that share the easy prefix (answer + SOS sufficiency + x=f(y) pinch => f(f(y))=2f(y)-y + h>=0) but
DIFFER in how they close the hard "h=f-id is a nonnegative constant" step. All key algebra verified
symbolically this round (sympy): both original slacks = (x-f(y))^2; the right-inequality bound gives
h(t+p)-h(t) <= p^2/(4f(t)); the left-inequality bound gives f(t+p)^2 >= (f(t)+p)^2 - p^2/2.

Answer (to prove both directions): **f(x) = x + c for every constant c >= 0, and no others.**

---

modulus-telescope: new
Target: characterize ALL f:R_{>0}->R_{>0} satisfying the sandwich; prove answer = {x+c : c>=0}.
Technique: SOS sufficiency + equality-pinch substitution x=f(y) + quadratic modulus-of-continuity
  |h(a)-h(b)| <= (a-b)^2/(4 min(a,b)) closed by a telescoping (Riemann-sum) limit. No differentiability assumed.
Skeleton:
  1. Sufficiency: f(x)+y=x+f(y), both slacks = (x-f(y))^2>=0 — QM-AM-GM. [SOLID, verified]
  2. x=f(y): left => f(f(y))<=2f(y)-y, right => f(f(y))>=2f(y)-y, so f(f(y))=2f(y)-y. [SOLID]
  3. h=f-id: f^n(y)=y+n h(y) must stay >0 => h>=0. [SOLID]
  4. Right ineq at x=f(t),y=t+p: (2f(t)+p)^2>=4f(t)f(t+p) => h(t+p)-h(t) <= p^2/(4f(t)). [SOLID, verified]
  5. Symmetrize: |h(a)-h(b)| <= (a-b)^2/(4 min(a,b)). [SOLID]
  6. Telescope [t0,t0+L] in N steps: |h(t0+L)-h(t0)| <= L^2/(4 t0 N) -> 0 => h constant. [SOLID]
  7. c>=0; f(x)=x+c. [SOLID]
Key lemmas: f(f(y))=2f(y)-y (pinch collapses QM=GM=f(y)); (U) h(t+p)-h(t)<=p^2/(4f(t)) (quadratic
  AM-GM slack of right ineq at x=f(t)); h const (quadratic modulus telescopes, O(L^2/N)->0).
Open gaps: none conjectural — builder writes the O(p^2) bound and the telescoping limit rigorously;
  confirm step 4 needs only the LEFT direction f(f)<=2f-t plus the RIGHT inequality (no circularity).
Cases to cover: sufficiency + necessity; c=0 and c>0 in, c<0 out.
Watch out for: inequality direction when substituting f(f(t))<=2f(t)-t; uniform constant 1/(4 t0) via f>=id.
  This is the flagship — necessity is essentially complete.

modulus-derivative: new
Target: same whole claim.
Technique: same prefix and same bound (U)/step 5, but close via DIFFERENTIATION: the quadratic modulus
  forces h'==0 everywhere and h continuous, so h constant by the Mean Value Theorem.
Skeleton: steps 1-4 identical to modulus-telescope; then
  5. |h(b)-h(a)|/|b-a| <= |b-a|/(4 min(a,b)) -> 0 => h'(a)=0 for all a; h continuous (Lipschitz on compacts).
  6. h'==0 on the interval (0,inf) + continuity => h const (MVT). c>=0; f(x)=x+c.
Key lemmas: (U) as above; h'==0 (difference quotient -> 0); "derivative 0 on an interval => constant" (MVT).
Open gaps: cite MVT by name; confirm (0,inf) connected so no piecewise-constant escape.
Cases to cover: sufficiency + necessity.
Watch out for: MVT needs continuity (supplied by step 4). Shares lemma (U) with modulus-telescope — kept
  as a cheap alternative FINISH; the field's independence against (U) comes from two-sided-orbit.

two-sided-orbit: new
Target: same whole claim.
Technique: insurance route using the LEFT inequality prominently. Derive an independent LOWER modulus bound
  from the left inequality, get two-sided control |h(a)-h(b)| <= (a-b)^2/(2 min(a,b)), then a NO-calculus
  orbit-interleaving contradiction (arithmetic progressions of different step come within bounded distance
  infinitely often while diverging, squeezing the step difference to 0).
Skeleton:
  1-3. Same prefix (SOS; f(f(y))=2f(y)-y; f^n(y)=y+n h(y); h>=0).
  4. Right upper bound (U). [SOLID]
  5. Left ineq at x=f(t),y=t+p: 2f(t)^2+2f(t+p)^2>=(2f(t)+p)^2 => f(t+p)^2>=(f(t)+p)^2-p^2/2
     => h(t+p)-h(t) >= -p^2/(2(f(t)+p)). [SOLID, verified]
  6. |h(b)-h(a)| <= (b-a)^2/(2 min(a,b)). [SOLID]
  7. If h(a)=c1<c2=h(b): interleave orbits a_n=a+n c1, b_m=b+m c2 so 0<=a_n-b_m<c2 bounded while
     min->inf; step 6 => |c1-c2| <= c2^2/(2 min) -> 0. Contradiction => h const.
Key lemmas: left-ineq lower bound (QM-AM slack, quadratic in p); orbit interleaving via floor (no Kronecker);
  bounded step-gap squeezed by a modulus -> 0.
Open gaps: step 7 fixed-point sub-case c1=0 (a_n=a bounded, min stays finite) needs a separate argument —
  flagged in the file; fallback is step-6 telescoping. Builder must handle it without hand-waving.
Cases to cover: sufficiency; necessity main case (both steps>0) and degenerate case (a step =0).
Watch out for: the c1=0 sub-case is the genuine gap; sign care taking square roots in step 5.

---
Recommendation to outline-reviewer: register all three (genuinely distinct closings of the hard step —
telescoping / MVT / orbit-interleaving). modulus-telescope is the flagship (necessity essentially complete
and fully verified). modulus-derivative is a cheap alternative finish on the same (U). two-sided-orbit is the
independence hedge: it leans on the LEFT inequality and a calculus-free finish, so it survives if (U)'s
right-inequality bound or the limiting finishes are ever disputed.

build set: modulus-telescope, two-sided-orbit
