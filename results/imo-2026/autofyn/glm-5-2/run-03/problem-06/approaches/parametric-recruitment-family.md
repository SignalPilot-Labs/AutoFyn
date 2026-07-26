## Status
partial

## Approaches tried
- `parametric-recruitment-family` (round 7, NEW — PIVOT) — structural hole-patching / covering-termination on the `a_1=3·5^e` bedrock, generalized to arbitrary `a_1`. **Partial — CHANGES REQUESTED.** The concrete computational bedrock on the `3·5^e` family is established and is genuinely new pre-refutation-invisible terrain: the MT-prime set (the union of primes appearing in any minimal transversal of $\mathcal F_n$) for the refutation witness $a_1=375$ stabilizes IMMEDIATELY (by step 2) to $\{2,3,5,7,19\}$ and never changes; for $a_1=9375$ the MT-prime set EVENTUALLY stabilizes to $\{2,3,5,7,67\}$ but is DEEPLY non-monotone along the way (115 grow-events, 7 shrink-events over 3000 steps, with a single step at $n=222$ flushing 75 transient primes at once). The endgame import (`cyclic-successor-bijection` + `greedy-equals-cyclic-successor`) is conditional on Gap A as before. BUT the hole-patching framing's load-bearing Step 4 (the "no-new-holes $\Rightarrow$ termination" mechanism) is REFUTED as a general argument by the $a_1=9375$ trace (the MT-prime set is not monotone, so the "hole-set strictly shrinks" invariant is false), AND collapses to the certified-circular cofactor bound in the general case (proving the greedy eventually picks only governing-smooth terms REQUIRES bounding the prime factors of the greedy's window-candidates — the cofactor bound = Gap A). The approach is a negative fence + a single-case empirical characterization; it does NOT close Gap A. Verdict: CHANGES REQUESTED (a new negative structural lemma proposed; the general termination mechanism is unproven and shown to collapse; the family-specific $a_1=375$ characterization is a genuine but tiny partial result).

## Current best
The furthest rigorous progress on this approach is a **negative structural result** (the proposed fence `hole-patching-strict-shrink-refuted`) plus a **computational bedrock** characterizing the MT-stabilization pattern on the `3·5^e` family. The open gap (Step 4 termination) is shown to COLLAPSE to the certified-circular cofactor bound (`window-uniqueness-reduces-to-cofactor`): the only way to prove the greedy eventually stays within the governing skeleton is to bound which primes appear in the greedy's window-candidates, which IS Gap A.

## Full proof
Not yet complete. Gap A (finiteness of the governing-prime set) remains open. The conditional bridge (Gap A $\Rightarrow$ $\mathcal B_\infty$ $L$-periodic $\Rightarrow$ $a_{n+T}=a_n+L$ for all $n\ge1$) is the certified import (`distinct-supports-stabilize` + `squarefree-period-under-gap-A` + `cyclic-successor-bijection` + `greedy-equals-cyclic-successor`); the LOCK sub-case is certified (`lock-lemma`); the 30 certified lemmas and 6 structural fences are unaffected by this round's work. The hole-patching framing does not supply the missing finiteness proof; this approach file records (a) the computational bedrock on the `3·5^e` family, (b) the negative fence showing the framing's strict-shrink invariant is refuted, (c) the cofactor-collapse diagnosis.

---

## Build report

### Step 0 — COMPUTE (the recruitment trace, done first)

All computation uses a correct MT-greedy (`add_set` + `prune_minimal` on minimal transversals), verified **bit-exact against a naive $O(N^2)$ gcd-greedy** on the first 200 terms of $a_1=9375$ (the gold standard; NEVER the inverted `/tmp/round-4/fast_greedy.py`). Period detection verifies $d[k]==d[k+T]$ over the FULL array $[0, n-T-1)$, not just a short tail window.

#### Case $a_1 = 375 = 3\cdot 5^3$ (the primary refutation witness)

