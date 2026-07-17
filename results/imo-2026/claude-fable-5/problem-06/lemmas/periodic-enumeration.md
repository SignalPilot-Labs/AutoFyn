# Lemma: Periodic enumeration

**Status:** CERTIFIED by proof-reviewer (round 3). Statement correct, proof sorry-free, no stronger than proved.

**Statement.** Let $M \ge 1$ and $\emptyset \neq R \subseteq \mathbb{Z}/M\mathbb{Z}$, let $c$ be an integer with $(c \bmod M) \in R$, and let $X = \{m \ge c : (m \bmod M) \in R\}$, enumerated increasingly as $x_1 = c < x_2 < x_3 < \cdots$. Then with $T = |R|$:
$$x_{n+T} = x_n + M \quad \text{for every } n \ge 1.$$

**Proof.** Fix $n \ge 1$. The window $(x_n, x_n + M]$ consists of $M$ consecutive integers, hence contains exactly one representative of each residue class mod $M$; every integer in it exceeds $x_n \ge c$, hence is $\ge c$. Therefore $|X \cap (x_n, x_n + M]| = |R| = T$. Since $(x_k)$ enumerates $X$ increasingly, the elements of $X$ in $(x_n, x_n + M]$ are exactly $x_{n+1} < \cdots < x_{n+T}$, the largest being $x_{n+T}$. Moreover $x_n + M \equiv x_n \pmod M$ with $x_n \in X$, and $x_n + M > c$, so $x_n + M \in X$; it is the largest integer of the window, hence the largest element of $X$ in the window. Thus $x_{n+T} = x_n + M$. $\square$

**Application.** In `approaches/small-prime-core.md` this is Step 6, applied with $c = a_1$, $M = \prod_{p \le a_1} p$, $R$ the set of admissible residues (Lemma 9 there), giving $a_{n+T} = a_n + L$ with $T = |R|$, $L = M$.
