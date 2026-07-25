## Status
solved

## Approaches tried
- (this file) Orbit-crossing: march one orbit (arithmetic progression) to infinity while
  keeping it within a bounded gap of a second orbit, and read off a contradiction from
  the R inequality evaluated across the two orbits. **This round: the residual {0,b}
  sub-case is now CLOSED via the reviewer's fixed-point-openness / boundary-separation
  mechanism. Proof complete.**

## Current best
**Complete.** Answer: **f(x) = x + c for every constant c ≥ 0, and no others.**
The exhaustiveness argument has two independent kills: (i) the Main Lemma (marching)
rules out two positive d-values, leaving range(d) ⊆ {0,b}; (ii) the openness/boundary
argument rules out F (fixed points) and G (shift-by-b points) both nonempty. See full
proof below.

## Full proof

We determine all functions f : ℝ_{>0} → ℝ_{>0} satisfying
$$\sqrt{\tfrac{x^2+f(y)^2}{2}} \;\ge\; \tfrac{f(x)+y}{2} \;\ge\; \sqrt{x\,f(y)}\qquad(x,y>0).\tag{$\star$}$$

**Answer.** The solutions are exactly the functions **f(x) = x + c with a constant c ≥ 0.**

### 0. Squaring the hypothesis

All quantities in ($\star$) are positive: $x,f(y)>0$ so $\sqrt{xf(y)}>0$; $f(x),y>0$ so
$\frac{f(x)+y}{2}>0$; and $\frac{x^2+f(y)^2}{2}>0$. For positive reals $A,M,B$ the chain
$\sqrt A\ge M\ge\sqrt B$ is equivalent to $A\ge M^2\ge B$ (the squaring map is strictly
increasing on $[0,\infty)$). Hence ($\star$) is **equivalent**, for all $x,y>0$, to the pair
$$\mathbf{L}(x,y):\quad 2\bigl(x^2+f(y)^2\bigr)\ \ge\ \bigl(f(x)+y\bigr)^2,\qquad
\mathbf{R}(x,y):\quad \bigl(f(x)+y\bigr)^2\ \ge\ 4\,x\,f(y).$$
We work with $\mathbf L,\mathbf R$ throughout. (No information is lost or added by squaring.)

### 1. Easy direction: every $f(x)=x+c$ with $c\ge0$ is a solution

First, for $f(x)=x+c$ to map $\mathbb R_{>0}$ into $\mathbb R_{>0}$ we need $x+c>0$ for all
$x>0$; letting $x\to0^+$ this forces $c\ge0$, and conversely $c\ge0$ gives $x+c>x>0$. So the
admissible constants are exactly $c\ge0$.

Now fix $c\ge0$ and put $f(t)=t+c$, so $f(x)=x+c$, $f(y)=y+c$. Compute the two defects:
$$\mathbf L\text{-defect}=2\bigl(x^2+(y+c)^2\bigr)-(x+c+y)^2,\qquad
\mathbf R\text{-defect}=(x+c+y)^2-4x(y+c).$$
Expanding (an SOS identity; verified symbolically with sympy — both differences reduce to $0$):
$$2\bigl(x^2+(y+c)^2\bigr)-(x+c+y)^2=\bigl((x-y)-c\bigr)^2,\qquad
(x+c+y)^2-4x(y+c)=\bigl((x-y)-c\bigr)^2.$$
Indeed, for $\mathbf R$: $(x+y+c)^2-4x(y+c)=(x-y)^2-2c(x-y)+c^2=\bigl((x-y)-c\bigr)^2$; and for
$\mathbf L$: $2x^2+2(y+c)^2-(x+y+c)^2=(x-y)^2-2c(x-y)+c^2=\bigl((x-y)-c\bigr)^2$. Both are squares,
hence $\ge0$, so both $\mathbf L$ and $\mathbf R$ hold for all $x,y>0$. Thus every $f(x)=x+c$
with $c\ge0$ satisfies ($\star$). $\qquad\square$ (easy direction)

### 2. Structural lemmas (valid for every solution $f$)

Let $f$ be any solution.

