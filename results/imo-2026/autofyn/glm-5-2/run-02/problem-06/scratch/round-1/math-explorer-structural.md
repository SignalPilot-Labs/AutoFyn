## imo-2026-06 — STRUCTURAL NUMBER-THEORY route (common-prime collapse)

### Distinct openings (this route surfaces)

1. **Pure-prime-power collapse (T=1, L=p).** If any term a_j is a pure prime power p^k (P(a_j)={p}), then every subsequent term must be divisible by p (to hit {p}). Since a_n is then a multiple of p, the smallest multiple of p strictly greater than a_n is a_n+p. So a_{n+1}=a_n+p from j onward: T=1, L=p. This is the clean sub-case; computationally it fires for a_1 ∈ {prime, prime power, 2·(odd prime) like 21→3, 33→3, 11→11, 8→2, 25→5, …} and many "rich" starts. **But it is NOT universal** — see opening 2.

2. **Multi-prime translation-periodic regime (general T, L=∏S).** Counter-example to the single-prime story: a_1=15 yields T=8, L=30=2·3·5; a_1=35 yields T=34, L=210=2·3·5·7; a_1=77 yields T=18, L=154=2·7·11. In every case L is the *squarefree product of a stable essential-prime set S*, and the residues a_n mod L cycle with period T. No pure prime power ever appears in these cycles (e.g. for a_1=15 the residue cycle mod 30 is {15,18,20,24,0,6,10,12}, every element divisible by ≥2 of {2,3,5}). The proof must reach the general translation-periodic conclusion a_{n+T}=a_n+L, not just T=1.

3. **Free-rider / essential-prime separation (the key structural invariant).** A prime q freshly introduced at step n is **never essential**: to be essential it would have to be the sole shared prime with some earlier a_i, but q∉P(a_i) for i<n. So every new prime is a *free rider* (it divides a_n because the smallest integer realizing the essential pattern happens to carry it, e.g. 18=2·3² carries the free rider 2; 42=2·3·7 carries free rider 7). Free riders are irrelevant to the covering logic and may be infinite in number (e.g. a_1=11 → a_n=11n, cofactors sweep all primes). The structural quantity is the **essential prime set**, which is always a subset of previously-seen primes and which one must show is eventually bounded.

4. **Transversal-family stabilization (the load-bearing step).** Let F_n = {P(a_i): i≤n} (family of prime-divisor sets). a_{n+1}'s P-set must be a *transversal* (hitting set) of F_n. As F_n grows, the family T(F_n) of transversals is **decreasing**. Once the universe of essential primes is bounded to a finite set S, T(F_n) is a decreasing sequence of subsets of the finite 2^S, so it **stabilizes**: T(F_n)=T(F_N) for n≥N. Then the greedy decision depends only on a_n mod L (L=∏S, squarefree): the next residue is a deterministic function of the current residue. Finitely many residues ⇒ residue sequence eventually periodic with period T ⇒ a_{n+T}=a_n+L (sum of gaps over one period = L). This is the direct adaptation of the aimo-0678 "mod-lcm finite-state reduction" crux.

5. **Min-of-set monovariant (borrowable from aimo-0678).** aimo-0678 bounded an unbounded coordinate via w_n = min{m≥a_n : m does not divide the frozen invariant s_n}, shown non-increasing. The analog here: once a frozen essential structure exists, define a min-of-set quantity that is monotone, forcing the essential prime set to stop growing. This is the most plausible route to close the hard gap of opening 4 (proving essential primes bounded).

### Candidate technique(s)
- Hitting-set / transversal duality on the family of prime-divisor sets F_n (decreasing-family-on-finite-set ⇒ stabilization).
- Finite-state reduction mod L (squarefree product of stable primes) ⇒ eventual periodicity of residues ⇒ translation-periodicity of values.
- Min-of-set integer monovariant to bound the essential-prime universe (the genuine crux).
- Sub-case shortcut: pure-prime-power detection ⇒ immediate T=1,L=p collapse (a one-line terminal case).

### Cheap-kill candidates
- **Parity / factor-2 injection:** once 2 divides some term, and 2 stays a free rider widely. For odd a_1, the second term a_2 is forced to be even (smallest > a_1 sharing a factor with a_1: e.g. a_1=15→a_2=18 even; a_1=21→a_2=24 even; a_1=35→a_2=36 even; a_1=77→a_2=78 even). So 2 enters S almost immediately for odd starts; it then stays. This gives a cheap lower anchor on S.
- **Pigeonhole on residues mod L once S is fixed:** only |S| primes ⇒ L=∏S ⇒ ≤L residues ⇒ finite state. (Standard, but only applicable after the hard step.)
- **Injection / size bound:** the number of distinct minimal transversals of F_n on essential primes is at most 2^|S|; once fixed, the residue pattern is forced.
- none obvious for a one-step kill — this is a 9/10 problem.

### Knowledge-base entries to use
(Could not read knowledge_base.md in full — file is large; the outliner must grep it for:) **decreasing-family / monotone-stabilization on a finite lattice**; **finite-state-machine ⇒ eventual periodicity**; **transversal / hitting-set duality**; **min-of-set monovariant**; **smooth-number density arguments** (if needed for the "new primes can't be essential forever" step). The outliner should search knowledge_base.md for entries on "eventually periodic", "monovariant", "finite state", "gcd/divisibility chains", "Bertrand/postulate size bounds".

