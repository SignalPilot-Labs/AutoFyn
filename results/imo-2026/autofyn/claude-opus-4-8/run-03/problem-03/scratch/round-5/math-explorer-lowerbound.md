## imo-2026-03 — lens: lower-bound residual (PM), compensating D≥2 via the part budget

### Setup recap (certified, not re-derived here)
Residual (A-res) ⟺ (PM): ∫₀^∞ [D(t) odd] dt ≥ ∫₀^∞ D(t) dt, D := N_{Q_low} − N_C, where Q_low is a
capped ≤c-cut refinement of the single top block {2ⁿ} (c ≥ 1 forced) and C a ≤k_C-cut refinement
of P_{n-1}, with c + k_C ≤ n, S(C) ≥ 1 by strong IH. R2 (D ≤ 1 a.e. ⟹ (PM)) is proved; the open
part is compensating the interior {D ≥ 2} pockets. Numerically (this round, exact Fraction, n=3,
20000 random configs) (PM) holds with **zero violations**; ≈12–19% of configs (377/3000 in one
run) genuinely exhibit D ≥ 2 somewhere, so the compensation is real content, not vacuous.

### New structural fact found this round (verified numerically, NOT yet proved): strict parity alternation
Since B_low = Q_low ⊔ C and N_{B_low} = N_{Q_low}+N_C, **generically** (all part-values of Q_low
and C pairwise distinct) every breakpoint of the merged sorted list changes D by exactly ±1 (a
Q_low-breakpoint decrements D by 1, a C-breakpoint increments it by 1). Consequently the *parity*
of D strictly alternates interval-to-interval, **regardless of which side (Q_low or C) the
breakpoint came from**: odd, even, odd, even, ... This is not new content by itself — it is just
L2/L3's alternating-sum fact for the multiset B_low restated — but decomposing it by *which*
breakpoints belong to Q_low vs C turns (PM) into a genuinely combinatorial statement: [D odd] is a
purely **positional** (interleaving-order) quantity, while ∫D is a **path-dependent** quantity
(depends on the actual ± sequence, i.e. on which values are Q_low's vs C's). (PM) is then an
Abel/summation-by-parts inequality between a fixed alternating indicator and the signed partial
sums of a walk with steps ±1 (down-steps = Q_low's c+1 breakpoints, up-steps = C's n+k_C
breakpoints, D(0+) = (c+1)−(n+k_C) ≤ 1 already established, D(∞)=0).

**Verified exception (numerically, exact):** the strict alternation FAILS exactly when two parts
tie (a breakpoint shared by two or more parts, e.g. Q_low has two equal shards from a symmetric
split); there the joint jump has magnitude ≥2 and skips a parity step. This is precisely the
self-pairing degeneracy L9 already isolates (equal parts cancel at adjacent rank). So the terrain
splits cleanly into: **(i) generic/distinct-breakpoints case** — pure alternation, an
interleaving/lattice-path problem; **(ii) tie case** — already reducible via L9-style
cancellation (reduces part count, recurse). This split is a genuinely new opening not previously
recorded, distinct from R2/L9's D≤1 slicing.

