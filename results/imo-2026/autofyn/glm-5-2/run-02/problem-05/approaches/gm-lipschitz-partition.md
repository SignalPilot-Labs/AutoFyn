# gm-lipschitz-partition

## Status
partial

## Approaches tried
- (round 1) Forcing-equality route: derive `|g(z)-g(y)| <= (sqrt(f(z))-sqrt(f(y)))^2` from the RHS (GM) inequality at the swapped equality-forcing substitutions `x=f(z)` and `x=f(y)`, then close by a discrete partition (tiny-Lipschitz). Algebra of the bound verified by hand and with sympy. **Open gap (G1): the quadratic self-bound admits a "large-deviation" branch that Fact 5 alone does not rule out — the partition path is doomed as a standalone uniqueness route.**
- (round 1, this round, PIVOT per outline-reviewer) Abandon the standalone partition. Fact 5 is retained as a *certified lemma* and becomes the engine for part (A) (at-most-one positive value): chained across a close encounter of two distinct positive-value orbits, Fact 5 forces the positive-value difference to be bounded above by a quantity that vanishes as the encounter point goes to infinity — contradiction. Part (B) (a fixed point forces `g equiv 0`) uses the orbit-close-encounter cover iteration with the corrected zero-region radius `2 sqrt(c x_0)` and quadratic cover growth. Existence is AM-GM / QM-AM. **All gaps closed; full proof below.**
- (round 2) Part B cover-iteration gap closed by replacing rightward-only iteration with the maximal-connected-component boundary-push argument (same `(†)` zero-region radius); Part A (Fact 5) unchanged.

## Current best
The full proof is closed. Headline: $f(x) = x + c$ for any constant $c \ge 0$. The two genuinely-different instruments this approach contributes versus `orbit-close-encounter` are (i) **Fact 5** as a derived inequality — a Lipschitz-type self-referential bound on $g$ via the gap of $\sqrt f$, proven cleanly from the RHS inequality and the iterate identity — and (ii) the use of **Fact 5 as the engine of part (A)** (the close-encounter contradiction is read off Fact 5, not off the raw $(\star)$ constraint).

## Full proof

**Notation.** Set $g(x) := f(x) - x$, so $f(x) = x + g(x)$. The target is to show $g$ is a constant $\ge 0$ on $\mathbb R_{>0}$, i.e. $f(x) = x + c$ for some $c \ge 0$.

We repeatedly use the standard AM-GM identity for positive $a, b$:
$$2(\mathrm{AM}-\mathrm{GM})(a,b) \;=\; (a+b) - 2\sqrt{ab} \;=\; (\sqrt a - \sqrt b)^2. \tag{AMGM}$$
(cite `knowledge_base.md`, *Standard inequalities — AM-GM, QM-AM*; the identity $2(\mathrm{AM}-\mathrm{GM})=(\sqrt a-\sqrt b)^2$ is the load-bearing algebra).

---

### Step 0 — Existence (the family $f(x)=x+c$, $c\ge 0$, works)

Fix $c\ge 0$ and set $f(x) = x + c$. Then $f(y) = y + c$, so the middle term is
$$\frac{f(x)+y}{2} = \frac{x+y+c}{2} = \frac{x + f(y)}{2} = \mathrm{AM}\bigl(x,\,f(y)\bigr).$$
The outer bounds are $\sqrt{x\,f(y)} = \mathrm{GM}\bigl(x,f(y)\bigr)$ and $\sqrt{\tfrac{x^2 + f(y)^2}{2}} = \mathrm{QM}\bigl(x,f(y)\bigr)$ (the quadratic mean / RMS). The required chain
$$\mathrm{QM}(x,f(y)) \;\ge\; \mathrm{AM}(x,f(y)) \;\ge\; \mathrm{GM}(x,f(y))$$
is exactly the universal AM-GM and QM-AM inequalities on the positive pair $\bigl(x, f(y)\bigr)$, valid for every $x, y > 0$. Positivity $f:\mathbb R_{>0}\to\mathbb R_{>0}$ requires $c\ge 0$. (cite `knowledge_base.md`, *Standard inequalities — AM-GM, QM-AM; equality cases pin down the extremal configuration.*) $\quad\square_{\text{Step 0}}$

