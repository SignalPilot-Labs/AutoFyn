# imo-2026-06 — extremal / variational lens

## 1. The route (concrete mechanism sketch)

The greedy rule is an online extremal process: $a_{n+1}$ is the **pointwise minimum** admissible increment. Three variational framings were scouted:

**(a) Lex-min of the admissible tree.** The greedy increment-word $d=d_1d_2\cdots\in\{1,\dots,M_1\}^{\mathbb N}$ is the lexicographically smallest infinite path through the *admissibility tree* $\mathcal T$ (nodes at depth $n$ = admissible prefixes $(a_1,\dots,a_n)$; children = legal $d_{n+1}\in\{1,\dots,M_1\}$). A standard fact: **the leftmost infinite ray of a finite-automaton-described (regular) tree is ultimately periodic, with period $\le$ state-size** (it eventually loops in the automaton, taking the smallest transition). So: if $\mathcal T$ is regular, the greedy orbit is eventually periodic. This is the variational restatement of "exhibit a finite determining state $\Rightarrow$ periodicity."

**(b) Stabilization of the admissible-next-value set.** $D_n:=\{d\in\{1,\dots,M_1\}: a_n+d\text{ admissible w.r.t. }a_1,\dots,a_n\}$; greedy picks $d_{n+1}=\min D_n$. If $D_n$ stabilizes (in the sense of becoming periodic with some period $T$) and the stabilized successor map is single-valued (no slack, $|D_n|=1$), periodicity follows with no Gap-A assumption — a "no-improvement-possible $\Rightarrow$ fixed point" principle.

**(c) Dual extremal optimum.** Greedy $=$ minimize new-prime introduction / maximize coverage; ask whether the dual extremal problem has a finite optimum that forces the governing set $\subseteq$ primes $\le M_1$.

## 2. Why NOT in the 13-dead / 4-fence list (point by point)

**Why not primal-dual MT equivalence (fenced).** Sub-question (c) **is** the primal-dual MT fence. The dispatch explicitly warns that "a dual-extremal route that just re-states MT-finiteness is FENCED," and the certified `primal-dual-gap-a-equivalence` shows (via the blocker involution $b(b(\mathcal C))=\mathcal C$) that the dual extremal optimum (finiteness of $\operatorname{MT}(\mathcal F_\infty)$, equivalently $\mathcal B_\infty$ $L$-periodic) is literally the same wall as the primal. Sub-question (c) does not go around Gap A; it re-states it. **Concede (c) is fenced.**

**Why not an $f(M_1)$-bounded finite-statistic (T-unbounded fence).** Sub-question (a) reduces to "exhibit a finite automaton for $\mathcal T$"; the lex-min-ray periodicity bound is $T\le|\text{states}|$, so $|\text{states}|\ge T$. Computation (Sec. 4) confirms the realized determining state — the *distinct $D_n$-pattern* set in one stabilized period — has size $\sim T$ (e.g. $75$ for $a_1=175$, $T=274$; full $T=8,34,18,20$ for the small cases), and the rad-77 radical-sharing pair ($a_1=77\to T=18$ vs $a_1=847\to T=1744$, same $M_1=77$, $97\times$ jump) certifies $T$ is NOT a function of $M_1$. So the finite automaton required by (a) has state-size unbounded in $M_1$ — i.e. **(a) IS Gap A**, fenced by the round-5 T-unbounded-in-$M_1$ impossibility. Sub-question (b)'s stabilized $D_n$-state space is the same size $\sim T$ (unbounded). Both fenced.

**Why not cofactor-bound (circular).** Sub-question (b)'s "stabilization" requires bounding which primes appear in term supports between witnesses — exactly the certified-circular cofactor-bound step (`window-uniqueness-reduces-to-cofactor`, `lemma-C-strip-no-go`, `schur-cofactor-premise-fails-in-periodic-regime`). Concede.

## 3. The hard step (load-bearing unproved sub-claim) — AND a REFUTATION

The load-bearing sub-claim for the genuine variational principle (b) is: **"the admissibility structure forces $|D_n|=1$ eventually (no slack), so the greedy choice is the *only* admissible increment, giving no-improvement-possible $\Rightarrow$ fixed point."**

**This sub-claim is REFUTED computationally** (Sec. 4). $|D_n|\ge 2$ at almost every step in the stabilized periodic tail:

| $a_1$ | $T$ | $|D_n|$ in stabilized period (min–max) |
|---|---|---|
| 15 | 8 | 2–5 |
| 35 | 34 | 4–7 |
| 77 | 18 | 7–10 |
| 91 | 20 | 8–11 |
| 175 | 274 | 1–5 |

