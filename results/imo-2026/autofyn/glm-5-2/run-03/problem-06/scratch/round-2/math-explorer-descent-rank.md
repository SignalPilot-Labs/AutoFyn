# imo-2026-06 — descent-rank lens (round 2)

Lens: give `growing-modulus-descent` a concrete strictly-decreasing rank, and scout the `prime-power-dichotomy` no-lock "else lock" mechanism. Both scoped to Gap A (finiteness of governing primes).

## (a) Concrete strictly-decreasing rank — **NONE FOUND; approach killed as framed**

### Setup (concrete definitions used)
- Pulled-in prime $q$: $q\notin P_1=S(a_1)$ lying in some $T\in\operatorname{MT}(\mathcal F_n)$ at some $n$.
- Witness type $\tau(q)=(A(q),B(q))\in 2^{P_1}\times 2^{P_1}$ (the gap-f form), where $A(q)=\{S(a_i)\cap P_1: a_i$ is a private witness of $q$ in some $T\ni q\}$ and $B(q)=\{p\in P_1: \exists T\in\operatorname{MT}(\mathcal F_n),\, q\in T,\, p\notin T\}$. Both finite.
- Pull-in event at step $n$: $q$ enters $\bigcup\operatorname{MT}(\mathcal F_n)$ for the first time.
- Candidate ranks at the moment of pull-in: $r_1$=#$\{T\in\operatorname{MT}(\mathcal F_n):q\in T\}$; $r_2$=#distinct-supports that $q$'s $T$'s must hit (i.e. supports not hit by any $T\setminus\{q\}$); $r_3=\#\operatorname{MT}(\mathcal F_n)$.

### Computation table ($a_1\in\{385,77,715,1309,2431\}$, MT enumerated by size-$\le 5$ hitting sets)

**$a_1=385=5\cdot7\cdot11$, $M_1=385$:** pulled-in events
| n | q | A | B | r1 | r2 | r3 | #supp | #MT |
|---|---|---|---|---|---|---|---|---|
| 2 | 2 | {5} | {5,7,11} | 2 | 1 | 7 | 2 | 7 |
| 2 | 3 | {5} | {5,7,11} | 2 | 1 | 7 | 2 | 7 |
| 2 | 13 | {5} | {5,7,11} | 2 | 1 | 7 | 2 | 7 |
| 5 | 19 | {7} | {5,7,11} | 2 | 1 | 8 | 5 | 8 |
Final MT (n=50): `{{2,7},{2,3,5},{2,3,11},{2,11,19},{3,7,11},{3,7,19},{5,7,11}}`, primes $\{2,3,5,7,11,19\}$. Note 13 was **transient** (pulled in at n=2, gone by n=38).

**$a_1=715=5\cdot11\cdot13$, $M_1=715$ (LOCKS at n=483, $a_{483}=3125=5^5$):** type $(A=\{5\},B=\{5,11,13\})$ has **8 events**:
| n | q | r1 | r3 |
|---|---|---|---|
| 2 | 2 | 2 | 5 |
| 2 | 3 | 2 | 5 |
| 3 | 29 | 4 | 5 |
| 4 | 73 | 2 | 5 |
| 5 | 7 | 2 | 7 |
| 6 | 37 | 2 | 7 |
| 7 | 149 | 6 | 7 |
| 9 | 151 | 4 | 5 |
$r_1$ seq $=[2,2,4,2,2,2,6,4]$ — **non-monotone, INCREASES**. $r_2\equiv1$. $r_3=[5,5,5,5,7,7,7,5]$ fluctuates.

**$a_1=1309=7\cdot11\cdot17$, $M_1=1309$:** type $(A=\{7\},B=\{7,11,17\})$ has 4 events: $r_1=[2,2,2,4]$ (increases), $r_2\equiv1$, $r_3=[5,5,12,12]$.

**$a_1=2431=11\cdot13\cdot17$, $M_1=2431$:** type $(A=\{13\},B=\{11,13,17\})$ has 5 events: $r_1=[3,4,4,4,4]$ (increases), $r_2\equiv1$, $r_3=[9,12,17,17,13]$.

