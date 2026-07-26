# imo-2026-06 — round 6 outline (CONFIRMED STALL, 5 rounds on Gap A)

## Honest field assessment

Three round-6 explorers fanned out across analytic/growth, Ramsey/vdW, and extremal/variational lenses. **All three returned NO-UNFENCED-ROUTE.** Two surfaced GENUINELY-NEW negative structural findings (not subsumed by the existing 4 fences); none surfaced a positive crack.

I checked each of the four dispatch-suggested candidate areas against the fenced list and the two new negative findings. Verdict on each, honestly:

**(a) Number-theoretic structure of the PERIOD (characterize L/T, prove M_1 | L).** COLLAPSES TO GAP A. `L` and `T` are not defined until periodicity is established — they are the *conclusion* of the theorem, not a priori objects. The empirical fact `M_1 | L` (verified: a_1=15 L=30, a_1=35 L=210, a_1=175 L=2730, a_1=847 L=18942 — all multiples of M_1) is a *consequence* of Gap A (under Gap A, L = rad(governing set); P_1 ⊆ governing empirically, so rad(P_1)=M_1 | L). Proving `M_1 | L` *without* first proving finiteness of the governing set presupposes the conclusion. Exhibiting a candidate (L,T) directly from a_1: the slope L/T varies wildly (3.75, 6.18, 8.56, 9.10, 9.96 across a_1∈{15,35,77,91,175}) with no function of M_1 — so no clean candidate exists, and even characterizing the slope gives growth-rate info, not periodicity (the analytic explorer already showed equidistribution + growth rate cannot distinguish governing from transient primes). **FENCED (analytic/density + Gap-A-circular). Do not open.**

**(b) Induction on the prime factorization of a_1 with a NON-cofactor step mechanism.** COLLAPSES TO FENCED ROUTES. The step "greedy(a_1·p) relates to greedy(a_1)" requires either a cofactor bound (fenced: `window-uniqueness-reduces-to-cofactor`, `lemma-C-strip-no-go`, `schur-cofactor-premise-fails-in-periodic-regime`) or a quotient descent (CERTIFIED DEAD: "drop a prime r" sub-sequence ≠ greedy(a_1/r), verified a_1=385 r=11, round-3 induction-on-P1 explorer rule). The CRT fiber-lift induction (aimo-0231) is certified circular (`crt-period-lifting` round 3). The Ramsey explorer's new structural finding (transition depends on FULL constraint history, not on any fixed-modulus residue — see new fence below) kills any induction that reads off the next state from a fixed residue statistic of a_1. No non-cofactor step mechanism survives. **FENCED. Do not open.**

**(c) Model-theoretic / compactness (orbit = unique model of a theory; periodicity by QE).** COLLAPSES TO THE FORWARD-DETERMINISTIC / T-UNBOUNDED FENCE. The greedy rule is a recursion with minimization over a growing constraint set — not first-order expressible in (Z,+,·) in a way that admits QE down to a finite state. The Ramsey explorer's new structural proof (new fence below) shows the transition a_n→a_{n+1} depends on the FULL constraint history {a_1,…,a_n}, so the only forward-deterministic determining state is the MT-state (full constraint-set history) — whose finiteness IS Gap A. A compactness/QE argument reducing the theory to a finite state is *exactly* the fenced finite-pigeonhole-state route (T-unbounded-in-M_1 impossibility, round 5). **FENCED. Do not open.**

**(d) Diophantine approximation / continued-fraction on the slope L/T.** COLLAPSES TO THE ANALYTIC/DENSITY FENCE. The slope is undefined pre-periodicity; the asymptotic growth rate a_n/n is the average of d_n ∈ {1,…,M_1}. The analytic explorer already showed: a_n mod q is empirically equidistributed (freq(W_q) = M_1/q) but this CANNOT distinguish governing q from transient q (transients realize the same M_1/q window frequency), so no Diophantine-approximation inequality on the slope separates "q > M_1 governing" from "q > M_1 transient." The contradiction half is the certified-circular covering-capacity argument (round 2). **FENCED. Do not open.**

