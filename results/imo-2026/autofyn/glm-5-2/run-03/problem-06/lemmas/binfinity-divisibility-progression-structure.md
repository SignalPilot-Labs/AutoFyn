# Lemma: $\mathcal B_\infty$ divisibility-progression structure (unconditional)

**Statement (unconditional).** Let $\mathcal F_\infty:=\{S(a_i):i\ge1\}$ (the family of prime supports of the greedy terms; multiplicity ignored, cf. `mt-depends-on-set-system`), let $\operatorname{MT}(\mathcal F_\infty)$ denote the family of minimal transversals (minimal hitting sets) of $\mathcal F_\infty$, and $\mathcal B_\infty:=\bigcap_{n\ge1}\mathcal B_n$ with $\mathcal B_n=\{m>0:\gcd(m,a_i)>1\ \forall i\le n\}$. Then
$$\mathcal B_\infty\ =\ \bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m\in\mathbb Z_{>0}:\operatorname{rad}(T)\mid m\}.$$
(Equivalently: $m\in\mathcal B_\infty$ iff some minimal transversal $T$ of $\mathcal F_\infty$ has $T\subseteq S(m)$, iff $\operatorname{rad}(T)\mid m$.) This identity holds **unconditionally** — the union may be infinite, but the pointwise equality is valid regardless.

**Proof.** Fix $m>0$.
- ($\Leftarrow$) If $T\in\operatorname{MT}(\mathcal F_\infty)$ and $\operatorname{rad}(T)\mid m$, then $T\subseteq S(m)$. As $T$ is a transversal of $\mathcal F_\infty$, $S(m)$ is a transversal, i.e. $S(m)\cap S(a_i)\ne\varnothing$ for every $i$, i.e. $\gcd(m,a_i)>1$ for every $i$, i.e. $m\in\mathcal B_\infty$.
- ($\Rightarrow$) Suppose $m\in\mathcal B_\infty$, i.e. $S(m)$ is a transversal of $\mathcal F_\infty$. The set $S(m)$ is **finite**. Consider the family $\{T\subseteq S(m):T\text{ is a transversal of }\mathcal F_\infty\}$; it is non-empty (it contains $S(m)$ itself). A finite non-empty family of sets has a minimal element under inclusion (start from $S(m)$, delete any element whose removal leaves a transversal, repeat; termination is guaranteed by the finiteness of $S(m)$). Call this minimal element $T_0$. By construction $T_0\in\operatorname{MT}(\mathcal F_\infty)$ and $T_0\subseteq S(m)$, i.e. $\operatorname{rad}(T_0)\mid m$. $\square$

**Depends on.** No hypothesis beyond the definitions. Isolates the representation that `distinct-supports-stabilize`'s corollary uses only conditionally (under Gap A, the union is finite and yields $L$-periodicity).

**Status.** Reviewer-certified (round 3). Unconditional. Importable by any approach that needs to reason about the structure of $\mathcal B_\infty$ before (or independently of) Gap A. (Note: the identity alone does NOT close Gap A — the union may be infinite, and periodicity requires the finiteness of $G=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}T$, which IS Gap A.)
