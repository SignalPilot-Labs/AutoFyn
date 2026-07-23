## Status
partial

## Approaches tried
- Reformulate the condition as a two-point metric cone constraint on the graph of the displacement and classify all admissible graphs as parallel translates of the diagonal.

## Current best
With \(g=f-\operatorname{id}\), the two nonnegative squared residuals imply the symmetric pair of cone estimates
\[
|g(x)-g(y)|\le \frac{(x-f(y))^2}{x+y+f(x)+f(y)},\qquad
|g(x)-g(y)|\le \frac{(y-f(x))^2}{x+y+f(x)+f(y)}. \tag{1}
\]
They also give the crossed factorization
\[
U(x,y)-L(y,x)=-(g(x)+g(y))\bigl(2(x-y)+g(x)-g(y)\bigr). \tag{2}
\]
A metric rigidity lemma asserting that every positive graph satisfying (1) for all ordered pairs has constant nonnegative displacement would immediately classify all solutions. The intended proof should use (1) at intermediate points selected near the reflected centers \(f(x)\), rather than assuming continuity or surjectivity.

Explicit gap: prove the two-point cone-graph classification from (1), including discontinuous graphs and the possibility that \(g\) changes sign. Then verify directly that \(f(x)=x+c\), \(c\ge0\), satisfies both original inequalities.
