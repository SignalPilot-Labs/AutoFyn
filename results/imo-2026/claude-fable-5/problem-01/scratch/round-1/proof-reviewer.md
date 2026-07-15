# Proof review — imo-2026-01, round 1

Problem: 2026 integers > 1 on a blackboard; move (m,n) → (gcd(m,n), lcm(m,n)/gcd(m,n)) on entries m,n > 1 at distinct places, repeated while possible. (a) Prove the process terminates with exactly one entry M > 1. (b) Prove M is choice-independent. `task: proof_only`, `answer_type: none` — no final numeric answer required; both parts must be proved. Both candidate proofs answer exactly this question.

## Independent verification performed (adversarial, both proofs)

The load-bearing step of BOTH proofs is the same pair of claims, which I re-derived from scratch and then attacked computationally:

1. **Per-prime move anatomy**: (a,b) = (v_p(m), v_p(n)) → (min(a,b), |a−b|), and gcd(a,b) = gcd(min(a,b), |a−b|) including zero cases — re-derived by hand (b=0: gcd(a,0)=a = gcd(0,a); a=b: gcd(a,a)=a=gcd(a,0); a>b≥1: standard subtractive Euclid). Correct.
2. **Exhaustive search over ALL move orders** (DFS on the full reachable-state graph, not sampled plays) on 87 initial boards — 74 random/structured + 13 adversarial (prime powers, equal entries, e.g. (8,8,8), (2^4·3^6, 2^6·3^4), (1024,32,8)): every reachable terminal board has **exactly one entry > 1**, and that entry **always equals ∏_p p^{gcd of p-exponents}** (multiset gcd with gcd(k,0)=k). 0 failures.
3. **25,000 random-move checks**: W = N + ΣΩ strictly decreases every move (0 violations); (P, N) strictly decreases lexicographically, with P|→P/d and P at-least-halving exactly when d = gcd ≥ 2, and N dropping by exactly 1 with q = mn when d = 1 (0 violations); Φ = ∏_p p^{G(A_p)} invariant (0 violations); ΔT = −Ω(gcd) exact (0 violations); no move ever outputs two 1s (0 violations).

## Approach 1: `prime-gcd-invariant` — VERDICT: APPROVE

