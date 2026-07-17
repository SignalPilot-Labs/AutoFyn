## Status
solved

## Approaches tried
- (round 1, this file) Legendre/convex-conjugate reformulation: substitute a=√x to read the right
  inequality (R) as a family of support lines a↦2√(f(y))·a−y beneath the convex profile
  Φ(a):=f(a²). The pure "conjugate is tight everywhere" plan (outline Step 3) fails: tightness in (R)
  holds only at x∈image(f)=(inf f,∞)-type set, so Φ=Ψ can fail below the image (concretely, for
  f=x+c one has Φ(a)=a²+c=Ψ(a) only for a≥√c). Resolved by keeping the support-line reading as the
  organizing frame and closing the growth comparison rigorously via the squared support inequality
  (the off-diagonal lever (∗)) read along orbits, plus an openness/connectedness finish for the
  fixed-point coexistence. Result: COMPLETE proof of both directions.

## Current best
Full characterization proved: f(x)=x+c for every constant c≥0, and no others. See Full proof.

## Full proof

Throughout, R>0 denotes the positive reals and f:R>0→R>0. Write the two hypotheses as, for all
x,y>0,
  (L)  √((x²+f(y)²)/2) ≥ (f(x)+y)/2,
  (R)  (f(x)+y)/2 ≥ √(x·f(y)).
All quantities appearing are positive, so squaring preserves the inequalities:
  (L²)  2(x²+f(y)²) ≥ (f(x)+y)²,
  (R²)  (f(x)+y)² ≥ 4x·f(y).

We prove the solution set is exactly {f(x)=x+c : c≥0}.

---

### Part (a). Sufficiency: every f(x)=x+c with c≥0 works.

First, f(x)=x+c maps R>0 into R>0 iff x+c>0 for every x>0, i.e. iff c≥0 (for c<0 and x∈(0,−c) we
get f(x)≤0, outside the codomain). So we take c≥0.

Substitute f(t)=t+c. For (R²):
  (f(x)+y)² − 4x·f(y) = (x+c+y)² − 4x(y+c) = (x−y−c)² ≥ 0,
an algebraic identity (verified by expansion:
(x+c+y)²−4x(y+c)=x²+y²+c²−2xy−2xc+2yc=(x−y−c)²). Hence (R²) holds, and since both sides of (R) are
positive, (R) holds.

For (L²):
  2(x²+f(y)²) − (f(x)+y)² = 2x²+2(y+c)² − (x+c+y)² = (x−(y+c))² = (x−y−c)² ≥ 0,
again an identity (with w:=y+c, 2x²+2w²−(x+w)²=(x−w)²). Hence (L²) holds, and (L) follows.

So both inequalities hold for every c≥0. This is the "SOS" content: both squared gaps equal the
single square (x−y−c)². ∎(a)

---

### Part (b). Necessity: any admissible f has the form f(x)=x+c, c≥0.

We use the convex/support-line ("Legendre") reading of (R) as the organizing frame, and close the
argument with the squared support inequality read along orbits.

#### Step 1. The diagonal collapse (★), injectivity, and g:=f−id ≥ 0.

Put x=f(y) in (R²) and (L²).

(R²) at x=f(y): (f(f(y))+y)² ≥ 4f(y)·f(y) = (2f(y))², and both sides positive, so
  f(f(y)) + y ≥ 2f(y).
(L²) at x=f(y): 2(f(y)²+f(y)²) ≥ (f(f(y))+y)², i.e. (2f(y))² ≥ (f(f(y))+y)², so
  f(f(y)) + y ≤ 2f(y).
Combining,
  (★)  f(f(y)) = 2f(y) − y   for all y>0.

Injectivity. If f(y₁)=f(y₂), then f(f(y₁))=f(f(y₂)); by (★), 2f(y₁)−y₁=2f(y₂)−y₂, and f(y₁)=f(y₂)
gives y₁=y₂. So f is injective.

Orbits are arithmetic; g≥0. Fix y and set aₙ:=fⁿ(y) (n≥0, a₀=y). Applying (★) at fⁿ(y),
  a_{n+2} = f(f(aₙ)) = 2f(aₙ) − aₙ = 2a_{n+1} − aₙ,  i.e.  a_{n+1}−aₙ = a₁−a₀ = f(y)−y
for all n. Hence, with g(y):=f(y)−y,
  aₙ = fⁿ(y) = y + n·g(y)   for all n≥0.
