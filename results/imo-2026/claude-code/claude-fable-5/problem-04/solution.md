# Problem 4 — Solution

*Written: 2026-07-22 15:39 PDT (Claude Fable 5). Analysis performed 2026-07-22 15:22–15:38 PDT; exact computational verification runs performed 15:26–15:37 PDT; see the companion file `problem4_verification.md`.*

## Statement

Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$
known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal T$ with measurements of
his choice. Then, they repeatedly perform the following steps: If $\mathcal T$ has at least one
angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a
point $P$ on the perimeter of $\mathcal T$, different from its three vertices. She then makes a
straight cut from $P$ to the opposite vertex of $\mathcal T$, splitting it into two triangles.
Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal T$.
For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no
matter how Shan-Yu plays?

---

## Answer

$$
\boxed{\ \theta=\frac{180^\circ}{n}\ \text{ for some integer } n\ge 2\ }
$$

i.e. Mulan can guarantee victory **exactly when $180^\circ/\theta$ is an integer**
($\theta\in\{90^\circ,\,60^\circ,\,45^\circ,\,36^\circ,\,30^\circ,\,\tfrac{180}{7}^\circ,\dots\}$).
For every other $\theta\in(0^\circ,180^\circ)$, Shan-Yu can keep the game going forever.

---

## Overview of the proof

Only the angles of $\mathcal T$ matter, so we model a triangle by its unordered triple of positive
angles summing to $180^\circ$, and we first show (Setup) that a move consists of: Mulan picks one
angle $\alpha$ of the triple and a real $x\in(0,\alpha)$; the two pieces are then
$(x,\beta,180-\beta-x)$ and $(\alpha-x,\gamma,\beta+x)$, and Shan-Yu keeps one of them.

*Mulan's side* ($\theta=180/n$): Lemma 1 shows that any triangle containing an angle equal to a
positive multiple $k\theta$ is lost for Shan-Yu — Mulan slices off an angle $\theta$ at that
vertex, leaving pieces containing $\theta$ and $(k-1)\theta$ respectively, and descends. Lemma 2
shows that from **any** triangle, Mulan has a single cut after which **both** pieces contain a
positive multiple of $\theta$; the key point is a counting inequality
$\lfloor\beta/\theta\rfloor+\lfloor\gamma/\theta\rfloor\le n-2$ made possible precisely because
$180=n\theta$.

*Shan-Yu's side* ($180/\theta\notin\mathbb Z$): the set $\mathcal N$ of triangles **none of whose
angles is a positive multiple of $\theta$** is nonempty, contains no stopping position, and is
*closed*: Lemma 3 shows that for every possible cut, at least one of the two pieces again lies in
$\mathcal N$. The single place where $180\not\equiv0\pmod\theta$ is used is the new angle
$\beta+x$ at the cut point, whose value modulo $\theta$ is $180$ minus that of its supplementary
partner. Shan-Yu simply always keeps a piece in $\mathcal N$ and never loses.

All angles below are measured in degrees.

---

## Setup — the game on angle triples

Let $\mathcal T=ABC$ have angles $\alpha,\beta,\gamma$ at $A,B,C$. If Mulan picks $P$ in the
interior of side $BC$, the cut is the segment $PA$, and it splits the angle at $A$ into two parts
$x=\angle BAP$ and $\alpha-x=\angle PAC$. As $P$ runs over the interior of segment $BC$, the ray
$AP$ sweeps the interior of angle $A$, so $x$ takes every value in the open interval $(0,\alpha)$,
and every such $x$ is realized by exactly one choice of $P$. The two pieces are the triangles
$ABP$ and $APC$, with angle triples
$$
T_1=(x,\ \beta,\ 180-\beta-x),\qquad
T_2=(\alpha-x,\ \gamma,\ \beta+x),
\tag{$\ast$}
$$
where the angle of $T_2$ at $P$ is $180-\gamma-(\alpha-x)=\beta+x$ because
$\alpha+\beta+\gamma=180$. (The two angles at $P$ are supplementary:
$(180-\beta-x)+(\beta+x)=180$.) All six listed angles are strictly positive, so both pieces are
genuine triangles.

