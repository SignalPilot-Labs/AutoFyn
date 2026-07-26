# Lemma: Greedy = cyclic successor in $\mathcal B_\infty$ from $n=1$ (pure-from-start)

**Statement.** For every $n\ge1$,
$$a_{n+1}=\min\bigl(\mathcal B_\infty\cap(a_n,\infty)\bigr),$$
where $\mathcal B_\infty=\bigcap_{n\ge1}\mathcal B_n$. In particular, *if* $\mathcal B_\infty$ is $L$-periodic for some finite $L$, then the sequence is the orbit of $a_1$ under the cyclic-successor map on $A=\mathcal B_\infty\bmod L$, starting at $n=1$ — there is NO transient: any eventual periodicity is in fact periodicity from the start.

**Proof.** Since $\mathcal B_{n+1}\subseteq\mathcal B_n$ (each new term imposes one more admissibility constraint), the family $(\mathcal B_n)$ is decreasing, so $\mathcal B_\infty=\bigcap_n\mathcal B_n\subseteq\mathcal B_n$. Hence $\mathcal B_\infty\cap(a_n,\infty)\subseteq\mathcal B_n\cap(a_n,\infty)$, giving
$$\min(\mathcal B_\infty\cap(a_n,\infty))\;\ge\;\min(\mathcal B_n\cap(a_n,\infty))=a_{n+1}.$$
By the "every term lies in $\mathcal B_\infty$" lemma, $a_{n+1}\in\mathcal B_\infty$, and $a_{n+1}>a_n$ by construction. So $a_{n+1}\in\mathcal B_\infty\cap(a_n,\infty)$, whence $a_{n+1}\ge\min(\mathcal B_\infty\cap(a_n,\infty))$. Combining the two inequalities yields equality. $\square$

(Depends on: every-term-in-binfinity.)

**Status.** Reviewer-certified (round 1). Unconditional (does NOT require $\mathcal B_\infty$ to be periodic). Resolves the "pure-from-start" wall modulo the periodicity of $\mathcal B_\infty$ itself. Verified computationally for $a_1=385$: the equality $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$ holds for all 700 terms tested (zero failures). Importable by any approach that establishes $\mathcal B_\infty$ is periodic and needs to upgrade "eventual" to "from $n=1$."
