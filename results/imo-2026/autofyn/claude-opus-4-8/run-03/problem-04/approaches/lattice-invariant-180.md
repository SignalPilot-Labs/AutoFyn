# Approach: lattice-invariant-180

## Status
solved

## Approaches tried
- Round 1: lattice/invariant framing proposed; characterization θ|180 conjectured and
  computationally confirmed — reached `partial` with 5 flagged gaps (G1–G5).
- Round 2: closed all gaps. Explicit starting triangle (θ/2, θ/2, 180−θ) for necessity;
  fully explicit plant cut x = (⌊β/θ⌋+1)θ − β with a clean "open interval of length α/θ > 1
  contains an integer" existence argument; separate clean θ=90 altitude; explicit forced
  descent with a strictly decreasing monovariant m and a finite move bound n−1. All
  non-degeneracy checks written out. — **solved**.

## Current best
Complete proof of the full characterization **Mulan wins ⟺ θ divides 180°**, both
directions, with all cases and non-degeneracy checks closed. See Full proof.

## Full proof

### 0. Answer

Mulan can guarantee victory in finitely many steps **if and only if θ divides 180°**, i.e.
if and only if 180/θ is a positive integer. Equivalently, the winning set is
$$\{\,\theta = 180^\circ/n : n \in \mathbb{Z},\ n \ge 2\,\} = \{90^\circ,\,60^\circ,\,45^\circ,\,36^\circ,\,30^\circ,\,180^\circ/7,\,22.5^\circ,\,20^\circ,\dots\}.$$
For every other θ (including all θ > 90°, and also θ = 40°, 50°, 70°, 25°, … which are
≤ 90° but do not divide 180°), Shan-Yu can play forever and prevent Mulan from ever
producing an angle equal to θ.

Throughout, all angle measures are in degrees and "triangle" means a nondegenerate
triangle, i.e. three angles, each strictly in (0°,180°), summing to 180°.

### 1. The one-cut algebra (exact description of a move)

Let the current triangle $\mathcal{T}$ have vertices $A,B,C$ with angles $\alpha,\beta,\gamma$
respectively, $\alpha+\beta+\gamma=180$. Mulan's move is: choose a point $P$ on the perimeter,
not a vertex, and cut from $P$ to the *opposite* vertex. Thus $P$ lies on some side, say $BC$
(the side opposite $A$), and the cut is the segment $AP$. This splits $\mathcal{T}$ into
$\triangle ABP$ and $\triangle APC$, and splits the angle $\alpha$ at $A$ into
$\angle BAP = x$ and $\angle PAC = \alpha - x$, where $x \in (0,\alpha)$ (strict, since $P$
is not a vertex, so $P$ is interior to side $BC$).

Computing the third angle of each child by the angle-sum law:
- In $\triangle ABP$: angles are $\beta$ (at $B$), $x$ (at $A$), and $\angle APB = 180-\beta-x$.
- In $\triangle APC$: angles are $\gamma$ (at $C$), $\alpha-x$ (at $A$), and
  $\angle APC = 180-\gamma-(\alpha-x) = \beta+x$, using $\alpha+\gamma = 180-\beta$.

Note $\angle APB + \angle APC = (180-\beta-x)+(\beta+x)=180$: the two cut-point angles are
**supplementary**. So, writing the two children as unordered angle-triples,
$$\boxed{\ \text{child}_1 = \{x,\ \beta,\ 180-x-\beta\},\qquad \text{child}_2 = \{\alpha-x,\ \gamma,\ x+\beta\}.\ }$$
Mulan freely chooses **which vertex to split** (equivalently, which side carries $P$) — the
formula above is stated for splitting the vertex $A$ of angle $\alpha$; splitting $B$ or $C$
is the same formula with the labels permuted — and freely chooses the real parameter
$x\in(0,\alpha)$. Shan-Yu then discards one child; the survivor becomes the new $\mathcal{T}$.

