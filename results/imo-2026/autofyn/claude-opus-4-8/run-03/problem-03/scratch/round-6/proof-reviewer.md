# Proof-reviewer report — round 6 — imo-2026-03

## Approach 1: segment-subset-pigeonhole — APPROVE (Status: solved)

**Verdict: APPROVE. True Status: solved.** The builder's recorded Status (solved) is CORRECT.
This is a complete, rigorous proof of both bounds giving c(n) = 2^n/(2^{n+1}−1). I attacked every
load-bearing step independently and it holds.

### Scores
- Correctness: 10/10 — every step re-derived and reproduced.
- Completeness/rigor: 10/10 — all cases (m ≤ n and m = n+1), all edge cases, no hand-waving.
- Progress: maximal — closes the run (both cruces that walled the field for 5 rounds).

### Independent verification of each load-bearing step

**Reduction (§0).** Rests on certified L0 (claiming = odd-rank sum), L1 (order irrelevance,
c(n) = max_A min_B Σ_odd(B), XY does ≤ n splits), L2 (Σ_odd = (1+S)/2). I re-read all three:
correct and exactly as invoked. The target reduces to max_A min_B S(B) = 1/D_n. S is the output-
multiset functional throughout — no pairing mismatch (the round-5 "reconciliation" worry is a
non-issue, as the builder states).

**UB1 (§1, the merge-alignment lemma, previously-open UB crux).** Re-derived from scratch. The
construction (bisect leftovers; lay S on [0,Σ(S)], T on [0,Σ(T)], cut both at the union C of
boundaries in [0,Σ(T)]) does produce q matched pairs of EQUAL length per C-cell (both blocks cut
at the same points) plus overhang of mass Σ(S)−Σ(T). By L4 (certified min-pairing = min over
pairs+singletons of Σ|u−v|+Σℓ), S(B) ≤ the explicit partition cost = 0 + 0 + (overhang paired
among itself) ≤ Σ(overhang) = Σ(S)−Σ(T), using |u−v| ≤ u+v. Cut budget is counted rigorously:
|L| + (≤|T| on S-parts) + (≤|S|−1 on T-parts) = m−1 exactly, and the T=∅ sub-case is handled.
**Numeric check I ran** (exact Fraction, n=1..5, all disjoint-(S,T) assignment patterns, 400
random A): 0 cases with S(B) > |Σ(S)−Σ(T)| and 0 cases with cuts > m−1. Solid.

**Pigeonhole (§2, m=n+1).** 2^{n+1} = D_n + 1 subset sums into D_n bins ⟹ two DISTINCT subsets
collide, |Σ(U)−Σ(V)| ≤ 1/D_n; S = U∖V, T = V∖U are disjoint with Σ(S)−Σ(T) = Σ(U)−Σ(V) and
(S,T) ≠ (∅,∅) since U△V ≠ ∅. Empty/full subsets are legitimate distinct pigeons; no collision
edge case is missed. Correct.

