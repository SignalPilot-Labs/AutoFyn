✻ Cooked for 1h 18m 18s

Setting up the mechanics of a cut

Fix a triangle with angles $A,B,C$ (at the corresponding vertices), $A+B+C=180^\circ$. Mulan chooses a side,
say $BC$, and an interior point $P$; the cut is the cevian from $P$ to the opposite vertex $A$. Writing
$x=\angle BAP\in(0,A)$ (Mulan controls $x$ freely over this whole open interval), the two resulting triangles
have angle-triples

$$\underbrace{{,B,\ x,\ A+C-x,}}_{\text{child}1\ (\text{keeps }B)},\qquad \underbrace{{,C,\ A-x,\ 
B+x,}}{\text{child}_2\ (\text{keeps }C)} .$$

(Indeed $\angle APB$ and $\angle APC$ are supplementary, and $180^\circ-B-x=A+C-x$, $180^\circ-\angle
APB=B+x$.) Shan‑Yu keeps one child. Cutting a different side just relabels which angle is the apex, so this
covers every move.

Let me write $M_\theta={k\theta : k\in\mathbb Z_{\ge 1},\ k\theta<180^\circ}$ (the multiples of $\theta$ that
can occur as an angle). Note $\theta\in M_\theta$, so avoiding $M_\theta$ implies avoiding $\theta$.

Answer

$$\boxed{\ \text{Mulan can force a win exactly when } \theta=\dfrac{180^\circ}{n}\ \text{for some integer }
n\ge 2\ }$$

equivalently, when $180^\circ/\theta$ is an integer (these are
$90^\circ,60^\circ,45^\circ,36^\circ,30^\circ,\dots$, all $\le 90^\circ$).

---
Part 1 — If $180^\circ/\theta\notin\mathbb Z$, Shan‑Yu survives forever

Call a triangle safe if none of its angles lies in $M_\theta$. A safe triangle never contains $\theta$. Shan‑Yu
starts at any safe triangle (only finitely many angle‑values are forbidden, so safe triangles exist). It
suffices to prove:

▎ Lemma. If $180^\circ/\theta\notin\mathbb Z$ and a cut of a triangle $T=(a,b,c)$ produces two children both 
▎ containing an angle in $M_\theta$, then $T$ already contains an angle in $M_\theta$.

Its contrapositive says: from a safe triangle, every cut leaves at least one safe child, so Shan‑Yu keeps a
safe triangle forever and never sees $\theta$.

Proof of Lemma. Take the apex to be $a$, base angles $b,c$; the children are ${b,x,a+c-x}$ and ${c,a-x,b+x}$.
If $b\in M_\theta$ or $c\in M_\theta$ we are done, so assume $b,c\notin M_\theta$. Then child$_1$'s multiple is
$x$ or $a+c-x$, and child$2$'s is $a-x$ or $b+x$. Check all four combinations (with $i\theta,j\theta\in 
M\theta$):

- $x=i\theta,\ a-x=j\theta$: then $a=(i+j)\theta\in M_\theta$ — so $T$ contains a multiple. ✓
- $x=i\theta,\ b+x=j\theta$: then $b=(j-i)\theta\in M_\theta$, contradicting $b\notin M_\theta$.
- $a+c-x=i\theta,\ a-x=j\theta$: then $c=(i-j)\theta\in M_\theta$, contradiction.
- $a+c-x=i\theta,\ b+x=j\theta$: adding gives $180^\circ=(i+j)\theta$, i.e. $\theta=180^\circ/(i+j)$,
contradicting $180^\circ/\theta\notin\mathbb Z$.

Only the first case is possible, and it forces $a\in M_\theta$. $\qquad\blacksquare$

Hence for every $\theta$ with $180^\circ/\theta\notin\mathbb Z$ (in particular all $\theta>90^\circ$), Shan‑Yu
wins.

---
Part 2 — If $\theta=180^\circ/n$ $(n\ge 2)$, Mulan wins

