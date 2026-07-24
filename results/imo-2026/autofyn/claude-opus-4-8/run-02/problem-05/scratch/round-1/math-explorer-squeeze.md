## imo-2026-05

### Distinct openings (squeeze / equality-chaining route)

1. **[STRONGEST — verified] Substitute x = f(y) into BOTH inequalities.**
   At x = f(y), inequality (1)'s LHS becomes sqrt((f(y)^2+f(y)^2)/2) = f(y) exactly (a
   trivial/degenerate QM-AM with equal arguments), so (1) collapses to
   `f(y) >= (f(f(y))+y)/2`, i.e. `2f(y) >= f(f(y)) + y`.
   At x = f(y), inequality (2)'s RHS becomes sqrt(f(y)*f(y)) = f(y) exactly (degenerate
   AM-GM), so (2) collapses to `(f(f(y))+y)/2 >= f(y)`, i.e. `f(f(y)) + y >= 2f(y)`.
   **These two are the same inequality in opposite directions ⇒ equality is FORCED:**
   `f(f(y)) = 2f(y) - y` for all y > 0. This is an exact derived functional equation
   (not a conjecture) — verified algebraically and it is the natural "collapse" move
   for this squeeze route (self-contained, only 3 lines, no case work).

2. **Recognize the answer family directly via the reverse algebraic identity.**
   If f(x) = x + c (any constant c), then f(x) + y = x + f(y) identically. Substituting
   this into (1) turns it into literally `sqrt((x^2+f(y)^2)/2) >= (x+f(y))/2` — the bare
   QM-AM inequality applied to the pair (x, f(y)), always true. Substituting into (2)
   turns it into `(x+f(y))/2 >= sqrt(x f(y))` — the bare AM-GM inequality on the same
   pair, always true. **So f(x) = x + c satisfies BOTH given inequalities identically for
   every c, with equality exactly when x = f(y).** Domain/codomain positivity (f(y) =
   y + c > 0 for every y > 0) forces c >= 0. Verified numerically (see below) — this
   family genuinely works, it is not just c = 0 (identity). The "answer" is therefore
   conjectured to be the whole one-parameter family `f(x) = x + c, c >= 0`, not merely
   f(x) = x.

3. **Orbit / iteration argument to promote the pointwise FE toward global constancy.**
   Let h(y) = f(y) - y. Opening 1's identity f(f(y)) = 2f(y) - y rewrites as
   `h(f(y)) = h(y)` — h is invariant along the forward orbit of f. If h(y0) = c0 for
   some y0, then by induction the orbit is f^n(y0) = y0 + n*c0 (each step adds c0
   because h stays c0 all along the orbit). Since f maps into R_>0, every iterate
   f^n(y0) must stay positive; if c0 < 0 this fails for large n — contradiction. **This
   forces h(y) >= 0 for every y, i.e. f(y) >= y everywhere**, purely from the derived FE
   plus the codomain constraint (no further use of the original two inequalities
   needed). This is a genuinely different mechanism than opening 1 (orbit/telescoping
   vs. one-shot substitution) and gives a global lower bound cheaply.
   **Gap**: this orbit argument alone only gives h >= 0 pointwise per-orbit, not that h
   is the SAME constant across different starting points y0 — full constancy of h
   still needs an argument tying different y's together (candidates: use the original
   inequalities at general (x,y), not just at x=f(y); or show f is monotone increasing
   and use monotonicity of h forced by monotonicity of f; or a second collapse using
   y = f(x) substituted into the *other* pairing). This is the remaining gap for the
   outliner to target.

4. **Growth-rate squeeze (asymptotic route, weaker but corroborating).** Fixing x and
   letting y -> infinity in (1) forces f(y) to grow at least linearly (roughly
   f(y) >= y/sqrt(2) + o(y)); fixing y and letting x -> infinity in (1) forces f to
   grow at most like sqrt(2) x + O(1). These bracket f between two different linear
   growth rates — not tight enough alone to pin f(x) = x + c exactly, but useful as a
   sanity check / secondary lemma to rule out wildly non-linear f, and cheap to state.

