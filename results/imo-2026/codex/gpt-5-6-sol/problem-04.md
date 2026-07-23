[
  \boxed{\theta=\frac{180^\circ}{n}\quad\text{for some integer }n\ge 2.}
  ]

  Call an angle marked if its measure is a positive integer multiple of (\theta).

  ### 1. Any triangle with a marked angle is winning for Mulan

  Suppose the triangle has an angle (k\theta).

  If (k=1), Mulan has already won. If (k\ge2), she cuts from that vertex along a ray dividing the angle into
  [
  \theta\quad\text{and}\quad (k-1)\theta.
  ]
  One resulting triangle has an angle (\theta). The other has an angle ((k-1)\theta). Thus Shan-Yu must either
  retain a triangle containing (\theta), or retain one whose marked angle has a smaller multiplier.

  Induction on (k) shows that every triangle containing a marked angle is winning for Mulan.

  ### 2. Sufficiency

  Assume
  [
  \theta=\frac{180^\circ}{n},\qquad n\ge2.
  ]

  Consider a nonterminal triangle with angles (A,B,C). If one of them is marked, the preceding argument applies.
  We may therefore assume none is marked.

  First suppose (n\ge3). Choose (A) to be a largest angle, so
  [
  A\ge60^\circ\ge\theta.
  ]
  Choose the integer (q) such that
  [
  B<q\theta<B+\theta.
  ]
  This is possible because (B) is not a multiple of (\theta). Since (A\ge\theta),
  [
  B<q\theta<B+\theta\le B+A=180^\circ-C.
  ]
  Set
  [
  x=q\theta-B,
  ]
  so (0<x<A). Mulan chooses (P) on the side opposite (A) so that the cut divides (A) into (x) and (A-x).

  The two resulting triangles have angle triples
  [
  (B,x,180^\circ-B-x)
  ]
  and
  [
  (C,A-x,B+x).
  ]
  By the definition of (x),
  [
  B+x=q\theta,
  ]
  while
  [
  180^\circ-B-x=180^\circ-q\theta=(n-q)\theta.
  ]
  Thus each resulting triangle contains a marked angle. Whichever one Shan-Yu retains, Mulan can win by Step 1.

  It remains to handle (n=2), so (\theta=90^\circ). Since the triangle has no marked angle, none of its angles is
  (90^\circ). Choose (A) so that the other two angles (B,C) are both less than (90^\circ): if the triangle is
  obtuse, take (A) to be its obtuse angle; otherwise any choice works. Set
  [
  x=90^\circ-B.
  ]
  Because (B,C<90^\circ),
  [
  0<x<A.
  ]
  After making the corresponding cut, the two new angles at (P) are both (90^\circ). Hence Mulan wins regardless
  of Shan-Yu’s choice.

  Therefore every (\theta=180^\circ/n), (n\ge2), works.

  ### 3. Necessity

  Now suppose (180^\circ) is not an integer multiple of (\theta). Shan-Yu initially chooses an equilateral
  triangle.

  Its (60^\circ) angles are not marked: if (60^\circ=k\theta), then
  [
  180^\circ=3k\theta,
  ]
  contrary to the assumption. Shan-Yu will maintain the invariant that the retained triangle has no marked angle.

  Let the current unmarked triangle have angles (A,B,C). Suppose Mulan cuts from the vertex of angle (A),
  dividing it into (x) and (A-x). The resulting triangles have angles
  [
  T_1=(B,x,180^\circ-B-x)
  ]
  and
  [
  T_2=(C,A-x,B+x).
  ]

  We claim that at least one of (T_1,T_2) is unmarked. Suppose instead that both are marked. Since (B) and (C)
  are unmarked, the marked angle in (T_1) must be either
  [
  x\quad\text{or}\quad 180^\circ-B-x,
  ]
  and the marked angle in (T_2) must be either
  [
  A-x\quad\text{or}\quad B+x.
  ]
  There are four possibilities:

  - If (x) and (A-x) are marked, then their sum (A) is marked.
  - If (x) and (B+x) are marked, then their difference (B) is marked.
  - If (180^\circ-B-x) and (A-x) are marked, then their difference
    [
    180^\circ-B-x-(A-x)=C
    ]
    is marked.

  - If (180^\circ-B-x) and (B+x) are marked, then their sum (180^\circ) is an integer multiple of (\theta).

  Every case is a contradiction. Hence one resulting triangle is unmarked, and Shan-Yu retains that one.

  He can repeat this forever. Since an angle equal to (\theta) is marked, the retained triangle never contains
  such an angle. Thus Mulan cannot guarantee victory unless (180^\circ) is an integer multiple of (\theta).

  Combining both directions gives precisely
  [
  \boxed{\theta\in\left{\frac{180^\circ}{2},\frac{180^\circ}{3},\frac{180^\circ}{4},\ldots\right}.}
  ]
─ Worked for 7m 20s ─────────────────────────────────────────────────────────────────────────────────────────────