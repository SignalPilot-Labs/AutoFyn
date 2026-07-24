# Proof Review — imo-2026-01 (Confucius gcd/lcm blackboard), Round 1

Problem has TWO parts: (a) exactly one M>1 remains after finitely many moves; (b) M is choice-independent. Both candidates target both parts end to end.

## Independent verification (mine, from scratch)
- Per-prime move rule: with a=v_p(m), b=v_p(n), the move sends (a,b) ↦ (min(a,b), |a−b|). Confirmed from FTA (v_p(gcd)=min, v_p(lcm)=max).
- Subtractive identity gcd(min(a,b),|a−b|)=gcd(a,b): checked exhaustively for all a,b∈[0,40) — no failures.
- Full mechanism: simulated 2000 random boards (sizes 2–6, values 2–60) × 15 random plays each. Every play left exactly one survivor, and its value ALWAYS equaled ∏_p p^{gcd(v_p across board)}, identical across all plays of a board. Confirms unique survivor (part a), the value formula, and choice-independence (part b).

## Approach 1 — global-lex-monovariant → APPROVE (Status: solved)
Scores: Correctness 10/10, Completeness/rigor 10/10, Progress: full solution.

- Part (a) termination: Φ=(N,P), N primary. Lemma 1 (P_new=P_old/gcd) and Lemma 2 (coprime move drops N by exactly 1; non-coprime keeps/drops N) are correct. Lemma 3 lex-descent case split is exhaustive and disjoint (gcd=1 vs gcd>1); every branch strictly drops Φ. Lemma 4 well-foundedness of lex on ℤ_{≥0}×ℤ_{≥1} argued correctly (N eventually constant ⇒ P strictly descends among positive integers). 
- Terminal N∈{0,1} correct (move possible iff N≥2). N=0 excluded via g_p invariant with an explicit non-circular note (Lemma 6 uses no termination claim). v_p(M)=g_p read off correctly via gcd(v_p(M),0,…,0)=v_p(M).
- Part (b): g_p invariance via (B1) subtractive identity (all boundaries a=b, a=0, b=0 checked) and (B2) gcd associativity over a zero-containing multiset. Correct. M=∏ p^{g_p} depends only on initial board.
- All boundary cases handled: a=b, zero exponents, coprime moves, m=n. gcd conventions stated correctly. No hand-waving, theorems named (FTA, well-ordering).

No gap found. Builder's recorded Status `solved` is correct.

## Approach 2 — per-prime-valuation-descent → APPROVE (Status: solved)
Scores: Correctness 10/10, Completeness/rigor 10/10, Progress: full solution.

- Genuinely distinct termination framing: Φ=(Ω,N) with Ω=Σ_i Ω(x_i) primary. Step 1 (ΔΩ=−Σ_p min(a_p,b_p)≤0, strict iff gcd>1) correct. Step 2 (coprime drops N by exactly 1) correct. Step 3 lex descent exhaustive/disjoint. Step 4 gives a correct explicit bound (Ω₀+1)·2026. The "no new primes" argument (g|m, h|lcm) correctly justifies Ω finite and well-defined — a subtlety approach 1 sidesteps by using the product.
- Part (b) identical g_p invariant, Lemma 1 (subtractive identity, boundaries explicit) and Lemma 2 (gcd determined pairwise via universal common-divisor property) both correct. Step B3 reads off M correctly. N=0 excluded non-circularly (Step 5 cites B2, which is termination-free). Sanity example {4,6}→6 correct.

No gap found. Builder's recorded Status `solved` is correct.

## Both circularity check
Neither proof is circular: the g_p invariant (part b) is proved with no appeal to termination, and part (a) imports only that invariant to exclude N=0. Confirmed in both.

## Certified lemmas (admitted to results/imo-2026-01/lemmas/)
- valuation-gcd-invariant.md — g_p invariance + subtractive identity (both approaches).
- termination-lex-monovariant.md — both monovariant forms (N,P) and (Ω,N), well-founded.

## Actions taken
- current.md written: Status=solved, Full proof = global-lex-monovariant (self-contained, product manifestly finite).
- record_outcome: verified-milestone for both slugs.

Final: both approaches are complete, rigorous, correct proofs of both parts.
