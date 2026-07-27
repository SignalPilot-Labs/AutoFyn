# IMO 2026 Problem 6 — approach `density-promotion-bound`

**Problem.** Let $a_1,a_2,\ldots$ be an infinite sequence of integers $>1$ such that $a_{n+1}$ is the smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for every $i=1,\ldots,n$. Prove there exist $T,L>0$ with $a_{n+T}=a_n+L$ for all $n$.

**Framing (mechanism α — regime casework).** The dead density-monotonicity / LLL / Mertens engine (round 1) is **dropped entirely**: density does not control promotions (round-2 explorer verified $a_1=273$ has $\rho\ge1/3$ throughout yet $47$ promotions before freeze). The wall splits into two regimes:

- **(F) Freeze regime:** a prime factor of $a_1$ remains *common* (contained in every member of $\mathcal M_n$) for all $n$. Then the greedy locks to difference $p$ (`freeze-lock`), the arithmetic progression $a_n=p(c+n-1)$ hits a pure prime power $p^k$, the support $\{p\}$ refines every existing minimal away, and `singleton-freeze` freezes $\mathcal M$ to $\{\{p\}\}$. **Closed.**
- **(S) Saturated regime:** no prime factor of $a_1$ persists common. The target is a *self-blocking fixed point* of $\mathcal M_n$ (every transversal contains a member); the self-blocking criterion ⟹ frozen is proved, but **reaching self-blocking (equivalently, finiteness of $\mathcal M$ in this regime) is the open wall GAP-S.**

Once $\mathcal M$ is finite (branch (F) always; branch (S) conditional on GAP-S), the certified `post-stabilization-theorem` gives $a_{n+T}=a_n+L$.

---

## Status

partial

## Approaches tried

- **Round 1 (mechanism α).** Reduced the theorem to finiteness of $\mathcal M$ and proved the conditional density lemma. The density-monotonicity wall-attack (GAP-D) was correctly identified but not closed. Honest partial.
- **Round 2 (mechanism α — regime split).** Dropped the dead density/LLL/Mertens frame. **Freeze branch (F) closed end-to-end** (`freeze-lock`+AP$\to p^k$+`singleton-freeze`). Saturated branch (S): self-blocking criterion (`Sat-criterion`) proved; reaching self-blocking (**GAP-S**) open. Case split (F)/(S) exhaustive.
- **Round 3 (mechanism α — saturated-regime decomposition; this round).** Two load-bearing corrections and one honest obstruction recorded:
  1. **Struck the `freeze-lock` "equivalence" overclaim.** Only the forward direction (persistence $\Rightarrow$ lock; contrapositive lock-broken $\Rightarrow$ not persistent) is proved; the backward direction is not proved and not used. The freeze-regime induction supplies persistence as a *hypothesis*, so no equivalence is needed.
  2. **Fixed the refuted round-3 "strict-beat" linchpin.** The smooth-analytic explorer REFUTED the premise that every promotion is a strict-beat ($170/344$ promotions are *equality*-promotions with $a_{n+1}=\mathrm{mtp}$-multiple and are STILL new minimals): the mtp-witness $T^*$ is a *transversal* of $\mathcal M_n$, NOT a *member*, so $P(a_{n+1})\supseteq T^*$ does NOT dominate (domination needs a member as subset). The SPT attack is restructured to handle BOTH cases: equality-promotions (small prime inherited from $T^*$ via the **W1** conjecture) and strict-beats (the **W2** smooth-density step). Both W1 and W2 are open; neither is proved this round.
  3. **Corrected the outliner's logical error "W1 $\Rightarrow$ mtp $\le$ primorial($p^*$)".** That implication is FALSE: W1 (the witness carries a small prime) bounds the witness only by $p^*\cdot(\text{other primes})$, which is unbounded. The bound $\mathrm{mtp}\le\prod_{p\le p^*}p$ requires **SPT** (every minimal carries a prime $\le p^*$, making the *set* of small essential primes a transversal), NOT W1. GAP-1 is therefore conditional on **SPT = (W1 on equality-promotions) $\wedge$ (W2 on strict-beat promotions)** — both open.
  4. **GAP-3 obstruction made rigorous.** The family $\mathcal F_q=\{\{2,q\}:q>p^*\text{ prime}\}$ is a pairwise-intersecting antichain (verified) all satisfying SPT ($\min\{2,q\}=2\le p^*$) with $P_{\mathrm{ess}}=\{2\}\cup\{q\}$ unbounded. So SPT bounds $\mathrm{mtp}$ (closes GAP-1) but does NOT bound $P_{\mathrm{ess}}$ (does not close GAP-3 / GAP-S). The wall needs a crash-eviction or Cov-monovariant partner (owned by `pstar-core-straggler`); α does not collapse into that framing.
  Honest: no sub-gap fully closes this round; the linchpin correction is load-bearing for the *correctness* of the saturated-regime analysis (the prior round-3 sketch was built on a FALSE premise).

