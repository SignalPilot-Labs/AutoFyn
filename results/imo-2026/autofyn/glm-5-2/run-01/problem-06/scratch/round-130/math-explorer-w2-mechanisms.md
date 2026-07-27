# Math-explorer (W2 attack-mechanism diversity) — round 130

## imo-2026-06 — scouting W2 mechanisms (strict-beat short-interval step)

**Recall W2.** In the saturated regime, at a strict-beat promotion, $a_{n+1}$ is the smallest valid integer in $(a_n, \mu_n)$ where $\mu_n$ is the mtp-multiple. W2 conjectures: $a_{n+1}$ is divisible by some prime $\le p^*:=\min P(a_1)$. (The equality-beat half is W1.) Together W1 ∧ W2 = SPT, which closes GAP-1 (mtp ≤ primorial(p*)). All probes below are CONJECTURE (evidence, not proof) unless labeled "certified."

Probes run on seeds $a_1\in\{15,35,77,91,105,143,175,195,323,385,899,1147,1365,2145,4199,5005,1001,1155\}$, generating the greedy sequence to 60 terms, tracking $\mathcal M_n$, all transversals (full $2^{|P_{\rm ess}|}$ enumeration when $|P_{\rm ess}|\le 14$), the witness $T^*$, the mtp-multiple $\mu_n$, the strict-beat candidate, and — crucially — *which transversal's product $a_{n+1}$ is a multiple of* (the "winning transversal"). Scripts: `/tmp/round-130/w2_probe.py`, `w2_struct.py`, `smc_probe.py`, `race_probe.py`.

### Key empirical findings (all CONJECTURE, labeled)

**F1 (decisive, 18 seeds, 0 violations).** At every strict-beat promotion, $a_{n+1}$ is a multiple of some transversal $T''$ of $\mathcal M_n$ with $T''$ containing a prime $\le p^*$. The winning transversal is always a SMALL-product one: product $\in\{10,14,22,26,21,6,\ldots\}$, typically $2q$ or $3q$ for a small/entering prime $q$. The smallest transversal-product dividing $a_{n+1}$ ALWAYS contains 2 or 3 (both $\le p^*$ after the Entering-2 lemma). All-large-prime transversals (product $\ge$ nextprime$(p^*)^2$) NEVER win (`all_large_winners=[]` in every recorded strict-beat).

**F2 (refutes the "witness-AP" sub-route).** $a_{n+1}$ is NOT always divisible by a prime of the witness $T^*$. Counter: $a_1=175=5^2\!\cdot\!7$, step 3, $\mathcal M_n=\{\{2,3,5\},\{2,7,13\},\{5,7\}\}$, witness $T^*=\{2,5\}$ (mtp=10), $a_{n+1}=189=3^3\!\cdot\!7$, divisible by neither 2 nor 5. The winning transversal is $\{3,7\}$ (product 21), whose small prime 3 is an ENTERING prime outside $T^*$. So W2 is genuinely independent of W1 — confirming the dispatch framing.

**F3 (the Cov sufficient condition).** Whenever $\mathrm{Cov}(\mathcal M_n)\neq\emptyset$ (some $\{2,p\}$-crash has occurred, $p\in P(a_1)$ — certified `cov-monovariant`), the set $\{2,p\}$ is a TRANSVERSAL of $\mathcal M_n$ for every $p\in\mathrm{Cov}$: 2 hits the core (minimals containing 2), and $p$ hits every straggler because every straggler meets $\{2,p\}$ (pairwise-intersection) but not via 2 (straggler lacks 2), so via $p$ — and this holds for EVERY $p\in\mathrm{Cov}$, so every straggler contains ALL of Cov. Product $2p\le 2\max P(a_1)$. The next multiple of $2p$ above $a_n$ lies within $2p$ of $a_n$ and is valid and divisible by $2\le p^*$. Hence **W2 holds trivially whenever $\mathrm{Cov}\neq\emptyset$** (the post-crash regime). Verified on all 18 seeds: every post-crash strict-beat has $a_{n+1}\le a_n+2\max P(a_1)$ and $2\mid a_{n+1}$ (or a small-prime divisor $\le p^*$). The HARD sub-case is **$\mathrm{Cov}=\emptyset$** (pre-crash, or terminal-self-blocking-without-crash as in $a_1\in\{35,175,323,\ldots\}$ per `cov-monovariant` Lemma C-ref).