**Lemma A. $f(f(y))=2f(y)-y$ for all $y>0$.**
Fix $y$ and substitute $x=f(y)$. Then $x^2+f(y)^2=2f(y)^2$ and $f(x)=f(f(y))$.
- $\mathbf L(f(y),y)$: $2\cdot 2f(y)^2\ge\bigl(f(f(y))+y\bigr)^2$, i.e. $\bigl(2f(y)\bigr)^2\ge\bigl(f(f(y))+y\bigr)^2$. Both sides are squares of positive numbers, so $2f(y)\ge f(f(y))+y$, giving $f(f(y))\le 2f(y)-y$.
- $\mathbf R(f(y),y)$: $\bigl(f(f(y))+y\bigr)^2\ge 4f(y)\cdot f(y)=\bigl(2f(y)\bigr)^2$, so $f(f(y))+y\ge 2f(y)$, giving $f(f(y))\ge 2f(y)-y$.

Combining, $f(f(y))=2f(y)-y$. $\square$

**Lemma B. $f$ is injective.**
If $f(a)=f(b)$ then $f(f(a))=f(f(b))$, so by Lemma A $2f(a)-a=2f(b)-b$. Since $f(a)=f(b)$
this reduces to $a=b$. $\square$

**Lemma C. Set $d(y):=f(y)-y$. Then (i) $d(f(y))=d(y)$; (ii) $f^{n}(y)=y+n\,d(y)$ for all
integers $n\ge0$; (iii) $d(y)\ge0$.**
(i) By Lemma A, $d(f(y))=f(f(y))-f(y)=(2f(y)-y)-f(y)=f(y)-y=d(y)$.
(ii) Induction on $n$. For $n=0$, $f^0(y)=y$. Assume $f^n(y)=y+n\,d(y)$. Applying (i)
repeatedly, $d\bigl(f^n(y)\bigr)=d(y)$, so
$f^{n+1}(y)=f\bigl(f^n(y)\bigr)=f^n(y)+d\bigl(f^n(y)\bigr)=y+n\,d(y)+d(y)=y+(n+1)d(y).$
(iii) Every iterate $f^n(y)$ lies in $\mathbb R_{>0}$, so $y+n\,d(y)>0$ for all $n\ge0$.
If $d(y)<0$ this fails for large $n$; hence $d(y)\ge0$. $\square$

Thus along any forward orbit $d$ is constant and the orbit $\{f^n(y)\}$ is an arithmetic
progression with common difference $d(y)\ge0$. In particular, for any point $p$ with
$d(p)=a$, all of $p,\,p+a,\,p+2a,\dots$ are points with $d$-value $a$.

### 3. Two cross-orbit inequalities

Let $p,q>0$ with $a:=d(p)$, $b:=d(q)$. Then $f(p)=p+a$, and by Lemma C
$f(f(p))=f(p)+d(f(p))=p+2a$, while $f(q)=q+b$. Substitute $(x,y)=(f(p),q)$ into
$\mathbf R$ and $\mathbf L$:

**R-test.** $\mathbf R(f(p),q)$ reads $\bigl(f(f(p))+q\bigr)^2\ge 4f(p)f(q)$, i.e.
$(p+2a+q)^2\ge 4(p+a)(q+b)$. Its defect factors (sympy-verified) as
$$(p+2a+q)^2-4(p+a)(q+b)=(p-q)^2+4(a-b)(p+a).$$
Hence $\mathbf R(f(p),q)$ is equivalent to
$$\boxed{\,(p-q)^2\ \ge\ 4(b-a)(p+a).}\tag{$\ddagger$}$$

**L-test.** $\mathbf L(f(p),q)$ reads $2\bigl(f(p)^2+f(q)^2\bigr)\ge\bigl(f(f(p))+q\bigr)^2$,
i.e. $2\bigl((p+a)^2+(q+b)^2\bigr)\ge(p+2a+q)^2$. Its defect factors (sympy-verified) as
$$2\bigl((p+a)^2+(q+b)^2\bigr)-(p+2a+q)^2=(p-q)^2+2(b-a)(a+b+2q),$$
so $\mathbf L(f(p),q)$ is equivalent to $(p-q)^2\ge 2(a-b)(a+b+2q).\tag{$\dagger$}$

(These two algebraic identities were checked symbolically; both defect differences reduce
to $0$.)

### 4. Main Lemma: $d$ takes at most one positive value

**Claim.** There do not exist two points with distinct positive $d$-values.

