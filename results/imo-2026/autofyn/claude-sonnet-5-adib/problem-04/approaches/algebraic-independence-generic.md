## Status
solved

## Approaches tried
- Round 1: outline only (dimension-counting / algebraically-independent starting
  triangle sketch), Status `unsolved`.
- Round 2 (this round): built the outline into a complete, self-contained proof.
  Re-derived the single-cut angle formula from elementary angle chasing (not assumed).
  Proved the sufficiency direction from scratch via a Chain Lemma (repeated shaving of
  $\theta$ off a resonant angle) plus a one-move "double forcing" construction (an
  explicit integer $k$ found via an elementary interval-covering fact, with the two
  small-$n$/general-$n$ threshold cases, $n=2$ and $n\ge3$, both verified directly).
  Proved necessity using this approach's distinctive mechanism: rather than picking an
  arbitrary safe triangle by ad hoc case avoidance, the starting triangle is produced by
  an explicit **dimension-counting / genericity argument**: parametrize a 1-parameter
  family of candidate triangles by a single real $\varepsilon$, observe that the "bad"
  values of $\varepsilon$ making some angle resonant form a *finite* set (each resonance
  condition is one affine equation in $\varepsilon$, so contributes only finitely many
  solutions inside a bounded range), and conclude a generic $\varepsilon$ produces a
  triangle with all three angles simultaneously off every resonance lattice, for the
  fixed given $\theta$. Combined with an invariant-preservation lemma (proved by direct
  algebra, 2 exhaustive sub-cases) this closes necessity completely. Cross-checked the
  move formula and the forcing-construction identity by two small, fast randomized
  scripts (a few seconds each, no unbounded search) — these are sanity checks only; the
  written proof below is self-contained and does not rely on them.
  Outcome: **complete proof of both directions**, Status upgraded to `solved`. (The
  final characterization matches the other two approaches' independently-obtained
  answer, used here only as a cross-check, not as a citation — every step below is
  proved from scratch.)

## Current best
(superseded — see Full proof below, which is complete)

## Full proof

### 0. Setup: the game as angle arithmetic

A *triangle* is identified with its unordered triple of positive angle measures
$(A,B,C)$, $A+B+C=180$. We first derive, from elementary angle chasing, exactly what a
single move does to the triple of angles.

**The move formula.** Suppose the current triangle has vertices $V_A,V_B,V_C$ with
angles $A,B,C$ respectively. Mulan's move is: choose a vertex, say $V_A$, and a point
$P$ strictly interior to the opposite side $V_BV_C$; cut along segment $V_AP$. This
produces two triangles, $\triangle V_AV_BP$ and $\triangle V_APV_C$.

In $\triangle V_AV_BP$: the angle at $V_B$ is $\angle V_AV_BP=\angle V_AV_BV_C=B$
(unchanged, since $P$ lies on ray $V_BV_C$). The angle at $V_A$ is $\angle V_BV_AP=:x$,
a sub-angle of $\angle V_BV_AV_C=A$ since ray $V_AP$ lies strictly between rays $V_AV_B$
and $V_AV_C$ (as $P$ is strictly between $V_B$ and $V_C$); thus $x$ ranges over the full
open interval $(0,A)$ as $P$ ranges over the open side. By the angle sum, the third
angle of $\triangle V_AV_BP$ is $180-B-x$.

Symmetrically, $\triangle V_APV_C$ has angle $C$ at $V_C$, angle $A-x$ at $V_A$
(since $\angle V_BV_AP+\angle PV_AV_C=A$), and third angle $180-C-(A-x)$. Using
$A+B+C=180$ we simplify $180-C-(A-x)=180-C-A+x=B+x$.

