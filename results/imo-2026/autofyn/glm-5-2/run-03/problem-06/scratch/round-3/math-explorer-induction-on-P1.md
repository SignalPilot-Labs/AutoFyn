# imo-2026-06 — structural induction on $|P_1|=|S(a_1)|$ (round 3)

Lens: bypass the transversal framework. Induct on $|P_1|$: base $|P_1|=1$ (LOCK, certified); $|P_1|=2$ direct CRT/valuation; inductive step via a "reducible prime" $r\in P_1$.

I scouted this route computationally (7000–12000 terms per case, strict period detector requiring ≥1500 consecutive diff-matches). I did NOT prove anything; the findings below are evidence/conjecture.

## Headline: the route PARTIALLY bypasses Gap A, but the inductive step has no clean quotient map

The structural-induction route has **one genuine win**, **one narrow hard sub-case**, and **one negative finding**:

- **WIN (base case).** $|P_1|=1$ is the certified `lock-lemma`. Moreover, the LOCK lemma covers a LARGE fraction of $|P_1|=2$ cases too: **every $a_1$ even** locks at $L=2$; **every $a_1=p^k q$ with $p$ the smaller prime AND $p=2$** locks; many $a_1=p^k q$ with $p$ odd smaller lock (e.g. $275=5^2\cdot 11\to L=5$, $325=5^2\cdot 13\to L=5$, $189=3^3\cdot 7\to L=3$, $63=3^2\cdot 7\to L=3$, $605=5\cdot 11^2\to L=5$). The round-2 "monovariant killer" $a_1=116=2^2\cdot 29$ is **LOCK at $L=2$** (lock-lemma covers it; $128=2^7$ is reached at $n=7$, the transient $59$ entering MT at $n=2$ is irrelevant under this framing).
- **NARROW HARD SUB-CASE.** The genuine $|P_1|=2$ NON-LOCK case is essentially squarefree-ish $a_1=pq$ (or $p^k q$ where no power of the smaller prime is reached, e.g. $175=5^2\cdot 7$, $245=5\cdot 7^2$, $539=7^2\cdot 11$, $637=7^2\cdot 13$, $847=7\cdot 11^2$, $135=3^3\cdot 5$). Here $2$ enters provably at $n=2$ ($a_2=a_1+p_{\rm sm}=p_{\rm sm}(q+1)$ is even), and the wall is *still* "bound the new governing primes" — i.e. Gap A in disguise, just specialized to $|P_1|=2$.
- **NEGATIVE FINDING (inductive step).** There is NO simple quotient/projection map from the greedy sequence of $a_1$ ($|P_1|=k$) to that of $a_1/r$ ($|P_1|=k-1$). Tested for $a_1=385=5\cdot 7\cdot 11$, $r=11$: (i) the not-$r$ sub-sequence does NOT match $\text{greedy}(35)$ (first terms $390,392,399,406,\dots$ vs greedy(35)=$35,40,42,45,\dots$); (ii) the $r$-divisible sub-sequence divided by $r$ does not match a smaller greedy either; (iii) the $p$-adic valuations $v_p(a_n)$ are bounded but do NOT stabilize to a constant (e.g. for $a_1=385$: $v_5\in\{0,1,2,3,4\}$, $v_7\in\{0,1,2,3,4\}$, $v_{11}\in\{0,1,2,3\}$, all fluctuating in the tail). So "find a reducible prime whose valuation stabilizes" does not work.