**F4 (the SMC is false).** I tested the stronger "some minimal $M\subseteq S:=\{p\le p^*\}$" (which would make EVERY transversal small-prime-divisible). It FAILS, but only mildly: it fails at step 1 (the straggler $P(a_1)$ has primes $>p^*$) and, for $\ge 3$-factor $a_1$ (385, 1365, 2145, 5005, 1155), it fails at MANY steps because the straggler $P(a_1)=\{p^*,\ldots\}$ persists as a minimal with primes $>p^*$. SPT itself holds (0 violations) throughout. So SMC is too strong; W2 needs the *specific winning transversal*, not "every transversal."

**F5 (valid numbers in the window are sparse).** In $(a_n,\mu_n]$, the valid numbers are typically exactly $\{a_{n+1},\mu_n\}$, occasionally three (e.g. $a_1=899$ step 12: $\{1302,1305,1334\}$). The slack $\mu_n-a_{n+1}$ is small (often $\le p^*$, e.g. $a_1=899$: slack $\equiv 29=p^*$; $a_1=429$: slack 1–3). This sparsity is an artifact of the transversal-product structure (F1), not a density fact.

### Mechanism (a) — Elementary short-interval sieve / CRT
**Sub-claim:** in an interval of length mtp $\le$ primorial$(p^*)$, force the smallest valid transversal-number to carry a small prime using only that multiples of small primes are dense (Bertrand/Chebyshev/CRT), NOT asymptotic smooth density.

**Obstacle (why it fails as a standalone mechanism):** validity is MULTIPLICATIVE (depends on the prime-factor set $P(m)$ hitting every $M\in\mathcal M_n$), NOT additive. Valid numbers do NOT form a union of residue classes mod $L'=\prod_{p\le p^*}p$ — two numbers congruent mod $L'$ can have different prime-factor sets (e.g. $L'+2$ vs $2L'+2$). A pure residue-count/CRT sieve over the window can bound the COUNT of $p^*$-rough integers (elementary inclusion-exclusion over small-prime multiples — a Brun-sieve flavor, available in `knowledge_base.md` only implicitly via "pigeonhole"), but it cannot force the smallest VALID to be small-prime, because the validity filter is an independent multiplicative constraint that does not align with residues. The density of small-prime multiples is irrelevant when the valid set is a sparse multiplicative subsemigroup.

**VERDICT: blocked as a standalone W2 mechanism.** A weak sub-lemma (p*-rough numbers are sparse in intervals of length primorial(p*) — elementary, via $\prod(1-1/q)$) is available and could supplement another mechanism, but cannot close W2 alone.

### Mechanism (b) — Greedy descent / minimal-criminal on the witness
**Sub-claim:** assume the smallest strict-beat candidate $a_{n+1}$ is $p^*$-rough (all prime factors $>p^*$); derive that some smaller valid number was available, contradicting the greedy's smallest-first pick, using only the structure of $\mathcal M_n$ (pairwise-intersecting minimal supports).

