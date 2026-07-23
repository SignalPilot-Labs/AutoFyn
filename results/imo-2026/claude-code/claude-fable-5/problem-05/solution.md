# IMO Problem 5 — Solution

**Work started:** 2026-07-22 15:55:56 PDT
**Solution finalized:** 2026-07-22 15:58:14 PDT
*(Verified numerically/symbolically by script and adversarially reviewed by an independent checker before write-up.)*

## Problem

Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions
$f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}$ such that

$$\sqrt{\frac{x^2+f(y)^2}{2}}\;\ge\;\frac{f(x)+y}{2}\;\ge\;\sqrt{x f(y)}
\qquad\text{for all } x,y\in\mathbb{R}_{>0}.$$

## Answer

$$\boxed{f(x)=x+c \text{ for an arbitrary constant } c\ge 0.}$$

## Solution

Call the left inequality **(L)** and the right inequality **(R)**.

### These functions work

Let $f(x)=x+c$ with $c\ge 0$; then $f$ maps $\mathbb{R}_{>0}$ into $\mathbb{R}_{>0}$. The key
observation is that the middle term is exactly the **arithmetic mean** of $x$ and $f(y)$:

$$\frac{f(x)+y}{2}=\frac{(x+c)+y}{2}=\frac{x+(y+c)}{2}=\frac{x+f(y)}{2}.$$

The left term is the quadratic mean of $x$ and $f(y)$ and the right term is their geometric
mean, so the chain is precisely $\mathrm{QM}\ge \mathrm{AM}\ge \mathrm{GM}$ for the pair
$(x,f(y))$, which holds for all positive reals. $\checkmark$

### These are the only functions

Suppose $f$ satisfies the chain.

**Step 1: The functional equation $f(f(y)) = 2f(y)-y$.**
Fix $y>0$ and substitute $x=f(y)$ (legal, since $f(y)\in\mathbb{R}_{>0}$). Then

$$\sqrt{\frac{f(y)^2+f(y)^2}{2}}=f(y),\qquad \sqrt{f(y)\cdot f(y)}=f(y),$$

so the chain squeezes the middle term:
$f(y)\ \ge\ \tfrac{f(f(y))+y}{2}\ \ge\ f(y)$, forcing equality:

$$(\ast)\qquad f(f(y)) = 2f(y)-y \qquad\text{for all } y>0.$$

**Step 2: $f(y)\ge y$ for all $y$.**
Fix $y$ and define the orbit $a_0=y$, $a_{n+1}=f(a_n)$; by induction $a_n>0$ for all $n$
since $f$ maps $\mathbb{R}_{>0}$ to itself. Applying $(\ast)$ at the point $a_{n-1}$ gives
$a_{n+1}=2a_n-a_{n-1}$ for all $n\ge 1$, so $(a_n)$ is an arithmetic progression:

$$a_n = y + n\bigl(f(y)-y\bigr).$$

If $f(y)<y$, then $a_n\to-\infty$, contradicting $a_n>0$. Hence $f(y)\ge y$ for all $y$.
Define $g(y):=f(y)-y\ \ge 0$.

**Step 3: The key two-point estimate.**
Let $y,z>0$ be arbitrary. Substitute $x=f(z)$ into **(L)** and use $(\ast)$:

$$\sqrt{\frac{f(z)^2+f(y)^2}{2}}\;\ge\;\frac{f(f(z))+y}{2}\;=\;\frac{2f(z)-z+y}{2}.$$

The right side is positive (it equals $\tfrac{f(f(z))+y}{2}$ with $f(f(z))>0$, $y>0$), so
squaring is legitimate:

$$2f(z)^2+2f(y)^2\;\ge\;\bigl(2f(z)-z+y\bigr)^2.$$

Write $A=f(z)$, $B=f(y)$, $\delta=g(z)-g(y)$. Since $y = B - g(y)$,

$$2f(z)-z+y \;=\; A+\bigl(f(z)-z\bigr)+y \;=\; A+g(z)+\bigl(B-g(y)\bigr) \;=\; A+B+\delta,$$

