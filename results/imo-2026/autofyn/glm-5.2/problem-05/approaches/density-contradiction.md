# Approach: density-contradiction

## Status
solved

## Target
Prove the full characterization: the solutions are exactly $f(x)=x+c$, $c\ge0$.
This approach proves **uniqueness** by contradiction, using the arithmetic-orbit
structure ($g\circ f=g$, $g\ge0$) plus a squeeze lemma
$|g(x)-g(y)|\le(x-f(y))^{2}/(x+f(y))$ derived from the two classical
QM-AM / AM-GM gaps. Two distinct positive values of $g$ are ruled out by a
Kronecker-density (irrational-ratio) argument and a commensurate-coset
(rational-ratio) argument; the remaining possibility that $g$ also attains
$0$ alongside a positive value is ruled out by propagation of the zero set
using the squeeze and the already-proved two-valued structure, followed by
intersection with the unbounded forward orbit of a positive-$g$ point. No
global monotonicity or continuity is used.

## Technique
Arithmetic-orbit invariance + classical-inequality squeeze +
Kronecker/equidistribution density (irrational ratio) and
commensurate-coset/growing-denominator kill (rational ratio) + zero-set
propagation + orbit intersection. Number-theoretic/dynamical framing
(distinct from monotonicity).

## Approaches tried
- (round 2, founding) Density/equidistribution contradiction via Kronecker.
  Initially flagged gaps: squeeze-neighborhood landing (irrational case) and the
  commensurate (rational-ratio) sub-case.
- (round 2, build) Full proof written. Key realizations: (i) the squeeze
  $|g(x)-g(y)|\le(x-f(y))^{2}/(x+f(y))$ has a denominator bounded below by a
  fixed positive constant $a+b>0$ at cross-orbit pairs, so the irrational case
  needs no rate/Diophantine-approximation argument beyond Kronecker density;
  (ii) the rational case splits into R1 (orbits in the same $d\mathbb Z$-coset,
  hence intersect $\Rightarrow\alpha=\beta$) and R2 (different cosets, where the
  minimum cross-distance $\rho>0$ is attained by infinitely many $(m,n)\to\infty$
  with denominator $\to\infty$, forcing the squeeze RHS $\to0$); (iii) once two
  distinct positive $g$-values are excluded, $g$ takes values in $\{0,\beta\}$,
  and if $0$ is attained alongside $\beta>0$ the zero set propagates rightward
  to a tail ray, intersecting the unbounded forward orbit of $b$ (where
  $g=\beta$), contradiction.
- (round 3, build) Closed the two gaps diagnosed by the round-2 reviewer.
  **Gap A (irrational target off by $\alpha$):** the cross-distance is
  $D=b-a+m\beta-(n+1)\alpha$ (because $f(y)=a+(n+1)\alpha$), so the Kronecker
  target must be $c_{0}=a-b$, NOT $a+\alpha-b$. Fixed $c_{0}$ to $a-b$ throughout
  Section 6; now $D\to0$ (sympy-verified: with $c_{0}=a-b$, $D\to0$; with the old
  $c_{0}=a+\alpha-b$, $D\to\alpha\ne0$). **Gap B (Stage B sign error):** the
  sub-case $a-b\in\beta\mathbb Z$ with $k\le-1$ had $a=b-|k|\beta<b$, so $a$ is
  NOT in the upward forward orbit of $B$; the orbit-membership kill fails there.
  Fixed by dropping the case split entirely and running the (case-independent)
  zero-set propagation rightward to a tail ray $[u,\infty)$, then intersecting
  the unbounded forward orbit $\{b+m\beta:m\ge0\}$ (on which $g\equiv\beta$ by
  invariance), giving the contradiction for EVERY $a$ with $g(a)=0$, regardless
  of the residue $a-b\bmod\beta$. Propagation step size
  $\eta_{+}(v)=\frac{\beta+\sqrt{\beta^{2}+8v\beta}}{2}>\sqrt{2v\beta}\to\infty$,
  so $v_{n}\to\infty$ in finitely-bounded many steps is replaced by the
  constant lower bound $\eta_{+}(v)\ge\sqrt{2u\beta}>0$ forcing $v_{n}\to\infty$.
  Also retracted the round-2 erroneous rejection of the (true) Master Squeeze
  Lemma; this proof keeps its own weaker squeeze for self-containment but
  acknowledges `lemmas/master-squeeze.md` as a certified equivalent.
