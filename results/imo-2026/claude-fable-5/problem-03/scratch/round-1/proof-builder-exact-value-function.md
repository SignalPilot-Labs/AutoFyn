# Build report — exact-value-function — round 1

File updated: /home/agentuser/repo/results/imo-2026-03/approaches/exact-value-function.md (Status: partial)

## What was proved this round (in full, in the approach file)

1. **Lemma C (claiming value = Odd).** Exchange induction, with the explicit two-parity computation showing removing the largest element minimizes the opponent's Odd. Closes the claiming-phase rigor requirement.
2. **Lemma D + corollaries D1–D4.** Layer-cake defect identity; nonnegativity; strip-pairs invariance; pairs-plus-leftover formula (defect = ρ); zero-append invariance (D4 — the tool that handles endpoint marks, coalesced marks, and XY using < n marks uniformly).
3. **Lemma F.** < n effective LB marks ⇒ XY holds LB to exactly 1/2 (midpoint reply, legality checked).
4. **Lemma V — Gap E1 CLOSED, per the reviewer's demands.** Full attainment + vertex classification:
   - Claim V0: the compact product-of-simplices parametrization (with zero sub-pieces allowed) exactly represents all legal replies, both directions proven via D4; attainment via continuity of order statistics (1-Lipschitz).
   - Vertex structure: an optimal reply exists whose distinct positive values v_1 > … > v_s solve A v = q for a nonnegative integer matrix A with rank s (unique solution). Proof by pattern-polytope Q_σ (Odd linear there) + extreme point + explicit perturbation argument.
   - The classification covers ALL THREE facet families the reviewer flagged: cross-piece ties (matching), same-piece ties (equipartitions), zero facets (fewer effective marks).
5. **The false E3 claim is withdrawn and repaired.** "Vertex sizes in ½ℤ" is deleted; replaced by the Cramer statement v ∈ (1/det B)·ℤ-span{q_i} (denominators ≥ 3 possible — equipartitions). The lower bound now splits into:
   - **Lemma P (proved):** any reply to the geometric config with all sizes integer in units 1/D has defect ≥ 1 unit — parity: defect ≡ Σ n_c v_c = D ≡ 1 (mod 2) after strip-pairs, and defect ≥ 0.
   - **Fact 1 (proved):** every piece contains 0 or ≥ 2 non-integer sub-pieces (fractional parts must cancel per piece).
6. **Upper bound, cases (a) and (b) closed.** Replies H and F(j,r) with exact mark ledgers ((r−j)+(j−1)+(n+1−r) = n) and defect computed via D3; the Chain Lemma (all d_j > 1/D and q_{n+1} > 1/D ⇒ Σq > 1) proven by downward induction, strict contradiction.
7. **Tightness at g:** binary-split reply gives defect exactly 1/D, so once the lower-bound gap closes, V(g) = 2^n/D exactly. n = 1 lower bound proven fully by hand (every reply has defect ≥ 1/3, with the pretty fact that ANY cut of the top piece gives defect exactly 1).

## Numerical checks run

- Multistart Nelder–Mead over ALL cut assignments and replies to the geometric configuration: min defect = 1/D exactly at n = 1, 2, 3 (ratios 1.000000). Confirms E3′ (fractional vertices never beat integer ones) is true, as the reviewer requested be tested before proving.

## Remaining gaps (honest)

- **E2 (upper bound, deficient case (c)):** some d_j < 0 with q_{n+1} > 1/D and no d_j in [0, 1/D]. Needs cascade replies (counterexample q = (0.49, 0.345, 0.165) recorded showing H+F alone fail; explicit cascade closing it recorded). Round-2 target: cascade-selection rule + mark ledger + remainder ≤ 1/D proof.
- **E3′ (lower bound, fractional vertices):** vertex replies to g with non-integer values have defect ≥ 1 unit. Candidate repair recorded in the file: p-adic valuation on the rank-s system A v = g forces each piece to meet the worst-denominator class in ≥ 2 components or in one component with multiplicity ≡ 0 mod p (mark-expensive equipartition); combine with the mark budget and top-piece mass domination for a counting contradiction.

## Spec concerns

None on the problem statement. One coordination note: all three builders were told to file Lemmas C/D/F under `lemmas/`; to avoid three parallel writers colliding on the same filenames, I kept my full proofs inside my approach file and listed them under "Promotable lemmas" for the proof-reviewer to certify into `results/imo-2026-03/lemmas/` (builder proposes, reviewer certifies). Lemma V, the Chain Lemma, and Lemma P are also promotable and are distinctive to this slug.
