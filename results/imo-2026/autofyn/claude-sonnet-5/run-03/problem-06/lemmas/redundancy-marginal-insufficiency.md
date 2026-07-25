## Lemma (Redundancy-Marginal-Insufficiency — negative result)

For a finite $Q\supseteq R(a_1)$ and $n\ge1$, write
$\rho_Q(n):=|R(a_n)\cap Q|$ (the number of $Q$-primes dividing $a_n$).
Knowing $\rho_Q(i)\ge2$ and $\rho_Q(j)\ge2$ for a pair $i<j$ does **not**
imply $|R(a_i)\cap R(a_j)|\ge2$ — the implication is FALSE in general, not
merely unproven.

### Proof (decisive counterexample, $a_1=35$)

Direct computation from the recursive definition (independently re-verified
by exact-integer simulation):
$$a_1=35=5\cdot7,\quad a_2=40=2^3\cdot5,\quad a_3=42=2\cdot3\cdot7,\quad
a_4=45=3^2\cdot5,$$
so $R(a_1)=\{5,7\}$, $R(a_2)=\{2,5\}$, $R(a_3)=\{2,3,7\}$, $R(a_4)=\{3,5\}$.

Direct intersection checks give $R(a_1)\cap R(a_3)=\{7\}$,
$R(a_1)\cap R(a_2)=\{5\}$, $R(a_2)\cap R(a_3)=\{2\}$, $R(a_3)\cap
R(a_4)=\{3\}$ — each a singleton, so (by `lemmas/nec-necessity.md`'s
definition) $Q_0:=\{2,3,5,7\}\subseteq\mathrm{Nec}\subseteq Q_{\min}$.

Now $\rho_{Q_0}(1)=|\{5,7\}\cap Q_0|=2$ and $\rho_{Q_0}(2)=|\{2,5\}\cap
Q_0|=2$, so also $\rho_{Q_{\min}}(1)\ge2$ and $\rho_{Q_{\min}}(2)\ge2$ (since
$Q_0\subseteq Q_{\min}$). Yet $R(a_1)\cap R(a_2)=\{5\}$, a singleton — size
$1$, not $\ge2$. $\blacksquare$

### Structural reason (why no repair of this mechanism can work)

$\rho_Q(n)$ is a **marginal** (single-index) statistic; the property needed
("every pair shares $\ge2$ $Q$-primes") is a **joint** (pair-of-indices)
statistic. For sets $A,B$ in a common universe, $|A|\ge2$ and $|B|\ge2$ place
no lower bound whatsoever on $|A\cap B|$ (e.g. $A=\{5,7\}$, $B=\{2,5\}$ above
have $|A\cap B|=1$ despite $|A|=|B|=2$; disjoint 2-element sets give
$|A\cap B|=0$). No aggregation of per-index counts can control a pairwise
intersection size in general — any working replacement must track
information about *pairs* of indices directly (e.g. the Hitting-Set Lemma's
framing).

### Provenance
Proved in `approaches/active-set-stabilization.md`, round 5, refuting the
round-5 outline's proposed "Redundancy Growth Lemma." Independently
re-verified by the proof-reviewer via exact-integer simulation (`sympy`),
confirming $a_1,\dots,a_4=(35,40,42,45)$ and all four stated intersections
exactly.

### Caveat
This rules out per-term redundancy counts as a route to bounding
$\mathrm{Nec}$ or proving $Q_{\min}$-self-sufficiency. It does not touch any
approach using pair-indexed statistics (e.g. `hitting-set-lemma.md`).
