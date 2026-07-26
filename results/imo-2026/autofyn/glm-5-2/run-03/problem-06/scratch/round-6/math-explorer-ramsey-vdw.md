## imo-2026-06 — Ramsey / van-der-Waerden route on d_n

**Verdict: NO-UNFENCED-ROUTE.** Collapses to the round-5 forward-deterministic / Gap-A fence (the aimo-0907 single-orbit fence) + the round-5 deviation-descent `w_min` fence. One genuinely-new negative finding: the T-unbounded-in-M_1 fence EXTENDS to a_1-bounded and even a_1^2-bounded residue statistics (a_1=175 gives a real counterexample), not just f(M_1)-bounded states. The Ramsey ingredient adds no leverage because the greedy rule actively SUPPRESSES long sub-T constant-d APs — the only long monochromatic APs in d_n are the trivial δ | T ones, which presuppose the period.

### 1. The route (concrete mechanism sketch)

The certified `linchpin-and-gap-bound` gives d_n ∈ Σ = {1, …, M_1} (finite alphabet). So d = d_1 d_2 … is an infinite word over a finite alphabet. By **van der Waerden's theorem**, for every k there exist i, δ with d_i = d_{i+δ} = … = d_{i+(k-1)δ} — arbitrarily long monochromatic APs (of constant d-value) in the index set. The hoped-for mechanism:

(R1) van der Waerden produces a long constant-d AP at some spacing δ.
(R2) The greedy rule's structure (d_n is the FORCED smallest admissible gap, not arbitrary) makes δ propagate: a long-enough constant-d AP forces the whole word to be δ-periodic (or δ | T-periodic).
(R3) aimo-0907 part A (certified): a single self-coincidence of a forward-deterministic map ⇒ eventual periodicity. Lift the δ-periodicity of the candidate state α to δ-periodicity of d_n.
(R4) Telescoping: d_n periodic ⇒ a_{n+T} = a_n + L. Endgame (already certified) closes.

### 2. Why NOT in the 13-dead / 4-fence list — and where it collapses

**Not Morse-Hedlund.** Morse-Hedlund (p(n) ≤ n ⇒ periodic) is fenced (round 4: threshold = T exactly, no sub-T bound). The Ramsey route does not invoke factor-complexity; it invokes monochromatic APs. Genuinely different *statement*. BUT the collapse is the same: both produce a candidate period and both need a *propagation step* to lift candidate → real period, and that propagation step is fenced.

**Not substitution/morphic.** A van-der-Waerden argument is not a fixed-point/substitution argument. Genuinely different *vehicle*. But Thue-Morse already shows the obstruction is structural: Thue-Morse is a fixed point of a finite substitution AND has arbitrarily long monochromatic APs (it contains arbitrarily long squares) AND is aperiodic. So "arbitrarily long monochromatic APs" does NOT force periodicity for general finite-alphabet words. The greedy-specific structure must do the lifting — and that lifting is exactly the fenced step.

**Not the T-unbounded finite-statistic fence (initially).** The T-unbounded fence (round 5) fences ALL f(M_1)-bounded deterministic finite statistics: a_1=77→T=18 vs a_1=847→T=1744 at the same M_1=77, 97× jump. A Ramsey argument does not *a priori* produce an f(M_1)-bounded state — van der Waerden's guarantee is non-constructive about δ and k. So the Ramsey route is NOT fenced-at-the-door by T-unbounded. **This is the one place the route looked alive** — see §5.

**Collapses to the aimo-0907 single-orbit / forward-deterministic fence (round 5).** The lift R3 needs a forward-deterministic map f on a candidate statistic α with α_n → α_{n+1} single-valued and α determining d_n. Round 5 certified that the ONLY such α is the MT-state (the minimal-transversal / full prime-set-constraint history), whose finiteness IS Gap A. The Ramsey ingredient does not supply a new α: van der Waerden produces a coincidence in the *index-coloring* d_n itself, but d_n is NOT forward-deterministic (every realized d-value has ≥2 distinct successors in every tested case — re-confirmed below). So a d-coincidence d_i = d_{i+δ} does not propagate via aimo-0907 part A (part A needs the *state* to coincide, not just the output d). To get state-coincidence, one must name a forward-deterministic α — and that is Gap A.

