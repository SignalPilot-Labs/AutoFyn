# proof-reviewer — round 3 — imo-2026-06

Start: 2026-07-25 16:51 UTC. Three builds reviewed independently. Every load-bearing claim re-derived / re-computed in Python (sympy factorint, brute-force greedy to 12000 terms, MT-free fiber-count, residue-class-forcing aperiodicity).

## integer-monovariant-transfer — Status: unsolved (dead-end) — Verdict: RETHINK

### What was proved (verified, certified)
- **Lemma A (block-index advance).** $b_n=\lfloor(a_n-a_1)/M_1\rfloor$ satisfies $b_{n+1}-b_n\in\{0,1\}$. Proof: $0\le r_n+d_n\le 2M_1-1<(b_n+2)M_1$ from $d_n\le M_1$. Re-verified for 13 starting values (incl. $6,15,35,77,91,143,175,385,847,1309,2085,116,145$): in every case $b_{n+1}-b_n\in\{0,1\}$. Certified `lemmas/block-index-advance.md` (trivial but unconditional and reusable).
- **Obstruction Theorem (negative).** The `aimo-0134` integrality-upgraded-monotonicity mechanism does NOT port. Certified as `lemmas/aimo-0134-obstruction.md`.

### The obstruction — load-bearing, re-derived and confirmed
1. **$C_n=nM_1-(a_{n+1}-a_1)=\sum_{k\le n}(M_1-d_k)$ is non-decreasing but unbounded in non-LOCK.** Re-derived the contrapositive: if $C_n$ bounded, then the non-negative integer series $\sum(M_1-d_k)$ has bounded partial sums $\Rightarrow$ $M_1-d_n=0$ eventually $\Rightarrow$ $d_n\equiv M_1$ eventually $\Rightarrow$ period-$1$ AP with $L=M_1$, contradicting non-LOCK ($L/T<M_1$). VALID. Confirmed computationally: $C_n$ grows linearly ($a_1=385$: $C_{399}=150172$; $a_1=2085$: $C_{399}=832179$; $a_1=15$: $C_{40}=462$).
2. **$b_n^{\rm avg}=\lfloor(a_n-a_1)/(n-1)\rfloor$ is non-monotone in non-LOCK.** Re-computed $a_1=15$: $b^{\rm avg}=(3,2,3,3,4,4,3,\dots)$ — neither non-decreasing ($3>2$) nor non-increasing ($2<3$). Confirmed non-monotone for $a_1\in\{35,77,91,175,847\}$. Cesàro-constancy to $\lfloor L/T\rfloor$ verified ($385\to8$, $1309\to8$, $2085\to4$, $175\to9$) — but it's a *consequence* of periodicity, not a cause.
3. **Root cause.** `aimo-0134` needs a *shrinking* range bound ($a_{k+1}\le k$ small vs $k+1$); our bound $d_n\le M_1$ is *constant* — no slack for integrality to upgrade. Sound.
4. **Transfer step = Gap A.** The finite-state pigeonhole on $(c_n,\text{recent }d\text{-window})$ is not closed (89 transition conflicts for $a_1=385$ on $a_n\bmod M_1$). Confirmed (round-3 finite-statistic explorer).

