# Lemma: move-monovariant

**Statement.** For a board B of k ≥ 2 positive integers, let P(B) be the product of its
elements, C(B) the count of elements > 1, and N(B) = (k+1)·P(B) + C(B). Every real move
strictly decreases N; hence every sequence of moves is finite. (Stated for k = 2026 with
constant 2027 in the source.)

**Proof.** Proved in full as Lemma 1 (§1) of `approaches/newman-confluence.md`: if
g = gcd(m,n) > 1 the product drops by ≥ 1 while C does not increase; if g = 1 the product is
unchanged and C drops by exactly 1. Verified numerically on 2000 random moves by the reviewer.

**Certified** by proof-reviewer, round 1. sorry-free; statement exactly as proved.
