# IMO 2026 Problem 6 — approach `pstar-core-straggler`

**Problem.** Let $a_1,a_2,\ldots$ be an infinite sequence of integers $>1$ such that $a_{n+1}$ is the smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for every $i\le n$. Prove there exist $T,L>0$ with $a_{n+T}=a_n+L$ for all $n\ge1$.

**Framing (mechanism — structural Cov-monovariant / restricted-common-prime core collapse).** This is the genuinely-different framing of the saturated-regime wall. It does **NOT** bound entering primes by value and does **NOT** route through SPT (every minimal has a prime $\le p^*$). Instead it bounds the **crash primes** — the primes $p$ that appear in $\{2,p\}$-type minimal members — to the finite set $P(a_1)$, via a bounded monotone subset (the *coverage* $\mathrm{Cov}(\mathcal M_n)\subseteq P(a_1)$), and caps the number of $\{2,p\}$-crashes by $|P(a_1)|$. The entering large primes ($167, 179, 503, \ldots$) are **free-riders evicted by crashes**, never persisting; they need not be bounded.

The freeze regime (F) is **imported, not re-proved** (`freeze-lock`, `singleton-freeze`, `common-primes-bounded`). Only the saturated branch (S) is attacked here.

**Honest summary of this build.** The structural shell (case split, 2-entry, Cov-monovariant, terminal self-blocking criterion, freeze import, $\delta$ finish) is **proved in full** below; it is SPT-free and value-free. The genuinely hard piece — **termination of the saturated regime after $\mathrm{Cov}$ stabilizes** — remains an explicit open wall (GAP-S'). Moreover, the outline's original Lemma C ("a $\{2,p\}$ crash is *forced* until $\mathrm{Cov}=P(a_1)$") is **refuted** by counterexample (Lemma C-ref below): several seeds terminate self-blocking with $\mathrm{Cov}\subsetneq P(a_1)$. The Cov-monovariant is therefore a *partial* invariant (it bounds $\{2,p\}$-crashes, not all crashes); it does not by itself close the wall. The reviewer's straggler-prime sub-claim concern is addressed in §5: it is *not* needed for the Cov-monovariant, and the lemma it fed is refuted, so it is moot.

---

## Status
partial

## Approaches tried
- **Round 4 (this build, first outline).** Opened the structural Cov-monovariant framing of the saturated wall, distinct from the SPT/density route (α), the mtp finite-state route (γ), and the analytic smooth-density route (`smooth-window-crash`). Freeze branch imported.
- **Round 4 (this build, filled in).** Proved in full: the case split, Lemma A (2-entry: $a_2=a_1+\min P(a_1)$ is even), Lemma B (Cov-monovariant: $\mathrm{Cov}\subseteq P(a_1)$ is monotone non-decreasing in regime (S) via a clean refinement obstruction — $\{2,p\}$'s only proper nonempty subsets are $\{2\},\{p\}$, both singleton-freeze/regime-(F) events), the crash-count bound ($\le|P(a_1)|$) and crash-primes-$\subseteq P(a_1)$, Lemma D (star+straggler self-blocking as a *sufficient* terminal), and the $\delta$ finish (imported). **Refuted** the outline's original Lemma C (crash-to-full-star) by counterexample: $a_1\in\{35,143,175,323,385,4199\}$ terminate self-blocking with $\mathrm{Cov}\subsetneq P(a_1)$. **Wall remaining (GAP-S'):** after $\mathrm{Cov}$ stabilizes at $\bar C\subseteq P(a_1)$ (no further $\{2,p\}$-crashes), prove the saturated regime still terminates (reaches *some* self-blocking family) — this is the same hard wall as α's GAP-S; the framing bounds the $\{2,p\}$-crashes SPT-free but does not bound the remaining crashes. **Sub-gap (GAP-A):** the core $\mathcal M_n^*$ stays nonempty throughout regime (S) — verified 0 violations on 17 saturated seeds, unproved. All key structural claims computationally verified on $\sim$18 seeds.

## Current best
The **Cov-monovariant** (Lemma B) is proved in full (SPT-free, unconditional within regime (S)): $\mathrm{Cov}(\mathcal M_n)=\{p\in P(a_1):\{2,p\}\in\mathcal M_n\}$ is monotone non-decreasing and $\subseteq P(a_1)$, hence stabilizes after $\le|P(a_1)|$ $\{2,p\}$-crashes; crash primes are $\subseteq P(a_1)$ (finite by $a_1$'s factorization). Together with the imported freeze branch, the imported $\delta$ finish, and the proved star+straggler self-blocking terminal (Lemma D), this reduces the saturated-regime wall to **proving termination after $\mathrm{Cov}$ stabilizes** (GAP-S'). The original "crash forced to $\mathrm{Cov}=P(a_1)$" Lemma C is refuted (Lemma C-ref); termination can occur at $\mathrm{Cov}\subsetneq P(a_1)$ via a richer self-blocking family. The wall is thus *broader* than the outline hoped — the Cov-monovariant is a genuine partial invariant, not a wall-closer.

## Full proof
*(Branch (F) complete, imported; branch (S) reduced to GAP-S'.)*

### 0. Notation and imports

For $m>1$ write $P(m)$ for the (nonempty) set of prime divisors of $m$. The admissibility rule at step $n+1$ is
$$\gcd(a_{n+1},a_i)>1\ \forall i\le n \iff P(a_{n+1})\cap P(a_i)\neq\emptyset\ \forall i\le n.$$
Let $\mathcal F_n=\{P(a_1),\ldots,P(a_n)\}$ and $\mathcal M_n=\min_{\subseteq}\mathcal F_n$ (the $\subseteq$-minimal members). A set of primes hits $\mathcal F_n$ iff it hits $\mathcal M_n$ (a non-minimal member contains a minimal one), so the admissible integers at step $n+1$ are
$$V_n=\{m>0:\ P(m)\text{ meets every }M\in\mathcal M_n\},\qquad a_{n+1}=\min\{m\in V_n:m>a_n\}.$$
Let $C_n=\bigcap_{M\in\mathcal M_n}M$ (the **common primes** at time $n$). Let $\mathcal M=\min\{P(a_i):i\ge1\}$ (the final family; finiteness is the wall) and $P=\bigcup_{M\in\mathcal M}$.

**Refinement dynamics** (used throughout). When $P(a_{n+1})$ is added to $\mathcal F_n$:
- if some $M\in\mathcal M_n$ satisfies $M\subseteq P(a_{n+1})$, then $P(a_{n+1})$ is dominated and $\mathcal M_{n+1}=\mathcal M_n$;
- otherwise $P(a_{n+1})$ is a new minimal and every old member $M\supsetneq P(a_{n+1})$ is removed, so $\mathcal M_{n+1}=(\mathcal M_n\setminus\{M:P(a_{n+1})\subsetneq M\})\cup\{P(a_{n+1})\}$.

A **promotion** is a step with $\mathcal M_{n+1}\neq\mathcal M_n$ (a new minimal entered). A **crash** is a promotion whose new minimal $P(a_{n+1})$ refines (is a proper subset of) at least one old member.

**Imports (reviewer-certified, in `lemmas/`; not re-proved).**
- `pairwise-intersection`: $P(a_i)\cap P(a_j)\neq\emptyset$ for all $i,j$; hence $\mathcal M_n$ is pairwise-intersecting.
- `common-primes-bounded`: $C_n\subseteq P(a_1)$ for every $n$ (every common prime divides $a_1$).
- `freeze-lock`: if $p\mid a_n$, $p\in C_n$, $p\in C_{n+1}$, then $a_{n+1}=a_n+p$.
- `singleton-freeze`: if $\{p\}\in\mathcal M_n$, then $\mathcal M_m=\mathcal M_n$ for all $m\ge n$.
- `mtp-monovariant-and-gap-bound`: $\mathrm{mtp}(\mathcal M_n):=\min\{\prod_{p\in T}p:T\text{ transversal of }\mathcal M_n\}$ is monotone non-decreasing and $a_{n+1}-a_n\le\mathrm{mtp}(\mathcal M_n)$.
- `Sat-criterion`: if $\mathcal M_n$ is self-blocking (every transversal contains a member of $\mathcal M_n$), then $\mathcal M_m=\mathcal M_n$ for all $m\ge n$ (frozen, hence $\mathcal M$ finite).
- `post-stabilization-theorem` (conditional on $\mathcal M$ finite): $a_{n+T}=a_n+L$ for all $n\ge1$ with $L=\prod_{p\in P}p$ (squarefree) and $T=|V|$.

### 1. Trivial collapses and case split (imported)

If $a_1=p^k$ is a prime power, $P(a_1)=\{p\}$, so $\{p\}\in\mathcal M_1$ and `singleton-freeze` gives $\mathcal M=\{\{p\}\}$ finite, $T=1,L=p$. Hence assume $a_1$ has $\ge2$ distinct prime factors. By `common-primes-bounded`, the only primes that can ever be common are in $P(a_1)$. The case split is exhaustive (excluded middle on "some factor of $a_1$ is permanently common"):
- **(F) Freeze regime:** some $p\in P(a_1)$ satisfies $p\in C_n$ for all $n\ge1$.
- **(S) Saturated regime:** every $p\in P(a_1)$ is absent from $C_n$ for some $n$ (no factor of $a_1$ is permanently common).

Branch (F) is solved end-to-end by import (`freeze-lock` $\Rightarrow$ $a_{n+1}=a_n+p$ $\Rightarrow$ AP $a_n=p(c+n-1)$ hits $p^k$ at $n=p^{k-1}-c+1$ $\Rightarrow$ $\{p\}$ dominates every minimal (each contains $p$) $\Rightarrow$ $\mathcal M_n=\{\{p\}\}$ $\Rightarrow$ `singleton-freeze` $\Rightarrow$ $\mathcal M=\{\{p\}\}$ finite $\Rightarrow$ `post-stabilization-theorem` gives $a_{n+1}=a_n+p$). **Henceforth assume (S).**

A consequence of (S), used repeatedly: **no singleton $\{p\}$ ever appears** (for $p\in P(a_1)$, a singleton $\{p\}\in\mathcal M_n$ would make $p\in C_n$ and then `singleton-freeze` would keep $p$ common forever — contradicting (S); for $p\notin P(a_1)$, $p\in C_n$ is impossible by `common-primes-bounded`). Also, **$2$ is never common** whenever $2\notin P(a_1)$: `common-primes-bounded` gives $C_n\subseteq P(a_1)\not\ni 2$, so $2\notin C_n$ for all $n$. (When $2\in P(a_1)$, the regime-(S) hypothesis says $2$ is not *permanently* common; the singleton $\{2\}$ is still excluded by the previous sentence, since it would freeze and make $2$ permanently common.)

### 2. Lemma A — $2$ enters (or is present from the start) and the core is initially nonempty

Define the **core** and the **straggler** at time $n$:
$$\mathcal M_n^*:=\{M\in\mathcal M_n:2\in M\}\ (\text{core}),\qquad \mathcal M_n^{\circ}:=\{M\in\mathcal M_n:2\notin M\}\ (\text{straggler}).$$
By definition $2\in\bigcap_{M\in\mathcal M_n^*}M$ (trivial: core members are exactly those containing $2$). The substantive content is that the core is nonempty initially.

**Lemma A (2-entry).** *If $a_1$ has $\ge2$ distinct prime factors, then $2\in\bigcup\mathcal M_n$ for some $n\le2$; equivalently the core is nonempty at time $1$ or $2$.*

*Proof.* Two cases.
- $2\in P(a_1)$ (i.e. $a_1$ even). Then $M_1:=P(a_1)\in\mathcal M_1$ (it is the only member) and $2\in M_1$, so $\mathcal M_1^*\neq\emptyset$.
- $2\notin P(a_1)$ (i.e. $a_1$ odd). Let $p^*=\min P(a_1)$ (odd, $\ge3$). We claim $a_2=a_1+p^*$, which is even. First, $a_1+p^*$ is admissible: $p^*\mid a_1$ and $p^*\mid p^*$, so $p^*\mid a_1+p^*$, hence $P(a_1+p^*)\cap P(a_1)\ni p^*\neq\emptyset$; and $a_1+p^*>a_1$. So $a_2\le a_1+p^*$. Conversely, take any $m$ with $a_1<m<a_1+p^*$ and suppose $P(m)\cap P(a_1)\neq\emptyset$; pick $q\in P(m)\cap P(a_1)$. Then $q\mid a_1$ and $q\mid m$, so $q\mid m-a_1$. But $0<m-a_1<p^*\le q$ (as $q\in P(a_1)$, $q\ge p^*=\min P(a_1)$), and no positive multiple of $q$ is $<q$. Contradiction. So no such $m$ is admissible, and $a_2=a_1+p^*$. Since $a_1$ and $p^*$ are both odd, $a_2$ is even, i.e. $2\in P(a_2)$.

  It remains to see $P(a_2)$ is a minimal member of $\mathcal F_2=\{P(a_1),P(a_2)\}$ containing $2$. We have $2\in P(a_2)$, $2\notin P(a_1)$. If $q\in P(a_1)\setminus\{p^*\}$, then $q\mid a_1$ but $q\nmid a_1+p^*$ (else $q\mid p^*$, forcing $q=p^*$ as both are prime), so $q\notin P(a_2)$; thus $P(a_1)\nsubseteq P(a_2)$. Also $P(a_2)\nsubseteq P(a_1)$ since $2\in P(a_2)\setminus P(a_1)$. Hence neither member of $\mathcal F_2$ contains the other, so both are minimal: $\mathcal M_2=\{P(a_1),P(a_2)\}$, and $P(a_2)\in\mathcal M_2^*$ is nonempty. ∎

**Remark (computational).** Verified on $a_1\in\{15,35,77,105,143,175,323,385,1001,1155,1365,2145,5005,4199,91,195\}$: in every case $a_2=a_1+\min P(a_1)$ is even and the core is nonempty from $n\le2$.

**GAP-A (core persistence — unproved).** The claim that $\mathcal M_n^*\neq\emptyset$ for *every* $n\ge2$ throughout regime (S) is **not proved here**. A core member $C\ni2$ can be refined by a straggler $S\subsetneq C$ with $2\notin S$ and $|S|\ge2$ (no singleton, so no freeze) — e.g. structurally $\{2,3,5\}\to\{3,5\}$ is permitted by the refinement rule. The greedy's smallest-first dynamics might prevent this in regime (S) (computationally the core never empties in any of the 17 saturated seeds tested — `core_min=1` throughout), but no proof is known. This gap is **not load-bearing for the Cov-monovariant** (Lemma B), which concerns only the $\{2,p\}$-members and does not require the core to be nonempty; it would be load-bearing only for a crash-forcing step (the refuted Lemma C). It is recorded honestly for completeness.

### 3. Lemma B — the Cov monovariant (proved in full, SPT-free)

For $n\ge1$ define the **coverage**
$$\mathrm{Cov}(\mathcal M_n):=\{p\in P(a_1):\{2,p\}\in\mathcal M_n\}\;\subseteq\;P(a_1).$$
(Only primes of $a_1$ are eligible, so $\mathrm{Cov}(\mathcal M_n)\subseteq P(a_1)$ is tautological; $P(a_1)$ is finite by the factorization of $a_1$.) Call a step a **$\{2,p\}$-crash** when a promotion adds the member $\{2,p\}$ for some $p\in P(a_1)$ (equivalently, when $p$ newly enters $\mathrm{Cov}$).

**Lemma B (Cov monovariant).** *Assume regime (S). Then:*
1. *$\mathrm{Cov}(\mathcal M_n)$ is monotone non-decreasing in $n$ (once $\{2,p\}\in\mathcal M_n$ for $p\in P(a_1)$, it persists: $\{2,p\}\in\mathcal M_m$ for all $m\ge n$).*
2. *$\mathrm{Cov}$ stabilizes after at most $|P(a_1)|$ $\{2,p\}$-crashes; in particular the number of $\{2,p\}$-crashes is $\le|P(a_1)|$ and every crash prime lies in $P(a_1)$.*

*Proof.* The heart is the **refinement obstruction**: in regime (S), the member $\{2,p\}$ (for $p\in P(a_1)$) can never be refined away. For suppose $\{2,p\}\in\mathcal M_n$ and at a later step a new minimal $M'$ refines it, i.e. $M'\subsetneq\{2,p\}$, $M'\in\mathcal M_m$, $m>n$. Since $M'$ is a nonempty proper subset of the two-element set $\{2,p\}$, we have $M'\in\bigl\{\{2\},\{p\}\bigr\}$.

- $M'=\{2\}$: then $2\in C_m$ (every minimal in $\mathcal M_m$ is hit by... — in fact $\{2\}\in\mathcal M_m$ means $2\in M$ for $M=\{2\}$, and for $2$ to be *common* we need $2\in\bigcap_{M\in\mathcal M_m}M$; but more directly, $\{2\}$ is a singleton, so by `singleton-freeze` $\mathcal M$ freezes to $\{\{2\}\}$ from time $m$, making $2$ permanently common — contradicting regime (S)). Concretely, `singleton-freeze` forces $\mathcal M_{m'}=\{\{2\}\}$ for all $m'\ge m$, so $2\in C_{m'}$ for all $m'\ge m$, contradicting (S). Moreover, if $2\notin P(a_1)$ this is doubly impossible by `common-primes-bounded` ($2\notin C_{m'}$ ever). 
- $M'=\{p\}$: then $\{p\}$ is a singleton with $p\in P(a_1)$; `singleton-freeze` makes $p$ permanently common, contradicting (S). (Equivalently, $p\in C_m$ and stays.)

