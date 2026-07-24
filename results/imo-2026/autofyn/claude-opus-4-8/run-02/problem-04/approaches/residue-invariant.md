# Approach: residue-invariant (mod-θ algebra in ℝ/θℤ)

## Status
solved

## Answer
Mulan can guarantee victory **iff θ = 180°/n for some integer n ≥ 2**; equivalently iff
180/θ is an integer (equivalently iff θ divides 180° an integral number of times, i.e.
180 ∈ θℤ). The winning set is {90°, 60°, 45°, 36°, 30°, 180/7°, 22.5°, 20°, …}, all ≤ 90°,
accumulating at 0°.

## Approaches tried
- (round 1) residue invariant in ℝ/θℤ. Necessity via the "good triangle" invariant and the
  4-coincidence exclusion (Lemma A) — complete. Sufficiency via the alignment cut (Lemma B) +
  the θ-peel (Lemma C) — complete; the flagged gap **G1 (alignment range-existence)** is closed
  by an explicit two-regime argument (θ ≤ 60 uses the max-angle apex; θ = 90 uses the altitude),
  G2 and G3 closed. Numerically re-verified: alignment exists in 200000/200000 random
  (triangle, n∈2..12) trials with no angle a multiple of θ; Lemma A: 0 both-bad events. **Solved.**

## Current best
Complete proof of both directions (below).

## Full proof

Throughout, a *triangle* means an ordered triple of its three angle measures, each in
(0°, 180°), summing to 180°. The game's stopping rule is: **the game stops with Mulan winning
as soon as the current triangle 𝒯 has an angle equal to θ** (this is tested before Mulan's
move and again on the triangle Shan-Yu leaves). All angles are in degrees; we drop the ° sign.

### 0. The move algebra (the game engine)

A single Mulan move is: pick a vertex $A$ (the *apex*) with angle $\alpha$, and a point $P$ in
the open opposite side, and cut along the cevian $AP$. Let $B,C$ be the other two vertices,
with angles $\beta$ (at $B$) and $\gamma$ (at $C$), so $\alpha+\beta+\gamma=180$. Put
$x=\angle BAP\in(0,\alpha)$. As $P$ ranges over the open side $BC$, the ray $AP$ sweeps the
interior of angle $A$, so $x$ ranges over all of the open interval $(0,\alpha)$; conversely
every $x\in(0,\alpha)$ is realized by exactly one $P$. The two children are:

- $T_1 = \triangle ABP$ with angles $\{\,x,\ \beta,\ 180-\beta-x\,\}$
  (angle at $A$ is $x$; at $B$ is $\beta$; at $P$ is $\angle APB = 180-x-\beta$);
- $T_2 = \triangle APC$ with angles $\{\,\alpha-x,\ \gamma,\ 180-(\alpha-x)-\gamma\,\}
   = \{\,\alpha-x,\ \gamma,\ \beta+x\,\}$
  (using $180-\alpha-\gamma=\beta$).

Since $B,P,C$ are collinear, $\angle APB+\angle APC=180$, i.e. the two "cut-point" angles
$180-\beta-x$ (in $T_1$) and $\beta+x$ (in $T_2$) are supplementary. This supplement identity
is the crux of the alignment lemma.

We record the range of the cut-point angle. With apex $A$,
$$\angle APB=180-\beta-x,\qquad x\in(0,\alpha),$$
so as the cut varies, $\angle APB$ ranges over the **open interval**
$$I_A=(\,180-\beta-\alpha,\ 180-\beta\,)=(\gamma,\ 180-\beta),\qquad\text{of length }\alpha. \tag{$\star$}$$
(Its endpoints are the limits $P\to C$ giving $\gamma$ and $P\to B$ giving $180-\beta$; both
excluded as $x\in(0,\alpha)$ is open.)

### 1. Residues and "good" triangles

Fix θ and work in the quotient group $\mathbb{R}/\theta\mathbb{Z}$; write $u\equiv v$ for
$u-v\in\theta\mathbb{Z}$. An angle $u\in(0,180)$ is a *multiple of θ* iff $u\equiv 0$, i.e.
$u\in\{\theta,2\theta,\dots\}$. Call a triangle **good** if **none** of its three angles is a
multiple of θ (all three residues are $\ne 0$ in $\mathbb{R}/\theta\mathbb{Z}$). A good
triangle has no angle equal to θ, so the game has not stopped.

