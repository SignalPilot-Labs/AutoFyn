## Windowed-$\epsilon$-automaton failure theorem — NEGATIVE result

**Statement.** Let $R:=\mathrm{rad}(a_1)$, $d_n:=a_{n+1}-a_n$,
$\ell_n:=\gcd(a_n,a_{n+1})$, $b_n$ the `legal-baseline-step.md` quantity,
and $\epsilon_n:=\mathbb1[d_n\ne b_n]$. Suppose $(d_n,\ell_n)$ is
eventually constant $=(d^*,\ell^*)$ for $n\ge n_0$, with $1\le d^*<R$.
Write $g:=\gcd(d^*,R)$. Then, for $n\ge n_0$, $\epsilon_n$ is eventually
periodic in $n$ with **exact period $R/g>1$**, and consequently
$\epsilon_{n+1}$ is **not** a function of any fixed-width window
$(\sigma_{n-w+1},\dots,\sigma_n)$ of the pair statistic
$\sigma_n=(d_n,\ell_n)$, for any window width $w$.

**Proof.** For $n\ge n_0$, $a_{n+1}\equiv a_n+d^*\pmod R$, so $a_n\bmod R$
advances by the fixed step $d^*$ each time: an orbit of exact period
$R/g$ under addition of $d^*$ in $\mathbb Z/R\mathbb Z$ (standard cyclic
group fact). Since $R/g>1$ (equivalent to $d^*\ne R$, true as $d^*<R$),
$b_n=R-(a_n\bmod R)$ (convention $0\mapsto R$) takes $R/g\ge2$ distinct
values over one period, so $\epsilon_n=\mathbb1[d^*\ne b_n]$ is not
constant on that period — it has period exactly $R/g$ in $n$ for
$n\ge n_0$. But every window $(\sigma_{n-w+1},\dots,\sigma_n)$ for
$n\ge n_0+w-1$ reads the identical key $((d^*,\ell^*),\dots,(d^*,\ell^*))$
regardless of where $n$ sits in the period, so no function of the window
alone can recover $\epsilon_{n+1}$ (it must, but cannot, distinguish the
$R/g\ge2$ possible phases). $\blacksquare$

**Realized, non-vacuous instance.** For $a_1=21$: $R=21$, and the
sequence satisfies $a_n=3(n+6)$ for every $n\ge1$ (proved directly by
induction from the definition — this is itself a complete solution of the
problem for $a_1=21$, with $T=1$, $L=3$), giving $d_n=3$, $\ell_n=3$
identically from $n=1$. Here $d^*=3$, $g=\gcd(3,21)=3$, period
$R/g=7>1$; direct computation confirms $\epsilon_n=0$ iff $7\mid n$, a
genuine period-7 pattern, verified independently by the proof-reviewer
via exact-integer simulation for $n=1,\dots,39$.

### Provenance
`approaches/bounded-link-invariant.md`, round 3, §4.2 (general theorem)
and its $a_1=21$ instance. Verified by the proof-reviewer round 3: the
modular-arithmetic argument was re-derived independently, and the
$a_1=21$ instance was independently re-simulated (Python, exact integer
arithmetic), confirming $a_n=3(n+6)$ and the period-7 pattern of
$\epsilon_n$ exactly.

### Status
Unconditional negative result. Rules out "compressed relative-gap sliding
window" as a viable finite-state mechanism for this problem: any correct
general finite-state argument must track an *additive/cumulative*
invariant (e.g. $a_n\bmod R$ or $a_n\bmod L$), not a purely relative
window of gaps — consistent with what `active-set-stabilization.md` and
`state-compactness-pigeonhole.md` already do (residue mod $L$).
