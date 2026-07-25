## imo-2026-03

self-similar-induction-on-n: revise
Target: The full lower-bound (Liu Bang's guarantee) claim c(n) = 2^n/(2^{n+1}-1),
via General Theorem GT(m) (self-similar peeling induction reducing the
multiset-minimax lower bound to a chain of geometric-comparison-set
alternating-sum inequalities OddSum(D∪Gamma_{j})>=target).
Technique: Self-similar peeling induction on the recursion depth j, split
by residual excess e = m-k (even e, odd e=1, odd e>=3, e=0 sliver), using
the certified Half-Sum Corollary, the corrected e-fold q=0-chain closed
form, and (round 21) the General Cardinality-Constrained Half-Sum Lemma
(GCH(k)).
Skeleton (two independent gap-closure tracks — assign to two builders if
both are dispatched, since they touch disjoint objects: the odd-e>=3 track
only needs the already-certified affine margin formula and the Case-B
track needs the certified GCH lemma's proof body; a single builder can
also do both sequentially since the first is short):

  TRACK 1 — Odd-excess e>=3 Endpoint Closure Theorem (short, 3-step,
  cap-free, no case explosion):
  1. Restate the already-certified margin identity (round 17,
     `lemmas/even-target-companion-peeling-and-corrected-qzero-chain.md`
     + `lemmas/half-sum-corollary-and-large-sum-closure-theorem.md`):
     LB_odd - T_odd = 2^k/6 + 2^m/6 - a1/2 - 1/2, valid for the WHOLE
     range a1 in (2^{k-1}, 2^k] (not just the width-1 window) — by direct
     algebraic combination of the two certified lemmas, cite both by name.
  2. Observe the margin is affine (slope -1/2) in a1 over the whole range,
     hence its minimum over a1 in (2^{k-1},2^k] is attained at the right
     endpoint a1=2^k (the range is closed there) — elementary monotonicity,
     no new machinery.
  3. Evaluate at a1=2^k: margin(2^k) = 2^k(2^e-2)/6 - 1/2. For odd e>=3,
     2^e-2 >= 6 (monotone increasing in e), so margin(2^k) >= 2^k - 1/2 >=
     3/2 > 0 for every k>=1 — closes GT(m) sub-case (i) for ALL k>=1 and
     ALL odd e>=3 unconditionally (no cardinality cap needed, since the
     Half-Sum Corollary this identity rests on is itself cap-free).
  Key lemma (new, to certify): "Odd-Excess e>=3 Endpoint Closure Theorem" —
  because the margin formula is affine over the full range and its
  worst-case endpoint value is a simple positive closed form in k,e.
  Watch out for: this is EXACTLY the same class of bug round 18 found in
  Claim B for e=1 (evaluating only at the window sup, not the true range
  endpoint) — the builder must explicitly verify a1=2^k is attained (range
  closed, not open) and must not silently reuse round 17's window-sup-only
  computation. Must also double check e=1 is explicitly excluded from this
  theorem's scope (e=1 stays on the separate, harder GCH(k) route,
  already closed in round 21) — do not conflate.

  TRACK 2 — Case-B(m,k) sliver via cap-free GCH strengthening:
  1. Re-examine the certified proof of the General Cardinality-Constrained
     Half-Sum Lemma (`lemmas/general-cardinality-constrained-half-sum-lemma.md`)
     line by line and confirm (or refute) that the hypothesis max(R)<=
     2^{k-1} (the value cap) is never load-bearing in Steps A, B, C0, C1 —
     only Case C2's "topmost interval" sub-argument even mentions the cap,
     and there only to define the domain, not the minimum (OddSum/AltSum
     is still affine slope +1 on the extended interval (v1,infty), so the
     infimum is still attained at the same captured endpoint r->v1+).
     If confirmed, this proves the CAP-FREE GENERALIZATION: AltSum(R∪
     Gamma_{k-1})>=1 for every finite multiset R with |R|<=k+1 (no bound
     on individual values), sum(R) in [2^k,2^k+1), all k>=1 (the k=1
     boundary needs a short separate direct check since it's outside GCH's
     originally-stated k>=2 range — small, |R|<=2, tractable by hand;
     confirmed numerically clean by round 22's explorer, 20,000 exact-
     Fraction trials).
  2. Given the cap-free GCH, close Case-B(m,k)'s sliver (b1 in
     (2^{m-1}-1,2^{m-1})) via a single Global-max peel: by the certified
     Global-max Peeling identity (`lemmas/altsum-corollary-and-growth-
     lemma.md`), AltSum(B∪Gamma_{m-2}) = b1 - AltSum(B'∪Gamma_{m-2}),
     B'=B\{b1}. Check B' is a feasible (cap-free) GCH(m-1) instance:
     sum(B') = 2^m-b1 in (2^{m-1},2^{m-1}+1), |B'|<=m = (m-1)+1 — matches
     exactly, with k:=m-1. Apply the cap-free GCH lemma from step 1 to get
     AltSum(B'∪Gamma_{m-2})>=1, hence AltSum(B∪Gamma_{m-2}) <= b1-1 <
     2^{m-1}-1 strictly (since b1<2^{m-1} in the sliver) — closes the
     sliver with strict inequality throughout, not just at the boundary.
  Key lemmas (new, to certify):
  - "Cap-Free General Cardinality-Constrained Half-Sum Lemma" — because
    the certified proof's Case C2 affine-slope argument never actually
    uses the upper cap, only Steps A and C1 use the CARDINALITY cap
    |R|<=k+1 (which stays, unchanged).
  - "Case-B(m,k) Sliver Closure Theorem" (via peel + cap-free GCH) —
    because b1 is always the global max in the sliver (b1>2^{m-1}-1>
    2^{m-2}=max(Gamma_{m-2})), so peeling it off reduces exactly to a
    cap-free GCH(m-1) instance at the threshold S in [2^{m-1},2^{m-1}+1).
  Open gaps: the line-by-line re-verification that Steps A/(C0)/(C1) never
  use the value cap must actually be carried out (not just asserted from
  round 22's informal read) — this is the crux of the whole track and must
  be checked rigorously, not assumed; the small k=1/m=2 boundary case
  needs its own short direct argument (outside GCH's originally-stated
  k>=2 range).
  Cases to cover: k=1 (m=2) boundary handled separately from k>=2 (main
  cap-free GCH range).
  Watch out for: do NOT assume this closes sub-case (i)'s own e=0 form
  (the same object under a different name) — round 22's explorer checked
  this directly and found sub-case (i)'s e=0 residual needs sum(R) just
  BELOW 2^{k-1} (opposite side of the threshold from where GCH applies,
  which needs S just above 2^k), so it is NOT literally the same
  statement. This track closes Case-B(m,k) specifically; sub-case (i)'s
  own e=0 residual (if it is a genuinely separate object, not resolved by
  the round 4/11 Corollary equivalence) stays open and should be flagged,
  not silently assumed closed, by whichever builder works this track.

Cases to cover overall: GT(m) full case split is even e (already closed,
round 17), odd e=1 (closed, round 21, via GCH(k)), odd e>=3 (Track 1,
this round), e=0/Case-B(m,k) sliver (Track 2, this round). If both tracks
close, flag explicitly in the file whether sub-case (i)'s own e=0 form is
still open as a distinct residual (per Track 2's "watch out for") — do not
overclaim GT(m) fully closed unless that specific sub-question is also
resolved or shown vacuous.

---

global-lp-vertex-sufficiency: revise
Target: The full upper-bound (Xiang Yu's guarantee) claim: for every
partition p of the stick by Liu Bang's n cuts, Xiang Yu has a response
achieving OddSum(response) <= c(n) — the n=3 Existence Theorem specifically
(n=2 fully closed both directions, round 19-20).
Technique: Region decomposition of B(3) (Liu Bang's legal partition space)
by explicit closed-form constructions, each construction proved via an
exact order-condition + mass-identity substitution to give
OddSum(construction) - c(3) as a simple closed form on its region of
validity (as already done for Region I via Construction H).
Skeleton:
  1. Split Region II (=B(3) \ Region I, still open) into two sub-regions
     mirroring its own defining inequalities, per round 22's explorer
     finding that a single uniform Region-II construction does not exist
     (8 prior mechanisms + Q/R/W/BB all individually fail somewhere):
       Region IIa := Region II ∩ {p4 > gamma(3)} (near-uniform sub-case,
         all four pieces comparable, g1,g2 near the floor, g3 large)
       Region IIb := Region II ∩ {p4 <= gamma(3)} (equivalently, within
         Region II's other defining half {g3+p4<=3g1}: p1 near its own
         upper edge 1/2, g3 pinned at the floor gamma(3), g1≈g2 large)
     Verify IIa ∪ IIb = Region II exactly (i.e. these two conditions
     partition Region II given its own definition {p4>gamma(3)} ∪
     {g3+p4<=3g1}) — a short set-algebra check, do first, before any
     construction proof, since the two round-22 hard points found sit one
     in each half but this is only checked at 2 points not proved
     exhaustive.
  2. Formalize Construction Q (bisect p1, tie a p2-fragment to p3:
     p1->(p1/2,p1/2), p2->(g2,p3)) — or its interchangeable sibling R
     (tie to p4 instead) — as the closer for Region IIa. Derive the exact
     closed-form value identity OddSum(Q)-c(3) = <closed form>(p4,gamma(3),...)
     via the same order-condition + mass-identity substitution method that
     produced Construction H's identity (p4-gamma(3))/2. Prove the order
     conditions needed for Q's rank-position formula (g2, p3 fall in the
     claimed sorted positions) hold throughout Region IIa, not just at the
     one counterexample point. Legality (p1/2,p1/2,g2,p3>0) is essentially
     free since p2>g2>0 always in B(3) — verify this explicitly but expect
     it to be a one-line check.
  3. Formalize Construction BB (p1->(g1,p2), p3->(p3/2,p3/2), leave
     p2,p4 untouched) as the closer for Region IIb. Round 22's explorer
     found BB lands within 5e-10 of c(3) exactly at the found worst point
     in IIb — strong evidence of an exact algebraic equality boundary, not
     a numeric fluke. Derive BB's exact closed-form value identity the
     same way; identify precisely which inequality of Region IIb's
     definition the equality boundary corresponds to (analogous to how
     Region I's boundary was exactly {g3+p4=3g1} for Construction H).
     Prove the order condition g1 >= p3/2 (needed for BB's sorted-position
     formula) holds throughout Region IIb — round 22 flagged this as
     checked only numerically at two points, not yet proved.
  4. If W (self-referential trisection p1->(p2,p3,p1-p2-p3), legal only
     when p1>p2+p3) is needed as a secondary witness where BB's order
     condition fails or is non-optimal, formalize its exact closed form
     too and prove its legality region covers exactly the gap BB leaves —
     otherwise drop it if BB alone suffices on all of Region IIb (test
     this first, it may simplify the proof to just Q/R + BB, two
     constructions instead of three).
  5. Combine: OddSum(best-of-{H,Q,R,BB[,W]}) <= c(3) for every p in B(3),
     completing the n=3 Existence Theorem's upper-bound direction. State
     and verify this is the FULL region cover (Region I ∪ IIa ∪ IIb =
     B(3)), not just a numeric near-cover.
Key lemmas (claim + mechanism):
  - Region II partition lemma: IIa ∪ IIb = Region II exactly, because
    Region II's own definition is a union of {p4>gamma(3)} and
    {g3+p4<=3g1}, and {p4<=gamma(3)} is the complement of the first —
    needs checking these two conditions' union/intersection structure
    exactly reproduces Region II (not merely a numerically-motivated
    relabeling).
  - Construction Q/R closed-form identity on Region IIa — mechanism:
    same substitution method as Construction H (rank-position + mass
    identity 4p4+g1+2g2+3g3=1).
  - Construction BB closed-form identity on Region IIb, with equality
    exactly at (to be determined) boundary inequality — mechanism: same
    substitution method; the near-exact numeric tightness (5e-10) is the
    signal a genuine closed-form equality exists, to be derived not
    assumed.
Open gaps: all four/five constructions' closed forms are currently only
numeric spot-checks at 1-2 points each (unlike Construction H, which has a
full proved closed form) — this round's job is to actually derive and
prove these identities, not just trust the numeric leads. The IIa/IIb
partition itself is unverified beyond 2 hard points.
Cases to cover: IIa (Q/R), IIb (BB, +W if needed) — enumerate explicitly
in the write-up; do not leave any sub-case of Region II uncovered by a
proved construction.
Watch out for: order-condition proofs (which sorted position each
fragment lands in) are exactly where round 21's Construction H work spent
most of its rigor — do not shortcut these for Q/R/BB by just checking
numerically at the found hard points; they must hold throughout the
claimed sub-region, per the same standard as Construction H. Also watch
for a Region IIa/IIb boundary overlap or gap (the two conditions as
stated are {p4>gamma(3)} and {p4<=gamma(3)}∩{g3+p4<=3g1} — if the second
conjunct is not automatically implied within Region II ∩ {p4<=gamma(3)},
there could be a third uncovered sliver; check this explicitly in step 1).
