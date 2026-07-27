# Approach γ: bounded-gap-lcm-reduction

IMO 2026 P6: $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \forall i\le n\}$; prove $\exists\,T,L>0$ with $a_{n+T}=a_n+L$ for all $n$.

## Status
partial

## Approaches tried
- γ round 2 (first build from scratch): introduced the **min-transversal-product monovariant** $\mathrm{mtp}(\mathcal M_n)=\min\{\prod_{p\in T}p:T\text{ transversal of }\mathcal M_n\}$ and proved, unconditionally, (i) $\mathrm{mtp}$ is monotone non-decreasing and (ii) the *global* gap bound $a_{n+1}-a_n\le\mathrm{mtp}(\mathcal M_n)$ at every step. Computationally verified on 8 seeds; the gap bound is tight (running max gap = stabilized mtp). Certified as `mtp-monovariant-and-gap-bound`. Two open sub-gaps: **GAP-1** (mtp bounded above) and **GAP-3** (bounded gaps $\Rightarrow$ $\mathcal M$ finite). Single-gap-trap guard: GAP-1 attacked via pigeonhole-on-small-primes, GAP-3 via `aimo-0678` residue-window finite-state.
- γ round 3 (this round): **scrutinized the dispatch's claim that W1 closes GAP-1.** Verdict (the crux of this round): **W1 does NOT bound the mtp PRODUCT.** W1 ("the mtp-witness $T^*$ contains a prime $\le p^*$") guarantees only a *small factor* in $T^*$; $T^*$ may also contain large primes, so $\prod T^*=\mathrm{mtp}$ is not bounded by $\prod_{p\le p^*}p$ from W1 alone (concrete counterfamily: $T^*=\{5,97\}$, $p^*=5$, product $485>30=\mathrm{primorial}(5)$, satisfies W1). The bound $\mathrm{mtp}\le\mathrm{primorial}(p^*)$ is instead a consequence of **SPT** ("every minimal $M\in\mathcal M_n$ contains a prime $\le p^*$"), because SPT makes $S:=P_{\mathrm{ess},n}\cap\{p:p\le p^*\}$ a transversal of product $\le\mathrm{primorial}(p^*)$. SPT is a separate, *stronger* 0-violation conjecture (41 saturated seeds, 0 violations, this round) whose hard half (the strict-beat case, 174/344 promotions) requires a short-interval smooth/rough-number density argument (W2) that is NOT in `knowledge_base.md` and is unproven. **Hence GAP-1 is reduced to SPT but NOT closed.** GAP-3 likewise assessed: the free-rider-eviction claim (large entering primes evicted by crashes) does NOT refute the unique-connector obstruction under γ's pure "gaps $\le G$" hypothesis, because eviction requires the crash mechanism (a stronger hypothesis than bounded gaps); and the strong free-rider universality is FALSE ($a_1=15$: the entering prime $2$ persists as essential in the final triangle $\{\{3,5\},\{2,3\},\{2,5\}\}$). The `aimo-0678` lcm-reduction finite-state route is DEAD (entering primes unbounded, confirmed round-3). GAP-3 stays open, and is effectively superseded by `pstar-core-straggler`'s direct Cov-monovariant+crash route to $\mathcal M$ finite (which does not pass through "gaps $\le G\Rightarrow\mathcal M$ finite" at all). Outcome: honest partial; the mtp monovariant remains the certified reusable asset; both sub-gaps remain open with sharpened articulation — in particular the field should stop citing W1 as a GAP-1 closer.

## Current best
The **mtp monovariant** (certified `mtp-monovariant-and-gap-bound`, unconditional): $\mathrm{mtp}(\mathcal M_n)$ is monotone non-decreasing and $a_{n+1}-a_n\le\mathrm{mtp}(\mathcal M_n)$ for every $n$ — the sharpest unconditional gap control in the field, importable by α/β/ε. Conditional on closing GAP-1 and GAP-3, the finish is the certified `post-stabilization-theorem` (δ).

