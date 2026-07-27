# Build report — orbit-monotonicity-sandwich (round 2)

## What I proved
Full characterization: the only solutions of IMO 2026 P5 are $f(x)=x+c$, $c\ge0$.
Status: **solved**. The proof is written in place at
`results/imo-2026-05/approaches/orbit-monotonicity-sandwich.md`.

## How the two flagged gaps were closed

The outline flagged two load-bearing gaps: (Step 3) monotonicity of $f$, and
(Step 5) crossing the gap region $(0,M]$. The build **does not use
monotonicity at all**; it replaces both gaps with a single, cleaner mechanism:

1. **Master squeeze (Section 4, re-derived from scratch).** The squared gaps
   $A=(f(x)+y)^2-4xf(y)$, $B=2(x^2+f(y)^2)-(f(x)+y)^2$ are both $\ge0$ by (H)
   and satisfy the SOS identity
   $A+B=2(x-f(y))^2$, $A-B=2(g(x)-g(y))(g(x)+g(y)+2x+2y)$
   (symbolically verified). Nonnegativity $\Rightarrow |A-B|\le A+B$, giving
   $|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^2$, i.e.
   $|g(x)-g(y)|\le(x-f(y))^2/(2x+2y)$ for all $x,y>0$.

2. **Asymptotic pinning (Section 5, replaces monotonicity).** For any $y_0$
   with $g(y_0)=\alpha>0$, the arithmetic orbit $y_n=y_0+n\alpha$ carries
   $g\equiv\alpha$; choosing the lattice point $y_{n+1}$ nearest to $x$ (within
   $\alpha/2$) and applying the squeeze with $y=y_n$ gives
   $|g(x)-\alpha|\le\alpha^2/(8(x+y_0))\to0$. Hence $g(x)\to\alpha$ as $x\to\infty$.
   Uniqueness of limits forces all positive values of $g$ to coincide at a
   single value $\beta>0$; the image of $g$ lies in $\{0,\beta\}$; and
   $g(x)\to\beta$ forces $g\equiv\beta$ on a tail ray $[X_0,\infty)$.

3. **Boundary contradiction (Section 7, closes the gap region).** If a zero
   $a$ existed (necessarily in the gap region $(0,X_0)$), the zero set $Z$ is
   open (squeeze gives $g(x)\to0$ at $a$, and $g\in\{0,\beta\}$ forces a
   neighbourhood of zeros), bounded above, nonempty. At $q=\sup Z$ (which lies
   in $(0,X_0]$, has $g(q)=\beta$, $f(q)=q+\beta$), a sequence $x_n\nearrow q$
   in $Z$ gives, via the master squeeze with $x=x_n$, $y=q$:
   $\beta(\beta+2x_n+2q)\le(x_n-q-\beta)^2$. Taking $n\to\infty$ yields
   $\beta(\beta+4q)\le\beta^2$, i.e. $q\le0$, contradicting $q>0$. So $Z=\emptyset$
   and $g\equiv\beta$.

No monotonicity, no IVT, no continuity beyond the local squeeze, no
equidistribution, no attainment of $\inf g$ is invoked. The proof is purely:
tight-point identity, codomain sign kill, SOS master squeeze, asymptotic
pinning, boundary contradiction.

## Verification of the family
Section 0: $f(x)=x+c$ makes the middle of (H) equal to $(x+f(y))/2$ (the AM of
$(x,f(y))$), reducing (H) to the classical QM$\ge$AM$\ge$GM chain — valid for
all $c\ge0$.

## Gaps remaining
None. The proof is complete by the CLAUDE.md definition (all cases covered,
every theorem named, final characterization stated and verified by
substitution).

## Spec concerns for the planner
- The proof is genuinely **independent of the monotonicity framing** that named
  this slug. The outliner's "monotonicity sandwich" was the intended route, but
  the asymptotic-pinning + boundary-contradiction mechanism is cleaner and
  actually closes both flagged gaps where monotonicity could not be proved. If
  the reviewer prefers the slug to match the mechanism, a rename is cosmetic;
  the math is sound either way. No re-outline needed.
- The proof structure overlaps slightly with the extremal-infimum route (both
  use a tail-ray constancy + kill the complementary region), but the mechanism
  here is squeeze-at-infinity via the *arithmetic orbit* (not infimum
  attainment), and the gap-region kill is a boundary contradiction (not a
  small-$y$ descent). The framings remain distinct; the field has not
  collapsed to one line.
- Two certifiable shared lemmas proposed (master squeeze; asymptotic pinning),
  stated cleanly in the Promotable lemmas section of the approach file. The
  master squeeze is load-bearing for all four approaches and should be
  certified so the others can import it.

## Promotable lemmas (for the reviewer to certify)
1. **Master squeeze** — $|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^2$ for all
   $x,y>0$, with $g=f-\mathrm{id}\ge0$. Proved in Section 4. Importable by
   density-contradiction, extremal-infimum, master-sos-identity.
2. **Asymptotic pinning** — if $g(y_0)=\alpha>0$ then $\lim_{x\to\infty}g(x)=\alpha$;
   all positive values of $g$ coincide. Proved in Section 5 (uses orbit
   invariance + master squeeze).