### Candidate technique(s)
- QM-AM and AM-GM equality analysis (`knowledge_base.md`: "Standard inequalities: AM-GM,
  Cauchy-Schwarz, QM-AM, Schur. Equality cases pin down the extremal configuration.").
- "Functional equations: test special values" (knowledge_base.md) — here the special
  value is x = f(y), which is the crux move of this whole route.
- Orbit/telescoping argument on the derived recursion f(f(y)) = 2f(y) - y (akin to
  "linear recurrences ... sequences eventually periodic" style reasoning in the KB,
  though here it's a divergence argument, not periodicity).

### Cheap-kill candidates
- The diagonal case x = y is **vacuous** (both inequalities reduce to QM-AM / AM-GM
  applied to (x, f(x)) trivially — no constraint on f). Do not waste effort there.
- Any single-point "dip" f(y0) < y0 (even an isolated exception, function otherwise
  = identity) breaks the inequality at nearby (x,y) — confirmed numerically (see
  below). This is consistent with opening 3's h >= 0 result and is a fast sanity
  check/counterexample-killer for any proposed non-affine f.
- Small non-affine perturbations (e.g. f(x) = x + 2 + 0.1 sin(x)) numerically FAIL the
  inequalities at large x, y — supports the conjecture that only affine shifts survive.

### Knowledge-base entries to use
- "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases pin down
  the extremal configuration." — directly the tool for opening 1 and opening 2.
- "Functional equations: test special values, check injectivity/surjectivity." — for
  opening 3's follow-up (need injectivity/monotonicity of f to finish the constancy
  argument).

### Analogous past problems (cruxes)
- Searched crux corpus (`domain=algebra`, subtopics `functional-equations` and
  `inequalities-SOS-and-convexity`, and `domain=combinatorics` `extremal-principle`).
  No crux was found with the exact "two-sided inequality squeeze forces exact FE via a
  degenerate-equality substitution" structure of this problem. The closest in *spirit*
  (squeeze-to-equality forcing every link tight, then deriving a contradiction/product
  identity) is `aimo-0910` (UK, permutation counting via `i*a_i` monotone chain: "When a
  chain of inequalities is squeezed between equal endpoints, force every link to
  equality") — but its domain (integer permutations, product-pairing contradiction) is
  not close enough to adapt directly; it only supports the general squeeze-to-equality
  *pattern*, not a specific technique to borrow. No genuinely analogous functional-
  inequality problem was found in the corpus (nothing combining QM-AM and AM-GM as two
  sides of one functional inequality with a self-referential f(y) substitution). Report
  as: no strong analog, this route's crux move (opening 1) appears to be intrinsic to
  the problem rather than a corpus-borrowable pattern.

### Prior progress
None — round 1, workspace `results/imo-2026-05/` is empty (no approaches, no
current.md content yet).

### Dead ends (do not retry)
None yet recorded (first round). Note for future rounds: **diagonal x=y substitution is
uninformative** — don't waste an approach slot rediscovering that it's vacuous.

### Small-case / intuition notes (conjectures, not proofs)
- **Conjectured answer: f(x) = x + c for any constant c >= 0** (not just f(x) = x).
  Verified numerically for c ∈ {0, 0.5, 1, 3, 10} against 20000 random (x,y) pairs in
  (0.001, 1000) with tolerance 1e-9 — all passed with no violation found.
- c < 0 (e.g. f(x) = x - 0.5) fails immediately (found a violating (x,y) pair) —
  consistent with the domain constraint f(y) = y + c > 0 needing c >= 0.
- Non-affine perturbations of the identity/shift (sinusoidal wiggle, piecewise jump)
  both fail — found explicit violating (x,y) numerically in each case. This is strong
  (numeric) evidence the family is exactly the affine shifts, not something richer.
- The algebraic reason f(x)=x+c works is clean and structural (opening 2): the two
  given inequalities *are* QM-AM and AM-GM in disguise once f(x)+y is rewritten as
  x+f(y), which happens iff f(x)-x is constant. This suggests the natural final target
  for the outliner: prove f(x) - x is constant (using the derived FE from opening 1
  plus a monotonicity/injectivity argument per opening 3's gap), then invoke opening 2
  to both derive AND verify the answer in one motion.
