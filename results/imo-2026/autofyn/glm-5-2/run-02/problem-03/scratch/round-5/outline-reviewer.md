# Outline review — imo-2026-03, round 5

Reviewed 4 approaches: ADVANCE `two-regime-disjunctive`, ADVANCE `cell-complex-l3`, REVISE `pairing-partner`, NEW `dyadic-halving-induction`. Verified load-bearing claims with exact-rational python (corollary bug, m_1-split branches, 5-cap family, moderate-dominant coverage, Φ=0 uniqueness, L(4) pair-pile). Prior dead engines respected (R-pile, A-pile, value-recursion, unified-potential, LP-dual, (U-E), bisect-recurse) — none re-entered.

---

## two-regime-disjunctive — APPROVE (CHANGES REQUESTED)

Headline target (U(3) → c(3)=8/15). Technique = finite menu of affine/abs-linear caps + multi-way contradiction — the SAME technique that closed the certified U(2) four-strategy family, generalized to n=3. Sound technique, not a dead engine.

Verified:
- **5-cap family {a, b−a, c−b, 2d−1, |a+b−c|} for d≥1/2**: 0 violations on N=60 grid (1041 configs, none with all 5 caps > 1/15). The contradiction is REAL (numerically confirmed). The GAP is writing the full case-by-case proof, not a false claim.
- Φ=0/dyadic cap imports (pair-pile, S1/S2/S3) all certified. L(3) imported as certified dependency (cell-complex). Correct.

Issues (fixable, not fatal):
1. **Step 4 (5-cap d≥1/2 contradiction) is unwritten.** The outline's sketch in Case c<a+b trails off ("need the full chain to get the contradiction"). The contradiction is numerically solid but the builder MUST write the complete chain (it is not yet a proof). The outline is honest that this is a GAP.
2. **Step 5 (d<1/2 thin sliver-tuning) is the hard GAP.** "Shave ε from a, match (a−ε) in d, split d's remainder to tune the 5-leftover alt-sum to base+ε with base<1/15" — the existence of base<1/15 via the tuning parameter is ASSERTED, not proved. The outline admits this ("the analytic proof of 'base<1/15 exists' ... is the hard step"). This is the make-or-break step for U(3); without it, the d<1/2 thin region is uncovered. Acceptable as a flagged GAP for the builder to attack, but the builder must NOT present the numerical "true cap ≈3/700 at (1,2,4,7)/14" as proof — it is evidence only.
3. **Step 6 "Moderate-dominant L∈[8/15,4/5] CLOSED" is OVERSTATED.** I checked: on N=60 grid, 782 moderate-dominant configs; 659 have a≤1/15 (cap-a works), but 123 (≈16%) have a>1/15 where cap-a FAILS. The outline only names "cap a or d−b−c" — cap-a is falsified for these 123, and the outline does not show cap d−b−c (or any other 17-family strategy) covers them. The builder must verify the FULL 17-family covers the moderate-dominant class, or this claim must be downgraded to "partially covered, GAP."
4. The dual vertex-principle (piecewise-concavity of Φ(P)) is correctly flagged as a FRAME not a proof — good. Do not let it become a hand-wave.

Verdict: technique sound (U(2) template), gaps honestly flagged, one claim overstated (moderate-dominant). BUILD.

---

## cell-complex-l3 — APPROVE (CHANGES REQUESTED)

L(4) certification + structural theorem + inductive lift. Owns G1 (Lemma L general-n).

Verified:
- **L(4) pair-pile multiset (8,8,4,4,2,2,1,1,1)/31**: sum=31=D(4), A=1=α(4)·D(4). Consistent with the certified enumeration (12 min multisets, min A=1/31, 0 violations). This is a legitimate finite certificate (same vertex-principle technique as L(3), sound). Fourth lower-bound data point (n=1,2,3,4 all certified over reals) — solid progress.
- The vertex-principle (continuous piecewise-linear A on compact polytope → min at arrangement vertex) is CERTIFIED round 4 and correctly applied. The DoF increase (n−1 tuples) and n=5 infeasibility (2.49B tuples) are correctly noted.