**Conclusion: there is NO genuinely-unfenced approach to open this round.** The bar ("not in 13-dead/4-fence list, not collapsing to any fence") is not met by any direction the three explorers scouted or by the four candidate areas above. The honest round-6 deliverable is: certify the two new negative findings as fences, append them to the consolidation, and keep the partial result as the run's standing deliverable.

---

## The field

### no-fixed-modulus-forward-determinism: NEW (negative structural lemma — nominate for certification)

**Target (lemma-level, not a whole-problem approach):** Certify the structural negative lemma that NO residue statistic a_n mod m at ANY fixed modulus m (including m = a_1, a_1·M_1, a_1²) is forward-deterministic for the greedy transition; the only forward-deterministic determining state is the full MT-constraint history, whose finiteness IS Gap A.

**Technique:** Structural proof from the greedy rule's definition + computational counterexample.

**Skeleton:**
1. The greedy transition a_n → a_{n+1} is defined as "smallest m > a_n with gcd(m, a_i) > 1 for every i ≤ n" — the admissibility depends on the FULL constraint history {a_1,…,a_n}, not on a_n alone. — by definition of the greedy rule.
2. For ANY fixed modulus m, two different histories can produce the same a_n mod m but different admissible-next sets (hence different a_{n+1} mod m). — by exhibiting a concrete counterexample.
3. Counterexample: a_1 = 175, m = a_1² = 30625. Compute the greedy orbit; among the realized states a_n mod 30625, there are 3498 conflict states (states with ≥ 2 distinct realized successors) — verified by the corrected MT-greedy at /tmp/round-6/mt_greedy.py (bit-exact vs naive gcd-greedy on a_1∈{15,385,847}). Real repeats exist (realized = 9625 < 30625), so the non-forward-determinism is genuine, not a coverage artifact. — by direct computation (cross-checked).
4. Corollary: the only forward-deterministic determining state is the full constraint-set state = MT(F_n); its finiteness IS Gap A. Re-derives the round-5 two-coincidence finding from the modulus side. — by structural implication.
5. This EXTENDS the round-5 T-unbounded-in-M_1 fence (which fences only f(M_1)-bounded deterministic states) to residue statistics at ANY fixed modulus (a_1-bounded, a_1²-bounded, etc.) — a clean widening. — by comparison with the certified fence.

**Key lemmas (claim + mechanism):**
- "No residue statistic a_n mod m is forward-deterministic" — because the transition depends on the full constraint history {a_1,…,a_n} by the greedy rule's definition; a_n mod m is a lossy projection that provably collapses distinct histories.
- "a_1=175, m=a_1²=30625 exhibits 3498 conflict states with real repeats" — the concrete witness (realized=9625 < state-space=30625).

