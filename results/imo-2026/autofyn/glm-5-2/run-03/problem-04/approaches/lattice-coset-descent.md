# IMO 2026 P4 — Mulan's Triangle Game (approach: lattice-coset-descent)

## Status
solved

## Approaches tried
- lattice-coset-descent (round 1, new) — full characterization, both directions. Necessity via the four-coset intersection lemma (closure of the safe complement of $L_\theta$); sufficiency via the max-angle lattice-point entry cut + index-$k$ descent. All sub-lemmas proved in full, all cases settled (incl. $n=2$ / $\theta=90°$ and the equilateral gap the reviewer flagged). Outcome: complete. (Prior: none.)

## Current best
Complete rigorous proof of the characterization $\theta = 180°/n$ for an integer $n\ge 2$. No open gaps.

## Full proof

**Theorem (answer).** *Mulan can guarantee victory in finitely many steps, regardless of how Shan-Yu plays, if and only if $\theta = 180°/n$ for some integer $n\ge 2$.*

Throughout, angles are measured in degrees and "$\theta\mathbb Z_{>0}$" denotes the set of *positive* integer multiples $\{\theta,2\theta,3\theta,\dots\}$ of $\theta$ (the value $0$ is never an angle, so it is excluded). We write $\mathbb Z$ for the integers and $\mathbb Z_{>0}$ for the positive integers.

---

### 1. Reduction to the angle game

The only data of the current triangle $\mathcal T$ that any move can affect or reveal is its **angle triple** $(a,b,c)$ with $a+b+c=180°$ and $a,b,c>0$; the side lengths are irrelevant to whether some angle equals $\theta$ and to the angles of either child produced by a straight cut. Hence the game is entirely played on the set
$$\mathcal S=\{(a,b,c):a,b,c>0,\;a+b+c=180°\}.$$

**Cut-geometry lemma.** *In a triangle $\triangle ABC$ with $\angle A=a,\angle B=b,\angle C=c$, Mulan may choose to cut to vertex $A$ by selecting a point $P$ on side $BC$ (not a vertex); the cut $AP$ splits $\triangle ABC$ into two triangles whose angle triples are*
$$\triangle ABP:\;(x,\;b,\;a+c-x),\qquad \triangle ACP:\;(a-x,\;c,\;b+x),$$
*where $x=\angle BAP\in(0,a)$. Conversely every $x\in(0,a)$ is realizable.*

*Proof.* Write the two sub-angles at $A$ as $\angle BAP=x$ and $\angle PAC=a-x$ with $0<x<a$. In $\triangle ABP$ the angles are $x$ (at $A$), $b$ (at $B$, since $P\in BC$ so $\angle ABP=\angle ABC=b$), and $180°-b-x=a+c-x$ (at $P$). In $\triangle ACP$ the angles are $a-x$ (at $A$), $c$ (at $C$), and $180°-c-(a-x)=b+x$ (at $P$). The two angles at $P$ sum to $(a+c-x)+(b+x)=180°$, as they must (they are supplementary at the straight cut). As $P$ moves along $BC$ from $B$ to $C$, the ray $AP$ rotates continuously, so $x=\angle BAP$ is a continuous function of the position of $P$ taking all values in $(0,a)$ (intermediate value theorem, applied between the limiting values $0$ and $a$). ∎

By relabeling the triangle, Mulan may cut to *any* of the three vertices; the formula above, with $(a,b,c)$ relabeled, covers all cases. Without loss of generality we always describe a cut "to vertex $A$" with parameter $x\in(0,a)$.

**Winning condition.** Mulan wins exactly when the current angle triple contains $\theta$. Since $\theta\in\theta\mathbb Z_{>0}$, every winning state lies in the set $L_\theta$ defined next.

---

### 2. The lattice $L_\theta$ and the safe complement

Define
$$L_\theta=\{(a,b,c)\in\mathcal S:\text{some one of }a,b,c\text{ lies in }\theta\mathbb Z_{>0}\}.$$
Call a state **safe** (for Shan-Yu) if it is *not* in $L_\theta$, i.e. none of its three angles is a positive multiple of $\theta$. Because $\theta$ itself is a positive multiple of $\theta$, every winning state lies in $L_\theta$; in particular a safe state has no angle equal to $\theta$, so **Mulan has not won from a safe state**.

---

### 3. NECESSITY — the four-coset intersection lemma

> **Lemma A (four-coset intersection / closure of the safe set).** *Let $(a,b,c)\in\mathcal S$ be safe (so $a,b,c\notin\theta\mathbb Z_{>0}$). Suppose $180°\notin\theta\mathbb Z_{>0}$ (equivalently $\theta\neq 180°/n$ for every integer $n\ge 2$). Then for every vertex at which Mulan cuts and every parameter $x$ in the legal range, **at least one of the two children is again safe** (i.e. lies outside $L_\theta$).*

