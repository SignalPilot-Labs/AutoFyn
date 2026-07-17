# Outline Review — imo-2026-03, Round 7

Field of 3: direct-constructive (advance, L2 lower), upper-vertex-reduction (NEW copy-of, different
framing for IH(q≥5) upper), upper-general-cascade (advance, B2 corrected). All three target the whole
problem end-to-end (both bounds), each owning a distinct open gap — good division of labor, no
single-gap trap this round: L2 (lower) vs B2 (upper) vs IH(q≥5) (upper) are three genuinely different
walls.

---

## 1. direct-constructive — ADVANCE (L2, augmented Δ-vertex) — APPROVE

**Verdict: APPROVE.** Sound. This closes the SOLE remaining lower-bound gap and could flip the lower
bound fully closed.

- Technique is right: extend the certified `DyadicLower-confined` PL-min-at-vertex spine to the
  augmented space (confined R_n fragments + stray sub-pieces of R_j, j<n). Reuses certified machinery,
  not a new wall.
- Correctly AVOIDS the refuted monotone exchange. The explorer's own data (716/17980 pointwise
  violations of "stray→confined weakly raises A") is honored — the outline routes L2 through the
  augmented vertex reduction, not a pointwise monotone swap. Good; this was the round-5/6 trap.
- Load-bearing steps carry mechanisms: step 6 midpoint-cancel induction (equal pair {2^{n-2},2^{n-2}}
  XOR-cancels via Lemma H → collapse to a DyadicLower instance with one fewer intact; valid because
  DyadicLower's proof used only #fragments ≤ n+1 and the sum, not the exact intact multiset); step 7
  G-even branch reuses the certified strictly-decreasing flat-move monovariant m = #{positive
  fragments}.
- The Count Lemma arithmetic checks: k_n+1 ≤ n−s+1 < n+s ⟺ 2s>1, true for s≥1 — so an R_n-fragment
  cannot fill all odd ranks. Correctly flagged as giving A>0 only, NOT A≥1 (the dyadic per-case bounds
  carry the ≥1).

**Issues to close while building (CHANGES-level, do not block build):**
- Step 6, sub-case a<2^{n-2}: the "smaller-n instance handled inductively" needs the induction
  hypothesis form written explicitly (what is the inductive statement, and does the augmented instance
  actually match its hypotheses?). The outliner flagged this; make it airtight, don't hand-wave
  "handled inductively."
- Step 7 G-even branch: confirm the flat-move monovariant still terminates once stray pieces are
  present — test at CLUSTERED tie-laden augmented vertices, NEVER random ones (per the standing rule;
  round-5's refutation lived exactly at clustered vertices).
- Case coverage: verify a=1 / Case-1(R_{n-1} intact / midpoint / a<2^{n-2}) / Case-2(G odd/even) /
  boundary w_1=2^{n-1} is exhaustive AND disjoint in the augmented space.

---

## 2. upper-vertex-reduction — NEW (copy-of direct-constructive) — CHANGES REQUESTED (built)

**Verdict: CHANGES REQUESTED — approved into the build set with the load-bearing step flagged.** This
is the genuinely-different upper framing DUE by the shared-gap-plateau rule (q-induction wall unmoved
3+ rounds).

**Graveyard / diversity check — PASSES:**
- NOT concavity-of-g (r3): explicitly uses only unconditional PL-max-at-vertex, never concavity. The
  r3 refutation was an interior VALLEY (a local MIN), which is harmless for an upper bound (a max
  characterization). Genuinely distinct.
- NOT step-by-step q-induction (r6 fixed-point obstruction kills SINGLE-STEP descent; this is a GLOBAL
  max characterization, collapsing an infinite family to finitely many vertex TYPES). Distinct.
- NOT potential/monovariant, greedy-XOR, or the menu. This is a structural reframe of the proof
  organization, not a vocabulary rename of the same move-set — it converts "bound f at every interior
  point via an adaptive strategy" into "bound f at finitely many vertices," where T and G are already
  certified-closed and only ONE explicit config (the geometric, type S) is new work.

**Kill-switch RE-RUN AT THE GATE (mechanism + conclusion) — PASSES:**
Computed min-over-4-cuts of the alternating sum A on q=5 (scaled D=31, geometric (16,8,4,2,1)):
- geometric fmin = **1.0000 exactly** — the tight worst case, and it is a boundary/vertex point
  (gap b_4−b_5 = 1/D AND sum = 31/D both active).
- 8 strict-interior flat configs: fmin ∈ [0.006, 0.200], all **< 1**. No interior peak above 1/D.
- Conclusion: the framing targets a TRUE statement AND max_{K_5} f is attained at the geometric
  vertex, uniquely at exactly 1/D. Kill-switch PASSES; do NOT drop it, do NOT fall back to FRAMING 2.

**Load-bearing gaps the builder MUST establish (this is the whole novelty):**
- **Step 2–3 (f PL + max-at-vertex).** DO NOT lean on the outline's stated principle "marginal of a
  jointly-PL function is PL" — that is FALSE in general (partial-minimisation preserves PL only under
  JOINT CONVEXITY, and A = μ{N odd} is a non-convex alternating sum). The empirics confirm max-at-
  vertex HOLDS, but the PROOF of it must not cite the false general principle. Either (a) prove f is
  linear on each arrangement cell by a direct structural argument specific to this A, or (b) prove
  max-at-vertex without full PL-ness (e.g. show any interior point can be pushed toward a vertex
  without decreasing f). This is the pass/fail step — if it cannot be made rigorous, the framing
  collapses to a numerical observation.
