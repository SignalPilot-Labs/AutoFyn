# Finite-rank multiple-line lemma

Let
\[
\Omega=\{(a,b,c)\in\mathbb R_{>0}^3:a+b+c=1\},\qquad t\in(0,1),
\]
and let \(W_0\) be the states having a coordinate equal to \(t\). Recursively define
\[
W_{r+1}=W_r\cup\operatorname{Pre}(W_r),
\]
where a state belongs to \(\operatorname{Pre}(E)\) if there is a legal triangle cut for which both possible retained children lie in \(E\). If \(1\ne mt\) for every positive integer \(m\), then for each \(r\), \(W_r\) is contained in a finite union of lines of the form
\[
a=kt,\qquad b=kt,\qquad c=kt
\]
with \(k\in\mathbb Z_{>0}\).

## Proof

For finite \(K\subset\mathbb Z_{>0}\), write \(\mathcal H_K\) for the union in \(\Omega\) of the three kinds of lines above, with \(k\in K\). Certainly \(W_0\subseteq\mathcal H_{\{1\}}\).

Suppose \(W_r\subseteq\mathcal H_K\) for a finite \(K\), and consider a predecessor obtained by cutting the angle \(a\). If the cut divides \(a\) into \(x\) and \(a-x\), where \(0<x<a\), its children are
\[
C_1=(x,b,1-b-x),\qquad C_2=(a-x,c,b+x).
\]
Choose in each child a coordinate witnessing membership in \(\mathcal H_K\), say a coordinate of \(C_1\) equals \(pt\) and a coordinate of \(C_2\) equals \(qt\), where \(p,q\in K\).

If the first chosen coordinate is the inherited coordinate \(b\), the parent already lies on \(b=pt\). If the second is the inherited coordinate \(c\), it lies on \(c=qt\). Otherwise the only four pairings are:

1. \(x=pt\), \(a-x=qt\), whence \(a=(p+q)t\).
2. \(x=pt\), \(b+x=qt\), whence \(b=(q-p)t\); positivity of \(b\) gives \(q>p\).
3. \(1-b-x=pt\), \(a-x=qt\). Since \(1-b=a+c\), subtracting the second equality from the first gives \(c=(p-q)t\); positivity gives \(p>q\).
4. \(1-b-x=pt\), \(b+x=qt\), whence \(1=(p+q)t\), contrary to the hypothesis.

Thus every predecessor lies in \(\mathcal H_{K'}\), where
\[
K'=K\cup\{p+q:p,q\in K\}\cup\{|p-q|:p,q\in K,\ p\ne q\}.
\]
This set is finite. The two other choices of cut vertex are cyclic permutations and give the same conclusion. Strict cut legality only restricts the projected sets, so it cannot create additional parents. Since \(W_{r+1}=W_r\cup\operatorname{Pre}(W_r)\), induction proves the claim. \(\square\)