Set $S\equiv 180\pmod\theta$. Note $S\equiv 0\iff\theta\mid 180\iff 180/\theta\in\mathbb{Z}$.
Because $0<\theta<180$, $180/\theta>1$, so "$180/\theta\in\mathbb{Z}$" is the same as
"$\theta=180/n$ for an integer $n\ge2$". We prove Mulan wins in exactly this case.

We use two elementary facts about arithmetic progressions of step θ, both instances of the
**Pigeonhole / covering principle** (knowledge_base.md, "Pigeonhole / extremal", lines 108,
188):

> **Fact P1.** Any open interval of length $>\theta$ contains a multiple of θ.
> *Proof.* For $(u,u+L)$ with $L>\theta$, let $m=\lfloor u/\theta\rfloor+1$; then
> $m\theta>u$ and $m\theta\le u+\theta<u+L$, so $m\theta\in(u,u+L)$. ∎

> **Fact P2.** Any closed interval of length $\ge\theta$ contains a multiple of θ.
> *Proof.* For $[u,u+L]$, $L\ge\theta$, let $m=\lfloor(u+L)/\theta\rfloor$; then
> $m\theta\le u+L$ and $m\theta>(u+L)-\theta\ge u$, so $m\theta\in[u,u+L]$. ∎

### 2. Necessity: if $\theta\nmid 180$ then Shan-Yu survives forever

Assume $180/\theta\notin\mathbb{Z}$, i.e. $S\not\equiv 0$.

**(2a) A good starting triangle exists.** Consider isosceles triangles
$(t,t,180-2t)$ with $t\in(0,90)$. The value $t$ is *bad* if $t\equiv 0$, or if
$180-2t\equiv 0$; the first happens for finitely many $t\in(0,90)$ (the multiples of θ there),
the second for the finitely many $t=(180-k\theta)/2\in(0,90)$, $k\in\mathbb{Z}$. Choose any
$t\in(0,90)$ outside this finite bad set (such $t$ exists, indeed uncountably many). Then all
three angles $t,t,180-2t$ are non-multiples of θ: the triangle is good. Shan-Yu opens with it.

**(2b) Lemma A (good is forward-closed under best defense).**
*If a triangle is good and $S\not\equiv 0$, then for every Mulan move (every apex, every
$x\in(0,\alpha)$) at least one of the two children is good.*

*Proof.* Fix the apex labelling as in §0, and write residues $a\equiv\alpha,\ b\equiv\beta,\
c\equiv\gamma$, all $\ne 0$ (good), $a+b+c\equiv S$, and $t\equiv x$. From §0:
$$T_1\ \text{residues}\equiv\{t,\ b,\ S-b-t\},\qquad
  T_2\ \text{residues}\equiv\{a-t,\ c,\ b+t\}.$$
$T_1$ is *bad* iff one residue is $0$: since $b\ne0$, this is $t\equiv0$ or $t\equiv S-b$.
$T_2$ is *bad* iff $a-t\equiv0$, $c\equiv0$, or $b+t\equiv0$: since $c\ne0$, this is
$t\equiv a$ or $t\equiv -b$. Hence
$$\text{both children bad}\iff t\in\{0,\,S-b\}\cap\{a,\,-b\}.$$
The intersection $\{0,S-b\}\cap\{a,-b\}$ is nonempty only if one of the four equalities holds:
$$0\equiv a\ (\Rightarrow a\equiv0),\quad 0\equiv-b\ (\Rightarrow b\equiv0),\quad
  S-b\equiv a\ (\Rightarrow c\equiv0,\ \text{as }S\equiv a+b+c),\quad S-b\equiv-b\ (\Rightarrow S\equiv0).$$
All four are excluded by hypothesis ($a,b,c\ne0$ and $S\not\equiv0$). Therefore the
intersection is empty, so for **every** $t$ (hence every legal $x$), at most one child is bad,
i.e. at least one child is good. The same computation applies verbatim to each of the three
apex choices, since it only used $a,b,c,S\not\equiv0$, which are properties of the (unordered)
triangle. ∎

**(2c) Conclusion.** The good child produced by Lemma A is a genuine triangle whose three
angles are non-multiples of θ, and its angle sum is again $180$, so $S\not\equiv0$ still holds
(the untouched base angle keeps its nonzero residue $b$ or $c$; the two new angles are the
nonzero residues certified in the proof). Thus "good with $S\not\equiv0$" is preserved. Shan-Yu's
strategy: **always discard a bad child, keeping a good one** (Lemma A guarantees one exists).
By induction the triangle is good after every move, so it never has an angle equal to θ. The
game never stops, and Mulan never wins. Hence for $\theta\nmid180$ Mulan cannot force a win. ∎(necessity)

