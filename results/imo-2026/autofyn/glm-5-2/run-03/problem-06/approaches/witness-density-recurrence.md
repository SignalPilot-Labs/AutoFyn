# witness-density-recurrence

## Status
partial

## Approaches tried
- (round 2, build) Witness-density / counting attack on Gap A — a COUNTING mechanism (genuinely distinct from the `aimo-0030` strip and the `aimo-0678` monovariant). The **spacing half is proved and non-circular** (Lemma W1: a governing prime $q>M_1$ is re-witnessed with density $\le M_1/q<1$ per step). The **density-incompatibility half (Step 5) is CIRCULAR as stated**, and the minimal-criminal induction the reviewer suggested does NOT de-circularize it. The obstruction is structural, not empirical: transient primes (which are *compatible* with Gap A being true — they are finite-lived by definition) provide unbounded covering capacity for $q$-free minimal transversals, and bounding the primes in the intermediate supports between consecutive witnesses IS Gap A. Recorded honestly as a RETHINK candidate; the spacing lemma W1 is left as a conditional observation (its "infinitely many distinct witnesses" premise is plausible but itself unproven — secondary gap). No false proof is presented. Verdict: CHANGES REQUESTED → should be RETIRED next round unless a genuinely non-circular density lower bound is found.

## Current best
A sound **upper bound on the re-witnessing density** of any governing prime $q>M_1$: density $\le M_1/q$ per step (Lemma W1, conditional on the "infinitely many distinct witnesses" premise W0). This is the only piece of this approach that is both non-circular and non-trivial; it is a genuine constraint but, being only an *upper* bound on density, it does NOT by itself contradict governance (a prime can be re-witnessed infinitely often at arbitrarily low density, e.g. at indices $2^k$, consistently with $\le M_1/q$). The matching *lower* bound on required density (Step 5) — which is what would force $q\le M_1\cdot C$ and close Gap A — cannot be established without first bounding the primes in intermediate supports, i.e. without Gap A. **Open gap: the entire density-incompatibility step (Step 5) is circular; the minimal-criminal induction on the order of governing primes $>M_1$ does not close it (see Step 5 analysis).**

## Full proof
Not complete. Below is the full attempt, with the circularity honestly marked.

---

### Setup and imports

We import the certified foundation (see `lemmas/`):
- **Linchpin and gap bound** (`linchpin-and-gap-bound.md`): every $a_n$ is divisible by some $p\in P_1=S(a_1)$, and $d_n:=a_{n+1}-a_n\le M_1:=\operatorname{rad}(a_1)=\prod_{p\in P_1}p$.
- **Pairwise-intersecting supports** (`pairwise-intersecting-supports.md`): $S(a_i)\cap S(a_j)\ne\varnothing$ for all $i,j$.
- **Every term in $\mathcal B_\infty$**, **greedy $=$ cyclic successor**, **cyclic-successor bijection**, **lock-lemma**.

Notation: $\mathcal F_n=\{S(a_1),\dots,S(a_n)\}$; $\operatorname{MT}(\mathcal F_n)$ its minimal transversals; $G_n:=\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}T$ (the primes appearing in some minimal transversal at step $n$); $\mathcal B_\infty=\bigcap_n\mathcal B_n$. By the equivalence in `transversal-saturation` Step 6, Gap A ($\mathcal B_\infty$ is $L$-periodic) is equivalent to "$G:=\bigcup_n G_n$ at the limit — equivalently the set of primes appearing in $\bigcup\operatorname{MT}(\mathcal F_n)$ for infinitely many $n$ — is finite."

### Step 1 — Governing vs transient (no circularity)

A prime $q$ is **governing** iff $q\in G_n$ for infinitely many $n$ (equivalently, $q$ appears in some minimal transversal of $\mathcal F_n$ for arbitrarily large $n$). A prime $q$ is **transient** iff $q\in G_n$ for some but only finitely many $n$. By construction every prime in $G:=\bigcup_n(\text{prime appearing in some } \operatorname{MT}(\mathcal F_n)\text{ at step }n)$ is either governing or transient, and the two classes are disjoint. Gap A is exactly the assertion "only finitely many primes are governing." This definition invokes no unbounded-covering-capacity assumption — it is a clean dichotomy.

