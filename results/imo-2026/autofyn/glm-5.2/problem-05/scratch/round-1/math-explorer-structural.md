## imo-2026-05 (route: structural substitutions → functional equation / additive-Cauchy form)

### The problem, restated
Find all $f:\mathbb R_{>0}\to\mathbb R_{>0}$ with
$$\sqrt{\tfrac{x^{2}+f(y)^{2}}2}\ge\tfrac{f(x)+y}{2}\ge\sqrt{xf(y)}\quad\forall x,y>0.$$
Conjectured answer (run state): $f(x)=x+c$, $c\ge 0$. Confirmed numerically for $c\in\{0,0.5,1,3,100\}$ (sampled $x,y\in[0.01,10]$, all pass); perturbations $f(x)=x+1+0.3\sin x$ and a step-$g$ function both FAIL.

### The core structural reduction (the cleanest FE a builder can attack)
The chain is the **QM-AM-GM chain for the pair $(x,f(y))$** with the AM $\tfrac{x+f(y)}2$ *replaced* by $\tfrac{f(x)+y}2$. Write $g(t)=f(t)-t$ (candidate $g\equiv c\ge0$). Then
$$\tfrac{f(x)+y}{2}-\tfrac{x+f(y)}2=\tfrac{g(x)-g(y)}2.$$
So the hypothesis is exactly:
> For all $x,y>0$, the deviation $\tfrac{g(x)-g(y)}2$ lies in the window $[-(\mathrm{AM\!-\!GM})(x,f(y)),\,(\mathrm{QM\!-\!AM})(x,f(y))]$, where both gaps are $\ge0$ and vanish iff $x=f(y)$.

Both gaps are $O\!\big((x-f(y))^{2}\big)$ near $x=f(y)$. This is the engine: **near $x=f(y)$ the window collapses and forces $g(x)\to g(y)$.** When $g\equiv c$ the deviation is identically $0$, the middle equals the AM, and the chain is the trivial QM$\ge$AM$\ge$GM — explaining both why the family works and why it is the natural extremal.

### Substitution matrix — ranked by load-bearing yield

1. **$x=f(y)$ (tight point).** RANK 1 — the single most productive substitution. At $x=f(y)$ both bounds become $\sqrt{f(y)^{2}}=f(y)$, so the sandwich forces the middle to equal $f(y)$:
$$\tfrac{f(f(y))+y}{2}=f(y)\quad\Longrightarrow\quad \boxed{\,f(f(y))=2f(y)-y\,},\quad\text{i.e.}\quad \boxed{\,g(f(y))=g(y)\,}.$$
   - The left equality is the QM-AM equality case ($x=f(y)$); the right equality is the AM-GM equality case *for the pair $(x,f(y))$* (also $x=f(y)$). Both classical-inequality equality conditions coincide here, so the chain is tight on BOTH sides simultaneously — this is why the substitution is so strong.
   - Verified symbolically and numerically for $f(x)=x+c$.

2. **Orbit iteration + codomain positivity.** RANK 2. From $g(f(y))=g(y)$, the forward orbit $y_{n}=f^{n}(y)$ satisfies $g(y_{n})=g(y)$, hence $y_{n+1}=f(y_{n})=y_{n}+g(y_{n})=y_{n}+g(y)$, i.e. $y_{n}=y+n\,g(y)$ (arithmetic progression). If $g(y)<0$ then $y_{n}\to-\infty$, eventually leaving $\mathbb R_{>0}$, contradicting $f>0$. Therefore
$$\boxed{\,g(y)\ge0\ \forall y>0\,}\quad\text{equiv.}\quad f\ge\mathrm{id}.$$
   - This is a clean, rigorous sign kill using only the iterate identity + positivity of the codomain. No continuity needed.

3. **Local squeeze near $x=f(y)$.** RANK 3 — the constancy engine. For $x$ near $f(y)$, both window endpoints are $O((x-f(y))^{2})$, so $|g(x)-g(y)|\le C\,(x-f(y))^{2}$. In particular $g$ is continuous at every point of the form $f(y)$, with quadratic modulus. This is what forces values to agree.