The two open sub-gaps, sharpened this round:
- **GAP-1 (mtp bounded):** equivalent (via monotonicity + KB *Invariants & monovariants*) to "$\mathrm{mtp}$ stabilizes", i.e. a permanent small transversal exists. The dispatch's proposed W1-route is **insufficient**: W1 (witness $T^*$ carries a prime $\le p^*$) does NOT bound $\prod T^*$. The correct GAP-1-closing statement is **SPT** (every minimal $M\in\mathcal M_n$ contains a prime $\le p^*$), which makes $S=P_{\mathrm{ess},n}\cap\{p\le p^*\}$ a transversal of product $\le\mathrm{primorial}(p^*)$. SPT is a 0-violation conjecture (41 seeds this round) whose hard half (strict-beat promotions, W2) is an unproven short-interval smooth-number density step (no KB entry). **Open.**
- **GAP-3 (bounded gaps $\Rightarrow$ $\mathcal M$ finite):** the `aimo-0678` lcm-reduction route is DEAD (the bounded coordinate is the gap $d_n$, not a term value; the greedy depends on $\mathcal M_n$, and entering primes are unbounded so no finite reduction modulus exists). The unique-connector obstruction stands: under ONLY "gaps $\le G$", a large fresh prime $q>G$ can serve as the unique connector between a new minimal $M'$ and an old minimal $M_0$ (with $M'\cap M_0=\{q\}$), perfectly consistent with gaps $\le G$. The free-rider-eviction claim does NOT refute this under γ's hypothesis, because eviction needs the crash mechanism (a stronger assumption than bounded gaps). **Open.** The live route to $\mathcal M$ finite is now `pstar-core-straggler`'s Cov-monovariant+crash-inevitability, not γ's GAP-3.

## Full proof
*(Not presented — both GAP-1 and GAP-3 are open. Below is the rigorous scaffolding: the certified monovariant machinery, the honest crux analysis of why W1 does not close GAP-1, the verdict on GAP-3, and the conditional finish.)*

---

### 0. Setup and conventions

Write $P(m)$ for the set of prime divisors of $m>1$. Define
$$\mathcal M_n:=\min\{P(a_i):1\le i\le n\}\quad\text{(inclusion-minimal prime-supports among the first $n$ terms)},$$
an antichain of nonempty finite sets of primes; $P_{\mathrm{ess},n}:=\bigcup\mathcal M_n$; $\mathcal M:=\min\{P(a_i):i\ge1\}=\lim_n\mathcal M_n$. A set $T$ is a *transversal* of $\mathcal M_n$ if $T\cap M\neq\emptyset$ for every $M\in\mathcal M_n$. The admissibility rule is
$$a_{n+1}=\min\{m>a_n:P(m)\text{ is a transversal of }\mathcal M_n\}$$
because $\gcd(m,a_i)>1\iff P(m)\cap P(a_i)\neq\emptyset$, and hitting $\{P(a_i):i\le n\}$ is equivalent to hitting its minimal members $\mathcal M_n$.

We import the following certified, unconditional facts:
- `pairwise-intersection.md`: every two $P(a_i)$ meet, so $\mathcal M_n$ is a pairwise-intersecting antichain.
- `mtp-monovariant-and-gap-bound.md` (γ, certified r2): $\mathrm{mtp}$ monotone non-decreasing, $a_{n+1}-a_n\le\mathrm{mtp}(\mathcal M_n)$ at every step.
- `singleton-freeze.md`, and the conditional-on-$\mathcal M$-finite machinery `transversal-residue-characterization.md`, `universal-membership-no-transient.md`, `greedy-equals-cyclic-successor.md`, `cyclic-successor-single-cycle.md`, `post-stabilization-theorem.md` (all imported from δ).
- `freeze-lock`, `common-primes-bounded`, `Sat-criterion` (α r2, certified) for the freeze-branch import.

### 1. The mtp monovariant (CERTIFIED, restated)

Define
$$\mathrm{mtp}(\mathcal M_n):=\min\Bigl\{\prod_{p\in T}p:\ T\subseteq P_{\mathrm{ess},n},\ T\text{ a transversal of }\mathcal M_n\Bigr\}.$$
The minimum is over a nonempty finite set ($P_{\mathrm{ess},n}$ is itself a transversal).

