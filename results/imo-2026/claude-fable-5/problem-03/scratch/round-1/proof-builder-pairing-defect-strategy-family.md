# Build report — round 1 — pairing-defect-strategy-family (imo-2026-03)

File written: `results/imo-2026-03/approaches/pairing-defect-strategy-family.md` — **Status: solved** (complete proof, both bounds, answer stated and verified).

## Answer
c(n) = 2^n/(2^{n+1} − 1), D := 2^{n+1} − 1.

## What was proved (all in full rigor in the approach file)

1. **Lemma C (claiming value):** first claimer gets exactly Odd(P) under optimal play — full exchange induction, both one-sided guarantees (the j > 1 branch via the termwise inequality q_i ≥ p_{i+2}); zero-length pieces covered.
2. **Lemma D suite:** defect(P) = measure{x : N_P(x) odd}; Δ-additivity E_{P⊎Q} = E_P Δ E_Q; strip-pairs invariance; pairs+leftovers bound. **Lemma P (pairing duality):** defect(P) = min over partial pairings of Σ|a−b| + Σ leftovers (≤ by Δ-subadditivity, ≥ by consecutive sorted pairing). Verified vs brute force on 300 random multisets.
3. **Lemma F:** LB leaving ≤ n positive pieces ⇒ XY halves all, LB = 1/2 < 2^n/D.
4. **Theorem UB (upper bound, all n) — closes old gap G3 by a new route:** pigeonhole on the 2^{n+1} subset sums over D intervals gives disjoint A, B with |ΣA − ΣB| ≤ 1/D; a merge process (cut the larger of a ∈ A, b ∈ B to make an exact equal pair, remainder stays) realizes it with an explicit mark ledger ≤ n and full legality checking (all marks strictly interior, distinct); final multiset = equal pairs + leftovers of total ≤ 1/D ⇒ Odd ≤ (1 + 1/D)/2 = 2^n/D. Exact-rational end-to-end verification (400 random configs each, n = 1..4; geometric configs give exactly 2^n/D). The round-0 cascade family and its deficient case are retired.
5. **Theorem LB (lower bound, all n) — closes old gap G4:** geometric marking (blocks 2^j/D). Via Lemma P, every pairing of any ≤ n-cut refinement costs ≥ 1/D: pairs-as-edges multigraph on the n+1 blocks has ≤ n edges vs n+1 vertices ⇒ some component is a tree; proper 2-coloring ε_j = ±1 telescopes block masses along edges to |Σ ε_j 2^j|·u ≤ cost, and binary uniqueness gives |Σ ε_j 2^j| ≥ 1. Uniform in XY's mark count k ≤ n (parity weapon covered); tightness at XY's halving reply (defect exactly 1/D); numeric confirmation (min defect over 3000 random refinements = exactly 1/D for n = 1..3, ≥ 1/D for n = 4, 5).

Convergence note: my earlier partial route for LB (mass-domination + piece counting, complete for top-block cut-counts k ∈ {0,1,m−1,m}, i.e. all n ≤ 3) was superseded mid-round: the shared memory file mentioned a sibling's "home-graph counting" idea for its gap L1; I re-derived that tree-signing argument from scratch (it needs my Lemma P to apply to defect), verified it, and it closes the lower bound for ALL n in one page. The two builders' routes remain distinct overall (my UB is pigeonhole+merge; the pairing-duality reduction is mine), but the LB tree argument is now shared mathematics — reviewer may want to note this when ranking.

## Remaining gaps
None. All rigor-rule boxes checked in-file: exhaustive cases (degenerate marks, fewer marks, equal pieces, all k ≤ n), named tools (layer-cake, pigeonhole, binary uniqueness, tree = connected with e = v−1), answer stated and verified at n = 1..4 against the explorers' exact computations, attainment shown (no inf/sup pathology).

## Spec concerns
- None on the problem statement. AoPS URL is Cloudflare-blocked from the container (HTML and ajax API both); no external solution was consulted — the proof is built from the outline + my derivations.

## Promotable lemmas (for certification into lemmas/)
claiming-value (Lemma C), defect-identity (Lemma D + D0–D2 + Lemma P), fewer-marks (Lemma F), upper-bound-pigeonhole-merge (Theorem UB), lower-bound-tree-signing (Theorem LB). All self-contained in the approach file, Sections 1–5.
