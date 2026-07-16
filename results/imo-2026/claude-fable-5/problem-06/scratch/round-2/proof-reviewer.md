# Round 2 — proof-reviewer report (independent adversarial re-verification)

Problem: `imo-2026-06` (IMO 2026 P6, proof_only, answer_type none). Candidate under review: the round-1-approved Full proof in `results/imo-2026-06/current.md`, from approach `crt-window-small-prime-lockin`. Treated as an unverified candidate; every step re-audited from scratch.

## Answer-to-question check
The proof targets exactly the problem's claim: existence of positive integers T, L with a_{n+T} = a_n + L for **every** n ≥ 1 (not just eventually). It proves periodicity from n = 1, which is what the statement demands. No final-answer requirement (answer_type none). Matches.

## Step-by-step audit (independent)

- **Standing facts.** Strict increase, unboundedness, well-definedness of the greedy step (candidate 2a_n always works). Valid.
- **Step 1 (pairwise sharing).** gcd(a_i, a_j) > 1 for all i, j: defining condition for i < j, trivial for i = j. Valid — and correctly covers the "future terms" direction needed in Step 2 (⊆): a term shares a factor with every term, including later ones, because the later term's defining condition covers the pair.
- **Step 2 (terms = V).** (⊇) uses finiteness of terms < m, candidacy of m at step n+1 (needs gcd only with a_1..a_n — correct, no over-requirement), greedy minimality gives a_{n+1} ≤ m, maximality of n gives a_{n+1} ≥ m. Valid; no circularity (V defined via the sequence, used only as a characterization).
- **Step 3 (H* = types; realization).** The construction m_j = p_1^j p_2⋯p_r has P(m_j) = X exactly, meets every P(a_k) since X ∈ H*, and is eventually ≥ a_1, hence in V, hence a term. Corollaries 3.1 (intersecting) and 3.2 (descent to minimal member) are correct finite-set arguments. "Every Y ∈ M meets A" and "every element of A ≤ g = ∏A" both valid (each p ∈ A divides g).
- **Step 4 (Exclusion Principle).** Static residue of greedy minimality; the a_{n+1} = m sandwich is the same valid argument as Step 2 (⊇). Verified by fresh code: 0 EP failures on all non-terms in (385, 30000) and on 8 other seeds.
- **Step 5 (Quantitative Witness).** Checked line by line. Key points all sound: X = Y∖{ρ} ∉ H* by minimality of Y; m > a_1 forced (else P(m) = P(a_1) ∈ H*); m not a term (type not in H*); EP gives term t < m with P(t) ∩ X = ∅; P(t) ∩ Y ⊆ {ρ} and nonempty (Cor 3.1) forces ρ ∈ P(t); U ⊆ P(t) minimal has U ∩ Y = {ρ}; and the number-theoretic size bound ∏_{p∈U} p ≤ ∏_{p∈P(t)} p ≤ t < m (radical divides t). This size bound is the essential input the certified no-go lemma shows cannot be dispensed with — consistent.
- **Step 6 (load-bearing step — re-derived independently).** Suppose prime ρ ≥ a_1·g in Y_1 ∈ M. Since a_1 ≥ 2, ρ ≥ 2g > g ≥ max A, so ρ ∉ A; every M-member containing ρ then contains an A-element ≠ ρ, so has size ≥ 2 (this note also guarantees X_{i+1} ≠ ∅ for the QW output U, so c_{i+1} ≥ 2 — checked). Case (a) (c_i ≥ a_1): m = c_i is a legitimate QW input (squarefree, P(m) = X_i); output gives ρ·c_{i+1} < c_i, so c_i strictly decreases — infinite run impossible by well-ordering. Case (b) (c_i < a_1): minimal j ≥ 1 with s_i^j c_i ≥ a_1 exists (s_i ≥ 2); m = s_i·(s_i^{j−1}c_i) < s_i·a_1 ≤ g·a_1 ≤ ρ by minimality of j (j−1 ≥ 0 and s_i^{j−1}c_i < a_1, using c_i < a_1 for j−1 = 0); QW gives ρ < m — contradiction. Cases exhaustive and disjoint by trichotomy. My independent derivation reproduces the claim exactly. The remark that the stronger bound ρ ≤ g is FALSE (a_1 = 385) was re-confirmed by fresh computation: {2,11,19} is a minimal member with 19 > g = 14, but 19 < a_1·g = 5390.
- **Step 7 (E finite, common-E-prime claim).** E ⊆ {primes < a_1·g} finite; Claim 7.1 (any two terms share a prime of E) via U ⊆ P(t), U ∈ M ⊆ H*, Cor 3.1. Valid.
- **Step 8 (finale).** Claim 8.1 (m ∈ V ⟺ m+L ∈ V for m ≥ a_1, L = ∏E) — both directions checked; the (⇐) direction correctly uses that m+L is a term and p | L, p | m+L ⟹ p | m. φ(x) = x+L is a strictly increasing bijection V → V ∩ [a_1+L, ∞) (surjectivity from (⇐)). a_n = v_n since the strictly increasing sequence enumerates exactly V and min V = a_1. The index-matching induction (φ(v_n) = v_{n+T} with T = |V ∩ [a_1, a_1+L)| ≥ 1) is spelled out and correct. Conclusion a_{n+T} = a_n + L for all n ≥ 1.

## Adversarial checks performed (fresh code, independent of round-1 scripts)

1. **Sieve-based greedy simulator** (not the round-1 bitmask script): 9 seeds — 6, 10, 15, 21, 22, 35, 45, 77, 385.
2. **Exclusion Principle:** 0 failures on every seed's full simulated range (for 385: all non-terms in (385, 30000)).
3. **Minimal members / bound:** for a_1 = 385, recomputed minimal transversals on a 15278-term prefix: {2,7}, {2,3,5}, {2,3,11}, {2,11,19}, {3,7,11}, {3,7,19}, {5,7,11}; E = {2,3,5,7,11,19}; every prime < a_1·g = 5390 (Step 6 bound holds; strict p ≤ g bound fails at 19, as the proof's Remark states). ∏E = 43890 = claimed L.
4. **Exact periodicity from n = 1** with the proof's own T, L definitions: holds on all 9 seeds; for 385, T = 5088, L = 43890, verified across all 15278 simulated terms (three full periods).

No gap, skipped case, circularity, or crux-move citation found. Edge cases checked: singleton members of M (handled by the |Z| ≥ 2 note), m = a_1 degenerate QW input (excluded inside QW), j ≥ 1 in Case (b) (forced by c_i < a_1), |A| = 1 (max A = g still holds).

## Certified lemmas
No new promotable lemmas this round (round-1 certifications stand; nothing new was flagged).

## Scores — `crt-window-small-prime-lockin`
- Correctness: 10/10 — every step re-derived; load-bearing Step 6 reproduced independently.
- Completeness / rigor: 10/10 — all cases settled, tools named, no hand-waving found under adversarial reading.
- Progress: solved (unchanged from round 1; this round confirms it).

## True Status
**solved.** Builder's recorded Status is correct. `current.md` updated with the round-2 re-verification note; Full proof unchanged.

## Outcome recorded
`record_outcome(imo-2026-06, crt-window-small-prime-lockin, round 2, verified-milestone)` — note: independent re-verification passed, APPROVE confirmed.

## Verdict
**APPROVE** (slug `crt-window-small-prime-lockin`, Status: solved)
