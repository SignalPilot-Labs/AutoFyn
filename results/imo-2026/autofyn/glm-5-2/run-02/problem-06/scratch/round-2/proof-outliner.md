## imo-2026-06

**Context (from the 3 round-2 explorers + R1 reviewer):** The round-1 field collapsed to ONE crux — **Lemma 4**: every pair of terms a_i, a_j (i<j) shares a prime ≤ R := rad(a_1). It is equivalent to E ⊆ Q_R (essential primes finite) and to the free-rider dichotomy. The consecutive case is PROVED (gap bound ⟹ shared prime ≤ R). The non-consecutive case is the open 9/10 crux. essential-monovariant already has Lemmas 1,2,3 + the full translation-periodicity Theorem PROVED conditional on Lemma 4. crude-reduced-type has Steps 1–6 certified-correct but un-built. The three round-2 explorers CONVERGED on a hard truth: **no framing escapes the crux** (it is a real structural fact, not an artifact of one framing). So the diversity mandate is satisfied by fielding **genuinely different PROOF ROUTES to the crux itself** — descent+transversal (Route D), propagation (Route P), grid-counting (Route G) — not by re-framing the whole problem. The dispatch resolves the overlap between the crux-descent explorer's "new `crux-descent`" and the alt-framing explorer's "new `descent-coprime-shift`" (same route family) by absorbing Route D INTO essential-monovariant as its named Lemma-4 attack — avoiding the single-gap trap of two descent approaches.

**Free partial lemma (from crux-descent explorer, verified numerically for a_1 ∈ {15,35,77,105}):** *If a_j is a multiple of R = rad(a_1), then (a_i, a_j) satisfies Lemma 4 for every i < j.* Proof: a_j mult of R ⟹ every prime of a_1 divides a_j; by Lemma 1 a_i has a prime q ∈ P(a_1) ⊆ Q_R; q | R | a_j and q | a_i ⟹ shared small prime. Corollary: any counterexample to Lemma 4 has a_j mod R ≠ 0. This is certified-into-`lemmas/` material this round.

---

### essential-monovariant: advance (with named crux route)
Target: the whole theorem (∃ T,L>0 with a_{n+T}=a_n+L for all n≥1) — Lemma 4 ⟹ Theorem (Section 5, already proved conditional); now the gap Lemma 4 gets a NAMED attack.
Technique: gap-bound monovariant (Lemma 2, proved) + finite-state mod L_0 (Theorem, conditional, proved) + **descent + stripped-auxiliary-transversal attack on Lemma 4** (Route D, NEW — aimo-0030 spirit, adapted).
Skeleton:
  1. Lemma 1 (every term divisible by a prime of a_1) — PROVED.
  2. Lemma 2 (gap bound a_{n+1}−a_n ≤ R) — PROVED (next-multiple-of-R candidate).
  3. Lemma 3 (consecutive terms share only primes ≤ R) — PROVED (shared prime divides the gap ≤ R).
  4. Lemma 4 (crux: every pair shares a prime ≤ R) — [GAP], NOW ATTACKED by Route D below.
  5. Theorem (Lemma 4 ⟹ a_{n+T}=a_n+L_0 for all n≥1, no transient) — PROVED conditional.
Route D attack on Lemma 4 (the named gap-fill the builder attempts):
  4a. Minimal-counterexample: let (a_i, a_j), i<j−1, be a lexicographically-minimal pair sharing only primes >R (consecutive pairs are Lemma 3). By the free partial lemma, a_j mod R ≠ 0.
  4b. Stripped auxiliary: build x ≤ a_i carrying exactly a_i's small-prime signature τ(a_i) (no big primes), ARMED as a transversal of the seen small-prime type family F_{j−1} (so x hits every a_k, k<j, via a small prime — admissible at stage j−1).
  4c. CRT coprime-shift: for each large prime p | a_j (p>R, hence gcd(p,L_0)=1), p | x forbids ONE residue of the shift multiplier mod p; pigeonhole gives a shift k ≤ |P_large(a_j)|+1 ≤ O(log a_j) avoiding all large primes, so the shifted x + k·L_0 is still admissible at stage j−1, coprime to a_j, and > a_{j−1} (L_0 large).
  4d. Contradiction: x+k·L_0 ∈ (a_{j−1}, a_j) admissible ⟹ a_j not greedy-minimal ⟹ contradiction.
