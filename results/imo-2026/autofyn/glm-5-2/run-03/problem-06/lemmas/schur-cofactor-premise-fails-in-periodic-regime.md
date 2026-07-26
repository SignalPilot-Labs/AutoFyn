# Lemma: schur-cofactor-premise-fails-in-periodic-regime (NEGATIVE, conditional on Gap A)

*Certified: round 4 (reviewer). Source: `approaches/minimal-criminal-schur-contradiction.md`, Step 7 (A3) + MT-transient discussion. Verified computationally ($a_1=15$: AP $k_{i+6}=k_i+10$ confirmed over 200 terms; blocker involution confirmed).*

## Statement

Suppose Gap A holds for the greedy sequence, so the sequence is eventually periodic: there exist $T,L$ with $a_{n+T}=a_n+L$ for all $n\ge1$ (in fact from $n=1$ by `cyclic-successor-bijection`). Let $q$ be any governing prime (so $q\mid L$). Let $n_1<n_2<\cdots$ be the indices with $q\mid a_{n_i}$, and write the **cofactor** $k_i:=a_{n_i}/q$.

Then:

(i) *(AP structure)* $(k_i)$ is a finite union of arithmetic progressions with common difference $L/q\ge1$. Concretely, if $s$ is the number of $q$-multiples per period $T$ (a constant, since $a_n\bmod q$ is $T$-periodic via $q\mid L$), then for every $i\ge1$:
$$k_{i+s} \;=\; k_i + \frac{L}{q}.$$

(ii) *(Infinite prime divisors)* The set $\bigcup_i\operatorname{primefactors}(k_i)$ of primes dividing some cofactor is **INFINITE**. (By classical Schur's theorem on prime divisors of polynomials: each AP $\frac{L}{q}m + c_j$ is a non-constant integer polynomial in $m$, hence takes values with infinitely many prime divisors. Equivalently, by the smooth-number density argument: $P$-smooth numbers $\le X$ number $O((\log X)^{|P|})$ while the AP contributes $\Omega(X)$ values $\le X$.)

(iii) *(MT-transient $\not\Rightarrow$ cofactor-transient)* Let $G$ be the (finite) set of governing primes (= prime factors of $L$). Since $\bigcup_i\operatorname{primefactors}(k_i)$ is infinite but $G$ is finite, infinitely many **MT-transient** primes (primes not in $G$, i.e. not in any $T\in\operatorname{MT}(\mathcal F_\infty)$) divide some $k_i$. Hence an MT-transient prime can divide infinitely many cofactors — being redundant in the eventual minimal transversal does not stop a prime from dividing terms of the linearly-growing sequence.

## Consequence (fencing)

The Schur / `aimo-0727` cofactor-prime-finiteness premise — "the cofactor sequence $(k_i)$ has eventually fixed-finite prime set $\subseteq G\cup\{q\}$" — is **provably false in the periodic regime**, i.e. in the very regime the theorem establishes (theorem true $\Rightarrow$ Schur premise false). No Schur-style cofactor-prime-finiteness contradiction can close Gap A on the minimal-criminal setup (Steps 1–6 of `minimal-criminal-schur-contradiction`); future builders should not retry this sub-route. The natural rescue ("separate transient primes that die from governing primes; the active-transient set eventually empties") fails because the implication MT-transient $\Rightarrow$ cofactor-transient is empirically and structurally false.

## Proof sketch

Periodicity $a_{n+T}=a_n+L$ with $q\mid a_{n_i}$ and $q\mid L$ gives $q\mid a_{n_i+T}$, so $n_i+T=n_{i+s}$ for fixed $s$ (the periodicity is a bijection on indices, and $a_n\bmod q$ is $T$-periodic). Then $k_{i+s}=a_{n_i+T}/q=(a_{n_i}+L)/q=k_i+L/q$. The AP has common difference $L/q\ge1$ (positive since $q\mid L$). Schur's theorem (non-constant integer polynomial $\Rightarrow$ infinitely many prime divisors) applies to each residue class $j\pmod s$ giving $k_{j+ms}=(L/q)m+c_j$. ∎

## Scope

Conditional on Gap A (the periodic regime). The fencing consequence is: the Schur premise cannot be established in the contradiction setting (where Gap A is assumed false) by the natural route (MT-transient $\Rightarrow$ cofactor-transient), because that route is false in the regime the theorem establishes. Subsumes the $|P_1|=2$-specialized version `cofactor-transient-obstruction-P1-equals-2` (not separately certified).

## Tools

Classical Schur's theorem on prime divisors of polynomials (knowledge_base); smooth-number density (alternative proof). `binfinity-divisibility-progression-structure` (governing $\Leftrightarrow$ $q\mid L$). `cyclic-successor-bijection` (periodicity from $n=1$).