**Non-degeneracy (used repeatedly).** For any $x\in(0,\alpha)$ both children are genuine
triangles: all six angles lie strictly in $(0,180)$. Indeed $x>0$, $\beta>0$, $\alpha-x>0$,
$\gamma>0$ are immediate; and
$$180-x-\beta > 180-\alpha-\beta=\gamma>0,\qquad 180-x-\beta<180-\beta<180,$$
$$0<\beta<x+\beta<\alpha+\beta=180-\gamma<180.$$
So every cut with $x\in(0,\alpha)$ is a legal move producing two nondegenerate triangles.

**Terminology.** For a real angle $\varphi$, say $\varphi$ is *on-lattice* if $\varphi/\theta$
is a (positive) integer, i.e. $\varphi \in \theta\mathbb{Z} := \{k\theta : k\in\mathbb{Z}_{\ge 1}\}$;
equivalently $\varphi \equiv 0 \pmod{\theta}$. Since $\theta$ itself is on-lattice, an
on-lattice angle in a triangle need not equal $\theta$, but the game stops (Mulan wins) exactly
when some angle equals $\theta$. We say θ *divides* 180, written $\theta\mid 180$, if
$180/\theta\in\mathbb{Z}$.

### 2. Necessity: if θ ∤ 180 then Shan-Yu wins

We show that when $180/\theta \notin \mathbb{Z}$, Shan-Yu has a strategy keeping the following
invariant true forever:

> **Invariant $I$:** the current triangle has **no on-lattice angle**, i.e. none of its three
> angles is an integer multiple of θ.

Because $\theta = 1\cdot\theta$ is on-lattice, $I$ implies in particular that no angle equals
$\theta$, so the game never stops and Mulan never wins. Thus it suffices to establish that
Shan-Yu can start with, and forever maintain, $I$.

Here "Shan-Yu wins" means: there exists an initial triangle and a discard rule such that, no
matter how Mulan cuts, an angle equal to θ never appears, so the game does not stop in finitely
many steps. This is exactly the negation of "Mulan can guarantee victory in finitely many
steps."

**Base case (explicit starting triangle).** Shan-Yu starts with the isosceles triangle
$$\mathcal{T}_0 = (\theta/2,\ \theta/2,\ 180-\theta).$$
This is a valid triangle: $\theta/2>0$, $180-\theta>0$ (as $\theta<180$), and the three angles
sum to $\theta/2+\theta/2+(180-\theta)=180$. It satisfies $I$:
- $\theta/2$ is not on-lattice: $\theta/2 = k\theta$ would force $k=\tfrac12\notin\mathbb{Z}$.
- $180-\theta$ is not on-lattice: $180-\theta = k\theta$ for some integer $k\ge 1$ would give
  $180=(k+1)\theta$, i.e. $180/\theta = k+1 \in \mathbb{Z}$, contradicting $\theta\nmid 180$.

So $\mathcal{T}_0$ has all three angles off-lattice.

**Inductive step (the covering lemma).** Suppose the current triangle has angles
$\alpha,\beta,\gamma$, all off-lattice, and $\theta\nmid 180$. Mulan makes any move: she picks a
vertex to split — relabel so its angle is $\alpha$ and the neighbours are $\beta,\gamma$ — and
any $x\in(0,\alpha)$. We claim **at least one of the two children has all angles off-lattice**;
Shan-Yu keeps that child, preserving $I$.

Suppose, for contradiction, that **both** children contain an on-lattice angle.

In $\text{child}_1=\{x,\beta,180-x-\beta\}$ the angle $\beta$ is off-lattice by hypothesis, so
the on-lattice angle of $\text{child}_1$ is $x$ or $180-x-\beta$; that is,
$$x\equiv 0 \quad\text{or}\quad 180-x-\beta\equiv 0 \pmod{\theta},$$
i.e. $x\equiv 0$ or $x\equiv 180-\beta \pmod{\theta}$.