**True Status: solved** (builder's recorded Status `solved` is correct).

**Scores.** Correctness 10/10; Completeness/rigor 10/10; Progress: full solution from a bare skeleton.

**Audit trail (what I checked, step by step).**
- Setup: multiset-gcd characterization (★) — existence via least positive linear combination + division algorithm, uniqueness via mutual divisibility, both zero cases handled explicitly. (G1) zeros inert, (G2) fold rule — both derived from (★) correctly. Sound.
- Lemma 1 (valuation formulas for gcd/lcm/quotient): rebuilt from (V1)–(V4); the constructions g = ∏p^min, ℓ = ∏p^max are verified as gcd/lcm via the common-divisor / common-multiple characterizations, not assumed. Sound.
- Lemma 2 (lcm/gcd = 1 ⟺ m = n) and Lemma 3 (no move outputs two 1s; cases A/B/C disjoint and exhaustive — checked: m=n vs m≠n splits, then gcd=1 vs gcd>1; the "gcd=1 forces m≠n" point is proven, not assumed). Sound.
- Termination: Lemma 4 (ΔT = −Ω(gcd), exact per-prime bookkeeping via (E) min+|a−b|=max) and Lemma 5 (ΔW ≤ −1 in all three cases; Case B is the critical one where T is flat and N carries the decrease — handled). W ≥ 0 integer + well-ordering ⇒ ≤ W(B₀) moves. Sound.
- Exactly one: N ≥ 1 preserved (Lemma 3, induction along the play, from N₀ = 2026), stopping ⟺ N ≤ 1 (legality iff N ≥ 2 — correct, board always has 2026 places), so terminal N = 1. Both directions present ("exactly one", not "at most one"). Sound.
- Part (b): Lemma 6 (subtractive Euclid with zero cases — all cases spelled out), Lemma 7 (multiset invariance via double fold (G2) + Lemma 6 — the per-prime/global-move legality subtlety is addressed explicitly), Step 6 reads v_p(M) = g_p(B₀) off the terminal shape, finiteness of relevant primes proven, M = ∏ p^{g_p(B₀)} choice-independent. No circularity: (b) uses (a) only for the terminal shape.
- Hidden-gap hunt: no "clearly/obviously/similarly" carrying weight; every WLOG justified by explicit symmetry; no crux-move citations; all knowledge-base tools named. Nothing found.

## Approach 2: `star-monoid-product-descent` — VERDICT: APPROVE

**True Status: solved** (builder's recorded Status `solved` is correct).

**Scores.** Correctness 10/10; Completeness/rigor 10/10; Progress: full solution, genuinely independent engines (different termination monovariant, different exactly-one argument).

**Audit trail.**
- Step 2, Lemma 2 (multiset gcd via CD(A) = D(g)): uniqueness via D(0) infinite vs D(g≥1) finite — correct; pair existence by strong induction on x+y with the subtractive step D(x)∩D(y) = D(x−y)∩D(y) (both inclusions written out; sum strictly drops since y ≥ 1; zero bases explicit); general existence by induction on |A|. Sound and self-contained.
- Lemma 3 (Euclid identity with zeros) via equality of common-divisor sets — cases b=0, a=b explicit. Lemma 4 (splitting off a pair) via CD algebra. Sound.
- Step 3: ⋆ well-defined (finitely many contributing primes via G({0,0})=0), monoid laws proven via Lemma 4; crucially Φ is defined **order-free** (∏_p p^{G(A_p(S))}), so no generalized-associativity hand-wave is load-bearing — the fold identity Φ(S ⊎ {y}) = Φ(S) ⋆ y is proven but only decorative. Sound.
- Step 4: Lemma 6 (Φ invariant — same double-fold argument, correct); Lemma 7 extremes: Φ ≥ 2 iff some entry > 1 (the flagged worry "Φ({2,3}) = 1?" is correctly resolved: gcd(k,0) = k so Φ({2,3}) = 6), Φ(all-ones) = 1, Φ({M,1,…,1}) = M — each verified from CD sets. Sound.
- Step 5: Lemma 8 — P(S′) = P(S)/d derived from dq = lcm = mn/d (Lemma 1(4)); integrality of P/d proven (d | m | P); d ≥ 2 vs d = 1 disjoint/exhaustive; d = 1 forces m ≠ n, q = mn > 1, N drops by exactly 1. Lemma 9 — infinite-play contradiction: at most log₂P(S₀) gcd≥2 moves (P at-least-halves and is never increased — the chaining is written out), then all moves have d = 1 and N strictly descends below 0. This is a correct concrete well-foundedness proof for the lex pair (P, N). Sound.
- Step 6/7: N(S_f) ≤ 1 (Lemma 10); N = 0 excluded by Φ(S_f) = Φ(S₀) ≥ 2 vs Φ = 1 — a genuinely different exactly-one argument from approach 1's, equally valid; M = Φ(S₀) choice-independent. No circularity.
- Hidden-gap hunt: nothing found; all cases audited in the file's own audit trail match the actual text.

Note the two approaches share the subtractive-Euclid core but prove it independently from scratch — no cross-citation of unproven material; the shared-fate risk did not materialize because both cores are correct (independently confirmed above).

## Lemma certifications

All four proposed lemma files checked against the proofs that claim to establish them; statements are exact (no overclaim beyond what is proved). All CERTIFIED (status lines updated in the files):
- `lemmas/move-anatomy.md` — certified (proved in prime-gcd-invariant Steps 1–2).
- `lemmas/multiset-gcd-invariance.md` — certified (proved in prime-gcd-invariant Setup + Step 5).
- `lemmas/multiset-gcd-characterization.md` — certified (proved in star-monoid Step 2; the part-5 recursion is indeed established inside the |A|-induction there).
- `lemmas/euclid-identity-with-zeros.md` — certified (proved in star-monoid Step 2, Lemma 3).

## Records and files

- `record_outcome`: `prime-gcd-invariant` → verified-milestone; `star-monoid-product-descent` → verified-milestone.
- `results/imo-2026-01/current.md` created: **Status: solved**, Full proof = prime-gcd-invariant's (the leaner engine), star-monoid noted as the certified alternative.
- Housekeeping note for the orchestrator: `problems.jsonl` lists imo-2026-01 as `difficulty_level: "medium"` (rating 5), not hard; the run targeted it per dispatch. Also, `newman-confluence` was registered but never built — with the problem solved it needs no further work.

**Goal Progress: SOLVED — imo-2026-01 `current.md` Status = solved (both built approaches APPROVED as complete proofs, recorded verified-milestone; ranking: star-monoid-product-descent 1516.8 / prime-gcd-invariant 1514.5 / newman-confluence 1468.7, expanded 1/1/0). Run goal met in round 1.**
