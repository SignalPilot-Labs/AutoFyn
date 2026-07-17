# Lemma: Reduction

**Status:** CERTIFIED by proof-reviewer (round 3). Statement correct, proof sorry-free, no stronger than proved.

**Setting.** $(a_n)_{n \ge 1}$ the greedy sequence; $A = \{a_n : n \ge 1\}$; $W_n = \{m > 1 : \gcd(m, a_i) > 1 \ \forall i \le n\}$; $V_\infty = \{m > 1 : \gcd(m, a_i) > 1 \ \forall i \ge 1\}$. The greedy rule restates as $a_{n+1} = \min(W_n \cap (a_n, \infty))$ ($\ast$). Depends on: `clique.md`.

**Statement.**
(i) $A \subseteq V_\infty$.
(ii) $a_{n+1} = \min(V_\infty \cap (a_n, \infty))$ for every $n \ge 1$.
(iii) $A = V_\infty \cap [a_1, \infty)$; the sequence is the increasing enumeration of $V_\infty \cap [a_1, \infty)$.

**Proof.** (i) Fix $k$. $a_k > 1$; for $i = k$, $\gcd(a_k, a_k) = a_k > 1$; for $i \neq k$, $\gcd(a_k, a_i) > 1$ by the Clique lemma. So $a_k \in V_\infty$.

(ii) $V_\infty \subseteq W_n$ (the $V_\infty$ condition quantifies over all $i \ge 1$, hence all $i \le n$), so $\min(V_\infty \cap (a_n, \infty)) \ge \min(W_n \cap (a_n, \infty)) = a_{n+1}$ by ($\ast$), the left minimum being well-defined since $a_{n+1} \in V_\infty \cap (a_n, \infty)$ by (i). The same membership gives the reverse inequality $\le a_{n+1}$. Equality follows.

(iii) ($\subseteq$) by (i) and $a_n \ge a_1$. ($\supseteq$) Let $v \in V_\infty$, $v \ge a_1$, $v \notin A$. The sequence is strictly increasing and unbounded with $a_1 \le v$, so $a_n < v < a_{n+1}$ for some $n \ge 1$; then $v \in V_\infty \cap (a_n, \infty)$ with $v < a_{n+1}$, contradicting (ii). Since the sequence lists $A$ increasingly, it is the increasing enumeration of $V_\infty \cap [a_1, \infty)$. $\square$

**Proved in:** `approaches/small-prime-core.md`, Lemma 3.
