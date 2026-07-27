## imo-2026-06

Scout route: **transversal density done right** (α framing). The orchestrator flagged the obstruction: "promoting a new prime $q$ into $P_{\text{ess}}$ shrinks $V$, so transversal density does not grow monotonically; a bound surviving the pairwise-intersecting correlation of $\mathcal M$ (inclusion-exclusion / LLL) is required." I computed the density evolution and the promotion dynamics on ~150 seeds. **Headline: the density-monotonicity frame is the WRONG frame for the wall.** Density survives correlation fine (a clean lower bound exists), but density does NOT control promotions — free-rider primes in the greedy's specific pick do. The real wall is termination of the promotion process via **saturation or singleton-freeze**, and I found a clean, universally-verified sub-chain for the freeze branch. Redirect the wall-attack away from density.

### Distinct openings (far from α-density-monotonicity, β-Bertrand/Dickson, ε-omega-induction)

1. **Opening C — common-prime → arithmetic → $p^k$ → singleton-freeze.** CONJECTURE (verified on all common-prime seeds: 273, 413, 745, 813, 893, …): if a *common prime* $p$ emerges (a prime contained in EVERY member of $\mathcal M$), then $\{p\}$ is a transversal, so multiples of $p$ lie in $V$; the greedy locks to $a_{n+1}=a_n+p$ (smallest multiple of $p$ above $a_n$; the residues $a_n{+}1,\dots,a_n{+}p{-}1$ are not multiples of $p$ and fail to hit the $\{p,\cdot\}$-supports without $p$). Then $a_n=p\cdot(c{+}n{-}1)$ is arithmetic, and it hits $p^k$ when $c{+}n{-}1=p^{k-1}$ (always reachable for large $k$): that term has support $\{p\}$, a NEW minimal support, triggering **singleton-freeze** (already certified, `lemmas/singleton-freeze.md`). $\mathcal M\to\{\{p\}\}$, finite. Verified exactly: $a_1=273\Rightarrow a_{153}=729=3^6$; $a_1=413\Rightarrow a_{285}=2401=7^4$; $a_1=413,427,497,511,553,623$ all freeze at $\{7\}$; $a_1=745\to\{5\}$; $a_1=893\to\{19\}$. The common prime is the **smallest prime factor of $a_1$** in every freeze-regime seed tested.

2. **Opening S — saturated-antichain fixed point (no common prime).** CONJECTURE (verified: 15, 35, 65, 91, 143, 323, 899, 1517, 2491, 385, 429, 455, …): when no common prime emerges, $\mathcal M$ reaches a **saturated** antichain — every transversal of $\mathcal M$ contains a member of $\mathcal M$ as a subset — at which point no promotion is possible (a promotion requires a transversal containing no member; saturation forbids it). This is a structural fixed point; $\mathcal M$ is then finite and small ($|\mathcal M|\in\{3,4,5,6,7\}$ in all tests). Canonical example $a_1=15=3\cdot5$: $\mathcal M=\{\{2,3\},\{3,5\},\{2,5\}\}=K_3$ on $\{2,3,5\}$; every transversal (size-$\ge2$ subset hitting all three edges) contains an edge. $a_1=p\cdot q$ (both odd) typically yields $\mathcal M=K_3$ on $\{2,p,q\}$.

3. **Opening R — min-product-transversal monovariant.** Define $\tau^*=\arg\min_{\tau\text{ transversal}}\prod_{p\in\tau}p$. Adding a support shrinks the transversal set, so $\prod\tau^*$ is **non-decreasing** under promotions and stabilizes in both regimes (freeze: stabilizes at $p$; saturated: stabilizes at $2\cdot q$ for a structural prime $q$). Stabilization of $\prod\tau^*$ coincides with termination. Not a strict monovariant (can be constant for long stretches, e.g. $a_1=273$: $\prod\tau^*=3$ throughout), so it is a *termination certificate* not a descent driver — but it is the exact quantity whose stabilization IS the wall.

4. **Opening D-redirect (kill the density frame).** The α "density grows to choke new primes" mechanism is false: $a_1=273$ has $\rho\ge1/3$ throughout (min-product transversal $\{3\}$, prod $3$) yet suffers 47 promotions before freezing. Promotions are driven by **free-rider primes in the greedy's specific arithmetic pick** $a_n=p(c{+}n{-}1)$, not by density. Do NOT pursue density-monotonicity or LLL/inclusion-exclusion lower bounds on $\rho$ as the wall-attack — they solve a quantity that doesn't control the process.

### The density obstruction, concretely (points 1–2 of the task)