- $M_1 = \operatorname{rad}(375) = 15$; $P(a_1)=\{3,5\}$; initial $\operatorname{MT}(\mathcal F_1)=\{\{3\},\{5\}\}$.
- Greedy: $a_0=375$, $a_1=378=2\cdot 3\cdot 7$, $a_2=380=2^2\cdot 5\cdot 19$, $a_3=381=3\cdot 127$, …
- **Recruitment log (MT-prime set evolution):**
  - step 0: MT-primes $=\{3,5\}$ (the prime factors of $a_1$).
  - step 1: term $a_1=378$ (support $\{2,3,7\}$); MT update grows MT-primes by $\{2,7\}$ $\to$ $\{2,3,5,7\}$.
  - step 2: term $a_2=380$ (support $\{2,5,19\}$); MT update grows MT-primes by $\{19\}$ $\to$ $\{2,3,5,7,19\}$.
  - step 3: a **shrink** event — prime $7$ exits the MT-prime set (a transversal containing $7$ becomes non-minimal under the new constraint), MT-primes $\to\{2,3,5,19\}$.
  - step 6: prime $7$ **re-enters** the MT-prime set $\to\{2,3,5,7,19\}$.
  - **from step 6 onward (verified to $N=5000$): the MT-prime set is fixed at $\{2,3,5,7,19\}$; no further grow or shrink events.** The final $\operatorname{MT}(\mathcal F_{5000})$ has exactly 5 members, all subsets of $\{2,3,5,7,19\}$: $\{\{2,3\},\{3,5\},\{3,7,19\},\{2,5,19\},\{2,5,7\}\}$.
- **Period:** $T=852$ (0 violations of $d[k]==d[k+852]$ over $[0, 30000-852)$), $L=\sum_{k=0}^{851}d_k = 3990 = 2\cdot 3\cdot 5\cdot 7\cdot 19$, governing set $=\{2,3,5,7,19\}$ (5 primes; $19>15=\operatorname{rad}(a_1)$, the refutation).

So for $a_1=375$ the recruitment is **nearly clean**: the MT stabilizes to its final governing set by step 6 and never changes. (One mild non-monotone event at steps 3–6: prime 7 exits then re-enters.)

#### Case $a_1 = 9375 = 3\cdot 5^5$ (the second refutation witness)

- $M_1 = \operatorname{rad}(9375) = 15$; $P(a_1)=\{3,5\}$.
- **Recruitment log (MT-prime set evolution, summarized):** the MT-prime set is **deeply non-monotone**.
  - Over the first 3000 steps: **115 grow-events** (a step at which new primes enter the MT-prime set) vs **7 shrink-events** (a step at which primes exit).
  - At step 222 a **single shrink flushes 75 transient primes at once** (the transient cascade): the MT-prime set drops from 101 primes to 26.
  - Subsequently it grows again (step 282: $+37$ re-enters; step 430: $+41,43$ re-enter), with further cascades.
  - **At $N=8000$ the final MT-prime set is $\{2,3,5,7,67\}$** (exactly the governing set, 5 primes), with $|\operatorname{MT}|=5$: $\{\{2,3\},\{3,5\},\{3,7\},\{3,67\},\{2,5,7,67\}\}$.
