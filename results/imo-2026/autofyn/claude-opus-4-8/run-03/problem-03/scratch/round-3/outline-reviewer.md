# Outline Review — imo-2026-03, Round 3

Field handed up: 4 approaches (2 advances, 2 new). Free numerical inputs re-verified this
round: peel-max identity S(B)=b_(1)−S(B∖{b_(1)}) (0/20000 bad) and min-odd-sum floor
S_odd≥sum/2 (0/20000 bad) both hold exactly — the part-count-fix base case and the
global-max induction rest on solid ground.

## induction-peel — APPROVE (advance, leader; keep slug)
Both open gaps carry a real mechanism, not a bare label.
- **A2 (lower Case 2):** band decomposition B=Q⊔C is sound — every part of C ≤ 2^{n-1} so
  N_C is even above the mid-band and the overlap W is confined to t≤2^{n-1}; at most one part
  of Q exceeds 2^{n-1} (two would sum > 2^n), giving the uncancellable high-band term
  h=max(q_1−2^{n-1},0). The residual h+|S_low(Q)−S(C)|≥1 is honestly flagged open and is
  closed by induction on the cut budget c (budget cap on W), NOT by the |S(Q)−S(C)| bound
  already proven too weak. Mechanism is stated and consistent.
- **B (upper bound):** part-count fix is correct — dropping "≤k+1 parts" is validated by the
  min-odd floor (base V_0=S_odd≤sum holds at any part count, 0/20000). The r=a_1/ρ two-branch
  step (BISECT if r≥1, MATCH if r<1) with the "twin cancels equal at adjacent rank" mechanism
  is the right shape; the two branch inequalities + equalization pinning ratio 2 are the
  isolated remaining obligation.
Issue to watch (carry into build): the round-2 "twin AND original both survive" pitfall — do
not delete the matched original in MATCH.

## alternating-sum-potential — APPROVE (advance; keep slug)
Genuinely different mechanism from induction-peel (analytic band accounting + amortized
charging witness, not a DP) — this is the diversity anchor on the upper crux.
- **G1:** band-confined W via L4/L3, bounding W by the (n−j)-cut budget on R′ (each cut adds
  ≤1 odd interval) rather than the trivial min(S(Q),S(R′)). Concrete and near-term-closable.
- **G2:** the shared crux. The outliner is honest that the charging route "may also need
  lookahead"; the aimo-0012 amortized bookkeeping (credit 1/D_n per cut, β≥sum·(2^n−1)/D_n) is
  a legitimately different accounting from the DP. Acceptable with the stated fallback
  (import induction-peel's DP as a black box for the branch choice if pure charging stalls).
Single-gap-trap note: both live approaches use L4 min-pairing as the upper-bound witness, but
their construction mechanisms (DP vs charging) diverge, so they do not share one wall on B/G2.
Keep them differentiated in build.

## global-max-peel — APPROVE, REGISTERED (new, far-from-field lower bound)
Registered at cold-start 1500. Generalized IH G(n) — every ≤n-cut refinement of {2^0,…,2^n}
has S(B)≥1 — verified numerically (min S = 1.0000 over 200k random refinements, n=1..4;
target attained, never violated). The peel-CURRENT-global-max framing (induction on part
count via the verified peel-max identity) is a genuinely different induction variable from
the fixed-top peel and plausibly collapses Case 1 and Case 2 into one argument. Concrete,
numerically backed far bet.
Issue (carry into build, per outliner's own caveat): the generalized IH must range over
refinements of ARBITRARY superincreasing multisets, else the peeled residual escapes the
hypothesis; and if the induction is forced back into a case split on m's origin it has bought
nothing over induction-peel — report that honestly if so. Lower bound only this round.

## huffman-merge-exchange — RETHINK, NOT REGISTERED
The make-or-break translation step (step 1: cut↔merge correspondence with objective match
under L4) is not merely unverified — its one offered mechanism is numerically FALSE. L4's
consecutive-pairing cost reproduces S exactly (0/5000), but that is a fixed pairing of the
final sorted multiset. The recursive "combine two smallest, charge |diff|, replace by sum"
merge objective the approach needs mismatches S in 4170/5000 random cases. The outliner's
stated bridge — "combining sorted-adjacent masses is exactly a bottom-up merge order that
realizes L4's cost" — is precisely this refuted claim: the Σ|diff| functional does NOT
decompose over a merge order. Steps 2–4 are all gated on step 1, which collapses. Per the
gate rule (a lemma whose mechanism does not yield the claim is pushed back) and CLAUDE.md
(a cut approach is never registered), this stays out of the pool. If the outliner wants a
far upper-bound framing next round, it must supply an objective that provably decomposes —
the merge-cost bridge as stated cannot.

## Ranking (post-update, best-first)
- induction-peel 1617 (leader; advanced, Case 1 rigorous)
- alternating-sum-potential 1542 (advanced; diverse upper-crux mechanism)
- global-max-peel 1500 (new, numerically-backed lower-bound far bet)
- explicit-certificate 1438 (unbuilt stub; provably-false "concentrate don't spread" upper mechanism)
- smoothing-extremal 1403 (dead-end, Lemma G refuted)

## Field-diversity note for the orchestrator
The upper-bound crux (Sub-claim B / G2) remains the shared wall; the two live approaches now
attack it with genuinely different mechanisms (value-function DP vs amortized charging
witness), which is the right kind of diversity — do not collapse them. global-max-peel adds a
third framing but only on the LOWER bound. After this round the field still lacks a *rigorous,
non-DP* upper-bound construction; the huffman merge bet was the attempt and it failed the
plausibility gate. If B/G2 does not close next round, task the outliner for a fresh
upper-bound framing that is NOT another min-pairing-witness variant.

build set: induction-peel, alternating-sum-potential, global-max-peel