**Lemma 1 (mtp monovariant — CERTIFIED as `mtp-monovariant-and-gap-bound`).**
(a) $\mathrm{mtp}(\mathcal M_n)\le\mathrm{mtp}(\mathcal M_{n+1})$ for all $n\ge1$.
(b) $a_{n+1}-a_n\le\mathrm{mtp}(\mathcal M_n)$ for all $n\ge1$.

*Proof.* See the certified lemma file. (a): refinement shrinks the transversal family, $\mathrm{Trans}(\mathcal M_{n+1})\subseteq\mathrm{Trans}(\mathcal M_n)$, so the minimum of $\prod T$ over the subset is $\ge$ the minimum over the superset. (b): a witness $T^*$ of product $L^*=\mathrm{mtp}(\mathcal M_n)$ has every multiple valid; the smallest multiple of $L^*$ above $a_n$ is $\le a_n+L^*$, and the greedy choice is $\le$ this valid candidate. ∎

**Corollary 1.1.** $a_{n+1}-a_n$ is bounded above by a monotone non-decreasing integer sequence.

*Proof.* Lemma 1(a)+(b). ∎

**Corollary 1.2 (trivial collapses).** If $a_1$ is even, $2\in P(a_1)$, so $\{2\}\in\mathcal M_1$; `singleton-freeze` freezes $\mathcal M=\{\{2\}\}$ and `post-stabilization-theorem` gives $a_{n+1}=a_n+2$ ($T=1,L=2$). If $a_1=p^k$, similarly $\{p\}\in\mathcal M_1$ gives $T=1,L=p$. Hence the only nontrivial case is **$a_1$ odd with at least two distinct prime factors**; we assume this henceforth. In this regime, $a_2$ is even (smallest valid $>$ an odd number is even), so $2$ enters at step 2.

### 2. GAP-1: is mtp bounded? (OPEN — crux analysis of the W1 route)

**Conjecture 2.1 (GAP-1).** There exists $G=G(a_1)$ with $\mathrm{mtp}(\mathcal M_n)\le G$ for every $n\ge1$.

By Lemma 1(a) and KB *Invariants & monovariants* (a bounded monotone integer sequence stabilizes), Conjecture 2.1 is equivalent to: **$\mathrm{mtp}(\mathcal M_n)$ stabilizes** at some $G^*$. Once stabilized, a *fixed* witness transversal $T^*$ of product $G^*$ persists as a transversal for all large $n$: when $\mathrm{mtp}$ first attains $G^*$ at time $n_0$, pick a witness $T^*$ of $\mathcal M_{n_0}$; §1 gives $\mathrm{Trans}(\mathcal M_{n_0+1})\subseteq\mathrm{Trans}(\mathcal M_{n_0})$, so either $T^*$ stays a transversal (and $\mathrm{mtp}$ stays $G^*$) or $T^*$ is lost and $\mathrm{mtp}$ *increases* — contradicting stabilization at $G^*$. Hence $T^*$ remains a transversal forever after $n_0$. Thus GAP-1 $\Leftrightarrow$ "a permanent small transversal exists".

**Why the naive bound fails.** $\mathrm{mtp}\le 2\,p_{\max}(a_1)$ (any bound in terms only of primes of $a_1$) is refuted: $a_1=175=5^2\cdot7$ yields $\mathrm{mtp}_{\mathrm{final}}=21=3\cdot7$, with the prime $3\notin P(a_1)$ entering mid-evolution (verified computationally, r2).

#### 2.1 The dispatch's W1-route — CRUX VERDICT: W1 does NOT bound the mtp product

The dispatch (following the smooth-analytic explorer) proposed closing GAP-1 via **W1**: "the mtp-witness $T^*$ always contains a prime $\le p^*:=\min P(a_1)$" (0 violations, 26 saturated seeds). The proposed chain was W1 $\Rightarrow$ $\mathrm{mtp}\le\mathrm{primorial}(p^*)$. **This chain is invalid.** We record the honest verdict carefully.

