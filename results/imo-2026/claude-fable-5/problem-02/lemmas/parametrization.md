# Lemma: Parametrization of K and L (CERTIFIED)

**Status: CERTIFIED by proof-reviewer, round 1. Full proof in `results/imo-2026-02/approaches/fixed-point-t.md`, §2 (Lemma 2). Prerequisite: `lemmas/setup-bookkeeping.md`. Reviewer checks: Law-of-Sines derivations in BMK / CNL read line by line (nondegeneracy from Lemma 1.1, ray BM = ray BA, ray CN = ray CA) — sound; closed forms independently confirmed numerically: K, L rebuilt from the closed forms reproduce all six hypothesis angles to ≤ 2e-15 on 5 test triangles.**

## Statement
In the setting of `setup-bookkeeping.md`, with τ := cot(α + γ) and σ := cot(α + β) (well-defined: α+γ ∈ (0, C), α+β ∈ (0, B)):
  K = (c/2)(cos α − τ sin α)·e^{i(B−α)},
  L = C + (b/2)(cos α − σ sin α)·e^{i(π−C+α)}.
Equivalently BK = (c/2)·sin γ/sin(α+γ), CL = (b/2)·sin β/sin(α+β).

## Proof mechanism
Law of Sines in triangle BMK (angles α at B, γ at M, π−α−γ at K; BM = c/2, ray BM = ray BA) and in triangle CNL (angles α at C, β at N; CN = b/2, ray CN = ray CA); then sin γ = sin((α+γ)−α) expanded. Full prose in `approaches/fixed-point-t.md` Lemma 2.
