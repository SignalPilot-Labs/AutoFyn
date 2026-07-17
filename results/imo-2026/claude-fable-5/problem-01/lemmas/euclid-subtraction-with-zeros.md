# Lemma: euclid-subtraction-with-zeros

**Statement.** For nonnegative integers a, b, the pairs {a, b} and {min(a,b), |a − b|} have
identical sets of common divisors; hence equal gcds, with the convention gcd(0,0) = 0 (and one
pair is (0,0) iff the other is).

**Proof.** Proved in full as Lemma 4 of `approaches/per-prime-gcd-invariant.md` (WLOG a ≥ b;
d | a, d | b iff d | b, d | a − b; all zero-valuation cases checked explicitly). The same fact
appears as Fact E of `approaches/newman-confluence.md`.

**Certified** by proof-reviewer, round 1. sorry-free; statement exactly as proved.
