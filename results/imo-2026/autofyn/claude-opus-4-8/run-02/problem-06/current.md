# IMO 2026 P6 — tracking

## Status
solved

## Approaches tried
- `admissible-set-periodicity` (round 2) — **SOLVED, APPROVE.** Closed the last gap (HS) via the spine (SP): *any two distinct terms share a prime ≤ a₁*. Proved by a minimal-counterexample descent using the greedy bridge (★)/G3, Lemma B (small factor), and the compression witness (Step C). Hence S = {primes ≤ a₁} is a finite hitting set, and the certified periodicity machine yields aₙ₊T = aₙ + L for all n ≥ 1. Independently reviewer-verified step by step; SP confirmed with 0 violations across 27 diverse a₁ (primes, prime powers, primorials, products) up to 400 terms.
- `essential-prime-counting` (round 1) — partial. Interval-occupancy Σ1/p² counting; cannot exclude sparse density-zero disjoint families. Superseded.
- `profile-class-recruitment` (round 2) — partial. Rigorous reduction of (HS) to (REC) (both-infinite disjoint-profile types) via finite profile alphabet + Step 4a; (REC) recruitment-termination left as honest open gap. Superseded by the descent solve.

## Current best
Full solution below. The reduction (static admissible set A, enumeration, bounded gaps, and the
finite-hitting-set ⇒ exact-periodicity machine) was certified in round 1
(`lemmas/enumeration-and-bounded-gaps.md`, `lemmas/finite-hitting-set-periodicity.md`). The round-2
new content proves the finiteness nucleus outright, with the explicit hitting set S = {primes ≤ a₁}:
every pair of terms shares a *small* common prime, so no large "sole connector" ever arises.

## Full proof

**Setup.** Fix the greedy sequence a₁ < a₂ < ⋯ (all aᵢ > 1), where for every n,
aₙ₊₁ = min{ x > aₙ : gcd(x, aᵢ) > 1 for all i ≤ n } (Rule). For m > 1, supp(m) is its set of prime
factors. Put S₀ = supp(a₁), R = rad(a₁). Call a prime **small** if p ≤ a₁, **big** if p > a₁. Let
A = { x > 1 : gcd(x, aᵢ) > 1 for all i ≥ 1 } (the admissible set); a **term** is a member of the
sequence, and every term is ≥ a₁.

**Certified imports (round 1, reviewer-certified).**
- *Lemma 1.* For m ≠ n, gcd(aₘ, aₙ) > 1; every term lies in A.
- *Lemma 2 (enumeration).* aₙ₊₁ = min(A ∩ (aₙ, ∞)); (aₙ) is the increasing enumeration of A ∩ [a₁, ∞); no element of A lies strictly between consecutive terms.
- *Lemma 3 (bounded gaps).* Every multiple m > 1 of R lies in A; hence aₙ₊₁ − aₙ ≤ R and aₙ → ∞.
- *Periodicity Machine.* If S is a finite **hitting set** (every pair of distinct terms shares a prime in S) and L = ∏_{p∈S} p, then with T = |A ∩ [a₁, a₁+L)| ≥ 1 one has aₙ₊T = aₙ + L for every n ≥ 1. (Accepts any finite hitting set.)

It remains to exhibit one finite hitting set. We prove **(SP): any two distinct terms have a common
prime ≤ a₁**, which makes S = {primes ≤ a₁} (finite) a hitting set.

**Step A — the bridge (★).** *For an integer n ≥ a₁: n is a term ⇔ gcd(n, m) > 1 for every term
m < n.* (⇒) is Lemma 1. (⇐) If n = a₁ it is a term (no smaller term exists; hypothesis vacuous). If
n > a₁, let j = max{ k : aₖ < n } (finite, nonempty as aₖ → ∞); the terms below n are exactly
a₁,…,a_j, so gcd(n, aᵢ) > 1 for all i ≤ j, making n eligible in the Rule producing a_{j+1}; hence
a_{j+1} ≤ n, while maximality of j gives a_{j+1} ≥ n, so a_{j+1} = n. **Corollary (G3):** if x ≥ a₁ is
not a term, then (contrapositive) some term b* < x has gcd(b*, x) = 1.

**Step B — small factor.** *Every term b has a prime factor ≤ a₁.* If b = a₁, any prime dividing a₁
is ≤ a₁. Otherwise b, a₁ are distinct terms, so gcd(b, a₁) > 1 (Lemma 1); a prime dividing this gcd
divides a₁, hence is ≤ a₁.

**Step C — compression witness.** *For every term b there is an integer x with supp(x) = {small primes
dividing b}, no big prime factor, and a₁ ≤ x ≤ b.* Let α be the product of the distinct small primes
dividing b; by Step B, α > 1, squarefree, α | b (so α ≤ b), and supp(α) = {small primes of b}.
- If b has no big prime factor, take x = b: supp(b) is all small, a₁ ≤ b ≤ b.
- Otherwise fix a big prime q | b and a small prime p | b (so p | α, p ≤ α). Let N ≥ 0 be least with
  p^N α ≥ a₁ and set x = p^N α; then supp(x) = supp(α) and x ≥ a₁. If N = 0, x = α | b ≤ b. If N ≥ 1,
  minimality gives p^{N−1}α < a₁, so x = p·p^{N−1}α < p·a₁ ≤ α·a₁ < α·q ≤ b, using p ≤ α, a₁ < q, and
  αq | b (α squarefree over small primes of b, q ∉ supp(α), so αq is a product of distinct primes
  dividing b). In all cases a₁ ≤ x ≤ b as claimed.

**Step D — the spine (SP), by descent.** Call a pair of distinct terms {b, b′} **violating** if it
shares no prime ≤ a₁. Suppose one exists; by well-ordering pick a violating pair {b, b′}, b < b′, with
max = b′ minimal.
1. By Step B pick a small prime p | b; violating ⇒ p ∤ b′.
2. Take the compression x of b (Step C): every prime of x is a small prime of b, none dividing b′
   (violating), so gcd(x, b′) = 1, with a₁ ≤ x ≤ b < b′.
3. x is not a term: else x ≤ b < b′ would make x, b′ distinct terms with gcd 1, contradicting Lemma 1.
   As x ≥ a₁ and x is not a term, G3 gives a term b* < x with gcd(b*, x) = 1.
4. Then b* < x ≤ b, so b* ≠ b and max{b, b*} = b < b′. Being distinct terms, b, b* share a prime r
   (Lemma 1). If r were small, r | b would give r ∈ supp(x), so r | x; but r | b* and gcd(b*, x) = 1
   force r ∤ x — contradiction. Hence every common prime of b, b* is big, so {b, b*} is a violating
   pair with max b < b′, contradicting minimality of b′.

Therefore no violating pair exists: **(SP)** holds.

**Conclusion.** By (SP), every pair of distinct terms shares a prime in S = {primes ≤ a₁}, a finite
set; S is a finite hitting set. The certified Periodicity Machine, with L = ∏_{p ≤ a₁} p and
T = |A ∩ [a₁, a₁+L)| ≥ 1, yields aₙ₊T = aₙ + L for every n ≥ 1. Since T, L ≥ 1 are positive integers,
this is exactly the required conclusion. ∎
