# Outline review — imo-2026-03 (IMO 2026 P3), round 8

Context: whole problem is ONE gap from solved. UB `c(n)≤2^n/D_n` certified; answer `c(n)=2^n/D_n`
pinned; sole residual = `f≥1` at the tied non-degenerate minimizer = "minimality ⇒ benign visible
reduced subsystem." The outliner nominated a 4-approach field: one NEW plateau-breaking framing plus
three advances of the live routes. I vetted each adversarially, ran the key numeric check on the NEW
slug's load-bearing step, registered the NEW slug, and re-ranked the whole field.

---

## 1. unified-residual-budget-induction — NEW — APPROVE (register + build)

**Technique is genuinely new and NOT a re-tread.** Strong induction on cut count `N` via removal of a
BF-invisible (even) tie-block, using the certified `odd-block-formula`/`symmetric-odd-block-move` fact
that even blocks contribute exactly 0 to `f`. This does not touch the determinant/benign-U object at
all, so it is a real fresh framing — exactly what the plateau rule (routes 2/3/4 share one wall for
3+ rounds) demanded. I explicitly checked it against every REFUTED path in Rules/Broken:
- NOT the circulation V-kink (no local variational move).
- NOT "benign=det/gcd±1" (never invokes it).
- NOT global integrality (it uses BF-invisibility + IH, never claims sub-pieces integer).
- NOT the Jacobsthal per-cut f-decrement driver (block removal keeps `f` EXACTLY equal via BF, it is
  not a per-cut monovariant on `f`).
- NOT odd-cancellation Positivity (uses POS-CHAR), NOT laminar geometry, NOT consecutive-ones/TU.
Clean. The two "peel" gaps are genuinely different machinery from the benign-U determinant chase.

**The `f = f(complement)` peel and the cut-cost gaps are real, but G2 is the decisive crux — and the
naive statement is provably in tension.** I ran the outliner's own example (`self-similar` step 2 /
Gap-B explorer's exp. 2), n=3 leaf at top piece 8, donor piece 4:
`P* = {8/3,8/3,8/3,8/3,2,4/3,1}`, `Σ=15=D_3`, `f=5/3`. Removing the even block of four `8/3`'s:
- BF-preserving complement `{2,4/3,1}`: `f=5/3` ✓ but `Σ=13/3` — **NOT a refinement of any `W_m`**
  (no power-of-two-stick total). So "apply Claim(N−k) to the complement" does NOT type-check: Claim
  is proved only over refinements of `W_n`, and this object is outside that class.
- Mass-conserving reattach (give the donor `8/3` back so piece 4 = `{4}`): complement `{4,2,1}` is a
  genuine `W_2` refinement, `Σ=7` ✓ — but now `f=3 ≠ 5/3`, so **BF is broken**.

So the two requirements of G2 — (i) the complement is a legitimate `≤(N−k)`-cut refinement of a `W_m`,
and (ii) `f(complement)=f(P*)` — are in direct tension in the natural construction. This is precisely
the round-2 role rule: *check the IH actually applies to the POST-move object.* Here it does not,
under either naive reattachment. This does NOT kill the approach (a new whole-attempt with an explicit
honest gap is a valid population member), but the builder must resolve G2 by EITHER (a) extending
Claim to a broader dyadic-multiset / rescaled-sub-stick class and proving `f≥1` there directly — which
risks re-opening the whole difficulty, so this must be surfaced, not asserted — OR (b) finding a
conservation that is simultaneously BF-invariant and lands in a genuine `W_m` refinement.

**Issues to close while building (do NOT assert):**
- **G2 (load-bearing, above)** — the complement-legitimacy vs BF-invariance tension. Prove which class
  Claim(N−k) is being invoked over; do not hand-wave `f(P*)=f(complement)≥1`.
- **G1 (cut-cost ≥ t)** — currently numeric evidence only. Must prove `v` (shared, non-power-of-2)
  forces every copy into a split piece; the outliner correctly avoided the REFUTED `p≥n+1` reduction
  (count by block SIZE t, never distinct-value count p — n=2 all-even has p=2 via a mult-4 class).
- Base case: cover the leaf-at-the-very-top sub-case (the sole `f<1` witness, over-budget for its own
  n) — the induction must confirm it never fits `≤n` cuts.

I did NOT copy this slug into the two-fill fork. Fill A (generalize the concentration Reduction Lemma
to peel a whole even block) is already exactly `concentration-exclusion-rigidity`'s C1 job, and Fill B
(combinatorial recount) is the Gap-B explorer's route inside `self-similar`. Copying would duplicate
existing slugs and over-populate the shared G2 wall. Build the unified slug as ONE new whole-attempt
primarily on the combinatorial-recount spine (the genuinely new part); revisit a copy next round only
if it proves a shared prefix and both fills become independently viable.

