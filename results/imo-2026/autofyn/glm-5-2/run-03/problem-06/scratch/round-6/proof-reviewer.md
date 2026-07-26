# Round 6 proof-reviewer report — IMO 2026 P6

**Reviewer:** adversarial, independent re-derivation. Re-ran `mt_greedy.py` (bit-exact vs naive $O(N^2)$ gcd-greedy on $a_1\in\{15,385,847\}$, all three match) and the corrected naive gcd-greedy for the $D_n$-slack enumeration. Did NOT use the round-4 `fast_greedy.py` (inverted-subset bug). Period detection used $\texttt{min\_run}\ge 2000$ per the round-5 pitfall rule.

## Task 1 — certify the two new negative structural lemmas

### Lemma 1: `no-fixed-modulus-forward-determinism` — **APPROVE / verified-milestone (Status: sound)**

**The load-bearing claim** (Step 2): in the periodic regime with period $(T,L)$, forward-determinism of $a_n\bmod m$ requires $T\le g:=\gcd(L,m)$ AND pairwise distinctness of $a_0,\dots,a_{T-1}\bmod g$. **Re-derived from scratch independently:** $a_n=a_r+qL$ for $n=qT+r$, so $a_n\bmod m\equiv a_r+qL\pmod m$. Forward-det $\Leftrightarrow$ $[a_r+qL\equiv a_{r'}+q'L\pmod m\Rightarrow r=r']$ $\Leftrightarrow$ (contrapositive, $r\ne r'$) $a_r-a_{r'}\notin\langle L\rangle_m=\{kL\bmod m\}=g\cdot\mathbb Z/m\mathbb Z=\{x:g\mid x\}$ $\Leftrightarrow$ $a_r\not\equiv a_{r'}\pmod g$ for all $r\ne r'$. Pigeonhole: if $T>g$ two residues coincide $\Rightarrow$ conflict. **The derivation reproduces the lemma's boxed condition exactly.** Sound.

**Structural size obstruction (Step 3), $a_1=175$:** $P_1=\{5,7\}$, $M_1=35$, $L=2730=2\cdot3\cdot5\cdot7\cdot13$, $P_1$-part of $L=5\cdot7=35$. For any $k\ge1$, $a_1^k$ is $P_1$-smooth $\Rightarrow$ $\gcd(L,a_1^k)\mid 35<274=T$. Sound, no computation needed. Same argument covers $m=M_1=35$ and $m=a_1\cdot M_1=6125$ (all $P_1$-smooth).

**Reviewer-independent re-run of the conflict table** (`/tmp/verify_conflict2.py`, replicates builder's `conflict_probe.py` method, unordered pairs, $N$ as builder specified):

| $a_1$ | $m$ | $N$ | realized | conflict states | conflict pairs | builder's conflict states | builder's conflict pairs |
|---|---|---|---|---|---|---|---|
| 175 | $a_1^2=30625$ | 50000 | 9625 | **4447** | 116423 | 4447 | 116423 |
| 175 | $a_1=175$ | 50000 | 55 | 40 | 20798505 | 40 | 20798505 |
| 175 | $M_1=35$ | 50000 | 11 | 8 | 103992605 | 8 | 103992605 |
| 77 | $a_1^2=5929$ | 5000 | 1309 | 77 | 992 | 77 | 992 |
| 77 | $a_1=77$ | 5000 | 17 | 1 | 77284 | 1 | 77284 |
| 91 | $a_1^2=8281$ | 5000 | 1729 | 91 | 681 | 91 | 681 |
| 91 | $a_1=91$ | 5000 | 19 | 1 | 62500 | 1 | 62500 |
| 847 | $a_1^2=717409$ | 50000 | 49999 | 0 | 0 | 0 | 0 |

**Every row matches the builder's recomputed table bit-exact.** Periods confirmed: $15\to(8,30)$, $35\to(34,210)$, $77\to(18,154)$, $91\to(20,182)$, $175\to(274,2730)$, $847\to(1744,18942)$.

**On the explorer-vs-builder discrepancy ($3498$ vs $4447$):** the reviewer checked that the two plausible forward-det definitions — $a_n\bmod m\to a_{n+1}\bmod m$ (which the explorer's `forward_det_count` actually computes) vs $a_n\bmod m\to d_{n+1}$ (the lemma's stated definition) — are **equivalent** when $m>M_1$ (because $d_{n+1}\le M_1<m$ so $d_{n+1}\bmod m=d_{n+1}$, and $a_{n+1}\bmod m=(a_n\bmod m)+d_{n+1}\bmod m$ determines and is determined by $d_{n+1}$). Both definitions give $4447$ at $N=50000$. The explorer's $3498$ is therefore a plain under-count from an unreleased ad-hoc probe (the explorer's `ramsey_probe.py` only measures $a_n\bmod a_1$ for $N=6000$, not $a_n\bmod a_1^2$ at $N=50000$). The lemma honestly documents this discrepancy and uses the verified $4447$.

**On the $a_1=847$ "YES" row:** honestly flagged as an undersampling artifact ($a_1^2=717409\gg N=50000$; realized $=N-1=49999$ means no residue has repeated; verifying needs $N>7.2\cdot10^5$; the $a_1=175$ counterexample settles the universal-over-$a_1$ claim negatively; the round-5 T-unbounded fence already handles $a_1=847$ via the rad-77 pair). Honest.

**Scope honesty:** the lemma explicitly limits its structural proof to $P_1$-smooth function-of-$a_1$ moduli (Step 3 "Scope and honesty" admits exotic $m$ with primes outside $P_1$ like $m=a_1+1$ are not structurally proven; only witnessed computationally for $\{77,91\}$ via distinctness). The information-theoretic root-cause (Step 1: $d_{n+1}$ depends on $(a_n,\operatorname{MT}(\mathcal F_n))$, and $a_n\bmod m$ discards the second component) is universal but the existence of conflict pairs is witness-dependent.

**Genuinely new (not subsumed):** the round-5 T-unbounded-in-$M_1$ fence fences every $f(M_1)$-bounded deterministic statistic (state *size* bounded in $M_1$). This lemma fences residue statistics at moduli $m=a_1^k$ that are **NOT** $f(M_1)$-bounded ($a_1=175\Rightarrow a_1^2=30625\gg M_1=35$). Different domain, genuine sharpening. Not a restatement.

**Verdict: APPROVE.** The lemma is certified as a negative/structural fence (the 5th structural fence). Record `verified-milestone`.

### Lemma 2: `D_n-slack-obstruction` — **APPROVE / verified-milestone (Status: sound)**

**The load-bearing claim** (Step 3): at a step with $|D_n|\ge 2$, the greedy minimum is a tie-break, not a forced extremum. Trivial to re-derive: $|D_n|\ge2$ $\Rightarrow$ $\exists d,d'\in D_n$ with $d<d'$, both admissible; greedy picks $d=\min D_n$ solely because $d<d'$ in the natural ordering, NOT because $d$ is the unique admissible increment. The variational "no-improvement $\Rightarrow$ fixed point" principle is incoherent when there is no unique extremum. Sound (elementary).

**Reviewer-independent re-run** (`/tmp/verify_dn2.py`, correct naive gcd-greedy, $|D_n|$ enumerated over one full stabilized period $[0,T)$):

| $a_1$ | $M_1$ | $T$ | $\min|D_n|$ | $\max|D_n|$ | mean | $|D|\ge2$ count | builder's count |
|---|---|---|---|---|---|---|---|
| 15 | 15 | 8 | 2 | 7 | 4.38 | 8/8 | 8/8 |
| 35 | 35 | 34 | 4 | 11 | 5.74 | 34/34 | 34/34 |
| 77 | 77 | 18 | 7 | 17 | 9.50 | 18/18 | 18/18 |
| 91 | 91 | 20 | 8 | 19 | 10.35 | 20/20 | 20/20 |
| 175 | 35 | 274 | 1 | 11 | 3.31 | 263/274 (96.0%) | 263/274 |

**Every row matches the builder's table exactly.** Per-step sizes match bit-exact (e.g. $a_1=15$: $[7,6,2,2,4,5,5,4]$; $a_1=35$: $[11,9,6,5,5,5,6,6,5,4,4,6,6,5,5,5,5,6,6,6,7,7,6,5,5,4,5,5,4,5,7,7,6,6]$; $a_1=77$: $[17,15,9,7,8,7,8,7,7,9,10,10,9,10,9,10,10,9]$; $a_1=91$: $[19,16,8,8,9,8,8,9,8,8,10,11,11,10,11,11,10,11,11,10]$; $a_1=175$ starts $[11,10,6,4,1,3,3,4,4,3,4,3,3,2,2,3,5,4,5,5,\dots]$). **Hand-verified $D_0$ for $a_1=15$ $=\{3,5,6,9,10,12,15\}$, size $7$** — matching the builder's hand-enumeration exactly. The greedy value $=\min D_n$ verified at every step with 0 violations across all transitions in every case. Gap bound $d_n\le M_1$ verified at every step.

**$a_1=175$ exception steps:** the $11$ forced steps ($|D_n|=1$) verified at indices $4,25,46,67,88,150,171,192,213,234,256$ (step $4$ forced $d=15$; the rest forced $d=21$), isolated (no two consecutive), $4.0\%$ of the $274$-step period. Matches builder's claim.

**On the explorer's under-count** ($[2,5]/[1,5]$ vs builder's $[2,7]/[1,11]$): the explorer used an unspecified narrower admissibility definition (the explorer's `extremal_probe.py`); the builder used the correct full admissibility check $\gcd(a_n+d,a_i)>1\ \forall i\le n$. The reviewer's independent enumeration (with the full check) reproduces the builder's larger numbers exactly. The qualitative finding ($|D_n|\ge 2$ almost everywhere) is unchanged and in fact strengthened (4/5 cases 100%).

**Genuinely new (not subsumed):** the variational "greedy $=$ forced extremum $\Rightarrow$ periodicity" sub-class was NOT fenced by any of the 4 existing fences (syndetic-divisible fences pure-statics; primal-dual fences the primal framing; schur-premise-false fences Schur/cofactor; T-unbounded/deviation-wmin fences $f(M_1)$-bounded finite-statistic and deviation-descent). The $D_n$-slack lemma fences a *variational* sub-class — the premise that the greedy minimum is forced by extremality. Different mechanism, genuine new fence.

**Verdict: APPROVE.** The lemma is certified as a negative/structural fence (the 6th structural fence). Record `verified-milestone`.

## No approach-level proofs to review this round

Round 6 was a CONSOLIDATION round: the build set was the two lemma files (negative structural fences), not whole-problem approach files. No `approaches/<slug>.md` was built or revised this round. The two lemmas are certified above; no APPROVE/CHANGES/RETHINK verdict is emitted for any approach slug.

## Explorer cross-check

All three round-6 explorers returned NO-UNFENCED-ROUTE, each collapsing cleanly to existing fences:
- `analytic-growth` (`/tmp/round-6/math-explorer-analytic-growth.md`) — collapses to cofactor-bound + density/covering-capacity fences; the spacing upper bound is sound but no matching non-circular lower bound exists.
- `ramsey-vdw` (`/tmp/round-6/math-explorer-ramsey-vdw.md`) — collapses to `aimo-0907` single-orbit + `deviation-descent-blocked-by-wmin-fence`; greedy suppresses long sub-$T$ const-$d$ APs (longest $\le 25$ across 6 cases). Surfaced the no-fixed-modulus extension (certified above).
- `extremal-variational` (`/tmp/round-6/math-explorer-extremal-variational.md`) — sub-questions (a)/(c) collapse to T-unbounded / primal-dual; sub-question (b) REFUTED by the $D_n$-slack obstruction (certified above).

## Consolidation (Task 2) — `current.md` updated

Appended `## Round 6 update (reviewer-certified)` to `results/imo-2026-06/current.md` (Status stays `partial`; prior rounds preserved). Bumps:
- **Structural fences: 4 → 6** (adds `no-fixed-modulus-forward-determinism` and `D_n-slack-obstruction`).
- **Dead mechanisms: ~13 → ~16** (adds analytic/growth-rate, Ramsey/van-der-Waerden, extremal/variational as fenced sub-classes).
- **Certified lemmas: 28 → 30** (Round 6 (2) line added to the `## Full proof` enumeration).
- **Open target unchanged:** $q\le M_1=\operatorname{rad}(a_1)$ (273+ cases, 0 failures).

Consolidated deliverable re-confirmed: conditional proof (Gap A $\Rightarrow$ endgame $\Rightarrow$ $a_{n+T}=a_n+L$ from $n=1$) + LOCK sub-case + unconditional pure-from-start + conditional bridge + 30 certified lemmas (incl. 9 negative/structural) + 6 structural fences + the T-unbounded-in-$M_1$ impossibility.

## Goal Progress

Status: **partial**; fence count: **6**; lemma count: **30**; new APPROVEs: **2** (both negative/structural lemmas certified); no whole-problem APPROVE this round (round 6 was consolidation + two lemma certifications, not an attack round).