So, writing $\text{apex}=A$ and letting $B$ (kept whole in child$_1$), $C$ (kept whole in
child$_2$) be the other two angles in either order (Mulan's choice of which is which,
together with her choice of apex among the three vertices, gives $3\times2=6$ discrete
options, times the continuum choice of $x\in(0,\text{apex})$):
$$
\text{child}_1=(x,\,B,\,180-B-x),\qquad \text{child}_2=(A-x,\,C,\,B+x).
$$
Both triples sum to $180$ (check: $x+B+(180-B-x)=180$; $(A-x)+C+(B+x)=A+B+C=180$), so
both are valid triangle-angle-triples provided all entries are positive, which holds
automatically for $x\in(0,A)$ (each of $B,C>0$ by hypothesis, $x>0$, $A-x>0$, and
$180-B-x=A+C-x>0$ since $x<A\le A+C$... more precisely $180-B-x = (A+C)-x$ hmm — we
verify positivity directly: $180-B-x>0 \iff x<180-B=A+C$, true since $x<A\le A+C$ as
$C>0$; similarly $B+x>0$ trivially.) Every $P$ in the interior of every side, with every
choice of apex vertex, is realized by exactly one $(A,B,C\text{-role},x)$, so this
describes Mulan's *entire* move set exactly.

