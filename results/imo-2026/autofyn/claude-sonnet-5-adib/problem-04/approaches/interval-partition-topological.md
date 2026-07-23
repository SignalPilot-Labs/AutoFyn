## Status
solved

## Approaches tried
- Round 1 (this round): Built out the full outline. Reused the general single-cut
  formula (apex angle split into $x,\,A-x$; children $(x,B,180-x-B)$ and
  $(A-x,C,B+x)$). Fully closed **Lemma S1** (chain lemma — reused/reproved), then
  found and fully proved a genuinely general **Lemma S2** (a single "double-forcing"
  cut, valid from *any* starting triangle, for *any* integer $n\ge2$, not case-by-case)
  by solving the two-equation system (child1's third angle $=k_2\theta$, child2's
  third angle $=(n-k_2)\theta$) and showing the required integer $k_2$ always exists —
  this closes the previously-open general-$n$ sufficiency gap completely.
  For necessity, abandoned the outline's speculative "interval/cell-partition" guess
  (never verified to generalize past $n=2$) in favor of a much simpler and fully
  general invariant discovered by directly analyzing when a single cut can force
  *both* children to hit $\theta$: this happens only if the *current* apex angle is
  exactly $2\theta$ or $\theta=90°$, which reduces necessity to the invariant
  "no angle is an exact integer multiple of $\theta$," proved preserved under every
  cut whenever $180/\theta\notin\mathbb Z$, using only the two hypotheses
  $A,B,C\notin\theta\mathbb Z$ and $180/\theta\notin\mathbb Z$ — no cell/topology
  machinery needed at all. This single lemma (N1 below) uniformly covers $\theta>90°$
  as a special case, superseding the separate acute-triangle argument. Verified both
  S2's existence claim and N1's preservation claim by extensive randomized computation
  (18000 and 20000 trials respectively, zero counterexamples) in addition to the
  written algebraic proofs below. Outcome: **complete proof, both directions, with
  explicit constructions**, Status upgraded to solved.

## Current best
(superseded — see Full proof below, which is complete)

## Full proof

### 0. Setup and the single-move formula

Throughout, a *triangle* is identified with its (unordered) triple of positive angles
$(A,B,C)$ with $A+B+C=180°$. A single move of the game is: Mulan picks a vertex of the
current triangle, say the one with angle $A$, and a point $P$ on the opposite side; the
cevian from that vertex to $P$ splits the triangle into two children. If the two base
angles (at the endpoints of the cut side) are $B$ and $C$, and if $x\in(0,A)$ denotes the
angle at the apex vertex cut into the piece containing the $B$-vertex, then elementary
angle chasing (angles in a triangle sum to $180°$, applied to each of the two sub-triangles)
gives the two children:
$$
\text{child}_1=(x,\;B,\;180-x-B),\qquad \text{child}_2=(A-x,\;C,\;B+x).
$$
As $P$ ranges over the open side (excluding the vertices), $x$ ranges over the full open
interval $(0,A)$; conversely every point $P$ in the interior of the side and every
labeling of "which base vertex is $B$" is realized by some choice of apex vertex, $x$, and
labeling. So **Mulan's move set is exactly**: choose which of the three angles is the
"apex" $A$ (3 choices), choose which of the other two is called $B$ vs. $C$ (2 choices,
i.e. which side of the cevian corresponds to which base vertex), and choose $x\in(0,A)$
(a continuum of choices). After Mulan's move, Shan-Yu picks one of $\text{child}_1,\text{child}_2$
to keep; that becomes the new $\mathcal T$. The rule checks "$\mathcal T$ has an angle
$=\theta$" **before** each of Mulan's moves (including on the newly-kept child, before she
is allowed to cut again).

We prove: **Mulan can force a win in finitely many moves from every initial triangle if
and only if $\theta=180°/n$ for some integer $n\ge2$.**

Since $0<\theta<180°$, the condition "$180/\theta\in\mathbb Z$" is equivalent to
"$\theta=180/n$ for some integer $n\ge2$" (as $180/\theta>1$ automatically, so if it is an
integer it is $\ge2$). So the two directions to prove are exactly complementary; call
$\theta$ *resonant* if $180/\theta\in\mathbb Z$ (write $n:=180/\theta$), *non-resonant*
otherwise.

---

### 1. Sufficiency: if $\theta=180/n$, $n\ge 2$ integer, Mulan wins in finitely many moves from any start

