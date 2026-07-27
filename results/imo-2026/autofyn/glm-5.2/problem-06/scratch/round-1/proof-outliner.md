# IMO 2026 P6 — proof-outliner field (round 1)

Problem: greedy sequence $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \forall i\le n\}$. Prove $\exists\,T,L>0$ with $a_{n+T}=a_n+L$ for all $n$.

Shared structural skeleton (used by every approach, made rigorous per-slug): write $P(m)$ for prime-divisor set. $a_{n+1}$ admissible $\iff$ $P(a_{n+1})$ is a **transversal** (hitting set) of $\mathcal F_n=\{P(a_1),\dots,P(a_n)\}$, equivalently of its minimal elements $\mathcal M_n$ (minimal under $\subseteq$). Only minimal supports constrain admissibility.

THE SHARED WALL: every naive route needs "only finitely many primes are load-bearing / $\mathcal M_n$ stabilizes." The field below diversifies the MECHANISM for this (or sidesteps it), so the approaches do not die on one gap.

---

## density-promotion-bound
**new** | Target: whole claim.
**Framing (mechanism α — analytic density).** Prove $P$ finite via a Mertens/$\Sigma 1/p$ covering-density argument: once enough small primes are structural, $P$-smooth transversal-composites are so dense that the greedy always finds one before any number needing a new prime. Then the valid set is periodic mod $L=\prod_{p\in P}p$, and the greedy is a finite-state walk.

Technique: density/counting + finite-state pigeonhole (KB "Pigeonhole/extremal", "Modular arithmetic, CRT").

Skeleton:
1. Define structural prime $p$: ever the sole satisfier of some past constraint (i.e. some $a_j$ whose only common factor with $a_{n+1}$ is $p$). Let $S$=structural set. Show $S$ only grows (monotone). — by definition + "structural stays structural."
2. Free-rider lemma: a prime $q\notin S$ dividing a term that also has a structural factor never becomes structural (its constraint is weaker than the structural co-rider's). — because the constraint "$m$ divisible by $p$ or $q$" is implied by "$m$ divisible by $p$" once $p\in S$ rides with $q$ in some term; inductive on co-rider set $\subseteq S$. **GAP**: the induction needs that every co-rider is structural — prove the support of every term contains a structural prime (else that term's whole support is non-structural, forcing a new structural prime — contradiction-handling needs care).
3. **Crux (GAP):** $|S|$ bounded. Mechanism: let $S_k$ be the structural set after $k$ promotions. Show $\exists K$ s.t. beyond promotion $K$, the set of $S_K$-transversal composites in any interval $[x,x+C\cdot\prod_{p\in S_K}p]$ is nonempty and beats the next multiple of any candidate new prime $q$. Use $\sum_{p\le x}1/p\sim\log\log x$ (Mertens) to lower-bound transversal density; a new prime $q$ requires ALL $S_K$-transversals in $(a_n, \text{next mult of }q)$ to fail other constraints — impossible once density $>1-1/q$. **Hard because:** the constraints are not independent; need a clean lower bound on transversal density that survives the "hitting every minimal support" condition (inclusion-exclusion / Lovász-local-lemma flavor).
4. Once $S$ stable, $L=\prod_{p\in S}p$ (squarefree). Valid set $V=\{m:P(m)\supseteq\text{hits }\mathcal M\}$ is a union of residue classes mod $L$ (CRT over squarefree $L$). — by CRT.
5. Greedy: $a_{n+1}=\min\{m\in V:m>a_n\}$; state $a_n\bmod L\in V$ finite, deterministic update $\to$ eventually periodic residues. — finite-state pigeonhole.
6. Lift: periodic residues mod $L$ $\Rightarrow$ $a_{n+T}=a_n+L$ (period-sum $=L$ because residues repeat exactly once per full advance of $L$). **GAP**: prove the cycle is a single cycle and the sum is exactly $L$, not a proper divisor — needs the walk visits every residue of $V$ (connectivity of the cyclic-next graph on $V$).

