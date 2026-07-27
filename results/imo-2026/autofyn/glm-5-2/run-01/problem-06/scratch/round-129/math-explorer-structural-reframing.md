## imo-2026-06 — STRUCTURAL / COMBINATORIAL reframe of the saturated-regime wall

Lens: structural termination via intersecting-antichain + greedy-refinement dynamics, deliberately NOT routing through "bound entering primes by value / SPT."

### Distinct openings (the angles surfaced)

1. **p*-core / straggler decomposition (the one genuinely-different framing that is ALIVE).** In every saturated seed probed (15, 35, 77, 105, 143, 175, 323, 4199, 5005, 1001, 1155, 1365, 2145, 385; ~14 saturated seeds), the final family splits as
   `straggler(s) ∪ core`, where `p* = min(∪M) = 2` (always 2 for odd a_1), the **core** = `{M ∈ M : 2 ∈ M}` collapses to a **2-star** `{{2,p} : p ∈ S}` with `S ⊆ P(a_1)`, and the **straggler** is `P(a_1)` (or a refinement of it) — a minimal NOT containing 2. Examples: a_1=5005 → straggler {5,7,11,13}, core {{2,5},{2,7},{2,11},{2,13}}; a_1=1155=3·5·7·11 → straggler {3,5,7,11}, core {{2,3},{2,5},{2,7},{2,11}}; a_1=2145 → same pattern over P(a_1). For squarefree odd a_1 with ≥3 prime factors, `S = P(a_1)` exactly (conjecture, 6/6). The star + straggler is **self-blocking** (verified): any transversal either uses 2 (misses the straggler) or uses ≥1 straggler-prime, and picking all straggler-primes reproduces the straggler member itself; any {2,p} subset is a member. Self-blocking ⟹ frozen (certified `Sat-criterion`). **This framing bounds the CRASH primes (drawn from P(a_1), bounded by a_1's factorization) and treats the entering large primes (167, 179, 503, …) as FREE-RIDERS that are evicted by crashes, never persisting. It does NOT bound entering primes by value.** That is the genuine diversification from SPT.

2. **Crash = smooth-number event (value-dependent; the hard step).** Every crash (a promotion with `removed ≥ 2`) lands at a **smooth number** with ≤3 distinct prime factors and high exponents: 2^a·p^b (e.g. 5120=2^10·5, 5324=2^2·11^3, 5408=2^5·13^2, 5488=2^4·7^3, 4352=2^8·17, 1458=2·3^6, 243=3^5, 2304=2^8·3^2, 2662=2·11^3) and occasionally 2^a·3^b·7^c (5292, 2268). The crash support is `{2,p}` with `p ∈ P(a_1)` in the FINAL crashes (intermediate crashes may use a small entering prime like 3, but the terminal star is over P(a_1)). So the crash primes are bounded by `a_1`; the entering large primes are not. The hard step is proving a crash `{2,p}` (p∈P(a_1)) eventually arrives — this is a smooth-number / gap-bound argument, NOT a pigeonhole-on-transversal argument.

3. **Refinement well-foundedness / multiset-of-sizes (DEAD — honest negative finding).** The Dershowitz–Manna multiset of member sizes `{|M| : M ∈ M_n}` is NOT a monovariant: incomparable adds (new minimal incomparable to all existing) grow it, and they dominate. Counts on a_1=5005: 50 incomparable adds vs 5 crashes; |M| grows to 31 before the final crash to 5. The multiset strictly decreases ONLY at crashes. So no well-founded multiset measure on the family exists without already knowing crashes occur. **Dickson's lemma is defeated exactly here**: over a FIXED prime universe of size k, the antichain M_n ⊆ {0,1}^k cannot be infinite (WQO) → stabilizes; but the universe grows via incomparable adds carrying fresh large free-rider primes, so k is unbounded and Dickson does not apply. The greedy's smallest-first does NOT close this gap structurally — it closes it only via the gap bound `a_{n+1}-a_n ≤ mtp` feeding into smooth-number density, i.e. value-dependently.

4. **τ (min transversal cardinality) ceiling (DEAD — honest negative).** τ(M_n) is monotone non-decreasing (Trans(M_{n+1}) ⊆ Trans(M_n), certified). But τ is NOT structurally bounded for pairwise-intersecting antichains in general: projective planes of order q give pairwise-intersecting antichains (lines) with τ = q+1, unbounded. So no static Helly/Sperner/EKR theorem bounds τ without the greedy generation. minAvSz is likewise not a lattice formality (round-3 memory confirmed Avoid(M_{n+1})⊄Avoid(M_n)); the probe confirms nAvail oscillates (5005: 1128 then drops to 4 at the crash). No value-free transversal-cardinality monovariant exists.

5. **Refinement depth (trivially useless).** Since M_n is an ANTICHAIN (members are inclusion-incomparable), the longest strict-inclusion chain among members is always 1. rdepth=1 throughout every seed. Not a measure.

### Where the unbounded universe defeats naive WQO, and whether smallest-first repairs it

Dickson fails because the universe of primes in minimals grows without bound via incomparable adds of `{2, q, large_free_rider}` (e.g. 5005 sees primes 167, 179, 193, 251, 359, 503, 509, … in minimals). Smallest-first does NOT repair this by pure combinatorics. What smallest-first DOES give is (i) the mtp gap bound (certified `mtp-monovariant-and-gap-bound`) and (ii) the fact that the CRASH pick is the smallest valid candidate, which lands on smooth numbers 2^k·p. Both are value-dependent. So the repair is value-dependent — pure structural WQO does not close the gap.

### Candidate technique(s)

- **Subfamily / restricted-common-prime freeze.** Apply `freeze-lock`-style reasoning NOT to the whole M_n (which needs a globally common prime — that's the freeze regime, solved) but to the CORE subfamily `M_n^* = {M∈M_n : 2∈M}`, where 2 IS common. The core undergoes a freeze-like collapse to a 2-star, while the straggler (lacking 2) survives. The terminal self-blocking star+straggler is the saturated analogue of the singleton freeze.
- **Smooth-number / perfect-power density** for the crash step (the field's round-3 "analytic crash" bucket): prove 2^k·p (p∈P(a_1)) is eventually the greedy pick. The gap bound `a_{n+1}-a_n ≤ mtp(M_n)` plus the fact that 2 is common to the core (so powers of 2 times a straggler-prime are valid candidates once {2,p} is a transversal) is the engine.
- **Dershowitz–Manna multiset termination** is the RIGHT template conceptually but FAILS here (incomparable adds grow the multiset); record as a negative so the outliner doesn't build on it.

### Cheap-kill candidates

- **Immediate 2-entry for odd a_1**: for odd a_1 with ≥2 prime factors, a_2 is even (smallest valid > odd is even), so 2 ∈ P(a_2) enters at step 2; 2 then becomes common to the core. This prunes to "2 enters, core forms" with zero work. (For even a_1 or prime-power a_1: freeze/singleton-freeze, already solved — `singleton-freeze`, `freeze-lock`.)
- **Star + straggler is self-blocking** is a cheap structural verification: with straggler S and core {{2,p}:p∈S}, every transversal contains a member (verified on all saturated finals). So the terminal config, once reached, freezes — no heavy machinery for the freeze step.
- **Free-rider eviction**: every entering large prime q appears only in core minimals `{2,q,…}` that are strict supersets of the eventual `{2,p}` crash member; once {2,p} arrives (p the small partner), all `{2,q,…}` are refined away. So the large primes never persist — they are provably evicted by the crash, NOT bounded by value. (This is the structural fact that lets the framing avoid SPT.)

### Knowledge-base entries to use

- `Invariants & monovariants` (the mtp monovariant is the certified instance; the multiset-order idea is the failed cousin — note the failure).
- `Pigeonhole / extremal` (for the crash-step: the star's primes are pigeonhole-bounded by |P(a_1)|, NOT by prime value).
- `Induction / structural` + `Infinite descent` (the core-collapse is a descent of the core's "2-star coverage" measure: as crashes {2,p} accumulate, the set of straggler-primes p already covered grows monotonically to all of P(a_1) — THIS is a genuine monotone quantity: `Cov(M_n) = {p ∈ P(a_1) : {2,p} ∈ M_n}`, the set of straggler-primes already crashed into the core. Cov is monotone non-decreasing and bounded above by P(a_1); once Cov = P(a_1), the star is complete and self-blocking ⟹ freeze. THIS IS THE VALUE-FREE MONOVARIANT THE LENS ASKED FOR — but it bounds the crash primes, not the entering primes.)
- General `monovariant → bounded → stabilizes` (knowledge_base *Invariants & monovariants*): Cov is a bounded monotone integer-quantity (a subset of the finite set P(a_1)), so it stabilizes.

### Analogous past problems (cruxes)

- `aimo-0678` (NT, size-bounding-and-descent + modular) — the lcm-reduction finite-state template; already the carrier for γ's GAP-3. The crash-step here is the missing "a_n | M" analogue; the Cov-monovariant + star-completion is a cleaner finite-state collapse than γ's residue window because Cov only ranges over subsets of P(a_1) (finite by construction).
- `aimo-0193` (combinatorics, invariants-and-monovariants: "cap the strictly-increasing monovariant by identifying the maximum") — the Cov-monovariant is capped by |P(a_1)| exactly this way: monotone, integer-valued, bounded above, hence stabilizes.
- No crux in the corpus uses WQO/Dickson/Higman (verified by search: 0 hits) — so the Dickson route is NOT a mined move; the failure here is consistent with the corpus having no such template.

### Prior progress

- **Best reusable asset**: `mtp-monovariant-and-gap-bound` (γ, certified) — the gap bound `a_{n+1}-a_n ≤ mtp(M_n)` is the value-side input the crash step needs (to argue 2^k·p is reachable in bounded steps).
- **Best structural asset for THIS framing**: `Sat-criterion` (self-blocking ⟹ frozen) + `pairwise-intersection` (M_n pairwise intersecting). The star+straggler terminal config is self-blocking, so reaching it freezes.
- Freeze regime SOLVED (α r2); the p*-core framing leaves the freeze branch untouched and attacks ONLY the saturated branch via the Cov-monovariant + crash-into-core.

### Dead ends (do not retry)

- **Dershowitz–Manna multiset of member sizes** as a global monovariant — FAILS: incomparable adds grow it (50 vs 5 on 5005). Not a monovariant. Do not build on it.
- **τ (min transversal cardinality) as a structurally-bounded ceiling** — FAILS: projective planes give unbounded-τ pairwise-intersecting antichains; no static bound. Only the greedy bounds it, value-dependently.
- **Refinement depth / longest inclusion chain among M_n** — trivially 1 (antichain). Useless.
- **"Saturated |M| ≤ 7"** (round-3 small-seed observation) — REFUTED: a_1=5005 reaches |M|=31 before crashing. The bound on |M| is not 7; it grows with |P(a_1)| and the transient. Do not assert a small constant cap.
- **Pure WQO / Dickson on the prime universe** — FAILS: universe unbounded (free-rider primes 167…509 enter). The greedy's smallest-first does not repair this structurally.
- **minAvSz monotonicity as a lattice formality** — confirmed NOT (round 3); nAvail oscillates. Do not assert it descends.

### Small-case / intuition notes (CONJECTURE, evidence not proof)

- **CONJECTURE (core-star):** for odd squarefree a_1 with ≥3 prime factors, the saturated regime terminates with `M = {P(a_1)} ∪ {{2,p} : p ∈ P(a_1)}` (star over all of P(a_1)). 6/6 on {105,1001,1155,1365,2145,5005}; the straggler is exactly P(a_1) (un-refined). For 2-prime a_1 the terminal is the triangle {P(a_1),{2,p},{2,q}}.
- **CONJECTURE (Cov monovariant):** `Cov(M_n) = {p ∈ P(a_1) : {2,p} ∈ M_n}` is monotone non-decreasing (once {2,p} enters the core it is never refined — {2,p} has no proper nonempty subset that is a transversal-avoiding-the-rest EXCEPT {2} or {p}, and {2} would be a singleton freeze while {p} would require p common). Plausible but UNCHECKED for monotonicity across all steps — the outliner must prove {2,p} persists once it enters. If true, Cov stabilizes at ⊆P(a_1) in ≤|P(a_1)| crashes, giving the freeze.
- **CONJECTURE (crash inevitability):** the crash {2,p} (p∈P(a_1)) arrives because, with 2 common to the core and p in the straggler, `{2,p}` is a transversal of M_n, so multiples of 2p are valid; the smallest such above a_n is ≤ a_n + 2p ≤ a_n + mtp, and the specific pick 2^k·p (a pure smooth number) is forced when intermediate candidates are all dominated. This is the unproven hard step; it is value-dependent (smooth-number existence) but bounds CRASH primes, not entering primes.
- **The entering large primes are free-riders, universally evicted** (14 seeds, 0 violations): every prime q > max P(a_1) entering a minimal enters as `{2,q,…}` and is evicted when a {2,p} crash (p∈P(a_1)∪{small}) refines it. So the framing's claim "entering primes need not be bounded" is empirically solid.

### Verdict for the outliner

**A genuinely-different structural framing IS alive: the p*-core collapse with the Cov monovariant.** It attacks the saturated wall by proving the CORE (subfamily containing 2) collapses to a 2-star over P(a_1) — a freeze-like restricted-common-prime argument — while the straggler P(a_1) survives and the star+straggler is self-blocking. It bounds the CRASH primes (⊆P(a_1), finite by construction) and the Cov-monovariant, NOT the entering large primes (which are evicted free-riders). This is a real diversification at the CRASH step (the outliner's round-3 single-gap-trap guard): crash-via-Cov-monovariant + star-completion is distinct from SPT-density (α), permanent-transversal (β), mtp-pigeonhole (γ GAP-1), and finite-state-lcm (γ GAP-3).

**Honest caveat (the framing does NOT escape value entirely):** the crash-inevitability step still needs a smooth-number argument (2^k·p is the greedy pick). Pure-combinatorial measures (multiset, τ, refinement-depth) all collapse — I verified each fails. So the structural framing's hard step is "smooth-number crash is forced," which is the round-3 "analytic crash" bucket, now with a clean monovariant (Cov) capping how many crashes suffice (≤|P(a_1)|). The convergence of the field onto "some value/smooth-number argument at the crash" is REAL, not an artifact; what this lens adds is the bounded CRASH-PRIME set (P(a_1)) and the Cov monovariant, which replace "bound entering primes by value" with "bound crash primes by a_1's factorization + bound crash count by |P(a_1)|."

**Skeleton for the outliner (pointer, not a plan):**
- Lemma A (2-entry): for odd a_1 with ≥2 prime factors, 2 ∈ P(a_2) and the core M_n^* = {M∈M_n:2∈M} is nonempty from n≥2; 2 is common to M_n^* forever (conjecture — prove: a new core minimal is a transversal of M_{n-1}^*? needs check).
- Lemma B (Cov monovariant): Cov(M_n) = {p∈P(a_1):{2,p}∈M_n} is monotone non-decreasing and ⊆P(a_1); the hard sub-step is proving {2,p} persists once entered (no refinement of {2,p} except singleton-{2} or {p}, which are freeze events).
- Lemma C (crash inevitability — HARD, value-dependent): so long as Cov ≠ P(a_1), a crash {2,p} for some p∈P(a_1)\Cov eventually arrives. This is the smooth-number step; uses the mtp gap bound + 2 common to core + p in straggler ⟹ {2,p} transversal ⟹ 2^k·p valid ⟹ eventually picked.
- Lemma D (terminal freeze): Cov = P(a_1) ⟹ M = {straggler} ∪ {{2,p}:p∈P(a_1)} is self-blocking ⟹ `Sat-criterion` ⟹ frozen ⟹ `post-stabilization-theorem`.
- The wall is Lemma C; A,B,D are structural and cheap. The framing dies iff Lemma C (smooth-number crash forced) is unprovable — but that is a DIFFERENT hard step from SPT, so it does not die together with α/β/γ.
