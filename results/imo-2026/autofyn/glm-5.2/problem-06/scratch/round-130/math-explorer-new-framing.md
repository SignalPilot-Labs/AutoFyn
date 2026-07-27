# imo-2026-06 — genuinely-different whole-wall framing (round 130)

Lens: a framing of the WHOLE wall (finiteness of $\mathcal M$) far from both the SPT-route (α/smooth-window-crash/γ: bound prime VALUES, min$(M)\le p^*$) and the Cov-route (pstar: bound {2,p}-crash-prime MEMBERSHIP $\subseteq P(a_1)$). Computed on ~20 saturated + freeze seeds; exact term-by-term greedy.

## The wall, restated for orientation
$\mathcal M_n=\min_\subseteq\{P(a_1),\dots,P(a_n)\}$; a promotion adds a new minimal $M'=P(a_{n+1})$ (not dominated); a crash refines (removes $\ge1$ old member). Wall = prove $\mathcal M=\bigcup_n\mathcal M_n$ finite. Two live framings both bottom out on "a smooth-number argument at the crash." This report scouts framings that do NOT route through the crash.

---

## Candidate framings — verdicts

### (A) Minimal-criminal / descent on the prime set — BLOCKED (collapses to SPT)
Shape: assume $P_{\rm ess}$ infinite; let $q$ be the smallest essential prime $>p^*$ "causing trouble"; when $q$ enters in $M'=P(a_{n+1})$ with $q\in M'$, construct a smaller admissible $m<a_{n+1}$, contradicting smallest-first.
Obstacle: $M'\supseteq T^*$ (a minimal transversal of $\mathcal M_n$, since $M'$ hits every member). To build $m<a_{n+1}$ admissible we must exhibit a transversal of $\mathcal M_n$ whose product-multiple lands in $(a_n,a_{n+1})$ and does NOT use $q$. That is *exactly* "the strict-beat admissible carries a small prime $\le p^*$" = **W2**. The descent's engine (greedy smallest-first) and SPT's engine are the same once you write down what "smaller admissible" must mean. No genuinely different mechanism.
VERDICT: blocked — not far from the SPT route.

### (B) König's infinity lemma / compactness on the refinement forest — BLOCKED for the whole wall (only bounds the small piece)
Shape: build the refinement DAG (nodes = minimals ever appearing, edge $M\to M'$ when $M'\subsetneq M$ at a promotion). If infinitely many promotions, the DAG is infinite. König: a finitely-branching infinite tree has an infinite branch.
Obstacle (verified): the refinement DAG is TINY. Across all seeds, refinements are $<10\%$ of promotions (e.g. a1=46189: 477 promotions, only the "r" tokens are refinements — the bulk are incomparable additions). Reason: a refinement chain $M_1\supsetneq M_2\supsetneq\cdots$ has length $\le|M_1|$ (primes shrink), and the children of $M$ are subsets of $M$ ($\le 2^{|M|}$). So the refinement forest is finite IF minimal sizes are bounded. **But the bulk of the wall is incomparable additions** (new minimals carrying fresh primes, not refining anything), and König says nothing about those — they are an unbounded-width frontier, not a branch. König bounds the wrong sub-structure.
VERDICT: blocked for the whole wall (bounds only the refinement forest, which is already small; incomparable additions escape it).