- (round 3, follow-up) Fixed a pre-existing off-by-one indexing error in
  Section 7 R2 (flagged on re-audit after Gaps A/B were certified closed).
  The cross-distance $D_{m,n}=(b-a)+d(mq-(n+1)p)$ uses orbit index $m$ (for
  $x=b+m\beta$) and image index $n+1$ (for $f(y)=a+(n+1)\alpha$); the Bézout
  equation must use the SAME indices, $(n+1)p-mq=k^{*}$, not
  $(n+1)p-(m+1)q=k^{*}$ (which mixes orbit index $m$ with image index $m+1$ and
  inserts a spurious $-dq$ term, turning $|D_{m,n}|$ from $\rho$ into
  $|\rho\pm dq|$). Re-indexed to the consistent equation; sympy-verified that
  under $(n+1)p-mq=k^{*}$ the cross-distance reduces to $-\sigma\rho$, hence
  $|D_{m,n}|=\rho$ exactly. The conclusion (fixed positive numerator,
  denominator $\to\infty$, bound $\to0$) is robust to the slip, but the written
  algebra is now correct.

## Current best
Complete characterization proved: $f(x)=x+c$, $c\ge0$. No residual gaps.

## Full proof

We prove that the functions $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfying
$$\sqrt{\frac{x^{2}+f(y)^{2}}{2}}\;\ge\;\frac{f(x)+y}{2}\;\ge\;\sqrt{x\,f(y)}
\qquad(\star)\qquad\forall\,x,y>0$$
are exactly $f(x)=x+c$ with $c\ge0$.

---

### 0. Notation and the classical-inequality window

Set $a=x$ and $b=f(y)$, and write
$$\mathrm{QM}=\sqrt{\tfrac{a^{2}+b^{2}}{2}},\qquad
\mathrm{AM}=\tfrac{a+b}{2},\qquad
\mathrm{GM}=\sqrt{ab}=\sqrt{x\,f(y)}.$$
The classical chain is $\mathrm{QM}\ge\mathrm{AM}\ge\mathrm{GM}$
(knowledge_base: Standard inequalities — AM-GM, QM-AM), with equality
throughout iff $a=b$, i.e. iff $x=f(y)$. Define the displacement
$$g(t):=f(t)-t\qquad(t>0).$$
Since $f(x)+y=x+g(x)+y$ and $x+f(y)=x+y+g(y)$,
$$\frac{f(x)+y}{2}=\frac{x+f(y)}{2}+\frac{g(x)-g(y)}{2}
=\mathrm{AM}+\frac{g(x)-g(y)}{2}.$$
Thus $(\star)$ is precisely the statement that the deviation
$s:=g(x)-g(y)$ satisfies
$$-2L\;\le\;s\;\le\;2U,\qquad
U:=\mathrm{QM}-\mathrm{AM}\ge0,\quad L:=\mathrm{AM}-\mathrm{GM}\ge0.$$
(Left inequality $\mathrm{AM}+s/2\le\mathrm{QM}\Leftrightarrow s\le2(\mathrm{QM}-\mathrm{AM})=2U$;
right inequality $\mathrm{AM}+s/2\ge\mathrm{GM}\Leftrightarrow s\ge-2(\mathrm{AM}-\mathrm{GM})=-2L$.)

---

### 1. The candidate family is admissible

Let $f(x)=x+c$ with $c\ge0$, so $g\equiv c$ and $f(y)=y+c$. Then
$\frac{f(x)+y}{2}=\frac{x+y+c}{2}=\frac{x+f(y)}{2}=\mathrm{AM}$ (the deviation
$s=g(x)-g(y)=0$ vanishes), and $(\star)$ reduces to the classical chain
$\mathrm{QM}\ge\mathrm{AM}\ge\mathrm{GM}$ for the pair $(x,y+c)$, which holds for
all $x,y>0$. Hence every $f(x)=x+c$, $c\ge0$, is a solution.

