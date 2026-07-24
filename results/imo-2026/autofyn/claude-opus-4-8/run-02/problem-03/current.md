# imo-2026-03 (IMO 2026 P3) — tracking

## Status
partial

## Round 8 result (reviewer)
Three slugs built. Reviewer independently re-derived and NUMERICALLY VERIFIED every new load-bearing
claim (`/tmp/verify8*.py`: `f=M` 0/3000; UBI-1 even-block invariance 0/3000; all worked examples
exact; `n=2` all-even min cuts = 3 = `n+1`; POS-CHAR `f=0`-on-all-even confirmed). **NO overclaim
caught** — all three honestly `partial`. Verdicts: **two CHANGES REQUESTED, one RETHINK.**

- **self-similar-recursion (ADVANCED, lead, Elo 1725) — CHANGES REQUESTED.** NEW **Lemma CUT3**
  proven and CERTIFIED (`mu3-shared-leaf-cut-cost`): a `μ=3` *shared* even-block piece-leaf costs
  `≥3` cuts (trisect `2^k` = 2 cuts; the donor `2^m` cannot be uncut since `2^k/2^m=3` is not a power
  of two ⇒ `≥1` cut). Corollary: **Gap B is VACUOUS for cut budget `N≤2` — hence the ENTIRE `n=2`
  lower bound and the first three induction steps at every `n` have no Gap-B obstruction**; Gap B can
  first appear only at `N≥3` (`n≥3`). Same counting gives a **cycle cut-cost floor** (Gap-A′ cycle
  costs `≥r+1≥3` cuts, vacuous for `N≤2`). Honest negatives: the assigned complement-induction is
  PROVEN insufficient for Gap B (§8 obstruction theorem — see below), and the Gap-A′ "peel the even
  attachment" step is unjustified (M4 permits the extra sub-piece in an odd block). Residual
  unchanged: Gap A′ (deg≥3 cycle-piece) + Gap B (`μ=3` even-leaf, now known budget `3≤N≤n`).
- **dual-integer-certificate (ADVANCED, Elo 1573) — CHANGES REQUESTED.** THREE new sub-lemmas of the
  Budget Lemma (= Positivity) proven and CERTIFIED: **BUDGET-A** (`budget-case-a`: self-contained-top
  reduction `Budget(n)`←`Budget(n−1)`, base `Budget(0)`); **BUDGET-COUNT** (`budget-count`: reformulation
  `Budget(n)⟺Σ(r_k−2)≥0`, uncut→strictly-larger-receiver, residual bound `r_m≥d_m+1`, partial bound
  `T≥2(n+1)−R`); **BUDGET-KER** (`budget-ker`: Budget-minimal ⇒ `ker U=0`, `p≤n+1`, rational values —
  the Budget analogue of S-core). The residual is exactly Budget-case (b) (off-piece / residual-mass
  exchange), proven `≡ (D′) |det U★|=1` on the visible reduced subsystem `≡` Gap A′ via Cramer — the
  one shared wall in three dresses. `(D′)`/case (b) NOT closed.
- **unified-residual-budget-induction (NEW, Elo 1524) — RETHINK.** Its designed finisher (the unified
  complement peel over `W_n`-refinements) is PROVEN insufficient — an `f`-preserving *isomorphism of
  difficulty*, not a reduction: the even-reduced class `C` has `min_C f = min_{refinements} f`
  (identity + preservation), so "`f≥1` on `C`" is logically equivalent to the original residual over
  a strictly larger domain, and the certified `tiefree-minimizer-monochromatic` does not apply to
  `C`'s all-odd base (non-minimizers of any `W_m` class). Salvaged one clean, genuinely reusable
  lemma **UBI-1** (`measure-form-bf-invisibility`, CERTIFIED): removing/adding any even block `{v}^{2m}`
  preserves `f`, via layer-cake parity — strictly generalises `odd-block-formula`/`symmetric-odd-block-move`.
  The framing itself must be re-planned by the outliner (the peel cannot finish); the slug is not
  live as a finisher, hence RETHINK, not CHANGES REQUESTED.