**Open gaps:** The structural proof (Step 2's "two different histories with same a_n mod m but different successors") is currently exhibited computationally (Step 3) — the builder should write it up as a clean lemma file citing the computation as witness and giving the structural argument for WHY the projection is lossy. Whether a fully non-computational proof is feasible is itself the open sub-question; the lemma is certifiable as a structural fence with the computational witness as evidence (precedent: `monovariant-non-monotonicity` was certified with a computational witness a_1=116).

**Cases to cover:** none (single counterexample suffices for the negative claim).

**Watch out for:** the a_1=847 mod a_1² row is an ARTIFACT (realized = N-1 = 49999, state space 717409 ≫ N — trivially each state has one successor, not forward-determinism). The builder must NOT cite the 847 row; only the 175 row (realized=9625 < 30625, real repeats) is a genuine witness. Also must use the CORRECTED greedy (/tmp/round-6/mt_greedy.py), NOT the round-4 fast_greedy.py with the inverted-subset bug.

**Relationship to existing fences:** genuinely new. The round-5 T-unbounded-in-M_1 fence fences f(M_1)-BOUNDED deterministic states. This new lemma sharpens it: even a_1-bounded and a_1²-bounded residue statistics are not forward-deterministic — by a STRUCTURAL argument (history-dependence of the transition), not just by the rad-77 period-jump. Not subsumed.

---

### D_n-slack-obstruction: NEW (negative structural lemma — nominate for certification)

**Target (lemma-level):** Certify the structural negative lemma that the "greedy = forced extremum" / "no-improvement ⇒ fixed point" variational sub-mechanism is structurally FALSE for this process: in the periodic regime, |D_n| ≥ 2 at almost every step (the admissible-increment set has slack almost everywhere), so the greedy minimum is a tie-break by minimality, not the consequence of a forced extremum.

**Technique:** Direct computation of D_n over the stabilized periodic tail + structural interpretation.

**Skeleton:**
1. Define D_n := {d ∈ {1,…,M_1} : a_n + d is admissible w.r.t. {a_1,…,a_n}}; the greedy rule picks d_{n+1} = min D_n. — by definition.
2. Compute D_n over the stabilized periodic tail (the periodic regime, conditional on Gap A so periodicity holds) for a_1 ∈ {15,35,77,91,175}. — by direct computation (corrected greedy).
3. Result: |D_n| ∈ [2,5] (a_1=15), [4,7] (a_1=35), [7,10] (a_1=77), [8,11] (a_1=91), [1,5] (a_1=175). |D_n| ≥ 2 at almost every step in every case. — by computation.
4. Structural interpretation: the admissibility structure does NOT force the greedy value; the greedy rule is a tie-break by minimality layered on a multi-valued admissible set, not a forced extremum. — by reading off Step 3.
5. Corollary: the variational principle "no-improvement-possible ⇒ fixed point" (and any sub-class of variational arguments that relies on the greedy minimum being forced) is REFUTED — it is structurally false, not merely unproved. Fences off the entire "greedy = forced extremum" sub-class of variational framings for future rounds. — by structural implication.

**Key lemmas (claim + mechanism):**
- "|D_n| ≥ 2 almost everywhere in the periodic regime" — because at each step, multiple d ∈ {1,…,M_1} values yield admissible a_n + d (the admissibility constraint is a hitting/transversal condition that is satisfied by many small increments, not a unique one); computed directly across 5 starting values.
- "Greedy ≠ forced extremum" — because |D_n| ≥ 2 means the minimum is a choice among admissible options, not a unique forced value; the variational "no-improvement ⇒ fixed point" principle therefore has no leverage.

**Open gaps:** The "almost everywhere" qualifier (Step 3) is currently computational. The builder should write up the lemma with the computation as evidence and the structural interpretation. A clean non-computational proof that |D_n| ≥ 2 in the periodic regime (e.g. exhibiting two admissible increments by a pigeonhole/transversal argument) would strengthen it; whether that's feasible is the open sub-question, but the lemma is certifiable with the computational witness (precedent: `monovariant-non-monotonicity`).

**Cases to cover:** none (multiple a_1 across diverse M_1 suffice for the negative claim).

**Watch out for:** the a_1=175 row has |D_n| min = 1 (so the "≥ 2 everywhere" claim is FALSE — only "≥ 2 almost everywhere" holds). The builder must state the lemma as "≥ 2 at almost every step" / "≥ 2 with positive density in the period," NOT "≥ 2 everywhere." Also the a_1=175 case shows the realized D_n-pattern set (75) is a PROPER SUBSET of one period (T=274) — so even the D_n-state is not a bijection onto the period; the builder should note this as additional evidence that the D_n-state is not a forward-deterministic determining state (consistent with the no-fixed-modulus lemma above).

**Relationship to existing fences:** genuinely new. The round-5 fences cover cofactor, finite-state, coincidence-doubling, deviation-descent. The "greedy = forced extremum" variational sub-mechanism was NOT previously fenced (the extremal/variational lens was not scouted before round 6). This new lemma fills that gap. Not subsumed.

---

### p1-equals-2-direct: ADVANCE? — NO (fenced, honestly)

The dispatch asks: is there a NON-cofactor sub-step in p1-equals-2-direct worth a focused builder advance, or is it fenced?

**Honest answer: FENCED.** The approach's only open step is Step 4 (the cofactor-bound wall for |P_1|=2 NON-LOCK), which IS Gap A specialized to |P_1|=2. Every other step (1–3, 5–9) is certified. Step 9 of the approach file itself enumerates the candidate non-cofactor mechanisms ("greedy-dynamic window-uniqueness argument") — and these have ALL been fenced in rounds 3–5:
- window-uniqueness reduces to cofactor (certified `window-uniqueness-reduces-to-cofactor`).
- increment-window-automaton (round-4 fence, k_min unbounded in M_1).
- 2-density dominance (REFUTED, a_1=15 a_9=45 odd, round-3 rule).
- minimal-criminal + Schur specialization (certified dead, Step 8 of this approach).
- The new round-6 no-fixed-modulus forward-determinism fence kills any residue-statistic sub-step for |P_1|=2 too (the a_1=175 mod a_1² counterexample is itself a |P_1|=2 NON-LOCK case: a_1=175=5²·7, M_1=35).

No non-cofactor sub-step survives. **Do NOT advance p1-equals-2-direct this round.** Status remains CHANGES-REQUESTED (open cofactor wall); honestly, the approach is a specialization of the fenced wall and should be marked as such in current.md rather than re-attacked.

---

### Revisions / copies: NONE

- `two-coincidence-periodicity` (RETHINK, round 5) — certified dead (single-orbit mount collapses to Gap A + T-unbounded fence). No revision productive: the route's antecedent IS the wall.
- `deviation-index-descent` (RETHINK, round 5) — certified dead (B2 double-fenced). No revision productive without first breaking one of two fences, none broken this round.
- `minimal-criminal-schur-contradiction` (CHANGES, round 4) — Schur Step 7 certified dead; mount Steps 1–6 reusable but no non-cofactor Step 7 mechanism found in 2 rounds. No revision.
- `primal-minimal-support-stabilization` (CHANGES, round 4) — ≡ Gap A (certified `primal-dual-gap-a-equivalence`). No revision.

No copy requests: no live approach has two viable ways to fill the same gap (all open gaps are the single fenced wall).

---

### Consolidation task (reviewer-owned current.md)

The `## Full proof` section in current.md is already clean (conditional proof + LOCK + endgame + 28 lemmas enumerated by round + empirical conjecture). Round-6 consolidation append:

1. Add a **round-6 lemma batch** (after certification): `no-fixed-modulus-forward-determinism` (−, structural, sharpens T-unbounded fence to all fixed-modulus residue statistics), `D_n-slack-obstruction` (−, structural, fences variational "greedy = forced extremum" sub-class).
2. Bump the fence count: "FOUR structural fences" → "SIX structural fences" (or fold no-fixed-modulus into T-unbounded as a sharpening — but it's cleaner as a separate lemma since it covers a_1-bounded statistics the T-unbounded fence does not).
3. Add to the dead-mechanism list (~13 → ~15): "Ramsey / van-der-Waerden on d_n to force periodicity" (collapses to forward-deterministic + deviation-descent fences; long sub-T constant-d APs are SHORT, ≤25 vs T up to 1744), "extremal / variational lex-min-of-regular-tree + no-improvement-⇒-fixed-point" (collapses to T-unbounded + cofactor + D_n-slack).
4. Re-state the standing empirical conjecture q ≤ M_1 = rad(a_1) (273+ cases, 0 failures) as the open target, with the note that NO non-circular proof mechanism exists across 15+ routes and 6 structural fences.

This is a current.md edit, not a builder task; the reviewer (or orchestrator) can apply it directly. NO builder dispatch for consolidation.

---

## FIELD

- **no-fixed-modulus-forward-determinism** — NEW (negative structural lemma, nominate for certification). Not a whole-problem approach; a fence write-up. Builder writes the lemma file `results/imo-2026-06/lemmas/no-fixed-modulus-forward-determinism.md`, reviewer certifies.
- **D_n-slack-obstruction** — NEW (negative structural lemma, nominate for certification). Not a whole-problem approach; a fence write-up. Builder writes the lemma file `results/imo-2026-06/lemmas/D_n-slack-obstruction.md`, reviewer certifies.
- **p1-equals-2-direct** — NO ADVANCE (fenced; honestly state in current.md).
- No new whole-problem approach opened (no genuinely-unfenced route exists on the table or in the four candidate areas).
- No revisions, no copies.
- Consolidation append to current.md (reviewer/orchestrator applies; no builder dispatch).

**recommended build set:** `no-fixed-modulus-forward-determinism`, `D_n-slack-obstruction` (two negative-lemma write-up tasks; dispatch one builder per lemma, each told to write the lemma file for certification — these are lemma tasks, not approach-advancement). No approach-builder dispatch this round.
