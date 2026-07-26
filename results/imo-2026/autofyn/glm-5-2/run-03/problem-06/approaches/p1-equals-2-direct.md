# Approach: p1-equals-2-direct (round 7, REVISED — pivot)

Smallest-open-base specialization. We narrow the theorem to the case $|P_1|=2$ NON-LOCK and attack it directly, importing the certified LOCK base and endgame, plus the round-3 certified foundation (`two-entry-lemma`, `P1-minimal-transversal-lemma`).

**Round-7 PIVOT.** The central conjecture $q\le \operatorname{rad}(a_1)$ is **REFUTED** (independently verified by the naive $O(N^2)$ gcd-greedy, gold standard). The witness $a_1=375=3\cdot5^3$ IS a $|P_1|=2$ case ($P_1=\{3,5\}$, $M_1=15$) with governing prime $19>15=M_1$ (period $T=852$, $L=3990=2\cdot3\cdot5\cdot7\cdot19$, verified by `/tmp/round-6/mt_greedy.py` at $N=3000$ with $\geq 3T=2556$ consecutive diff-matches). The prior target of this approach — "every governing prime $r\le M_1=pq$" (Step 4 of the round-4 write-up) — is therefore **dead in this approach's own regime**: $|P_1|=2$ admits governing primes above $M_1$. The THEOREM (eventual AP) still holds for $a_1=375$ (it IS periodic). Real Gap A = **FINITENESS of the governing-prime set**, with no sharp a-priori bound currently known.

