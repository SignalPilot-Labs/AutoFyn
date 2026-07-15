# Alternating discrepancy layer-cake lemma

## Statement
For a finite multiset \(B\) of nonnegative reals, sorted as \(b_1\ge b_2\ge\cdots\),
\[
D(B)=b_1-b_2+b_3-b_4+\cdots
=\int_0^\infty \mathbf 1_{\{\#\{i:b_i\ge t\}\text{ odd}\}}\,dt.
\]

## Certified proof
Use \(b_i=\int_0^\infty\mathbf1_{t\le b_i}\,dt\) and interchange the finite sum and integral. At each fixed threshold, the indicators are one for exactly the first \(N(t)\) sorted entries. Their alternating sum is one if \(N(t)\) is odd and zero otherwise. Endpoint conventions affect only finitely many thresholds and hence not the integral. ∎
