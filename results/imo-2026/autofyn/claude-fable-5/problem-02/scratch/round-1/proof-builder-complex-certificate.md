# Build report — complex-certificate (imo-2026-02, round 1)

## Outcome
Status set to **solved**. Full proof written to
`results/imo-2026-02/approaches/complex-certificate.md`. No remaining gaps.

## What was built
Followed the outline-reviewer's mandated change 1: dropped the raw Im(·)=0 encoding
entirely and re-encoded via the branch-pinned trig-resolved forms. The proof:

1. **Part 0** — all interiority hypotheses consumed up front: K, L ∈ int(ABC)
   (proved, not assumed, from K ∈ int(BMC), L ∈ int(BNC)); angle additivities
   ∠ACK = φ+χ, ∠ABL = φ+ψ from the two "inside the angle" hypotheses; all named
   angles in (0,π) so every sine is positive (this is what kills the mirror branches).
2. **Part 1** — median-formula reduction OM = ON ⟺ OB² − OC² = (c²−b²)/2 (proved inline).
3. **Part 2** — six law-of-sines relations E1–E6 in six explicitly nondegenerate triangles.
4. **Part 3** — elimination of χ and ψ in closed form. New clean finding: each side
   collapses to a single relation linear in (b,c):
   ℓ_K := b sin²(φ+u) − c[cosA − cos(φ+u)cos(A+φ−u)] = 0 (u = ∠KAB), and the b↔c,
   u→v mirror ℓ_L = 0 (v = ∠LAC). The bracket identity used in the elimination is
   displayed with a full product-to-sum table.
5. **Part 4** — A, K, L non-collinear, proved synthetically from the sector hypotheses
   via a cot-monotonicity argument at B and at C (the two strict inequalities
   ∠ABL > ∠ABK and ∠ACK > ∠ACL force AL > AK and AK > AL on a common ray — contradiction).
   This was the reviewer's required lemma 2.
6. **Part 5** — circumcentre by Cramer (determinant sin(A−u−v) ≠ 0 by Part 4); goal
   reduced to one trig polynomial G = 0.
7. **Part 6** — the certificate: **2 sinA · G = α·ℓ_K + β·ℓ_L identically in all six
   free variables** (no branch conditions, no nonvanishing multiplier beyond sinA ≠ 0),
   with small closed-form cofactors
   α = −[b(sin²φ+sin²v) + c sin(φ+v)sin(A−φ−v)],
   β = c(sin²φ+sin²u) + b sin(φ+u)sin(A−φ−u).
   Verified by three coefficient identities (b², bc, c²); Id-c² follows from Id-b² by
   u↔v symmetry; Id-b² (5 terms) and Id-bc (6 terms) verified line-by-line via displayed
   Fourier-mode tables with mode-by-mode cancellation. Human-checkable end to end.

The reviewer's prediction was exactly right: after the trig-resolved encoding the
certificate exists over the full algebraic variety — the cofactors found are tiny.

## Verification artifacts (all under /tmp/round-1/scratch/)
- `build_cc_1.py` — full configuration reconstructed numerically from scratch
  (A=55°, b=4.3, c=6, φ=18°): all five hypothesis conditions hold to 1e-13, K ∈ int(BMC),
  L ∈ int(BNC), and OM − ON ≈ 5e-13; ℓ_K, ℓ_L, G all ≈ 0.
- `build_cc_2.py`, `build_cc_10.py` — bracket identity (symbolic zero + Fourier table).
- `build_cc_4.py` — certificate cofactor discovery (linear solve; one-parameter family,
  b5 = 0 chosen for the clean real form).
- `build_cc_5.py`, `build_cc_6.py`, `build_cc_final.py` — certificate (10) exactly zero
  under exp-expansion, with the expressions exactly as displayed in the proof file.
- `build_cc_7.py`–`build_cc_9.py` — the three coefficient identities and their
  displayed Fourier tables (sums exactly 0).

## Convergence note for the orchestrator/reviewer
As the outline-reviewer anticipated, after re-encoding this approach performs the same
elimination as secant-trig-identity in different coordinates (my ℓ_K = 0 is the
χ-eliminated closed form of its E1/E5/E3 system). If both come back solved, they are
near-duplicates at the core identity; the certificate identity (10) here is the closed
form of that shared gap and either write-up can cite it. Prune one slug next round if
both are approved.

## Promotable lemmas (proposed for certification)
1. `median-reduction` — OM = ON ⟺ pow(B,ω) − pow(C,ω) = (c²−b²)/2 (Parts 1, 5).
2. `AKL-noncollinear` — A, K, L not collinear from the sector hypotheses (Part 4).
3. `side-relations` — ℓ_K = 0, ℓ_L = 0 (Part 3), the branch-free encoding.
4. The certificate identity (10) itself (Part 6) — importable by secant-trig-identity.

## Spec concerns:
(none)