### Analogous past problems (cruxes)
- **aimo-0678 (IMO-SL 2015, France)** — *the single most directly analogous crux.* Its three crux moves map onto our problem almost one-for-one: (a) **invariant-sum / regime-splitting** → identify the divisibility "phase" where the recurrence simplifies; (b) **min-of-set monovariant** w_n = min{m≥a_n : m fails the frozen invariant}, shown non-increasing ⇒ boundedness of the runaway coordinate; (c) **mod-lcm finite-state reduction** → once one coordinate is bounded, reduce the other mod lcm of attainable values, giving a deterministic map on a finite set ⇒ eventually periodic. Our problem replaces "boundedness of a_n" with "boundedness of the essential-prime set S", then lifts periodicity to *translation*-periodicity via the value gap summing to L over one residue period. Adaptable, not citable.
- **aimo-0477 (IMO-SL 2018, Mongolia)** — secondary analog. Crux: track g_n=gcd(a_1,a_n); show v_p(g_n) is nondecreasing for every p, giving an ascending divisor chain of the fixed a_1 that stabilizes; then integrality forces the residual part to divide downward ⇒ eventually constant. The "stabilizing divisor chain bounded by a fixed term" shape is a candidate for proving our essential-prime set stabilizes (treat the lcm of essential primes seen-so-far as a bounded-monomial chain).
- **aimo-0502 (IMO-SL 2008)** — tertiary, only for the "exhibit a number in (N/2,N) where N has no divisor" size-bounding trick and the "normalize by overall gcd so terms are setwise coprime" move; possibly useful if a contradiction-style bound on a new essential prime is needed.
- No crux in the corpus matches the *greedy-smallest* feature exactly; the closest structural analog is the periodicity conclusion of aimo-0678.

### Prior progress
- None. Workspace fresh: `results/imo-2026-06/approaches/` empty, no `.ranking.json`, no lemmas, `current.md` Status=unsolved.

### Dead ends (do not retry)
- None yet (round 1).
- **Warning to outliner:** do NOT build the whole field around the "common-prime collapse to T=1, L=p" framing. It is FALSE in general (a_1=15,35,77,105 are counter-examples). Any approach that assumes "eventually some term is a pure prime power" is dead on arrival for those starts. The T=1 collapse is at most a *terminal sub-case*, not the main argument.

### Small-case / intuition notes (all CONJECTURES, evidenced numerically not proved)
- For a_1 = prime or prime power p^k: a_n = p·n from the start; T=1, L=p. (Conjectured universal for these starts.)
- For a_1 = 2·(odd): collapses to T=1, L=2 immediately (a_1=6→L=2; a_1=10→L=2; a_1=30→L=2; a_1=210→L=2).
- For a_1 = odd composite with ≥2 odd prime factors and no factor 2: enters the multi-prime regime. Observed (conjectured): L = squarefree product of the stable essential set S, where S = {2} ∪ {odd primes that never get "killed" by a pure-prime-power term}. Conjectured: S is exactly the set of primes p such that no term a_n is a pure power of p alone AND p divides the gcd of the eventual residue-cycle structure.
- a_1=15: S={2,3,5}, L=30, T=8, residue cycle mod 30 = {15,18,20,24,0,6,10,12}.
- a_1=35: S={2,3,5,7}, L=210, T=34.
- a_1=77: S={2,7,11}, L=154, T=18.
- a_1=105: not detected in 150 terms — needs longer run; conjectured S⊇{2,3,5,7}, L≥210. (Free riders in the tail include 11,13,17,19,23,29,31,41,43,47,53,59,61 — all free riders, confirming new primes keep appearing but do not affect structure.)
- The differences a_{n+1}-a_n in the eventual regime sum to L over T terms and each gap is a "jump to next valid residue".
- Free-rider primes can be infinite (a_1=11: a_n=11n, cofactors sweep all primes) — so "S_n stabilizes" in the naive sense (set of all primes dividing any term) is FALSE; only the *essential* prime set stabilizes. This distinction is load-bearing and easy to get wrong.

### Hard steps a builder will face
1. **Proving the essential-prime set is eventually bounded** (the crux gap of opening 4). The "free riders can be infinite" note shows the naive stabilization fails; the right invariant is the transversal family on essential primes. A min-of-set monovariant (aimo-0678 style) or a divisor-chain stabilization (aimo-0477 style) is the candidate, but neither is automatic — this is where the proof lives or dies.
2. **Lifting residue-periodicity to value-translation-periodicity.** Once residues mod L cycle with period T, the greedy "smallest integer > a_n in the next valid residue" must produce gaps summing to exactly L over one period. This needs the validity pattern to be a *cycle of residues* (not just a set), and needs every valid residue to actually be hit. Plausible but must be proved, not asserted.
3. **Defining "essential prime" cleanly without circularity.** The natural definition "p is essential for a_n iff some earlier a_i has P(a_i)∩P(a_n)={p}" is workable but the outliner must verify it supports the stabilization argument.
4. **Covering the T=1 sub-case cleanly** as a corollary (pure-prime-power appearance) without making it the main load-bearing claim — otherwise the multi-prime starts (15,35,77,105) break the proof.
5. **No skipped cases:** the outliner must handle (a) starts that collapse to T=1, (b) starts that enter multi-prime regime, and (c) verify the transversal-stabilization step covers both uniformly.

### Most promising opening
Opening 4 (transversal-family stabilization → finite-state mod L → translation-periodic) is the natural main argument; opening 5 (min-of-set monovariant) is the most likely way to close its crux gap (bounding the essential primes). Opening 2 is the correct *target shape* (general T, L=∏S), and opening 1 is a terminal sub-case to fold in, not the main line.