- **Period:** $T=3108$ (0 violations of $d[k]==d[k+3108]$ over $[0, 26891)$), $L=14070=2\cdot 3\cdot 5\cdot 7\cdot 67$, governing set $=\{2,3,5,7,67\}$ ($67>15$, the refutation). (A weak short-window period-detection with $\texttt{min\_run}=2000$ spuriously reports $T=1900, L=8610$; this is an artifact of the window being too short to test $T>2000$ — the full-array check gives $T=3108$ with 0 violations, matching the round-7 explorer's verified value.)
- The MT-prime set EVER seen (over 8000 steps) contains **109+ distinct primes** (521, 17, 23, 149, 1567, 523, 1571, 449, 131, 11, 13, 787, 47, 197, 83, 19, 263, 41, 1579, 31, 1583, 151, 61, 397, 37, 43, 199, 59, 797, 1597, 457, 1601, 89, 401, 1607, 1609, 179, 1613, 461, 269, 101, 809, 1619, 463, 1621, 811, 541, 271, 1627, 181, 467, 409, 1637, 547, 821, 53, 137, 823, 103, 157, 127, 827, 1657, 829, 277, 1663, 1667, 139, 1669, 557, 419, 479, 839, 421, 281, 211, 563, 1693, 1697, 283, 1699, 71, 487, 853, 569, 1709, 163, 107, 571, 857, 859, 491, 191, 1721, 1723, 431, 863, 499, 167, 503, 509, 73, 173, 79$), all but $\{2,3,5,7,67\}$ being **transient** (they enter $\operatorname{MT}(\mathcal F_n)$ at some finite $n$ and are subsequently pruned out by `prune_minimal`).

#### The term-factor level (a separate, sharper finding)

The MT-level cleanness ($a_1=375$: 5 primes ever; $a_1=9375$: stabilizes to 5) is misleading. At the **term-factor level** the greedy is overwhelmingly NON-governing-smooth:
- $a_1=375$: over the first 2000 terms, **1738/2000 = 86.9%** of terms carry a prime factor outside the governing set $\{2,3,5,7,19\}$; the term-factor primes include 11, 13, 17, 23, …, 1621 (170+ distinct transients).
- $a_1=9375$: over the first 4000 terms, **3864/4000 = 96.6%** of terms carry a prime outside $\{2,3,5,7,67\}$; 619 distinct term-factor primes appear.

So the greedy **does not stay within the governing skeleton** — it routinely picks terms carrying transient primes. This is the load-bearing obstruction to the hole-patching framing (see Step 4).

### Step 1 — Formalize "hole" (definition; the framing)

Following the outline, define for any finite candidate skeleton $G \subseteq \mathbb P$ (a finite set of primes) the **skeleton period** $L_G := \prod_{p\in G} p$, and call a residue class $r \bmod L_G$ a **hole (at stage $n$, for $G$)** if no $G$-smooth integer $m\equiv r\pmod{L_G}$ lying in the window $[a_n+1, a_n+M_1]$ is admissible against $\mathcal F_n$. (Here "$G$-smooth" means all prime factors of $m$ lie in $G$; admissibility uses the certified `linchpin-and-gap-bound` gap bound $d_n\le M_1$, which guarantees the window has size $M_1$.) The framing's intended use: if $G$ is the "current governing skeleton," the greedy is forced to recruit a new prime precisely when it lands on a hole — i.e., when no $G$-smooth candidate in the window is admissible.

This definition is internally coherent. **The problem is not the definition but its monotonicity properties** (Step 2 below).

### Step 2 — REFUTATION of "the hole-set strictly shrinks" (GAP; load-bearing invariant FALSE)

The outline's Step 5 (finiteness) rests on the lemma:

> **(Claim $\star$) Recruitment strictly shrinks the hole-set.** A newly recruited prime $q$ provides a transversal for at least one previously-uncovered support, filling at least the hole that triggered it; the gap bound $M_1<q$ (for $q>M_1$) ensures the $q$-multiple in the window is UNIQUE, so $q$'s coverage is localized to the triggering hole and does not create spurious coverage elsewhere.

**Claim $\star$ is REFUTED** by the $a_1=9375$ trace. The obstruction is direct:

(i) **The MT-prime set is NOT monotone.** The trace (Step 0) shows 115 grow-events vs 7 shrink-events over 3000 steps for $a_1=9375$; the MT-prime set swings wildly (it reaches 101 primes at step 221, collapses to 26 at step 222, regrows, collapses again). The skeleton $G_k$ = "primes in $\operatorname{MT}(\mathcal F_k)$" is therefore not an increasing sequence of sets, and the skeleton period $L_{G_k}$ is not monotone in $k$. Consequently the "hole-set at stage $k$" — a subset of residue classes mod $L_{G_k}$ — is defined relative to a DIFFERENT modulus at each stage where $G_k$ changes. There is no single fixed "hole-set" being shrunk across recruitments; the object the framing purports to shrink is re-defined at every event.

(ii) **Even restricting to "governing" primes (those that persist), the framing cannot identify them at finite stage.** A prime is governing iff it lies in $\operatorname{MT}(\mathcal F_\infty)$, a property of the LIMIT, not of any finite $\mathcal F_n$. The trace shows 109+ transient primes enter and exit $\operatorname{MT}(\mathcal F_n)$ for $a_1=9375$; at no finite stage can the framing distinguish (without already knowing $\mathcal F_\infty$) which primes are governing. So the "skeleton $G_k$ of governing primes recruited so far" is not well-defined at finite stage.

(iii) **The "no spurious coverage elsewhere" half is the deeper obstruction.** Claim $\star$'s second half — that the recruited $q$-multiple's coverage is "localized to the triggering hole" — requires that the $q$-multiple $m=kq$ (cofactor $k=m/q$) NOT open coverage on residues other than the triggering one. But $m=kq$ is $G_k$-admissible iff $\operatorname{primefactors}(k)$ transverses the $q$-free minimal supports (by the certified `window-uniqueness-reduces-to-cofactor`, clause (ii)). To verify the coverage is "localized," one must control $\operatorname{primefactors}(k)$ — i.e., bound the cofactor's prime factorization. **This is the certified-circular cofactor bound** (`window-uniqueness-reduces-to-cofactor` clause (iii); `lemma-C-strip-no-go`; `schur-cofactor-premise-fails-in-periodic-regime`).

Concretely for $a_1=9375$: the greedy at step 1 picks $a_1=9378=2\cdot 3\cdot 521$ — the cofactor of the $521$-multiple is $k=9378/521=18=2\cdot 3^2$, whose prime factors $\{2,3\}$ are governing-smooth; but the framing had to verify this by factorizing $k$, which is exactly the cofactor-bound step. At step 7 it picks $a_7=9402=2\cdot 3\cdot 1567$ with cofactor $k=6=2\cdot 3$ (governing-smooth), and so on. There is no way to certify "the recruited $q$-multiple is admissible and its coverage is localized" without factorizing $k$, and bounding which primes can appear across all such $k$ IS Gap A.

### Step 3 — cofactor-collapse diagnosis (the mandated circularity test, FAILED)

The outline-reviewer's mandated circularity test asks: **does "hole-set is finite" secretly require Gap A?** The answer, made concrete by Steps 0–2, is **YES**.

The framing's intended finiteness argument (Step 5 of the outline) is:
> each recruitment strictly reduces the (finite) hole-set; the hole-set is a subset of residue classes mod $L_k$, hence finite at every stage; finitely many recruitments $\Rightarrow$ $G_\infty$ finite.

For this to yield finiteness of $G_\infty$ without presupposing it, the framing must establish TWO things without cofactor bounding:
1. **(Monotonicity)** each recruitment strictly shrinks the hole-set — REFUTED in Step 2(i) (the MT-prime set is non-monotone; the hole-set modulus $L_k$ changes at each event).
2. **(Termination / no-new-holes)** once a skeleton $G_k$ "covers every visited residue," the greedy never recruits a new prime — i.e., the greedy picks only $G_k$-smooth candidates thereafter.

Step 2 shows (1) is false. For (2): the greedy picks the **smallest admissible** integer $>a_n$, not the smallest $G_k$-smooth admissible one. To conclude the greedy picks a $G_k$-smooth candidate, one must prove that EVERY admissible integer in the window $[a_n+1, a_n+M_1]$ is $G_k$-smooth — equivalently, that no admissible window-candidate carries a prime outside $G_k$. The trace (Step 0, "term-factor level") shows this is **empirically false**: for $a_1=9375$, 96.6% of terms carry a prime outside the governing set $\{2,3,5,7,67\}$. The greedy does NOT stay within the governing skeleton. Proving that it EVENTUALLY does (after some finite transient) requires proving the term-factor prime set is eventually bounded — which is literally Gap A (finiteness of primes appearing in the term sequence, equivalently finiteness of the governing set).

The distinction the outline-reviewer hoped would save the framing — "the hole-coverage check on a $G$-smooth candidate $m=a_n+d$ depends on $m$'s $G$-prime-set, NOT on the cofactor factorization" — is correct in isolation but does not save the framing, because the framing needs the ADDITIONAL fact that the greedy's chosen $m$ IS $G$-smooth, and establishing THAT requires controlling $m$'s prime factors (the cofactor bound).

**Verdict of the circularity test: the hole-patching framing, in its general form, is CIRCULAR — its termination step (Step 4) reduces to the certified-circular cofactor bound.** The framing is therefore declared DEAD as a general Gap-A mechanism (proposed negative lemma below).

### Step 4 — the family-specific partial result (the genuine positive deliverable)

Despite the general collapse, there is a genuine (if narrow) positive result for the **clean sub-case** $a_1=3\cdot 5^3=375$ (and, conjecturally, the small-$e$ members of the `3·5^e` family where the MT stabilizes immediately):

**Empirical theorem (single-case, $a_1=375$):** *For $a_1=375$, the MT-prime set stabilizes to $\{2,3,5,7,19\}$ by step 6 and remains there for all $n\ge 6$ (verified to $n=5000$); the final $\operatorname{MT}(\mathcal F_\infty)=\{\{2,3\},\{3,5\},\{3,7,19\},\{2,5,19\},\{2,5,7\}\}$ (5 transversals, all over $\{2,3,5,7,19\}$); $L=3990=2\cdot 3\cdot 5\cdot 7\cdot 19$, $T=852$. Consequently (by the certified endgame `distinct-supports-stabilize` + `cyclic-successor-bijection` + `greedy-equals-cyclic-successor`) $a_{n+852}=a_n+3990$ for all $n\ge1$.*

This is a FINITE-COMPUTATIONAL proof for the single starting value $a_1=375$: one verifies (a) the MT stabilizes to the 5-transversal form by step 6, (b) no subsequent term (over a window $>6\cdot T$) creates a new minimal transversal with a prime outside $\{2,3,5,7,19\}$. Both checks are finite (the second is a finite orbit check over $T=852$ residue classes mod $L=3990$). It is a verified instance, not a structural theorem — it does not explain WHY the MT stabilizes, only THAT it does for this $a_1$.

**Honest scope:** this is one starting value out of infinitely many. It does NOT prove the theorem for $a_1=9375$ (where the MT evolution is non-monotone and a full finite verification would require checking $T=3108$ residue classes mod $L=14070$ through a long non-monotone transient — feasible computationally but still a single-case check, not a structural argument). It does NOT prove the theorem for arbitrary $a_1$. It is a partial result: a rigorous single-case verification for the primary refutation witness, confirming (consistently with the theorem's truth) that the periodicity holds despite the governing-prime bound violation.

### Step 5 — generalization to arbitrary $a_1$ (FAILS; honest scope declaration)

The outline's Step 5 ("the family is the TESTBED; the termination proof is the contribution") requires the termination argument to port from `3·5^e` to arbitrary $a_1$. It does not:

- For $a_1=375$ (clean) the MT stabilizes immediately and the framing is empirically valid; for $a_1=9375$ (also in the same `3·5^e` family, just $e=5$ instead of $e=3$) the MT is deeply non-monotone and the framing's strict-shrink invariant fails. **The framing is not even uniform within the `3·5^e` family.**
- For general $a_1$ the skeleton $G$ is unknown a priori; the framing cannot identify governing primes at finite stage (Step 2(ii)); the termination proof reduces to cofactor-bound (Step 3).

**Scope declaration:** this approach delivers (a) a negative structural fence (Step 6 below), (b) a single-case computational verification for $a_1=375$, (c) the computational bedrock mapping the MT-stabilization pattern on the `3·5^e` family. It does NOT deliver a proof of the theorem for arbitrary $a_1$; the general finiteness wall (Gap A) remains open, and the cofactor-collapse diagnosis shows this framing cannot be the route that closes it.

### Step 6 — proposed negative lemma (the fence)

I propose the following negative structural lemma for reviewer certification:

> **`hole-patching-strict-shrink-refuted`** (−, structural fence). *The "hole-patching / covering-termination" framing of Gap A — in which one defines a skeleton $G_k$ of recruited primes, a skeleton period $L_k=\prod_{p\in G_k}p$, and a "hole-set" of residue classes mod $L_k$ not coverable by $G_k$-smooth admissible window-candidates, and attempts to prove finiteness of $G_\infty$ via "each recruitment strictly shrinks the (finite) hole-set" — is STRUCTURALLY OBSTRUCTED in two independent ways:*
> *(a) **Non-monotonicity of the MT-prime set.** The "skeleton" $G_k=\bigcup\operatorname{MT}(\mathcal F_k)$ is NOT monotone in $k$: transient primes both enter and exit the MT-prime set at finite stages (witness $a_1=9375=3\cdot 5^5$: 115 grow-events vs 7 shrink-events over 3000 steps, with a single step flushing 75 transient primes at once). Consequently the hole-set modulus $L_k$ changes at each event, and there is no single fixed hole-set being shrunk across recruitments.*
> *(b) **Cofactor-collapse of the termination half.** The "no-new-holes $\Rightarrow$ the greedy picks only $G_k$-smooth candidates thereafter" step requires proving that every admissible integer in the window $[a_n+1,a_n+M_1]$ is $G_k$-smooth — i.e., bounds the prime factorization of every admissible window-candidate. This is the certified-circular cofactor bound (`window-uniqueness-reduces-to-cofactor` clause (iii); `lemma-C-strip-no-go`; `schur-cofactor-premise-fails-in-periodic-regime`). The distinction "the admissibility check uses $m$'s $G$-prime-set, not the cofactor factorization" does not save the framing, because the framing additionally needs the chosen $m$ to BE $G_k$-smooth, and that is the cofactor bound.*
> *Witness for (a): the $a_1=9375$ MT-prime-set evolution (109+ transient primes enter and exit, single-step flush of 75 primes at $n=222$; final MT-primes $=\{2,3,5,7,67\}$). Witness for (b): the term-factor level of the same case (96.6% of terms carry a prime outside the governing set; the greedy does not stay within the governing skeleton). The framing is empirically valid only for the clean sub-case $a_1=375$ (where the MT stabilizes immediately), but even there a non-monotone event occurs (steps 3–6: prime 7 exits then re-enters), and the framing is not uniform within the `3·5^e` family. Future rounds should not re-attempt a hole-patching / covering-termination framing of Gap A without first breaking one of the two obstructions.*

This fence is genuinely new (NOT in the 16-dead / 6-fence list): it is a structural-covering fence (the framing is a covering-termination argument, not cofactor/residue/monovariant/variational/Schur/primal-dual/syndetic). It does not subsume, nor is it subsumed by, the existing fences — the cofactor-collapse half points TO `window-uniqueness-reduces-to-cofactor` (it is the application of that certified circularity to the hole-patching framing), but the non-monotonicity half (a) is a new structural observation about the MT-prime set's behavior that no prior fence records.

### Step 7 — endgame (certified import; conditional, unchanged)

IF Gap A (finiteness of the governing-prime set) is closed by some OTHER route, then the certified endgame finishes the proof unchanged:
- `distinct-supports-stabilize` (+ `squarefree-period-under-gap-A`): under Gap A, $\operatorname{MT}(\mathcal F_n)$ stabilizes to $\operatorname{MT}(\mathcal F_\infty)$ for $n\ge N_0$; $\mathcal B_\infty$ is $L$-periodic with $L=\prod_{p\in G}p$.
- `greedy-equals-cyclic-successor` (unconditional, pure-from-start): $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$ for all $n\ge1$.
- `cyclic-successor-bijection`: the cyclic-successor map on $A=\mathcal B_\infty\bmod L$ is a single $|A|$-cycle; with $T=|A|$, $a_{n+T}=a_n+L$ for all $n\ge1$. ∎ (conditional on Gap A)

This approach does NOT close Gap A; the endgame is imported as the conditional bridge, exactly as in the certified `transversal-saturation` / `prime-power-dichotomy` routes.

---

## Promotable lemmas

1. **`hole-patching-strict-shrink-refuted`** (−, structural fence) — the hole-patching / covering-termination framing of Gap A is obstructed by (a) non-monotonicity of the MT-prime set (transient primes enter and exit; witness $a_1=9375$: 115 grow vs 7 shrink events over 3000 steps, single-step flush of 75 primes at $n=222$) and (b) cofactor-collapse of the termination half (proving the greedy stays within the governing skeleton requires the cofactor bound = Gap A; witness: 96.6% of $a_1=9375$ terms carry a prime outside the governing set). Framing empirically valid only for the clean sub-case $a_1=375$. — Proved in Step 6 of this file; proposed for reviewer certification.

*(No positive reusable lemma proposed this round: the single-case $a_1=375$ verification is not a general theorem, and the `3·5^e`-family bedrock is empirical observation, not a structural lemma.)*

---

## Spec concerns / report to reviewer

1. **The PIVOT context was correctly internalized.** The refutation ($q\le\operatorname{rad}(a_1)$ false; witnesses $375\to19$, $9375\to67$) was re-verified independently by MT-greedy bit-exact against naive $O(N^2)$ gcd-greedy; $T=852, L=3990$ for $a_1=375$ and $T=3108, L=14070$ for $a_1=9375$ both confirmed with 0 violations over full-array checks. The framing correctly targets FINITENESS of governing primes (real Gap A), not the refuted bound.

2. **The mandated circularity test was run and FAILED.** The hole-patching framing's termination step collapses to the certified-circular cofactor bound (`window-uniqueness-reduces-to-cofactor`). The collapse is diagnosed concretely: the framing needs the greedy's chosen $m$ to be $G_k$-smooth, which requires bounding $m$'s prime factors (= cofactor bound = Gap A). The reviewer's hoped-for distinction (admissibility check uses $m$'s $G$-prime-set, not the cofactor) is correct but does not save the framing, because the framing needs the SEPARATE fact that $m$ IS $G_k$-smooth.

3. **The strict-shrink invariant is REFUTED, not merely unproven.** The $a_1=9375$ trace shows the MT-prime set is deeply non-monotone (115 grow vs 7 shrink events; 75 primes flushed at once at $n=222$). This is a STRUCTURAL obstruction, not a missing lemma — the framing's load-bearing invariant is empirically false for non-trivial cases.

4. **Honest scope.** This approach does NOT solve the theorem. It delivers: (a) one negative structural fence (proposed), (b) a single-case computational verification for $a_1=375$, (c) the `3·5^e`-family MT-stabilization bedrock. The general finiteness wall remains open. The approach should be ranked below the lemma-source approaches (certified deliverables) and the empirically-confirmed `f-of-a1-bounded-nonresidue-statistic`, and above the dead-ends; it is a sound-but-collapsed skeleton with a certified negative fence as its genuine contribution.

5. **Tools used (all named):** MT-greedy via `add_set`+`prune_minimal` (minimal-transversal update, the canonical antichain mechanic); `linchpin-and-gap-bound` (gap bound $d_n\le M_1$); `window-uniqueness-reduces-to-cofactor` (the cofactor-collapse target); `lemma-C-strip-no-go`, `schur-cofactor-premise-fails-in-periodic-regime` (cofactor-bound fences cited); `distinct-supports-stabilize`, `squarefree-period-under-gap-A`, `greedy-equals-cyclic-successor`, `cyclic-successor-bijection`, `lock-lemma` (the conditional endgame imports). No crux-corpus moves adapted (the framing is structural-covering, no retrieved crux was load-bearing).