Issues:
1. **Structural theorem is CONJECTURED, not proved.** "Every level-n arrangement vertex attaining A=α(n) is the pair-pile family + one-zero degenerations" — verified n=3 (5 multisets), n=4 (12 multisets), but the mechanism ("pair-pile's equal pairs force even-mult blocks contributing 0, except the irreducible consecutive pair contributing α") is a combinatorial reformulation, not a proof. The outline is honest: "the proof must show ANY arrangement vertex NOT of the pair-pile form has A>α(n) WITHOUT enumeration." This is the load-bearing GAP. It is NOT a restatement of the vertex principle (the vertex principle is a reduction continuous→finite; the structural theorem is a characterization of which vertex wins — a different, harder claim). It is a real opening, not a verbal relabel.
2. **Inductive lift GAP.** Even with the structural theorem, "the level-(n+1) minimizer decomposes via M⊎R into a level-n pair-pile in R plus the M-sub-pile" is unproved. The outline admits this. The mechanism (D(n+1)=2D(n)+1 self-similar recursion) is plausible but the decomposition must be shown to preserve the vertex structure.
3. **Shared-wall note**: the structural theorem's mechanism (even-mult blocks, consecutive pair) overlaps with pairing-partner's superincreasing-R lever. This is NOT a near-twin (cell-complex is undecomposed variational; pairing-partner is decomposed Hall matching) — different framings, converging on the same equality structure. Acceptable. The outline correctly notes the cell-complex route is INDEPENDENT of the (FALSE) superincreasing-R corollary σ≤a_1.

Verdict: L(4) certification is real bug-free progress; structural theorem + inductive lift are real GAPs, honestly flagged, not restatements. BUILD.

---

## pairing-partner — APPROVE (CHANGES REQUESTED)

REVISE to fix the two certified-but-INVALID lemmas via the m_1-split.

Verified the bug claims (exact-rational python):
- **`lemma-superincreasing-R` corollary σ≤M/2=a_1 is FALSE for k≥2.** Confirmed: 4/15 integer n=3 k=3 configs violate (e.g. m=(3,3,1,1): σ=5>4=a_1). The outliner's "50%" is the real-valued fraction (likely higher than the integer 27%); the integer count is enough to confirm the corollary is invalid. The IDENTITY (a_j−Σ_{l>j}a_l=α(n+1)) STANDS; only the magnitude corollary is invalid. Correctly removed.
- **`lemma-L3-unrefined-R-subcase` proof only covers m_1≥a_1=4 (Branch 1).** Confirmed: the closed form A=7−2(s_3+s_5) is derived under "s_1=4 via b_1≤σ≤4," which requires m_1≥4 (so σ≤4). For Branch 2 (m_1<4), m_1 is NOT global rank 1 (a_1=4 is), so the formula's structure changes — the proof does not apply. The RESULT (A≥1/15) survives via the independent cell-complex L(3) certification. Correctly flagged.

The m_1-split is a SOUND partition: Branch 1 (m_1≥a_1, m_1 global rank 1) and Branch 2 (m_1<a_1, a_1 global rank 1) are structurally distinct and disjoint, covering all configs.

