# Lemma: Single-residual indicator (Lemma 19)

**Source:** `approaches/greedy-halving-adversary.md`, round 9.

**Statement.** Let $F=\{v\}\cup P$ where $P$ is a finite multiset of
positive reals in which every distinct value has even multiplicity (i.e.
$P$ decomposes into exactly-equal pairs, possibly of different values
across different pairs), and $v>0$ is a further single element. Then for
every $x\ge0$,
$$N_F(x)\equiv \mathbb1[x<v]\pmod 2,$$
hence $u_F(x):=\mathbb1[N_F(x)\text{ odd}]=\mathbb1[x<v]$ identically on
$[0,\infty)$, and $A(F)=v$.

**Proof.** For fixed $x\ge0$, $N_F(x)=\mathbb1[v>x]+N_P(x)$. Write
$N_P(x)=\sum_w \mu(w)\mathbb1[w>x]$ (sum over distinct values $w$ in $P$,
$\mu(w)$ = $P$'s even multiplicity of $w$). Each term is even (even
$\mu(w)$ times a nonnegative integer indicator sum), so $N_P(x)$ is even
for every $x$. Thus $N_F(x)\equiv\mathbb1[v>x]\pmod2$ for every $x$, giving
$u_F(x)=\mathbb1[x<v]$, and by the certified `integral-alternating-sum-
formula`, $A(F)=\int_0^\infty u_F=\int_0^v 1\,dx=v$. $\blacksquare$

**Status.** Proved in full, unconditionally, general (no ladder structure
assumed). Independently re-verified by the reviewer with 2000 random exact-
`Fraction` trials comparing $A(F)$ (via direct sort-and-alternate-sum) to
$v$, zero mismatches.

**Scope.** This is a *pointwise-in-$x$* strengthening of the value-only
conclusion already available from the certified `leftover-formula`; the
pointwise form is what is needed to instantiate `cross-term-identity-
threshold` (Lemma 8) in the derivation of `single-residual-exact-peel-
identity` below.

**Certified by:** proof-reviewer, round 9.
