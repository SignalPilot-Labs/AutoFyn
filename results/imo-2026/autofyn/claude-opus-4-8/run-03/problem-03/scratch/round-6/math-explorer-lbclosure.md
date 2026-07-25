## imo-2026-03 — LOWER-BOUND RESIDUAL CLOSURE (lens: shared wall across all 3 LB approaches)

### Setup recap (verified against current files, all claims below re-checked, not just trusted)
The shared wall is the single statement, in any of 3 equivalent languages:
- (PM) ∫[D odd] ≥ ∫D, D = N_{Q_low} − N_C (induction-peel / interlacing-bijection).
- (Tβ)/(Wβ) β(B) ≤ 2^n−1, coupled overlap 2W ≤ e + S(Q_low) + (S(R)−1) (alternating-sum).
- (CB) Σ_m A_{2m} ≤ Σ_m B_{2m−1} in the concrete Case-B (k_C=0) shard form (induction-peel §3.4).
All are cross-checked as literally the same identity (L12 = IB-1 = R4), so a closure of any one
closes all three simultaneously — there is really ONE open inequality, not three.

### Is (CB) [k_C=0 shard inequality] provable from Σ s_k ≤ 2^n alone? — NO, and here is concrete
evidence why, plus what extra structure is needed.
I ran the exact closed forms from induction-peel §3.4 directly (Fraction arithmetic, layer-cake
computed from scratch as an independent check, not trusting the closed-form band formulas) and
confirmed (CB) holds in every sampled case (n=2,3,4; several thousand random/targeted shard
profiles), so it is very likely TRUE, but three findings bear on *how* to close it:

1. **A striking invariance at the boundary s_1 = H.** When the largest Q_low-shard is exactly
   H = 2^{n-1} (i.e. Q_low = {H} ⊔ rest, rest summing to 2^n − H = H, any legal split of the rest
   into further shards ≤ H), the slack S(B_low) − (1−e) is numerically **CONSTANT regardless of
   how the remaining mass H is split** (verified exactly, n=3: slack = 0 for {4,2,2}, {4,3,1},
   {4,2.5,1.5}, ...; n=4: slack = 2 for {8,6,2}, {8,4,4}, {8,5,3}, ...). This is a genuine new
   structural fact, not previously reported by any approach file. It strongly suggests a
   **peeling/reduction principle**: the shard exactly at H "locks in" against C's own top part
   (C's max element is also exactly H = 2^{n-1}, since C = P_{n-1} = {2^{n-1},...,1} in Case B) —
   these two H-valued elements interact like an L9-style self-pairing / fixed offset, after which
   the residual game on "rest of Q_low (sum H) vs. rest of C (sum H−1, = P_{n-2} dyadic)" should
   be a **smaller copy of the exact same problem one level down** (n → n−1). If this reduction can
   be made rigorous, (CB) becomes closable by **induction on c_shards / on n**, peeling off an
   H-shard at a time — a genuinely different mechanism than R2/L9 (which handle D ≤ 1 or
   S(Q_low)=0, not the s_1=H boundary). **This is the single most promising concrete lead found
   this round** — worth a dedicated sub-lemma attempt: "Q_low ∋ shard = H ⟹ slack(Q_low) =
   slack(Q_low ∖ {H} restricted appropriately, at level n−1)".

2. **No global monotone smoothing/majorization argument works on the shard vector.** Tested Robin-
   Hood transfers (move mass from a larger shard to a smaller one, both staying ≤ H): in ~3000
   random trials on n=4, roughly 1/5 of transfers *increased* the slack and the rest decreased it
   — no consistent sign. So a Schur-convexity/majorization proof of (CB) purely in the shard
   values (ignoring which C-band each shard's boundary falls in) **cannot work directly**; this
   is the same obstruction the round-2 "smoothing toward dyadic" (Lemma G) hit, now confirmed to
   recur even in the narrower Case-B / fixed-C setting. **Do not re-attempt** a pure majorization
   argument on Q_low's shard vector alone without conditioning on which band (I_j) each shard
   boundary lands in.

3. **The pure sum bound Σs_k ≤ 2^n is not by itself the whole story** — the s_1 = H invariance
   above shows the interaction between Q_low's shard VALUES (not just their sum) and C's own
   values (specifically C containing the value H) is doing real work. A rearrangement / Abel-
   summation argument that pairs each Q_low shard against the specific dyadic C-value it "competes
   with" (i.e., matches s_k against C-values 2^{n−k}, 2^{n−k−1}, ... by the closed-form band
   structure in §3.4) is more promising than a pure LP/mass argument. This is consistent with
   the reviewer's own suggested mechanism ("s_k > 2^{n−k+2m−1} is large for its rank").

### Which of the 3 languages is closest to genuine closure, and the single missing step in each
- **induction-peel (analytic/level-set charging).** Closest to a *concrete* finite target: (CB) is
  fully reduced to closed-form band sums in known variables (s_1,...,s_{c+1}). Missing step: a
  rearrangement/Abel-summation proof of Σ A_{2m} ≤ Σ B_{2m−1} from Σs_k≤2^n AND s_k≤H — the s_1=H
  invariance (finding 1 above) is the natural entry point (peel-and-recurse on the shard vector,
  NOT on the multiset B as a whole — a new induction variable, c_shards, not yet used by anyone).
  Still needs the separate k_C≥1 aggregate cross-scale charging afterward (harder, only aggregate
  survives there per the round-5 pointwise refutation).
- **alternating-sum-potential (β-Hall / matching-deficit).** Cleanest STATEMENT (β(B) ≤ 2^n−1, one
  line) but the coupled (Wβ) explicitly needs S(R)−1 (the lower block's surplus over its own IH
  floor) — this is a genuinely different, harder-looking dependency than (CB)'s pure shard
  inequality, because in Case B, R = P_{n-1} is UNCUT so S(R) is large (Jacobsthal-like, not just
  ≥1) — meaning (Wβ) in Case B has huge slack available (consistent with (CB)'s empirical
  "far more benign" status noted in round 5). The missing step here is the same Hall-style
  explicit injection/deficit-accounting that induction-peel and interlacing-bijection also lack;
  no new mechanism was found this round beyond the equivalence.
- **interlacing-bijection (combinatorial injection Φ).** Correctly isolates the target as "even-up
  excursion time ⟶ odd-down excursion time" but the injection is NOT built past height ≤ 2. The
  s_1=H invariance (finding 1) suggests a cleaner combinatorial reading: at s_1=H, the walk D
  starts at 0, takes one +1 step crossing t=H (Q_low's H-shard) that EXACTLY CANCELS the −1 step
  from C's own H-value crossing at the same threshold t=H (both cross at the same point!) — so the
  two H-events are a literal L9-style matched pair with ZERO net walk displacement, after which the
  walk on (0,H) is the SAME two-source walk one level down. This is a concrete conjectural
  mechanism for Φ's totality that has not been tried: pair Q_low's boundary-H shard against C's
  own top element FIRST (a "give away the tie" move), then recurse the injection on the residual.

### A cleaner reformulation of (PM) not yet tried
None of the three approaches has tried recasting (PM)/(CB) as an **induction on the number of
shards c_shards** (equivalently on the number of cuts XY spends on the single top block), with the
s_1 = H boundary as the base/peel step. All three current inductions are on **n** (the recursion
depth over dyadic scales); the shard-count induction found here is orthogonal and specific to
Case B (and possibly extendable to general k_C by treating each origin group's shard-count
separately, echoing O1′ "every group is at its own part-budget frontier"). This is a genuinely
different reduction axis from anything in the field so far and is the strongest lead this round.

### Cheap-kill candidates
- Try to FALSIFY the s_1=H invariance at larger n / more exotic rest-splits (only checked n=3,4,
  small samples) before investing in the peel-by-shard-count induction — a 30s exact-Fraction
  check across many n, many rest-partitions (including partitions with >2 further shards) is the
  natural next cheap step for whichever builder picks this up.
- Check whether the invariance generalizes to s_1 = any value ≥ H is impossible (H is the cap by
  definition of Q_low, so s_1 ≤ H always — the boundary is exactly s_1 = H, not a a range),
  confirming the "peel a boundary shard" step is a genuine 0-parameter special case, not a family
  to search over.

### Knowledge-base entries in play
- **Pigeonhole/extremal principle**, **invariants & monovariants** (General Proof Methods,
  Combinatorics) — the s_1=H invariance is exactly an "invariant under further splitting of the
  rest," a natural KB-flavored lemma once formalized.
- **Piecewise-concavity smoothing** entry — explicitly checked and found NOT applicable here (no
  monotone smoothing direction on the shard vector); do not force this entry.
- Hall's marriage theorem entry — per existing round-3 rule, this is a KNOWN dead end (there is a
  min-pairing closed form already; no existence question remains). Do not resurrect for the
  injection Φ in interlacing-bijection; Φ needs to be constructed explicitly, not merely shown to
  exist via Hall's condition — and the field's own O3 obstruction (peeling reproduces the SAME
  overlap W) already shows recursive/Hall-style existence arguments dodge nothing here.

### Analogous past problems (crux moves corpus)
Did not have budget this round to query the crux corpus directly (all prior rounds report having
checked broadly and found the field's own KB entries — pigeonhole/extremal, invariants — as the
relevant ones; no distinctly-analogous solved IMO problem was surfaced by prior rounds either, per
current.md's approach files, none of which cite a crux-corpus problem_id for the LB residual). No
new claim made here about crux-corpus analogues; flagging as unexplored rather than asserting
"none" — a future round with more budget should run a `subtopic` filter on "extremal
combinatorics" / "layer-cake / rearrangement" style entries specifically for this closing step.

### Prior progress
Unchanged from current.md: LB residual narrowed to c_n≥2 ∧ e<1; Case B (k_C=0) reduced to (CB)
which is numerically confirmed (now independently re-confirmed by this round's fresh, from-scratch
layer-cake computation, not reusing the induction-peel closed-form band formulas) but not proven.

### Dead ends (do not retry)
- Pointwise per-level charging A_{2m} ≤ B_{2m−1} for k_C ≥ 1 — REFUTED (round 5, re-confirmed
  structurally consistent this round: Case B pointwise DOES hold, only the k_C≥1 aggregate case
  fails pointwise, matching the existing record — no contradiction found).
- Pure majorization / Robin-Hood smoothing on the Q_low shard vector (this round, confirmed non-
  monotone: ~1/5 of random transfers move slack the "wrong" way) — extends the round-2 Lemma-G
  refutation into the narrower Case-B setting; do not attempt a smoothing proof of (CB) that
  ignores which C-band a shard's threshold falls in.
- Floor/ceiling slack decomposition of Lemma IB-1 / R4 (∫⌊D+/2⌋ vs ∫⌈D-/2⌉ via ⌊x/2⌋=x/2−{odd}/2)
  — checked this round algebraically: it is EXACTLY CIRCULAR, reduces back to (PM) itself
  (1−e ≤ meas{D odd}), giving zero new leverage. Do not re-attempt this specific algebraic route
  as if it were a new angle; it is a restatement, not a reduction.

### Small-case / intuition notes (labeled conjecture)
- Conjecture (numeric, n≤4, several thousand trials, exact Fraction): (CB) holds with equality
  exactly on the boundary family {s_1 = H, rest arbitrary split ≤ H} — this is an OPEN PLATEAU of
  minimizers (matches the round-5 note that equality regions are generically open/full-dimensional,
  not a single unique witness).
- Conjecture: the s_1=H "peel and recurse to level n−1" mechanism, if formalized, likely closes
  (CB) by induction on c_shards (with the H-shard peel as the inductive step and a small base case
  c_shards=1, i.e. Q_low = {2^n} uncut which is Case 1, already closed). This has NOT been proven —
  it is a concrete conjecture with strong numerical support (finding 1) that the next round's
  outliner/builder should attempt to formalize as the primary new push on this wall.
