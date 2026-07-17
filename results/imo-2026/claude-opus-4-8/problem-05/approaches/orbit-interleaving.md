## Status
solved

## Approaches tried
- (round 1) orbit + two-AP interleaving at infinity, then openness+connectedness to kill the
  fixed-point/defect coexistence — **worked**; complete rigorous proof of the full characterization.

## Current best
Complete proof (below). The functional equation (★) f(f(y))=2f(y)−y is forced by the sandwich at
x=f(y); iterating it makes each forward orbit an arithmetic progression, which yields g:=f−id≥0 and
g constant on orbits; the off-diagonal lever (∗) plus interleaving two orbits at infinity forces all
positive values of g to be a single constant c>0; and the cross-constraint (b−z)²≥4cz makes the
zero-set and the defect-set both open, so connectedness of (0,∞) forces one to be empty. Answer:
f(x)=x+c for every c≥0, and no others.

## Full proof

We determine all functions f:(0,∞)→(0,∞) satisfying, for all x,y>0,
$$\sqrt{\frac{x^2+f(y)^2}{2}}\;\ge\;\frac{f(x)+y}{2}\;\ge\;\sqrt{x\,f(y)}.\qquad(\dagger)$$

**Answer.** The solutions are exactly the functions $f(x)=x+c$ with $c$ a constant $\ge 0$.

Throughout, all quantities $x,y,f(x),f(y)$ are positive, so every expression under a square root is
positive and both sides of each inequality in $(\dagger)$ are positive. Squaring a comparison of two
positive numbers is an equivalence, so $(\dagger)$ is equivalent to the pair
$$2\bigl(x^2+f(y)^2\bigr)\;\ge\;(f(x)+y)^2\quad(\mathrm{L}^2),\qquad (f(x)+y)^2\;\ge\;4x\,f(y)\quad(\mathrm{R}^2),$$
valid for all $x,y>0$. (The right inequality of $(\dagger)$ squares to $(\mathrm{R}^2)$ after
multiplying by $4$; the left squares to $(\mathrm{L}^2)$ after multiplying by $4$.)

---

### Part (a): Sufficiency

Let $c\ge 0$ be a constant and $f(x)=x+c$. First, $f$ maps $(0,\infty)$ into $(0,\infty)$: for $x>0$
we have $f(x)=x+c>0$ since both $x>0$ and $c\ge 0$. Now check $(\mathrm{L}^2)$ and $(\mathrm{R}^2)$.

For $(\mathrm{R}^2)$, with $f(x)=x+c$ and $f(y)=y+c$,
$$(f(x)+y)^2-4x\,f(y)=(x+c+y)^2-4x(y+c)=(x-y-c)^2\;\ge\;0,$$
the middle equality being the algebraic identity
$$(x+c+y)^2-4x(y+c)=x^2+y^2+c^2-2xy-2xc+2yc=(x-y-c)^2,$$
which one verifies by expanding both sides (checked symbolically). Hence $(\mathrm{R}^2)$ holds.

For $(\mathrm{L}^2)$, writing $u=y+c=f(y)$,
$$2\bigl(x^2+f(y)^2\bigr)-(f(x)+y)^2=2x^2+2u^2-(x+u)^2=(x-u)^2=(x-y-c)^2\;\ge\;0,$$
so $(\mathrm{L}^2)$ holds. Thus $f(x)=x+c$ satisfies $(\dagger)$ for every $c\ge 0$.

Finally, $c\ge 0$ is necessary for a function of the form $f(x)=x+c$ to be admissible at all: if
$c<0$, then for $0<x<-c$ we would have $f(x)=x+c<0\notin(0,\infty)$, so $f$ would fail to have
codomain $(0,\infty)$. Hence exactly the values $c\ge 0$ give admissible affine solutions.

---

### Part (b): Necessity

Let $f$ be any solution of $(\dagger)$. Define
$$g(y):=f(y)-y\qquad(y>0).$$

#### Step 1: The functional equation $(\star)$.