### Why no rank can work (the structural obstruction)
1. **$r_2\equiv1$ always** (structural, not coincidence): at the moment $q$ is first pulled in, $q$ is the unique new hitter of exactly ONE support — the support $S(a_n)$ that introduced it. So $r_2$ is a constant, useless.
2. **$r_1,r_3$ are non-monotone and often INCREASE** (715: $r_1$ goes $2\to4\to2\to6\to4$; 1309: $2\to2\to2\to4$). No strictly-decreasing property.
3. **The $(A,B)$ type is intrinsically too coarse.** At $a_1=385$, primes $2,3,13$ are pulled in **simultaneously at n=2** with **identical** type $(A=\{5\},B=\{5,7,11\})$ and identical ranks. No rank can strictly order simultaneous same-type events. I verified the finer type $\{(p,S(a_i)\cap P_1):\ldots\}$ from the approach file — it is ALSO identical for $2$ and $3$ at n=2 (both yield $\{(5,\{5\}),(7,\{5\}),(11,\{5\})\}$), so refining the type within the $P_1$-interaction family does not help.
4. **The $L$-construction is doubly flawed**: it enlarges $L$ for EVERY pulled-in prime including transient ones (13 at 385, 37/47 at 1309, 29/73/149/151 at 715 all drop out). The correct modulus uses only the stable MT primes. So $L_k=\prod L_{k-1}\cdot q$ over-counts.

**Verdict: KILL `growing-modulus-descent` as framed.** No concrete strictly-decreasing rank exists for the $(A,B)$ witness type; the approach collapses to the same finiteness wall (Gap A) as `transversal-saturation` with no independent descent mechanism. The "vague descent is the failure mode" — confirmed.

## (b) No-lock recursion ("every $P_1$-prime recurs, else lock") — mechanism INVALID, but lemma SUPPORTED

The round-1 `prime-power-dichotomy` "else lock" mechanism (a $P_1$-prime $p$ stops recurring $\Rightarrow$ lock) was refuted by the reviewer. My scan confirms the refuted mechanism but finds the **lemma itself holds** (no counterexample), via a DIFFERENT mechanism than "else lock".

### Computation (scan $a_1\in[6,3000]$, non-prime-power, $K=250$ terms)
- 1162 LOCK cases (prime power appears within 250 terms).
- 1371 no-lock cases (no prime power in 250 terms). Of these, 1013 have ALL $P_1$-primes recurring in the 2nd half; 358 flagged as "dropouts."
- **All 358 "dropouts" are false signals**, two kinds:
  - **$|P_1|=2$ de-facto locks** ($a_1=514=2\cdot257$, $753=3\cdot251$, $771=3\cdot257$, ...): the small prime divides every term (spacing = small prime), the large prime appears only in $a_1$, and the lock prime power appears LATE — $514$ locks at $a_{256}=2^9=512\cdot2$ wait actually $2^{10}=1024$? Concretely $514\to$ locks at term #256 ($2^8$-related); $753$ at #479; $1042$ at #504. So "no prime power in 250 terms" was just insufficient horizon.
  - **$|P_1|\ge3$ sparse recurrence** ($a_1=2085=3\cdot5\cdot139$): the large prime 139 was flagged "dropped" because it was absent from terms 125–250, but running to 1500 terms shows 139 **recurs 12 times** (terms 1,93,276,459,550,642,823,915,1006,1188,...). The recurrence is just sparse; the short-window check was a false negative.

So: **the lemma "in the no-lock regime, every $p\in P_1$ recurs" is SUPPORTED across all tested $a_1$ (zero real counterexamples).** But the round-1 *mechanism* ("else lock" — terms avoiding $p$ shrink to a singleton support $\Rightarrow$ lock) is still invalid: a $P_1$-prime can go silent for hundreds of terms without forcing a lock (2085: 139 silent for ~180 terms between appearances, no lock through 6000 terms).