- **Step 4 case S (geometric-vertex leaf).** Bound f(S-vertex) ≤ 1/D with an explicit (q−1)-cut leaf
  strategy. This is a SINGLE explicit config — much cheaper than the whole residual — and is the only
  genuinely new leaf. Must be written, not asserted "= 1/D EXACTLY because dyadic dominance."
- **Step 4 exhaustiveness (T∪G∪S).** Prove every arrangement vertex is type T (tie), G (gap=1/D), or
  S (pure sum-boundary geometric). Watch vertices where several piece-lower-bounds b_i=1/D are active
  — confirm they collapse into T (ties) or G. Do not leave this as "verify."
- Keep the argument a GLOBAL max characterization; never argue f is concave (that reopens the r3
  valley) and never a single-step descent (that reopens the r6 fixed point).

Registered by copy_approach off direct-constructive (inherits Elo; imports lower bound + IH(q≤4) +
CaseB-Reductions). Build it — but the reviewer must treat step 2–3 as the acceptance criterion.

---

## 3. upper-general-cascade — ADVANCE (B2, corrected threshold) — APPROVE

**Verdict: APPROVE.** The arithmetic correction is verified and the advance is legitimate.

- **Threshold fix VERIFIED.** 1 − 2(a_2+a_3) < (2^{n−1}−1)/D ⟺ a_2+a_3 > (2^{n+1}−2^{n−1})/(2D) =
  3·2^{n−1}/(2D) = **3·2^{n−2}/D**. The file's 2^{n−1}/D is exactly 50% too small. The correction is
  arithmetically correct and MUST be made before advancing.
- **Consequence is real, not cosmetic.** The B2 residual (a_2+a_3 ≤ 3·2^{n−2}/D) is EMPTY for n≤2 but
  NONEMPTY for n≥3 (explorer LP: n=3 min a_2+a_3 = 17/45 < 2/5; n=5 = 11/45 < 8/21). The file's current
  "B2 settled for n≤2 for the right reason" is right only vacuously; the correction exposes a genuine
  n≥3,4 residual. Fixing the file's overclaim is itself valuable (prevents a false "solved").
- The geometric sits EXACTLY at a_2+a_3 = 3·2^{n−2}/D (verified n=2..5) — correct tightness calibration.

**Issues to close while building:**
- Step 3 (B2-flat leaf) is the real open work — the explicit n-cut cut pattern and its <1/D bound are
  UNWRITTEN. The dyadic cap chain a_j < 3·2^{n−j}/D is stated with mechanism (gaps>1/D + the a_2+a_3
  bound force each a_j below the geometric ceiling) — sound analog of IH4-flat's b_2<4/D, but the leaf
  strategy itself must be constructed, not asserted.
- Test the leaf on the explorer's exact residual witnesses: n=3 {47/90,31/135,43/270,4/45} and n=5
  {32/63,2/15,73/630,31/315,17/210,4/63}.
- Do NOT re-propose IH+(m) dual-bound (r6 graveyard).

---

## Diversity note for the orchestrator

Positive this round: the three build slugs attack three DIFFERENT walls (L2 lower / B2 upper /
IH(q≥5) upper) with two distinct upper-side organizing principles (step-cascade vs global vertex
characterization). The round-6 diversity flag (twins collapsed to one pair-creation move-set on the
upper wall) is answered by upper-vertex-reduction's global-max reframe. If upper-vertex-reduction's
step 2–3 cannot be made rigorous next round, the upper wall will again be down to one framing —
escalate then.

## Ranking (updated, stale flags cleared)
- upper-general-cascade 1685.8 (advanced, live)
- direct-constructive 1682.9 (advanced, live) — drawn twin, slight nudge from tie-breaks
- upper-vertex-reduction 1642.1 (new, gated-in; below established leaders, above dead)
- caseB-matching 1510.8 (dead-end)
- potential-duality 1418.9 (parked)
- induction-recursion 1331.0 (dead-end)

build set: direct-constructive, upper-vertex-reduction, upper-general-cascade