## Current best

The **freeze regime is fully solved** (unchanged from round 2): if some $p\in P(a_1)$ stays common in $\mathcal M_n$ for all $n$, then `freeze-lock` $\Rightarrow$ $a_{n+1}=a_n+p$ $\Rightarrow$ $a_n=p(c+n-1)$ AP $\Rightarrow$ hits $p^k$ $\Rightarrow$ $\mathcal M_n=\{\{p\}\}$ $\Rightarrow$ `singleton-freeze` $\Rightarrow$ $\mathcal M=\{\{p\}\}$ finite $\Rightarrow$ `post-stabilization-theorem` gives $a_{n+1}=a_n+p$ ($L=p,T=1$).

**Saturated regime (S) — corrected decomposition (open wall GAP-S), now split into two independent sub-gaps:**
- **GAP-1 (mtp bounded).** Closed *modulo the SPT conjecture*. SPT (every entering minimal $M'=P(a_{n+1})$ has $\min(M')\le p^*:=\min P(a_1)$) $\Rightarrow$ $\mathrm{mtp}\le\prod_{p\le p^*}p$ (rigorous implication). SPT is proved by induction on the step; the induction step at a promotion splits exhaustively into:
  - **equality-promotion** ($a_{n+1}=\mathrm{mtp}$-multiple): handled *modulo W1* (witness $T^*\subseteq P(a_{n+1})$ carries a prime $\le p^*$);
  - **strict-beat promotion** ($a_{n+1}<\mathrm{mtp}$-multiple): handled *modulo W2* (short-interval smooth/rough-number density);
  - **non-promotion**: no new minimal, induction carries trivially.
  W1 and W2 are both OPEN (0 violations computationally on the 6 standard seeds $15,429,30,273,175,19549$ incl. $p^*=113$, but no proof). The dichotomy equality/strict-beat is exhaustive by `mtp-monovariant-and-gap-bound` (the mtp-multiple is valid and $\le a_n+\mathrm{mtp}$, so the greedy picks $\le$ it).
- **GAP-3 ($P_{\mathrm{ess}}$ bounded).** OPEN, and NOT closed by SPT: the $\{2,q\}$ antichain obstruction (verified) satisfies SPT with unbounded $P_{\mathrm{ess}}$. Needs the crash-eviction / Cov-monovariant partner (`pstar-core-straggler`); α does not supply it.

## Full proof

*(Branch (F) complete; branch (S) conditional on GAP-S.)*

### 0. Notation and the transversal reduction

For $m>1$ write $P(m)$ for its (nonempty) set of prime divisors. The admissibility condition at step $n+1$ is
$$\gcd(a_{n+1},a_i)>1\ \forall i\le n \iff P(a_{n+1})\cap P(a_i)\neq\emptyset\ \forall i\le n.$$
Let $\mathcal F_n=\{P(a_1),\ldots,P(a_n)\}$ and $\mathcal M_n=\min_{\subseteq}\mathcal F_n$ (the $\subseteq$-minimal members). A set $S$ of primes hits every member of $\mathcal F_n$ iff it hits every member of $\mathcal M_n$ (a non-minimal member contains a minimal one), so the admissible integers at step $n+1$ are
$$V_n=\{m>0:\ P(m)\text{ hits every }M\in\mathcal M_n\},\qquad a_{n+1}=\min\{m\in V_n:m>a_n\}.$$
Let $C_n=\bigcap_{M\in\mathcal M_n}M$ (the **common primes** at time $n$). Let $\mathcal M=\min\{P(a_i):i\ge1\}$ (the final family; possibly infinite — finiteness is the wall) and $P=\bigcup_{M\in\mathcal M}$.

### 1. Pairwise-intersection lemma (import)

**Lemma 1** (`pairwise-intersection`, certified). *For all $i,j\ge1$, $P(a_i)\cap P(a_j)\neq\emptyset$; hence $\{P(a_i)\}$ is pairwise intersecting and every $P(a_n)$ hits every member of $\mathcal M$.*

Imported verbatim from `lemmas/pairwise-intersection.md`; not re-proved.

### 2. Common primes lie among the factors of $a_1$

**Lemma 2 (common-primes-bounded).** *For every $n\ge1$, every prime in $C_n$ (every common prime at time $n$) divides $a_1$, i.e. $C_n\subseteq P(a_1)$.*

