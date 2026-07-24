# Lemma (per-prime move step) — CERTIFIED round 1

A move `{m,n} → {gcd(m,n), lcm(m,n)/gcd(m,n)}` (with m,n>1) acts, for every prime p, on the
touched valuation pair `(a,b)=(v_p(m),v_p(n))` by
```
(a,b) ↦ (min(a,b), |a-b|),
```
all untouched positions' valuations unchanged. In particular `lcm(m,n)/gcd(m,n)` is a positive integer.

Proof: v_p(gcd)=min(a,b) and v_p(lcm)=max(a,b) by unique factorization; since gcd|lcm the quotient is
integral and v_p(lcm/gcd)=max-min=|a-b|.

Certified by proof-reviewer, round 1 (verified for 2000 random (m,n) pairs across primes 2..13).
Source: perprime-valuation §1 / descent-induction §1.
