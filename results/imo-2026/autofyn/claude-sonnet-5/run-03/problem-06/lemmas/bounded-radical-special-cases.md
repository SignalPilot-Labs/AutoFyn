## Bounded-Radical Special Cases

**Statement.** Write $R:=\mathrm{rad}(a_1)$ and $[2,R]$ for the set of
primes $\le R$. Then:
- (i) $R(a_1)\cap R(a_j)\cap[2,R]\ne\emptyset$ for every $j\ge1$;
- (ii) $R(a_n)\cap R(a_{n+1})\cap[2,R]\ne\emptyset$ for every $n\ge1$.

**Proof.** (i) $R(a_1)=Q_0\subseteq[2,R]$ since every prime dividing $a_1$
divides $R=\prod_{p\mid a_1}p$ and hence is $\le R$. By
`lemmas/prime-factors-a1-cover-forever.md`, $R(a_1)\cap R(a_j)\ne
\emptyset$ for every $j$; any witness lies in $R(a_1)\subseteq[2,R]$, so
lies in $R(a_1)\cap R(a_j)\cap[2,R]$.

(ii) By `lemmas/adjacent-link-lemma.md`, $\gcd(a_n,a_{n+1})$ is a positive
integer $\le R$; by `lemmas/pairwise-non-coprimality.md` it is $>1$, so it
has a prime factor $p$, and $p\le\gcd(a_n,a_{n+1})\le R$ (a prime factor
of an integer $x$ is itself $\le x$). Hence $p\in R(a_n)\cap R(a_{n+1})
\cap[2,R]$. $\blacksquare$

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md` (round 4, §11.1),
independently re-derived by the proof-reviewer (round 4) — both parts are
short, elementary consequences of already-certified lemmas.

### Status
Unconditional. Shows any candidate hitting set $Q\supseteq[2,R]\supseteq
Q_0$ need not separately worry about pairs involving index $1$ or
adjacent pairs — both are automatically hit. Does not extend to
non-adjacent pairs with both indices $\ge2$; see
`bounded-radical-refutation.md` for a proof that $[2,R]$ alone is
insufficient in general for such pairs.
