# Lemma: Closed form of the circumcentre of AKL (CERTIFIED)

**Status: CERTIFIED by proof-reviewer, round 1. Proposed by proof-builder (quadratic-ideal-certificate), Promotable lemma 4; full proof in `results/imo-2026-02/approaches/quadratic-ideal-certificate.md`, Step 5 (Lemma 5 + Applications 5.1, 5.2), with the equivalent form proved independently in `approaches/fixed-point-t.md` §4–§5 (Lemmas 4, 5). Prerequisites: `setup-bookkeeping.md`, `parametrization.md`, `constraint-quadratics.md`.**

## Statement
In the setting of `setup-bookkeeping.md`, the point

  X := M + (a/4)·(1, cot(A + α))
    = ( (2c cos B + a)/4 , (c sin B)/2 + (a/4)·cot(A + α) )

satisfies |XA| = |XK| and |XA| = |XL|; hence X lies on the perpendicular bisectors of AK and AL, and (since these are distinct lines — K ≠ L, proved in fixed-point-t §6) X **is** the circumcentre O of triangle AKL. Its abscissa (2A_x + B_x + C_x)/4 is the abscissa of the midpoint of MN, giving OM = ON at once.

Underlying identity (free parameters B₀, C₀, α₀ ∈ ℝ, d₀ > 0, sin C₀ ≠ 0, sin(A₀+α₀) ≠ 0, A₀ := π − B₀ − C₀): with Â = d₀ sin C₀·(cos B₀, sin B₀), K̂(t) = (d₀ sin C₀/2)(cos α₀ − t sin α₀)(cos(B₀−α₀), sin(B₀−α₀)), X̂ = Â/2 + (d₀ sin A₀/4)(1, cot(A₀+α₀)):

  X̂·(Â − K̂(t)) − (|Â|² − |K̂(t)|²)/2 ≡ m₀·q₀(t) identically in t,

m₀ = (d₀ sin C₀)² sin α₀/(8 sin C₀ sin(A₀+α₀)), q₀ the quadratic of `constraint-quadratics.md` at θ = C₀. Applied at (B, C, α, d) and (C, B, α, d) (the latter pulled back by the reflection ψ(x,y) = (a−x, y)), and evaluated at the roots τ, σ.

## Reviewer checks
- The free-parameter identity re-derived exactly in sympy: all polynomial coefficients in t of Ê(X̂; K̂(t)) − m₀q₀(t) vanish identically. Reflection bookkeeping ψ(A) = Â*, ψ(L(s)) = K̂*(s), ψ(X) = X̂* verified exactly.
- End-to-end: on 18 configurations built directly from the problem hypotheses (root-solved, all six angle conditions + interiority confirmed), the true circumcentre O of AKL equals X to ≤ 2.4e-15.