Key lemmas (claim + one-line mechanism that makes it true):
  - Lemma 4b transversal-stripped-auxiliary: x = (∏_{p∈τ(a_i)} p)·(powers) ≤ a_i carrying τ(a_i) and no big primes — because τ(a_i) ⊆ Q_R and removing a_i's big-prime cofactors leaves the small-prime part. **TENSION:** making x a transversal of F_{j−1} may require MORE small primes than τ(a_i) carries (a pair-witness enlargement), which can push x > a_i. This is the central load-bearing sub-step.
  - Lemma 4c CRT-coprime-shift: each large prime p|a_j forbids one residue of the multiplier mod p (p ∤ L_0 since p>R) — by CRT/pigeonhole a good multiplier ≤ |P_large|+1 exists (verified on synthetic failure a_i=2·3·107, a_j=5·7·107, R=105: k=1 works).
  - Free partial lemma (multiple-of-R ⟹ Lemma 4 for (a_i,a_j)) — mechanism: a_j mult of R ⟹ every prime of a_1 divides a_j; Lemma 1 gives a_i a prime of a_1; shared. **Certify into `lemmas/multiple-of-r-satisfies-lemma-4.md`.**
Open gaps: Step 4b/4d — the stripped-auxiliary may not be a transversal of F_{j−1} without enlargement that breaks x ≤ a_i; the CRT bound gives a finite bound on the first failure (j_0 ≤ O(L_0 log L_0)) — a finite reduction, NOT yet a contradiction. The second independent constraint on (i_0,j_0) (conflicting with the size bound) is the missing lever.
Cases to cover: none new (T=1 sub-cases auto-handled by the general Theorem).
Watch out for: the aimo-0030 descent uses a game's "bad ⇒ move to good" rule P6 lacks; the P6-native replacement is greedy minimality (x < a_j admissible ⟹ a_j not minimal). The transversal enlargement vs x ≤ a_i tension is the real wall — do NOT assert it resolves; the builder must either resolve it or report the precise obstruction.
Builds on: essential-monovariant (Lemmas 1,2,3, Theorem — all certified), aimo-0030 descent scaffold (imported), free multiple-of-R partial lemma.
What the builder should attempt this round (bounded): attempt the stripped-auxiliary-transversal descent (Steps 4a–4d); (a) certify the multiple-of-R partial lemma into `lemmas/`; (b) if the descent cannot close, write the SHARPEST partial — the CRT finite bound on j_0, the precise obstruction (where transversal enlargement breaks x ≤ a_i), and the bridge 4-cycle a_i—(small)—a_{j−1}—(small)—a_j—(large)—a_i as the structural lever to hunt for the second constraint.

---

