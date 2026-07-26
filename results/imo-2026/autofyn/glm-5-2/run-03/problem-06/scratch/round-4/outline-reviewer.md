# Round 4 outline-reviewer report — imo-2026-06

Gate review of the round-4 field. The stall is deep (3rd round on Gap A; ~10 mechanisms certified dead). Per the orchestrator's stall rule the bar for "genuinely new" is HIGH, and an approach that is Gap A in cleaner clothes is acceptable ONLY IF its stabilization argument uses a genuinely non-cofactor greedy mechanism. I read `run_state.md`, `current.md`, the `.ranking.json`, both new approach skeletons, and the round-3 reviewer record; I ran an independent computational check on the load-bearing empirical claims.

## Independent empirical verification (the decision-relevant facts)

1. **Schur premise fails — CONFIRMED.** For a1=15, q=3 (a genuine governing prime ≤ M_1=15), the cofactors k_i = a_n/3 across 600 terms carry prime factors **up to 241** (the outliner reported 199; the true max over 600 terms is 241 — even worse), and **136 of 242 q-multiples have a cofactor-prime > 15**. So "k_i's prime set is eventually fixed-finite ⊆ G ≤ M_1" is empirically FALSE as stated, exactly as the outliner admits. The minimal-criminal approach's crux (transient-death) is the only rescue, and it is open.

2. **Primal antichain — INCONCLUSIVE on my finite window, NOT refuted.** Computing minimal supports over the first 1500 terms gives a large antichain (17–146 supports) still carrying transient primes > M_1 for a1 ∈ {15,35,175,847}. This does NOT refute the outliner's "MS_∞ tiny (3–7), primes ≤ M_1" claim, because MS_∞ is over the *full periodic family* (a1=385 stabilizes at n≈38 with T=5088); a 1500-term window is too short for transient primes to die out of the minimal antichain. The claim is consistent with the standing governing-prime conjecture (q ≤ M_1, 100+ cases 0 failures) and I cannot falsify it without computing a full period. I accept the outliner's empirical signal for the primal as plausible-but-unverified.

## Approach 1: `minimal-criminal-schur-contradiction` (NEW) — REGISTER, CHANGES REQUESTED

**Why REGISTER (not CUT):** The minimal-criminal setup is sound and genuinely new. Well-ordering gives a smallest governing prime q > M_1 if any exists (this is the standard minimal-criminal on the smallest element — NOT the witness-density-recurrence rescue, which failed because its "induction on the order of governing primes > M_1" pushed UP and was not well-founded; here there is no upward induction, just a single contradiction on the smallest q). Steps 1–6 (well-ordering, (M_1,q) transient by minimality, q | infinitely many a_n, local walk mod q with forced d_n ≤ M_1 < q at q-multiple steps, cofactor-transversal structure, P_1-linchpin always transverses) are all sound and follow from `linchpin-and-gap-bound` + `binfinity-divisibility-progression-structure` + arithmetic. The contradiction SHAPE (minimal-criminal + Schur cofactor-prime-finiteness) is NOT in the 10+ dead list (strip/cofactor, monovariant, density, CRT-lift, free-rider, residue-statistic, substitution/morphic, ergodic-window, increment-automaton, pure statics, p-adic). It is the genuinely-new door the stall rule demanded.

**Why CHANGES REQUESTED (two unproved cruxes the builder must close or certify dead):**

- **Crux A (transient-death).** Step 7 Candidate A requires "every prime p > M_1 stops dividing cofactors k_i after finitely many q-multiples." The outliner honestly admits this is "possibly as hard as Gap A." I flag a sharper concern the outliner under-stated: there are TWO DIFFERENT notions of "transient" in play, and minimality of q gives only one of them.
  - **MT-transient** (what minimality of q actually gives for primes in (M_1,q)): p drops out of MT(F_∞) eventually. This is the established meaning.
  - **Cofactor-transient** (what Schur needs): p stops dividing k_i = a_n/q eventually.
  - These are NOT the same. A prime p ∈ (M_1,q) being MT-transient (not in the eventual MT) does NOT imply p stops dividing cofactors k_i — p could divide infinitely many a_n (hence infinitely many k_i at q-multiple indices) while not being governing (p redundant in the eventual transversal sense). My computation (136/242 q-multiples for a1=15,q=3 have a cofactor-prime > M_1) is consistent with this: large primes persist in k_i. **The builder must either prove MT-transient ⇒ cofactor-transient (a genuinely new bridge, not available from existing lemmas), or prove cofactor-transient directly by a greedy-dynamic argument, or show the two notions coincide under the minimal-criminal hypothesis.** If none of these hold, the framing dies and must be certified with a negative lemma explaining WHY no Schur-style contradiction ports (the value would be fencing off future Schur/minimal-criminal retries).

