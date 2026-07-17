# Approach: marching-orbits

## Status
solved

## Approaches tried
- Round-1 outline: match two forward f-orbits (each an arithmetic progression) at bounded offset far out; the right inequality's slack then grows linearly in the d-mismatch, forcing all positive d-values equal. Mixed 0/c case killed by fixed-point propagation + AP-hits-excluded-interval. Mechanisms checked by hand algebra; not yet written rigorously.
- Round-1 build: full rigorous write-up completed. All gaps flagged by the outline-reviewer closed: explicit choice of m and n in the marching lemma with concrete bounds (no limits), the dichotomy stated as range(d) ⊆ {0,c}, the 4b bootstrap induction written out, and the 4c floor-type AP-hits-interval argument made explicit with concrete constants. — worked; complete proof below.

## Current best
Complete proof of the full characterization: the solutions are exactly f(x) = x + c, c ≥ 0. No open gaps. See Full proof.

## Target
Determine all f: R_{>0} → R_{>0} with sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x·f(y)) for all x,y > 0.
**Answer: exactly the family f(x) = x + c, where c ≥ 0 is a constant.**

## Full proof

**Answer.** The functions satisfying the condition are exactly

$$f(x) = x + c, \qquad c \ge 0 \text{ a constant.}$$

Throughout, the hypothesis is: $f\colon \mathbb{R}_{>0}\to\mathbb{R}_{>0}$ and for all $x,y>0$,

$$\sqrt{\frac{x^2+f(y)^2}{2}} \;\ge\; \frac{f(x)+y}{2} \;\ge\; \sqrt{x\,f(y)}. \tag{$\ast$}$$

**Squaring legality.** For all $x,y>0$ every quantity in $(\ast)$ is positive: $x^2+f(y)^2>0$, $\frac{f(x)+y}{2}>0$ (since $f(x)>0$, $y>0$), and $x f(y)>0$. For positive reals $A,B,C$ with $B>0$, the chain $\sqrt{A}\ge B\ge \sqrt{C}$ holds if and only if $A\ge B^2$ and $B^2\ge C$ (squaring is strictly increasing on $\mathbb{R}_{\ge 0}$). Hence $(\ast)$ is equivalent to the pair

$$\text{(L)}\quad 2\bigl(x^2+f(y)^2\bigr)\ \ge\ \bigl(f(x)+y\bigr)^2, \qquad\qquad \text{(R)}\quad \bigl(f(x)+y\bigr)^2\ \ge\ 4\,x\,f(y),$$

for all $x,y>0$. We use (L) and (R) throughout. (This is the standard QM ≥ AM ≥ GM shape — cf. "Standard inequalities" in `knowledge_base.md` — but we do not need the mean inequalities themselves; we work with (L) and (R) directly.)

---

### Part 1. Sufficiency: every $f(x)=x+c$ with $c\ge 0$ works

First, $f(x)=x+c$ maps $\mathbb{R}_{>0}\to\mathbb{R}_{>0}$: for $x>0$ and $c\ge 0$, $x+c>0$. (For $c<0$ this already fails: $x=-c/2>0$ gives $f(x)=c/2\le 0$; so no $c<0$ can be admitted, independently of the inequalities.)

Now verify (R): with $f(x)=x+c$, $f(y)=y+c$,

$$\bigl(f(x)+y\bigr)^2-4xf(y) = (x+y+c)^2-4x(y+c).$$

Expand both:
$(x+y+c)^2 = x^2+y^2+c^2+2xy+2xc+2yc$ and $4x(y+c)=4xy+4xc$. Subtracting:

$$x^2+y^2+c^2+2xy+2xc+2yc-4xy-4xc = x^2+y^2+c^2-2xy-2xc+2yc = (x-y-c)^2 \ \ge\ 0.$$

(Check: $(x-y-c)^2 = x^2+y^2+c^2 -2xy -2xc +2yc$. ✓)

Verify (L): write $u=y+c=f(y)$, so

$$2\bigl(x^2+f(y)^2\bigr)-\bigl(f(x)+y\bigr)^2 = 2x^2+2u^2-(x+u)^2 = x^2-2xu+u^2 = (x-u)^2=(x-y-c)^2\ \ge\ 0.$$

Both (L) and (R) hold, so by the equivalence above $(\ast)$ holds. Sufficiency is proved.