**Proposition 2.2 (W1 does not bound the product).** The implication
$$\text{(W1)}\;(\exists\,p\in T^*\text{ with }p\le p^*)\quad\Longrightarrow\quad \prod_{p\in T^*}p\le\prod_{p\le p^*}p\;=:\mathrm{primorial}(p^*)$$
is **false in general**. W1 guarantees only that $T^*$ contains a *small factor*; $T^*$ may also contain arbitrarily large primes, and the product of those large primes is unconstrained by W1.

*Proof of the negative verdict (counterfamily).* Fix $p^*=5$ (so $\mathrm{primorial}(5)=2\cdot3\cdot5=30$). Consider a transversal $T^*=\{5,97\}$. It satisfies W1 ($5\le p^*$) yet $\prod T^*=485>30=\mathrm{primorial}(p^*)$. More generally, for any $p^*$ and any prime $Q>p^*$ with $Q\cdot p^*>\mathrm{primorial}(p^*)$ (such $Q$ exists for every $p^*\ge5$, since $\mathrm{primorial}(p^*)/(p^*)$ is a fixed finite number), the transversal $\{p^*,Q\}$ satisfies W1 but violates the claimed bound. Hence W1 alone furnishes no upper bound on $\mathrm{mtp}=\prod T^*$. ∎

(The smooth-analytic explorer itself flagged this in its "cheap-kill candidates": a direct inequality $\prod(\text{large-only transversal})>\mathrm{primorial}(p^*)$ does *not* hold in general — constructible counterfamilies exist — so the small-prime-in-witness fact is "genuinely empirical-and-tight, not a formality." Our Proposition 2.2 sharpens this: even granting W1, the product bound does not follow.)

#### 2.2 The correct GAP-1-closing statement is SPT, not W1

The bound $\mathrm{mtp}\le\mathrm{primorial}(p^*)$, when it holds, is a consequence of a *different and stronger* property:

**Definition 2.3 (SPT — small-prime-on-every-minimal).** Say SPT holds for $\mathcal M_n$ if every $M\in\mathcal M_n$ satisfies $\min M\le p^*$ (equivalently $M\cap\{p:p\le p^*\}\neq\emptyset$).

**Proposition 2.4 (SPT $\Rightarrow$ GAP-1).** If SPT holds for $\mathcal M_n$, then
$$\mathrm{mtp}(\mathcal M_n)\le\prod_{p\le p^*}p=\mathrm{primorial}(p^*).$$

*Proof.* Under SPT the set $S:=P_{\mathrm{ess},n}\cap\{p:p\le p^*\}$ meets every $M\in\mathcal M_n$, i.e. $S$ is a transversal of $\mathcal M_n$. Hence $S$ is among the transversals over which the minimum defining $\mathrm{mtp}$ is taken, so
$$\mathrm{mtp}(\mathcal M_n)\le\prod_{p\in S}p\le\prod_{p\le p^*}p=\mathrm{primorial}(p^*).\quad\square$$
The bound is in terms of $p^*=\min P(a_1)$ alone, hence $G(a_1)=\mathrm{primorial}(\min P(a_1))$.

**Remark 2.5 (SPT $\not\Rightarrow$ W1, W1 $\not\Rightarrow$ SPT — independence).** The two conjectures are logically independent. SPT $\not\Rightarrow$ W1: with $p^*=5$, a min-product witness $T^*=\{7\}$ (single prime $7\le\mathrm{primorial}(5)=30$) contains no prime $\le p^*$, yet SPT can still hold (the small primes form *a* transversal, not necessarily the min-product one). W1 $\not\Rightarrow$ SPT: the witness carrying a small prime says nothing about whether every *minimal* carries one. So W1 is neither necessary nor sufficient for GAP-1; only SPT (or any statement exhibiting a bounded-product transversal) closes GAP-1. The empirical coincidence "both hold with 0 violations" reflects the underlying greedy dynamics, not a logical implication.

#### 2.3 SPT is itself an open conjecture (the hard half W2)