### (C) Strictly-decreasing potential (Lyapunov) — BLOCKED (the data is a plateau, not a descent)
Shape: find a bounded-below strictly-decreasing integer quantity along promotions (the dual of mtp, which is monotone INcreasing). Candidates: #active-large-primes, $1/$mtp, #avoiding-transversals, minAvSz.
Obstacle (verified + round-3 rules): all four tracked ranks (mtp, $\tau$, minAvSz, fixTr#) **stabilize early (~5 promotions) and then promotions continue on the plateau**. The crash that eventually terminates is a smooth-number event (every saturated crash lands at a $\le3$-distinct-prime number: $2^a p^b$, $2^a3^b7^c$, prime powers — confirmed on all saturated seeds). There is no decreasing quantity to find; the process runs along a plateau and exits via a value-event, not a descent.
VERDICT: blocked — no descent exists (plateau+crash structure, already articulated round 3).

### (D) Direct structural cap on $|\mathcal M_n|$ (value-free, EKR/Helly-flavored) — DEAD (refuted by data)
Shape: prove the greedy-generated pairwise-intersecting antichain has $|\mathcal M_n|\le 2^{|P(a_1)|}$ once Cov stabilizes, purely combinatorially.
Obstacle (refuted): a1=46189 ($|P(a_1)|=4$) reaches $|\mathcal M_n|=288$ (still growing at 1500 terms), with 268 entering primes. $2^{|P(a_1)|}=16\ll 288$. a1=37961 stabilizes at $|\mathcal M|=65$. The greedy-generated family genuinely realizes large pairwise-intersecting antichains (projective-plane-like: 287/288 minimals of 46189 are size-3 triples all sharing the prime 2 — a "star," not a common-point-free projective plane, but unbounded in count). No static $|P(a_1)|$-only cap exists; the round-3 rule "NEVER bound $\tau$ structurally for pairwise-intersecting antichains — projective planes" stands.
VERDICT: dead — refuted by 46189/37961.

### (E) Straggler-stabilization + star-transversal completion — PROMISING (the genuinely-different framing)
Discovered by studying actual dynamics. This is the report's main finding.

**Decomposition.** Split $\mathcal M_n$ into
- the **straggler family** $\mathcal S_n=\{M\in\mathcal M_n:2\notin M\}$ (no-2 minimals), and
- the **star** $\mathcal M_n^*=\{M\in\mathcal M_n:2\in M\}$ (2-containing minimals).

**Structural fact 1 (PROVABLE, pure set theory, value-free).** *Stragglers are closed under refinement: if $M\in\mathcal S_n$ and a later promotion adds $M'\subsetneq M$, then $M'\in\mathcal S_n$.* Proof: $M'\subseteq M$ and $2\notin M\Rightarrow 2\notin M'$, so $M'$ is a straggler. Consequently the straggler family evolves as a **closed subsystem**: star promotions (with 2) never refine stragglers (a 2-set can't be a subset of a no-2-set), so $\mathcal S_n$ changes ONLY when a new straggler is added (refining old stragglers). Verified on all 17 seeds (`straggler-closed-under-refinement: True`).

**Structural fact 2 (PROVABLE).** *Every star member $M'$ covers a clean transversal: $M'\supseteq\{2\}\cup T$ for some minimal transversal $T$ of $\mathcal S_n$.* Proof: $M'$ hits every member of $\mathcal M_n$, in particular every straggler; since stragglers lack 2, $M'\setminus\{2\}$ hits every straggler, i.e. is a transversal of $\mathcal S_n$, hence contains a minimal transversal $T$. Verified: "every star member covers a clean $\{2\}\cup T$: True" on ALL 17 seeds.

**Empirical fact 3 (CONJECTURE, strong).** *The straggler family stabilizes after finitely many steps and is TINY (1–3 members).* Verified: a1=46189 (477 promotions) — straggler $=\{11,13,17,19\}=P(a_1)$ stabilizes at **step 2**, never changes; the other 475 promotions are all star. a1=96577: straggler stabilizes at term ~416 (11 straggler promotions). a1=37961: straggler $=P(a_1)=\{7,11,17,29\}$, stabilizes at step 2; all 227 later promotions are star. The straggler family is 1–3 members in every seed.

**Empirical fact 4 (CONJECTURE).** *Once $\mathcal S$ stabilizes to a fixed finite family, the terminal family is $\mathcal S\cup\text{star}$ reaching generalized self-blocking; the clean star $\{\{2\}\cup T:T\text{ minimal transversal of }\mathcal S\}$ is a SUFFICIENT terminal (generalized Lemma D), but the actual terminal may be richer (free-rider star members).* Verified: seeds where star$==$clean (15,35,77,91,105,143,195,323,385,429,1001,96577,25025,62491,4199 — star exactly the clean transversals, self-blocking); seeds where terminal is richer (175: 2 of 4 clean transversals yet already self-blocking; 37961: 60 free-rider star members stabilize at $|\mathcal M|=65$; 46189: 283 free-rider star members, not yet stabilized).

