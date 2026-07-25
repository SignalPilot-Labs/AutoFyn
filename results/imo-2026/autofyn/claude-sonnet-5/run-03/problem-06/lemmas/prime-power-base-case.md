## Prime-Power Base Case Theorem

**Statement.** If $a_1=p^k$ for a prime $p$ and integer $k\ge1$, then
$T=1$ and $L=p$: $a_{n+1}=a_n+p$ for every $n\ge1$, so $a_n=a_1+(n-1)p$.
In particular this covers every **even** $a_1$ (take $p=2$).

**Proof.** By induction on $n\ge1$, showing $a_n\equiv0\pmod p$ and
$a_{n+1}=a_n+p$. Since $R(a_1)=\{p\}$ (the only prime factor), for any
candidate $m$, $\gcd(m,a_1)>1\iff p\mid m$. By the inductive hypothesis
every earlier term is a multiple of $p$, so any candidate $m$ divisible by
$p$ automatically satisfies $\gcd(m,a_i)\ge p>1$ against every earlier
term $a_i$ at once; and (using the constraint against $a_1$ alone, which
forces $p\mid m$ for validity) any candidate not divisible by $p$ is
invalid. Hence the smallest valid candidate exceeding $a_n$ is the next
multiple of $p$ after $a_n$, namely $a_n+p$ (since $a_n$ itself is already
a multiple of $p$). $\blacksquare$

### Provenance
Proved in `approaches/renormalization-induction-on-seed.md` (round 4,
§3). Independently re-verified by the proof-reviewer (round 4): the
induction is elementary and self-contained, matches direct simulation for
several prime-power seeds.

### Status
Unconditional, fully closes every prime-power seed instance (including
all even $a_1$) with no $Q$-machinery needed. Usable standalone or as the
base case of any future induction on $\omega(a_1)$.
