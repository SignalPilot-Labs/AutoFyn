# Outline review — imo-2026-03, round 1

All three approaches target the whole claim (both bounds of c(n) = 2^n/(2^{n+1}-1)) end to end — no fragment slugs, no single-gap split. Field diversity is genuine: three distinct lower-bound mechanisms (merge-induction / parity+rounding / tie-enumeration) and two distinct upper-bound mechanisms (pairing recursion / response averaging). Residual overlap: GAP III (pairing-exchange-normal-form) ≈ GAP 4 (geometric-cascade-induction) — the leftover invariant — is shared; parity-alternating-sum's averaging upper bound is the hedge, correctly identified by the outliner.

## Numerical verification I ran (all exact or high-trial random search)

1. **Merge Lemma (GAP 1 of geometric-cascade-induction) is FALSE as stated** — both in general and in the restricted setting actually used. General counterexample: P = (49, 32), Q = (42, 31, 25, 14): oddsum(P∪Q) = 106 < σ(P)/2 + oddsum(Q) = 40.5 + 67 = 107.5. Restricted counterexample (n = 3, P = even-count fragments of 8, Q = uncut {4,2,1}): P = (5.108, 1.322, 0.453, 1.118), oddsum(P∪Q) = 8.678 < 4 + oddsum(Q) = 9. ~40% of random restricted instances fail. The lemma fails because it charges Q at its *actual* oddsum, which can exceed L(n-1); the final target oddsum ≥ 2^n held in every failing instance, so the *conclusion* of the induction survives, but the inductive step as written does not factor through oddsum(Q).
2. **The lower-bound claim itself checks out**: exact integral enumeration and 100k-trial continuous random search both give min oddsum = 2^n for n = 1, 2, 3, and **integral optima exist** ((2,1)→[2,1]; n=2 → [3,2,1,1]; n=3 → [5,4,2,2,1,1]) — direct support for the parity approach's Rounding Lemma. No non-integral response beat 2^n.
3. **The greedy pairing algorithm as literally specified fails for n ≥ 3**: e.g. n=3, p = (0.4608, 0.2307, 0.1561, 0.1524) gives greedy leftover r = 0.0740 > 1/15, i.e. LB value 0.5370 > 8/15 = 0.5333. Also n=4: p = (0.4388, 0.2228, 0.1296, 0.1271, 0.0817) → 0.5203 > 0.5161. **But the optimal XY still meets the target on those same configs** (300k-trial search: 0.5054 ≤ 0.5333 etc.), so the conjectured answer is NOT contradicted — the Leftover Lemma needs XY to deviate from naive greedy, exactly as GAP III / GAP 4 anticipated. These counterexample configs are concrete test data for the strengthened invariant; builders should record them.

## Verdicts

### parity-alternating-sum — APPROVE
The strongest skeleton. The parity observation (integer pieces, odd total D ⟹ A ≡ 1 mod 2, A ≥ 0 ⟹ A ≥ 1) is verified and decisive; the budget caveat (GAP A': parity false for > n cuts) is correctly flagged, which is the trap a careless version would fall into. My check 2 confirms integral optima exist for n ≤ 3, so the Rounding Lemma is empirically true where tested. Issues for the builder:
- GAP A: the TU/interval-matrix mechanism is sketched, not established — the tie system's constraint matrix must actually be exhibited as an interval matrix; the alternative "slide to nearest tie + induct on non-integral cuts" may be easier. Also the "never cut the unit piece" sub-claim needs its own swap argument (cutting the smallest piece never decreases oddsum) — prove it, don't cite numerics.
- Sliver/endpoint limits: deleting a cut is legal (≤ n marks), state this explicitly when taking ε → 0 limits.
- GAP B (averaging weights): do n = 1 and n = 2 fully by hand before generalizing. If averaging stalls, this slug may import slug 3's upper bound once certified — but do not merge the slugs.

### pairing-exchange-normal-form — APPROVE
The most concrete. Normalization (GAP I) via piecewise linearity is a standard and sound smoothing argument; tie-pattern rigidity from distinct subset sums of powers of 2 (GAP II) is a plausible mechanism but the enumeration must be provably exhaustive — the outline says so itself. Issues:
- GAP III: my check 3 confirms the naive greedy in step "Repeat until…" is refuted for n ≥ 3 (configs above). The Leftover Lemma must be restated as "XY has SOME cutting strategy achieving r ≤ 1/D", with the greedy only a guide. Builder: use my counterexample configs plus the outline's (0.45, 0.15, 0.1×4) as the test suite for the strengthened invariant; the "σ-bound OR spare-cut" disjunctive hypothesis and the 2p_1 − σ potential are both worth testing computationally before proving.
- GAP II enumeration: run exact rational enumeration for n = 2, 3, 4 first (my check 2 gives the n ≤ 3 optima to validate against).
- Whoever proves Lemma 0 and the Pairs Lemma first must certify them in `lemmas/` — every approach depends on them.

### geometric-cascade-induction — CHANGES REQUESTED (do not build this round)
The framing (induction on n via self-similarity) is legitimate, but its load-bearing GAP 1, the even-case Merge Lemma, is **false as stated** (check 1, counterexamples above) — the "6+ hand cases" in the file were equality cases that masked the failure. The inductive step 3 cannot chain through oddsum(Q); it must be reworked into a joint statement over (P, Q) — e.g. "for all even-count partitions P of 2^n and all legal Q, oddsum(P∪Q) ≥ 2^{n-1} + L(n-1)" proved directly, or a corrected merge inequality with a weaker functional of Q. Until the outliner repairs step 3, building would waste a builder on a refuted lemma. GAP 4 (upper bound) is identical to GAP III of pairing-exchange-normal-form, so nothing is lost by parking this slug: if slug 3 cracks the leftover invariant it is certified as a shared lemma. Send back to the outliner next round with the counterexamples above; the approach file should record the falsification so no builder relies on the current Merge Lemma.

## Ranking (registered + Elo updated)

- pairing-exchange-normal-form (1517) — draw with parity slug; both beat geometric-cascade-induction.
- parity-alternating-sum (1514)
- geometric-cascade-induction (1469) — load-bearing lemma falsified, needs re-plan.

Comparisons applied: parity > geometric, pairing > geometric, parity = pairing (draw).

## Diversity note for the orchestrator
The field is healthy: two live slugs with disjoint failure modes (parity/rounding vs normalization/enumeration for the lower bound; averaging vs invariant-pairing for the upper). Watch the shared leftover-invariant gap (GAP III/GAP 4): if both invariant-based upper bounds stall on it for 2+ rounds while averaging (GAP B) also stalls, demand a genuinely new upper-bound framing.

## Instructions to builders
- parity-alternating-sum builder: certify Lemma 0 + Pairs Lemma in `lemmas/` first; then attack GAP A (rounding) — exact enumeration for n ≤ 3 is already validated (integral optima [2,1], [3,2,1,1], [5,4,2,2,1,1]); then GAP B by hand for n = 1, 2.
- pairing-exchange-normal-form builder: record the greedy counterexamples (n=3: (0.4608, 0.2307, 0.1561, 0.1524); n=4: (0.4388, 0.2228, 0.1296, 0.1271, 0.0817)) in the approach file; search computationally for the true invariant of the Leftover Lemma before proving; run the exact tie-pattern enumeration for n ≤ 4.

build set: parity-alternating-sum, pairing-exchange-normal-form
