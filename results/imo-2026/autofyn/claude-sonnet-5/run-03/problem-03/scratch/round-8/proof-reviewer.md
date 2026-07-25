# Round 8 proof-reviewer report — imo-2026-03

Overall problem Status: **partial** (unchanged — no approach claims, nor
achieves, a complete proof of the whole problem). All 5 built approaches
reviewed adversarially; every load-bearing new claim was independently
re-derived and/or stress-tested with fresh, from-scratch exact-`Fraction`
Python scripts (not the builders' own scripts), per round-7 lessons.
`results/imo-2026-03/current.md` has been rewritten to reflect this
round's accurate overall Status and Current best. Four new lemma files
were certified (see below); none rejected.

---

## 1. `lp-duality-split-polytope` — Verdict: CHANGES REQUESTED (Status: partial, correctly self-reported)

**Claim:** idx=1 (splitting the top piece), the last open case of the
general-`n` Multi-Piece Necessity Theorem for the triangular family, is
now closed via a direct 3-case peeling argument (`y_max≥N-1`, `y_max≤N-2`,
`N-2<y_max<N-1`) plus two new two-sided induction lemmas (Lemma $f$, Lemma
$g$) and a Small-Tail Bound. Combined with the previously-certified
Theorem B (idx≥2), this claims the full Multi-Piece Necessity Theorem for
every `idx`, every `n≥3`.

**Independent verification performed:**
- Re-implemented `OddSum`/`AltSum` from scratch and tested Lemma $f$
  (30,000 random exact trials, `r=1..15`, `t∈(0,1]`) and Lemma $g$ (30,000
  trials, `r=2..15`, `u∈(1,2)`): zero violations of the stated interval
  bounds in both.
- Tested the main theorem $A(N,N,y)\ge1$ with 60,000 random trials
  (`N=4..40`, `m=2..12`) plus a dedicated boundary sweep (thousands of
  points per `N,m` approaching `y_max=N-2` and `y_max=N-1` from both
  sides, `N=4..29`): zero violations; confirmed the exact tight case
  `A(4,4,3,1/2,1/2)=1` claimed by the proof.
- Traced the case-by-case algebra by hand: the three cases are exhaustive
  and disjoint (they partition `(0,∞)`); each "unique max, peel" step is
  correctly justified (elements bounded appropriately in each case); the
  final chained inequalities are correct in both directions (I re-derived,
  e.g., Case 1's conclusion `AltSum(S)≥y_max-(N-2)≥1` independently and it
  matches).
- Independently re-verified Theorem A's reduction (the bridge from
  original-units excess to the normalized `A(N,k,y)≥1` claim) by
  reconstructing the actual triangular family and computing both sides
  directly in original units for `n=3..7`, every `idx` (28 instances):
  exact match in every case.
- Re-confirmed (already certified) Theorem B's own proof is untouched and
  still correct; the combination logic (idx=1 ⟺ k=N, idx≥2 ⟺ k≤N-1,
  exhaustive) is correct.