**m ≤ n case (builder's added bisect-all argument).** Bisect all m ≤ n parts ⟹ B is m equal
pairs ⟹ S(B) = 0 ≤ 1/D_n by L4. Airtight; this was implicit in the skeleton and is now closed.

**LB1 (§3, tree-extraction, previously-open LB crux).** Re-derived. S(B) = Σ_e d_e over the
consecutive-pair multigraph G (V = n+2 parts+dummy, E = ⌈N/2⌉ ≤ n+1 < V since N ≤ 2n+1). The
cycle-rank count Σ_c(v_c−e_c) = V−E ≥ 1 with v_c−e_c ≤ 1 (=1 iff tree) forces a tree component;
the parity split (N odd ⟹ δ deg 1; N even ⟹ E ≤ n ⟹ V−E ≥ 2) correctly guarantees a tree
component with a real part-vertex. The edge-length identity Σ_{v∈K}σ(v)a_v = Σ_{e∈K}±d_e is valid
precisely because K is a component (every edge incident to K has both endpoints in K) — this is
the one place a naive H would break, and the proof correctly restricts to a component. Bipartite
2-coloring ⟹ each edge contributes ±d_e ⟹ |Σσ(v)a_v| ≤ Σ_{e∈K}d_e ≤ Σ_all d_e = S(B). ε read
off K is nonzero (K has a real part), δ drops (a_δ=0), so Δ(A) ≤ S(B). Self-loops (1-cycles) are
correctly excluded from tree components. **Numeric check I ran** (dyadic A, random ≤n-split
refinements, n=1..4, 300 each): 0 violations of S(B) ≥ Δ(A).

**LB2 (§4, dyadic Δ).** Δ(dyadic) = (1/D_n)·min|Σ ε_i 2^{i−1}| over nonzero ε ∈ {−1,0,1}^{n+1};
the top nonzero term 2^{j−1} strictly exceeds Σ_{i<j}2^{i−1} = 2^{j−1}−1, so the integer combo is
nonzero (≥ 1), = 1 at ε=(1,0,…,0). Correct; verified Δ·D_n = 1 for n=1..6.

**Final answer.** c(n) = (1 + 1/D_n)/2 = 2^n/D_n = 2^n/(2^{n+1}−1). n=1 ⟹ 2/3 (matches base
case). Tightness at dyadic confirmed: subset sums are exactly {0,…,D_n}/D_n, closest distinct pair
differs by 1/D_n, so UB meets LB at the dyadic profile. Answer stated and verified.

**No contradiction with prior refutations.** The round-4/5 "known-false" notes killed specific
mechanisms (top-part-restricted UB, averaging, randomized-XY, |S(Q)−S(C)| bounds). UB1's
merge-alignment is a genuinely different construction (not a one-pass greedy, not restricted to
top parts), so none of the refutations apply. This is the "genuinely different framing far from
the layer-cake wall" the orchestrator asked for.

**Actions taken:** wrote Status solved + Full proof into current.md (reviewer-owned). Certified
the four promotable lemmas into lemmas/: L15 (UB1 merge-alignment), L16 (LB1 tree-extraction),
L17 (LB2 dyadic Δ, folded into L16's file). All held to the full bar (statements correct, no
stronger than proved, no sorry). UB2 (pigeonhole) is elementary and lives inline in §2 rather than
as a separate lemma file.

## Approach 2: induction-peel — CHANGES REQUESTED (Status: partial)

**Verdict: CHANGES REQUESTED. True Status: partial.** Builder's recorded Status (partial) is
CORRECT and honest. This round it retired the UB branch-inequality line as dead (F1, n=5
all-branches counterexample) and falsified-first the proposed shard-count/boundary-invariance axis
for (CB) (slack is non-constant: n=3 witness rest={3.9,0.1} slack 9/5 vs rest={2,2} slack 0). No
new gap closed; no overclaim. The (CB) and k_C≥1 charging gaps stand.

### Scores
- Correctness: 9/10 — the falsification and the retirement are sound; no false claims.
- Completeness/rigor: partial — LB residual still open on all layer-cake sub-routes.
- Progress: negative-utility this round (correctly killed a dead route); the approach is now
  **superseded** by segment-subset-pigeonhole, which solved the whole problem independently.

**Gap (unchanged):** (CB) Σ A_{2m} ≤ Σ B_{2m−1} in Case B (k_C=0) from Σ s_k ≤ 2^n, and the
k_C≥1 cross-scale aggregate charging. The builder itself recommends ceding both bounds to
segment-subset-pigeonhole; induction-peel remains valuable only as the certified-lemma anchor
(L0–L14). No re-dispatch needed now that the problem is solved.

## Summary
The run's goal is met. segment-subset-pigeonhole is a complete, verified solution:
**c(n) = 2^n/(2^{n+1} − 1).** current.md updated; L15/L16 certified; induction-peel remains a
correct partial anchor.
</content>
