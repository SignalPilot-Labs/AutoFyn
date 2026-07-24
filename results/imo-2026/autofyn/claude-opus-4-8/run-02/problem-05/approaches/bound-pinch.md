## Status
partial

## Approaches tried
- (round 1) bound-pinch, analytic two-sided envelope + inf(f−id) minimizing route (independent of the
  orbit-distance cross-comparison). Established rigorously: the construction half in full; the two
  "master" quadratic reformulations (A′),(B′) of the given inequalities; f(y) ≥ y (via the shared FE
  bootstrap); the well-defined constant c := inf(f−id) ≥ 0; the exact upper-envelope bound (UENV);
  the LEFT/RIGHT propagation lemmas; and the reduction of the whole problem to constancy of g = f−id.
  OUTCOME: partial. The analytic envelope route provably *reduces* the global-constant crux to the same
  structure orbit-distance attacks — the minimizing set is an arithmetic progression of step c and the
  route hits the "fill between AP points / attain the inf" wall. This wall could not be closed by the
  envelope/minimizing-sequence machinery alone (see Current best for the precise open step). This is an
  honest analytic hedge that confirms the field shares one wall on constancy; the construction and all
  one-sided bounds are complete and certifiable.

## Current best

**Answer (to be proved): f(x) = x + c for a constant c ≥ 0, and nothing else.**

### Notation and the two given inequalities
Write the hypothesis as the pair (valid for all x, y > 0), obtained by squaring the outer terms of the
chain (all quantities positive, so squaring is reversible):
- (A):  2(x² + f(y)²) ≥ (f(x) + y)²   [left inequality: QM ≥ mean],
- (B):  (f(x) + y)² ≥ 4x f(y)          [right inequality: mean ≥ GM].

Set g(x) := f(x) − x. Substituting f(x) = x + g(x), f(y) = y + g(y) and expanding (verified with sympy):

- (A′):  (x − y)² + 4y·g(y) + 2g(y)² − 2(x+y)·g(x) − g(x)² ≥ 0,
- (B′):  (x − y)² + g(x)² + 2(x+y)·g(x) − 4x·g(y) ≥ 0.

These are *exact* algebraic equivalents of (A),(B) for all x, y > 0. (Sanity check: with g ≡ c both
residuals collapse to the perfect square (x − y − c)²; see Construction.)

### Part 1 — Construction half (COMPLETE and verified)
Let f(x) = x + c with c a real constant. For every x, y > 0,
  2(x² + f(y)²) − (f(x)+y)² = (x − y − c)²   and   (f(x)+y)² − 4x f(y) = (x − y − c)²,
both identities holding for **every** real c (expand, or sympy: `sp.factor` gives `(x−y−c)²` for each).
Since (x − y − c)² ≥ 0, both (A) and (B) hold, so the whole chain holds. Thus f(x) = x + c satisfies the
functional inequality for every real c.
Codomain constraint: f must map ℝ_{>0} → ℝ_{>0}, i.e. x + c > 0 for all x > 0. Taking x → 0⁺ forces
c ≥ 0. Conversely c ≥ 0 gives x + c > 0 for all x > 0. Hence **exactly the c ≥ 0 members are admissible.**
This proves that every f(x) = x + c, c ≥ 0, is a solution; it remains (Uniqueness) to show there are no
others. ∎ (construction)

### Part 2 — f(y) ≥ y for all y (COMPLETE)
Put x = f(y) into the *whole* chain. The left term becomes √((f(y)²+f(y)²)/2) = √(f(y)²) = f(y) (as
f(y) > 0); the right term becomes √(f(y)·f(y)) = f(y). The chain reads
  f(y) ≥ (f(f(y)) + y)/2 ≥ f(y),
forcing equality throughout, hence the exact functional equation
  (FE):  f(f(y)) = 2f(y) − y   for all y > 0.
Fix y and set x₀ = y, x_{n+1} = f(x_n). (FE) applied at x_n gives x_{n+2} = 2x_{n+1} − x_n, a linear
recurrence with constant first difference: x_{n+1} − x_n = x_1 − x_0 = f(y) − y = g(y) for all n, so
  x_n = y + n·g(y).
Every x_n = f^n(y) is a value of f, hence a positive real. If g(y) < 0 then x_n = y + n g(y) → −∞, so
x_n < 0 for large n — contradiction. Therefore **g(y) ≥ 0, i.e. f(y) ≥ y, for all y > 0.** ∎ (f ≥ id)

(FE is the single shared reduction used here; the constancy argument below does **not** use orbits or the
cross-orbit comparison — it is the independent analytic branch.)

### Part 3 — The constant c := inf_{t>0} g(t) (COMPLETE setup)
By Part 2, g ≥ 0, so the set {g(t) : t > 0} ⊆ [0, ∞) is nonempty and bounded below; its infimum
  c := inf_{t>0} g(t)
exists and satisfies 0 ≤ c ≤ g(1) < ∞. By definition of infimum, g(x) ≥ c for all x, and there is a
minimizing sequence t_k > 0 with g(t_k) → c. **The uniqueness half is exactly the claim g(x) ≤ c for all
x** (then g(x) = c for all x, i.e. f(x) = x + c, and c ≥ 0 by Part 2 or Part 1).

### Part 4 — Exact upper envelope (COMPLETE)
Treat (A′) as a quadratic in g(x): g(x)² + 2(x+y)g(x) − [(x−y)² + 4y g(y) + 2g(y)²] ≤ 0. Since g(x) ≥ 0,
g(x) is at most the positive root, and using 2x²+2y²+4y g(y)+2g(y)² = 2x² + 2(y+g(y))² = 2x² + 2f(y)²,

  (UENV):  g(x) ≤ √(2x² + 2 f(y)²) − x − y     for all x, y > 0.