The smooth-analytic explorer established (opening 4) the equivalence
$$\text{SPT for all $n$}\;\Longleftrightarrow\;\text{"every promotion's $a_{n+1}$ carries a prime $\le p^*$"},$$
because every entering minimal is $P(a_{n+1})$ at a promotion step, and $P(a_1)$ itself already satisfies the small-prime property. The explorer then split the promotions into:
- **Equality-promotions (170/344):** $a_{n+1}$ equals the mtp-multiple, so $T^*\subseteq P(a_{n+1})$; IF W1 holds, $a_{n+1}$ inherits a small prime for free. (Caveat per the explorer: $T^*$ is a transversal, not a member of $\mathcal M_n$, so $P(a_{n+1})\supseteq T^*$ does *not* make $P(a_{n+1})$ dominated — the "strict-beat linchpin" of earlier rounds is refuted; both cases occur.)
- **Strict-beat promotions (174/344):** $a_{n+1}$ lies strictly below the mtp-multiple; the small-prime property of $a_{n+1}$ is then a genuine **short-interval smooth/rough-number density** statement (W2): "the smallest valid integer in $(a_n,\text{mtp-multiple})$ carries a prime $\le p^*$."

W2 is an analytic-number-theory step with **no entry in `knowledge_base.md`** (no Dickman/de Bruijn, no Brun sieve). Standard Dickman bounds are *asymptotic* ($x\to\infty$), whereas the saturated regime keeps $a_n=O(a_1)$ (bounded $x$, where asymptotic density is meaningless). No proof of W2 exists this round; the explorer explicitly records it as a 0-violation CONJECTURE.

**Computational verification (this round, 41 saturated seeds, script `/tmp/round-129/mtp_bound_check.py`).** We checked, at every computable step ($|P_{\mathrm{ess},n}|\le18$) of each of 41 saturated seeds $a_1\in\{15,35,105,165,385,429,1001,2145,4199,7429,12673,175,187,221,323,899,1147,1517,1763,2021,2461,667,1189,1207,1387,1591,1739,2501,2773,3059,3239,3713,4331,5293,6499,7387,8633,15341,5183,6161,10403\}$:
- $\mathrm{mtp}(\mathcal M_n)\le\mathrm{primorial}(p^*)$ — **0 violations**;
- SPT (every $M\in\mathcal M_n$ has a prime $\le p^*$) — **0 violations**;
- W1 (witness $T^*$ contains a prime $\le p^*$) — **0 violations**.

The data is consistent with SPT and with the bound, but a numeric check is not a proof; the strict-beat density step (W2) remains unproven.

**Status of GAP-1:** **open.** The dispatch's W1-route is refuted as a GAP-1-closer (Proposition 2.2). The correct closing statement is SPT (Proposition 2.4), which is a 0-violation conjecture whose hard half (W2, strict-beat smooth-density) is unproven and uses machinery absent from `knowledge_base.md`. If GAP-1 fails, γ dies (mtp unbounded $\Rightarrow$ gaps unbounded $\Rightarrow$ no finite-state reduction).

### 3. GAP-3: do bounded gaps force $\mathcal M$ finite? (OPEN — verdict on the free-rider route)

**Conjecture 3.1 (GAP-3).** If $a_{n+1}-a_n\le G$ for every $n\ge N_0$, then $\mathcal M=\min\{P(a_i):i\ge1\}$ is finite.

#### 3.1 The unique-connector obstruction (recorded, stands)

A new minimal $M'=P(a_{n+1})$ is introduced (admissibility) as a transversal of $\mathcal M_n$ containing no member of $\mathcal M_n$ as a subset. The obstruction: $M'$ may contain a *large* prime $q>G$. Indeed $q\mid a_{n+1}$ and $q>G\ge a_{n+1}-a_n$ imply $a_n\in(a_{n+1}-G,a_{n+1})\subseteq(a_{n+1}-q,a_{n+1})$, strictly between consecutive multiples of $q$; hence $q\nmid a_n$, i.e. $q$ is "fresh" at step $n+1$. A large fresh prime $q>G$ can serve as the *unique connector* between $M'$ and some $M_0\in\mathcal M_n$ with $M'\cap M_0=\{q\}$, the many small-gap terms between introducing events all being hit by $M'\setminus\{q\}$ — perfectly consistent with gaps $\le G$. This invalidates any "only primes $\le G$ connect" claim by direct analogy with `aimo-0415` (whose pigeonhole is over a *fixed* small-prime set in a *finite* product, not an adaptive family).

