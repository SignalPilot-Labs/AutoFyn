# Outline-reviewer — imo-2026-06, round 5

4th round on Gap A. Three round-5 explorers: two DEAD (minimal-counterexample with a sharp NEW T-unbounded-in-M_1 impossibility subsuming the modular-residue/ergodic-window/increment-automaton fences; p-adic with a clean L≠lcm(L_p:p|M_1) obstruction), one LIVE (crux-corpus-pull surfacing four mechanisms M1–M4). The outliner mounted four new approaches. Below: per-approach verdict, the ranking, the build set, and a candid stall assessment.

## Per-approach verdict

### `two-coincidence-periodicity` — CHANGES REQUESTED (build)

**Framing genuinely different?** Yes. It attacks the theorem END-TO-END by proving d_n eventually periodic directly (then telescoping), going AROUND Gap A (no B_∞/MT/cofactors/finiteness-of-governing-primes). Not a Gap-A variation, not in the fenced list.

**Right technique?** The `aimo-0907` coincidence-doubling ⇒ periodicity mechanism is sound in principle for deterministic processes. But the outline has a serious internal confusion I verified concretely:

- **The "two coincidences" role is muddled.** For a forward-single-valued deterministic abstraction α (α_{n+1}=f(α_n)), ONE self-coincidence α_a=α_b propagates by induction to α_{a+k}=α_{b+k} for ALL k≥0 — i.e. α is eventually periodic with period (b−a). The "second coincidence" is REDUNDANT for α itself. The second coincidence only earns its keep if α is NOT forward-deterministic-determining (α→α_{n+1} but NOT α→d_{n+1}), in which case α-periodicity does not lift to d_n-periodicity and the two-coincidence mechanism is supposed to supply the lift. That lift is the load-bearing open claim (Gap A4) and the outline honestly flags it — but it is the REAL content of the approach, and the outline's watch-out "(i) the one-coincidence ⇒ periodicity argument is TRIVIAL for a finite-state map but our state is the infinite past" misdiagnoses the obstacle. The obstacle is NOT "infinite state" (forward determinism propagates regardless); it is that α does not determine d_{n+1}, so α-periodicity is too coarse to lift.

- **The outliner's claim "M1 uses NO finiteness assumption" is FALSE.** Step 3 explicitly invokes "pigeonhole on the abstraction's finite alphabet (|P_1| small)." That IS a finiteness assumption. The new T-unbounded-in-M_1 impossibility (rad-77 witness: a_1=77→T=18 vs a_1=847→T=1744 at the same M_1=77) kills ANY f(M_1)-bounded forward-deterministic statistic σ with σ→d_{n+1} single-valued (it has ≥T realized values, T unbounded in M_1). So:
  - If α is forward-deterministic AND determines d_{n+1}, it is FENCED by the new impossibility (|realized| ≥ T > |alphabet| = f(M_1)).
  - If α is forward-deterministic but does NOT determine d_{n+1}, α-periodicity is trivial (one coincidence, period ≤ |alphabet|) but does NOT lift — and the lift is the unproved two-coincidence mechanism (A4).
  - If α is NOT forward-deterministic, coincidences do not propagate and no periodicity follows at all.

- **Concrete check (a_1=15, |P_1|=2, T=8).** The natural candidate α_n = (which p∈{3,5} divides d_n) has period 4 (a proper divisor of T=8) and is NOT forward-single-valued: (3,)→() at n=0 but (3,)→(3,) at n=3. So the named abstractions fail Step 2's single-valuedness. The builder must search for a genuinely forward-deterministic abstraction; the probe will tell.

**Hard steps open vs merely flagged?** A1 (single-valued abstraction), A3 (second coincidence), A4 (lift lemma for infinite-state map), A5 (lift to d_n) are ALL genuinely open — none is certified, none is smuggled from an existing lemma. A2 (non-circular first coincidence) correctly bars the cofactor-AP trap (citing `schur-cofactor-premise-fails-in-periodic-regime`). The honest flagging is good; the mechanism is genuinely unclear.

