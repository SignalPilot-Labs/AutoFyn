## Lemma (Positive-Density Upgrade of the scalar-difference pigeonhole)

Fix $T\ge1$, let $R:=\mathrm{rad}(a_1)$, $g_n(T):=a_{n+T}-a_n\in[T,TR]$
(telescoping the certified `bounded-gap-via-rad-a1.md`), and
$m:=TR-T+1$ (the number of possible values of $g_n(T)$). There is a value
$L(T)\in[T,TR]$ such that, writing $Y_T:=\{n\ge1:g_n(T)=L(T)\}$,
$$\limsup_{N\to\infty}\frac{|Y_T\cap[1,N]|}{N}\ \ge\ \frac1m\ >\ 0.$$

### Proof
For $v\in[T,TR]$, $N\ge1$, let $c_v(N):=|\{n\in[1,N]:g_n(T)=v\}|$. Every
$n\in[1,N]$ contributes to exactly one $c_v(N)$ (Lemma 1), so
$\sum_{v=T}^{TR}c_v(N)=N$ for all $N$.

Suppose for contradiction that $s_v:=\limsup_N c_v(N)/N<1/m$ for every $v$.
Let $\varepsilon:=\min_v(1/m-s_v)/2>0$ (minimum of finitely many positive
numbers). By definition of limsup, for each $v$ there is $N_v$ with
$c_v(N)/N<s_v+\varepsilon\le1/m-\varepsilon$ for all $N\ge N_v$. Let
$N_0:=\max_v N_v$. Then for $N\ge N_0$,
$\sum_v c_v(N)/N < m(1/m-\varepsilon)=1-m\varepsilon<1$, contradicting
$\sum_v c_v(N)/N=1$. Hence some $v=L(T)$ has $\limsup_N c_v(N)/N\ge1/m$.
$\blacksquare$

### Remark
This $L(T)$ also witnesses the plain pigeonhole conclusion ($Y_T$ infinite):
$c_v(N)$ is non-decreasing in $N$, so $\limsup_N c_v(N)=\lim_N c_v(N)$; if
finite, $c_v(N)/N\to0$, contradicting the positive limsup, so
$c_{L(T)}(N)\to\infty$.

### What this does and does not give
Guarantees $Y_T$ recurs with frequency $\ge1/m$ along arbitrarily long
prefixes, infinitely often (positive **upper** density) — strictly stronger
than mere infiniteness. Does **not** give positive lower density or
syndeticity (bounded gaps); upgrading to those requires additional
structure not established here.

### Provenance
Proved in `approaches/scalar-difference-pigeonhole.md`, §2, round 5.
Independently re-derived by the proof-reviewer (standard finite-alphabet
limsup/subadditivity argument); no gap found. Self-contained — depends only
on Lemma 1's finite-alphabet bound, reusable by any problem needing a
"some value recurs with positive density" pigeonhole upgrade.