---

### 2. Orbit invariance $g(f(y))=g(y)$

Take $x=f(y)$ in $(\star)$. Then the pair is $(a,b)=(f(y),f(y))$, so
$\mathrm{QM}=\mathrm{AM}=\mathrm{GM}=f(y)$, and the window collapses to a point;
$(\star)$ forces $\frac{f(f(y))+y}{2}=f(y)$, i.e.
$$f(f(y))=2f(y)-y.$$
Subtracting $f(y)$ from both sides gives
$$g(f(y))=f(f(y))-f(y)=f(y)-y=g(y).\qquad(\dagger)$$
(This also follows from the certified Master Squeeze Lemma
`results/imo-2026-05/lemmas/master-squeeze.md` by setting $x=f(y)$, which
makes the RHS $=0$; we give the direct classical-inequality derivation for
self-containment.)

---

### 3. Sign: $g\ge0$ everywhere

By $(\dagger)$ the displacement is invariant under forward iteration:
$g(f^{n}(y))=g(y)$ for all $n\ge0$. Writing $y_{n}=f^{n}(y)$, we have
$y_{n+1}=f(y_{n})=y_{n}+g(y_{n})=y_{n}+g(y)$, hence
$$y_{n}=y+n\,g(y)\qquad(n\ge0).$$
Each $y_{n}=f^{n}(y)$ lies in $\mathbb R_{>0}$ (the codomain). If $g(y)<0$, then
$y_{n}=y+n\,g(y)\to-\infty$, so for large $n$ we have $y_{n}\le0$, contradicting
$y_{n}>0$. Therefore
$$g(y)\ge0\qquad\forall\,y>0.\qquad(\ddagger)$$

---

### 4. The squeeze lemma

**Lemma (squeeze).** For all $x,y>0$,
$$\boxed{\,|g(x)-g(y)|\;\le\;\frac{(x-f(y))^{2}}{x+f(y)}\,}.\qquad(\S)$$

*Proof.* We bound each of the two classical gaps. Put $a=x$, $b=f(y)$.

*Upper bound $2U$.* Rationalizing,
$$2U=\sqrt{2(a^{2}+b^{2})}-(a+b)
   =\frac{2(a^{2}+b^{2})-(a+b)^{2}}{\sqrt{2(a^{2}+b^{2})}+(a+b)}
   =\frac{(a-b)^{2}}{\sqrt{2(a^{2}+b^{2})}+(a+b)}
   \le\frac{(a-b)^{2}}{a+b},$$
since $\sqrt{2(a^{2}+b^{2})}\ge0$ and $a+b>0$.

*Lower bound $2L$.* By the difference of two squares,
$$2L=(a+b)-2\sqrt{ab}=(\sqrt a-\sqrt b)^{2}
    =\frac{(a-b)^{2}}{(\sqrt a+\sqrt b)^{2}}
    \le\frac{(a-b)^{2}}{a+b},$$
since $(\sqrt a+\sqrt b)^{2}=a+b+2\sqrt{ab}\ge a+b$.

From $(\star)$ we have $s=g(x)-g(y)\le2U$ and $-s\le2L$.
If $s\ge0$: $|s|=s\le2U\le\frac{(a-b)^{2}}{a+b}=\frac{(x-f(y))^{2}}{x+f(y)}$.
If $s\le0$: $|s|=-s\le2L\le\frac{(x-f(y))^{2}}{x+f(y)}$.
In either case $(\S)$ holds. $\square$

A direct corollary of $(\S)$: at every *image point* $f(y)$, the displacement
$g$ is continuous with value $g(y)$, with quadratic modulus, since
$|g(x)-g(y)|\le(x-f(y))^{2}/(x+f(y))\to0$ as $x\to f(y)$ (the denominator
$x+f(y)\to2f(y)>0$ stays bounded away from $0$).

