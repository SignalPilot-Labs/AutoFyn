## imo-2026-03

potential-weighting-upper-bound: advance
Target: Determine c(n) = 2^n/(2^{n+1}-1) for the Liu Bang/Xiang Yu stick game — this file carries the
UPPER-BOUND direction (the lower bound against the dyadic construction is already fully unconditional,
`lemmas/all-cycles-resolution.md` + `lemmas/superincreasing-no-early-zero.md`, round 8). The remaining
work is Sharp Argmin Recovery (SAR) at background scope |B|<=1, reduced (round 12) to proving Claim A
via the Non-Matching-Witness Criterion on the non-dominated prefix, itself split into named Gaps
1a/1b/1c (§17-§24 of the approach file). This round appends §25, reconciling three explorer findings.

Technique: strong induction on q=|Z_0| within the scope family F (§17.5), using the certified
Generalized Multi-Background Peeling Lemma's DELETE/KEEP/MATCH trichotomy plus the General
Rank-Extraction Identity to handle insertion position — unchanged spine, this round supplies three new
buildable sub-results within it.

Skeleton (round 16 additions, §25 of the approach file):
  1. Gap 1b base case (rest=∅, q=3): PROVED this round (not just corroborated) — a ~10-line
     contradiction argument combining two already-free bounds on A_1 (A_1<=b_0 via Shrink-List
     Corollary; A_1<=w_1-b_0 via the "keep w_1" candidate) with the certified exact q=3 DELETE/KEEP
     dichotomy — by direct algebra + independent re-derivation.
  2. Gap 1c half-step lemma: reduce to Step-3's "extremal witness + nearest-neighbor local rewrite"
     construction (drop the witness element closest to d) — by the General Rank-Extraction Identity's
     insertion-difference form, applied twice (once ruling out the naive "same witness" transfer, once
     as the recommended route for Step 3 itself).
  3. Gap 1a Two-Touch Lemma (A_1's exact closed form at |C|=1): reduce to induction on |W|, base case
     |W|=2 already IS the certified Three-Bound Domination Lemma — by repeated triple-collapse
     (any selection touching >=3 elements is dominated by a <=2-touch alternative).

Key lemmas (claim + mechanism):
  - Sum-Bound Base Case Lemma (NEW, proved this round): at genuine trigger+h=0, q=3, M=D_{k*} exactly
    — because assuming the negation (2D_{k*}>w_1) forces, via the two free A_1 bounds and the trigger,
    both w_1<D_{k*}+b_0 and D_{k*}>b_0 simultaneously, which combine (using D_{k*}=d_{k*}-b_0, forced by
    D_{k*}>b_0) to w_1<d_{k*}, directly contradicting h=0's own requirement d_{k*}<w_1.
  - Single-Background Two-Touch Lemma (conjectural, NOT proved): OPT_{+1}({b0},W) is always achieved by
    a selection touching <=2 elements of W — because (conjectured mechanism, not yet shown) any 3+-touch
    selection is dominated by a 2-touch alternative via repeated Three-Bound-Domination-style collapses.
  - Half-step Step-3 construction (conjectural, NOT proved): dropping the LHS-optimal witness's element
    nearest to the newly-matched value d gives a valid X-selection already beating the RHS optimum —
    because (conjectured mechanism) the insertion-difference identity's sign-flip term becomes favorable
    exactly when the dropped element minimizes |x-d| over the witness.
  - Insertion-Difference Identity (NEW, proved, general, no F-provenance needed): e(M∪{d})-e(M) =
    (-1)^h*(d-2e(tail_d)), h=#{m in M: m>d} — because inserting d into the sorted descending sequence
    shifts every element ranked above d down one parity slot, flipping the sign of everything below the
    insertion point and adding d itself at the new slot's sign.

Open gaps: Gap 1a's Two-Touch Lemma (open, induction skeleton given); Gap 1c's half-step Step-3
construction (open, algebraic route given via the now-proved Insertion-Difference Identity); Gap 1b's
general recursion-depth induction beyond the now-closed rest=∅ base case (open, large, lower priority
this round); the σ=-1 mirrors of both the Sum Bound and the half-step (queued, not started).

Cases to cover: Gap 1a's Two-Touch induction must show, at every |W|, that any selection touching k>=3
elements is dominated (not merely that SOME 2-touch alternative exists — the base case |W|=2 is
literally the certified Three-Bound Domination Lemma read as an inequality). Gap 1c's half-step must
stay strictly within "genuine top-level F-provenance" scope (round 15's confirmed simplification: only
the base generator's own trigger+global-k* needs to be genuine, not every deeper match partner).

Watch out for: (i) Gap 1b's base-case proof closes ONLY rest=∅ (q=3) — do not report "Sum Bound proved"
without this qualification, the general |rest| induction is untouched; (ii) even a full proof of
Two-Touch does NOT by itself close Gap 1a's general-q Per-Partner Domination induction — A_{3,l}'s own
recursive DELETE/KEEP/MATCH peeling still needs its own per-q case analysis (as the certified q=3 proof
already does), Two-Touch only removes A_1's opacity as an input; (iii) do NOT port Two-Touch to |C|=2
(re-confirmed dead this round, independent check: 357/1500 = 23.8% failure, matches the explorer's 24%)
— the half-step lemma needs its own, structurally different argument; (iv) do NOT resurrect the
half-step's Step-2 "same witness, drop d" naive transfer (confirmed FALSE this round, concrete
counterexample via the Insertion-Difference Identity); (v) the half-step's Step-3 construction
(1,267 combined checks, 0 violations) was NOT independently re-verified by the outliner this round
(time budget prioritized Gap 1b's proof re-derivation and Gap 1a/1c's shared identity check) — flag
this explicitly for the builder as its own first task before spending build time on the algebra.

---

Benched, no change this round (no explorer targeted them, no new leverage found or expected):
dyadic-cascade-induction (lower bound already fully unconditional since round 8 — no open task),
concavity-minimax-duality (its machinery is tied to superincreasing-reachable states, gives zero
leverage on the arbitrary-opening upper-bound gap that remains open). Not nominated this round.
