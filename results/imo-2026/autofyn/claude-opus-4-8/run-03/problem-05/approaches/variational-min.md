## Status
partial

## Approaches tried
- (this file) Variational characterization: express d(y) as an infimum over x of an
  explicit expression, with the minimizer x=f(y), then use the "tangency at the
  minimizer" between two orbits to force d constant.

## Current best
Answer conjectured: **f(x) = x + c for every constant c ≥ 0** (and no others).

### Shared facts (proved for EVERY solution f) — same as shift-family-sos
- **Lemma A:** f(f(y)) = 2f(y) − y  (set x=f(y) in both squared inequalities L,R).
- **Lemma B:** f injective.
- **Lemma C:** d(y):=f(y)−y satisfies d(f(y))=d(y), fⁿ(y)=y+n d(y), and d(y) ≥ 0.
  Squared hypotheses: L(x,y): 2(x²+f(y)²)≥(f(x)+y)²;  R(x,y): (f(x)+y)²≥4x f(y).

### Easy direction (all f(x)=x+c, c≥0, work) — COMPLETE
Both defects equal ((x−y)−c)²≥0 (see shift-family-sos for the two-line expansion);
codomain positivity forces c≥0. ∎(easy)

## Route to exhaustiveness (this approach's distinct spine: optimization / tangency)
Rewrite R as a bound on d(y). With f(x)=x+d(x), f(y)=y+d(y):
  R(x,y) ⟺ 4x·f(y) ≤ (f(x)+y)²
  ⟹ **f(y) ≤ (f(x)+y)² / (4x)  for ALL x>0.**   (★)
So f(y) ≤ inf_{x>0} (f(x)+y)²/(4x). By AM-GM, (f(x)+y)²/(4x) is minimized in the
"variable" f(x)+y over x, and Lemma A says equality in R holds at x=f(y): plug x=f(y),
using f(f(y))=2f(y)−y, RHS = (2f(y)−y+y)²/(4f(y)) = (2f(y))²/(4f(y)) = f(y). Hence

  **f(y) = min_{x>0} (f(x)+y)²/(4x),  attained at x = f(y).**   (♦)

This is a clean variational identity: f is its own "Legendre-type" envelope, and the
unique... (Lemma B) minimizer is x=f(y).

**Key structural consequence to exploit (GAP 1).** Fix two arguments u,v. Both (♦) at
y=u and at y=v are envelopes of the SAME family {(f(x)+·)²/(4x)}. The minimizer map
y ↦ f(y) is therefore monotone (envelope of affine-in-y¹ᐟ²... ) — establish that
y↦f(y) is strictly increasing from (♦) [the minimizer of a parametrized min of the
form min_x (g(x)+y)²/(4x) moves monotonically in y]. 

**Then GAP 2 (pin d constant via tangency).** At the minimizer x*=f(y) the "first-order"
balance in (♦) is (f(x*)+y)/(2x*)·f'-type condition; without differentiability, use the
discrete comparison: for any x, (f(x)+y)² ≥ 4x f(y) with equality at x=f(y). Take two
points y=u (min at f(u)) and y=v (min at f(v)); subtract the two envelope identities and
use that the SAME g(x)=f(x) supports both. Show the common supporting family forces
f(x)−x ≡ const: if d(u)≠d(v), the two tangency/equality points x=f(u),x=f(v) give a pair
(x,y) plugged back into L that violates 2(x²+f(y)²)≥(f(x)+y)². Concretely, evaluate L at
x=f(u), y=v: gap is 2(f(u)²+f(v)²) − (f(f(u))+v)² = 2(f(u)²+f(v)²) − (2f(u)−u+v)²;
force ≥0 and show it FAILS unless d(u)=d(v).

## Cases to cover
- Existence: DONE.
- Exhaustiveness via (♦): GAP 1 (monotone minimizer) + GAP 2 (tangency ⟹ d const).

## Watch out for
- The min in (♦) is a genuine minimum (attained), not just inf — use Lemma A to certify
  the minimizer x=f(y); do not assume smoothness.
- The concrete test L at (x,y)=(f(u),v): compute 2(f(u)²+f(v)²)−(2f(u)−u+v)² symbolically
  in a=d(u),b=d(v); this is the likely clean pin — verify it reduces to a form ≥0 only
  when a=b. (Check the sign carefully; this is the load-bearing computation.)
- No continuity assumed; keep everything algebraic.
</content>
</invoke>