**Remark (transience is compatible with Gap A).** A transient prime is, by definition, finite-lived in $G_n$. There can in principle be *infinitely many distinct* transient primes over the full sequence while the governing set stays finite (each transient prime eventually drops out; a fresh one can take its place). The data is consistent with this: e.g. for $a_1=145=5\cdot29$ (which locks at $n=97$, $L=5$), the MT-prime set at $n=40$ is $\{2,3,5,7,11,13,29,31,37,41,43,47,53,59,61,67\}$ — all $\le M_1=145$, but the set *grows with $n$* and *drops to $\{5\}$* at the lock. Each of $7,11,\dots,67$ is transient (dropped by the lock). This fact — that transient primes are unbounded in number over the sequence — is *not* a contradiction of Gap A; it is fully compatible with it. **This compatibility is the structural reason the density lower bound below is circular**, as we shall see.

### Step 2 — Re-witnessing structure

If $q$ is governing, there are infinitely many "witness steps" $n_k\to\infty$ with $q\in G_{n_k}$. At each such step, by the standard characterization of minimal transversals (every element of a minimal transversal is private to some member it hits), there is a *private witness*: a term $a_{i_k}$ ($i_k\le n_k$) with $S(a_{i_k})\cap T_k=\{q\}$ for some $T_k\in\operatorname{MT}(\mathcal F_{n_k})\ni q$. In particular $q\mid a_{i_k}$.

> **Premise W0 (open, plausible).** *If $q$ is governing, the set of distinct private-witness indices $\{i_k\}$ is infinite.*
>
> W0 is plausible but **not proved here**. The obvious reduction ("governing $\Rightarrow q$ divides infinitely many $a_i$") is itself non-trivial: $q$ could in principle divide only finitely many terms and still appear in $\operatorname{MT}(\mathcal F_n)$ for infinitely many $n$, sustained by a fixed finite witness set and a growing $T_k\setminus\{q\}$ that keeps transversing the tail family $\{S(a_j):q\nmid a_j\}$. Whether the *minimality* of $T_k$ forbids this indefinitely is not resolved in this round; we flag W0 as a **secondary open gap**. Everything below is conditional on W0.

Assuming W0, enumerate the distinct private witnesses in increasing index order: $a_{i_1}<a_{i_2}<\cdots$ (infinitely many).

### Step 3 — The spacing lemma (sound, non-circular) — Lemma W1

**Lemma W1 (witness-index spacing).** *Assuming W0:* if $q$ is a governing prime, the private-witness indices satisfy
$$i_{k+1}-i_k\;\ge\;\frac{q}{M_1}\qquad\text{for all }k,$$
so the witness **density** (witnesses per step) is $\le M_1/q$. In particular, if $q>M_1$ then $i_{k+1}-i_k\ge2$ (witnesses are non-adjacent) and the density is $<1$.

*Proof.* Two distinct witnesses $a_{i_k}\ne a_{i_{k+1}}$ are both multiples of $q$ (each is a private witness of $q$, so $q\mid a_{i_k}$ and $q\mid a_{i_{k+1}}$). Distinct positive multiples of $q$ differ by at least $q$, so $a_{i_{k+1}}-a_{i_k}\ge q$. By the certified gap bound $d_n\le M_1$,
$$a_{i_{k+1}}-a_{i_k}\;=\;\sum_{n=i_k}^{i_{k+1}-1}d_n\;\le\;(i_{k+1}-i_k)\cdot M_1.$$
Combining, $q\le(i_{k+1}-i_k)M_1$, i.e. $i_{k+1}-i_k\ge q/M_1$. The density of witness indices in $\{1,\dots,N\}$ is $|\{k:i_k\le N\}|/N\le M_1/q$ (at most one witness per $q/M_1$-window). ∎

**Lemma W1 is sound and non-circular.** It uses only the gap bound (certified, unconditional) and the divisibility $q\mid a_{i_k}$ (definitional for private witnesses). It does NOT assume Gap A, does NOT bound the primes in intermediate supports, and does NOT invoke any covering capacity. It is a clean *upper* bound on witness density. We record it (conditional on W0) as the approach's positive output.

