# Round 3 proof-reviewer — IMO 2026 Problem 5 (density-contradiction)

## Verdict: CHANGES REQUESTED (Status: partial — one small gap remains)

The rewrite closed BOTH diagnosed gaps (A and B) correctly. But in
re-reading Section 7 (the rational-ratio R2 sub-case, unchanged from
round 2 and never re-audited for indexing), I found a **new** (pre-existing,
not round-3-introduced) off-by-one algebra error in the cross-distance
computation. The conclusion of R2 is still valid (the bound still tends to
0), but the written algebra step is wrong, so the proof is not rigorous as
written. One-line fix.

---

## Gap A (irrational Kronecker target) — CLOSED, verified

The cross-distance is $D=b-a+m\beta-(n+1)\alpha$ (since $f(y)=a+(n+1)\alpha$,
the image of the orbit point $a+n\alpha$). For $D\to0$ one needs
$m\beta-(n+1)\alpha\to a-b$, so the Kronecker target must be $c_{0}=a-b$.

sympy check: with $c_{0}=a-b$, substituting $m\beta-(n+1)\alpha=c_{0}$ gives
$D=0$; with the old wrong $c_{0}=a+\alpha-b$, $D=\alpha\ne0$. Confirmed.

The Kronecker/Weyl equidistribution application is sound: $\{\{m\gamma\}\}$
($\gamma=\beta/\alpha\notin\mathbb Q$) is dense in $[0,1)$ for $m\ge0$
(forward orbit of an irrational rotation is dense — standard). The target
phase $c_{0}/\alpha$ is unrestricted. The non-negativity constraint
$m,n\ge0$ (equivalently $N=n+1\ge1$) is met because equidistribution gives
arbitrarily large $m$, and for large $m$, $m\gamma-c_{0}/\alpha$ is large
positive, so $N=\lceil m\gamma-c_{0}/\alpha\rceil\ge1$. The denominator
$\ge a+b>0$ defuses any rate concern. Gap A is genuinely closed.

## Gap B (Stage B sign error) — CLOSED, verified

The case split on $a-b\bmod\beta\mathbb Z$ is dropped; Stage B now runs a
single case-independent engine:

- **Base (8i):** $g(a)=0\Rightarrow f(a)=a$ (image point); squeeze
  $|g(x)|\le(x-a)^2/(x+a)\to0$ gives continuity at $a$ with value $0$; the
  two-valued structure $(\bullet)$ ($g\in\{0,\beta\}$) forces $g\equiv0$ on
  a non-degenerate interval around $a$. Valid.
- **Propagation (8ii):** if $g\equiv0$ on $[u,v]$, $f(v)=v$ (image point);
  squeeze with $y=v$, $x=v+\eta$ gives $g(v+\eta)\le\eta^{2}/(2v+\eta)$,
  strictly increasing in $\eta>0$ (derivative
  $\eta(4v+\eta)/(2v+\eta)^2>0$ — verified), unique positive root
  $\eta_{+}(v)=(\beta+\sqrt{\beta^{2}+8v\beta})/2$ (verified:
  $\eta_{+}^{2}-\beta\eta_{+}-2v\beta=0$). For $0<\eta<\eta_{+}(v)$,
  $g(v+\eta)<\beta\Rightarrow g(v+\eta)=0$; zero-interval extends rightward.
  Valid.
- **Reaches $+\infty$ (8iii):** $\eta_{+}(v)^{2}-2v\beta=\beta\,\eta_{+}(v)>0$
  (sympy-verified — even cleaner than the builder's
  $\frac{\beta^{3/2}\sqrt{\beta+8v}}2+\frac{\beta^{2}}2$, which equals the
  same thing). So $\eta_{+}(v)>\sqrt{2v\beta}\ge\sqrt{2u\beta}>0$ (constant
  lower bound, since $v\ge u$ throughout as the interval only grows
  rightward). Each step advances by $\ge\sqrt{2u\beta}$, so
  $v_{n}\to+\infty$. $g\equiv0$ on $[u_{0},\infty)$.
- **Contradiction (8iv):** $B=\{b+m\beta:m\ge0\}$ unbounded above, $g\equiv\beta$
  on $B$. Pick $m$ with $b+m\beta\ge u_{0}$; then $g=0$ (propagation) and
  $g=\beta$ (invariance), contradiction. Case-independent — works for every
  residue of $a-b\bmod\beta$. Gap B is genuinely closed.

## NEW gap (pre-existing, Section 7 R2): off-by-one in cross-distance

This is in the rational-ratio R2 sub-case, which was unchanged from round 2
(only Sections 6 and 8 were rewritten). The round-2 reviewer approved R2, but
the approval missed an indexing slip.