Fix $y>0$ and substitute $x=f(y)$ into $(\mathrm{R}^2)$ and $(\mathrm{L}^2)$.

In $(\mathrm{R}^2)$: $(f(f(y))+y)^2\ge 4\,f(y)\cdot f(y)=4f(y)^2$. Both $f(f(y))+y$ and $2f(y)$ are
positive, so taking square roots gives $f(f(y))+y\ge 2f(y)$, i.e. $f(f(y))\ge 2f(y)-y$.

In $(\mathrm{L}^2)$: $2\bigl(f(y)^2+f(y)^2\bigr)\ge (f(f(y))+y)^2$, i.e. $(2f(y))^2\ge(f(f(y))+y)^2$;
taking square roots of the two positive numbers gives $2f(y)\ge f(f(y))+y$, i.e.
$f(f(y))\le 2f(y)-y$.

Combining the two,
$$f(f(y))=2f(y)-y\qquad\text{for all }y>0.\qquad(\star)$$

#### Step 2: Orbits are arithmetic progressions; $g\ge 0$ and $g$ is orbit-invariant.

Fix $y>0$ and define the forward orbit $a_0=y$, $a_{n+1}=f(a_n)$ for $n\ge0$. Every $a_n$ lies in
$(0,\infty)$ because $f$ has codomain $(0,\infty)$. Applying $(\star)$ at the point $a_n$ gives
$f(f(a_n))=2f(a_n)-a_n$, i.e.
$$a_{n+2}=2a_{n+1}-a_n\qquad(n\ge0).$$
Thus the successive differences $a_{n+1}-a_n$ are all equal to $a_1-a_0=f(y)-y=g(y)$, so
$$a_n=y+n\,g(y)\qquad(n\ge0).$$

If $g(y)<0$, then $a_n=y+n\,g(y)\to-\infty$, so some $a_n<0$, contradicting $a_n>0$. Hence
$$g(y)\ge 0\quad\text{for all }y>0,\qquad\text{i.e. } f(y)\ge y.$$

Moreover $g$ is invariant along the orbit: using $(\star)$,
$$g(f(y))=f(f(y))-f(y)=\bigl(2f(y)-y\bigr)-f(y)=f(y)-y=g(y).$$
Applying this repeatedly, $g(a_n)=g(y)$ for every $n\ge0$. In particular, $g$ takes the constant
value $g(y)$ on the whole orbit
$$\mathcal O(y)=\{\,y+n\,g(y):n\ge0\,\},$$
which, when $g(y)>0$, is an infinite arithmetic progression with common difference $g(y)$.

#### Step 3: The off-diagonal lever $(\ast)$.

Write $f=\mathrm{id}+g$ in $(\mathrm{R}^2)$ at a general pair $(a,b)$ (with $x=a,y=b$):
$$(f(a)+b)^2-4a\,f(b)=(a+g(a)+b)^2-4a\,(b+g(b)).$$
Expanding $(a+g(a)+b)^2=(a+b)^2+2(a+b)g(a)+g(a)^2$ and using $(a+b)^2-4ab=(a-b)^2$,
$$(a+g(a)+b)^2-4a\,(b+g(b))=(a-b)^2+2(a+b)g(a)+g(a)^2-4a\,g(b)$$
(the identity is verified symbolically). Since the left side is $\ge0$ by $(\mathrm{R}^2)$,
$$(a-b)^2+2(a+b)\,g(a)+g(a)^2\;\ge\;4a\,g(b)\qquad\text{for all }a,b>0.\qquad(\ast)$$

#### Step 4: All positive values of $g$ are equal.

Suppose $g(a)=s_a>0$ and $g(b)=s_b>0$ for some $a,b>0$. Both orbits are infinite arithmetic
progressions, $\mathcal O(a)$ with step $s_a$ and $\mathcal O(b)$ with step $s_b$, on which $g$ is
constant ($=s_a$ on $\mathcal O(a)$, $=s_b$ on $\mathcal O(b)$) by Step 2.