Since every aₙ>0 and this must hold for all n≥0, we cannot have g(y)<0 (otherwise y+n g(y)<0 for n
large). Therefore
  g(y) = f(y) − y ≥ 0   for all y>0.

Orbit-invariance of g. From (★), g(f(y)) = f(f(y))−f(y) = (2f(y)−y)−f(y) = f(y)−y = g(y). By
iteration g(fⁿ(y)) = g(y) for all n≥0. In particular, writing y↦f(y) etc., every point of the orbit
{y+n g(y): n≥0} has the same g-value g(y). (†)

#### Step 2. The support-line (Legendre) reading of (R), and the master lever (∗).

Substitute a=√x (a bijection of (0,∞) onto itself, x=a²). Then (R) reads
  f(a²) ≥ 2√(f(y))·a − y   for all a>0, y>0.
Thus the convex profile Φ(a):=f(a²) lies above every affine line ℓ_y(a):=2√(f(y))·a − y; each y
contributes a support line of slope 2√(f(y))>0. This is exactly the statement that Φ dominates the
Legendre-type envelope Ψ(a):=sup_{y>0}[2√(f(y))a−y] (a convex, nondecreasing function, being a
supremum of increasing affine maps). The equality case of (R) — where a support line touches Φ —
occurs precisely at x=f(y) (the diagonal collapse of Step 1). Reading how the touching support lines
grow along an orbit is what forces the profile.

To run this quantitatively we use the squared form of the support inequality. Writing f=id+g and
expanding (R²) with x=a, y=b (renaming variables):
  (a+g(a)+b)² − 4a(b+g(b)) = (a−b)² + 2(a+b)g(a) + g(a)² − 4a·g(b),
an identity (verified by expansion). Since (R²) says the left side is ≥0,
  (∗)  (a−b)² + 2(a+b)g(a) + g(a)² ≥ 4a·g(b)   for all a,b>0.
This is the squared support inequality: it packages, for each pair, how the support slope at b
(namely 2√(f(b)), whose square is 4f(b)=4(b+g(b))) is bounded by the profile value at a.

#### Step 3. All positive defects are equal (the growth-rate comparison).

Claim. If g(a)>0 and g(b)>0 then g(a)=g(b).

Write s:=g(a)>0, t:=g(b)>0. By Step 1 the orbits
  Aₙ := a + n·s = fⁿ(a),   Bₘ := b + m·t = fᵐ(b)   (n,m ≥ 0)
escape to +∞ (s,t>0), and by (†) g(Aₙ)=s, g(Bₘ)=t for all n,m.

For each n, choose m=m(n) to be the largest integer m≥0 with Bₘ ≤ Aₙ; this exists for all large n
(as Aₙ→∞) and m(n)→∞, and by maximality Bₘ₊₁=Bₘ+t>Aₙ, so
  0 ≤ Aₙ − B_{m(n)} < t.   (‡)
This is the interleaving of the two orbits: a point of orbit(a) trapped within t of a point of
orbit(b), with both →∞.

Apply (∗) with the pair (Aₙ, B_{m(n)}), using g(Aₙ)=s and g(B_{m(n)})=t:
  (Aₙ − B_{m(n)})² + 2(Aₙ + B_{m(n)})·s + s² ≥ 4Aₙ·t.
Divide by Aₙ>0:
  (Aₙ−B_{m(n)})²/Aₙ + 2s·(Aₙ+B_{m(n)})/Aₙ + s²/Aₙ ≥ 4t.
Estimate each term as n→∞ (so Aₙ→∞):
 • by (‡), (Aₙ−B_{m(n)})² < t², so the first term < t²/Aₙ → 0;
 • by (‡), Aₙ−t < B_{m(n)} ≤ Aₙ, so B_{m(n)}/Aₙ → 1, hence (Aₙ+B_{m(n)})/Aₙ → 2 and the second term
   → 4s;
 • the third term s²/Aₙ → 0.
Therefore the left side converges to 4s. Since it is ≥ 4t for every n, passing to the limit gives
4s ≥ 4t, i.e. g(a) ≥ g(b). By symmetry (swap the roles of a and b) g(b) ≥ g(a). Hence g(a)=g(b),
proving the Claim.