**The error.** The squeeze $(\star\star)$ is set up (Section 6) with
$x=b+m\beta$ (orbit point, index $m\ge0$) and $f(y)=a+(n+1)\alpha$ (image of
orbit point $a+n\alpha$). So the cross-distance is
$$D=b-a+m\beta-(n+1)\alpha=(b-a)+d\bigl(mq-(n+1)p\bigr).$$
R2 solves the Bezout equation $(n+1)p-(m+1)q=k^{*}$ (note: index $m+1$ on
the $q$-side). Substituting gives
$(n+1)p=k^{*}+(m+1)q=k^{*}+mq+q$, so
$mq-(n+1)p=-(k^{*}+q)$, and
$$D=-(a-b)-d\,k^{*}-d\,q=\mp\rho-d\,q\ne\mp\rho.$$
The proof writes $D=-(a-b)-d\,k^{*}=\mp\rho$, **dropping the $-d\,q$ term**.
sympy + numerical confirmation: with $a=0.3,b=0,\alpha=2,\beta=3$ ($p=2,q=3$,
$\rho=0.3,k^{*}=0$), the parametrization gives $D=-3.3$ (fixed), NOT
$\pm0.3=\pm\rho$. The proof's claim $|D|=\rho$ is wrong.

**The conclusion of R2 is still valid.** $D$ is a FIXED constant
($=\mp\rho-d\,q$, independent of $m,n$ since $q,d,\rho$ are all fixed), and
the denominator $b+m\beta+a+(n+1)\alpha\to+\infty$, so
$|\beta-\alpha|\le D^{2}/\text{denom}\to0$ regardless of whether $D^{2}$ is
$\rho^{2}$ or $(\rho+dq)^{2}$. The numerical check confirms: the bound
$D^{2}/\text{denom}\to0$ along the subsequence. So the R2 contradiction is
correctly reached; only the written intermediate value is wrong.

**Fix (one line, two options):**
- Re-index to $x=b+(m+1)\beta$ (an image point of $B$, still an orbit point
  with index $m+1\ge1\ge0$, so $g(x)=\beta$). Then
  $D=(b-a)+d((m+1)q-(n+1)p)=-(a-b)-dk^{*}=\mp\rho$ exactly, matching the
  equation $(n+1)p-(m+1)q=k^{*}$. OR
- Change the equation to $(n+1)p-mq=k^{*}$ (keeping $x=b+m\beta$). Then
  $mq-(n+1)p=-k^{*}$ and $D=-(a-b)-dk^{*}=\mp\rho$ exactly.

Either fix makes the written algebra consistent. The bound $\to0$ and the
contradiction are unaffected.

## Master squeeze retraction — done

Section 4 Remark explicitly retracts the round-2 erroneous rejection,
acknowledges `lemmas/master-squeeze.md` as a certified equivalent, and notes
the proof keeps its own weaker self-contained squeeze $(\S)$ with no step
relying on the sharper master form. Verified: no step below Section 4
invokes the master squeeze. Clean.

## Edge cases

- $g$ takes no positive value: $g\equiv0$ by $g\ge0$ (Section 9). $f(x)=x$.
  ✓
- $g$ takes a positive $\beta$ and a zero: Stage B contradiction (Section 8,
  case-independent). ✓
- $g$ nonconstant with only positive values: Stage A forbids two distinct
  positive values, so at most one $\beta$; Stage B forbids zero; hence
  $g\equiv\beta$. ✓
- $g$ has no zero: the desired conclusion (no contradiction needed). ✓
- Candidate family $f(x)=x+c$, $c\ge0$: exhibited and verified by
  substitution (Section 1; $s\equiv0$, chain $=$ classical QM$\ge$AM$\ge$GM
  for $(x,y+c)$). ✓

The final characterization $\boxed{f(x)=x+c,\ c\ge0}$ is correct.

## Score

| axis | score |
|---|---|
| Correctness | 8/10 — one wrong algebra step in R2 (off-by-one); conclusion valid |
| Completeness / rigor | 8/10 — R2 written computation not rigorous as stated |
| Progress | 10/10 — both diagnosed gaps genuinely closed; one new (pre-existing) minor gap found |

## True Status: partial

The proof is ~95% complete and correct. Both round-2 gaps (A, B) are
genuinely closed. The master-squeeze retraction is clean. All edge cases are
covered. The ONLY remaining issue is the R2 cross-distance indexing slip
(off-by-one between orbit-point index $m$ and image-point index $m+1$),
which makes the written algebra step wrong but leaves the conclusion valid.
A one-line re-index fixes it. Not `solved` as written (one wrong step), but
very close — CHANGES REQUESTED.

## Required fix for APPROVE next round

In Section 7, Sub-case R2, make the orbit/image indexing consistent: either
(a) use $x=b+(m+1)\beta$ in the cross-distance (matching the equation
$(n+1)p-(m+1)q=k^{*}$), or (b) change the Bezout equation to
$(n+1)p-mq=k^{*}$ (matching $x=b+m\beta$). Then $|D|=\rho$ exactly and the
bound $|\beta-\alpha|\le\rho^{2}/\text{denom}\to0$ is rigorous. No other
change needed.
