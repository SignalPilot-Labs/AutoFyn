# Lemma: cyclic-successor-single-cycle (and period-sum = L)

**Hypothesis (GAP).** $V=\{r:\{p\in P:p\mid r\}\text{ hits }\mathcal M\}\subseteq\{0,\ldots,L-1\}$ finite nonempty, $L=\prod_{p\in P}p$.

**Statement.** List $V=\{v_0<v_1<\cdots<v_{k-1}\}$ with $v_0=0$, $k=|V|$. The cyclic successor $\varphi(v_i)=v_{i+1}$ for $i<k-1$, $\varphi(v_{k-1})=v_0$, is a **single $k$-cycle** visiting every element of $V$. The sum of increments over one full period is exactly $L$:
$$\sum_{i=0}^{k-1}[(\varphi(v_i)-v_i)\bmod L]=L.$$

**Proof.** By definition $\varphi$ walks $V$ in increasing cyclic order: $v_0\to v_1\to\cdots\to v_{k-1}\to v_0$, a single cycle of length $k$. The increments telescope:
$$(v_1-v_0)+(v_2-v_1)+\cdots+(v_{k-1}-v_{k-2})+(L-v_{k-1}+v_0)=L,$$
using $v_0=0$. ∎

*Conditional on GAP. Tautological once $\varphi$ is identified as the plain cyclic successor (not a pairwise-intersection-based jump map).*

**Source.** Approaches `transversal-single-cycle-finish` (Lemmas 4–5), `density-promotion-bound` (Lemma 5), `bertrand-dickson-eviction` (Lemma 9). Reviewer-certified.