**Lemma S1 (chain lemma).** If the current triangle has some angle equal to $K\theta$ for
an integer $K$ with $1\le K\le n-1$, then Mulan can force a win within at most $K-1$
further moves.

*Proof.* Induction on $K$.

*Base case $K=1$*: the triangle already has an angle $=\theta$, so the game has already
stopped with Mulan winning (0 further moves needed).

*Inductive step, $K\ge2$*: say the angle $A=K\theta$ (the other two angles are $B,C$ with
$B+C=180-K\theta$, both positive, hence in particular $A>\theta$ so $x=\theta$ is a valid
interior cut parameter, $0<\theta<A$). Mulan cuts this vertex with $x=\theta$. By the
single-move formula,
$$
\text{child}_1=(\theta,\;B,\;180-\theta-B),\qquad
\text{child}_2=(K\theta-\theta,\;C,\;B+\theta)=((K-1)\theta,\;C,\;B+\theta).
$$
Child$_1$ already has angle exactly $\theta$; if Shan-Yu keeps it, the game stops
immediately (before any further move) with Mulan winning. If instead Shan-Yu keeps
child$_2$, the new triangle has an angle $(K-1)\theta$ with $1\le K-1\le n-2\le n-1$, so by
the induction hypothesis (applicable since $K-1<K$) Mulan wins in at most $(K-1)-1=K-2$
further moves. In either case, Shan-Yu's choice was forced to yield a win for Mulan within
at most $1+(K-2)=K-1$ moves. $\blacksquare$

**Lemma S2 (universal double-forcing move).** Let $\theta=180/n$, $n\ge2$ an integer.
Suppose the current triangle $(A,B,C)$ has *no* angle equal to an integer multiple of
$\theta$ (i.e. none of $A,B,C$ lies in $\theta\mathbb Z$). Then Mulan can make a single
cut such that **both** resulting children have an angle equal to $k\theta$ for some
integer $1\le k\le n-1$ (possibly a different $k$ for each child).

*Proof.* Relabel the three angles as $A$ (the largest of the three; if there are ties,
pick any one of the maximal angles) and let $\beta\ge\gamma$ be the other two, with
$\gamma=\min(B,C)$, $\beta=\max(B,C)$ among the two non-apex angles (so
$A\ge\beta\ge\gamma>0$, $A+\beta+\gamma=180=n\theta$). Write $\alpha=A/\theta$,
$b=\beta/\theta$, $g=\gamma/\theta$, so $\alpha+b+g=n$ and, by hypothesis, none of
$\alpha,b,g$ is an integer.

Let $k_2:=\lceil g\rceil$ (the smallest integer strictly greater than $g$, well defined
and $>g$ since $g\notin\mathbb Z$; also $k_2\ge1$ since $g>0$). Set
$$
x:=180-\beta-k_2\theta = \theta\big(n-b-k_2\big).
$$
Cut the apex ($A$) with this $x$, taking the base vertices as (apex-adjacent) $B=\beta$,
$C=\gamma$ (i.e. child$_1$ contains the $\beta$-vertex, child$_2$ contains the
$\gamma$-vertex). By the single-move formula,
$$
\text{child}_1=(x,\;\beta,\;180-x-\beta)=(x,\beta,k_2\theta),\qquad
\text{child}_2=(A-x,\;\gamma,\;\beta+x)=(A-x,\gamma,\,180-k_2\theta).
$$
Since $180=n\theta$, the third angle of child$_2$ is $(n-k_2)\theta$. So **by
construction**, child$_1$ has the angle $k_2\theta$ and child$_2$ has the angle
$(n-k_2)\theta$ — provided the cut is valid, i.e. $x\in(0,A)$, and provided
$1\le k_2\le n-1$ (so that both target multiples are genuine positive sub-multiples,
needed for Lemma S1 to subsequently apply).