**Crucially, W1 alone does NOT contradict governance.** A prime $q>M_1$ can be re-witnessed infinitely often with density $\le M_1/q<1$ — for instance at indices $i_k=\lfloor k\cdot q/M_1\rfloor$ — and this is fully consistent with both W1 and with $q$ being governing. To close Gap A, the spacing upper bound must be paired with a *lower* bound on required density: governance must force re-witnessing *frequently enough* that the two bounds meet, yielding $q\le M_1\cdot C$. That lower bound is Step 5 — and it is where the approach founders.

### Step 4 — The density-incompatibility target

**Desired (Step 5) lower bound.** There is a constant $C=C(|P_1|)$, finite and depending only on $|P_1|$, such that every governing prime $q$ has witness density $\ge 1/C$. Combined with W1's $\le M_1/q$, this would give $1/C\le M_1/q$, i.e. $q\le M_1\cdot C$, bounding every governing prime — hence Gap A (the governing primes lie in $\{p\le M_1\cdot C\}$, finite).

The proposed mechanism: between consecutive private witnesses $a_{i_k},a_{i_{k+1}}$, the intermediate terms $a_{i_k+1},\dots,a_{i_{k+1}-1}$ are added to $\mathcal F_n$. For $q$ to *stay out* of $G_n$ throughout this stretch (only returning at $i_{k+1}$), every intermediate support must be absorbed by some $q$-free minimal transversal of the growing family. The number of intermediate supports absorbable in this way is bounded by the **covering capacity** of $T_k\setminus\{q\}$ — the maximum number of distinct new supports that $T_k\setminus\{q\}$ (or its $q$-free MT successors) can hit without requiring $q$. If this covering capacity is $C$, then $i_{k+1}-i_k\le C$, giving density $\ge1/C$.

### Step 5 — THE CIRCULARITY (honest analysis)

**The covering capacity of $T_k\setminus\{q\}$ is UNBOUNDED for the greedy-sequence family unless the primes appearing in the intermediate supports are already bounded. Bounding those primes IS Gap A.** Therefore Step 5, as stated, assumes Gap A to prove Gap A. This was the reviewer's finding; we confirm it and show the minimal-criminal induction does not rescue it.

#### 5a. The abstract counterexample (reviewer's star/projective-plane point, spelled out).

Consider a pairwise-intersecting family in which there is a fixed "core" hit by $T\setminus\{q\}$, plus a stream of new supports each carrying a *fresh outer prime* $r_k$ that $T\setminus\{q\}$ does not hit. Concretely: let $T\setminus\{q\}=\{p_1,\dots,p_s\}$ (fixed small primes) and suppose the new supports are $\{p_1, r_k\}$ for a stream of distinct fresh primes $r_k\notin T$. Each new support is hit by $p_1\in T\setminus\{q\}$, so $T$ (hence $T\setminus\{q\}$) keeps transversing it. But to build a *$q$-free minimal transversal*, each new support $\{p_1,r_k\}$ — if we do not use $q$ — is hit by $p_1$, so $p_1$ alone in a $q$-free MT suffices for it; no fresh prime is forced. So this particular configuration does NOT exhibit unbounded covering capacity. The bad configuration is the dual one:

**Bad configuration.** New supports $\{r_k\}$ each equal to a fresh singleton prime, OR more realistically $\{q, r_k\}$ — each new support contains $q$ (so $T$ with $q\in T$ hits it) but NO prime of $T\setminus\{q\}$. Then a $q$-free transversal must include $r_k$ itself (the only other hitter). Each fresh support forces a fresh prime into the $q$-free MT. The covering capacity of $T\setminus\{q\}$ — the number of such supports absorbable without $q$ — is unbounded, because each requires its own fresh outer prime, and there is no a priori bound on how many fresh outer primes appear in the intermediate supports.

