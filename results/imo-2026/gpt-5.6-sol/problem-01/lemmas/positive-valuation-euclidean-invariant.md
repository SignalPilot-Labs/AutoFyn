# Positive-valuation Euclidean invariant

Under the move
\[
(m,n)\longmapsto\left(\gcd(m,n),\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right),
\]
fix a prime \(p\). If \(p\) divides at least one board entry, then it continues to do so after the move, and the gcd of all positive \(p\)-adic valuations on the board is invariant. If \(p\) is absent, it remains absent.

## Proof
Write \(x=v_p(m)\), \(y=v_p(n)\). The two selected exponents change by
\[
(x,y)\longmapsto(\min(x,y),|x-y|).
\]
If both are zero, both remain zero. If exactly one is positive, that same positive exponent remains. If \(x,y>0\) and unequal, say \(x<y\), the pair becomes \((x,y-x)\), and
\[
c\mid x,\ c\mid y\quad\Longleftrightarrow\quad c\mid x,\ c\mid(y-x)
\]
for every positive integer \(c\). If \(x=y>0\), two copies of \(x\) become one copy of \(x\) and a zero. Thus in every case positivity of the selected support and the common divisors of its positive exponents are preserved. The unselected exponents do not change, so adjoining them preserves both conclusions for the entire board. ∎