Both cases contradict regime (S). Hence **no proper nonempty subset of $\{2,p\}$ ever becomes a minimal in regime (S)**. By the refinement dynamics (§0), a member is removed from $\mathcal M$ only when a *proper subset* of it appears as a new minimal; since no proper subset of $\{2,p\}$ can appear, $\{2,p\}$ is never removed. Once $\{2,p\}\in\mathcal M_n$, it stays in $\mathcal M_m$ for all $m\ge n$. This proves (1).

For (2): $\mathrm{Cov}(\mathcal M_n)\subseteq P(a_1)$ is a finite set of size $\le|P(a_1)|$, and by (1) it is monotone non-decreasing. A bounded monotone subset of a finite set stabilizes (KB: *Invariants & monovariants* — a bounded monotone integer-quantity stabilizes; here the integer quantity is $|\mathrm{Cov}|$, bounded by $|P(a_1)|$). So there is $\bar C\subseteq P(a_1)$ and $N_0$ with $\mathrm{Cov}(\mathcal M_n)=\bar C$ for all $n\ge N_0$. Each increase of $\mathrm{Cov}$ corresponds to a distinct $\{2,p\}$-crash (a distinct $p\in P(a_1)$ newly added), so the total number of $\{2,p\}$-crashes is $|\bar C|\le|P(a_1)|$, and every such crash prime $p$ lies in $P(a_1)$. ∎

