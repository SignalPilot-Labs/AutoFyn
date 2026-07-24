## Sigma2-Untouched Closure Theorem (MaxCeil's top-cut branch, $\sigma_2$ untouched)

**Source:** `rank-pigeonhole-budget`, round 27, §7.14.

**Statement.** Let $m\ge2$ and let $\sigma=(\sigma_1,\dots,\sigma_m)$ be any
ratio-2 superincreasing tail ($\sigma_i=2\sigma_{i+1}$). Let $S$ be any
legal refinement of $\sigma$ (any number of cuts, any distribution across
the elements) subject only to:

- (a) $\sigma_1$ receives at least one cut ($\sigma_1$ split into
  $c_1+1\ge2$ positive parts, $c_1\ge1$), and
- (b) $\sigma_2$ receives **zero** cuts (appears in $S$ untouched, as a
  single element equal to $\sigma_2$).

No restriction is placed on $\sigma_3,\dots,\sigma_m$: each may be
untouched or split into arbitrarily many parts, and $c_1$ may be
arbitrarily large. Then
$$A(S)\ \le\ \sigma_1-\sigma_m.$$

**Proof (sketch, full detail in the source file's §7.14).** Write
$y_1\ge\dots\ge y_{c_1+1}>0$ for $\sigma_1$'s fragments. As in the
already-certified Lemma 1 / GC's "at most one part exceeds $\tau_1$"
argument, at most one $y_i$ can exceed $\sigma_2$ (two would sum to
$>2\sigma_2=\sigma_1$).

- If no $y_i$ exceeds $\sigma_2$: let $\mu:=1+t$, $t$ = number of $y_i$
  tied exactly at $\sigma_2$. If $\mu$ odd, `odd-run-reduction-lemma`
  collapses the tied top block to one surviving $\sigma_2$, peel it via
  `sharp-dominant-removal-identity`, bound the rest by Fact 1
  ($A\ge0$): $A(S)\le\sigma_2\le\sigma_1-\sigma_m$ (using $\sigma_1=
  2\sigma_2\ge\sigma_2+\sigma_m$). If $\mu$ even, the whole tied top
  block cancels to $0$ exactly (top-run cancellation), and Fact 2
  ($A\le\mathrm{Total}$) on the remainder plus mass conservation
  ($\mathrm{Total}(S)=R(\sigma)$) gives $A(S)\le R(\sigma)-\mu\sigma_2\le
  R(\sigma)-2\sigma_2=\sigma_1-\sigma_m$ (using the identity
  $R(\sigma)+\sigma_m=2\sigma_1$).
- If exactly one $y_1>\sigma_2$: $y_1$ is the strict unique max of $S$
  (all else, including $\sigma_2$, is $<y_1$); peel via
  `sharp-dominant-removal-identity`. In $S\setminus\{y_1\}$, $\sigma_2$
  is now the strict unique max (the remaining $\sigma_1$-fragments sum
  to $<\sigma_2$, hence each is $<\sigma_2$); peel again. This gives
  $A(S)=y_1-\sigma_2+A(S\setminus\{y_1,\sigma_2\})$, and Fact 2 plus mass
  conservation gives $A(S\setminus\{y_1,\sigma_2\})\le R(\sigma)-y_1-
  \sigma_2$, so $A(S)\le R(\sigma)-2\sigma_2=\sigma_1-\sigma_m$.

Every case closes at $A(S)\le\sigma_1-\sigma_m$. $\blacksquare$

**Scope.** Fully general: no bound on $m$, no bound on total cut count, no
restriction on how $\sigma_3,\dots,\sigma_m$ are refined. Only requires
(a) $\ge1$ cut on $\sigma_1$ and (b) zero cuts on $\sigma_2$. Reuses only
already-certified facts: `sharp-dominant-removal-identity`,
`odd-run-reduction-lemma`, Fact 1 (`half-bound-lemma`), Fact 2
($A\le\mathrm{Total}$, both in §5.2 of `rank-pigeonhole-budget.md`), and
identity (7.10.1)/(5.4), $R(\sigma)+\sigma_m=2\sigma_1$ (an elementary
finite-geometric-sum identity for any ratio-2 tail).

**Numerically cross-checked** (not a substitute for the proof): exact
`Fraction` search, $m=2,\dots,7$, $2000$ random legal $\sigma_2$-untouched
refinements per $m$ (random cut counts and positions on $\sigma_1$ and on
each of $\sigma_3,\dots,\sigma_m$ independently); zero violations of
$A(S)\le\sigma_1-\sigma_m$ found.

**Certification status.** CERTIFIED round 27. Proof-reviewer independently
re-derived the full case split (odd/even $\mu$ in the $\sigma_2$-untouched
case; the two-peel argument in the $y_1>\sigma_2$ case) by hand, confirmed
the identity $R(\sigma)+\sigma_m=2\sigma_1$ algebraically for general $m$,
and re-verified with a fresh independent exact-`Fraction` script
(`/tmp/verify_714.py`, 20,000 random trials, $m=2,\dots,7$, arbitrary cut
counts on $\sigma_1$ and $\sigma_3,\dots,\sigma_m$): zero violations. No
gap found.

**Relationship to prior work.** Strictly generalizes $4$ of the $5$
individually hand-closed shapes in `rank-pigeonhole-budget`'s round-26
§7.13 ($m=4$ case) — shapes $(1,0,0,0),(2,0,0,0),(1,0,1,0),(1,0,0,1)$ —
to arbitrary $m$ and arbitrary cut multiplicities in one uniform argument.
Does **not** cover shapes where $\sigma_2$ itself is cut (e.g. $m=4$'s
shape $(1,1,0,0)$) — see the companion Necessity Theorem
(`rank-pigeonhole-budget.md` §7.15), which proves that residual family is,
for $m\ge5$, provably entangled with $(\star_k)$, $k\ge3$ (the project's
central open lower-bound obstruction), not closable by elementary facts
alone.