- $\rho=|R|/L$ is **non-increasing** as $\mathcal M$ grows (each promotion adds a hitting condition). Confirmed. But it does NOT crash: across all seeds $\rho$ stays in $[0.02,0.5]$ and **converges to a positive limit** (e.g. $a_1=429\to0.2117$, $a_1=455\to0.1619$, $a_1=385\to0.116$). The naive $1/L=\prod(1/p)$ bound is useless ($\to0$ super-exponentially); the **min-product-transversal bound $\rho\ge 1/\prod_{p\in\tau^*}p$ is the correct correlation-surviving lower bound**, and it is trivially TRUE (every multiple of $\prod_{p\in\tau^*}p$ has $\tau^*\subseteq D(m)$, hence is in $V$). Empirically $\rho\cdot\prod\tau^*\in[1.0,2.0]$ (so the bound is within a factor 2 of tight).
- **LLL/union-bound are vacuous here, and necessarily so.** Union bound: $\rho\ge1-\sum_{M}\prod_{p\in M}(1-1/p)$; for $K_3$ this is $1-19/15<0$. LLL: the "miss" events $E_M=\{D\cap M=\emptyset\}$ are dependent whenever $M,M'$ share a prime — but $\mathcal M$ is **pairwise intersecting** (`lemmas/pairwise-intersection.md`), so ALL pairs are dependent; LLL gives nothing. This is a structural dead end, confirming the orchestrator's worry. **The min-product-transversal bound is the way around it** — but as Opening D-redirect notes, $\rho$ itself is not the wall quantity.

### The outbidding mechanism (point 3)

What goes WRONG is NOT "new primes arbitrarily large so no fixed window" and NOT "correlation kills density." It is: **even at density $1/3$, the greedy's pick $a_n+p$ carries free-rider prime factors of $(c{+}n{-}1)$, and a new prime $q\mid(c{+}n{-}1)$ with $\{p,q\}$ not yet dominated yields a promotion.** Promotions continue at full density. The process terminates NOT because density outbids new primes, but because the arithmetic line eventually lands on $p^k$ (a pure power of $p$, support $\{p\}$), triggering singleton-freeze. The "threshold" is not a density threshold; it is the **guaranteed hit of an arithmetic progression on a pure prime power** (always reachable: $c{+}n{-}1=p^{k-1}$ for $n=p^{k-1}-c{+}1$). CONJECTURE, verified on every freeze-regime seed.

### Smooth-number framing (point 4)

Explored, **less promising than C/S**. Smooth numbers $\Psi(x,y)\sim x\rho(u)$ give density $\to0$ as $x\to\infty$ for fixed $y$, so no uniform fixed-window density beats new-prime candidates independently of $\mathcal M$'s correlation. The one useful contact: in the common-prime regime the greedy's picks are exactly $p\cdot(\text{linear})$, and "$p$-smooth with all factors $p$" = pure powers $p^k$ = the freeze trigger — i.e. smooth-number density *is* Opening C in disguise, not an independent framing. Do not pursue smooth numbers as a separate route.

### Candidate technique(s)

- **Singleton-freeze** (certified, `lemmas/singleton-freeze.md`) — the terminal lemma for Opening C.
- **Structural fixed-point / saturation** (combinatorics: "operation exhausted until stuck", cf. aimo-0014) — Opening S: show promotions exhaust to a saturated antichain.
- **Arithmetic-progression-hits-prime-power** (number theory: AP $p\cdot(c{+}n)$ contains $p^k$ since $c{+}n=p^{k-1}$ is solvable) — the cheap kill for the common-prime branch.
- **Monovariant / non-decreasing-and-bounded** (`knowledge_base.md` Invariants & monovariants) — $\prod\tau^*$ stabilizes; proving strict drop on non-terminal promotions would terminate.
- Min-product transversal $\tau^*$ (combinatorial optimization on the antichain).

### Cheap-kill candidates

- **Saturation test**: once $\mathcal M$'s min-product transversal $\tau^*$ has stabilized AND every transversal contains a member, no promotion is possible — structural kill, no density computation. Try this BEFORE any analytic bound.
- **Singleton emergence**: check whether a common prime $p$ has emerged (intersection of all $M$ nonempty); if so, the AP-hits-$p^k$ argument is a one-line termination (modulo proving the diff locks to $p$).
- **Parity/injection on $|\mathcal M|$** in the no-common-prime regime: empirically $|\mathcal M|\le7$ and the entering non-$a_1$ primes are a bounded set $\{2,3,5,7\}$ — a pigeonhole/size bound on the structural prime set would cap $|\mathcal M|$ and force saturation.

### Knowledge-base entries to use