**Corollary (crash-prime bound, SPT-free).** *In regime (S), the primes appearing in $\{2,p\}$-type crash members are drawn from $P(a_1)$ (finite by the factorization of $a_1$), and the number of such crashes is $\le|P(a_1)|$. The entering large primes (those not in $P(a_1)$) are never crash primes of $\{2,p\}$-type; they enter only as free-riders in larger core members $\{2,p,q,\ldots\}$ and are evicted when a $\{2,p\}$-crash (or another refinement) arrives.*

**Remark (computationally verified).** On the 17 saturated seeds $a_1\in\{15,35,77,105,143,175,323,385,1001,1155,1365,2145,5005,4199,91,195\}$: $\mathrm{Cov}$ is monotone non-decreasing throughout regime (S) (0 violations); the number of $\{2,p\}$-crashes is $\le|P(a_1)|$ in every case; every $\{2,p\}$-crash prime lies in $P(a_1)$. (The only observed decreases of $\mathrm{Cov}$ occur at the regime-(F) singleton transition — e.g. $a_1=33$: $\{2,3\}$ refined by $\{3\}$ at the singleton-freeze step — which is outside regime (S) by definition.)

### 4. Lemma C-ref — the original "crash to full star" claim is FALSE

The outline's Lemma C asserted: *while $\mathrm{Cov}(\mathcal M_n)\neq P(a_1)$, a $\{2,p\}$-crash for some $p\in P(a_1)\setminus\mathrm{Cov}$ is eventually forced.* **This is refuted by counterexample.**

