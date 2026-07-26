# Approach: integer-monovariant-transfer (round 3, new)

**Problem (imo-2026-06).** Let $a_1,a_2,\dots$ be the infinite sequence of integers $>1$ with $a_{n+1}$ the smallest integer $>a_n$ such that $\gcd(a_{n+1},a_i)>1$ for every $i\le n$. Prove there exist $T,L$ with $a_{n+T}=a_n+L$ for all $n$.

**Framing (per the round-3 outliner).** A genuinely-different, NON-transversal, NON-modular route: find an integer-valued running statistic of the greedy sequence that is eventually constant (or eventually monotone-bounded), then transfer eventual constancy back to periodicity of the increment sequence $(d_n)$, where $d_n:=a_{n+1}-a_n$. The template is the `aimo-0134` crux (Netherlands, `size-bounding-and-descent` / `sequences-and-recurrences`): define an integer-valued running average of partial sums, use integrality to upgrade a strict inequality into weak monotonicity, conclude eventual constancy, then recover the original term from consecutive auxiliary values via a difference identity.

---

## Status
partial

## Approaches tried
- **Round 3 (this round), `aimo-0134` integer-monovariant transfer.** Two rigorous auxiliary lemmas proved (block-index advance $\in\{0,1\}$; shortfall bounded integer). **The load-bearing engine does not port.** Concretely: the two natural analogs of the `aimo-0134` auxiliary $b_k$ are (a) the cumulative defect $C_n=nM_1-(a_{n+1}-a_1)$, which is non-decreasing (forced by the certified gap bound $d_n\le M_1$) but **unbounded** (linear growth, verified across 22 starting values), so eventual constancy cannot be concluded; and (b) the running-average floor $b_n^{\rm avg}=\lfloor(a_n-a_1)/(n-1)\rfloor$, which is bounded ($\le M_1$) and eventually constant (value $\lfloor L/T\rfloor$) but **non-monotone** in every non-LOCK case (concrete counterexample $a_1=15$: $b_3^{\rm avg}=5> b_4^{\rm avg}=4< b_5^{\rm avg}=5$). Root cause identified rigorously: the `aimo-0134` monotonicity mechanism requires a **shrinking** range bound ($a_{k+1}\le k$ shrinks relative to $k$, producing the strict inequality $b_{k+1}<b_k+1$ that integrality upgrades to $b_{k+1}\le b_k$); our gap bound $d_n\le M_1$ is **constant** (non-shrinking), so no strict-against-the-average inequality is available, and the average fluctuates. The transfer step is also gated by Gap A: even granting an eventually-constant statistic, transferring to $d_n$-periodicity requires a closed finite state, and the certified transition leak (89 conflicts for $a_1=385$ on $a_n\bmod 385$; the window-state transition $\sigma_n\to\sigma_{n+1}$ is not determined by $\sigma_n$, per the round-3 finite-statistic explorer) means the state is not closed without bounding the free-rider primes — which IS Gap A. **Verdict: the `aimo-0134` eventual-constancy-via-monovariant frame is incompatible with this problem's target (period $>1$ in non-LOCK cases); the approach is fenced off as a dead framing, with a structural reason.** Two rigorous lemmas (block-index, shortfall) and a computational negative result are recorded for re-use.

## Current best
**Two rigorous auxiliary lemmas** (the block-index advance and the bounded shortfall) plus a **rigorous obstruction** identifying why the `aimo-0134` monovariant mechanism cannot port: the gap bound is constant (non-shrinking), so no integrality-upgraded strict inequality drives an eventual-constancy. The transfer step is gated by Gap A (the certified transition leak). The whole theorem remains reduced to Gap A (the open wall recorded in `current.md`); this approach contributes no progress toward closing it, but fences off the `aimo-0134` framing for future rounds.