*Proof.* By relabeling we may assume the cut is to vertex $A$ with parameter $x\in(0,a)$, producing
$$C_1=(x,\;b,\;a+c-x),\qquad C_2=(a-x,\;c,\;b+x).$$
(All six entries are positive: $x>0$, $a-x>0$, $b,c>0$ by hypothesis; $a+c-x>c>0$ since $x<a$; $b+x>0$.)

We show that it is **impossible** for both $C_1$ and $C_2$ to lie in $L_\theta$. Because $(a,b,c)$ is safe, $b\notin\theta\mathbb Z_{>0}$ and $c\notin\theta\mathbb Z_{>0}$, so:
- $C_1\in L_\theta$ iff $x\in\theta\mathbb Z_{>0}$ **or** $a+c-x\in\theta\mathbb Z_{>0}$ (the middle entry $b$ is not a multiple);
- $C_2\in L_\theta$ iff $a-x\in\theta\mathbb Z_{>0}$ **or** $b+x\in\theta\mathbb Z_{>0}$ (the middle entry $c$ is not a multiple).

So "$C_1\in L_\theta$ **and** $C_2\in L_\theta$" is a conjunction of two two-term disjunctions, hence is the disjunction of exactly four pairwise conjunctions. We settle each.

**(i)** $x\in\theta\mathbb Z_{>0}$ and $a-x\in\theta\mathbb Z_{>0}$. Then $x=m\theta$ and $a-x=p\theta$ for some $m,p\in\mathbb Z_{>0}$, giving $a=(m+p)\theta\in\theta\mathbb Z_{>0}$, contradicting that $a$ is safe.

**(ii)** $x\in\theta\mathbb Z_{>0}$ and $b+x\in\theta\mathbb Z_{>0}$. Then $x=m\theta$ and $b+x=p\theta$ for $m,p\in\mathbb Z_{>0}$. Since $b+x>x$ (because $b>0$), we have $p\theta>m\theta$, hence $p>m$, i.e. $p-m\ge 1$, and $b=(p-m)\theta\in\theta\mathbb Z_{>0}$, contradicting that $b$ is safe.

**(iii)** $a+c-x\in\theta\mathbb Z_{>0}$ and $a-x\in\theta\mathbb Z_{>0}$. Then $a+c-x=m\theta$ and $a-x=p\theta$ for $m,p\in\mathbb Z_{>0}$. Since $a+c-x>a-x$ (because $c>0$), we have $m>p$, hence $m-p\ge 1$, and $(a+c-x)-(a-x)=c=(m-p)\theta\in\theta\mathbb Z_{>0}$, contradicting that $c$ is safe.

**(iv)** $a+c-x\in\theta\mathbb Z_{>0}$ and $b+x\in\theta\mathbb Z_{>0}$. Then $a+c-x=m\theta$ and $b+x=p\theta$ for $m,p\in\mathbb Z_{>0}$. Adding,
$$(a+c-x)+(b+x)=a+b+c=180°=(m+p)\theta,$$
so $180°\in\theta\mathbb Z_{>0}$, i.e. $\theta=180°/n$ for $n=m+p\ge 2$. This contradicts the hypothesis $180°\notin\theta\mathbb Z_{>0}$.

The four cases (i)–(iv) exhaust the conjunction of the two disjunctions (a $2\times 2$ expansion yields exactly these four term-pairs, and they are exhaustive: every witness of "$C_1\in L_\theta$ and $C_2\in L_\theta$" falls under one of the four). Each leads to a contradiction. Hence **no** choice of vertex and parameter makes both children land in $L_\theta$; at least one child is safe. ∎

