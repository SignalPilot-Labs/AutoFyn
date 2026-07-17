# Approach: family-invariance-boundary

## Status
unsolved

## Approaches tried
- (none yet — opened round 1)

## Current best
Nothing established beyond the shared unconditional reduction
OM = ON ⟺ F := pow(B, ω) − pow(C, ω) = (c² − b²)/2, and the numerically observed
facts that (i) the valid (K, L) form a smooth 1-parameter family in φ = ∠KBA, and
(ii) F is exactly constant along it.

## Outline

**Target (whole problem):** OM = ON for O the circumcentre ω = ⊙(AKL).

**Framing (deformation, not identity-grinding).** The hypotheses cut out a
1-parameter family of configurations (φ, K(φ), L(φ)) for a fixed triangle. Prove
the target quantity F(φ) = pow(B, ω_φ) − pow(C, ω_φ) is CONSTANT along the family,
then compute its value at one distinguished (limiting/degenerate) member where the
geometry collapses to something computable. This replaces one hard global identity
by (a) a differential statement and (b) one explicit limit evaluation.

**Step 1 (reduction).** OM = ON ⟺ F = (c² − b²)/2 — median formula, unconditional.

**Step 2 (the family is a smooth curve).** Using the trig system of the sibling
approach (E1–E6 there), for each φ in the valid open interval the pair (α_K, χ) is
determined by the K-side 2×2 system and (α_L, ψ) by the L-side system; the
solutions depend real-analytically on φ by the implicit function theorem, provided
the Jacobian of each 2×2 system is nonzero on the valid range.
**Gap:** verify the Jacobian nonvanishing (or restate via a monotonicity argument:
e.g. show χ and α_K are strictly monotone in φ).

**Step 3 (invariance: F'(φ) = 0).** Differentiate F along the family. Structural
route rather than brute force: F = pow(B,ω) − pow(C,ω) is a linear functional of
the circle ω (in the (center, |center|²−R²) coordinates, pow(P, ·) is affine), so
F' depends only on the velocity of ω in the 3-dimensional space of circles. The
circle ω_φ always passes through the FIXED point A, so its velocity lies in the
2-dim space of circles through A; F' = 0 for all φ iff the velocity stays in the
1-dim subspace of directions along which pow(B) − pow(C) is unchanged — i.e. iff
the derivative circle-direction is "radical-axis-parallel to line BC-difference".
Concretely: writing circle as |z|² − 2⟨o, z⟩ + e = 0 (o = center, e = pow(0)),
F = −2⟨o, B − C⟩ + (|B|² − |C|²), so F' = −2⟨o'(φ), B − C⟩ and the whole claim is:
  **the centre O(φ) moves PERPENDICULAR to BC** — exactly the explorer's observed
"O slides along the perpendicular bisector of MN" (that line is ⊥ BC).
**Gap (load-bearing):** prove ⟨O'(φ), B − C⟩ = 0 from the differentiated
constraint system. This is one bilinear identity in the differentials of E1–E6;
it may factor more cleanly than the finite identity (constants of motion often
do). If it resists, this approach dies here — record why.

**Step 4 (anchor: evaluate F at a boundary/limit member).** As φ tends to an
endpoint of the valid interval the configuration degenerates (numerics: K, L
approach the boundaries of their triangles / the containment conditions become
equalities). Identify the limit configuration explicitly — candidates: K → line
MC, L → line NB, or K, L → points where ψ or χ → 0, making the limiting K₀, L₀
solvable in closed form — and compute F there in closed form, obtaining
(c² − b²)/2.
**Gap (load-bearing):** identify and rigorously justify the limit configuration
(continuity of F up to the closed interval endpoint), then do the closed-form
evaluation. Alternative anchor avoiding limits: if some interior member is
computable in closed form (e.g. the φ with ψ = φ or χ = ψ), use it instead.

**Step 5 (assemble).** F is constant (Step 3) and equals (c²−b²)/2 at the anchor
(Step 4), hence everywhere; Step 1 converts this to OM = ON. Every configuration
in the problem statement belongs to the family by definition (its own φ), so the
proof covers all admissible (K, L), including the a-priori possibility of several
branches for the same φ — **Gap:** if the K-side/L-side systems admit multiple
valid solution branches for one φ, run the argument on each branch (connectivity
of the valid set must be addressed, or the anchor argument repeated per branch).

## Cases to cover
- Each connected component / branch of the valid family (Step 5).
- Isoceles b = c (statement trivializes by symmetry? still must be argued or
  absorbed).

## Watch out for
- This route needs genuine analytic care (IFT hypotheses, boundary limits); the
  rigor bar is the same as everywhere — "numerically the family looks smooth" is
  not a step.
- Do not assume the family is connected or that φ ranges over a single interval
  without proof.
- The anchor evaluation must be an admissible LIMIT of valid configurations, with
  F continuous up to it; F need not equal (c²−b²)/2 at arbitrary degenerate
  solutions of the equations (mirror branches exist where OM ≠ ON).
