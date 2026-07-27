# Proof builder report — density-contradiction (round 2)

## What was built
A complete, rigorous characterization proof for IMO 2026 P5, written to
`results/imo-2026-05/approaches/density-contradiction.md`. Status: **solved**.

The solution is $f(x)=x+c$, $c\ge0$.

## Structure of the proof
1. **Candidate family admissible** (Section 1): for $g\equiv c$ the deviation
   $s=g(x)-g(y)\equiv0$, so $(\star)$ reduces to the classical QM-AM-GM chain
   for $(x,f(y))=(x,y+c)$.
2. **Orbit invariance $g(f(y))=g(y)$** (Section 2): $x=f(y)$ collapses the
   window (QM=AM=GM), forcing $f(f(y))=2f(y)-y$.
3. **Sign $g\ge0$** (Section 3): forward orbit $y_n=y+n\,g(y)$ stays positive;
   $g(y)<0\Rightarrow y_n\to-\infty$, contradiction.
4. **Squeeze lemma** (Section 4, the certifiable engine):
   $|g(x)-g(y)|\le(x-f(y))^{2}/(x+f(y))$.
   Derived from scratch: $2(\mathrm{QM}-\mathrm{AM})\le(a-b)^{2}/(a+b)$
   (rationalization) and $2(\mathrm{AM}-\mathrm{GM})\le(a-b)^{2}/(a+b)$
   (difference of two squares), with $a=x,b=f(y)$; then
   $|s|\le\max(2U,2L)\le$ bound. **NOTE: the outliner's "master squeeze"
   $|s|(g(x)+g(y)+2x+2y)\le(x-f(y))^{2}$ is too strong and is NOT implied by
   the two classical inequalities** (exhibited a counterexample: $a=1,b=3$,
   $s\to2U=1$ would require $|s|\le4/(8+s)\approx0.44$, false). I replaced it
   with the correct, weaker-but-sufficient bound $|s|\le(x-f(y))^{2}/(x+f(y))$,
   which is exactly what the two classical gaps give. The reviewer should
   flag this correction to the other approaches that import the outliner's
   version (master-sos-identity, orbit-monotonicity-sandwich,
   extremal-infimum) — they should import **my** squeeze lemma, not the
   outliner's.
5. **Stage A — two distinct positive values excluded** (Sections 6–7):
   - **Irrational ratio** (Section 6, Kronecker/Weyl): the cross-orbit
     denominator $b+m\beta+a+(n+1)\alpha\ge a+b>0$ is bounded *below* (constant),
     so Kronecker density (which gives the landing distance $\to0$) directly
     forces $|\beta-\alpha|\to0$. **No Diophantine-approximation rate needed**
     — the reviewer's "rate argument" worry is moot: the denominator does not
     grow in the irrational case (it is bounded below). The squeeze RHS
     $\le\varepsilon^{2}/(a+b)\to0$.
   - **Rational ratio** (Section 7): $\alpha=pd,\beta=qd$, $\gcd(p,q)=1$.
     *R1* (same $d\mathbb Z$-coset): image-point sets intersect (Bezout on
     $p,q$), giving a common point carrying both $\alpha$ and $\beta$.
     *R2* (distinct cosets): coset residue $\rho=\min_{k}|a-b+dk|\in(0,d/2]$,
     attained at $k^{*}$; infinitely many $(m,n)\to\infty$ with cross-distance
     $=\pm\rho$ (solve $(n+1)p-(m+1)q=k^{*}$, $m\equiv r_{0}\bmod p$,
     $n\to\infty$); denominator $\to\infty$, RHS $\to\rho^{2}/\infty\to0<$ LHS.