Thus the game is equivalently: the state is an unordered triple of positive reals summing to
$180$; if the state contains $\theta$, Mulan has won; otherwise Mulan chooses which entry
$\alpha$ to *destroy* and a value $x\in(0,\alpha)$, and Shan-Yu replaces the state by $T_1$ or
$T_2$ from $(\ast)$. (Swapping the roles of $\beta$ and $\gamma$ in $(\ast)$ and replacing $x$
by $\alpha-x$ exchanges $T_1\leftrightarrow T_2$, so the labelling of $\beta,\gamma$ is
immaterial.)

---

## Part 1 — If $\theta=180/n$ for an integer $n\ge2$, Mulan wins

**Lemma 1.** *Let $k\ge1$ be an integer with $k\theta<180$. From any triangle having an angle
equal to $k\theta$, Mulan wins in at most $k-1$ cuts.*

*Proof.* Induction on $k$. If $k=1$ the triangle has an angle $\theta$, so the game has already
stopped with Mulan the winner ($0$ cuts). Let $k\ge2$ and let the triangle be $(k\theta,\beta,\gamma)$.
If it contains an angle $\theta$ we are done; otherwise Mulan cuts the vertex with angle
$k\theta$ using $x=\theta\in(0,k\theta)$. By $(\ast)$ the pieces are
$$
T_1=(\theta,\ \beta,\ 180-\beta-\theta),\qquad
T_2=\big((k-1)\theta,\ \gamma,\ \beta+\theta\big).
$$
If Shan-Yu keeps $T_1$, it has an angle exactly $\theta$ and the game stops with Mulan winning.
If he keeps $T_2$, it contains the angle $(k-1)\theta$, where $1\le k-1$ and $(k-1)\theta<180$,
so by the induction hypothesis Mulan wins in at most $k-2$ further cuts; in total at most $k-1$.
$\blacksquare$

**Lemma 2.** *Let $\theta=180/n$ with $n\ge2$ an integer. From any triangle whatsoever, Mulan
wins in at most $n-1$ cuts.*

*Proof.* Let the triangle be $(\alpha,\beta,\gamma)$. Every angle is $<180=n\theta$, so if some
angle is a positive multiple of $\theta$ it equals $k\theta$ with $1\le k\le n-1$, and Lemma 1
finishes in at most $n-2$ cuts. So assume no angle lies in $\theta\mathbb Z$, and label the
triple so that $\alpha$ is a **largest** angle. Put
$$
b=\left\lfloor\beta/\theta\right\rfloor,\qquad c=\left\lfloor\gamma/\theta\right\rfloor,
$$
so that, strictly (since $\beta,\gamma\notin\theta\mathbb Z$),
$$
b\theta<\beta<(b+1)\theta,\qquad c\theta<\gamma<(c+1)\theta.
\tag{2.1}
$$

*Claim: $b+c\le n-2$.*
If $n\ge3$, then $\theta\le60\le\alpha$ (a largest angle of a triangle is $\ge60$), and
$\alpha\ne\theta$ since no angle is a multiple; hence $\alpha>\theta$ and
$\lfloor\alpha/\theta\rfloor\ge1$. Summing the strict lower bounds in (2.1) together with
$\alpha>\lfloor\alpha/\theta\rfloor\,\theta$ gives
$180=\alpha+\beta+\gamma>\big(\lfloor\alpha/\theta\rfloor+b+c\big)\theta$, i.e.
$\lfloor\alpha/\theta\rfloor+b+c\le n-1$, whence $b+c\le n-2$.
If $n=2$ (so $\theta=90$): since $\alpha$ is largest, $\beta\le\alpha$ and $\alpha+\beta<180$
force $\beta<90$, and likewise $\gamma<90$; hence $b=c=0=n-2$. ∎(claim)