### Errors found (minor, non-load-bearing, flagged honestly)
- **LOCK parenthetical is FALSE.** The proof says "for LOCK cases $C_n\equiv0$, trivially bounded." This is WRONG: for LOCK with lock prime $p\ne M_1$ (e.g. $a_1=116=2^2\cdot29$, $M_1=58$, lock prime $p=2$), $C_n=\sum(58-d_k)$ grows linearly ($C_{10}=616$, $C_{20}=1176$, $C_{30}=1736$). $C_n\equiv0$ holds ONLY for the special LOCK case $a_1=p$ ($p=M_1$). This side remark does NOT affect the obstruction's load-bearing claim (non-LOCK $\Rightarrow$ $C_n$ unbounded, proved by the valid contrapositive), but it is a factual error that the certified lemma corrects.
- **$C_{400}$ numbers are off-by-one.** Builder claims $a_1=385$: $C_{400}=150172$; I get $150172=C_{399}$ (builder's "$C_{400}$" is the sum $\sum_{k=1}^{399}$). For $a_1=2085$, builder claims $830094$; I get $C_{400}=832173$, $C_{399}=832179$ — neither matches $830094$ (off by $\sim M_1=2085$). Indexing slip; the qualitative claim (unbounded linear growth) is unaffected.

### Verdict
The `aimo-0134` integer-monovariant template is the WHOLE approach, and it is provably dead (constant bound, no shrinking-range integrality upgrade, transfer gated by Gap A). This is exactly the situation of `growing-modulus-descent` in round 2 (dead monovariant engine) $\Rightarrow$ RETHINK. Two lemmas certified (block-index-advance trivial; aimo-0134-obstruction negative). The framing is fenced off: future rounds should NOT re-dispatch the `aimo-0134` template. (A *different* integer-monovariant mechanism is not ruled out, but is not on the table.)

---

## crt-period-lifting — Status: partial — Verdict: CHANGES REQUESTED

### What was proved (verified, certified)
- **Lemma F1 (fiber-count lift, unconditional identity).** $|A|\le p\cdot|A\bmod L_k|$ where $L=L_k\cdot p$. Trivial fiber counting ($\pi:\mathbb Z/L\mathbb Z\to\mathbb Z/L_k\mathbb Z$ has fibers of size $p$). Re-derived; sound. Lift ratios verified computationally for $a_1\in\{6,385,1309,847,175\}$: every ratio $|A_k|/|A_{k-1}|\le p_k$ (slack $1.0\times$–$11\times$), $T\le L$ in every case. Builder's table matches ($385$: ratios $2,3,3.67,5.09,3.32,13.68$; $847$: $2,3,4,2.67,27.25$; $175$: $2,3,3.67,1.55,8.06$). Certified as part of `lemmas/squarefree-period-under-gap-A.md`.
- **Lemma F2 (unconditional $\mathcal B_\infty$ representation).** $\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m:\operatorname{rad}(T)\mid m\}$. ($\Leftarrow$) transversal $\subseteq S(m)$. ($\Rightarrow$) $S(m)$ finite $\Rightarrow$ finite descending chain to a minimal sub-transversal $T_0\subseteq S(m)$. Standard; sound. This is the unconditional version of `distinct-supports-stabilize`'s conditional corollary. Certified `lemmas/binfinity-divisibility-progression-structure.md`. (Note: the representation alone does NOT close Gap A — the union may be infinite; periodicity needs $G$ finite = Gap A.)
- **Conditional squarefree-period refinement.** Under Gap A, $L=\prod_{p\in G}p$ is squarefree (lcm of squarefree $\operatorname{rad}(T)$'s), $T\le L$. Sound. Certified `lemmas/squarefree-period-under-gap-A.md`. Genuine refinement of `distinct-supports-stabilize`.

### The wall — confirmed honestly
- **`aimo-0231` nontrivial content does NOT port.** In `aimo-0231` the map is a polynomial iterate; here the cyclic-successor map is a single $|A|$-cycle (`cyclic-successor-bijection`), so return time $=|A|$ exactly and the lift bound is the trivial fiber-count identity. Captures no greedy structure. Confirmed.
- **Cofactor-bounding induction is circular.** The "smallest $L_k$-admissible multiple" cofactor depends on transient primes (full admissibility, not just $G_k$-skeleton); bounding which transient primes appear IS Gap A — same circularity certified dead for `witness-density-recurrence` round 2. Confirmed honest.

### Verdict
The conditional structural refinement + two unconditional lemmas are a genuine (if thin) contribution; the CRT-lift *mechanism for closing Gap A* is dead (circular). This is the situation of `transversal-saturation` round 2 (dead strip, surviving lemmas) $\Rightarrow$ CHANGES REQUESTED as a lemma source. The CRT-lift cofactor induction should NOT be re-attempted; the approach stays for its certified conditional structure.

---

## p1-equals-2-direct — Status: partial — Verdict: CHANGES REQUESTED

### What was proved (verified, certified)
- **`two-entry-lemma` ($|P_1|=2$ NON-LOCK).** $a_2=a_1+p_{\rm sm}=p_{\rm sm}(p_{\rm sm}^{k-1}q+1)$ is even. Proof re-derived: at $n=1$ only constraint is $S(a_2)\cap P_1\ne\varnothing$; smallest $p$-multiple above $a_1$ is $a_1+p$; any $m\in(a_1,a_1+p)$ has $m\bmod p=j\ne0$ and $m\bmod q=j\ne0$ (since $0<j<p<q$), so $S(m)\cap P_1=\varnothing$. Then $p^{k-1}q$ odd $\Rightarrow$ $p^{k-1}q+1$ even. Sound. Verified on 8 NON-LOCK cases ($15,35,65,77,91,143,175,847$): every $a_2=a_1+p_{\rm sm}$ and $2\mid a_2$. Certified `lemmas/two-entry-lemma.md`. The lever is genuinely $|P_1|=2$-specific (no single prime dominates for $|P_1|\ge3$).
- **`P1-minimal-transversal-lemma` ($|P_1|=2$ NON-LOCK).** $P_1=\{p,q\}\in\operatorname{MT}(\mathcal F_\infty)$. Proof re-derived: linchpin ($P_1$ transversal) + the sub-result "$r\mid a_n\,\forall n\Rightarrow a_{n+1}=a_n+r\Rightarrow a_n=r(b+n-1)\Rightarrow$ choose $j$ with $r^{j-1}\ge b$, $n=r^{j-1}-b+1\Rightarrow a_n=r^j$ prime power $\Rightarrow$ LOCK." Contrapositive: NON-LOCK $\Rightarrow$ neither $\{p\}$ nor $\{q\}$ is a transversal $\Rightarrow$ $P_1$ minimal. Sound. Verified on 8 NON-LOCK cases: neither $p$ nor $q$ divides all of the first 200 terms. The sub-result "$r\mid a_n\,\forall n\Rightarrow$ LOCK" is a self-contained engine, importable. Certified `lemmas/P1-minimal-transversal-lemma.md`.

### The wall — confirmed honestly
- **Cofactor-bound wall (Gap A specialized to $|P_1|=2$) OPEN.** Governing primes $\le M_1$ verified for $a_1\in\{15,35,65,77,91,143,175,847,385\}$: $41\le77$ (847), $13\le35$ (175), $19\le385$ (385). Re-verified governing sets and periods from scratch (847: $T=1744,L=18942$; 175: $T=274,L=2730$; 385: $T=5088,L=43890$). All match.
- **$2$-density mechanism REFUTED.** $a_1=15$, $a_8=42$: smallest admissible $m>42$ is $a_9=45=3^2\cdot5$ (ODD). Re-verified: $44=2^2\cdot11$, $S(44)\cap\{3,5\}=\varnothing$, inadmissible. $v_2(a_n)$ over $n=1..40$ takes all of $\{0,1,2,3,4,5\}$ and fluctuates — does not stabilize. Confirmed. The $2$-density lever is a statistical bias, not a rigid cofactor bound.

### Verdict
Two sound unconditional structural lemmas (genuine narrowing of the $|P_1|=2$ base case with a new lever) + honest cofactor-bound wall. The 2-density mechanism is refuted, but the structural lemmas are the contribution. CHANGES REQUESTED — the approach is a legitimate partial base case; the cofactor-bound wall (Gap A specialized) remains open.

---

## Lemma certifications (7 new this round)

All seven proposed lemma-candidates are **CERTIFIED** (sound, no stronger than proved):

1. `block-index-advance` (integer-monovariant) — +, trivial but unconditional, verified 13 cases.
2. `aimo-0134-obstruction` (integer-monovariant) — −, the shrinking-range integrality mechanism is provably absent; the contrapositive ($C_n$ bounded $\Rightarrow$ $d_n\to M_1$ $\Rightarrow$ not non-LOCK) is valid; the LOCK parenthetical error is corrected in the lemma file.
3. `binfinity-divisibility-progression-structure` (crt-lifting) — +, unconditional $\mathcal B_\infty=\bigcup\operatorname{rad}(T)\mathbb Z$ via finite-sub-transversal; isolates the representation from periodicity.
4. `squarefree-period-under-gap-A` (crt-lifting) — +, conditional refinement ($L$ squarefree, $T\le L$, fiber-count lift); the lift is trivial but the squarefree-ness is a genuine sharpening of `distinct-supports-stabilize`.
5. `two-entry-lemma` (p1-equals-2) — +, $|P_1|=2$-specific, verified 8 cases.
6. `P1-minimal-transversal-lemma` (p1-equals-2) — +, $P_1\in\operatorname{MT}(\mathcal F_\infty)$ + the "$r\mid a_n\,\forall n\Rightarrow$ LOCK" sub-result; verified 8 cases.
7. `syndetic-divisible-closed-not-periodic` (covering-systems explorer, recommended by outline-reviewer) — −, the counterexample $B=6\mathbb Z\cup\bigcup_{p\equiv1(4)}p\mathbb Z$ is divisibility-closed, syndetic (max gap $5\le6$), aperiodic. **The explorer's "density-$1/2$ subfamily" proof was hand-wavy; I replaced it with the clean rigorous proof:** $L$-periodicity forces class $L\bmod6\subseteq B$ but only $0\bmod6\subseteq B$ (classes $1..5\bmod6$ contain $1,2,3,4,11\notin B$), so $6\mid L$; then for each prime $p\equiv1(4)$, $p\mid L$ (class $L\bmod p\subseteq B$ but only $0\bmod p\subseteq B$, since each nonzero class contains a prime $q\equiv3(4)$ coprime to $6p$ by Dirichlet $\Rightarrow q\notin B$); infinitely many such $p$ $\Rightarrow$ $L$ divisible by infinitely many primes, contradiction. Verified computationally ($L\le400$ all aperiodic; structural witnesses for $L\in\{1,2,3,5,7,11,30,42,100\}$; divisibility-closure over $[1,150]$; max gap $5$ over $[1,2000]$).

Total certified lemmas: 21 (was 14).

---

## Per-slug routing

- `integer-monovariant-transfer` — **RETHINK** (unsolved/dead-end: the `aimo-0134` engine is the whole approach and is provably dead; fenced off; 2 lemmas certified). Retire the `aimo-0134` template.
- `crt-period-lifting` — **CHANGES REQUESTED** (partial: F1/F2 + conditional refinement certified; CRT-lift cofactor mechanism for Gap A is circular/dead — set it aside; keep as lemma source).
- `p1-equals-2-direct` — **CHANGES REQUESTED** (partial: two-entry + P1-minimal-transversal certified; cofactor-bound wall open; 2-density mechanism refuted; legitimate narrowed base case).

---

## Headline for the orchestrator

**The stall is NOT broken.** All three round-3 framings failed to escape Gap A:
- `integer-monovariant-transfer` (the outline-reviewer's only genuinely-orthogonal hope) is now a **certified dead-end** — the `aimo-0134` shrinking-range integrality mechanism is provably absent (constant gap bound), and the transfer step is gated by Gap A. The genuinely-orthogonal escape has died.
- `crt-period-lifting` and `p1-equals-2-direct` both bottom out on the cofactor-bound conjecture (Gap A) — the single-gap-trap the outline-reviewer flagged. The CRT-lift cofactor induction is circular (same as witness-density round 2); the $2$-density mechanism is refuted ($a_1=15$).

**Progress is real but structural, not wall-closing.** 7 new lemmas certified (21 total). The wall is now SHARPLY CHARACTERIZED from three independent negative directions:
1. Pure statics cannot work (`syndetic-divisible-closed-not-periodic`): divisibility-closure + syndeticity $\not\Rightarrow$ periodicity.
2. The `aimo-0134` integer-monovariant template cannot work (`aimo-0134-obstruction`): constant bound $\Rightarrow$ no shrinking-range integrality upgrade.
3. Transversal/MT bounds cannot work (rounds 1–2): strip/monovariant/density all dead on the covering-capacity obstruction.

**What round 4 should do.** The field has now exhausted (a) transversal/MT/strip, (b) monovariant (`aimo-0134`), (c) density/covering-capacity, (d) CRT-lift cofactor, (e) pure statics/sieve, (f) $2$-density for $|P_1|=2$. The remaining genuinely-orthogonal directions are **dynamical-systems / combinatorics-on-words flavored**: treat the cyclic-successor map on $\mathcal B_\infty$ as a substitution/morphism on the increment sequence $(d_n)$; or attempt a direct ergodic/recurrence argument on the cyclic-successor orbit; or attack the increment pattern $(d_n)$ as a morphic word and prove eventual periodicity from the greedy rule + gap bound WITHOUT ever forming $\mathcal B_\infty$/MT/transversals. The reviewer also re-flags the standing empirical conjecture: every governing prime $q\le M_1=\operatorname{rad}(a_1)$ holds across 273+ cases with 0 failures — a direct proof of this (not via strip/monovariant/density/CRT-lift) would close Gap A immediately; the obstacle is finding a non-circular mechanism, and the three negative lemmas now delimit exactly which mechanisms are forbidden.