**Lemma C-ref (refutation).** *There exist saturated-regime seeds that terminate (reach a self-blocking, frozen family) with $\mathrm{Cov}\subsetneq P(a_1)$. For these, no $\{2,p\}$-crash completes the star over all of $P(a_1)$; the process terminates via a richer self-blocking family.*

*Evidence (computationally verified, exact terminal families).* All terminal families below are self-blocking (verified by exhaustive transversal search) and frozen by `Sat-criterion`; in each $\mathrm{Cov}\subsetneq P(a_1)$:

| $a_1$ | $P(a_1)$ | terminal $\mathcal M$ | $\mathrm{Cov}$ |
|---|---|---|---|
| $35$ | $\{5,7\}$ | $\{\{2,3,7\},\{2,5\},\{3,5\},\{5,7\}\}$ | $\{5\}$ |
| $143$ | $\{11,13\}$ | $\{\{11,13\},\{11,3\},\{2,3,13\},\{2,11\}\}$ | $\{11\}$ |
| $175$ | $\{5,7\}$ | $\{\{2,13,7\},\{3,7\},\{13,3,5\},\{2,3,5\},\{5,7\}\}$ | $\emptyset$ |
| $323$ | $\{17,19\}$ | $\{\{17,2\},\{17,19\},\{19,2,3\},\{17,3\}\}$ | $\{17\}$ |
| $385$ | $\{5,7,11\}$ | $\{\{11,5,7\},\{19,2,11\},\{11,3,7\},\{19,3,7\},\{2,3,5\},\{2,7\},\{11,2,3\}\}$ | $\{7\}$ |
| $4199$ | $\{13,17,19\}$ | $\{\{2,83,13\},\{17,2\},\{2,3,13\},\{19,2,3\},\{17,3,13\},\{17,19,13\},\{17,83,3\}\}$ | $\{17\}$ |

