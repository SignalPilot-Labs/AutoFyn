# Approach: translation-self-similarity

## Status
unsolved

## Framing
Prove periodicity NOT by bounding primes or stabilizing a transversal family, but by exhibiting a translation symmetry directly: construct L (and T) so that the greedy rule COMMUTES with m ↦ m+L — i.e. the allowed set above a_T is exactly L + (allowed set above a_1). Then induction from the seed gives a_{n+T}=a_n+L from n=1 (or eventually). Bypasses the prime-bounding / free-rider wall entirely by proving the symmetry as a functional equation.

## Target
Prove ∃ T,L>0 with a_{n+T}=a_n+L for all n.

## Technique
Construction + induction via a translation-equivariance (functional) equation for the greedy map. Per knowledge_base "Invariants & monovariants" (translation invariance) and the crux spirit of aimo-0079 ("substitute x=m−a so a shift forces periodicity").

## Skeleton
1. **Reformulate the greedy.** Let A_n = {m > a_n : gcd(m,a_i)>1 ∀ i≤n} (allowed set above a_n). Then a_{n+1} = min A_n. The sequence is determined by the nested constraint sets.
2. **Self-similarity equation (the crux).** Seek T, L such that A_T = L + A_0 (as sets, where A_0 = {m > a_1 : gcd(m,a_1)>1}, and L+A_0 = {L+m : m∈A_0}) — i.e. the allowed set above a_T is the allowed set above a_1, translated by L. Mechanism to find L: L must be a period of the prime-divisor structure, i.e. L ≡ 0 mod every prime that could be "relevant"; conjecturally L = product of the essential primes (but this approach tries to AVOID naming them — derive L as any common period of the residue classes {a_i mod (small modulus)} for i=1..T). Candidate: L = 2·rad(a_1)·(forced primes) — compute from seed.
3. **Translation-equivariance of the greedy min.** If A_T = L + A_0 (translation as sets) AND a_T = a_1 + L (the base alignment), then min A_T = min(L + A_0) = L + min A_0 = L + a_2, i.e. a_{T+1} = a_2 + L. — by translation-equivariance of "min".
4. **Inductive propagation.** Repeat: once a_{T+k} = a_k + L for all k ≤ n, the constraint set above a_{T+n} equals the constraint set above a_n translated by L (because each a_{T+i}=a_i+L has the same prime-divisor SET as a_i — PROVIDED adding L preserves prime divisors, i.e. L ≡ 0 mod each prime dividing any a_i). Hence A_{T+n} = L + A_n, so a_{T+n+1} = L + a_{n+1}. Induct forever. — by induction + the prime-divisor-preservation property.
5. **Base case verification.** Exhibit concrete T, L (from numerics: e.g. a_1=15 → T=8, L=30) and verify (a) a_T = a_1 + L, (b) P(a_{T+i}) = P(a_i) for i=1..T (translation preserves prime divisors because L is a multiple of every prime appearing in the first T terms). — by direct computation on the finite seed block.
6. **General existence of T, L (the hard part).** For ARBITRARY a_1, prove such T, L exist. Mechanism: take L = lcm of all primes dividing {a_1,…,a_T} for a sufficiently long prefix T; the prefix's prime set is finite; if the greedy on the prefix returns to a residue class matching a_1 (mod L) with the same prime-divisor signature, close the loop. Existence of such a return is itself a pigeonhole/finite-state claim (so this approach does NOT fully escape finite-state — but the INDUCTIVE LIFT is via self-similarity, which is the distinct mechanism).
7. **Conclude.** a_{n+T} = a_n + L for all n ≥ 1 (no transient, by the from-seed induction).

## Key lemmas (claim + one-line mechanism)
- **Lemma A (prime-divisor preservation under +L):** P(a_i + L) = P(a_i) whenever L is a multiple of every prime in P(a_i) — FALSE in general (e.g. 15+30=45, P=⟨3,5⟩ same ✓; but 18+30=48=2⁴·3, P={2,3} same as 18={2,3} ✓; 20+30=50=2·5² P={2,5} same ✓; 24+30=54=2·3³ P={2,3} same ✓). Mechanism: if L ≡ 0 mod p for each p|a_i, then gcd(a_i+L, a_i) = gcd(L, a_i) = a_i (if L multiple of a_i) — NOT generally. The correct mechanism: a_i + L ≡ a_i (mod p) for each p|a_i, so each p|a_i still divides a_i+L; but NEW primes can appear (e.g. 15+30=45, no new; but 6+30=36=2²·3², P={2,3} same as 6={2,3} ✓). The lemma as stated (P preserved) is STRONGER than "old primes still divide" — it forbids new primes. This is the crux: need L such that a_i+L has NO new prime. NOT automatic.
- **Lemma B (self-similarity of A):** A_{T+n} = L + A_n — mechanism: the constraint "m hits a_{T+i}=a_i+L" is, mod each prime, the same as "m−L hits a_i" (because a_{T+i} ≡ a_i mod p for p|L). So m∈A_{T+n} iff (m−L)∈A_n, PROVIDED the only primes that matter are divisors of L.
- **Lemma C (existence of the closing return):** some T makes a_T ≡ a_1 (mod L) with matching prime-divisor signature — mechanism: pigeonhole on the finite residue-tuple state (this borrows finite-state, but only for EXISTENCE of the return, not for the periodicity lift).

## Open gaps
- Lemma A is the wall: P(a_i+L)=P(a_i) is FALSE in general; need to either (i) weaken to "the GREEDY DECISION is preserved" (which only needs old primes to persist, not new primes to be absent — because new primes in a_i+L would only make it MORE connected, not less, so the greedy min is unaffected upward) OR (ii) prove L is special (a "fixed point" of the prime structure). The correct weakening must be identified.
- Step 6: existence of the closing return for arbitrary a_1 — this may collapse back into finite-state pigeonhole (approach crude-reduced-type). The distinct contribution of THIS approach is the inductive lift (step 4); if existence also needs finite-state, the approach is a hybrid. That's acceptable but note it.
- T, L for the general case: numerics give candidates for small a_1 but not a general construction.

## Cases to cover
- Even a_1, prime-power a_1: T=1, L=2 resp. L=p trivially satisfy the self-similarity (a_1+L has same prime divisors). Sub-case handled.
- a_1=1001 (long transient): the from-seed induction may FAIL if transient > 0; need the eventual version (shift the base to a_N for large N).

## Watch out for
- Lemma A as literally stated is false; do not assert P(a_i+L)=P(a_i) without the weakening. The right statement is about the greedy min being preserved, which is more forgiving.
- a_1=1001 had no period in 1500 terms — the from-seed induction likely fails here; the approach must allow EVENTUAL self-similarity (base at a_N, not a_1).
- The approach is genuinely different in LIFT mechanism (inductive symmetry vs finite-state pigeonhole) but may share the existence-of-return step with crude-reduced-type. Keep the lift distinct.
