## Status
unsolved

## Approaches tried
(new this round — extremal element + finite two-point contradiction, aimo-0481 template)

## Current best
Empty — new approach.

## Approach (skeleton — whole problem)

**Answer:** f(x) = x + c for every constant c ≥ 0.

### Part (a) — Sufficiency
Import shared lemma `suff-affine` (orbit-interleaving.md Part (a)).

### Part (b) — Necessity, via ruling out two distinct defect values (framing: finite contradiction)

Analogy: aimo-0481 derives a pointwise dichotomy then rules out MIXING two branches by feeding one
point from each branch into the ORIGINAL relation and deriving a contradiction. Adapt: here the
"branch label" of a point y is its defect value g(y)=f(y)−y, and we rule out two different labels.

**Step 1.** Establish (★), injectivity, f≥id, g≥0, g orbit-invariant, and the two-point lever
  (∗): (a−b)² + 2(a+b)g(a) + g(a)² ≥ 4a·g(b)   ∀ a,b>0,   and its swap
  (∗'): (a−b)² + 2(a+b)g(b) + g(b)² ≥ 4b·g(a).
(All shared/cheap; (∗) is (R) squared with f=id+g.)

**Step 2 (extremal-element setup).** Suppose, for contradiction, g is not constant. Let
c₁ = inf g and c₂ = sup g with c₁ < c₂ (0 ≤ c₁ < c₂ ≤ ∞). Pick points near the extremes: for
ε>0, a with g(a) < c₁+ε and b with g(b) > c₂−ε (if c₂=∞, g(b) arbitrarily large).

**Step 3 (KEY LEMMA `separate-defects-contradict`).** Feed the extremal pair into (∗)/(∗') using
the orbit AP structure to control |a−b|. Mechanism (the crux move, cf. aimo-0481):
  - Orbit-invariance gives infinite APs of EXACT defect: {a + k g(a)} all have defect g(a),
    {b + j g(b)} all have defect g(b). Interleave to pick A in the first, B in the second, both
    large, with |A−B| ≤ g(b) (choose B in b's orbit nearest below A). Then (∗) at (A,B):
      4A·g(b) ≤ (A−B)² + 2(A+B)g(a) + g(a)² ≤ g(b)² + 4A·g(a) + g(a)².
    Divide by 4A, A→∞: g(b) ≤ g(a) < c₁+ε, contradicting g(b) > c₂−ε once ε < (c₂−c₁)/2.
  - This directly contradicts c₁<c₂. Hence g is constant on the set where g>0 (both orbits need
    positive step). The value is a single c ≥ 0.

**Step 4 (finish: no separated zero — OPEN GAP `kill-mixed-zero`).** Step 3 leaves the case where
g is 0 at some points and c>0 at others (a zero has a one-point orbit, so Step 3's interleaving
does not apply to it). Rule out via the single-pair (∗) with a zero z and a positive point b:
  (∗) at (z,b): (z−b)² + 0 + 0 ≥ 4z·c  ⟹  (b−z)² ≥ 4cz  for all b with g(b)=c.
  (∗') at (z,b): (z−b)² + 2(z+b)c + c² ≥ 0 (auto). The binding constraint (b−z)² ≥ 4cz must hold
  for EVERY positive-defect b; show it fails for some admissible b (e.g. b in an orbit passing near
  z, or via injectivity f(z)=z forcing a nearby positive-defect preimage structure). This finite
  contradiction closes the mixed case.

**Conclusion.** g ≡ c ≥ 0; f(x)=x+c; with (a), the full set.

## Open gaps
- Step 4 `kill-mixed-zero`: derive a contradiction from (b−z)² ≥ 4cz holding for all positive-defect
  b coexisting with a zero z — the same residual as orbit-interleaving Step 5, attacked here as a
  finite two-point contradiction rather than a limit.

## Cases to cover
- c₁<c₂ with both positive (Step 3, closed); c₁=0 attained with c₂>0 (Step 4, the gap); g constant
  (the target, includes c=0 giving f=id).

## Watch out for
- Do not claim (∗) for a single pair forces g(a)=g(b) — it does not (for f=id+c it is tight at
  a−b=c, not a contradiction). The contradiction needs the orbit-AP interleaving of Step 3, i.e.
  MANY pairs with controlled |A−B| at large argument.
- c₂=∞ must be handled (the same divide-by-4A argument gives g(b) ≤ g(a) regardless of size).
