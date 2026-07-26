# Outline review — imo-2026-03, round 3

Reviewer verdicts on the 5 approaches on the table (2 advances, 1 new, 1 copy, 1 retired). Pre-flight computations run (sympy/Fraction): greedy R-pile on (.6,.2,.1,.1) → oddsum 1/2 < 8/15 after 2 marks, pairs at consecutive ranks, A=0 (confirmed); greedy on dyadic (8,4,2,1)/15 → oddsum 3/5 > 8/15 after one mark (overshoots, regime-N tool only — confirmed); CK (odd-count ⟹ A ≥ smallest) one-line proof sound; unified-Ψ make-or-break M−total(R)=2M−1 = 1/15 = α(3) on dyadic but = 1/5 ≠ 1/15 on non-dyadic (.6,.2,.1,.1) — **fatal for the unified single-boundary-charge claim**.

---

## pairing-partner — APPROVE (CHANGES REQUESTED)

Advance. Engine C (global weight-function / charging inequality) for the k≥2 sub-case of Lemma L (gap G1).

- Whole attempt? Yes — targets c(n)=f(n) end to end (lower bound via weight-function + imported k≤1 + pair-pile upper bound; regime-N upper bound delegated as a tracked gap to the sibling).
- Right technique? The amortized-charging pattern (crux aimo-0019) + rank-cap weighted-sum (aimo-0146) is a legitimate corpus-backed technique for "maintain a linear lower bound on a sorted alternating sum." Genuinely different from per-mark induction (it works globally, no exchange, no k-classification).
- Skeleton sound? Steps 1–5 and 7–9 are imported/certified machinery (Lemma G, M⊎R decomposition, k=0/k=1 proved, pair-pile). Step 6 (find w) is the new content. Logic chains: A ≥ Σw (W1) ∧ Σw ≥ α(n) (W2) ⟹ A ≥ α(n). Valid.
- Load-bearing lemmas WITH mechanism? CK (odd-count → A ≥ smallest) has a one-line proof (verified, sound). (W1) matching inequality: mechanism is "w chosen so Σw bounded above by the alternating sum on any sorted multiset" — valid framing (the alternating-sign rank weights already give equality; the engine seeks a coarser w depending on size). (W2) conservation: mechanism is amortized charging of each dyadic-level piece against the geometric sum — crux aimo-0019 pattern, plausible. Named with mechanisms. OK.
- Single-gap trap? Engine C's even-count sub-case is the genuinely-new territory (weight function on pair-pile-type extremals). The odd-count sub-case shares the ΔA −2T wall with Engine A (the transfer twin), but the even-count sub-case is Engine C's distinctive ownership. Not a near-twin of the transfer — different mechanism (global inequality vs extremal swap), different failure mode (no hybrid w exists vs two tails don't cancel).
- Avoids recorded dead ends? Yes — no multi-aux L* (FALSE), no WLOG-k=1 (literal monotonicity FALSE), no per-mark monovariant.
- Fixable gaps to close while building:
  1. **Find the hybrid w** (size + local-rank). The outline itself flags: a pure-size w cannot detect the pair-pile's canceling-equal-pairs parity-of-multiplicity, so w likely needs local-rank info. The builder must either construct such a w or show the even-count pair-pile extremal admits Σw = α(n) with equality (the cleanest target).
  2. **Conjecture (S)** "splitting a piece ≤ α(n) never helps Xiang" shares the ΔA −2T hard step with Engine A — if (S) is unprovable, the odd-count sub-case stalls. The builder should treat the EVEN-count sub-case as the primary new contribution (Engine C's distinctive value) and not over-invest in (S).
- Watch out: if no hybrid w exists, this route dies. Honest bet.

## two-regime-disjunctive — APPROVE (CHANGES REQUESTED)

Advance. Engine R-pile (greedy recursive pile-matching of the two largest) for regime-N (gap G2).

- Whole attempt? Yes — targets c(n)=f(n) end to end (upper bound via regime-D pair-pile + regime-N greedy; lower bound delegated to pairing-partner).
- Right technique? Recursive one-move-then-recurse (crux aimo-0369) + greedy pile-match is a legitimate technique; the greedy controls the global sort at each step (always the two current largest), unlike the killed global Hall matching.
- Skeleton sound? Steps 1–4 (regime D imported) chain. Step 4 regime-N: admissibility a_1≥2a_2 ⟹ residual a_1−a_2 ≥ a_2, pair (a_2,a_2) lands below residual, cancels. Valid per-step logic.
- Load-bearing lemma WITH mechanism? "Consecutive-rank invariant": mechanism is "equal pieces cluster in the sorted order + admissibility keeps the residual above the pair, so the pair is a block below the residual." This is a valid mechanism for ONE step (verified on (.6,.2,.1,.1): A=0 after 2 marks, pairs at consecutive ranks). The open step is the INDUCTIVE proof across multiple pile-matches (residual from step 1 may interleave with pair from step 2). Named with mechanism. OK.
- Complete case coverage? Dominant non-dyadic (a_1≥2a_2 — greedy runs); balanced non-dyadic (a_1<2a_2 — bisect/sliver fallback); near-dyadic (must detect dyadic-ness and route to pair-pile, since greedy overshoots on the exact dyadic). Cases identified and disjoint. The balanced fallback for n≥3 is the weak point (n=2 four-strategy template doesn't lift).
- Avoids recorded dead ends? Yes — no A≤0 pairing (FALSE), no (2^n−1)-way flat casework, no per-mark induction.
- Fixable gaps to close while building:
  1. **Prove the consecutive-rank invariant inductively** across multiple pile-matches. This is the SAME interleaving wall that killed Hall (round 1) — the greedy must control it LOCALLY at each step. The builder must show the residual from step i does not interleave between the pair created at step i+1. This is the load-bearing hard step.
  2. **Balanced-case fallback for n≥3** (a_1<2a_2): generalize U(1) sliver + U(2) Strategies B/C/E via the recursion (not flat casework).
  3. **Residual tail ≤ 1/2 bound** for non-dyadic P after the greedy terminates (giving A < α(n) strictly).
  4. **Dyadic detection** — the greedy overshoots on the exact dyadic (verified: 3/5 > 8/15 after one mark); the dyadic MUST be detected and routed to the pair-pile. The detection condition is the certified dyadic-vs-non-dyadic boundary.
- Watch out: if the consecutive-rank invariant fails inductively, this route dies (the fallback to majorization is KILLED — pair-pile doesn't majorize all refinements). Engine R-pile is the live engine.

## unified-mersenne-charging — RETHINK

New. Single amortized potential Ψ=1/A subsuming both bounds via charging the per-round +1 to the boundary M−total(R)=α(n+1) (crux aimo-0019). REJECTED — do NOT register.

Reasons (three independent fatal flaws):

1. **Circular on the lower bound.** The outline's step 4 (lower bound) explicitly concedes: "This is Lemma L rephrased in Ψ-space." The claim "prove NO Xiang response can avoid producing the +1 boundary term" IS Lemma L (the open gap G1). The "new mechanism" (charging) does not actually provide a technique for Lemma L — it restates it. The +1 being a single boundary quantity is the OPEN GAP, not a realized mechanism.

2. **Fatally flawed on the upper bound half.** Step 5 (upper bound) only handles the dyadic via the certified pair-pile (regime D, already done). It does NOT touch regime-N (gap G2) — for non-dyadic configs the +1 boundary charge has no target. The outline's "Cases to cover" lists "non-dyadic Liu config" and "balanced configs" as needing the +1 to telescope, with no mechanism.

3. **The make-or-break is FALSE for arbitrary partitions (verified).** The load-bearing claim is that the +1 is a SINGLE boundary quantity M−total(R). I tested the outline's own candidate (option (a): M = largest piece, R = rest, so M−total(R) = 2M−1): on the dyadic level-3, 2M−1 = 1/15 = α(3) ✓; on the non-dyadic (.6,.2,.1,.1), 2M−1 = 1/5 ≠ 1/15 = α(3). So the +1 is NOT a single boundary quantity for arbitrary partitions. The outline's option (b) (multi-boundary contributions telescope) is the SAME unverified hope that retired induct-one-mark ("no potential accounting for the +1 is identified"). This is a recorded dead end re-dressed.

- Load-bearing lemmas WITHOUT mechanism: "Charge invariance under both players' moves" is ASSERTED ("the boundary quantity is invariant under who controls the split") — no mechanism, just a conjecture. The "+1 boundary charge" lemma's "mechanism" is the algebraic identity 2D(n)+1=D(n+1) — that's the IDENTITY verification (already known), not a technique producing the +1 from structure. Violates the rigor rule "a lemma named without its mechanism is an unverified hand-off."
- Single-gap trap: this approach is a near-twin of the RETIRED induct-one-mark (both "Mersenne identity + hope the +1 has a potential accounting"). The outliner's defense ("the new content is the charging argument via aimo-0019") does not hold up — the charging argument is not realized in the outline; it IS the open gap. Pursuing it spends a builder slot on a line that either re-proves Lemma L+U (the field's job, not a shortcut) or dies the same death as induct-one-mark.

Direction for the outliner: if a unified framing is desired, it must identify a CONCRETE charging target that is provably a single quantity for arbitrary partitions (not M−total(R), which is dyadic-only), or abandon the unified route and keep the L+U split. The M=largest-piece candidate is already falsified.

## pairing-partner-transfer — APPROVE the copy (CHANGES REQUESTED)

Copy of pairing-partner (Engine A: extremal minimizer + non-improving 2-piece transfer for the same gap G1). Copy approved — genuinely different mechanism from Engine C.

- Whole attempt? Yes — identical end-to-end target as pairing-partner; the ONLY difference is step 6 (Engine A vs Engine C). Steps 1–5, 7–9 identical (same imports).
- Right technique? Non-improving transfer on the extremal minimizer (crux aimo-0119) is a legitimate variational technique — pick the A-minimizing Xiang refinement (tie-broken by fewest marks in M, then lex-smallest sorted vector), show any 2-piece transfer (merge two smallest M-sub-pieces + bisect largest unsplit R-piece) is non-improving (A(C') ≤ A(C*)), iterate to k=1.
- Load-bearing lemma WITH mechanism? "Two-tail cancellation": mechanism is "the ΔA for the 2-piece simultaneous move involves two tail terms T_M, T_R; the conjecture is T_M + T_R ≤ 0 because the merge raises a piece's rank while the bisect lowers one, and the tail re-indexings are opposite." This is a PLAUSIBLE mechanism (the two operations are at the same sorted-rank boundary, tails opposite) — named, with a stated reason. Not yet verified, but the mechanism is identified (unlike unified-mersenne's asserted invariance). OK as a load-bearing conjecture.
- Single-gap trap test (the dispatch's specific concern)? Engine A and Engine C target the SAME gap (G1 k≥2) but via DIFFERENT mechanisms (extremal swap vs global inequality) with DIFFERENT failure modes (two tails don't cancel vs no hybrid w exists). The outline honestly notes the odd-count sub-case of Engine C shares the ΔA −2T wall with Engine A — but Engine C's even-count sub-case is its distinctive ownership. They are NOT three variations of one framing: Engine A is a variational swap, Engine C is a global inequality, unified-Ψ (cut) was a potential rephrasing. Approving the copy.
- Avoids recorded dead ends? Engine A only needs the WEAK form A(C') ≤ A(C*) (non-increasing, not strict) — the tie-break (b) handles equality — so it sidesteps the "literal monotonicity FALSE" objection (n=3: k=2,3 extremals more numerous than k=1). No multi-aux L*, no per-mark monovariant.
- Fixable gaps to close while building:
  1. **Verify the two-tail cancellation T_M + T_R ≤ 0** — the SINGLE load-bearing unproved step. The builder should first test it computationally on n=3 brute force (enumerate k≥2 minimizers of the dyadic, apply the transfer, check A' ≤ A) before attempting a proof. If the tails do NOT cancel, Engine A dies the SAME −2T death as per-mark — record honestly and fall back.
  2. The transfer is one canonical move (merge two smallest M-sub-pieces + bisect largest unsplit R-piece); the tie-break (b) handles equality. Iterate to k=1, where the proved sub-case closes.
- Watch out: HIGH risk, highest reward (the outliner's own assessment). If the two tails cancel, G1 closes; if not, dies the per-mark death. Worth running in parallel with Engine C as a fallback.

## induct-one-mark — RETIRED (rank low)

Value-recursion route conceded dead (round 2). k=0/k=1 sub-cases subsumed by pairing-partner. Included in ranking as a loss to anchor the live approaches; ranked at the bottom.

---

## Field diversity assessment

After cutting unified-mersenne-charging, the live field is:
- pairing-partner (Engine C, global weight-function) — G1 lower bound, MED risk.
- pairing-partner-transfer (Engine A, extremal transfer) — G1 lower bound, HIGH risk, different mechanism.
- two-regime-disjunctive (Engine R-pile, greedy recursive) — G2 upper bound, MED risk.
- induct-one-mark (retired) — anchor.

The two G1 approaches (Engine C, Engine A) share the ΔA −2T wall on the odd-count sub-case but have distinctive separate territories (Engine C: even-count weight function; Engine A: 2-piece transfer cancellation). They are not single-gap twins. The G2 approach is on a completely different bound. The field is adequately diverse; the headline risk is that BOTH G1 engines hit the ΔA −2T wall (the interleaving obstruction) — if that happens next round, the outliner should field an approach attacking G1 from a framing far from both the weight-function and the extremal-swap (e.g., a structural/topological argument on the sorted multiset, or a probabilistic/averaging bound). For this round, the three live approaches are the right build set.

---

## Ranking table (after update_ranking, K=32 Elo)

| slug | Elo | last_outcome | note |
|---|---|---|---|
| pairing-partner | 1544.17 | advanced | leader; most certified machinery (L*, mirror, k=0/k=1); Engine C weight-function for G1 |
| pairing-partner-transfer | 1515.77 | (new copy) | inherits source Elo; Engine A extremal transfer for G1; HIGH risk |
| two-regime-disjunctive | 1506.00 | advanced | G2 closest; Engine R-pile greedy; consecutive-rank invariant is the hard step |
| induct-one-mark | 1451.46 | partial (dead) | retired; value-recursion conceded rephrasing of L+U; anchor |

Comparisons applied (anchored to last outcomes): pairing-partner > induct-one-mark; two-regime > induct-one-mark; pairing-partner-transfer > induct-one-mark; pairing-partner > two-regime (more proven machinery); pairing-partner = pairing-partner-transfer (draw — twins, equal claim on G1); two-regime > pairing-partner-transfer (advanced vs fresh copy). All stale flags cleared.

---

## Build set

Three builders in parallel, one per slug:
- **pairing-partner** — close step 6 (find hybrid w; own the even-count sub-case; treat (S) as secondary).
- **two-regime-disjunctive** — prove the consecutive-rank invariant inductively; handle balanced fallback n≥3; residual tail ≤1/2; dyadic detection.
- **pairing-partner-transfer** — computationally test two-tail cancellation T_M+T_R≤0 on n=3 brute force FIRST, then prove or die honestly.

unified-mersenne-charging NOT built (RETHINK — circular + falsified make-or-break). induct-one-mark NOT re-dispatched (retired).

build set: pairing-partner, two-regime-disjunctive, pairing-partner-transfer