Now set $k=b+1$. Then $k\ge1$ and $n-k\ge c+1\ge1$ (so also $k\le n-1$). Mulan cuts the vertex
with angle $\alpha$ using
$$
x=k\theta-\beta.
$$
This is a legal cut: $x>0$ by the right inequality of (2.1); and $x<\alpha$ because
$$
x<\alpha
\iff k\theta<\alpha+\beta=180-\gamma
\iff \gamma<(n-k)\theta,
$$
which holds since $\gamma<(c+1)\theta\le(n-k)\theta$ by (2.1) and $n-k\ge c+1$. By $(\ast)$ the
two pieces are
$$
T_1=\big(k\theta-\beta,\ \beta,\ 180-k\theta\big)=\big(k\theta-\beta,\ \beta,\ (n-k)\theta\big),
\qquad
T_2=\big(\alpha+\beta-k\theta,\ \gamma,\ k\theta\big).
$$
$T_1$ contains the angle $(n-k)\theta$ and $T_2$ contains the angle $k\theta$, with
$1\le k,\,n-k\le n-1$, so both are positive multiples of $\theta$ smaller than $180$. Whichever
piece Shan-Yu keeps, Lemma 1 lets Mulan win in at most $\max(k,n-k)-1\le n-2$ further cuts;
in total at most $n-1$ cuts. $\blacksquare$

For $\theta=90^\circ$ ($n=2$) Mulan's cut in Lemma 2 is the classical one: $x=90-\beta$ means
$P$ is the foot of the altitude from the largest angle, and both pieces are right triangles.

---

## Part 2 — If $180/\theta$ is not an integer, Shan-Yu wins

Throughout this part, congruences are modulo the subgroup
$\theta\mathbb Z=\{k\theta:k\in\mathbb Z\}$ of $(\mathbb R,+)$; note that for a number
$a\in(0,180)$, $a\equiv0\pmod\theta$ if and only if $a$ is a *positive* multiple of $\theta$.
The hypothesis $180/\theta\notin\mathbb Z$ says exactly
$$
180\not\equiv0\pmod\theta.
\tag{3.0}
$$

Let
$$
\mathcal N=\Big\{(\alpha,\beta,\gamma)\ :\ \alpha,\beta,\gamma>0,\ \alpha+\beta+\gamma=180,\
\alpha,\beta,\gamma\not\equiv0\ (\mathrm{mod}\ \theta)\Big\}.
$$
Since $\theta\in\theta\mathbb Z$, **no triangle in $\mathcal N$ has an angle equal to $\theta$**;
in particular the game never stops while the current triangle lies in $\mathcal N$.

**Existence of a starting triangle in $\mathcal N$.** Only finitely many values in $(0,180)$ are
multiples of $\theta$. Choose $\alpha\in(0,60)$ with $\alpha\not\equiv0$; then choose
$\beta\in(60,120)$ avoiding the finitely many values with $\beta\equiv0$ or
$180-\alpha-\beta\equiv0$ — an uncountable interval minus a finite set is nonempty. Then
$\gamma=180-\alpha-\beta\in(0,120)$ and $(\alpha,\beta,\gamma)\in\mathcal N$.

**Lemma 3 (closure of $\mathcal N$).** *Let $(\alpha,\beta,\gamma)\in\mathcal N$ and consider an
arbitrary cut: an arbitrary destroyed angle — by the symmetry noted in the Setup we may write it
as $\alpha$, with $\beta$ the kept angle of $T_1$ and $\gamma$ the kept angle of $T_2$ — and an
arbitrary $x\in(0,\alpha)$, producing by $(\ast)$*
$$
T_1=(x,\ \beta,\ 180-\beta-x),\qquad T_2=(\alpha-x,\ \gamma,\ \beta+x).
$$
*Then $T_1\in\mathcal N$ or $T_2\in\mathcal N$.*

