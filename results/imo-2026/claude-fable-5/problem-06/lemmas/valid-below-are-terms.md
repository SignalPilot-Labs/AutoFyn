# Lemma: Valid-below-are-terms

**Status:** CERTIFIED by proof-reviewer (round 3). Statement correct, proof sorry-free, no stronger than proved.

**Setting.** $(a_n)$ the greedy sequence; $W_n = \{m > 1 : \gcd(m, a_i) > 1 \ \forall i \le n\}$ (NOTE: the unbounded constraint set — no lower bound on $m$ beyond $m > 1$; this is deliberately not the set $\{m > a_n : \dots\}$, for which the statement would be vacuous). Greedy rule: $a_{n+1} = \min(W_n \cap (a_n, \infty))$ ($\ast$). Depends on: `clique.md`.

**Statement.** For every $n \ge 1$: $W_n \cap [a_1, a_n] = \{a_1, \dots, a_n\}$.

**Proof.** Induction on $n$.

*Base $n = 1$:* $[a_1, a_1] = \{a_1\}$ and $a_1 \in W_1$ since $\gcd(a_1, a_1) = a_1 > 1$.

*Step:* assume the claim for $n$. ($\supseteq$) Each $a_k$, $k \le n+1$, lies in $[a_1, a_{n+1}]$ (increasing sequence) and in $W_{n+1}$ ($a_k > 1$; $\gcd(a_k, a_i) > 1$ for $i \le n+1$ by Clique, trivially for $i = k$). ($\subseteq$) Let $x \in W_{n+1} \cap [a_1, a_{n+1}]$; note $W_{n+1} \subseteq W_n$. Three exhaustive disjoint cases:
- $x = a_{n+1}$: done.
- $a_n < x < a_{n+1}$: then $x \in W_n \cap (a_n, \infty)$ with $x < a_{n+1}$, contradicting ($\ast$). Impossible.
- $a_1 \le x \le a_n$: then $x \in W_n \cap [a_1, a_n] = \{a_1, \dots, a_n\}$ by the induction hypothesis. $\square$

**Proved in:** `approaches/small-prime-core.md`, Lemma 4.
