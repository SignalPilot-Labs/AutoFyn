# Lemma: exponent-pair Euclidean preservation

**Name:** exponent-pair Euclidean-step preservation of gcd

**Statement.** Let p be a prime. For integers x, y ≥ 1 with p-adic valuations
a = v_p(x), b = v_p(y), the move that replaces {x, y} by {gcd(x,y), lcm(x,y)/gcd(x,y)}
replaces the p-valuation pair {a, b} by {min(a,b), |a−b|}. Consequently

  gcd(a, b) = gcd(min(a,b), |a−b|),

so the gcd of the two valuations is preserved. With the convention gcd(0,k)=k
(and gcd(0,0)=0), this holds verbatim when one of a, b is 0.

**Proof.** By the standard p-adic valuation identities
v_p(gcd(x,y)) = min(v_p(x), v_p(y)) = min(a,b) and
v_p(lcm(x,y)) = max(v_p(x), v_p(y)) = max(a,b), hence
v_p(lcm(x,y)/gcd(x,y)) = max(a,b) − min(a,b) = |a−b|.
So the new valuation pair is {min(a,b), |a−b|}.

For the gcd preservation: by symmetry assume a ≤ b, so the new pair is
{a, b−a}. The (subtractive) Euclidean algorithm identity states
gcd(a, b) = gcd(a, b−a) for b ≥ a. To verify it: every common divisor of
{a, b} divides a and b, hence divides b−a, so it divides both entries of the
new pair; conversely every common divisor of {a, b−a} divides a and b−a,
hence divides (b−a)+a = b, so it divides both entries of the old pair. The two
sets of common divisors coincide, so their largest elements coincide:
gcd(a,b) = gcd(a, b−a). Substituting a = min(a,b), b−a = |a−b| gives
gcd(a,b) = gcd(min(a,b), |a−b|).

Zero case: if a = 0 (x not divisible by p), then min(0,b)=0 and |0−b|=b,
so the new pair is {0, b}; the old pair was {0, b}. Trivially preserved, and
indeed gcd(0,b) = b = gcd(0,b). Symmetric for b = 0. If a = b = 0, the new
pair is {0,0}, also preserved. ∎

**Certified by:** proof-builder (round 1), invariant-first approach.
**Location proved:** results/imo-2026-01/approaches/invariant-first.md (Step 1–2)
and this lemma file.