*Remark (relation to the Master Squeeze).* The certified Master Squeeze Lemma
(`lemmas/master-squeeze.md`) gives the sharper (equivalent-to-the-chain) bound
$|g(x)-g(y)|\le(x-f(y))^{2}/(2x+2y)$. Round 2 of this approach erroneously
rejected that lemma as false; that rejection was an error (the lemma is a true
theorem, equivalent to the chain both directions — see the reviewer's
adjudication). The weaker bound $(\S)$ derived above is fully sufficient for
this proof and is self-contained, so we keep it; no step below relies on the
sharper master form.

---

### 5. Set-up for the contradiction

Assume $g$ is not constant. We will derive a contradiction in two stages.
Stage A (Sections 6–7) rules out two distinct **positive** values of $g$;
Stage B (Section 8) rules out the value $0$ coexisting with a positive value.
Together they force $g$ constant.

---

### 6. Stage A, irrational-ratio case

Suppose $g(a)=\alpha>0$ and $g(b)=\beta>0$ with $\alpha\ne\beta$ and
$\alpha/\beta\notin\mathbb Q$. By $(\dagger)$ and the AP formula of Section 3,
$$A:=\{a+n\alpha:n\ge0\},\qquad B:=\{b+m\beta:m\ge0\}$$
are the forward orbits, with $g\equiv\alpha$ on $A$ and $g\equiv\beta$ on $B$.
The image points of $A$ are $f(a+n\alpha)=a+n\alpha+\alpha=a+(n+1)\alpha$.

Apply the squeeze $(\S)$ with $y=a+n\alpha\in A$ (so $f(y)=a+(n+1)\alpha$,
$g(y)=\alpha$) and $x=b+m\beta\in B$ (so $g(x)=\beta$):
$$|\beta-\alpha|\;\le\;\frac{\bigl(b+m\beta-a-(n+1)\alpha\bigr)^{2}}
                             {b+m\beta+a+(n+1)\alpha}.\qquad(\star\star)$$
The denominator satisfies
$$b+m\beta+a+(n+1)\alpha\;\ge\;a+b\;>0$$
for all $m,n\ge0$. Hence $(\star\star)$ gives
$$|\beta-\alpha|\;\le\;\frac{D_{m,n}^{2}}{a+b},
\qquad D_{m,n}:=b-a+m\beta-(n+1)\alpha.\qquad(\star\star\star)$$

**Claim.** For every $\varepsilon>0$ there exist $m,n\ge0$ with
$|D_{m,n}|<\varepsilon$, i.e.
$$\bigl|m\beta-(n+1)\alpha-(a-b)\bigr|<\varepsilon.$$

*Proof of claim.* Set $c_{0}:=a-b$ (any real target — Kronecker makes no
restriction on the target phase). We must realize $m\beta-(n+1)\alpha$ within
$\varepsilon$ of $c_{0}$ with $m,n\ge0$. Put $\gamma:=\beta/\alpha\notin\mathbb
Q$; dividing the target by $\alpha>0$, the condition becomes: find
$m,n\ge0$ with $|m\gamma-(n+1)-c_{0}/\alpha|<\varepsilon/\alpha$, i.e.
$|m\gamma - N - c_{0}/\alpha|<\varepsilon/\alpha$ where $N:=n+1\ge1$ is an
integer. Equivalently, on the circle $\mathbb R/\mathbb Z$, we need
$|\{m\gamma\}-\{c_{0}/\alpha\}|<\varepsilon/\alpha$ for some $m\ge0$ with
$m\gamma\ge c_{0}/\alpha$ (so that the integer part
$N:=\lceil m\gamma-c_{0}/\alpha\rceil\ge1$ and $n:=N-1\ge0$).

