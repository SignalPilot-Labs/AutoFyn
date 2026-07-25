## Nec-Necessity Lemma

**Definition.** For the actual sequence $(a_n)_{n\ge1}$ (no candidate $Q$
chosen), a prime $p$ is **necessary** if there exist indices $i<j$ with
$R(a_i)\cap R(a_j)=\{p\}$ (i.e. $p$ is the unique common prime factor of
$a_i,a_j$; equivalently $\gcd(a_i,a_j)$ is a power of $p$). Let
$$\mathrm{Nec} := \{p\text{ prime} : p\text{ is necessary}\}.$$

**Statement.** If there exists a finite set of primes $Q$ such that
$\mathrm{Good}_Q$ holds for every $n\ge1$ (the Unified Central Claim:
every pair $a_i,a_j$ shares a prime factor lying in $Q$), then
$\mathrm{Nec}\subseteq Q$; in particular $\mathrm{Nec}$ is finite whenever
any finite self-sufficient $Q$ exists.

**Proof.** Let $p\in\mathrm{Nec}$, witnessed by $i<j$ with $R(a_i)\cap
R(a_j)=\{p\}$. By hypothesis, $a_i,a_j$ share a prime $q\in Q$, i.e.
$q\in R(a_i)\cap R(a_j)$. Since $R(a_i)\cap R(a_j)=\{p\}$ has exactly one
element, $q=p$, so $p\in Q$. As $p\in\mathrm{Nec}$ was arbitrary,
$\mathrm{Nec}\subseteq Q$; since $Q$ is finite, so is $\mathrm{Nec}$.
$\blacksquare$

**Monotonicity of self-sufficiency under enlargement.** If $Q'\subseteq
Q''$ are finite prime sets and every pair $a_i,a_j$ shares a prime of
$Q'$, then every pair shares a prime of $Q''$ too (immediate: if
$p\in Q'\cap R(a_i)\cap R(a_j)$ then $p\in Q''$ too, since $Q'\subseteq
Q''$).

**Corollary.** If any finite self-sufficient $Q$ exists at all, then
$Q_{\min}:=\mathrm{Nec}\cup R(a_1)$ is the unique smallest candidate
contained in every valid $Q$, and $Q_{\min}$ itself is a distinguished,
fully computable-in-principle candidate to test for self-sufficiency.

### Provenance
Proved in `approaches/active-set-stabilization.md` (round 4). Independently
re-verified by the proof-reviewer (round 4): the argument is a direct
two-line consequence of the definitions, non-circular (it does not assume
Hypothesis SS or periodicity, only that *some* finite self-sufficient $Q$
exists). The numerical claim that $Q_{\min}$ is self-sufficient on tested
ranges for several seeds, including an adversarial three-large-prime seed
$a_1=194287=37\cdot59\cdot89$ (giving $\mathrm{Nec}=\{2,3,17,37,59,89,
103\}$, with the recruited prime $103>89=\max R(a_1)$, refuting any
belief that recruited primes are bounded by $\max R(a_1)$), was
independently re-simulated from scratch by the proof-reviewer and matches
exactly (same $\mathrm{Nec}$ set, zero uncovered pairs).

### Status
Unconditional (the lemma itself; the numerics are evidence, not proof).
Sharpens the still-open central existence question to a concrete,
explicit, computable-in-principle candidate $Q_{\min}=\mathrm{Nec}\cup
R(a_1)$: does $Q_{\min}$ exist as a *finite* set (i.e. is $\mathrm{Nec}$
finite), and is it self-sufficient? This remains open; a "no" to either
part (e.g. an $a_1$ with provably infinite $\mathrm{Nec}$) would show no
finite self-sufficient $Q$ exists for that $a_1$ at all.