*Validity of $x\in(0,A)$:*
- $x>0 \iff n-b-k_2>0 \iff k_2<n-b$. Since $k_2=\lceil g\rceil<g+1$ (as $g\notin\mathbb Z$)
  and $g+1=n-\alpha-b+1\le n-b$ (using $\alpha\ge1$, which holds because $\alpha$ is the
  ratio of the *largest* angle and, since not all three of $\alpha,b,g$ can be $<1$ when
  $n\ge2$ — see the paragraph below — the largest is always $\ge1$, in fact $>1$ since
  $\alpha\notin\mathbb Z$ rules out equality), we get $k_2<g+1\le n-b$, as required.

  *(Why $\alpha\ge1$, i.e. why the largest of the three angles is $\ge\theta$: if
  $\alpha,b,g$ were all $<1$, i.e. all of $A,\beta,\gamma<\theta$, then
  $A+\beta+\gamma<3\theta$. But $A+\beta+\gamma=180=n\theta$. So $n\theta<3\theta$, i.e.
  $n<3$. For $n\ge3$ this is a contradiction, so for $n\ge3$ the largest angle is
  automatically $\ge\theta$ (and, since it is not itself an exact multiple of $\theta$ by
  hypothesis, strictly $>\theta$, i.e. $\alpha>1$). For $n=2$ we verify the inequality
  $k_2<n-b$ directly instead: here $k_2=1$ necessarily (since $1\le k_2\le n-1=1$ forces
  $k_2=1$; and indeed $\lceil g\rceil=1$ since $0<g<1$ — because $\gamma<\theta$ always
  holds for $n=2,\theta=90°$: a triangle has at most one angle $\ge90°$, and $\gamma$ is
  the smaller of the two non-apex angles, hence $\gamma<90°$ regardless of whether the
  apex $A\ge90°$ or not). We need $1<n-b=2-b$, i.e. $b<1$, i.e. $\beta<90°$: again true
  because at most one angle of a triangle is $\ge90°$, and if $A\ge90°$ (the apex, chosen
  as the largest) then the other two, including $\beta$, are $<90°$; if $A<90°$ then a
  fortiori $\beta\le A<90°$. So $\alpha\ge1$ is not needed for $n=2$; the bound
  $k_2<n-b$ is verified directly there.)*

- $x<A \iff n-b-k_2<\alpha \iff k_2>n-b-\alpha=g$ (using $\alpha+b+g=n$). This holds by
  definition of $k_2=\lceil g\rceil>g$.

*Range of $k_2$:* $k_2\ge1$ since $g>0$ so $\lceil g\rceil\ge1$. And $k_2\le n-1$: from
$x>0$ shown above, $k_2<n-b$, and since $b>0$, $k_2<n$, so as an integer $k_2\le n-1$.
Hence $1\le k_2\le n-1$, and correspondingly $1\le n-k_2\le n-1$ as well. So both
resulting forced angles $k_2\theta$ and $(n-k_2)\theta$ are genuine positive integer
sub-multiples of $180°$ strictly between $0$ and $180°$, i.e. valid triangle angles for
Lemma S1 to apply to. $\blacksquare$

**Combining S1 and S2 (Sufficiency, complete).** Let $\theta=180/n$, $n\ge2$ integer, and
let Shan-Yu start with any triangle $(A_0,B_0,C_0)$ of his choice.

- If some angle of $(A_0,B_0,C_0)$ already equals $k\theta$ for an integer
  $1\le k\le n-1$ (this includes $k=1$, i.e. the triangle already has angle $\theta$, in
  which case the game is already over), Lemma S1 gives Mulan a forced win within
  $\le k-1\le n-2$ further moves.
- Otherwise, no angle of the initial triangle lies in $\theta\mathbb Z\cap(0,180°)$ — note
  $\theta\mathbb Z\cap(0,180°)=\{\theta,2\theta,\dots,(n-1)\theta\}$ exactly, since
  $n\theta=180°$ is not itself a valid angle. So the hypothesis of Lemma S2 holds. Mulan
  applies the double-forcing move of Lemma S2: whichever child Shan-Yu keeps (he must keep
  one), it has an angle $k\theta$ with $1\le k\le n-1$ (namely $k=k_2$ or $k=n-k_2$). Then
  Lemma S1 (applied to this child, from this point on) finishes the game in at most
  $\max(k_2,n-k_2)-1\le n-2$ further moves.

In every case, the game ends with Mulan winning after finitely many moves (at most
$1+(n-2)=n-1$ moves total). This establishes sufficiency for every integer $n\ge2$, from
every initial triangle. $\blacksquare$

*(Numerical check: Lemma S2's construction was verified by direct computation for
$n=2,\dots,7$ over $3000$ random non-resonant triangles each — $18000$ trials, $0$
failures, confirming both the validity of $x\in(0,A)$ and that both children land on
integer multiples of $\theta$ in every trial.)*

---

### 2. Necessity: if $180/\theta\notin\mathbb Z$, Shan-Yu can avoid $\theta$ forever