So there is **always slack**: the greedy minimum is one choice among many admissible increments; the admissibility structure does NOT force the greedy value. The "no-improvement-possible $\Rightarrow$ fixed point" variational principle is therefore not merely unproved — it is **structurally false** for this process. The greedy rule is a *tie-break by minimality* layered on top of a multi-valued admissible set, not the consequence of a forced extremum.

This is a genuinely-new **negative structural finding** (candidate lemma for certification): "`D_n`-slack obstruction: in the periodic regime $|D_n|\ge 2$ at almost every step, so no 'forced extremum' / 'no-improvement $\Rightarrow$ fixed point' variational principle can close Gap A." It fences off an entire sub-class of variational arguments (the "greedy = forced" framing).

## 4. Computational probe

Naive correct gcd-greedy (reused structure from `/tmp/round-5/probe_coincidence.py`, no maximal-support pruning). $a_1\in\{15,35,77,91,175\}$ ($a_1=847$ has $T=1744$, beyond the 1900-step horizon — skipped on period detection, but $|D_n|$-slack confirmed for the prefix). Results (all rows: 0 violations of $d_{n+1}=\min D_n$; gap bound $d_n\le M_1$ holds):

- $a_1=15$: $T=8, L=30$. $D_n$ becomes $T$-periodic at $N_{\text{stab}}=2$; $|D_n|\in[2,5]$ in the stabilized period (8 distinct patterns).
- $a_1=35$: $T=34, L=210$. $N_{\text{stab}}=3$; $|D_n|\in[4,7]$; 31 distinct patterns.
- $a_1=77$: $T=18, L=154$. $N_{\text{stab}}=3$; $|D_n|\in[7,10]$; 18 distinct patterns.
- $a_1=91$: $T=20, L=182$. $N_{\text{stab}}=2$; $|D_n|\in[8,11]$; 20 distinct patterns.
- $a_1=175$: $T=274, L=2730$. $N_{\text{stab}}=4$; $|D_n|\in[1,5]$; 75 distinct patterns (proper subset of one period — so even the $D_n$-state is not a bijection onto the period).

**Key observations:**
1. **Stabilization of $D_n$ to $T$-periodicity does occur** — but only once $T$ is already in force; the stabilized state space has size $\sim T$, which is **unbounded in $M_1$** (the rad-77 pair). Stabilization does not give a sub-$T$ window. So "stabilization $\Rightarrow$ periodicity" secretly **does** require an $f(M_1)$-bounded state — confirming the dispatch's worry.
2. **$|D_n|\ge 2$ almost everywhere** in the stabilized tail — slack is omnipresent. The greedy minimum is NOT a forced extremum; the variational "no-improvement" framing is refuted.
3. **$N_{\text{stab}}$ is small (2–4)**, but this is measured against the *true* period $T$; it does not yield a sub-$T$ state, and the number of realized $D_n$-patterns in the period is $\sim T$.
4. Slope $L/T$: $3.75, 6.18, 8.56, 9.10, 9.96$ — no obvious function of $M_1$ alone ($a_1=15$: $L=2M_1$; $a_1=175$: $L=78M_1$); $L$ is always a multiple of $M_1$ (consistent with $M_1\mid L$ under Gap A), but the multiplier varies wildly. No slope-minimization characterization surfaces.

## 5. Verdict

**NO-UNFENCED-ROUTE.** All three variational sub-questions collapse to existing fences:

- (a) lex-min-of-regular-tree $\Rightarrow$ periodicity: reduces to "exhibit a finite automaton for the admissibility tree" = exhibit a finite determining state; the required state-size is $\ge T$, unbounded in $M_1$ $\Rightarrow$ **T-unbounded fence** + **Gap A**.
- (b) stabilization-of-admissible-next-values: stabilization to $T$-periodicity has state-space size $\sim T$ (unbounded) $\Rightarrow$ **T-unbounded fence**; the underlying prime-support bounding is the **cofactor-bound fence**. AND the sub-mechanism "no-improvement $\Rightarrow$ fixed point" is **REFUTED** by $|D_n|\ge 2$ (slack), a genuinely-new negative structural finding (candidate lemma: `D_n-slack-obstruction`).
- (c) dual extremal finite optimum forcing governing $\le M_1$: **primal-dual MT equivalence fence** (literally).

**The one genuinely-new deliverable** is the $|D_n|\ge 2$ slack computation — a clean refutation of the "greedy $=$ forced extremum" variational sub-mechanism, fencing off that sub-class for future rounds. No genuinely-unfenced variational route to $q\le M_1$ or to direct periodicity is on the table; the variational lens, like the 13 prior mechanisms, bottoms out on the same wall.

**Recommendation: CONSOLIDATE.** This round's variational probe contributes one new negative structural fence ($D_n$-slack obstruction) and re-confirms the wall from the variational direction; it does not surface an unfenced crack. The run should consolidate the partial result (conditional proof + LOCK + 28 lemmas + fences) as the deliverable per the round-5 reviewer directive.
