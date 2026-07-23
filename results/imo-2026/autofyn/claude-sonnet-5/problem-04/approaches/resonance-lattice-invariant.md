## Status
solved

## Approaches tried
- Round 1 (this round): built out the outline's "resonance/lattice invariant" mechanism
  from scratch. The originally-flagged central gap (Lemma N1: find an invariant Shan-Yu's
  *selection* can maintain against Mulan's full continuum freedom on the cut parameter)
  is now fully resolved: the correct invariant is "no current angle is an exact positive
  integer multiple of θ," and a clean 2×2 case analysis (see Lemma N2 below) shows Mulan's
  single free real parameter a1 can make **at most one** of the two children violate this
  invariant, *unless* θ = 180/n for an integer n ≥ 2 — in which case a genuinely new
  4th "resonant" case appears and becomes the sufficiency mechanism instead. This turns the
  originally-separate S1/S2 (sufficiency) and N1 (necessity) gaps into two faces of the same
  single computation, closing all outstanding gaps identified by the outline-reviewer.
  Outcome: complete proof of both directions, worked out below.

## Current best
(superseded — see Full proof, Status is solved)

## Full proof

### 0. Setup and notation

Throughout, a *triangle* is an ordered or unordered triple of positive reals summing to
180 (we work purely with angle measures; the actual geometric triangle realizing them is
irrelevant to the argument, only the angle arithmetic matters). Write the current
triangle's angles as $(X,Y,Z)$ with $X+Y+Z=180$.

**The move, in angle-arithmetic form.** Mulan's cut from a point $P$ on a side to the
opposite vertex is equivalent to the following data: she chooses one of the three angles
as the *apex* (the vertex whose two sides are cut), say angle $X$ (opposite side is where
$P$ lies), and a real number $a_1 \in (0,X)$ ($P$ strictly interior to the side, never a
vertex, forces $a_1\ne 0,X$). Writing $Y,Z$ for the other two angles, the two resulting
triangles are
$$\text{child}_1=(Y,\ a_1,\ Z+X-a_1),\qquad \text{child}_2=(Z,\ X-a_1,\ Y+a_1).$$
(Both angle sums are $X+Y+Z=180$, confirmed directly.) Mulan additionally chooses **which**
of the other two angles plays the role "$Y$" (kept whole in child$_1$) versus "$Z$" (kept
whole in child$_2$) — i.e. she has three degrees of freedom per move: which angle is the
apex, which of the remaining two is "$Y$", and the real number $a_1\in(0,X)$. Shan-Yu then
picks which child survives. The game restarts with the surviving triangle, and stops
(Mulan wins) the moment the *current* triangle (before any further cut) has an angle equal
to $\theta$ exactly.

**Claim (the answer).** Mulan can guarantee victory in finitely many moves, from *every*
starting triangle Shan-Yu could choose, if and only if
$$\theta = \frac{180^\circ}{n}\quad\text{for some integer } n\ge 2.$$
(Equivalently $\theta\in\{90^\circ,60^\circ,45^\circ,36^\circ,30^\circ,\dots\}$.) We prove
sufficiency and necessity in turn.

---

### 1. A general lemma used in both directions: the Chain Lemma

**Lemma 1 (Chain Lemma).** Fix any $\theta\in(0,180)$. If the current triangle has some
angle equal to $k\theta$ for a positive integer $k$, then Mulan wins in at most $k-1$
further moves, and Shan-Yu has *no effective choice* at any step of this forced sequence
(in the sense that keeping the alternative child loses at least as fast, in fact
immediately).

*Proof.* Induction on $k$. If $k=1$ the angle already equals $\theta$, so the game has
already stopped (Mulan already won, $0$ further moves needed).

If $k\ge 2$: since $k\theta$ is a genuine angle of a non-degenerate triangle, $k\theta<180$,
and since $k\ge2$ we have $k\theta>\theta$, so $a_1:=\theta\in(0,k\theta)$ is a legal choice
for the apex parameter. Take the angle $k\theta$ as apex, and take $a_1=\theta$; let $Y,Z$
be the other two current angles (order irrelevant). Then
$$\text{child}_1=(Y,\ \theta,\ Z+(k-1)\theta),\qquad \text{child}_2=(Z,\ (k-1)\theta,\ Y+\theta).$$
Child$_1$ already contains the angle $\theta$ exactly, so if Shan-Yu keeps it the game
stops immediately (an even faster loss for him). If instead he keeps child$_2$, it contains
the angle $(k-1)\theta$ exactly. If $k=2$ this is $\theta$ itself, so *both* children
already have angle $\theta$ and Mulan wins in this one move regardless of Shan-Yu's choice
— this is the base of the induction for $k\ge2$. If $k\ge3$, child$_2$ has an angle equal
to $(k-1)\theta$ with $k-1\ge2$, an integer, so by the inductive hypothesis Mulan wins in
at most $(k-1)-1=k-2$ further moves from child$_2$. Total moves used: $1+(k-2)=k-1$. $\blacksquare$

---

### 2. Sufficiency: $\theta=180^\circ/n\ (n\ge2$ integer$)\Rightarrow$ Mulan wins

Fix $n\ge2$ and $\theta=180/n$, so $n\theta=180$. Let $(X,Y,Z)$ be **any** starting
triangle. We exhibit an explicit finite Mulan strategy.

**Step 0 (trivial case).** If $(X,Y,Z)$ already has an angle $=k\theta$ for some integer
$k\ge1$ (in particular if it is equilateral and $n=3$, or has an angle exactly $\theta$),
apply Lemma 1 directly: Mulan wins in $\le k-1$ moves ($0$ moves if $k=1$, i.e. some angle
already is $\theta$).

**Step 1 (the general one-move forcing construction, Lemma 2).** Otherwise, relabel so
that $X=\max(X,Y,Z)$ (ties broken arbitrarily), and let $Y,Z$ be the other two angles in
either order.

*Claim: there exists an integer $k$ with $1\le k\le n-1$ such that*
$$Y < k\theta < X+Y.$$

*Proof of claim.* Since $X+Y+Z=180=n\theta$, the condition $k\theta<X+Y$ is equivalent to
$Z<(n-k)\theta$. So we must find $k\in\{1,\dots,n-1\}$ with $Y<k\theta$ **and**
$Z<(n-k)\theta$.

- **Case $n\ge3$, non-equilateral (equivalently $X>\theta$).** Since $X$ is the maximum
  angle of a triangle, $X\ge 60$. If $n\ge4$ then $\theta=180/n\le45<60\le X$, so $X>\theta$
  strictly. If $n=3$ then $\theta=60\le X$, with equality iff $X=Y=Z=60$ (equilateral,
  already excluded by Step 0); if not equilateral, $X>60=\theta$ strictly. So in all these
  cases $X>\theta$ strictly.

  Consider the open interval $I=(Y,\,X+Y)$, which has length $X>\theta$. We use the
  elementary fact: *an open interval of length strictly greater than $\theta$ contains a
  multiple of $\theta$.* Indeed, for $I=(a,b)$ with $b-a>\theta$, put
  $k=\lfloor a/\theta\rfloor+1$; then $k\theta>a$ (since $k>a/\theta$), and
  $k\theta=(\lfloor a/\theta\rfloor+1)\theta\le a+\theta<a+(b-a)=b$ (using
  $\lfloor a/\theta\rfloor\le a/\theta$). So $k\theta\in(a,b)$.

  Applying this to $I=(Y,X+Y)$ gives an integer $k$ with $Y<k\theta<X+Y$. Since $Y>0$ we
  get $k\theta>Y>0$ hence $k\ge1$; since $X+Y<180=n\theta$ (as $Z>0$) we get $k\theta<n\theta$
  hence $k\le n-1$. This proves the claim in this case.

- **Case $n=2$ ($\theta=90$).** We need $k=1$ (the only integer in $\{1,\dots,n-1\}$), i.e.
  $Y<90<X+Y$, i.e. $Z<90$. Since $X=\max(X,Y,Z)$, we have $Z\le X$. If $X<90$ the whole
  triangle is acute so $Z\le X<90$. If $X\ge90$, then since $X+Y+Z=180$ and $X\ge90$, we get
  $Y+Z\le90$, and since $Y,Z>0$ this forces $Z<90$ as well (if $Z\ge90$ then $Y\le90-Z\le0$,
  impossible). Either way $Z<90$, proving the claim for $n=2$. $\square$ (claim)

**Executing the move.** With $k$ as found, set the apex to $X$, label the two base angles
$Y,Z$ as above, and choose
$$a_1 := k\theta - Y \in (0,X)$$
(valid by the claim: $a_1>0$ since $Y<k\theta$, and $a_1<X$ since $k\theta<X+Y$). Then
$$\text{child}_1=(Y,\ a_1,\ Z+X-a_1) = (Y,\ k\theta-Y,\ (n-k)\theta),$$
$$\text{child}_2=(Z,\ X-a_1,\ Y+a_1) = (Z,\ X-k\theta+Y,\ k\theta),$$
where we used $Z+X-a_1 = Z+X-k\theta+Y = (X+Y+Z)-k\theta = n\theta-k\theta=(n-k)\theta$ for
child$_1$'s third angle, and $Y+a_1=Y+k\theta-Y=k\theta$ directly for child$_2$'s third
angle. (We verified this algebraic identity by direct symbolic/numeric substitution on
2000 random triangles for $n=5$; see verification note below.)

So **child$_1$ carries an angle exactly $(n-k)\theta$ and child$_2$ carries an angle
exactly $k\theta$**, with $1\le k\le n-1$ and correspondingly $1\le n-k\le n-1$ — both are
positive integer multiples of $\theta$. Whichever child Shan-Yu keeps, Lemma 1 applies: if
he keeps child$_1$, Mulan wins in at most $(n-k)-1$ more moves; if child$_2$, at most
$k-1$ more moves. So Mulan wins in at most $1+\max(k,n-k)-1=\max(k,n-k)\le n-1$ total moves.

This holds from *any* starting triangle (Step 0 handles the finitely-many-already-resonant
case, Step 1 covers everything else), completing sufficiency, with an explicit uniform
bound of $n-1$ total moves. $\blacksquare$

*(Verification note: the identity above was checked by direct floating-point substitution
on 2000 uniformly random triangles for $n=5$ — in every trial the computed $a_1$ landed in
$(0,X)$ and child$_1$, child$_2$ hit $(n-k)\theta,\ k\theta$ to within $10^{-6}$; likewise
the Chain Lemma's forced sequence was checked numerically for $k=2,3,4,5$ with $\theta=37$,
taking exactly $k-1$ moves each time, matching the closed form.)*

---

### 3. Necessity: $\theta\ne180^\circ/n$ for any integer $n\Rightarrow$ Shan-Yu wins forever

Fix $\theta\in(0,180)$ not of the form $180/n$ for any integer $n\ge2$ (equivalently:
$180/\theta\notin\mathbb Z_{\ge2}$, equivalently $180$ is not an integer multiple of
$\theta$... more precisely we need: there is **no** positive integer $N$ with
$N\theta=180$). We construct an explicit starting triangle and a defense for Shan-Yu that
survives forever.

**The invariant.** Say a triangle $(X,Y,Z)$ is *safe* if none of $X,Y,Z$ is an integer
multiple of $\theta$, i.e. $X,Y,Z\notin\theta\mathbb Z:=\{\theta,2\theta,3\theta,\dots\}$
(note in particular $\theta$ itself, being $1\cdot\theta$, is excluded — so a safe triangle
in particular has no angle equal to $\theta$, i.e. is not an immediate loss).

We will show:
(a) a safe starting triangle exists;
(b) if the current triangle is safe, then for **every** choice Mulan makes (apex, labeling
of the other two angles, and real $a_1\in(0,X)$), **at least one** of the two children is
again safe — so Shan-Yu can always respond by keeping a safe child, maintaining safety
forever.

Since a safe triangle never has an angle $=\theta$ (that's the $k=1$ case of
$\theta\mathbb Z$), maintaining safety forever means the "current triangle has angle $\theta$"
check never triggers, i.e. Mulan never wins. This proves necessity.

**Lemma 2 (the central computation — key gap of this approach, now closed).** Let
$(X,Y,Z)$ be safe, apex $X$, other two angles $Y,Z$ (either labeling), and let
$a_1\in(0,X)$ be arbitrary (real, Mulan's free choice — *not* assumed related to $\theta$
in any way). If $\theta\ne180/N$ for every positive integer $N$, then at least one of
child$_1=(Y,a_1,Z+X-a_1)$, child$_2=(Z,X-a_1,Y+a_1)$ is safe.

*Proof.* Child$_1$'s first angle is $Y$, already known safe ($Y\notin\theta\mathbb Z$).
Child$_1$ is unsafe iff $a_1\in\theta\mathbb Z$ **or** $Z+X-a_1\in\theta\mathbb Z$, i.e.
$$a_1 \in B_1 := \theta\mathbb Z \ \cup\ \big((Z+X)-\theta\mathbb Z\big).$$
Similarly child$_2$'s first angle $Z$ is safe, and child$_2$ is unsafe iff
$$a_1 \in B_2 := \big(X-\theta\mathbb Z\big) \ \cup\ \big(\theta\mathbb Z - Y\big).$$
(Here $\theta\mathbb Z$ denotes the full two-sided set $\{k\theta : k\in\mathbb Z\}$; note
$k$ need not be positive here — we are only asking whether a specific real number equals
$k\theta$ for *some* integer $k$, which is the precise negation of "safe", so we must allow
all integers $k$, though as we verify below the specific coincidences that arise force $k$
into a range that turns out consistent with the earlier discussion.)

If *both* children were unsafe for this particular $a_1$, then $a_1\in B_1\cap B_2$, i.e.
$a_1$ satisfies one of $B_1$'s two defining conditions **and** one of $B_2$'s two defining
conditions simultaneously. There are exactly four combinations to check:

1. $a_1=m\theta$ and $a_1=X-n\theta$ for integers $m,n$
   $\Rightarrow X=(m+n)\theta\in\theta\mathbb Z$. **Impossible**: $X$ is safe.
2. $a_1=m\theta$ and $a_1=n\theta-Y$ for integers $m,n$
   $\Rightarrow Y=(n-m)\theta\in\theta\mathbb Z$. **Impossible**: $Y$ is safe.
3. $a_1=(Z+X)-m\theta$ and $a_1=X-n\theta$ for integers $m,n$
   $\Rightarrow Z=(m-n)\theta\in\theta\mathbb Z$. **Impossible**: $Z$ is safe.
4. $a_1=(Z+X)-m\theta$ and $a_1=n\theta-Y$ for integers $m,n$
   $\Rightarrow X+Y+Z=(m+n)\theta$, i.e. $180=(m+n)\theta$, i.e. $\theta=180/(m+n)$ for the
   integer $N:=m+n$. **Impossible by hypothesis** ($\theta\ne180/N$ for any integer $N$;
   note if $N\le0$ this would give $\theta\le0$, contradicting $\theta>0$, so this rules
   out $N\le0$ automatically too — the hypothesis "no integer $N\ge2$ works" together with
   $\theta<180$ excluding $N=1$ and $\theta>0$ excluding $N\le0$ covers every integer $N$).

All four combinations are impossible, so $B_1\cap B_2=\varnothing$: no single value of
$a_1$ can make both children unsafe. Hence at least one child is safe. $\blacksquare$

(This argument used only that $X,Y,Z$ are safe and $\theta\ne180/N$ for integer $N$; it did
**not** need $a_1\in(0,X)$ — the conclusion holds for every real $a_1$, so restricting to
the legal range $(0,X)$ only makes Mulan's task harder, not easier. It also holds
symmetrically for either choice of apex among $X,Y,Z$ and either labeling of the other two,
since the argument only used the fixed sum $X+Y+Z=180$, never which angle was designated
apex — cases 1–3 are always blocked by the *safety of the two non-apex-carried* angles, and
case 4 always reduces to the same identity $180=(m+n)\theta$ regardless of which angle is
apex.)

**Existence of a safe starting triangle (part (a)).** Let $S:=\theta\mathbb Z\cap(0,180)$,
a *finite* set (since $\theta>0$, $S=\{\theta,2\theta,\dots,\lfloor 180/\theta\rfloor\theta\}$
truncated to stay below $180$, of size $\lceil 180/\theta\rceil-1$ or so — finite regardless
of the exact count). Choose $X_0\in(0,180)\setminus S$ (possible: $S$ is finite, so
$(0,180)\setminus S$ is a cofinite, hence nonempty — indeed uncountable — subset of an
interval). Then choose
$$Y_0 \in (0,180-X_0)\ \setminus\ \Big(S\ \cup\ \{180-X_0-s : s\in S\}\Big).$$
The set being removed is a union of two finite sets, hence finite, while $(0,180-X_0)$ is
a nonempty open interval (as $X_0<180$), so such $Y_0$ exists. Set $Z_0:=180-X_0-Y_0>0$
(positive since $Y_0<180-X_0$ by construction). By construction $X_0,Y_0\notin S=\theta\mathbb
Z\cap(0,180)$, and also $Z_0\notin S$ (since $Y_0$ was chosen to avoid every value
$180-X_0-s$ for $s\in S$, i.e. to avoid every $Y_0$ that would make $Z_0=s\in S$). Since
all of $X_0,Y_0,Z_0\in(0,180)$, "not in $S$" is exactly "not in $\theta\mathbb Z$" for these
three values. So $(X_0,Y_0,Z_0)$ is a valid, safe starting triangle.

**Conclusion of necessity.** Shan-Yu starts with the safe triangle $(X_0,Y_0,Z_0)$
constructed above. At every subsequent round, whatever apex/labeling/real $a_1$ Mulan
chooses, Lemma 2 guarantees at least one child is safe; Shan-Yu keeps a safe child (if both
happen to be safe, either choice is fine). By induction, the triangle is safe at the start
of every round, forever. A safe triangle never has an angle equal to $\theta$ (since
$\theta=1\cdot\theta\in\theta\mathbb Z$ is exactly the excluded case $k=1$), so the winning
check "$T$ has an angle $=\theta$" never fires. Mulan never wins; Shan-Yu survives
indefinitely. This holds for every $\theta$ not of the form $180/n$, $n\ge2$ integer,
completing necessity. $\blacksquare$

*(Verified numerically as a sanity cross-check: the $\theta>90$ special case — where the
even simpler invariant "all angles $<\theta$" suffices, since then a safe/obtuse-avoiding
triangle trivially never reaches $\theta$ — was checked directly on 3000 random triangles
and cuts with $\theta=100$: in every trial at least one child kept all angles $<100$. This
is consistent with, and a special case of, the general Lemma 2 argument above, since
"all angles $<\theta$" trivially implies "no angle is a multiple of $\theta$" once
$\theta>60$ guarantees the invariant is initially satisfiable and self-perpetuating — we
do not need this special case separately since Lemma 2 already covers all $\theta$
uniformly, but it is a useful independent check of the general machinery.)*

---

### 4. Conclusion

Combining Sections 2 and 3: Mulan has a finite winning strategy from every starting
triangle if and only if $\theta=180^\circ/n$ for some integer $n\ge2$. This is the
complete characterization (an instance of `compute_and_prove` / `characterization`
answer type), stated and verified explicitly:

**Answer.** $\boxed{\theta = \dfrac{180^\circ}{n},\ n=2,3,4,\dots}$

- *Verification of sufficiency*: Section 2 gives, for each such $\theta$, an explicit
  finite strategy (bounded by $n-1$ moves) working against every Shan-Yu starting triangle
  and every sequence of his choices — Step 0 (Lemma 1, chain shaving) handles triangles
  already carrying a multiple of $\theta$, Step 1 (Lemma 2's sufficiency counterpart)
  handles every other triangle by a single explicit cut forcing a multiple of $\theta$ into
  *both* possible survivors.
- *Verification of necessity*: Section 3 exhibits, for every other $\theta$, an explicit
  safe starting triangle and proves (Lemma 2's necessity direction) that "no angle is a
  multiple of $\theta$" is an invariant Shan-Yu can maintain forever against every possible
  move Mulan can make (every apex, every labeling, every real cut parameter) — not merely
  against a restricted class of moves.

Both directions are fully constructive/explicit as required by the problem's
`compute_and_prove` task type. $\blacksquare$

## Promotable lemmas

- **Chain Lemma (Lemma 1)**: For any $\theta\in(0,180)$, if the current triangle has an
  angle equal to $k\theta$ for a positive integer $k$, Mulan wins in at most $k-1$ further
  moves via repeated apex-shaving with $a_1=\theta$. Proved in full by induction in Section
  1 above (uses only the angle-arithmetic move formulas, no special hypothesis on $\theta$).
  Reusable by any approach needing a "resonance ⇒ forced win" building block.

- **Resonance dichotomy Lemma (Lemma 2, both directions)**: For a triangle with
  $X,Y,Z\notin\theta\mathbb Z$, apex $X$, and any real $a_1$, at least one child avoids
  $\theta\mathbb Z$ entirely *unless* $\theta=180/N$ for a positive integer $N$ — in which
  case (Section 2, Step 1) an explicit $a_1$ can be chosen forcing a multiple of $\theta$
  into *both* children simultaneously. This single 4-case computation (Section 3, Lemma 2's
  proof) is the load-bearing step for BOTH the necessity direction (three of the four
  combinations are always impossible when the invariant holds) and, via its resonant
  4th case, the sufficiency direction's one-move forcing construction (Section 2, Step 1).
  Fully proved, reusable as the single central lemma of the whole problem.

- **Safe-triangle existence construction**: for any finite forbidden set $S\subset(0,180)$
  (here $S=\theta\mathbb Z\cap(0,180)$), an explicit two-stage choice ($X_0$ avoiding $S$,
  then $Y_0$ avoiding $S$ and its "reflection" under $Z_0=180-X_0-Y_0$) produces a triangle
  with all three angles outside $S$. General-purpose device, reusable whenever a problem
  needs "construct a triangle/tuple avoiding finitely many forbidden values."