**Why this is genuinely different from BOTH live framings.**
- vs SPT: no prime-VALUE bound anywhere. The straggler closure (fact 1) and the clean-cover (fact 2) are pure $\subseteq$-set theory. The large free-rider primes (e.g. 2633 in 46189) live ONLY in star members, never in stragglers — the straggler subsystem is value-free.
- vs Cov: Cov bounds $\{2,p\}$-crash primes $\subseteq P(a_1)$ (a 2-element star-member sub-type). This framing bounds the **straggler subsystem** (a different, no-2 sub-family) and reduces the wall to **star completion over a FIXED FINITE straggler family** $\mathcal S$. Once $\mathcal S$ is fixed, the clean minimal transversals $T_1,\dots,T_K$ of $\mathcal S$ are FINITE in number (their ground set is $\bigcup\mathcal S$, finite), so the clean star $\{\{2\}\cup T_i\}$ is finite — a self-blocking sufficient terminal exists *structurally*. The open piece is whether the greedy's smallest-first installs enough of them (or a richer self-blocking family) before running out — a **transversal-installation-timing** question, NOT a smooth-density/W2 question.

**The open sub-gap (honest).** After $\mathcal S$ stabilizes, why does the star reach self-blocking? Free-rider star members (like 37961's 60, 46189's 283) can accumulate: a star member $\{2\}\cup U$ with a free-rider prime $q\notin\bigcup\mathcal S$ is added only when the "clean" version $\{2\}\cup(U\setminus\{q\})$ is behind $a_n$ (its product $\le a_n$) — i.e. when the clean transversal multiples have all been passed. This is genuinely the SAME flavor of value-timing obstruction as the crash, BUT over a fixed finite ground set $\bigcup\mathcal S$ and a finite transversal menu $T_1,\dots,T_K$, which is a more constrained setting than the original crash. The sub-gap "straggler stabilization is provable" also needs work (closure gives bounded-depth REFINEMENT chains from $P(a_1)$, but incomparable straggler additions like 4199's $\{13,83\}$ need a separate argument — empirically they stop, conjecturally because the smallest-odd-admissible prefers small primes).

**Straggler primes are NOT always small** (honest correction): 4199 has a straggler $\{13,83\}$ (83 a free-rider IN a straggler), 175 has 13. So "straggler primes $\subseteq P(a_1)\cup\{3,5,7\}$" is FALSE in general. The right claim is only "straggler family stabilizes finitely" (fact 3, conjecture), NOT "straggler primes bounded by value." This keeps the framing value-free.

---

## Distinct openings for the outliner
1. **Prove straggler stabilization** (fact 3): closure (fact 1) + an argument that incomparable straggler additions terminate. Candidate: the smallest-odd-admissible is a multiple of an odd-transversal of $\mathcal S_n$, and odd-transversals use primes of $\bigcup\mathcal S_n$; induction on $|\bigcup\mathcal S_n|$ with a size bound on straggler members. This is the load-bearing new lemma.
2. **Generalized Lemma D**: for fixed finite straggler family $\mathcal S$, the family $\mathcal S\cup\{\{2\}\cup T:T\text{ minimal transversal of }\mathcal S\}$ is self-blocking (value-free, unconditional). Verified self-blocking on every stabilized seed where star$==$clean. This is a clean importable terminal, strictly generalizing pstar's Lemma D (which only handles $\{2,p\}$ pairs).
3. **Star-installation-timing sub-gap**: once $\mathcal S$ fixed, prove the star reaches SOME self-blocking family (clean or richer) over the finite transversal menu — the genuinely open piece, but on a more constrained (fixed finite ground set) stage than the original crash.

## Candidate technique(s)
- **Invariants & monovariants** (KB): the straggler closure is a monovariant-style invariant (the no-2 sub-family is a trapped subsystem).
- **Hall's marriage / SDR** (KB, Combinatorics): the star$=$clean-transversals structure is literally a hitting-set/transversal characterization; transversal finiteness over a finite ground set is the engine.
- **General proof methods — contradiction + extremal** (KB): assume $\mathcal M$ infinite; the straggler subsystem (closed) must then either be infinite (contradicting stabilization) or the star is infinite over a fixed $\mathcal S$ (the narrowed target).

## Cheap-kill candidates
- **Trivial-case prune** (already done): $a_1$ even or prime power $\Rightarrow$ freeze. Only odd $a_1$ with $\ge2$ primes is the hard case — there the FIRST straggler is $P(a_1)$ (no 2), giving the closed subsystem a definite seed.
- **Injection / finite-ground-set**: once $\mathcal S$ stabilizes, minimal transversals of $\mathcal S$ are subsets of the finite set $\bigcup\mathcal S$, so there are $\le 2^{|\bigcup\mathcal S|}$ of them — a finite clean-star menu. (This is the one genuinely value-free finiteness that falls out.)

## Knowledge-base entries to use
- *Invariants & monovariants* (Combinatorics / General Proof Methods) — for the straggler-closure subsystem.
- *Hall's marriage theorem / SDR* (Combinatorics) — for the transversal characterization of the star.
- *Pigeonhole / extremal principle* + *Induction / structural induction* (General Proof Methods) — for the straggler-stabilization induction.
- *post-stabilization-theorem* (lemma, imported) — the finish once $\mathcal M$ finite.

## Analogous past problems (cruxes)
None genuinely analogous. The closest in *spirit* (process termination via monovariant) are aimo-0121 (distribute-evenly process; charge moves against per-part surplus — amortized-counting flavor) and aimo-0014 (exhaust a degree-reducing operation until stuck in a uniform-parity terminal state). Neither shares the prime-support/transversal structure; they are analogies of "termination of a greedy process," not of the wall. No crux move transfers directly.

## Prior progress
Best live: the conditional transversal theorem (δ, certified) + freeze regime (α, solved) + mtp monovariant (γ, certified) + Cov-monovariant (pstar, certified). The wall (saturated termination) open. This report adds a NEW structural fact (straggler closure, PROVABLE) not in any prior approach, and a NEW decomposition (wall splits into straggler-stabilization + star-completion-over-fixed-$\mathcal S$).

## Dead ends (do not retry)
- (A) minimal-criminal on primes — collapses to W2/SPT.
- (B) König on refinement forest — only bounds the tiny refinement piece; incomparable additions escape.
- (C) decreasing Lyapunov — no descent exists (plateau+crash, round 3).
- (D) static $|\mathcal M|\le 2^{|P(a_1)|}$ cap — refuted (46189: 288 vs 16).
- (per run_state) ω-only induction, Bertrand eviction, density-monotonicity/LLL/Mertens, Dickson WQO multiset, naive finite-state/lcm-reduction, "free-rider universality," W1-as-GAP-1-closer, the round-3 "linchpin," pstar's Lemma C (crash-to-full-star) — all dead.

## Small-case / intuition notes (CONJECTURES, not proved)
- Straggler family stabilizes finitely and is 1–3 members in every seed (17/17). CONJECTURE.
- Once $\mathcal S$ fixed, the clean star $\{\{2\}\cup T_i\}$ (minimal transversals of $\mathcal S$) is a self-blocking sufficient terminal (generalized Lemma D) — PROVABLE-looking, verified. CONJECTURE pending proof.
- The actual terminal may use only SOME clean transversals (175: 2/4) OR be richer with free-rider star members (37961: 60 free-rider; 46189: 283 free-rider, still growing) — so "all clean transversals installed" is sufficient, not necessary. CONJECTURE.
- Large free-rider primes (2633 in 46189) appear ONLY in star members, never in stragglers — verified 17/17. CONJECTURE that stragglers are the value-free trapped subsystem.

---

the most promising genuinely-different framing = (E) straggler-stabilization + star-transversal completion, because it rests on a PROVABLE value-free structural fact (straggler closure under refinement — pure set theory, verified 17/17) that NO prior approach uses, and it splits the wall into a closed subsystem (stragglers, stabilizes) + a star-completion question over a FIXED FINITE straggler family whose clean minimal transversals are finite in number (a sufficient self-blocking terminal exists structurally); it is far from both the SPT-route (no prime-value bound anywhere; the trapped straggler subsystem is value-free) and the Cov-route (Cov bounds $\{2,p\}$-crash-prime membership in $P(a_1)$ — a 2-element star sub-type — whereas this bounds the no-2 STRAGGLER sub-family, a different subsystem, and handles the star via transversal structure over fixed $\mathcal S$, not crash-prime membership).