Key lemmas:
- $|S|$ bounded — because transversal density $\ge 1-\prod(1-1/p)$ exceeds any single-prime cover once $S$ large (Mertens).
- Free-rider invisibility — because non-structural constraints are logically weaker than a structural one riding in the same term.

Open gaps: step 2 induction base; step 3 (the real wall — density bound surviving correlated constraints); step 6 (single-cycle / period-sum $=L$).
Watch out for: density bound must be on the *transversal* set (hitting all minimal supports), not all $S$-smooth numbers — these differ when $\mathcal M$ has overlapping supports.

---

## bertrand-dickson-eviction
**new** | Target: whole claim.
**Framing (mechanism β — WQO + Bertrand eviction).** Bound the ambient prime set by evicting large primes (a prime $q$ bigger than the smallest available $P$-transversal composite can never be a minimal support), then invoke Dickson's lemma (no infinite antichain in $\mathbb N^k$) to force $\mathcal M$ finite and stabilizing.

Technique: Bertrand's postulate (KB) + Dickson's lemma (state/prove; standard, short) + CRT/pigeonhole finish.

Skeleton:
1. **Eviction lemma (GAP):** $\exists C=C(a_1)$ s.t. every prime $q>C$ that ever divides some $a_n$ is a free rider (non-structural). Mechanism: if $q$ is to be structural it must be the unique connector to some $a_j$ at some greedy step, i.e. no $P_{<q}$-transversal composite lies in $(a_n, a_{n+1})$ with $a_{n+1}\equiv0\pmod q$. But among primes $\le q$ already collected, a Bertrand-style step gives a composite $<q$ (or $<\text{next mult of }q$) hitting all current minimal supports — contradiction. **Hard because:** need the current minimal supports to be hittable by small primes already collected; inductive on the build-up of $P$. The constant $C$ depends on the *evolution*, not just $a_1$ — must show it stabilizes.
2. With ambient primes bounded by $C$, represent each $P(a_n)\cap\{p\le C\}$ as a $0/1$-vector in $\{0,1\}^{\pi(C)}$. Dickson's lemma ($\mathbb N^k$ under product order is a WQO $\Rightarrow$ no infinite antichain): the set of minimal supports $\mathcal M$ is a finite antichain. — Dickson (cite + short proof).
3. Monotone stabilization: $\mathcal M_n$ changes by adding minimal elements / removing newly-dominated ones; an antichain in a WQO cannot gain minimal elements forever (each gain strictly refines; finitely many possible $\Rightarrow$ stabilizes). — WQO + finite antichain.
4. Once $\mathcal M_\infty$ stable, finish as in density route steps 4–6: $L=\prod_{p\in\bigcup\mathcal M_\infty}p$, valid set periodic mod $L$, finite-state walk, periodic.

Key lemmas:
- Eviction of primes $>C(a_1)$ — because a smaller composite transversal always outbids them (Bertrand guarantees a prime in a dyadic window to build the composite).
- $\mathcal M$ finite — by Dickson once ambient primes bounded.

Open gaps: step 1 (Bertrand eviction with a stabilization-respecting $C$ — the distinct wall here); the single-cycle lift (step 6 of density route, shared).
Watch out for: Dickson needs the ambient set FIXED before applying — the eviction must give a single uniform $C$, not one per timestep.
Diversity vs density: attacks the SAME "$P$ finite" conclusion but via WQO structure, not analytic density — fails on a different sub-step (the eviction constant).

---

## bounded-gap-lcm-reduction
**new** | Target: whole claim. **Sidestep candidate — does NOT isolate "$P$ finite" first.**
**Framing (mechanism γ — aimo-0678 adapted).** Prove gaps $d_n=a_{n+1}-a_n$ are BOUNDED by some $G$ (a different target from "$P$ finite"); then reduce $a_n\bmod M$, $M=\operatorname{lcm}(1,\dots,G)$, to a finite state and apply the aimo-0678 "bound one coordinate, reduce the other mod lcm" pigeonhole. Finiteness of load-bearing primes becomes a CONSEQUENCE (only primes $\le G$ can be the unique connector in a bounded-gap world).