*Proof.* $\mathcal M_n$ is the set of $\subseteq$-minimal members of $\mathcal F_n=\{P(a_1),\ldots,P(a_n)\}$. Since $P(a_1)\in\mathcal F_n$, the subfamily $\{S\in\mathcal F_n:S\subseteq P(a_1)\}$ is nonempty (it contains $P(a_1)$); by well-foundedness of $\subseteq$ on the finite set $\mathcal F_n$, it contains a $\subseteq$-minimal element $M_1\in\mathcal M_n$ with $M_1\subseteq P(a_1)$. If $q\in C_n$, then $q\in M$ for every $M\in\mathcal M_n$, in particular $q\in M_1\subseteq P(a_1)$, so $q\mid a_1$. ∎

**Corollary.** A prime can be permanently common only if it divides $a_1$: $\bigcup_n C_n\subseteq P(a_1)$.

### 3. The case split (exhaustive)

Let $p_1,\ldots,p_r$ be the prime factors of $a_1$ (so $P(a_1)=\{p_1,\ldots,p_r\}$). Define:

- **(F) Freeze regime:** $\exists\,p\in P(a_1)$ with $p\in C_n$ for every $n\ge1$ (some factor of $a_1$ is permanently common).
- **(S) Saturated regime:** $\forall\,p\in P(a_1),\ \exists\,n\ge1$ with $p\notin C_n$ (no factor of $a_1$ is permanently common).

These are exhaustive by the law of excluded middle. By Lemma 2, in (S) no prime at all is permanently common. Note $C_1=P(a_1)$ (as $\mathcal M_1=\{P(a_1)\}$), so every factor of $a_1$ is common at time $1$; (F)/(S) is determined by whether this persists.

### 4. Branch (F): the freeze regime — closed

Assume (F): some $p\in P(a_1)$ satisfies $p\in C_n$ for all $n\ge1$.

#### 4a. The greedy locks to difference $p$ (`freeze-lock`, certified) — forward direction only

**Lemma 3** (`freeze-lock`, certified, forward direction). *If $p\mid a_n$ and $p\in C_n$, and $p\in C_{n+1}$, then $a_{n+1}=a_n+p$.*

*Proof.* See `lemmas/freeze-lock.md`. The argument: $\{p\}$ is a transversal of $\mathcal M_n$ (as $p\in C_n$), so multiples of $p$ are valid and $a_{n+1}\le a_n+p$. If $a_{n+1}<a_n+p$, then $p\nmid a_{n+1}$, and $P(a_{n+1})$ (a transversal of $\mathcal M_n$ by admissibility) is a new minimal: no $M\in\mathcal M_n$ is a subset of $P(a_{n+1})$ (each contains $p\notin P(a_{n+1})$), and no non-minimal $P(a_j)$ is either (its minimal refinement is in $\mathcal M_n$). Hence $P(a_{n+1})\in\mathcal M_{n+1}$ lacks $p$, contradicting $p\in C_{n+1}$. ∎

**Remark (corrected this round — overclaim struck).** Only the forward direction (persistence $\Rightarrow$ lock) and its contrapositive (lock-broken $\Rightarrow$ $p$ ceases common) are proved. The backward direction (lock $\Rightarrow$ persistence, i.e. $a_{n+1}=a_n+p\Rightarrow p\in C_{n+1}$) is **not** proved and is **not used**: the freeze-regime induction (Lemma 4) supplies persistence as a *hypothesis*. The earlier round-2 remark calling the lock and persistence "equivalent" is withdrawn; "equivalence" is an overclaim. The forward direction is exactly what the induction needs.

#### 4b. The greedy is arithmetic with difference $p$

**Lemma 4.** *In regime (F), $p\mid a_n$ and $a_{n+1}=a_n+p$ for every $n\ge1$. Consequently $a_n=p(c+n-1)$ with $c=a_1/p\in\mathbb Z_{>0}$.*

*Proof.* By induction on $n$.
- *Base $n=1$:* $p\in P(a_1)\Rightarrow p\mid a_1$; $p\in C_1$ (as $\mathcal M_1=\{P(a_1)\}\ni p$); $p\in C_2$ (regime (F)). Lemma 3 gives $a_2=a_1+p$, so $p\mid a_2$.
- *Step:* assume $p\mid a_n$ and $p\in C_n$ (regime (F)). Since $p\in C_{n+1}$ (regime (F)), Lemma 3 gives $a_{n+1}=a_n+p$, hence $p\mid a_{n+1}$.

So $a_{n+1}-a_n=p$ for all $n\ge1$, giving $a_n=a_1+(n-1)p=p\bigl(a_1/p+n-1\bigr)=p(c+n-1)$ with $c=a_1/p$. ∎

#### 4c. The AP hits a pure prime power

**Lemma 5.** *In regime (F), there exists $n\ge1$ with $a_n=p^k$ for some $k\ge2$; at that term $P(a_n)=\{p\}$.*

