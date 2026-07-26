# Round 4 proof-builder report — `minimal-criminal-schur-contradiction`

## What I proved

**Steps 1–6 (the minimal-criminal setup) — SOUND and rigorous.** Assuming Gap A fails, well-ordering gives a smallest governing prime $q > M_1 = \operatorname{rad}(a_1)$. By minimality, primes in $(M_1,q)$ are MT-transient. $q$ governs $\Rightarrow$ $q\mid a_n$ for infinitely many $n$ (via `binfinity-divisibility-progression-structure`). At each $q$-multiple index, the gap bound $d_{n-1}\le M_1 < q$ forces $a_{n-1}\bmod q \in [q-M_1, q-1]$ and $d_{n-1} = q-(a_{n-1}\bmod q)$. The cofactor $k_i = a_{n_i}/q$ has its prime factors transversing the prior non-$q$-multiple supports (greedy admissibility + the $q$-/$q$-free split). $P_1$ always provides a small-prime transversal (linchpin). None of this invokes the certified-circular cofactor bound. The setup is genuinely new (not in the 10+ dead list) and reusable as a mount point for any future Step 7 mechanism.

**Step 7 (the contradiction) — NEGATIVE RESOLUTION: the Schur/`aimo-0727` sub-route is certified dead, by three independent obstructions.**

- **(A1) The `aimo-0727` engine is absent.** The crux's load-bearing mechanism is the multiplicative recurrence $a_{k+1}\mid a_k(b_k+2)$, which confines new prime factors of $a_{k+1}$ to divisors of $a_k$ or of $b_k+2$ (bounded). Here consecutive cofactors are related additively ($k_{i+1}-k_i = (\text{sum of }d\text{'s})/q$), with no confining recurrence. Verified: ratios $k_{i+1}/k_i$ range over $[1.04,1.33]$ for $a_1=15,q=3$, no pattern.
- **(A2) The contrapositive is false in general.** Schur's theorem (forward: non-constant polynomial $\Rightarrow$ infinitely many prime divisors) yields the contrapositive "fixed finite prime set $\Rightarrow$ bounded" ONLY for polynomial-driven sequences. For arbitrary sequences the implication is false: $k_i = 2^i$ has prime set $\{2\}$ yet is unbounded. The greedy cofactor sequence is not polynomial-driven (no recurrence, per A1).
- **(A3) The Schur premise is provably FALSE in the periodic regime — the very regime the theorem establishes.** Once $a_{n+T}=a_n+L$ with $q\mid L$, the $q$-multiples at each residue class $r\bmod T$ form an AP $a_r + jL$, so the cofactors $k_j = a_r/q + j(L/q)$ are an AP with positive common difference $L/q$. An unbounded AP has infinitely many prime divisors (smooth-number density: $P$-smooth numbers $\le X$ are $O((\log X)^s)$, but the AP contributes $\Omega(X)$ values $\le X$). So the cofactor prime set is INFINITE — the opposite of "fixed finite." Empirically ($a_1=15$, $T=8$, $L=30$, $q=3$): distinct primes $>M_1=15$ in cofactors grow without bound (59 at 500 terms $\to$ 516 at 6000; max 2477).

**The rescue also fails:** MT-transient $\not\Rightarrow$ cofactor-transient. In the $a_1=15$ periodic case the MT has stabilized from $n=0$ (governing $\{2,3,5\}\le M_1$), every prime $>15$ is MT-transient from the start, yet 361 distinct such primes appear in cofactors AFTER stabilization. A prime redundant in the eventual MT can still divide infinitely many terms of the linearly-growing sequence.

**Candidate B (local-walk periodicity mod $q$) — dead.** $a_n\bmod q$ is not a closed finite state (round-3 finite-statistic explorer: 89 conflicts for $a_1=385$ on $\bmod M_1$); no periodicity-mod-$q$ argument mounts, and `syndetic-divisible-closed-not-periodic` fences pure-statics.

## Gaps remaining

**Step 7 has no viable contradiction mechanism in this framing.** The Schur sub-route is certified dead (A1–A3); Candidate B is dead; no further candidate is apparent. The setup (Steps 1–6) is sound but does not close Gap A. The approach is therefore **partial**, with the open gap precisely: "find a contradiction mechanism (not Schur, not cofactor-bound, not pure-static, not mod-$q$ finite-state) that mounts on the minimal-criminal setup."