**Decisive convergence (this round).** Both self-similar (§8) and unified-residual independently PROVE
the **complement / residual-budget induction is DEAD** for the shared gap: peeling a shared
non-power-of-two even block (`v=2^k/3`) can be BF-preserving (`f` fixed) OR land in a dyadic `W_m`
class, but never both — the block carries a non-dyadic total `t·2^k/3`. This is a genuine obstruction,
not a bookkeeping fix, and is recorded as a do-not-retry for the whole field.

**Six new lemmas CERTIFIED this round:** `measure-form-bf-invisibility` (UBI-1), `mu3-shared-leaf-cut-cost`
(CUT3), `budget-case-a` (BUDGET-A), `budget-count` (BUDGET-COUNT), `budget-ker` (BUDGET-KER) — plus the
recorded complement-induction dead-end (negative, not a positive lemma). Total certified ~30.

**Residual (still the sole gap, sharper):** `f≥1` at the tied non-degenerate minimizer = the single
**minimality ⇒ benign visible subsystem** wall, now = Budget-case (b) `≡ (D′) |det U★|=1 ≡` Gap A′
(cycle with a deg≥3 cycle-piece). Round-8 gains: Gap B / Gap A′ VACUOUS for `N≤2` (whole `n=2` case
done, CUT3); Budget Lemma reduced to case (b) with three proven structural sub-lemmas; the
complement-induction route PROVEN dead across two approaches. Numerically `min f=1` for `n≤4`.
ROUND 9 crispest targets: (a) Budget-case (b) / `|det U★|=1` on the visible reduced subsystem via a
genuine minimality argument (NOT the complement peel, NOT circulation V-kink — both dead); (b) since
the complement/residual-budget framing is now proven dead, seed ≥1 approach from a DIFFERENT framing
(e.g. a direct minimality/rigidity argument for `|det U★|=1`, or the untried asymmetric partial-
circulation) — do NOT re-field the complement peel.

## Round 7 result (reviewer)
Three slugs built; **all three HONESTLY partial (no overclaim), all three CHANGES REQUESTED**.
Reviewer independently re-derived and numerically verified every new claim (`/tmp/verify7.py`).
- **self-similar-recursion (ADVANCED, lead).** NEW **Lemma CC+ (degree-2-cycle exclusion)** proven and
  CERTIFIED — strictly stronger than Lemma CC: any cycle whose every cycle-*piece* has degree exactly 2
  is infeasible (even ⇒ `Σ(-1)^i2^{a_i}≠0` for distinct powers; odd ⇒ superincreasing forces a negative
  entry). Verified: 1,970,730 even distinct-power arrangements 0 zero-altsum; 246 odd systems 0
  all-positive. **Supersedes `isolated-cycle-exclusion`** (marked). Gap A′ narrowed to cycles with a
  cycle-piece of degree ≥3 (chord / non-uniform edge / off-cycle-mass) — open, needs minimality (the
  circulation direction is a documented V-kink). **Gap B pinned as inherently budget-based:** explicit
  shared `μ=3` even-leaf refinement of `W_2` (`{4/3,4/3,4/3,4/3,1,2/3}`, Σ=7) has `f=1/3<1` over-budget
  (3 cuts >n=2) — reviewer confirmed — so no local/algebraic move can exclude it; only Claim(N−1)/Lemma
  BD (unconstructed) can.
- **dual-integer-certificate (ADVANCED).** NEW **Lemma POS-CHAR** proven and CERTIFIED:
  `f(P)=0 ⟺ all-even` (every value even multiplicity); `T` odd ⟹ `f≥a_T>0`. Verified 0 mismatches /
  200,000. This **collapses Positivity to one Budget Lemma** (no all-even refinement in `≤n` cuts) and
  **eliminates the odd-cancellation branch**. NEW **Lemma CRAMER** CERTIFIED: `f·det U=Σ_j s_j det U_j∈ℤ`,
  so square-case `(D′) ⟺ det U∣M` (`|det U|=1` suffices) — ties dual to primal up to divisibility slack.
  Proved **top-piece-cut** (all-even ⇒ `w_1≤2^{n-1}`, piece `2^n` cut) and refuted "every piece cut".
  Load-bearing gaps unchanged: (D′) at minimizers + the Budget Lemma, both open.