so $2A^2+2B^2\ge (A+B+\delta)^2$. Using $2A^2+2B^2-(A+B)^2=(A-B)^2$, this is equivalent to

$$(\mathrm{I})\qquad (A-B)^2\;\ge\;2(A+B)\,\delta+\delta^2 .$$

Now suppose $\delta\ge 0$, i.e. $g(z)\ge g(y)$. Since
$A-B=(z+g(z))-(y+g(y))=(z-y)+\delta$, substituting into (I) and cancelling $\delta^2$:

$$(z-y)^2+2(z-y)\delta \;\ge\; 2(A+B)\,\delta
\;\Longrightarrow\; (z-y)^2 \;\ge\; 2\delta\bigl(A+B-(z-y)\bigr).$$

But $A+B-(z-y) = (z+g(z))+(y+g(y))-z+y = 2y+g(y)+g(z)\ \ge\ 2y > 0$, hence

$$0\le g(z)-g(y)\;\le\;\frac{(z-y)^2}{2\,\bigl(2y+g(y)+g(z)\bigr)}\;\le\;\frac{(z-y)^2}{4y}.$$

By the symmetric argument with $y$ and $z$ swapped (if $g(y)\ge g(z)$, the same derivation
gives $g(y)-g(z)\le (y-z)^2/(4z)$), in all cases:

$$(\mathrm{IV})\qquad \bigl|g(z)-g(y)\bigr|\;\le\;\frac{(z-y)^2}{4\min(y,z)}
\qquad\text{for all } y,z>0.$$

**Step 4: $g$ is constant.**
Fix $0<a<b$ and $n\ge 1$; set $t_i=a+i\,\frac{b-a}{n}$ $(i=0,\dots,n)$ and
$h=\frac{b-a}{n}$. Every $t_i\ge a$, so by (IV) and the triangle inequality,

$$|g(b)-g(a)|\;\le\;\sum_{i=0}^{n-1}\bigl|g(t_{i+1})-g(t_i)\bigr|
\;\le\; n\cdot\frac{h^2}{4a}\;=\;\frac{(b-a)^2}{4an}\;\xrightarrow[n\to\infty]{}\;0 .$$

Since $|g(b)-g(a)|$ is a fixed nonnegative number, $g(b)=g(a)$. (Note this telescoping
uses only the pointwise bound (IV) — no continuity or other regularity of $f$ is assumed
anywhere.) Hence $g\equiv c$ for some constant $c\ge 0$ (nonnegativity from Step 2), i.e.

$$f(x)=x+c,\qquad c\ge 0.$$

Together with the verification, the solutions are exactly $f(x)=x+c$ with $c\ge 0$. $\blacksquare$

## Approach summary (written 2026-07-22 15:58 PDT)

1. **Recognize the shape:** the chain is $\mathrm{QM}(x,f(y))\ \ge\ \text{middle}\ \ge\ \mathrm{GM}(x,f(y))$, and for $f(x)=x+c$ the middle is exactly $\mathrm{AM}(x,f(y))$ — suggesting the answer is the family of shifts.
2. **Exploit the equality case:** at $x=f(y)$ the QM and GM coincide, squeezing the middle and yielding the exact equation $f(f(y))=2f(y)-y$.
3. **Orbit argument:** iterating $f$ produces an arithmetic progression $y+n(f(y)-y)$, which stays positive only if $f(y)\ge y$.
4. **Self-substitution $x=f(z)$** into the left inequality converts the chain into the clean two-point inequality $(A-B)^2\ge 2(A+B)\delta+\delta^2$ for $\delta=g(z)-g(y)$, giving the Hölder-type bound $|g(z)-g(y)|\le (z-y)^2/(4\min(y,z))$.
5. **Telescoping** over a fine partition forces $g$ to be constant — no regularity assumptions needed.

**Verification performed:** algebraic identities checked by $10^5$-trial random substitution
(scripts `check1.py`, `check2.py` in session scratchpad); chain verified numerically for
$f(x)=x+c$ over 200{,}000 random samples; full proof adversarially reviewed step-by-step by
an independent checker (verdict: correct, no gaps).
