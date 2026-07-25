## imo-2026-03 — lens: does a single equality-rigidity theorem close BOTH walls?

**Verdict up front: the literal premise is a MIRAGE — numerically REFUTED — but the probe surfaces
a real, narrower, usable reframing for the LB wall only.**

### What I tested
The round-4 outline-reviewer flagged: "the LB extremal witness (dyadic cascade, S=1) is EXACTLY
the UB dyadic cascade — a proof characterizing 'S(B)≥1 with equality iff B is cascade-type' could
close BOTH walls at once." I tested the "equality iff cascade" (uniqueness/rigidity) claim directly
by numerically searching the FULL equality set {B : S(B)=1} for LB's dyadic A=P_n, n=2,3, not just
confirming the cascade attains it.

**Finding 1 (numeric, n=2, P_2={1,2,4}, ≤2 cuts).** Splitting only the top piece 4 into three
shards (a1,a2,a3), leaving 2 and 1 untouched, gives S(B)=1 for an entire OPEN 2‑parameter region:
whenever the sorted order interlaces as a1 ≥ 2 ≥ a2 ≥ 1 ≥ a3 > 0 (sum a1+a2+a3=4), S(B) =
(a1+a2+a3) − (2+1) = 4−3 = 1 identically — independent of the exact shard values. Random sampling
(300k draws) found ~40+ visibly distinct numeric minimizers instantly, all sharing this rank
pattern, plus a *second*, topologically different minimizer family from a degenerate 1-cut split
(4→2,2 with 2,1 untouched, giving B={2,2,2,1}, S=1) — i.e. even the "cut topology" (which original
piece absorbs how many cuts) is not unique at the optimum.

**Finding 2 (n=3, P_3={1,2,4,8}, split top 8 into 4 shards, leave 4,2,1 untouched).** Same
phenomenon at the next scale: S(B)=1 for the interlacing region a1≥4≥a2≥2≥a3≥1≥a4>0 — in a
200k-sample sweep, **9435/200000 (≈4.7%)** of random splits landed in this exact-equality region.
This is a full-dimensional (positive-Lebesgue-measure) plateau in parameter space, not an isolated
point or even a finite set of points.

**Conclusion on equality.** {B : S(B)=1} for A=P_n is NOT a single point up to relabeling — it is a
union of full-dimensional cells, one per admissible "interlacing pattern" of the split shards
against the surviving untouched values. The right invariant is a **discrete rank/interlacing
pattern**, not a numeric value: S is a layer-cake/parity functional (L3: S=meas{N(t) odd}), so it
is locally constant in the continuous split parameters and jumps only when a shard crosses an
existing part's value (changing N(t)'s parity structure). "The dyadic cascade" is just one
(distinguished, symmetric) point deep inside one of these plateaus — not a rigid extremal.

**Finding 3 (does the plateau transfer to generic, non-dyadic A?).** Tested A={5,3,2,1} (sum 11,
NOT dyadic), splitting the top part 5 into 4 shards, rest untouched — the analogous setup to
Finding 2. Result: **min ≈ 1.0 is attained, but the near-min plateau fraction is ~5×10⁻⁶ of samples**
(vs 4.7% for the dyadic P_3 case) — i.e. for generic A the minimizer is essentially an ISOLATED
boundary configuration, not a plateau. The wide equality region is a **special feature of the
dyadic profile's power-of-2 gaps** (each "window" between consecutive untouched scales 2^{j+1},2^j
has width exactly 2^j, matching the shard budget exactly) and does **not generalize** to arbitrary
A. This directly falsifies the "closes both walls" hope: LB's extremal set is degenerate-wide
*because* A is dyadic; XY's optimization against a generic A is genuinely rigid/isolated (confirms
F1 — no interlacing-freedom shortcut exists off the dyadic profile).

### Which wall this genuinely helps
- **LB wall (residual (PM)/Gβ, the {D≥2} interior compensation): a real, narrower opening.**
  Since S(B)=1 is governed by a discrete interlacing/rank pattern rather than exact values, the
  outstanding gap (compensating ∫_{D≥2}(D−[D odd]) by ∫_{D≤0}([D odd]−D)) may be more tractable
  reframed as a **combinatorial bijection/counting argument on interlacing patterns** (map each
  "excess" rank-crossing where D≥2 to a matching "deficit" crossing where D≤0, using the
  origin-group-sum budget) rather than as a continuous integral inequality. This is a genuinely
  different framing from both current LB mechanisms (profile-IH/W-overlap and β-Hall-deficit) —
  worth opening as a discrete/bijective LB approach. It is NOT yet a proof; I have not found the
  bijection, only that the natural target object is rank patterns, not measures.
