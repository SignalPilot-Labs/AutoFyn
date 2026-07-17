## Status
partial

## Approaches tried
- Use the reflected map \(T(x)=2x-f(x)\) to manufacture inverse dynamics and then collapse two-sided positive arithmetic orbits.

## Current best
Writing \(g(x)=f(x)-x\) and \(T(x)=x-g(x)=2x-f(x)\), exact expansion yields
\[
(T(x)-y)^2+4x(g(x)-g(y))\ge0,
\]
\[
(T(x)-y)^2-2(g(x)-g(y))(y+f(y)+g(x))\ge0. \tag{1}
\]
Whenever \(T(x)>0\), substitution \(y=T(x)\) squeezes \(g(T(x))=g(x)\), hence \(f(T(x))=x\). If \(T(x)>0\) globally, then \(T=f^{-1}\), and every two-sided orbit obeys \(x_{n+1}-x_n=g(x_0)\). Positivity for all \(n\in\mathbb Z\) forces this increment to vanish, yielding \(f=\operatorname{id}\).

This route cannot by itself be the final classification because nonzero translations are genuine solutions and satisfy \(T(x)\le0\) for small \(x\). The approach must therefore split at the threshold set \(\{x:T(x)>0\}\): prove the reflected inverse mechanism forces \(g=0\) on any two-sided component, while the complementary initial segment propagates a single positive translation parameter to the entire domain.

Explicit gap: classify the threshold geometry without assuming monotonicity, and show it yields either \(g\equiv0\) or \(g\equiv c>0\). Then verify every translation.
