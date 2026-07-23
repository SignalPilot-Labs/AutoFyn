# Lemma: move-valuation

**Statement.** For positive integers m, n and any prime p, with a = v_p(m), b = v_p(n):
v_p(gcd(m,n)) = min(a,b), v_p(lcm(m,n)) = max(a,b), and v_p(lcm(m,n)/gcd(m,n)) = |a − b|.
Consequently the move {m,n} ↦ {gcd(m,n), lcm(m,n)/gcd(m,n)} acts on the valuation pair at every
prime simultaneously as (a,b) ↦ (min(a,b), |a − b|).

**Proof.** Proved in full as Lemma 1 of `approaches/per-prime-gcd-invariant.md` (from the
divisibility criterion of the Fundamental Theorem of Arithmetic: d | x iff v_p(d) ≤ v_p(x) for
all p; gcd is the number with valuations min, lcm the number with valuations max; the quotient
is an integer since gcd | lcm, so valuations subtract).

**Certified** by proof-reviewer, round 1. sorry-free; statement exactly as proved.
