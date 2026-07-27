# IMO 2026 Problem 5 — current tracking

## Problem
Let $\Rpos$ be the set of positive real numbers. Determine all functions $f:\Rpos\to\Rpos$ such that
$$\sqrt{\frac{x^2+f(y)^2}{2}}\ge \frac{f(x)+y}{2}\ge \sqrt{xf(y)}$$
for every $x,y\in\Rpos$.

## Status
solved

## Approaches tried
- (round 2) **orbit-monotonicity-sandwich** — VERIFIED SOLVED. Self-contained
  proof: orbit invariance $g(f(y))=g(y)$; codomain sign kill $g\ge0$; master
  squeeze (SOS, proven in-file); asymptotic pinning along the arithmetic orbit
  forces $\lim_{x\to\infty}g(x)=\alpha$ for every positive value $\alpha$ of $g$,
  hence all positive values coincide at a single $\beta$; $g\equiv\beta$ on a
  tail ray; boundary contradiction at $q=\sup\{g=0\}$ kills any zero
  ($\beta(\beta+4q)\le\beta^2\Rightarrow q\le0$, contradicting $q>0$). All cases
  covered. APPROVE.
- (round 2) **master-sos-identity** — partial. Proves and certifies the
  Master Squeeze Lemma (both directions, sympy-verified, certified into
  `lemmas/master-squeeze.md`). The direct algebraic kill from the squeeze plus
  $g\ge0$ alone is honestly flagged open (sub-routes need regularity not given;
  optimization "bound" retracted as a non-result). CHANGES REQUESTED.
- (round 2) **density-contradiction** — partial. Correct weaker squeeze
  (independently derived, denominator bounded below by $a+b$ correctly defuses
  the Kronecker rate concern) and correct rational-ratio R1/R2 kill. Two gaps:
  (A) irrational-case target $c_0=a+\alpha-b$ is off by $\alpha$ (should be
  $a-b$), so as written the cross-distance tends to $\alpha\ne0$, not $0$;
  (B) Stage B's $a-b\in\beta\mathbb Z$, $k\le-1$ sub-case has a sign error
  ($a=b-(-k)\beta<b$, so $a\notin$ forward orbit $B$); the propagation
  argument (which is case-independent) fixes it but is not applied there as
  written. Also erroneously rejects the master squeeze as false (it is a true
  theorem equivalent to the chain); this does not propagate since the proof
  uses its own weaker squeeze. CHANGES REQUESTED.

## Current best
Full verified solution: $f(x)=x+c$, $c\ge0$, proven by the
orbit-monotonicity-sandwich approach (self-contained). The Master Squeeze
Lemma (equivalence of the chain to the squeeze, both directions) is certified
in `lemmas/master-squeeze.md` and importable.

## Full proof

The solutions are exactly $f(x)=x+c$ with $c\ge0$.

### 0. The candidate family works (exhibit + verify)

For $f(x)=x+c$ with $c\ge0$, $f(y)=y+c$, so $\frac{f(x)+y}{2}=\frac{x+f(y)}{2}$,
the arithmetic mean of the pair $(x,f(y))$. The chain becomes the classical
$$\sqrt{\frac{x^{2}+f(y)^{2}}{2}}\ge\frac{x+f(y)}{2}\ge\sqrt{x\,f(y)},$$
i.e. QM$\ge$AM$\ge$GM for the two positive numbers $x$ and $f(y)$
(knowledge_base: Standard inequalities — AM-GM, QM-AM; equality iff $x=f(y)$).
Hence every $f(x)=x+c$, $c\ge0$, is a solution.

### 1. Square form

Set $A:=(f(x)+y)^{2}-4xf(y)$, $B:=2(x^{2}+f(y)^{2})-(f(x)+y)^{2}$. The
hypothesis is $A\ge0\land B\ge0$ for all $x,y>0$.

### 2. Orbit invariance

Define $g(t)=f(t)-t$. Substituting $x=f(y)$ collapses the chain to equality,
forcing $f(f(y))=2f(y)-y$, i.e. $g(f(y))=g(y)$. Iterating, $g(f^{n}(y))=g(y)$.

### 3. Nonnegativity $g\ge0$

The forward orbit $y_{n}=f^{n}(y)=y+n\,g(y)$ is an arithmetic progression; each
$y_{n}>0$ (codomain). If $g(y)<0$, then $y_{n}\to-\infty$, eventually $\le0$,
contradiction. So $g\ge0$ everywhere.

### 4. Master squeeze