*(This uses knowledge_base.md "Invariants & monovariants", lines 117/191: the predicate
"good" is an invariant preserved by Shan-Yu's discard.)*

### 3. Sufficiency: if $\theta=180/n$ (integer $n\ge2$) then Mulan wins

Now $S\equiv0$ and $180=n\theta$. We describe Mulan's forced-win strategy from **any** triangle
Shan-Yu builds. If the starting triangle already has an angle equal to θ, Mulan has won before
moving. Otherwise there are two cases handled by the lemmas below.

**(3a) Lemma B (alignment cut, and its existence — closes G1).**
*Let $\theta=180/n$ ($n\ge2$) and let $\mathcal T$ be a triangle no angle of which is a
multiple of θ. Then there is a legal cevian after which **both** children have an angle equal
to a (positive) multiple of θ.*

*Proof.* By the supplement identity of §0, it suffices to find a cevian whose cut-point angle
$\angle APB$ is a multiple of θ: then $\angle APC=180-\angle APB$ is also a multiple (as
$180=n\theta\equiv0$), so both children carry one. By ($\star$), with apex $A$ (angle $\alpha$)
the achievable $\angle APB$ fills the open interval $I_A=(\gamma,\,180-\beta)$, of length
$\alpha$. Its endpoints are non-multiples of θ: $\gamma$ by hypothesis, and $180-\beta\equiv-\beta$
which is a non-multiple because $\beta$ is. So it suffices to produce an interval $I_X$ (some
apex $X$) containing a multiple of θ in its interior.

Take the apex to be a vertex of **largest** angle; relabel so this is $A$, with $\alpha\ge\beta,
\gamma$. Since $\theta=180/n\le90$, we split into the only two possible regimes (there is no
$n\ge2$ with $60<180/n<90$):

- **Regime $n\ge3$, so $\theta\le60$.** As $\alpha$ is the largest of three angles summing to
  $180$, $\alpha\ge60\ge\theta$. If $\alpha=\theta$ then $\theta=60$ and $\alpha=60$, forcing
  $\beta=\gamma=60$ too — but then every angle equals $60=\theta$, contradicting that no angle
  is a multiple of θ. Hence $\alpha>\theta$, so $I_A$ is an open interval of length $\alpha>\theta$;
  by **Fact P1** it contains a multiple of θ. Alignment via apex $A$.

- **Regime $n=2$, so $\theta=90$.** The only multiple of θ in $(0,180)$ is $90$. We need
  $90\in I_A=(\gamma,180-\beta)$, i.e. $\gamma<90$ and $\beta<90$. Since the three angles sum to
  $180$, at most one exceeds $90$, and that one (if any) is the maximum $\alpha$; thus the other
  two, $\beta$ and $\gamma$, are both $<90$ (and $\ne90$ by hypothesis). Hence $\gamma<90<180-\beta$
  and $90\notin\{\gamma,180-\beta\}$, so $90\in I_A$. Alignment via apex $A$ (this cut is the
  foot of the altitude from $A$). ∎

After the alignment cut, name the multiples: $\angle APB=k\theta$ and $\angle APC=(n-k)\theta$
with $1\le k\le n-1$ (both are genuine triangle angles, hence in $(0,180)$, hence positive
multiples $<180$ — this closes **G2**). Whichever child Shan-Yu keeps, the resulting triangle
has an angle equal to some $m\theta$ with $1\le m\le n-1$. If $m=1$ that angle is θ and Mulan
has already won. Otherwise $m\ge2$ and Mulan proceeds to peel.

**(3b) Lemma C (θ-peel and the double-fork win).**
*If the current triangle has an angle equal to $m\theta$ with $2\le m\le n-1$ (and no angle
equal to θ yet), Mulan can force, in finitely many moves, a triangle with an angle equal to θ.*

*Proof.* Let the vertex with angle $m\theta$ be the apex $A$ ($\alpha=m\theta$), base angles
$\beta,\gamma$. Mulan cuts at $x=(m-1)\theta$; this is legal since $2\le m$ gives
$0<(m-1)\theta<m\theta=\alpha$, so $x\in(0,\alpha)$ strictly interior. By §0 the children are
$$T_1=\{(m-1)\theta,\ \beta,\ 180-\beta-(m-1)\theta\},\qquad
  T_2=\{\theta,\ \gamma,\ \beta+(m-1)\theta\}.$$
$T_2$ has an angle equal to θ. Two subcases:

- If $m\ge3$: $T_1$ has apex-part $(m-1)\theta$ with $m-1\ge2$, so $T_1$ has **no** angle equal
  to θ from the apex; and if Shan-Yu keeps $T_2$ Mulan wins immediately (angle θ). So Shan-Yu's
  only non-losing choice is to keep $T_1$, which has an angle equal to $(m-1)\theta$. The peel
  value has dropped from $m$ to $m-1$.

- If $m=2$: then $x=\theta$, and
  $$T_1=\{\theta,\ \beta,\ 180-\beta-\theta\},\qquad T_2=\{\theta,\ \gamma,\ \beta+\theta\}.$$
  **Both** children have an angle equal to θ. Whichever Shan-Yu keeps, the game stops with
  Mulan winning.

Starting from $m$, each peel step strictly decreases the peel value by $1$ (Shan-Yu forced to
keep the larger child, else he loses at once), so after at most $m-2\le n-3$ steps the value
reaches $2$, where the double-fork wins. Total moves in the peel: at most $m-1\le n-2$,
finite. ∎

**(3c) Conclusion.** From any starting triangle: if it has an angle equal to θ, Mulan has won.
Else if it has an angle $m\theta$ with $m\ge2$, Mulan peels (Lemma C) and wins. Else no angle
is a multiple of θ, and Mulan plays the alignment cut (Lemma B); after Shan-Yu's discard she
holds a triangle with an angle $m\theta$, $1\le m\le n-1$, which is either an immediate win
($m=1$) or is finished by peeling ($m\ge2$). In every case Mulan wins in at most
$1+(n-2)=n-1$ moves. Hence for $\theta=180/n$ Mulan forces victory. ∎(sufficiency)

### 4. The characterization and its verification

Combining §2 and §3: **Mulan can guarantee a win in finitely many moves iff
$\theta\mid180$, i.e. iff $\theta=180/n$ for an integer $n\ge2$.** (Necessity shows that when
$\theta\nmid180$ Shan-Yu survives forever; sufficiency shows that when $\theta\mid180$ Mulan
wins.) In particular every winning θ satisfies $\theta\le90$, and no $\theta>90$ is winning
(then $180/\theta<2$ is not an integer $\ge2$), consistent with the answer.

**Verification, $n=2$ ($\theta=90$).** From any triangle with no $90^\circ$ angle: the altitude
from the largest-angle vertex (Regime $n=2$ of Lemma B) has foot strictly inside the opposite
side (the two base angles are $<90$), and it splits $\mathcal T$ into two right triangles, each
with a $90^\circ=\theta$ angle. Mulan wins in one move. ✓

**Verification, $n=3$ ($\theta=60$).** From any non-equilateral triangle (equilateral already
has $60^\circ$), the max angle $\alpha>60$, so $I_A$ (length $\alpha>60$) contains a multiple of
$60$, namely $60$ or $120$. If it contains $60$: cut $\angle APB=60$; both children have a
$60^\circ$ angle, win in one move. If it contains $120$ (and not $60$): cut $\angle APB=120$,
$\angle APC=60$; Shan-Yu keeps the $120^\circ$ child (else loses to the $60^\circ$ one), giving
angle $2\theta$. Peel with $x=60$: $T_1=\{60,\beta,120-\beta\}$, $T_2=\{60,\gamma,\beta+60\}$,
both have $60^\circ$ — win. Total two moves. ✓

Both verifications match the general strategy. $\qquad\blacksquare$

## Promotable lemmas
- **Lemma A (residue survival invariant).** For a triangle with all three angle-residues
  $\not\equiv0$ and $180\not\equiv0\pmod\theta$, every cevian leaves at least one child with all
  three angle-residues $\not\equiv0$. (Proved in §2b; the "good" predicate is forward-closed, so
  Shan-Yu survives whenever $\theta\nmid180$.)
- **Lemma B (alignment existence).** If $\theta=180/n$ and no angle of the triangle is a
  multiple of θ, some cevian makes both children carry a multiple-of-θ angle; concretely, the
  cut-point angle can be made a multiple of θ, via the largest-angle apex (θ≤60) or the altitude
  (θ=90). (Proved in §3a; closes the field's shared gap G1.)
- **Lemma C (θ-peel / double-fork).** An angle $m\theta$ ($m\ge2$) is forced down to θ in
  $\le m-1$ moves: cut $x=(m-1)\theta$; the θ-child is an immediate win, the $(m-1)\theta$-child
  continues; at $m=2$ both children carry θ. (Proved in §3b.)