- **Invariants & monovariants** (Combinatorics) — $\prod\tau^*$ non-decreasing + bounded; structural fixed point.
- **Modular arithmetic, CRT** (already used in conditional theorem).
- **Pigeonhole / extremal principle** — cap $|\mathcal M|$ / structural prime set in saturated regime.
- NOTE: knowledge_base.md has **no LLL / Janson / inclusion-exclusion lower-bound entry** — and they are vacuous here anyway (pairwise-intersecting $\mathcal M$). Do not add them; use the min-product-transversal bound instead.
- **Mertens 3rd theorem** (stated in α's §7) is NOT needed for the wall — it was set up for the dead density-monotonicity frame. Drop it.

### Analogous past problems (cruxes)

- **aimo-0014** (combinatorics, processes-and-algorithms) — "Exhaustively apply a degree-reducing operation until the graph is stuck in a uniform-parity state, using that it must terminate." Analogous: our promotions exhaust until $\mathcal M$ is stuck (saturated) or frozen. Crux: operation-exhaustion-to-stuck-state. Mild analogy (graph degree vs prime supports), but the termination-by-exhaustion structure matches Opening S.
- **aimo-0077** (combinatorics, extremal-principle) — "Assume nontermination forces a repeating state-cycle; take the minimal-index object acted on within that cycle and show restoring it requires a forbidden smaller-index action." Analogue flavor: a nontermination contradiction via a minimal witness. Our state space is infinite (numbers grow), but the *essential* structure ($\mathcal M$) is a finite-type object — a saturation/freeze argument plays the role of "stuck state."
- **aimo-0121** (combinatorics, invariants-and-monovariants) — "Track the running maximum as a monovariant; every non-terminal position admits a move increasing the max, so move-count is bounded by (target−current)." Analogy to the $\prod\tau^*$ monovariant (Opening R), but ours is non-strict.
- No exact match for the common-prime→arithmetic→$p^k$→freeze chain exists in the corpus; the closest structural kin is the "AP hits a prime power" + singleton-freeze combination, which is problem-specific.

### Prior progress

The conditional theorem (`lemmas/post-stabilization-theorem.md`) is DONE and certified: $\mathcal M$ finite $\Rightarrow$ $a_{n+T}=a_n+L$ ($L=\prod P$, $T=|R|$). 8 lemmas certified. The ONLY open wall is finiteness of $\mathcal M$. α (`density-promotion-bound.md`) set up the density engine (Lemma 6: conditional density $\ge1/L$) and correctly identified the monotonicity obstruction but did not close GAP-D. β (`bertrand-dickson-eviction.md`) proved the unconditional gap-at-promotion bound $a_i-a_{i-1}\le\prod_{p\in O}p$ (`lemmas/gap-bound-at-promotion.md`) — a real partial result but insufficient (depends on $a_{i-1}\to\infty$).

### Dead ends (do not retry)

- **α density-monotonicity / LLL lower bound on $\rho$** (GAP-D as framed): density does not control promotions (free-rider primes do; verified $a_1=273$: $\rho\ge1/3$ with 47 promotions). LLL is vacuous (pairwise-intersecting $\mathcal M$ makes all events dependent). Do not pursue "density grows to choke new primes."
- **β Bertrand's postulate to evict large primes**: honestly admitted dead (no dyadic interval forced to contain a new essential prime). Bertrand does not bound prime sizes here.
- **β "ever-minimal supports form an antichain under refinement"**: FALSE (self-corrected, $a_1=30$: $\{2,3,5\}\to\{2\}$).
- **Mertens/$\sum1/p$ engine** (α §7): set up for the dead density frame; not needed. Drop.

### Small-case / intuition notes (all CONJECTURE, strongly verified on ~150 seeds)

1. **Two regimes, both universal.** Every seed reaches EITHER singleton-freeze ($\mathcal M\to\{\{p\}\}$) OR a saturated antichain (no common prime, $|\mathcal M|\le7$). No seed exhibited infinite non-saturating promotions.
2. **Freeze regime**: common prime = smallest prime factor of $a_1$; greedy locks to diff $p$; freeze at term $p^k$ ($a_1=273\to3^6=729$@n153; $413\to7^4=2401$@n285; $413,427,497,511,553,623\to\{7\}$; $745\to\{5\}$; $893\to\{19\}$). The AP-hits-$p^k$ step is the clean sub-lemma.
3. **Saturated regime**: no common prime; $\mathcal M$ a small saturated antichain ($a_1=pq$ both odd $\Rightarrow K_3$ on $\{2,p,q\}$, $|\mathcal M|=3$); entering non-$a_1$ primes bounded to $\{2,3,5,7\}$. $a_1=15$ is the canonical saturated case (period $T=8,L=30$, NOT arithmetic — so the saturated regime genuinely needs the conditional theorem, not the arithmetic shortcut).
4. **min-product transversal $\prod\tau^*$ stabilizes** in both regimes (freeze: $=p$; saturated: $=2q$), and stabilization = termination.
5. **The distinction between regimes is subtle** (e.g. $a_1=15=3\cdot5\to$ saturated; $a_1=21=3\cdot7\to$ freeze via $\{3\}$) — both have smallest factor 3 — so the wall must handle both branches or find a unifying invariant. The outliner should build ≥1 approach on Opening C (freeze) and ≥1 on Opening S (saturation), since neither subsumes the other on current evidence.
