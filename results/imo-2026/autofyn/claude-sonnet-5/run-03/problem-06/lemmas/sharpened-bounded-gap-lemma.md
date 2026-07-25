## Lemma (Sharpened Bounded-Gap Lemma — residue-dependent gap bound)

Let $R:=\mathrm{rad}(a_1)$ and $r_n:=a_n\bmod R\in\{0,\dots,R-1\}$. For every
$n\ge1$:
$$a_{n+1}-a_n\ \le\ R-r_n\ \ (r_n\ne0), \qquad a_{n+1}-a_n\ \le\ R\ \ (r_n=0).$$
Equivalently, writing $M_n$ for the least multiple of $R$ strictly exceeding
$a_n$: $a_{n+1}\le M_n$.

### Proof
This is the exact quantity implicit in the proof of
`lemmas/bounded-gap-via-rad-a1.md`: that proof shows $M:=R(\lfloor
a_n/R\rfloor+1)$ is always a legal candidate for $a_{n+1}$ (it shares a
prime of $R(a_1)$ with every $a_i$, $i\le n$, since every $a_i$ has a prime
factor in $R(a_1)$ — `lemmas/prime-factors-a1-cover-forever.md` — and every
prime of $R(a_1)$ divides $M$), so $a_{n+1}\le M$ by minimality. Writing
$a_n=Rq+r_n$: if $r_n>0$, $M=R(q+1)$ so $M-a_n=R-r_n$; if $r_n=0$,
$M=a_n+R$ so $M-a_n=R$. $\blacksquare$

### Strengthens
The certified `bounded-gap-via-rad-a1.md`'s flat bound $a_{n+1}-a_n\le R$ to
a residue-dependent bound, tightest when $a_n$ is just past a multiple of
$R$.

### Caveat (does not by itself resolve the central gap)
Legality of a candidate $c\in(a_n,M_n]$ depends on $\gcd(c,a_i)>1$ for
*every* $i\le n$, i.e. on the full prime factorizations of
$a_1,\dots,a_n$, not on $a_n\bmod R$ alone. Two indices with the same
residue mod $R$ can have entirely different "recently active" primes
outside $R(a_1)$ (cf. `nec-necessity.md`'s counterexamples), so $r_n$ alone
does not determine $a_{n+1}-a_n$; this lemma does not close the central
existence gap by itself.

### Provenance
Proved in `approaches/scalar-difference-pigeonhole.md`, §3, round 5.
Independently re-derived by the proof-reviewer directly from the internals
of `bounded-gap-via-rad-a1.md`; no gap found.