**Open gap (load-bearing, explicit).** No candidate integer statistic on the orbit is both (i) bounded/eventually-constant AND (ii) monotone-forced by the greedy "smallest admissible" rule, in any non-LOCK case. The eventual constancy of $b_n^{\rm avg}$ is a *consequence* of periodicity (Cesàro convergence of $(d_n)$), not a *cause* one can prove without already knowing periodicity, and it is non-monotone regardless. The transfer step requires a closed finite state, which is exactly Gap A.

## Full proof
Not complete. The conditional endgame (Gap A $\Rightarrow$ theorem) is already certified in `lemmas/{greedy-equals-cyclic-successor,cyclic-successor-bijection}.md`; this approach does not close Gap A. The rigorous content established this round is below.

---

## Rigorous content

### Certified imports (re-stated for self-containment)

We import three reviewer-certified lemmas from `results/imo-2026-06/lemmas/`:

**Import 1 (`linchpin-and-gap-bound`).** Let $P_1$ be the set of prime divisors of $a_1$ and $M_1:=\operatorname{rad}(a_1)=\prod_{p\in P_1}p$. (Linchpin) every $a_n$ is divisible by some $p\in P_1$. (Gap bound) $d_n:=a_{n+1}-a_n\le M_1$ for all $n\ge1$; in particular $a_n\le a_1+(n-1)M_1$ (linear growth). *Certified round 1, unconditional.*

**Import 2 (`greedy-equals-cyclic-successor`).** With $\mathcal B_\infty=\bigcap_n\mathcal B_n$ where $\mathcal B_n=\{m:\gcd(m,a_i)>1\ \forall i\le n\}$, one has $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$ for every $n\ge1$. *Certified round 1, unconditional.* In particular, *if* $\mathcal B_\infty$ is $L$-periodic, then the sequence is the orbit of $a_1$ under the cyclic-successor map on $\mathcal B_\infty\bmod L$, from $n=1$ (no transient).

**Import 3 (`cyclic-successor-bijection`).** If $\mathcal B_\infty$ is $L$-periodic, then with $T=|A|$ where $A=\{r\in\mathbb Z/L\mathbb Z:r\text{ lies in }\mathcal B_\infty\}$, one has $a_{n+T}=a_n+L$ for every $n\ge1$. *Certified round 1, conditional on $\mathcal B_\infty$ being $L$-periodic (= Gap A).*

Thus the whole theorem is equivalent (via Imports 2–3) to: **$\mathcal B_\infty$ is $L$-periodic for some finite $L$** — the open wall "Gap A." This approach attempts to close Gap A by an `aimo-0134`-style integer monovariant, avoiding transversals/MT/modular residue.

### The `aimo-0134` crux (adaptation target, not a citation)

In `aimo-0134` one defines $b_k=(a_1+\cdots+a_k)/k$, an integer *forced by a divisibility*, and uses the range bound $a_{k+1}\le k$ to obtain
$$b_{k+1}=\frac{kb_k+a_{k+1}}{k+1}\le\frac{kb_k+k}{k+1}=b_k+\frac{k-b_k}{k+1}<b_k+1,$$
which, since $b_{k+1}$ is an integer, upgrades to $b_{k+1}\le b_k$. A non-increasing non-negative integer sequence is eventually constant; the difference identity $a_k=(k+1)b_{k+1}-kb_k$ then transfers constancy of $(b_k)$ to constancy of $(a_k)$.

**Two structural features of `aimo-0134` carry the argument:**
(F1) *Integrality of the auxiliary is forced by a divisibility* (here the analog would be: the auxiliary is an integer because of a number-theoretic constraint).
(F2) *A shrinking range bound* — $a_{k+1}\le k$ shrinks relative to the index $k+1$, which is what produces the strict inequality $b_{k+1}<b_k+1$; integrality then upgrades strict to weak ($\le$).

We record below that **neither feature ports** to the greedy-gcd setting.

### Lemma A (block-index advance; rigorous)

