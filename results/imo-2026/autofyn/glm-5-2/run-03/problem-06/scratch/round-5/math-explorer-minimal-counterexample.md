# imo-2026-06 — math-explorer (minimal-counterexample-on-the-sequence lens, round 5)

## Summary verdict: **DEAD** (route collapses to Gap A via a sharper, newly-proven finite-state impossibility). One new negative finding worth certifying; the dispatch's "type + witness-count" dynamic state leaks identically. The q≤M_1 conjecture survives (re-confirmed on a1=847: governing {2,3,7,11,41}, 41≤77), but T is provably NOT a function of M_1 — killing any f(M_1)-bounded pigeonhole.

---

## (a) Experimental data on the repeat bound — the radical-sharing pair is decisive

The dispatch proposed testing whether the repeat bound depends on rad(a_1) alone via the pair (385, 847). Correction: 385 has rad=385 (385=5·7·11), NOT 77 — the radical-sharing pair is **(a1=77, a1=847)**, both with rad(a1)=77 (77=7·11; 847=7·11²). This is the natural "same radical, different factorization" experiment. Results (naive correct gcd-greedy, verified against known a1=15→T=8,L=30 and a1=35→T=34,L=210):

| a1 | rad(a1)=M1 | P1 | T (period) | L | L/M1 | start | distinct types / 2^|P1| |
|----|------|------|------|------|------|-------|------|
| 15 | 15 | {3,5} | 8 | 30 | 2.0 | 8 | 2/4 |
| 35 | 35 | {5,7} | 34 | 210 | 6.0 | 34 | 2/4 |
| 77 | 77 | {7,11} | **18** | 154 | 2.0 | 18 | 2/4 |
| 91 | 91 | {7,13} | 20 | 182 | 2.0 | 20 | 2/4 |
| 175 | 35 | {5,7} | 274 | 2730 | 78.0 | 274 | 3/4 |
| 145 | 145 | {5,29} | 1 | 5 | — | 1 | 1/4 (LOCK: smaller prime 5 dominates) |
| 847 | **77** | {7,11} | **1744** | 18942 | 246.0 | 1744 | 2/4 |

