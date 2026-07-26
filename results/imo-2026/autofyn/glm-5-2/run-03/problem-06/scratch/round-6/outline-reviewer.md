# imo-2026-06 — round 6 outline review

## Field state (independent re-verification)

Round 5 left a 12-slug population, 28 certified lemmas, 4 structural fences, ~13 dead mechanisms, and the theorem reduced to Gap A (conditional endgame + LOCK + pure-from-start + conditional bridge all certified). Round 6 dispatched three explorers (analytic-growth / Ramsey-vdW / extremal-variational); all three returned NO-UNFENCED-ROUTE. The outliner honestly reports NO genuinely-unfenced approach to open and nominates two genuinely-new negative structural lemmas for certification.

I independently re-ran the corrected MT-greedy (`/tmp/round-6/mt_greedy.py`, bit-exact vs naive on a1∈{15,385,847}) and re-checked the four dismissed candidate areas. Findings below.

## Independent verification of the two negative lemmas

### no-fixed-modulus-forward-determinism — VERIFY (with one number to fix)

Re-ran a1=175, mod=a1²=30625, N=60000 with the corrected MT-greedy:
- realized states = **9625** / 30625 — matches the explorer exactly. Real repeats exist (realized < state space), so the non-forward-determinism is genuine, not a coverage artifact.
- conflict states (states with ≥2 distinct successors): my count is **4611** (N=60000) / **4447** (N=50000). The explorer reported **3498**. The realized count matches exactly, but the conflict count does NOT match either definition I could reconstruct (≥2 successors, or ≥2 successors among states appearing ≥2 times — both give the same number since every realized state repeats). The qualitative conclusion (thousands of conflicts ⇒ a_n mod a1² is genuinely NOT forward-deterministic) is robustly confirmed and even *strengthened* by my higher count, but the exact number 3498 in the outline is not reproducible.

**Structural argument (sound):** the greedy transition is defined as "smallest m>a_n with gcd(m,a_i)>1 ∀ i≤n" — admissibility depends on the FULL constraint history {a_1,…,a_n}, not on a_n alone. So for ANY fixed modulus m, a_n mod m is a lossy projection that provably collapses distinct histories. This is true by definition; the a1=175 witness exhibits it concretely. The a1=847 mod a1² row IS an artifact (realized=N-1=49999 ≪ state space 717409; no state has repeated yet, so trivially single-successor — not forward-determinism, just insufficient horizon). The outline already flags this correctly; the builder must NOT cite the 847 row.

**Genuinely new vs the round-5 T-unbounded-in-M1 fence:** YES. The round-5 fence covers f(M1)-bounded deterministic statistics (rad-77 witness: a1=77→T=18 vs a1=847→T=1744 at the same M1=77, so no f(M1)-bounded state can force periodicity). The new lemma extends this to a1-bounded and a1²-bounded residue statistics — which are NOT f(M1)-bounded (a1=77 vs a1=847 share M1=77 but a1²=5929 vs 717409, 120× apart). The structural reason (history-dependence) is also a cleaner articulation than the rad-77 period-jump. Not subsumed.