Technique: bounded-gap + lcm reduction + pigeonhole (crux `aimo-0678`: "once one coordinate bounded, reduce the other mod lcm of bounded values").

Skeleton:
1. **Bounded-gap lemma (GAP, the wall here):** $\exists G$ s.t. $d_n\le G$ for all $n$. Mechanism: in any window $(a_n, a_n+G]$ there is a valid $m$ (hits all minimal supports). This is a *syndeticity* claim on the valid set $V_n$. **Hard because:** $V_n$ shrinks as $n$ grows; must show it stays syndetic with a uniform gap $G$ even as new minimal supports appear. Candidate: $G=$ product of primes dividing $a_1$ (a multiple of $a_1$ is always valid — but is it within $G$? $a_n$ grows, so the next multiple of $a_1$ above $a_n$ is within $a_1$ of it... is $a_1$ a valid choice? $a_1$'s multiples hit $a_1$ but do they hit ALL $a_i$? No — only those sharing a factor with $a_1$. So multiples of $a_1$ need NOT be valid.). This gap is genuinely open.
2. Assuming $d_n\le G$: any prime $q>G$ that divides $a_{n+1}=a_n+d$ ($d\le G$) — to be the *unique* connector to some $a_i$, need $q|a_i$ too, so $a_i\equiv a_{n+1}\equiv0\pmod q$, i.e. $a_i,a_{n+1}$ are consecutive-ish multiples of $q$ within the sequence. Since $q>G\ge d_n$, between two multiples of $q$ in the sequence the value jumps by $\ge q>G$, but consecutive terms jump $\le G$ — so two consecutive terms can't both be multiples of $q$ unless $q|d_n$... Pigeonhole shows large primes appear sparsely and can't be the unique connector. (GAP: formalize "unique connector" count $\Rightarrow$ only primes $\le G$ are load-bearing.)
3. With load-bearing primes $\le G$, take $M=\operatorname{lcm}(1,\dots,G)$ (or $\prod_{p\le G}p$). The state $(a_n\bmod M, \text{active constraint signature})$ is finite — signature = which residue classes mod small primes have been claimed; finite since primes $\le G$ finite. (GAP: the signature must capture the constraint family reduced mod $M$ — show finitely many signatures.)
4. Deterministic update on finite state $\to$ eventually periodic (aimo-0678 finite-pair pigeonhole). — KB "Order of element / eventual periodicity mod $m$".
5. Periodic state $\Rightarrow$ periodic $a_n\bmod M$ $\Rightarrow$ periodic gaps $d_n$ with period $T$ and sum $L=M\cdot$(integer) $\Rightarrow$ $a_{n+T}=a_n+L$.

Key lemmas:
- Bounded gaps $d_n\le G$ — because the valid set stays syndetic (the genuinely hard, distinct-from-"$P$ finite" target).
- Large primes ($>G$) non-load-bearing — because in a bounded-gap world they appear too sparsely to be unique connectors.

Open gaps: step 1 (bounded gaps — the wall, *different statement* than "$P$ finite"); step 2 (sparse-large-prime formalization); step 3 (finite signature).
Diversity: attacks periodicity DUAL to "$P$ finite"; if the wall "$P$ finite" proves unbreakable, this route can still succeed via the gap bound. Risk: bounded gaps may be EQUIVALENT to $L$ finite (since gaps $\le L$ in the periodic regime) — if so this route collapses onto the wall; flag for reviewer.

---

## transversal-single-cycle-finish
**new** | Target: whole claim. **Builds the post-stabilization machinery rigorously; leaves "$\mathcal M$ stabilizes" as an explicit gap (to be filled by density/Dickson).**
**Framing (mechanism δ — order-theoretic finish).** Assuming $\mathcal M$ (minimal supports) has stabilized with ambient prime set $P$, rigorously prove: (a) free-rider primes are invisible, (b) $L=\prod P$ is squarefree and is the exact period-sum, (c) the greedy walk on the transversal residue set $R\subseteq\mathbb Z/L\mathbb Z$ is a SINGLE cycle, (d) $a_{n+T}=a_n+L$ with $T=|R|$ (transient absorbed). The distinctive hard step is the single-cycle / period-sum-$=L$ proof (a gap common to ALL routes but never isolated elsewhere).

Technique: CRT + cyclic order on residues + extremal (KB "Modular arithmetic, CRT", "Pigeonhole/extremal").

Skeleton:
1. Assume $\mathcal M$ stable, $P=\bigcup\mathcal M$, $L=\prod_{p\in P}p$ (squarefree — prove no prime power: a structural prime contributes one covering role; GAP). Free-rider lemma: primes $\notin P$ invisible to admissibility (GAP: inductive, as in density route step 2).
2. $R=\{r\bmod L:\{p\in P:p|r\}\text{ hits }\mathcal M\}$ — finite. Admissibility $\iff$ $m\bmod L\in R$ (CRT over squarefree $L$).
3. Greedy map $\varphi:R\to R$, $\varphi(r)=$ least residue $>r$ cyclically in $R$ (i.e. next element of $R$ above $r$, wrapping). $a_{n+1}=a_n+(\varphi(r)-r\bmod L)$. Deterministic.
4. **Single-cycle lemma (GAP, distinctive):** $\varphi$ is a single cycle on $R$ (not several sub-cycles). Mechanism: $\varphi$ is the "cyclic successor" map; it is a bijection (inverse = cyclic predecessor) on a finite set $\Rightarrow$ union of cycles; need ONE cycle. Use: $R$ is pairwise-$P$-intersecting (any two residues share a structural prime — else their supports are disjoint, neither hits the other's... ). Pairwise-intersecting + greedy-smallest-first $\Rightarrow$ the cyclic order is connected. **Hard because:** "pairwise intersecting $\Rightarrow$ connected cyclic order" is false in general (e.g. $R$ could split into two intersecting clusters with no cross-residue); need the greedy's dynamics to force cross-cluster bridges.
5. Single cycle $\Rightarrow$ period $T=|R|$, and over one cycle residues advance by exactly $L$ (each residue visited once, running value increases by $L$). Hence $a_{n+T}=a_n+L$. Transient: before entering $R$, finitely many terms — show they're absorbed (the relation holds "for all $n$" including the transient — GAP: prove transient length $0$ OR handle by redefining $T,L$; data suggests transient $0$ but must prove).

Key lemmas:
- $\varphi$ is a single cycle on $R$ — because $R$ pairwise-intersecting under $P$ AND the greedy's smallest-first rule forces a connected cyclic order (the real distinctive gap).
- Period-sum $=L$ exactly — because one full cycle visits each residue once $\Rightarrow$ advance $=L$.

Open gaps: squarefree $L$; free-rider induction; **single-cycle lemma (the isolated distinctive gap)**; transient absorption.
Diversity: does NOT attack the wall; isolates and attacks a DIFFERENT hard step (single-cycle) that every other route also needs but leaves implicit. Pairs with any of approaches 1–3 that supply the stabilization.

---

## omega-induction-loaded
**new** | Target: whole claim. **Speculative / higher-risk reframe.**
**Framing (mechanism ε — structural induction on $\omega(a_1)$).** Strengthen the claim (induction loading): for a sequence starting at $a_1$ with $\omega(a_1)=k$ distinct prime factors, the theorem holds AND the structural set $S$ satisfies $|S|\le g(k)$ for a function depending only on $k$ (data: $k=2$ gives $|S|\le5$; $k=3$ gives $|S|\le5$; promoted primes are always the smallest few). Prove by induction on $k$.

Technique: strong induction + structural reduction (KB "Induction", "Invariants/monovariants").

Skeleton:
1. Base $k=1$ ($a_1$ a prime power or single-prime): collapse to $S=\{p\}$, $T=1$, $L=p$ — prove the greedy always reaches the next multiple of $p$ before needing another prime. (Mostly direct; small GAP: characterize when collapse happens.)
2. Inductive step ($\omega(a_1)=k$): $a_2$ = smallest $>a_1$ sharing a prime with $a_1$. Either (i) collapse to a single prime $p|a_1$ (done, base case), or (ii) a new prime $q$ is promoted.
3. **Promotion-size lemma (GAP):** any promoted prime $q\le g(k)$ (small, depending only on $k$). Mechanism: $q$ promoted $\iff$ no $S$-transversal composite in $(a_n,\text{next mult of }q)$; the smallest such composite is $\le\prod_{p\in S}p\le\prod_{i=1}^{k+g(k-1)}p_i$ (bounded by induction on $|S|$). So $q$ bounded. (Circular — needs care; possibly reduce to bounding $|S|$ by induction on $k$.)
4. **Reduction lemma (GAP, the wall here):** after promotion, the effective structure reduces to an instance with $\omega\le k$ (the promoted prime merges into the structural set; the "competing" primes of $a_1$ that haven't collapsed are $\le k$). Apply induction. Mechanism: the constraint family's minimal supports use $\le k$ "active" primes from $a_1$ plus promoted small primes; promoted primes are bounded in number by $g(k)$.
5. Finish: $|S|\le g(\omega(a_1))$ finite $\Rightarrow$ stabilize $\Rightarrow$ periodic via the transversal machinery (approach 4).

Key lemmas:
- $|S|\le g(\omega(a_1))$ — by induction; promoted primes bounded in number by the loaded hypothesis.
- Reduction to lower-$\omega$ instance — because each promotion absorbs one competing prime into the structural set.

Open gaps: promotion-size lemma (circularity risk); reduction lemma (the real wall — showing $\omega$ effectively decreases); base-case collapse characterization.
Diversity: genuinely different framing (structural induction on prime-factor count); if $|S|\le g(k)$ is FALSE (i.e. $|S|$ unbounded for fixed $k$), this approach dies — data is suggestive but not conclusive. Flag as speculative.
Watch out for: the claim $|S|\le g(k)$ is an empirical conjecture; a single counterexample (large $|S|$ for $k=2$) kills the approach. Run a computational check on more $a_1$ with $\omega=2$ before committing builder time.

---

## Diversity map (for the reviewer)

| slug | mechanism | attacks the wall? | the wall (distinct statement) |
|---|---|---|---|
| density-promotion-bound | α: Σ1/p density | yes, head-on | transversal-density lower bound |
| bertrand-dickson-eviction | β: WQO+Bertrand | yes, differently | Bertrand eviction constant stabilizes |
| bounded-gap-lcm-reduction | γ: aimo-0678 dual | sidesteps | bounded gaps $d_n\le G$ |
| transversal-single-cycle-finish | δ: order/CRT finish | no (leaves wall as gap) | single-cycle + period-sum$=L$ |
| omega-induction-loaded | ε: structural induction | reframe | $\|S\|\le g(\omega(a_1))$ (conjectural) |

Approaches 1,2,4 share the conclusion "$\mathcal M$ stabilizes" but 1,2 attack it by different mechanisms (density vs WQO) and 4 leaves it as a gap and attacks a different step. Approach 3 sidesteps (bounded gaps). Approach 5 reframes via induction. No two approaches share the same wall via the same mechanism — the field does not collapse to one gap.

## Build set recommendation

Advance to builders (round 1): **`density-promotion-bound`, `bertrand-dickson-eviction`, `bounded-gap-lcm-reduction`, `transversal-single-cycle-finish`**.

- The three wall-attacking/sidestepping approaches (1,2,3) run in parallel — if any one's mechanism lands, the wall falls and approach 4 supplies the finish.
- Approach 4 builds the post-stabilization machinery rigorously in parallel; its outputs (free-rider lemma, squarefree-$L$, single-cycle) are IMPORTABLE by 1/2/3.
- Hold `omega-induction-loaded` for round 2: first run a computational check of the conjecture $|S|\le g(\omega(a_1))$ on more $\omega=2$ starts (e.g. $a_1=pq$ for primes up to 200); if it survives, promote to the build set as the 5th. If it fails, drop it.
- Suggest one builder also attempt the **free-rider lemma** as a certifiable shared lemma (it's needed by 1,2,4 and is a clean inductive claim) — but this is a sub-lemma, not a whole-claim slug; register it in `lemmas/` once certified, do NOT make it its own approach.