---

### Part 2. The core identity and arithmetic-progression orbits

**Lemma 1 (core identity).** For all $y>0$: $\;f(f(y)) = 2f(y)-y$.

*Proof.* Substitute $x=f(y)$ in $(\ast)$ (legal: $f(y)>0$). The left end becomes $\sqrt{\frac{f(y)^2+f(y)^2}{2}} = \sqrt{f(y)^2}=f(y)$ (as $f(y)>0$), and the right end becomes $\sqrt{f(y)\cdot f(y)} = f(y)$. So $(\ast)$ reads

$$f(y)\ \ge\ \frac{f(f(y))+y}{2}\ \ge\ f(y),$$

forcing $\frac{f(f(y))+y}{2}=f(y)$, i.e. $f(f(y))=2f(y)-y$. $\square$

Define $d(y):=f(y)-y$ for $y>0$. Lemma 1 gives, for every $y>0$,

$$d(f(y)) = f(f(y))-f(y) = \bigl(2f(y)-y\bigr)-f(y) = f(y)-y = d(y). \tag{2.1}$$

**Lemma 2 (AP orbits and $f\ge \mathrm{id}$).** Fix $y>0$ and define the forward orbit $y_0=y$, $y_{n+1}=f(y_n)$ for $n\ge 0$. Then for every integer $n\ge 0$:
(a) $y_n>0$; (b) $d(y_n)=d(y)$; (c) $y_n = y + n\,d(y)$.
Moreover $d(y)\ge 0$ for every $y>0$.

*Proof.* Induction on $n$. Base $n=0$: $y_0=y>0$, $d(y_0)=d(y)$, $y_0=y+0$. Inductive step: assume (a)–(c) for $n$. Since $y_n>0$, $y_{n+1}=f(y_n)>0$ (codomain), giving (a). By (2.1) applied at $y_n$: $d(y_{n+1})=d(f(y_n))=d(y_n)=d(y)$, giving (b). And $y_{n+1}=f(y_n)=y_n+d(y_n)=\bigl(y+n\,d(y)\bigr)+d(y)=y+(n+1)d(y)$, giving (c).

Now suppose $d(y)<0$ for some $y>0$. Choose an integer $n>y/|d(y)|$ (Archimedean property). Then $y_n = y+n\,d(y) = y-n|d(y)| < y - y = 0$, contradicting (a). Hence $d(y)\ge 0$ for all $y>0$. $\square$

So every forward orbit is the arithmetic progression $y_n=y+n\,d(y)$ with common difference $d(y)\ge 0$, and $d$ is constant along it.

---

### Part 3. Marching-orbits lemma: all positive values of $d$ coincide

**Lemma 3.** If $x,y>0$ satisfy $d(x)>0$ and $d(y)>0$, then $d(x)=d(y)$.

*Proof.* Write $p=d(x)>0$, $q=d(y)>0$ and suppose for contradiction $p<q$. By Lemma 2, the orbit points

$$x_m = x+mp \quad (m\ge 0), \qquad y_n = y+nq \quad (n\ge 0)$$

are all positive with $d(x_m)=p$, $d(y_n)=q$; in particular $f(x_m)=x_m+p$ and $f(y_n)=y_n+q$.

**Choice of $n$.** Since $q-p>0$, choose an integer $n$ large enough that

$$y_n = y+nq \;>\; \max\!\left(x+p,\ \frac{p^2}{q-p}\right); \tag{3.1}$$

explicitly, any integer $n > \frac{1}{q}\max\!\bigl(x+p,\ p^2/(q-p)\bigr)$ works (Archimedean property). Fix such an $n$.

**Choice of $m$.** Set $m=\bigl\lceil (y_n-x)/p \bigr\rceil$. By (3.1), $y_n-x>p>0$, so $(y_n-x)/p>1$ and hence $m\ge 2$; in particular $m$ is a positive integer and $x_m$ is a genuine orbit point. By definition of the ceiling,

$$\frac{y_n-x}{p}\ \le\ m\ <\ \frac{y_n-x}{p}+1,$$

so multiplying by $p>0$ and adding $x$:

$$y_n \ \le\ x_m = x+mp\ <\ y_n+p.$$

Set $S := x_m-y_n$; then $0\le S<p$.