> **Corollary (Shan-Yu's defense — necessity).** *If $\theta\neq 180°/n$ for every integer $n\ge 2$, Shan-Yu has a strategy that prevents Mulan from ever winning: open with the equilateral triangle and, after every Mulan cut, keep a safe child.*

*Proof.* Assume $\theta\neq 180°/n$, so $180°\notin\theta\mathbb Z_{>0}$.

**The equilateral $(60°,60°,60°)$ is safe.** If $60°\in\theta\mathbb Z_{>0}$, then $60°=m\theta$ for some $m\in\mathbb Z_{>0}$, giving $180°=3\cdot 60°=3m\theta\in\theta\mathbb Z_{>0}$, contradicting $\theta\neq 180°/n$. So $60°\notin\theta\mathbb Z_{>0}$, and the equilateral is safe.

**Inductive invariant.** Shan-Yu maintains: the current state is safe. Initially true (equilateral). Suppose the current state is safe. By Lemma A, whatever Mulan does, at least one child is safe; Shan-Yu keeps such a child. The new state is safe. By induction the state is safe forever. Since every safe state lies outside $L_\theta$ and hence has no angle equal to $\theta$ (as $\theta\in\theta\mathbb Z_{>0}\subseteq L_\theta$), Mulan never wins. ∎

This establishes the **necessity** direction: if $\theta$ is not of the form $180°/n$, Mulan cannot guarantee victory.

---

### 4. SUFFICIENCY — entering $L_\theta$ in one move (the lattice-point entry cut)

Assume henceforth $\theta=180°/n$ for an integer $n\ge 2$, so that $180°=n\theta\in\theta\mathbb Z_{>0}$.

> **Lemma B (lattice-point-in-open-interval).** *Let $(a,b,c)\in\mathcal S$ be a state with no angle a positive multiple of $\theta$ (i.e. a Phase-1 state). Relabel so that $A\ge B\ge C$ are the three angles in non-increasing order. Then there exists an integer $k$ with $1\le k\le n-1$ such that $k\theta\in(C,\,A+C)$ (open interval).*

*Proof.* We split on $n$.

**Case $n\ge 3$ (so $\theta\le 60°$).** Since $A$ is the maximum of three positive angles summing to $180°$, we have $A\ge 60°$. We first claim $A>\theta$ (strictly). Suppose for contradiction $A\le\theta$; then every angle is $\le\theta$ and, being a non-multiple of $\theta$ (Phase-1 hypothesis), each angle is $<\theta$. Hence $180°=a+b+c<3\theta$, giving $n\theta<3\theta$, i.e. $n<3$, contradicting $n\ge 3$. So $A>\theta$.

The interval $(C,\,A+C)$ has length $A>\theta$. We claim it contains a positive multiple of $\theta$. Since $C$ is *not* a multiple of $\theta$ (Phase-1 hypothesis), $C/\theta\notin\mathbb Z$; let $m=\lceil C/\theta\rceil$, the least integer $\ge C/\theta$. Then $m\ge 1$ (as $C>0$) and $m\theta>C$ (strictly, because $C$ is not a multiple). Also $m\theta\le C+\theta<C+A=A+C$ (using $\theta<A$). Thus $m\theta\in(C,A+C)$, and we take $k=m$. Finally $k\theta<A+C<180°=n\theta$ gives $k<n$, i.e. $k\le n-1$. ∎ (case $n\ge 3$)

**Case $n=2$ (so $\theta=90°$).** The only positive multiple of $\theta=90°$ below $180°$ is $90°$ itself (i.e. $k=1$). We must show $90°\in(C,\,A+C)$, i.e. $C<90°<A+C=180°-B$.

- *$C<90°$:* at most one angle of a triangle can be $\ge 90°$ (two would sum to $\ge 180°$, leaving the third $\le 0°$); since $C$ is the *minimum*, $C<90°$.
- *$90°<A+C$, i.e. $B<90°$:* if $B\ge 90°$, then $A\ge B\ge 90°$ (as $A\ge B$), so $A+B\ge 180°$, forcing $C\le 0°$, impossible. So $B<90°$.

Hence $90°\in(C,A+C)$, i.e. $k=1$ works. (Note this also covers the **equilateral** $(60°,60°,60°)$, which is a Phase-1 state for $n=2$: here $C=60°<90°<A+C=120°$. The bound "$A\ge 90°$" is not needed and is in fact false here; the direct $C<90°<A+C$ argument is what replaces it.) ∎ (case $n=2$)

> **Corollary C (Phase-1 entry).** *From any Phase-1 state $(a,b,c)$ (no angle a multiple of $\theta$), Mulan can force **both** children into $L_\theta$ in one move.*

*Proof.* Relabel with $A\ge B\ge C$. By Lemma B pick $k\in\{1,\dots,n-1\}$ with $k\theta\in(C,A+C)$, and set $x=A+C-k\theta$. The inequalities $C<k\theta<A+C$ give $0<x<A$, so this is a legal cut at vertex $A$. The cut-geometry lemma produces
$$C_1=(x,\;B,\;A+C-x),\qquad C_2=(A-x,\;C,\;B+x).$$
Compute the third angles using $A+B+C=180°=n\theta$:
- $C_1$'s third angle $=A+C-x=A+C-(A+C-k\theta)=k\theta\in\theta\mathbb Z_{>0}$, so $C_1\in L_\theta$;
- $C_2$'s third angle $=B+x=B+A+C-k\theta=180°-k\theta=(n-k)\theta\in\theta\mathbb Z_{>0}$ (and $n-k\ge 1$ since $k\le n-1$), so $C_2\in L_\theta$.

Both children lie in $L_\theta$, regardless of which one Shan-Yu discards. ∎

---

### 5. SUFFICIENCY — the index-$k$ descent within $L_\theta$

> **Lemma D (forced descent).** *Suppose the current state has an angle equal to $j\theta$ for some $j\in\{2,\dots,n-1\}$, the other two angles being $b,c$ (so $j\theta+b+c=180°$). Mulan can play so that Shan-Yu is forced to hand her a new state with an angle $(j-1)\theta$.*

*Proof.* Mulan cuts to the vertex carrying angle $j\theta$ with parameter $x=\theta$. This is legal since $0<\theta<j\theta$ (as $j\ge 2$). The cut-geometry lemma (with $a=j\theta$, $b,c$ the other angles) gives
$$C_1=(\theta,\;b,\;j\theta+c-\theta)=(\theta,\;b,\;(j-1)\theta+c),$$
$$C_2=(j\theta-\theta,\;c,\;b+\theta)=((j-1)\theta,\;c,\;b+\theta).$$
$C_1$ contains the angle $\theta$: if Shan-Yu keeps $C_1$, the game stops and Mulan wins. To postpone defeat Shan-Yu must keep $C_2$. Verify $C_2$ is a valid triangle: all three entries are positive — $(j-1)\theta>0$ (as $j\ge 2$), $c>0$, $b+\theta>0$ — and their sum is $(j-1)\theta+c+b+\theta=j\theta+b+c=180°$. So $C_2$ is the forced new state, and it carries the angle $(j-1)\theta$. ∎

> **Corollary E (Mulan's win from any state when $\theta=180°/n$).** *If $\theta=180°/n$, $n\ge 2$, Mulan wins in at most $n-1$ moves from any state.*

*Proof.* From the current state:

- *If some angle equals $\theta$:* Mulan has already won (0 further moves).
- *If some angle equals $j\theta$ for $j\in\{2,\dots,n-1\}$* (a positive multiple of $\theta$ but not $\theta$ itself): skip Phase 1; apply Lemma D repeatedly. The index $j$ drops by $1$ each forced move: $j\to j-1\to\dots\to 1$. After $j-1\le n-2$ moves the index reaches $1$, i.e. an angle $\theta$ appears; the game stops.
- *If no angle is a positive multiple of $\theta$* (a Phase-1 state): play Corollary C first (1 move), after which **both** children lie in $L_\theta$. Whichever Shan-Yu keeps, the new state carries an angle $j\theta$ with $1\le j\le n-1$. If $j=1$ we are done (total 1 move); if $j\ge 2$ apply the descent of Lemma D, terminating in at most $j-1\le n-2$ more moves.

Total move count in the worst case: $1$ (entry) $+\;(n-2)$ (descent) $=\;n-1$. ∎

This establishes **sufficiency**: for every $\theta=180°/n$, $n\ge 2$, Mulan guarantees victory in finitely many (indeed $\le n-1$) moves.

---

### 6. Sharpness of the move bound and conclusion

The bound $n-1$ is tight in the worst case: for $n=2$ ($\theta=90°$) the strategy always takes exactly $1=n-1$ move from a $\theta$-free state (both children receive a $90°$ angle), and one verifies that no $0$-move win is possible from a triangle with no $90°$ angle.

Combining the two directions:

- **Necessity** (Section 3, Lemma A + Corollary): if $\theta\neq 180°/n$ for every integer $n\ge 2$, Shan-Yu opens equilateral and maintains a safe state forever, so Mulan cannot guarantee a win.
- **Sufficiency** (Sections 4–5, Lemmas B, D + Corollaries C, E): if $\theta=180°/n$ for an integer $n\ge 2$, Mulan wins in at most $n-1$ moves from any opening, regardless of Shan-Yu's play.

Therefore **Mulan can guarantee her victory in finitely many steps if and only if $\theta=\dfrac{180°}{n}$ for some integer $n\ge 2$**. ∎

---

## Promotable lemmas

The following three lemmas are proved in full above and are reusable by any other approach to this problem (or any problem reducing to the same angle game):

1. **Cut-geometry lemma** (Section 1). Cutting to the vertex of angle $a$ with parameter $x\in(0,a)$ produces children $(x,b,a+c-x)$ and $(a-x,c,b+x)$; every $x\in(0,a)$ is realizable. *Location:* Section 1 of this file.

2. **Four-coset intersection / closure-of-safe-set lemma (Lemma A)** (Section 3). If a state is safe (no angle a positive multiple of $\theta$) and $180°\notin\theta\mathbb Z_{>0}$, then no cut can put both children in $L_\theta$; at least one child remains safe. Proved by exhaustive $2\times 2$ case analysis. *Location:* Section 3 of this file.

3. **Lattice-point entry + index-$k$ descent (Lemmas B, D + Corollaries C, E)** (Sections 4–5). When $\theta=180°/n$, from any state Mulan enters $L_\theta$ in one move (max-angle lattice-point cut) and then forces a descent of the multiple index $j\to j-1$ by cutting the $j\theta$-vertex with parameter $\theta$; total $\le n-1$ moves. *Location:* Sections 4–5 of this file.
