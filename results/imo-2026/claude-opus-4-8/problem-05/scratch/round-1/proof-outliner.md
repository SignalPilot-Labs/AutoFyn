## imo-2026-05

**Answer (all four approaches target this):** f(x) = x + c for every constant c ≥ 0, and no others.
Sufficiency verified symbolically + numerically (0 violations for c∈{0,0.5,5}); both inequalities
squared collapse to (x−y−c)²≥0. c≥0 is forced by the R>0 codomain. Any outline concluding f=id is
WRONG (misses c>0). Necessity is the hard direction: prove g(y):=f(y)−y is a global constant.

Field: 4 rival NEW approaches (population was empty). All share three cheap, fully-provable facts
(state as certified lemmas, do not re-litigate): (★) f(f(y))=2f(y)−y from x=f(y); injectivity;
f≥id with g orbit-invariant. They DIVERGE at the constancy gap via four different machineries:
extremal limit / convex duality / order+continuity / finite contradiction — kept far apart so they
don't share one wall. The off-diagonal lever (∗) (R squared, f=id+g) is
  (a−b)² + 2(a+b)g(a) + g(a)² ≥ 4a·g(b)  ∀a,b>0
— I verified it is exactly what the two-level counterexample violates (1 < 8 at a=1,b=2).

---

orbit-interleaving: new   [STRONGEST — advance candidate; carry the constancy the furthest]
Target: full characterization f(x)=x+c, c≥0.
Technique: functional equation (★) → orbit = arithmetic progression → two-AP interleaving at ∞ via (∗).
Skeleton:
  1. Sufficiency: (R),(L) squared reduce to (x−y−c)² ≥ 0 — by algebra (shared lemma `suff-affine`).
  2. x=f(y) collapses sandwich to equality f(f(y))=2f(y)−y — by QM=GM at repeated argument.
  3. Orbit aₙ=fⁿ(y)=y+n·g(y); positivity ⇒ g≥0; g(f(y))=g(y) ⇒ g constant on AP {y+n g(y)}.
  4. (∗): (a−b)²+2(a+b)g(a)+g(a)² ≥ 4a g(b) — R squared with f=id+g.
  5. KEY: all positive defects equal — interleave O(a),O(b) at ∞, divide (∗) by 4A→∞ ⇒ g(b)≤g(a).
  6. Residual: exclude a zero of g coexisting with positive value c.
Key lemmas (claim + mechanism):
  - `all-positive-defects-equal` — because for g(a),g(b)>0, picking A=a+k·g(a)→∞ and B in O(b) with
    |A−B|<g(b), (∗) gives 4A·g(b) ≤ g(b)²+4A·g(a)+g(a)²; ÷4A, A→∞ ⇒ g(b)≤g(a); symmetric ⇒ equal.
  - `no-fixed-point` (GAP) — because (R) at (z,b) gives (b−z)²≥4cz for every b∈P; and swapped (∗)
    forces g(b)=c whenever some positive point sits within 2√(cb); reduce to "P not separated from
    any point" and finish.
Open gaps: Step 6 `no-fixed-point` ONLY (rule out fixed point coexisting with defect c>0). Steps 1–5
  are expected fully rigorous.
Cases to cover: c=0 (f=id) and c>0, in sufficiency and final answer; zero-set empty vs nonempty.
Watch out for: Step 5 needs BOTH orbits infinite (g>0) — that's why zeros are quarantined to Step 6,
  not folded in. Don't stop at f=id.

---