**The slack computation.** Apply (R) at the pair $(x,y)=(x_m,\,y_n)$:

$$\bigl(f(x_m)+y_n\bigr)^2\ \ge\ 4\,x_m\,f(y_n), \qquad\text{i.e.}\qquad (x_m+p+y_n)^2\ \ge\ 4\,x_m\,(y_n+q). \tag{3.2}$$

Substitute $x_m=y_n+S$ and expand both sides:

$$(x_m+p+y_n)^2 = (2y_n+S+p)^2 = 4y_n^2+4y_n(S+p)+(S+p)^2,$$
$$4x_m(y_n+q) = 4(y_n+S)(y_n+q) = 4y_n^2+4y_n(S+q)+4Sq.$$

Subtracting, the slack of (3.2) is

$$\Delta := (x_m+p+y_n)^2-4x_m(y_n+q) = 4y_n\bigl[(S+p)-(S+q)\bigr]+(S+p)^2-4Sq = 4y_n(p-q)+(S+p)^2-4Sq.$$

**Bounding the O(1) terms explicitly.** Since $0\le S<p$: $(S+p)^2<(p+p)^2=4p^2$, and $-4Sq\le 0$. Hence

$$\Delta \ <\ 4y_n(p-q)+4p^2 \ =\ -4y_n(q-p)+4p^2.$$

By (3.1), $y_n>p^2/(q-p)$, so $4y_n(q-p)>4p^2$ and therefore $\Delta<0$. This contradicts (3.2), which asserts $\Delta\ge 0$.

Hence $p<q$ is impossible. Running the same argument with the roles of $(x,p)$ and $(y,q)$ interchanged shows $q<p$ is impossible. Therefore $p=q$. $\square$

**Dichotomy.** By Lemma 3, $d$ takes at most one positive value. Precisely, exactly one of the following holds:

- **Case A:** $d(y)=0$ for all $y>0$; then $f=\mathrm{id}$, i.e. $f(x)=x+0$, a member of the claimed family.
- Otherwise there is some $y_\ast$ with $c:=d(y_\ast)>0$, and by Lemma 3 every positive value of $d$ equals $c$; combined with $d\ge 0$ (Lemma 2), $$\operatorname{range}(d)\subseteq\{0,c\}. \tag{3.3}$$ This splits into:
  - **Case B:** $d(y)=c$ for all $y>0$; then $f(x)=x+c$ with $c>0$, a member of the claimed family.
  - **Case C (mixed):** $\operatorname{range}(d)=\{0,c\}$: there exist $a>0$ with $d(a)=0$ (i.e. $f(a)=a$) **and** $b>0$ with $d(b)=c>0$.

These three cases are exhaustive and mutually exclusive. Cases A and B give the claimed family, so it remains to rule out Case C. Assume Case C for the rest of Part 4 and fix such $a$ and $b$.

---

### Part 4. The mixed case is impossible

#### 4a. Exclusion zone around every fixed point

**Lemma 4.** Let $a>0$ be a fixed point ($f(a)=a$) and let $s>0$ satisfy $d(s)=c$. Then $|s-a|\ \ge\ 2\sqrt{ac}$.

*Proof.* Apply (R) at $(x,y)=(a,s)$: $\bigl(f(a)+s\bigr)^2\ge 4a\,f(s)$, i.e. $(a+s)^2\ge 4a(s+c)$. Expand:

$$(a+s)^2-4a(s+c) = a^2+2as+s^2-4as-4ac = (s-a)^2-4ac\ \ge\ 0,$$

so $(s-a)^2\ge 4ac$ and, taking square roots ($4ac>0$), $|s-a|\ge 2\sqrt{ac}$. $\square$

Equivalently: **no point with $d$-value $c$ lies in the open interval $\bigl(a-2\sqrt{ac},\ a+2\sqrt{ac}\bigr)$**, whose length is $4\sqrt{ac}$.

(Note this used $f(a)=a$ *exactly*; the dichotomy (3.3) is what makes fixed points genuinely available in Case C.)

#### 4b. Fixed points propagate to $+\infty$

**Lemma 5.** Let $a>0$ be a fixed point. Then every $x\in\bigl[a,\ a+c+\sqrt{4ac+2c^2}\bigr)$ is a fixed point.

