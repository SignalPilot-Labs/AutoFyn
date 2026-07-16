ALWAYS: When analyzing a gcd/lcm board operation, immediately compute what happens to p-adic valuations (v_p) for each prime separately — the operation on the pair (v_p(m), v_p(n)) → (min, |diff|) is the Euclidean subtraction step, which reveals invariants like gcd of the valuation multiset. (because this was the key structural observation for imo-2026-01, round 1)
ALWAYS: Look for aimo-0440 (blackboard subtraction to zero) and aimo-0678 (gcd/lcm recurrence) in the crux corpus when dealing with gcd/lcm blackboard problems — these are the most analogous crux moves. (round 1)

ALWAYS: For termination of board games where one operation keeps a monovariant constant, pair it with a second quantity (like N_gt1 or count of numbers > 1) and use lexicographic ordering on the pair. (because product alone was insufficient when gcd(m,n)=1 for imo-2026-01, round 1)

ALWAYS: Distinguish the "coordinatewise gcd of exponent vectors" from the "ordinary gcd" — they differ when numbers share no common prime factor but each prime has valuations with gcd > 0 (e.g., [2,3]: ordinary gcd=1, but M=6). (because the invariant for imo-2026-01 is NOT the ordinary gcd, round 1)

ALWAYS: Check gcd(k,0) = k convention when any valuation might be 0 — this is what ensures D_p ≥ 1 whenever some board number has prime factor p, preventing the N_gt1=0 case. (because this convention is load-bearing in the termination argument for imo-2026-01, round 1)
ALWAYS: For a blackboard process with k = count of numbers > 1, verify the three move cases: (A) m=n gives k→k-1, (B) gcd(m,n)=1 gives k→k-1, (C) gcd>1 and m≠n gives k→k (but P→P/gcd). Never assume k only changes via one mechanism. (confirmed computationally for imo-2026-01, round 1)
