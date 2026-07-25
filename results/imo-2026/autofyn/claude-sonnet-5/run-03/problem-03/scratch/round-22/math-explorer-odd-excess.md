## imo-2026-03 (GT(m) odd excess e>=3 lens)

- **Headline finding (near-complete, cheap): odd excess e>=3 is already closeable in full, with NO cardinality cap and NO case-split on the window, using machinery that is already certified.** This is a much easier case than e=1 (which needed the hard GCH(k) construction in round 21) — the round-17/18 "not attempted, deferred" status for e>=3 undersells how close it already is.

### The mechanism

Recall (round 17, certified `even-target-companion-peeling-and-corrected-qzero-chain.md`) the exact closed form for odd excess e=m-k=2t+1: `O_m = 2^k + E_k + (2^{m+1}-2^{k+2})/3`. Combined with the certified Half-Sum Corollary (`half-sum-corollary-and-large-sum-closure-theorem.md`, cap-free: OddSum(N) >= sum(N)/2 for ANY finite multiset), round 17 derived the margin identity (already algebraically verified, `/tmp/symbolic_check.py` in that round):
```
LB_odd - T_odd = 2^k/6 + 2^m/6 - a1/2 - 1/2
```
This is **affine (linear, slope -1/2) in a1 over the WHOLE range a1 in (2^{k-1},2^k]**, not just inside the width-1 window. Round 17 only ever evaluated it at the window's supremum a1->2^{k-1}+1 (needed at the time because round 15's separate Window Reduction Theorem was believed to cover everything outside the window — later round 18 found that belief was wrong for e=1). **Because the margin is monotone (linear) over the ENTIRE range, the true worst case for the WHOLE range (2^{k-1},2^k] is simply the endpoint a1=2^k** (attained, since the range is closed there) — no window-splitting needed at all.

Evaluating at a1=2^k exactly:
```
margin(2^k) = 2^k/6 + 2^m/6 - 2^k/2 - 1/2 = 2^k(2^e-2)/6 - 1/2
```
where e=m-k. For **e=1** this is -1/2 < 0 (exactly the known genuine residual near a1=2^k that round 18-21 attacked with the harder cardinality-capped GCH(k) machinery — consistent, cross-validates the formula). For **odd e>=3**: 2^e-2 >= 2^3-2 = 6 (increasing in e), so
```
margin(2^k) >= 2^k*6/6 - 1/2 = 2^k - 1/2 >= 1.5 > 0  for all k>=1.
```
So the margin is **strictly positive at the global worst point, for every k>=1 and every odd e>=3**, in one uniform algebraic step — no case split on k, no cardinality-cap argument (Half-Sum Corollary needs no bound on |D| or count), just monotonicity + one endpoint evaluation.

### Numeric stress test (exact Fraction, direct multiset computation, not just the margin formula)

I computed OddSum(D union Gamma_{m-1}) directly (not via the intermediate formula) for random D = {a1} union R with max(R) <= 2^{k-1} (sub-case (i)'s own hypothesis), a1 uniform in the FULL range (2^{k-1},2^k], R of RANDOM COUNT up to 8 pieces (deliberately no cardinality cap, unlike e=1's requirement), sum(R)=2^m-a1 exactly, k=1..5, e in {1,3,5,7}, 300 trials each:
```
(k,e)   violations/trials
(1,1)   116/300   <- known-open residual, needs cap (matches prior rounds)
(1,3)     0/300
(1,5)     0/300
(1,7)     0/300
(2,1)     6/300    <- known-open residual (a1 near 2^k, no cap)
(2,3)     0/300
(2,5)     0/300
(2,7)     0/300
(3..5, e=1,3,5,7)   0/300 for all e>=3 (and e=1 at k>=3, matching round 17-18's finding that e=1 outside the tiny (2^k-1,2^k] window and inside k>=3 was already OK before round 21's full fix)
```
Confirms: **zero violations at any tested (k,e) with e in {3,5,7}, across k=1..5, even without a cardinality cap on |R|** — matching the closed-form margin prediction exactly. Also directly computed the closed-form margin at a1=2^k symbolically for k=1..6, e in {3,5,7,9}: always positive (values from 1.5 up to thousands), matching `2^k(2^e-2)/6-1/2`.

### What this means for the outliner