*Proof.* Apply (L) at $(x,a)$ for any $x>0$: $2\bigl(x^2+f(a)^2\bigr)\ge\bigl(f(x)+a\bigr)^2$, i.e. $2(x^2+a^2)\ge(f(x)+a)^2$. Since $f(x)+a>0$, taking square roots gives

$$f(x)\ \le\ \sqrt{2(x^2+a^2)}-a, \qquad\text{i.e.}\qquad d(x)\ \le\ \sqrt{2(x^2+a^2)}-x-a. \tag{4.1}$$

**Claim:** $\sqrt{2(x^2+a^2)} < x+a+c$ for all $x\in\bigl[a,\ a+c+\sqrt{4ac+2c^2}\bigr)$.

Both sides are positive, so the claim is equivalent (squaring, strictly increasing on $\mathbb{R}_{\ge0}$) to

$$2x^2+2a^2 \;<\; x^2+a^2+c^2+2ax+2cx+2ac \quad\Longleftrightarrow\quad P(x):= x^2-2(a+c)x+\bigl(a^2-c^2-2ac\bigr)\;<\;0.$$

$P$ is an upward parabola with roots

$$x = (a+c)\pm\sqrt{(a+c)^2-(a^2-c^2-2ac)} = (a+c)\pm\sqrt{4ac+2c^2}.$$

(Check the discriminant: $(a+c)^2-a^2+c^2+2ac = a^2+2ac+c^2-a^2+c^2+2ac = 4ac+2c^2$. ✓) Since $a>0$, $c>0$ give $4ac+2c^2>c^2$, we have $\sqrt{4ac+2c^2}>c$, so the lower root satisfies $(a+c)-\sqrt{4ac+2c^2} < (a+c)-c = a$. Hence $P(x)<0$ strictly on the open interval between the roots, which contains $\bigl[a,\ a+c+\sqrt{4ac+2c^2}\bigr)$. This proves the claim (strictly, including both endpoints of the half-open interval: the left endpoint $x=a$ lies strictly above the lower root, and every $x$ strictly below the upper root works).

Combining the claim with (4.1): for $x$ in the stated interval, $d(x)\le\sqrt{2(x^2+a^2)}-x-a < c$. By the dichotomy (3.3), $d(x)\in\{0,c\}$, so $d(x)=0$: $x$ is a fixed point. $\square$

**Corollary 6 (unbounded fixed points).** With $a$ the fixed point from Case C, define $a_k := a+kc$ for integers $k\ge 0$. Then every $a_k$ is a fixed point; in particular the set of fixed points is unbounded above.

*Proof.* Induction on $k$. Base: $a_0=a$ is fixed. Step: suppose $a_k$ is fixed. Since $\sqrt{4a_kc+2c^2}>0$, we have

$$a_{k+1} = a_k+c \;\in\; \bigl[a_k,\ a_k+c+\sqrt{4a_kc+2c^2}\bigr),$$

so by Lemma 5 (applied at the fixed point $a_k$), $a_{k+1}$ is a fixed point. Since $c>0$, $a_k=a+kc\to+\infty$. $\square$

#### 4c. The orbit of $b$ must enter an exclusion zone — contradiction

By Lemma 2, the forward orbit $b_n := b+nc$ ($n\ge 0$) consists of positive points with $d(b_n)=c$ for all $n$, and $b_n\to+\infty$.

**Choice of a large fixed point.** By Corollary 6, choose a fixed point $a' = a_k$ with

$$a' \ \ge\ \max\bigl(16c,\ 2b+1\bigr); \tag{4.2}$$

this is possible since $a_k\to\infty$ (take any integer $k \ge \max(16c,\,2b+1)/c$, say). Set

$$\alpha := a'-2\sqrt{a'c}, \qquad \beta := a'+2\sqrt{a'c},$$

so by Lemma 4 **no point with $d$-value $c$ lies in the open interval $(\alpha,\beta)$**. We record two consequences of (4.2):

