# Proof review — imo-2026-05 (IMO 2026 P5)

Confirmed answer to prove (both directions): **f(x) = x + c for every constant c ≥ 0**.

I re-derived every load-bearing step independently. All key algebraic identities were verified in
sympy (each reduces to exactly 0): the two Part-(a) SOS identities `(x+c+y)²−4x(y+c)=(x−y−c)²` and
`2(x²+(y+c)²)−(x+y+c)²=(x−y−c)²`, the off-diagonal-lever identity
`(a+g(a)+b)²−4a(b+g(b))=(a−b)²+2(a+b)g(a)+g(a)²−4a g(b)`, and the cross-constraint identity
`(z+b)²−4z(b+c)=(b−z)²−4cz`. I checked numerically that f(x)=x+c (c=0,0.5,1,3) satisfies the
original sandwich and that non-affine perturbations (x+√x, 1.1x) fail. I stress-tested the two
openness inequality chains in the closing argument (200k random samples each) — both hold.

All three approaches share the same correct spine and each closes it rigorously. There is **no**
quantifier slip in the closing argument: the rigidity is forced by the lever (∗), which holds for
**all** a,b>0 (not merely on Im(f)), so nothing image-restricted is applied globally. The
interleaving limit is legitimate (both interleaved points are genuine positive orbit points where g
is exactly known by orbit-invariance), and the openness+connectedness finish is airtight (explicit
radii, verified). The symmetry step (swap a,b) in Step 4 is valid.

---

## orbit-interleaving — APPROVE (Status: solved)

- **Correctness:** 10/10. (★) derived cleanly from R²,L² at x=f(y); orbit-AP and g≥0 correct;
  lever (∗) exact; Step 4 interleaving with j=⌊(A_k−b)/s_b⌋≥1 gives 0≤A_k−B_k<s_b and the limit
  s_b≤s_a, symmetric ⇒ s_a=s_b; cross-constraint (C) and both openness radii
  (ε=min(b/2,√(cb)) for P, ε=min(z/2,2√(cz)) for Z) verified; connectedness finish correct.
- **Completeness/rigor:** 10/10. Both directions proven; c≥0 necessity from codomain stated;
  every case settled; no hand-waving.
- **Progress:** full solution from prior `unsolved`.
- Builder Status `solved` is **correct**. This is the cleanest proof — written into current.md.

## convex-duality — APPROVE (Status: solved)

- **Correctness:** 10/10. Same verified spine. The Legendre/support-line framing (Step 2) is used
  only as organizing narrative; the actual force comes from the squared lever (∗) valid for all
  a,b>0. The builder's own note correctly flags that the naive "conjugate tight everywhere" plan
  fails (tightness only on Im(f)) and does **not** rely on it — so the known trap is avoided.
  Steps 1,3,4,5 are identical in substance to orbit-interleaving and correct.
- **Completeness/rigor:** 10/10. Both directions; degenerate P=∅ case explicitly handled.
- Builder Status `solved` is **correct**.

## monotone-continuity — APPROVE (Status: solved)

- **Correctness:** 10/10. Same verified spine. Step 2's squeeze (♦)
  `2√t(√x−√t)≤f(x)−f(t)≤√(2(x²+t²))−2t` is correctly derived for t∈Im(f) and yields the sign law
  and continuity at image points — but these are **not** used in the closing argument (the note and
  Step 6 make clear they are a-posteriori corollaries). The rigidity is routed through the lever
  (∗), valid for all a,b>0. So the image-restricted facts are never applied globally — no quantifier
  slip. Steps 1,3,4,5 correct; openness radii (δ=min(β/2,√(2cβ)) for P; 2√(cz) for Z) verified.
- **Completeness/rigor:** 10/10. Both directions; every case settled.
- Builder Status `solved` is **correct**.

---

## Certified lemmas
- `sandwich-collapse` (★) — certified → `lemmas/sandwich-collapse.md`.
- `off-diagonal-lever` (∗) — certified → `lemmas/off-diagonal-lever.md`.
- `defects-equal-and-constant` — certified → `lemmas/defects-equal-and-constant.md`.
(`squeeze-diamond` (♦) from monotone-continuity is correct as stated but not needed for the solution;
not separately certified as a core lemma.)

## Verdicts
- orbit-interleaving: **APPROVE** (solved)
- convex-duality: **APPROVE** (solved)
- monotone-continuity: **APPROVE** (solved)
