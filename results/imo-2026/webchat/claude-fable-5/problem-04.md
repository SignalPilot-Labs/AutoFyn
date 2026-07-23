## Answer

Mulan can guarantee victory exactly when
$$\boxed{\theta=\frac{180^\circ}{n}\ \text{ for some integer } n\ge 2,}$$
i.e. precisely when $180^\circ/\theta$ is an integer.

Throughout, write a triangle by its (multi)set of angles. The whole game is governed by one computation.

**Anatomy of a cut.** Let $\mathcal T$ have vertices $U,V,W$ with angles $u,v,w$. If $P$ lies strictly inside side $UV$ and we cut along $WP$, and $p:=\angle UPW$, then the two pieces are
$$\triangle UWP=\{u,\;p,\;180^\circ-u-p\},\qquad \triangle VWP=\{v,\;180^\circ-p,\;p-v\},$$
and the attainable values of $p$ are exactly the open interval $(v,\;180^\circ-u)$.

*Proof.* $\angle WUP=u$ and $\angle WVP=v$ since $P\in UV$; $\angle VPW=180^\circ-p$; the angle sums give the third angles as stated. Writing $p=180^\circ-u-\angle UWP$ with $\angle UWP\in(0^\circ,w)$ shows $p\in(v,180^\circ-u)$, since $180^\circ - u - w = v$. Conversely, for any $p$ in that interval, the ray from $W$ making angle $180^\circ-u-p\in(0^\circ,w)$ with $WU$ (on the side of $V$) meets segment $UV$ at an interior point $P$, realizing that $p$. $\square$

Note the pieces' new angles all lie in $(0^\circ,180^\circ)$: indeed $180^\circ-u-p\in(0^\circ,w+v)$ and $p-v\in(0^\circ,w+u)$.

## Part 1: If $\theta=180^\circ/n$, Mulan wins

Call an angle *marked* if it equals $k\theta$ for some $k\in\{1,\dots,n-1\}$.

**Lemma A.** If $\mathcal T$ contains a marked angle $k\theta$, Mulan wins within $k-1$ further cuts.

*Proof.* Induct on $k$. If $k=1$, the triangle has angle $\theta$ and the game stops with Mulan winning. If $k\ge 2$, say the angle at $W$ is $w=k\theta$ and the others are $u,v$. Mulan cuts through $W$ using $p=180^\circ-u-\theta$; this is valid since $p<180^\circ-u$ and $p>v\iff 180^\circ-u-v>\theta\iff k\theta>\theta$. By the anatomy, the pieces are
$$\{u,\;180^\circ-u-\theta,\;\theta\}\quad\text{and}\quad\{v,\;u+\theta,\;(k-1)\theta\},$$
because $p-v=(180^\circ-u-v)-\theta=(k-1)\theta$. If Shan‑Yu keeps the first piece, it contains $\theta$ and Mulan wins immediately; if he keeps the second, it contains the marked angle $(k-1)\theta$ and the induction hypothesis finishes in $\le k-2$ more cuts. $\square$

**Lemma B.** If $\mathcal T$ has no marked angle (in particular, no angle $\theta$), Mulan has a cut for which *both* pieces contain a marked angle.

*Proof.* Let $W$ be a vertex of maximum angle $w$, with other angles $u,v$. She cuts through $W$, so $p$ may be any value in $(v,180^\circ-u)$, an interval of length $w$. She chooses $p=k\theta$ for a suitable integer $k$:

*Case $n=2$ ($\theta=90^\circ$):* since $w$ is the maximum and $w\ne 90^\circ$, at most one angle is $\ge 90^\circ$ and it is $w$; hence $u,v<90^\circ$, so $p=90^\circ\in(v,180^\circ-u)$ is attainable.

*Case $n\ge 3$:* the maximum angle satisfies $w\ge 60^\circ\ge\theta$, and $w\ne\theta$ since $w$ is not marked, so $w>\theta$. Take $k=\lfloor v/\theta\rfloor+1$; then $k\theta>v$ and $k\theta\le v+\theta<v+w=180^\circ-u$, so $p=k\theta$ is attainable.