In $\text{child}_2=\{\alpha-x,\gamma,x+\beta\}$ the angle $\gamma$ is off-lattice, so the
on-lattice angle is $\alpha-x$ or $x+\beta$; that is,
$$\alpha-x\equiv 0\quad\text{or}\quad x+\beta\equiv 0 \pmod{\theta},$$
i.e. $x\equiv \alpha$ or $x\equiv -\beta \pmod{\theta}$.

Thus $(x\equiv 0 \ \lor\ x\equiv 180-\beta)\ \wedge\ (x\equiv \alpha\ \lor\ x\equiv -\beta)$
$\pmod\theta$. This conjunction of two two-way disjunctions has **exactly four** cases, and we
treat each (all congruences mod θ):

- **(i)** $x\equiv 0$ and $x\equiv\alpha$ $\Rightarrow$ $\alpha\equiv 0$. Since
  $\alpha\in(0,180)$, this means $\alpha$ is a positive integer multiple of θ, i.e. $\alpha$ is
  on-lattice — contradicting the hypothesis $\alpha$ off-lattice.
- **(ii)** $x\equiv 0$ and $x\equiv -\beta$ $\Rightarrow$ $\beta\equiv 0$ $\Rightarrow$ $\beta$
  on-lattice — contradiction.
- **(iii)** $x\equiv 180-\beta$ and $x\equiv\alpha$ $\Rightarrow$ $\alpha\equiv 180-\beta$
  $\Rightarrow$ $\alpha+\beta\equiv 180$. But $\alpha+\beta = 180-\gamma$, so
  $180-\gamma\equiv 180$, giving $\gamma\equiv 0$ $\Rightarrow$ $\gamma$ on-lattice —
  contradiction.
- **(iv)** $x\equiv 180-\beta$ and $x\equiv -\beta$ $\Rightarrow$ $180-\beta\equiv -\beta$
  $\Rightarrow$ $180\equiv 0 \pmod\theta$ $\Rightarrow$ $\theta\mid 180$ — contradicting
  $\theta\nmid 180$.

Every case is contradictory. Hence the assumption "both children on-lattice" is impossible: at
least one child is entirely off-lattice. This argument used only $\alpha,\beta,\gamma$
off-lattice and $\theta\nmid 180$, and it holds for **every** cut vertex Mulan may choose and
**every** $x\in(0,\alpha)$ she may choose (the four cases exhaust all $x$). By the
non-degeneracy remark in §1, the off-lattice child Shan-Yu keeps is a genuine triangle.

**Conclusion of necessity.** By induction on the number of moves, Shan-Yu maintains invariant
$I$ forever. Since $I$ forbids any angle equal to θ (indeed any on-lattice angle), the game
never stops, so Mulan cannot guarantee victory in finitely many steps. This proves: for every
$\theta$ with $\theta\nmid 180$, Shan-Yu wins. In particular this covers **all** $\theta>90$
(if $\theta>90$ then $180/\theta<2$, so $180/\theta\in\{$ integers $\}$ only if $180/\theta=1$,
i.e. $\theta=180$, excluded; hence $\theta\nmid 180$) as well as every $\theta\le 90$ with
$\theta\nmid 180$ (e.g. $40,50,70,25$). $\qquad\blacksquare$ *(necessity)*

### 3. Sufficiency: if θ | 180 then Mulan wins

Let $n := 180/\theta \in \mathbb{Z}$, $n\ge 2$ (since $0<\theta<180$). Then $\theta=180/n\le 90$.
We describe an explicit strategy for Mulan winning in at most $n-1$ moves against any play of
Shan-Yu, from any initial triangle.