4. **Swap $(x,y)\leftrightarrow(y,x)$.** RANK 4. Writing the window for $(x,y)$ and for $(y,x)$ gives two interval constraints on the same quantity $g(x)-g(y)$; their intersection is tighter than either (one supplies the AM-GM side, the other the QM-AM side, with the roles' $f$-arguments swapped). Useful for sharpening but does not independently kill — it lands on the same window reduction.

5. **$y\to0^{+}$ (boundary).** RANK 5 (weak). Without continuity the limit $\lim_{y\to0}f(y)$ is not pinned; one only gets coarse bounds like $f(x)^{2}\le 2(x^{2}+\liminf f(y)^{2})$. Does NOT cleanly force $g(0^{+})$. Do not build a primary line on this.

6. **$y=f(x)$ (AM-GM equality point for the *right* inequality).** DEAD — yields $(f(x)-x)^{2}\ge0$, automatic, no new information. (Reason: AM-GM equality for the right inequality wants $f(x)=y$; setting $y=f(x)$ makes the RHS $\sqrt{x\,f(f(x))}$, not $\sqrt{f(x)\,y}$, so AM-GM does not tighten the given inequality.) Verified: combined with constraint #1 it reduces to $(f(x)-x)^{2}\ge0$.

7. **$x=y$ (diagonal).** DEAD — degenerates to the trivial QM$\ge$AM$\ge$GM chain for $(x,f(x))$, zero information. (Already noted in per-role rules.)

### Distinct openings for the outliner (each a different attack)
- **(A) Iterate-identity + monotonicity/lattice sandwich (aimo-0234 template).** Pin $g$ on each arithmetic orbit $\{y+n g(y)\}$ via $g\circ f=g$; establish $f$ (hence $g$) is monotone; trap every point between consecutive orbit points to get $g$ = a constant + bounded error; feed back and squeeze the error to zero. Most directly generalizes the conjectured family.
- **(B) Local-squeeze bootstrap to continuity, then global constancy.** Use the quadratic-modulus squeeze at every $f(y)$ to prove $g$ continuous on $\mathrm{image}(f)$; prove $\mathrm{image}(f)$ contains a half-line $(M,\infty)$ (needs IVT ⇒ needs continuity, so bootstrap from one seed point); then $g\circ f=g$ + continuity on a half-line + the squeeze propagates constancy; finally extend across the "gap region" $(0,M]$ via the cross-pair window.
- **(C) Extremal-value / infimum argument.** Let $m=\inf g\ge0$. If $m$ is attained at $y_{*}$, the orbit $y_{*}+n m$ carries $g\equiv m$; the squeeze near each orbit point forces $g\to m$ on neighborhoods; if $m=0$ the orbit is a fixed point and squeeze gives an open $g=0$ set, then propagate by connectedness. If $m$ not attained, take $g(y_{n})\to m$ and use the squeeze at $f(y_{n})$ to propagate $g\to m$ on expanding neighborhoods. Aim to conclude $g\equiv m$, then plug back to pin $m$.
- **(D) Direct two-window intersection kill.** Show that for non-constant $g$ there must exist a pair $(x,y)$ with $g(x)\ne g(y)$ and $x$ arbitrarily close to $f(y)$ (so the window is arbitrarily small ⇒ contradiction). The hard sub-claim is *existence* of such close cross-fiber pairs; this is where a density/equidistribution or a simple connectedness argument enters.

### Candidate technique(s) — pointers, not plans
- **QM-AM-GM sandwich + equality-case forcing** (knowledge_base: "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM. Equality cases pin down the extremal configuration"; "Functional equations: test special values, check injectivity/surjectivity").
- **Substitution at the shared equality point** of two classical inequalities (here $x=f(y)$) to collapse a sandwich — the load-bearing move.
- **Orbit/iterate + arithmetic progression + monotonicity sandwich** (crux aimo-0234) to pass from "pinned on a lattice" to "pinned everywhere".
- **One-sided-bound sandwich to equality** (crux aimo-0008) to upgrade a non-sharp bound to sharp.

### Cheap-kill candidates (try before heavy analysis)
- Codomain-positivity sign kill on the orbit (already gives $g\ge0$ for free — see substitution #2).
- The tight-point $x=f(y)$ (one substitution yields the iterate identity — see #1).
- Equality-case forcing for surjectivity: if one can show $f$ is surjective onto a half-line, then *every* point of that half-line is $f(y)$ and the squeeze applies there directly. (Not yet established — listed as a gap.)
- None of parity / pigeonhole / $v_{p}$ apply (real-domain problem).

### Knowledge-base entries to use
- "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases pin down the extremal configuration." (the framing of the whole chain)
- "Functional equations: test special values, check injectivity/surjectivity." (substitution matrix + the surjectivity gap)
- "Sum of squares (SOS) / completing the square" (the window gaps are squares: $\mathrm{AM\!-\!GM}=\tfrac{(\sqrt x-\sqrt{f(y)})^{2}}2$; $\mathrm{QM\!-\!AM}=\tfrac{(x-f(y))^{2}}{2(\sqrt{2(x^{2}+f(y)^{2})}+x+f(y))}$, SOS-flavored).
- "Contradiction" / "Induction" (general methods, for the orbit-descent and the squeeze-contradiction finishes).

### Analogous past problems (cruxes)
- **aimo-0234** ($f(xy+f(x))=xf(y)+2$ over $\mathbb R_{>0}$) — BEST match. Crux: *"When one substitution makes a fixed additive shift of the argument change the function by a constant, iterate that shift to pin the function exactly on an arithmetic progression, then use the function's monotonicity to trap every other point between consecutive progression values."* Directly analogous: our $g\circ f=g$ pins $g$ on the arithmetic orbit $\{y+n g(y)\}$; the remaining task is the monotonicity/sandwich step. Companion crux: *"Sandwich a monotone unknown function between floor/ceiling step-functions generated by an additive shift relation."* (Solution $f(x)=x+1$ there, same constant-shift family flavor.)
- **aimo-0008** ($f(x)f(y)\ge f(xy)$, $f(x+y)\ge f(x)+f(y)$ over $\mathbb Q_{>0}$) — strong second. Crux: *"Convert a one-sided bound into equality by sandwiching against a known exact value at a large point, splitting that point additively and letting the superadditive inequality force each summand to be tight."* Analogous to upgrading our window (a one-sided, non-sharp bound on $g(x)-g(y)$) to equality $g(x)=g(y)$ via a squeeze at a large/iterated point.
- **aimo-0190** ($f(1+xy)-f(x+y)=f(x)f(y)$) — PARTIAL fit only. Crux: *"Collapse a functional equation into Cauchy's additive equation"* + *"Pin a Cauchy-additive function to linear by exhibiting one-sided boundedness on a ray."* The "bounded below on a ray ⟹ linear" trick (we have $g\ge0$ on a ray) is a candidate FINISH **only for the $c=0$ sub-case**: a constant $g\equiv c$ is additive iff $c=0$, so the additive-Cauchy target recovers only $f(x)=x$ and silently misses $f(x)=x+c$, $c>0$. Use with care — see dead ends.

### Prior progress
None (round 1; workspace `results/imo-2026-05/` empty).

### Dead ends (do not retry)
- **"Right inequality $\Rightarrow f(x)/x$ is constant."** FALSE. The valid family $f(x)=x+c$ ($c>0$) has $f(x)/x=1+c/x$, not constant; the implication would rule out legal solutions. The right inequality $(f(x)+y)^{2}\ge4xf(y)$ is strictly weaker than AM-GM's $(f(x)+y)^{2}\ge4f(x)y$ and does not force $f(x)y\ge xf(y)$. Do not reduce to "$f(x)/x$ constant".
- **"Show $g$ is additive (Cauchy)."** Wrong target. $g\equiv c$ is constant, not additive (unless $c=0$). Pursuing additive-Cauchy structure recovers only the $c=0$ solution and is silent on $c>0$. The correct target is **"$g$ is constant"** (a fixed-shift, not additive, identity).
- **$x=y$ and $y=f(x)$ substitutions** — both degenerate to tautologies; zero information (see substitution matrix #6, #7).
- **Large-$x$ asymptotics alone.** If $g(x)\sim kx$ for large $x$, the left inequality gives $(1+k)^{2}\le2$, i.e. $k\le\sqrt2-1$; the right inequality is then automatic for large $x$. So the asymptotic route only bounds the leading coefficient, does NOT force $k=0$. Must be combined with the local squeeze / orbit structure — insufficient on its own.

### The gap a builder would close
**Pass from {local squeeze at every $f(y)$ + $g\circ f=g$ + $g\ge0$} to "$g$ is constant on all of $\mathbb R_{>0}$."** The obstruction is the **gap region** — points of $(0,M]$ where $M=\inf\mathrm{image}(f)$ (for $f(x)=x+c$ this is $M=c$, the interval $(0,c]$ is not hit by $f$). On $\mathrm{image}(f)=(M,\infty)$ the squeeze + iterate identity propagate constancy fairly directly; the points below $M$ are constrained only through cross-pairs $(x,y)$ with $y$ small and are the genuine difficulty. The cleanest finish (opening B or C) establishes enough regularity — continuity or monotonicity of $f$ (presently unproven) or attainment of $\inf g$ — to drag constancy across the gap. The aimo-0234 monotonicity-lattice-sandwich template is the most directly transferable tool.

### Small-case / intuition notes (conjecture, not proof)
- $f(x)=x+c$ works for all $c\ge0$ (numerically verified; the chain becomes the trivial QM-AM-GM chain for $(x,y+c)$). CONJECTURE: this is the full family.
- Non-constant $g$ fails: a step $g$ (value $0.7$ below $c=2$, value $2$ above) violates the chain at $y\approx1.96$, $x\approx2.65$ — exactly where $f(y)=y+0.7$ lands in the "$g=2$" region so the small window there cannot absorb the $1.3$ deviation. This is the mechanism the squeeze exploits. CONJECTURE (not proved): the squeeze + orbit invariance + $g\ge0$ suffice to force $g$ constant.
- $f(x)=kx$ works ONLY for $k=1$ (left inequality forces $k^{2}=1$); consistent with the family ($c=0$).