Consequently, on the set P:={y>0 : g(y)>0} the function g is constant, say g≡c with c>0 (if P≠∅).
Let Z:={y>0 : g(y)=0} be the set of fixed points of f (there f(y)=y). Thus (0,∞)=P⊔Z with g≡c on P
and g≡0 on Z.

#### Step 4. Fixed points cannot coexist with positive defect (openness + connectedness).

Suppose, for contradiction, that c>0 and both P and Z are nonempty.

Cross-constraint. Apply (∗) with a=z∈Z (so g(z)=0) and b∈P (so g(b)=c):
  (z−b)² + 2(z+b)·0 + 0² ≥ 4z·c,  i.e.  (b−z)² ≥ 4cz   for all z∈Z, b∈P.   (♣)
Since c>0 and z>0, the right side 4cz is strictly positive; so |b−z| ≥ 2√(cz) > 0: every fixed point
z is bounded away from every point of P by a positive amount.

P is open in (0,∞). Fix b∈P and put δ:=min(b/2, √(cb)) > 0. Take any point w with |w−b|<δ and
suppose w∈Z. Then (♣) applies with z=w, giving (b−w)² ≥ 4cw. But |w−b|<δ≤b/2 forces w>b−δ≥b/2,
hence 4cw > 4c(b/2) = 2cb, while (b−w)² < δ² ≤ (√(cb))² = cb. Therefore
(b−w)² < cb < 2cb < 4cw, contradicting (♣). Hence no such w lies in Z, so w∈P. Thus the interval
(b−δ,b+δ)∩(0,∞)⊆P, and P is open.

Z is open in (0,∞). Fix z∈Z and put r:=2√(cz)>0. For any point w with |w−z|<r: if w∈P then (♣)
applies with b=w, giving (w−z)² ≥ 4cz = r², i.e. |w−z|≥r, contradicting |w−z|<r. Hence no such w
lies in P, so w∈Z. Thus (z−r,z+r)∩(0,∞)⊆Z, and Z is open.

Now (0,∞)=P⊔Z is a partition of the connected space (0,∞) into two disjoint open sets, both assumed
nonempty. This contradicts connectedness of the interval (0,∞) (a connected topological space admits
no partition into two nonempty open subsets). Therefore one of P, Z is empty.

#### Step 5. Conclusion.

By Step 4 exactly one of the following holds:
 • Z=(0,∞): then g≡0, i.e. f(x)=x for all x (this is f(x)=x+c with c=0);
 • P=(0,∞): then g≡c for a single constant c>0, i.e. f(x)=x+c for all x.
In both cases f(x)=x+c for a single constant c≥0. (The degenerate possibility that the growth
comparison of Step 3 is vacuous — namely P=∅ — is the first case; the case P≠∅ is handled by Steps 3
and 4.)

Together with Part (a) (which shows every such f is admissible and forces c≥0 by the codomain), the
complete solution set is
  f(x) = x + c,   c ≥ 0. ∎

---

### Verification of the final answer.

For f(x)=x+c with c≥0 and any x,y>0, both squared gaps equal (x−y−c)²≥0 (Part (a)), so
√((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ √(x·f(y)) holds with equality exactly when x=y+c=f(y). Conversely
Part (b) shows no other f can satisfy the sandwich. Hence the answer f(x)=x+c, c≥0, is verified in
both directions.

## Promotable lemmas

- **Shared lemma `diagonal-collapse` (★) + basics.** For any admissible f: f(f(y))=2f(y)−y for all
  y>0; f is injective; fⁿ(y)=y+n·g(y) with g:=f−id ≥ 0; and g is orbit-invariant, g(f(y))=g(y).
  Proved in Step 1 from (R²),(L²) at x=f(y) and orbit positivity. (Same statement other approaches
  need; certify once.)
- **Shared lemma `off-diagonal-lever` (∗).** For any admissible f, writing g=f−id:
  (a−b)² + 2(a+b)g(a) + g(a)² ≥ 4a·g(b) for all a,b>0. Proved in Step 2 as the identity
  (a+g(a)+b)²−4a(b+g(b)) = (a−b)²+2(a+b)g(a)+g(a)²−4a g(b) applied to (R²).
- **Lemma `defects-equal-and-no-coexistence`.** For any admissible f, g=f−id is a constant c≥0.
  Proved in Steps 3–4 (orbit-interleaving growth comparison + openness/connectedness). Reusable to
  finish any approach that reaches g:R>0→{0}∪{c}.
