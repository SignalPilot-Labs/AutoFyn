## Lemma (Exact periodicity of a listed union of residue classes)

Let $L \ge 1$ be an integer, $\emptyset \neq \mathrm{GoodRes} \subseteq
\mathbb Z/L\mathbb Z$, and $c \ge 0$ an integer. Let
$$C := \{m \in \mathbb Z_{>c} : m \bmod L \in \mathrm{GoodRes}\},$$
listed in increasing order as $c_1 < c_2 < c_3 < \cdots$ (an infinite set),
and let $T := |\mathrm{GoodRes}|$. Then
$$c_{j+T} = c_j + L \quad \text{for every } j \ge 1$$
— exact periodicity from the very first listed element, with no separate
"two states coincide" pigeonhole step.

### Proof
Define $\varphi: C \to \mathbb Z$, $\varphi(x) = x+L$. If $x \in C$ then
$x > c \Rightarrow x+L > c$, and $(x+L) \bmod L = x \bmod L \in
\mathrm{GoodRes}$, so $\varphi(x) \in C$; in fact $\varphi(x) \in C' :=
C \cap (c+L, \infty)$ since $x+L > c+L$. $\varphi$ is a strictly increasing
injection (a translation).

$\varphi: C \to C'$ is surjective: given $y \in C'$, $y - L > c$, and
$(y-L) \bmod L = y \bmod L \in \mathrm{GoodRes}$, so $y - L \in C$ and
$\varphi(y-L) = y$. Hence $\varphi$ is an order-preserving bijection
$C \to C'$.

The interval $(c, c+L]$ contains exactly one representative of each residue
class mod $L$, of which exactly $T = |\mathrm{GoodRes}|$ lie in $C$; every
element of $C$ lies either in $(c,c+L]$ or in $C'$, so $C \setminus C' =
C \cap (c,c+L]$ has exactly $T$ elements, i.e. $C' = \{c_{T+1}, c_{T+2},
\dots\}$.

By induction on $j \ge 1$: $\varphi(c_j) = c_{j+T}$. Base case $j=1$:
$\varphi(c_1) = \min \varphi(C) = \min C' = c_{T+1}$ (order-preserving
bijection sends least element to least element). Inductive step: assuming
$\varphi(c_j) = c_{j+T}$, since $c_{j+1}$ is the least element of $C$
exceeding $c_j$ and $\varphi$ is a strictly increasing bijection onto $C'$,
$\varphi(c_{j+1})$ is the least element of $C'$ exceeding $\varphi(c_j) =
c_{j+T}$, which (since $C' = \{c_{T+1}, c_{T+2}, \dots\}$ and $c_{j+T} \in
C'$) is exactly $c_{j+T+1} = c_{(j+1)+T}$.

Thus $c_j + L = \varphi(c_j) = c_{j+T}$ for every $j \ge 1$. $\blacksquare$

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md`, round 2, as
"Lemma P." Self-contained, purely combinatorial, no dependence on the
sequence $(a_n)$ or on any other lemma for this problem. Verified by the
proof-reviewer, round 2, both by re-checking the bijection argument and by
independent computational testing (200 randomized trials of $(L,
\mathrm{GoodRes}, c)$, all confirming $c_{j+T} = c_j + L$ for every checked
$j$).

### Use
Once a "self-sufficiency" hypothesis is granted (some finite prime set $Q$
eventually governs candidate validity exactly, mod $L = \prod_{q \in Q} q$),
this lemma gives a direct, exact-from-the-start proof that the accepted set
$A$'s tail (as a listed set) is periodic — strictly stronger and shorter
than an orbit-pigeonhole telescoping argument, though it applies only to the
*tail* $A \cap (c, \infty)$ for some cutoff $c$, not (by itself) to the
entire sequence from $n=1$; extending to all $n \ge 1$ remains a separate,
unresolved gap for this problem (see
`lemmas/eventual-periodicity-given-hypothesis-ss.md`).
