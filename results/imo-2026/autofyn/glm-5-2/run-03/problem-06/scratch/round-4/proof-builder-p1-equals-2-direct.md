# Round 4 proof-builder report — p1-equals-2-direct (ADVANCE)

## Summary

Advanced the smallest-open-base specialization `p1-equals-2-direct` per the outline-reviewer's APPROVE charge: attempted the minimal-criminal contradiction specialized to $|P_1|=2$. **Two new lemmas proved** (one positive, one negative-fence). The cofactor-bound wall for $|P_1|=2$ is **NOT cracked**; status remains **partial**. The minimal-criminal + Schur specialization is now a certified dead-end for $|P_1|=2$.

## What was done

1. **Imported the certified foundation** (`two-entry-lemma`, `P1-minimal-transversal-lemma`, `linchpin-and-gap-bound`, `lock-lemma`, `binfinity-divisibility-progression-structure`, endgame lemmas) — not re-derived. Preserved the round-3 Steps 1–5 verbatim.

2. **Set up the minimal-criminal specialization for $|P_1|=2$ (Step 6).** Smallest governing $r>M_1=pq$; all primes in $(M_1,r)$ MT-transient by minimality; $r$ divides infinitely many $a_n$ (via `binfinity-divisibility-progression-structure`); local walk mod $r$ with FORCED $d_n=r-(a_n\bmod r)$ at $r$-multiple steps (since $d_n\le M_1<r$); cofactor-transversal structure; linchpin gives the 2-element transversal $\{p,q\}$ always.

3. **Proved one positive structural lemma (Step 7): cofactor $P_1$-divisibility.** For $|P_1|=2$ NON-LOCK and hypothetical $r>M_1=pq$: every $r$-multiple cofactor $k=a_n/r$ is divisible by $p$ or $q$. Mechanism: $m\in\mathcal B_\infty$ $\Rightarrow$ $\operatorname{rad}(T)\mid m$ for some $T\in\operatorname{MT}(\mathcal F_\infty)$; incomparability of $T$ with $\{p,q\}\in\operatorname{MT}$ forces $T$ to contain exactly one of $\{p,q\}$ (or be $\{p,q\}$); coprimality transfers divisibility to $k$. The lemma is genuinely $|P_1|=2$-specific (uses `P1-minimal-transversal-lemma`'s incomparability). Verified computationally: PASSes for every actual governing $r\notin P_1$ across $a_1\in\{15,35,65,77,91,143,175\}$, 400 terms each; FAILs for $r\in P_1$ as expected (the hypothetical $r>M_1$ excludes $P_1$). **Weak:** forces only $k\ge\min(p,q)\ge3$, no upper bound, no contradiction.

4. **Certified the negative obstruction (Step 8): cofactor-transient obstruction.** The Schur premise "cofactor's prime set eventually fixed-finite $\subseteq G$" is STRUCTURALLY FALSE in $|P_1|=2$ — not merely unproved. In any periodic realization ($a_{n+T}=a_n+L$, $r\mid L$ governing), the cofactor sequence satisfies $k_{i+s}=k_i+L/r$ (theorem: periodicity + $r\mid L$), so $(k_i)$ is a union of $s$ arithmetic progressions with common difference $L/r>0$. By classical Schur (nonconstant integer polynomial $\Rightarrow$ infinitely many prime divisors), $\bigcup_i S(k_i)$ is INFINITE — not $\subseteq$ finite $G$. Hence MT-transient $\ne$ cofactor-transient (MT-transient primes appear in cofactors forever; infinitely many distinct ones appear). Verified: $a_1=15,r=3$ gives $k_{i+6}=k_i+10$ (theorem), 198 distinct cofactor primes $>M_1$ in 2000 terms; same AP structure confirmed across all $|P_1|=2$ cases and every governing $r$.

## Gaps / honest assessment

- **Cofactor-bound wall for $|P_1|=2$ (Step 4) remains OPEN.** The conjecture "every governing prime $r\le M_1=pq$" is confirmed computationally (8 cases, 0 failures) but no non-circular proof exists.
- **The minimal-criminal + Schur specialization is a certified dead-end for $|P_1|=2$** (Step 8 settles Crux A negatively for $|P_1|=2$: the Schur premise is structurally false). This is the round's contribution — fencing off future $|P_1|=2$-specialized Schur retries with a clean structural obstruction, not just an empirical counterexample.
- **The 2-density mechanism remains REFUTED** (round 3, not revived).
- Even an unconditional $|P_1|=2$ solve would shrink the theorem to $|P_1|\ge3$ — but I cannot deliver one.

## Lemmas proposed for certification

1. **`cofactor-P1-divisibility`** (POSITIVE, NEW). Statement: In $|P_1|=2$ NON-LOCK, for any hypothetical governing $r>M_1=pq$ (equivalently $r\notin P_1$, $\gcd(r,pq)=1$), every $r$-multiple cofactor $k=a_n/r$ is divisible by $p$ or $q$. Mechanism: MT-witness + incomparability with $\{p,q\}\in\operatorname{MT}$ + coprimality. Where proved: Step 7. Verified computationally.

2. **`cofactor-transient-obstruction-P1-equals-2`** (NEGATIVE, NEW). Statement: In $|P_1|=2$ NON-LOCK, the Schur premise "cofactor $k_i=a_{n_i}/r$ has eventually fixed-finite prime set $\subseteq G$" is structurally false. In any periodic realization, $k_{i+s}=k_i+L/r$ (union of APs), so by classical Schur $\bigcup_i S(k_i)$ is infinite — not $\subseteq$ finite $G$. Hence MT-transient $\ne$ cofactor-transient; the minimal-criminal + Schur specialization for $|P_1|=2$ is a certified dead-end. Where proved: Step 8. Fences off future $|P_1|=2$-specialized Schur/minimal-criminal retries.

## Coordination with sibling builder

The `minimal-criminal-schur-contradiction` (general) builder owns the general skeleton; I specialized to $|P_1|=2$. The negative lemma `cofactor-transient-obstruction-P1-equals-2` is the $|P_1|=2$-specialized version of the general Crux A; if the general builder proves a general "MT-transient $\ne$ cofactor-transient" negative lemma, my $|P_1|=2$ version is a corollary and can be deduplicated. I did NOT duplicate general-case work — the specialization uses the $|P_1|=2$-specific incomparability (exactly-one-of-$\{p,q\}$), which is a genuine structural difference.

verdict-request: CHANGES REQUESTED
