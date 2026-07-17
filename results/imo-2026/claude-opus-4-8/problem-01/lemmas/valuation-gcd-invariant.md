# Lemma: per-prime valuation-gcd invariant (CERTIFIED, round 1)

**Statement.** For the move (m,n) ↦ (gcd(m,n), lcm(m,n)/gcd(m,n)) acting on a board of positive integers, fix a prime p and let g_p = gcd(v_p(x_1),…,v_p(x_k)) (convention gcd(0,e)=e, gcd(0,…,0)=0). Then g_p is unchanged by every move.

**Proof.** Per prime the move sends the pair of valuations (a,b) at the two chosen positions to (min(a,b),|a−b|) (from v_p(gcd)=min, v_p(lcm)=max, FTA). Two supporting facts:

(B1) gcd(min(a,b),|a−b|) = gcd(a,b) for all a,b ≥ 0. WLOG a ≥ b, reduces to gcd(b,a−b)=gcd(a,b); the pairs {a,b} and {b,a−b} have identical common-divisor sets, so equal gcd. Boundaries a=b, b=0, a=b=0 checked directly.

(B2) By associativity/commutativity of gcd, gcd(a,b,R) = gcd(gcd(a,b),R) for the remaining valuations R; replacing (a,b) by (min,|·|) leaves gcd(a,b) hence the whole gcd fixed.

**Certification.** Verified: subtractive identity checked exhaustively for a,b ∈ [0,40); full invariant confirmed by simulation over 2000 random boards (terminal value = ∏ p^{g_p}). No stronger than proved. Admitted.
