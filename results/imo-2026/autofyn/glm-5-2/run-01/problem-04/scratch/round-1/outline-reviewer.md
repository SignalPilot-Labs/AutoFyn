## imo-2026-04 — outline-reviewer report (round 1)

Answer conjecture under review: Mulan wins in finitely many steps iff `180°/θ ∈ ℤ`, i.e.
`θ = 180°/n` for an integer `n ≥ 2`. Cross-confirmed by all three explorers and numerically
verified on the 1° grid. The core reduction (supplementary `P`-angles `p1+p2=180`; the
four-case closure on `S_θ`-free triples; Lemma R induction `mθ→(m−1)θ`; Lemma F
interval-contains-integer) is solid and I confirmed the load-bearing algebra by
independent small-case computation (see below). The four-case closure is short, purely
algebraic, and verified; it is the unique correct necessity engine — every approach uses
it, and that shared-gap risk is acceptable because the closure is genuinely simple.

### Small-case sanity checks I ran

1. **Four-case closure (necessity):** verified the four linear combinations of `γ`
   telescope to `A`, `B`, `C`, `180`. Algebraically exact; no discretization gap. Sound.
2. **Lemma R induction positivity:** the outliner flagged `A+θ<180` as a gap. It is
   fillable: in the kept child2, `A < 180−mθ` (since `A+B=180−mθ` and `B>0`), hence
   `A+θ < 180−(m−1)θ ≤ 180−θ < 180`. The induction is robust; the multiple stays at a
   vertex of the kept child (whether inherited or a `P`-angle), so `γ=θ` is always a valid
   cut. APPROVE-grade, gap fillable.
3. **Chip-transfer `t=1` dynamics:** the GREEDY (always cut the largest coordinate) CYCLES
   — e.g. `q=(3,2,3)` for `n=8` is a fixed point under greedy. BUT smart `t=1` play
   (cut the coordinate with value `m=2` first, i.e. Lemma R's base case) wins from EVERY
   integer `q`-state with sum `n` (exhaustive search, `n∈{3,…,12}`, zero unwinnable
   states). So the transfer engine WORKS — but its "monovariant" is exactly Lemma R's
   multiple-index descent, NOT a genuinely new transfer-specific potential. The cycles
   prove no strict monovariant exists for the *pure greedy* transfer op; the winning
   descent is the direct approach's Lemma R. This drives the chip-transfer verdict below.

---

### Verdicts

#### `direct-four-case-interval` — APPROVE
The canonical direct proof; both engines (four-case closure necessity; Lemma R + Lemma F
sufficiency) are correct and independently verified. The skeleton is sound end to end:
necessity is a clean four-case contradiction with the equilateral as the universal
`B_θ`-free witness; sufficiency stratifies as `n=2` (special move `γ=90−A`) then `n≥3`
(Lemma F reaches a multiple in one move, Lemma R descends `m→m−1`). Cases covered: `n=2`,
`n≥3`, `θ>90°` (necessity, `180/θ<2` non-integer), irrational and rational-non-`1/n`
`180/θ` (both uniform under the four-case closure). Gaps are fillable, not fatal:
- **Step 5 positivity:** fillable as shown above (`A<180−mθ`).
- **Step 6 strict containment:** the open-interval formulation already gives `γ∈(0,C)`
  strict; the builder just needs to state the endpoint-exclusion and `n−k≥1, k≥1`
  bounds explicitly.
- **Step 5/6 interface:** Lemma R applies to whichever `P`-angle (value `kθ` or
  `(n−k)θ`) Shan-Yu's kept child carries, since both are vertex angles `∈{θ,…,(n−1)θ}`.
  The `m=1` case is the immediate win. Fine.
- **Step 4 `n=2`:** verify both acute and obtuse non-right openings give two angles `<90°`
  when the largest is split. True (at most one angle `≥90°`, the largest). Fillable.
Register and build. The leader.

#### `attractor-level-fixpoint` — APPROVE
The framing is a genuine logical re-packaging, not a new algebraic engine: necessity
reuses the four-case closure (shared, acceptable), sufficiency reuses Lemma R + Lemma F
(shared, acceptable). Its DISTINCTIVE contribution is the **determinacy / no-draw clause**
for the uncountable state space — a real mathematical question the direct approach
hand-waves by exhibiting explicit strategies for both sides. The outliner honestly flags
this as the hard gap and supplies a sound fallback: deduce complementarity
(`W∪S=X, W∩S=∅`) from "explicit Mulan strategy + explicit Shan-Yu strategy cover all
cases" rather than from transfinite game theory. That fallback makes the approach safe
even if the abstract determinacy argument stalls. The level bound `W_{n−1}=X` is just
Lemma R+F repackaged and is sound. This is a legitimate cross-check on the no-draw
question and a cleaner vehicle for the "finitely many steps" clause (explicit level
bound). Not a near-duplicate: its hard gap (determinacy) is disjoint from the direct
approach's hard gaps (induction positivity, interval strictness). Build.
Gaps for the builder:
- **Step 2 (determinacy):** write the no-draw argument. Prefer the constructive
  fallback (explicit strategies partition the space) over transfinite iteration; state
  that `W_{n−1}=X` (step 4) makes the attractor collapse at finite stage `n−1`, so the
  complement `S` is exactly `B_θ`-free and no state is undetermined.
- **Step 3 (⊆):** prove a `B_θ`-bearing triple is not in `S` via Lemma R (well-founded
  ladder, indices strictly decrease). Cite the shared Lemma R; do not re-prove.
Register and build.

#### `chip-transfer-monovariant` — CHANGES REQUESTED
The technique (Euclidean descent / monovariant on the multiple-index) is the RIGHT idea
and is sound — but the framing's claim of a DISTINCTIVE transfer-specific monovariant is
**not supported by evidence**. My computation shows:
- The pure `t=1` transfer op CYCLES under greedy play (`q=(3,2,3)`, `n=8`, is a fixed
  point when the largest coordinate is cut). This proves **no strict monovariant exists
  for the greedy transfer op**.
- Smart `t=1` play (cut the smallest `m≥2` first) wins from every integer `q`-state —
  but that winning descent **is exactly Lemma R's multiple-index descent**, i.e. the
  direct approach's engine, not a new potential.

So the approach's defining hard gap (Step 3: "FIND the monovariant") resolves to: the
monovariant IS the multiple-index (Lemma R), and the approach's sufficiency is a
re-derivation of the direct proof in `q`-space. The outliner itself warns "Do NOT pretend
a failed monovariant is a different proof." The fallback (Step 4, interval lemma in
`q`-space) is verbatim the direct approach's Lemma F.

