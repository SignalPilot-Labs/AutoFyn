# Proof review — imo-2026-03 / pairing-exchange-normal-form (round 1)

## Verdict: APPROVE — Status: solved

Claimed answer c(n) = 2^n/(2^{n+1}-1). I verified the proof adversarially, step by step, and independently re-derived/checked the load-bearing steps. No gap found.

## What I checked (and how)

### Lemma 0 (game value = oddsum) — VERIFIED
- Hand-checked the backward-induction recursion V(M) = max_x [x + σ(M∖x) − V(M∖x)] and both guarantee directions (i)/(ii). The rank-shift computation evensum(M∖a_i) = Σ_{j<i even} a_j + Σ_{j>i odd} a_j is correct, and both parity cases of oddsum(M) − P(a_i) ≥ 0 telescope correctly.
- Independently verified numerically: exact minimax on 200 random multisets (|M| ≤ 7) matches oddsum to 1e-12.
- The problem statement (optimal play both sides, LB guarantee regardless of XY's play) is exactly what Lemma 0(i)/(ii) delivers. The implicit assumption that all pieces get claimed is harmless (lengths ≥ 0, claiming never hurts; and the rules force claiming until pieces run out).

### Lemmas 1–3 (peeling) — VERIFIED
Re-derived the sign-flip formulas from scratch. Removing a_i flips signs of ranks > i: Δ = (−1)^{i+1}x + 2(−1)^i T with 0 ≤ T ≤ a_{i+1} (F1) — both parities give Δ ≤ x. For the pair removal, ranks strictly between i and j flip, ranks past j keep sign; Δ = (−1)^{i+1}x + (−1)^{j+1}y + 2(−1)^i U. All four parity cases check out, including the c = 0 subcase of case 3 and the F2/F3 uses (U ≥ a_{j−1} ≥ y for c odd; U ≤ a_{i+1} − a_{j−1} ≤ x − y for c even ≥ 2). Also spot-checked numerically during my Theorem B simulation (Lemma 4 bound never violated).

### Lemma 4 (Partition Lemma, A(M) = min_Π cost(Π)) — VERIFIED
Peeling telescopes since Lemmas 2–3 hold for arbitrary multisets; equality for the adjacent pairing is definitional. Correct.

### Theorem A (lower bound) — VERIFIED, this is the crux
- LB's config: pieces 2^0,…,2^n in units of 1/D. XY adds m ≤ n interior marks → N ≤ 2n+1 fragments → any pairing partition has ≤ n pairs.
- The graph claim ("bad component has ≥ |V(C)| edges") is correct: connectivity needs ≥ |V|−1 non-loop edges; exactly |V|−1 total edges forces a loop-free multiplicity-free tree (a multi-edge or loop would leave ≤ |V|−2 distinct adjacencies, disconnecting), and a tree is bipartite = good. Covers the |V|=1-with-loop case (1 edge ≥ 1).
- The counting contradiction (all bad ⟹ edges ≥ n+1 > n) is right, so a good (bipartite, loopless) component K exists.
- Block-locality (every pair/singleton stays within one component) holds because a pair is an edge. Signing gives cost_K ≥ |Σ_{i∈V(K)} δ_i 2^i| ≥ 2^t − (2^t − 1) = 1, since the powers are distinct. Other components contribute cost ≥ 0. Hence cost(Π₀) = A(M) ≥ 1 unit and oddsum ≥ (1 + 1/D)/2 = 2^n/D.
- Independent numerical attack: I minimized oddsum over all XY cut allocations and positions (Nelder–Mead, 150–200 restarts per allocation pattern) against LB's geometric config for n = 1, 2, 3. Minimum found: exactly 2^n units (2.0, 4.0, 8.0) — the bound is tight and never beaten.

### Lemma 5 (Folding) — VERIFIED
Invariant σ(A) − σ(B) = v through the cross-fold loop; B must empty first (else σ(B) = −v ≤ 0 with positive pieces); fold-down leaves ≤ 1 piece of length ≤ σ(A′) = v. Mark count: mark-iterations reduce the working count by exactly 1, markless (equal) iterations by 2, and a count-to-0 finish is necessarily markless (a strict fold always leaves a positive remainder), so marks ≤ |A|+|B|−1. Correct, including B = ∅ and v = 0 edge cases. All marks strictly interior to current pieces ⟹ distinctness is automatic.

### Theorem B (upper bound) — VERIFIED
- Case k ≤ n: halve all pieces, A(M) = 0, LB gets 1/2 < 2^n/D. Correct.
- Case k = n+1: pigeonhole on 2^{n+1} subset sums in [0,1] gives distinct T ≠ T′ with |σ_T − σ_{T′}| ≤ 1/(2^{n+1}−1); symmetric-difference sets fed to Lemma 5 (≤ |S|−1 marks) plus halving the rest (n+1−|S| marks) totals ≤ n marks. Final multiset = equal pairs + ≤1 leftover r ≤ 1/D, so A(M) ≤ r ≤ 1/D by Lemma 4, and LB is held to (1+1/D)/2 = 2^n/D by Lemma 0(ii).
- Independent simulation of exactly this strategy: 4000+ random LB configs per n ∈ {2,3,4,5} plus the outline-reviewer's two greedy counterexamples plus geometric configs — mark count always ≤ n, LB value always ≤ 2^n/D (worst case attains it exactly, at the geometric config). Adversarial Nelder–Mead maximization of the strategy value over LB configs at n = 2, 3 could not exceed 2^n/D.

## Answer verification
c(n) = 2^n/(2^{n+1}−1): matched bound + construction. n=1: 2/3 verified by direct play. n=2: 4/7 confirmed by my independent minimization (min oddsum = 4 units of 1/7 ⟹ LB gets (1+1/7)/2 = 4/7). Both directions numerically tight for n ≤ 3 (lower) and n ≤ 5 (upper). `answer_type: expression` satisfied — answer stated explicitly.

## Overclaim check
Builder's Status `solved` is accurate. No hand-waving found; every "case" enumerated is settled; no circularity (lower and upper bounds are independent; Lemma 4 is used in both but proved unconditionally); no crux-move citations — everything proved in-file. Pigeonhole is named and cited to knowledge_base.md.

## Scores
- Correctness: 10/10 — every step re-derived independently; numerics confirm both bounds exactly.
- Completeness / rigor: 10/10 — endpoint marks, zero-length pieces, duplicate-subset (v=0), B*=∅, k ≤ n, and mark-distinctness edge cases all handled explicitly.
- Progress: 10/10 — from unsolved to a complete proof in one build; both round-1 outline gaps (GAP I/II and the refuted greedy GAP III) replaced by correct arguments.

## Promotable lemmas — certification
1. **Lemma 0 (oddsum value)** — CERTIFIED. Statement exact, proof complete, no `sorry`-equivalent. → lemmas/oddsum-claiming-value.md
2. **Partition Lemma (Lemmas 1–4)** — CERTIFIED. Full parity casework present; statement not stronger than proved (A(M) = min_Π cost(Π)). → lemmas/partition-lemma.md
3. **Folding Lemma (Lemma 5)** — CERTIFIED. Mark count and leftover bound both proved; edge cases handled. → lemmas/folding-lemma.md

## Outcome recorded
`record_outcome(slug=pairing-exchange-normal-form, outcome=verified-milestone)` — "both bounds closed and verified; problem solved."

## Verdict: APPROVE (Status: solved)
