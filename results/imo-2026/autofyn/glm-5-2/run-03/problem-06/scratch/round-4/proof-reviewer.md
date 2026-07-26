# Round 4 proof-reviewer report — `imo-2026-06`

**Round 4 review of three built approaches.** All three builders self-assessed CHANGES REQUESTED (partial). I verified each independently (re-derived the load-bearing steps, ran the computations). Verdict: **all three CHANGES REQUESTED — honest, no over-claiming.** The headline Schur-premise-false argument is **rigorous and correct** (verified: AP structure, Schur's theorem application, blocker involution, cofactor-P1-divisibility). Four new lemmas certified (one proposed lemma rejected as subsumed). Wall now resists ~11+ mechanisms.

---

## Approach 1: `minimal-criminal-schur-contradiction` — CHANGES REQUESTED (partial)

### What the builder claims
- A genuinely-new minimal-criminal **setup** (Steps 1–6): well-ordering gives a smallest governing $q>M_1$; primes in $(M_1,q)$ are MT-transient; $q\mid a_n$ infinitely often; at $q$-multiple steps $d_{n-1}=q-(a_{n-1}\bmod q)$ is forced (since $d_{n-1}\le M_1<q$); cofactor $k_i=a_{n_i}/q$ has $\operatorname{primefactors}(k_i)$ transversing prior non-$q$-multiple supports; $P_1$ always provides a small-prime transversal.
- A **negative resolution** of Step 7 (the Schur/`aimo-0727` contradiction sub-route) by three independent obstructions (A1 engine absent, A2 contrapositive false in general, A3 premise provably false in periodic regime).

### Independent verification
**(A3) is the load-bearing claim — re-derived from scratch.** Suppose Gap A holds, so $a_{n+T}=a_n+L$. Let $q$ govern, so $q\mid L$. The $q$-multiples occur at a fixed set of residue classes mod $T$ (since $a_n\bmod q$ is $T$-periodic via $q\mid L$). If $n_i$ indexes the $q$-multiples and $s=$ count per period, then $n_{i+s}=n_i+T$ and
$$k_{i+s}=\frac{a_{n_i+T}}{q}=\frac{a_{n_i}+L}{q}=k_i+\frac{L}{q}.$$
So $(k_i)$ is a union of $s$ arithmetic progressions with common difference $L/q\ge1$. **Schur's theorem** (non-constant integer polynomial $\Rightarrow$ infinitely many prime divisors) applies to each $f_j(m)=(L/q)m+c_j$. ∎

**Computational verification (ran myself):**
- $a_1=15$: $T=8$, $L=30$, $q=3$ governing. Confirmed periodic from $n=0$. Cofactor AP: $k_{i+6}=k_i+10$ holds over 200 terms. Distinct primes $>M_1=15$ in cofactors grow: 25 distinct over 200 terms, max 127. (Builder's numbers for longer horizons consistent.)
- The AP-structure identity $k_{i+s}=k_i+L/q$ is a **theorem** of periodicity + $q\mid L$ (not merely empirical).

**(A1) re-derived.** The `aimo-0727` crux's confining engine is the multiplicative recurrence $a_{k+1}\mid a_k(b_k+2)$; here consecutive cofactors satisfy $k_{i+1}-k_i=(\sum d_n)/q$ (additive, no recurrence). Confirmed the engine is absent. **(A2) re-derived.** Schur's contrapositive "fixed finite prime set $\Rightarrow$ bounded" requires the sequence to be polynomial-driven; counterexample $k_i=2^i$ (prime set $\{2\}$, unbounded) shows the implication is false in general. Both obstructions are sound.

**MT-transient $\not\Rightarrow$ cofactor-transient.** In the periodic regime, the cofactor AP has infinitely many prime divisors (Schur); only finitely many can be governing (in $G$ = prime factors of $L$); so infinitely many MT-transient primes divide some cofactor. Rigorous. The empirical $a_1=15$ case (361+ distinct MT-transient primes in cofactors after MT stabilization) confirms.

### Status assessment
- Steps 1–6: SOUND, genuinely new (not a re-derivation of any of the 10+ dead mechanisms). Reusable mount point.
- Step 7 (Schur sub-route): certified dead by three independent obstructions. The negative lemma `schur-cofactor-premise-fails-in-periodic-regime` is rigorous and certified.
- No gap in the negative resolution; no over-claiming. The setup is partial progress (a reusable mount point + a certified fence), but Gap A is NOT closed.

**Verdict: CHANGES REQUESTED.** Status: partial. The gap: "find a contradiction mechanism (not Schur, not cofactor-bound, not pure-static, not mod-$q$ finite-state) that mounts on Steps 1–6." No such mechanism on the table.

---

## Approach 2: `primal-minimal-support-stabilization` — CHANGES REQUESTED (partial)

### What the builder claims
- Two structural lemmas: (1) primal–dual equivalence of Gap A via blocker involution; (2) window-uniqueness reduces to cofactor-bound.
- Honest fencing: the primal framing is provably equivalent to Gap A (Lemma 1); the window-uniqueness continuation unpacks to the cofactor wall (Lemma 2).
- Empirical silver lining (CONJECTURE): across 19 NON-LOCK $a_1$ (80k+ steps), no prime $>M_1$ enters any minimal support at any finite $n$.

### Independent verification
**Lemma 1 (blocker involution) re-derived.** The classical blocker involution $b(b(\mathcal C))=\mathcal C$ on clutters over a finite ground (Edmonds–Fulkerson) is correctly invoked. The two directions:
- (P)$\Rightarrow$(D): $\operatorname{MS}_\infty$ clutter over finite ground $X\subseteq G$; $b(\operatorname{MS}_\infty)=\operatorname{MT}(\mathcal F_\infty)$ finite clutter over $X$. ✓
- (D)$\Rightarrow$(P): every $S\in\operatorname{MS}_\infty$ is a transversal of $\operatorname{MT}(\mathcal F_\infty)$ (since $S=S(a_j)$ and every $T\in\operatorname{MT}$ hits $S(a_j)$), so $S\subseteq Y=\bigcup\operatorname{MT}$; hence $\bigcup\operatorname{MS}_\infty\subseteq Y$ finite; blocker involution gives $b(b(\operatorname{MS}_\infty))=\operatorname{MS}_\infty$. ✓

**Computational verification (ran myself):** $a_1=15$, $\operatorname{MS}_\infty=\{\{2,3\},\{2,5\},\{3,5\}\}$; $\operatorname{MT}(\operatorname{MT}(\mathcal F_{40}))=\operatorname{MS}$ confirmed. Blocker involution holds.

**Lemma 2 (window-uniqueness reduces to cofactor) re-derived.**
- (i) Window size $M_1<q$ $\Rightarrow$ at most one $q$-multiple. ✓
- (ii) Admissibility decomposes: $m=kq$ admissible iff $\operatorname{primefactors}(k)$ hits $q$-free minimals. ✓
- (iii) To prove $q$ never enters via window-uniqueness, must show (a) $\operatorname{primefactors}(k)$ fails the transversal OR (b) smaller admissible $m'$ exists — both require controlling $\operatorname{primefactors}(k)$, the certified-circular cofactor-bound step. ✓

The reduction to the cofactor wall is honest and rigorous.

### Status assessment
- Both lemmas are sound, rigorous, and reusable as fences.
- No over-claiming. The builder explicitly states Step 4 (load-bearing) is open and cannot be proved without either a genuinely new non-cofactor ingredient or re-proving the dead cofactor bound.
- The empirical silver lining is correctly labeled a CONJECTURE (not proved).

**Verdict: CHANGES REQUESTED.** Status: partial. The gap: Step 4 — no non-cofactor greedy-dynamic ingredient found; the framing is fenced off as equivalent to Gap A.

---

## Approach 3: `p1-equals-2-direct` — CHANGES REQUESTED (partial)

### What the builder claims
- Round-4 specialization of the minimal-criminal setup to $|P_1|=2$ (tightest base).
- **Positive lemma `cofactor-P1-divisibility`:** for hypothetical governing $r>M_1=pq$, every $r$-multiple cofactor $k=a_n/r$ is divisible by $p$ or $q$.
- **Negative lemma `cofactor-transient-obstruction-P1-equals-2`:** the Schur premise is structurally false in $|P_1|=2$ (AP structure + Schur $\Rightarrow$ infinite cofactor prime set).

### Independent verification
**Positive lemma re-derived from scratch.** The case split on $T\in\operatorname{MT}(\mathcal F_\infty)$:
- $T=\{p,q\}$: $pq\mid m$, $r\mid m$, $\gcd(r,pq)=1$ $\Rightarrow$ $pq\mid k$. ✓
- $r\in T$: minimality of $r$ $\Rightarrow$ $T_0\subseteq$ primes $\le M_1$; incomparability with $\{p,q\}\in\operatorname{MT}$ (since $\{p,q\}$ is a transversal, $\{p,q\}\subseteq T$ would contradict minimality of $T$); $T\cap\{p,q\}\ne\varnothing$ (transversality of $S(a_1)=\{p,q\}$); so exactly one of $\{p,q\}$ in $T$; coprimality $\gcd(r,\operatorname{rad}(T_0\cup\{p\}))=1$ transfers $p\mid k$. ✓
- $r\notin T$, $T\ne\{p,q\}$: $T\subseteq$ primes $\le M_1$; same incomparability; $\operatorname{rad}(T)\mid k$ with $p\in\operatorname{rad}(T)$. ✓

**Computational verification (ran myself):** $a_1=15$, $r=2$ (governing, $\notin P_1$): 0 cofactor failures over 350 2-multiples. $a_1=35$, $r\in\{2,3\}$: 0 failures. The lemma is sound (but weak — only forces $k\ge\min(p,q)\ge3$, no upper bound).

**Negative lemma re-derived.** Same AP argument as the general `schur-cofactor-premise-fails-in-periodic-regime`, specialized to $|P_1|=2$. Verified: $a_1=35$, $r=3$, $T=34$, $L=210$, $s=18$, $L/r=70$, $k_{i+s}=k_i+70$ holds. Sound.

**Note:** The negative lemma `cofactor-transient-obstruction-P1-equals-2` is literally a corollary of the general `schur-cofactor-premise-fails-in-periodic-regime` (which applies to any periodic greedy sequence regardless of $|P_1|$). I **reject separate certification** of the $|P_1|=2$ version as subsumed; the general fence covers it. The builder honestly acknowledged this potential deduplication.

### Status assessment
- The positive lemma is sound but weak (no upper bound on $k$).
- The negative lemma is sound but subsumed by the general version.
- No over-claiming. The cofactor-bound wall for $|P_1|=2$ remains open.

**Verdict: CHANGES REQUESTED.** Status: partial. The gap: cofactor-bound for $|P_1|=2$ (Step 4) remains open; the minimal-criminal + Schur specialization is fenced off.

---

## Lemma certification summary

**Certified (4 new, total 25):**
1. `schur-cofactor-premise-fails-in-periodic-regime` (−, general fence; subsumes #5 below).
2. `primal-dual-gap-a-equivalence` (structural, fences primal framing).
3. `window-uniqueness-reduces-to-cofactor` (structural, fences window-local escapes).
4. `cofactor-P1-divisibility` (+, $|P_1|=2$-specific, weak but genuine).

**Rejected (subsumed):**
- `cofactor-transient-obstruction-P1-equals-2` — subsumed by `schur-cofactor-premise-fails-in-periodic-regime` (general version covers $|P_1|=2$). Not separately certified; referenced as corollary.

**Total certified lemmas: 25** (was 21; +4 this round).

---

## Round-5 directive: is the $q\le M_1$ conjecture provable with olympiad-accessible tools?

**Candid assessment: I do NOT believe the $q\le M_1$ conjecture is provable with the tools currently on the table.** The wall now resists **~11+ independent mechanisms**, all collapsing to the same cofactor-transversal circularity:

1. `aimo-0030` prime-factor strip (Lemma C no-go + admissibility-transfer obstruction).
2. `aimo-0678` MT-frontier monovariant (non-monotone, certified).
3. Density/covering-capacity lower bound (circular, certified).
4. Modular/residue finite-statistic (minimal functional modulus = $L$).
5. `aimo-0134` integer-monovariant transfer (no shrinking range, certified).
6. `aimo-0231` CRT fiber-lift (trivial identity, circular).
7. 2-density dominance for $|P_1|=2$ (refuted by $a_1=15$).
8. Pure statics (`syndetic-divisible-closed-not-periodic` counterexample).
9. Schur/`aimo-0727` cofactor-finiteness (premise provably false in periodic regime, certified this round).
10. Primal minimal-support stabilization (equivalent to dual via blocker involution, certified this round).
11. Window-uniqueness (reduces to cofactor-bound, certified this round).

The pattern is unmistakable: **every** route that tries to bound which primes enter term-supports between consecutive large-prime witnesses reduces to the SAME cofactor-transversal step, and that step is circular (bounding the cofactor's primes IS Gap A). The negative lemmas now PROVE that several natural-sounding escapes (pure statics, Schur cofactor-finiteness, primal framing, window-uniqueness) are not merely unproved but **structurally incapable** of working.

**My judgment: the problem requires a genuinely different mathematical insight not yet on the table.** The $q\le M_1$ conjecture is almost certainly TRUE (273+ cases, 0 failures, holds at every finite stage in 19 NON-LOCK cases across 80k+ steps), but its proof is not accessible by any cofactor/transversal/MT/statics/monovariant/residue route. The obstacle is structural: the cofactor-transversal structure is a tautology of the greedy admissibility condition, and any argument that tries to extract a prime bound from it presupposes the bound.

**The one untried direction I can name (with low confidence):** a **direct combinatorial induction on the increment sequence $(d_n)$ as a word over the finite alphabet $\{1,\dots,M_1\}$**, exploiting the greedy rule's LOCAL rewriting — WITHOUT forming $\mathcal B_\infty$ or $\operatorname{MT}$ at all. The round-3 dispatch flagged this (combinatorics-on-words / substitution-morphism); the round-4 explorers reportedly scouted it dead for the general case, but I have not seen a rigorous obstruction for the $|P_1|=2$ specialization specifically. The hope: prove $(d_n)$ is the fixed point of a finite substitution (or a finite-state transducer) by exhibiting the substitution explicitly from the greedy rule + gap bound; then periodicity of $(d_n)$ is a purely combinatorial fact (finite substitution $\Rightarrow$ eventually periodic if the substitution is primitive / the orbit is finite). This sidesteps Gap A entirely — no cofactor, no MT, no transversal — IF the substitution can be exhibited. The risk: the "transition leak" (89 conflicts for $a_1=385$ on $\bmod M_1$) suggests the state may not be finite-state-determined from a residue window alone; but a DYNAMIC window state (recent $d$-pattern + witness-type count) might close. **I recommend round 5 mount exactly one focused attempt at exhibiting the substitution for $|P_1|=2$ cases (smallest, most-structured) and proving its primitivity — and if that fails with a clean obstruction, the problem should be flagged as likely beyond olympiad-accessible tools and the run should consolidate.**

**Fallback if round 5 also fails:** the run has built a deep, rigorous characterization of the wall (25 certified lemmas, 11+ dead mechanisms, the cofactor-bound circularity identified from multiple angles). The conditional proof (Gap A $\Rightarrow$ theorem) is complete and certified; the LOCK sub-case is solved; the endgame is rigorous. This is substantial partial progress on a genuinely hard problem, even without a full solve.

## Status
partial