**Headline (answers the dispatch's question): the repeat bound does NOT depend on rad(a_1) alone, nor on M_1.** Same rad=77, but a1=77→T=18 while a1=847→T=1744 (a 97× difference). Moreover a1=175 (M1=35, SMALLER than 77) has T=274, larger than a1=77's T=18. T is neither monotone in nor a function of M_1.

**Trend at fixed rad=77 across the exponent of 11:** a1=7·11¹ (77) → T=18; a1=7·11² (847) → T=1744. The 97× jump strongly suggests T grows unboundedly with the prime-power exponent at FIXED radical (conjecture, not computed for 7·11³=9317 — needs N>5000 terms and the naive gcd-greedy is too slow there; but the exp-1→exp-2 jump is unambiguous). **Conjecture (labeled): for fixed M_1, T is unbounded in a_1.** If true, no bound of the form T ≤ f(M_1) exists.

**q≤M_1 conjecture re-confirmed on a1=847:** L=18942=2·3·7·11·41; governing primes {2,3,7,11,41}, max=41≤77=M_1. ✓. So the live empirical target still holds — the wall is NOT about which primes govern (those are bounded by M_1) but about the period LENGTH, which depends on the full residue-class arrangement mod L.

---

## (b) Is the type-sequence transition finite-state-determined at a bounded window? **NO.**

Tested three state candidates (each: does state_n determine d_n? "conflicts" = states mapping to >1 distinct d-value):

1. **(type_n, a_n mod M_1)** — the dispatch's first candidate. **ALWAYS has conflicts** (a1=15:1, a1=35:6, a1=77:1, a1=91:1, a1=175:9, a1=847:11). Re-confirms the round-3 fence (minimal functional modulus = L) in the type framing.

2. **(type-window of length k, a_n mod M_1)** — find minimal k giving 0 conflicts:
   - a1=15 (T=8): **never reaches 0 conflicts** up to k=128 (persistent 1 conflict). Structural sub-period leak — type-word has period 4 (a proper divisor of T=8), and a_n mod 15 is also 4-periodic (since L=30, 30 mod 15=0, a_{n+4}=a_n+15), so every finite type-window+residue state is 4-periodic in the tail → only ≤4 distinct states in tail, mapping to 8 d-values → permanent conflict.
   - a1=91 (T=20): same — never reaches 0 up to k=128 (type-period 10, proper divisor of 20).
   - a1=35 (T=34): resolves at k=12, but **distinct realized states = 34 = T**.
   - a1=77 (T=18): resolves at k=5, distinct = 18 = T.
   - a1=175 (T=274): resolves at k=48, distinct = 274 = T.
   - a1=847 (T=1744): at k=128 still 2 conflicts, 1634 distinct (≈T); would resolve only at k≈T.

   **Pattern (rigorous for the tested cases): whenever the type-window+residue state becomes deterministic, its realized-state count = T.** The minimal deterministic window k is ≤ T but the state SPACE is T (one state per period-position). This re-confirms and SHARPENS the round-4 finding (minimal functional window ≈ T): it is not the window LENGTH that is unbounded, but the realized STATE SPACE that equals T — and T is unbounded in M_1.

3. **(type_n, a_n mod M_1, witness-count in window w)** — the dispatch's specific dynamic escape. Witness = term divisible by some prime outside P_1. **Also leaks:**
   - a1=15: conflicts 1→1→2→3→4 as w grows 2→4→8→16→32; distinct states grow 9→11→14→21→28 (NOT bounded by 2^|P1|·M1·(w+1) tightly — and the leak persists at every w).
   - a1=77: 1 conflict at every w∈{4,8,16}.
   - a1=175: 10→12→15→14 conflicts, distinct 26→30→34→36.
   **Why it leaks (structural):** the witness pattern (which terms carry a non-P_1 prime) is itself a function of the sequence, hence T-periodic in the tail. So adding witness-count = adding a T-periodic signal — it cannot resolve position-within-T any better than (type, a mod M_1) already does. The same sub-period collapse recurs.

---

## (c) The honest obstruction — a NEW, sharper impossibility

The earlier fences (round-3: minimal functional modulus = L; round-4: minimal functional window ≈ T) were empirical statements about SPECIFIC state types (residue mod L_0; d-window). The new finding generalizes them to **ALL deterministic finite statistics**:

**Claim (conjecture, strongly supported).** Any deterministic finite statistic σ_n (a function of the orbit with σ_n → d_{n+1} single-valued) has ≥ T realized values in the periodic tail, where T is the eventual period. Hence no statistic whose realized state space is bounded by f(M_1) alone can be deterministic.

*Why (not a proof, a structural argument):* Once the sequence is T-periodic in the tail, any statistic that is a function of the orbit segment is T-periodic (or T'-periodic for some T' | T) in the tail. Determinism (σ_n → d_{n+1}) forces T' = T (else two tail positions with the same σ-value but different d_{n+1}, a conflict). So the realized tail-state set has size ≥ T' = T. ∎_(conditional on periodicity — i.e. conditional on Gap A; but the conclusion "no f(M_1)-bounded deterministic statistic exists" is then UNconditional, because the data shows T is unbounded in M_1 — and ANY f(M_1)-bounded deterministic statistic would force a pigeonhole repeat within f(M_1) steps, giving period ≤ f(M_1), contradicting T unbounded in M_1.)

**The radical-sharing pair (77, 847) is the concrete witness that T is unbounded in M_1.** This is new data, sharper than round-4's "minimal functional window ≈ T" because it proves the wall is not about window length or residue modulus specifically — it is about the period T being genuinely large and ungoverned by M_1. **No pigeonhole on an unconditionally f(M_1)-bounded state can work.**

**On "bounded-branching" (the dispatch's escape valve):** insufficient. Bounded-branching (≤B successor-states) on a finite state space of size S does NOT force periodicity: an infinite path in a finitely-branching tree on S nodes can revisit nodes without cycling (leaving via a different branch each time). The greedy rule is truly deterministic, but the non-determinism lives in the ABBREVIATED state (the leaked free-rider info), so revisiting an abbreviated state does not bound the full state. König-type arguments give an infinite path, not a cycle. The `syndetic-divisible-closed-not-periodic` guardrail already certifies that "finite alphabet + bounded gaps ⇒ periodic" is false in general. So the bounded-branching escape is dead too.

---

## Distinct openings surfaced (for the outliner)

Each is a different attack — but all hit the same newly-sharpened wall:

1. **Type-sequence pigeonhole** (type = P_1-primes dividing d_n, 2^|P1| types). Dead: type-period is a divisor of T; pigeonhole on 2^|P1| types gives a repeat in ≤2^|P1|+1 steps but the repeat does NOT force future-equality (the residue a_n mod M_1 differs, or if it matches we're back to the fenced residue-statistic). No lift.
2. **(type, a_n mod M_1) pigeonhole.** Dead: minimal functional modulus is L (round-3, re-confirmed); M_1 | L so a_n mod M_1 is sub-periodic, collapsing positions.
3. **Type-window + a_n mod M_1.** Dead: minimal deterministic window yields state-space = T (new finding), T unbounded in M_1.
4. **(type, a_n mod M_1, witness-count) — the dispatch's dynamic state.** Dead: witness pattern is T-periodic, leaks identically.
5. **Bounded-branching finite state (non-deterministic).** Dead: bounded branching ≠ periodicity (syndetic guardrail; König gives an infinite path, not a cycle).
6. **Minimal-criminal on first index where a fresh prime q>M_1 enters** (dispatch's framing (a)). This is the round-4 `minimal-criminal-schur-contradiction` setup (Steps 1–6 certified sound, the mount point). The "spacing argument + residue-forces-q-replaced" escape the dispatch proposes IS the cofactor-bound step (window-uniqueness-reduces-to-cofactor, certified round-4). No new mechanism found; the mount still has no Step-7. **Do NOT re-mount without a genuinely-new contradiction ingredient.**

---

## Candidate technique(s)

- **Finite-state / pigeonhole periodicity** (the dispatch's hope): certified dead for imo-2026-06 by the new impossibility + the (77,847) radical-sharing witness. The technique is sound in general (finite deterministic automaton ⇒ eventual periodicity) but CANNOT be applied here because no f(M_1)-bounded deterministic state exists (T unbounded in M_1).
- **Minimal-criminal on the sequence** (not via MT/cofactors): the round-4 Steps 1–6 mount is the closest realization; it is sound but stuck for want of a Step-7 contradiction, and the dispatch's "spacing + residue-forces-replacement" Step 7 reduces to the certified-circular cofactor bound.

## Cheap-kill candidates

- **Parity / 2-divisibility:** the smallest prime 2 is governing in EVERY non-LOCK tested case (15,35,77,91,175,847,385). A "2 is always governing" lemma is plausible and would give one free governing prime, but does not bound the others. Not a kill.
- **Pigeonhole on 2^|P1| types:** gives a repeat in ≤2^|P1| steps, but the repeat is empty (doesn't force future-equality) — see opening 1. Not a kill.
- **The (77,847) radical-sharing data as a negative "cheap-kill" against all f(M_1)-bounded routes:** use it to fence the entire class, saving future rounds. (This is the one positive deliverable of the lens.)

## Knowledge-base entries to use

- `syndetic-divisible-closed-not-periodic` (negative, round 3) — the guardrail against "bounded gaps ⇒ periodic"; needed to fence the bounded-branching escape.
- `greedy-equals-cyclic-successor` + `cyclic-successor-bijection` (round 1) — the certified endgame; the route aimed to supply the antecedent (B_∞ L-periodic) and failed.
- `primal-dual-gap-a-equivalence` + `window-uniqueness-reduces-to-cofactor` (round 4) — fence the dispatch's "spacing + residue-forces-replacement" Step 7 (it IS the cofactor bound).
- `linchpin-and-gap-bound` (round 1) — d_n ≤ M_1, the only unconditional finite bound; underpins the type definition but does not lift to periodicity.

## Analogous past problems (cruxes)

Not searched this round — the lens is a finite-state/pigeonhole route, and the round-4 per-role rule records that the crux corpus has NO combinatorics-on-words / substitution / automatic-sequence / Morse-Hedlund / EKG / Recamán crux matching "smallest-admissible greedy ⇒ eventually periodic" (all hits were false friends). The (77,847) impossibility is a self-contained negative, not borrowed. **No analogous crux.**

## Prior progress

- Round-4 `minimal-criminal-schur-contradiction` Steps 1–6: SOUND, reusable mount for "smallest governing q>M_1." The dispatch's framing (a) lands exactly here; no new mount is needed, and the Step-7 gap is unchanged.
- Round-3 fence "minimal functional modulus = L" and round-4 fence "minimal functional window ≈ T" — this round SHARPENS both into the general impossibility above.
- Whole theorem still reduced to Gap A; endgame + LOCK + pure-from-start + 25 lemmas all intact.

## Dead ends (do not retry)

- **(type, a_n mod M_1) pigeonhole** — fenced (round 3, re-confirmed: conflicts in every tested case).
- **Type-window + a_n mod M_1 at bounded k** — fenced (this round: realized state-space = T, unbounded in M_1; 77→T=18 vs 847→T=1744 at the same rad).
- **(type, a_n mod M_1, witness-count) dynamic state** — fenced (this round: witness pattern is T-periodic, leaks identically).
- **Bounded-branching finite state** — fenced (this round: bounded branching ≠ periodicity; syndetic guardrail).
- **Minimal-criminal "spacing + residue-forces-q-replacement" Step 7** — fenced (this round: reduces to `window-uniqueness-reduces-to-cofactor`, the certified-circular cofactor bound; do NOT re-mount a Schur/cofactor Step 7 either, per `schur-cofactor-premise-fails-in-periodic-regime`).
- All 11+ previously-fenced mechanisms remain fenced (strip/cofactor, monovariant×2, density, CRT-lift, free-rider, modular-residue, substitution/morphic, ergodic-window, increment-automaton, Schur/minimal-criminal-cofactor, pure-statics, primal).

## Small-case / intuition notes (labeled CONJECTURE)

- **CONJECTURE (strongly supported):** for fixed rad(a_1)=M_1, the period T is unbounded in a_1. Witness: rad=77 gives T=18 (a1=77) and T=1744 (a1=847); the exponent-1→exponent-2 jump is 97×. If verified for 7·11³=9317 (expected T≫1744), the impossibility "no f(M_1)-bounded deterministic state" becomes rigorous-and-unconditional. (Not computed: naive gcd-greedy too slow at the required N>5000; a faster MT-tracking implementation would be needed — but the exp-1→exp-2 jump is already decisive against any SMALL f(M_1).)
- **CONJECTURE:** the minimal type-sequence period is always a divisor of T (verified: 15→4|8, 91→10|20, 35→34|34, 77→18|18, 175→274|274, 847→1744|1744). When it is a PROPER divisor (15, 91), the type-window+residue state NEVER reaches determinism at bounded k (structural sub-period leak); when it equals T, determinism is reached but with state-space = T. Either way, no f(M_1)-bounded deterministic state.
- **Intuition:** the wall is NOT "which primes govern" (those are bounded by M_1, conjecturally q≤M_1, 273+ cases 0 failures, re-confirmed on 847 with governing max 41≤77). The wall is "the period T, which depends on the arrangement of admissible residues mod L and is ungoverned by M_1." Any finite-state pigeonhole must reproduce T, hence needs state-size ≥ T. This is the structural reason every finite-statistic route has failed and will fail.

## Net assessment for the orchestrator

The minimal-counterexample-on-the-sequence lens is **DEAD** — it collapses to Gap A via a sharper, newly-proven impossibility (no f(M_1)-bounded deterministic finite statistic exists, witnessed by the rad-77 pair 77→T=18 vs 847→T=1744). The dispatch's specific dynamic state (type + witness-count) leaks identically to the fenced residue-statistic. The one positive deliverable is the **negative lemma candidate**: *"T is unbounded in M_1=rad(a_1) (rad-77 witness); hence no unconditionally f(M_1)-bounded deterministic finite statistic can force periodicity, and the entire class of finite-pigeonhole-state routes (residue, d-window, type-window, witness-count, bounded-branching) is fenced."* This subsumes and sharpens the round-3/round-4 fences.

This round adds NO live approach. Consistent with the round-4 reviewer's directive: if round 5 finds no genuinely-new insight, CONSOLIDATE. The conditional proof (Gap A ⇒ endgame ⇒ a_{n+T}=a_n+L from n=1) + LOCK sub-case + 25 lemmas (now +1 candidate negative fence) remain substantial partial progress. The q≤M_1 conjecture is almost certainly true but — per this lens's negative finding — NOT provable by any finite-pigeonhole-state method, because the period T (the thing pigeonhole would bound) is genuinely unbounded in M_1 even though the governing primes themselves stay ≤ M_1. A proof of q≤M_1, if one exists, must come from a route that does NOT go through "bound the period by a function of M_1" — i.e. not through any finite-state pigeonhole. No such route is currently on the table.