Suppose, for contradiction, $d$ takes two positive values $a<b$ (with $a,b>0$). Pick $p_0$
with $d(p_0)=a$ and $q_0$ with $d(q_0)=b$. By Lemma C the arithmetic progressions
$$P_m:=p_0+ma\ (m\ge0,\ d(P_m)=a),\qquad Q_n:=q_0+nb\ (n\ge0,\ d(Q_n)=b)$$
are all admissible points. Since $a>0$, $P_m\to\infty$ as $m\to\infty$; in particular
$P_m>q_0$ for all large $m$. For such $m$ define
$$n:=\Bigl\lfloor\tfrac{P_m-q_0}{b}\Bigr\rfloor\ \ge\ 0 .$$
Then $0\le P_m-q_0-nb<b$, i.e. $Q_n=q_0+nb$ satisfies $0\le P_m-Q_n<b$; moreover
$Q_n=q_0+nb>0$. Thus $Q_n$ is a valid point at bounded distance from $P_m$:
$$0\ \le\ P_m-Q_n\ <\ b\quad\Longrightarrow\quad (P_m-Q_n)^2\ <\ b^2 .$$
Apply the **R-test** ($\ddagger$) with $p=P_m$ (so its $d$-value is $a$) and $q=Q_n$
(so its $d$-value is $b$):
$$(P_m-Q_n)^2\ \ge\ 4(b-a)(P_m+a).$$
The left side is bounded above by $b^2$, while the right side equals $4(b-a)(P_m+a)$ and
tends to $+\infty$ as $m\to\infty$ (because $b-a>0$ and $P_m\to\infty$). For $m$ large enough
$4(b-a)(P_m+a)>b^2$, contradicting the inequality. This proves the Claim. $\square$

**Consequence.** The value set $d(\mathbb R_{>0})$ contains at most one positive number.
Combined with $d\ge0$ (Lemma C(iii)), exactly one of the following holds:
1. $d\equiv 0$, i.e. $f(x)=x$ for all $x$ (the case $c=0$);
2. $d\equiv b$ for a single constant $b>0$, i.e. $f(x)=x+b$ (the case $c=b>0$);
3. $d$ takes exactly the two values $0$ and $b$ for some fixed $b>0$, both attained.

Cases 1 and 2 give precisely $f(x)=x+c$ with $c\ge0$. It remains to eliminate Case 3.

### 5. Residual case: fixed points and a shift cannot coexist

Assume Case 3 and derive a contradiction. Partition
$$F:=\{x>0: d(x)=0\}\ (\text{fixed points}),\qquad G:=\{x>0: d(x)=b\},$$
so $F\sqcup G=(0,\infty)$, with $b>0$ fixed and **both $F$ and $G$ nonempty**.

**Step 5a: $F$ is open.**
Fix any $p\in F$ (so $f(p)=p$). We claim every point in the open interval
$$I_p:=\Bigl((b+p)-\sqrt{4bp+2b^2},\ (b+p)+\sqrt{4bp+2b^2}\Bigr)$$
lies in $F$. Take $x\in I_p$ and suppose, for contradiction, $x\in G$, i.e. $f(x)=x+b$.
Evaluate the hypothesis $\mathbf L(x,p)$ (which must hold, being part of ($\star$)):
$$\mathbf L(x,p):\quad 2\bigl(x^2+f(p)^2\bigr)\ \ge\ \bigl(f(x)+p\bigr)^2
\ \Longleftrightarrow\ 2(x^2+p^2)\ \ge\ (x+b+p)^2 .$$
Its defect (sympy-verified) is
$$2(x^2+p^2)-(x+b+p)^2=x^2-2(b+p)x+\bigl(p^2-2bp-b^2\bigr),$$
a upward-opening quadratic in $x$ with discriminant (over $4$) equal to
$(b+p)^2-(p^2-2bp-b^2)=2b^2+4bp>0$, hence with roots $(b+p)\pm\sqrt{4bp+2b^2}$, i.e. exactly
the endpoints of $I_p$. Therefore the defect is **strictly negative** for every
$x\in I_p$, so $\mathbf L(x,p)$ **fails** — contradicting that $\mathbf L$ holds for all
$x,y>0$. Hence no $x\in I_p$ can be in $G$; that is, $I_p\subseteq F$.

Finally $p\in I_p$: the condition $(b+p)-\sqrt{4bp+2b^2}<p$ is $b<\sqrt{4bp+2b^2}$, i.e.
$b^2<4bp+2b^2$, i.e. $0<4bp+b^2$, which holds. So $I_p$ is an open neighborhood of $p$
contained in $F$. As $p\in F$ was arbitrary, **$F$ is open** in $(0,\infty)$.