## Lemma proposed for certification

**`schur-cofactor-premise-fails-in-periodic-regime`** (negative, conditional on Gap A). *Statement.* In any eventually-periodic greedy sequence ($a_{n+T}=a_n+L$, $q$ governing, $q\mid L$), the cofactors $k_i = a_{n_i}/q$ form a finite union of APs with positive common difference $L/q$, hence have infinitely many prime divisors (smooth-number density). Therefore the Schur/`aimo-0727` premise "cofactors have eventually fixed-finite prime set" is provably false in the periodic regime. Moreover MT-transient $\not\Rightarrow$ cofactor-transient (a prime redundant in $\operatorname{MT}(\mathcal F_\infty)$ can divide infinitely many $a_n$). *Consequence:* no Schur-style cofactor-prime-finiteness contradiction can close Gap A on the minimal-criminal setup. Proved in `results/imo-2026-06/approaches/minimal-criminal-schur-contradiction.md`, Step 7 (A3) + the MT-transient discussion. This is the round-4 outline-reviewer's mandated fallback (certifying a negative lemma fencing the framing), and it is genuine progress on a problem where 10+ mechanisms are already dead.

## Empirical work (all claims tested before asserting)

- Cofactor prime factors for $a_1=15, q=3$ reach 2477 (max over 6000 terms); 280/450 $q$-multiples (over 600) have a cofactor-prime $> M_1=15$. Reviewer's "241, 136/242" confirmed and sharpened.
- $a_1=15$ is periodic from $n=0$: $T=8$, $L=30=2\cdot3\cdot5$, $M_1=15$. Governing primes $\{2,3,5\}\le M_1$ (conjecture holds).
- Cofactors at each residue class $r\bmod 8$ with $q=3 \mid a_r$ form AP $k = (5,6,8,10,12,14) + 10j$ (common difference $10 = L/q$). Verified all six APs.
- Distinct big primes ($>15$) in cofactors grow linearly with horizon: 59, 108, 198, 361, 516 at 500, 1000, 2000, 4000, 6000 terms — consistent with infinitely many prime divisors.
- $a_1\in\{847,1309\}$ cross-checked: cofactor primes exceed $M_1$ when $q$ is small relative to $M_1$ (e.g. $a_1=847=7\cdot11^2$, $q=7$, $M_1=77$: cofactor primes reach 523, 152/510 with big-prime). When $q$ is close to $M_1$ ($a_1=1309, q=7, M_1=1309$; $a_1=385, q=11, M_1=385$), cofactors stay $\le M_1$ but still form unbounded APs with infinitely many prime divisors (the density argument is regime-independent).

## crux port assessment (per CLAUDE.md — every borrowed step assessed)

- **`aimo-0727` (Netherlands, Schur cofactor-finiteness): DOES NOT PORT.** The crux has three sub-moves; the one the outliner invoked ("bounded cofactor $\Rightarrow$ finite prime set $\Rightarrow$ contradiction with infinite-prime-divisors hypothesis") is the FORWARD direction and is in the wrong direction for our contrapositive need. Its confining engine (multiplicative recurrence $a_{k+1}\mid a_k(b_k+2)$) is ABSENT in the greedy cofactor sequence (additive relation, no recurrence). The contrapositive ("fixed finite prime set $\Rightarrow$ bounded") is false for non-polynomial sequences ($k_i=2^i$). And the premise is provably false in the periodic regime (A3). This is the same lesson as round 3 (`aimo-0231` lift = trivial identity; `aimo-0134` shrinking range absent): the crux's load-bearing mechanism is problem-specific and does not survive the port. Honest assessment: dead, fenced by the proposed negative lemma.

## Self-assessment

The minimal-criminal setup is sound and genuinely new, but the Schur contradiction is certified dead by three independent obstructions and no alternative sub-route is available. This is the outline-reviewer's mandated negative-lemma fallback — the framing is fenced off, which is genuine progress on a deeply stalled problem (11+ mechanisms now dead). The setup itself (Steps 1–6) remains a reusable mount point for any future non-Schur contradiction mechanism on the smallest governing $q > M_1$.

verdict-request: CHANGES REQUESTED
