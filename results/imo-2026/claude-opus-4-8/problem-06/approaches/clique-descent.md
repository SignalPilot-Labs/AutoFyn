## Status
partial

## Approaches tried
- clique-descent (round 1, first build): reduced the whole problem to **Lemma S** ("no two clauses share only a large prime") via a divide-out + greedy-uniqueness argument, and proved a first-appearance partial. **Lemma S is FALSE** (a₁=385: clauses {3,7,19},{2,11,19} share only 19 > P₁=11). Retracted this round.
- clique-descent (round 2, this build): **retargeted OFF the false Lemma S.** Kept the certified reduction §§0–4 (imported from `lemmas/bounded-gaps-and-clique.md`) and reframed the crux as **"finitely many minimal clauses."** New rigorous structural content: (a) the minimal-clause family M is a **self-blocking clutter** (M equals its own blocker); (b) **finite-ground-set reduction** — if the set Q of large essential primes is finite, then there are finitely many minimal clauses, hence the conclusion (this is the airtight, non-circular replacement for the false Prop 1); (c) the **mutual-witness lemma** — every large essential prime q sits in two minimal clauses sharing *exactly* {q}, with disjoint nonempty small-shadows, giving a **reconciliation map** Φ: Q → {disjoint shadow-pairs of Π} with finite image. **Open gap:** the fibers of Φ are finite (equivalently Q is finite). This is a genuine arithmetic wall, not clutter-combinatorial. See Spec-concerns note.

## Current best
The whole problem is rigorously reduced to the single statement **"Q is finite"**, where Q := {primes q > P₁ appearing in some minimal clause}. Given Q finite, all minimal clauses live in the finite ground set Π ∪ Q, so there are finitely many, and the certified finish gives a_{n+T}=a_n+L for all n. New rigorous structure this round: M is self-blocking; each q ∈ Q yields two minimal clauses meeting in exactly {q} with disjoint nonempty small-shadows (mutual-witness lemma); hence a finite-image reconciliation map Φ: Q → {disjoint pairs of nonempty subsets of Π}. The **only** unproved input is that Φ has finite fibers.

---

### 0. Import of the certified reduction (do NOT re-derive)

From `lemmas/bounded-gaps-and-clique.md` (reviewer-certified) we import verbatim, with the notation there: $a_1>1$ integer, $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \forall i\le n\}$; $S_i=\operatorname{supp}(a_i)$; "$m$ hits $S$" iff $\operatorname{supp}(m)\cap S\ne\emptyset$; $A_n=\{m\ge1:m$ hits $S_i\ \forall i\le n\}$; $A=\bigcap_n A_n$; $P_1$ = largest prime factor of $a_1$; $\Pi=\{$primes $\le P_1\}$ (finite). Call a prime **small** if $\le P_1$, **large** if $>P_1$. A **clause** is a set $\operatorname{supp}(a_k)$; a clause $C$ is **minimal** if no clause is a proper subset of $C$. For a clause $C$ write $\sigma(C):=C\cap\Pi$ (its **small-shadow**).

Imported certified facts:

- **Tool 1.** Every positive multiple of $a_1$ lies in every $A_n$; hence $0<a_{n+1}-a_n\le a_1$, the sequence is well-defined and strictly increasing to $\infty$, and every term has a prime factor $\le P_1$. **Corollary 1.1:** every clause contains a small prime, so $\sigma(C)\ne\emptyset$ for every clause $C$.
- **Tool 2.** The clauses pairwise intersect ($\gcd(a_i,a_j)>1$ for all $i\ne j$); every term lies in $A$.
- **Sub-lemma E + Cor E.1.** If $w\in A$ and $w>a_1$ then $w$ is a term. Consequently a nonempty prime-set $T$ **is a clause iff $T$ hits every clause** (⇐ Cor E.1: a number of support $T$, $>a_1$, lies in $A$, so is a term; ⇒ Tool 2).
- **Finish package (certified).** *If there are finitely many minimal clauses*, then $A$ is a union of $T:=|A\bmod M|$ residue classes modulo $M:=\prod_{p\in E}p$ (where $E=\bigcup$ of the finitely many minimal clauses), $A_n=A$ for large $n$, the sequence is the increasing enumeration of $\{x\in A:x\ge a_1\}$ from $n=1$, and $a_{n+T}=a_n+L$ for **every** $n\ge1$ with $L=M\ge2$, $T=|A\bmod M|\ge1$. Non-circular and off-by-one clean.

Thus the entire problem is reduced, by certified material, to:

> **Crux.** The family $\mathcal M$ of minimal clauses is finite.

Everything below attacks the Crux. (This is a `none` answer-type problem: no numerical answer; the finish exhibits explicit $L=M$, $T=|A\bmod M|$.)

Two elementary facts about $\mathcal M$ used throughout:

- **(F1)** Every clause contains a minimal clause (clauses are finite nonempty sets, so the poset $(\mathcal C,\subseteq)$ has no infinite descending chain — well-ordering).
- **(F2)** A prime-set hits every clause iff it hits every minimal clause (⇐: given a clause $C$, take a minimal $D\subseteq C$ by (F1); hitting $D$ forces hitting $C$).

---

### 1. The minimal clauses form a self-blocking clutter (PROVED)

For a family $\mathcal H$ of nonempty finite sets, a **transversal** is a set meeting every member of $\mathcal H$, and the **blocker** $b(\mathcal H)$ is the family of **minimal** transversals. $\mathcal H$ is a **clutter** (antichain) if no member contains another.

**Lemma 1.** $\mathcal M$ is a clutter, and $\mathcal M=b(\mathcal M)$ (it is *self-blocking*). Explicitly, for a nonempty prime-set $T$:
$$T\ \text{is a clause}\iff T\ \text{is a transversal of }\mathcal M,$$
and $\mathcal M$ is exactly the family of minimal transversals of $\mathcal M$.

*Proof.* $\mathcal M$ is a clutter by definition of minimality. For the equivalence: $T$ is a clause $\iff$ $T$ hits every clause (Cor E.1) $\iff$ $T$ hits every minimal clause (F2) $\iff$ $T$ is a transversal of $\mathcal M$. Hence the clauses are exactly the transversals of $\mathcal M$, and the *minimal* clauses (= $\mathcal M$) are exactly the *minimal* transversals of $\mathcal M$, i.e. $\mathcal M=b(\mathcal M)$. $\qquad\square$

In particular (recovering Tool 2 intrinsically) any two members of $\mathcal M$ intersect: each member is a transversal, hence meets every member. Self-blocking clutters can be infinite, so Lemma 1 alone does not give the Crux — the arithmetic (the small/large split) must enter. Lemma 1 is the clean combinatorial skeleton the arithmetic hangs on.

---

### 2. Finite-ground-set reduction: it suffices that $Q$ is finite (PROVED)

Define the **large essential primes**
$$Q:=\{\text{primes }q>P_1:\ q\in C\text{ for some minimal clause }C\}.$$
(Small essential primes all lie in the fixed finite set $\Pi$.)

**Proposition 2 (replaces the false Proposition 1).** If $Q$ is finite, then $\mathcal M$ is finite, and hence (certified finish) the conclusion holds.

*Proof.* Let $C\in\mathcal M$. Each prime $p\in C$ is either $\le P_1$ (so $p\in\Pi$) or $>P_1$; in the latter case $p$ lies in the minimal clause $C$, so by definition $p\in Q$. Hence $C\subseteq\Pi\cup Q$. As $\Pi$ and $Q$ are both finite, $\Pi\cup Q$ is a finite ground set, so it has finitely many subsets; therefore $\mathcal M$ (a family of subsets of $\Pi\cup Q$) is finite. Apply the certified finish. $\qquad\square$

This is the airtight, non-circular reduction that survives $a_1=385$: it does **not** claim minimal clauses avoid large primes (they need not — $19$ is essential for $a_1=385$); it only needs *finitely many* large essential primes. It replaces the round-1 false Proposition 1 ("every minimal clause $\subseteq\Pi$"). Note we do **not** need any per-large-prime bound: finiteness of the *ground set* $\Pi\cup Q$ already caps $\mathcal M$.

> **Reduced Crux.** $Q$ is finite.

---

### 3. Mutual-witness lemma and the reconciliation map (PROVED, up to the fiber bound)

**Lemma 3 (mutual witness).** Let $q\in Q$. Then there exist two *distinct* minimal clauses $C,D$ with
$$q\in C\cap D\quad\text{and}\quad C\cap D=\{q\},$$
and their small-shadows $\sigma(C),\sigma(D)$ are **disjoint nonempty** subsets of $\Pi$.