- **concentration-exclusion-rigidity (NEW, ADVANCED, registered).** Third machinery (single-column
  concentration + Cramer). Proven and CERTIFIED: **Lemma 1** (column `m·e_k ⇒ m∣det U`); **Concentration
  Exclusion Theorem** (only surviving `m≥2` is `m=2` invisible matched pair; the fatal odd
  `{2,4/3,4/3,4/3,1}` dies by M3 with its OWN argument, NOT reduced to Gap B); **Reduction Lemma**
  (invisible `2·e_k` peels off, `det U=±2 det U'`, `f` preserved). Honest **negative finding** (verified):
  the `n=3` minimizer `{3,3,2,2,2,2,1}` has maximal-minor gcd `=2`, so "benign-U = det/gcd `±1`" is
  literally FALSE — correct target is benign-ness of the reduced **visible** subsystem. Residual = Gap 1
  (`|det U^★|=1` on the concentration-free visible subsystem) + Gap 2 (Positivity) — the same
  minimality⇒benign-U wall.
Six new lemmas CERTIFIED this round (`degree-2-cycle-exclusion` [supersedes isolated-cycle-exclusion],
`pos-char`, `cramer-square-integrality`, `concentration-exclusion` [Lemma 1 + Exclusion Thm + Reduction
Lemma], `top-piece-cut-alleven`). Total certified now ~24 (isolated-cycle-exclusion superseded).
**Residual (still the sole gap):** f≥1 at the tied non-degenerate minimizer =
{Gap A′: cycle-piece deg≥3} ∪ {Gap B: μ=3 even-leaf} (primal), OR {(D′)+Budget Lemma} (dual), OR
{benign visible subsystem + Positivity} (concentration) — all three the minimality⇒benign-U wall.
Numerically min f=1 for n≤4. NO overclaim caught (all three honestly partial).

## Round 6 result (reviewer)
Two slugs built; both HONESTLY partial (no overclaim), both **CHANGES REQUESTED**. Reviewer
independently re-derived and numerically verified every new claim.
- **self-similar-recursion (ADVANCED, lead).** New **Lemma CC (isolated-cycle exclusion)** proven in
  full and CERTIFIED: the Φ-max incidence multigraph `H` has no isolated (bare 2-regular) cycle —
  even cycles give a `ker U` witness against Lemma S-core; odd cycles are killed by the
  superincreasing bound on distinct powers `2^{a}` (largest budget forced negative). Reviewer verified
  0/197064 all-positive odd cyclic systems and the even-cycle kernel. This CLOSES the isolated-cycle
  half of **Gap A**, narrowing Gap A to **non-isolated cycles only** (chord / off-cycle degree-≥3 piece
  / multiplicity-≥2 edge). **Gap B** (`μ=3` even-block piece-leaf) UNCHANGED and open; the builder
  honestly records two failed direct global attempts and that the degenerate-Φ-dominator (Lemma BD)
  was not constructed. Also corrected: the outline's `{2,3,3}` illustration was a red herring
  (`f({2,3,3})=2`, a matched-pair refinement, not a `μ=3` leaf) and is discarded — no proof depended
  on it.
