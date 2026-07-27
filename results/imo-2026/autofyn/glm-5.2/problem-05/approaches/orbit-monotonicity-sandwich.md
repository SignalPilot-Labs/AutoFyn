# Approach: orbit-monotonicity-sandwich

## Status
solved

## Target
Prove the full characterization: the solutions are exactly $f(x)=x+c$, $c\ge0$.
(exhibit + verify the family; prove uniqueness — no other $f$ works.)

## Technique
Orbit/iterate identity + squeeze-at-infinity + boundary contradiction. Originally
planned as the aimo-0234 monotonicity-lattice sandwich, but the build replaced
the load-bearing (and unproven) monotonicity step and the separate gap-region
step by a single, cleaner mechanism: the master squeeze, evaluated along the
arithmetic orbit, forces $g(x)\to g(y_0)$ as $x\to\infty$ for every $y_0$ with
$g(y_0)>0$; this pins all positive values of $g$ to a single constant $\beta$,
forces $g\equiv\beta$ on a tail ray, and a boundary-contradiction (squeeze at
the rightmost zero of $g$) kills the possibility $g\in\{0,\beta\}$ with a zero.
No monotonicity, no continuity, no IVT is assumed.

## Shared derived facts (re-derived from scratch below)
- $g:=f-\mathrm{id}$. At $x=f(y)$ both classical inequalities are tight, forcing
  $f(f(y))=2f(y)-y$, i.e. $g(f(y))=g(y)$ (orbit invariance).
- The forward orbit $y_n=f^n(y)=y+n\,g(y)$ is an arithmetic progression.
- $g(y)<0$ makes the orbit eventually leave $\Rpos$, contradicting $f>0$; hence
  $g\ge0$ everywhere. No continuity used.
- Master squeeze (SOS of the two squared gaps):
  for all $x,y>0$,
  $$|g(x)-g(y)|\,\bigl(g(x)+g(y)+2x+2y\bigr)\;\le\;(x-f(y))^{2}.$$
  Since $g\ge0$, the factor is $\ge 2x+2y>0$, giving
  $|g(x)-g(y)|\le (x-f(y))^{2}/(2x+2y)$ for all $x,y>0$.

## Full proof

Let $\Rpos=\mathbb R_{>0}$. We must determine all $f:\Rpos\to\Rpos$ such that
$$\sqrt{\frac{x^{2}+f(y)^{2}}{2}}\;\ge\;\frac{f(x)+y}{2}\;\ge\;\sqrt{x\,f(y)}
\qquad\forall\,x,y>0. \tag{H}$$

We prove the solutions are exactly $f(x)=x+c$ for $c\ge0$.

---

### 0. The candidate family works (exhibit + verify)

