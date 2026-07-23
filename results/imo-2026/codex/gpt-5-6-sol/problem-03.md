[
  \boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
  ]

  We prove matching lower and upper bounds.

  ### 1. The claiming phase

  Suppose the final piece lengths, in nonincreasing order, are

  [
  x_1\ge x_2\ge\cdots\ge x_k.
  ]

  The value of the claiming game for Liu Bang is

  [
  P=x_1+x_3+x_5+\cdots.
  ]

  Indeed, by always taking a longest remaining piece, Liu’s (j)-th choice has length at least (x_{2j-1}).
  Conversely, if Xiang always takes a longest remaining piece, his (j)-th choice has length at least (x_{2j}), so
  Liu receives at most (P).

  Write

  [
  Q=x_2+x_4+\cdots,\qquad D=P-Q=2P-S,
  ]

  where (S=\sum x_i). Thus (D) is Liu’s advantage over Xiang.

  ### 2. A fixed initial partition

  Suppose Liu’s marks initially create (m) pieces of lengths

  [
  a_1,\ldots,a_m,\qquad \sum_{i=1}^m a_i=S,
  ]

  and Xiang may make at most (m-1) further cuts. Define

  [
  \delta(a_1,\ldots,a_m)

  \min_{\substack{\varepsilon_i\in{-1,0,1}\
  (\varepsilon_1,\ldots,\varepsilon_m)\ne(0,\ldots,0)}}
  \left|\sum_{i=1}^m\varepsilon_i a_i\right|.
  ]

  We claim that the value of the game after this initial partition is exactly

  [
  \frac{S+\delta}{2}.
  ]

  #### Liu’s lower bound

  Consider any refinement by at most (m-1) cuts. There are at most (2m-1) final pieces. Arrange them as
  (x_1\ge\cdots\ge x_k), and pair them as

  [
  (x_1,x_2),\ (x_3,x_4),\ldots.
  ]

  Construct a weighted multigraph whose (m) vertices represent the original pieces. For each pair ((x_{2j-
  1},x_{2j})), draw an edge between their original pieces, of weight (x_{2j}). If both came from the same
  original piece, this is a loop.

  Regard the excess (x_{2j-1}-x_{2j}) as residual mass at the vertex containing (x_{2j-1}). If (k) is odd, also
  regard (x_k) as residual mass. Let (R_i\ge0) be the total residual mass at vertex (i). Then

  [
  \sum_i R_i=P-Q=D.
  ]

  The graph has at most

  [
  \left\lfloor\frac{2m-1}{2}\right\rfloor=m-1
  ]

  edges. Consequently, at least one connected component is a tree: if every component contained a cycle, the
  total number of edges would be at least the total number (m) of vertices.

  Take such a tree component and bipartition its vertices as (C_+\cup C_-). At every vertex, its original length
  equals its residual mass plus all incident edge contributions. After taking the signed sum over the
  bipartition, every edge contribution cancels, giving

  [
  \sum_{i\in C_+}a_i-\sum_{i\in C_-}a_i

  \sum_{i\in C_+}R_i-\sum_{i\in C_-}R_i.
  ]

  The coefficient vector on the left is a nonzero vector in ({-1,0,1}^m). Hence

  [
  \delta
  \le
  \left|\sum_{i\in C_+}a_i-\sum_{i\in C_-}a_i\right|
  \le
  \sum_iR_i=D.
  ]

  Therefore

  [
  P=\frac{S+D}{2}\ge \frac{S+\delta}{2}.
  ]

  #### Xiang’s matching upper bound

  Choose (\varepsilon_i\in{-1,0,1}) attaining (\delta), and let

  [
  A={i:\varepsilon_i=1},\quad
  B={i:\varepsilon_i=-1},\quad
  C={i:\varepsilon_i=0}.
  ]

  Assume

  [
  U:=\sum_{i\in A}a_i\ge
  V:=\sum_{i\in B}a_i,
  ]

  so (U-V=\delta).

  Xiang bisects every piece indexed by (C), creating an equal pair from each, using (|C|) cuts.

  He then matches material from the (A)-pieces against material from the (B)-pieces. Take one currently unmatched
  piece from each side. Pair the shorter with an equal-length portion cut from the longer; this uses at most one
  new cut and exhausts at least one of the two current pieces. Thus all the (B)-material can be matched using at
  most

  [
  |A|+|B|-1
  ]

  cuts. Altogether, Xiang uses at most

  [
  |C|+|A|+|B|-1=m-1
  ]

  cuts. If one of (A,B) is empty, the same conclusion is immediate.

  This creates designated equal pairs covering total length

  [
  \sum_{i\in C}a_i+2V
  =S-(U-V)=S-\delta.
  ]

  During claiming, Xiang can secure one member of every designated pair: whenever Liu takes one member of an
  intact pair, Xiang takes its mate; otherwise he takes one member of any still-intact pair. Hence Xiang receives
  at least

  [
  \frac{S-\delta}{2},
  ]

  so Liu receives at most ((S+\delta)/2). The claim is proved.

  ### 3. Maximizing (\delta)

  Now take (m=n+1) and (S=1). For arbitrary positive (a_1,\ldots,a_m), consider their (2^m) subset sums. They lie
  between (0) and (1). After ordering them, two consecutive subset sums differ by at most

  [
  \frac1{2^m-1}.
  ]

  Subtracting the corresponding subsets and cancelling their intersection produces a nonzero coefficient vector
  in ({-1,0,1}^m). Therefore

  [
  \delta(a_1,\ldots,a_m)\le \frac1{2^m-1}.
  ]

  Equality is attainable by taking

  [
  (a_1,\ldots,a_m)

  \frac1{2^m-1}(1,2,4,\ldots,2^{m-1}).
  ]

  Indeed, any nonzero signed sum of distinct powers of (2) has absolute value at least (1): its largest power
  exceeds the sum of all smaller powers. Thus here

  [
  \delta=\frac1{2^m-1}.
  ]

  Consequently, with (m=n+1), Liu can obtain exactly

  [
  \frac12\left(1+\frac1{2^{n+1}-1}\right)

  \frac{2^n}{2^{n+1}-1}.
  ]

  Finally, if Liu uses fewer than (n) marks, he creates at most (n) pieces. Xiang can bisect every one of them,
  using at most (n) marks, and the resulting pieces form equal pairs. Xiang can then guarantee half of the stick,
  so Liu cannot improve on the value above by using fewer marks.

  Hence

  [
  \boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
  ]

─ Worked for 13m 54s ────────────────────────────────────────────────────────────────────────────────────────────