In either case $0<k\theta<180^\circ$, so $1\le k\le n-1$. The pieces are $\{u,\,k\theta,\,180^\circ-u-k\theta\}$ and $\{v,\,(n-k)\theta,\,k\theta-v\}$, using $180^\circ-k\theta=(n-k)\theta$ with $1\le n-k\le n-1$. Both contain a marked angle. $\square$

**Mulan's strategy.** If the initial triangle has a marked angle, she applies Lemma A. Otherwise she makes the single cut of Lemma B; whichever piece Shan‑Yu keeps has a marked angle, and Lemma A finishes. In total she wins in at most $n-1$ cuts, no matter what Shan‑Yu does.

## Part 2: If $180^\circ/\theta\notin\mathbb Z$, Shan‑Yu wins

Call a value $x\in(0^\circ,180^\circ)$ **red** if $x=k\theta$ for a positive integer $k$, and **green** otherwise. There are finitely many red values. Three facts hold, the first using $\theta\nmid 180^\circ$:

1. No two red values sum to $180^\circ$ (else $(k+\ell)\theta=180^\circ$).
2. If two red values sum to less than $180^\circ$, the sum is red.
3. A positive difference of two red values is red.

**Shan‑Yu's strategy: keep all three angles green.**

*He can start green.* $60^\circ$ is green (if $60^\circ=k\theta$ then $3k\theta=180^\circ$, contradiction), and since only finitely many $t\in(0^\circ,60^\circ)$ make $60^\circ+t$ or $60^\circ-t$ red, he may pick a triangle $\{60^\circ+t,\,60^\circ,\,60^\circ-t\}$ with all angles green.

*He can stay green.* Suppose the current angles $a,b,c$ are all green, and Mulan cuts through the vertex with angle $a$. By the anatomy (relabeling), the pieces are
$$\{b,\;p,\;180^\circ-b-p\}\quad\text{and}\quad\{c,\;180^\circ-p,\;p-c\},\qquad p\in(c,\;180^\circ-b),$$
and all four values $p,\ 180^\circ-p,\ 180^\circ-b-p,\ p-c$ lie in $(0^\circ,180^\circ)$. Since $b$ and $c$ are green, if *neither* piece were all‑green, then one of $\{p,\;180^\circ-b-p\}$ and one of $\{180^\circ-p,\;p-c\}$ would be red. All four combinations are impossible:

- $p$ and $180^\circ-p$ red: they sum to $180^\circ$, contradicting Fact 1.
- $p$ and $p-c$ red: then $c=p-(p-c)$ is red by Fact 3 — but $c$ is green.
- $180^\circ-b-p$ and $180^\circ-p$ red: then $b=(180^\circ-p)-(180^\circ-b-p)$ is red by Fact 3 — but $b$ is green.
- $180^\circ-b-p$ and $p-c$ red: their sum is $180^\circ-b-c=a\in(0^\circ,180^\circ)$, red by Fact 2 — but $a$ is green.

So for every possible cut (the same argument applies verbatim to cuts through the other two vertices), at least one piece has all angles green, and Shan‑Yu keeps it.

By induction, every triangle that ever occurs is all‑green. Since $\theta$ is red, no triangle ever has an angle equal to $\theta$, so the game never stops and Mulan can never win — let alone guarantee a win in finitely many steps.

## Conclusion

Combining the two parts: Mulan can guarantee victory in finitely many steps if and only if
$$\theta\in\left\{\tfrac{180^\circ}{2},\tfrac{180^\circ}{3},\tfrac{180^\circ}{4},\dots\right\}=\{90^\circ,\,60^\circ,\,45^\circ,\,36^\circ,\,30^\circ,\dots\},$$
that is, exactly when $180^\circ/\theta$ is an integer; and in that case she needs at most $\tfrac{180^\circ}{\theta}-1$ cuts.

time 11 mins