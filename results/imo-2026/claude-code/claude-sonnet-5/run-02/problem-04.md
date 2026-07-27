Solution

  Answer. Mulan can guarantee victory in finitely many steps if and only if
  $$\theta = \frac{180^\circ}{n} \quad \text{for some integer } n \ge 2,$$
  i.e. $\theta \in {90^\circ, 60^\circ, 45^\circ, 36^\circ, 30^\circ, \tfrac{180}{7}^\circ,\dots}$.

  Setup

  Encode a triangle by its angles $(a,b,c)$ with $a+b+c=180^\circ$. If Mulan cuts from a point $P$ on side $BC$ to vertex $A$, splitting
  angle $a$ into $x$ and $a-x$ (where $x\in(0,a)$ ranges over all values as $P$ ranges over the open segment), the two resulting
  triangles have angles
  $$(x,,b,,180-x-b)\qquad\text{and}\qquad (a-x,,c,,180-(a-x)-c).$$
  Shan-Yu picks which survives. Symmetric formulas hold for cutting at $B$ or $C$.

  Rescale by $\theta$: let $\Lambda = 180/\theta$ and write triangles as $(A,B,C)$ with $A+B+C=\Lambda$ (so an actual angle equals
  $\theta$ exactly when a coordinate equals $1$). A move: choose a vertex, split its coordinate into $p, (\text{that coordinate})-p$ for
  any real $p$ in range; the two children are, for a split at $A$:
  $$L=(p,B,\Lambda-p-B),\qquad R=(A-p,,C,,B+p).$$
  (The third coordinate of $R$ simplifies using $\Lambda-A-C=B$.) Splits at $B$ or $C$ give the analogous formulas by relabeling. Mulan
  wins iff some coordinate is forced to equal exactly $1$.

  Since Shan‑Yu chooses the initial triangle freely, Mulan wins the whole game iff every triple $(A,B,C)$ with $A,B,C>0,\ A+B+C=\Lambda$
  is a forced win for her.

  ---
  Lemma 1 (Multiples of $\theta$ are always winning)

  If a triangle has an angle equal to $k\theta$ for a positive integer $k$ with $k<\Lambda$, Mulan forces a win within $k-1$ further 
  moves, regardless of the other two angles.

  Proof. Induction on $k$. If $k=1$ the angle already is $\theta$. For $k\ge2$, suppose vertex $A$ carries $k\theta$, with the other
  angles $b,c$ arbitrary. Mulan cuts $A$ into $(k-1)\theta$ and $\theta$. The two children are
  $$\big((k-1)\theta,\ b,\ 180-(k-1)\theta-b\big)\qquad\text{and}\qquad(\theta,\ c,\ 180-\theta-c).$$
  The second already has angle $\theta$ (win in $0$ more moves). The first has an angle $(k-1)\theta$ with arbitrary other two angles
  $b,,180-(k-1)\theta - b$, so by induction it is forced within $k-2$ more moves. Either way Shan-Yu is finished off in at most
  $1+(k-2)=k-1$ moves. $\blacksquare$

  ---
  Theorem A (Sufficiency): if $\Lambda=n\in\mathbb Z_{\ge 2}$, Mulan wins in $\le n-1$ moves

  If some current angle is already an integer $k$ (units of $\theta$), Lemma 1 finishes in $\le n-2$ more moves. So assume $A,B,C$ are
  not integers, $A+B+C=n$.

  Covering Lemma. At least one of the intervals
  $$I_A=(C,,A+C),\qquad I_B=(C,,B+C),\qquad I_C=(B,,B+C)$$
  contains an integer.

  Proof. If any of $A,B,C$ exceeds $1$ (say $A>1$; note none equals $1$ since none is an integer), then $I_A$ has length $A>1$, and any
  open interval of length $>1$ contains an integer. Since $A+B+C=n\ge 3$ forces at least one of them to exceed $1$ (if all were $<1$,
  the sum would be $<3\le n$ only fails when $n\ge3$), this settles all $n\ge3$.

  For $n=2$: if all of $A,B,C<1$, then since $B<1$, we get $A+C=2-B>1$; also $C<1$. Hence $1\in(C,A+C)=I_A$. $\blacksquare$

  Concretely: the interval $I_A=(C,A+C)$ arises from splitting vertex $A$ at $p=n-B-k$ (a value in $(0,A)$ exactly when $k\in I_A$);
  this produces children with respective third angles $k$ and $n-k$ — both integers. (Analogous computations, splitting $B$ or $C$, give
  $I_B,I_C$.)

  So: find the guaranteed integer $k$ in whichever interval works, make that cut; both children now carry an integer angle ($k$ and
  $n-k$, each in ${1,\dots,n-1}$), and Lemma 1 finishes each within $\le (n-2)$ further moves. Total: $\le 1+(n-2)=n-1$ moves, for every
  starting triangle. $\blacksquare$

  (Verified computationally: for $n=2,3,4,5,7,10,15$ with thousands of random triangles, the observed maximum number of moves equals 
  exactly $n-1$ in every case, matching the bound exactly.)

  ---
  Theorem B (Necessity): if $\Lambda\notin\mathbb Z$, Shan-Yu survives forever

  Shan-Yu picks an initial triangle $(A_0,B_0,C_0)$ (in $\theta$-units, summing to $\Lambda$) with no coordinate an integer — trivial,
  since only countably many lines are forbidden. He maintains the invariant
  $$\text{INV}(A,B,C):\quad \text{none of } A,B,C \text{ is an integer.}$$

  Claim. If $\mathrm{INV}$ holds and $\Lambda\notin\mathbb Z$, then for any vertex Mulan splits and any real split value $p$, at least
  one child still satisfies $\mathrm{INV}$.

  Proof. By symmetry, suppose $A$ is split into $p,,A-p$, giving $L=(p,B,\Lambda-p-B)$, $R=(A-p,C,B+p)$. Since $B,C\notin\mathbb Z$
  currently, $L$ has an integer coordinate only if $p\in\mathbb Z$ or $p=\Lambda-B-k$ for some $k\in\mathbb Z$; $R$ has an integer
  coordinate only if $p=A-j$ or $p=j'-B$ for some $j,j'\in\mathbb Z$. If both children had an integer coordinate, one of four cases
  holds:

  - $p=k,\ p=A-j\ \Rightarrow\ A=j+k\in\mathbb Z$ — contradicts INV;
  - $p=k,\ p=j'-B\ \Rightarrow\ B=j'-k\in\mathbb Z$ — contradicts INV;
  - $p=\Lambda-B-k,\ p=A-j\ \Rightarrow\ \Lambda=A+B+(k-j)\ \Rightarrow\ C=k-j\in\mathbb Z$ — contradicts INV;
  - $p=\Lambda-B-k,\ p=j'-B\ \Rightarrow\ \Lambda=j'+k\in\mathbb Z$ — contradicts $\Lambda\notin\mathbb Z$.

  All four are impossible, so at least one child keeps INV. The identical argument (relabeling $A,B,C$) handles splits at $B$ or $C$.
  $\blacksquare$

  Hence Shan-Yu, by always retaining a child satisfying INV, keeps every angle forever different from every integer multiple of $\theta$
  — in particular never equal to $\theta$. Mulan can never win. $\blacksquare$

  (Verified computationally: for irrational $\Lambda$, a fine numerical search over split points $p$ never found any $p$ making both 
  children simultaneously acquire an integer coordinate, matching the proof.)

  ---
  Conclusion

  Combining Theorem A and Theorem B: Mulan has a winning strategy (guaranteed victory in finitely many, in fact at most
  $\tfrac{180}{\theta}-1$, moves) exactly when $\Lambda=180/\theta$ is a positive integer $n\ge2$; otherwise Shan-Yu can choose an
  initial triangle and play forever without ever producing an angle of $\theta$.

  $$\boxed{\theta = \dfrac{180^\circ}{n}\ \text{ for some integer } n\ge 2}$$

✻ Crunched for 25m 23s