# Outline review — imo-2026-01 (IMO 2026 P1), round 1

Problem: 2026 integers >1; move replaces m,n by (gcd, lcm/gcd); continue while ≥2 entries >1.
(a) exactly one survivor M>1; (b) M is choice-independent. `answer_type: none`, medium.

## Numerical verification of the load-bearing claims (all passed)
- **(1) primewise action (a,b)↦(min, max−min):** v_p(gcd)=min, v_p(lcm)=max, v_p(lcm/gcd)=max−min. Verified.
- **(2) g_p exact-invariant:** `gcd(min(a,b),max(a,b)−min(a,b))=gcd(a,b)` checked for all 0≤a,b≤14; changing two multiset entries to a pair with the same pairwise gcd preserves the overall gcd via `gcd(S)=gcd(gcd(rest),gcd(pair))`. Sound and non-circular.
- **Single survivor + M=∏p^{g_p}, order-independent:** 2000 random boards (n=2..8, values 2..60) × 20 random plays each — every play ended with exactly one survivor equal to `∏_p p^{g_p}`. No mismatch.
- **Local-confluence necessary condition** (for confluence approach): 3000 boards (n=3..5), every pair of distinct first moves led to boards with the same normal form. Holds.

## per-prime-gcd-invariant — APPROVE (strongest, lowest risk)
Framing is fully sound end-to-end. Load-bearing claims (1),(2),(3) are all correct:
- Step 4 "≤1 survivor" is genuinely definitional from move-legality (needs two entries >1), **not** circular.
- Step 5 "≥1 survivor" from g·ℓ=lcm(m,n)>1 is prime-free and airtight (outputs never both 1).
- Lemma B lex monovariant is correct: on gcd>1 moves Ω_total strictly drops (Ω(gcd)>0); on gcd=1 moves Ω_total is constant and K drops by 1 (gcd output =1); K never increases (two touched slots contribute at most 2 to K). So (Ω_total,K) strictly lex-decreases every move — termination is airtight. Concentration onto one slot is FORCED by the terminal condition, correctly not treated as a hard fact.

Issues for the builder to close (fixable, not blocking):
- Write Lemma A with the multiset-gcd associativity `gcd(A∪B)=gcd(gcd A,gcd B)` stated explicitly and the `gcd(0,x)=x`, `gcd(0,0)=0` conventions for positions where p∤entry (exponent 0).
- Lemma B: state the m=n subcase (g=m, ℓ=1, K drops) and the identity Ω(g)+Ω(ℓ)=Ω(m)+Ω(n)−Ω(gcd).
- Step 7: gcd of {2025 zeros, one e_p} = e_p, and all nonzero exponents live in the single terminal slot.

## strong-induction-descent — APPROVE (sound; shares the g_p engine)
Same monovariant + g_p-preservation engine as approach 1, but recursive: strong induction on Φ=(Ω_total,K), IH carries the value μ(B)=∏p^{g_p}. The step is valid strong induction — every first move drops Φ and preserves μ, so every play ends at μ(B), giving (b) from the IH without any terminal-state structure argument. Legitimate architectural variant.
Builder must: state P(B) over ALL board sizes (B′ may contain inert 1s = exponent-0 slots); keep μ(B) inside the IH (else (b) is lost); handle the base case (Φ minimal ⇒ ≤1 entry >1, plus non-collapse ⇒ exactly one = μ(B)).

## confluence-normal-form — APPROVE (diversity approach; carries the real risk)
Prime-free (a) via (P=∏a_i, A=#{>1}) is sound: P halves on gcd>1 moves, A drops on gcd=1 moves, both well-founded. (b) via Newman's Lemma is a genuinely capable technique (terminating + locally confluent ⇒ unique normal form), and it is the framing furthest from the compute-M route — worth keeping for diversity.

**The load-bearing risk is exactly Gap 1 (local-confluence overlap case), confirmed.** The disjoint case (commuting moves) is trivial; the danger is the 3-slot overlap case. Specific guidance for the builder:
- Local confluence must be proven WITHOUT assuming global confluence (Newman's whole point). Do NOT prove Gap 1 by asserting "the 3-entry sub-board has a unique terminal" — that IS confluence for n=3 and is circular if invoked bare. The clean route is well-founded induction on Φ: assume all boards of smaller Φ are confluent, then the overlap join reduces to a smaller-Φ instance. Alternatively an explicit finite continuation of both B1,B2 to a common board.
- Do NOT smuggle g_p in (would collapse this into approach 1).
- Fallback flagged by the outliner (direct order-independence / swap argument) is acceptable if the confluence write-up proves intractable — flag early rather than stall.

## Diversity of the field
Approaches 1 and 3 share the g_p-preservation engine (they die together if that engine fails — but it is verified sound). Approach 2 (confluence) is the genuinely distinct framing and the only prime-free route to (b). No approach repeats a recorded dead end (none exist yet). Field is adequately diverse for round 1.

## Ranking (Elo after this round)
per-prime-gcd-invariant 1531 > strong-induction-descent 1500 > confluence-normal-form 1469.
Rationale: per-prime is the cleanest, most self-contained, lowest-risk full solve; strong-induction is sound but shares the engine (lower marginal value); confluence is the diversity play but carries the one genuine open risk (Gap 1).

## Build decision
Build the two lowest-risk approaches most likely to produce a complete, correct solve this round. per-prime-gcd-invariant is the primary (should close all gaps to `solved`); strong-induction-descent adds a robustness/architecture variant that yields (b) via the IH without a terminal-state argument. confluence-normal-form stays live in the population for diversity but is not built this round (its Gap 1 risk makes it a poorer round-1 bet).

build set: per-prime-gcd-invariant, strong-induction-descent