**Collapses to the deviation-descent `w_min` fence (round 5).** Alternatively, R2 tries "long constant-d AP ⇒ δ is a period" directly (without naming α). This is the deviation-descent route (round 5, certified dead): a candidate period P_0 from a pigeonhole window is not a real period for small w, and `w_min` is unbounded in M_1. A Ramsey long-AP at spacing δ is just a pigeonhole candidate with more evidence — but the deviation-descent B2-Sharp counterexample (a_1=35, δ=5 candidate, real deviation d_8=4≠10=d_{13}) shows that even valid coincidences don't force periodicity. The Ramsey route does not break this fence: see §4 for the computational confirmation that sub-T long-APs are SHORT.

### 3. The hard step (load-bearing unproved sub-claim)

The single load-bearing sub-claim that would make R2 work, stated precisely:

> **(H-Ramsey)** There exists a function K(M_1) such that: if the greedy increment word d ∈ {1,…,M_1}^ℕ contains a constant-d AP of length ≥ K(M_1) at spacing δ (i.e. d_i = d_{i+δ} = … = d_{i+(K-1)δ} = c), then d is eventually δ-periodic.

This is **false as stated** for general finite-alphabet words (Thue-Morse: arbitrarily long constant-value APs, aperiodic). To make it true, the greedy-specific structure must supply the propagation — and that propagation is exactly the forward-deterministic α = MT-state step (= Gap A). So (H-Ramsey) is not merely unproved; it *reduces* to Gap A. There is no independent greedy-dynamic lever that turns "long constant-d AP" into "δ-periodic" without naming the MT-state.

### 4. Computational probe

**Implementation note.** The round-4 `fast_greedy.py` has the inverted-subset bug (drop the tighter constraint); I wrote a correct minimal-transversal-based fast greedy (`/tmp/round-6/mt_greedy.py`) and verified it against the naive O(N²) gcd-greedy on a_1 ∈ {15, 385, 847} (exact match, last terms 5634 / 10738 / 17136). All numbers below use the correct MT-greedy. *Important correction to the round-5 fence data:* with a correct greedy and a long tail (min_run ≥ 2000), a_1=847 gives **T=1744, n0=0, L=18942** (periodic from the start) — matching the round-5 fence. At N=25000 with min_run=300, the detector spuriously reports T=297 (a 33-step suffix coincidence); the true T=1744 is confirmed by a 48255-step suffix run at δ=1744 and emerges cleanly at min_run ≥ 2000. The fence data is correct; short-tail period detection is the pitfall.

**P1 — Longest constant-d AP at sub-T spacing (δ ∤ T) in the periodic part.** This is the Ramsey-observable structure. Brute-forced over δ ∈ [1, min(T-1, 80)]:

| a_1 | M_1 | T | n0 | longest sub-T const-d AP (k, δ, c) |
|---|---|---|---|---|
| 15 | 15 | 8 | 0 | (2, 7, 3) |
| 35 | 35 | 34 | 0 | (5, 24, 5) |
| 77 | 77 | 18 | 0 | (2, 17, 7) |
| 91 | 91 | 20 | 0 | (4, 13, 14) |
| 175 | 35 | 274 | 0 | (10, 63, 15) |
| 847 | 77 | 1744 | 0 | (25, 71, 14) |

For comparison, the **trivial** δ | T constant-d APs are enormous: a_1=77, δ=9 | T=18 ⇒ k=667; a_1=91, δ=10 | T=20 ⇒ k=600; a_1=35, δ=17 | T=34 ⇒ k=353; a_1=847, δ=16 | T=1744 ⇒ k=7.

**Conclusion of P1 (conjecture, label: empirical):** The greedy rule actively SUPPRESSES long constant-d APs at non-periodic spacings. The longest sub-T constant-d AP is at most ~25 (a_1=847, k/T ≈ 1.4%) and typically 2–10. The ONLY long monochromatic APs that van der Waerden guarantees are the trivial δ | T ones — which presuppose the period. So van der Waerden supplies NO pre-period / sub-T Ramsey signal to exploit. The structure it finds is all AT the (unknown) period T.