The reviewer's examples: the star $\{\{1,j\}:j\ge2\}$ (here $1$ plays $q$; each $\{1,j\}$ requires $j$ in a $1$-free transversal, unbounded), and projective-plane lines (pairwise-intersecting families where minimal transversals have unbounded size and unbounded prime membership). These show that for an *abstract* pairwise-intersecting family, the covering capacity of $T\setminus\{q\}$ is unbounded. The escape hatch named by the outliner — "the greedy coupling is essential to bound it" — provides no mechanism: the greedy coupling ($d_n\le M_1$, terms in $\mathcal B_\infty$, cyclic-successor structure) constrains the *gaps* and the *greedy pick*, but it does not, by itself, bound which primes appear in the supports $S(a_j)$ between witnesses. And bounding those primes is exactly Gap A.

#### 5b. The minimal-criminal attempt (reviewer's suggested rescue) — DOES NOT CLOSE.

Following the reviewer's suggestion, choose $q$ to be the **smallest governing prime** $>M_1$ (minimal criminal). Then every governing prime other than $q$ is either $\le M_1$ (small) or $\ge q$ (large). The hope: intermediate supports between consecutive witnesses of $q$ carry only (a) small primes $\le M_1$, hit by the small primes in $T\setminus\{q\}$, and (b) large primes $\ge q$, each a witness of "another governing prime $\ge q$, handled by the same minimal-criminal induction on $q$."

**This rescue fails, for two independent reasons.**