*Proof.* Pick a minimal clause $C$ with $q\in C$ (exists since $q\in Q$). By Cor 1.1, $C$ contains a small prime $p_0\le P_1$; as $q>P_1$, $p_0\ne q$, so $C\setminus\{q\}\ne\emptyset$. Since $C$ is minimal and $C\setminus\{q\}\subsetneq C$, the set $C\setminus\{q\}$ is **not** a clause; by Lemma 1 (Cor E.1 direction) it therefore does **not** hit every clause: there is a clause $D_0$ with $D_0\cap(C\setminus\{q\})=\emptyset$. Take a minimal clause $D\subseteq D_0$ (F1). Then $D\cap(C\setminus\{q\})\subseteq D_0\cap(C\setminus\{q\})=\emptyset$, so $D\cap C\subseteq\{q\}$; by Tool 2 (both are clauses) $D\cap C\ne\emptyset$, hence $D\cap C=\{q\}$. Thus $q\in D$. Since $p_0\in C\setminus\{q\}$ but $p_0\notin D$, we have $C\ne D$. Finally $\sigma(C)\cap\sigma(D)\subseteq(C\cap D)\cap\Pi=\{q\}\cap\Pi=\emptyset$ (as $q$ is large), and both shadows are nonempty by Cor 1.1. $\qquad\square$

Lemma 3 lets us define, choosing one such pair $(C_q,D_q)$ for each $q\in Q$, a **reconciliation map**
$$\Phi:\ Q\ \longrightarrow\ \mathcal P^{\ne\emptyset}(\Pi)\times\mathcal P^{\ne\emptyset}(\Pi),\qquad \Phi(q)=\bigl(\sigma(C_q),\sigma(D_q)\bigr),$$
whose image lies in the **finite** set of ordered pairs $(\sigma,\tau)$ of disjoint nonempty subsets of $\Pi$ (at most $3^{|\Pi|}=3^{\pi(P_1)}$ pairs). Therefore:

**Proposition 3.** $Q$ is finite $\iff$ every fiber $\Phi^{-1}(\sigma,\tau)$ is finite.

*Proof.* $\Phi$ has finite image; a map into a finite codomain has finite domain iff all fibers are finite. $\qquad\square$

Combining §§2–3: **the whole problem is reduced to proving that each fiber $\Phi^{-1}(\sigma,\tau)$ is finite** — i.e. only finitely many large primes $q$ can each reconcile the *same* disjoint pair of small-shadows $(\sigma,\tau)$. This is the isolated remaining gap; §4 records what is known toward it and why it is the genuine hard core.

---

### 4. Status of the fiber bound (the GAP), and partial progress

**Gap (Reduced Crux, restated).** For each pair $(\sigma,\tau)$ of disjoint nonempty subsets of $\Pi$, only finitely many large primes $q$ admit minimal clauses $C_q\supseteq\sigma\cup\{q\}$, $D_q\supseteq\tau\cup\{q\}$ with $C_q\cap D_q=\{q\}$, $\sigma(C_q)=\sigma$, $\sigma(D_q)=\tau$.

**Partial progress (PROVED): a conditional fiber bound.** Fix a nonempty shadow $\sigma\subseteq\Pi$. Since a minimal clause $C_q$ with $\sigma(C_q)=\sigma$ contains $q\notin\sigma$, the set $\sigma\subsetneq C_q$ is **not** a clause, so (Lemma 1) $\sigma$ misses some clause; shrinking it (F1) fix **one** minimal clause $W_\sigma$ with $W_\sigma\cap\sigma=\emptyset$ (depending only on $\sigma$, not on $q$). Now suppose additionally that $C_q$ has **exactly one large prime** (namely $q$), i.e. $C_q=\sigma\cup\{q\}$. Then, because $W_\sigma$ avoids $\sigma$,
$$C_q\cap W_\sigma=(\sigma\cup\{q\})\cap W_\sigma=\{q\}\cap W_\sigma,$$
and $C_q\cap W_\sigma\ne\emptyset$ (Tool 2), forcing $q\in W_\sigma$. Thus **every such $q$ lies in the single finite set $W_\sigma$**, so there are at most $|W_\sigma|$ of them. Summing over the finitely many shadows $\sigma\subseteq\Pi$: *if every minimal clause contains at most one large prime (call this **Lemma T**), then $Q$ is finite and the problem is solved.*

**Why this is not yet a proof.** Lemma T ("at most one large prime per minimal clause") is verified for many $a_1$ (e.g. $385,4199,255,1001,2145,5005,2431,435,\dots$: every genuine minimal clause has $\le1$ large prime), but for large primorials such as $a_1=255255$ a *shallow* simulation ($N=1000$) exhibits apparent minimal clauses with two or more large primes (e.g. $\{2,3,47,911\}$). The outline-reviewer independently flagged that shallow simulation of primorial starts **wildly overcounts** minimal clauses (truncation artifact: at $a_1=2310$ the count collapses to $1$ clause / $0$ large primes only at $N\ge1600$). I could not run these primorials to convergence within budget, so **Lemma T is not established** — it may hold with the apparent multi-large clauses being truncation artifacts, or it may genuinely fail, in which case the fiber bound needs the general (non-single-large) argument. Either way the fiber bound remains open.