Issue (the framing is overstated, not the partition):
- **Branch 2 "cheap-kill / one-line dyadic-dominance identity" is OVERSTATED.** I derived the reduction: Branch 2's claim A≥2a_1−total_R=α(n+1) is equivalent to **rest_oddrank ≥ σ/2**, where rest_oddrank is Liu's odd-global-rank sum from the rest = {M-small}∪{R\{a_1}}. This is a HALL-TYPE MATCHING on the rest polytope (smaller than the full Match, but the SAME KIND of problem as Branch 1's Hall matching on rank indices). The outline's "closes it in one line IF the pairing bound holds" is circular: the "pairing bound" IS the Hall matching. The outline is partially honest (flags it as a GAP needing rigorous proof) but the "one-line / cheap-kill" framing misleads — BOTH branches reduce to Hall-type matchings, not just Branch 1. The builder must NOT treat Branch 2 as one-line; it needs a real proof that rest_oddrank ≥ σ/2 (which may be easier than Branch 1's full Match because the rest is a smaller polytope with all pieces < a_1 and R\{a_1} superincreasing, but it is not trivial).

Other:
- Branch 1 Hall matching on rank indices: CONJECTURE (verified n=1..5, OPEN), per-position bound s_{2j}≤a_{j+1} correctly noted as FALSE (b=(4/3,4/3,4/3) counterexample). Genuine Hall/marriage argument needed. Honest GAP.
- R-refined sub-cases (k≤n) remain OPEN. Correctly flagged.
- The re-worked L(3) proof (Branch 1 uses the round-4 casework valid only when m_1≥a_1; Branch 2 uses the cheap-kill) — the builder must verify the closed form A=7−2(s_3+s_5) is correct under m_1≥a_1 (the round-4 proof's assumption, now correctly scoped).

Verdict: the m_1-split is a sound, necessary fix for the invalid certified lemmas. The bug identification is accurate. The "cheap-kill" framing is overstated (Branch 2 is also a Hall sub-problem) but honestly flagged as a GAP. BUILD — fixing the certified-but-invalid lemmas is important for correctness regardless of whether G1 closes.

---

## dyadic-halving-induction — APPROVE (CHANGES REQUESTED) — REGISTER (NEW)

NEW G2 framing: Φ(config)=Σ|p_i−2p_{i+1}| (halving defect), Φ=0 iff dyadic, induction on halving depth. Genuinely different from two-regime-disjunctive (structural invariant + 2-adic framing vs config-variable casework) and from cell-complex (G2 upper bound vs G1 lower bound).

Verified:
- **Φ=0 iff dyadic (uniqueness)**: sound one-line lemma. Confirmed Φ=0 at the dyadic for n=1..5 (geometric series telescopes). The "a=2b=4c=…=2^n·p_{n+1}, sum=1 ⟹ p_{n+1}=1/D(n)" uniqueness is correct.
- **Local-kink (near-dyadic, harvestable partial)**: the asymmetric slopes (c=1 mass-up, c=2 mass-down) from the perturbation sweep are a genuine 2-adic signature. Verified 47/47 non-dyadic n=3 configs have cap<α(3). This is a sound harvestable PARTIAL lemma (the LOCAL half of (U-E), which round 4 correctly distinguished from the GLOBAL half = G2-restated).

Near-twin assessment (the dispatch's key question): I judge dyadic-halving GENUINELY FAR from two-regime-disjunctive, NOT a near-twin, because:
- The n=3 case split is organized by HALVING-LEVEL INDEX (which of the 3 consecutive ratios ≠2:1), a structural/2-adic disjunction — different from two-regime's config-variable inequalities (d≥1/2, c≥a+b, etc.).
- The sliver MECHANISM differs: dyadic-halving's is the Φ-kink perturbation (2-adic asymmetric slope), two-regime's is the affine/abs-linear cap from the 17-family. These are not technique-swaps on the same gap; they are different constructions.
- The distinctive territory is the general-n inductive lift (halving-depth induction), which two-regime does NOT own (two-regime is n=3-specific casework with no general-n lift planned).

BUT two serious risks (flagged, not fatal):
1. **n=3 shared wall with two-regime**: both need SOME sliver strategy for non-dyadic n=3 configs. If the Φ-kink sliver turns out to reduce to two-regime's 17-family sliver construction, the n=3 half becomes a near-twin. The outline honestly flags this. The builder must develop the Φ-kink sliver as a GENUINELY different construction, or the n=3 half adds nothing over two-regime.
2. **General-n inductive lift is UNPROVEN and ADJACENT to the KILLED bisect-recurse engine.** The killed engine (round 3) died because "f(n)/2 < f(n−1) strictly; bisecting does NOT reduce to a level-(n−1) sub-game with the same answer." The dyadic-halving lift recurses on R (a scaled level-n sub-config) when the top-level ratio is exactly 2:1 — structurally different from always-bisecting, BUT it faces the SAME WALL: the sub-config's cap does not determine the full config's cap because Xiang's marks span both M and R. The outline admits "the recursion on R is NOT a clean U(n) sub-problem." The structural distinction ("recurse on R when top is exactly dyadic, not always-bisect") is real but does NOT yet supply a mechanism for how cap(R-sub-game) relates to cap(full config). This is the load-bearing GAP and it is adjacent to a recorded dead end — the builder must provide a CONCRETE mechanism (not a verbal "we recurse on the config structure, not the value recursion") or this lift dies the same death as bisect-recurse.

Verdict: the Φ=0 uniqueness and local-kink are sound harvestable partials; the 2-adic framing is genuinely different. REGISTER (NEW). BUILD, but the builder should focus on: (a) the Φ=0 uniqueness lemma (clean, certify it), (b) the local-kink partial (harvestable, certify it), (c) the n=3 Φ-organization of the sliver (test whether it yields genuinely different sliver insights from two-regime's 17-family). The general-n lift should be left as a flagged GAP for the outliner to mature with a concrete mechanism — do NOT spend builder effort proving the lift this round (high risk of repeating the bisect-recurse death).

---

## Ranker actions

- **REGISTER** `dyadic-halving-induction` (NEW, APPROVED). Cold-start Elo 1500.
- No copies requested (verified — the outliner did not ask to branch).
- `pairing-partner-transfer` (RETIRED round 4, dead-end) and `induct-one-mark` (dead route) remain in the pool but sunk; they lose to all live approaches.

## Ranking (head-to-head, anchored to last outcomes)

Anchoring: cell-complex-l3 (verified-milestone, L(4) certified this round, bug-free) vs pairing-partner (advanced last round BUT certified lemmas found INVALID this round — setback). cell-complex narrowly wins this round: its certifications are accumulating and bug-free (L(3), L(4) reals), while pairing-partner's certified lemmas had invalid proofs (even though being fixed via m_1-split and the result survives via cell-complex). pairing-partner remains the furthest on the ANALYTIC general-n route (Hall conjecture verified n=1..5), so the gap narrows but does not invert dramatically.

comparisons = [
  {cell-complex-l3 > pairing-partner}   — clean accumulating certs vs buggy-lemma setback this round
  {cell-complex-l3 > two-regime-disjunctive}  — L(3),L(4) certified milestones vs U(3) still open
  {cell-complex-l3 > dyadic-halving-induction} — established certified vs new unproven
  {pairing-partner DRAW two-regime-disjunctive} — both partial; p-p has bug-but-sound-fix + Hall conjecture (n=1..5); two-regime has 5-cap numerically sound but moderate-dominant overstated; different gaps (G1 vs G2)
  {pairing-partner > dyadic-halving-induction}  — established + verified conjecture vs new
  {two-regime-disjunctive > dyadic-halving-induction} — established 17-family vs new Φ-framing (but share n=3 wall)
  {pairing-partner > pairing-partner-transfer}  — live vs dead-end
  {pairing-partner > induct-one-mark}  — live vs dead route
  {cell-complex-l3 > pairing-partner-transfer}
  {cell-complex-l3 > induct-one-mark}
  {two-regime-disjunctive > pairing-partner-transfer}
  {two-regime-disjunctive > induct-one-mark}
  {dyadic-halving-induction > pairing-partner-transfer}  — new live vs dead-end
  {dyadic-halving-induction > induct-one-mark}  — new live vs dead route
]

build set: two-regime-disjunctive, cell-complex-l3, pairing-partner, dyadic-halving-induction