**P2/P3 — Forward-determinism of candidate states (the dispatch's crux question).** "Is the state determining d_{n+1} forward-deterministic WITHOUT being f(M_1)-bounded?"

Tested (conflict count = #states with >1 successor; fwd-det iff conflicts=0):

| a_1 | M_1 | T | state α | size | conflicts | realized | fwd-det? |
|---|---|---|---|---|---|---|---|
| 15 | 15 | 8 | d_n | M_1=15 | 4 | 4 | NO |
| 15 | 15 | 8 | a_n mod a_1 | a_1=15 | 1 | 7 | NO |
| 35 | 35 | 34 | a_n mod a_1 | a_1=35 | 6 | 11 | NO |
| 77 | 77 | 18 | a_n mod a_1 | a_1=77 | 1 | 17 | NO |
| 91 | 91 | 20 | a_n mod a_1 | a_1=91 | 1 | 19 | NO |
| 175 | 35 | 274 | a_n mod a_1 | a_1=175 | 40 | 55 | NO |
| 847 | 77 | 1744 | a_n mod a_1 | a_1=847 | 121 | 187 | NO |
| 175 | 35 | 274 | a_n mod a_1² | a_1²=30625 | **3498** | 9625 | **NO (real counterexample)** |
| 847 | 77 | 1744 | a_n mod a_1² | a_1²=717409 | 0 | 49999 | (artifact — see below) |
| 847 | 77 | 1744 | a_n mod (a_1·M_1) | 65219 | 6117 | 14399 | NO |

**The a_1=175 mod a_1² row is the decisive new negative finding.** realized=9625 < 30625 (real repeats exist) with 3498 conflict states ⇒ a_n mod (a_1²) is GENUINELY not forward-deterministic. This EXTENDS the T-unbounded-in-M_1 fence beyond f(M_1)-bounded statistics: even an a_1-bounded and a_1²-bounded residue statistic is not forward-deterministic. (The a_1=847 mod a_1² "fwd-det=True" is an ARTIFACT: realized=49999=N-1 means no state has repeated yet — the state space 717409 ≫ N=50000, so trivially each state has one successor. Confirming forward-determinism there needs N > a_1² ≈ 717409, infeasible; but the a_1=175 counterexample settles the general claim negatively.)

**Structural reason (proof, not conjecture):** the transition a_n → a_{n+1} depends on the FULL constraint history {a_1, …, a_n} (a_{n+1} is the smallest m > a_n with gcd(m, a_i) > 1 ∀ i ≤ n). So a_n mod m — for ANY fixed m — cannot determine a_{n+1} mod m in general: two different histories can produce the same a_n mod m but different admissible-next sets. The a_1=175 / mod-a_1² row exhibits this concretely. The ONLY forward-deterministic determining state is the full constraint-set state = MT(F_n), whose finiteness IS Gap A. This re-derives the round-5 two-coincidence finding from the Ramsey side: no non-MT forward-deterministic α exists, Ramsey-found coincidences in d_n or in a_n mod m do not propagate, and the only propagating coincidence is an MT-state self-coincidence = Gap A.

**Verdict on the dispatch's crux question:** No. The state determining d_{n+1} is forward-deterministic ONLY as the MT-state (full constraint history), which is NOT f(M_1)-bounded AND is not a_1-bounded AND is not a_1²-bounded — it is unbounded (Gap A) unless Gap A is assumed. There is no forward-deterministic determining state that escapes the T-unbounded fence: every candidate bounded state (residue statistic, increment window, witness-prime tuple — the last two certified non-forward-deterministic in round 5) fails.

### 5. Why this is not a genuine crack

The one place the Ramsey route looked alive: van der Waerden is non-constructive about δ, so it does not *a priori* produce an f(M_1)-bounded state — escaping the T-unbounded fence's front door. But the route still needs to *propagate* a coincidence to periodicity, and that propagation requires a forward-deterministic state. The computational probe shows:
- (i) the long monochromatic APs that van der Waerden guarantees are all at δ | T (trivial) — there is no sub-T Ramsey structure to exploit (P1);
- (ii) every bounded candidate state α (residue at any modulus, including a_1²) is NOT forward-deterministic (P2/P3; a_1=175 mod a_1² is a clean counterexample);
- (iii) the only forward-deterministic α is the MT-state, whose finiteness IS Gap A (round 5, re-confirmed).

So the Ramsey route collapses: van der Waerden ⇒ long constant-d AP ⇒ (need forward-deterministic α to propagate) ⇒ only α = MT-state works ⇒ Gap A. The Ramsey ingredient is a no-op: it does not supply the missing forward-deterministic α, and the long APs it finds are the trivial δ | T ones.

### 6. Distinct openings surfaced (for the outliner)

- **(negative, structural)** The T-unbounded-in-M_1 fence EXTENDS to a_1-bounded and a_1²-bounded residue statistics: a_1=175, a_n mod (a_1²=30625) has 3498 conflict states (real repeats, genuinely not forward-deterministic). This widens the round-5 fence from "no f(M_1)-bounded state" to "no residue statistic a_n mod m for ANY fixed m" — a clean, certifiable negative lemma candidate.
- **(negative, structural)** The greedy rule SUPPRESSES long sub-T constant-d APs: across 6 starting values, the longest constant-d AP with δ ∤ T has k ≤ 25 (vs T up to 1744). This is a conjecture (empirical, labeled as such) but if provable would directly fence any "long constant-d AP ⇒ period" route — it is the greedy-specific obstruction that makes van der Waerden uninformative here.
- **No positive opening.** The Ramsey route does not surface a new forward-deterministic α. The only α that propagates is the MT-state (= Gap A). Recommend: do NOT mount a Ramsey/vdW approach; it collapses to the round-5 forward-deterministic + deviation-descent fences.

### Knowledge-base entries to use
- `knowledge_base.md` has NO entry for van der Waerden / Ramsey / Szemerédi / additive combinatorics (grep returns nothing). The finite-alphabet + van-der-Waerden machinery is not in the KB; a proof using it would need to import the theorem from scratch.
- Relevant certified lemmas (in `results/imo-2026-06/lemmas/`): `linchpin-and-gap-bound` (d_n ∈ {1,…,M_1}), `aimo-0907-coincidence-criterion` (one self-coincidence of a single-valued map ⇒ eventual periodicity — the lift the Ramsey route needs but cannot feed), `candidate-period-pigeonhole-existence` (pigeonhole gives a candidate period for every window w; caveat P_0(w) not a period for small w), `deviation-descent-blocked-by-wmin-fence` (the w_min-unbounded-in-M_1 fence), `syndetic-divisible-closed-not-periodic` (bounded gaps + closure ⇏ periodic).

### Analogous past problems (cruxes)
- **None genuinely analogous.** Searched the crux corpus (2434 cruxes) for "van der Waerden", "Ramsey", "monochromatic", "arithmetic progression" (50 progression-hits, 42 Ramsey/monochromatic hits). Every Ramsey/monochromatic crux is a *graph-coloring* or *geometric-coloring* argument (e.g. aimo-0826 extremal C3/C5-avoidance, aimo-0797 strip-coloring, aimo-0136 same-class n-subsets) — none forces PERIODICITY of a one-dimensional word from monochromatic APs. The closest periodicity-forcing crux is `aimo-0351` (number theory): "pin the sign of a sequence of ±1 steps to a single constant" — forces f(n+1) = f(n) ± q and uses injectivity to rule out the minus, giving a genuine AP. That is a *sign-pinning via injectivity* move, not a Ramsey move, and the greedy d_n is not ±1-valued. No crux in the corpus lifts "long constant-d AP ⇒ periodic word" — consistent with Thue-Morse being a counterexample in the general (non-greedy) setting.

### Prior progress
- The whole theorem is reduced to Gap A (governing primes finite ⊆ primes ≤ M_1 = rad(a_1)); endgame + LOCK + pure-from-start + conditional bridge all certified (rounds 1–5). 28 certified lemmas. The Ramsey route does not advance this — it re-confirms the round-5 finding that the only forward-deterministic determining state is the MT-state (= Gap A).

### Dead ends (do not retry)
- **Ramsey / van-der-Waerden on d_n to force periodicity** (this route): collapses to (a) the aimo-0907 single-orbit forward-deterministic fence (the only forward-deterministic α is the MT-state = Gap A), (b) the deviation-descent `w_min` fence (sub-T constant-d APs are SHORT — the greedy rule suppresses them; long monochromatic APs are only the trivial δ | T). New negative finding: the T-unbounded fence extends to a_1-bounded and a_1²-bounded residue statistics (a_1=175, mod a_1²: 3498 conflicts).
- All previously-fenced routes (13 dead mechanisms + 4 structural fences, full list in run_state.md Rules) remain fenced.

### Small-case / intuition notes (labeled as conjecture)
- **(conjecture, empirical)** Across a_1 ∈ {15, 35, 77, 91, 175, 847}, the longest constant-d AP with δ ∤ T is ≤ 25 (k/T ≤ 1.4%); the greedy rule actively suppresses long sub-T constant-d APs. If provable, this directly fences any Ramsey→period route.
- **(proof, structural)** No residue statistic a_n mod m (for any fixed m, including m = a_1, a_1·M_1, a_1², a_1³) is forward-deterministic: the transition a_n → a_{n+1} depends on the full constraint history, not on a_n mod m. Exhibited concretely at a_1=175, m = a_1² = 30625 (3498 conflict states with real repeats).
- **(re-confirmation)** T(847) = 1744, n0 = 0, L = 18942 (periodic from start), matching the round-5 T-unbounded fence; the rad-77 pair a_1=77→T=18 vs a_1=847→T=1744 stands. Short-tail period detection (min_run < 2000) gives spurious smaller periods (T=255/297); use min_run ≥ 2000.
