## Bounded-Radical Refutation (negative)

**Statement.** The candidate hitting set $Q^\star:=\{p\text{ prime}:p\le
\mathrm{rad}(a_1)\}$ does **not** always satisfy the Unified Central Claim
(the Hitting-Set property of `hitting-set-lemma.md`): there exists $a_1$
(namely $a_1=375$) and indices $i,j$ (namely $i=3,j=7$) with $R(a_i)\cap
R(a_j)\cap[2,\mathrm{rad}(a_1)]=\emptyset$.

**Proof (hand-verified, no computer-only step used as a proof step).**
Let $a_1=375=3\cdot5^3$, so $R:=\mathrm{rad}(375)=15$ and the primes
$\le15$ are $\{2,3,5,7,11,13\}$. Computing the sequence term by term from
the raw recursive definition:
- $a_2=378=2\cdot3^3\cdot7$ (candidates $376,377$ rejected: coprime to
  $375$).
- $a_3=380=2^2\cdot5\cdot19$ (candidate $379$ rejected, prime, coprime to
  $375$; $380$ shares $5$ with $375$ and $2$ with $378$).
- $a_4=384=2^7\cdot3$ ($381,382,383$ rejected: $381=3\cdot127$ fails
  against $380$, $382,383$ coprime to $375$).
- $a_5=390=2\cdot3\cdot5\cdot13$ ($385,386,387,388,389$ rejected in turn).
- $a_6=396=2^2\cdot3^2\cdot11$ ($391,\dots,395$ rejected in turn).
- $a_7=399=3\cdot7\cdot19$ ($397,398$ rejected; $399$ passes against all
  six earlier terms).

Then $R(a_3)=\{2,5,19\}$ and $R(a_7)=\{3,7,19\}$, so $R(a_3)\cap
R(a_7)=\{19\}$ (their only common prime factor is $19$, so
$\gcd(a_3,a_7)=19$). Since $19>15=R$, the primes $\le15$ dividing $a_3$
are $\{2,5\}$ and those dividing $a_7$ are $\{3,7\}$ — disjoint sets —
so $R(a_3)\cap R(a_7)\cap[2,15]=\{2,5\}\cap\{3,7\}=\emptyset$. $\blacksquare$

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md` (round 4, §11.3).
Independently re-verified by the proof-reviewer (round 4) via exact
integer simulation from scratch, confirming the sequence
$375,378,380,384,390,396,399,\dots$ and $\gcd(a_3,a_7)=19$ exactly.

### Status
Unconditional, negative result. Rules out $Q=\{p\le\mathrm{rad}(a_1)\}$ as
a universal, $a_1$-only-derived closed-form witness for the Unified
Central Claim. Does **not** refute the existence of *some* finite
self-sufficient $Q$ for $a_1=375$ (a direct computational check finds
$Q=\{2,3,5,7,19\}$ works on the tested range) — only this specific
closed-form candidate is killed. Reusable as a standing counterexample:
any future approach proposing a closed-form hitting set of the form
$\{p\le f(a_1)\}$ for simple $f$ related to $\mathrm{rad}(a_1)$ should be
checked against $a_1=375$ before further investment.