For each integer $k\ge0$ set $A_k=a+k\,s_a\in\mathcal O(a)$, so $g(A_k)=s_a$ and $A_k\to\infty$. Take
$k$ large enough that $A_k\ge b+s_b$, and define
$$j=\left\lfloor\frac{A_k-b}{s_b}\right\rfloor,\qquad B_k=b+j\,s_b\in\mathcal O(b).$$
Because $A_k-b\ge s_b$ we have $j\ge1\ge0$, so $B_k$ is a genuine point of $\mathcal O(b)$ and
$g(B_k)=s_b$. By the definition of the floor,
$$b+j\,s_b\le A_k<b+(j+1)s_b\quad\Longrightarrow\quad 0\le A_k-B_k<s_b .$$

Apply $(\ast)$ at the pair $(A_k,B_k)$ (so $a\mapsto A_k$, $b\mapsto B_k$, $g(a)=s_a$, $g(b)=s_b$):
$$(A_k-B_k)^2+2(A_k+B_k)\,s_a+s_a^2\;\ge\;4A_k\,s_b .$$
Using $A_k-B_k<s_b$ (so $(A_k-B_k)^2<s_b^2$) and $B_k\le A_k$ (so $A_k+B_k\le 2A_k$) on the left,
$$4A_k\,s_b\;<\;s_b^2+2(2A_k)\,s_a+s_a^2\;=\;s_b^2+4A_k\,s_a+s_a^2 .$$
Dividing by $4A_k>0$,
$$s_b\;<\;s_a+\frac{s_a^2+s_b^2}{4A_k}.$$
Letting $k\to\infty$ (so $A_k\to\infty$) yields $s_b\le s_a$. Interchanging the roles of $a$ and $b$
gives $s_a\le s_b$. Hence $s_a=s_b$.

Therefore there is a single constant $c\ge 0$ such that
$$g(y)\in\{0,c\}\quad\text{for all }y>0,$$
where $c$ is the common positive value of $g$ (and we may take $c=0$ if $g$ is identically $0$).
Set
$$Z=\{\,y>0:g(y)=0\,\}\ (\text{i.e. } f(y)=y),\qquad P=\{\,y>0:g(y)=c\,\}.$$
If $c=0$ then $Z=(0,\infty)$ and $f=\mathrm{id}$, i.e. $f(x)=x+0$; we are done. Assume henceforth
$c>0$, so $Z\sqcup P=(0,\infty)$ is a disjoint partition. If $P=\varnothing$ then $g\equiv0$ and
$f(x)=x$; if $Z=\varnothing$ then $g\equiv c$ and $f(x)=x+c$. It remains to show that $Z$ and $P$
cannot both be nonempty.

#### Step 5: The zero-set and the defect-set cannot coexist.

Assume $c>0$ and both $Z\ne\varnothing$ and $P\ne\varnothing$; we derive a contradiction.

**Cross-constraint.** Take any $z\in Z$ and $b\in P$, so $f(z)=z$ and $f(b)=b+c$. Apply
$(\mathrm{R}^2)$ at $(x,y)=(z,b)$:
$$(f(z)+b)^2\ge 4z\,f(b)\;\Longrightarrow\;(z+b)^2\ge 4z(b+c).$$
Expanding, $(z+b)^2-4z(b+c)=z^2-2zb+b^2-4zc=(b-z)^2-4cz$ (verified symbolically), so
$$(b-z)^2\;\ge\;4cz\qquad\text{for all }z\in Z,\ b\in P.\qquad(\mathrm{C})$$

**$P$ is open in $(0,\infty)$.** Let $b\in P$ and put $\varepsilon=\min\!\bigl(\tfrac b2,\sqrt{cb}\bigr)>0$.
Consider any $t$ with $|t-b|<\varepsilon$; then $t\in(b-\tfrac b2,\,b+\tfrac b2)=(\tfrac b2,\tfrac{3b}{2})\subset(0,\infty)$,
so $t$ lies in the domain and $t\in Z$ or $t\in P$. Suppose $t\in Z$. Then by $(\mathrm C)$ (with
$z=t$), $(b-t)^2\ge 4ct$. But $t>b-\varepsilon\ge \tfrac b2$, so $4ct>4c\cdot\tfrac b2=2cb$, while
$(b-t)^2<\varepsilon^2\le cb<2cb$; this contradicts $(b-t)^2\ge 4ct$. Hence no such $t$ is in $Z$, so
every $t\in(b-\varepsilon,b+\varepsilon)$ lies in $P$. Thus $P$ is open.