- Odd excess **e=1** stays exactly as round 21 left it: fully closed via the (much harder, cardinality-cap-dependent) General Cardinality-Constrained Half-Sum Lemma GCH(k). Nothing new here from my lens.
- Odd excess **e>=3**: essentially a **one-paragraph closure** away from certified. What's needed to formally close it (not yet written up as a theorem/lemma by any round, so still technically "open" per the file's own honest bookkeeping, but the actual mathematical content is basically done): (1) restate the already-certified margin identity `LB_odd - T_odd = 2^k/6+2^m/6-a1/2-1/2` (round 17, derivable directly from the two already-certified building blocks — chain closed form + Half-Sum Corollary — so this itself needs no new certification, just correct citation); (2) note it's affine/monotone decreasing in a1 over the WHOLE range (2^{k-1},2^k], so the global minimum over the range is at a1=2^k (not the window sup as round 17 mistakenly treated as sufficient); (3) evaluate at a1=2^k: margin = 2^k(2^e-2)/6 - 1/2 >= 2^k-1/2 > 0 for every k>=1 and every odd e>=3 (using 2^e-2>=6 monotonically in e). This closes GT(m) sub-case (i) for ALL k>=1 and ALL odd e>=3 in one shot, no cardinality cap, no window split, no case explosion.
- This is a genuine "cheap kill turned into a near-complete closure" — recommend the outliner dispatch a builder to formalize exactly these 3 steps as a certified theorem (call it, e.g., the "Odd-Excess e>=3 Endpoint Closure Theorem"). Given how short and mechanical the argument is (three certified/elementary steps), this should be closeable in a single round, likely faster than any other open GT(m) sub-case.
- Caution/verify-before-trust: I have NOT verified whether GT(m)'s sub-case (i) even/odd split is exhaustive together with sub-case (ii) and Case-B(m,k) — i.e. whether closing e>=3 (odd) plus the already-certified even case (Claim A, all e>=2 even, full range — also independently re-verified by round-17's reviewer as holding for the whole range via its own "a fortiori" monotonicity argument, though also not yet promoted to a standalone certified lemma file) plus e=1 (certified) together leave ONLY e=0 (Case-B(m,k)'s sliver, a genuinely different explorer's territory) as GT(m)'s sole remaining open case. Based on my reading of current.md's own bookkeeping ("the only remaining open obstruction ... is exactly the e=0 sliver"), this matches — i.e. once e>=3 (odd) is formally certified, sub-case (i) of GT(m) is ENTIRELY closed for every e>=1, and the ENTIRE remaining GT(m) gap collapses to the single e=0 object (shared with Case-B(m,k)). This would be a major consolidation, worth flagging strongly to the outliner.

### Candidate technique(s)
Elementary algebra on an already-certified affine formula (Half-Sum Corollary + corrected e-fold q=0-chain closed form), monotonicity argument, single-endpoint evaluation. No new proof technology needed — this is pure "correctly finish evaluating what round 17 already derived but stopped short of," per the file's own Rule 26/28 pattern (previously-derived correct identities not fully exploited).

### Cheap-kill candidates
None needed beyond what's above — the endpoint check IS the cheap kill, and it survives (positively) rather than killing the approach. No further pruning needed before a builder writes this up.

### Knowledge-base entries to use
This whole line stays entirely within the problem's own homegrown machinery (Lemma AS / OddSum-AltSum identity, the certified Half-Sum Corollary, the certified corrected e-fold q=0-chain closed form) — no external knowledge_base.md theorem is load-bearing here beyond what's already cited by the prior rounds (basic algebra/geometric-series summation).

### Analogous past problems (cruxes)
None sought this round — the closing step is pure in-house algebra on already-derived formulas, not a technique transplant from the crux corpus. (Prior rounds already searched extensively for GT(m)-relevant cruxes; nothing new to add from this narrow algebraic lens.)

### Prior progress
- e=1: fully closed for all k>=2, all a1 in (2^{k-1},2^k], via the certified General Cardinality-Constrained Half-Sum Lemma (round 21), `lemmas/general-cardinality-constrained-half-sum-lemma.md`.
- Even e>=2: independently re-verified by round 17's reviewer as fully proved for the WHOLE range a1 in (2^{k-1},2^k] (Claim A, monotonicity "a fortiori" argument) — genuinely established mathematically, but not (as far as I can tell) promoted to its own standalone certified lemma file; only its two building blocks are certified. (Not my lens, flagged for completeness / cross-check by the e=0/even-lens explorer if applicable.)
- e=0 (both sub-case (i)'s own sliver and the structurally-identical Case-B(m,k) sliver): the sole other genuinely open GT(m) gap, explicitly out of scope for this report (different explorer's lens).

### Dead ends (do not retry)
- Round 16's naive one-step Odd->Odd q=0-chain telescoping identity: FALSE (certified rejection in `half-sum-corollary-and-large-sum-closure-theorem.md`'s scope note) — do not resurrect; the correct coupled Odd/Even two-term recursion (certified, `even-target-companion-peeling-and-corrected-qzero-chain.md`) must be used instead.
- Evaluating Claim B's margin only at the window's supremum a1->2^{k-1}+1 and treating that as covering the whole outside-window range: this is exactly the bug round 18 found for e=1 (false there) — my finding shows it happens to not matter for e>=3 (the endpoint a1=2^k is what actually governs, and it's positive there), but any future write-up must explicitly evaluate at a1=2^k, not just cite the window-sup computation, to avoid repeating this exact class of bug.
- Do not assume a cardinality cap is needed for e>=3 — numerically confirmed unnecessary (zero violations even with piece count up to 8, uncapped, in my stress test); a future builder should NOT invest effort building an e>=3 analogue of the round-21 GCH(k) machinery (unneeded, would be wasted effort — the plain Half-Sum Corollary already suffices).

### Small-case / intuition notes (conjecture, cross-validated numerically)
- The pattern "margin at a1=2^k grows like 2^k(2^e-2)/6" strongly suggests the true worst-case OddSum, as e grows, gets further and further above target 2^m — i.e. large odd excess is the EASIEST regime of GT(m), not a harder one; the difficulty is concentrated entirely at small excess (e=0, e=1) near a1 close to 2^k. This matches the file's own repeated finding (rounds 15-21) that "width-1 window / sliver near the top boundary" objects are the recurring hard core of the whole problem, and is further evidence that once e=0 (Case-B(m,k)-type sliver) is closed, GT(m) is essentially done.
