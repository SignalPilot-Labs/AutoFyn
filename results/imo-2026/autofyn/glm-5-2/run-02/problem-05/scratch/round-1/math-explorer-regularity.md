## imo-2026-05 — route: regularity / monotonicity-then-structure

**Route summary.** Uniqueness via the orbit structure of $g:=f-\mathrm{id}$, NOT via a classical monotonicity-then-Cauchy argument. The two original inequalities, rewritten in $g$-form, give a pair of asymmetric two-point constraints $(\star),(\star\star)$. These, plus the orbit-invariance $g\circ f=g$ (from $f(f(x))=2f(x)-x$) which makes every level set $L_c=\{g=c\}$ a union of forward arithmetic progressions (APs) of step $c$, force: (A) $g$ takes **at most one positive value**; (B) if a fixed point exists ($g=0$ somewhere), then $g\equiv 0$. Together $\Rightarrow$ $g$ is constant $\Rightarrow f(x)=x+c$, $c\ge 0$. This route yields a *complete* uniqueness argument; the outliner should formalize the three derived facts below.

Setup (known, from seed): $f(f(x))=2f(x)-x$ (set $x=f(y)$, both inequalities hit equality). So $g(f(x))=g(x)$; forward orbit of $x$ is $\{x+ng(x)\}_{n\ge0}$; positivity $\Rightarrow g\ge0$, i.e. $f\ge\mathrm{id}$. Full two-sided truncated orbit of a step-$c$ point is $\{a+nc:n\ge0\}$ with smallest element $a\in(0,c]$. Level set $L_c$ ($c>0$) is a union of such forward APs; each is unbounded. $L_0$ = fixed points (singleton orbits).

### Key derived asymmetric constraints (in $g$-form)
Right ineq $(f(x)+y)^2\ge4xf(y)$ becomes, with $f=x+g$:
$$4x\,g(y)\le(x-y)^2+2(x+y)g(x)+g(x)^2 \qquad(\star)$$
Swapping $x\leftrightarrow y$ (original is "for all $x,y$"):
$$4y\,g(x)\le(x-y)^2+2(x+y)g(y)+g(y)^2 \qquad(\star\star)$$
Within one level set ($g(x)=g(y)=c$) both reduce to $(x-y-c)^2\ge0$ — tautological. **All content is across distinct level sets.** For $c_a<c_b$, $x\in L_{c_a}$, $y\in L_{c_b}$, the binding one is $(\star)$: $4x\,c_b\le(x-y)^2+2(x+y)c_a+c_a^2$.

Left inequality in $g$-form is non-binding across positive level sets (verified); it only matters for the fixed-point upper bound below.

### (A) Two distinct positive values are impossible
Suppose $g$ takes $c_a<c_b$ (both $>0$), on orbits $O_a=\{a_1+nc_a\}$, $O_b=\{a_2+mc_b\}$ (forward APs, unbounded). For each large $m$, pick $n$ nearest $(a_2+mc_b-a_1)/c_a$; then $|x-y|\le c_a/2$ with $x\in O_a,y\in O_b$ and $x,y\to\infty$. Inject into $(\star)$:
$$4t\,c_b\le(c_a/2)^2+4t\,c_a+c_a^2=\tfrac54 c_a^2+4t\,c_a\;\Longrightarrow\;4t(c_b-c_a)\le\tfrac54 c_a^2.$$
So $t\le 5c_a^2/(16(c_b-c_a))$, a fixed bound — contradiction with $t\to\infty$.
The "close encounter at large $t$" holds for **any** pair of unbounded forward APs: irrational step ratio $\Rightarrow$ differences dense $\Rightarrow$ arbitrarily close; rational ratio $p/q$ (coprime, $d=\gcd$) $\Rightarrow$ APs lie in residue classes mod $d$ — same class collides (forbidden, would put $c_a,c_b$ on one point), different classes are disjoint and have nearest distance $\le d/2\le c_a/2$ achieved periodically at arbitrarily large $t$. (Numerically verified: $c_a=2,c_b=4$ disjoint $\to$ violation $\sim 8\cdot10^4$; $c_a=\sqrt3,c_b=2$ irrational $\to$ violation $\sim10^4$; colliding pair $c_a=1,c_b=1.01$ is an *invalid* config — not a counterexample.)
**Conclusion: $g$ takes at most one positive value.** So $g:\mathbb R_{>0}\to\{0,c\}$ for some $c>0$, or $g\equiv0$, or $g\equiv c$.

### (B) A fixed point forces $g\equiv0$
Suppose $x_0$ is a fixed point ($g(x_0)=0$, i.e. $f(x_0)=x_0$). Right inequality at $x=x_0$:
$$f(y)\le\frac{(x_0+y)^2}{4x_0}\;\Longrightarrow\;g(y)=f(y)-y\le\frac{(y-x_0)^2}{4x_0}\quad\forall y>0.\qquad(\dagger)$$
(Tautology at $y=x_0$; equality $f(x_0)=x_0\le x_0$.) This is a **global quadratic upper bound on $g$**; in particular $g(y)\to0$ as $y\to x_0$.