In each, the straggler members and the non-$\{2,p\}$ core members (carrying entering free-rider primes like $3,13,19,83$) jointly form a self-blocking family *without* completing the $2$-star over $P(a_1)$. ∎ (refutation; the original Lemma C is false)

**Consequence for the wall.** The Cov-monovariant bounds the $\{2,p\}$-crashes but does **not** bound the *other* crashes (straggler refinements, $\{2,p,q\}$-type core crashes, free-rider introductions). Termination, when it occurs, need not pass through $\mathrm{Cov}=P(a_1)$; it can occur at any stabilized value $\bar C\subseteq P(a_1)$ via a richer self-blocking configuration. So the wall is *not* "force $\mathrm{Cov}=P(a_1)$"; it is **prove the saturated regime terminates at all**.

### 5. Addressing the reviewer's straggler-prime concern

The reviewer flagged that the outline's Lemma C needed an unstated sub-claim: *the straggler (a minimal $\not\ni2$) contains some prime $p\in P(a_1)\setminus\mathrm{Cov}$*, and that `common-primes-bounded` does not justify this (it bounds common primes, not straggler primes). The concern is **well-founded**, and the resolution is:

1. **The Cov-monovariant (Lemma B) does not use the straggler-prime sub-claim.** Lemma B's refinement obstruction concerns only the $\{2,p\}$-members and their subsets $\{2\},\{p\}$; it invokes no property of stragglers. So Lemma B (the proved contribution of this approach) stands without the sub-claim.