---

### Step 1 — The second iterate $f(f(y)) = 2f(y) - y$

Substitute $x = f(y)$ (valid: $f(y) > 0$) in the original chain.

*LHS inequality:* $\sqrt{\tfrac{f(y)^2 + f(y)^2}{2}} = f(y) \ge \tfrac{f(f(y)) + y}{2}$, so $f(f(y)) \le 2f(y) - y$.

*RHS inequality:* $\tfrac{f(f(y)) + y}{2} \ge \sqrt{f(y)\cdot f(y)} = f(y)$, so $f(f(y)) \ge 2f(y) - y$.

Combining,
$$\boxed{f(f(y)) = 2f(y) - y \quad\text{for all } y > 0.} \tag{1}$$
Both inequalities are used: each becomes an equality exactly when $x = f(y)$, the equality case of AM-GM / QM-AM on $\bigl(x, f(y)\bigr)$. (cite `knowledge_base.md`, *Functional equations — test special values*; *Standard inequalities — equality cases*.) $\quad\square_{\text{Step 1}}$

---

### Step 2 — Orbit structure, injectivity, and $g\ge 0$

Expand (1): $f(f(y)) = f(y) + g(f(y))$ and $2f(y) - y = f(y) + (f(y)-y) = f(y) + g(y)$. Equating,
$$\boxed{g(f(y)) = g(y) \quad\text{for all } y > 0.} \tag{2}$$
So $g$ is constant along each forward orbit. Inductively, $f^{n}(y) = y + n\,g(y)$: the forward orbit of $y$ is the arithmetic progression $\{y + n\,g(y) : n \ge 0\}$.

*Injectivity.* If $f(a) = f(b)$, applying $f$ and using (1) gives $2f(a) - a = 2f(b) - b$, hence $a = b$. (cite `knowledge_base.md`, *Functional equations — injectivity*.)

*Non-negativity.* The forward orbit $\{y + n\,g(y) : n \ge 0\}$ lies in $\mathbb R_{>0}$, so $y + n\,g(y) > 0$ for every $n \ge 0$. If $g(y) < 0$, taking $n \to \infty$ gives $y + n g(y) \to -\infty < 0$, contradiction. Therefore
$$\boxed{g(y) \ge 0 \quad\text{for all } y > 0, \quad\text{i.e. } f \ge \mathrm{id}.} \tag{3}$$
(cite `knowledge_base.md`, *Invariants & monovariants — orbit analysis*.) $\quad\square_{\text{Step 2}}$

---

### Step 3 — Fact 5 (the crux instrument): a Lipschitz-type self-referential bound on $g$

**Lemma (Fact 5).** *For all $y, z > 0$,*
$$\boxed{\bigl|\,g(z) - g(y)\,\bigr| \;\le\; \bigl(\sqrt{f(z)} - \sqrt{f(y)}\bigr)^2.} \tag{F5}$$

*Proof.* Substitute $x = f(z)$ (valid: $f(z) > 0$) into the RHS inequality $\tfrac{f(x) + y}{2} \ge \sqrt{x\,f(y)}$:
$$\frac{f(f(z)) + y}{2} \ge \sqrt{f(z)\,f(y)}.$$
By (1), $f(f(z)) = 2f(z) - z = f(z) + g(z)$. Also $f(y) = y + g(y)$, so $f(z) + y = f(z) + f(y) - g(y)$. Hence the LHS equals
$$\frac{f(z) + f(y) + g(z) - g(y)}{2} = \mathrm{AM}\bigl(f(z), f(y)\bigr) + \frac{g(z) - g(y)}{2}.$$
The RHS is $\mathrm{GM}\bigl(f(z), f(y)\bigr)$. Therefore
$$\frac{g(z) - g(y)}{2} \;\ge\; -\bigl(\mathrm{AM}-\mathrm{GM}\bigr)\bigl(f(z), f(y)\bigr) \;=\; -\frac{\bigl(\sqrt{f(z)} - \sqrt{f(y)}\bigr)^2}{2},$$
using (AMGM). That is,
$$g(z) - g(y) \;\ge\; -\bigl(\sqrt{f(z)} - \sqrt{f(y)}\bigr)^2. \tag{F5+}$$
Swapping the roles of $y$ and $z$ (substitute $x = f(y)$ and read the target variable as $z$) gives the identical inequality
$$g(y) - g(z) \;\ge\; -\bigl(\sqrt{f(z)} - \sqrt{f(y)}\bigr)^2. \tag{F5-}$$
Combining (F5+) and (F5-) yields (F5). $\quad\square_{\text{Fact 5}}$