- **Crux B (the Schur step itself).** The crux `aimo-0727` is "in the WRONG direction" (the outliner's own words): it proves a cofactor UNBOUNDED from infinite-prime-divisors; we want the contrapositive (fixed-finite prime set ⇒ k_i trivial ⇒ contradicts unboundedness). Classical Schur (finitely many prime divisors ⇒ the sequence is bounded ONLY for polynomial-driven sequences) does NOT apply to the greedily-generated (k_i) which is not polynomial-driven. The builder must either (i) exhibit the specific mechanism in `aimo-0727` that makes "fixed-finite prime set ⇒ trivial" work for THIS sequence and prove it from scratch (every borrowed step must be re-proven per CLAUDE.md), or (ii) find a different contradiction (Candidate B is weak — the walk mod q is not a closed finite state, per the round-3 finite-statistic explorer; do not pursue unless a genuinely-closed finite state mod q is found).

**Fences cleared:** NOT a strip/cofactor bound (the contradiction never invokes "cofactor of smallest admissible q-multiple ≤ M_1"); NOT aimo-0134 (no monovariant); NOT pure statics (uses greedy order + local walk); NOT CRT-lift (no fiber-counting). The `syndetic-divisible-closed-not-periodic` guardrail is respected (the contradiction is greedy-dynamic). REGISTER at cold-start 1500.

## Approach 2: `primal-minimal-support-stabilization` (NEW) — REGISTER, CHANGES REQUESTED

**Why REGISTER (not CUT):** The outliner ACKNOWLEDGES this is EQUIVALENT to Gap A (primal = dual, per the round-4 increment-induction explorer). Per the stall rule this is acceptable ONLY IF the stabilization uses a genuinely non-cofactor greedy mechanism. There IS one new ingredient not present in the dual MT bound: the **window-uniqueness** argument (Step 4 candidate (a)) — because d_n ≤ M_1, the carrying term m lies in a window [a_n+1, a_n+M_1] of size M_1, so a prime q > M_1 dividing m means at most ONE q-multiple lies in the window, uniquely determined by a_n mod q; greedy-minimality then asks whether that unique q-multiple is the SMALLEST admissible m. This window-local lever is genuinely not in the dual MT bound (which never used q > M_1 > window size). So it is NOT "just the dual MT renamed." The negative-lemma fallback (certify "primal ≡ Gap A") is itself valuable progress in a deep stall.

**Why CHANGES REQUESTED (the crux to close):**

- **The admissibility check re-enters the cofactor bound.** This is the skeptic's note and I confirm it is load-bearing. "Is the unique q-multiple m = kq admissible" = "does S(m) = {q} ∪ primefactors(k) hit every current minimal support" = "primefactors(k) transverses the current minimals not containing q." Bounding primefactors(k) IS the cofactor-bound step certified dead for witness-density-recurrence (round 2) and crt-period-lifting (round 3). So the window-uniqueness argument, when unpacked, lands back on the cofactor-bound wall — UNLESS the builder exhibits a greedy-dynamic ingredient that exploits "smallest m in the window" beyond "is the q-multiple admissible."

- **The builder's job is precisely to find that ingredient.** Candidate directions worth testing: (a) when the unique q-multiple is NOT the smallest admissible m, the greedy picks a smaller m whose support AVOIDS q — quantify how often this happens and whether it forces q to die; (b) track the life-cycle of a prime q > M_1 that ever enters MS (it must die, else governing by definition) and exhibit the death mechanism. If neither yields a non-circular bound, the approach founders and the builder MUST certify the negative lemma "primal-minimal-support-stabilization ≡ Gap A (no non-cofactor greedy-minimality argument exists in the primal that the dual MT lacks)" — this is the explicit fallback and it IS the round's contribution (fences off future primal retries).

**Fences cleared:** NOT the dual MT bound (window-uniqueness is new); NOT strip/cofactor (does not invoke "cofactor of smallest admissible q-multiple ≤ M_1" as a bound — though the admissibility check threatens to re-enter it, which is the flagged risk); NOT aimo-0134; NOT pure statics (greedy rule is load-bearing); `syndetic-divisible-closed-not-periodic` guardrail respected. REGISTER at cold-start 1500.

**Diversity-of-thought check:** The two new approaches are close but not identical — minimal-criminal is a CONTRADICTION on the smallest governing q (Schur cofactor-finiteness), primal is a DIRECT stabilization (greedy-minimality forces primes small). They share a dependency: primal's window-uniqueness candidate (a) explicitly links to minimal-criminal Step 5 (cofactor-transversal structure). If the cofactor-transversal/admissibility wall is the SAME wall for both, they could fail together. I flag this: the field has NOT collapsed to one framing (transversal-saturation/prime-power-dichotomy remain distinct certified-lemma sources; p1-equals-2-direct is a distinct base-case specialization), but the two NEW approaches do share a sub-wall (cofactor-transversal admissibility). The builder for each must diversify the gap-fill mechanism, not re-derive the same cofactor argument in two costumes.

## Approach 3: `p1-equals-2-direct` (ADVANCE) — APPROVE for build

The certified foundation (`two-entry-lemma`, `P1-minimal-transversal-lemma`) is sound and reviewer-verified. The ADVANCE re-uses the minimal-criminal + Schur skeleton SPECIALIZED to |P_1|=2, where the structure is tightest (M_1 = p·q, two small primes, the 2-element transversal {p,q} is always available as the linchpin). The 2-density mechanism is correctly marked REFUTED (a1=15: a9=45 odd, v_2 fluctuates) — do NOT revive it. The crux (Step 4, the |P_1|=2-specialized transient-death) is the SAME crux as minimal-criminal Step 7; the outliner correctly notes they are coupled ("if one cracks it, both benefit"). Even an UNCONDITIONAL |P_1|=2 solve shrinks the theorem to |P_1|≥3 — genuine partial progress either way. APPROVE. The builder should attack the |P_1|=2 specialization first (smallest, tightest), and report whether the |P_1|=2 leverage yields a transient-death argument the general case lacks.

## Retirements

- **`integer-monovariant-transfer` → RETIRE confirmed.** The `aimo-0134-obstruction` certified negative lemma fences it (constant gap bound ⇒ no shrinking-range integrality upgrade; C_n unbounded non-LOCK; b_avg non-monotone a1=15). Keep the certified sub-lemmas `block-index-advance` + `aimo-0134-obstruction` in the cache; do not re-attempt the aimo-0134 template. The ranker entry stays (dead records are population memory); I clear its `stale` flag and rank it below all live approaches.
- **`growing-modulus-descent`, `witness-density-recurrence`, `free-rider-type-replacement`**: already retired rounds 2–3; keep negative lemmas certified. Confirmed.
- **`transversal-saturation`, `prime-power-dichotomy`, `crt-period-lifting`**: kept as certified-lemma sources, NOT built this round. `stale` flags cleared. crt-period-lifting's cofactor-lift mechanism stays dead (do not re-attempt).

## Ranking (head-to-head, anchored to last outcomes)

Field post-review (live approaches above dead):

1. transversal-saturation (partial, certified endgame+foundation, lemma-source) — top.
2. prime-power-dichotomy (partial, LOCK certified, dichotomy) — second.
3. p1-equals-2-direct (partial, two certified lemmas, smallest open base, ADVANCED this round) — third.
4. minimal-criminal-schur-contradiction (NEW, genuinely-new open door, two open cruxes) — ranks alongside p1 (draw): p1 has certified progress, minimal-criminal is the broader genuinely-new general door; they share the crux.
5. crt-period-lifting (partial, F1/F2 certified, cofactor mechanism dead) — below the live doors.
6. primal-minimal-support-stabilization (NEW, ≡ Gap A, mechanism unpacks to cofactor-bound, negative-lemma fallback) — below crt (crt has certified reusable lemmas; primal's mechanism is closer to circular).
7. integer-monovariant-transfer (dead, retired this round) — below all live.
8. witness-density-recurrence (dead).
9. growing-modulus-descent (dead).
10. free-rider-type-replacement (dead).

New approaches registered at cold-start 1500; the comparisons below anchor them to the established field (a dead `last_outcome` loses to a live sibling; a partial with certified lemmas beats a fresh open door with no certified progress yet).

## Verdicts summary

- `minimal-criminal-schur-contradiction`: REGISTER, CHANGES REQUESTED (two open cruxes: transient-death with the MT-transient-vs-cofactor-transient gap; the Schur step itself in the wrong direction and must be re-proven from scratch for the greedily-generated (k_i)).
- `primal-minimal-support-stabilization`: REGISTER, CHANGES REQUESTED (the admissibility check re-enters the cofactor bound; the builder must exhibit a genuinely-new greedy-dynamic ingredient exploiting "smallest m in the window" beyond "is the q-multiple admissible," OR certify the "primal ≡ Gap A" negative lemma).
- `p1-equals-2-direct`: APPROVE (advance; attack the |P_1|=2 specialization of the minimal-criminal crux first).
- `integer-monovariant-transfer`: RETIRE confirmed (fenced by `aimo-0134-obstruction`).

## Candid assessment

The outliner's own honest verdict ("No — I do NOT believe a breakthrough is reachable this round, and the wall is likely genuinely impenetrable with the current arsenal") is the right one. The two new approaches are put up NOT to solve but to (i) satisfy the stall-rule requirement of challenging the gap with a genuinely-new door, and (ii) each carry an explicit negative-lemma fallback that, if the builder founders, sharpens the wall's characterization (primal ≡ Gap A; Schur-premise-fails-via-transient-primes). Even a non-solve adding 2 negative lemmas is genuine progress on a problem where 10+ mechanisms are already dead. The live empirical target (q ≤ M_1 = rad(a_1), 100+ cases 0 failures) stands un-proven; the minimal-criminal + Schur contradiction is the most promising remaining attack on it, but the transient-death crux is the wall.

build set: minimal-criminal-schur-contradiction, primal-minimal-support-stabilization, p1-equals-2-direct