**Verdict: APPROVE for certification** as a structural negative lemma with computational witness (precedent: `monovariant-non-monotonicity` certified with a1=116 witness). **CHANGES note to the builder:** report the conflict count from a fresh independent run (4611 at N=60000 in my verification, NOT the explorer's 3498 which I could not reproduce); state the lemma as "no residue statistic a_n mod m at ANY fixed modulus m (incl. m=a1, a1·M1, a1²) is forward-deterministic" with the structural argument as the primary justification and the a1=175/mod-a1² computation as witness evidence. Do not cite the a1=847 mod a1² row.

### D_n-slack-obstruction — VERIFY (sound)

Re-ran a1=15 (M1=15), N=30, naive admissibility check on the MT-greedy orbit:
- |D_n| over the first 29 steps: [7, 6, 2, 2, 4, 5, 5, 4, 4, 3, 2, 2, 4, 5, 5, 4, 4, 3, 2, 2, 4, 5, 5, 4, 4, 3, 2, 2, 4]. After the n=0,1 transient, the stabilized period (T=8) shows |D_n| ∈ {2,3,4,5} — min=2, matching the explorer's [2,5] for a1=15 exactly. The greedy minimum is one choice among multiple admissible increments; slack is omnipresent in the period.

**Structural argument (sound):** the admissible-increment set D_n is a transversal/hitting condition (a_n+d admissible iff its prime-factor set hits every prior term-support); many small increments satisfy a hitting condition against a bounded family, so |D_n|≥2 generically. The a1=175 case (min=1 in the period) shows the claim must be stated as "≥2 at almost every step / with positive density in the period," NOT "≥2 everywhere" — the outline flags this correctly.

**Genuinely new vs prior fences:** YES. No prior fence covered the variational/"greedy = forced extremum"/"no-improvement ⇒ fixed point" sub-class (the extremal lens was not scouted before round 6). The cofactor, finite-state, coincidence-doubling, deviation-descent fences do not address the variational principle. Not subsumed.

**Verdict: APPROVE for certification** as a structural negative lemma with computational witness across 5 starting values. **CHANGES note to the builder:** state the lemma as "≥2 almost everywhere" (not "everywhere"), citing the a1=175 min=1 counterexample to the stronger claim; note additionally that the realized D_n-pattern set for a1=175 (75) is a PROPER SUBSET of one period (T=274), so the D_n-state is not a bijection onto the period — consistent with the no-fixed-modulus lemma above (the D_n-state is also not a forward-deterministic determining state).

## Independent verification of the outliner's "no genuinely-unfenced approach" verdict

I checked each of the four dispatch-suggested candidate areas against the fenced list and the two new negative findings. I agree with the outliner on all four.

**(a) Period characterization (M1|L, characterize L/T).** I re-confirmed M1|L empirically: a1=175 gives T=274, L=2730=78·35=78·M1 (my MT-greedy run); the round-5 records a1=15 L=30=2·15, a1=35 L=210=6·35, a1=847 L=18942=246·77. But L and T are the CONCLUSION's parameters — literally the slope and period the theorem asserts. They are undefined until periodicity is established. Proving M1|L without first proving periodicity is circular (it presupposes the conclusion). The slope L/T varies wildly (3.75, 6.18, 8.56, 9.10, 9.96) with no function of M1, so no clean candidate (L,T) is constructible from a1 alone. **FENCED (Gap-A-circular + analytic/density). Agree.**

**(b) Factorization-induction with a non-cofactor step.** Every step mechanism either needs a cofactor bound (fenced: `window-uniqueness-reduces-to-cofactor`, `lemma-C-strip-no-go`, `schur-cofactor-premise-fails-in-periodic-regime`) or a quotient descent (CERTIFIED DEAD: "drop a prime r" sub-sequence ≠ greedy(a1/r), a1=385 r=11, round 3). The CRT fiber-lift induction (aimo-0231) is certified circular. The new no-fixed-modulus finding (verified above) kills any induction that reads the next state from a fixed residue statistic of a1. **FENCED. Agree.**

**(c) Model-theoretic / compactness.** The greedy rule is a recursion with minimization over a GROWING constraint set — not first-order expressible in (Z,+,·) in a way admitting QE to a finite state. More decisively: the no-fixed-modulus finding (verified above) shows the transition a_n→a_{n+1} depends on the FULL constraint history {a1,…,an}, so the only forward-deterministic determining state is the MT-state (full constraint-set history) — whose finiteness IS Gap A. A compactness/QE argument reducing the theory to a finite state is exactly the fenced finite-pigeonhole-state route (T-unbounded-in-M1 impossibility). **FENCED. Agree.**

**(d) Diophantine approximation on the slope L/T.** The slope is undefined pre-periodicity; the asymptotic growth rate a_n/n is the average of d_n∈{1,…,M1}. a_n mod q is empirically equidistributed (freq = M1/q) but this CANNOT distinguish governing q from transient q (transients realize the same M1/q window frequency) — the analytic explorer already showed this. The contradiction half is the certified-circular covering-capacity argument (round 2). **FENCED. Agree.**

**Conclusion: I concur with the outliner. There is NO genuinely-unfenced approach to open this round.** The bar ("not in 13-dead/4-fence list, not collapsing to any fence, not killed by the two new negative findings") is not met by any direction the three explorers scouted or by the four candidate areas above. I did not find a framing the outliner missed.

## The round-6 field

- **no-fixed-modulus-forward-determinism** — NEW negative structural lemma (APPROVE for certification, with the conflict-count CHANGES note above). Not a whole-problem approach; a fence write-up. Genuinely new (extends T-unbounded fence to a1-bounded and a1²-bounded residue statistics; structural reason = history-dependence of the greedy transition).
- **D_n-slack-obstruction** — NEW negative structural lemma (APPROVE for certification, with the "almost everywhere" CHANGES note above). Not a whole-problem approach; a fence write-up. Genuinely new (fences the variational "greedy = forced extremum" sub-class, not previously scouted).
- **p1-equals-2-direct** — NO ADVANCE (fenced). The only open step is the cofactor wall for |P1|=2 NON-LOCK = Gap A specialized to |P1|=2. The new no-fixed-modulus fence kills any residue-statistic sub-step for |P1|=2 too (the a1=175/mod-a1² witness is itself a |P1|=2 NON-LOCK case: a1=175=5²·7, M1=35). Status remains CHANGES-REQUESTED (open cofactor wall); should be marked as a fenced specialization in current.md rather than re-attacked. Agree with outliner.
- **two-coincidence-periodicity, deviation-index-descent** — stale=true, dead-end (round 5). No revision productive (antecedents IS the wall / double-fenced). Sink in ranking.
- **minimal-criminal-schur-contradiction, primal-minimal-support-stabilization** — no revision (Schur Step 7 dead 2 rounds; primal ≡ Gap A). Keep as mount/lens.
- **transversal-saturation, prime-power-dichotomy, crt-period-lifting** — lemma sources (certified conditional machinery). Stay high.
- No new whole-problem approach opened. No copies productive (no live approach has two viable ways to fill the same gap — all open gaps are the single fenced wall).

## Shared-wall note (for the orchestrator)

The entire population now bottoms out on ONE wall (Gap A = finiteness of governing primes ⊆ primes ≤ M1 = rad(a1)). This is the 6th round on that wall; 15+ mechanisms dead; 4→6 structural fences after this round's certifications. The field is genuinely collapsed to one framing — not because the approaches are lazy, but because every genuinely-different framing scouted (analytic, Ramsey, extremal, p-adic, finite-state, coincidence-doubling, deviation-descent, substitution/morphic, ergodic-window, Schur, primal, CRT, monovariant×2, density, strip, cofactor, free-rider, modular-residue) reduces to the same wall. The honest deliverable is the partial result (conditional proof + LOCK + endgame + 30 lemmas + 6 fences), NOT another variation. The orchestrator should treat round 7 as consolidation unless a genuinely-unfenced mechanism is surfaced — and none is currently on the table.

## Ranking (head-to-head, anchored to last outcomes)

No new approaches to register (outliner opened none). No copies. Ranking the existing 12-slug field. The two round-5 stale dead-end approaches (two-coincidence-periodicity, deviation-index-descent) sink below every live approach; the lemma-source trio stays on top; p1-equals-2-direct (advanced but fenced) holds below the lemma sources.

Comparisons (each anchored: live partial > dead-end; advanced > dead-end; lemma-source top > lemma-source next):

- transversal-saturation > two-coincidence-periodicity (live partial lemma-source vs stale dead-end)
- transversal-saturation > deviation-index-descent (live partial vs stale dead-end)
- prime-power-dichotomy > two-coincidence-periodicity (live partial lemma-source vs stale dead-end)
- prime-power-dichotomy > deviation-index-descent (live partial vs stale dead-end)
- crt-period-lifting > two-coincidence-periodicity (live partial lemma-source vs stale dead-end)
- crt-period-lifting > deviation-index-descent (live partial vs stale dead-end)
- p1-equals-2-direct > two-coincidence-periodicity (advanced vs stale dead-end)
- p1-equals-2-direct > deviation-index-descent (advanced vs stale dead-end)
- minimal-criminal-schur-contradiction > two-coincidence-periodicity (partial live mount vs stale dead-end)
- minimal-criminal-schur-contradiction > deviation-index-descent (partial live mount vs stale dead-end)
- two-coincidence-periodicity vs deviation-index-descent: draw (both stale dead-end, same round)
- transversal-saturation > prime-power-dichotomy (top lemma-source, more selected, higher certified machinery density)
- prime-power-dichotomy > crt-period-lifting (higher, more recent certified conditional content)

## Build set

No approach-advancement builders this round (p1-equals-2-direct fenced; no live advance; no new approach opened). The build set is the two negative-lemma certification tasks — one builder each writes the lemma file, the reviewer certifies. The builders must observe the CHANGES notes (correct conflict count for no-fixed-modulus; "almost everywhere" phrasing + a1=175 min=1 caveat for D_n-slack).

build set: no-fixed-modulus-forward-determinism, D_n-slack-obstruction
