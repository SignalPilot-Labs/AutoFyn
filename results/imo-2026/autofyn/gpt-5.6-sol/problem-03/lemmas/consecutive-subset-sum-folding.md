# Consecutive-subset-sum folding lemma

## Statement
For positive masses \(a_1,\ldots,a_m\) with total \(1\), there is a refinement using at most \(m-1\) cuts whose multiset consists of equal pairs and at most one residual piece of length \(r\), where
\[
0\le r\le \frac1{2^m-1}.
\]
When \(r=0\), the residual is absent and at most \(m-2\) cuts suffice.

## Proof
List all \(2^m\) subset sums with multiplicity in nondecreasing order,
\[
0=b_0\le b_1\le\cdots\le b_{2^m-1}=1.
\]
The adjacent gaps sum to \(1\), so some consecutive gap \(r=b_{j+1}-b_j\) is at most \(1/(2^m-1)\). Choose subsets representing its endpoints, cancel their common elements, and obtain disjoint sets \(P,N\) such that
\[
\sum_{i\in P}a_i-\sum_{i\in N}a_i=r.
\]
Put all unused indices in \(Z\).

If \(r>0\), every \(p\in P\) has \(a_p\ge r\): otherwise adjoining \(p\) to the lower endpoint subset would produce a subset sum strictly inside the consecutive gap. If additionally \(N=\varnothing\), this forces \(P\) to be a singleton, which itself is the residual.

Now suppose \(r>0\) and \(N\ne\varnothing\). Let \(A=\sum_{P}a_i\) and \(B=\sum_Na_i\), so \(A=B+r\). Concatenate the \(P\)-parents along \([0,A]\), placing any chosen \(p_*\in P\) last, and concatenate the \(N\)-parents along \([0,B]\). Because \(a_{p_*}\ge r\), all earlier \(P\)-parents end by coordinate \(B\). Take the common refinement of the two concatenations on \([0,B]\). Its cells occur in equal pairs, while \([B,A]\) lies in the last \(P\)-parent and is one residual of length \(r\).

Each internal boundary of either concatenation requires at most one cut on the opposite side, and truncation at \(B\) requires at most one further cut. Thus the supported parents use at most
\[
(|P|-1)+(|N|-1)+1=|P|+|N|-1
\]
cuts. If \(r=0\), both supports are nonempty and the same common-refinement construction has no truncation cut, hence uses at most \(|P|+|N|-2\) cuts and leaves no residual.

Finally halve each parent indexed by \(Z\), using one cut to create an equal pair. The total cut count is at most \(m-1\) when \(r>0\), and at most \(m-2\) when \(r=0\). Every abstract subdivision boundary lying inside a parent corresponds to a legal physical cut in that parent. ∎
