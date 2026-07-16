# Outline Review — imo-2026-03, Round 6

Verified all load-bearing numerical claims on a 1/4-grid at n=3, using the CORRECT joint cut
budget (#Q-cuts + #R-cuts ≤ n). A crucial correction: an earlier pass that ignored the budget and
admitted 5-part Q at n=3 produced spurious "violations" of both LL and the INC bound — those Q need
t=4 cuts, over the n=3 budget, so they are not valid instances. With the budget enforced (|Q|≤n+1,
and R=G_2 forces |Q|≤4), all the genuine claims check out except one (the ll-dyadic-symdiff slack
claim — see below).

---

## ll-inclusion-gap — CHANGES REQUESTED (revise; build)

**Technique is right and the target is verified true.** The INC arithmetic bound
`A(Q) ≤ A(R) − 1` in the branch `S_Q ⊆ S_R` holds with **0 violations** over 574 valid n=3
instances (R = G_2 and all 1-cut refinements with A(R)≥1). This genuinely gives
`A(Q∪R)=A(R)−A(Q) ≥ 1` via the certified INC reduction. So the skeleton reaches the actual LL
claim, not a fragment.

**Does it bypass the FALSE Structural Lemma? Partly — the mechanism WORDING re-imports the false
claim and must be rewritten.** The false Structural Lemma part (a) was "S_Q⊆S_R ⟹ no Q-piece in a
forbidden-band interior (e.g. (1,2))". I confirmed by direct computation that the counterexample
Q={3/2,3/2,2,3}, R=G_2 **is** an inclusion config (S_Q=[2,3) ⊆ [0,1)∪[2,4)=S_R) with two parts in
(1,2) — so part (a) is indeed false. (NOTE: math-explorer-sub3b Key-finding-4 / line 62 is WRONG
when it says this config has S_Q⊄S_R; current.md and the certified lemma are right. Do not let the
builder trust that explorer remark.)

The outline's key-lemma mechanism (lines 30–31) as written — *"no Q-piece in an odd-N_G forbidden
interior, so bottom pieces ≤1"* — is the false claim reworded. It happens to be valid only for
ODD-count Q (e.g. 3-part: any piece in (1,2) makes N_Q=3 odd just below it, breaking inclusion),
which is exactly the clean Candidate-3 n=3 proof (q3 ≥ A(Q)/2 by Forcing + ΣQ=2^n, and q3 ≤ 1 by the
odd-count parity, giving A(Q) ≤ 2 = A(G_2)−1). For EVEN-count / even-multiplicity interior pieces
(the {3/2,3/2} pair) it is FALSE. Required change: state the INC branch as a **parity condition** —
on every even-N_G band, N_Q must be even, so interior pieces occur in parity-balanced groups — and
run the value arithmetic on that, NOT on "no piece in the band". The n=3 odd-count case is the
anchor; the substance (G-INC-1 general n, G-INC-2 refined R, even-multiplicity interior) stays open
and is honestly flagged.

**GAP branch:** alignment-cost ≥1 is open and honestly flagged; not circular. Fine to leave as a gap.

This is the cleanest, closest-to-closing lower-bound route — its distinctive INC inequality is
verified true. Build it.

## ll-dyadic-symdiff — CHANGES REQUESTED (advance; build, but fix a FALSE step)

**Identity is sound and non-circular.** `A(Q∪R)=2^{n−1}−A(Q'∪R)` (max(Q)=2^{n−1}, Q'=Q∖{2^{n−1}})
verified with 0 mismatches, and the reduced target `A(Q'∪R) ≤ 2^{n−1}−1` holds with 0 violations.
The outliner's circularity guard is respected: Q'∪R has sum 3·2^{n−1}−1 (not a valid G_{n−1}
refinement), and step 3→4 closes it via the INC/GAP arithmetic, NOT a naive induction on Q'∪R. No
circularity. Worth certifying the identity as a shared lemma.

**Step 2 is FALSE and cannot be built as written.** The outline claims: max(Q) < 2^{n−1} ⟹
`A(Q∪R) ≥ 2` ("strict slack, full-measure level contribution"). This is false even within Sub-3b:
- Q={15/4, 13/4, 1}, R=G_2 (a valid Sub-3b instance, max(Q)=15/4<4): **A(Q∪R)=3/2 < 2**.
- 29 Sub-3b configs with max(Q)<4 and A_union<2 were found; the min is 3/2.

The sub-3b explorer's "Key finding 3" (max(Q)<4 ⟹ A≥2, min=2) is a **coarse-grid artifact** — it
used a 1/2-grid that never samples 15/4. The "A≥2 slack / full-measure level" mechanism is dead. The
max(Q)<2^{n−1} branch must instead prove only `A(Q∪R) ≥ 1` (still true: min observed 3/2 > 1), by a
different argument — most naturally by folding it into the same INC/GAP arithmetic rather than a
level-measure slack. Because both the tight branch (step 3→4) and the fixed step-2 branch then defer
to the INC/GAP mechanism, this slug largely converges on ll-inclusion-gap's crux (as
math-explorer-sub3b Key-finding-1 also observes: Sub-3b = INC ∪ GAP). Its independent value is the
identity. Build to (a) certify the identity, (b) delete the false A≥2 slack claim.

## geometric-selfsimilar — CHANGES REQUESTED (advance; build)

Right technique for the upper bound (multilevel partial-shadow recursion for B2; dominant-chop for
C), the only upper-bound front, and B is fully closed at n=2. B2 numerics support val≤c(3) (all
denom-15 configs). Regime B2 general-n termination + the "final piece ≤ 1/D" formula, and Regime C
general n, are honestly flagged open. Regime C's dominant-chop mechanism is thin (pinned to one
witness, admits "genuinely open"); the explorer confirms shadow/binary-halving both fail for C, so C
needs a genuinely new chopping analysis — this is the real risk but it is the correct front and not a
recorded dead end. Focus the build on B2 general-n (the tractable half); leave C as a flagged gap.
No RETHINK — the recorded dead ends (single-level PS+B1 for k=2, binary-halving A_1 for C, shadow for
C, one-cut-at-A_2) are all avoided by the multilevel recursion.

## alternating-sum-value / extremal-smoothing — not nominated

Correctly left out. alternating-sum-value stalled at R3 (its LL gap is a subset of the LL routes
above; greedy-XY dead-end recorded). extremal-smoothing's S1 is stuck 3+ rounds with no mechanism.
Both remain live in the population at lower Elo.

---

## Ranking (updated this round, stale cleared)

1643.3 geometric-selfsimilar · 1545.0 ll-inclusion-gap · 1502.4 ll-dyadic-symdiff ·
1447.0 alternating-sum-value · 1362.4 extremal-smoothing.

Anchors: geometric-selfsimilar (leader, upper bound moving, B closed at n=2) beats the LL routes and
the stalled pair; ll-inclusion-gap > ll-dyadic-symdiff because its INC inequality is verified true and
coherent whereas ll-dyadic-symdiff carries a FALSE step-2 slack claim; both LL routes beat the
R3-stalled alternating-sum-value; extremal-smoothing last (S1 long-shot). No new slugs to register
(all three nominated slugs already in the population); no copy requested.

build set: ll-inclusion-gap, ll-dyadic-symdiff, geometric-selfsimilar
