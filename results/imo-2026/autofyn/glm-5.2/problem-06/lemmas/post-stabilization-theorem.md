# Lemma: post-stabilization-theorem

**Hypothesis (GAP).** The family $\mathcal M=\min\{P(a_i):i\ge1\}$ of minimal prime-supports of the greedy sequence is finite.

**Statement.** Assume GAP. Set $P=\bigcup\mathcal M$, $L=\prod_{p\in P}p$ (squarefree by construction), and
$$V=\{r\in\{0,\ldots,L-1\}:\{p\in P:p\mid r\}\text{ is a transversal (hitting set) of }\mathcal M\}.$$
Then $V$ is finite nonempty ($0\in V$), and with $T=|V|$,
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge1.$$

**Proof.** Composes the following lemmas (each proved in full in this directory): `transversal-residue-characterization`, `universal-membership-no-transient`, `greedy-equals-cyclic-successor`, `cyclic-successor-single-cycle`. By `universal-membership-no-transient`, every $a_n\bmod L\in V$ (so the dynamics hold from $n=1$, no transient). By `greedy-equals-cyclic-successor`, $r_{n+1}=\varphi(r_n)$ where $\varphi$ is the cyclic successor in $V$. By `cyclic-successor-single-cycle`, $\varphi$ is one $|V|$-cycle with period-sum $L$. Hence $a_{n+T}=a_n+L$ for all $n\ge1$. ∎

*Conditional only on GAP. Verified computationally on $a_1=15$ ($T=8,L=30$), $a_1=429$ ($T=908,L=4290$), $a_1=30$ ($T=1,L=2$).*

**Source.** Approach `transversal-single-cycle-finish` (Theorem A), round 1. Reviewer-certified.
