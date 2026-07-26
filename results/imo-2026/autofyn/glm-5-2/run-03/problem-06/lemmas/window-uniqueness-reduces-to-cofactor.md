# Lemma: window-uniqueness-reduces-to-cofactor (structural, NEGATIVE-fence)

*Certified: round 4 (reviewer). Source: `approaches/primal-minimal-support-stabilization.md`, Lemma 2. Verified computationally on $a_1=116$ (LOCK-at-2): 154 big-prime-entry events, each with exactly one $q$-multiple in the window.*

## Statement

Suppose at step $n+1$ the greedy picks $a_{n+1}=m$ with a prime $q>M_1=\operatorname{rad}(a_1)$ dividing $m$. Then:

- (i) *(Window-uniqueness)* $m$ is the **unique** multiple of $q$ in the window $[a_n+1, a_n+M_1]$.
- (ii) *(Admissibility = cofactor-transversal)* Writing $m=kq$ ($k=m/q\in\mathbb Z_{>0}$), $m$ is admissible (i.e. $S(m)$ hits every $S\in\operatorname{MS}_n$, the current inclusion-minimal supports) iff $\operatorname{primefactors}(k)$ hits every $S\in\operatorname{MS}_n$ with $q\notin S$.
- (iii) *(Reduction)* Consequently, to prove "no prime $q>M_1$ ever enters a new minimal support" using only the window-uniqueness ingredient, one must — for every $q>M_1$ and every step at which the unique $q$-multiple $m=kq$ lies in the window — establish one of:
   (a) $\operatorname{primefactors}(k)$ fails to hit every $q$-free minimal in $\operatorname{MS}_n$ (so $m$ is inadmissible), or
   (b) some smaller admissible $m'\in(a_n, kq)$ exists in the window (so $m$ is not the smallest admissible).

   Both (a) and (b) require bounding / controlling the prime factorization of the cofactor $k=m/q$ — which is the **cofactor-bound step** certified dead for `witness-density-recurrence` (round 2) and `crt-period-lifting` (round 3).

## Proof

(i) The window $W=[a_n+1, a_n+M_1]$ has $|W|=M_1$. Consecutive $q$-multiples differ by $q>M_1=|W|$, so at most one lies in $W$. If $q\mid m=a_{n+1}\in W$, $m$ is that one. ✓

(ii) $m$ admissible $\iff S(m)=\{q\}\cup\operatorname{primefactors}(k)$ hits every $S\in\operatorname{MS}_n$. For $S$ with $q\in S$, automatic. For $S$ with $q\notin S$, reduces to $\operatorname{primefactors}(k)\cap S\ne\varnothing$. ✓

(iii) Per (i)+(ii), when $q>M_1$ and $q\mid m=kq$ in $W$, $m$ admissible iff $\operatorname{primefactors}(k)$ transverses the $q$-free minimals, and $m$ picked iff additionally $m$ is smallest admissible in $W$. To prove $q$ never enters a new minimal support (such $m$ never picked), must show: for every such $q$-multiple $m=kq$ in $W$, EITHER $m$ inadmissible (clause (a)) OR $m$ not smallest (clause (b)). Clause (a) requires controlling $\operatorname{primefactors}(k)$ to show it omits a prime needed to hit some $q$-free minimal. Clause (b) requires exhibiting an admissible $m'<m$ in $W$ — controlling prime factorizations of candidates in the interval. Both are versions of the cofactor-bound step (bound/control $\operatorname{primefactors}(k)$ for $k=m/q$). ∎

## Consequence (fencing)

The window-uniqueness ingredient (a genuine structural refinement of the dual MT bound) does NOT escape the cofactor wall. Any future window-local greedy-minimality argument that tries to bound new primes via "the unique $q$-multiple in the window" unpacks to bounding the cofactor's prime factorization — the certified-circular dead step. Future builders should not retry a window-uniqueness escape without a genuinely new non-cofactor ingredient.

## Scope

Unconditional (within the greedy setup). The cofactor-bound step certified dead is: "bounding which primes appear in intermediate supports IS Gap A; transient primes give unbounded covering capacity compatibly with Gap A" (`witness-density-recurrence`, round 2); "the actual greedy uses full admissibility incl. transient primes; bounding which transient primes appear IS Gap A" (`crt-period-lifting`, round 3).

## Tools

`linchpin-and-gap-bound` (gap bound $d_n\le M_1$, giving the window size). Greedy admissibility + the $q$-/$q$-free prime-factor split.
