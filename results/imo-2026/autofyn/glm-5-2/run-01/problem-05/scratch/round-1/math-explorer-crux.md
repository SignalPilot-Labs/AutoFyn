## imo-2026-05

Lens: retrieval — adapt a known crux move from the corpus / knowledge base.

### The structure that matters (verified, not proved)

Let $A=(f(x)+y)^2$, $Q=2(x^2+f(y)^2)$ (left upper bound), $G=4xf(y)$ (right lower bound). The problem says $G\le A\le Q$ for all $x,y>0$. The classical inequalities give, with $B=(x+f(y))^2$:
$$G\le B\le Q,\qquad Q-G=2(x-f(y))^2.$$
So $A$ and $B$ both lie in a window of width $2(x-f(y))^2$ that **collapses to a point exactly when $x=f(y)$**. At $x=f(y)$ we have $G=B=Q$, forcing $A=B$ (all positive), i.e.
$$f(x)+y=x+f(y)\quad\text{when }x=f(y)\;\Longrightarrow\; f(f(y))=2f(y)-y.$$
Equivalently the displacement $g(t)=f(t)-t$ satisfies $g(f(y))=g(y)$ (invariant along $f$-orbits).

For the candidate family $f(x)=x+c$ ($c\ge0$): both gaps factor as $(x-y-c)^2$ (verified symbolically), so both inequalities reduce to a single square $\ge0$ with the SAME equality point $y=x-c$. Numerical check: $f=x$, $f=x+0.5$, $f=x+2$ satisfy; $f=2x$, $f=0.5x$, $f=x^2$, $f=\sqrt{x}$ all fail (conjectured exclusion, not proved).

### Distinct openings surfaced

1. **Equality-point collapse → iterate relation → force $g$ constant.** Set $x=f(y)$; the sandwich window $[G,Q]$ collapses, forcing $f(f(y))=2f(y)-y$, i.e. $g(f(y))=g(y)$. Then exploit the full force of the original inequalities (not just the equality point) to upgrade "invariant along orbits" to "$g$ globally constant". This is the natural primary route.
2. **Square-gap / SOS identity.** Both gaps are perfect squares for the candidate; investigate whether $A-B$ or $Q-A$ vs $A-G$ admit an SOS decomposition whose non-negativity forces $A=B$ generally. A "both inequalities are the same square" identity would be a one-move kill.
3. **Symmetric swap / reflection.** Swap roles of $(x,y)$ (the middle $\frac{f(x)+y}{2}$ is asymmetric, but comparing with the version obtained by reflecting through the candidate equality $x\leftrightarrow f(y)$ may force $f(x)-x=f(y)-y$) — akin to the aimo-0190 reflection-symmetry trick.
4. **Supporting-line / concavity finish (aimo-0089 style).** If one first extracts $f(x)+y=x+f(y)$ as a functional identity, the problem degenerates to classical QM-AM/AM-GM; a concavity/Jensen regularization is a fallback if the algebraic equality-point route stalls.

### Candidate technique(s)
- **Equality-case pinching of classical inequalities (QM-AM + AM-GM).** The two bounds are the QM-AM upper and AM-GM lower bounds on the *same* pair $(x, f(y))$; the unknown $f(x)+y$ is squeezed into their common window.
- **Special-value substitution $x=f(y)$** (the equality case of both classical inequalities simultaneously) to collapse the window and extract a functional iterate relation.
- **SOS / completing-the-square** to show both gaps share a square.
- **"Test special values / injectivity-surjectivity"** for FE — check whether $f$ is injective/surjective (needed to turn orbit-invariance into global constancy).

### Cheap-kill candidates
- Substitute $x=f(y)$ (equality point) to get the iterate relation $f(f(y))=2f(y)-y$ in one move — this is the cheap structural kill.
- Substitute $y=x$: gives the trivial classical AM-GM/QM-AM, no info (rules out nothing) — do not waste a round here.
- Check injectivity of $f$ from the right inequality near equality (if $f$ injective, $g(f(y))=g(y)$ plus injectivity-related arguments may force $g$ constant).
- $v_p$-style multiplicity: not applicable (reals).

### Knowledge-base entries to use
- **Standard inequalities: AM-GM, QM-AM (equality cases pin down the extremal configuration).** — the backbone.
- **Sum of squares (SOS) / completing the square.** — to factor the two gaps and possibly show they coincide.
- **Functional equations: test special values, check injectivity/surjectivity.** — for the iterate→constancy finish.

### Analogous past problems (cruxes)