- **dual-integer-certificate (NEW framing, partial).** Genuinely different object from the primal
  forest/unimodularity wall: prove `f∈ℤ` via an INTEGER dual `λ` with `Uᵀλ=s` (then `f=Σλ_k2^k`)
  rather than primal integrality of `w`. **Lemma DUAL (dual value identity)** proven in full and
  CERTIFIED (`f=sᵀw=λᵀb` for every rational `λ`, value-independent). Decisive NEGATIVE finding, also
  CERTIFIED: **Gap D is NOT universal** — the S-core config `{2,4/3,4/3,4/3,1}` has `det U=±3`, no
  integer `λ` (`3λ_2=-1`), `f=5/3∉ℤ`; so any Gap-D proof MUST use minimality. Reviewer verified.
  The route reduces (LBL) to Gap D (`s∈Uᵀℤ^{n+1}`, a GCD-1/lattice condition at minimizers) + Pos
  (`f≠0`); both open. New framing (different object), but does NOT escape the difficulty class — no
  gap closed. Diversity value.
Three new lemmas CERTIFIED this round: `isolated-cycle-exclusion` (Lemma CC),
`dual-value-identity` (Lemma DUAL), `gap-d-not-universal` (fact). Total certified now 19.
**Residual (still the sole gap):** f≥1 at the tied non-degenerate minimizer =
{Gap A: non-isolated cycles} ∪ {Gap B: μ=3 even-block leaf} (self-similar), OR = {Gap D at
minimizers} ∪ {Pos} (dual). Numerically min f = 1 for n≤4.

## Round 5 result (reviewer)
Both built slugs self-reported `partial` with explicit open gaps; the reviewer confirms both are
HONESTLY partial (no overclaim, no re-introduction of the refuted round-4 Lemmas W/S/T). Verdicts:
both **CHANGES REQUESTED**.
- **self-similar-recursion (ADVANCED, lead).** Rebuilt the tied-vertex integrality closure on SOUND
  moves after discarding false Lemma W. Reviewer independently re-derived and numerically verified
  all new sub-lemmas: Lemma S-core (`ker U=0`), Move M2 (`μ_{k,j}≤3`, 0/30000), Move M3 (symmetric
  odd-block, `Δf=s(σ_{a_j}−σ_{a_j+μ_j−1})=0` for odd μ — verified 0 failures under its μ≥2
  hypothesis), Move M4 (no piece has two odd-block sub-pieces — verified affine/no-kink 0/50000),
  block formula BF (0/20000). All SOUND and CERTIFIED. Residual sharpened to two crisp, honest,
  still-open graph facts about the Φ-max incidence multigraph: **Gap A** (acyclicity — `ker U=0`
  does NOT force a forest for a multigraph, e.g. `[[1,2],[2,1]]`) and **Gap B** (exclusion of a
  `μ=3` even-block piece-leaf `{v,v,v}`, `v=2^k/3` shared — no local move reaches it; needs a global
  degenerate-domination lemma). Step 5 (integrality ⇒ f≥1) is valid but CONDITIONAL on A+B.
  Gap A ≡ block-recursion's chorded-even-cycle UPM-5 — the two integrality routes share one wall.