## 2. self-similar-recursion — ADVANCE (lead, Elo 1725) — APPROVE (build)

Technique sound; imports certified CC+/S-core/M2/M3/M4/BF. Residual is the primal cycle route:
Gap A′ (cycle carrying a deg≥3 cycle-piece) via peeling the off-cycle/chord even attachment
(BF-invisible ⇒ drops degree to 2 ⇒ CC+ applies), plus Gap B via Claim(N−3) on the complement.
Distinct machinery from the unified slug at Gap A′ (it uses the primal cycle/CC+ structure, not a
generic block). Correctly forbids the dead levers (circulation V-kink; naive M4-extension to
mixed/even pairs — the det-minimality explorer re-verified this is ALSO a V-kink, `f=1+2|δ|`).
- **Open gap to close, not assert:** its Gap A′ peel assumes the deg≥3 attachment is ALWAYS an
  even/BF-invisible block. If the off-cycle mass is an ODD block it feeds `f` and the peel fails —
  the builder must PROVE the attachment can't be odd-block, not assume it.
- Its Gap-B step shares G2 with the unified slug (flagged in the outline — good). Same complement-
  legitimacy caveat applies; do not assert `f(P)=f(complement)`.

## 3. dual-integer-certificate — ADVANCE (Elo 1573) — APPROVE (build)

Best-de-risked pick. The Budget-Lemma peeling induction has a genuinely CLEAN, self-contained,
certifiable sub-lemma independent of the hard wall: **case (a) `R=0` (`w_1=2^{n-1}`, top pair
self-contained)** reduces to an all-even refinement of `W_{n-1}` with exactly `N−1` cuts ⇒ strong
induction on n ⇒ `N≥n+1`. The budget-lemma explorer verified this reproduces the certified n=2 minimal
example exactly. Build case (a) as a certifiable sub-lemma — real progress even if case (b) resists.
- **Case (b)** (`R>0` or a `w_1`-copy outside piece `2^n`) is `≅` Gap A′ (correctly flagged) and
  shares the wall; route via the unified induction or reachability reuse.
- The `(D′) |det U★|=1 via minimality` half must be stated on the VISIBLE reduced subsystem `U★`
  (Reduction Lemma peels invisible matched pairs) — NOT raw `U` (minor-gcd can be even; certified
  negative). Do not re-attempt small-p as a stand-alone lever (refuted) or the odd-cancellation branch
  (POS-CHAR closed it).

## 4. concentration-exclusion-rigidity — ADVANCE (Elo 1491) — APPROVE technique, NOT in build set

Sound (Concentration Exclusion Thm + Reduction Lemma certified). But its own file states its round-8
value is "primarily to SUPPLY the generalized peel engine" — a supporting sub-component, not a
finisher. Its C1 (generalize Reduction Lemma to an arbitrary even block/leaf) is exactly Fill A of the
unified slug, and its C2 is the shared benign-U wall. To keep the build set focused (problem is one
gap from solved) I leave it unbuilt this round; if the unified induction lands it becomes a certified
sub-component of it. Kept live in the population (not cut).

---

## Diversity / field note (for the orchestrator)

The plateau flagged in prior rounds (routes 2/3/4 all bottom out on "minimality ⇒ no surviving deg≥3
cycle-piece") is now partially broken by the NEW `unified-residual-budget-induction` framing (induction
on N via BF-invisible-block removal, never touching the determinant). BUT watch the emerging *new*
convergence: unified's G2, self-similar's Gap-B step, and dual's case (b) are ALL becoming the same
"complement-legitimacy" wall. They remain differentiated by distinct certifiable side-content (dual's
case (a) is clean and needs no G2; self-similar's Gap A′ uses primal CC+ cycle structure; unified is
the pure induction). If next round they collapse fully onto G2, seed a genuinely different framing
(the det-minimality explorer's untried opening 3 asymmetric partial-circulation, or opening 4 rank-
contiguity pigeonhole) rather than a fourth variation of the complement induction.

## Ranking (updated, best-first)

self-similar-recursion 1725 > alternating-sum 1603 > dual-integer-certificate 1573 >
unified-residual-budget-induction 1524 (new) > concentration-exclusion-rigidity 1491 >
cut-budget-jacobsthal 1464 > block-recursion-tievertex 1427 > game-value 1404 > majorization 1289.
All stale flags (self-similar, dual, concentration) cleared.

build set: unified-residual-budget-induction, dual-integer-certificate, self-similar-recursion
