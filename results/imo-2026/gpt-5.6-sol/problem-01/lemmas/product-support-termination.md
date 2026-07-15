# Product-support termination lemma

Consider a finite board of positive integers. A legal move chooses two entries \(m,n>1\) and replaces them by
\[
\gcd(m,n),\qquad \frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}.
\]
Let \(P\) be the product of all board entries and let \(r\) be the number of entries greater than \(1\). Then the positive integer \(2^rP\) strictly decreases under every legal move. Consequently every sequence of legal moves is finite.

## Proof
Put \(d=\gcd(m,n)\), \(L=\operatorname{lcm}(m,n)\). Since \(dL=mn\), the product of the two new entries is \(L=mn/d\), so the board product changes from \(P\) to \(P/d\).

If \(d=1\), the new pair is \((1,mn)\), so \(r\) decreases by one and \(P\) is unchanged. Hence \(2^rP\) is halved.

If \(d>1\), the new pair has at most two nonunits, so \(r\) does not increase, while the product is divided by \(d\ge2\). Hence \(2^rP\) again decreases by at least a factor of two. A positive integer cannot decrease strictly infinitely often, proving termination. ∎
