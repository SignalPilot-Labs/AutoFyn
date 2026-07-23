# proof-builder report — two-step-spiral-chain (imo-2026-02, round 1)

Status: unsolved (dead end, recorded honestly, not forced).

Per the outline's own instruction, the first action was a numeric gate on
its two named key lemmas, run on TWO independent generic scalene triangles
over the whole valid 1-parameter family (filtered to the branch satisfying
all containment/betweenness hypotheses, where OM=ON is confirmed to hold to
~1e-9-1e-14, matching the other explorers/builders' findings):

1. Lemma "triangle BKL ~ triangle NLC via spiral similarity" (equal angle
   ∠LBK=∠LNC, already given, PLUS matching ratio BK/BL=NL/NC): REFUTED. The
   ratio difference BK/BL - NL/NC varies smoothly over a range of ~0.5 and
   changes sign within the family on both test triangles — not a numerical
   artifact, a genuine non-identity.

2. Lemma "C,K,M,X concyclic for some natural X (L, B, or an auxiliary point)":
   REFUTED. Ran the general 4-point concyclicity determinant test over all 20
   subsets of {A,B,C,M,N,K,L} containing K (with C,M as the outline
   specifically wanted), across all sampled t on both triangles. No subset's
   determinant is even close to zero at any single t, let alone identically
   zero across the family.

Both refutations are robust (order-of-magnitude larger than solver noise,
reproduced on a second independent triangle), so the approach is retired
rather than forced. Full numeric evidence tables and reasoning are in
results/imo-2026-02/approaches/two-step-spiral-chain.md.

No lemma promotable to the shared cache from this round (both candidates were
disproved, not proved).

Relevant paths:
- results/imo-2026-02/approaches/two-step-spiral-chain.md (updated, Status: unsolved)