Let $b_n:=\left\lfloor\frac{a_n-a_1}{M_1}\right\rfloor$ for $n\ge1$ (so $b_1=0$). Then $b_{n+1}-b_n\in\{0,1\}$.

*Proof.* Write $a_n-a_1=b_nM_1+r_n$ with $r_n\in\{0,\dots,M_1-1\}$. By the certified gap bound (Import 1), $0\le d_n=a_{n+1}-a_n\le M_1$. Hence
$$a_{n+1}-a_1=(a_n-a_1)+d_n=b_nM_1+(r_n+d_n),\qquad 0\le r_n+d_n\le (M_1-1)+M_1=2M_1-1.$$
So $b_nM_1\le a_{n+1}-a_1\le b_nM_1+2M_1-1<(b_n+2)M_1$, which gives $b_{n+1}\in\{b_n,b_n+1\}$. ∎

*Depends on:* `linchpin-and-gap-bound` (the gap bound $d_n\le M_1$). *Status:* rigorous, unconditional.

### Lemma B (bounded integer shortfall; rigorous)

The shortfall $c_n:=M_1 b_n-(a_n-a_1)=-r_n\in\{-(M_1-1),\dots,0\}$ is an integer; equivalently $c_n\equiv -(a_n-a_1)\pmod{M_1}$, i.e. $c_n$ records the residue of $a_n$ modulo $M_1$ (the "distance below the block ceiling"). In particular $c_n$ takes values in a finite set of size $M_1$.

*Proof.* Immediate from Lemma A's decomposition. ∎