By the **Kronecker / Weyl equidistribution theorem** (knowledge_base:
"Kronecker / Weyl equidistribution" — for irrational $\gamma$, the sequence
$\{m\gamma\}_{m\ge0}$ is dense in $[0,1)$; indeed equidistributed), the set
$\{m\gamma:m\ge0\}$ visits every subinterval of $[0,1)$ infinitely often.
Hence there are arbitrarily large $m$ with
$|\{m\gamma\}-\{c_{0}/\alpha\}|<\varepsilon/\alpha$; choosing $m$ large enough
also ensures $m\gamma\ge c_{0}/\alpha$ (the orbit $m\gamma$ is unbounded above
since $\gamma>0$), so the associated $N=\lceil m\gamma-c_{0}/\alpha\rceil\ge1$
and $n=N-1\ge0$. For such $(m,n)$,
$$|D_{m,n}|=\bigl|(b-a)+m\beta-(n+1)\alpha\bigr|
          =\bigl|m\beta-(n+1)\alpha-c_{0}\bigr|<\varepsilon.$$
(Indeed $c_{0}=a-b$, so $(b-a)-c_{0}=(b-a)-(a-b)=0$.) $\square_{\text{claim}}$

Feeding into $(\star\star\star)$,
$$|\beta-\alpha|<\frac{\varepsilon^{2}}{a+b}.$$
Since $\varepsilon>0$ was arbitrary and $a+b>0$ is fixed, this forces
$|\beta-\alpha|=0$, i.e. $\alpha=\beta$, contradicting $\alpha\ne\beta$.
(Diophantine-approximation rate is irrelevant here: the denominator is bounded
*below* by $a+b$, so *any* arbitrarily small landing distance gives the
contradiction; Kronecker density supplies it directly.) Hence the
irrational-ratio case cannot occur.

---

### 7. Stage A, rational-ratio case

Suppose $g(a)=\alpha>0$, $g(b)=\beta>0$, $\alpha\ne\beta$, with
$\alpha/\beta=p/q\in\mathbb Q$ in lowest terms, $p,q\in\mathbb Z_{>0}$,
$\gcd(p,q)=1$. Then $\alpha=pd$, $\beta=qd$ for $d:=\alpha/p=\beta/q>0$.
Both orbit image-point sets
$$A'=\{a+(n+1)pd:n\ge0\}\subset a+d\mathbb Z,\qquad
  B'=\{b+(m+1)qd:m\ge0\}\subset b+d\mathbb Z.$$

#### Sub-case R1: $a-b\in d\mathbb Z$ (same coset)

The two image-point sets lie in the *same* coset. We show they intersect.
Differences of elements take the form
$$A'-B'=\{(a-b)+d\bigl((n+1)p-(m+1)q\bigr):m,n\ge0\}.$$
The integer $k=(n+1)p-(m+1)q$ ranges over all of $\mathbb Z$ as $m,n\ge0$ vary:
for any $k_{0}\in\mathbb Z$, the congruence $(m+1)q\equiv-k_{0}\pmod p$ (solvable
since $\gcd(q,p)=1$) gives a residue class $m\equiv m_{0}\pmod p$; taking
$m=m_{0}+tp$ with $t$ large yields $n=(k_{0}+(m+1)q)/p-1\ge0$. In particular
$k$ attains $k^{*}:=-(a-b)/d\in\mathbb Z$, whereupon
$a-b+dk^{*}=0$, i.e. some $A'$-point equals some $B'$-point: call it $z$.
Then $z=a+(n+1)\alpha\in A$ (so $g(z)=\alpha$ by orbit invariance) and
$z=b+(m+1)\beta\in B$ (so $g(z)=\beta$). Hence $\alpha=\beta$, contradiction.

#### Sub-case R2: $a-b\notin d\mathbb Z$ (distinct cosets)

Define the **coset residue**
$$\rho:=\min_{k\in\mathbb Z}|a-b+dk|\;\in\;(0,d/2]$$
(positive because $a-b\notin d\mathbb Z$), attained at some $k^{*}\in\mathbb Z$:
$a-b+dk^{*}=\sigma\rho$ for a sign $\sigma\in\{+1,-1\}$, equivalently
$b-a=dk^{*}-\sigma\rho$. We produce infinitely many $(m,n)\ge0$, arbitrarily
large, with the cross-distance in $(\star\star)$ of modulus $\rho$.