This round we (i) **re-target** from the dead $\le M_1$ bound to **finiteness**; (ii) **strengthen** the certified `cofactor-P1-divisibility` lever (the approach's positive deliverable) — the hypothesis relaxes from "hypothetical governing $r>M_1$" to "any governing $r\notin P_1$ (equivalently $\gcd(r,pq)=1$)"; the proof uses incomparability alone, with no minimal-criminal hypothesis; (iii) attempt the **slot-counting finiteness** argument (outline Step 4) and run the mandated **circularity test**.

**Outcome (round 7).** The strengthened `cofactor-P1-divisibility` lemma is proved (Step 10) and verified across 8 cases incl. the refutation witness ($a_1=375$, governing $\{2,3,5,7,19\}$; for $r\in\{2,7,19\}\setminus\{3,5\}=P_1$: 0 cofactor-fails in 3000 terms; $r=19$: 210 multiples, all cofactors divisible by 3 or 5). BUT the finiteness step (Step 11) is an explicit **GAP**: the lever forces the cofactor $k=a_n/r$ to carry $p$ or $q$ — a single small-prime factor — but does NOT bound $k$ above, does NOT bound the prime-factorization of $k$, and does NOT bound the cardinality of $G\cap(M_1,\infty)$. The "large-prime + small-cofactor slot-counting" argument (outline Step 4) **collapses to the certified-circular cofactor-bound wall**: bounding which primes appear in the cofactor's full factorization IS Gap A (the `schur-cofactor-premise-fails-in-periodic-regime` obstruction proves the cofactor prime set is INFINITE in the periodic regime). The trivial size bound $r\le a_{n_1}\le a_1+(n_1-1)M_1$ for the first $r$-multiple is VACUOUS (it bounds $n_1$ given $r$, not $r$; it does not bound the NUMBER of governing primes). The $|P_1|=2$ specialization does NOT give a cleaner finiteness argument than the general case — it hits the SAME wall. Status stays `partial`.

## Status
partial

## Approaches tried
- round 3, direct CRT + $2$-density on $|P_1|=2$ NON-LOCK — Two clean lemmas proved unconditionally (the $2$-entry lemma; the "$P_1$ is a minimal transversal" lemma). Cofactor-bound wall NOT closed: the hoped "$2$-density forces witnesses to be $2$-multiples" mechanism is REFUTED by $a_1=15$, $a_9=45$ odd. Outcome: partial.
- round 4, minimal-criminal + Schur specialized to $|P_1|=2$ — Set up the contradiction framework. Proved ONE positive structural lemma (`cofactor-P1-divisibility`: for hypothetical $r>M_1$, every $r$-multiple cofactor $k$ is divisible by $p$ or $q$). CERTIFIED the negative obstruction (Schur premise structurally false in $|P_1|=2$ periodic cases — cofactor AP + classical Schur $\Rightarrow$ infinitely many cofactor prime divisors; subsumed by the general `schur-cofactor-premise-fails-in-periodic-regime`). The cofactor-bound wall for $|P_1|=2$ is NOT cracked; the minimal-criminal + Schur specialization is a certified dead-end. Outcome: partial.
- round 7, REVISE/PIVOT — dropped the refuted $r\le M_1$ target; re-targeted FINITENESS of $G$ for $|P_1|=2$. STRENGTHENED `cofactor-P1-divisibility` (Step 10): hypothesis relaxed from "hypothetical $r>M_1$" to "any governing $r\notin P_1$ (i.e. $\gcd(r,pq)=1$)"; proof uses incomparability alone, no minimal-criminal needed; verified 0 cofactor-fails across $a_1\in\{15,35,65,77,91,143,375\}$ for every governing $r\notin P_1$ (incl. the refutation witness $a_1=375$, governing $\{2,3,5,7,19\}$, $r=19$: 210 multiples, 0 fails). Attempted the slot-counting finiteness argument (Step 11); ran the mandated circularity test. RESULT: the lever is too weak — it forces $k$ to carry $p$ or $q$ (a single small factor) but NOT to be small or to have finitely many prime divisors ($k$ ranges over the infinite set $\{pj:j\ge1\}\cup\{qj:j\ge1\}$). The slot-counting collapses to the cofactor-bound wall (bounding the full prime factorization of $k$ IS Gap A, by the `schur-cofactor-premise-fails-in-periodic-regime` obstruction). The trivial $r\le a_1$ bound is VACUOUS (bounds $n_1$ given $r$, not the cardinality of $G$). The $|P_1|=2$ specialization hits the SAME wall as the general case. Outcome: partial — one strengthened promotable lemma; finiteness GAP open and fenced by the same cofactor-bound circularity; the route is NOT dead (the certified lever survives and is now stronger) but is NOT solved.

## Current best

**Strengthened `cofactor-P1-divisibility` lemma (Step 10, this round's positive deliverable).** *Statement:* In the $|P_1|=2$ NON-LOCK regime ($a_1=p^kq$ or $pq$, $p<q$ odd primes), for ANY governing prime $r\notin P_1$ (equivalently $r$ prime with $\gcd(r,pq)=1$, i.e. $r\ne p,q$), every $r$-multiple cofactor $k=a_n/r$ (over terms $a_n\in\mathcal B_\infty$, which is every term) is divisible by $p$ or by $q$. *Mechanism:* $m=a_n\in\mathcal B_\infty$ $\Rightarrow$ some $T\in\operatorname{MT}(\mathcal F_\infty)$ has $\operatorname{rad}(T)\mid m$ (`binfinity-divisibility-progression-structure`); incomparability of $T$ with the minimal transversal $\{p,q\}\in\operatorname{MT}$ (`P1-minimal-transversal-lemma`) forces $T$ to contain exactly one of $\{p,q\}$ (since $\{p,q\}\not\subseteq T$ by minimality of $T$ — dropping $T\setminus\{p,q\}$ leaves a transversal — and $T\cap\{p,q\}\ne\varnothing$ by transversality of $S(a_1)=\{p,q\}$); coprimality $\gcd(r,\operatorname{rad}(T\setminus\{r\}))=1$ (as $r$ is prime and $r\notin T\setminus\{r\}$) transfers the divisibility to $k=m/r$. *Strengthens the round-4 certified version* by dropping the minimal-criminal hypothesis "$r$ is the smallest governing prime $>M_1$" — incomparability alone suffices; the "minimality of $r$" was an unused crutch. *Verified* for $a_1\in\{15,35,65,77,91,143,375\}$, every governing $r\notin P_1$: 0 cofactor-fails in 600–3000 terms; e.g. $a_1=375$, $r=19$: 210 multiples, 0 fails; $r=7$: 550 multiples, 0 fails; $r=2$: 2517 multiples, 0 fails. (Fails for $r\in P_1$ as expected — $\gcd(r,pq)\ne1$.)

**Conditional endgame (imported, certified).** Conditional on Gap A (finiteness of $G$), `distinct-supports-stabilize` $\Rightarrow$ $\mathcal B_\infty$ is $L$-periodic with $L=\prod_{r\in G}r$; `greedy-equals-cyclic-successor` + `cyclic-successor-bijection` $\Rightarrow$ $a_{n+T}=a_n+L$ for all $n\ge1$.

**Open gap (finiteness for $|P_1|=2$).** No non-trivial bound on the cardinality of $G\cap(M_1,\infty)$ is proven. The strengthened `cofactor-P1-divisibility` is consistent with the refutation witness ($a_1=375$, gov $19$; $19$'s cofactors carry 3 or 5) but provides no mechanism to PROVE finiteness. The slot-counting finiteness argument (Step 11) is GAP — it collapses to the cofactor-bound wall (circularity test FAILED: Step 11 secretly requires bounding the full prime factorization of the cofactor $k$, which IS Gap A by the `schur-cofactor-premise-fails-in-periodic-regime` obstruction). The trivial bound $r\le a_1$ (reviewer's caution) holds but is vacuous.

## Full proof
Not yet complete. The two round-3 unconditional lemmas (Steps 2–3), the round-4 minimal-criminal specialization (Step 6) + positive cofactor-divisibility lemma (Step 7) + negative cofactor-transient obstruction (Step 8), and the round-7 STRENGTHENED cofactor-divisibility lemma (Step 10) + circularity-test report (Step 11) are below. The finiteness step (Step 11) remains an explicit GAP; the conditional endgame (Step 5) is certified-imported.

---

### Setup and notation

Let $a_1,a_2,\dots$ be the sequence of the problem. Write $S(n)$ for the set of prime divisors of $n$, $P_1:=S(a_1)$, $M_1:=\operatorname{rad}(a_1)=\prod_{p\in P_1}p$, and $\mathcal F_n:=\{S(a_1),\dots,S(a_n)\}$, $\mathcal F_\infty:=\{S(a_n):n\ge1\}$. A *transversal* of $\mathcal F_\infty$ is a set $T$ of primes meeting every $S(a_n)$; an MT is a minimal one. Call a prime *governing* if it lies in $\bigcup\operatorname{MT}(\mathcal F_\infty)$ (equivalently — per the certified `mt-depends-on-set-system` + `distinct-supports-stabilize` — it divides the eventual period $L$). The whole theorem is, by the certified endgame, equivalent to **Gap A**: the set $G$ of governing primes is finite.

**Imported (certified) lemmas.**
- `linchpin-and-gap-bound`: every $a_n$ has a $P_1$-factor; and $d_n:=a_{n+1}-a_n\le M_1$.
- `lock-lemma`: if some term $a_i=p^k$ is a prime power, then $a_{n+1}=a_n+p$ for every $n\ge1$ (so $T=1,L=p$).
- `pairwise-intersecting-supports`: $S(a_i)\cap S(a_j)\ne\varnothing$ for all $i,j$.
- `every-term-in-binfinity` + `greedy-equals-cyclic-successor` + `cyclic-successor-bijection`: conditional on $\mathcal B_\infty$ being $L$-periodic (equivalently on Gap A), $a_{n+T}=a_n+L$ for all $n\ge1$.
- `distinct-supports-stabilize` (conditional on Gap A): $\mathcal B_\infty$ is $L$-periodic with $L=\prod_{r\in G}r$.
- `binfinity-divisibility-progression-structure` (unconditional): $m\in\mathcal B_\infty$ iff some $T\in\operatorname{MT}(\mathcal F_\infty)$ has $\operatorname{rad}(T)\mid m$.
- `two-entry-lemma` (round 3): $a_2=a_1+p=p(p^{k-1}q+1)$ is even, so $2\in S(a_2)$.
- `P1-minimal-transversal-lemma` (round 3): $P_1=\{p,q\}\in\operatorname{MT}(\mathcal F_\infty)$; both $p,q$ governing.
- `cofactor-P1-divisibility` (round 4, STRENGTHENED round 7 — see Step 10): for any governing $r\notin P_1$, every $r$-multiple cofactor $k$ is divisible by $p$ or $q$.
- `schur-cofactor-premise-fails-in-periodic-regime` (round 4, negative): in any periodic greedy sequence the cofactor AP $k_{i+s}=k_i+L/r$ has infinitely many prime divisors by classical Schur, so the cofactor-prime-finiteness premise is structurally false in the very regime the theorem establishes.

### Step 1 — Reduction to $|P_1|=2$ NON-LOCK

The `lock-lemma` handles every case in which some term is a prime power (every $a_1$ even, every $a_1=p^k$ or $a_1=p$, and more generally every $a_1$ for which a prime-power term is reached). The residual open case is $|P_1|=2$ AND no term is a prime power — the **$|P_1|=2$ NON-LOCK** regime. Write $P_1=\{p_{\rm sm},p_{\rm lg}\}=\{p,q\}$ with $p<q$.

**Claim.** In the $|P_1|=2$ NON-LOCK regime, $a_1$ is odd (so $p,q$ are both odd). *Proof.* If $2\mid a_1$, then $2\in P_1$, and by the `lock-lemma` coverage ($a_1$ even $\Rightarrow$ lock), the sequence locks at $L=2$ — contradicting NON-LOCK. Hence $2\nmid a_1$, so both primes of $P_1$ are odd. $\square$

In particular $a_1=p^kq$ or $a_1=pq$ (the only shapes with exactly two distinct prime factors), with $p<q$ odd primes. The $|P_1|\ge3$ case is deferred to `crt-period-lifting`.

### Step 2 — Lemma (2-entry): $a_2=a_1+p$ is even
*Imported, certified (`two-entry-lemma`).* $a_2=a_1+p=p(p^{k-1}q+1)$; since $p,q$ are odd, $p^{k-1}q+1$ is even, so $2\in S(a_2)$. The lever is genuinely $|P_1|=2$-specific.

### Step 3 — Lemma ($P_1$ is a minimal transversal): $P_1\in\operatorname{MT}(\mathcal F_\infty)$
*Imported, certified (`P1-minimal-transversal-lemma`).* $P_1=\{p,q\}$ is a minimal transversal of $\mathcal F_\infty$: transversality is the linchpin; minimality uses the sub-result "if $r\in P_1$ divides $a_n$ for every $n$, then the sequence LOCKs" — contradicting NON-LOCK. Hence both $p$ and $q$ are governing primes.

### Step 4 — The PRIOR target $r\le M_1$ is REFUTED (round 7 pivot)

The round-4 write-up posed as the open target: *every governing prime $r$ satisfies $r\le M_1=pq$* (the "cofactor-bound for $|P_1|=2$" conjecture, a specialization of the global $q\le\operatorname{rad}(a_1)$ conjecture to the $|P_1|=2$ regime).

**This target is REFUTED in the approach's own regime.** The witness $a_1=375=3\cdot5^3$ is a $|P_1|=2$ NON-LOCK case ($P_1=\{3,5\}$, $M_1=15$); the greedy sequence (computed by the corrected `/tmp/round-6/mt_greedy.py`, verified bit-exact against the naive $O(N^2)$ gcd-greedy gold standard on $a_1\in\{15,385,847,375\}$) has fundamental period $T=852$, $L=3990=2\cdot3\cdot5\cdot7\cdot19$, detected by $\geq 3T=2556$ consecutive diff-matches at $N=3000$; the governing prime $19$ satisfies $19>15=M_1$. The prime $19$ genuinely governs: among the first 3000 terms, 210 are divisible by 19 (period $T=852$ has $\approx 210\cdot 852/3000 \approx 60$ per period, a positive density). So $|P_1|=2$ admits governing primes strictly above $M_1=pq$.

The global conjecture $q\le\operatorname{rad}(a_1)$ is likewise refuted by the violation family $a_1=3\cdot5^e$ (odd $e\ge3$), $L=210\cdot X(e)$ with $X$ prime $>15$ ($e=3\to X=19$; $e=5\to X=67$; verified independently by the orchestrator). The THEOREM (eventual AP) still holds in every witness — they ARE periodic. The sharp bound $r\le M_1$ is dead as a TARGET.

**Re-target (round 7).** Drop the claim $r\le M_1$. The real Gap A specialized to $|P_1|=2$ is:
> **(Finiteness for $|P_1|=2$ NON-LOCK, TARGET).** The set $G$ of governing primes is FINITE.

No sharp a-priori bound on $\max G$ or on $|G|$ is currently known. The conditional endgame (Step 5) reduces the $|P_1|=2$ case to this finiteness target.

### Step 5 — Conditional conclusion (assuming finiteness)

Assume the finiteness target of Step 4. Then $G$ is finite. By `distinct-supports-stabilize` (Hypothesis = Gap A satisfied), there is $N_0$ with $\operatorname{MT}(\mathcal F_n)=\operatorname{MT}(\mathcal F_\infty)$ for $n\ge N_0$, and $\mathcal B_\infty$ is $L$-periodic with $L=\prod_{r\in G}r$. By `greedy-equals-cyclic-successor` (unconditional) the greedy equals the cyclic successor in $\mathcal B_\infty$ from $n=1$; by `cyclic-successor-bijection`, $a_{n+T}=a_n+L$ for all $n\ge1$, with $T=|\mathcal B_\infty\bmod L|$. This solves the $|P_1|=2$ NON-LOCK case (conditional on finiteness), and — with `crt-period-lifting` for the inductive lift — shrinks the theorem to $|P_1|\ge3$. $\square$ (conditional on Step 4-finiteness)

---

### Step 6 — Round-4 minimal-criminal specialization (mount; retained for context)

The round-4 minimal-criminal mount is retained as a reusable scaffold (Steps 6.1–6.5 of the round-4 write-up: well-ordering gives smallest governing $r>M_1$; primes in $(M_1,r)$ MT-transient; $r\mid a_n$ infinitely often; at $r$-multiple steps $d_n=r-(a_n\bmod r)$ forced since $d_n\le M_1<r$; cofactor-transversal structure; the linchpin $\{p,q\}$ always provides a small-prime transversal). The Schur Step 7 sub-route is **certified dead** (`schur-cofactor-premise-fails-in-periodic-regime`); we do NOT re-walk it. The mount is retained only to motivate the cofactor-divisibility lever, which SURVIVES the pivot.

### Step 7 — Lemma (cofactor $P_1$-divisibility, round-4 version, hypothetical $r>M_1$)

*Imported, certified round 4. SUPERSEDED by the strengthened Step 10 below (which relaxes the hypothesis); retained for provenance.* For $|P_1|=2$ NON-LOCK and hypothetical governing $r>M_1=pq$ (so $r\notin P_1$, $\gcd(r,pq)=1$), every $r$-multiple cofactor $k=a_n/r$ is divisible by $p$ or $q$. *Proof:* as in `lemmas/cofactor-P1-divisibility.md`, split on $T\in\operatorname{MT}(\mathcal F_\infty)$ with $\operatorname{rad}(T)\mid m$ — incomparability with $\{p,q\}$ forces exactly one of $\{p,q\}$ in $T$; coprimality $\gcd(r,\operatorname{rad}(T\setminus\{r\}))=1$ (from $r>M_1\ge\operatorname{rad}(T\setminus\{r\})$) transfers divisibility to $k$.

### Step 8 — Negative Lemma (cofactor-transient obstruction, $|P_1|=2$)

*Imported, certified round 4 (subsumed by the general `schur-cofactor-premise-fails-in-periodic-regime`).* In actual periodic $|P_1|=2$ cases the cofactor sequence $k_i=a_{n_i}/r$ is a union of $s$ arithmetic progressions with common difference $L/r>0$ (one AP per residue class modulo $L/r$); by classical Schur each AP has infinitely many prime divisors. The Schur premise "cofactor's prime set is eventually fixed-finite $\subseteq G$" is structurally false in the $|P_1|=2$ regime. This fences off the Schur/`aimo-0727` cofactor-finiteness contradiction and — crucially for Step 11 below — establishes that the cofactor's prime factorization is GENERALLY INFINITE in the periodic regime.

### Step 9 — What would still be needed (round-4 note, superseded by Step 11)

The round-4 note (a greedy-dynamic window-uniqueness argument, or a dynamical-systems framing specialized to $|P_1|=2$) is superseded by the round-7 Step 11 analysis (the slot-counting route is GAP, fenced by the cofactor-bound wall).

---

### Step 10 — STRENGTHENED Lemma (cofactor $P_1$-divisibility, any governing $r\notin P_1$) — round 7

**Lemma (strengthened).** *In the $|P_1|=2$ NON-LOCK regime, let $r$ be ANY governing prime with $r\notin P_1$ (equivalently $r$ is prime and $\gcd(r,pq)=1$, i.e. $r\ne p,q$). Then for every $r$-multiple term $a_n$ (i.e. every term, since every $a_n\in\mathcal B_\infty$ by `every-term-in-binfinity`), the cofactor $k=a_n/r$ is divisible by $p$ or by $q$.*

This **strengthens** the round-4 certified version (Step 7 / `lemmas/cofactor-P1-divisibility.md`) in two ways: (a) the hypothesis relaxes from "hypothetical governing $r>M_1$" to "any governing $r\notin P_1$" — in particular it now applies to ACTUAL governing primes (e.g. $r=2,7,19$ for $a_1=375$), not only the minimal-criminal hypothetical; (b) the proof uses ONLY incomparability with $\{p,q\}\in\operatorname{MT}$, with NO minimal-criminal hypothesis (the round-4 "minimality of $r$ as smallest governing $>M_1$" was an unused crutch — it was only invoked to conclude $T_0\subseteq\{\text{primes}\le M_1\}$, which is unnecessary for the divisibility transfer).

*Proof.* Let $m=a_n\in\mathcal B_\infty$ with $r\mid m$ (so $m=rk$, $k=m/r$). By `binfinity-divisibility-progression-structure`, there exists $T\in\operatorname{MT}(\mathcal F_\infty)$ with $\operatorname{rad}(T)\mid m$, i.e. $T\subseteq S(m)$. Since $r\mid m$ and $r$ is prime, $r\in S(m)$.

**Incomparability fact.** $T\in\operatorname{MT}(\mathcal F_\infty)$ and $\{p,q\}\in\operatorname{MT}(\mathcal F_\infty)$ (by `P1-minimal-transversal-lemma`) are distinct minimal transversals, hence incomparable under inclusion: neither $T\subseteq\{p,q\}$ nor $\{p,q\}\subseteq T$.

- $\{p,q\}\not\subseteq T$: otherwise, since $\{p,q\}$ is itself a transversal, $T$ would not be minimal (drop $T\setminus\{p,q\}$, still a transversal) — contradiction.
- $T\cap\{p,q\}\ne\varnothing$: $T$ must hit $S(a_1)=\{p,q\}$ (transversality of $\mathcal F_\infty$, which contains $S(a_1)$).

Combining: $T$ contains **exactly one** of $\{p,q\}$. WLOG say $p\in T$ (the $q$-case is symmetric). Note $r\notin\{p,q\}$ (hypothesis), so $p\ne r$.

Now split on whether $r\in T$:

- **$r\notin T$.** Then $\operatorname{rad}(T)\mid m=rk$ and $\gcd(r,\operatorname{rad}(T))=1$ (as $r$ is prime and $r\notin T$ so $r\nmid\operatorname{rad}(T)$). Hence $r\cdot\operatorname{rad}(T)\mid m=rk$, so $\operatorname{rad}(T)\mid k$. Since $p\in T$, $p\mid\operatorname{rad}(T)\mid k$. ✓

- **$r\in T$.** Write $T=\{r\}\cup T_0$ with $T_0=T\setminus\{r\}$ (a set of primes, $r\notin T_0$). $\operatorname{rad}(T)=r\cdot\operatorname{rad}(T_0)\mid m=rk$ gives $\operatorname{rad}(T_0)\mid k$. Since $p\in T$ and $p\ne r$, we have $p\in T_0$; hence $p\mid\operatorname{rad}(T_0)\mid k$. ✓

In both cases $p\mid k$ (symmetrically $q\mid k$ if $q\in T$). $\square$

**Computational verification.** For $a_1\in\{15,35,65,77,91,143,375\}$ (all $|P_1|=2$ NON-LOCK; $a_1=375$ is the refutation witness), computed the greedy sequence with the corrected `/tmp/round-6/mt_greedy.py` (bit-exact vs naive $O(N^2)$ gcd-greedy on $a_1\in\{15,385,847\}$). For every governing $r\notin P_1$ (identified as a prime factor of the detected $L$), checked every $r$-multiple cofactor $k=a_n/r$ for divisibility by $p$ or $q$. Result: **0 cofactor-fails** across all cases (600–3000 terms each). Highlights:

| $a_1$ | $P_1$ | $M_1$ | governing $G$ (primes of $L$) | $r\notin P_1$ tested | $r$-multiples | cofactor-fails |
|---|---|---|---|---|---|---|
| 15 | $\{3,5\}$ | 15 | $\{2,3,5\}$ | $r=2$ | 525 | 0 |
| 35 | $\{5,7\}$ | 35 | $\{2,3,5,7\}$ | $r=2,3$ | 441 / 318 | 0 / 0 |
| 65 | $\{5,13\}$ | 65 | $\{2,3,5,13\}$ | $r=2,3$ | 445 / 310 | 0 / 0 |
| 77 | $\{7,11\}$ | 77 | $\{2,7,11\}$ | $r=2$ | 566 | 0 |
| 91 | $\{7,13\}$ | 91 | $\{2,7,13\}$ | $r=2$ | 570 | 0 |
| 143 | $\{11,13\}$ | 143 | $\{2,3,11,13\}$ | $r=2,3$ | 459 / 337 | 0 / 0 |
| **375** | $\{3,5\}$ | 15 | $\{2,3,5,7,19\}$ | $r=2,7,19$ | 2517 / 550 / 210 | 0 / 0 / 0 |

(The lemma FAILS for $r\in P_1$ as expected — e.g. $a_1=375$, $r=3$: 1257 cofactor-fails; $r=5$: 141 fails — confirming the hypothesis $r\notin P_1$ is essential, matching the round-4 remark. The proof breaks at "$\gcd(r,p)=1$" when $r=p$.)

**Honest assessment of the lemma's reach.** The strengthened lemma is a genuine, clean $|P_1|=2$-specific structural fact (the incomparability "exactly one of $\{p,q\}$" uses `P1-minimal-transversal-lemma`, unavailable for $|P_1|\ge3$). It is strictly stronger than the round-4 version (applies to all governing $r\notin P_1$, including actual primes, not only the minimal-criminal hypothetical). But it is **weak** in the same way as before: it forces $k\ge\min(p,q)\ge3$ (a single small-prime factor of the cofactor), giving no upper bound on $k$, no bound on the prime factorization of $k$, and no bound on $r$. The lemma does not close the finiteness wall; it is recorded as a partial structural advance for the $|P_1|=2$ specialization.

### Step 11 — The finiteness step (slot-counting): GAP + circularity test

The revised plan (per the outline-reviewer's directive) attempts the "small-cofactor-for-large-$r$ + bounded-gap slot-counting" finiteness argument. We develop the candidate argument and then run the mandated circularity test, which shows the argument is **circular** (collapses to the cofactor-bound wall).

**Candidate argument (sketch).** Assume for contradiction that $G$ is INFINITE for a $|P_1|=2$ NON-LOCK $a_1$. Then $G\setminus P_1$ is infinite (as $P_1$ is finite); enumerate $G\setminus P_1=\{r_1<r_2<\cdots\}$, all coprime to $pq$. By `binfinity-divisibility-progression-structure`, each $r_i$ governing $\Rightarrow$ $r_i$-multiples appear as terms: for each $i$ there is a term $a_{n_i}=r_i\cdot k_i$ with $k_i\ge1$. By the strengthened Step-10 lemma, $k_i$ is divisible by $p$ or $q$, so $k_i\ge\min(p,q)\ge3$, hence $a_{n_i}\ge3r_i$. The "slot" idea: each large governing $r_i$ contributes $r_i$-multiple terms of the form $r_i\cdot(p\cdot j)$ or $r_i\cdot(q\cdot j)$; the window-uniqueness $d_n\le M_1<r_i$ (for $r_i>M_1$) gives at most one $r_i$-multiple per window of $M_1$ consecutive increments; one hopes to count "large-prime + small-cofactor" slots per bounded window and conclude only finitely many $r_i$ can be accommodated.

**Why this does NOT yield finiteness.** Three independent obstructions:

1. **The cofactor is NOT small.** The strengthened lemma forces $p\mid k_i$ or $q\mid k_i$ — a single small-prime factor — but $k_i=a_{n_i}/r_i$ grows with $n_i$ (linearly in $n_i$, since $a_n\le a_1+(n-1)M_1$). So $k_i\in\{p\cdot j:j\ge1\}\cup\{q\cdot j:j\ge1\}$, an **infinite** set. The "small-cofactor" premise of the slot-counting argument is FALSE for all but the first few $r_i$-multiples; the cofactor is not confined to a finite set of slots. The only cofactor that is "small" is the FIRST $r_i$-multiple's (where $k_i\ge\min(p,q)$ but is otherwise unconstrained above); and even that first cofactor can be as large as $\sim a_{n_i}/r_i$, with $n_i$ itself unbounded.

2. **The trivial size bound is vacuous.** The only a-priori size bound on $r_i$ is $r_i\le a_{n_i}\le a_1+(n_i-1)M_1$, which bounds $n_i$ GIVEN $r_i$, not $r_i$ a priori. It does not bound the NUMBER of governing primes (the cardinality of $G\cap(M_1,\infty)$), which is the finiteness target. The reviewer's caution is exact: $r\le a_1$ is trivially true for the first $r$-multiple (when $n_1=1$, i.e. $r\mid a_1$, which is excluded by $r\notin P_1$) and otherwise gives no information. (For the refutation witness $a_1=375$: $19\le375$ holds trivially, and $19$ IS finite — but the trivial bound does not PROVE $19$ is the only governing prime $>M_1$, nor that the set is finite.)

3. **Circularity (the mandated test).** To make the slot-counting rigorous — to show only finitely many distinct large $r$-values can be accommodated — one must bound WHICH primes can appear in the cofactor's prime factorization (so that the "slots" $r\cdot k$ with $k\in\{pj\}\cup\{qj\}$ are constrained to finitely many prime values $r$). But bounding the prime factorization of the cofactor $k=a_n/r$ IS Gap A: by the `schur-cofactor-premise-fails-in-periodic-regime` obstruction (Step 8), in any periodic realization the cofactor sequence $k_i$ is a union of APs with common difference $L/r>0$, and by classical Schur the set of primes dividing some $k_i$ is INFINITE. So the cofactor's prime factorization is provably infinite in the periodic regime; bounding it finitely presupposes the very finiteness (Gap A) we are trying to prove. **The slot-counting argument is circular: it secretly requires Gap A.**

**Conclusion of the circularity test: FAILED.** The slot-counting finiteness argument collapses to the cofactor-bound wall (the same wall certified dead for `witness-density-recurrence`, `crt-period-lifting`, `primal-minimal-support-stabilization`, `minimal-criminal-schur-contradiction`). The $|P_1|=2$ specialization, via the strengthened `cofactor-P1-divisibility` lever, does NOT give a cleaner finiteness argument than the general case — it hits the SAME obstruction. The lever is too weak: it provides a $P_1$-factor of the cofactor (a floor on $k$, not a ceiling; a single small-prime factor, not a finite prime-factorization).

**Consistency with the refutation witness.** The stress-test $a_1=375$ (governing $\{2,3,5,7,19\}$, $19>M_1=15$) is consistent with the lever: $19$'s 210 $r$-multiples all carry cofactor divisible by 3 or 5 (0 fails). The governing set IS finite here ($|G|=5$), as the theorem requires. But the lever does not PROVE the finiteness — it is merely consistent with it. The trivial bound $19\le375=a_1$ holds but is vacuous (it would also "hold" for any $r\le375$, finite or infinite in cardinality).

**Honest conclusion.** The finiteness step (Step 11) is an explicit GAP. The strengthened `cofactor-P1-divisibility` is a real advance (Step 10, promotable) but is insufficient to close Gap A for $|P_1|=2$. The $|P_1|=2$ route is NOT dead (the certified lever survives the pivot and is now stronger), but it is NOT solved. A genuinely new ingredient — not reducing to bounding the cofactor's full prime factorization — would be needed to close Step 11; none is on the table within this approach's framing.

---

## Spec concerns

- **The trivial-bound trap.** The reviewer's caution is borne out: the natural "first $r$-multiple" observation gives $r\le a_{n_1}$, which is vacuous as a finiteness mechanism. Any future finiteness argument in this approach must target the CARDINALITY of $G\cap(M_1,\infty)$, not the individual size of $r$; and it must do so without bounding the cofactor's full prime factorization (else circular).
- **The cofactor-bound wall is genuinely shared.** The $|P_1|=2$ specialization does not escape the wall that kills the general case. The `schur-cofactor-premise-fails-in-periodic-regime` obstruction applies identically in $|P_1|=2$ (Step 8 is a specialization). A non-circular finiteness proof for $|P_1|=2$, if it exists, must come from a DIFFERENT mechanism (e.g. the `parametric-recruitment-family` structural-covering route or the `f-of-a1-bounded-nonresidue-statistic` forward-determinism route), not from a cofactor-bound variant.
- **The strengthened lemma's reach.** It is a divisibility fact (floor on $k$), not a size fact (no ceiling on $k$) and not a finiteness fact (no bound on $|G|$). Proposing it as a promotable lemma in its strengthened form (Step 10) — but flagging that it does NOT close Gap A, so consumers must not over-claim.

## Promotable lemmas

1. **`cofactor-P1-divisibility` (STRENGTHENED, round 7)** — proposed as a REFINEMENT of the certified round-4 lemma `lemmas/cofactor-P1-divisibility.md`. *Statement:* In the $|P_1|=2$ NON-LOCK regime, for ANY governing prime $r\notin P_1$ (equivalently $r$ prime, $\gcd(r,pq)=1$, i.e. $r\ne p,q$ — NOT only the minimal-criminal hypothetical $r>M_1$), every $r$-multiple cofactor $k=a_n/r$ (over terms $a_n\in\mathcal B_\infty$, i.e. every term) is divisible by $p$ or by $q$. *Mechanism:* $m\in\mathcal B_\infty$ $\Rightarrow$ $\operatorname{rad}(T)\mid m$ for some $T\in\operatorname{MT}(\mathcal F_\infty)$ (`binfinity-divisibility-progression-structure`); incomparability of $T$ with the minimal transversal $\{p,q\}\in\operatorname{MT}$ (`P1-minimal-transversal-lemma`) forces $T$ to contain exactly one of $\{p,q\}$ (via $\{p,q\}\not\subseteq T$ — minimality of $T$ given $\{p,q\}$ is a transversal — and $T\cap\{p,q\}\ne\varnothing$ — transversality of $S(a_1)=\{p,q\}$); coprimality $\gcd(r,\operatorname{rad}(T\setminus\{r\}))=1$ (as $r$ is prime, $r\notin T\setminus\{r\}$) transfers the divisibility to $k=m/r$. NO minimal-criminal hypothesis needed (the round-4 "smallest governing $r>M_1$" was an unused crutch). *Where proved:* Step 10 of this file. Unconditional within the $|P_1|=2$ NON-LOCK regime. *Verified* for $a_1\in\{15,35,65,77,91,143,375\}$, every governing $r\notin P_1$, 600–3000 terms: 0 cofactor-fails (incl. the refutation witness $a_1=375$, $r\in\{2,7,19\}$: 2517/550/210 multiples, 0 fails each). *Limitation (explicit):* forces only $k\ge\min(p,q)\ge3$ — a floor, not a ceiling; no upper bound on $k$, no bound on the prime factorization of $k$, no bound on $|G|$. Does NOT close Gap A. Consumers must not over-claim. *If the reviewer prefers not to refine the existing lemma file, this strengthening can stand as a corollary note in this approach file.*

2. **`p1eq2-finiteness-slot-counting-circular` (NEW NEGATIVE, round 7)** — proposed for certification as a fence. *Statement:* For $|P_1|=2$ NON-LOCK, the "small-cofactor-for-large-$r$ + bounded-gap slot-counting" finiteness argument is CIRCULAR: it requires bounding the prime factorization of the cofactor $k=a_n/r$, which IS Gap A (by the `schur-cofactor-premise-fails-in-periodic-regime` obstruction: in any periodic realization the cofactor AP has infinitely many prime divisors). The strengthened `cofactor-P1-divisibility` (which forces only $p\mid k$ or $q\mid k$, a single small-prime factor) is too weak to make the slot set finite — $k$ ranges over the infinite set $\{pj:j\ge1\}\cup\{qj:j\ge1\}$. The trivial size bound $r\le a_{n_1}$ is vacuous (bounds $n_1$ given $r$, not the cardinality of $G$). Consequently the $|P_1|=2$ specialization via the cofactor-divisibility lever hits the SAME cofactor-bound wall as the general case; it does NOT give a cleaner finiteness argument. *Where proved:* Step 11 of this file. Fences off future $|P_1|=2$-specialized cofactor-divisibility finiteness retries that do not first break the cofactor-bound circularity.