The approach's ONLY genuinely distinct content is the **necessity** route: Kronecker
equidistribution for irrational `180/θ` (Step 5) and explicit periodic orbits for
rational-non-`1/n` `180/θ=p/q` (Step 6, e.g. the `θ=72°` test case). These ARE a
different mathematical home from four-case casework — but the outliner admits they are
HEAVIER, split into sub-cases, and must handle Mulan's non-`t=1` moves (the reduction
explorer left the `θ=72°` sub-case UNRESOLVED for non-greedy Mulan play). The four-case
closure already covers necessity uniformly.

Verdict: the technique is sound (the answer is right, the descent works), but the
distinctiveness is overstated. The builder must EITHER:
- (a) earn genuine distinctiveness by making the necessity periodic-orbit route
  (Steps 5–6) rigorous AND self-contained (not falling back to four-case) — handling
  Mulan's arbitrary `t`, not just `t=1`; OR
- (b) honestly relabel the sufficiency as Lemma R and concede the approach is a
  `q`-space cross-check of the direct proof.

I keep it alive (registered, buildable) because the necessity orbit route is a real
cross-check and the approach is not doomed — but rank it below the other two pending
evidence of (a). If the builder cannot deliver (a) or (b), it should be merged into
`direct-four-case-interval` next round.

#### `modular-residue-orbit` — RETHINK (refused, NOT registered)
The outliner SELF-FLAGS this as THIN, and the self-flag is correct. Its necessity IS the
four-case algebra restated in modular language (Step 3 explicitly re-derives the four
linear combinations of `γ` mod `θ`); the "total residue `≠0`" invariant alone is
INSUFFICIENT (one residue can be `0` while the others sum to the nonzero total — the
outliner states this). Its sufficiency is the interval lemma + Lemma R, identical to
`direct-four-case-interval`. So this approach shares BOTH engines with the direct
approach and adds only a one-line modular punchline that does not by itself prove
closure. This is the textbook **single-gap trap / near-duplicate** that CLAUDE.md
warns against: it will die with its twin if the four-case closure has a flaw, and it
contributes no independent engine. Registering it would pollute the population with a
twin of `direct-four-case-interval`. **Refused — not registered, not built.** If a
modular viewpoint is desired later, it can be folded into the direct proof as a
remark; it is not a rival approach.

---

### Diversity / shared-gap audit

The necessity direction has ONE correct engine (the four-case closure), so all three
approved approaches share it. This is acceptable: the closure is short, algebraic, and
verified. The genuine diversity is in:
- **Sufficiency packaging:** direct (Lemma R+F explicit) vs attractor (level
  stratification + determinacy). Distinct logical structure; not single-gap-duplicates.
- **Necessity cross-check:** chip-transfer's Kronecker/periodic-orbit route (if the
  builder makes it rigorous) is a genuinely different mathematical home for necessity,
  independent of four-case casework. This is where the approach can earn its keep.
- **The no-draw question:** only the attractor approach tackles it explicitly; the
  direct approach hand-waves via explicit strategies. Genuine cross-check.

The refused `modular-residue-orbit` would have added a fourth clone of the four-case
necessity with no new sufficiency engine — correctly cut.

### Ranking (pairwise, anchored to real prospect of closing the characterization)

All three approved approaches are new this round (cold-start Elo 1500); there are no
established approaches to anchor against, so I rank the three head-to-head:
- `direct-four-case-interval` > `attractor-level-fixpoint` — direct is more complete
  (explicit strategies both directions, both engines verified); attractor's distinctive
  determinacy gap is still open.
- `direct-four-case-interval` > `chip-transfer-monovariant` — direct's sufficiency is
  the verified Lemma R+F; chip-transfer's distinctive monovariant does not exist
  (cycles prove no greedy-transfer monovariant; smart play = Lemma R), and its
  distinctiveness rests on an unresolved necessity route.
- `attractor-level-fixpoint` > `chip-transfer-monovariant` — attractor's
  distinctive gap (determinacy) is a cleaner, more tractable logical contribution than
  chip-transfer's heavier unresolved necessity orbit route; attractor also has a sound
  fallback. Slight edge.

build set: direct-four-case-interval, attractor-level-fixpoint, chip-transfer-monovariant