**Nature of the wall.** The fiber bound is genuinely **arithmetic**, not clutter-combinatorial: two large primes $q\ne q'$ in the same fiber give minimal clauses $C_q,C_{q'}$ of the same small-shadow $\sigma$, which share $\sigma$ and are perfectly consistent with Lemma 1 (self-blocking clutters admit arbitrarily many such members). So no purely combinatorial argument on $\mathcal M$ can bound the fiber; the bound must come from the **greedy minimality/size** structure — precisely: a large prime $q$ can enter a term only when no smaller admissible integer of small-shadow $\sigma$ exists in the current gap, and once the $\sigma$-transversal structure "matures" this stops happening. Making this rigorous is the shared hard core with the descent framing.

**First-appearance partial (PROVED, imported from round 1).** For a large prime $q$, let $i$ be the least index with $q\mid a_i$. Then $b:=a_i/q^{v_q(a_i)}$ (support $S_i\setminus\{q\}$) hits every earlier clause $S_\ell$ ($\ell<i$), since $a_i$ hits $S_\ell$ via a prime $\ne q$ (as $q\nmid a_\ell$). Hence $b\in A_{i-1}$; if $b>a_1$ then $b$ is an earlier term (Sub-lemma E) and $S_i\setminus\{q\}\subsetneq S_i$ is a clause, so **the first-appearance clause of $q$ is not minimal.** This shows every large *essential* prime must appear in a *later* (mutual-witness) clause — consistent with Lemma 3 — but does not bound the number of distinct such primes.

---

### 5. Spec-concerns note (for the orchestrator)

- **Clique-descent's sunflower step (round-2 outline step 3) is not free.** The claim "for fixed large $q$, the minimal clauses containing $q$ have pairwise-disjoint small-shadows" is **not** provable from the self-blocking-clutter combinatorics alone (I could not find a combinatorial proof, and self-blocking clutters do not force it). It appears to require the same greedy-size arithmetic as the fiber bound. So clique-descent does *not* have a free per-prime bound; fortunately **Proposition 2 makes the per-prime bound unnecessary** — finiteness of the ground set $\Pi\cup Q$ alone gives the Crux, so the *sole* gap is "$Q$ finite" (equivalently, finite fibers of $\Phi$).
- **Shared-gap confirmation.** The fiber bound (this approach) and descent-shared-prime's Lemma S′ $b\le a_1$ branch are, as the reviewer predicted, the *same* arithmetic phenomenon viewed two ways: a large prime cannot repeatedly reconcile a fixed disjoint small-shadow gap because the greedy prefers smaller reconcilers. If both stall again, round 3 should open the growth/size framing directly (bound, via $a_n\le n\,a_1$ and the mature small-prime admissible density, the largest prime that can appear in a term).

## Full proof
(Not present: Status is `partial`. §§0–3 are complete and rigorous — the problem is reduced to "$Q$ finite" via the self-blocking clutter, the finite-ground-set Proposition 2, and the mutual-witness reconciliation map. The sole gap is the finite-fiber statement in §4.)

## Promotable lemmas
- **Lemma 1 (self-blocking clutter).** The minimal-clause family $\mathcal M$ satisfies: a nonempty prime-set is a clause iff it is a transversal of $\mathcal M$; consequently $\mathcal M=b(\mathcal M)$. *(Proved in full in §1; intrinsic restatement of Cor E.1 + F2.)*
- **Proposition 2 (finite-ground-set reduction).** If $Q=\{$large primes in some minimal clause$\}$ is finite, then $\mathcal M$ is finite and $a_{n+T}=a_n+L$ holds for all $n$. *(Proved in full in §2; the correct replacement for the retracted false Proposition 1. Reusable by every approach — it turns the crux into "finitely many large essential primes.")*
- **Lemma 3 (mutual witness).** Every large essential prime $q$ lies in two distinct minimal clauses meeting in exactly $\{q\}$, with disjoint nonempty small-shadows; hence the reconciliation map $\Phi:Q\to\{$disjoint shadow-pairs$\}$ has finite image, and $Q$ is finite iff $\Phi$ has finite fibers. *(Proved in full in §3.)*
