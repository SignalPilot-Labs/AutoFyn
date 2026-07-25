## Adjacent-Link Neighborhood Insufficiency (negative)

**Statement.** The candidate $Q:=\Lambda\cup Q_0$ (the stabilized
adjacent-link prime set unioned with $a_1$'s own prime factors) is **not**
always a valid hitting set for the Unified Central Claim: for $a_1=99$,
$Q_0=\{3,11\}$ and (stabilized) $\Lambda=\{2,3\}$, so $\Lambda\cup
Q_0=\{2,3,11\}$, yet the pair $(a_3,a_5)=(105,110)$ has $\gcd(105,110)=5
\notin\{2,3,11\}$.

**Proof.** Direct computation of the greedy sequence for $a_1=99$:
$a_1=99=3^2\cdot11$, $a_2=102=2\cdot3\cdot17$, $a_3=105=3\cdot5\cdot7$,
$a_4=108=2^2\cdot3^3$, $a_5=110=2\cdot5\cdot11$. Then $R(a_3)=\{3,5,7\}$
and $R(a_5)=\{2,5,11\}$, so $R(a_3)\cap R(a_5)=\{5\}$ and
$\gcd(a_3,a_5)=5$. Since $5\notin\{2,3,11\}=\Lambda\cup Q_0$, this pair is
uncovered. $\blacksquare$

### Provenance
The underlying finding (that $\Lambda\cup Q_0$ fails for $a_1=99$ via a
pair sharing only the prime $5$) originates with the round-4
outline-reviewer's pre-build check and was independently re-confirmed by
`approaches/jacobsthal-covering-bound.md` (round 4, §7.0) via a fresh,
larger-term-count simulation. **Correction by the proof-reviewer (round
4):** the builder's approach file mislabels the witnessing pair as
$(a_2,a_4)=(105,110)$; independent re-simulation confirms the values
$105,110$ are correct but belong to indices $a_3,a_5$, not $a_2,a_4$
(which are actually $102,108$, with $\gcd(102,108)=6$, not a
counterexample). The underlying mathematical conclusion — that
$\Lambda\cup Q_0=\{2,3,11\}$ fails to hit every pair for $a_1=99$ — is
correct and reproduced independently here with the corrected indices;
only the index labels in the source approach file were wrong, not the
substance of the claim.

### Status
Unconditional, negative result. Rules out "$Q=$ some fixed-order
neighborhood of adjacent-link primes" as a universal hitting set; the
mechanism must look at least at gap $2$ for this instance (empirically,
$\Lambda^{(2)}=\{2,3,5,11\}$ does hit every tested pair for $a_1=99$, per
`approaches/jacobsthal-covering-bound.md` §7.1 — evidence only, not
proved in general).