**Why build anyway.** This is the ONLY route on the table that goes AROUND Gap A rather than through it. The computational probe (does a second pre-periodic coincidence exist in |P_1|=2 cases a_1∈{15,35,77,91}?) is cheap and decisive: if no second coincidence exists in these cases, the approach is dead on arrival; if one exists, the lift mechanism has a concrete target. Worth one build with the probe first.

**Changes the builder must make while building:**
1. Resolve the mechanism confusion: decide whether α is forward-deterministic-determining (FENCED) or forward-deterministic-non-determining (needs the A4 lift). Do NOT proceed without this decision.
2. Run the computational double-coincidence probe on a_1∈{15,35,77,91} FIRST. If no second pre-periodic coincidence in any candidate abstraction, declare the approach dead.
3. Address the new T-unbounded-in-M_1 impossibility explicitly: either show α escapes it (non-determining, non-f(M_1)-bounded alphabet) or concede the route is fenced.

---

### `deviation-index-descent` — APPROVE (build)

**Framing genuinely different?** Yes. A minimal-index descent on the first deviation of d_n from a candidate period T_0, mounted on the CERTIFIED Steps 1–6 of `minimal-criminal-schur-contradiction` but re-targeted from the prime q (Schur, fenced) to the deviation index. NOT a Gap-A variation, NOT in the fenced list, NOT killed by the new T-unbounded-in-M_1 impossibility (it is a descent, not a pigeonhole-state route; the candidate T_0 is pigeonhole-existence on the infinite word, NOT bounded by f(M_1) a priori).

**Right technique?** The `aimo-0077` minimal-index-on-violation + `aimo-0009` modular-exclusion-jump template is sound in principle. The mount (Steps 1–6, reviewer-certified sound) gives: well-ordering of governing primes, q|a_n infinitely often, d_{n-1}=q−(a_{n-1} mod q) FORCED at q-multiples (the key greedy-specific ingredient). The forced-increment identity is the genuine "forbidden smaller-index action" the descent needs.

**B1 (candidate period) is non-circular.** Option (b): T_0 = offset of the first coincidence of a length-k window of d_n over the finite alphabet {1,…,M_1}. Pigeonhole on infinite words guarantees existence (no bound a priori, which is fine — the descent proves T_0 is the TRUE period). This does NOT presuppose Gap A (it is a property of the increment word, not of B_∞/MT/governing-primes). Option (a) correctly barred (would couple to M1 = single-gap trap). Option (c) correctly barred (conditional-on-Gap-A, circular). ONE caveat: a single window-coincidence does NOT by itself force periodicity (Morse-Hedlund needs the full complexity bound p(k)≤k, not one coincidence). The descent must propagate the one coincidence to full periodicity — that is B2's job.

**B2 (rewriting yields smaller-index deviation) is the load-bearing open mechanism.** The outline honestly flags it. The mechanism: at a q-multiple step, d_{n-1} is forced to a specific value; a deviation at index i forces a specific earlier structure, creating a deviation at j<i. This is hand-wavy as written ("specific earlier structure," "creates a deviation" need precise formulation), but it is a GENUINE new mechanism (the greedy forced-increment is certified and not in any fence). The `window-uniqueness-reduces-to-cofactor` fence warns that B2 must NOT reduce to cofactor-prime bounding — the builder must ensure the rewriting uses the forced increment, not cofactor primes.

**Why build.** Genuinely new framing, certified mount, the forced-increment identity is a real greedy-specific ingredient not yet exploited for a descent, and B2 is a concrete open question worth one focused attempt. Cheaper to test than M1 (no computational probe needed; the descent is a proof attempt).

---

### `augmented-bijective-state` — RETHINK (do not build, do not register)

