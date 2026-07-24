## Status
unsolved

## Approaches tried
- (this file) monotone-gap: derive the FE, then extract MONOTONICITY of f from the original
  inequalities and turn order-preservation of iterates into monotonicity of the gap g(x)=f(x)-x.
  A third, order-theoretic framing (distinct from orbit-distance's density argument and bound-pinch's
  analytic pinch) so the field spans three independent mechanisms.

## Current best
Answer to prove: **f(x)=x+c, c>=0**. Construction half identical to orbit-distance (residual
(x-y-c)^2>=0 for both (A) and (B); codomain forces c>=0).

### Uniqueness half — the skeleton
Steps 1-4 (FE, orbits are APs f^n(y)=y+n g(y), g>=0, injectivity) are shared with orbit-distance —
import them (or the certified lemmas). Then:

5. **f is non-decreasing.** Target lemma: x_1 < x_2 ⇒ f(x_1) <= f(x_2). Mechanism to pursue: combine
   the lower bound from (B), f(x) >= 2 sqrt(x f(y)) - y, with the upper bound from (A),
   f(x) <= sqrt(2x^2+2f(y)^2) - y, as x moves and y is held at a well-chosen value; a decrease
   f(x_1) > f(x_2) with x_1<x_2 should contradict (B) (which is increasing in x on the RHS) for a
   suitable y. [This is the load-bearing gap of this route — see HARD STEPS.]

6. **g is non-decreasing.** Since f is order-preserving, so is every iterate: x_1<x_2 ⇒
   f^n(x_1) < f^n(x_2), i.e. x_1 + n g(x_1) < x_2 + n g(x_2) for all n>=0. Dividing by n and letting
   n->∞ gives g(x_1) <= g(x_2). Hence **g is non-decreasing.** (This step is clean once step 5 holds.)

7. **g is constant.** With g non-decreasing and 0 <= g, rule out a strict increase. Mechanism: if
   g(x_1) < g(x_2) for some x_1<x_2, feed a far-separated pair into (A). Using f(y)=y+g(y):
        (A):  (x-y)^2 + 4y g(y) + 2 g(y)^2 >= 2(x+y) g(x) + g(x)^2.
   Send x->∞ with g non-decreasing: the growth of g(x) is bracketed (leading order forces
   limsup g(x)/x <= 1/2), and a non-decreasing non-constant g contradicts the exact orbit-AP
   structure combined with (A)/(B) at large separations. [Second gap — see HARD STEPS. The
   orbit-distance approach closes precisely this via bounded-distance orbit comparison; if step 7
   resists, import that closure.]

8. **Assemble.** g ≡ c constant, so f(x)=x+c; codomain gives c>=0; construction verifies. Answer stated.

### HARD STEPS / gaps to nail down (for the builder)
- **Step 5 (monotonicity of f) is the crux of THIS framing** and is NOT yet established. It may be
  false to prove directly from a single (x,y) pair; likely needs (B) with y chosen adaptively.
  If monotonicity cannot be secured, this whole route stalls — flag for RETHINK and defer to
  orbit-distance (which needs no monotonicity).
- **Step 7 (constant from non-decreasing)** — g non-decreasing alone does NOT force constancy; it is
  order in the SAME direction as identity. Needs the original inequalities at large separation to
  cap g from above, matching the lower cap. This is essentially the same global-constant gap; the
  bounded-distance mechanism in orbit-distance is the known way to finish and can be borrowed here.
- **Watch out:** order-preservation of iterates gives g NON-DECREASING, never non-increasing, so a
  one-sided monotonicity of g is all step 6 yields — do not claim constancy from step 6 alone.

### Cases to cover
- Construction for all c>=0.
- Both a possible strictly-increasing g and constant g in step 7 (the former to be excluded).