### The real mechanism for $|P_1|=2$ dropouts (clean, provable)
If $P_1=\{p_{\rm sm},p_{\rm lg}\}$ with $p_{\rm sm}<p_{\rm lg}$ and $p_{\rm lg}$ never recurs: $a_2$ is the smallest $m>a_1$ sharing a prime with $a_1$. The next multiple of $p_{\rm sm}$ is $a_1+p_{\rm sm}$ (admissible, shares $p_{\rm sm}$); any non-$p_{\rm sm}$-multiple must share $p_{\rm lg}$ with $a_1$, requiring $m\ge a_1+p_{\rm lg}\gg a_1+p_{\rm sm}$. So $a_2$ is a $p_{\rm sm}$-multiple. Inductively every term is a $p_{\rm sm}$-multiple $\Rightarrow$ lock at $L=p_{\rm sm}$. This is exactly the even-$a_1$ lock (Lemma 9/Cor. 10) generalized. So for $|P_1|=2$, "dropout $\Rightarrow$ lock" is a theorem via the density argument — but it gives Gap C only for $|P_1|=2$, and all $|P_1|=2$ cases are either lock or the dropout-implies-lock; the no-lock $|P_1|=2$ regime has both primes recurring (e.g. $a_1=77=7\cdot11$: both 7 and 11 recur; MT stabilizes $\{2,7\},\{2,11\},\{7,11\}$).

### For $|P_1|\ge3$: no dropouts observed, but no mechanism proven
In 694 no-lock $|P_1|\ge3$ cases, ZERO have a $P_1$-prime that fails to recur (with adequate horizon). So "every $P_1$-prime recurs" is empirically true for $|P_1|\ge3$, but I found no proof mechanism. The naive induction "if one drops, the rest cover, and inductively one of them locks" fails: the historical terms (those sharing the dropped prime) keep imposing constraints that prevent a clean restart.

**Recommendation for the no-lock branch:** do NOT pursue the "else lock" recursion — it gives Gap C only for $|P_1|=2$ (already covered by the lock lemma). For $|P_1|\ge3$ it has no mechanism. The cleaner route to Gap A is the **MT-prime bound** $q\le M_1$ (see below).

## Bonus finding: the MT-prime bound $q\le M_1$ is the live route (confirms reviewer, refines the claim)

### $a_1=2085=3\cdot5\cdot139$ — the crucial slow case (NEW)
This is the case that DISTINGUISHES term-primes from MT-primes:
- $M_1=2085$. **Term-primes EXCEED $M_1$**: primes 2087, 2089, 2099, 2111, ..., up to 2621 appear in the terms; 378 distinct non-$P_1$ primes appear by n=3000. So any bound on TERM primes is FALSE.
- **But MT-primes stay bounded**: $\operatorname{MT}(\mathcal F_n)$ stabilizes at $n=60$ to 5 transversals with prime set $\{2,3,5,11,19\}$, all $\le M_1$. Verified at n=60,80,100,150,200,500,1000,2000 — the set $\{2,3,5,11,19\}$ remains a transversal (every distinct support contains one of these primes) throughout. (At n$\ge$500 it ceases to be MINIMAL — the true MT shrinks further — but the prime set never grows.)
- The sequence is near-lock at 3 (998/1000 last terms divisible by 3; gaps mostly 3 and 6) but a sparse non-3 term every ~500 steps blocks $3^9=19683$ (skipped at n=3852: $a_{3851}=19680,a_{3852}=19686$). Distinct supports grow LINEARLY (2320 at n=6000) — these are the long period's supports, NOT a sign of aperiodicity; the MT stabilized long ago.
- Primes 13, 37, 47, 139 were pulled in early then DROPPED OUT of MT by n=60 — further evidence the descent approach's "enlarge $L$ for every pulled-in prime" is wrong.

### MT-prime bound $q\le M_1$ verified across 24 no-lock $a_1$
For each of $\{385,77,1309,2431,105,165,455,1001,777,2925,1365,1785,2145,2805,3135,3465,2085,...\}$ (all no-lock, n=60), every prime in $\bigcup\operatorname{MT}(\mathcal F_{60})$ is $\le M_1=\operatorname{rad}(a_1)$. **Zero violations.** The MT-prime set is always a tiny subset of $\{p:p\le M_1\}$, typically $\{2,3\}\cup P_1$ plus one or two small primes (often 7, 11, 13, 19). This is the live route to Gap A: prove the MT-prime set is bounded by $M_1$.

