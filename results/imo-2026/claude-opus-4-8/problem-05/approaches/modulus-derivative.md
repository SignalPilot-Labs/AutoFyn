# Approach: modulus-derivative

## Status
partial

## Target (whole problem)
Find all f: R_{>0}->R_{>0} with sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y)) for all x,y>0.
Answer: f(x)=x+c, c>=0.

## Route (spine)
Same easy prefix (SOS sufficiency; x=f(y) pinch => f(f(y))=2f(y)-y; h>=0; the quadratic bound (U)),
but the HARD "h constant" step is closed by a differentiation/MVT finish instead of telescoping:
the bound |h(a)-h(b)| <= (a-b)^2/(4 min(a,b)) makes every difference quotient vanish, so h is
differentiable with h'==0 everywhere and continuous, hence constant by the Mean Value Theorem.

## Skeleton
1. Sufficiency (SOS, slack (x-f(y))^2). [SOLID — see modulus-telescope step 1]
2. x=f(y) pinch => f(f(y))=2f(y)-y. [SOLID]
3. h=f-id >= 0 via f^n(y)=y+n h(y) positivity. [SOLID]
4. (U): h(t+p)-h(t) <= p^2/(4 f(t)); symmetrized to |h(a)-h(b)| <= (a-b)^2/(4 min(a,b)). [SOLID]
5. **Derivative finish.** For fixed a: |h(b)-h(a)|/|b-a| <= |b-a|/(4 min(a,b)) -> 0 as b->a.
   So h is differentiable at every a with h'(a)=0. Also step 4 => h is (locally Lipschitz, hence)
   continuous. A continuous function with h'==0 on the interval (0,infty) is constant (MVT / KB
   "Direct proof"). So h == c. [needs the standard "derivative 0 => constant" lemma cited precisely]
6. c>=0 from step 3; f(x)=x+c. [SOLID]

## Key lemmas (claim + mechanism)
- (U): h(t+p)-h(t) <= p^2/(4f(t)) — quadratic AM-GM slack of the right inequality at x=f(t).
- h'==0 everywhere — because the difference quotient is bounded by |b-a|/(4 min(a,b)) -> 0.
- h'==0 + continuity => constant — Mean Value Theorem on the connected domain (0,infty).

## Open gaps
- Step 5 relies on MVT (requires h continuous, supplied by step 4's Lipschitz-on-compacts bound).
  Builder must state the "differentiable with zero derivative => constant" theorem by name and confirm
  the domain (0,infty) is an interval (connected) so no piecewise-constant escape.

## Cases to cover
- Sufficiency + necessity; c=0 and c>0 included, c<0 excluded.

## Watch out for
- MVT needs h continuous on [a,b] and differentiable on (a,b): both hold globally here. Do not skip citing continuity.
- This shares lemma (U) with modulus-telescope; if (U) were ever disputed both fall — that is why the field also carries an L-based route (two-sided-orbit).