If the initial triangle already has an angle equal to θ, the game stops immediately and Mulan
wins. So assume throughout that the current triangle has **no angle equal to θ** (otherwise the
game has already stopped in Mulan's favour). We split into the case $n=2$ ($\theta=90$) and the
case $n\ge 3$ ($\theta\le 60$).

We use two elementary facts. (a) In any triangle the largest angle is $\ge 60$ (three angles
$<60$ would sum to $<180$). (b) In any triangle at most one angle is $\ge 90$ (two angles
$\ge 90$ would sum to $\ge 180$, leaving the third $\le 0$); hence at least two angles are
$<90$ (acute).

#### 3a. Case θ = 90 (n = 2): one-move win by an altitude cut

The current triangle has no $90°$ angle. By fact (b) at least two of its angles are acute; let
$A$ be a vertex chosen so that **its two neighbours' angles are both acute** — concretely, if
some angle is $>90$ (obtuse), take $A$ to be that obtuse vertex, so its two neighbours are the
two acute angles; if all three angles are acute, take $A$ to be any vertex. Write the angle at
$A$ as $\alpha$ and the neighbours as $\beta,\gamma$, with $\beta,\gamma<90$.

Mulan splits vertex $A$ at $x=90-\beta$. This is legal: $x=90-\beta>0$ since $\beta<90$, and
$x<\alpha$ since $\alpha+\beta = 180-\gamma > 90$ (as $\gamma<90$) gives $\alpha>90-\beta=x$. So
$x\in(0,\alpha)$. The children are
$$\text{child}_1=\{x,\beta,180-x-\beta\}=\{90-\beta,\ \beta,\ 90\},$$
$$\text{child}_2=\{\alpha-x,\gamma,x+\beta\}=\{\alpha-90+\beta,\ \gamma,\ 90\}=\{90-\gamma,\ \gamma,\ 90\},$$
where in $\text{child}_2$ we used $\alpha+\beta=180-\gamma$, so $\alpha-90+\beta=90-\gamma>0$.
Both children have an angle equal to $90=\theta$. Whichever child Shan-Yu keeps, the new triangle
has a θ-angle, so the game stops and Mulan wins **in one move**. (Geometrically, $AP$ is the
altitude from $A$; it meets the opposite side in its interior precisely because the two base
angles $\beta,\gamma$ are acute.)

#### 3b. Case θ ≤ 60 (n ≥ 3): plant, then descend

**Step 1 (double plant).** The current triangle has angles $\alpha\ge\beta\ge\gamma>0$ (relabel
so $\alpha$ is the largest). We first note $\alpha>\theta$:
- If $\theta<60$: $\alpha\ge 60>\theta$ by fact (a).
- If $\theta=60$: by fact (a) $\alpha\ge 60$; and $\alpha=60$ would force $\beta+\gamma=120$
  with $\beta,\gamma\le\alpha=60$, hence $\beta=\gamma=60$, an equilateral triangle whose angle
  $60=\theta$ would have already stopped the game. Since the game is continuing, $\alpha>60=\theta$.

Mulan splits the largest vertex (angle $\alpha$; neighbours $\beta,\gamma$) at
$$x = m\theta-\beta,\qquad m := \left\lfloor \beta/\theta\right\rfloor + 1 \in \mathbb{Z}_{\ge 1}.$$
*Legality* $x\in(0,\alpha)$: from $m>\beta/\theta$ we get $m\theta>\beta$, so $x>0$; and
$m = \lfloor\beta/\theta\rfloor+1 \le \beta/\theta+1$ gives $m\theta\le\beta+\theta$, so
$x=m\theta-\beta\le\theta<\alpha$. Hence $x\in(0,\theta]\subset(0,\alpha)$, a legal interior cut.
(This is precisely the statement that the open interval $(\beta/\theta,\ (\alpha+\beta)/\theta)$,
which has length $\alpha/\theta>1$, contains the integer $m=\lfloor\beta/\theta\rfloor+1$;
indeed $\beta/\theta < m \le \beta/\theta+1 < (\alpha+\beta)/\theta$, the last inequality being
$\alpha/\theta>1$.)

Now compute the children's cut-point angles:
- $\text{child}_2$ has angle $x+\beta = m\theta$, a positive multiple of θ with
  $x+\beta\in(0,180)$ (by §1 non-degeneracy). Since $m\theta<\alpha+\beta<180$ we have
  $1\le m\le n-1$; so $x+\beta = m\theta$ is on-lattice.
- $\text{child}_1$ has angle $180-x-\beta = 180-m\theta = (n-m)\theta$, using $\theta\mid 180$
  ($180=n\theta$). This lies in $(0,180)$ (non-degeneracy), and equals $(n-m)\theta$ with
  $1\le n-m\le n-1$; so it is on-lattice too.

Thus **both children contain an on-lattice angle** — this is where $\theta\mid 180$ is used:
the two supplementary cut-point angles $x+\beta$ and $180-x-\beta$ sum to $180\equiv 0\pmod\theta$,
so making one $\equiv 0$ forces the other $\equiv 0$ as well. Whichever child Shan-Yu keeps, the
new triangle has an angle equal to $k\theta$ for some integer $k$ with $1\le k\le n-1$ ($k=m$ or
$k=n-m$).

If $k=1$ this angle equals θ and Mulan has already won. Otherwise $k\ge 2$ and we proceed.

**Step 2 (forced descent).** We prove:

> **Descent Lemma.** If the current triangle has an angle equal to $k\theta$ with integer
> $k\ge 2$, then in one move Mulan either wins outright, or forces the survivor to have an angle
> equal to $(k-1)\theta$.

*Proof.* Let the vertex of angle $k\theta$ have neighbours $\beta',\gamma'$
($k\theta+\beta'+\gamma'=180$). Mulan splits that vertex at $x=\theta$. Legality:
$0<\theta<k\theta$ (as $k\ge 2$), so $x\in(0,k\theta)$. The children are
$$\text{child}_1=\{\theta,\ \beta',\ 180-\theta-\beta'\},\qquad
  \text{child}_2=\{k\theta-\theta,\ \gamma',\ \theta+\beta'\}=\{(k-1)\theta,\ \gamma',\ \theta+\beta'\}.$$
$\text{child}_1$ contains the angle $\theta$: if Shan-Yu keeps it, the game stops and Mulan wins.
Otherwise Shan-Yu keeps $\text{child}_2$, whose angle $(k-1)\theta$ is the claimed on-lattice
angle. Non-degeneracy of $\text{child}_2$: $(k-1)\theta>0$, $\gamma'>0$, and
$\theta+\beta'=180-(k-1)\theta-\gamma'\in(0,180)$; also $180-\theta-\beta'=(k-1)\theta+\gamma'>0$
so $\text{child}_1$ is a genuine triangle and the cut is legal. Either way Mulan's aim is met. ∎

**Termination.** Starting from the angle $k\theta$ ($2\le k\le n-1$) produced in Step 1, apply
the Descent Lemma repeatedly. Each application either ends the game in Mulan's favour, or
strictly decreases the integer multiplier by exactly $1$: $k\theta\to(k-1)\theta\to\cdots$. The
multiplier is a strictly decreasing sequence of integers bounded below by $1$, so after at most
$k-1\le n-2$ applications it reaches multiplier $1$, i.e. an angle equal to $\theta$ — at which
point the game stops and Mulan wins. (The multiplier $m$, resp. $k$, is the required
monovariant; see *Invariants & monovariants*, knowledge_base.md, combinatorics section.)

**Move count.** Mulan wins in at most $1$ (Step 1 plant) $+ (n-2)$ (descent) $= n-1 = 180/\theta-1$
moves — finite, as required. This completes the case $n\ge 3$.

Combining §3a and §3b: whenever $\theta\mid 180$, Mulan guarantees victory in finitely many
moves. $\qquad\blacksquare$ *(sufficiency)*

### 4. Verification of the answer

The two directions §2 and §3 together prove: **Mulan can guarantee victory in finitely many
steps if and only if $\theta\mid 180$**, i.e. iff $\theta=180/n$ for an integer $n\ge 2$. We
verify the answer set explicitly against the required characterization:

- **Winning values** $\theta=180/n$: $n=2\Rightarrow 90$ (won in one altitude move, §3a);
  $n=3\Rightarrow 60$, $n=4\Rightarrow 45$, $n=5\Rightarrow 36$, $n=6\Rightarrow 30$,
  $n=7\Rightarrow 180/7\approx25.71$, $n=8\Rightarrow 22.5$, $n=10\Rightarrow 18$, … each won by
  plant-then-descend (§3b), in at most $n-1$ moves. Sanity example ($\theta=60$, triangle
  $(100,30,50)$): plant at the $100°$ vertex with $\beta=30$, $m=\lfloor30/60\rfloor+1=1$,
  $x=1\cdot60-30=30$; children $\{30,30,120\}$ and $\{70,50,60\}$, both on-lattice
  ($120=2\theta$, $60=\theta$). If Shan-Yu keeps $\{30,30,120\}$, split the $120=2\theta$ vertex
  at $x=60$: child $\{60,30,90\}$ contains $60=\theta$ — win. Matches §3b with $n=3$, $\le 2$ moves.
- **Losing values** $\theta\nmid 180$: all $\theta>90$; and $\theta\le90$ with $\theta\nmid180$,
  e.g. $\theta=40$ ($180/40=4.5$), $50$ ($3.6$), $70$ ($18/7$), $25$ ($7.2$). For each, Shan-Yu
  starts from $(\theta/2,\theta/2,180-\theta)$ and keeps an off-lattice child forever (§2), so no
  angle ever equals θ. (E.g. $\theta=40$: start $(20,20,140)$, all off-lattice.)

This refutes both natural wrong conjectures: "$\theta\le90$ suffices" is false ($\theta=40\le90$
loses), and "$\theta\mid90$" is false ($\theta=60\mid180$ but $60\nmid90$, yet $60$ wins). The
criterion is divisibility of the angle-sum $180$, and §2 case (iv) pinpoints why: $180\equiv0
\pmod\theta$ is the unique arithmetic relation that lets Mulan break the lattice defense. $\qquad\blacksquare$

## Promotable lemmas

**Lattice-covering lemma** (proved in §2, inductive step). *Let $0<\theta<180$ with
$\theta\nmid 180$. If a triangle has angles $\alpha,\beta,\gamma$ with none an integer multiple
of θ, then for every choice of cut vertex (its angle $\alpha$, neighbours $\beta,\gamma$) and
every $x\in(0,\alpha)$, at least one of the two children
$\{x,\beta,180-x-\beta\}$, $\{\alpha-x,\gamma,x+\beta\}$ has all three angles off the lattice
$\theta\mathbb{Z}$.* Proof: the four-case mod-θ exhaustion in §2 (both-children-on-lattice forces
$\alpha\equiv0$, $\beta\equiv0$, $\gamma\equiv0$, or $180\equiv0\pmod\theta$, each contradicting
the hypotheses). Suitable for `lemmas/lattice-covering.md`; imported by angle-sum-anchor and
reduce-to-2theta.

**Supplementary-plant lemma** (proved in §3b, Step 1). *If $\theta\mid 180$ and a triangle has a
vertex of angle $\alpha>\theta$ with a neighbour $\beta$, then the cut $x=(\lfloor\beta/\theta
\rfloor+1)\theta-\beta\in(0,\theta]\subset(0,\alpha)$ makes both children carry a positive
integer multiple of θ (namely $x+\beta=m\theta$ and $180-x-\beta=(n-m)\theta$, $n=180/\theta$).*

**Descent lemma** (proved in §3b, Step 2). *If a triangle has an angle $k\theta$, $k\ge2$
integer, the cut $x=\theta$ at that vertex either wins immediately or forces a survivor with
angle $(k-1)\theta$; iterating reaches angle θ in $\le k-1$ moves.*