For $f(x)=x+c$ with $c\ge0$ one has $f(y)=y+c$, so
$$\frac{f(x)+y}{2}=\frac{x+c+y}{2}=\frac{x+(y+c)}{2}=\frac{x+f(y)}{2}.$$
Thus the middle of (H) equals the arithmetic mean of the pair $(x,f(y))$, and
(H) becomes the classical chain
$$\sqrt{\frac{x^{2}+f(y)^{2}}{2}}\;\ge\;\frac{x+f(y)}{2}\;\ge\;\sqrt{x\,f(y)},
$$
which is QM$\ge$AM$\ge$GM for the two positive numbers $x$ and $f(y)$ (cite
knowledge_base: "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM. Equality
cases pin down the extremal configuration"). Hence every $f(x)=x+c$, $c\ge0$,
satisfies (H). The rest of the proof establishes uniqueness.

---

### 1. Square form of the hypothesis

Set
$$A:=(f(x)+y)^{2}-4x\,f(y),\qquad B:=2\bigl(x^{2}+f(y)^{2}\bigr)-(f(x)+y)^{2}.$$
Since $\frac{f(x)+y}{2}\ge\sqrt{xf(y)}\iff (f(x)+y)^{2}\ge 4xf(y)$ and
$\sqrt{\frac{x^{2}+f(y)^{2}}{2}}\ge\frac{f(x)+y}{2}\iff (f(x)+y)^{2}\le
2(x^{2}+f(y)^{2})$, condition (H) is equivalent to
$$A\ge0\quad\text{and}\quad B\ge0\qquad\forall\,x,y>0. \tag{1}$$

---

### 2. Orbit invariance $g(f(y))=g(y)$ (tight point $x=f(y)$)

Define $g(t):=f(t)-t$ (no sign assumption yet). Substitute $x=f(y)$ into (H):
the left side becomes
$\sqrt{(f(y)^{2}+f(y)^{2})/2}=f(y)$ and the right side becomes
$\sqrt{f(y)\cdot f(y)}=f(y)$. The displayed chain forces
$$f(y)\;\ge\;\frac{f(f(y))+y}{2}\;\ge\;f(y),$$
so equality holds throughout and
$$f(f(y))=2f(y)-y.\tag{2}$$
Subtracting $f(y)$ from both sides and using $f(t)-t=g(t)$:
$$g(f(y))=f(f(y))-f(y)=(2f(y)-y)-f(y)=f(y)-y=g(y). \tag{3}$$
This is **orbit invariance**: $g$ is constant along forward iterates of $f$.

---

### 3. Nonnegativity $g\ge0$ (codomain-positivity sign kill)

Let $y_0=y$ and define $y_{n+1}=f(y_n)$ (the forward orbit). Iterating (3) gives
$g(y_n)=g(y)$ for all $n\ge0$, hence
$$y_{n+1}=f(y_n)=y_n+g(y_n)=y_n+g(y),$$
so by induction $y_n=y+n\,g(y)$ — an arithmetic progression with step $g(y)$.

Suppose $g(y)<0$ for some $y>0$. Then $y_n=y+n\,g(y)\to-\infty$, so for $n$ large
enough $y_n\le0$, which is impossible because each $y_n=f(y_{n-1})\in\Rpos$ by
the codomain of $f$. Contradiction. Therefore
$$g(y)\ge0\qquad\forall\,y>0,\qquad\text{i.e.}\quad f\ge\mathrm{id}. \tag{4}$$
(No continuity is used; this is purely the iterate identity plus positivity of
the codomain.)

---

### 4. Master squeeze (SOS of the two squared gaps)

We compute $A+B$ and $A-B$ with $f(x)=x+g(x)$, $f(y)=y+g(y)$.

**Sum.**
$$A+B=\bigl[(f(x)+y)^{2}-4xf(y)\bigr]+\bigl[2(x^{2}+f(y)^{2})-(f(x)+y)^{2}\bigr]
=2\bigl(x^{2}+f(y)^{2}-2xf(y)\bigr)=2\,(x-f(y))^{2}. \tag{5}$$

**Difference.** Expand $f(x)+y=x+g(x)+y$ and $f(y)=y+g(y)$:
$$A=2(x+y)\,g(x)+g(x)^{2}-4x\,g(y)+(x-y)^{2},$$
$$B=4y\,g(y)+2g(y)^{2}-2(x+y)\,g(x)-g(x)^{2}+(x-y)^{2},$$
where we used $(f(x)+y)^{2}=(x+y)^{2}+2(x+y)g(x)+g(x)^{2}$ and
$2(x^{2}+f(y)^{2})=2(x^{2}+y^{2})+4y\,g(y)+2g(y)^{2}$, then
$(x+y)^{2}-4xy=(x-y)^{2}$ and $2(x^{2}+y^{2})-4xy=(x-y)^{2}$. Subtracting and
collecting (the $(x-y)^{2}$ and $(x+y)g(\cdot)$ terms cancel by the symmetric
placement):
$$A-B=2\,g(x)^{2}+4(x+y)g(x)-2\,g(y)^{2}-4(x+y)g(y)
=2\,(g(x)-g(y))\bigl(g(x)+g(y)+2x+2y\bigr). \tag{6}$$
(Identity (6) is a direct polynomial expansion; it is the SOS / completing-the-
square reduction of knowledge_base: "Sum of squares (SOS) / completing the
square: prove a real inequality by rewriting LHS−RHS as a sum of squares." It was
verified by symbolic expansion.)

Now (1) gives $A\ge0$ and $B\ge0$. For any two nonnegative real numbers,
$|A-B|\le A+B$. Applying this and using (5), (6):
$$\bigl|\,2\,(g(x)-g(y))\bigl(g(x)+g(y)+2x+2y\bigr)\,\bigr|
\;\le\;2\,(x-f(y))^{2}.$$
Dividing by $2$:
$$\boxed{\;|g(x)-g(y)|\,\bigl(g(x)+g(y)+2x+2y\bigr)\;\le\;(x-f(y))^{2}\;}
\qquad\forall\,x,y>0. \tag{$\star$}$$
By (4) the factor $g(x)+g(y)+2x+2y\ge 2x+2y>0$, so we may divide and obtain the
**quadratic-modulus squeeze**
$$\boxed{\;|g(x)-g(y)|\;\le\;\frac{(x-f(y))^{2}}{2x+2y}\;}\qquad\forall\,x,y>0.
\tag{$\star\star$}$$
(For reference: $x-f(y)=x-y-g(y)$.) This is the **master squeeze**, the engine
of the rest of the proof. Note it holds for *every* pair $(x,y)$, not only at
image points; it is tight (small right-hand side) exactly when $x\approx f(y)$.

---

### 5. Limit at infinity: every positive value of $g$ is a common limit

**Lemma 5 (asymptotic pinning).** *If $g(y_0)=\alpha>0$, then
$\displaystyle\lim_{x\to\infty}g(x)=\alpha$.*

*Proof.* By orbit invariance (3), the arithmetic orbit
$y_n=y_0+n\alpha$ ($n\ge0$) carries $g(y_n)=\alpha$ for every $n$, and
$f(y_n)=y_n+\alpha=y_{n+1}$.

Fix $x\ge y_0+\alpha$. Choose the index $n\ge0$ so that
$y_{n+1}=y_0+(n+1)\alpha$ is a nearest lattice point to $x$ among
$\{y_0+m\alpha:m\ge1\}$; such $n$ exists for every $x\ge y_0+\alpha/2$ (the
lattice $\{y_0+m\alpha\}_{m\ge1}$ covers $[y_0+\alpha/2,\infty)$ within
$\alpha/2$), and it gives
$$|x-y_{n+1}|\le\tfrac{\alpha}{2}. \tag{7}$$
Apply the squeeze $(\star\star)$ with $y=y_n$ (so $g(y_n)=\alpha$ and
$f(y_n)=y_{n+1}$):
$$|g(x)-\alpha|=|g(x)-g(y_n)|\le\frac{(x-f(y_n))^{2}}{2(x+y_n)}
=\frac{(x-y_{n+1})^{2}}{2(x+y_n)}
\le\frac{(\alpha/2)^{2}}{2(x+y_n)}
=\frac{\alpha^{2}}{8(x+y_n)}.$$
Since $y_n=y_0+n\alpha\ge y_0>0$, we have $x+y_n\ge x+y_0$, and therefore
$$0\le|g(x)-\alpha|\le\frac{\alpha^{2}}{8(x+y_0)}\qquad\forall\,x\ge y_0+\alpha.
\tag{8}$$
The right-hand side tends to $0$ as $x\to\infty$, proving the lemma. ∎

**Corollary 5.1 (positive values coincide).** *If $g$ takes a positive value,
then all its positive values are equal. Concretely: for any $a,b>0$ with
$g(a)>0$ and $g(b)>0$, $g(a)=g(b)$.*

*Proof.* By Lemma 5, $\lim_{x\to\infty}g(x)=g(a)$ and also
$=\,g(b)$. Uniqueness of limits gives $g(a)=g(b)$. ∎

Denote the common positive value (if it exists) by $\beta>0$.

---

### 6. $g$ is eventually constant on a tail ray

**Lemma 6.** *If $g$ takes a positive value $\beta>0$, then
$g\equiv\beta$ on $[X_0,\infty)$ for some $X_0>0$.*

*Proof.* By Lemma 5 (applied to any one point where $g=\beta$),
$g(x)\to\beta$ as $x\to\infty$. By Corollary 5.1 every positive value of $g$
equals $\beta$, and by (4) every value of $g$ is $\ge0$; hence the image of $g$
is contained in $\{0,\beta\}$. Take $\varepsilon=\beta/2>0$ in the definition of
$g(x)\to\beta$: there is $X_0$ such that for all $x\ge X_0$,
$|g(x)-\beta|<\beta/2$, i.e. $g(x)>\beta/2>0$. Since the image of $g$ lies in
$\{0,\beta\}$, this forces $g(x)=\beta$ for every $x\ge X_0$. ∎

---

### 7. No zeros: boundary contradiction (kills the "gap region")

We still must rule out the possibility that $g$ takes the value $0$ somewhere
while being $\beta>0$ on the tail. This is precisely the **gap region** of the
outline (points below $X_0$ that are not forced by the tail argument); the
squeeze kills it directly, with no monotonicity input.

**Lemma 7 (zero-set is open).** *If $g(a)=0$ for some $a>0$, then $g$ vanishes
on an open neighbourhood of $a$.*

*Proof.* $g(a)=0\Rightarrow f(a)=a$. Apply $(\star\star)$ with $y=a$:
$$|g(x)-g(a)|=|g(x)|\le\frac{(x-f(a))^{2}}{2(x+a)}=\frac{(x-a)^{2}}{2(x+a)}
\qquad\forall x>0.$$
The right-hand side tends to $0$ as $x\to a$, so $g(x)\to0=g(a)$: $g$ is
continuous at $a$. Since the image of $g$ lies in $\{0,\beta\}$ and
$g(x)\to0<\beta/2$, for $x$ sufficiently close to $a$ one has
$g(x)<\beta/2$, hence $g(x)=0$. ∎

**Lemma 8 (no zeros when $\beta>0$).** *If $g$ takes a positive value $\beta>0$,
then $g(x)>0$ for every $x>0$.*

*Proof.* Suppose, for contradiction, that $g(a)=0$ for some $a>0$. Let
$Z:=\{x>0:g(x)=0\}$. By Lemma 7, $Z$ is open; by Lemma 6, $Z\subseteq(0,X_0)$, so
$Z$ is bounded above and nonempty. Set $q:=\sup Z\le X_0$.

*Claim:* $q\notin Z$ and $g(q)=\beta$. Indeed, if $q\in Z$, then by Lemma 7 a
whole open neighbourhood of $q$ lies in $Z$, contradicting the definition of $q$
as the supremum of $Z$ (which would then be strictly larger). Hence $q\notin Z$,
so $g(q)\ne0$, and since the image of $g$ is in $\{0,\beta\}$ one gets
$g(q)=\beta$, i.e. $f(q)=q+\beta$.

By definition of the supremum of a set not containing its supremum, there is a
sequence $(x_n)\subset Z$ with $x_n\nearrow q$ (for every $\delta>0$,
$(q-\delta,q)\cap Z\ne\emptyset$, else $q-\delta$ would be a smaller upper
bound). For each $n$, $g(x_n)=0$ and $f(x_n)=x_n$.

Apply the master squeeze $(\star)$ with $x=x_n$ and $y=q$:
$$|g(x_n)-g(q)|\,\bigl(g(x_n)+g(q)+2x_n+2q\bigr)\le(x_n-f(q))^{2}.$$
Substituting $g(x_n)=0$, $g(q)=\beta$, $f(q)=q+\beta$:
$$\beta\,(\beta+2x_n+2q)\le(x_n-q-\beta)^{2}. \tag{9}$$
Let $n\to\infty$ (so $x_n\to q$). The left side tends to $\beta(\beta+4q)$ and
the right side to $(q-q-\beta)^{2}=\beta^{2}$. Passing to the limit in (9):
$$\beta(\beta+4q)\le\beta^{2}.$$
Since $\beta>0$, divide by $\beta$: $\beta+4q\le\beta$, i.e. $q\le0$. But
$q\ge x_n>0$ for all $n$, so $q>0$. Contradiction.

Therefore $Z=\emptyset$: $g$ has no zero. ∎

---

### 8. Conclusion of uniqueness

We collect the cases.

*Case 1.* $g$ takes no positive value. Then by (4) ($g\ge0$) one has $g\equiv0$,
i.e. $f(x)=x$ (the $c=0$ solution).

*Case 2.* $g$ takes a positive value. By Corollary 5.1 the common positive value
is $\beta>0$; by Lemma 6, $g\equiv\beta$ on a tail ray; by Lemma 8, $g$ has no
zero. Since every value of $g$ lies in $\{0,\beta\}$ and $0$ never occurs,
$g\equiv\beta$ on all of $\Rpos$. Hence $f(x)=x+\beta$.

In either case $g\equiv c$ for some $c\ge0$, i.e. $f(x)=x+c$ with $c\ge0$.

Together with Section 0 (every such $f$ works), the solutions of (H) are
exactly
$$\boxed{\,f(x)=x+c,\qquad c\ge0\,}.\qquad\blacksquare$$

---

### Notes on the route vs. the outline

- The outline's load-bearing gap (Step 3, *monotonicity of $f$*) is **not
  used**: it is replaced by the asymptotic pinning Lemma 5, which derives the
  limit at infinity purely from the master squeeze + the arithmetic orbit, with
  no monotonicity or continuity input. The "watch out for" warning
  ($f\ge\mathrm{id}$ does not imply monotone) is therefore moot.
- The outline's gap-region step (Step 5) is **closed** by Lemma 8: the zero set
  (which, if nonempty, lives entirely in the gap region $(0,X_0)$) is killed by a
  squeeze at its rightmost boundary point. This is the gap-region crossing
  mechanism, carried out in full.
- The "orbit mesh may be large" warning is handled by (8): the squeeze error is
  $O(\alpha^{2}/(x+y_0))$, which vanishes as $x\to\infty$ independently of the
  mesh size $\alpha$.
- No Kronecker equidistribution, no IVT, no attainment of $\inf g$, no
  monotonicity is invoked. The argument is: tight-point identity, codomain sign
  kill, SOS master squeeze, asymptotic pinning, boundary contradiction.

## Approaches tried
- (round 2, founding) Orbit-arithmetic + monotonicity sandwich. Open gaps
  flagged: monotonicity of $f$; gap region $(0,M]$.
- (round 2, build) Closed both flagged gaps by replacing monotonicity with an
  asymptotic pinning lemma (squeeze along the arithmetic orbit forces
  $g(x)\to g(y_0)$ at infinity, hence all positive values coincide) and closing
  the gap region by a boundary contradiction at $\sup\{g=0\}$. Full characterization
  $f(x)=x+c$, $c\ge0$ proved; verified by substitution. Status: solved.

## Current best
Full proof: the only solutions are $f(x)=x+c$, $c\ge0$. No open gaps.

## Promotable lemmas
- **Master squeeze (proved in Section 4).** Statement: for any solution $f$ of
  (H), writing $g(t)=f(t)-t\ge0$, for all $x,y>0$
  $$|g(x)-g(y)|\,\bigl(g(x)+g(y)+2x+2y\bigr)\;\le\;(x-f(y))^{2},$$
  equivalently $|g(x)-g(y)|\le(x-f(y))^{2}/(2x+2y)$. Mechanism: the squared gaps
  $A=(f(x)+y)^{2}-4xf(y)$, $B=2(x^{2}+f(y)^{2})-(f(x)+y)^{2}$ are both
  $\ge0$ by (H) and satisfy the SOS identity $A+B=2(x-f(y))^{2}$,
  $A-B=2(g(x)-g(y))(g(x)+g(y)+2x+2y)$; nonnegativity gives $|A-B|\le A+B$.
  Proved in `results/imo-2026-05/approaches/orbit-monotonicity-sandwich.md`,
  Section 4. Load-bearing for the whole field; importable by the other
  approaches in place of re-derivation.
- **Asymptotic pinning (proved in Section 5).** Statement: under (H) with
  $g=f-\mathrm{id}\ge0$ and orbit invariance $g(f(y))=g(y)$, if $g(y_0)=\alpha>0$
  then $\lim_{x\to\infty}g(x)=\alpha$; consequently all positive values of $g$
  coincide. Mechanism: squeeze along the arithmetic orbit
  $y_n=y_0+n\alpha$ choosing the lattice point nearest $x$, giving
  $|g(x)-\alpha|\le\alpha^{2}/(8(x+y_0))\to0$. Proved in Section 5.