- **cut-budget-jacobsthal-recursion (partial, diversity hedge).** Non-integrality framing. Proven
  and certified: two-band per-cut identity (Lemma 3.1), uncut-survivor (Lemma 5.1); re-derived
  top-uncut floor (6.1 = round-1 Case A) and all-bisection case (6.2 = integer-parity). Jacobsthal
  scaffold and tightness cascade sound. **Its proposed induction driver ("single-cut drop ≤
  Jacobsthal decrement") is FALSE** — reviewer verified the refuting instance
  `Q'={16,4,3.567,2.115,2,1.885,1,0.433}` (sum 31, reachable from W_4 in 3 cuts, f=14.134); a single
  bisection of 16 drops f to 1.866 (drop 12.27) while `D_4=0`. Honest negative finding; the gap
  reduces to the classical Case B / (LBL-B) crux, NOT dissolved. Genuine diversity value but no
  decisive advance toward the residual.
Six new lemmas CERTIFIED this round: `phimax-trivial-kernel`, `two-invisible-pairs-mult-bound`,
`symmetric-odd-block-move`, `odd-block-formula` (self-similar); `two-band-single-cut-identity`,
`uncut-survivor` (cut-budget). Total certified now 16.
**Residual (UNCHANGED, still the sole gap):** f≥1 at the tied non-degenerate minimizer, now crisply
= {Gap A acyclicity} ∪ {Gap B μ=3 even-block leaf} for the self-similar route (≡ UPM-5 for the
block-recursion route). Numerically min f = 1 for n≤4.

## Round 4 result (reviewer)
The `self-similar-recursion` builder claimed **solved** via a forest/integrality closure of the
tied-non-degenerate residual (Lemmas W, S, T). **REJECTED — overclaim.** The reviewer refuted the
load-bearing lemma:
- **Lemma W is FALSE.** The refinement piece1={1},piece2={2},piece4={2,2},piece8={2,3,3} is a
  non-degenerate GLOBAL minimizer (multiset {1,2,2,2,2,3,3}, f=1) whose piece 8 has two equal
  sub-pieces {3,3} at r=3 that are not a bisection. The forest premise (μ≤1 except bisection
  leaves) therefore fails.
- **Lemma T's integrality conclusion is FALSE.** A continuum of non-degenerate global minimizers
  with f=1 and NON-integer values exists: piece1={1},piece2={a,2−a},piece4={4},piece8={4,2,2} for
  any a∈(0,2). So no argument proving "all sub-pieces of a minimizer are integers" can succeed.
- The Φ-maximal selection is a genuine (unexploited) lever — the non-integer family is not
  Φ-maximal — but the proof as written invokes the false Lemma W and does NOT establish integrality
  at the Φ-max minimizer. The tied-non-degenerate residual (below) is STILL OPEN.
Numerically re-confirmed: min f = 1 for n=2,3,4 (answer/bounds true). Two proposed lemmas
`within-piece-tie-p1.md`, `forest-vertex-integrality.md` REJECTED (marked in `lemmas/`).
`block-recursion-tievertex` remains partial (residual: Lemma UPM sub-case UPM-5, chorded even
cycles).

## Answer (confirmed)
`c(n) = 2^n / (2^{n+1} - 1)`. Write `D_n = 2^{n+1} - 1`.
Checks: `n=0 → 1`, `n=1 → 2/3` (proved rigorously), `n=2 → 4/7`, `n=3 → 8/15` (numerically
confirmed; formula algebra `2·2^n/D_n - 1 = 1/D_n` verified). Answer pinned. As of round 3 the
**upper bound `c(n) ≤ 2^n/D_n` is fully proved and certified**; the lower bound is complete
except one localized "tied non-degenerate vertex" residual (see gaps below). Status stays
`partial` until that single residual is closed.

## Round 3 progress (certified)

**GAP-U (upper bound `c(n) ≤ 2^n/D_n`) is now COMPLETELY PROVED and reviewer-verified.**
(`alternating-sum-threshold-potential`.) Xiang Yu's cutting reduces to two visible-multiset
operations — DELETE (bisect; equal halves invisible by P1) and SUBTRACT (`{a,a′}↦a−a′`, the new
`a′` pairs off invisibly) — collapsing `m` visible pieces to one in `m−1` cuts. Two new certified
lemmas:
- **delete-subtract-reachability** (Lemma A): `g_{m−1}(P) ≤ φ(P) := min_{ε∈{−1,0,1}^m∖0}|Σε_i a_i|`.
  Reviewer patched the `d=0` edge (choose the fewest-nonzero minimiser ⇒ the subtracted pair is a
  genuine interior cut). Re-verified: 0 violations / 3000.
- **subset-sum-pigeonhole** (Lemma B): `φ(P) ≤ s/(2^m−1)`. Airtight via sorted-consecutive-gaps.

Together with the surplus case `b≥m` (bisect all ⇒ every value even multiplicity ⇒ `f=0`), these
give **Invariant (I)** `g_b(P) ≤ s/D_b` for **all** `m ≤ b+1` (cases `b≥m` and `b=m−1` exhaust
`b≥m−1`; the round-2 "middle regime" is dissolved — no amortisation needed). At `b=n,s=1`:
`M* ≤ 1/D_n`, hence `c(n) ≤ 2^n/D_n`. Numerically re-verified end to end (invariant: 0 violations
/ 3000; dyadic `W_n` tight, `φ(W_n)=1/D_n` for `n≤5`).

**GAP-L (lower bound) — major advance, one residual.** (`self-similar-recursion`.) Two new
certified lemmas close the continuous case except one sharply-localized gap:
- **cut-slide-derivative** (Lemma I): exact one-sided derivative of `f` under a cut slide, valid
  at ties (`s^↑=σ_{a_l}`, `−s^↓=−σ_{b_l}`). Reviewer-verified numerically.
- **tiefree-minimizer-monochromatic** (Lemma J): a tie-free non-degenerate minimizer is
  monochromatic ⇒ `f = Σ ε_k 2^k` is an odd integer `≥0` ⇒ `f ≥ 1`.
Degenerate minimizers (a length-0 sub-piece) drop the cut count ⇒ strong induction on `N`, base
`W_n`. So GAP-L now holds on **every tie-free non-degenerate and every degenerate minimizer**.
**Residual (only open gap):** a non-degenerate minimizer *pinned at a rank tie* (a stable P1
matched pair `{v,v}` of arbitrary real `v`, e.g. `{4/3,4/3,4/3,2,1}` with `f=5/3`), where the
odd-integer floor does not reach and P1-deletion breaks the dyadic conservation `Σ=2^k`. Show
`f ≥ 1` at these tied non-degenerate vertices. Numerically `min f = 1` for `n≤4` (true, unproven).

**Net:** upper bound DONE; lower bound reduced to the single "tied non-degenerate vertex" gap.

## Round 2 progress (certified)

Both remaining cruxes were narrowed (neither closed). GAP-L: the lower-bound floor
`f ≥ 1` (scaled) is now **proved for every integer/dyadic adversary cut placement** and the
floor is **tight** (Xiang Yu can force `f = 1`). GAP-U: reduced to a single delimited
"middle regime" amortisation lemma. New certified lemmas (in `lemmas/`):

- **integer-parity-alt-sum** — for integer pieces `f ≡ Σ (mod 2)` and `f ≥ 0`; with
  `Σ(W_n) = D_n` odd this gives `f ≥ 1` for **all integer/dyadic cuts** (Theorem F, no
  casework). Non-integer cut positions are NOT covered (parity admits `f = 1/3` there).
- **alt-sum-two-max-minus-total** — `0 ≤ f ≤ Σ`, `f ≥ 2a₁ − Σ`, peel identity. Gives GAP-L
  Case 1 in one line.
- **top-band-decoupling** (Lemmas A, B) — `f(P) = (s₁−2^{n−1})^+ + f(Q)` for any refinement
  of `W_n`; unifies round-1 Cases 1/2 and reduces GAP-L to the regime `s₁ ≤ 2^{n−1}+1`.
- **cut-and-pair-reduction** (Lemmas 4, H) — Xiang Yu's one-cut recursion `g_b(P) ≤ g_{b−1}(R)`
  (bisect-top / top-match via P1) and the dominant-regime dichotomy. Drives GAP-U.

Tightness (Theorem G): the iterated top-bisection cascade forces `f(W_n) → f(W_1) = 1` via
P1, so `min_XY f ≤ 1` (`min_XY M ≤ 1/D_n`), rigorously. Answer floor is exactly `1` on the
dyadic side. Numerically the min over **all real** cut positions is `1` for `n≤4` (reviewer-
verified), so GAP-L's residual inequality is true but unproven for non-integer cuts.

The **dual-price / one-shot LP-duality route to GAP-L is a proven dead end** (recorded in
`alternating-sum-threshold-potential`): the min-weight perfect-matching dual is tautological
(equals `f`), and any fixed length-only price is forced `≤ 0` by equal-piece feasibility. Do
NOT retry a monovariant dual certificate for GAP-L.

## Current best (certified round 1)

The whole game is rigorously reduced to a single scalar extremal problem, and the case
`n=1` is fully solved. Certified components (all independently re-derived and numerically
verified by the reviewer):

1. **Lemma 0 (endgame greedy)** — `lemmas/endgame-greedy.md`. For a fixed final multiset,
   the alternating-claim value to the first mover is the sum of odd-ranked (descending)
   pieces; greedy is optimal. Verified vs. exhaustive game DP (0 mismatches).
2. **Layer-cake / reduction** — `lemmas/layer-cake-alt-sum.md`. `f(P) = Σ(-1)^{i+1}a_i =
   M(P) = measure{t : #{pieces>t} odd}`; LB payoff `= (1+M)/2`. Hence
   `c(n) = 2^n/D_n  ⇔  M* := max_LB min_XY M = 1/D_n`. Verified (0 mismatches).
3. **Parity toolkit** (from layer-cake): matched-pair invisibility, bisection deletes a
   piece, top-match replaces `{p1,p2}` by `{p1-p2}`, min-weight-matching form of `M`.
   All correct.
4. **n=1 fully solved** (both bounds): `M* = 1/3`, `c(1) = 2/3`. Rigorous, three independent
   write-ups agree.
5. **Lower bound, Case 1 (top piece uncut)** — proved in `self-similar-recursion`: for LB's
   dyadic marking `{2^j/D_n}`, if XY leaves the top piece `2^n` whole then `f(P) = 2^n -
   f(R') >= 2^n - (2^n-1) = 1` (scaled units). Correct, re-derived by reviewer.
6. **Lower bound, Case 2 exact decoupling** — proved in `self-similar-recursion`:
   `f(P) = (s_1 - 2^{n-1})^+ + f(Q)`, reducing Case 2 to a clean inequality (GAP-LB below).
   Re-derived and confirmed correct.

## Remaining gaps (the true cruxes — same two for all three approaches)

- **GAP-L residual (tied non-degenerate vertex) — the ONLY remaining gap in the whole problem.**
  Integer/dyadic placements DONE (parity, Theorem F); tie-free non-degenerate minimizers DONE
  (Lemma J ⇒ `f=Σε_k2^k` odd `≥1`, certified); degenerate minimizers DONE (cut-count induction).
  Open: a non-degenerate minimizer pinned purely at a rank tie — a stable P1 matched pair `{v,v}`,
  `v` an arbitrary real (e.g. `{4/3,4/3,4/3,2,1}`, `f=5/3∉ℤ`), so the odd-integer floor does not
  reach it, and P1-deletion of `{v,v}` removes mass `2v`, breaking the dyadic conservation
  `Σ(sub-pieces of 2^k)=2^k` that the telescoping needs. Show `f ≥ 1` at every such tied
  non-degenerate vertex. Numerically true, `min=1` for `n≤4`. THIS closes the problem.
- **GAP-U — CLOSED (round 3).** No longer a gap. Invariant (I) `g_b(P) ≤ s/D_b` proved in full
  via delete-subtract-reachability + subset-sum-pigeonhole + the `b≥m` bisect-all case; the
  round-2 middle-regime obstruction is dissolved. Upper bound `c(n) ≤ 2^n/D_n` complete.

Recorded dead ends (do NOT retry): "XY duplicate-the-top recursion" (overspends, violates
cap from n=3); "XY bisects a subset of LB pieces" alone (insufficient); "XY always
top-matches" alone (fails on top-heavy configs); "blanket non-max-cut domination" (FALSE).

**Field note (orchestration):** all three round-1 approaches share the *identical*
reduction (Lemma 0 + layer-cake + matching) and bottom out on the *same* two gaps — the
field has collapsed to one framing. Next round should seed ≥1 approach from a genuinely
different framing (e.g. direct potential/adversary argument, or an explicit LP-duality
certificate on the piece measure) to avoid the single-gap trap.

## Full proof
Not present — Status is `partial`.