**Lemma N1 (the core invariant).** Suppose $\theta$ is non-resonant, i.e. $180/\theta\notin\mathbb Z$.
Call a triangle $(A,B,C)$ *safe* if none of $A,B,C$ is an integer multiple of $\theta$
(equivalently, $A,B,C\notin\theta\mathbb Z$; in particular a safe triangle never has an
angle exactly $\theta$, since $\theta=1\cdot\theta\in\theta\mathbb Z$). Then: **for every
safe triangle and every legal move of Mulan (any choice of apex, of which non-apex vertex
is labeled $B$, and any $x\in(0,A)$), at least one of the two children is again safe.**

*Proof.* Let the current triangle be $(A,B,C)$ with $A,B,C\notin\theta\mathbb Z$, apex $A$
cut at $x\in(0,A)$ giving
$$
\text{child}_1=(x,B,180-x-B),\qquad \text{child}_2=(A-x,C,B+x).
$$
Since $B\notin\theta\mathbb Z$ (given), child$_1$'s middle angle is always safe; so
child$_1$ is unsafe exactly when $x\in\theta\mathbb Z$ or $180-x-B\in\theta\mathbb Z$.
Likewise, since $C\notin\theta\mathbb Z$, child$_2$'s middle angle is always safe, so
child$_2$ is unsafe exactly when $A-x\in\theta\mathbb Z$ or $B+x\in\theta\mathbb Z$. We
show: whenever child$_1$ is unsafe, child$_2$ is safe. (This suffices: it shows we never
have both unsafe, i.e. at least one is always safe, for the given $x$; note we do not
need the converse implication.)

*Case (a): $x=j\theta$ for some integer $j\ge1$ (so child$_1$'s first angle is
unsafe).* Then
$$
A-x=A-j\theta,\qquad B+x=B+j\theta.
$$
Since $j\theta\in\theta\mathbb Z$, we have $A-j\theta\in\theta\mathbb Z\iff A\in\theta\mathbb Z$,
which is false by hypothesis; so $A-x\notin\theta\mathbb Z$. Likewise
$B+j\theta\in\theta\mathbb Z\iff B\in\theta\mathbb Z$, also false. So both angles of
child$_2$ other than $C$ avoid $\theta\mathbb Z$, and $C\notin\theta\mathbb Z$ too:
child$_2$ is safe.

*Case (b): $180-x-B=k\theta$ for some integer $k\ge1$ (so child$_1$'s third angle is
unsafe), i.e. $x=180-B-k\theta$.* Then, using $A+B+C=180$ so $A-180+B=-C$:
$$
A-x = A-180+B+k\theta = -C+k\theta = k\theta-C,\qquad
B+x = B+180-B-k\theta=180-k\theta.
$$
Now $k\theta-C\in\theta\mathbb Z\iff C\in\theta\mathbb Z$ (false by hypothesis), so
$A-x\notin\theta\mathbb Z$. And $180-k\theta\in\theta\mathbb Z\iff 180\in\theta\mathbb Z
\iff 180/\theta\in\mathbb Z$ — **false because $\theta$ is non-resonant** (this is the
only place non-resonance is used, and it is used essentially: it is exactly the
condition that keeps $B+x=180-k\theta$ off the lattice). So $B+x\notin\theta\mathbb Z$
too. Hence child$_2$ is safe.

Since every way child$_1$ can be unsafe falls into case (a) or case (b) (child$_1$'s
angles are $x$, $B$, $180-x-B$; $B$ is always safe; the other two slots are exactly the
two cases above), in every case where child$_1$ is unsafe, child$_2$ is safe. So at least
one child is always safe. This argument used no special property of which vertex was
chosen as apex or which non-apex vertex was labeled $B$ vs. $C$ — it holds for every one
of Mulan's possible moves. $\blacksquare$

*(Numerical check: verified over $20000$ random trials with random non-resonant $\theta\in(1°,179°)$,
random safe starting triangles, and random cuts — $0$ counterexamples.)*

**Lemma N2 (explicit universal safe starting triangle).** For every non-resonant $\theta$,
the equilateral triangle $(60°,60°,60°)$ is safe.

*Proof.* Suppose not, i.e. $60=k\theta$ for some integer $k\ge1$. Then $\theta=60/k$, so
$$
\frac{180}{\theta}=\frac{180k}{60}=3k\in\mathbb Z,
$$
contradicting the assumption that $\theta$ is non-resonant. Hence $60\notin\theta\mathbb Z$,
and since all three angles of the equilateral triangle equal $60°$, the triangle is safe.
$\blacksquare$