#### 3.2 Verdict: the free-rider-eviction route does NOT refute the obstruction

The structural-reframing explorer (round 129, `/tmp/round-129/math-explorer-structural-reframing.md`) reports, on 14 saturated seeds, 0 violations of: "every large entering prime $q>\max P(a_1)$ entering a minimal enters as $\{2,q,\ldots\}$ and is evicted when a $\{2,p\}$ crash ($p\in P(a_1)\cup\{\text{small}\}$) refines it; large primes never persist." The dispatch asks whether this *refutes* the unique-connector obstruction, unblocking GAP-3. **Verdict: no, for two independent reasons.**

**(i) The eviction needs the crash mechanism — a stronger hypothesis than "gaps $\le G$."** GAP-3 is a statement *under the sole hypothesis that gaps are bounded*. The free-rider eviction is not a consequence of bounded gaps; it is a consequence of the **crash-inevitability** mechanism (`pstar-core-straggler` Lemma C: with $2$ common to the core and $p$ in the straggler, $\{2,p\}$ is a transversal $\Rightarrow$ $2p$-multiples valid within the mtp-window $\Rightarrow$ the greedy's smallest-first pick is the smooth $2^k\cdot p$, which crashes the $\{2,q,\ldots\}$ minimals). That mechanism requires (a) $2$ to be common to the core, (b) a straggler prime $p\in P(a_1)\setminus\mathrm{Cov}$, (c) a smooth-number crash to actually arrive — none of which follow from "gaps $\le G$" alone. Hence, *within γ's logical framing* (which assumes only bounded gaps), the eviction does not apply, and the unique-connector obstruction stands. (If one grants the full crash machinery, one proves $\mathcal M$ finite *directly* — `pstar-core-straggler`'s route — and γ's "gaps $\le G\Rightarrow\mathcal M$ finite" detour becomes unnecessary. The crash route does not pass through GAP-3 at all.)

**(ii) The strong free-rider universality is FALSE.** The blanket claim "every entering prime is a transient free-rider" is refuted by $a_1=15=3\cdot5$: $a_2=18=2\cdot3^2$ (entering prime $2$), $a_3=20=2^2\cdot5$, and the final family is the triangle $\mathcal M=\{\{3,5\},\{2,3\},\{2,5\}\}$ — the entering prime $2$ *persists as essential* (it lies in two of the three final minimals). So the eviction claim must be narrowed to "large primes $q>\max P(a_1)$ are evicted," and even this narrowed form is a 0-violation *conjecture* (14 seeds), not a proof, and it depends (per (i)) on the crash mechanism. The small entering primes (notably $2$ itself, which enters for every odd $a_1$) are *not* evicted; they are exactly what make the saturated terminal family finite in the structural explorer's data.

**Combining (i)+(ii):** under γ's pure "gaps $\le G$" hypothesis, neither the eviction nor any other available mechanism rules out infinitely many large unique connectors. GAP-3 stands open.

#### 3.3 The `aimo-0678` lcm-reduction route is DEAD

The adapted second solution of `aimo-0678` (crux corpus; technique *bounded coordinate $\Rightarrow$ lcm-reduce $\Rightarrow$ finite-state $\Rightarrow$ periodic*) sets $L=\mathrm{lcm}(1,\ldots,G)$, uses $d_n\mid L$ and $r_n=a_n\bmod L$, and asks whether $d_n$ is determined by a finite state. The load-bearing step in `aimo-0678` is "$a_n\mid M$" (the bounded coordinate *divides* the reduction modulus, collapsing dependence on the unbounded coordinate). In P6 the bounded coordinate is the *gap* $d_n$, not a term value, and the greedy $d_n=\min\{j: P(a_n+j)\text{ transversal of }\mathcal M_n\}$ depends on $\mathcal M_n$ — whose prime universe $P_{\mathrm{ess},n}$ is unbounded in $n$ (entering free-rider primes $167,179,503,\ldots$ appear in minimals for $a_1=5005$, per the structural explorer). Hence there is no finite reduction modulus $L$ built from primes $\le G$ that captures transversality, and the finite-state collapse fails. (Round-3 finite-state lens confirmation: the state is infinite because entering primes are unbounded.) The route is dead.

**A subsidiary observation (does not close GAP-3).** If GAP-1 holds (mtp stabilizes at $G^*$ with permanent witness $T^*$), then for all large $n$ the multiple of $G^*$ above $a_n$ is valid, giving the sharper bound $d_n\le G^*-(a_n\bmod G^*)$ (when $G^*\nmid a_n$) and $d_n\le G^*$ otherwise — so most gaps are $<G^*$, and $a_n\bmod G^*$ partly governs $d_n$. This narrows the candidate window but does not eliminate the large-prime obstruction: validity of the small-$j$ candidates still depends on their (possibly large) prime factors. A genuine narrowing, not a proof.

**Status of GAP-3:** **open.** The unique-connector obstruction stands (§3.1); the free-rider-eviction route does not refute it under γ's hypothesis (§3.2); the `aimo-0678` finite-state route is dead (§3.3). The live path to $\mathcal M$ finite is `pstar-core-straggler`'s Cov-monovariant + crash-inevitability, which does not route through GAP-3. If GAP-3 fails, γ dies even if GAP-1 succeeds.

### 4. Conditional finish (imports δ)

**Theorem 4.1 (conditional on GAP-1 and GAP-3).** If Conjectures 2.1 and 3.1 both hold, then $\mathcal M$ is finite, and by the certified `post-stabilization-theorem` (δ) there exist $T=|V|>0$ and $L=\prod_{p\in\bigcup\mathcal M}p>0$ with
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge1.$$

*Proof.* GAP-1 gives $\mathrm{mtp}(\mathcal M_n)\le G$; by Lemma 1(a) the monotone integer $\mathrm{mtp}$ stabilizes at some $G^*\le G$ after finitely many steps, so by §2 a permanent transversal of product $G^*$ exists from some $n_0$ on, giving $a_{n+1}-a_n\le G^*$ for $n\ge n_0$. GAP-3 then forces $\mathcal M$ finite. The certified `post-stabilization-theorem` (composing `transversal-residue-characterization`, `universal-membership-no-transient`, `greedy-equals-cyclic-successor`, `cyclic-successor-single-cycle`) gives the displayed identity. ∎

(Equivalently: close GAP-1 via SPT (Proposition 2.4) and close $\mathcal M$-finiteness via the crash route (the `pstar-core-straggler` mechanism, which directly yields $\mathcal M$ finite without the GAP-3 detour), then apply `post-stabilization-theorem`.)

### 5. Summary of independence and field placement

γ's certified asset (the mtp monovariant) is imported across the field (α, β-retired, the smooth/pstar framings). This round's contribution is the honest crux verdict:

- **W1 does not bound the mtp product** (Proposition 2.2); the GAP-1 closer is SPT (Proposition 2.4), a separate stronger conjecture with an unproven analytic hard half (W2, absent from KB). The field should stop citing W1 as a GAP-1 closer.
- **GAP-3's unique-connector obstruction is not refuted by free-rider eviction** under γ's "gaps $\le G$" hypothesis (§3.2), because eviction needs the crash mechanism; the strong free-rider universality is FALSE ($a_1=15$).
- γ's GAP-3 (lcm-reduction finite-state route) is dead; the live route to $\mathcal M$ finite is `pstar-core-straggler`'s Cov-monovariant + crash-inevitability, which bypasses GAP-3 entirely.

γ thus remains the cleanest *carrier of the mtp monovariant* but is no longer a plausible standalone whole-problem solver: both its sub-gaps are open, GAP-1 reduces to the (unproven) SPT, and GAP-3 is superseded by pstar. Status **partial**, honestly.

---

## Promotable lemmas

*(None new this round. The reusable asset remains the certified `mtp-monovariant-and-gap-bound` (γ r2). This round's contribution is a negative/clarifying verdict (Proposition 2.2: W1 $\not\Rightarrow$ mtp bounded) and the SPT-vs-W1 distinction; Proposition 2.4 (SPT $\Rightarrow$ mtp $\le\mathrm{primorial}(p^*)$) is a one-line conditional whose hypothesis is an unproven conjecture, so it is not certified as a standalone lemma.)*
