# Lexicographic multiplicity descent

Consider the same board move. Let \(\Omega(t)\) be the number of prime factors of \(t\), counted with multiplicity, with \(\Omega(1)=0\). Define
\[
S=\sum_b\Omega(b),\qquad r=\#\{b:b>1\}.
\]
Then every legal move strictly decreases \((S,r)\) in lexicographic order. Consequently every sequence of moves is finite.

## Proof
For selected \(m,n>1\), put \(d=\gcd(m,n)\), \(L=\operatorname{lcm}(m,n)\). Complete additivity of \(\Omega\), together with \(mn=dL\) and \(L=d(L/d)\), gives
\[
\Omega(m)+\Omega(n)-\left(\Omega(d)+\Omega(L/d)\right)=\Omega(d).
\]
Thus if \(d>1\), then \(S\) decreases strictly. If \(d=1\), then the pair becomes \((1,mn)\); complete additivity shows that \(S\) is unchanged, while the number \(r\) of nonunits decreases by one. Hence \((S,r)\) always decreases lexicographically.

The nonnegative integer \(S\) can decrease only finitely many times, and while \(S\) is fixed, the nonnegative integer \(r\) strictly decreases at each move. Therefore an infinite sequence is impossible. ∎
