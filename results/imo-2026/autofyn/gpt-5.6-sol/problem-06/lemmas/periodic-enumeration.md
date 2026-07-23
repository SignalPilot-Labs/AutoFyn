# Periodic enumeration lemma

Let \(A,L\) be positive integers, and let \(G\) be an infinite subset of \(\{A,A+1,\ldots\}\) such that
\[
m\in G\quad\Longleftrightarrow\quad m+L\in G
\qquad(m\ge A).
\]
Put \(T=|G\cap[A,A+L)|\). If \(T>0\) and \(g_1<g_2<\cdots\) is the increasing enumeration of \(G\), then
\[
g_{n+T}=g_n+L
\]
for every \(n\ge1\).

## Proof

For \(j\ge0\), let
\[
B_j=[A+jL,A+(j+1)L)\cap\mathbb Z.
\]
Translation by \(L\) is an order-preserving bijection from \(G\cap B_j\) to \(G\cap B_{j+1}\). It maps into the latter set by the assumed equivalence; it is onto because if \(y\in G\cap B_{j+1}\), then \(y-L\ge A\), and the equivalence applied to \(y-L\) gives \(y-L\in G\cap B_j\). Thus each block contains exactly \(T\) elements.

Write the unique division of \(n\ge1\) as \(n=jT+k\), where \(j\ge0\) and \(1\le k\le T\). Then \(g_n\) is the \(k\)-th element of \(G\cap B_j\), because the preceding \(j\) blocks contain \(jT\) elements. The order-preserving translation sends it to the \(k\)-th element of \(G\cap B_{j+1}\), whose global index is \((j+1)T+k=n+T\). Hence \(g_{n+T}=g_n+L\). ∎
