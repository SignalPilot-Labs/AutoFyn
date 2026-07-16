# Outline review — imo-2026-03 (round 3)

Problem: max_LB min_XY val, answer c(n) = 2^n/(2^{n+1}−1) (confirmed, do not re-derive). All work in
unnormalized units: G_n = {1,…,2^n}, D = 2^{n+1}−1; lower bound ⟺ val ≥ 2^n ⟺ A ≥ 1, upper bound ⟺
val ≤ 2^n. Reduction (Lemma G), measure form (Lemma M0), merge lemma all certified — foundation solid.

## Load-bearing claims tested this round (bounded numerics)
- **Shadow strategy gives val = A_1 exactly** (Regime A of the corrected upper bound). Verified on three
  n=2 configs with A_1 ≥ 1/2: carving A_1 into {A_2,…,A_m, r=2A_1−1} makes every non-A_1 piece an equal
  pair; sorted odd-picks give val = A_1 to the rational point. **Sound.**
- **The disproven "all cuts on A_1" is genuinely dead.** For (0.4,0.4,0.2), n=2: forcing XY to cut only
  A_1 gives min val = 0.625 > 4/7 ≈ 0.5714, while XY's true 2-cut min = 0.508 ≤ 4/7. The correction
  (regime split / cut any piece) is mandatory and is present in all three revisions. Confirmed.
- **LL t=1 proof holds:** sampled Q={q,8−q} × refinements of G_2 (n=3): 0 violations of A(Q∪R) ≥ 1. The
  argument (Q-odd region is the single interval (q,2^n−q); B ≤ max(R)−q; max(R) ≤ 2^{n−1} cancels
  A(Q)=2^n−2q down to A(R) ≥ 1) is clean and complete. **This is real, correct new progress.**
- **Extremal-smoothing premise supported:** coarse maximin over n=2 LB configs peaks at 0.5714 = 4/7 at
  the geometric config (4/7,2/7,1/7). Geom is (numerically) the maximizer; V(geom) = c(n). Consistent
  with the bypass route's foundation.

## Verdicts

### geometric-selfsimilar — CHANGES REQUESTED (strongest; build)
Technique right, skeleton sound, no circular step, avoids the recorded dead ends. LL t=1 (step 5) is
now closed correctly and must be written in. Regime A of the corrected upper bound (shadow, val = A_1
for 1/2 ≤ A_1 ≤ c(n)) is proven-sound (verified). Cut budget checks out: splitting A_1 into m pieces
uses m−1 ≤ n cuts since m ≤ n+1.
Open gaps the builder must carry as explicit gaps (not hand-wave):
- **LL t≥2, A(Q)>0 residual middle** (step 6) — the load-bearing lower-bound gap. The two settled
  sub-chunks (disjoint-region B=0; Q-odd ⊇ R-odd giving A(Q)=A(Q∪R)+A(R)) are legitimate; the residual
  is real and unproven. Do NOT let "self-similar recursion is the natural handle" stand as a closed step.
- **Regime B** (A_1 < 1/2): only the loose bound val ≤ 1/2 < c(n) is needed — must still write a clean
  pairing/A-decrease argument, not assert it.
- **Regime C** (A_1 > c(n)): OPEN. The proposed recursive-reduction (first cut splits A_1 into
  (1−A_1, 2A_1−1), recurse the (n−1) bound on a scaled sub-instance) is a mechanism, not yet a proof —
  keep it flagged as a gap; the scaling/IH must be made rigorous, and the note that equal-n-split only
  reaches A_1 ≤ (n+1)/D < c(n) shows the naive fallback is insufficient.

### alternating-sum-value — CHANGES REQUESTED (distinct rival; build)
Genuinely distinct from geometric-selfsimilar (integral-rep tool; parity LL mechanism; potential-decrease
upper bound), so a failure of one mechanism does not sink both — not the single-line trap. Certified
foundation + Case 1 + tightness are solid.
Issues to fix while building:
- **LL via parity-of-piece-count** is concrete only for the sub-case k=2n+1 (all n cuts, "1" uncut) AND
  min-piece ≥ 1, where A ≥ min ≥ 1 in one line. The report already warns not to overclaim this closes LL
  — honour that. The residual (min < 1, or k even) is the same difficulty class as the shared gap; write
  it as an explicit gap, do not paper over it with "strengthen the IH."
- **Potential-decrease greedy upper bound (Opening 4)** is currently close to a restatement of the goal
  ("n greedy cuts drive A ≤ 1 for every config, tight at geometric") with no proven per-cut bound. This
  is a hidden difficulty behind a bare label. Builder must FIRST validate the greedy sign on a few
  configs (bounded), then either prove a genuine per-cut decrease bound or record it as an open gap —
  not present it as established. The essential constraint (≤ n cuts prevents the {2/3,2/3,2/3}-type
  over-splitting that would push A below 1 with too many cuts) must actually be used.

### extremal-smoothing — CHANGES REQUESTED (bypass route; build)
This is the primary upper-bound bypass now that "all cuts on A_1" is dead and the per-config strategy has
two open regimes. Value-at-geometric (S0) = LL (imported) + one replica response, and the maximizer
premise is numerically supported. Worth a build slot as the genuine bypass of Claim U.
Issues:
- **GAP S1 (smoothing) is the whole bet and is the least substantiated.** Local concavity ("min of
  affine payoffs is concave within a fixed sort-order + XY-response cell") is a valid standard fact. But
  the global step — "no competing local max above c(n)" via the exchange argument — is currently
  hand-waved. Builder must verify the perturbation sign on 2–3 explicit non-geometric spectra (bounded)
  BEFORE committing, and must route the global step through USC + exchange, not naive calculus (the min
  of piecewise-linear is not globally concave — heed the watch-out).
- Do not over-claim a UNIQUE maximizer (a second n=2 config also hits 4/7); only the MAX VALUE = c(n) is
  needed. State XY uses ≤ n cuts on the ≤ side.

## No RETHINK
None of the three repeats a recorded dead end: all three explicitly drop "concentrate all cuts on A_1"
and the failed top/bottom (A_top ≥ 2B) decomposition. No circular step in any DONE portion. The
approaches are three distinct whole attempts (distinct upper-bound routes; LL t≥2 attacked by two
distinct mechanisms), so the field is broad, not collapsed.

## Shared-gap watch
LL t≥2 (A(Q)>0) has been the shared open lower-bound gap since round 2. It is now attacked by two
distinct mechanisms (B-casework in geometric-selfsimilar, parity-of-piece-count in alternating-sum-value)
and the upper bound is being bypassed by extremal-smoothing — so the field has not collapsed to one
line. If LL t≥2 remains unchanged after this round, it should be flagged next round as a plateau
requiring a dedicated bypass explorer per the CLAUDE.md shared-gap rule.

## Ranking (updated, stale cleared)
geometric-selfsimilar 1558.9 > alternating-sum-value 1499.5 > extremal-smoothing 1441.6.
Anchors: geom-ss has the most proven content this round (LL t=1 closed + Regime A upper bound proven),
so it beats both; alt-sum has real proven foundation + a concrete (if partial) LL handle, beating the
outline-only extremal-smoothing whose core lemma (S1) is entirely unproven.

build set: geometric-selfsimilar, alternating-sum-value, extremal-smoothing