6. **Stage B — zero alongside positive excluded** (Section 8):
   - If $a-b\in\beta\mathbb Z$: the orbit $B$ hits $a$ (or $a\in B$), forcing
     $g(a)=\beta$, contradiction.
   - If $a-b\notin\beta\mathbb Z$: the two-valued structure $g\in\{0,\beta\}$
     (from Stage A) + squeeze propagation. Base: continuity at $a$ (Section 4
     corollary) + two-valued $\Rightarrow g=0$ on a neighborhood of $a$
     (a value-$\beta$ sequence would violate $g\to0$). Propagation: $g=0$ on
     $[u,v]\Rightarrow$ squeeze with $y=x-\eta\in[u,v]$ gives
     $g(x)\le\eta^{2}/(2u)<\beta\Rightarrow g(x)=0$; extend past $v$ and below
     $u$; iterate to all of $\mathbb R_{>0}$, contradicting $\beta>0$.
7. **Conclusion** (Section 9): $g\equiv c\ge0$; substitution verified.

## Gaps remaining
**None.** Every case is settled:
- Irrational ratio: rigorous (Kronecker, denominator bounded below).
- Rational ratio R1 (intersect): rigorous (Bezout).
- Rational ratio R2 (grow-kill): rigorous (residue attained at $k^{*}$,
  infinitely many large $(m,n)$ with denominator $\to\infty$).
- One value zero + one positive, $a-b\in\beta\mathbb Z$: rigorous.
- One value zero + one positive, $a-b\notin\beta\mathbb Z$: rigorous
  (two-valued structure + continuity-at-image-point + squeeze propagation).
- One-sided Kronecker ($m,n\ge0$): confirmed — equidistribution visits every
  subinterval infinitely often, so large $m$ with $m\gamma\ge c_{0}/\alpha$
  exists.
- Final characterization verified by substitution.

## Spec concerns / corrections for the field
1. **The outliner's master squeeze is wrong (too strong).** The identity
   "$U+L=(x-f(y))^{2}/2$, $U-L=-(g(x)-g(y))(\cdots)/2$" is dimensionally and
   numerically inconsistent (I verified: for $a=1,b=3$ it would force
   $|s|\le0.44$ where the true maximum is $|s|=1$). The correct consequence of
   the two classical gaps is
   $|g(x)-g(y)|\le(x-f(y))^{2}/(x+f(y))$ (denominator $x+f(y)=x+y+g(y)\ge x$),
   which I derived and used. **The other three approaches should import MY
   squeeze lemma**, not the outliner's. This is a load-bearing correction:
   any approach relying on the outliner's stronger (false) bound is unsound.
2. **The "rate argument" the reviewer flagged is a non-issue.** In the
   irrational case the denominator is bounded *below* by the constant
   $a+b>0$ (not growing), so Kronecker density (arbitrary landing closeness)
   suffices; no Dirichlet/continued-fraction rate is needed. The reviewer's
   numerical check (RHS $\sim10^{-11}$ vs $|\beta-\alpha|\sim0.59$) is
   consistent with this. I prove the contradiction directly from density + the
   lower bound on the denominator, not from any rate.
3. **The rational case is closed**, not a gap. The reviewer flagged it as
   "load-bearing open"; the grow-kill (R2) + the coset-intersect (R1) settle it
   fully, and the zero-alongside-positive case is handled by the two-valued
   structure + propagation (which crucially relies on Stage A having reduced
   $g$ to $\{0,\beta\}$).
4. **No monotonicity or global continuity is used**, only (i) continuity at
   image points (Section 4 corollary, used in Stage B base case) and (ii)
   Kronecker density. The approach is genuinely distinct from
   orbit-monotonicity-sandwich.

## Promotable / certifiable lemmas (for the reviewer)
- **Squeeze lemma** (Section 4): $|g(x)-g(y)|\le(x-f(y))^{2}/(x+f(y))$.
  Fully proven from the two classical gaps. **Recommend certifying into
  `results/imo-2026-05/lemmas/squeeze.md` and having the other approaches
  import THIS version, discarding the outliner's.**
- **Orbit invariance + sign** (Sections 2–3): $g(f(y))=g(y)$, $g\ge0$.
  Fully proven; certifiable.
- **Two-distinct-positive-values exclusion** (Sections 6–7): under $(\star)$,
  $g$ takes at most one positive value. Fully proven (Kronecker + commensurate
  cosets). Certifiable; importable by extremal-infimum and others.