**Step 5b: a boundary point in $G$ approached from $F$.**
The interval $(0,\infty)$ is connected. $F$ is open, nonempty, and **proper** (since
$G\ne\emptyset$). A connected space has no proper nonempty clopen subset; therefore $F$,
being open and proper, cannot also be closed. Hence there exists a point
$$t\in\overline{F}\setminus F\subseteq(0,\infty).$$
Since $(0,\infty)=F\sqcup G$ and $t\notin F$, we have $t\in G$ (so $f(t)=t+b$). And
$t\in\overline F$ gives a sequence $p_n\in F$ with $p_n\to t$ and $p_n\ne t$.

**Step 5c: separation contradiction.**
For any $x\in F$ and $y\in G$, evaluate the hypothesis $\mathbf R(x,y)$ (again part of
($\star$)) using $f(x)=x$, $f(y)=y+b$:
$$\mathbf R(x,y):\quad (x+y)^2\ \ge\ 4x(y+b)
\ \Longleftrightarrow\ (x-y)^2\ \ge\ 4bx,$$
the equivalence being $(x+y)^2-4x(y+b)=(x-y)^2-4bx$ (sympy-verified). Apply this with
$x=p_n\in F$ and $y=t\in G$:
$$(p_n-t)^2\ \ge\ 4b\,p_n\qquad(\text{all }n).$$
Let $n\to\infty$: the left side $(p_n-t)^2\to0$ (as $p_n\to t$), while the right side
$4b\,p_n\to 4bt$. Passing to the limit yields $0\ge 4bt$. But $b>0$ and $t>0$ give
$4bt>0$, a contradiction.

Therefore Case 3 is impossible. $\square$

### 6. Conclusion

By Section 4, every solution falls into Case 1, 2, or 3; Section 5 rules out Case 3, so
every solution is $f(x)=x$ or $f(x)=x+b$ ($b>0$) — that is, $f(x)=x+c$ for some constant
$c\ge0$. By Section 1, each such function is indeed a solution, and $c\ge0$ is forced by
the codomain. Hence the complete solution set is
$$\boxed{\,f(x)=x+c,\quad c\ge0.}$$
$\blacksquare$

### Named tools invoked
- **Squaring equivalence for positive reals** (Section 0): $\sqrt A\ge M\ge\sqrt B\iff A\ge M^2\ge B$ for $A,M,B>0$ (strict monotonicity of $t\mapsto t^2$ on $[0,\infty)$).
- **Standard inequalities / SOS** (`knowledge_base.md`, "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM …; equality cases"): the easy direction is the QM–AM/AM–GM equality analysis, both defects being the perfect square $((x-y)-c)^2$. The right bound $\frac{f(x)+y}{2}\ge\sqrt{xf(y)}$ is AM–GM on $f(x)+y$ vs. $\sqrt{xf(y)}$ at the fixed-point locus.
- **Connectedness of an interval** (Section 5b): $(0,\infty)$ is connected, so it has no proper nonempty clopen subset; an open proper nonempty subset is not closed and hence has a boundary point in its complement.
- **Archimedean / floor bounding** (Section 4): $n=\lfloor(P_m-q_0)/b\rfloor$ keeps two arithmetic progressions within a fixed gap $<b$; growth of a linear term beats a bounded square.

## Promotable lemmas

- **Lemma A (self-involution relation).** For every solution $f$ of ($\star$),
  $f(f(y))=2f(y)-y$ for all $y>0$. Proved in Section 2 (substitute $x=f(y)$; $\mathbf L,\mathbf R$ each force one inequality). Reusable by all approaches.
- **Lemma C (orbit structure).** With $d(y)=f(y)-y$: $d(f(y))=d(y)$, $f^n(y)=y+n\,d(y)$,
  and $d(y)\ge0$. Proved in Section 2.
- **R-test / L-test identities.** For points $p,q$ with $d(p)=a,d(q)=b$:
  $\mathbf R(f(p),q)\iff(p-q)^2\ge4(b-a)(p+a)$, and
  $\mathbf L(f(p),q)\iff(p-q)^2\ge2(a-b)(a+b+2q)$. Proved (and sympy-verified) in Section 3.
- **Fixed-point openness lemma.** For a solution with $d(\{\cdot\})\subseteq\{0,b\}$, the fixed-point set $F=\{x:f(x)=x\}$ is open: each $p\in F$ has neighborhood $I_p=((b+p)\pm\sqrt{4bp+2b^2})\subseteq F$, from $\mathbf L(x,p)$. Proved in Section 5a. Reusable to close the residual case in the sibling approaches (monotonicity-orbits, shift-family-sos, variational-min).