2. **The sub-claim was load-bearing only for the (refuted) Lemma C.** Lemma C needed a straggler prime $p\in P(a_1)\setminus\mathrm{Cov}$ so that $\{2,p\}$ would be a transversal ($2$ hits the core, $p$ hits the straggler) and hence a forced crash. Since Lemma C is refuted (§4 — termination occurs at $\mathrm{Cov}\subsetneq P(a_1)$ via richer self-blocking families), the sub-claim is moot.

3. **Empirical status of the sub-claim (for honesty).** The sub-claim "while $\mathrm{Cov}\neq P(a_1)$, some straggler member meets $P(a_1)\setminus\mathrm{Cov}$" was checked on the 17 saturated seeds: it held at *every* time step with $\mathrm{Cov}\neq P(a_1)$ (0 violations). The structural reason (when it holds): if $\{2,p\}\in\mathcal M_n$ (i.e. $p\in\mathrm{Cov}$) then by pairwise-intersection every straggler $S$ (with $2\notin S$) must meet $\{2,p\}$, forcing $p\in S$; so **every straggler contains all of $\mathrm{Cov}$**. The open piece is whether some straggler *also* meets $P(a_1)\setminus\mathrm{Cov}$ — this is not automatic (a straggler could be $\mathrm{Cov}\cup\{\text{entering primes outside }P(a_1)\}$) and, per (2), is no longer needed. It is **not proved** and is **not a gap in the proved part**.

### 6. Lemma D — the star+straggler is a self-blocking terminal (proved; sufficient, not necessary)

Lemma C-ref shows the actual terminal need not be the "full star $+$ straggler $P(a_1)$." But the star+straggler *is* a self-blocking configuration, so it is a legitimate **sufficient** terminal (and the importable structural lemma). We prove it for a general straggler $S\subseteq P(a_1)$ with $2\notin S$.

**Lemma D (star+straggler self-blocking).** *Let $S\subseteq P(a_1)$ be nonempty with $2\notin S$ (automatic if $a_1$ is odd; if $a_1$ is even, take $S\subseteq P(a_1)\setminus\{2\}$). Then the family*
$$\mathcal F_S\;:=\;\{S\}\cup\bigl\{\{2,p\}:p\in S\bigr\}$$
*is self-blocking: every transversal of $\mathcal F_S$ contains a member of $\mathcal F_S$ as a subset.*

*Proof.* Let $T$ be a transversal of $\mathcal F_S$ (a set meeting every member). Split on whether $2\in T$.
- **$2\in T$.** To meet the member $S$ (which lacks $2$), $T$ must contain some $p\in S$. Then $\{2,p\}\subseteq T$ for that $p$, and $\{2,p\}\in\mathcal F_S$ is a member. So $T$ contains a member.
- **$2\notin T$.** To meet each member $\{2,p\}$ (for every $p\in S$) without using $2$, $T$ must contain $p$ for every $p\in S$, i.e. $S\subseteq T$. But $S\in\mathcal F_S$ is a member. So $T$ contains a member.

Either way $T$ contains a member; hence no transversal avoids all members, i.e. $\mathcal F_S$ is self-blocking. ∎

**Corollary.** *If at some time $n$ in regime (S) the family takes the form $\mathcal F_S$ for some $S\subseteq P(a_1)\setminus\{2\}$ (in particular the "full star" $\mathcal F_{P(a_1)\setminus\{2\}}$ for odd $a_1$, realized e.g. by $a_1\in\{15,77,91,105,1001,1155,1365,2145,5005\}$), then by Lemma D and `Sat-criterion` $\mathcal M$ is frozen and finite from $n$ on.*

**Remark.** The actual terminal may be a *richer* self-blocking family (§4 table) not of the star+straggler form; Lemma D is a sufficient, not necessary, terminal. By `Sat-criterion` (imported), *any* self-blocking family freezes — so reaching *any* self-blocking configuration suffices for finiteness.