Equivalently f(x) ≤ √(2x² + 2 f(y)²) − y. This is the analytic upper envelope of f.

### Part 5 — Propagation lemmas (COMPLETE)
From (B′) with y = x + s (s > 0), i.e. bounding g(x+s) by g(x): expanding gives (sympy-verified)
  (RIGHT):  4x·(g(x+s) − g(x)) ≤ (s + g(x))²,      so  g(x+s) − g(x) ≤ (s+g(x))²/(4x).
From (B′) with y = x − s (0 < s < x):
  (LEFT):   4x·(g(x−s) − g(x)) ≤ (g(x) − s)²,      so  g(x−s) − g(x) ≤ (g(x)−s)²/(4x).

Two exact consequences:
- **Left step.** Take s = g(x) in (LEFT) (legitimate whenever x > g(x)): the RHS is 0, so
  g(x − g(x)) ≤ g(x). Combined with g ≥ c: if g(x) = c and x > c then c ≤ g(x−c) ≤ c, so g(x−c) = c.
- **Right step (from UENV).** If a is a minimizer, g(a) = c, then f(a) = a + c and (UENV) with y = a gives
  g(x) ≤ √(2x² + 2(a+c)²) − x − a for all x. Evaluating at x = a + c:
  g(a+c) ≤ √(2(a+c)² + 2(a+c)²) − (a+c) − a = 2(a+c) − 2a − c = c, so with g ≥ c, **g(a+c) = c**.
  (For x ≠ a+c the bound is > c, since 2x²+2(a+c)² − (x+a+c)² = (x − a − c)² > 0; so a single minimizer
  pins the gap only at the shifted point a+c.)

### Part 6 — Reduction achieved, and the open step (the crux wall)
Combining the two steps of Part 5: **if the infimum c is attained at some point a (g(a) = c), then the
minimizing set S = {t : g(t) = c} contains the full arithmetic progression {a + kc : k ∈ ℤ} ∩ (0, ∞)**
(closed under +c by the right step and under −c by the left step). Near each AP point a+kc the envelope
(UENV) forces g(x) ≤ c + O((x − (a+kc))²), so g is squeezed to c on the AP and is within O(c²) of c
between consecutive AP points, but is **not** pinned to c strictly between them.

**Open step (honest gap).** Two intertwined obstructions remain, and the analytic envelope/minimizing-
sequence machinery does not close them:
1. *Attainment.* Without continuity of f, the infimum c need not be attained, so the AP of minimizers may
   be empty; the minimizing sequence t_k need not converge, converge to a positive point, or go to ∞ in a
   controlled way. Every attempt to feed t_k into (UENV) or (B′) to bound g(x) at a *fixed* target x is
   defeated by the term (x − t_k)², which dominates unless t_k stays within *bounded distance* of x.
2. *Filling between AP points.* Even granting attainment, propagation moves the gap-value c only in steps
   of exactly c; pinning g(x) = c for an x strictly between two AP minimizers requires comparing points at
   bounded distance across different "phases" — precisely the cross-orbit bounded-distance comparison that
   the orbit-distance approach performs. The envelope route provably *reduces to* this same comparison
   rather than bypassing it.

Consequently the two-sided-envelope framing reaches the identical global-constant wall as the other
framings; it does not independently surmount it. Per the approach's own contingency note, the constancy
step defers to the orbit-distance cross-comparison. Everything up to and including the reduction
(Parts 1–6) is complete and rigorous; the single remaining step is g(x) ≤ c for all x, equivalently the
filling of the AP established in Part 6.

**Net rigorous progress this round:** the construction half is fully proved and verified; f ≥ id, the
master inequalities (A′),(B′), the exact upper envelope (UENV), the propagation lemmas (LEFT)/(RIGHT),
and the reduction of uniqueness to constancy of g are all proved. The uniqueness half is reduced to a
single explicit inequality (g ≤ c everywhere) whose closure needs the bounded-distance cross-comparison.

## Promotable lemmas
- **Master reformulation (A′),(B′).** For every x, y > 0, with g = f − id:
  (A′) (x−y)² + 4y g(y) + 2g(y)² − 2(x+y)g(x) − g(x)² ≥ 0 and
  (B′) (x−y)² + g(x)² + 2(x+y)g(x) − 4x g(y) ≥ 0, exactly equivalent to (A),(B). Proved in Notation
  section (sympy-verified). Reusable by any approach.
- **Construction lemma.** For every real c, 2(x²+f(y)²)−(f(x)+y)² = (f(x)+y)²−4x f(y) = (x−y−c)² when
  f = id + c; hence f(x)=x+c solves the chain, and codomain forces c ≥ 0. Proved in full in Part 1.
- **f ≥ id lemma.** From the chain, f(f(y)) = 2f(y) − y (FE), whence f^n(y) = y + n(f(y)−y) and positivity
  forces f(y) ≥ y for all y. Proved in full in Part 2.
- **Upper envelope (UENV).** f(x) ≤ √(2x² + 2 f(y)²) − y for all x, y > 0. Proved in Part 4.
- **Propagation lemmas (LEFT)/(RIGHT).** 4x(g(x±s) − g(x)) ≤ (g(x) ∓ s)² (signs as in Part 5). Proved in
  Part 5, sympy-verified.