*Redundancy of the LHS inequality for uniqueness.* The LHS (RMS) inequality gives the parallel (one-sided) bound $g(z) - g(y) \le 2(\mathrm{RMS}-\mathrm{AM})(f(z),f(y))$. Since $\mathrm{RMS}+\mathrm{AM} \ge \mathrm{AM}+\mathrm{GM}$ implies $\mathrm{RMS}-\mathrm{AM} \le \mathrm{AM}-\mathrm{GM}$, this is weaker than (F5); so after Step 1 the LHS inequality carries no further uniqueness information. (We do not use it again.) $\quad\square_{\text{Step 3}}$

---

### Step 4 — Part (A): $g$ takes at most one positive value

We prove (A) using **Fact 5 as the engine**, chained across a close encounter of two distinct positive-value orbits. The auxiliary number-theoretic input is the following standard lemma.

**Lemma (close encounter).** *Let $A = \{a + np : n \ge 0\}$, $B = \{b + mq : m \ge 0\}$ with $p, q > 0$ be two unbounded forward arithmetic progressions. For every $\epsilon > 0$ there exist $n, m \ge 0$ with*
$$|A_n - B_m| \le \epsilon, \qquad \min(A_n, B_m) \to \infty$$
*(i.e. arbitrarily large $\epsilon$-close encounters), **provided** either (i) $p/q \notin \mathbb Q$, or (ii) $p/q \in \mathbb Q$ and $\epsilon \ge \delta_0$, where $\delta_0 := \min_{k \in \mathbb Z} |a - b + k d| \in (0, d/2]$ with $d := \gcd(p,q)$, and $a \not\equiv b \pmod d$.*

*Proof of close encounter.* Two cases.

*Case (i): $p/q \notin \mathbb Q$.* The sequence of fractional parts $\{((a + np) - b)/q\}_{n \ge 0}$ is dense (equidistributed) in $[0,1)$ by Kronecker / Weyl equidistribution (cite `knowledge_base.md`, *Kronecker / Weyl equidistribution*). For any $N$ there exists $n \ge N$ with $\{((a+np)-b)/q\} \in [0, \epsilon/q] \cup [1-\epsilon/q, 1)$. Taking $m := \lfloor ((a+np) - b)/q \rfloor \ge 0$ (for $n$ large enough), we get $|(a+np) - (b + mq)| \le \epsilon$, and $A_n = a + np \to \infty$ as $n \to \infty$.

*Case (ii): $p/q \in \mathbb Q$.* Write $p = P d$, $q = Q d$ with $\gcd(P,Q) = 1$ and $d = \gcd(p,q)$. Then $A \subset a + d\mathbb Z$ and $B \subset b + d\mathbb Z$. If $a \equiv b \pmod d$, the two progressions, both unbounded above within the same residue class, must intersect: a collision. If $a \not\equiv b \pmod d$, the cyclic distance between the residue classes is $\delta_0 = \min_{k \in \mathbb Z}|a - b + kd| \in (0, d/2]$. Pick $k_0 \in \mathbb Z$ with $a - b + k_0 d = \pm \delta_0$.

We seek $n, m \ge 0$ with $A_n - B_m = a - b + d(P n - Q m) = \pm \delta_0 = a - b + k_0 d$, i.e. $P n - Q m = k_0$. Since $\gcd(P, Q) = 1$, Bézout gives one integer solution $(n_0, m_0) \in \mathbb Z^2$ of $P n - Q m = k_0$; the full solution family is $(n_0 + Q\ell,\; m_0 + P\ell)$ for $\ell \in \mathbb Z$. Taking $\ell \to +\infty$ makes both $n = n_0 + Q\ell \to +\infty$ and $m = m_0 + P\ell \to +\infty$ (since $P, Q > 0$); for $\ell$ large enough, $n, m \ge 0$. For these, $A_n - B_m = \pm \delta_0 \le \epsilon$, and $\min(A_n, B_m) \to \infty$. (cite `knowledge_base.md`, *Modular arithmetic / Bézout*.) $\quad\square_{\text{close encounter}}$