**Obstacle (why it's hard):** Two layers.
1. **Persistence of $P(a_1)$ (certified-adjacent, 0-viol, 41 seeds — recorded in `smooth-window-crash` §3):** $P(a_1)\in\mathcal M_n$ for all $n$ in regime (S), and no strict subset of $P(a_1)$ ever appears as a support. This gives "every valid number is divisible by some prime of $P(a_1)$, hence $\ge p^*$" — but NOT $\le p^*$. That is exactly the W1-gap recorded in `density-promotion-bound` §5e (the gap between $\ge p^*$ and $\le p^*$).
2. **The witness-AP variant fails (F2):** the natural construction "mu is divisible by $q\in T^*$ (W1); consider $\mu-q,\mu-2q,\ldots$; the largest below $\mu$ and above $a_n$ is a candidate" requires $a_{n+1}\equiv 0\pmod q$ for $q\in T^*$ — REFUTED by $a_1=175$ step 3 (witness $\{2,5\}$, $a_{n+1}=189$ divisible by neither).
3. **Entering-prime entanglement:** the small prime carried by $a_{n+1}$ can be an ENTERING prime (2, 3) outside $T^*$ (F2). Proving entering primes are $\le p^*$ IS the bounded-entering conjecture (`math-explorer.md` round-3 rule) — which is GAP-3 territory. So a minimal-criminal that produces a smaller valid number using entering primes $\le p^*$ partially circularizes into the GAP-3 wall.

**VERDICT: partially promising — the persistence-of-$P(a_1)$ lever is real and worth one builder attempt, but the direct construction is obstructed (F2) and the entering-prime dimension entangles W2 with GAP-3.** A viable narrow sub-route: the smallest multiple of $p^*$ above $a_n$ (within $p^*$ of $a_n$) is valid IFF it hits all stragglers; using Cov (every straggler contains all of Cov), if $p^*\in\mathrm{Cov}$ this works (F3). So mechanism (b) reduces to (c)+Cov in the post-crash regime, and is stuck in the pre-crash regime.

### Mechanism (c) — Cofactor / lcm arithmetic / TRANSVERSAL-PRODUCT RACE  ⭐ MOST PROMISING
**Sub-claim (clean reformulation of W2):** The valid numbers are exactly $\bigcup_{T\text{ transversal of }\mathcal M_n}\{m:\prod_{p\in T}p\mid m\}$ — a union of arithmetic progressions, one per transversal, with period $\prod T$. The greedy pick is $a_{n+1}=\min_T\{\text{smallest multiple of }\prod T\text{ above }a_n\}$. The mtp-multiple $\mu_n$ is the AP from the WITNESS $T^*$ (smallest period mtp). A strict-beat means the winner is a NON-witness transversal $T''$ with $\prod T''>\text{mtp}$. W2 becomes: **the winning $T''$ contains a prime $\le p^*$.**

**Why this is a finite arithmetic question, NOT analytic density:** the APs have explicit periods (transversal products). The all-large-prime transversals have periods $\ge$ nextprime$(p^*)^2$ (huge — this is the SAME obstruction recorded in `smooth-window-crash` §3 as "nextprime-squared $<$ primorial(p*)", which blocked W1's cheap proof, but HERE it HELPS: it makes all-large transversals' APs have LARGE period, so their next-multiple above $a_n$ is FAR on average). The small-product transversals (containing 2 or 3) have tiny periods ($2q$, $3q$) and their next-multiples are CLOSE. The race is won by small-period APs → small prime.

**The clean sufficient condition via Cov (F3, the post-crash kill):** if $\mathrm{Cov}(\mathcal M_n)\neq\emptyset$, then for any $p\in\mathrm{Cov}$, $\{2,p\}$ is a transversal (2 hits core, $p$ hits every straggler — every straggler contains all of Cov), period $2p\le 2\max P(a_1)$, next-multiple within $2p$ of $a_n$, divisible by $2\le p^*$. So $a_{n+1}\le a_n+2p$ and $2\mid a_{n+1}$. W2 holds trivially. This uses `cov-monovariant` (certified) — a genuine cross-approach asset.

**The residual obstacle (pre-crash, $\mathrm{Cov}=\emptyset$):** here $\{2,p\}$ is not auto a transversal. Yet F1 shows the winner is STILL a small-product transversal ($\{3,7\}$, $\{2,5\}$, $\{2,7\}$, etc.) containing a small entering prime. The reason a large-period all-large AP doesn't win by "coincidence" (i.e. $a_n$ sitting just below one of its rare multiples): **$a_n$ itself is a transversal-multiple** (it was the previous greedy pick, hence valid, hence divisible by $\prod T_n$ for some transversal $T_n$). This constrains $a_n$'s residues mod the large transversal products. The precise sub-claim to prove: *for every all-large transversal $T_{\rm lg}$ (product $P_{\rm lg}$), $a_n$ is NOT within $[\,P_{\rm lg}-(\text{gap bound}),\,P_{\rm lg}-1\,]\pmod{P_{\rm lg}}$ — i.e. the next multiple of $P_{\rm lg}$ above $a_n$ is farther than the next multiple of the small transversal.* This is a residue-constraint argument using that $a_n$ is itself a transversal-multiple; it is FINITE and CONCRETE, no asymptotics.

**VERDICT: most promising.** Reframes W2 as a transversal-AP race (finite, concrete), supplies a clean post-crash proof via Cov (certified asset), and isolates the genuine residual gap (pre-crash residue constraint on $a_n$) as a finite, attackable sub-claim — NOT a smooth-density analytic step. The field has NOT tried this framing; all prior W2 work (`smooth-window-crash` §5, `density-promotion-bound` §5f) assumed Dickman/de Bruijn smooth-number density was needed.

### Mechanism (d) — Value-free combinatorial replacement (avoid W2 entirely)
**Sub-claim:** close GAP-1 (mtp bounded) WITHOUT proving W2, by a different route (Cov-monovariant partner, or direct mtp-bound via self-blocking family structure).

**Obstacle:** CONFIRMED dead as a W2-bypass. The Cov-monovariant (`pstar-core-straggler`, certified) bounds only $\{2,p\}$-crash primes $\subseteq P(a_1)$; its own wall GAP-S' ("termination after Cov stabilizes") is the SAME wall as α's GAP-S (`pstar-core-straggler` §7, `density-promotion-bound` §5h) — the dispatch's note that "pure-combinatorial bypasses collapse" is empirically and structurally confirmed. The Cov route and the SPT/W2 route SHARE the crash-inevitability step; neither subsumes the other.

**VERDICT: dead as a W2-bypass.** BUT the Cov structure is a powerful SUB-INPUT to mechanism (c) — it supplies the post-crash sufficient condition (F3). So (d) folds INTO (c), not beside it.

---

## Summary table

| Mechanism | Sub-claim | Obstacle | Verdict |
|---|---|---|---|
| (a) elementary sieve/CRT | residue count forces small prime in window | validity is multiplicative, not additive; valid set $\neq$ residue classes mod $L'$ | **blocked** (standalone); weak sub-lemma only |
| (b) greedy descent / minimal-criminal | construct smaller valid from $p^*$-rough $a_{n+1}$ | witness-AP variant REFUTED (F2); persistence gives $\ge p^*$ not $\le p^*$; entering-prime entangles GAP-3 | **partially promising**; reduces to (c)+Cov post-crash |
| (c) transversal-product RACE | $a_{n+1}$=min over transversal APs; winner has small period → small prime | pre-crash ($\mathrm{Cov}=\emptyset$): rule out large-period AP winning by $a_n$-residue coincidence | **MOST PROMISING** ⭐ |
| (d) value-free combinatorial bypass | close GAP-1 without W2 (Cov partner) | GAP-S' = same wall; bypasses collapse (confirmed) | **dead** as bypass; folds into (c) as sub-input |

## Distinct openings (for the outliner)
- **(c) Transversal-AP race:** reframe W2 as $a_{n+1}=\min_T(\text{next mult. of }\prod T)$; prove the winner has small period ⇒ small prime. Splits cleanly into (c-i) post-crash ($\mathrm{Cov}\neq\emptyset$, killed by `cov-monovariant`), (c-ii) pre-crash ($\mathrm{Cov}=\emptyset$, the $a_n$-residue-constraint sub-claim).
- **(b-narrow) smallest-multiple-of-$p^*$ candidate:** the multiple of $p^*$ within $p^*$ of $a_n$ is valid IFF it hits all stragglers; via "every straggler contains all of Cov," this works when $p^*\in\mathrm{Cov}$ (post-crash). Pre-crash needs the straggler-common-prime structure (a Cov-free analog).
- **(a-weak) elementary rough-number sparsity sub-lemma:** $\prod(1-1/q)$ inclusion-exclusion gives that $p^*$-rough numbers in a primorial$(p^*)$-length interval are few — use only as a SUPPLEMENT to (c), to bound how many large-period AP hits can land in the window.

## Candidate technique(s)
- **Transversal / hitting-set duality** (combinatorics): valid numbers = union of transversal-product APs; the min-next-multiple race. This is the load-bearing reframe for (c).
- **Invariants & monovariants** (KB): the bounded-monotone-stabilizes principle, already used for Cov; applies to the post-crash termination.
- **CRT / modular arithmetic** (KB Number Theory): for the pre-crash residue-constraint sub-claim — $a_n$ is a transversal-multiple, constraining $a_n\bmod P_{\rm lg}$.
- **Pigeonhole / extremal principle** (KB Combinatorics): for the "small-period AP always has a multiple closer than large-period AP" race bound.

## Cheap-kill candidates
- **Post-crash W2 (Cov $\neq\emptyset$):** trivial via F3 — $\{2,p\}$ transversal, $2\mid a_{n+1}$, $2\le p^*$. This is a near-formality given `cov-monovariant` + `pairwise-intersection`; the outliner can ship it as a certified lemma immediately.
- **$a_{n+1}\le a_n+2\max P(a_1)$ in the post-crash regime:** direct corollary of the $\{2,p\}$-AP (next multiple within $2p$).

## Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics) — bounded monotone Cov stabilizes.
- **CRT / modular arithmetic, Hensel** (Number Theory) — pre-crash residue constraint on $a_n$.
- **Pigeonhole / extremal principle** (Combinatorics) — the AP-period race.
- **Bertrand's postulate** (Number Theory) — only as the "nextprime$(p^*)$ exists and is $>p^*$" fact, NOT for eviction (Bertrand-eviction is DEAD per `math-explorer.md`).

## Analogous past problems (cruxes)
- **aimo-0030** (`divisibility-and-gcd`): "no legal move connects two good numbers, so any two good numbers share a prime factor; since $k$ itself is good, every good number shares a prime with $k$." Analogue: persistence of $P(a_1)\in\mathcal M_n$ ⟹ every valid number shares a prime with $P(a_1)$ (mechanism (b)'s lever). Crux move: *read the obstruction off a non-adjacency class, forcing a shared prime.* Genuinely analogous to the persistence lever, not to W2's product-race.
- **aimo-0610** (`double-counting` / CRT): "count residue configurations avoiding every multiple of pairwise-coprime moduli as a product of per-modulus choices via CRT." Closest analogue to mechanism (a)'s sieve sub-lemma — but it counts ADDITIVE residue avoidances, whereas W2's validity is multiplicative; the match is partial, not load-bearing.
- **aimo-0436** (`diophantine-and-factoring` / CRT): "force a prime divisor outside any prescribed finite set by evaluating at a large multiple of their product." Inverts W2 (forces large prime, not small); not directly analogous but the CRT-gluing technique is the same tool the pre-crash residue sub-claim would use.

No crux in the corpus is a genuine load-bearing match for the transversal-AP product-race (mechanism (c)) — that framing appears to be novel to this problem. Do not force a match.

## Prior progress
- **Certified assets importable by W2 work:** `mtp-monovariant-and-gap-bound` (the window + mtp-multiple validity), `pairwise-intersection` (every two minimals meet ⟹ straggler-Cov structure), `cov-monovariant` (Cov $\subseteq P(a_1)$ monotone, the post-crash kill), `entering-2` (2 ∈ $P_{\rm ess}$ from step 2, so $2\le p^*$ is always available as a "small prime"), `common-primes-bounded`, `Sat-criterion`.
- **W1 (mtp-witness carries small prime):** 0 violations, 2044 step-records, 41 seeds — but NOT a formality (nextprime-squared obstruction). W2 is independent of W1 (F2).
- **The W1 "persistence of $P(a_1)$" sub-fact** (every transversal contains a prime $\ge p^*$): recorded in `smooth-window-crash` §3 as 0-viol but giving $\ge p^*$ not $\le p^*$. Mechanism (c) does NOT rely on closing this gap — it routes through the AP-race instead.

## Dead ends (do not retry)
- **Dickman/de Bruijn asymptotic smooth-number density for W2** (`smooth-window-crash` §5, `density-promotion-bound` §5f): DEAD as the primary mechanism — KB has no entry, the bounds are asymptotic while $a_n$ stays $O(a_1)$-ish, and validity is multiplicative not additive. F1-F3 show W2 is a finite transversal-AP question, NOT an analytic-density question. (May still surface as the (a-weak) sparsity supplement.)
- **Witness-AP minimal-criminal** ($a_{n+1}\equiv 0\bmod q$, $q\in T^*$): REFUTED by F2 ($a_1=175$ step 3). Do not build on "the strict-beat pick is a multiple of a witness prime."
- **"Every minimal $\subseteq S=\{p\le p^*\}$" (SMC):** FALSE (F4), fails for $\ge 3$-factor $a_1$ at many steps because the straggler $P(a_1)$ persists. Do not assert; SPT (every minimal HAS a prime $\le p^*$) is the right weaker statement.
- **Pure-combinatorial W2 bypass (mechanism (d)):** confirmed DEAD; Cov-route GAP-S' = SPT-route GAP-S. Do not claim a value-free bypass exists.
- **Bertrand-eviction, $\omega$-only induction, density-monotonicity/LLL/Mertens:** DEAD per `math-explorer.md` (rounds 1–3). Not retried.

## Small-case / intuition notes (CONJECTURE)
- **F1 (18 seeds, 0 viol):** the winning transversal at every strict-beat is small-product (product $\le 2\max P(a_1)$) and contains 2 or 3 (both $\le p^*$). All-large transversals never win. This is the empirical heart of mechanism (c).
- **F3 (post-crash kill):** when $\mathrm{Cov}\neq\emptyset$, $\{2,p\}$ is a transversal of period $2p$, so $a_{n+1}\le a_n+2p$ and $2\mid a_{n+1}$. Verified on all post-crash strict-beats. CONJECTURE that this is a theorem (it follows from `cov-monovariant`+`pairwise-intersection` directly — a builder can certify it).
- **F5 (sparse window):** valid numbers in $(a_n,\mu_n]$ are typically exactly 2, occasionally 3. The slack $\mu_n-a_{n+1}$ is small. CONJECTURE: a consequence of the AP-race structure (small-period APs dominate), not an independent fact.
- **Pre-crash residue sub-claim (the real open piece of (c)):** CONJECTURE that $a_n$ being a transversal-multiple prevents large-period all-large APs from winning. Verified on all pre-crash strict-beats (e.g. $a_1=175$ step 3: $a_n=182=2\cdot7\cdot13$, divisible by transversal $\{2,7\}$ product 14; the winning $\{3,7\}$ period 21 beats all-large options). The finite residue check is the next builder target.

---

most promising mechanism for W2 = **(c) the transversal-product RACE** ($a_{n+1}=\min_T$ next-multiple of $\prod T$; the winner has small period hence a small prime), because it reframes W2 as a finite arithmetic question (no asymptotic density, no KB entry needed), supplies a clean post-crash proof via the certified `cov-monovariant` (F3: $\{2,p\}$ is a transversal ⟹ $2\mid a_{n+1}\le a_n+2p$), and isolates the genuine residual gap (pre-crash $\mathrm{Cov}=\emptyset$: rule out a large-period all-large transversal AP winning by an $a_n$-residue coincidence — a finite CRT residue-constraint sub-claim, using that $a_n$ is itself a transversal-multiple). The field has NOT tried (c); it has tried W2 only as (Z = "Dickman/de Bruijn smooth-number density at the crash" in `smooth-window-crash` §5 / `density-promotion-bound` §5f), which is blocked (asymptotic-vs-bounded-$x$ tension, validity is multiplicative not additive). Mechanism (b) (minimal-criminal) is partially promising but its witness-AP variant is refuted (F2) and it reduces to (c)+Cov post-crash; mechanism (a) (elementary sieve) is blocked standalone (validity $\neq$ residue classes); mechanism (d) (value-free bypass) is dead (GAP-S'=GAP-S) but folds into (c) as the Cov sub-input.
