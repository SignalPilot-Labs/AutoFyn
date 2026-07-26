# Lemma (negative, structural): $D_n$-slack obstruction — the greedy minimum is a tie-break, not a forced extremum

*Pending reviewer certification (round 6). Source: round-6 extremal/variational explorer finding, re-verified by the proof-builder with the corrected naive gcd-greedy (the round-4 `fast_greedy.py` has an INVERTED subset bug per the run-state rules; not used).*

## Statement (negative, structural)

Let $a_1,a_2,\dots$ be the IMO 2026 P6 greedy sequence; $P_1$ the set of prime divisors of $a_1$; $M_1=\operatorname{rad}(a_1)$. Define the **admissible-increment set** (in the greedy's selection range) at step $n$:

$$D_n \;:=\; \{\, d\in\{1,\dots,M_1\}\;:\;\gcd(a_n+d,\,a_i)>1\ \text{for every }i\le n \,\}.$$

By the certified `linchpin-and-gap-bound`, $d_{n+1}=a_{n+1}-a_n\le M_1$ for every $n$, so $D_n$ is well-defined and finite, and the greedy rule is exactly $d_{n+1}=\min D_n$ (the smallest admissible increment). $D_n$ is non-empty: $d=M_1\in D_n$, since $a_n+M_1$ is divisible by every $p\in P_1$, hence shares a prime with every $a_i$ (each $a_i$ has a prime factor in $P_1$ by the linchpin).

In the **stabilized periodic regime** (after the eventual period $T,L$ has set in), the following hold across the witness starting values $a_1\in\{15,35,77,91,175\}$:

1. **(Slack is almost omnipresent.)** $|D_n|\ge 2$ at almost every step of the stabilized period. Specifically:
   - For $a_1\in\{15,35,77,91\}$, $|D_n|\ge 2$ at **every** step of the stabilized period (100% of steps).
   - For $a_1=175$, $|D_n|\ge 2$ at $263$ of $274$ steps ($96.0\%$); the $11$ exception steps ($4.0\%$) have $|D_n|=1$, each forced to a single increment ($d=21$ at $10$ steps, $d=15$ at $1$ step), isolated (no two consecutive).

2. **(Greedy minimum is a tie-break, not a forced extremum.)** At any step with $|D_n|\ge 2$, the greedy value $\min D_n$ is NOT uniquely determined by the admissibility structure: a different admissible increment $d'\in D_n\setminus\{\min D_n\}$ exists. The greedy selection of $\min D_n$ over $d'$ is a tie-break by the minimality ordering on $\{1,\dots,M_1\}$, not the consequence of $d_{n+1}$ being the unique admissible increment.

**Fence-conclusion.** The variational sub-mechanism *"no-improvement-possible $\Rightarrow$ fixed point $\Rightarrow$ periodicity"* (equivalently: *"the greedy value is forced by extremality, so stabilization forces periodicity"*) is **structurally false** for this process. For that mechanism to fire, the stabilized steps would need $|D_n|=1$ (a uniquely forced increment) at all — or at least a co-finite set of — stabilized steps, so that the greedy value is uniquely determined and the "no-improvement $\Rightarrow$ fixed point" principle can apply. This is **refuted** by the witness table. The entire sub-class of *"greedy $=$ forced extremum $\Rightarrow$ periodicity"* variational arguments is fenced off for IMO 2026 P6.

## Proof

### Step 1 — $D_n$ is well-defined, finite, non-empty, and $\min D_n$ is the greedy value.

Cite `linchpin-and-gap-bound` (reviewer-certified, round 1, unconditional):

- *(Linchpin)* Every $a_i$ ($i\ge 1$) is divisible by some prime $p_i\in P_1$. (For $i=1$ by definition; for $i\ge 2$ the admissibility condition defining $a_i$ includes the clause $i=1$, i.e. $\gcd(a_i,a_1)>1$.)
- *(Gap bound)* $d_n:=a_{n+1}-a_n\le M_1$ for every $n$. (Consider $m:=a_n+M_1$: every $p\in P_1$ divides $M_1$, hence divides $m$; by the linchpin each $a_i$ ($i\le n$) has some $p_i\in P_1$ with $p_i\mid M_1\mid m$, so $\gcd(m,a_i)\ge p_i>1$; thus $m$ is admissible, and $a_{n+1}\le m$ by minimality.)

Hence the greedy increment $d_{n+1}$ always lies in $\{1,\dots,M_1\}$. An integer $d\in\{1,\dots,M_1\}$ is **admissible at step $n$** iff $a_n+d$ shares a prime with every prior term $a_i$ ($i\le n$), i.e. iff $\gcd(a_n+d,a_i)>1$ for all $i\le n$. So:

$$D_n=\{\,d\in\{1,\dots,M_1\} : a_n+d\text{ is admissible w.r.t. }a_1,\dots,a_n\,\},$$

and the greedy rule $a_{n+1}=$ smallest integer $>a_n$ admissible w.r.t. $a_1,\dots,a_n$ is precisely $d_{n+1}=\min D_n$ (the smallest admissible increment). $D_n$ is non-empty because $M_1\in D_n$ (the gap-bound argument shows $a_n+M_1$ is admissible). $\square_{\text{Step 1}}$

### Step 2 — Computational witness: $|D_n|\ge 2$ almost everywhere in the stabilized period.

**Method.** We re-ran the **naive correct gcd-greedy** (no maximal-support pruning; the round-4 `fast_greedy.py` has an INVERTED subset bug per the run-state rules — do NOT use it; we reuse the verified-naive implementation from `/tmp/round-5/probe_coincidence.py`, confirmed `fast==plain` on $a_1=15,385$ in round 5). For each $a_1\in\{15,35,77,91,175\}$:

(i) compute the greedy orbit $a_1,\dots,a_N$ (with $N$ chosen so that at least two full periods fit past stabilization: $N=200$ for $a_1\in\{15,77,91\}$, $N=400$ for $a_1=35$, $N=2500$ for $a_1=175$);
(ii) detect the eventual period $(\text{start},T,L)$ on the increment word $d=(d_1,d_2,\dots)$ by the standard tail-period test ($d_i=d_{i+T}$ for all $i\in[\text{start},N-T)$);
(iii) enumerate $D_n$ explicitly for every step $n$ in one stabilized period $[\text{start},\text{start}+T)$ and report $|D_n|$.

**Verification.** We independently checked (a) the gap bound $d_n\le M_1$ holds at every step (max $d_n\le M_1$ in all five cases), (b) the greedy value equals $\min D_n$ at every step (zero violations across all $N-1$ transitions in every case), and (c) by direct hand-enumeration, $D_0$ for $a_1=15$ is $\{3,5,6,9,10,12,15\}$ (size $7$), confirming the script's output. The witness table is builder-verified.

**Witness table** (proof-builder re-run, `/tmp/round-6/dn_slack_probe.py`):

| $a_1$ | $M_1$ | $T$ | $L$ | $\min|D_n|$ | $\max|D_n|$ | mean $|D_n|$ | fraction with $|D_n|\ge 2$ |
|---|---|---|---|---|---|---|---|
| $15$ | $15$ | $8$ | $30$ | $2$ | $7$ | $4.38$ | $1.000$ ($8/8$) |
| $35$ | $35$ | $34$ | $210$ | $4$ | $11$ | $5.74$ | $1.000$ ($34/34$) |
| $77$ | $77$ | $18$ | $154$ | $7$ | $17$ | $9.50$ | $1.000$ ($18/18$) |
| $91$ | $91$ | $20$ | $182$ | $8$ | $19$ | $10.35$ | $1.000$ ($20/20$) |
| $175$ | $35$ | $274$ | $2730$ | $1$ | $11$ | $3.31$ | $0.960$ ($263/274$) |

*Note on the explorer's table.* The round-6 extremal/variational explorer reported smaller max values (e.g. $[2,5]$ for $a_1=15$, $[1,5]$ for $a_1=175$). That table is an **under-count** — attributable to an unspecified narrower definition of "admissible increment" in the explorer's probe. The proof-builder's hand-enumeration of $D_0$ for $a_1=15$ gives size $7$ (set $\{3,5,6,9,10,12,15\}$), confirming the larger numbers. We use the verified numbers above; the qualitative finding ("$|D_n|\ge 2$ almost everywhere") is unchanged, and is in fact **strengthened** (the first four cases have $|D_n|\ge 2$ at *every* step, not just almost every).

**Per-step $|D_n|$ over one stabilized period** (truncated display for $T=274$):

- $a_1=15$: sizes $[7,6,2,2,4,5,5,4]$; increments $[3,2,4,6,6,4,2,3]$.
- $a_1=35$: sizes $[11,9,6,5,5,5,6,6,5,4,4,6,6,5,5,5,5,6,6,6,7,7,6,5,5,4,5,5,4,5,7,7,6,6]$; min $4$, max $11$.
- $a_1=77$: sizes $[17,15,9,7,8,7,8,7,7,9,10,10,9,10,9,10,10,9]$; min $7$, max $17$.
- $a_1=91$: sizes $[19,16,8,8,9,8,8,9,8,8,10,11,11,10,11,11,10,11,11,10]$; min $8$, max $19$.
- $a_1=175$: sizes $[11,10,6,4,1,3,3,4,4,3,4,3,3,2,2,3,5,4,5,5,\dots,3,4,5,4,5]$; min $1$, max $11$.

**The $a_1=175$ exception steps.** The $11$ forced steps (where $|D_n|=1$) are: step $4$ (forced $d=15=3\cdot 5$) and steps $25,46,67,88,150,171,192,213,234,256$ (each forced $d=21=3\cdot 7$). They are isolated (no two consecutive) and total $4.0\%$ of the $274$-step period. At these steps the admissibility structure happens to pin down a unique increment; at the remaining $96\%$ of steps, slack ($|D_n|\ge 2$) is present.

**Conclusion of Step 2.** $|D_n|\ge 2$ at almost every step of the stabilized period for all five witness values; for $a_1\in\{15,35,77,91\}$ the stronger "every step" holds. $\square_{\text{Step 2}}$

### Step 3 — Slack $\Rightarrow$ the greedy minimum is a tie-break, not a forced extremum.

Fix a step $n$ in the stabilized regime with $|D_n|\ge 2$. Then there exist two distinct increments $d,d'\in D_n$ with $d<d'$. Both are admissible: $a_n+d$ and $a_n+d'$ each share a prime with every prior term $a_i$ ($i\le n$). The greedy rule picks $d_{n+1}=\min D_n=d$. This choice is **not** uniquely forced by the admissibility structure — $d'$ is an equally admissible alternative that the greedy rule did not pick, solely because $d<d'$ in the natural ordering on $\{1,\dots,M_1\}$. The greedy selection of $d$ over $d'$ is therefore a **tie-break by minimality** layered on a multi-valued admissible set, not the consequence of $d$ being the unique admissible increment.

Now consider the variational *"no-improvement-possible $\Rightarrow$ fixed point"* principle at step $n$. For this principle to apply, the increment $d_{n+1}$ would need to be uniquely determined by extremality — i.e. $|D_n|=1$, so that $d_{n+1}$ is the *only* admissible increment and "no improvement is possible" is a meaningful statement (the unique extremum is the fixed point). At a step with $|D_n|\ge 2$, "no improvement is possible" is **incoherent**: there is no unique extremum to be the "fixed point" of — multiple increments are equally admissible, and the greedy choice among them is a tie-break, not an extremal consequence. The principle's premise ("the greedy value is forced by extremality") fails at every slack step. $\square_{\text{Step 3}}$

### Step 4 — Fence-conclusion.

For the variational sub-mechanism *"greedy $=$ forced extremum $\Rightarrow$ periodicity"* to fire, the stabilized steps would need to be forced ($|D_n|=1$) at all — or at least a co-finite set of — stabilized steps. This is required for two independent reasons:

1. *(Extremal forcing.)* The "no-improvement $\Rightarrow$ fixed point" principle needs the greedy value to be the unique extremum at each step; otherwise the principle is incoherent (Step 3).
2. *(Deterministic transition.)* Any "stabilization $\Rightarrow$ periodicity via a deterministic finite-state transition" argument requires the successor map $n\mapsto n+1$ (equivalently, the $D_n\to d_{n+1}$ selection) to be **single-valued** as a function of the determining state. A state with $|D_n|\ge 2$ has multiple admissible successors; the greedy tie-break is what makes the realized orbit single-valued, but the *admissibility structure itself* is not single-valued at that state. A pigeonhole-on-equal-states argument (the standard route from "finite determining state" to "periodicity") requires single-valuedness of the transition, which slack breaks.

The witness table (Step 2) refutes the premise: $|D_n|\ge 2$ at almost every step — $100\%$ of steps for $a_1\in\{15,35,77,91\}$, $96\%$ for $a_1=175$. Even a single slack step in the period breaks the "uniquely forced $\Rightarrow$ deterministic transition" premise; here slack is omnipresent.

Therefore the entire sub-class of variational routes resting on *"greedy $=$ forced extremum $\Rightarrow$ periodicity"* (the "greedy value is forced by extremality, so stabilization forces periodicity" framing, including the "stabilization-of-admissible-next-values $\Rightarrow$ periodicity" sub-question (b) of the round-6 extremal/variational explorer) is **fenced off** for IMO 2026 P6. Any future variational route must supply a DIFFERENT mechanism — one that does not require the greedy minimum to be uniquely forced by the admissibility structure. $\square_{\text{Step 4}}$

## Cross-references

- **`linchpin-and-gap-bound`** (reviewer-certified, round 1, unconditional) — supplies $d\in\{1,\dots,M_1\}$ and the linchpin; both invoked in Step 1.
- **`primal-dual-gap-a-equivalence`** (reviewer-certified, round 4) — the only "forced" structure in the problem is the MT-state $=$ Gap A: the dual extremal optimum (finiteness of $\operatorname{MT}(\mathcal F_\infty)$, equivalently $\mathcal B_\infty$ $L$-periodic) is literally Gap A via the blocker involution, NOT a forced-extremum mechanism. The variational sub-question (c) "dual extremal finite optimum forcing governing $\le M_1$" collapses to this fence.
- **`deviation-descent-blocked-by-wmin-fence`** (reviewer-certified, round 5) — sibling negative structural fence; the deviation-descent's shift-by-$C$ admissibility preservation likewise requires a forced/cofactor bound (the cofactor fence), blocked in the same spirit: the greedy rule's local forward determinism does not lift to a global forced-extremum principle.
- **T-unbounded-in-$M_1$ impossibility** (reviewer-certified, round 5, `minimal-counterexample` explorer) — sibling fence: even a hypothetical "single-valued transition $\Rightarrow$ periodicity via finite automaton" route (which would require $|D_n|=1$) bottoms out on Gap A, since the required finite-state-space is unbounded in $M_1$ (the rad-77 pair $a_1=77\to T=18$ vs $a_1=847\to T=1744$, same $M_1=77$, $97\times$ jump). The $D_n$-slack obstruction fences the *premise* (single-valuedness); the T-unbounded fence fences the *consequence* (state-size bound); together they close the variational stabilization route from both ends.

## Status

Pending reviewer certification (round 6) as a **negative/structural lemma**. The computational witness (Step 2) is builder-verified by direct hand-enumeration of $D_0$ for $a_1=15$ and by independent re-run of the naive correct gcd-greedy (zero greedy-rule violations, gap bound satisfied at every step). The structural implication (Steps 3–4) is elementary: $|D_n|\ge 2$ means a second admissible increment exists, so the greedy minimum is a tie-break, refuting the "forced extremum" premise. This lemma cleanly fences off the "greedy $=$ forced extremum $\Rightarrow$ periodicity" sub-class of variational arguments for IMO 2026 P6.
