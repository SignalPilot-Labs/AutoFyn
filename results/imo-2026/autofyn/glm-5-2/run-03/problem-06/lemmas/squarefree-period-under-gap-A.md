# Lemma: squarefree period and prime-by-prime lift bound (conditional on Gap A)

**Statement (conditional on Gap A).** Assume **Gap A**: the governing set $G:=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}T$ (primes appearing in any minimal transversal of $\mathcal F_\infty$) is finite. Then:

(i) $\mathcal B_\infty$ is $L$-periodic with $L:=\prod_{p\in G}p$, and $L$ is **squarefree** (each $\operatorname{rad}(T)$ is squarefree; $L=\operatorname{lcm}\{\operatorname{rad}(T):T\in\operatorname{MT}(\mathcal F_\infty)\}$ is an lcm of squarefree numbers, hence squarefree).

(ii) (Fiber-count lift bound, unconditional identity.) For any ordering $G=(p_1,\dots,p_s)$ and $L_k:=\prod_{j\le k}p_j$ ($L_0=1$, $L_s=L$), the projected set $A_k:=\mathcal B_\infty\bmod L_k\subseteq\mathbb Z/L_k\mathbb Z$ satisfies $|A_0|=1$ and
$$|A_k|\ \le\ p_k\cdot|A_{k-1}|\quad(k\ge1),\qquad\text{hence}\quad T:=|A_s|\le\prod_{j=1}^{s}p_j=L.$$

**Proof of (i).** By `binfinity-divisibility-progression-structure` (unconditional), $\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m:\operatorname{rad}(T)\mid m\}$. Under Gap A this is a finite union. For each $T\in\operatorname{MT}(\mathcal F_\infty)$ we have $T\subseteq G$, so $\operatorname{rad}(T)\mid L$; membership $m\in\{n:\operatorname{rad}(T)\mid n\}$ depends only on $m\bmod L$. A finite union of $L$-periodic sets is $L$-periodic. Squarefreeness: $L=\operatorname{lcm}\{\operatorname{rad}(T):T\in\operatorname{MT}(\mathcal F_\infty)\}$; each $\operatorname{rad}(T)$ is squarefree; the lcm of squarefree numbers is squarefree. $\square$

**Proof of (ii).** The reduction map $\pi:\mathbb Z/L_k\mathbb Z\to\mathbb Z/L_{k-1}\mathbb Z$ has fibers of size exactly $L_k/L_{k-1}=p_k$. For any $A\subseteq\mathbb Z/L_k\mathbb Z$ with image $A_{k-1}=\pi(A)$, $|A|=\sum_{r\in A_{k-1}}|\pi^{-1}(r)\cap A|\le\sum_{r\in A_{k-1}}p_k=p_k\cdot|A_{k-1}|$. Telescoping from $|A_0|=1$ (the single residue mod $1$) gives $|A_s|\le\prod p_k=L$. $\square$

**Depends on.** `binfinity-divisibility-progression-structure` (unconditional) + Gap A (for the periodicity and finiteness). Sharpens `distinct-supports-stabilize`'s corollary by making the **squarefree-ness of $L$** and the **prime-by-prime lift bound $T\le L$** explicit.

**Status.** Reviewer-certified (round 3). Conditional on Gap A (same gate as `distinct-supports-stabilize`). The fiber-count identity (ii) is a trivial combinatorial fact (verified computationally for $a_1\in\{6,385,1309,847,175\}$: every lift ratio $|A_k|/|A_{k-1}|\le p_k$, with slack $1.0\times$–$11\times$; $T\le L$ in every case) — it captures **no greedy-specific structure** and does NOT close Gap A; it bounds $T$ in terms of $L$, but $L$ is the product of the (a priori unbounded) governing set $G$.

**Note on non-portability.** The `aimo-0231` nontrivial content (return time of a *polynomial iterate* grows by $\le p$ when the modulus is lifted) does NOT port: the cyclic-successor map on $A$ is structurally a single $|A|$-cycle (`cyclic-successor-bijection`), so the return time equals $|A|$ exactly, and the lift bound is the trivial fiber-count identity above. No greedy-specific mechanism is captured.