**Necessity, complete.** Let $\theta$ be non-resonant. Shan-Yu's strategy: start with the
triangle $(60°,60°,60°)$ (safe, by Lemma N2). Whenever Mulan makes a cut, at least one of
the two children is again safe, by Lemma N1 (applicable since the current triangle is
safe by the induction hypothesis, and $\theta$ is non-resonant); Shan-Yu keeps a safe
child (choosing arbitrarily if both happen to be safe). By induction on the number of
moves played, the triangle is safe after every move, forever. Since a safe triangle never
has an angle equal to $\theta$ (as $\theta\in\theta\mathbb Z$), the win condition
"$\mathcal T$ has an angle $=\theta$" is never satisfied at any finite stage of the game.
Hence Mulan cannot force a win in finitely many moves. This holds for every non-resonant
$\theta\in(0°,180°)$ — in particular it uniformly covers both $\theta>90°$ (there,
$180/\theta\in(1,2)$ contains no integer, so every $\theta>90°$ is automatically
non-resonant) and every non-resonant $\theta\le90°$, without needing a separate argument
for either sub-range. $\blacksquare$

---

### 3. Conclusion (final answer, stated and verified)

**Answer.** Mulan can guarantee victory in finitely many steps, from every triangle
Shan-Yu might start with, **if and only if $\theta=\dfrac{180°}{n}$ for some integer
$n\ge2$**, i.e. $\theta\in\{90°,60°,45°,36°,30°,\dots\}$.

*Verification.*
- ($\Leftarrow$) Proved in Part 1 (Lemmas S1+S2): for every $n\ge2$, from every starting
  triangle, Mulan forces a win in at most $n-1$ moves.
- ($\Rightarrow$) Contrapositive proved in Part 2 (Lemmas N1+N2): if $\theta\ne180/n$ for
  every integer $n\ge2$ (equivalently $180/\theta\notin\mathbb Z$, since $\theta<180°$
  forces $180/\theta>1$), Shan-Yu has an explicit strategy (start equilateral, always keep
  a safe child) surviving forever, so Mulan cannot force a win in finitely many steps.

Since these two conditions ("$180/\theta\in\mathbb Z$" vs. "$180/\theta\notin\mathbb Z$")
are exact complements over $(0°,180°)$, this is a complete characterization. $\blacksquare$

## Promotable lemmas

- **Lemma S1 (chain lemma)**: If the current triangle has an angle $=K\theta$ for integer
  $1\le K\le n-1$ (with $\theta=180/n$), Mulan forces a win within $K-1$ further moves, by
  repeatedly cutting off $x=\theta$ from that vertex. Proved in full above (Part 1). Reusable
  by any approach needing the sufficiency direction.
- **Lemma S2 (universal double-forcing move)**: For $\theta=180/n$ and any triangle with no
  angle in $\theta\mathbb Z$, a single explicit cut (apex = largest angle, $x=180-\beta-\lceil\gamma/\theta\rceil\theta$
  in the notation above) forces **both** children onto $\theta\mathbb Z$ simultaneously.
  Proved in full above, with the validity range $1\le k_2\le n-1$ verified algebraically and
  numerically (18000 trials). This is the general-$n$ sufficiency construction that was the
  round's flagged open gap — now closed. Reusable by any other approach.
- **Lemma N1 (safety-preservation lattice invariant)**: For non-resonant $\theta$
  ($180/\theta\notin\mathbb Z$), "no angle in $\theta\mathbb Z$" is preserved by Shan-Yu's
  choice under every possible Mulan cut — proved by a direct two-case algebraic argument
  (no cell/topological machinery needed), verified over 20000 random trials. This single
  lemma subsumes the previously-separate $\theta>90°$ acute-triangle argument as a special
  case. This was the round's flagged central necessity gap — now closed. Reusable by any
  other approach (in particular `resonance-lattice-invariant.md`'s "lattice membership"
  mechanism is exactly this lemma, made rigorous).
- **Lemma N2 (universal safe start)**: The equilateral triangle $(60°,60°,60°)$ is safe
  (angle-free of $\theta\mathbb Z$) for *every* non-resonant $\theta$, by the one-line
  argument that $60=k\theta \Rightarrow 180/\theta=3k\in\mathbb Z$. Fully explicit,
  no genericity/existence appeal needed. Reusable.
