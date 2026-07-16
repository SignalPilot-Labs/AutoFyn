# Arithmetic-orbit lemma

Let \(f:\mathbb R_{>0}\to\mathbb R_{>0}\) satisfy
\[
\sqrt{\frac{x^2+f(y)^2}{2}}\ge \frac{f(x)+y}{2}\ge\sqrt{xf(y)}
\]
for all positive \(x,y\), and put \(g(t)=f(t)-t\). Then, for every \(y>0\) and integer \(n\ge0\),
\[
f^n(y)=y+ng(y),\qquad g(f^n(y))=g(y),\qquad g(y)\ge0.
\]

## Proof

Set \(x=f(y)\). Both outside terms in the sandwich are then \(f(y)\), so the middle term is also \(f(y)\). Hence
\[
f(f(y))=2f(y)-y,
\]
and therefore \(g(f(y))=g(y)\). Simultaneous induction now gives
\[
g(f^n(y))=g(y),\qquad f^{n+1}(y)=f^n(y)+g(f^n(y))=y+(n+1)g(y).
\]
If \(g(y)<0\), the Archimedean property supplies an integer \(n>y/(-g(y))\), for which \(f^n(y)=y+ng(y)<0\), contradicting the positive codomain. Thus \(g(y)\ge0\). ∎
