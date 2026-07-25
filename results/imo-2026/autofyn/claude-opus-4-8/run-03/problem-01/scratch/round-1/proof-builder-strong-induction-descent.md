# Build report — strong-induction-descent (imo-2026-01), round 1

Status: **solved**. Both (a) and (b) proved via a single strong (well-founded) induction on Φ=(Ω_total, K) in lex order over admissible boards (≥1 active entry). Value μ(B)=∏_p p^{g_p} is carried inside the IH, so order-independence (b) drops out of the IH — no terminal-state structure argument needed (architecturally distinct from per-prime-gcd-invariant, which reasons about the terminal multiset directly).

## All reviewer/outliner asks closed
- Primewise action (a,b)↦(min,max−min): §1, from v_p(gcd)=min, v_p(lcm)=max.
- Φ strict lex-decrease, ALL cases: §3 — gcd>1 (incl. m=n), gcd=1 (K drops via output 1); Ω-balance identity Ω(g)+Ω(ℓ)=Ω(m)+Ω(n)−Ω(g) proved in §2. Well-foundedness of ℕ²-lex proved explicitly.
- Non-collapse: §4, prime-free (g·ℓ=lcm>1).
- μ preserved: §5, with (5a) subtractive Euclid gcd(min,max−min)=gcd(a,b) incl. boundary a=b, a=0, and (5b) multiset-gcd associativity gcd(S∪T)=gcd(gcd S,gcd T) with gcd(0,x)=x, gcd(0,0)=0 conventions.
- Induction ranges over ALL board sizes (admissible boards, inert 1s = exponent-0 slots) — B' after a move is handled generically; base case (Case 1, no legal move) gives survivor value = μ via g_p(B)=gcd(v_p(e),0,…)=v_p(e).
- Value μ(B) kept inside the IH (P(B) statement clause b′) — (b) not lost.
- Concrete example {4,6,9}, μ=6, two distinct plays both → 6 (§8).

## Spec concerns
None. Problem is `proof_only`, `answer_type: none` — no closed answer required, but M=∏_p p^{g_p} is stated explicitly for (b). Note the problem metadata lists difficulty_level "medium" (not hard), difficulty_rating 5; the run targets it anyway per dispatch. `2026` is irrelevant — proof holds for every n≥2 (and the induction for every admissible board).

## Distinctness
Shares Lemma 5 g_p engine with per-prime-gcd-invariant (flagged by reviewer as robustness variant). The distinct spine is the recursion: every first move drops Φ and preserves μ, IH delivers the survivor value; no argument about the structure of the terminal board is used to get (b). Kept far from confluence-normal-form (no rewriting/Newman machinery).

## Promotable lemmas
Lemmas 1, 3, 4, 5 (see approach file §Promotable). Lemma 5 is the shared g_p invariant — worth certifying into lemmas/ for import by per-prime-gcd-invariant.