- **UB wall (arbitrary-A cap): the idea does NOT help, and Finding 3 gives a positive reason why
  not.** The "many B's work" freedom that makes the LB side easy to hit is a dyadic-only artifact;
  XY facing generic A has no such freedom and must hit a value-tuned, nearly-isolated target. This
  reinforces (does not overturn) the F1 finding already on record: no rigidity shortcut rescues the
  branch-inequality / averaging cruxes. Do not expect an "aim for any interlacing-compatible B"
  strategy to work off the dyadic profile.

### Hardest step / is it a mirage
The literal reviewer-flagged claim ("S(B)≥1 with equality iff B is cascade-type") is a mirage as
stated — equality is not rigid, it is a whole family sharing one interlacing pattern. The salvageable
core is: recast the open {D≥2} compensation as counting/matching interlacing crossings rather than
integrating a real-valued function. The hardest step to make this real: formalize "interlacing
pattern" combinatorially (which rank slots the c shards of Q and k_C shards of C occupy relative to
each other) and show the origin-group-sum constraint (Q from a single block of mass 2^n, C a
refinement of P_{n-1}) forces every pattern realizable with ≤2n+1 total parts to have deficit ≥
excess. This has not been attempted by any current approach and is untested beyond the two data
points above.

- Distinct openings: (1) discrete interlacing/rank-pattern bijection for the LB {D≥2} compensation
  (new, not tried by any live approach — closest existing language is L3/L4/L10's parity-matching
  machinery, but none of the three live LB mechanisms frame the gap combinatorially/bijectively);
  (2) explicit characterization of the FULL equality-plateau structure of S(B)=1 at A=G_n (could be
  a clean standalone lemma: "S(B)=1 iff every scale-window [2^{j-1},2^j] absorbs its shards in an
  order-consistent way" — useful as a sanity/verification tool for whichever LB proof lands, even
  if not load-bearing itself); (3) negative confirmation that no analogous plateau exists for
  generic A (Finding 3) — this should be recorded as evidence AGAINST any future "borrow LB's
  equality freedom for the UB" idea, saving a round.
- Candidate technique(s): discrete/bijective counting on interlacing patterns (new); layer-cake
  parity (L3) as the reason equality is plateau-valued, not point-valued (explains, does not by
  itself close, the gap).
- Cheap-kill candidates: none obvious beyond what's already banked (L9, R2). The origin-group-sum
  budget |Q_low|+|C|≤2n+1 (already flagged in current.md) remains the correct lever; this lens adds
  the *combinatorial* framing of what to do with it, not a new inequality.
- Knowledge-base entries to use: none of the generic KB theorems (rearrangement/majorization/
  matching, referenced around line 120 "Multiset partitions & power-sum matching") add anything
  beyond what L3/L4/L9/L10/L11 already encode; this is a purely internal-lemma-driven line.
- Analogous past problems (cruxes): checked combinatorics/games-and-strategy subtopic (39 cruxes).
  `aimo-0117` — "Assign the played values as a two-sided geometric (dyadic) sequence so the single
  largest value strictly exceeds the sum of all others" is the closest analog (superincreasing-set
  idea) but it is exactly the mechanism ALREADY used and exhausted (L6/A0's "at most one large
  shard"); it does not address the {D≥2} interior gap and offers no new interlacing/bijection tool.
  No crux in this subtopic addresses a layer-cake-parity equality-plateau argument; genuinely
  nothing analogous found for that specific piece — say so rather than force a match.
- Prior progress: unchanged from current.md — LB residual = (PM) ∫[D odd]≥∫D, closed on D≤1 (R2)
  and S(Q_low)=0 (L9); open on {D≥2} interior. UB fully open (branch inequalities / averaging both
  exhausted).
- Dead ends (do not retry): "smoothing toward the dyadic cascade" (Lemma G, round 2) — this probe
  gives a NEW reason it was doomed beyond the round-2 mechanism failure: there is no unique cascade
  to smooth toward in the first place, the equality set is an extended plateau, so any argument
  premised on convergence to "the" extremal point is targeting a mirage. Also reaffirm: do not
  attempt to transfer LB's equality-plateau freedom to the UB construction for generic A (Finding 3
  shows the plateau collapses to near-zero measure off the dyadic profile).
- Small-case / intuition notes (CONJECTURE, numeric only): (a) the LB equality set at A=G_n is a
  finite union of open interlacing-pattern cells, each satisfying "shards of the split top block
  weave exactly once through each successor scale-gap" — conjectured pattern-count grows with n but
  untested beyond n=2,3; (b) the discrete-pattern reframing is plausible-looking but NOT reduced to
  a checked bijection — treat as an opening to scout, not a result.