With $f(x)=x+g(x)$, $f(y)=y+g(y)$:
$$A+B=2(x-f(y))^{2},\qquad
A-B=2\,(g(x)-g(y))\bigl(g(x)+g(y)+2x+2y\bigr).$$
(Both are direct polynomial expansions — completing the square; verified
symbolically.) Since $A,B\ge0$, $|A-B|\le A+B$:
$$\bigl|(g(x)-g(y))\bigl(g(x)+g(y)+2x+2y\bigr)\bigr|\le(x-f(y))^{2}.\qquad(\star)$$
By $g\ge0$, the second factor is $\ge2x+2y>0$, giving
$$|g(x)-g(y)|\le\frac{(x-f(y))^{2}}{2x+2y}.\qquad(\star\star)$$
(Equivalence to the original chain, both directions, is certified in
`lemmas/master-squeeze.md`.)

### 5. Asymptotic pinning

**Lemma.** If $g(y_{0})=\alpha>0$, then $\lim_{x\to\infty}g(x)=\alpha$.

*Proof.* The orbit $y_{n}=y_{0}+n\alpha$ carries $g(y_{n})=\alpha$ and
$f(y_{n})=y_{n+1}$. For $x\ge y_{0}+\alpha$, choose $n\ge0$ with
$y_{n+1}=y_{0}+(n+1)\alpha$ a nearest lattice point to $x$; then
$|x-y_{n+1}|\le\alpha/2$ (the lattice $\{y_{0}+m\alpha\}_{m\ge1}$ covers
$[y_{0}+\alpha/2,\infty)$ within $\alpha/2$). Apply $(\star\star)$ with
$y=y_{n}$:
$$|g(x)-\alpha|=|g(x)-g(y_{n})|\le\frac{(x-f(y_{n}))^{2}}{2(x+y_{n})}
=\frac{(x-y_{n+1})^{2}}{2(x+y_{n})}\le\frac{(\alpha/2)^{2}}{2(x+y_{0})}
=\frac{\alpha^{2}}{8(x+y_{0})}\xrightarrow[x\to\infty]{}0.\quad\square$$

**Corollary.** All positive values of $g$ coincide: if $g(a)>0$, $g(b)>0$,
then $\lim g=g(a)=g(b)$. Denote the common value $\beta>0$.

### 6. $g$ is eventually constant on a tail

By $g\ge0$ and the corollary, $g(\Rpos)\subseteq\{0,\beta\}$. Since
$g(x)\to\beta$, take $\varepsilon=\beta/2$: for $x\ge X_{0}$, $|g(x)-\beta|<\beta/2$,
so $g(x)>\beta/2>0$, forcing $g(x)=\beta$ on $[X_{0},\infty)$.

### 7. No zeros when $\beta>0$ (boundary contradiction)

If $g(a)=0$: $f(a)=a$, and $(\star\star)$ with $y=a$ gives
$|g(x)|\le(x-a)^{2}/(2(x+a))\to0$ as $x\to a$; so $g$ is continuous at $a$ with
value $0$, and (image in $\{0,\beta\}$) $g\equiv0$ on a neighborhood of $a$.
Thus $Z=\{g=0\}$ is open; and $Z\subseteq(0,X_{0})$ (bounded above).

Suppose $Z\ne\emptyset$. Set $q=\sup Z\le X_{0}$. Then $q\notin Z$ (else a
neighborhood of $q$ lies in $Z$, contradicting the supremum), so $g(q)=\beta$,
$f(q)=q+\beta$. Pick $(x_{n})\subset Z$ with $x_{n}\nearrow q$ ($g(x_{n})=0$,
$f(x_{n})=x_{n}$). Apply $(\star)$ with $x=x_{n}$, $y=q$:
$$\beta\,(\beta+2x_{n}+2q)\le(x_{n}-q-\beta)^{2}.$$
Let $n\to\infty$: LHS $\to\beta(\beta+4q)$, RHS $\to\beta^{2}$, giving
$\beta(\beta+4q)\le\beta^{2}$, i.e. $q\le0$ — contradicting $q\ge x_{n}>0$. So
$Z=\emptyset$.

### 8. Conclusion

*Case 1.* $g$ takes no positive value: by $g\ge0$, $g\equiv0$, i.e. $f(x)=x$.
*Case 2.* $g$ takes a positive value: $g\equiv\beta>0$ on the tail (Section 6)
and has no zero (Section 7), so $g\equiv\beta$ on all of $\Rpos$.

In either case $g\equiv c$ for some $c\ge0$, i.e. $f(x)=x+c$. Together with
Section 0, the solutions are exactly
$$\boxed{\,f(x)=x+c,\qquad c\ge0\,}.\qquad\blacksquare$$
