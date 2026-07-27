# Lemma: mtp-monovariant-and-gap-bound

**Statement (unconditional).** Let $\mathcal M_n=\min\{P(a_i):1\le i\le n\}$ be the family of inclusion-minimal prime-supports among the first $n$ terms of the greedy sequence, $P_{\mathrm{ess},n}=\bigcup\mathcal M_n$, and define the *min-transversal-product*
$$\mathrm{mtp}(\mathcal M_n):=\min\Bigl\{\prod_{p\in T}p:\ T\subseteq P_{\mathrm{ess},n},\ T\text{ is a transversal (hitting set) of }\mathcal M_n\Bigr\}.$$
(The minimum is over a nonempty finite set: $P_{\mathrm{ess},n}$ itself is a transversal.) Then:

1. **(Monotonicity)** $\mathrm{mtp}(\mathcal M_n)\le \mathrm{mtp}(\mathcal M_{n+1})$ for every $n\ge1$.
2. **(Global gap bound)** $a_{n+1}-a_n\le \mathrm{mtp}(\mathcal M_n)$ for every $n\ge1$.

*Unconditional — uses only the pairwise-intersection lemma (`pairwise-intersection.md`) and the admissibility rule. No finiteness hypothesis on $\mathcal M$. Computationally verified on $a_1\in\{15,35,77,143,175,323,4199,5005\}$: in every case $\mathrm{mtp}$ is monotone non-decreasing and the running maximum gap equals the stabilized $\mathrm{mtp}$.*

## Proof

**Notation.** For a finite family $\mathcal F$ of nonempty finite sets write $\mathrm{Trans}(\mathcal F)=\{T:T\text{ meets every }M\in\mathcal F\}$ (transversals, i.e. hitting sets). Supersets of transversals are transversals. Recall $\mathcal M_{n+1}$ is obtained from $\mathcal M_n$ by the following **refinement** operation when $P(a_{n+1})$ is added to $\{P(a_i):i\le n\}$:

- if $P(a_{n+1})$ contains some member $M\in\mathcal M_n$ (as a subset), then $P(a_{n+1})$ is not minimal and $\mathcal M_{n+1}=\mathcal M_n$;
- otherwise $P(a_{n+1})$ is a new minimal, and every old member $M\supsetneq P(a_{n+1})$ is removed (it is no longer minimal), so
$$\mathcal M_{n+1}=\bigl(\mathcal M_n\setminus\{M\in\mathcal M_n:P(a_{n+1})\subsetneq M\}\bigr)\cup\{P(a_{n+1})\}.$$

In particular every member of $\mathcal M_{n+1}\setminus\mathcal M_n$ is a subset of the member(s) it replaces.

**Claim (refinement shrinks the transversal family).** $\mathrm{Trans}(\mathcal M_{n+1})\subseteq\mathrm{Trans}(\mathcal M_n)$.

Let $T\in\mathrm{Trans}(\mathcal M_{n+1})$. We show $T$ meets every $M\in\mathcal M_n$. Fix $M\in\mathcal M_n$. There are two cases.
- $M\in\mathcal M_{n+1}$ (it stayed minimal). Then $T\cap M\neq\emptyset$ directly from $T\in\mathrm{Trans}(\mathcal M_{n+1})$.
- $M\notin\mathcal M_{n+1}$ (it was refined away). Then $P(a_{n+1})\in\mathcal M_{n+1}$ with $P(a_{n+1})\subsetneq M$. Since $T\in\mathrm{Trans}(\mathcal M_{n+1})$, $T\cap P(a_{n+1})\neq\emptyset$; and $P(a_{n+1})\subsetneq M$ gives $T\cap P(a_{n+1})\subseteq T\cap M$, so $T\cap M\neq\emptyset$.

Thus $T\in\mathrm{Trans}(\mathcal M_n)$, proving the claim.

**(1) Monotonicity.** $\mathrm{mtp}$ is a minimum of $\prod T$ over the transversal family. By the claim $\mathrm{Trans}(\mathcal M_{n+1})\subseteq\mathrm{Trans}(\mathcal M_n)$, and the minimum of a function over a subset is at least the minimum over the superset:
$$\mathrm{mtp}(\mathcal M_{n+1})=\min_{T\in\mathrm{Trans}(\mathcal M_{n+1})}\prod_{p\in T}p\;\ge\;\min_{T\in\mathrm{Trans}(\mathcal M_n)}\prod_{p\in T}p=\mathrm{mtp}(\mathcal M_n).\qquad\Box$$

**(2) Gap bound.** Fix $n$. Let $T^*\in\mathrm{Trans}(\mathcal M_n)$ be a witness attaining $\prod_{p\in T^*}p=\mathrm{mtp}(\mathcal M_n)$, and put $L^*=\prod_{p\in T^*}p=\mathrm{mtp}(\mathcal M_n)$. Every positive multiple $m$ of $L^*$ has $T^*\subseteq P(m)$ (each $p\in T^*$ divides $m$). Since $T^*$ is a transversal of $\mathcal M_n$ and supersets of transversals are transversals, $P(m)$ is a transversal of $\mathcal M_n$, i.e. $P(m)$ hits every minimal support among $\{P(a_i):i\le n\}$. Hitting every minimal support is equivalent to hitting $\{P(a_i):i\le n\}$ itself (a set hits a family iff it hits the family's minimal members), so $\gcd(m,a_i)>1$ for every $i\le n$: $m$ is a *valid* candidate for $a_{n+1}$.

The greedy choice is $a_{n+1}=\min\{m>a_n:m\text{ valid}\}$. The smallest multiple of $L^*$ strictly above $a_n$ is
$$m_0=\Bigl\lceil\tfrac{a_n+1}{L^*}\Bigr\rceil\,L^*\;\le\;a_n+L^*,$$
and $m_0$ is valid, hence $a_{n+1}\le m_0\le a_n+L^*=\mathrm{mtp}(\mathcal M_n)$. Therefore
$$a_{n+1}-a_n\le\mathrm{mtp}(\mathcal M_n).\qquad\blacksquare$$

## Remarks (not part of the certified statement)

- **Subsumes `gap-bound-at-promotion`.** That lemma bounds the gap *only at promotion steps* and with the (history-dependent) product $\prod_{p\in O}p$ where $O=P(a_i)\cap P_{\mathrm{ess},i-1}$. The present bound holds at *every* step and is governed by the global monovariant $\mathrm{mtp}(\mathcal M_n)$, independent of $a_{i-1}$.
- **Sharpness.** Computationally the bound is tight: for $a_1\in\{15,35,77,143,175,323,4199,5005\}$ the running maximum of $a_{n+1}-a_n$ equals the stabilized value of $\mathrm{mtp}(\mathcal M_n)$ (e.g. $a_1=175$: max gap $=21=\mathrm{mtp}_{\mathrm{final}}$).
- **What this lemma does NOT prove.** It establishes monotonicity and the gap bound unconditionally. It does *not* establish that $\mathrm{mtp}(\mathcal M_n)$ is bounded above (GAP-1 of approach `bounded-gap-lcm-reduction`), nor that bounded gaps force $\mathcal M$ to be finite (GAP-3). Both remain open.

**Source.** Approach `bounded-gap-lcm-reduction` (γ), round 2. Proposed for certification.
