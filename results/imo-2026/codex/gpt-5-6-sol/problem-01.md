Let the initial integers be (x_1,\dots,x_{2026}).

  ### (a) Termination

  At any stage, let

  [
  P=\prod_{i=1}^{2026}x_i,
  \qquad
  K=#{i:x_i>1}.
  ]

  Suppose (m,n>1) are selected, and put (d=\gcd(m,n)). Since

  [
  mn=\gcd(m,n)\operatorname{lcm}(m,n),
  ]

  the product of the two new entries is

  [
  d\cdot \frac{\operatorname{lcm}(m,n)}d
  =\operatorname{lcm}(m,n)
  =\frac{mn}{d}.
  ]

  Thus the board product changes from (P) to (P/d).

  - If (d>1), then (P) strictly decreases.
  - If (d=1), the new entries are (1) and (mn), so (P) stays unchanged but (K) decreases by one.

  Moreover, (K) can never increase. Hence moves with (d=1) can occur only finitely many times, while moves with
  (d>1) can also occur only finitely many times because they strictly decrease the positive integer (P).
  Therefore the process terminates.

  At least one of the two new entries is always greater than (1): if (d>1), the first one is; if (d=1), the
  second one is (mn>1). Consequently, the board can never lose all its entries greater than (1).

  When the process terminates, there cannot be two entries greater than (1), since they would allow another move.
  Therefore exactly one entry (M) is greater than (1).

  ### (b) Independence of (M)

  Fix a prime (p). For every board entry (x_i), write

  [
  e_i=v_p(x_i).
  ]

  Consider the quantity

  [
  G_p=\gcd(e_1,e_2,\dots,e_{2026}),
  ]

  using the conventions (\gcd(0,a)=a) and (\gcd(0,\dots,0)=0).

  If the selected numbers have (p)-adic valuations (a) and (b), their replacements have valuations

  [
  \min(a,b)
  \quad\text{and}\quad
  \max(a,b)-\min(a,b)=|a-b|.
  ]

  Assume, for example, that (a\ge b). Then these are (b) and (a-b), and

  [
  \gcd(b,a-b)=\gcd(a,b).
  ]

  Thus replacing (a,b) by (\min(a,b),|a-b|) does not change the gcd of all (2026) valuations. Hence (G_p) is
  invariant under every move.

  At the end, the board consists of (M) and (2025) copies of (1). Therefore its (p)-adic valuations are

  [
  v_p(M),0,\dots,0,
  ]

  whose gcd is (v_p(M)). Consequently,

  [
  v_p(M)

  \gcd\bigl(v_p(x_1),v_p(x_2),\dots,v_p(x_{2026})\bigr)
  ]

  for every prime (p). Thus necessarily

  [
  \boxed{
  M=\prod_{p}
  p^{,\gcd(v_p(x_1),\dots,v_p(x_{2026}))}
  }.
  ]

  Only primes occurring in the initial integers contribute to this finite product. Since every prime exponent of
  (M) is determined solely by the initial board, (M) is independent of all choices made by Confucius.
  ─ Worked for 2m 30s ─────────────────────────────────────────────────────────────────────────────────────────────