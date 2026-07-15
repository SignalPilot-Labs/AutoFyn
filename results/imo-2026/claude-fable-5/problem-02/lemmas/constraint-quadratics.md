# Lemma: Constraint quadratics q_K(τ) = 0, q_L(σ) = 0 (CERTIFIED)

**Status: CERTIFIED by proof-reviewer, round 1. Full proof in `results/imo-2026-02/approaches/fixed-point-t.md`, §3 (Lemmas 3a, 3b, 3). Prerequisites: `setup-bookkeeping.md`, `parametrization.md`. Reviewer checks: every link of the Lemma 3b chain — the (E) ⟺ (E′) product-to-sum rearrangement, the cot-substitution identity (P−R)t² + 2Qt − (P+R) = (t²+1)(P cos u + Q sin u − R) at t = cot(u/2), and Lemma 3a closed forms — re-derived exactly in sympy (all == 0 identically); q_K(τ) = q_L(σ) = 0 confirmed numerically (≤ 4e-15) on independently constructed configurations.**

## Statement
For θ ∈ (0, π) define
  P(θ) := sin A cos θ + ½ sin θ cos A, Q(θ) := ½ sin A sin θ, R(θ) := sin A cos θ + ½ sin θ cos(A + 2α).
Then, with τ = cot(α+γ), σ = cot(α+β):
  q_K(τ) := (P(C) − R(C))τ² + 2Q(C)τ − (P(C) + R(C)) = 0,
  q_L(σ) := (P(B) − R(B))σ² + 2Q(B)σ − (P(B) + R(B)) = 0.
Moreover (Lemma 3a):
  P(θ) − R(θ) = sin θ sin α sin(A+α) (> 0 for θ ∈ {B, C}),
  P(θ) + R(θ) = 2 sin A cos θ + sin θ cos α cos(A+α).

Reusable conversion (Lemma 3b): for α+φ ∈ (0, π), t = cot(α+φ), the relation
  sin θ sin φ sin(A+2α+φ) = 2 sin A sin(α+φ) sin(θ−α−φ)
implies (P(θ)−R(θ))t² + 2Q(θ)t − (P(θ)+R(θ)) = 0.

## Proof mechanism
Law of Sines in triangle BKC (angles B−α, C−α−γ, A+2α+γ) equated with BK from the Parametrization Lemma, then a = c sin A/sin C; mirror in triangle BLC with a = b sin A/sin B. The conversion is product-to-sum (PS1) + expansion in cos u, sin u (u = 2(α+φ)) + the substitution cos u = (t²−1)/(t²+1), sin u = 2t/(t²+1) for t = cot(u/2), sin(u/2) > 0. Full prose in `approaches/fixed-point-t.md` §3.

## Numerical check
Verified during build at valid configurations (5 triangles × several α): both quadratic residuals ≤ 5e-15.