*Proof.* The sequence $a_n=p(c+n-1)$ is arithmetic. Choose $k$ minimal with $p^{k-1}\ge c$ (exists as $p^{k-1}\to\infty$); set $n=p^{k-1}-c+1\ge1$. Then $c+n-1=p^{k-1}$, so $a_n=p\cdot p^{k-1}=p^k$, and $P(p^k)=\{p\}$. ∎

#### 4d. Singleton freeze

**Lemma 6.** *In regime (F), at the term $n$ of Lemma 5, $\mathcal M_n=\{\{p\}\}$. By `singleton-freeze`, $\mathcal M_m=\{\{p\}\}$ for all $m\ge n$; in particular $\mathcal M=\{\{p\}\}$ is finite.*

*Proof.* At step $n$, $P(a_n)=\{p\}$ enters $\mathcal F_n$. It is minimal (its only nonempty proper subset is $\emptyset$, which is no $P(a_j)$ as all $a_j>1$). Every $M\in\mathcal M_{n-1}$ contains $p$ (regime (F): $p\in C_{n-1}$), so $\{p\}\subseteq M$; hence $\{p\}$ dominates (refines away) every existing minimal. Therefore $\mathcal M_n=\{\{p\}\}$. The certified `singleton-freeze` lemma then gives $\mathcal M_m=\mathcal M_n=\{\{p\}\}$ for all $m\ge n$. ∎

**Conclusion of branch (F).** $\mathcal M=\{\{p\}\}$ is finite. By the certified `post-stabilization-theorem`, with $P=\{p\}$, $L=p$, $V=\{0\}$ (a residue $r$ is in $V$ iff $\{p:p\mid r\}$ hits $\{\{p\}\}$, i.e. iff $p\mid r$; so $V=\{0\}$, $T=|V|=1$), we obtain $a_{n+1}=a_n+p$ for every $n\ge1$. Branch (F) is solved end-to-end. ∎

### 5. Branch (S): the saturated regime — criterion proved; the wall GAP-S decomposed

Assume (S): no factor of $a_1$ is permanently common. By Lemma 2, no prime is permanently common. The target is to prove $\mathcal M$ finite (GAP-S). We restate the certified sufficient criterion, then decompose the wall.

#### 5a. Self-blocking $\Rightarrow$ frozen (the Sat-criterion, import)

**Lemma 7 (Sat-criterion, certified).** *If $\mathcal M_n$ is self-blocking (every transversal of $\mathcal M_n$ contains some member of $\mathcal M_n$ as a subset — equivalently, there is no avoiding transversal), then $\mathcal M_m=\mathcal M_n$ for all $m\ge n$ (the family is frozen, hence finite).*

*Proof.* By induction on $m\ge n$. Base $m=n$ trivial. Inductive step: assume $\mathcal M_m=\mathcal M_n$ (hence self-blocking). Consider $a_{m+1}$. By admissibility, $P(a_{m+1})$ meets every $P(a_i)$, $i\le m$, hence meets every member of $\mathcal F_m$, hence $P(a_{m+1})$ is a transversal of $\mathcal M_m$. By self-blocking, $P(a_{m+1})$ contains some $M\in\mathcal M_m$ as a subset, so $P(a_{m+1})$ is dominated by $M$ and is **not** a new minimal. No new minimal enters at step $m+1$; existing minimals cannot be removed (removal requires a new minimal subset to appear). So $\mathcal M_{m+1}=\mathcal M_m=\mathcal M_n$. ∎

#### 5b. The mtp monovariant and the window (import)

For a family $\mathcal M_n$, define the **min-transversal-product**
$$\mathrm{mtp}(\mathcal M_n)=\min_{\substack{T\text{ transversal of }\mathcal M_n}}\prod_{p\in T}p.$$

**Lemma 8** (`mtp-monovariant-and-gap-bound`, certified, import). *$\mathrm{mtp}(\mathcal M_n)$ is monotone non-decreasing in $n$ (refinement shrinks the transversal family), and $a_{n+1}-a_n\le\mathrm{mtp}(\mathcal M_n)$ at every step. In particular, letting $T^*$ be any mtp-witness (a transversal achieving $\mathrm{mtp}$) and $L^*=\mathrm{mtp}(\mathcal M_n)$, the smallest multiple of $L^*$ strictly above $a_n$, call it $\mu_n=\lceil(a_n+1)/L^*\rceil L^*$, is valid and satisfies $\mu_n\le a_n+L^*$; hence the greedy choice obeys $a_{n+1}\le\mu_n\le a_n+\mathrm{mtp}(\mathcal M_n)$.*