*Proof of (A).* Suppose for contradiction that $g$ takes two distinct positive values $c_a < c_b$. Pick $a, b > 0$ with $g(a) = c_a$, $g(b) = c_b$. By (2), $g$ is constant on each forward orbit, so the level sets $L_{c_a} \supseteq \{a + n c_a : n \ge 0\}$ and $L_{c_b} \supseteq \{b + m c_b : m \ge 0\}$ contain two unbounded forward APs with steps $p = c_a$, $q = c_b$.

We apply the close-encounter lemma with $\epsilon := c_a / 2$. To verify the hypothesis in case (ii): there $d = \gcd(c_a, c_b) \le c_a$ (since $d \mid c_a$), so $\delta_0 \le d/2 \le c_a / 2 = \epsilon$. If $a \equiv b \pmod d$, the two orbits collide at some point, forcing $g$ to take both values $c_a$ and $c_b$ there — impossible, since $g$ is a function — so we are in the $a \not\equiv b \pmod d$ subcase and the lemma applies. In case (i) the lemma applies directly. Either way, we obtain sequences $n_k, m_k \to \infty$ with
$$|A_{n_k} - B_{m_k}| \le \epsilon = c_a/2, \qquad t_k := \min(A_{n_k}, B_{m_k}) \to \infty.$$

Now apply Fact 5 with $y = A_{n_k} \in L_{c_a}$ (so $g(y) = c_a$) and $z = B_{m_k} \in L_{c_b}$ (so $g(z) = c_b$):
$$\underbrace{c_b - c_a}_{=\,\delta\,>\,0} \;=\; |g(z) - g(y)| \;\le\; \bigl(\sqrt{f(z)} - \sqrt{f(y)}\bigr)^2.$$
We bound the RHS. Since $f(y) = y + c_a$ and $f(z) = z + c_b$,
$$|f(z) - f(y)| \;\le\; |z - y| + |c_b - c_a| \;\le\; \epsilon + \delta,$$
and, using $|\sqrt{u} - \sqrt{v}| = |u - v|/(\sqrt{u} + \sqrt{v}) \le |u - v|/(2\sqrt{\min(u,v)})$,
$$\bigl(\sqrt{f(z)} - \sqrt{f(y)}\bigr)^2 \;\le\; \frac{|f(z) - f(y)|^2}{4\,\min(f(y), f(z))} \;\le\; \frac{(\epsilon + \delta)^2}{4\,\min(f(y), f(z))}.$$
Since $\min(f(y), f(z)) = \min(y + c_a, z + c_b) \ge \min(y, z) = t_k \to \infty$, the right-hand side tends to $0$ as $k \to \infty$. Thus
$$0 \;<\; \delta \;=\; c_b - c_a \;\le\; \frac{(\epsilon + \delta)^2}{4\,t_k} \;\xrightarrow{k \to \infty}\; 0,$$
a contradiction. Therefore $g$ takes **at most one positive value**. $\quad\square_{\text{(A)}}$

Combining with (3), $g : \mathbb R_{>0} \to \{0, c\}$ for some $c > 0$, or $g \equiv 0$, or $g \equiv c > 0$.

---

### Step 5 — Part (B): a fixed point forces $g \equiv 0$

Square the RHS inequality $\tfrac{f(x)+y}{2} \ge \sqrt{x\,f(y)}$ (both sides positive):
$$\bigl(f(x) + y\bigr)^2 \ge 4\,x\,f(y).$$
Substituting $f = \mathrm{id} + g$ and expanding,
$$\bigl(x + g(x) + y\bigr)^2 - 4x\bigl(y + g(y)\bigr) = (x - y)^2 + 2(x+y)\,g(x) + g(x)^2 - 4x\,g(y) \;\ge\; 0,$$
i.e.
$$\boxed{4\,x\,g(y) \;\le\; (x - y)^2 + 2(x+y)\,g(x) + g(x)^2 \quad\text{for all } x, y > 0.} \tag{$\star$}$$
(cite `knowledge_base.md`, *SOS / completing the square*.)

