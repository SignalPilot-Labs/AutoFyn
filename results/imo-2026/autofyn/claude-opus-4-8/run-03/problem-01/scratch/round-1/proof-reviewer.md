# Proof review — imo-2026-01 (IMO 2026 P1), round 1

Problem: 2026 integers > 1; a move replaces m,n>1 by gcd(m,n) and lcm(m,n)/gcd(m,n).
(a) exactly one entry M > 1 remains after finitely many moves; (b) M is choice-independent.
Two candidate approaches reviewed independently.

## Independent verification
Brute force (`python3`, sympy) over 20000 random boards (size 2–7, entries 2–60), each
played to termination several times with random move orders: **every** play ended with
**exactly one** survivor, and that survivor **always** equaled the predicted closed form
∏_p p^{g_p}, g_p = gcd of the p-adic valuations of the initial board. Zero mismatches. The
coprime-move concern was checked explicitly: [2,3] → gcd=1, lcm/gcd=6 → [1,6]; this is NOT
a no-op — K drops from 2 to 1 while Ω_total stays 2, so the lex monovariant still strictly
decreases. Both proofs handle this exactly.

## Approach 1: per-prime-gcd-invariant — APPROVE (Status: solved)

Checked against the reviewer's attack list:
- **v_p(lcm/gcd)=max−min and integrality:** (V1)/(V2) derived from first principles;
  ℓ=lcm/gcd is an integer because gcd | lcm. Correct.
- **Termination monovariant strictly decreasing on EVERY legal move:** Step 4 splits on
  gcd(m,n). Ω_total change = −Ω(gcd) (identity Ω(g)+Ω(ℓ)=Ω(m)+Ω(n)−Ω(gcd), re-derived and
  correct). gcd>1 → Ω_total drops; gcd=1 → Ω_total flat but K drops by exactly 1 (ℓ=mn>1
  active, g=1 inactive). m=n subcase folded into gcd>1. No no-op move exists on a legal
  move. Airtight.
- **Exactly one survivor:** ≤1 from move-legality (K≤2 needed, Step 5); ≥1 from non-collapse
  g·ℓ=lcm>1 (Step 6). Both directions independent and non-circular. Airtight.
- **g_p exactly preserved incl. 0-exponents / gcd-with-zero:** Step 3 uses the subtractive
  Euclid identity (E) + gcd-associativity with gcd(0,x)=x, gcd(∅)=0; n=2 boundary handled.
  Correct.
- **Part (b) concludes choice-independence:** Step 8 shows terminal e_p = g_p (initial), so
  M=∏p^{g_p} is a function of the initial board alone — genuinely choice-independent, not
  merely "an invariant exists." Correct.
- No skipped case, hand-wave, or overclaim found. Builder's Status `solved` is accurate.

Scores: Correctness 10/10, Completeness/rigor 10/10, Progress: full solution of both parts.

## Approach 2: strong-induction-descent — APPROVE (Status: solved)

Same engine lemmas (primewise action §1, Ω-balance §2, lex monovariant §3, non-collapse §4,
per-prime gcd invariant §5), packaged as one strong (well-founded) induction on Φ=(Ω_total,K)
carrying μ(B)=∏p^{g_p} in the IH.
- Lemmas §1–§5 individually correct (same content as Approach 1, verified above). §5 states
  the multiset-gcd and subtractive-Euclid sub-facts (5a,5b) cleanly with divisor-set
  arguments incl. d=0 convention. Correct.
- Main induction (§6): Case 1 (no legal move) forces K=1 and computes survivor = μ(B) via
  gcd(v_p(e),0,…,0)=v_p(e); serves as the well-founded base. Case 2 applies IH to B′ (which
  is admissible by Lemma 4 and has Φ(B′)<Φ(B) by Lemma 3); the tail of an arbitrary play is
  a play from B′, and μ(B′)=μ(B) by Lemma 5, so the survivor is μ(B) for EVERY play. The
  "arbitrary play" quantifier is handled correctly — order-independence (b) falls out of the
  IH. No circularity. Airtight.
- No skipped case, hand-wave, or overclaim. Builder's Status `solved` is accurate.

Scores: Correctness 10/10, Completeness/rigor 10/10, Progress: full solution of both parts.

## Notes
Both proofs are genuinely distinct framings (explicit terminal-state analysis vs. unified
strong induction) that arrive at the same closed form, so they do not share a single fatal
gap. Both are correct and complete. `current.md` set to `solved` with the per-prime proof as
primary. Promotable lemmas certified into `results/imo-2026-01/lemmas/`: per-prime-gcd-invariant,
lex-monovariant-termination, non-collapse (each held to the full bar, statements no stronger
than proved).

## Verdicts
- per-prime-gcd-invariant: **APPROVE** (solved)
- strong-induction-descent: **APPROVE** (solved)