Step A (angles that are multiples of $\theta$ are already winning). I claim any triangle containing $k\theta$
with $1\le k\le n-1$ lets Mulan force a win, by induction on $k$.
- $k=1$: it contains $\theta$, game over.
- $k\ge 2$: take apex $a=k\theta$ and cut with $x=\theta$ (valid since $\theta<k\theta$). Then

Hence for every $\theta$ with $180^\circ/\theta\notin\mathbb Z$ (in particular all $\theta>90^\circ$), Shan‑Yu
wins.

---
Part 2 — If $\theta=180^\circ/n$ $(n\ge 2)$, Mulan wins

Step A (angles that are multiples of $\theta$ are already winning). I claim any triangle containing $k\theta$
with $1\le k\le n-1$ lets Mulan force a win, by induction on $k$.
- $k=1$: it contains $\theta$, game over.

Hence for every $\theta$ with $180^\circ/\theta\notin\mathbb Z$ (in particular all $\theta>90^\circ$), Shan‑Yu
wins.

---
Part 2 — If $\theta=180^\circ/n$ $(n\ge 2)$, Mulan wins

Step A (angles that are multiples of $\theta$ are already winning). I claim any triangle containing $k\theta$
with $1\le k\le n-1$ lets Mulan force a win, by induction on $k$.
- $k=1$: it contains $\theta$, game over.

Hence for every $\theta$ with $180^\circ/\theta\notin\mathbb Z$ (in particular all $\theta>90^\circ$), Shan‑Yu
wins.

---
Part 2 — If $\theta=180^\circ/n$ $(n\ge 2)$, Mulan wins

Step A (angles that are multiples of $\theta$ are already winning). I claim any triangle containing $k\theta$
with $1\le k\le n-1$ lets Mulan force a win, by induction on $k$.
- $k=1$: it contains $\theta$, game over.
- $k\ge 2$: take apex $a=k\theta$ and cut with $x=\theta$ (valid since $\theta<k\theta$). Then
$$\text{child}_1={b,\ \theta,\ a+c-\theta}\ \text{(contains }\theta\text{)},\qquad \text{child}_2={c,\
(k-1)\theta,\ b+\theta}\ \text{(contains }(k-1)\theta).$$
Child$_1$ ends the game; child$_2$ is winning by induction. Whatever Shan‑Yu keeps, Mulan wins. ✓

Step B (any triangle can be pushed into Step A in one move). Let $T=(a,b,c)$ be arbitrary (if it already
contains a multiple of $\theta$, use Step A). Take the apex $a$ to be the largest angle and $c$ the smallest.
Because $n\ge 2$:

- for $n\ge 3$: $a\ge 60^\circ\ge\theta$, and since $T$ is not the all‑$\theta$ triangle, $a>\theta$; an open
interval $(c,c+a)$ of length $a>\theta$ contains a multiple $i\theta$ of $\theta$;
- for $n=2$ ($\theta=90^\circ$): $c<90^\circ$ and $c+a=180^\circ-b>90^\circ$, so $90^\circ=i\theta$ (with
$i=1$) lies in $(c,c+a)$.

Pick such $i\theta\in(c,c+a)$ and cut with $x=a+c-i\theta\in(0,a)$. Then
$$\text{child}_1={b,\ x,\ i\theta},\qquad \text{child}_2={c,\ a-x,\ (n-i)\theta},$$
using $b+x=180^\circ-i\theta=(n-i)\theta$ (here $n\theta=180^\circ$ is essential). Both children contain a
multiple of $\theta$ with index in $[1,n-1]$, hence both are winning by Step A.

So from any starting triangle Shan‑Yu chooses, Mulan wins. Each branch takes at most one move (Step B) plus at
most $n-1$ moves (Step A), so victory comes in at most $n$ steps — finitely many.

---
Conclusion

Mulan can guarantee victory iff $\theta=\dfrac{180^\circ}{n}$ for some integer $n\ge 2$, i.e. iff $180^\circ$
is an integer multiple of $\theta$. For every other $\theta$ (in particular every $\theta>90^\circ$), Shan‑Yu
can keep all angles out of the finite set ${\theta,2\theta,\dots}$ forever and never lose.

