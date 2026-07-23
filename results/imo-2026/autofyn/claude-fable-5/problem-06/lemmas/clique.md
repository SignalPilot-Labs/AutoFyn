# Lemma: Clique

**Status:** CERTIFIED by proof-reviewer (round 3). Statement correct, proof sorry-free, no stronger than proved.

**Setting.** $(a_n)_{n \ge 1}$ is the greedy sequence of the problem: integers $> 1$, and for every $n \ge 1$, $a_{n+1}$ is the smallest integer $> a_n$ with $\gcd(a_{n+1}, a_i) > 1$ for all $i \le n$.

**Statement.** For all indices $m \neq n$: $\gcd(a_m, a_n) > 1$.

**Proof.** Without loss of generality $m > n$ (gcd is symmetric). By the defining rule, $a_m$ satisfies $\gcd(a_m, a_i) > 1$ for all $i \le m - 1$; in particular for $i = n$. $\square$

**Proved in:** `approaches/small-prime-core.md`, Lemma 1.
