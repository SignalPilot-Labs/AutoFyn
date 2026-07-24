# Outline review — round 13, imo-2026-03

Reviewed: `/tmp/round-13/proof-outliner.md` against
`results/imo-2026-03/approaches/greedy-halving-adversary.md`,
`results/imo-2026-03/approaches/lp-duality-certificate.md`, and
`results/imo-2026-03/current.md`.

## greedy-halving-adversary (revise) — APPROVE

Target: close two named open items in restricted Claim (B)'s Theorem P(n) —
(†)'s p2-cut complement, and ℓ(F)=2's mixed-regime sub-case (c) for P≠∅.
Technique: transplant the certified `exchange-smoothing-vertex-maximization`
+ `per-piece-vertex-decomposition-theorem` machinery (built for Claim (A)'s
Case-I closure, an upper-bound-producing tool) onto the new maximization
targets, via a new **p2-Pinned-Dominance Lemma**.

Checks performed:
- **Not a repeat of a dead end.** Confirmed the file's own Open Gaps §4
  correctly states P≠∅ needs a genuinely new *upper*-bound mechanism, distinct
  from all the *lower*-bound machinery (Propositions 20–24) that has
  accumulated so far — this outline is consistent with that diagnosis, not a
  re-hash of a lower-bound tool mislabeled as an upper-bound fix.
- **Mechanism check.** `exchange-smoothing-vertex-maximization` was already
  established (round 10/11) as a marking-agnostic vertex-characterization
  tool (not tied to Claim (A)'s specific reference-set shape) — so reusing
  its *reduction* machinery on a different maximization target (max_{G'} A(G'))
  is legitimate, and the outline correctly flags that only the reduction half
  transfers "for free"; the evaluation half (p2-Pinned-Dominance Lemma itself)
  is new, unproved, and explicitly not claimed as already-established.
- **Independent numeric spot-check of the new lemma.** I wrote and ran a
  fresh exact-`Fraction` script (not reusing any builder script) testing the
  p2-Pinned-Dominance claim at n=5: searched 20,000 random legal refinements
  of τ={p2,...,p6} under budget n-2=3, both unrestricted and forced-p2-cut.
  Result: the unrestricted maximum (5/21, matching the target p2−f(5) exactly)
  is achieved only by a p2-uncut configuration; the best forced-p2-cut value
  found (53/225 ≈ 0.2356) is strictly below the p2-uncut maximum (5/21 ≈
  0.2381). This supports the lemma's claim (p2-uncut vertices weakly dominate
  p2-cut ones) — plausible, not yet a proof, exactly as the outline frames it.
- **No overclaim.** The outline explicitly states "do not claim general-n
  unconditional closure even if step 1 succeeds" (still bottoms out at Prop
  22's own (⋆_{n-2}) conditioning) and separately flags the harder step-3
  instance (ℓ(F)=2, shifted reference t*) as possibly breaking the pinning
  argument — an honest, not hidden, risk.
- **Legality caveat is correctly flagged**, not glossed: "Watch out for" notes
  that the freed-budget redistribution from undoing p2's cut must be checked
  for legality (piece-budget/positivity constraints), not assumed by analogy
  — this is exactly the class of bug (illegal-refinement generation) that has
  bitten this project's own verification scripts twice before (round 10).

No fatal flaw found. Minor suggestion for the builder: when step 3's t*
version is attempted, explicitly test small n (n=4,5) numerically for the
shifted-reference pinning claim before investing in a full proof, the same
way I did for step 1 above — cheap and would catch a false generalization
early exactly like round-4's outline-reviewer catch pattern.

## lp-duality-certificate (revise) — APPROVE

Target: general upper bound c(n) ≤ a_n·T, redirected away from a literal LP
dual-certificate framing (correctly diagnosed by this round's explorer as a
relabeling of already-certified machinery) toward a simultaneous P(m)
induction closing p1<T/2 via a new **Peel-Target Existence Lemma**.

Checks performed:
- **Redirect is justified.** The outline's own diagnosis — that a literal
  per-cell LP dual certificate adds no leverage beyond the existing
  exchange-smoothing/vertex machinery, and the real obstruction is the
  file's own Open Gap 1 (exponentially many sign-pattern cells) — matches
  what's actually recorded in the approach file's Open Gaps §0–1. Not a
  fabricated pivot.
- **Generalized Theorem B_k Corollary reuse verified by direct read.** I
  read Theorem B_k's actual statement/proof (lines 511–525 of the approach
  file): it is *already* proved for arbitrary k∈{2,...,m}, and the proof
  text states explicitly "nothing in the original proof used k=2
  specifically." The Corollary's algebra (lines 363–384) depends only on
  S'_k's size (m−1) and total (T−2p_k), which is identical for every k — so
  the outline's claim "re-index only, no new proof needed" is a genuine,
  verified reuse, not a leap.
- **Independent re-derivation of the pigeonhole test.** I computed, with a
  fresh script, whether the on-file hard witness (2/5,3/10,1/5,1/10) at n=3
  actually lands in case (a) (some p_k ≥ a_nT/2) as the outline's sanity
  check requires: a_3T/2 = 4/15 ≈ 0.267, and p2 = 3/10 ≈ 0.3 already clears
  it — so the witness lands in case (a) via k=2 itself. I further verified,
  via Theorem B's own certified Corollary chain (using the already-fully-
  closed n=2 base case as IH), that Φ_min ≤ p2 + Φ_min(S') ≤ 37/70 ≈ 0.529 <
  a_3T ≈ 0.533, i.e. the corollary genuinely closes this witness. (This is
  slightly stronger than the historical round-9 record, which credited
  Theorem B_k with k=4 for this witness — not a contradiction since both
  routes reach the same optimal value 1/2, but worth flagging: the outline's
  own sanity check "both witnesses land in case (a)" is satisfied, and by an
  even more direct route than the outline itself anticipated. No corrective
  action needed for the outline as written.)
- **Elementary pigeonhole arithmetic double-checked.** The outline's claim
  that "if every p_i < a_nT/2 then T < m·a_nT/2, forcing a bound on m·a_n" is
  correct algebra. I confirmed the outline's honest framing is right: since
  a_n → 1/2 and m = n+1, m·a_n → ∞, so this bound is *not* generally
  vacuous for large n — case (b) is a real region needing the harder
  continuity argument, exactly as the outline says (it does not overclaim
  that the pigeonhole check alone closes the whole gap).
- **No repeat of round-10's refuted "always match top two" claim** — the
  outline explicitly disclaims this in its Watch-out-for section.

No fatal flaw found. The redirect is a genuine mechanism change (simultaneous
induction + peel-target dichotomy), not a bypass of the same wall one step
later — it targets the p1<T/2 regime's actual structure rather than another
crude closed-form template (Theorem D was already shown too weak, and the
outline does not resurrect it as the primary tool).

## Diversity note

Front 1 (greedy-halving-adversary, lower bound / Claim B) and Front 2
(lp-duality-certificate, upper bound) remain genuinely independent targets,
as established over many prior rounds — this is not a shared-gap plateau.
Both this round's revisions now reuse the *same* underlying certified tool
family (exchange-smoothing vertex characterization / per-piece decomposition)
in different directions (max vs a related peel/dichotomy argument) — this is
expected convergence of proven machinery, not evidence the two fronts have
collapsed into one line; they still attack disjoint halves of the theorem.

## build set: greedy-halving-adversary, lp-duality-certificate
