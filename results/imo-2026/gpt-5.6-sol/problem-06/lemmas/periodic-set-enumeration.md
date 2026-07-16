# Periodic-set enumeration lemma

## Statement
Let $G$ be an infinite subset of the integers at least $k$, let $L\ge1$, and suppose
\[
m\in G\quad\Longleftrightarrow\quad m+L\in G
\]
for every integer $m\ge k$. Set $T=|G\cap[k,k+L-1]|$, and suppose $T>0$. If $g_1<g_2<\cdots$ enumerates $G$, then $g_{n+T}=g_n+L$ for every $n\ge1$.

## Proof
Translation by $L$ is an order-preserving bijection from $G$ to $G\cap[k+L,\infty)$: the forward implication gives the map into the tail, while for $h\ge k+L$ in $G$, the reverse implication applied to $h-L\ge k$ gives $h-L\in G$. Exactly the $T$ elements of $G\cap[k,k+L-1]$ precede this tail. Hence the $n$th element of the tail is the $(n+T)$th element of $G$, while the order-preserving bijection identifies it with $g_n+L$. Therefore $g_{n+T}=g_n+L$. $\square$