### 7. The wall — GAP-S' (termination after Cov stabilizes)

Lemmas A, B, D reduce the saturated branch as follows. By Lemma B, in regime (S) the coverage $\mathrm{Cov}$ stabilizes at some $\bar C\subseteq P(a_1)$ after finitely many ($\le|P(a_1)|$) $\{2,p\}$-crashes; from time $N_0$ on, **no new $\{2,p\}$-member ever appears**. The remaining possible promotions are:
- straggler refinements (a straggler $S$ refined by $S'\subsetneq S$),
- core refinements by larger sets $\{2,p,q,\ldots\}$ (carrying free-rider primes $q\notin P(a_1)$),
- and (per Lemma C-ref) these can build a self-blocking family at $\bar C\subsetneq P(a_1)$.

**GAP-S' (the wall, open).** *In regime (S), after $\mathrm{Cov}$ stabilizes at $\bar C\subseteq P(a_1)$, prove the promotion process terminates — equivalently $\mathcal M_n$ stabilizes, equivalently $\mathcal M$ is finite.*

This is **the same hard wall as α's GAP-S** (regime-(S) termination); the contribution of this framing is that it bounds the $\{2,p\}$-crash count and crash primes SPT-free, narrowing (not closing) the wall. The framing does **not** prove that the post-stabilization promotions exhaust themselves — the entering free-rider primes $q\notin P(a_1)$ are unbounded a priori, and a priori the process could produce infinitely many straggler/$\{2,p,q\}$-type refinements without reaching self-blocking. Computationally this never happens (every one of $\sim$18 saturated seeds reaches a self-blocking family), but no proof is known.

**Why the framing survives a failure of SPT/W1 (its strategic value).** Lemma B's crash-prime bound is value-free: it uses only the factorization of $a_1$ (giving the finite container $P(a_1)$) and the refinement obstruction (a $\subseteq$-structural fact about two-element sets, not a prime-value bound). It does not invoke "every minimal carries a prime $\le p^*$" (SPT) or "the mtp-witness transversal has a small prime" (W1). If SPT/W1 fails, the $\{2,p\}$-crash count is still $\le|P(a_1)|$. The remaining wall (GAP-S') is genuinely the same termination question the rest of the field faces, but the partial invariant proved here is an independent structural fact.

### 8. Branch (S) finish (conditional on GAP-S')

Assume GAP-S' (regime (S) terminates: $\mathcal M$ finite). Then by `post-stabilization-theorem` (imported), with $P=\bigcup\mathcal M$, $L=\prod_{p\in P}p$ (squarefree), $V=\{r\in\{0,\ldots,L-1\}:\{p\in P:p\mid r\}\text{ hits }\mathcal M\}$, $T=|V|$, we have $a_{n+T}=a_n+L$ for every $n\ge1$. The terminal family is some self-blocking $\mathcal M$ (possibly the star+straggler $\mathcal F_S$ of Lemma D, possibly a richer family per §4); `Sat-criterion` certifies it freezes once reached. ∎ (conditional on GAP-S')

### 9. Conclusion

