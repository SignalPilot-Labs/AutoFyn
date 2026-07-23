ALWAYS: Run Python experiments early on sequences/combinatorics problems to discover the numerical structure before thinking about proofs (because experimental data reveals the right conjecture faster than pure thought, round 1)

ALWAYS: Verify periodicity experiments by checking a_{n+T} = a_n + L for n in a range of indices, not just a few (because periodic patterns can have a transient that confuses small-sample checks, round 1)

ALWAYS: For greedy sequence problems, compute the stable residue set mod L and verify it matches a simple number-theoretic characterization (because this reveals the right proof structure, round 1)

NEVER: Assume the stable prime set S equals the prime factors of a_1; S depends on the full dynamics and can both add and drop primes (round 1)

ALWAYS: Verify the periodicity statement holds for ALL n (not just eventually) — for IMO-style "a_{n+T}=a_n+L for all n" problems, this global version is often what's claimed and follows from a bijective state-machine argument, not just eventual periodicity (round 1, imo-2026-06)

ALWAYS: For greedy gcd-sequences, check the CLIQUE PROPERTY first (any two terms share a prime) — this is immediate from the definition and the key organizing lemma (round 1, imo-2026-06)

ALWAYS: Track when V mod M stabilizes (not when the prime set stabilizes) — the prime set may never stabilize but V mod M can stabilize after just a few terms (round 1, imo-2026-06)

ALWAYS: For greedy gcd-sequences, check if B^N = rad(a_1)^N is always a term — it is (every term shares a prime with a_1 via clique, so B^N in V_inf always). This gives P(a_1) as a persistent prime set and is the key lemma for proving E_inf finiteness (round 3, imo-2026-06)

ALWAYS: For antichain finiteness in greedy gcd-sequences, the correct target claim is E_inf ⊆ 2^{primes <= B} (all antichain primes <= rad(a_1)), NOT the weaker "each antichain element intersects P(a_1)". Test this computationally first (round 3, imo-2026-06)

NEVER: Apply the greedy "window" minimality argument (a_k/q in (a_{k-1}, a_k) hence invalid) for LARGE k -- for large k, a_k/q << a_{k-1}, so it's not in the window. The argument only applies for early terms (round 3, imo-2026-06)

NEVER: Assume the prime set of a greedy gcd-sequence is finite — new primes keep appearing in later terms as bonus factors, but their constraints are redundant mod M (round 1, imo-2026-06)

ALWAYS: For antichain-stabilization in greedy sequences, use the WQO (Dickson's lemma) applied to the SUBsequence of non-dominated terms — if P(a_i) ⊆ P(a_j) for i<j, the domination lemma shows a_j is dominated; so non-dominated prime sets form a bad sequence → finite by Dickson (round 2, imo-2026-06)

ALWAYS: For greedy gcd-sequences, consecutive terms ALWAYS share a prime ≤ rad(a_1). TRIVIAL PROOF: if large prime q > B divides both a_k and a_{k+1}, then q | (a_{k+1}-a_k) ≤ B < q, contradiction. This is the cheapest entry to the "small primes suffice" result (round 3, imo-2026-06)

ALWAYS: To prove two terms in a greedy gcd-sequence share a small prime (Small Common Prime Lemma), use aimo-0030 Claim 4 descent: assume (a_i, a_j) with i minimal shares only large primes; construct pure-small companion x_j (strip large primes, smallest ≥ a_1 with same small-prime set); use minimality of i to show x_j ∈ V_{i-1}; split on x_j < a_i (x_j is a prior term coprime to a_i, contradicts clique) vs x_j ≥ a_i (construct x_i too, show x_i is a prior term coprime to x_j, contradicts x_j ∈ V_{i-1}) (round 3, imo-2026-06)

ALWAYS: The greedy structural fact V_{i-1} ∩ (a_{k-1}, a_k) = ∅ for k ≤ i-1 implies V_{i-1} ∩ [a_1, a_{i-1}] = {a_1,...,a_{i-1}}: any V_{i-1}-valid element ≤ a_{i-1} must be a term. This is the key to both cases of the SCPL descent proof (round 3, imo-2026-06)

NEVER: Claim "E_n self-consistent iff E_n has a singleton" — counterexample: E* = {{2,3},{2,5},{3,5}} is self-consistent (every valid m divisible by ≥2 of {2,3,5}) with no singleton (round 2, imo-2026-06)

ALWAYS: Verify the "global for all n≥1" vs "eventual for n≥N" periodicity distinction in greedy sequence problems — the global version often requires showing all terms (including early ones) are already in V*, the stable valid set (round 2, imo-2026-06)

NEVER: Use Q=P(a_1) for the Small Common Prime Lemma in greedy gcd-sequences — this is FALSE (pairs (18,20) for a_1=15 share prime 2 ∉ P(a_1)={3,5}). The correct threshold is Q={primes ≤ p_max} where p_max=max prime factor of a_1 (round 3, imo-2026-06)

ALWAYS: For greedy gcd-sequences, the primes appearing in E_∞ (minimal antichain) are all ≤ max prime factor of a_1 — this makes E_∞ ⊆ 2^{finite Q}, so Dickson's Lemma gives finiteness. The WQO descent over P(a_1) fails; the correct approach is SCL + Dickson (round 3, imo-2026-06)

ALWAYS: When testing SCL (small common prime lemma), test with a_1 = product of two large primes like 101*103=10403 to stress-test: all pair-gcds still share primes ≤ 103 even when many intermediate primes appear as factors (round 3, imo-2026-06)