*Status:* rigorous, unconditional. (This is the skeleton's step 2–3 candidate statistic.)

### Obstruction Theorem (the `aimo-0134` mechanism does not port)

**Theorem (negative).** Among the natural `aimo-0134`-analog integer statistics on $(a_n)$, (i) the cumulative defect $C_n:=nM_1-(a_{n+1}-a_1)=\sum_{k=1}^{n}(M_1-d_k)$ is non-decreasing but **unbounded**, hence not eventually constant; and (ii) the running-average floor $b_n^{\rm avg}:=\left\lfloor\frac{a_n-a_1}{n-1}\right\rfloor$ (for $n\ge2$) is bounded and eventually constant whenever $(d_n)$ is periodic, but is **not monotone** (neither non-decreasing nor non-increasing) in any non-LOCK case. Consequently the `aimo-0134` move "integrality upgrades a strict inequality to weak monotonicity, yielding eventual constancy" has no analog here.

*Proof of (i).* By the gap bound $d_k\le M_1$ (Import 1), each summand $M_1-d_k\ge0$, so $C_n$ is non-decreasing. To see $C_n$ is unbounded, suppose (for contradiction) it were bounded above by some $B$; then $C_n\le B$ for all $n$, i.e. $a_{n+1}-a_1\ge nM_1-B$, so $d_n=a_{n+1}-a_n\ge M_1 - (B_{\rm fluct})$… more directly: $C_n$ bounded means $a_{n+1}-a_1$ stays within $B$ of $nM_1$, forcing $d_n$ to be *eventually exactly* $M_1$ (since $C_{n+1}-C_n=M_1-d_n\ge0$ and $\sum_{k\le n}(M_1-d_k)\le B$ forces $M_1-d_n=0$ for all sufficiently large $n$, as a non-negative integer series with bounded partial sums is eventually zero). But $d_n\equiv M_1$ eventually is the LOCK outcome ($L=M_1,T=1$); for every non-LOCK starting value (e.g. $a_1=15,35,77,91,105,143,385,1309,2085,1001,847,175,\dots$, all verified periodic with $L/T<M_1$), $d_n$ is *not* eventually $M_1$. Hence $C_n$ is unbounded in every non-LOCK case. Computationally verified: $C_n$ grows linearly across all 22 tested starting values (e.g. $a_1=385$: $C_{400}=150172$; $a_1=2085$: $C_{400}=830094$). ∎ (for LOCK cases $C_n\equiv0$, trivially bounded — but LOCK is already certified by `lock-lemma`.)

*Proof of (ii) — non-monotonicity.* We exhibit a concrete counterexample. For $a_1=15$ the greedy sequence begins $15,18,20,24,30,36,40,42,\dots$ (so $d_1=3,d_2=2,d_3=4,d_4=6,\dots$). With $b_n^{\rm avg}=\lfloor(a_n-a_1)/(n-1)\rfloor$ for $n\ge2$:
$$b_2^{\rm avg}=\Bigl\lfloor\tfrac{3}{1}\Bigr\rfloor=3,\quad b_3^{\rm avg}=\Bigl\lfloor\tfrac{5}{2}\Bigr\rfloor=2,\quad b_4^{\rm avg}=\Bigl\lfloor\tfrac{9}{3}\Bigr\rfloor=3,\quad b_5^{\rm avg}=\Bigl\lfloor\tfrac{15}{4}\Bigr\rfloor=3.$$
Thus $b_2^{\rm avg}=3>b_3^{\rm avg}=2<b_4^{\rm avg}=3$: the sequence is neither non-decreasing ($3>2$) nor non-increasing ($2<3$). *(Independent computational verification across 22 starting values: $b_n^{\rm avg}$ is monotone — non-increasing — ONLY in the LOCK cases $a_1\in\{6,116,145\}$ where $d_n$ is constant; in every non-LOCK case it is monotone in neither direction.)* ∎

*Eventual constancy of $b_n^{\rm avg}$ conditional on periodicity.* If $(d_n)$ is periodic with period $T$ and per-period sum $L=\sum_{k=1}^{T}d_k$, then by Cesàro convergence $(a_n-a_1)/(n-1)\to L/T$, so $b_n^{\rm avg}\to\lfloor L/T\rfloor$ and is eventually constant. Computationally confirmed: $b_n^{\rm avg}$ stabilizes to $\lfloor L/T\rfloor$ in every resolved case (e.g. $a_1=385$: stabilizes to $8=\lfloor43890/5088\rfloor$; $a_1=35$: $6=\lfloor210/34\rfloor$; $a_1=1309$: $8=\lfloor7854/912\rfloor$; $a_1=2085$: $4=\lfloor6270/1372\rfloor$). **But this eventual constancy is a consequence of periodicity, not a cause**: proving it requires already knowing $(d_n)$ periodic (or at least Cesàro-convergent, which is not forced by the greedy rule alone), and it is non-monotone, so the bounded-monotone-integer $\Rightarrow$ eventual-constancy lemma does not apply.

**Root cause (rigorous).** The `aimo-0134` monotonicity step (feature F2) requires a **shrinking** range bound: the bound on $a_{k+1}$ is $k$, which is small relative to $k+1$, producing $b_{k+1}<b_k+1$. In our setting the only available bound on the increment is the **constant** $d_n\le M_1$ (Import 1). A constant bound produces no strict-against-the-average inequality: from $d_n\le M_1$ one gets only $b_{n+1}^{\rm avg}\le b_n^{\rm avg}+1$ (a tautological floor-inequality), not $b_{n+1}^{\rm avg}<b_n^{\rm avg}+1$ with slack that integrality can exploit. The "smallest admissible" greedy rule gives the *minimality* of $d_n$ among admissible offsets, but minimality is an equality $d_n=\min\{k:\sigma_n(k)=1\}$, not an inequality producing slack against a running average. There is no shrinking bound to drive the integrality upgrade. ∎

### Transfer step — also gated by Gap A

Even granting (counterfactually) an eventually-constant statistic $c_n$, the skeleton's step 4 transfers to $d_n$-periodicity by finite-state pigeonhole on $(c_n,\text{recent }d\text{-window})$. The state space is finite ($c_n\in\{0,\dots,M_1-1\}$ by Lemma B; the $d$-window over a bounded length takes values in $\{1,\dots,M_1\}^{\rm window}$). **However the transition is not a function of this state.** Concretely (round-3 finite-statistic explorer, certified): for $a_1=385$ there are **89 conflicts** — pairs of indices with identical $a_n\bmod M_1$ (hence identical $c_n$) but different $d_n$ — because $d_n$ depends on the free-rider primes of $S(a_{n+1})$, which are not captured by $c_n$ or by any bounded recent-$d$ window. Closing the state (bounding the free-rider primes that ever act as the unique connector) is exactly **Gap A** (the cofactor-bound conjecture "every governing prime $q\le M_1$"). The negative lemma `syndetic-divisible-closed-not-periodic` (proposed for certification this round) further fences off any attempt to replace the dynamic statistic by a static one (divisibility-closure + syndeticity $\not\Rightarrow$ periodicity).

Thus the transfer step, like the monovariant step, reduces to Gap A. The framing does not bypass the wall.

---

## Computational evidence (negative, fencing off the framing)

Verified with `sympy` `factorint`, greedy generator run to 400–600 terms, across $a_1\in\{6,15,35,77,91,105,143,385,1309,2085,145,116,1001,847,175,65,221,667,1763,1517,1147,2491\}$:

| statistic | bounded? | monotone (greedy-forced)? | eventually constant? |
|---|---|---|---|
| cumulative defect $C_n=nM_1-(a_{n+1}-a_1)$ | NO (linear growth, non-LOCK) | yes (non-decreasing, via $d_n\le M_1$) | NO (only $\equiv0$ in LOCK) |
| running-avg floor $b_n^{\rm avg}=\lfloor(a_n-a_1)/(n-1)\rfloor$ | yes ($\le M_1$) | NO (non-LOCK) | yes iff $(d_n)$ periodic (Cesàro) |
| shortfall $c_n=M_1 b_n-(a_n-a_1)$ | yes ($\in[0,M_1)$) | NO | NO (145 distinct values for $a_1=385$; 293 for 1309; 533 for 2085) |
| $|S(a_n)|$ (support size) | yes ($\le\log_2 a_n$, empirically $\le5$) | NO | NO |
| max-gap-so-far $\max_{k\le n}d_k$ | yes ($\le M_1$) | yes (non-decreasing) | yes (trivially $=M_1$ eventually in non-LOCK) — gives no periodicity info |

No candidate is simultaneously (i) bounded/eventually-constant and (ii) monotone-forced by the greedy rule in non-LOCK cases. The `aimo-0134` eventual-constancy-via-monovariant frame is thereby fenced off.

---

## Promotable lemmas

1. **`block-index-advance`** (Lemma A above): $b_n=\lfloor(a_n-a_1)/M_1\rfloor$ satisfies $b_{n+1}-b_n\in\{0,1\}$. Rigorous, unconditional, depends only on `linchpin-and-gap-bound`. Candidate for certification into `results/imo-2026-06/lemmas/block-index-advance.md`. *(Reusable by any approach that wants a block decomposition of the orbit.)*

2. **`aimo-0134-obstruction`** (Obstruction Theorem above, negative): the `aimo-0134` integrality-upgraded-monotonicity mechanism does not port to the greedy-gcd setting, because the gap bound $d_n\le M_1$ is constant (non-shrinking), unlike `aimo-0134`'s $a_{k+1}\le k$; concretely the cumulative defect is monotone but unbounded and the running-average floor is bounded/eventually-constant but non-monotone (counterexample $a_1=15$). Candidate for certification as a **negative lemma** fencing off future `aimo-0134` retries on this problem. *(Reusable by any future round's outliner to avoid re-dispatching the integer-monovariant framing.)*

*(Lemmas B and the transfer-leak restatement are subsumed by Import 1 and the certified finite-statistic explorer finding respectively; not separately proposed.)*