- **(F) Freeze regime: SOLVED (imported `freeze-lock`+AP$\to p^k$+`singleton-freeze`+`post-stabilization-theorem`).**
- **(S) Saturated regime: PARTIAL.**
  - Proved (SPT-free, value-free): 2-entry (Lemma A); the Cov-monovariant $\mathrm{Cov}\subseteq P(a_1)$ is monotone non-decreasing in regime (S) with $\le|P(a_1)|$ $\{2,p\}$-crashes and crash primes $\subseteq P(a_1)$ (Lemma B); the star+straggler is a self-blocking sufficient terminal (Lemma D); the original "crash to full star" Lemma C is refuted (Lemma C-ref); the reviewer's straggler-prime sub-claim is moot (§5).
  - Open wall (GAP-S'): prove the saturated regime terminates after $\mathrm{Cov}$ stabilizes. This is the same termination wall as α's GAP-S; the Cov-monovariant narrows it (bounds $\{2,p\}$-crashes) but does not close it.
  - Sub-gap (GAP-A): the core $\mathcal M_n^*$ stays nonempty throughout regime (S) — unproved, 0 computational violations, not load-bearing for Lemma B.

The case split (prime-power / (F) / (S)) is exhaustive (excluded middle on "some factor of $a_1$ is permanently common," combined with the prime-power singleton-freeze). With GAP-S' open, this approach is **partial**: the freeze regime and the structural Cov-monovariant are proved end-to-end; the saturated-regime termination is the honest open wall. ∎

---

## Promotable lemmas

1. **Cov monovariant** (Lemma B, conditional on regime (S)). *$\mathrm{Cov}(\mathcal M_n)=\{p\in P(a_1):\{2,p\}\in\mathcal M_n\}$ is monotone non-decreasing and $\subseteq P(a_1)$; hence the number of $\{2,p\}$-crashes is $\le|P(a_1)|$ and the crash primes lie in $P(a_1)$.* **Proved in full above (§3).** SPT-free, value-free: uses only the factorization of $a_1$ and the refinement obstruction (a $\{2,p\}$-member's only proper nonempty subsets are $\{2\},\{p\}$, both singleton-freeze/regime-(F) events). The refinement obstruction is rigorous under regime (S): $\{2\}$ and $\{p\}$ would each trigger `singleton-freeze`, contradicting (S); when $2\notin P(a_1)$, $\{2\}$ is additionally excluded by `common-primes-bounded`. Importable as the crash-count/crash-prime bound for any saturated-regime argument.

2. **Star+straggler self-blocking** (Lemma D). *For any nonempty $S\subseteq P(a_1)$ with $2\notin S$, the family $\{S\}\cup\{\{2,p\}:p\in S\}$ is self-blocking (every transversal contains a member).* **Proved in full above (§6).** Structural, value-free, unconditional; importable as a sufficient terminal configuration for any saturated argument reaching the star+straggler form (e.g. odd squarefree $a_1$ with $\ge3$ factors: terminal $\mathcal F_{P(a_1)}$).

3. **2-entry** (Lemma A). *If $a_1$ has $\ge2$ distinct prime factors, then $2\in\bigcup\mathcal M_n$ for some $n\le2$; when $a_1$ is odd, $a_2=a_1+\min P(a_1)$ (even).* **Proved in full above (§2).** Importable wherever the 2-core framing is used.

## Open gaps
- **GAP-S'** (the wall): prove the saturated regime terminates after $\mathrm{Cov}$ stabilizes at $\bar C\subseteq P(a_1)$ — the same hard wall as α's GAP-S; the Cov-monovariant bounds $\{2,p\}$-crashes but not the remaining (straggler, $\{2,p,q\}$-type, free-rider) crashes.
- **GAP-A**: the core $\mathcal M_n^*$ stays nonempty throughout regime (S) (unproved; 0 violations on 17 saturated seeds; not load-bearing for Lemma B).
- **Lemma C (original outline)**: **REFUTED** (Lemma C-ref, §4) — termination need not pass through $\mathrm{Cov}=P(a_1)$.

## Cases to cover
- $a_1$ prime power: `singleton-freeze` (imported). ✓
- $a_1$ $\ge2$ prime factors, regime (F): freeze import (`freeze-lock`+AP$\to p^k$+`singleton-freeze`). ✓
- $a_1$ $\ge2$ prime factors, regime (S), $a_1$ odd: Cov-monovariant route (this approach). Partial (GAP-S').
- $a_1$ $\ge2$ prime factors, regime (S), $a_1$ even: Cov-monovariant applies (the refinement obstruction holds for $\{2,p\}$, $p\in P(a_1)\setminus\{2\}$, since $\{2\},\{p\}$ are still excluded in regime (S)); GAP-S' remains. (No even $a_1$ in regime (S) was found among $\sim$20 even seeds tested — all even seeds were regime (F) — but the framing covers the hypothetical case; if even $a_1$ is always regime (F), the freeze import covers it. Either way no coverage hole.)

## Watch out for
- The **free-rider universality conjecture is FALSE** ($a_1=15$, step 3, $a_3=20$, $P=\{2,5\}$ is a minimal transversal of $\mathcal M_2=\{\{3,5\},\{2,3\}\}$, no proper transversal subset). Use only the crash-refines-large-primes direction ($\{2,p\}\subsetneq\{2,p,q,\ldots\}$ is a genuine refinement, a subset relation), never the universal free-rider claim.
- **$|M|\le7$ is REFUTED** ($a_1=5005$ reaches $|M|=31$ transiently; $a_1=2310$ regime-(F) transient has $|M|=128$). Do not assert a small constant cap.
- **Dickson / multiset WQO fails** (incomparable adds grow the multiset; universe unbounded via free-rider primes). Do not build on it.
- **The original Lemma C (crash to full star $\mathrm{Cov}=P(a_1)$) is FALSE** — counterexamples in §4. Termination can occur at $\mathrm{Cov}\subsetneq P(a_1)$. Do not re-assert the full-star target.
- **Crash primes are $\subseteq P(a_1)$, but crash *terms* and entering primes are not bounded.** The bound is on the prime SET of $\{2,p\}$-crashes, not on term values or on the entering free-rider primes.
- **The straggler-prime sub-claim** (reviewer's concern) is NOT needed for the Cov-monovariant and is moot post-refutation. Do not re-introduce it as load-bearing.