Recall the cross-distance in $(\star\star)$ is (with $x=b+m\beta$ the orbit
point of $B$, index $m$; and $f(y)=a+(n+1)\alpha$ the image of the orbit point
$a+n\alpha$ of $A$, image index $n+1$)
$$D_{m,n}:=b-a+m\beta-(n+1)\alpha=(b-a)+d\bigl(mq-(n+1)p\bigr).$$
To make $D_{m,n}=\pm\rho$ we need $mq-(n+1)p=-k^{*}$, i.e. the **Bézout
equation on the same indices that appear in $D_{m,n}$** (orbit index $m$ on the
$B$-side, image index $n+1$ on the $A$-side — no index shift):
$$\boxed{\,(n+1)p-mq=k^{*}\,}.$$
(Indexing consistency is essential here: a round-2 version wrote
$(n+1)p-(m+1)q=k^{*}$, mixing the orbit index $m$ of $D_{m,n}$ with the image
index $m+1$ in the Bézout equation; that mismatch inserts a spurious $-dq$
term, turning $|D_{m,n}|$ from $\rho$ into $|\rho\pm dq|$. The corrected
equation above keeps both indices aligned and gives $|D_{m,n}|=\rho$ exactly.
The conclusion is robust to the slip in any case, since $|\rho\pm dq|$ is still
a fixed positive constant — but the clean identity is $|D_{m,n}|=\rho$.)

Solvability. The congruence $mq\equiv -k^{*}\pmod p$ is solvable since
$\gcd(q,p)=1$: it gives a residue $m\equiv m_{0}\pmod p$ with
$m_{0}\in\{0,\dots,p-1\}$. Write $m=m_{0}+tp$ ($t\ge0$); then
$$n+1=\frac{k^{*}+mq}{p}\in\mathbb Z$$
(by the congruence), and $n=\frac{k^{*}+mq}{p}-1\to\infty$ as $t\to\infty$,
with $n\ge0$ for all large $t$; simultaneously $m=m_{0}+tp\to\infty$. Hence
there are infinitely many admissible $(m,n)\to\infty$ satisfying the Bézout
equation.

For every such pair,
$$D_{m,n}=(b-a)+d(mq-(n+1)p)=(dk^{*}-\sigma\rho)+d(-k^{*})=-\sigma\rho,$$
so $|D_{m,n}|=\rho$ (sympy-verified: under $(n+1)p-mq=k^{*}$, the
substitution $b-a=dk^{*}-\sigma\rho$ reduces $D_{m,n}$ to $-\sigma\rho$).
Substituting into $(\star\star)$ along this subsequence,
$$|\beta-\alpha|\;\le\;\frac{D_{m,n}^{2}}{b+m\beta+a+(n+1)\alpha}
=\frac{\rho^{2}}{b+m\beta+a+(n+1)\alpha}
\;\xrightarrow[m,n\to\infty]{}\;0,$$
since the denominator $\to+\infty$ (both $m\beta$ and $(n+1)\alpha$ grow) while
$\rho^{2}>0$ is fixed. Thus $\alpha=\beta$, contradiction.

Both sub-cases of the rational ratio are excluded. Combined with Section 6
(irrational ratio), **no two distinct positive values of $g$ can coexist**:
there exists $\beta\ge0$ with
$$g(\mathbb R_{>0})\subseteq\{0,\beta\}.\qquad(\bullet)$$

---

### 8. Stage B: ruling out $0$ alongside a positive value

Assume $\beta>0$ and that $g$ attains $0$ (say $g(a)=0$, so $f(a)=a$) as well
as $\beta$ (say $g(b)=\beta$, so the forward orbit
$B=\{b+m\beta:m\ge0\}$ carries $g\equiv\beta$ by $(\dagger)$ and is unbounded
above). We derive a contradiction by a case-independent propagation argument.