The relation $L(a_1) = L(a_1/r)\cdot r\cdot(\text{new gov prime(s)})$ holds empirically (e.g. $L(385)=43890=210\cdot 209=L(35)\cdot 11\cdot 19$), but the "new gov prime" $19$ is genuinely new — it is NOT in $\text{greedy}(35)$'s governing set $\{2,3,5,7\}$ and is NOT predicted by greedy(35)'s structure. The extension from $|P_1|=k-1$ to $|P_1|=k$ QUALITATIVELY CHANGES the admissibility structure (new terms like $a_5=399=3\cdot 7\cdot 19$ appear that are absent from greedy(35) entirely — $399=210+189$ and $189\bmod 210$ is NOT in greedy(35)'s residue set).

## Distinct openings (each a different attack the outliner could build)

1. **CLOSE THE $|P_1|=2$ NON-LOCK CASE DIRECTLY.** This is the route's strongest target. Empirically (13 squarefree $a_1=pq$ + 8 non-squarefree $a_1=p^k q$ tested to convergence), the governing primes are ALWAYS $\subseteq P_1\cup\{2,3,5,7,13,19,41\}$ — but NOT bounded by an absolute constant ($a_1=847=7\cdot 11^2$ gives gov prime $41$). The right conjecture is the existing $q\le M_1=\operatorname{rad}(a_1)$ bound, specialized to $|P_1|=2$. The $|P_1|=2$ constraint gives ONE rigid lever: **$a_2=a_1+p_{\rm sm}$ is provably even, so $2$ enters at $n=2$** (proof: $a_1+k$ for $1\le k<p_{\rm sm}$ shares no prime with $a_1=pq$, since $p\nmid k$ and $q\nmid k$ as $k<p<q$). After $2$ enters, the active primes are $\{2,p_{\rm sm}\}\cup$ (prime factors of $q+1$). The greedy from $a_2$ onward has $2$-multiples at density $1/2\gg 1/p_{\rm sm}$. A direct density/CRT argument bounding the new gov primes for $|P_1|=2$ might exist; the empirical bound $q\le M_1=p\cdot q$ is loose enough to admit a clean proof.
2. **`aimo-0134`-STYLE INTEGER-MONOVOVARIANT FRAMING (the genuinely different route).** The crux of `aimo-0134` (Netherlands, sequences-and-recurrences, see below): define an integer-valued running statistic $b_k=\lfloor\text{partial}/k\rfloor$, use integrality to upgrade a strict inequality into weak monotonicity, conclude eventual constancy, then transfer back to the original sequence. **This is a genuinely different framing** — it bypasses the transversal/Gap-A structure entirely and instead seeks ANY integer-valued monotone statistic on the greedy sequence (the gap bound $d_n\le M_1$ is the analog of $a_k\le k$). Candidate statistic: $b_n=\lfloor(a_n-a_1)/M_1\rfloor$ or a running residue-class density. If a non-trivial integer monovariant exists, eventual periodicity of $d_n$ follows directly. **Flag for the outliner as a rival approach distinct from the |P_1| induction.**
3. **`aimo-0231`-STYLE CRT LIFTING (inductive step template).** The crux of `aimo-0231` (modular-arithmetic-and-CRT): the first-return time of an iterated map mod $N$ decomposes as $\text{lcm}$ over prime-power factors via CRT, and lifting from $p^{e-1}$ to $p^e$ grows the return time by at most a factor $p$. **This is the cleanest template for the inductive step** (lifting periodicity from $|P_1|=k-1$ to $|P_1|=k$ via CRT over the new prime's modulus). The obstruction: in our problem the "map" is the greedy successor, not a polynomial iterate, and CRT doesn't cleanly apply because the admissibility constraints couple all primes simultaneously. But the structural idea — bound the period growth per added prime — is the right shape.
4. **$|P_1|=3$ "EXTENSION" ANALYSIS.** Empirically, for $a_1=385=5\cdot 7\cdot 11$, $L(385)=L(35)\cdot 11\cdot 19$. The "extra" factor beyond the new $P_1$ prime ($11$) is one new gov prime ($19$). Across $|P_1|=3$ cases I tested (105, 1001, 1309, 2485, 7429), the non-$P_1$ gov primes are $\subseteq\{2,3\}$ EXCEPT for $a_1=385$ which pulls in $19$. So $|P_1|=3$ is mostly easier than $|P_1|=2$ (smaller non-$P_1$ gov set); $385$ is the outlier. A direct characterization of WHEN $|P_1|=3$ pulls in a "large" new gov prime would be a stepping stone.

## Candidate technique(s)
- **Structural induction on $|P_1|=|S(a_1)|$** with `lock-lemma` as base. The route's spine.
- **Integer-valued monotone statistic → eventual constancy** (`aimo-0134` crux): a different framing that does NOT go through transversals.
- **CRT-based period lifting** (`aimo-0231` crux): template for the inductive step.
- **Density argument for the $|P_1|=2$ NON-LOCK case**: $2$-multiples at density $1/2$ dominate after $n=2$.

## Cheap-kill candidates
- **$|P_1|=2$ NON-LOCK: prove the new gov primes are bounded by an absolute function of $\max P_1$ or by $M_1$.** Empirically true; a clean density argument may close it.
- **The "else LOCK" recursion for $|P_1|=2$** (per round-2 descent-rank explorer): if the larger $P_1$-prime $q$ never recurs, every term is a $p_{\rm sm}$-multiple $\Rightarrow$ lock. **This IS a theorem for $|P_1|=2$** (subsumed by lock-lemma). For $|P_1|\ge 3$ no mechanism. Do NOT use for $|P_1|\ge 3$.
- **LOCK coverage extension**: classify exactly which $a_1=p^k q$ lock. The classification is non-trivial (e.g. $175=5^2\cdot 7$ does NOT lock, $275=5^2\cdot 11$ does, $135=3^3\cdot 5$ does not, $189=3^3\cdot 7$ does). Pattern (conjecture): lock occurs iff a power $p^j$ is reachable before a "blocking" non-$p$-multiple term appears; the blocking structure depends on $q+1$'s factorization. Not a clean closed form.

## Knowledge-base entries to use
- **Invariants & monovariants** (KB): the eventual-constancy-via-integer-monovariant template (`aimo-0134`).
- **Modular arithmetic, CRT** (KB): the period-lifting template (`aimo-0231`).
- **Pigeonhole / extremal principle** (KB): finite-state-via-finite-statistic.
- **Vieta jumping / infinite descent** (KB): the minimal-criminal framing (already tried via the strip; certified dead via `lemma-C-strip-no-go` — do NOT re-attempt the strip in this framing).

## Analogous past problems (cruxes)
- **`aimo-0134`** (Netherlands, NT/sequences-and-recurrences) — **strongest analogue for opening 2.** Crux: "Replace a sequence by the integer-valued running average of its partial sums, and use integrality to upgrade a strict inequality on the average into a weak monotonicity that forces eventual constancy." Then "Recover an original term from consecutive values of the partial-sum running average via a difference identity, to transfer eventual-constancy of the average back to the original sequence." The shape is exactly: bounded-gap greedy sequence $\to$ integer statistic $\to$ monotonicity $\to$ eventual constancy $\to$ transfer back. **The greedy rule $a_{n+1}=\min\{m>a_n:\text{admissible}\}$ with $d_n\le M_1$ is the analog of $a_k\in[0,k-1]$ with $a_k=$ the unique value making the partial sum divisible by $k$.** Adaptation target: find an integer-valued statistic $b_n$ on $(a_n)$ that is monotone bounded. This is genuinely different from the transversal route.
- **`aimo-0231`** (NT/modular-arithmetic-and-CRT) — **analogue for opening 3 (inductive lifting).** Crux: "Decompose the first-hitting-time of an iterated map mod $N$ as the lcm, over the prime-power factors of $N$, of the first-hitting-times modulo each prime power" + "Bound how much an iteration's first-return-to-0 time can grow when the modulus is lifted from $p^{e-1}$ to $p^e$ by counting the residues mod $p^e$ that reduce to 0 mod $p^{e-1}$" (grows by at most factor $p$). Analogue: lift periodicity from $|P_1|=k-1$ to $|P_1|=k$ via CRT; bound the period growth per added prime. The obstruction: greedy successor is not a polynomial iterate, and admissibility couples primes.
- **`aimo-0098`** (Netherlands, NT/divisibility-and-gcd) — **analogue for the LOCK base case.** Crux: "When the defining relation only promises SOME prime divisor satisfies it, evaluate at prime powers (where the prime divisor is unique) to turn the existential into a forced equation." This is exactly the LOCK lemma's logic: at a prime-power term, the prime is unique, admissibility forces divisibility. The second crux "Induct on $\Omega(n)$ to extend from prime powers to all integers, the chosen prime being harmless" — **this is the structural-induction-on-$|P_1|$ idea** — BUT the "harmless choice" property FAILS in our problem (extension qualitatively changes admissibility; see negative finding). So `aimo-0098` validates the LOCK base but its inductive crux does NOT port.
- No crux corpus entry directly treats gcd-greedy-minimal-transversal structure; the matches above are on the *greedy/integer-monovariant/inductive-lifting* moves, not the hypergraph framing. Do not force a hypergraph analogue.

## Prior progress
- **Certified reusable (importable into this route):** `lock-lemma` (the base case, prime-power term $\Rightarrow T=1,L=p$), `linchpin-and-gap-bound` ($d_n\le M_1$, linchpin), `pairwise-intersecting-supports`, `every-term-in-binfinity`, `greedy-equals-cyclic-successor` (Gap B closed unconditionally), `cyclic-successor-bijection` (endgame, conditional on Gap A), `distinct-supports-stabilize` + `mt-depends-on-set-system` (the Gap-A→periodicity bridge).
- **Whole theorem still reduced to Gap A** (finiteness of governing primes / $\mathcal B_\infty$ $L$-periodic).
- Three attack mechanisms on Gap A certified dead (strip/monovariant/density); this route's $|P_1|=2$ specialization is a FOURTH angle on Gap A, not a bypass. The genuinely-different bypass is opening 2 (`aimo-0134` integer-monovariant), NOT the |P_1| induction per se.

## Dead ends (do not retry)
- **The naive "drop a prime $r$" reduction**: the not-$r$ sub-sequence does NOT match $\text{greedy}(a_1/r)$, and the $r$-divisible sub-sequence/r doesn't either. Verified for $a_1=385$, $r=11$. There is no simple quotient map.
- **"$v_r(a_n)$ stabilizes ⇒ descent"**: valuations are bounded but FLUCTUATE in the tail (verified for $a_1=385$ over 1200 terms; $v_5,v_7,v_{11},v_{19}$ all take multiple values in the late tail). No stabilization.
- **The `aimo-0030` prime-factor strip** (certified dead, `lemma-C-strip-no-go`): do NOT re-attempt in the $|P_1|=2$ specialization — the same admissibility-transfer obstruction will re-appear (the strip is a Gap-A mechanism regardless of $|P_1|$).
- **Absolute-constant bound on non-$P_1$ gov primes for $|P_1|=2$**: FALSE. $a_1=847=7\cdot 11^2$ has gov prime $41$; $a_1=175=5^2\cdot 7$ has gov prime $13$. The bound $q\le M_1=\operatorname{rad}(a_1)$ is the right (looser) target, NOT an absolute constant.
- **The "else LOCK" recursion for $|P_1|\ge 3$** (round-2 descent-rank): invalid; a $P_1$-prime can go silent for hundreds of terms without forcing a lock ($a_1=2085$: prime $139$ silent ~180 terms, no lock through 6000 terms).

## Small-case / intuition notes (CONJECTURES, labeled)

### $|P_1|=2$ NON-LOCK period data (all verified by ≥1500-match window)

| $a_1$ | factorization | $T$ | $L$ | non-$P_1$ gov primes |
|---|---|---|---|---|
| 15 | $3\cdot 5$ | 8 | $2\cdot3\cdot5$ | $\{2\}$ |
| 35 | $5\cdot 7$ | 34 | $2\cdot3\cdot5\cdot7$ | $\{2,3\}$ |
| 65 | $5\cdot 13$ | 58 | $2\cdot3\cdot5\cdot13$ | $\{2,3\}$ |
| 77 | $7\cdot 11$ | 18 | $2\cdot7\cdot11$ | $\{2\}$ |
| 91 | $7\cdot 13$ | 20 | $2\cdot7\cdot13$ | $\{2\}$ |
| 143 | $11\cdot 13$ | 64 | $2\cdot3\cdot11\cdot13$ | $\{2,3\}$ |
| 221 | $13\cdot 17$ | 334 | $2\cdot3\cdot5\cdot13\cdot17$ | $\{2,3,5\}$ |
| 437 | $19\cdot 23$ | 160 | $2\cdot5\cdot19\cdot23$ | $\{2,5\}$ |
| 667 | $23\cdot 29$ | 542 | $2\cdot3\cdot5\cdot23\cdot29$ | $\{2,3,5\}$ |
| 1147 | $31\cdot 37$ | 68 | $2\cdot31\cdot37$ | $\{2\}$ |
| 1517 | $37\cdot 41$ | 190 | $2\cdot3\cdot37\cdot41$ | $\{2,3\}$ |
| 1763 | $41\cdot 43$ | 1342 | $2\cdot3\cdot7\cdot41\cdot43$ | $\{2,3,7\}$ |
| 2491 | $47\cdot 53$ | 100 | $2\cdot47\cdot53$ | $\{2\}$ |
| 175 | $5^2\cdot 7$ | 274 | $2\cdot3\cdot5\cdot7\cdot13$ | $\{2,3,13\}$ |
| 847 | $7\cdot 11^2$ | 1744 | $2\cdot3\cdot7\cdot11\cdot41$ | $\{2,3,41\}$ |

**Conjecture (empirical, $|P_1|=2$ NON-LOCK):** every governing prime $q$ satisfies $q\le M_1=\operatorname{rad}(a_1)$. Holds in all 15+ tested cases; the absolute-constant strengthening is FALSE ($41$ from $a_1=847$). The non-$P_1$ gov set is typically $\subseteq\{2,3,5,7\}$ but can include $13$ ($a_1=175$), $19$ ($a_1=385$, $|P_1|=3$), $41$ ($a_1=847$).

### $|P_1|=3$ period data
| $a_1$ | $T$ | $L$ | non-$P_1$ gov |
|---|---|---|---|
| 105=$3\cdot5\cdot7$ | 58 | $2\cdot3\cdot5\cdot7$ | $\{2\}$ |
| 385=$5\cdot7\cdot11$ | 5088 | $2\cdot3\cdot5\cdot7\cdot11\cdot19$ | $\{2,3,19\}$ |
| 1001=$7\cdot11\cdot13$ | 282 | $2\cdot7\cdot11\cdot13$ | $\{2\}$ |
| 1309=$7\cdot11\cdot17$ | 912 | $2\cdot3\cdot7\cdot11\cdot17$ | $\{2,3\}$ |
| 7429=$17\cdot19\cdot23$ | 2268 | $2\cdot3\cdot17\cdot19\cdot23$ | $\{2,3\}$ |
| 2485=$5\cdot7\cdot71$ | 28 | $2\cdot3\cdot5\cdot7$ | $\{2,3\}$ |

**Conjecture:** $|P_1|=3$ non-$P_1$ gov $\subseteq\{2,3\}$ EXCEPT for $a_1=385$ (pulls in $19$). $385$ is the systematic outlier across rounds.

### LOCK coverage for $|P_1|=2$ (empirical)
- $a_1$ even $\Rightarrow$ LOCK at $L=2$ (always; covered by `lock-lemma`).
- $a_1=p^k q$ with $p<q$ and $p=2$ $\Rightarrow$ LOCK at $L=2$.
- $a_1=p\cdot q$ ($p=3$, $q\in\{5,7,11,13,\dots\}$): some lock (e.g. $21=3\cdot7\to L=3$, $33=3\cdot11\to L=3$), some don't ($15=3\cdot5$ NON-LOCK). The lock occurs iff $p^j$ is reached before a blocking term; mechanism unclear.
- $a_1=p^k q$ with $p$ odd smaller: some lock ($275=5^2\cdot11$, $325=5^2\cdot13$, $189=3^3\cdot7$, $63=3^2\cdot7$, $605=5\cdot11^2$), some don't ($175=5^2\cdot7$, $245=5\cdot7^2$, $539=7^2\cdot11$, $637=7^2\cdot13$, $847=7\cdot11^2$, $135=3^3\cdot5$). **No clean closed-form classification found.**

### Where the route re-encounters Gap A
The $|P_1|=2$ NON-LOCK case re-encounters Gap A **at the step "bound which primes enter as governing."** Concretely: after $2$ enters at $n=2$ (provable), the active primes are $\{2,p_{\rm sm}\}\cup$ (factors of $q+1$); subsequent witnesses pull in new primes via cofactor structure (e.g. for $a_1=385$, $a_5=399=3\cdot7\cdot19$ pulls in $19$ as the cofactor of the smallest $7$-multiple above $396$). Bounding these cofactor-primes IS Gap A — the $|P_1|=2$ constraint narrows the wall but does not remove it. The naive "drop-$r$ sub-sequence" reduction does NOT provide a non-circular descent.

## Concrete recommendation for the outliner

**Open a `|P_1|=2-NON-LOCK-direct` approach** with the following skeleton (hard steps flagged):
1. **Reduce to $|P_1|=2$ NON-LOCK.** LOCK case (covered by `lock-lemma`) handles all $a_1$ even and all reachable-prime-power cases. WLOG $a_1=pq$ or $p^k q$ ($p$ odd smaller), no prime power reached. **[EASY — uses certified `lock-lemma`]**
2. **Prove $a_2=a_1+p_{\rm sm}$ is even, so $2$ enters at $n=2$.** **[EASY — elementary, see proof above]**
3. **Bound the new governing primes in the $|P_1|=2$ NON-LOCK regime.** Target: $q\le M_1=\operatorname{rad}(a_1)=p_{\rm sm}\cdot p_{\rm lg}$ (the existing empirical conjecture, specialized). The lever: $2$-multiples at density $1/2$ dominate. **[HARD — this is Gap A specialized to $|P_1|=2$; the strip is dead, need a NEW mechanism. Candidate: density of $2$-multiples + cofactor analysis of witnesses]**
4. **Lift to general $|P_1|$ via CRT (the `aimo-0231` template).** **[HARD — no clean quotient map found; the inductive step is the route's main obstruction. Flag as the load-bearing gap.]**

**OR (preferred, genuinely different framing): open a `integer-monovariant` approach** based on `aimo-0134` — seek ANY integer-valued monotone bounded statistic on $(a_n)$ (using $d_n\le M_1$ as the range bound), conclude eventual constancy, transfer back to $d_n$. This bypasses the transversal framework entirely AND does not require the inductive step. **Flag for the outliner as the higher-priority rival; the |P_1| induction is a fallback if the |P_1|=2 step 3 can be closed.**

**Obstruction verdict on the |P_1| induction as a STANDALONE route:** the inductive step (step 4) has no clean mechanism. The route's value is (a) the certified LOCK base, (b) the $|P_1|=2$ specialization narrowing Gap A, and (c) the `aimo-0134` / `aimo-0231` crux pointers. It should be opened as an approach with step 3 as the load-bearing hard step and step 4 declared as a conditional gap, NOT as a complete standalone proof.