**$Z$ is open in $(0,\infty)$.** Let $z\in Z$ and put $\varepsilon=\min\!\bigl(\tfrac z2,\,2\sqrt{cz}\bigr)>0$.
Consider any $t$ with $|t-z|<\varepsilon$; then $t\in(\tfrac z2,\tfrac{3z}{2})\subset(0,\infty)$, so
$t\in Z$ or $t\in P$. Suppose $t\in P$. Then by $(\mathrm C)$ (with $b=t$), $(t-z)^2\ge 4cz$, i.e.
$|t-z|\ge 2\sqrt{cz}\ge\varepsilon$, contradicting $|t-z|<\varepsilon$. Hence no such $t$ is in $P$,
so every $t\in(z-\varepsilon,z+\varepsilon)$ lies in $Z$. Thus $Z$ is open.

**Connectedness.** We have written $(0,\infty)=Z\sqcup P$ as a disjoint union of two open sets, both
nonempty by assumption. This contradicts the connectedness of the interval $(0,\infty)$ (a partition
of a connected space into two nonempty disjoint open sets is impossible). Therefore the assumption is
false: at least one of $Z,P$ is empty.

Consequently, when $c>0$ we must have $Z=\varnothing$ (whence $g\equiv c$, $f(x)=x+c$) or
$P=\varnothing$ (whence $g\equiv0$, $f(x)=x$). Combined with the $c=0$ case of Step 4, every solution
satisfies
$$f(x)=x+c\quad\text{for a single constant }c\ge 0.$$

---

### Conclusion

By Part (b) every solution has the form $f(x)=x+c$ with $c\ge0$, and by Part (a) every such function
is indeed a solution (and $c\ge0$ is forced by the codomain). Hence the complete solution set of
$(\dagger)$ is
$$\boxed{\,f(x)=x+c,\qquad c\ \text{a constant with}\ c\ge 0.\,}$$
$\blacksquare$

## Promotable lemmas

- **`sandwich-collapse` (★).** For any solution $f$ of $(\dagger)$, $f(f(y))=2f(y)-y$ for all $y>0$.
  *Proof:* substitute $x=f(y)$ into $(\mathrm R^2)$ and $(\mathrm L^2)$; the two give
  $f(f(y))\ge 2f(y)-y$ and $\le$, respectively (Step 1). Certified content: Step 1 above.

- **`defect-nonneg-orbit-invariant`.** With $g=f-\mathrm{id}$: $g(y)\ge0$ for all $y$, and
  $g(f(y))=g(y)$; the forward orbit is the AP $\{y+n\,g(y):n\ge0\}$ on which $g$ is constant.
  *Proof:* iterate $(\star)$ to get $a_{n+2}=2a_{n+1}-a_n$, hence $a_n=y+ng(y)$; positivity forces
  $g\ge0$; $g(f(y))=g(y)$ from $(\star)$ (Step 2).

- **`off-diagonal-lever` (∗).** For any solution, with $g=f-\mathrm{id}$,
  $(a-b)^2+2(a+b)g(a)+g(a)^2\ge 4a\,g(b)$ for all $a,b>0$. *Proof:* rewrite $(\mathrm R^2)$ with
  $f=\mathrm{id}+g$ (Step 3; identity verified symbolically).

- **`all-positive-defects-equal`.** If $g(a)>0$ and $g(b)>0$ then $g(a)=g(b)$ (Step 4). Together with
  the above this shows $g$ takes values in $\{0,c\}$ for a single $c\ge0$.