**Universal lower bound on any positive step.** Let $g$ take value $c>0$ somewhere, on orbit with smallest element $a\in(0,c]$. The forward orbit $\to\infty$, so either it straddles $x_0$ (some point $\le x_0<$ next) — then nearest orbit point is within $c/2$ of $x_0$, and $(\dagger)$ there gives $c\le(c/2)^2/(4x_0)=c^2/(16x_0)$, i.e. **$c\ge16x_0$** — or the orbit lies entirely above $x_0$ (smallest point $a>x_0$, forcing $c>x_0$); then $(\dagger)$ at $a$ gives $c\le(a-x_0)^2/(4x_0)\le(c-x_0)^2/(4x_0)$, i.e. $(c/x_0)^2-6(c/x_0)+1\ge0$, so **$c\ge(3+2\sqrt2)x_0$**. (Entirely-below is impossible: forward orbit $\to\infty$.) Note $c\le x_0$ is ruled out (would force straddle $\Rightarrow c\ge16x_0>x_0$). Universal lower bound: $c\ge(3+2\sqrt2)x_0\approx5.83\,x_0$.

**Exclude fixed point + positive step.** For $y$ with $|y-x_0|<2(\sqrt2+1)x_0$, $(\dagger)$ gives $g(y)<(3+2\sqrt2)x_0\le c$ for any positive step $c$ — so $g(y)=0$. Since $x_0-2(\sqrt2+1)x_0<0$, this makes $g\equiv0$ on $(0,\,(3+2\sqrt2)x_0)$, an interval extending both sides of $x_0$. Pick a fresh fixed point $x_1$ near the right end $(3+2\sqrt2)x_0$ and iterate: the zero-region grows by a factor $(3+2\sqrt2)$ each step $\Rightarrow$ covers all of $\mathbb R_{>0}$ in finitely-many-multiplicatively steps. Hence $g\equiv0$, i.e. $f=\mathrm{id}$ ($c=0$).

(Left inequality at $y\in(x_0,\infty)$ where $f(y)=y$, viewed as a quadratic in $y$, gives $f(x)\le\sqrt{2(x_0^2+x^2)}-x_0$ for $x\le x_0$ — a consistency bound; not needed once (A)+(B) already force $g$ constant.)

### Synthesis (the route yields full uniqueness)
- $g$ takes $\le1$ positive value (A). If it takes one, $c>0$: if any fixed point also exists, (B) forces $g\equiv0$, contradiction — so no fixed points, $g\equiv c$, $f(x)=x+c$.
- If $g$ takes no positive value, $g\equiv0$, $f=\mathrm{id}$ ($c=0$).
- Existence for every $c\ge0$: $f(x)=x+c$ makes middle $=(x+f(y))/2$, both bounds = QM-AM and AM-GM on the pair $(x,f(y))$. (Seed-verified.)

**Final answer (conjecture, now with complete uniqueness route):** $f(x)=x+c$ for any constant $c\ge0$.