**(i) Base case: a non-degenerate zero-interval around $a$.**
Since $g(a)=0$, $a$ is an image point: $f(a)=a$. The squeeze $(\S)$ with $y=a$
gives, for every $x>0$,
$$g(x)=|g(x)-g(a)|\le\frac{(x-a)^{2}}{x+a}.\qquad(\S_{a})$$
The right-hand side $\to0$ as $x\to a$, so by the image-point continuity
corollary of Section 4, $g$ is continuous at $a$ with value $0$. By the
two-valued structure $(\bullet)$, $g(x)\in\{0,\beta\}$; choose
$\delta\in(0,a)$ such that $(x-a)^{2}/(x+a)<\beta$ whenever $|x-a|<\delta$ and
$x>0$ (possible since the bound $\to0$). Then for every $x\in(a-\delta,a+\delta)$
we have $g(x)<\beta$, and the only value of $g$ strictly below $\beta$ in
$\{0,\beta\}$ is $0$. Hence
$$g\equiv0\quad\text{on }I_{0}:=(a-\delta,a+\delta),$$
a non-degenerate interval. Pick any closed non-degenerate
$[u_{0},v_{0}]\subset I_{0}$ with $0<u_{0}<a<v_{0}$.

**(ii) Rightward propagation step.**
Suppose $g\equiv0$ on a non-degenerate interval $[u,v]$ with $0<u\le v$.
Then $f(v)=v$ (since $g(v)=0$), and $v$ is an image point. Apply $(\S)$ with
$y=v$ and $x=v+\eta$ ($\eta>0$):
$$g(v+\eta)=|g(v+\eta)-g(v)|\le\frac{\eta^{2}}{(v+\eta)+v}=\frac{\eta^{2}}{2v+\eta}.$$
The function $\eta\mapsto\eta^{2}/(2v+\eta)$ is strictly increasing for $\eta>0$
(derivative $\eta(4v+\eta)/(2v+\eta)^{2}>0$) and equals $0$ at $\eta=0$. Its
unique positive solution to $=\beta$ is
$$\eta_{+}(v)=\frac{\beta+\sqrt{\beta^{2}+8v\beta}}{2}.$$
Hence for every $0<\eta<\eta_{+}(v)$ we have
$g(v+\eta)<\beta$, and by $(\bullet)$ again $g(v+\eta)=0$. Thus
$$g\equiv0\quad\text{on }[v,\,v+\eta_{+}(v)),$$
so the zero-interval extends rightward to $[u,\,v+\eta_{+}(v))$ (more precisely,
to any $[u,v']$ with $v'<v+\eta_{+}(v)$).

**(iii) Rightward propagation reaches $+\infty$.**
Iterate (ii): starting from $[u_{0},v_{0}]$, define
$v_{n+1}=v_{n}+\eta_{+}(v_{n})$ (or any value below it). We claim $v_{n}\to+\infty$.
Indeed,
$$\eta_{+}(v)=\frac{\beta+\sqrt{\beta^{2}+8v\beta}}{2}>\sqrt{2v\beta}\ge\sqrt{2u\beta}>0,$$
since $\eta_{+}(v)^{2}-2v\beta=\tfrac{\beta^{3/2}\sqrt{\beta+8v}}{2}+\tfrac{\beta^{2}}{2}>0$
(direct expansion) and $v\ge u$ throughout (the interval only grows rightward).
Each step advances by at least the positive constant $\sqrt{2u\beta}$, hence
$v_{n}\to+\infty$. Consequently
$$g\equiv0\quad\text{on }[u_{0},\infty).\qquad(\diamond)$$

**(iv) Contradiction via orbit intersection.**
The forward orbit of $b$ is $B=\{b+m\beta:m\ge0\}$, unbounded above, with
$g\equiv\beta$ on $B$ by orbit invariance $(\dagger)$. Choose $m$ large enough
that $b+m\beta\ge u_{0}$ (possible since $B$ is unbounded above). By $(\diamond)$,
$g(b+m\beta)=0$; by orbit invariance, $g(b+m\beta)=g(b)=\beta>0$. This is a
contradiction.

Hence $0$ cannot coexist with a positive value: if $\beta>0$ is attained then
$g$ has no zero.

*Remark on the dropped case split.* Round 2 split Stage B on
$a-b\bmod\beta\mathbb Z$ and attempted an orbit-membership kill when
$a-b\in\beta\mathbb Z$. That sub-argument had a sign error for $k\le-1$ (where
$a=b+k\beta<b$, so $a$ is NOT in the upward forward orbit of $b$). The
propagation + orbit-intersection argument above is **case-independent**: it
works for every $a$ with $g(a)=0$ regardless of the residue
$a-b\bmod\beta$, and it supersedes the broken case split entirely.

---

### 9. Conclusion of uniqueness

By Stage A, all positive values of $g$ coincide: there is at most one positive
value $\beta$. By Stage B, if such a positive $\beta$ is attained then $g$
attains no zero. Hence exactly two possibilities remain:
- $g$ takes no positive value: by $g\ge0$ (Section 3), $g\equiv0$, i.e. $f(x)=x$;
- $g$ takes the positive value $\beta$: by Stage B it has no zero, and by
  Stage A $\beta$ is the only positive value, so $g\equiv\beta$ on all of
  $\mathbb R_{>0}$.

In every case $g$ is a constant $c\ge0$, giving
$$f(x)=x+g(x)=x+c,\qquad c\ge0.$$
Together with Section 1 (every such $f$ is a solution), the set of solutions is
exactly
$$\boxed{\,f(x)=x+c,\quad c\ge0\,}.$$
Substitution was verified in Section 1: for $g\equiv c$ the deviation
$s=g(x)-g(y)\equiv0$, so $(\star)$ is the classical $\mathrm{QM}\ge\mathrm{AM}\ge\mathrm{GM}$
chain for $(x,f(y))=(x,y+c)$, valid for all $x,y>0$. $\blacksquare$

---

## Promotable lemmas

**Squeeze lemma (proven in full, Section 4).**
*Statement.* For every $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfying $(\star)$,
with $g(t)=f(t)-t$, one has $|g(x)-g(y)|\le(x-f(y))^{2}/(x+f(y))$ for all
$x,y>0$. *Where proved:* `results/imo-2026-05/approaches/density-contradiction.md`,
Section 4. *Derivation:* from the QM-AM upper gap
$2(\mathrm{QM}-\mathrm{AM})\le(a-b)^{2}/(a+b)$ and the AM-GM lower gap
$2(\mathrm{AM}-\mathrm{GM})\le(a-b)^{2}/(a+b)$ with $a=x,b=f(y)$
(rationalization / difference of two squares); then $|s|\le\max(2U,2L)\le$ bound.
Weaker than but independent of the certified `lemmas/master-squeeze.md`.

**Orbit invariance + sign (proven in full, Sections 2–3).**
*Statement.* $g(f(y))=g(y)$ and $g\ge0$ everywhere on $\mathbb R_{>0}$.
*Where proved:* ibid., Sections 2–3. *Derivation:* $x=f(y)$ collapses the
window giving $f(f(y))=2f(y)-y$; forward orbit $y_{n}=y+n\,g(y)$ stays positive,
forcing $g(y)\ge0$.

**Two-distinct-positive-values exclusion (proven in full, Sections 6–7).**
*Statement.* Under $(\star)$, $g$ cannot take two distinct positive values.
*Where proved:* ibid., Sections 6 (irrational ratio, Kronecker density) and 7
(rational ratio, commensurate-coset intersect-or-grow-kill). Importable by any
approach needing "$g$ takes values in $\{0,\beta\}$."

**Zero-alongside-positive exclusion (proven in full, Section 8).**
*Statement.* Under $(\star)$ and $(\bullet)$ ($g$ takes values in $\{0,\beta\}$),
if $g$ attains $0$ and a positive $\beta$, then $g\equiv0$ on a tail ray
$[u_{0},\infty)$; combined with orbit invariance this forces $\beta=0$, a
contradiction. *Where proved:* ibid., Section 8 (base case via image-point
continuity + two-valued structure; rightward propagation with step
$\eta_{+}(v)>\sqrt{2v\beta}$ reaching $+\infty$; orbit-intersection
contradiction).