**Finding: no gap found. This sub-theorem is genuinely, fully proved.**
Certified as `lemmas/idx1-closure-and-full-multi-piece-necessity.md`
(supersedes/completes `non-top-piece-theorem-b.md`'s scope).

**Why the approach's overall Status still must be `partial`, not
`solved`:** as the file itself correctly states, this is a **necessity**
result (no single-piece response to *this specific* LB family reaches
`c(n)`) — it is one ingredient toward, not a proof of, the general
upper-bound direction of the whole problem, and does not touch the lower
bound direction or the general (non-triangular-family) balanced region.
The builder's own Status line and scope note are accurate; no overclaim
found.

---

## 2. `self-similar-induction-on-n` — Verdict: CHANGES REQUESTED (Status: partial, correctly self-reported)

**Claim:** Branch II of the residual sliver's `L_0(ℓ,ε)` recursion is
proved, via a genuine well-founded strong induction on `ℓ`, to be
logically **equivalent** to the (separately still-open) Branch-I.A window
recurring at lower levels. A deeper hypothesis-cap bug was found in round
6/7's boxed `L_0(ℓ,ε)` statement and fixed by dropping a vestigial,
non-load-bearing cap.

**Independent check:** Read the full derivation of the counterexample-to-
naive-recursion (`ℓ=3, ε=1/2, c_1=39/10`) and the fix (showing Branch
I.A's closing inequality holds uncapped). The logic is sound: the file
explicitly exhibits a witness showing the reduction bottoms out in the
still-unproved window, so it correctly does **not** claim Branch II is
closed — only that the sliver's two previously-separate open pieces
collapse into one. This is exactly what real, honest partial progress
looks like; no overclaim, no hidden gap in what's actually asserted as
proved.

**Gap that remains (for the next round's builder):** the Branch-I.A
window itself (`c_1∈[2^{ℓ-1},2^{ℓ-1}+1-ε)` restricted to no second large
element) is still open at every level; closing it directly would now
(by this round's equivalence) also close Branch II for free.

---

## 3. `greedy-reduction-geometric` — Verdict: CHANGES REQUESTED (Status: partial, correctly self-reported)

**Claim:** Insertion-Robustness (Open Sub-Problem A, Subcase (a) of
Theorem 7'$(m,k;L)$'s inductive step) is now closed in full,
unconditionally, via new Theorem 12 (Single-Insertion Monotonicity) and
Theorem 13 (General Insertion Monotonicity): for any finite multisets
$N,R$ of positive reals, $\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N)$,
dropping the previously-hypothesized cap `max(R_1)≤μ_1` entirely.

**Independent verification:** I derived the rank-shift/parity argument
completely independently (before reading the file's own proof line by
line) and arrived at the identical conclusion: inserting one element at
an even original-parity position contributes `AltSum(suffix)≥0` (via the
nonnegativity fact), and at an odd position contributes
`v-AltSum(suffix)`, which is `>0` since `v > max(suffix) ≥ AltSum(suffix)`
(the insertion point forces `v` to exceed everything below it) — so in
both cases the change lies in `[0,v]`, confirming the theorem generally,
not just in special cases. Stress-tested independently with a fresh
50,000-trial exact-`Fraction` script (many forced ties): zero violations.
Confirmed the application chain to Open Sub-Problem A
(`OddSum(B'∪S''∪R1)≥OddSum(B'∪S'')≥S'`, direct and correct) genuinely
drops the cap hypothesis, since Theorem 13 needs none.

**Finding: no gap found; this is a genuine, correct, general closure of
Subcase (a).** Certified `lemmas/insertion-monotonicity-theorems-12-13.md`.

**Why Status stays `partial`:** Subcase (b) (Open Sub-Problem B,
Level-Absorption, cut-budget-corrected) remains open, untouched this
round, honestly reported as such.

---

## 4. `universal-halving-adversary` — Verdict: CHANGES REQUESTED (Status: partial, correctly self-reported)

**Claim:** New Theorem 12 (Generalized Subset-Tie Lemma, any index) is
proved: a direct generalization of the certified Theorem 9/11 allowing
XY to subdivide-and-tie any piece `p_i` (not just `p_1`) against a subset
`J` of the remaining pieces. Separately, honestly documents an
inconclusive/plateau finding: the survivor rate of best-of-named-additive
tools appears to *grow*, not shrink, with `n`, and per the outline-
reviewer's decision this round, the Existence Theorem's full closure is
redirected to the new sibling `global-lp-vertex-sufficiency`.

**Independent verification:** My first from-scratch attempt to verify
Theorem 12's construction numerically produced ~40% "violations" — tracked
this to my own script bug (I omitted the untouched original copy of a
tied piece `p_m`, `m∈J`, keeping only the split fragment; the construction
requires *both* copies present in the merged multiset). After correcting
this, 20,000 fresh exact trials gave zero discrepancies, confirming the
theorem is correct as stated (this near-miss is itself a useful
confirmation of how easy the corresponding error would be to make in a
real proof, and the approach file's own proof does state the construction
correctly with both copies).

**Finding: Theorem 12 is correctly proved; no gap.** Certified
`lemmas/generalized-subset-tie-theorem12.md`. The file's honesty about the
plateau/inconclusive result (explicitly not claiming the Existence Theorem
proved or disproved at any `n`) is accurate and appropriately cautious —
no overclaim.

---

## 5. `global-lp-vertex-sufficiency` — Verdict: CHANGES REQUESTED (Status: partial, correctly self-reported; new approach this round)

**Claim:** A Global Vertex Lemma (finite affine-shape structure of `V(p)`
for any number of simultaneously-split pieces, generalizing the certified
single/two-piece vertex lemmas), a new Lipschitz-continuity fact for
`V(p)` as `p` varies, and a resulting existence-of-a-maximizer corollary.
Identifies a precise obstruction (concavity of `V(p)` does not follow from
classical LP-value-convexity, since the parameter `p` enters the objective
directly, not just the RHS) — neither proved nor disproved.

**Independent verification:**
- Global Vertex Lemma: checked that the claimed extension from
  single/two-piece splits to any number of simultaneous splits is a
  purely local linear-algebra fact (each split piece contributes its own
  independent equality/free-block), correctly not requiring new
  machinery — legitimate assembly, no gap.
- Lipschitz continuity: checked the one delicate step (the
  rearrangement-inequality direction — sorted matching is the ℓ1-optimal
  minimum, so the canonical proportional matching gives a valid *upper*
  bound, not claimed as equality) is used in the correct direction; the
  proof is otherwise an elementary triangle-inequality argument. No sign
  error, no gap.
- The concavity obstruction diagnosis (classical LP value-convexity needs
  the parameter to enter only the RHS with a parameter-independent cost
  vector; here `p` enters both the RHS and the objective) is a correct
  and precise application of standard parametric-LP theory — I could not
  find a hole in this diagnosis, and it correctly explains why the
  "natural" next step doesn't fall out automatically.

**Finding: both the Global Vertex Lemma and Lipschitz continuity are
genuinely, fully proved; the concavity obstruction is honestly and
correctly diagnosed as open (not resolved either way), and the reported
15-trial numeric check at `n=2` is explicitly and correctly flagged as
weak/inconclusive, not a proof.** Certified
`lemmas/global-vertex-lemma-and-lipschitz-continuity.md`.

---

## Certified lemmas this round (all pass full bar: `sorry`-free, statement
correct, no stronger than proved, independently re-verified)

1. `lemmas/idx1-closure-and-full-multi-piece-necessity.md` — Multi-Piece
   Necessity Theorem for the triangular family, now complete for every
   `idx`, every `n≥3`.
2. `lemmas/insertion-monotonicity-theorems-12-13.md` — General Insertion
   Monotonicity (`OddSum(N∪R)≥OddSum(N)` unconditionally); closes
   Insertion-Robustness / Subcase (a).
3. `lemmas/generalized-subset-tie-theorem12.md` — Generalized Subset-Tie
   Lemma (any index, not just `p_1`).
4. `lemmas/global-vertex-lemma-and-lipschitz-continuity.md` — Global
   Vertex Lemma (any number of split pieces) + Lipschitz continuity of
   `V(p)`.

No lemma was rejected this round; no builder overclaimed `solved` for its
approach (all 5 correctly self-reported `partial`).

## current.md

Rewritten in full (`results/imo-2026-03/current.md`) to reflect: overall
Status `partial`; this round's five approach outcomes; the now-complete
Multi-Piece Necessity Theorem moved from "open gap" to "proved,
certified"; Insertion-Robustness/Subcase (a) moved from open to closed;
Branch II's reduction to the Branch-I.A window; the new honest finding
that additive-construction survivor rates may grow with `n`; and the new
`global-lp-vertex-sufficiency` approach's Global Vertex Lemma, Lipschitz
continuity, and precisely-located concavity obstruction. The two
remaining top-level gaps (lower bound: Branch-I.A window +
middle-regime + Level-Absorption; upper bound: balanced-region residual,
now split between the additive-tool route and the new LP/compactness
route via concavity) are stated explicitly at the end of "Current best."

## Overall verdict

No approach reaches `solved` this round (the whole `imo-2026-03` problem
remains unsolved). All 5 approaches get **CHANGES REQUESTED**: each made
genuine, independently-verified progress with an honestly-stated real gap
remaining; none is fundamentally broken (no RETHINK warranted). This round
is unusually productive: two previously-open gaps (idx=1 of Multi-Piece
Necessity; Insertion-Robustness/Subcase (a)) are now fully, independently
verified closed, and a genuinely new framing (`global-lp-vertex-
sufficiency`) has entered the population with real structural content and
a precisely diagnosed obstruction.