### crude-reduced-type: advance (build out the certified scaffold)
Target: the whole theorem (∃ T,L>0 with a_{n+T}=a_n+L for all n≥1).
Technique: finite-lattice stabilization (Steps 1–6, R1 reviewer "standard and correct") + free-rider wall (Step 7 = Lemma 4, the shared crux, INHERITED) + cyclic-permutation residue walk (Steps 8–10, mirror essential-monovariant's Theorem).
Skeleton:
  1. Cheap bound: every a_n (n≥2) has a prime factor p | a_1, hence p ≤ a_1 — by gcd(a_n,a_1)>1 (greedy).
  2. Reduced types r_n = P(a_n)∩Q (Q = primes ≤ a_1) live in the finite lattice 2^Q \ {∅} — by finiteness of Q.
  3. Seen-type family F_n = {r_i : i≤n} stabilizes: F_n = F for n≥N — monotone-increasing on finite 2^Q.
  4. Transversal family H_n = {transversals of F_n} stabilizes: H_n = H for n≥N' — nested-decreasing on finite 2^Q.
  5. Fixed valid-residue set V_0 = {r ∈ {0,…,L_0−1} : P(r)∩Q ∈ H} mod L_0 = ∏_{p∈Q} p — by definition; H fixed from Step 4.
  6. Post-stabilization, a_{n+1} mod L_0 ∈ V_0 — the greedy m=a_{n+1} must hit every earlier a_i, so r(m) is a transversal of F ⊇ F_n, i.e. r(m)∈H, i.e. residue ∈ V_0.
  7. FREE-RIDER WALL [GAP = Lemma 4]: a_{n+1} = min{m>a_n : m mod L_0 ∈ V_0}. Equivalently NO m in (a_n, next-V_0-residue) is admissible via a free-rider prime >R. This is exactly the free-rider dichotomy = Lemma 4 (imported from essential-monovariant's attack). crude-reduced-type does NOT independently prove Lemma 4; it INHERITS it.
  8. Deterministic residue walk: φ:V_0→V_0 (cyclic successor in natural order, wrapping by +L_0) — well-defined once Step 7 holds.
  9. Cyclic-permutation periodicity: φ is the cyclic successor on the finite ordered subset V_0 ⟹ bijection ⟹ single orbit of length T=|V_0| ⟹ r_{n+T}=r_n for all n≥1 (NO transient — the orbit is purely periodic from a_1's state, since φ is a bijection).
  10. Lift: sum of value-gaps over one cycle telescopes to L_0 (wraps exactly once) ⟹ a_{n+T}=a_n+L_0 for all n≥1. Set L=L_0, T=|V_0|.
Key lemmas (claim + one-line mechanism that makes it true):
  - Lemma B (stabilization): F_n monotone-increasing, H_n monotone-decreasing on finite 2^Q ⟹ both stabilize — by monotone-bounded-on-finite.
  - Lemma C (free-rider wall = Lemma 4): a free-rider prime q>R is never the unique shared prime of any pair — because (Lemma 4) every pair already shares a small prime ≤R. This is the inherited crux; the R1 reviewer's "route (b)" cleaner formulation (prove the dichotomy directly) is Lemma 4 in disguise — do NOT claim it as independent.
  - Lemma (cyclic permutation ⟹ no transient): φ is a bijection on V_0, so the orbit is purely periodic from n=1 (no tail) — this is the R1 reviewer's defusing of the "for all n" ambiguity; add as an explicit step.
Open gaps: Step 7 (free-rider wall = Lemma 4, the shared crux) — INHERITED, not independently closed by this approach. Step 10 (gap-sum = L_0 over one cycle, wraps exactly once) — verify.
Cases to cover: even a_1 / prime-power a_1 (T=1, V_0 collapses to one residue) auto-handled; generic case = odd squarefree ≥2 prime factors.
Watch out for: Q = primes ≤ a_1 (NOT just primes dividing a_1 — too coarse, drops 2 for odd a_1=15). L_0 astronomically large; finiteness is all Step 9 needs. The frozen-prefix regress (re-stabilize over larger Q ⟹ larger N'' ⟹ larger B ⟹ larger Q) terminates ONLY because E is finite — so route (a) (frozen-prefix bound) is somewhat circular; use route (b) (direct dichotomy = Lemma 4 inherited) instead.
Builds on: crude-reduced-type (Steps 1–6 certified-correct per R1 reviewer), essential-monovariant (Lemmas 1,2,3 + Theorem structure, for the conditional Step 7 + Steps 8–10).
What the builder should attempt this round (bounded): write Steps 1–6 RIGOROUSLY (the certified scaffold, full proofs); state Step 7 as the explicit free-rider wall gap (= Lemma 4, imported); add Steps 8–10 (deterministic walk + cyclic-permutation-no-transient + telescoping lift) mirroring essential-monovariant's Theorem. Output: a second complete conditional-on-crux proof, with the free-rider wall as the single marked [GAP].

---

### propagation-bezout: new
Target: the whole theorem — Lemma 4 ⟹ inherit essential-monovariant's Theorem (Section 5); this approach attacks Lemma 4 by PROPAGATION, not descent.
Technique: propagation of small-prime sharing from the consecutive seed via Bezout-style composition of index-shifts (aimo-0648 crux (ii) extremal-forces-equality + crux (iii) Bezout-composition-of-index-shifts). Genuinely different mechanism from descent (Route D) and counting (Route G).
Skeleton:
  1. Inherit Lemmas 1,2,3 (gap bound, consecutive-only-small) from essential-monovariant — certified.
  2. Consecutive seed: every consecutive pair (a_n, a_{n+1}) shares a small prime ≤ R (Lemma 3). So "shift-by-1" preserves small-prime sharing.
  3. Extremal-forces-equality (aimo-0648 (ii)): suppose a_{n+1} is the minimal admissible and hits some a_i (i<n) ONLY via a large prime p>R. Then every "cheaper" candidate hitting a_i via a small prime must fail admissibility against some other term — forcing a structural tension. Lemma 3 breaks the tension: at least one partner (the consecutive a_{n−1} or a_{n+1}) is hit by a small prime, giving a SEED of small-prime sharing.
  4. Bezout-propagation (aimo-0648 (iii)): compose index-shifts. The consecutive small-prime sharing gives shifts of size 1. If "small-prime sharing between a_i and a_{i+k}" is invariant under some composition of shifts whose gcd is 1, then Bezout extends it from shift 1 to every shift k ≥ 1 — yielding Lemma 4 for all non-consecutive pairs.
  5. Inherit essential-monovariant's Theorem (Lemma 4 ⟹ a_{n+T}=a_n+L for all n≥1).
Key lemmas (claim + one-line mechanism that makes it true):
  - Consecutive-seed (Lemma 3, inherited): consecutive pairs share a small prime — by the gap bound.
  - Shift-composition invariance: "a_i and a_{i+k} share a small prime" is preserved under composition of shifts — mechanism: the greedy's translation-equivariance after the gap bound makes index-shifts compose like integer additions. **THIS IS THE LOAD-BEARING AND SPECULATIVE STEP.**
Open gaps: Step 4 (Bezout-propagation) — the central gap. The aimo-0648 move composes FLOOR-AVERAGE recurrence shifts (a linear recurrence); P6's greedy has no such linear recurrence. The "index-shift composition" needs a P6-native mechanism, and the only natural one is the residue-walk map φ from essential-monovariant's Theorem — but φ is defined via Lemma 4, making the propagation CIRCULAR as a proof of Lemma 4. The builder must determine whether a pre-Lemma-4 shift algebra exists.
Cases to cover: T=1 sub-cases (trivial propagation); generic odd squarefree a_1.
Watch out for: CIRCULARITY is the central risk — the Bezout composition likely needs the residue-walk structure (Lemma 4) to define the shift algebra, making propagation a reformulation rather than an independent proof. Do NOT assert the composition is closed without proving the algebra pre-exists Lemma 4. The aimo-0648 (ii) "extremal-forces-equality" lever is the genuinely portable intuition; the (iii) Bezout step may not port.
Builds on: essential-monovariant (Lemmas 1,2,3, Theorem — all certified), aimo-0648 crux (ii)+(iii) (imported as the propagation scaffold).
What the builder should attempt this round (bounded): write the skeleton (Steps 1–5); identify PRECISELY where the Bezout-composition needs the residue-walk structure (= Lemma 4) and whether a pre-Lemma-4 shift algebra can be defined (e.g. via the gap-bound window alone). If circular, report the obstruction honestly — the propagation framing is still a genuinely different angle worth one builder round, and the extremal-forces-equality sub-lemma (Step 3) may yield a partial result even if the full propagation fails.

---

### grid-counting-shared-primes: new
Target: the whole theorem — Lemma 4 ⟹ inherit essential-monovariant's Theorem; this approach attacks Lemma 4 by COUNTING, not descent or propagation.
Technique: grid-covering counting (aimo-0447): form the (i,j) grid of shared primes P(a_i)∩P(a_j); bound cells-per-prime; large primes > span divide at most one term ⟹ cover zero shared cells; small primes cover the rest; double-count to force pairwise small-prime intersection.
Skeleton:
  1. Fix the first N terms a_1,…,a_N. By the gap bound (Lemma 2), they lie in an interval of length ≤ (N−1)·R.
  2. Form the N(N−1)/2 off-diagonal cells; cell (i,j) carries the shared primes P(a_i)∩P(a_j).
  3. Cells-per-prime bound (aimo-0447 port): a prime p divides a_i for ≤ ⌈(N−1)R/p⌉ + 1 of the first N terms (a_1,…,a_N lie in an interval of length (N−1)R; p divides at most ⌈span/p⌉+1 of them). So p covers ≤ (⌈(N−1)R/p⌉+1)² shared cells.
  4. Large-prime-span lemma (CLEAN, PROVABLE): if p > (N−1)·R (the span), then p divides AT MOST ONE of a_1,…,a_N — because two terms divisible by p would have difference a multiple of p but |difference| ≤ span < p ⟹ difference = 0. So a large prime p > span covers ZERO shared cells (it divides one term, so it is not shared by any pair).
  5. Small-prime cell-count bound: sum over primes p ≤ (N−1)R of (⌈(N−1)R/p⌉+1)². Use Σ 1/p² < 1/2 (Euler product; aimo-0447 uses Σ1/p² < 1/2 + PNT for lower-order terms) to bound the small-prime cell coverage < ½·(number of cells) + O(N).
  6. Double-count: total off-diagonal cells = N(N−1)/2. Every cell is covered by ≥1 prime (greedy ⟹ every pair shares SOME prime). Large primes (> span) cover 0; small primes (≤ span) cover < ½·N(N−1)/2 + O(N). **GAP:** the count does not force EVERY cell to be small-prime-covered; it only bounds the aggregate.
  7. Inherit essential-monovariant's Theorem (Lemma 4 ⟹ conclusion).
Key lemmas (claim + one-line mechanism that makes it true):
  - Large-prime-span lemma (Step 4): a prime p > span divides at most one term — because two terms divisible by p have difference a nonzero multiple of p, but |difference| ≤ span < p. **CLEAN, PROVABLE** (verified: for a_1=15, N=40, span=147, zero big primes > span divide >1 term).
  - Small-prime coverage bound (Step 5): Σ_{p≤span} (span/p+1)² ≤ span²·Σ1/p² + 2·span·Σ1/p + π(span) — by Euler product / partial sums; aimo-0447 uses Σ1/p² < 1/2.
Open gaps: Step 6 (double-count forces pairwise small-prime) — the CENTRAL GAP. aimo-0447's "large prime > interval length" gives large = > (N−1)R (GROWS with N), NOT > R. So the counting shows every pair shares a prime ≤ (N−1)R (a growing window), NOT ≤ R (the fixed Lemma 4 bound). To get Lemma 4 (≤ R), the threshold must shrink from (N−1)R to R — which is exactly the free-rider dichotomy (the shared crux). Also Step 5's Σ1/p² < ½ bound is heavy analytic number theory (Euler product); knowledge_base has no Jacobsthal/Siegel — must re-prove or import carefully.
Cases to cover: T=1 sub-cases (grid trivially all cells small); generic odd squarefree a_1.
Watch out for: the GROWING-WINDOW problem is the fatal gap — counting gives ≤ (N−1)R, not ≤ R. Do NOT claim the grid proves Lemma 4 for the fixed R; it proves a weaker growing-window version. The aimo-0447 conclusion (min{a,b} > (cn)^{n/2}) is a LOWER bound on term size, not a pairwise-small-prime claim — the adaptation is non-trivial and may not close. Σ1/p² < ½ is analytic; flag the heaviness.
Builds on: essential-monovariant (Lemmas 1,2 — gap bound gives the span bound; Theorem — inherited), aimo-0447 grid-covering crux (imported as the counting scaffold).
What the builder should attempt this round (bounded): write the skeleton (Steps 1–7); PROVE the large-prime-span lemma (Step 4, the clean sound part); state the central gap explicitly (Step 6: the threshold is (N−1)R, not R; counting gives a growing-window Lemma-4-analogue, not the fixed-R Lemma 4). Report honestly whether the counting can be sharpened to the fixed R (likely: only via the free-rider dichotomy = the crux itself), and whether the aggregate-coverage bound can be turned into a per-cell forcing (likely: no, aggregate bounds do not force per-cell coverage).

---

### translation-self-similarity: dormant (recommend merge-as-lemma if Lemma 4 closes)
### covering-system-redundancy: dormant (recommend merge-as-lemma if Lemma 4 closes)
Recommendation: leave BOTH dormant this round (no builder slot). R1 reviewer flagged translation-self-similarity's literal set-translation as FALSE (concrete counterexample: a_1=15, T=8, L=30, the candidate 51=30+21 ∈ 30+A_1 but coprime to a_3=20, so 51 ∉ A_9); the weakened "min-preservation" reduces to Lemma 4. R1 reviewer flagged covering-system-redundancy's "redundancy of late primes" as exactly the free-rider dichotomy = Lemma 4 (same wall as crude-reduced-type, restated in covering vocabulary). The alt-framing explorer confirms: DO NOT re-field either — both reduce to the crux with no genuinely distinct mechanism. Do NOT revise to differentiate — the crux is a real structural fact (per the alt-framing explorer's hard finding), so no restatement escapes it. If Lemma 4 closes via any of the three live crux routes (descent, propagation, counting), both become IMMEDIATE COROLLARIES and should be MERGED as expository lemmas into the winning approach (their covering-language / symmetry-language may give a cleaner restatement of the free-rider dichotomy but are not separate proofs). Keep them registered (live in the ranker) so the reviewer can re-rank if a round-2 outcome changes the picture, but spend no builder slots here.

---

## Nomination summary

Field of rival approaches (4 active, 2 dormant):
- essential-monovariant — ADVANCE (named crux route: descent+stripped-auxiliary-transversal + multiple-of-R partial lemma). Best Elo, partial; keeps the population leader advancing with a concrete Lemma-4 attack.
- crude-reduced-type — ADVANCE (build Steps 1–6 rigorously + free-rider wall as explicit inherited gap + cyclic-permutation no-transient lift). Produces a second complete conditional-on-crux proof.
- propagation-bezout — NEW (Route P, aimo-0648 propagation from consecutive seed via Bezout index-shift composition). Genuinely different mechanism (propagation, not descent); central risk = circularity (shift algebra may need Lemma 4).
- grid-counting-shared-primes — NEW (Route G, aimo-0447 grid-covering counting). Genuinely different mechanism (counting, not descent or propagation); central gap = growing-window threshold (≤(N−1)R, not ≤R).
- translation-self-similarity — DORMANT (recommend merge-as-lemma if Lemma 4 closes).
- covering-system-redundancy — DORMANT (recommend merge-as-lemma if Lemma 4 closes).

Diversity check (the three crux routes are far apart in MECHANISM):
| Approach | Mechanism to attack Lemma 4 | Distinct engine |
|---|---|---|
| essential-monovariant (Route D) | minimal-counterexample descent + stripped-auxiliary-transversal + CRT coprime-shift | descent on a violating pair, greedy-minimality contradiction |
| propagation-bezout (Route P) | extremal-forces-equality + Bezout composition of index-shifts from the consecutive seed | propagation of a seed relation |
| grid-counting-shared-primes (Route G) | cells-per-prime double-counting + large-prime-divides-≤1-term | aggregate counting forces per-cell coverage |

No two share the mechanism. The two dormant approaches are restatements, not independent routes.

SUGGESTED build set (the outline-reviewer makes the final call):
build set: essential-monovariant, crude-reduced-type, propagation-bezout, grid-counting-shared-primes

(4 builders, one per slug. Each owns its own approach file, so parallel builds never collide. The set mixes two advances — one closing the leader's gap via a named route, one building out the certified scaffold — and two new genuinely-different-mechanism crux attacks. No copies this round: nothing is proven yet, so the copy mechanism has no certified shared prefix to branch from. The two dormant approaches stay registered for re-ranking but get no builder slot.)
