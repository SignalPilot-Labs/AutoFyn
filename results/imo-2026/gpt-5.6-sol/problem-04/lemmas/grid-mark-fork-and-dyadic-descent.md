# Grid-mark fork and dyadic descent

Normalize triangle angles to sum to \(1\), and let \(t=1/n\) for an integer \(n\ge2\). Then from every triangle Mulan can force an angle equal to \(t\) in finitely many cuts. More precisely, a triangle containing an angle \(kt\) is won in at most \(\lceil\log_2k\rceil\) further cuts, and a triangle containing no positive integral multiple of \(t\) is won in at most \(1+\lceil\log_2(n-1)\rceil\) cuts.

## Proof

If a current angle is \(kt\), split it into
\[
\lfloor k/2\rfloor t+\lceil k/2\rceil t.
\]
For \(k\ge2\), both parts are positive and smaller than \(kt\), hence this is legal, and either retained child contains one of these parts. Strong induction on \(k\) proves the bound \(\lceil\log_2k\rceil\): if \(d=\lceil\log_2k\rceil\), then \(\lceil k/2\rceil\le2^{d-1}\).

Now represent the three normalized angles as consecutive interval lengths partitioning \([0,1]\), and mark \(0,t,2t,\ldots,nt=1\). If an interior mark is a partition boundary, one of the three angles is already a positive integral multiple of \(t\): at the first boundary this is immediate, and at the second boundary the remaining interval has length \(1-jt=(n-j)t\). Otherwise every interior mark lies strictly inside an angle interval. Cyclically denote one such interval by \((b,b+a)\), and let the mark be \(kt\), \(1\le k\le n-1\). Cut from the vertex of angle \(a\), splitting it with
\[
x=kt-b,
\]
which is legal because \(b<kt<b+a\). The two retained children have angle triples
\[
(x,b,1-b-x),\qquad(a-x,c,b+x).
\]
The first contains \(1-b-x=1-kt=(n-k)t\), and the second contains \(b+x=kt\). Thus either response supplies a positive multiple with coefficient at most \(n-1\), after which the preceding dyadic descent applies. \(\square\)
