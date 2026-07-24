# proof-reviewer role memory

ALWAYS: for IMO-2026-06 (greedy pairwise-gcd sequence), the finite-hitting-set ⇒ exact-periodicity reduction is genuinely airtight and reviewer-certified in lemmas/; the ONLY open gap is finiteness of the essential/sole-connector prime set (HS/MCL). Pure Σ1/p² counting provably cannot close it (bounds pair density, not the number of distinct essential primes; sparse density-zero disjoint families evade it). Closing needs greedy minimality. (round 1)

NEVER: don't be fooled by a T=|A∩[a1,a1+L)| that equals the simulation length — that makes the a_{n+T}=a_n+L check vacuous. Generate enough terms (>> T) so the periodicity check is non-vacuous before trusting a numerical "periodOK". (round 1)

ALWAYS: for IMO-2026-06, the finiteness nucleus (HS) is CLOSED (round 2, APPROVE) — not by bounding sole-connector primes but by proving they cannot exist: spine (SP) "any two distinct terms share a prime <= a1", via greedy bridge (star)/G3 + compression witness + minimal-counterexample descent on max(pair). Problem SOLVED; do not reopen. (round 2)