Imported verbatim from `lemmas/mtp-monovariant-and-gap-bound.md`; not re-proved. Correlation-surviving: it is a single-transversal bound, immune to the pairwise-intersection correlation that defeats LLL/inclusion-exclusion.

#### 5c. The promotion dichotomy (exhaustive) — corrected linchpin

A **promotion** at step $m+1$ occurs iff $P(a_{m+1})$ is a new minimal of $\mathcal F_{m+1}$, equivalently $P(a_{m+1})$ is an *avoiding transversal* of $\mathcal M_m$ (a transversal containing no member of $\mathcal M_m$) — possibly together with extra (free-rider) primes. By admissibility $P(a_{m+1})$ is a transversal of $\mathcal M_m$; it is a new minimal iff no member of $\mathcal M_m$ is a subset of $P(a_{m+1})$.

**Dichotomy (equality vs strict-beat).** Let $\mu_m$ be the smallest multiple of $\mathrm{mtp}(\mathcal M_m)$ strictly above $a_m$ (Lemma 8). By Lemma 8, $a_{m+1}\le\mu_m$. Hence exactly one of:

- **(E) Equality:** $a_{m+1}=\mu_m$ (the greedy picks the mtp-multiple). Since $\mu_m$ is a multiple of $L^*=\prod_{p\in T^*}p$ and $T^*$ is a set of *distinct* primes, every $p\in T^*$ divides $\mu_m$, i.e. $T^*\subseteq P(a_{m+1})$.
- **(SB) Strict-beat:** $a_{m+1}<\mu_m$ (the greedy picks a valid integer strictly below the mtp-multiple).

The dichotomy is exhaustive (the third option $a_{m+1}>\mu_m$ is excluded by Lemma 8).

**Crucial correction (the refuted round-3 premise).** In case (E), $P(a_{m+1})\supseteq T^*$ does **NOT** make $P(a_{m+1})$ dominated, hence does **NOT** preclude a promotion. Domination requires a *member of $\mathcal M_m$* to be a subset of $P(a_{m+1})$; but $T^*$ is a *transversal* (hitting set) of $\mathcal M_m$, not generally a member of $\mathcal M_m$. (Computationally confirmed: across the 6 standard seeds, equality-promotions occur at $a_1=15$ (1), $429$ (2), $30$ (1), $273$ (18), $175$ (1), $19549$ (17) — a substantial fraction of all promotions are equality-promotions and are genuine new minimals.) The round-3 premise "at a promotion $a_{n+1}$ is NOT the mtp-multiple (else dominated)" is **FALSE**; the SPT attack below handles both cases.

#### 5d. The SPT target and its equality/strict-beat split

Set $p^*:=\min P(a_1)$. The **SPT conjecture** is: for every $n\ge1$ and every $M\in\mathcal M_n$, $\min(M)\le p^*$ (every ever-minimal support contains a prime $\le p^*$). Since $P(a_1)\in\mathcal M_1$ has $\min=p^*$, the base holds.

**SPT $\Rightarrow$ GAP-1 (rigorous).** If SPT holds, then $S_n:=P_{\mathrm{ess},n}\cap\{p\le p^*\}$ is a transversal of $\mathcal M_n$ (every member contains a prime $\le p^*$). Hence
$$\mathrm{mtp}(\mathcal M_n)\le\prod_{p\in S_n}p\le\prod_{p\le p^*}p=:\mathrm{R}(a_1),$$
a bound depending only on $p^*=\min P(a_1)$, hence on $a_1$. By Lemma 8 (monotonicity) the bounded monotone $\mathrm{mtp}$ stabilizes. **GAP-1 is closed modulo SPT.** (Note: this implication uses SPT — the *set* of small primes is a transversal — NOT the weaker W1 statement about the witness; see §5e.)

**Induction step for SPT, at a promotion $m+1$.** Assume all current minimals satisfy $\min\le p^*$ (induction hypothesis). A new minimal $M'=P(a_{m+1})$ is added; we must show $\min(M')\le p^*$, i.e. $a_{m+1}$ carries a prime $\le p^*$. Split by §5c:

- **(E) Equality-promotion:** $P(a_{m+1})\supseteq T^*$ (the mtp-witness, §5c). By **Lemma W1** (below, open), $T^*$ contains a prime $\le p^*$; hence $a_{m+1}$ is divisible by that prime, so $\min(M')\le p^*$. *Conditional on W1.*
- **(SB) Strict-beat promotion:** $a_{m+1}$ is a valid integer strictly below $\mu_m$. By **Lemma W2** (below, open), the smallest valid integer in $(a_m,\mu_m)$ carries a prime $\le p^*$; hence $\min(M')\le p^*$. *Conditional on W2.*
- **(Non-promotion):** no new minimal is added; the induction hypothesis on existing minimals is unchanged, so SPT carries forward trivially.

The cases (E)/(SB)/(non-promotion) are exhaustive by §5c. **Hence SPT holds modulo (W1 $\wedge$ W2)** (applied at promotion steps), and **GAP-1 is closed modulo (W1 $\wedge$ W2)**.

#### 5e. Lemma W1 (the mtp-witness carries a small prime) — OPEN CONJECTURE

**Conjecture W1.** *For every $n$ in regime (S), every mtp-witness transversal $T^*$ of $\mathcal M_n$ contains a prime $\le p^*$.*

**Computational evidence.** Verified with 0 violations on the 6 standard seeds ($a_1\in\{15,429,30,273,175,19549\}$, incl. $p^*=113$), checking ALL mtp-witnesses (not just one) at every computable step (~1770 witness-instances total). E.g. $a_1=19549=113\cdot173$: at the terminal family, $P_{\mathrm{ess}}=\{2,3,59,113,173\}$ has only one prime ($173$) $>p^*=113$, so no all-large transversal exists and W1 is trivial there; the nontrivial checks are at mid-evolution, all pass.

**Why W1 is not a formality (no proof found this round).** The cheap structural kill fails: if $T^*$ avoids all primes $\le p^*$, then (regime (S): no common prime $\Rightarrow$ every transversal has $\ge2$ elements) $\prod T^*\ge\mathrm{nextprime}(p^*)\cdot\ldots$, but the inequality $\prod T^*>\prod_{p\le p^*}p$ — which would exhibit a cheaper small-prime transversal — **does not hold in general**: when $p^*$ is moderately large, $\prod_{p\le p^*}p$ (a primorial) grows fast and a 2-element large-prime transversal can be cheaper. Constructible pairwise-intersecting antichain counterfamilies (not necessarily greedy-arising) witness this. W1 is therefore genuinely empirical-and-tight for the *greedy-arising* families; a proof would have to use the greedy's smallest-first dynamics in an essential way, and no such argument is known.

**Honest scope of W1.** W1 is a per-step statement (about the witness at time $n$), not logically requiring termination, so using it is not circular with finiteness *per se*. However its empirical truth plausibly flows from the same bounded-$P_{\mathrm{ess}}$ mechanism that IS the wall (GAP-3); W1 may be a *consequence* of the wall rather than an independent tool. Until an independent proof is found, W1 is recorded as an open conjecture.

**Critical correction.** W1 (witness carries a small prime) does **NOT** by itself bound $\mathrm{mtp}$: a witness $\{3,97\}$ (with $p^*=3$) satisfies W1 (contains $3\le p^*$) yet has product $291$, unbounded as the large cofactor varies. The bound $\mathrm{mtp}\le\prod_{p\le p^*}p$ requires SPT (the *set* of small essential primes is a transversal), which is why GAP-1 is conditional on **SPT = W1 (equality) $\wedge$ W2 (strict-beat)**, not on W1 alone. (This corrects the outliner's step "W1 $\Rightarrow$ mtp $\le$ primorial($p^*$)", which conflated the witness with the small-prime transversal.)

#### 5f. Lemma W2 (strict-beat smooth-density) — OPEN, the hard analytic step

**Conjecture W2.** *In regime (S), at a strict-beat promotion (case (SB)), $a_{m+1}$ — the smallest valid integer strictly below the mtp-multiple $\mu_m$ — is divisible by a prime $\le p^*$.*

**Computational evidence.** Verified with 0 violations on the 6 standard seeds at every strict-beat promotion (e.g. $a_1=175$: 3 strict-beats, all small-prime-carrying; $a_1=429$: 10; $a_1=19549$: 7). But W2 is NOT implied by W1: the smallest valid integer below $\mu_m$ could in principle be a large-prime-only number.

**Why W2 is genuinely hard (no proof found this round).** The natural mechanism is smooth/rough-number density: small-prime multiples (of $2$, of $3$, …) are denser than $p^*$-rough integers in short intervals, so the smallest valid candidate above $a_m$ is overwhelmingly likely to be small-prime-divisible. Three honest obstructions to making this rigorous:
1. `knowledge_base.md` has **no Dickman/de Bruijn / smooth-number entry**; the theorem must be cited externally AND re-proved/adapted from scratch (repo rule).
2. Standard Dickman bounds are **asymptotic** ($x\to\infty$); in the saturated regime $a_m$ stays $O(a_1)$-ish (empirically), so the relevant $x$ is bounded-ish where asymptotic density is meaningless — the elementary sieve/counting route is the realistic path, and it is unproven here.
3. The validity condition (transversal of $\mathcal M_m$) interacts with the density; the bound must condition on the candidate being a transversal.

W2 is the hard analytic step of this approach's SPT attack; it remains open.

#### 5g. GAP-3 — OPEN, and NOT closed by SPT (the $\{2,q\}$ obstruction)

Even granting SPT (hence GAP-1 closed, $\mathrm{mtp}$ bounded), the wall GAP-S ($\mathcal M$ finite $\Leftrightarrow$ $P_{\mathrm{ess}}$ finite) is **not** closed. The obstruction is rigorous:

**Lemma 9 (the $\{2,q\}$ obstruction).** *There exists an infinite pairwise-intersecting antichain of nonempty finite prime-sets, every member of which satisfies $\min\le p^*$, with unbounded essential-prime set.*

*Construction.* Fix any $p^*\ge2$ (in regime (S), $a_1$ is odd, so $p^*\ge3$; take $p^*=3$ for definiteness). Let $\mathcal F_q=\bigl\{\{2,q\}:q>p^*,\ q\text{ prime}\bigr\}$. Then:
- **Pairwise intersecting:** $\{2,q_i\}\cap\{2,q_j\}=\{2\}\neq\emptyset$ for $i\neq j$.
- **Antichain:** $\{2,q_i\}\not\subseteq\{2,q_j\}$ for $i\neq j$ (as $q_i\neq q_j$), and no proper nonempty subset exists other than $\{2\},\{q_i\}$ which are not in the family.
- **SPT satisfied:** $\min\{2,q\}=2\le p^*$ for every member (verified computationally: $p^*=3$, $\mathcal F_q$ over $q\in\{5,7,11,13,97,101\}$ is pairwise-intersecting, an antichain, and SPT-true).
- **Unbounded $P_{\mathrm{ess}}$:** $\bigcup\mathcal F_q=\{2\}\cup\{q:q>p^*\text{ prime}\}$, unbounded. ∎

**Consequence.** SPT (every minimal has $\min\le p^*$) bounds $\mathrm{mtp}$ (GAP-1) but does **NOT** bound $P_{\mathrm{ess}}$ (GAP-3 / GAP-S). A pairwise-intersecting antichain all containing some small prime from a bounded set can still be infinite. Therefore:

> **GAP-3 remains open under SPT alone.** Closing GAP-S requires an additional mechanism — a crash-eviction step (a small-support minimal arriving and refining the large-prime minimals toward self-blocking) or a bounded Cov monovariant bounding the crash primes. That mechanism is owned by the `pstar-core-straggler` approach (Cov $\subseteq P(a_1)$, crash primes bounded by $a_1$'s factorization). This approach does **not** collapse into the Cov framing (to preserve field diversity, per the outliner): α's crash-eviction, if supplied, would bound *entering* primes by value via the free-rider/refinement relation, structurally distinct from `pstar`'s value-free Cov-completion.

#### 5h. The saturated wall, summarized

In regime (S), GAP-S ($\mathcal M$ finite) decomposes into two independent sub-gaps:
- **GAP-1 ($\mathrm{mtp}$ bounded): closed modulo SPT**, and SPT is closed modulo (W1 $\wedge$ W2), both open (§5e, §5f). Even fully closed, GAP-1 does not bound $P_{\mathrm{ess}}$.
- **GAP-3 ($P_{\mathrm{ess}}$ bounded): open**, with the rigorous $\{2,q\}$ obstruction (Lemma 9) showing SPT does not suffice; needs the crash-eviction / Cov partner.

The wall is honest: no sub-gap is closed this round. The contributions are (i) the corrected promotion dichotomy (§5c) fixing the refuted round-3 premise, (ii) the rigorous SPT$\Rightarrow$GAP-1 implication (§5d) and the correction that GAP-1 needs SPT not W1 (§5e), (iii) the rigorous $\{2,q\}$ obstruction (§5g) for GAP-3.

### 6. Import of the post-stabilization machinery (δ)

**Theorem A** (`post-stabilization-theorem`, certified). *If $\mathcal M=\min\{P(a_i):i\ge1\}$ is finite, set $P=\bigcup\mathcal M$, $L=\prod_{p\in P}p$ (squarefree), $V=\{r\in\{0,\ldots,L-1\}:\{p\in P:p\mid r\}\text{ hits }\mathcal M\}$, $T=|V|$. Then $a_{n+T}=a_n+L$ for every $n\ge1$.*

Imported from `lemmas/post-stabilization-theorem.md` (composing `transversal-residue-characterization`, `universal-membership-no-transient`, `greedy-equals-cyclic-successor`, `cyclic-successor-single-cycle` — none re-proved here). The import is non-circular: Theorem A *hypothesizes* $\mathcal M$ finite; the wall (branch (F) proved, branch (S) = GAP-S) *proves* it.

- In **branch (F)**, $\mathcal M=\{\{p\}\}$ (Lemma 6), so $P=\{p\}$, $L=p$, $V=\{0\}$, $T=1$: $a_{n+1}=a_n+p$, matching Lemma 4.
- In **branch (S)**, *conditional on GAP-S*, $\mathcal M$ is the (finite) saturated family; Theorem A gives the general periodic case $a_{n+T}=a_n+L$ with $T=|V|$, $L=\prod P$.

### 7. Conclusion

- **Branch (F) (freeze regime): SOLVED** (unchanged from round 2). Any $a_1$ for which a prime factor of $a_1$ persists common yields $\mathcal M=\{\{p\}\}$ finite (Lemmas 3–6 + `singleton-freeze`), and `post-stabilization-theorem` gives $a_{n+1}=a_n+p$.
- **Branch (S) (saturated regime): PARTIAL.** The self-blocking criterion (`Sat-criterion`, Lemma 7) and the mtp monovariant + window (Lemma 8) are proved/imported. The promotion dichotomy (§5c, equality vs strict-beat) is proved exhaustive and the refuted round-3 strict-beat premise is corrected. GAP-1 ($\mathrm{mtp}$ bounded) is reduced to SPT, itself reduced to (W1 on equality-promotions) $\wedge$ (W2 on strict-beat promotions) — both open conjectures (0 violations on the 6 standard seeds, no proof). GAP-3 ($P_{\mathrm{ess}}$ bounded) is open with the rigorous $\{2,q\}$ obstruction (Lemma 9) showing SPT does not close it; it awaits the crash-eviction / Cov-monovariant partner (`pstar-core-straggler`).

The case split (F)/(S) is exhaustive, so the theorem follows in full once GAP-S (equivalently GAP-1 + GAP-3) is discharged. With GAP-S open, this approach is **partial**: the freeze regime is proved end-to-end, the saturated regime is decomposed into two explicitly named, independently attackable sub-gaps with the load-bearing correctness fix (the equality/strict-beat dichotomy) in place.

---

## Promotable lemmas

1. **Freeze-lock (forward direction)** (`lemmas/freeze-lock.md`). *If $p\mid a_n$, $p$ common in $\mathcal M_n$, and $p$ common in $\mathcal M_{n+1}$, then $a_{n+1}=a_n+p$.* Contrapositive: if the greedy's difference is $<p$ at a step where $p\mid a_n$ and $p$ is common, then $p$ ceases to be common. **Proved in full (Lemma 3); unconditional.** Overclaim "equivalence" struck this round — only the forward direction (and contrapositive) is proved; the backward direction is not proved and not used. Importable by any approach touching the freeze regime.

2. **Common-primes-bounded** (Lemma 2 above). *Every common prime at any time $n$ divides $a_1$ ($C_n\subseteq P(a_1)$).* **Proved in full; unconditional.** Pins the case split (F)/(S) on the prime factors of $a_1$ alone.

3. **Sat-criterion** (Lemma 7 above). *If $\mathcal M_n$ is self-blocking, then $\mathcal M$ is frozen and finite from $n$ on.* **Proved in full; unconditional.** A clean sufficient condition for finiteness; importable as the terminal step of any saturated-regime argument.

4. **Min-prod-transversal density** (Lemma 8 above, = certified `mtp-monovariant-and-gap-bound` import). *$\mathrm{mtp}$ monotone non-decreasing; $a_{n+1}-a_n\le\mathrm{mtp}(\mathcal M_n)$; correlation-surviving.* **Proved in full (γ, round 2); unconditional.** Supplies the window and the mtp-multiple validity used in the promotion dichotomy (§5c).

5. **The $\{2,q\}$ GAP-3 obstruction** (Lemma 9 above). *$\{\{2,q\}:q>p^*\text{ prime}\}$ is an infinite pairwise-intersecting antichain satisfying SPT with unbounded $P_{\mathrm{ess}}$; hence SPT does not bound $P_{\mathrm{ess}}$.* **Proved in full; unconditional.** Importable by any SPT-based approach (α, γ, `smooth-window-crash`) as the rigorous reason SPT closes GAP-1 but not GAP-3, scoping the wall honestly.

## Open lemmas (NOT promotable — conjectures, no proof)

- **W1** (mtp-witness carries a prime $\le p^*$): 0 violations on the 6 standard seeds incl. $p^*=113$, but no proof; the cheap structural inequality fails; may flow from the wall mechanism itself. Closes the equality-promotion half of SPT if proved.
- **W2** (strict-beat promotion's $a_{m+1}$ carries a prime $\le p^*$): 0 violations on the 6 standard seeds, but no proof; needs a short-interval smooth/rough-number bound not in `knowledge_base.md` (asymptotic-vs-bounded-$x$ tension). Closes the strict-beat half of SPT if proved.