*Proof.* Suppose $T_1\notin\mathcal N$, i.e. one of its three angles is $\equiv0\pmod\theta$.
Since $\beta\not\equiv0$, either $x\equiv0$ or $180-\beta-x\equiv0$, i.e.
$$
x\equiv0
\qquad\text{or}\qquad
x\equiv180-\beta \pmod\theta .
$$

*Case $x\equiv0$.* The angles of $T_2$ satisfy
$$
\alpha-x\equiv\alpha\not\equiv0,\qquad
\gamma\not\equiv0,\qquad
\beta+x\equiv\beta\not\equiv0,
$$
so $T_2\in\mathcal N$.

*Case $x\equiv180-\beta$.* Using $\alpha+\beta+\gamma=180$,
$$
\alpha-x\equiv\alpha-(180-\beta)=-\gamma\not\equiv0,\qquad
\gamma\not\equiv0,\qquad
\beta+x\equiv180\not\equiv0,
$$
where $-\gamma\not\equiv0$ because $\gamma\not\equiv0$ ($\theta\mathbb Z$ is a subgroup), and the
last non-congruence is exactly (3.0). So $T_2\in\mathcal N$. $\blacksquare$

**Shan-Yu's strategy.** Start with any triangle in $\mathcal N$. After each of Mulan's cuts, keep
a piece lying in $\mathcal N$; this is always possible by Lemma 3. By induction, the triangle on
the table lies in $\mathcal N$ after every round, hence never has an angle equal to $\theta$, and
the game continues forever. Mulan cannot win — in finitely many steps or at all. $\blacksquare$

---

## Conclusion

If $\theta=180^\circ/n$ for an integer $n\ge2$, Lemma 2 gives Mulan a strategy winning in at most
$n-1$ cuts from any initial triangle. If $180^\circ/\theta$ is not an integer, Part 2 gives
Shan-Yu an initial triangle and a discarding rule under which the game never stops. Hence Mulan
can guarantee victory in finitely many steps **exactly for**
$$
\theta=\frac{180^\circ}{n},\qquad n\in\{2,3,4,\dots\}. \qquad\blacksquare
$$

---

## Remarks

1. **Where the divisibility is used.** Mulan's side uses $180=n\theta$ only in the claim
   $b+c\le n-2$ of Lemma 2, which guarantees the "double-threat" cut $x=k\theta-\beta$ is legal
   and both pieces catch a multiple of $\theta$. Shan-Yu's side uses $180\not\equiv0\pmod\theta$
   only for the new angle $\beta+x$ in the second case of Lemma 3 — if $\theta$ divided $180$,
   the value $\beta+x\equiv180\equiv0$ would be a multiple of $\theta$ and the invariant would
   break, which is precisely the door Mulan walks through in Lemma 2.

2. **Why "avoid $\theta$" must be strengthened to "avoid all multiples of $\theta$".** The naive
   invariant "no angle equals $\theta$" is not closed: from an angle $2\theta$, Mulan's cut
   $x=\theta$ puts an angle $\theta$ in *both* pieces (this is Lemma 1 with $k=2$). The set
   $\mathcal N$ is the exact closure of the losing positions' complement: for $180/\theta\notin
   \mathbb Z$, one can show Mulan's winning set is *exactly* the set of triangles containing a
   positive multiple of $\theta$ (verified exhaustively for all rational instances with
   denominator $\le 52$ in the companion file).

3. **Obtuse $\theta$.** For $\theta>90^\circ$ the answer is "Shan-Yu wins", consistent with
   $180/\theta\in(1,2)$ never being an integer; the residue strategy covers this case
   uniformly. (A simpler ad-hoc invariant also works there: keep all angles $<\theta$; of the
   two supplementary new angles at $P$, at most one is $\ge\theta$.)

4. **Sharpness of the step bound.** Mulan's $n-1$ cuts in Lemma 2 are achieved through a chain
   $k\theta\to(k-1)\theta\to\dots$; no attempt is made here to optimize the number of cuts, only
   to show it is finite and uniformly bounded.
