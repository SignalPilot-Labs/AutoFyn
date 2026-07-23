# Lemma: overlap-joining

**Statement.** Let a board hold m, n, k > 1 in three places (rest R), and let B₁, B₂ be the
results of the move on (m,n) resp. (m,k). Then both B₁ and B₂ reach, by explicit finite move
sequences, the same board {t, 1, E} ∪ R, where t = gcd(m,n,k) and E is the pair-collapse value
E₁ = E(mn/d², dk/t²) = E(en/t², mk/e²) = E₂ (d = gcd(m,n), e = gcd(m,k)); the key identity is
gcd(|α−β|, |min(α,β)−γ|) = gcd(|α−β|, |α−γ|) at every prime. This is local confluence in the
overlapping-places case.

**Proof.** Proved in full as Lemma 5, Case 3 (§5) of `approaches/newman-confluence.md`.
E₁ = E₂ re-derived independently by the reviewer and checked on 5000 random triples.

**Certified** by proof-reviewer, round 1. sorry-free; statement exactly as proved.