1. **The interval lies above $b_0=b$:** since $a'\ge 16c$, we have $\sqrt{c}\le\sqrt{a'}/4$, so $2\sqrt{a'c}=2\sqrt{a'}\sqrt{c}\le\tfrac{1}{2}a'$, hence $\alpha = a'-2\sqrt{a'c}\ \ge\ a'/2\ \ge\ b+\tfrac12 \ >\ b = b_0.$
2. **The interval is longer than the orbit gap:** $\beta-\alpha = 4\sqrt{a'c}\ \ge\ 4\sqrt{16c\cdot c} = 16c\ >\ c.$

**The orbit lands in $(\alpha,\beta)$.** The set $\{n\ge 0 : b_n>\alpha\}$ is nonempty (as $b_n\to+\infty$); let $n_\ast$ be its least element. Since $b_0=b<\alpha$ (consequence 1), $n_\ast\ge 1$, and by minimality $b_{n_\ast-1}\le\alpha$. Then

$$\alpha \;<\; b_{n_\ast} \;=\; b_{n_\ast-1}+c \;\le\; \alpha+c \;<\; \alpha+(\beta-\alpha) \;=\; \beta,$$

using consequence 2 in the last strict inequality. So $b_{n_\ast}\in(\alpha,\beta)$, i.e. $|b_{n_\ast}-a'|<2\sqrt{a'c}$, while $d(b_{n_\ast})=c$. This contradicts Lemma 4 applied to the fixed point $a'$ and the point $s=b_{n_\ast}$.

**Conclusion of Part 4.** Case C is impossible.

---

### Part 5. Conclusion

By the dichotomy of Part 3 and the elimination of the mixed case in Part 4, either $d\equiv 0$ or $d\equiv c$ for a single constant $c>0$; in both cases $f(x)=x+c$ with a constant $c\ge 0$. Conversely, Part 1 shows every such $f$ satisfies $(\ast)$ (and no $c<0$ gives a valid map $\mathbb{R}_{>0}\to\mathbb{R}_{>0}$). Therefore the solutions are exactly

$$\boxed{\,f(x)=x+c,\quad c\ge 0\text{ a constant.}\,}$$

**Verification of the answer** (required for the `characterize_functions` answer type): sufficiency was verified by the explicit identities in Part 1 — for $f(x)=x+c$, both squared slacks equal $(x-y-c)^2\ge 0$; e.g. $c=1$, $x=3$, $y=2$: middle $=(4+2)/2=3$, left $=\sqrt{(9+9)/2}=3$, right $=\sqrt{3\cdot 3}=3$, chain holds with equality (here $x-y-c=0$); and $x=5$, $y=1$, $c=1$: left $=\sqrt{(25+4)/2}=\sqrt{14.5}\approx 3.807$, middle $=(6+1)/2=3.5$, right $=\sqrt{5\cdot 2}=\sqrt{10}\approx 3.162$. ✓ ∎

---

## Cases covered
- $d\equiv 0$ (Case A) — the $c=0$ member.
- $d\equiv c>0$ (Case B) — the $c>0$ members.
- Mixed $\operatorname{range}(d)=\{0,c\}$ (Case C) — impossible (Part 4). Exhaustive by Lemma 2 ($d\ge0$) and Lemma 3 (at most one positive value).

## Tools invoked
- Equivalence of $\sqrt{A}\ge B\ge\sqrt{C}$ (all positive) with $A\ge B^2\ge C$ — monotonicity of squaring (elementary; "Standard inequalities" context in `knowledge_base.md`).
- Linear recurrence $y_{n+1}=2y_n-y_{n-1}$ solved by arithmetic progressions — direct induction here (KB: "Linear recurrences").
- Archimedean property of $\mathbb{R}$ (Lemma 2 negativity, choice of $n$ in Lemma 3, choice of $k$ in 4c).
- Well-ordering of $\mathbb{N}$ (least $n_\ast$ in 4c; KB: "Infinite descent / extremal principle").

## Promotable lemmas
- **core-identity-ap-orbits** (proved in full in Part 2 above, Lemmas 1–2): *Let $f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}$ satisfy $(\ast)$ for all $x,y>0$. Then (i) $f(f(y))=2f(y)-y$ for all $y>0$; (ii) $d:=f-\mathrm{id}$ satisfies $d\ge 0$ and $d(f(y))=d(y)$; (iii) the forward orbit $y_n=f^n(y)$ equals $y+n\,d(y)$ for all $n\ge0$.* Reusable by every rival approach (two-point-pinch already relies on exactly this). Proposed file drafted at `results/imo-2026-05/lemmas/core-identity-ap-orbits.md` (marked uncertified; reviewer to certify).