Suppose $x_0 > 0$ is a fixed point: $g(x_0) = 0$, equivalently $f(x_0) = x_0$. Evaluate $(\star)$ at $x = x_0$:
$$4\,x_0\,g(y) \;\le\; (x_0 - y)^2 + 0 + 0, \qquad\text{i.e.}\qquad \boxed{g(y) \;\le\; \frac{(y - x_0)^2}{4\,x_0} \;\text{ for all } y > 0.} \tag{$\dagger$}$$

Now invoke part (A): $g$ takes values in $\{0, c\}$ for some $c > 0$, or $g \equiv 0$. In the latter case we are done. In the former case, by $(\dagger)$, wherever $(y - x_0)^2 / (4 x_0) < c$, i.e. $|y - x_0| < 2\sqrt{c\,x_0}$, we have $g(y) < c$, hence $g(y) = 0$. So the **zero-region**
$$Z(x_0) \;:=\; \bigl(x_0 - 2\sqrt{c\,x_0},\; x_0 + 2\sqrt{c\,x_0}\bigr) \cap \mathbb R_{>0}$$
is contained in $\{y : g(y) = 0\}$; every point of $Z(x_0)$ is itself a fixed point. (No lower bound on $c$ is needed: this works for any $c > 0$.)

**Zero-region around any fixed point.** The bound $(\dagger)$ was derived by substituting $x = x_0$ into $(\star)$; the identical substitution at any fixed point $s$ (i.e. any $s > 0$ with $g(s) = 0$) gives, by the same algebra,
$$g(y) \;\le\; \frac{(y - s)^2}{4\,s} \qquad\text{for all } y > 0. \tag{$\dagger_s$}$$
Hence, wherever $|y - s| < 2\sqrt{c\,s}$, $(\dagger_s)$ gives $g(y) < c$, so $g(y) = 0$. That is,
$$\bigl(s - 2\sqrt{c\,s},\; s + 2\sqrt{c\,s}\bigr) \cap \mathbb R_{>0} \;\subseteq\; S \;:=\; \{y > 0 : g(y) = 0\} \quad\text{for every fixed point } s \in S. \tag{4}$$
In particular $S$ is **open**: every $s \in S$ is the centre of an open interval (the one in (4)) contained in $S$.

**Maximal connected component (boundary-push).** Let $I = (\alpha, \beta)$ be the connected component of the open set $S$ that contains $x_0$. (It is a nonempty open interval, since $x_0 \in S$ and $S$ is open.) We show $\alpha = 0$ and $\beta = \infty$, which forces $I = (0, \infty) = \mathbb R_{>0}$, i.e. $S = \mathbb R_{>0}$, i.e. $g \equiv 0$ — contradicting $c > 0$.

*Right endpoint: $\beta = \infty$.* Suppose for contradiction $\beta < \infty$. Since $\beta$ is the right endpoint of the component containing $x_0$ and $x_0 \in I$, we have $\beta \ge x_0 + 2\sqrt{c\,x_0} > 0$ (by (4) applied at $s = x_0$, the entire interval around $x_0$ lies in $S$, hence in $I$). Pick $s \in I$ arbitrarily close to $\beta$ from below; then $s \in S$, so by (4) the whole interval $(s - 2\sqrt{c\,s},\; s + 2\sqrt{c\,s})$ lies in $S$. This interval is connected and contains $s \in I$, so it is contained in the same component $I$. Its right endpoint is $s + 2\sqrt{c\,s}$. As $s \to \beta^{-}$, continuity of $s \mapsto s + 2\sqrt{c\,s}$ on $(0,\infty)$ gives
$$s + 2\sqrt{c\,s} \;\longrightarrow\; \beta + 2\sqrt{c\,\beta}.$$
Because $\beta > 0$ and $c > 0$, the limit $\beta + 2\sqrt{c\,\beta} > \beta$ (strictly). So for $s$ close enough to $\beta$ from below, $s + 2\sqrt{c\,s} > \beta$, which places points of $I$ strictly to the right of $\beta$ — contradicting the definition of $\beta$ as the supremum of $I$. Hence $\beta = \infty$.