**The finiteness half IS Gap A.** The outliner is honest (Gap C2): "the finiteness proof CANNOT use an f(M_1) bound. The ONLY escape is a finiteness proof from a source OTHER than M_1. No such source is currently identified." The new T-unbounded-in-M_1 impossibility kills the obvious version: a bijective state that determines a_{n+1} (hence d_{n+1}) is a forward-deterministic-determining statistic, so it has ≥T realized values, T unbounded in M_1 — contradiction with f(M_1)-boundedness. The outliner's claim "the encoding search is NOT fenced" is technically true (only the window encoding is fenced), but the finiteness half has NO identified mechanism — building this would be building an approach whose central lemma (finiteness from a non-M_1 source) is the unsolved problem itself.

**Reversibility half already certified elsewhere.** `cyclic-successor-bijection` + `greedy-equals-cyclic-successor` ARE certified and reusable. No progress is lost by cutting M2 — the reusable content is already in the lemma cache.

**Not fenced (the framing is genuinely new), but not buildable.** RETHINK: the outliner must identify a non-f(M_1) finiteness source before this can be built. Without one, the approach is a restatement of Gap A in bijective-state language, not a route past it.

---

### `frozen-radical-monovariant` — RETHINK (do not build, do not register)

**Fatal flaw: the finish is FENCED.** Step 5 ("reduce mod lcm of attainable a_n") is the modular-residue statistic fence (minimal functional modulus = L, round 3). The outliner explicitly concedes this ("FENCED; this approach CANNOT use it") and asks for an alternative finish — but no alternative is identified, and the candidate alternative ("once w_n is constant, the skeleton-failing set is fixed, forcing the increment-word into a finite automaton") risks the increment-window fence (round 4).

**Monovariant mechanism weakly fitted.** The `aimo-0678` non-increasing mechanism is "the current term falls into the next step's failing set (a_n ∈ W_{n+1} so w_{n+1} ≤ a_n)." Our greedy makes a_{n+1} ADMISSIBLE (shares a prime with all priors) — the OPPOSITE of failing. The outliner honestly rates this the weakest candidate (Gap D2 "weak structural fit"). Even if w_n is non-increasing (unproved), the approach cannot conclude because the finish is fenced.

**Not fenced as a monovariant (genuinely different from the two dead ones), but not buildable as a whole proof.** RETHINK: the outliner must identify a non-fenced finish before this can be built. The monovariant half alone does not give a proof.

---

## Pairwise comparison list (fed to update_ranking)

Anchored to certified outcomes: lemma-sources (transversal-saturation, prime-power-dichotomy, crt-period-lifting) > new untested; new live > fenced/dead; M1 ≈ M3 (both new, both live, different mechanisms); p1-equals-2-direct (certified lemmas, smallest open base) ≈ the new ones (draw — p1 has certified content but is stuck on a fenced-ish cofactor wall).

1. transversal-saturation > two-coincidence-periodicity
2. prime-power-dichotomy > two-coincidence-periodicity
3. crt-period-lifting > two-coincidence-periodicity
4. two-coincidence-periodicity > minimal-criminal-schur-contradiction (new live vs Schur-dead)
5. two-coincidence-periodicity > primal-minimal-support-stabilization (new vs fenced ≡ Gap A)
6. two-coincidence-periodicity > integer-monovariant-transfer (new vs dead)
7. two-coincidence-periodicity > witness-density-recurrence (new vs dead)
8. two-coincidence-periodicity > growing-modulus-descent (new vs dead)
9. two-coincidence-periodicity > free-rider-type-replacement (new vs dead)
10. transversal-saturation > deviation-index-descent
11. prime-power-dichotomy > deviation-index-descent
12. crt-period-lifting > deviation-index-descent
13. deviation-index-descent > minimal-criminal-schur-contradiction (new descent on certified mount vs Schur-dead)
14. deviation-index-descent > primal-minimal-support-stabilization (new vs fenced)
15. deviation-index-descent > integer-monovariant-transfer (new vs dead)
16. deviation-index-descent > witness-density-recurrence (new vs dead)
17. deviation-index-descent > growing-modulus-descent (new vs dead)
18. deviation-index-descent > free-rider-type-replacement (new vs dead)
19. two-coincidence-periodicity vs deviation-index-descent — DRAW (both new, both live, different mechanisms; M1 cleaner-in-principle but mechanism-confused, M3 solid-mount but B2 open)
20. p1-equals-2-direct vs two-coincidence-periodicity — DRAW (p1 has certified lemmas + smallest open base; M1 is a full attack with a new mechanism but nothing certified)
21. p1-equals-2-direct vs deviation-index-descent — DRAW (same reasoning)
22. minimal-criminal-schur-contradiction > primal-minimal-support-stabilization (Steps 1–6 certified mount vs fenced ≡ Gap A)
23. p1-equals-2-direct > primal-minimal-support-stabilization (smallest open base with certified lemmas vs fenced)

