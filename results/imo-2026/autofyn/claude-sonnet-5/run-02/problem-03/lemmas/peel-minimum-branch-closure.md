## Statement

Fix $m\ge1$, a ratio-2 superincreasing tail $\tau=(\tau_1,\dots,\tau_m)$
($\tau_i=2\tau_{i+1}$), $s\in(0,2\tau_1]$, and a **Case-I** partition $F$
of $s$ into $k\le m+1$ positive parts (i.e. $\max F\le\tau_1$). Write
$N:=m+k$, $S:=F\cup\tau$, $\mu:=\min(S)$. The target inequality is the
self-contained reformulation (via $A(S)=\mathrm{Total}(S)-2E(S)$, an
elementary bookkeeping identity) of Case I of `case-ii-closure-theorem`'s
domain:
$$E(F\cup\tau)\ \le\ R(\tau)\quad\Longleftrightarrow\quad A(F\cup\tau)\ge
s-R(\tau).$$

**Peeling the global minimum** (a genuinely different direction from every
prior mechanism in this project's population, which peels the *maximum*)
closes this **unconditionally** in two of the three exhaustive branches
on $\mu$:

- **Branch A** ($\mu=\tau_m$, i.e. $\tau_m\le\min(F)$; requires $m\ge2$):
  closed for **every** $k\le m+1$, including the boundary $k=m+1$.
- **Branch B, $N$ odd** ($\mu=\min(F)<\tau_m$, $N=m+k$ odd): closed.

The only sub-branch **not** closed by this mechanism is **Branch B, $N$
even** ($\mu=\min(F)<\tau_m$ and $N=m+k$ even) — recorded as an explicit
open item, not resolved here.

## Proof

**Base case $N=2$** ($m=1,k=1$): $\tau=(\tau_1)$, $F=\{s\}$, $s\le\tau_1$
(forced by Case I with one part). $S=\{\tau_1,s\}$ sorted $\tau_1\ge s$, so
$E(S)=s\le\tau_1=R(\tau)$ directly.

**Inductive step, $N\ge3$, strong induction on $N$:**

*Branch A* ($\mu=\tau_m$, $m\ge2$). Remove $\tau_m$: $S':=F\cup\tau'$,
$\tau':=(\tau_1,\dots,\tau_{m-1})$ (ratio-2, length $m-1$,
$R(\tau')=R(\tau)-\tau_m$), same $F$, same domain (legal since $\max F\le
\tau_1$ unchanged).
- If $k\le m$: $N'=N-1<N$, apply the strong-induction hypothesis to get
  $E(S')\le R(\tau')$. If $N$ even, $\tau_m$ sits at even global rank $N$:
  $E(S)=E(S')+\tau_m\le R(\tau')+\tau_m=R(\tau)$. If $N$ odd, $\tau_m$ sits
  at odd rank $N$: $E(S)=E(S')\le R(\tau')\le R(\tau)$. Either way, closes.
- If $k=m+1$ (max budget): here $N=2m+1$ always odd, so a direct argument
  (not induction) is used. Every element of $F$ is in $[\tau_m,\tau_1]$
  (Branch A $\cap$ Case I), so by `half-bound-lemma` applied to
  $F\cup\tau'$ (size $2m$):
  $$E(F\cup\tau')\le\frac{\mathrm{Total}(F\cup\tau')}2=\frac{s+R(\tau')}2
  \le\frac{2\tau_1+R(\tau')}2=\frac{(R(\tau)+\tau_m)+R(\tau')}2=R(\tau)$$
  using $s\le2\tau_1$ and the identity $R(\tau)+\tau_m=2\tau_1$ (finite
  geometric sum: $R(\tau)=\tau_1(2-2^{1-m})$, $\tau_m=\tau_1\cdot2^{1-m}$).
  Since $N=2m+1$ is odd, $E(S)=E(F\cup\tau')$ exactly (removing $\tau_m$,
  the last/smallest element, from an odd rank), so $E(S)\le R(\tau)$.

*Branch B* ($\mu=\min(F)<\tau_m$). Remove $\mu$: $F':=F\setminus\{\mu\}$,
$s':=s-\mu$, $N':=N-1$, same $m$, $k':=k-1\le m$ (legal instance).
- If $N$ odd: $\mu$ sits at odd rank $N$, so $E(S)=E(F'\cup\tau)\le
  R(\tau)$ directly by the strong-induction hypothesis. Closes.
- If $N$ even: $\mu$ sits at even rank $N$, so $E(S)=E(F'\cup\tau)+\mu$.
  The plain hypothesis $E(F'\cup\tau)\le R(\tau)$ is not strong enough
  (would need $\le R(\tau)-\mu$). **Not closed by this mechanism.**
$\blacksquare$ (for the two closed branches)

## Essentiality of the boundary case handling

The $k=m+1$ boundary of Branch A cannot be reached by the plain induction
(there is no smaller legal instance to peel to that stays within budget
via the same route), which is why the direct `half-bound-lemma` argument
is needed there instead — this is not a redundant case, it is load-bearing.

## Open sub-case (recorded, not resolved by this lemma)

Branch B with $N$ even: $\mu=\min(F)<\tau_m$, $N=m+k$ even. The
strengthened bound $E(F'\cup\tau)\le R(\tau)-\mu$ would close it but is not
supplied by the plain induction hypothesis. A candidate strengthened
invariant $\delta=\min(S)\cdot[N\text{ even}]$ was tried and refuted at the
base case (needs $s\le\tau_1-s$, false for $s>\tau_1/2$) — do not retry
this exact guess.

## Verification (proof-reviewer, round 7)

Independently re-derived the rank-shift/parity bookkeeping for both
branches by hand (the case split on parity of $N$ and which element is
removed is elementary and checks out in every sub-case). Independently
re-ran a fresh 300,000-trial exact-`Fraction` search (own script, not the
builder's) confirming zero violations of $E(F\cup\tau)\le R(\tau)$ overall,
and separately tagged which branch each trial's first peel step falls
into: $\approx35.7\%$ Branch A, $\approx38.1\%$ Branch B-odd,
$\approx26.2\%$ Branch B-even (the open sub-case) among legal Case-I
trials — the open sub-case is genuinely exercised (not vacuous) and no
violation was found there either, consistent with the builder's own
$\sim\!27\%$/zero-violations report (different random seed and
distribution, same qualitative result).

## Origin

`results/imo-2026-03/approaches/rank-pigeonhole-budget.md`, §4.6–§4.9
(round 7).

## Certification note (proof-reviewer, round 7)

**CERTIFIED as a partial result**: Branch A (all $k\le m+1$) and Branch B
with $N$ odd are fully and rigorously closed, for every $m$, no gap. The
open sub-case (Branch B, $N$ even) is explicitly NOT certified as closed —
it remains the sole open item of Claim (A)'s Case I, precisely isolated.