### Distinct openings (for the outliner's rival approaches — different framings, not this one re-labeled)
1. **Orbit/AP + two-point $g$-constraint (this route).** Rewrite in $g$, derive $(\star),(\star\star)$, force $\le1$ positive value + no fixed-point/positive mix.
2. **Functional self-sharpening of the right inequality.** For the translation, $\sup_y(2\sqrt{xf(y)}-y)=f(x)$ (achieved at $y=f^{-1}(x)$-ish). Try to prove $f(x)=\sup_y(2\sqrt{xf(y)}-y)$ as an *equality* from the inequalities — a functional fixed point pinning $f$.
3. **Local-boundedness/regularity then Cauchy-type.** $(\dagger)$ already shows $g$ is locally bounded near any fixed point; try to extract local boundedness (hence regularity) of $f$ on intervals *without* assuming a fixed point, then bootstrap. (Riskier — no fixed point to anchor.)
4. **Ordering/comparability direct.** Try to extract monotonicity of $f$ directly from $(\star),(\star\star)$ by varying one variable (didn't yield a clean comparison in scouting — the asymmetric form gives lower/upper bounds that grow with $x$, not a direct $f(x_1)$ vs $f(x_2)$ comparison).

### Candidate technique(s)
- **Functional equations** (KB "Functional equations"): injectivity, special substitutions, iteration relations — already gives $f(f(x))=2f(x)-x$.
- **Standard inequalities** (KB "AM-GM / QM-AM"): existence side + the tautology at $x=y$, $x=f(y)$, $x=f^{-1}(y)$.
- **Invariants & monovariants / orbit analysis**: $g$ constant on orbits; AP structure.
- No crux-corpus analogue needed (the orbit/AP + asymmetric-bound mechanism is problem-specific; see below).

### Cheap-kill candidates
- Symmetric substitutions ($x=y$, $y=f(x)$, $y=f^{-1}(x)$) all tautological — confirms the content is purely asymmetric, so don't waste rounds on symmetric specializations.
- The "two APs with coprime-rational step ratio collide, hence can't coexist" is a free multiplicity-style kill on a sub-case.

### Knowledge-base entries to use
- **Functional equations** (injectivity, special values, iteration).
- **Standard inequalities** (AM-GM, QM-AM — existence + tautology identification).
- **Invariants & monovariants** (orbit/AP structure of $g$).
- **Direct proof + Contradiction** (the two contradictions: two-positive-values, fixed-point-mix).

### Analogous past problems (cruxes)
Query field: `domain=algebra, subtopic=functional-equations` and `inequalities-SOS-and-convexity`. The mechanism here (orbit invariance from a second-order iteration relation + asymmetric two-point inequality forcing the displacement constant) is problem-specific; a corpus match is unlikely to be load-bearing. **None found that genuinely resembles the crux** — do not force a match. (Outliner may still scan `functional-equations` algebra cruxes for "iteration relation $f(f(x))=\ldots$" flavor, but the AP-proximity + quadratic-bound argument is bespoke.)

### Prior progress
Round 1, no approaches filed. Seed established: conjecture $f(x)=x+c$ ($c\ge0$), existence via AM-GM/QM-AM, iteration $f(f(x))=2f(x)-x$, $g\ge0$, orbits are APs, $g\circ f=g$. This route fills the uniqueness gap.

### Dead ends (do not retry)
- **Symmetric specializations** ($x=y$, $x=f(y)$, $y=f^{-1}(x)$): all reduce to $(f(x)-x)^2\ge0$ tautologies. No information.
- **Direct monotonicity of $f$ from the raw inequalities** by varying one variable: the asymmetric form yields lower bounds growing like $\sqrt x$ and upper bounds growing like $x$ — no direct $f(x_1)$-vs-$f(x_2)$ comparison. Skip this framing (opening 4 is a trap).
- **Periodic perturbations of constant $g$ ignoring orbit-invariance** (e.g. $g=1+0.1\sin x$): violate strongly (numerically $\sim5$) but aren't valid orbit-invariant $g$ — not a legitimate counterexample family; only test *orbit-invariant* nonconstant $g$.

### Open gaps / risks
1. **Rigor of "close encounter at large $t$ for disjoint rational-ratio APs":** the periodic-distance argument needs the two forward APs to achieve their cyclically-minimal separation at unbounded $t$. Standard (Frobenius/Bezout) but the outliner must state it cleanly: for coprime $p,q$ with $c_a=pd,c_b=qd$, distinct residues mod $d$ give a finite cyclic distance $\delta\in(0,d/2]$ repeated every $\text{lcm}$-period $\to\infty$.
2. **Entirely-above lower bound $c\ge(3+2\sqrt2)x_0$:** re-derive carefully; the straddle case's $c\ge16x_0$ is clean, the entirely-above case's algebra $(c/x_0)^2-6(c/x_0)+1\ge0$ must be checked (takes larger root $3+2\sqrt2$ since $c>x_0$).
3. **Fixed-point interval iteration to all of $\mathbb R_{>0}$:** growth factor $(3+2\sqrt2)>1$ per step, so $\bigcup_n(0,(3+2\sqrt2)^n x_0)=\mathbb R_{>0}$. State as a multiplicative-iteration cover.
4. The route does **not** need to separately prove continuity/measurability — the orbit/AP + quadratic-bound argument is purely algebraic and handles wild (non-measurable) $g$ too. This is a strength: no auto-continuity theorem required.

### Small-case / intuition notes (conjecture, numerically corroborated)
- Constant $g=c$ ($c=1,2$): both $(\star),(\star\star)$ tight (max lhs-rhs $\approx -2.5\text{e}-4$, numerical zero). Consistent with $f=x+c$ being a solution.
- Nonconstant orbit-invariant $g$ (e.g. $g=\sqrt2$ on $\{\pi+n\sqrt2:n\ge0\}$, $g=2$ elsewhere — a valid orbit-invariant partition): violates $(\star\star)$ at close pairs with large $y$, violation magnitude $\sim 8.7$ at $y\approx4.56$. Confirms nonconstant $g$ fails — **labeled conjecture until formalized**.
- Two-AP test (disjoint, $c_a=2,c_b=4$): violation $\sim8\text{e}4$. (Irrational $c_a=\sqrt3,c_b=2$: $\sim10^4$.)
- Equality cases of $(\star)$ within a level set: $(x-y-c)^2=0$, i.e. $y=x-c$ — the orbit step itself. Consistent with the translation being the unique tight configuration.

### Promising next moves (for outliner)
1. Formalize (A): state $(\star),(\star\star)$; lemma "two unbounded forward APs of distinct steps meet within $\min(c_a,c_b)/2$ at arbitrarily large $t$"; contradiction via $(\star)$.
2. Formalize (B): $(\dagger)$; lemma "any positive step $c$ satisfies $c\ge(3+2\sqrt2)x_0$ when $x_0$ is a fixed point" (case split straddle/entirely-above); exclude fixed-point+positive-step via interval-cover iteration.
3. Combine $\Rightarrow g$ constant $\Rightarrow f(x)=x+c$, $c\ge0$; verify existence by AM-GM/QM-AM substitution.
4. This is a single end-to-end approach (one slug), not a split — the three facts chain linearly; the outliner may keep one rival (opening 2: self-sharpening sup) as a genuinely different framing.