**1. `aimo-0008` (Bulgaria, FE with two inequalities).** Crux move: *"Convert a one-sided bound into equality by sandwiching against a known exact value at a large point, splitting that point additively and letting the superadditive inequality force each summand to be tight."* Also: *"Amplify a lossy additive bound by feeding a power of the argument through the same bound and taking the n-th root, so the constant error becomes negligible."*
- **Why analogous:** Both are "find all $f$" with TWO simultaneous inequalities, solution $f(x)=x$ (here $x+c$). Both use a known exact value (there $f(a)=a$; here the equality-point $x=f(y)$ where the window collapses) and superadditivity/sandwich to force each summand tight.
- **Adaptation sketch:** aimo-0008 picks a large anchor $a^n=f(a^n)$ (exact value) and writes $a^n = x+(a^n-x)$, forcing $f(x)=x$ by sandwich. Here the "exact value" is implicit: at $x=f(y)$ the window $[G,Q]$ degenerates, forcing $f(x)+y=x+f(y)$. The analogue of "split additively" is splitting the equality $x=f(y)$ across orbits.
- **Remaining gap (must prove from scratch):** the iterate relation $f(f(y))=2f(y)-y$ alone does NOT force $g\equiv c$ — need to use the inequalities for *generic* $(x,y)$, not just the equality point, to upgrade orbit-invariance to global constancy. aimo-0008's amplification-by-powers has no direct analogue over $\mathbb R$; a different bootstrapping argument is required.

**2. `aimo-0190`.** Crux: *"Pin a Cauchy-additive function to linear by exhibiting one-sided boundedness on a ray, obtained from a square identity"* and *"To prove a fixed shift identity $g(x+c)-g(x)=\text{const}$, parametrize the argument via a symmetric function so a reflection symmetry equates two evaluations."*
- **Why analogous:** the target conclusion $f(x)-x=c$ is literally a fixed-shift identity; the move "obtain boundedness/constancy from a square identity" rhymes with our gaps being perfect squares $(x-y-c)^2$.
- **Adaptation sketch:** show $g=f-\mathrm{id}$ is bounded on a ray (or constant on a sub-interval) from the square-gap non-negativity, then upgrade to globally constant via a Cauchy/Jensen-type argument.
- **Remaining gap:** we have no additivity equation for $g$; only $g(f(y))=g(y)$. Need injectivity/surjectivity of $f$ (or a second relation) to turn this into a Cauchy equation.

**3. `aimo-0089` (functional inequality → affine/quadratic via supporting line + Jensen).** Crux: *"Reinterpret a weighted-average functional inequality as a supporting-line (supergradient) bound"* and *"Rewrite a derivative-at-midpoint = secant-slope relation as a two-variable identity, then differentiate into Jensen's equation."*
- **Why analogous:** also a FE inequality with a weighted-average middle term, solved by pinning the function via convexity/concavity; the "two bounds pinch the middle to the tangent" theme matches our QM-AM/AM-GM pinching.
- **Adaptation sketch (fallback):** if the algebraic equality-point route stalls, interpret $\frac{f(x)+y}{2}$ as a secant/support value and derive a Jensen-type equation for $g$.
- **Remaining gap:** our inequality is purely algebraic (no convexity hypothesis on $f$); the supporting-line machinery is heavier than needed. **Flag: tempting but does not transfer cleanly** — our gaps are exact squares, which is the stronger, simpler structure to exploit first.

### Tempting-but-not-transferring cruxes
- `aimo-0089` supporting-line/Jensen route: overkill; the square-gap SOS structure is the real engine. Pursue only if route 1 stalls.
- `aimo-0010` / `aimo-0051` iterate-graph cruxes (integer-domain, bounded-displacement + injectivity graph machinery): the orbit-counting and residue-class apparatus is specific to $\mathbb Z$/discrete; over $\mathbb R_{>0}$ with no boundedness hypothesis it does not port. The *idea* "iterate relation + invariance along orbits" transfers; the counting proofs do not.

### Prior progress
None (round 1, population empty). Conjectured answer (matches run_state baseline): $f(x)=x+c$, $c\ge0$.

### Dead ends (do not retry)
- $y=x$ substitution: degenerates to plain AM-GM/QM-AM, gives zero information — confirmed trivial, do not build an approach on it.
- $f(x)=kx$ ($k\ne1$): numerically fails (714 violations); do not pursue proportional families.
- $f(x)=x^2$, $f(x)=\sqrt{x}$: numerically fail — exclude.

### Small-case / intuition notes (conjectures, not proofs)
- The whole inequality for $f=x+c$ collapses to the single square $(x-y-c)^2\ge0$ in BOTH halves — verified symbolically. Conjecture: this coincidence is the key; an SOS identity showing both gaps equal the same square for *any* solution is the likely one-move kill (unproved).
- At $x=f(y)$ the window $[G,Q]$ collapses, forcing $f(f(y))=2f(y)-y$ — verified algebraically; this is a theorem (derivable from the hypotheses), label it established-once-derived.
- $g(f(y))=g(y)$ admits non-constant solutions in general (e.g. periodic $g$ along orbits); the original inequalities must rule these out — this is the open crux, not yet proved.