**(i) Transient primes are not bounded by the minimal-criminal choice, and they provide unbounded covering capacity — *compatibly with Gap A*.** The minimal-criminal choice of $q$ excludes only primes in $(M_1,q)$ from being *governing*. It says nothing about *transient* primes (primes in $G_n$ for finitely many $n$). A transient prime $r$ can appear in an intermediate support $S(a_j)$ and serve as a hitter in a $q$-free minimal transversal during its finite lifetime. Because transient primes are by hypothesis finite-lived, there is no contradiction in having *infinitely many distinct* transient primes over the full sequence while the *governing* set stays finite (Step 1's remark; verified for $a_1=145$, where $7,11,\dots,67$ are transient and drop at the lock). The minimal-criminal choice of $q$ does not bound the *value* of transient primes (a transient prime can be arbitrarily large — the data shows term-primes reaching well beyond $M_1$ in some sequences), nor their *number*. Hence the covering capacity of $q$-free MTs — which can recruit fresh transient primes as hitters for each fresh intermediate support — is unbounded, *even when Gap A is true*. Since unbounded covering capacity is consistent with Gap A, no contradiction follows from it.

Concretely: in the bad configuration of 5a, replace the "fresh outer primes $r_k$" by *transient* primes (each $r_k$ appears in $G_n$ for finitely many $n$ and then drops). The intermediate support $\{q,r_k\}$ is absorbed by a $q$-free MT containing $r_k$ while $r_k$ is alive; when $r_k$ drops, a new transient prime $r_{k+1}$ takes its role. The covering capacity (number of consecutive intermediate supports absorbable without re-witnessing $q$) is the length of the longest run of distinct live transient primes, which is unbounded in the abstract and is NOT bounded by the minimal-criminal choice of $q$.

**(ii) Governing primes $\ge q$ (other than $q$) are not bounded by the minimal-criminal choice either, and the "induction on the order of governing primes $>M_1$" is not well-founded.** The induction as stated ("assume all governing primes in $(M_1,q)$ excluded; show $q$ excluded") is a single-step descent: by minimality of $q$, no governing prime lies in $(M_1,q)$ — that is the base, free. But to exclude $q$, the intermediate supports' large primes $\ge q$ (other governing primes) are invoked and "handled by the same induction." Those primes are $\ge q$, *not* $<q$; the induction (which only excludes primes $<q$) does **not** apply to them. The dispatch's own warning is decisive here: "witnesses $\ge q$ other than $q$ itself — can they carry $q$ as a cofactor and re-witness it?" They can: a fresh large prime $r>q$, governing or transient, in an intermediate support, behaves exactly like the fresh outer prime of the abstract bad configuration; the minimal-criminal induction has no purchase on it because $r\not<q$. The induction "pushes the problem to the next prime up," not down — it is not a well-founded descent.

**Conclusion of Step 5.** The covering-capacity bound $C$ is unbounded for the greedy-sequence family *unless the primes in the intermediate supports are already bounded*, which is Gap A. The minimal-criminal choice of $q$ as the smallest governing prime $>M_1$ excludes only primes in $(M_1,q)$ from being governing — too weak to bound either (i) transient primes (unbounded, compatible with Gap A) or (ii) governing primes $\ge q$ (unbounded, not handled by the descent). **Step 5 is circular, and the minimal-criminal rescue does not de-circularize it.**

### Step 6 — What would be needed (honest specification of the missing ingredient)

To make this approach non-circular, one would need a density lower bound of the form "governance forces re-witnessing at density $\ge\delta(q)$" that does **not** proceed via covering capacity of $T\setminus\{q\}$ (since that is unbounded). Candidates we considered and could not make rigorous in this round:

- **A direct "dropout" argument**: if $q$ stays out of $G_n$ for too long, then *some structural property of the greedy pick* forces $q$ back. We could not identify such a property without already knowing the supports' primes are bounded.
- **A residue-class / finite-state argument**: if the $P_1$-support stream stabilizes (it does, unconditionally — the free F3 observation), maybe the *pattern* of when $q$ is required is eventually periodic, forcing a fixed density. But "when $q$ is required" depends on the large primes in the supports, which are not bounded a priori — again Gap A.
- **Pairing W1's upper bound with a *structural* lower bound from the lock dichotomy**: if the sequence does NOT lock, maybe the no-lock structure forces every "essential" prime to recur frequently. We found no such mechanism (and the `prime-power-dichotomy` approach confirms the no-lock regime relies on the same Gap-A strip as `transversal-saturation`).

The honest state: W1 is a sound upper bound on density; no matching non-circular lower bound is known. The approach as set up cannot close Gap A.

### Step 7 — Endgame (conditional, certified)

Were a non-circular density lower bound $\ge1/C$ established, the conclusion would be: every governing $q$ satisfies $q\le M_1\cdot C$; the governing set $G\subseteq\{p\le M_1\cdot C\}$ is finite; distinct supports (subsets of primes $\le M_1\cdot C$ appearing in some $a_i$) form an increasing bounded family $\Rightarrow$ stabilize; $\operatorname{MT}$ depends only on the set-system $\Rightarrow$ $\operatorname{MT}(\mathcal F_n)$ stabilizes $\Rightarrow$ $\mathcal B_\infty$ is $L$-periodic; by the certified `cyclic-successor-bijection` and `greedy-equals-cyclic-successor` lemmas, $a_{n+T}=a_n+L$ for all $n\ge1$. The lock sub-case is covered by the certified `lock-lemma`. This endgame is sound *conditional on Step 5*, which is the open (circular) wall.

### Summary

- **Proved (conditional on W0):** Lemma W1 — a governing prime $q$ is re-witnessed with density $\le M_1/q$ (sound, non-circular, uses only the certified gap bound and divisibility).
- **Circular, not rescued:** Step 5 — the covering-capacity density lower bound. Unbounded for abstract pairwise-intersecting families; the minimal-criminal choice of $q$ does not bound transient primes (compatible with Gap A) or governing primes $\ge q$; the "induction on the order of governing primes $>M_1$" is not well-founded (pushes the problem up, not down).
- **Secondary gap:** Premise W0 (governing $\Rightarrow$ infinitely many distinct private witnesses) — plausible, unproved here.
- **Honest verdict:** the approach is a RETHINK candidate. It provides a genuinely different *costume* (counting/density rather than strip or monovariant), but the load-bearing density lower bound is circular in exactly the way the reviewer predicted, and the minimal-criminal rescue fails for the structural reasons above. We do NOT present a circular argument as a proof. ∎ (conditional on a non-circular Step 5, which is not in hand)

## Promotable lemmas
- **Lemma W1 (witness-index spacing)** — *conditional on Premise W0.* Statement: a governing prime $q$'s private-witness indices $i_k$ satisfy $i_{k+1}-i_k\ge q/M_1$, i.e. witness density $\le M_1/q$. Proved in Step 3, sound and non-circular. Conditional on W0 (governing $\Rightarrow$ infinitely many distinct private witnesses), which is plausible but unproved. **Not proposed for certification this round** (the premise W0 is open); recorded here as a conditional observation for any approach that can independently close W0 and needs a density upper bound on governing-prime re-witnessing.