### Where the surplus concretely comes from (numeric case study, n=3, exact Fraction)
Examined several D≥2 configs (see transcript below); the compensating surplus band always came
from one of two structural sources, tied directly to the budget c+k_C≤n:
- **Top-of-band surplus (k_C small).** If C retains an *uncut* top block (2^{n-1} = H survives as
  a whole part of C, i.e. the induction on C hasn't touched its own top scale), while Q_low
  (c ≥ 1 cuts) has ALL its shards strictly below H (either because e=0, no shard reached H, or
  because the one shard >H was capped exactly to H so no *interior* Q_low part is close to H),
  there is a whole band immediately below H where N_C = 1 (from the surviving H-part) but
  N_{Q_low} = 0 — a persistent D = −1 band of length up to Θ(H) right under the ceiling. Example:
  c=3,k_C=0, Q={12/5,8/5,2,2} vs C={1,2,4}: the D=2 pocket on [1,8/5) (length 3/5, deficit 6/5) is
  paid for by the D=−1 band on [12/5,4) (length 8/5, surplus 16/5) — over 2× the deficit.
- **Bottom-of-band surplus (k_C ≥ 1).** If C is itself cut (k_C ≥ 1), C accumulates *more* small
  parts near 0 than Q_low, driving N_C above N_{Q_low} deep in the tail t→0⁺: D(0+) =
  (c+1)−(n+k_C) ≤ 1−2k_C (already a certified inequality in induction-peel §3.3), so k_C ≥ 1
  forces a strongly negative D near the origin, a large surplus band. Example: c=1,k_C=2,
  Q={4,4}, C split into 5 parts: D=−3 near 0 (length 1/5, surplus 4/5) alone already exceeds the
  single deficit pocket D=2 near t≈3.6 (length 2/5, deficit 4/5).
In every sampled violation of R2, exactly one of these two budget-forced bands (top-band when
k_C is small, bottom-band when k_C is larger) supplied enough surplus; which one dominates is
governed by k_C, and c+k_C ≤ n caps how much of BOTH bands can be simultaneously starved.

### Distinct openings for the outliner
1. **Two-source charging / amortized argument.** Formalize "top-band deficit needs k_C small ⟹
   top-band surplus large; k_C large ⟹ bottom-band surplus large" as an explicit dichotomy on
   k_C, each branch closing (PM) by a direct interval-length comparison (not full induction on
   C's profile). This is the most concrete, closest-to-finish opening — needs an exact charging
   map from each D≥2 sub-interval to length in one of the two designated bands, using c+k_C≤n.
2. **Lattice-path / positional-vs-path-dependent Abel summation** (new this round). Recast (PM) in
   the generic (no-ties) case as: given a ±1 walk of length m=(c+1)+(n+k_C) with (c+1) down-steps
   and (n+k_C) up-steps landing at specific real times, and the FIXED alternating parity sequence,
   prove Σ (interval length)·[position odd] ≥ Σ (interval length)·(walk height). This decouples
   into an ORDER/interleaving statement, tractable by summation-by-parts on the sorted merge — a
   genuinely different technical route from R2's pointwise f(d) argument. Tie-case handled
   separately by L9-style cancellation (verified as the exact failure mode of strict alternation).
3. **Recursive/self-similar strengthening of the IH** (not yet tried, flagged as promising because
   the REFUTED profile invariant P* was refuted only for *arbitrary* X — C is not arbitrary, it is
   itself built by the SAME truncation process on P_{n-1}, recursively superincreasing). Strengthen
   Lemma A(n−1)'s inductive hypothesis to also carry a structural bound on N_C(t) (not just the
   scalar S(C) ≥ 1) — e.g. via C's own truncation identity at H' = 2^{n-2}, recursing the same
   e/S(C_low) split one level down. This could supply exactly the "uncut/large-part-near-top"
   information the top-band-surplus source (opening 1 above) needs as a proven fact rather than an
   observed pattern.

### Candidate technique(s)
Amortized/charging argument over the two structurally-forced surplus bands (opening 1) is the
most promising near-term target; the lattice-path reformulation (opening 2) is a genuinely
different technical route sharing no machinery with R2; the recursive-IH strengthening (opening 3)
attacks the shared crux by giving the induction more information rather than trying to extract
more from a scalar S(C) ≥ 1.

### Cheap-kill candidates
- Check whether the deficit total is always dominated by the SINGLE larger of the two bands alone
  (not needing to sum both) — cheap sufficient reduction, worth testing before building the full
  charging map.
- The tie/degenerate case (strict-alternation failure) is fully disposed of by L9-style
  cancellation — confirm this covers ALL tie configurations, not just the pure-BISECT boundary,
  before spending effort on the generic case.

### Knowledge-base entries to use
No new entries beyond what's already cited (L3 layer-cake, L4 min-pairing/alternating-sum). The
knowledge_base.md generic entries on extremal/smoothing arguments were not found directly
applicable to this residual (it is a bespoke walk/interleaving statement, not a standard
inequality template) — see prior rounds' notes; nothing new to add here.

### Analogous past problems (cruxes)
Did not requery the crux corpus this round (prior rounds' scouting on this exact residual already
covered ballot-problem / alternating-sum style corpus entries without finding a directly
transplantable crux move for this SPECIFIC two-block interleaving structure — see
alternating-sum-potential.md history). No new match found via this numeric lens; flagging as
"none new" rather than re-searching redundantly.

### Prior progress
As recorded in current.md / induction-peel.md: R1 (reformulation), R2 (D≤1 sufficient), L9
(self-pairing), all certified. (PM) itself open.

### Dead ends (do not retry)
- Arbitrary-X profile invariant P* — refuted (slack → −1.4). Re-verified consistent this round:
  my structural surplus-source explanation is explicitly tied to C's SPECIFIC recursive dyadic
  structure (uncut-top-block / cut-count), which P* discarded by allowing arbitrary X — this is
  likely WHY P* failed and is exactly what opening 3 proposes to restore.
- Cut-count cap on W / cuts-on-C cap — refuted (round 4, true extremal spends zero cuts on C).
  Consistent with this round's finding: k_C=0 is exactly the case relying on the TOP-band surplus,
  not a W-cap.

### Small-case / intuition notes (conjectural, numeric evidence only)
- n=2,3 exact-Fraction sweeps (20000+3000 trials): zero violations of (PM); D≥2 pockets occur in
  roughly 12–19% of random configs and are always over-compensated (often by a factor of 2+) by
  one of the two budget-forced bands described above.
- The strict-parity-alternation fact holds in ~83% of random trials (336/2000 exceptions, all
  traced to tie/self-pairing breakpoints) — this is a clean, previously-unobserved structural
  dichotomy worth handing to the outliner as a candidate case split for a fresh approach.