*Left endpoint: $\alpha = 0$.* Suppose for contradiction $\alpha > 0$. Pick $s \in I$ arbitrarily close to $\alpha$ from above; then $s \in S$, and by (4) the interval $(s - 2\sqrt{c\,s},\; s + 2\sqrt{c\,s}) \subseteq S$ is connected, contains $s \in I$, hence is contained in $I$. Its left endpoint $s - 2\sqrt{c\,s}$ tends, as $s \to \alpha^{+}$, to
$$\alpha - 2\sqrt{c\,\alpha}.$$
Because $\alpha > 0$ and $c > 0$, this limit satisfies $\alpha - 2\sqrt{c\,\alpha} < \alpha$ (strictly). So for $s$ close enough to $\alpha$ from above, $s - 2\sqrt{c\,s} < \alpha$, placing points of $I$ strictly to the left of $\alpha$ — contradicting the definition of $\alpha$ as the infimum of $I$. The only remaining option (since $S \subseteq \mathbb R_{>0}$, so $I \subseteq \mathbb R_{>0}$) is $\alpha = 0$.

Combining, $I = (0, \infty) = \mathbb R_{>0}$, so $S = \mathbb R_{>0}$, i.e. $g \equiv 0$ on all of $\mathbb R_{>0}$. This contradicts the assumption that $g$ also takes the positive value $c > 0$. Therefore: **if a fixed point exists, $g$ cannot take any positive value; combined with $g \ge 0$ from (3), this gives $g \equiv 0$, i.e. $f(x) = x$ (the case $c = 0$).** $\quad\square_{\text{(B)}}$

---

### Step 6 — Synthesis

By (A) and (3), $g$ is either identically $0$, identically a positive constant $c$, or the mixed $\{0, c\}$ case.

- *If the mixed $\{0, c\}$ case holds*, some point has $g = 0$, i.e. a fixed point exists, and (B) forces $g \equiv 0$, contradicting $c > 0$. Excluded.
- *If $g \equiv 0$*, every point is a fixed point; (B) is consistent and gives $f(x) = x$ (i.e. $c = 0$).
- *If $g \equiv c > 0$*, no fixed point exists, (B) does not run, and $f(x) = x + c$ with $c > 0$.

Combining with the existence check (Step 0), the complete solution set is
$$\boxed{\,f(x) = x + c \quad\text{for any constant } c \ge 0.\,} \qquad\blacksquare$$

---

## Promotable lemmas

- **Fact 5** (self-referential $g$-bound): for all $y, z > 0$, $|g(z) - g(y)| \le (\sqrt{f(z)} - \sqrt{f(y)})^2$, where $g := f - \mathrm{id}$. Proven in Step 3 from the RHS inequality at $x = f(z)$ (and the symmetric swap $x = f(y)$) plus the iterate identity (1) and the AM-GM identity $2(\mathrm{AM}-\mathrm{GM}) = (\sqrt a - \sqrt b)^2$. Importable by any approach using the iterate $f(f(y)) = 2f(y) - y$. **Proposed for `results/imo-2026-05/lemmas/fact-5-g-bound.md`.**
- **Iterate–orbit–nonnegativity preamble** (shared with `orbit-close-encounter`): $f(f(y)) = 2f(y) - y$; $g(f(y)) = g(y)$; $f^n(y) = y + n g(y)$; $f$ injective; $g \ge 0$. Proven in Steps 1–2. **Proposed for `results/imo-2026-05/lemmas/iterate-orbit.md`.**
- **Close-encounter lemma**: the number-theoretic input to (A), stated and proven (Kronecker/Weyl + Bézout). Proven in Step 4. Importable by any approach needing close encounters of two unbounded forward APs. **Proposed for `results/imo-2026-05/lemmas/close-encounter.md`.**
