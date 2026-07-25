## imo-2026-05

Answer (all four approaches target this whole claim): **f(x) = x + c for every constant
c ≥ 0, and no others.** Shared, proved-for-every-solution scaffolding (in each file):
Lemma A f(f(y))=2f(y)−y (x=f(y) forces both bounds tight); Lemma B f injective; Lemma C
d(y):=f(y)−y is orbit-invariant, fⁿ(y)=y+n·d(y), d(y)≥0. Easy direction COMPLETE in every
file: R-defect = L-defect = ((x−y)−c)²≥0, positivity ⟹ c≥0. The whole game is exhaustiveness:
force d ≡ const. The four routes attack that by GENUINELY DIFFERENT means.

---
orbit-crossing: new  [STRONGEST — near-complete]
Target: characterize all f (answer f(x)=x+c, c≥0).
Technique: cross-orbit marching — bounded-gap approximation of two arithmetic-progression
orbits + the R inequality across them.
Skeleton:
  1. Lemmas A,B,C — as above.
  2. R-test: R at (x,y)=(f(p),q) ⟺ (p−q)² ≥ 4(b−a)(p+a), a=d(p),b=d(q). [sympy-verified]
  3. L-test: L at (f(p),q) ⟺ (p−q)² ≥ 2(a−b)(a+b+2q). [sympy-verified]
  4. Main Lemma (COMPLETE): if d takes two positive values a<b, march Pₘ=p₀+ma→∞ keeping
     Qₙ=q₀+nb within gap <b (choose n=⌊(p₀+ma−q₀)/b⌋); R-test gives bounded ≥ 4(b−a)Pₘ→∞,
     contradiction. So d takes ≤1 positive value ⟹ d∈{0,b}.
  5. Residual: rule out fixed points F and shift-set G both nonempty.
Key lemmas:
  - Main Lemma d has ≤1 positive value — because a bounded (x−y)² cannot dominate a linear
    RHS that →∞ once the two orbits are kept within a fixed gap. [the crux move]
Open gaps: step 5, the {0,b} sub-case (F,G both nonempty). Levers supplied: raw R gives
  (x−y)²≥4bx so F,G are separated; envelope identity; extremal nearest-pair.
Cases to cover: existence DONE; two-positive-values DONE; {0,b} GAP.
Watch out for: Main Lemma NEEDS the smaller value >0 (orbits must march); that is precisely
  why the leftover case is a=0 (fixed points). Don't chase large-n telescoping (square term
  dominates).

---
monotonicity-orbits: new
Target: characterize all f.
Technique: order rigidity — f nondecreasing ⟹ d nondecreasing ⟹ (with ≤1 positive value)
a threshold, killed by a near-threshold R-violation.
Skeleton:
  1. Lemmas A,B,C.
  2. GAP: f nondecreasing (lever: R,L sandwich 2√(x f(y))−y ≤ f(x) ≤ √(2x²+2f(y)²)−y, both
     increasing in x; show f = sup_y of the lower envelope).
  3. Lemma D (COMPLETE given 2): fⁿ(u)≤fⁿ(v) ⟹ n(d(u)−d(v))≤v−u ∀n ⟹ d nondecreasing.
  4. Finish (COMPLETE given ≤1 positive value, importable from orbit-crossing): threshold t,
     take x→t⁻∈F, y→t⁺∈G, R gives (x−y)²≥4bx → 0≥4bt>0, contradiction.
Key lemmas:
  - d nondecreasing — because f nondecreasing makes each iterate order-preserving and the
    orbit-AP slopes cannot invert without the faster orbit overtaking.
  - near-threshold R-violation — because R-defect=(x−y)²−4bx → −4tb<0 as x,y→t. [sympy-verified]
Open gaps: GAP 2 (monotonicity of f) — the distinct wall of this route.
Cases to cover: existence DONE; d monotone DONE (given GAP); threshold DONE.
Watch out for: monotonicity proof must avoid assuming continuity; make "f = envelope" rigorous.

---
shift-family-sos: new
Target: characterize all f.
Technique: direct quadratic-form squeeze — reduce both inequalities to two-variable
inequalities in a=d(x),b=d(y) and force a=b uniformly (handles ALL cases in one framing,
including the {0,b} case orbit-crossing leaves open).
Skeleton:
  1. Lemmas A,B,C.
  2. Reduced forms: R′ (x−y)²+a²+2a(x+y)−4bx ≥0; L′ (x−y)²−2a(x+y)+4by+2b²−a² ≥0.
  3. GAP: show these force a=b ∀x,y. Levers: R′ tight at x=f(y); combine R′-upper-control
     and L′-lower-control (mirrored (x,y)/(y,x)) to sandwich a,b.
Key lemmas:
  - R′ is tight exactly at x=f(y) — because that is the AM-GM equality locus, giving d(y) as
    an infimum whose minimizer pins the relation between orbits.
Open gaps: the a=b pin (whole exhaustiveness).
Cases to cover: existence DONE; a=b GAP.
Watch out for: large-n substitutions are vacuous (square term dominates); the bite is at
  comparable x,y. Also usable: the sympy-verified R-test/L-test from orbit-crossing.

---
variational-min: new
Target: characterize all f.
Technique: envelope/optimization — f is its own lower envelope f(y)=min_x (f(x)+y)²/(4x),
minimizer x=f(y); tangency of two envelopes forces d constant.
Skeleton:
  1. Lemmas A,B,C.
  2. Envelope identity (♦): f(y)=min_{x>0}(f(x)+y)²/(4x), attained at x=f(y) (via Lemma A).
  3. GAP 1: minimizer map y↦f(y) monotone. GAP 2: tangency ⟹ d constant, tested by L at
     (x,y)=(f(u),v): defect (u−v)²+2(b−a)(a+b+2v), force ≥0 only when a=b.
Key lemmas:
  - Envelope identity — because R says f(y)≤(f(x)+y)²/(4x) for all x, and Lemma A certifies
    equality at x=f(y), so the ≤ is a genuine attained min.
Open gaps: GAP 1 (monotone minimizer) + GAP 2 (tangency pin).
Cases to cover: existence DONE; envelope pin GAP.
Watch out for: the min is attained (use Lemma A), no smoothness; the load-bearing check is
  the L-at-(f(u),v) defect sign.

---
Diversity note: four distinct organizing principles — cross-orbit marching (metric/growth),
order rigidity (monotonicity), uniform quadratic-form algebra, and variational envelope.
orbit-crossing is near-complete (only the {0,b} sub-case open); shift-family-sos and
monotonicity-orbits both independently attack that residual by different mechanisms, so the
field does not share one wall.

build set: orbit-crossing, shift-family-sos, monotonicity-orbits, variational-min
</content>