### The mechanism for the MT-prime bound (observed, not proven)
For 2085: once $\{2,3,5,11,19\}$ became a transversal (n=60), EVERY subsequent support $S(a_n)$ contains at least one of these primes. Why? The greedy picks $a_{n+1}=\min(\mathcal B_n\cap(a_n,\infty))$; once the MT stabilizes, $\mathcal B_n=\mathcal B_\infty$ is $L$-periodic and the greedy's picks all lie in $\mathcal B_\infty$, whose members are hit by the stable MT. This is the **self-sustaining stabilization**: a stable transversal $G$ forces all future terms to be hit by $G$ (since future terms lie in $\mathcal B_\infty=\bigcup_{T\subseteq G}\{\text{multiples of }\operatorname{rad}(T)\}$... ). The bootstrapping step — proving $G$ forms in the first place within primes $\le M_1$ — is the actual Gap A wall. The data says $G\subseteq\{p\le M_1\}$ always; proving it is the open problem (the reviewer's "most promising direction," confirmed correct and now sharpened: it is a bound on MT-primes, NOT term-primes).

## Distinct openings (for the outliner)
1. **Prove the MT-prime bound $q\le M_1$** (the reviewer's direction, correctly scoped to MT primes). Mechanism to develop: the self-sustaining stabilization — show that once a transversal $G\subseteq\{p\le M_1\}$ forms, all future supports are hit by $G$, and the formation of $G$ itself uses only primes $\le M_1$ via the gap bound $d_n\le M_1$ (every candidate in the window $[a_n,a_n+M_1]$ is hit by $P_1$, and the minimal transversals refine within $\{p\le M_1\}$). This closes Gap A directly.
2. **A genuinely different framing (per the 3+ round plateau rule): periodicity of the residue map on $\mathbb Z/L\mathbb Z$ WITHOUT bounding MT primes.** Since 2085 has MT stable at n=60 with a long period, one could try to prove the greedy map $r\mapsto r'$ on $\mathbb Z/M_1\mathbb Z$ is eventually periodic by a pumping-lemma / Kolmogorov-style finite-state argument on the support-pattern stream, bypassing the explicit MT-prime bound. (Scout only — I did not develop this.)
3. **Retire `growing-modulus-descent` and `free-rider-type-replacement`**; consolidate the field on `transversal-saturation` (Gap A = MT-prime bound) and `prime-power-dichotomy` (LOCK certified; NO-LOCK should redirect to the MT-prime bound, NOT the "else lock" recursion).

## Knowledge-base / crux candidates
- The MT-prime bound route is the same as `transversal-saturation` Step 7's corrected target. The crux corpus (divisibility-and-gcd subtopic) was already scouted round 1; no NEW analogous crux found for the MT-prime bound specifically. The closest structural analog is the self-sustaining fixed-point argument (a stable hitting set absorbing all future sets) — not a standard named crux in the corpus.

## Dead ends (do not retry)
- **`growing-modulus-descent` typed rank descent** (this report): no strictly-decreasing rank exists for the $(A,B)$ type; simultaneous same-type pull-ins and non-monotone $r_1$ kill it. Do NOT retry with a finer $(A,B)$-family type — verified that the finest $P_1$-interaction type still fails to distinguish simultaneous pull-ins.
- **`free-rider-type-replacement` (Gap F)** (round 1, certified dead): same-type replacement is FALSE.
- **`prime-power-dichotomy` "else lock" mechanism** (this report): invalid for $|P_1|\ge3$; only works for $|P_1|=2$ (subsumed by the lock lemma). Do NOT use as the route to Gap C.
- **Any bound on TERM primes** (this report): FALSE — $a_1=2085$ has term-primes up to 2621 $>M_1=2085$. The bound is on MT-primes only.

## Small-case / intuition notes (CONJECTURES, not proved)
- CONJECTURE (strong): for every no-lock $a_1$, $\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}T\subseteq\{p:p\le M_1=\operatorname{rad}(a_1)\}$ for all sufficiently large $n$. Holds in 24+ tested cases. This IS Gap A.
- CONJECTURE: the stable MT-prime set is always a subset of $\{2,3\}\cup P_1\cup\{7,11,13,19\}$-ish (very small). Holds empirically.
- CONJECTURE: in the no-lock regime, every $p\in P_1$ recurs infinitely often. Holds (no counterexample). Implied by (but weaker than) the MT-prime bound.
- $a_1=2085$ is the recommended stress test for ANY approach to Gap A: it has term-primes $>M_1$ (so term-prime bounds fail), long period (so naive period detection fails before n~6000), but MT stabilizes at n=60 (so the MT-prime bound holds). Any proof must distinguish MT-primes from term-primes.
