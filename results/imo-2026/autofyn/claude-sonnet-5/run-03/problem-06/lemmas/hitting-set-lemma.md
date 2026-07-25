## Hitting-Set Lemma

**Statement.** Fix a finite set of primes $Q\supseteq R(a_1)$. The Unified
Central Claim for $Q$ ("$\mathrm{Good}_Q(a_n)$ holds for every $n\ge1$",
i.e. every two terms $a_i,a_j$ of the sequence share a prime factor lying
in $Q$) holds **iff** $Q$ is a hitting set for the family
$$\{W(i,j) := R(a_i)\cap R(a_j) : i,j\ge1,\ i\ne j\}$$
of nonempty finite prime sets, i.e. $Q\cap W(i,j)\ne\emptyset$ for every
$i\ne j$.

As a free corollary, $Q_0:=R(a_1)$ already hits every $W(1,j)$ (any
finite $Q\supseteq R(a_1)$ automatically hits pairs involving index $1$),
so the remaining difficulty of finding a hitting $Q$ is confined to pairs
$(i,j)$ with $i,j\ge2$.

**Proof.** By definition, "every two terms share a prime factor in $Q$"
means: for every $i\ne j$, $R(a_i)\cap R(a_j)\cap Q\ne\emptyset$, i.e.
$W(i,j)\cap Q\ne\emptyset$. This is exactly the statement that $Q$ hits
every set in the family $\{W(i,j)\}$ — a one-line unwinding of the
definitions, no further argument needed. For the corollary: $W(1,j)=
R(a_1)\cap R(a_j)$, and by `lemmas/pairwise-non-coprimality.md`,
$\gcd(a_1,a_j)>1$, so $W(1,j)\ne\emptyset$; since $Q\supseteq R(a_1)$ and
any prime witnessing $\gcd(a_1,a_j)>1$ lies in $R(a_1)\subseteq Q$, that
witness lies in $Q\cap W(1,j)$. $\blacksquare$

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md` (round 4, §10.1),
independently verified by the proof-reviewer (round 4): the statement is
an immediate unwinding of the definition of $\mathrm{Good}_Q$ together
with the certified `pairwise-non-coprimality.md`.

### Status
Unconditional. Reframes the still-open central existence question ("does
a finite self-sufficient $Q$ exist?") as a set-hitting problem over the
family $\{W(i,j)\}$; does not itself resolve existence.