mixed-defect-contradiction: new   [same residual as orbit-interleaving but a FINITE-contradiction framing]
Target: full characterization.
Technique: extremal element (inf/sup g) + two-point contradiction, aimo-0481 "rule out mixed branches" template.
Skeleton:
  1. Sufficiency (`suff-affine`).  2. (★), injectivity, f≥id, g≥0, (∗) and swap (∗').
  3. Assume g nonconstant: c₁=inf g < c₂=sup g. Pick near-extreme a,b; interleave orbits; (∗)÷4A→∞
     ⇒ g(b)≤g(a) ⇒ contradiction with c₁<c₂ (handles c₂=∞ too).
  4. Residual mixed-zero case via single-pair (∗): (b−z)²≥4cz for all defect-c points b — contradict.
Key lemmas:
  - `separate-defects-contradict` — because interleaved orbits give controlled |A−B| at large A, and
    (∗)÷4A pins g(b)≤g(a); two different extreme labels cannot coexist.
  - `kill-mixed-zero` (GAP) — because (b−z)²≥4cz must hold for every positive-defect b, contradicted
    by an admissible b near z (finite version of orbit-interleaving's gap).
Open gaps: `kill-mixed-zero`.
Cases to cover: c₁<c₂ both positive (closed); c₁=0 attained with c₂>0 (gap); constant (target).
Watch out for: a single pair does NOT force g(a)=g(b) (tight at a−b=c for the true answer) — the
  contradiction needs the many-pair orbit interleaving, not one substitution.

---

convex-duality: new   [genuinely different closing — convex analysis, no orbit interleaving]
Target: full characterization.
Technique: substitute a=√x to read (R) as a Legendre/support inequality; convexity + tightness ⇒ affine.
Skeleton:
  1. Sufficiency (`suff-affine`).  2. (★), f≥id, g≥0 (shared).
  3. (R) ⇒ f(a²) ≥ sup_y[2√(f(y))·a − y] =: Ψ(a): a sup of affine functions ⇒ Ψ convex, nondecreasing.
  4. Equality attained at each a (x=f(y) tightness) ⇒ f(a²)=Ψ(a) exactly, so f(·²) is convex/conjugate.
  5. (L) gives a matching upper conjugate; lower=upper ⇒ the profile 2√(f(y)) is affine ⇒ f(x)=x+c.
Key lemmas:
  - `conjugate-tight` (GAP) — because x=f(y) is the equality case of (R); must show the equality
    locus covers all a>0 (image/cofinality of f), so f(a²) equals its conjugate everywhere.
  - `dual-cap` + affineness (GAP) — because a convex function tight against conjugates from BOTH (R)
    and (L) has no slack, forcing supporting lines to a single affine profile ⇒ g constant.
Open gaps: `conjugate-tight` (tightness at every a without assuming surjectivity), and the convex
  "two-sided tight ⇒ affine" extraction.
Cases to cover: c=0, c>0; non-attained sup excluded by tightness.
Watch out for: do NOT assume f continuous — convexity of Ψ is FREE as a sup of affine maps; f's image
  may not be all of R>0, so justify tightness at each a via (★) directly, not surjectivity.

---

monotone-continuity: new   [order/topology framing — earns continuity from the inequalities]
Target: full characterization.
Technique: prove f strictly increasing then continuous from (R)/(L); then affine iterate + connectedness.
Skeleton:
  1. Sufficiency (`suff-affine`).  2. (★), injectivity, f≥id, g≥0.
  3. `f-increasing`: from the strictly-increasing lower envelope 2√(x f(y)) vs slower upper envelope
     √(2x²+2f(y)²)−y, a decrease violates a sandwich; injectivity ⇒ strict.
  4. `f-continuous`: monotone ⇒ only jump discontinuities; a jump breaks the QM–AM–GM squeeze for x,y
     straddling it ⇒ no jumps.
  5. `g-constant`: continuous + orbit-invariant g satisfying (∗); local-constant (via (∗) on nearby
     defect values, the 1<8 mechanism) upgraded to global by connectedness of (0,∞).
Key lemmas: `f-increasing`, `f-continuous`, `g-constant` (all three are gaps; mechanisms above).
Open gaps: all three steps 3–5 need to be made precise; the jump-exclusion (Step 4) is load-bearing.
Cases to cover: c=0, c>0; countable jump set must be shown EMPTY, not just small.
Watch out for: do NOT assume continuity — deriving it (Step 4) is the whole point; assuming it is a
  rigor violation the reviewer will catch.

---

Notes for the outline-reviewer / build set:
- orbit-interleaving is the most developed (Steps 1–5 rigorous; one clean residual gap) — prime to
  ADVANCE/build first.
- mixed-defect-contradiction shares that residual gap but via a finite framing — build to see which
  finishing of the zero-coexistence case is cleaner; if it collapses to the identical wall, keep only one.
- convex-duality and monotone-continuity are the genuine FAR-framing hedges (convex analysis / order-
  topology) — build at least one so the field is not one framing if the residual gap proves stubborn.
- Suggested build set: orbit-interleaving, convex-duality, monotone-continuity (three distinct
  framings), plus mixed-defect-contradiction if builder budget allows.
