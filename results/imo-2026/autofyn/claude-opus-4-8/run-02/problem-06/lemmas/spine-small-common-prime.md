# Certified lemma: the spine (SP) and hitting set (HS) — closes IMO 2026 P6

Certified round 2 (proof-reviewer), from `admissible-set-periodicity` (Steps A–E).
Independently re-derived and simulation-checked (0 SP-violations across 27 diverse a₁ up to 400 terms).
Notation as in `enumeration-and-bounded-gaps.md`: greedy sequence a₁<a₂<⋯, R=rad(a₁), S₀=supp(a₁);
"small" prime = p ≤ a₁, "big" = p > a₁; "term" = a member of the sequence (all ≥ a₁).

## Lemma A (bridge ★) and Corollary G3
For n ≥ a₁: n is a term ⇔ gcd(n,m) > 1 for every term m < n.
Corollary (G3): if x ≥ a₁ is not a term, some term b* < x has gcd(b*, x) = 1.
*Proof.* (⇒) Lemma 1. (⇐) n = a₁ is a term (vacuous hypothesis); for n > a₁, j = max{k : aₖ < n}
exists (aₖ → ∞), terms below n are a₁,…,a_j, hypothesis makes n eligible in the Rule for a_{j+1},
so a_{j+1} ≤ n, and maximality gives a_{j+1} ≥ n, hence = n. G3 is the contrapositive. □

## Lemma B (small prime factor)
Every term b has a prime factor ≤ a₁.
*Proof.* b = a₁: any prime of a₁. Else gcd(b, a₁) > 1 (Lemma 1); a common prime divides a₁, so ≤ a₁. □

## Lemma C (compression witness)
For every term b there is an integer x with supp(x) = {small primes dividing b}, no big prime factor,
and a₁ ≤ x ≤ b.
*Proof.* α = product of distinct small primes of b (α > 1 squarefree, α | b, α ≤ b). If b has no big
prime, x = b. Else fix big q | b, small p | b (p | α ⇒ p ≤ α), x = p^N α, N ≥ 0 least with x ≥ a₁.
N = 0: x = α | b. N ≥ 1: p^{N−1}α < a₁ ⇒ x = p·p^{N−1}α < p·a₁ ≤ α·a₁ < α·q ≤ b (using p ≤ α, a₁ < q,
αq | b). □

## Lemma D (spine SP)  ⇒  (HS)
Any two distinct terms share a common prime ≤ a₁. Hence S = {primes ≤ a₁} is a finite hitting set.
*Proof (minimal-counterexample descent).* Call distinct terms {b,b′} violating if they share no
prime ≤ a₁. If any exist, pick one with max b′ minimal (b < b′). Pick small p | b (Lemma B); p ∤ b′.
Compression x of b (Lemma C) has all primes small dividing b, none dividing b′ ⇒ gcd(x,b′) = 1,
a₁ ≤ x ≤ b < b′. If x were a term it would be distinct from b′ and coprime — contra Lemma 1; so x is
not a term, and G3 gives a term b* < x with gcd(b*,x) = 1. Then max{b,b*} = b < b′; distinct terms
b,b* share a prime r (Lemma 1); r small ⇒ r | b ⇒ r | x, contradicting gcd(b*,x) = 1 with r | b*. So
r is big, {b,b*} is violating with max < b′ — contradiction. Hence no violating pair; (SP) holds. □

## Consequence
With the certified Periodicity Machine (`finite-hitting-set-periodicity.md`) applied to
S = {primes ≤ a₁}, L = ∏_{p≤a₁} p, T = |A ∩ [a₁, a₁+L)| ≥ 1: aₙ₊T = aₙ + L for every n ≥ 1.
This completes IMO 2026 P6.
