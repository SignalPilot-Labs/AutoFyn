# Lemma: non-collapse (a move's outputs are never both 1)

**Statement.** For a move on m,n>1 producing g=gcd(m,n), ℓ=lcm(m,n)/gcd(m,n), at least one
of g,ℓ exceeds 1. Consequently the board never becomes all-1s, and a board reached from a
board with ≥1 active entry again has ≥1 active entry.

**Proof.** g·ℓ = lcm(m,n) ≥ max(m,n) > 1 (each of m,n>1 divides lcm), so g,ℓ cannot both
equal 1. ∎

**Certified** (proof-reviewer, round 1): correct. Proved in per-prime-gcd-invariant (Step 6)
and strong-induction-descent (§4).
