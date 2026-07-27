# Proof builder report — density-contradiction (round 3)

## What was built
Closed both gaps diagnosed by the round-2 reviewer in
`results/imo-2026-05/approaches/density-contradiction.md` and rewrote the
proof cleanly end-to-end. Status set to **solved**. The approach now gives a
second, independent, fully rigorous derivation of $f(x)=x+c,\ c\ge0$ via
Kronecker density + commensurate cosets + zero-set propagation, distinct in
framing from the certified orbit-monotonicity-sandwich route.

## The two gaps and how each is now closed

### Gap A — irrational-case Kronecker target off by $\alpha$
**Diagnosis (reviewer):** The cross-distance is
$D=b-a+m\beta-(n+1)\alpha$ because $f(y)=a+(n+1)\alpha$ (the image of the
orbit point $a+n\alpha$). To drive $D\to0$ one needs
$m\beta-(n+1)\alpha\to a-b$. Round 2 set $c_{0}:=a+\alpha-b$, which drives
$m\beta-(n+1)\alpha\to a+\alpha-b$, hence
$D\to(b-a)+(a+\alpha-b)=\alpha\ne0$, so the bound tends to
$\alpha^{2}/(a+b)>0$ and does not force $\beta=\alpha$.

**Fix.** Set $c_{0}:=a-b$ (Section 6, the claim paragraph). Then
$m\beta-(n+1)\alpha\to a-b$ gives $D\to(b-a)+(a-b)=0$. Kronecker/Weyl
equidistribution (knowledge_base: "Kronecker / Weyl equidistribution") works
for any target phase $c_{0}/\alpha$ on the circle, so the density landing is
unaffected; only the target label changes. The final chain becomes
$|D_{m,n}|=|m\beta-(n+1)\alpha-c_{0}|<\varepsilon$, fed into
$|\beta-\alpha|\le D_{m,n}^{2}/(a+b)<\varepsilon^{2}/(a+b)\to0$.

**sympy verification:**
```
D when m*beta-(n+1)*alpha = a-b   (c0=a-b):   0      <- correct
D when m*beta-(n+1)*alpha = a+alpha-b (wrong): alpha  <- old bug
```
The whole irrational case now forces $\alpha=\beta$. The "denominator bounded
below by $a+b>0$ so no Diophantine rate is needed" observation is preserved
unchanged and correct.

### Gap B — Stage B sign error in the $a-b\in\beta\mathbb Z$, $k\le-1$ sub-case
**Diagnosis (reviewer):** With $a-b=k\beta$, $k\le-1$ gives
$a=b-|k|\beta<b$, so $a$ is NOT in the upward forward orbit
$\{b+m\beta:m\ge0\}$; the orbit-membership kill fails there, but the
case-split routed this sub-case to the broken argument instead of the
(case-independent) propagation that follows.

**Fix.** Dropped the case split on $a-b\bmod\beta\mathbb Z$ entirely and
made the propagation argument the sole engine of Stage B (Section 8). It is
fully case-independent:

1. **Base case** (Section 8(i)): $g(a)=0\Rightarrow f(a)=a$ (image point);
   squeeze $(\S)$ with $y=a$ gives $g(x)\le(x-a)^{2}/(x+a)\to0$, so $g$ is
   continuous at $a$ with value $0$; the two-valued structure $(\bullet)$
   ($g\in\{0,\beta\}$) then forces $g\equiv0$ on a non-degenerate interval
   $I_{0}\ni a$. Pick $[u_{0},v_{0}]\subset I_{0}$, $0<u_{0}$.

2. **Rightward propagation step** (Section 8(ii)): if $g\equiv0$ on $[u,v]$
   with $0<u\le v$, then $f(v)=v$ is an image point; $(\S)$ with $y=v$,
   $x=v+\eta$ gives $g(v+\eta)\le\eta^{2}/(2v+\eta)$, strictly increasing in
   $\eta$, with unique positive root
   $\eta_{+}(v)=\frac{\beta+\sqrt{\beta^{2}+8v\beta}}{2}$ where the bound
   $=\beta$. For $0<\eta<\eta_{+}(v)$, $g(v+\eta)<\beta\Rightarrow g(v+\eta)=0$;
   the zero-interval extends rightward.

3. **Propagation reaches $+\infty$** (Section 8(iii)):
   $\eta_{+}(v)^{2}-2v\beta=\frac{\beta^{3/2}\sqrt{\beta+8v}}{2}+\frac{\beta^{2}}{2}>0$
   (direct expansion, sympy-verified), so $\eta_{+}(v)>\sqrt{2v\beta}\ge\sqrt{2u\beta}>0$
   (constant lower bound, since $v\ge u$ throughout). Each step advances by at
   least $\sqrt{2u\beta}>0$, so $v_{n}\to+\infty$; hence $g\equiv0$ on
   $[u_{0},\infty)$.

