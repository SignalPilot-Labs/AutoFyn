# Build report — secant-trig-identity (imo-2026-02, round 1)

## Status set: solved

## What was closed

Both gaps from the outline are closed; the approach file now contains a complete
prose proof (`results/imo-2026-02/approaches/secant-trig-identity.md`).

1. **Orientation/directed-length gap (secondary) — eliminated structurally.**
   Replaced the tangent–chord + power-of-a-point machinery (Steps 2–3 of the outline)
   by a branch-free formulation: with A at the origin, a point P = |AP|·u(θ) lies on a
   circle ω ∋ A with centre O iff X cos θ + Y sin θ = |AP|, where (X,Y) = 2O. The goal
   OM = ON becomes the linear condition (c − b cos A)X − b sin A·Y = (c²−b²)/2 via the
   median expansion (no powers, no signed secants, no δ). All configuration content is
   isolated in Step 0 (three interiority lemmas, proven: sector description of angle
   interiors, int(△BMC) ⊆ int(△ABC) via affine functionals, angle-addition lemma),
   which yields the angle splittings ∠ACK = φ+χ, ∠ABL = φ+ψ and the ranges making all
   sines positive.

2. **The load-bearing elimination identity — proved.**
   - χ and ψ are eliminated by a determinant of a homogeneous 2×2 system in
     (sin u, cos u) (no divisions), giving the constraint pair
     (K): c·N(s) = b sin²s, (L): b·N(t) = c sin²t, where s = φ+α, t = φ+β,
     μ = 2φ+A, N(w) = sin w sin(μ−w) − 2 sin(w−φ) sin(μ−φ−w).
   - The goal reduces (solving the two chord equations, Δ = sin(A−α−β) ≠ 0 from
     non-collinearity of A, K, L) to G·sin s sin t = c² sin²t·V + b² sin²s·U + bc·W,
     which the constraints turn into bc·[N(s)U + N(t)V + W].
   - **Key Identity (the crux, new):** N(s)U + N(t)V + W =
     sin(s−t)·[N(s)N(t) − sin²s sin²t] holds for ALL real (s,t,φ,μ). The reviewer's
     branch-freeness evidence is explained exactly: the identity is unconditional
     modulo the constraint product N(s)N(t) = sin²s sin²t, whose deficiency factors
     out with multiplier sin(s−t).
   - KI is proven human-checkably by interpolation: both sides are trig polynomials
     in s with only odd frequencies |k| ≤ 3 (bookkeeping shown), so
     D(s) = e^{−3is}Q(e^{2is}) with deg Q ≤ 3; D vanishes at s ∈ {t, 0, φ, μ−φ}
     (four short product-to-sum computations using N(w) = σ − sin w sin(μ−w),
     σ = 2 sin φ sin(μ−φ), and two 2-line lemmas B1, B3); four distinct roots kill Q;
     density + continuity extend to all of ℝ⁴.

## Machine checks (discovery/verification only; the prose stands alone)

- `/tmp/round-1/scratch/builder_identity4.py` — sympy exact: KI LHS−RHS ≡ 0.
- `/tmp/round-1/scratch/builder_identity3.py` — discovery of the sin(α−β) multiplier.
- `/tmp/round-1/scratch/builder_endtoend.py` — 33 numbered checks × 3 scalene
  configurations: every displayed equation of the proof (hypothesis angles, angle
  additions, chord equations, E1–E6, (K), (L), Goal′, G-assembly, KI, B1, B3, and
  OM = ON itself) verified to ≤ 1e-11.
- `/tmp/round-1/scratch/builder_final_check.py` — sympy exact check of the two
  grouped evaluation computations exactly as typeset in the file.

## Remaining gaps

None. The one input taken from the problem statement rather than derived is the
non-collinearity of A, K, L (the statement says "circumcentre of triangle AKL", which
presupposes a triangle; the proof flags this use explicitly in Step 5).

## Promotable lemmas (proposed for certification)

Listed in the approach file: **KI**, the **constraint pair (K)/(L)** (full trig
encoding of the hypotheses), and the **interiority package** (Lemmas 0.1–0.3). KI +
(K)/(L) is exactly the certificate the complex-certificate sibling seeks; if this
proof is APPROVEd, that sibling is redundant.

## Spec concerns:

(none)