(M2 augmented-bijective-state and M4 frozen-radical-monovariant NOT registered, NOT ranked — RETHINK.)

## Final ranking (Elo-sorted, post update_ranking)

| # | slug | Elo | status |
|---|------|-----|--------|
| 1 | transversal-saturation | 1643 | lemma source (Gap A open, strip dead) |
| 2 | prime-power-dichotomy | 1589 | lemma source (LOCK certified, Gap C open) |
| 3 | crt-period-lifting | 1573 | lemma source (F1/F2 certified, CRT-lift dead) |
| 4 | deviation-index-descent | 1547 | NEW (APPROVE; B2 open) |
| 5 | two-coincidence-periodicity | 1546 | NEW (CHANGES REQUESTED; A4/impossibility confusion) |
| 6 | p1-equals-2-direct | 1542 | smallest open base (cofactor wall open) |
| 7 | minimal-criminal-schur-contradiction | 1515 | mount point (Schur dead) |
| 8 | integer-monovariant-transfer | 1484 | dead/retired |
| 9 | primal-minimal-support-stabilization | 1444 | fenced (≡ Gap A) |
| 10 | witness-density-recurrence | 1411 | dead |
| 11 | growing-modulus-descent | 1382 | dead |
| 12 | free-rider-type-replacement | 1324 | dead |

## Round-5 assessment — genuine progress or consolidate?

**Genuine, but narrow, progress this round.** Two of the four new approaches (`two-coincidence-periodicity`, `deviation-index-descent`) are GENUINELY different framings not hit by the new T-unbounded-in-M_1 impossibility and not in the fenced list. M1 is the only route on the table that goes AROUND Gap A (proving d_n-periodic directly) rather than THROUGH it; M3 is a descent on a certified mount with a real greedy-specific ingredient (the forced-increment identity). Both deserve one real build each.

But the honest prognosis is grim. M1 has a serious internal mechanism confusion (the "second coincidence" role is muddled; the outliner's "no finiteness assumption" claim is wrong — Step 3's pigeonhole IS a finiteness assumption, and the new impossibility bites if α determines d_{n+1}). M3's B2 is a hand-wavy open mechanism that may reduce to the cofactor-bound fence. The two long shots (M2, M4) are correctly RETHUNK — M2's finiteness half IS Gap A with no non-M_1 source identified; M4's finish is fenced.

**Decision: build M1 and M3 this round (one builder each). Do NOT consolidate yet** — M1's computational probe (does a second pre-periodic coincidence exist in |P_1|=2 cases?) is cheap and decisive: a negative result kills M1 cleanly and the run should consolidate next round; a positive result gives the live route a concrete target. M3 is a focused proof attempt on a certified mount. If BOTH fail with clean obstructions next round, CONSOLIDATE: the conditional proof (Gap A ⇒ endgame ⇒ a_{n+T}=a_n+L from n=1) + LOCK sub-case + 25 certified lemmas (now including the sharp T-unbounded-in-M_1 impossibility as a strong negative deliverable) constitute substantial partial progress on a genuinely IMO-P6-hard problem. The q≤M_1 conjecture is almost certainly true (273+ cases, 0 failures) but, per the accumulated fences + the new impossibility, NOT provable by any cofactor/transversal/MT/statics/monovariant/residue/finite-pigeonhole-state/Schur/primal route — a non-circular proof, if one exists, goes through coincidence-doubling (M1) or a deviation descent (M3), and this round is the last honest shot at both.

build set: two-coincidence-periodicity, deviation-index-descent