4. **Contradiction via orbit intersection** (Section 8(iv)): the forward orbit
   $B=\{b+m\beta:m\ge0\}$ is unbounded above and carries $g\equiv\beta$ by
   invariance $(\dagger)$. Pick $m$ with $b+m\beta\ge u_{0}$; then propagation
   gives $g(b+m\beta)=0$ while invariance gives $g(b+m\beta)=\beta>0$.
   Contradiction — for every $a$ with $g(a)=0$, regardless of the residue
   $a-b\bmod\beta$.

A remark explicitly records that this supersedes the broken round-2 case split
and why (the $k\le-1$ sign error is moot because no case split is made).

## Side error retracted
Round 2 rejected the Master Squeeze Lemma as "false." That rejection was an
error (the lemma is a true theorem equivalent to the chain both directions,
certified in `lemmas/master-squeeze.md`). Added a Remark in Section 4
acknowledging this and noting the proof keeps its own weaker, self-contained
squeeze $(\S)$ (sufficient for every step below); no step relies on the
sharper master form, so the retraction changes nothing load-bearing.

## Completeness / case discipline
- Irrational ratio $\alpha/\beta\notin\mathbb Q$: closed (Section 6, Kronecker).
- Rational ratio $\alpha/\beta=p/q\in\mathbb Q$:
  - R1 same $d\mathbb Z$-coset: closed (Bezout intersection, Section 7).
  - R2 distinct cosets: closed (fixed residue $\rho$, growing denominator,
    Section 7).
- Zero alongside positive $\beta>0$: closed for every residue of $a-b\bmod\beta$
  by case-independent propagation + orbit intersection (Section 8).
- No positive value at all: $g\equiv0$ (Section 9, by $g\ge0$).
- Candidate family $f(x)=x+c$, $c\ge0$: exhibited and verified by substitution
  (Section 1).
- Edge cases: $g$ constant zero handled (Section 9); the propagation's
  rightward-only reach is sufficient because the forward orbit of $b$ is
  unbounded above, so no leftward propagation is needed.

## Residual gaps
None. Every case is settled, every theorem invoked is named (AM-GM, QM-AM,
Kronecker/Weyl equidistribution, Bezout), the final answer
$\boxed{f(x)=x+c,\ c\ge0}$ is stated and verified by substitution.

## Promotable lemmas
- Squeeze (Section 4): $|g(x)-g(y)|\le(x-f(y))^{2}/(x+f(y))$ — weaker than but
  independent of `lemmas/master-squeeze.md`.
- Orbit invariance + sign (Sections 2–3).
- Two-distinct-positive-values exclusion (Sections 6–7).
- Zero-alongside-positive exclusion (Section 8) — propagation + orbit
  intersection, case-independent.

## Addendum (round-3 follow-up): R2 indexing fix

After Gaps A and B were certified closed, the reviewer re-audited the
unchanged Section 7 R2 sub-case and found a pre-existing off-by-one indexing
error. The cross-distance
$D_{m,n}=(b-a)+d(mq-(n+1)p)$ uses the orbit index $m$ (for $x=b+m\beta$) and
the image index $n+1$ (for $f(y)=a+(n+1)\alpha$); the round-2 Bézout equation
$(n+1)p-(m+1)q=k^{*}$ mixed the orbit index $m$ of $D_{m,n}$ with the image
index $m+1$ on the $B$-side, dropping a $-dq$ term so that the proof claimed
$|D_{m,n}|=\rho$ when in fact $|D_{m,n}|=|\rho\pm dq|$. **Fix:** re-indexed the
Bézout equation to use the same indices that appear in $D_{m,n}$, namely
$(n+1)p-mq=k^{*}$ (orbit index $m$, image index $n+1$, both sides consistent).
Sympy-verified: under $(n+1)p-mq=k^{*}$ with $b-a=dk^{*}-\sigma\rho$, the
cross-distance reduces exactly to $D_{m,n}=-\sigma\rho$, hence
$|D_{m,n}|=\rho$. The solvability argument (congruence $mq\equiv-k^{*}\pmod p$,
solvable via $\gcd(q,p)=1$; $m=m_{0}+tp$, $n=(k^{*}+mq)/p-1\to\infty$, $n\ge0$
for large $t$) is unchanged in structure and still yields infinitely many
admissible $(m,n)\to\infty$. The conclusion (fixed positive numerator
$\rho^{2}>0$, denominator $b+m\beta+a+(n+1)\alpha\to+\infty$, squeeze bound
$\to0$, forcing $\alpha=\beta$) is unaffected; the written algebra is now
correct. Note: the conclusion was robust even to the slip, since
$|\rho\pm dq|$ is also a fixed positive constant (with $\rho\in(0,d/2]$,
$dq>0$), but the clean identity $|D_{m,n}|=\rho$ is now what the proof states.
R1 (same-coset intersection) was already consistently image-indexed
($(n+1)p-(m+1)q$ with both $A',B'$ image-point sets) and needed no change.
Residual gaps: none.
