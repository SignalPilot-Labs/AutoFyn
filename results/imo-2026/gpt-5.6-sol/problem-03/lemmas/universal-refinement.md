# Universal refinement lemma

## Statement
Let \(V\le n+1\) positive parent masses have total \(S\). At most \(n\) legal positive binary cuts can produce sorted alternating discrepancy at most \(S/(2^{n+1}-1)\). If \(V\le n\), discrepancy \(0\) is attainable.

## Certified proof
For \(V=n+1\), consider all \(2^V\) subset sums in \([0,S]\). Two equal sums give difference zero; otherwise two consecutive sorted subset sums differ by some \(d\le S/(2^V-1)\). Canceling their common indices gives disjoint sets \(A,B\), not both empty, with \(\sum_Aa_i-\sum_Ba_i=d\ge0\); let \(C\) contain the remaining parents.

If \(B\ne\varnothing\), greedily transport equal positive amounts between parents in \(A\) and \(B\), exhausting the smaller current remainder at each step. Let \(e\) be the number of matched fragment pairs and \(r\) the number of positive residual remainders in \(A\). If \(d>0\), then \(r\ge1\) and \(e\le |A|+|B|-r\). Thus the \(2e+r\) fragments in these parents cost
\[
2e+r-(|A|+|B|)\le |A|+|B|-r
\]
cuts. Bisecting each \(C\)-parent costs \(|C|\) more, for at most \(V-r\le V-1=n\) cuts. Deleting designated equal pairs leaves residual total mass \(d\), so the discrepancy is at most \(d\le S/(2^V-1)\). If \(d=0\), the last transport step exhausts two remainders, whence \(e\le |A|+|B|-1\); after bisecting \(C\), fewer than \(n\) cuts produce only equal pairs and discrepancy zero.

If \(B=\varnothing\), the nonempty set \(A\) has total mass \(d\). Bisect every parent except one parent in \(A\). This costs \(V-1=n\) cuts; deleting equal pairs leaves one mass at most \(d\), proving the same bound.

For \(V\le n\), use the same construction. In the transport case with \(d>0\), additionally bisect each of the \(r\) residual fragments; the total cut count is at most \((V-r)+r=V\le n\), and all fragments are paired equally. The \(d=0\) case already has discrepancy zero. In the empty-\(B\) case, bisect every parent, using \(V\le n\) cuts. Every prescribed subdivision into positive fragment lengths is implemented within its parent by marks at successive partial sums, so all cuts are legal and distinct. ∎