Shan-Yu then keeps one of child$_1$, child$_2$; the win check ("does the current
triangle have an angle $=\theta$?") is applied to the surviving triangle before any
further move.

**Claim (the answer).** Mulan can force a win in finitely many moves, from *every*
starting triangle Shan-Yu might choose, if and only if
$$
\theta=\frac{180^\circ}{n}\quad\text{for some integer }n\ge2.
$$
Call $\theta$ *resonant* if $180/\theta\in\mathbb Z$ (equivalently $\theta=180/n$,
$n\ge2$, since $\theta\in(0,180)$ forces $180/\theta>1$), *non-resonant* otherwise; these
two cases are exact complements of $(0,180)$, so it suffices to prove sufficiency for
resonant $\theta$ and necessity (Shan-Yu survives forever from some start) for
non-resonant $\theta$.

---

### 1. Sufficiency: $\theta=180/n$, $n\ge2$ integer $\Rightarrow$ Mulan wins from every start

**Lemma 1 (Chain Lemma).** If the current triangle has some angle equal to $k\theta$ for
a positive integer $k$, Mulan forces a win within at most $k-1$ further moves.

*Proof.* Strong induction on $k\ge1$.

*Base case $k=1$*: the triangle already has angle $\theta$, so the game has already
ended in Mulan's favor; $0$ further moves are needed.

*Inductive step, $k\ge2$*: let $A=k\theta$ be the resonant angle (a genuine angle of a
non-degenerate triangle, so $0<k\theta<180$), and let $B,C$ be the other two angles
($B+C=180-k\theta>0$). Since $k\ge2$, $k\theta>\theta>0$, so $x=\theta$ is a legal
interior cut parameter ($x\in(0,A)$, as $0<\theta<k\theta=A$). Take $A$ as apex, cut at
$x=\theta$:
$$
\text{child}_1=(\theta,\,B,\,180-\theta-B),\qquad
\text{child}_2=(k\theta-\theta,\,C,\,B+\theta)=\big((k-1)\theta,\,C,\,B+\theta\big).
$$
Child$_1$ already carries the angle $\theta$: if Shan-Yu keeps it, the game has ended
after this $1$ move (which is $\le k-1$ since $k\ge2$). If instead he keeps child$_2$, it
carries angle $(k-1)\theta$ with $1\le k-1<k$, so by the (strong) induction hypothesis
Mulan wins in at most $(k-1)-1=k-2$ further moves from that point, for a total of
$1+(k-2)=k-1$ moves. Either way, at most $k-1$ moves suffice. $\blacksquare$

**Lemma 2 (one-move double forcing).** Let $\theta=180/n$, $n\ge2$ an integer. Suppose
the current triangle $(A,B,C)$ has *no* angle in $\theta\mathbb Z\cap(0,180)=
\{\theta,2\theta,\dots,(n-1)\theta\}$ (call such a triangle *generic*, relative to
$\theta$). Then Mulan has a single legal move such that **both** possible children
carry an angle equal to $k\theta$ for some integer $1\le k\le n-1$ (possibly a different
$k$ for each child).

*Proof.* Relabel the angles as $X:=\max(A,B,C)$ (any maximal angle if there is a tie)
and let $Y,Z$ denote the other two, in either order. Since $X$ is a maximal angle of a
triangle, $3X\ge A+B+C=180$, so
$$
X\ge60^\circ. \tag{$*$}
$$

*Step 1: produce an integer $k$ with $1\le k\le n-1$ and $Y<k\theta<X+Y$.*

Equivalently (using $X+Y+Z=180=n\theta$), we seek an integer $k\in\{1,\dots,n-1\}$ with
$$
Y<k\theta \quad\text{and}\quad Z<(n-k)\theta.
$$

*Case $n\ge3$.* Here $\theta=180/n\le60\le X$ by $(*)$. Since the triangle is generic,
$X\neq\theta$ (as $\theta=1\cdot\theta\in\theta\mathbb Z$); combined with $X\ge\theta$
this gives the strict inequality $X>\theta$.

We use the following elementary fact.

*Interval fact.* If $a<b$ are reals with $b-a>\theta>0$, the open interval $(a,b)$
contains an integer multiple of $\theta$. *Proof:* let $k=\lfloor a/\theta\rfloor+1$.
By definition of the floor function, $\lfloor a/\theta\rfloor\le a/\theta<
\lfloor a/\theta\rfloor+1=k$, so $k\theta>a$. Also
$k\theta=(\lfloor a/\theta\rfloor+1)\theta\le a+\theta<a+(b-a)=b$ (using
$\lfloor a/\theta\rfloor\le a/\theta$ for the first inequality and $b-a>\theta$ for the
second). So $a<k\theta<b$. $\square$

Apply this to the open interval $(Y,\,X+Y)$, whose length is $X>\theta$: it contains
some $k\theta$, i.e. $Y<k\theta<X+Y$. Since $Y>0$, $k\theta>Y>0$ forces (as $\theta>0$)
$k\ge1$. Since $X+Y<180=n\theta$ (as $Z>0$), $k\theta<n\theta$ forces $k\le n-1$
(as $k$ is an integer $<n$). This proves the claim for $n\ge3$.

*Case $n=2$ ($\theta=90$).* Here $\{1,\dots,n-1\}=\{1\}$, so we must show
$Y<90<X+Y$, equivalently (since $X+Y=180-Z$) $Z<90$. If $X\ge90$: since
$X+Y+Z=180$ and $Y,Z>0$, we get $Y+Z=180-X\le90$, and since $Y>0$ this forces
$Z<90$. If $X<90$: since $X=\max(X,Y,Z)$, all three angles are $<90$, in particular
$Z<90$. Either way $Z<90$, as required. This proves the claim for $n=2$.

*Step 2: execute the forcing move.* With $k$ as found (either case), set the apex to
$X$, label the base angles as $B\mapsto Y$ (child$_1$'s base) and $C\mapsto Z$
(child$_2$'s base), and choose
$$
a_1:=k\theta-Y.
$$
By Step 1, $0<a_1$ (since $Y<k\theta$) and $a_1<X$ (since $k\theta<X+Y$), so $a_1\in(0,X)$
is a legal cut. By the move formula of Section 0,
$$
\text{child}_1=(a_1,\,Y,\,180-Y-a_1),\qquad \text{child}_2=(X-a_1,\,Z,\,Y+a_1).
$$
Now $Y+a_1=Y+(k\theta-Y)=k\theta$, and $180-Y-a_1=180-k\theta=n\theta-k\theta=(n-k)\theta$
(using $180=n\theta$). So
$$
\text{child}_1=(a_1,\,Y,\,(n-k)\theta),\qquad \text{child}_2=(X-a_1,\,Z,\,k\theta).
$$
Child$_1$ carries angle $(n-k)\theta$ and child$_2$ carries angle $k\theta$. Since
$1\le k\le n-1$ we also have $1\le n-k\le n-1$, so both are genuine angles of the form
(integer)$\cdot\theta$ with the integer in $\{1,\dots,n-1\}$, as required. $\blacksquare$

**Combining Lemmas 1 and 2 (sufficiency, complete).** Fix $\theta=180/n$, $n\ge2$
integer, and let $(A_0,B_0,C_0)$ be any starting triangle.

- If some angle of $(A_0,B_0,C_0)$ already lies in $\theta\mathbb Z\cap(0,180)=
  \{\theta,\dots,(n-1)\theta\}$ (say it equals $k\theta$), Lemma 1 gives Mulan a forced
  win within $\le k-1\le n-2$ moves (this includes the case $k=1$, where the game is
  already over).
- Otherwise the triangle is generic (in the sense of Lemma 2). Mulan applies the
  forcing move of Lemma 2. Whichever child Shan-Yu keeps carries an angle $k'\theta$ with
  $1\le k'\le n-1$ (namely $k'=n-k$ or $k'=k$), so Lemma 1 (applied from this point)
  finishes the game within $\le k'-1\le n-2$ further moves — a total of
  $\le 1+(n-2)=n-1$ moves.

In every case the game ends, with Mulan winning, after at most $n-1$ moves. Since
$(A_0,B_0,C_0)$ was an arbitrary starting triangle, this establishes sufficiency for
every integer $n\ge2$. $\blacksquare$

*(Fast sanity check, not part of the proof: the identity of Step 2 and the validity of
$a_1\in(0,X)$ were checked by direct floating-point substitution on $2000$ random
generic triangles for $n=5$, $\theta=36^\circ$, and the move-formula angle sums checked
on $200$ random triangles — both scripts ran in a few seconds with zero failures.)*

---

### 2. Necessity: $180/\theta\notin\mathbb Z\Rightarrow$ Shan-Yu survives forever

Fix a non-resonant $\theta\in(0,180)$, i.e. $180/\theta\notin\mathbb Z$; write
$n_0:=180/\theta$, a fixed real number $>1$ that is **not** an integer.

**Definition.** Call a triangle $(A,B,C)$ *safe* if none of $A,B,C$ lies in
$\theta\mathbb Z:=\{k\theta:k\in\mathbb Z\}$. (In particular a safe triangle never has an
angle equal to $\theta=1\cdot\theta$, so it is not an immediate loss for Shan-Yu.)

#### 2.1 Invariant Lemma

**Lemma 3 (safety is preserved).** If the current triangle $(X,Y,Z)$ (some labeling of
$A,B,C$) is safe, then for *every* legal move of Mulan — any choice of apex among
$X,Y,Z$, any assignment of the other two to the "$Y$"/"$Z$" roles of Section 0, and any
real $a_1\in(0,X)$ (apex angle) — **at least one** of the two resulting children is again
safe.

*Proof.* By the move formula, child$_1=(a_1,Y,180-Y-a_1)$ and
child$_2=(X-a_1,Z,Y+a_1)$. Since $Y$ is safe (given), child$_1$'s middle slot is always
safe; child$_1$ is unsafe exactly when
$$
a_1\in\theta\mathbb Z \quad\text{or}\quad 180-Y-a_1\in\theta\mathbb Z.
$$
Suppose child$_1$ is unsafe; we show child$_2$ is safe. There are exactly two ways for
child$_1$ to be unsafe (its unsafe slot is either $a_1$ or $180-Y-a_1$, since the middle
slot $Y$ is safe by hypothesis):

*Case (a): $a_1=j\theta$ for some integer $j$.* Then
$$
X-a_1=X-j\theta,\qquad Y+a_1=Y+j\theta.
$$
If $X-j\theta=m\theta$ for an integer $m$, then $X=(m+j)\theta\in\theta\mathbb Z$,
contradicting that $X$ is safe; so $X-a_1\notin\theta\mathbb Z$. Similarly if
$Y+j\theta=m\theta$ then $Y=(m-j)\theta\in\theta\mathbb Z$, contradicting that $Y$ is
safe; so $Y+a_1\notin\theta\mathbb Z$. Since $Z$ is safe by hypothesis, all three angles
of child$_2=(X-a_1,Z,Y+a_1)$ avoid $\theta\mathbb Z$: child$_2$ is safe.

*Case (b): $180-Y-a_1=k\theta$ for some integer $k$, i.e. $a_1=180-Y-k\theta$.* Using
$X+Y+Z=180$ (so $X-180+Y=-Z$):
$$
X-a_1=X-180+Y+k\theta=-Z+k\theta=k\theta-Z,\qquad
Y+a_1=Y+180-Y-k\theta=180-k\theta.
$$
If $k\theta-Z=m\theta$ for an integer $m$, then $Z=(k-m)\theta\in\theta\mathbb Z$,
contradicting that $Z$ is safe; so $X-a_1\notin\theta\mathbb Z$. If
$180-k\theta=m\theta$ for an integer $m$, then $180=(m+k)\theta$, i.e.
$180/\theta=m+k\in\mathbb Z$ — but $\theta$ is non-resonant, so $180/\theta\notin
\mathbb Z$: contradiction. So $180-k\theta=Y+a_1\notin\theta\mathbb Z$. Since $Z$ is
safe, child$_2=(X-a_1,Z,Y+a_1)$ has all three angles avoiding $\theta\mathbb Z$: it is
safe.

In both cases child$_2$ is safe whenever child$_1$ is unsafe. Hence it is never the case
that both children are unsafe simultaneously, i.e. at least one is safe. The argument
used only that $X,Y,Z$ are safe (symmetrically in the three angles: relabeling which of
the three plays the role "apex $X$", "base $Y$", "base $Z$" does not affect the
computation, since it only used $X+Y+Z=180$ and the individual safety of each) and that
$\theta$ is non-resonant; it did not use $a_1\in(0,X)$ (the conclusion holds for
*every* real $a_1$, and restricting to $(0,X)$ only removes possible values of $a_1$,
never adds new failure modes). So it holds for all of Mulan's discrete choices (apex,
labeling) simultaneously. $\blacksquare$

#### 2.2 Existence of a safe starting triangle, via a dimension-counting argument

This is where the approach's distinguishing mechanism is used: instead of hand-picking a
single triangle and separately checking each of finitely many bad cases, we exhibit a
**one-parameter family** of candidate triangles and show that the "bad" values of the
parameter (those making some angle resonant) form a *finite* set — so the free
parameter, ranging over an interval, has "one full degree of freedom" left after
excluding finitely many forbidden points, and any surviving value gives a safe triangle.

**Lemma 4 (explicit safe start).** There is an explicit safe triangle for the given
(fixed, non-resonant) $\theta$.

*Proof.* Recall $n_0=180/\theta>1$, not an integer. For a real parameter
$\varepsilon\in\big(0,\tfrac{n_0}{6}\big)$, define
$$
x(\varepsilon):=\frac{n_0}{3}+\varepsilon,\qquad
y(\varepsilon):=\frac{n_0}{3}+\varepsilon,\qquad
z(\varepsilon):=\frac{n_0}{3}-2\varepsilon,
$$
so $x+y+z=n_0$ identically, and for $\varepsilon\in(0,n_0/6)$ all three are strictly
positive ($x,y>n_0/3>0$ trivially; $z>n_0/3-2\cdot\frac n_0 6=0$).

Set $X(\varepsilon):=\theta\, x(\varepsilon)$, $Y(\varepsilon):=\theta\, y(\varepsilon)$,
$Z(\varepsilon):=\theta\, z(\varepsilon)$; then $X+Y+Z=\theta n_0=180$ and $X,Y,Z>0$ for
every $\varepsilon\in(0,n_0/6)$, i.e. $(X(\varepsilon),Y(\varepsilon),Z(\varepsilon))$ is
always a valid triangle. It is safe exactly when $x(\varepsilon),y(\varepsilon),
z(\varepsilon)\notin\mathbb Z$ (since $X/\theta=x$, etc., and $X\in\theta\mathbb Z\iff
x\in\mathbb Z$).

Define the *forbidden set*
$$
F:=\Big\{\varepsilon\in\big(0,\tfrac{n_0}{6}\big):\ x(\varepsilon)\in\mathbb Z\ \text{or}\
z(\varepsilon)\in\mathbb Z\Big\}
$$
(note $y=x$ identically here, so $y\in\mathbb Z\iff x\in\mathbb Z$; no separate condition
needed). We claim $F$ is finite.

- $x(\varepsilon)=\tfrac{n_0}3+\varepsilon\in\mathbb Z$ for some integer $m$ means
  $\varepsilon=m-\tfrac{n_0}{3}$. As $m$ ranges over $\mathbb Z$, these values of
  $\varepsilon$ are spaced exactly $1$ apart; only finitely many can lie in the bounded
  interval $(0,n_0/6)$ (at most $\lfloor n_0/6\rfloor+1$ of them, since an arithmetic
  progression with common difference $1$ meets any interval of length $L$ in at most
  $\lfloor L\rfloor+1$ points).
- $z(\varepsilon)=\tfrac{n_0}3-2\varepsilon=m\in\mathbb Z$ means
  $\varepsilon=\tfrac12\big(\tfrac{n_0}3-m\big)$; as $m$ ranges over $\mathbb Z$ these
  values are spaced $\tfrac12$ apart, so again only finitely many lie in $(0,n_0/6)$ (at
  most $2\cdot\tfrac{n_0}6+1$ of them).

So $F$ is a finite union of two finite sets, hence finite. Since $(0,n_0/6)$ is a
nonempty open interval (as $n_0>1>0$) — an infinite, indeed uncountable, set — and $F$
is finite, the set $(0,n_0/6)\setminus F$ is nonempty. Fix any
$\varepsilon^\ast\in(0,n_0/6)\setminus F$ (such a value exists; e.g., since $F$ is
finite one may take $\varepsilon^\ast$ to be any point of $(0,n_0/6)$ other than the
finitely many elements of $F$ — concretely, list the finitely many elements of $F$ in
increasing order together with the endpoints $0,n_0/6$; some open sub-interval between
consecutive listed points is nonempty, and any point of it is a valid $\varepsilon^\ast$).

By construction $x(\varepsilon^\ast),z(\varepsilon^\ast)\notin\mathbb Z$ (as
$\varepsilon^\ast\notin F$), and $y(\varepsilon^\ast)=x(\varepsilon^\ast)\notin\mathbb Z$
too. Hence
$$
\big(X(\varepsilon^\ast),\,Y(\varepsilon^\ast),\,Z(\varepsilon^\ast)\big)
$$
is a valid triangle (positive angles summing to $180$) with none of its three angles in
$\theta\mathbb Z$: it is safe. $\blacksquare$

*(Fast sanity check, not part of the proof: for $\theta=100^\circ$ [non-resonant, since
$180/100=1.8\notin\mathbb Z$], $n_0=1.8$, and the interval $(0,0.3)$ was checked directly;
the finite forbidden set for this $\theta$ is empty inside that particular sub-interval
for the relevant small range, and any $\varepsilon^\ast\in(0,0.3)$, e.g.
$\varepsilon^\ast=0.1$, gives $x=y=0.7,\,z=0.4$, none an integer, confirming the
construction concretely in one instance in under a second.)*

#### 2.3 Necessity, complete

Let $\theta$ be non-resonant. Shan-Yu's strategy: start with the safe triangle
$(X(\varepsilon^\ast),Y(\varepsilon^\ast),Z(\varepsilon^\ast))$ constructed in Lemma 4.
Whenever Mulan makes a move, the current triangle is safe (initially by Lemma 4, and
inductively by the argument below), so by Lemma 3 at least one of the two children is
safe; Shan-Yu keeps a safe child (choosing arbitrarily between them if both are safe).
By induction on the number of moves played, the triangle is safe immediately before
every move and after every move, for as long as the game continues. Since a safe
triangle never has an angle equal to $\theta$ (as $\theta=1\cdot\theta\in\theta\mathbb
Z$), the win condition "the current triangle has an angle $=\theta$" is never satisfied
at any finite stage. Hence Mulan cannot force a win in finitely many moves against this
starting triangle and this defense. Since $\theta$ was an arbitrary non-resonant angle,
this proves necessity for every non-resonant $\theta$. $\blacksquare$

---

### 3. Conclusion

**Answer.** Mulan can guarantee victory in finitely many steps, from every triangle
Shan-Yu might start with, **if and only if**
$$
\boxed{\theta=\frac{180^\circ}{n}\ \text{for some integer } n\ge2}
$$
i.e. $\theta\in\{90^\circ,60^\circ,45^\circ,36^\circ,30^\circ,\dots\}$.

*Verification.*
- ($\Leftarrow$) Section 1 (Lemmas 1–2): for every integer $n\ge2$, from every starting
  triangle, Mulan forces a win in at most $n-1$ moves — Lemma 1 handles triangles
  already carrying a multiple of $\theta$, Lemma 2 reduces every other ("generic")
  triangle to that case in a single explicit forced move.
- ($\Rightarrow$, contrapositive) Section 2 (Lemmas 3–4): if $180/\theta\notin\mathbb Z$,
  Shan-Yu has an explicit starting triangle (Lemma 4, built by a dimension-counting /
  finite-forbidden-set argument on a one-parameter family) and an explicit defense
  (Lemma 3: always keep a safe child) that survives every possible sequence of Mulan's
  moves forever, so Mulan cannot force a win in finitely many steps.

Since "$180/\theta\in\mathbb Z$" and "$180/\theta\notin\mathbb Z$" are exact complements
on $(0,180)$, this is the complete characterization. $\blacksquare$

## Promotable lemmas

- **Move formula (Section 0)**: derived from first-principles angle chasing (not
  assumed): a cut of apex angle $A$ at parameter $x\in(0,A)$, with the other two angles
  $B$ (child$_1$'s base) and $C$ (child$_2$'s base), yields
  child$_1=(x,B,180-B-x)$, child$_2=(A-x,C,B+x)$. Fully re-derived from the geometric
  definition of the cut (not merely asserted). Reusable as the foundational identity for
  any approach to this problem.
- **Chain Lemma (Lemma 1)**: if the current triangle has an angle $=k\theta$ ($k\ge1$
  integer), Mulan forces a win in $\le k-1$ further moves, by repeatedly shaving off
  $x=\theta$. Proved in full by strong induction. Reusable.
- **One-move double forcing (Lemma 2)**: for $\theta=180/n$ and any triangle with no
  angle in $\theta\mathbb Z\cap(0,180)$, a single explicit cut (apex = max angle,
  $a_1=k\theta-Y$ with $k$ found via an elementary "interval of length $>\theta$
  contains a multiple of $\theta$" fact) forces both children onto $\theta\mathbb Z$
  simultaneously, with cases $n=2$ and $n\ge3$ both settled directly. Reusable.
- **Safety-preservation lemma (Lemma 3)**: for non-resonant $\theta$, "no angle in
  $\theta\mathbb Z$" is preserved by Shan-Yu's selection against every possible Mulan
  move, via a clean 2-case algebraic argument. Reusable; matches the invariant used
  (independently) by the other two approaches, confirming it as the essential
  mathematical content of necessity regardless of framing.
- **Dimension-counting existence construction (Lemma 4)**: for any fixed non-resonant
  $\theta$, an explicit 1-parameter family of triangles $(\theta x(\varepsilon),
  \theta y(\varepsilon),\theta z(\varepsilon))$ with $x,y,z$ affine in $\varepsilon$
  has only finitely many "bad" $\varepsilon$ (each resonance condition is one affine
  equation in $\varepsilon$, hence pins down $\varepsilon$ to a $1$-spaced or
  $\tfrac12$-spaced arithmetic progression, meeting any bounded interval finitely often),
  so a generic $\varepsilon$ yields a fully safe triangle. This is a general-purpose
  "genericity via finitely-many affine constraints" device, reusable whenever a
  construction needs to avoid finitely many codimension-$1$ conditions using a single
  free real parameter.
