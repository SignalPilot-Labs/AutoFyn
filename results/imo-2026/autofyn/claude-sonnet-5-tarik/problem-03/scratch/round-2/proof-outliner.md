## imo-2026-03

Context: round 1 ended with a proof-builder hanging 909+s with no output on one of the
two build-set slugs (dyadic-cascade-induction, elementary-exchange-smoothing) — no build
progress exists yet; `.ranking.json` shows all four approaches still at `expanded:0`,
`last_outcome:null`. My job this round was to make the two build-set approaches' open
gaps SMALLER, MORE CONCRETE, and BOUNDED (no unbounded symbolic search / exhaustive
general-n casework), which is the most likely cause of the hang (Step 4's general-n
case-split accounting in dyadic-cascade-induction, and Step 3's conjectural general-n
slope derivation in elementary-exchange-smoothing). I did real mathematical work to
de-risk both gaps (not just re-wording them) and pushed the resulting insight into the
other two approaches as well. All four approach files under
`results/imo-2026-03/approaches/` have been edited in place; this report summarizes what
changed and why.

**Key new mechanism found this round (applies across approaches):** work with the excess
e := L − X = 2L − S (S = current total length) instead of L directly. e_n := 2c(n)−1 =
1/(2^{n+1}−1) is the target, and satisfies the clean recursion e_n = e_{n-1}/(2+e_{n-1})
(verified algebraically). **Lemma P-zero** (immediate corollary of the shared Lemma P): a
duplicate pair {x,x} contributes exactly 0 to e (it adds +x to L and +x to X, which
cancel in L−X) — this is strictly cleaner than reasoning about L directly, because it
means e(after XY's move) = e(residual multiset with the duplicate pair deleted) EXACTLY,
with no leftover cross-term depending on the piece that got split. Using this, I derived
and hand-verified (exact fractions, small bounded computations, not floating-point search)
a **max-normalized strengthened claim**: e ≤ a_1/2^m after m cuts, where a_1 is the
largest current piece (verified tight at the dyadic optimum for n=1,2: e_1=1/3, a_1=2/3,
ratio 1/2=2^{-1} ✓; e_2=1/7, a_1=4/7, ratio 1/4=2^{-2} ✓). This closes **Case (i)
(a_1 ≥ 2a_2) of the upper-bound induction completely**: XY bisects a_1 (always produces a
duplicate pair, no relation to a_2 needed), so e(after) = e({a_2,…,a_k}) exactly, and by
IH(n−1)'s max-form, e(residual) ≤ a_2/2^{n-1} ≤ (a_1/2)/2^{n-1} = a_1/2^n — done, no
rank-interleaving accounting needed at all. **Case (ii) (a_1 < 2a_2) is NOT resolved this
way** — I found and worked out by hand a concrete example (ratios a_1:a_2:a_3 =
1:0.9:0.6, rescaled) showing the naive "bound the tail sum by (k−1)·a_2" chain overshoots
the target for n≥2 (the required inequality e_{n-1}·n ≤ e_n·(n+2) holds with equality at
n=1 but fails at n=2: 0.667 > 0.571) — this is genuine remaining mathematical content, not
a bookkeeping slip, and is now the field's single shared open gap, narrowed to a specific
bounded 2-then-3-variable hand computation (see below) instead of a vague "accounting is
subtle."

---

dyadic-cascade-induction: advance (revised in place this round)
Target: c(n) = 2^n/(2^{n+1}-1), both directions (construction + matching upper bound), for
all positive integers n.
Technique: exchange-argument reduction (Lemma G) to an order-statistic optimization, then
explicit adversary-strategy induction on n for both directions, now reformulated via the
excess e = L−X and Lemma P-zero for the upper bound.
Skeleton:
  1. Lemma G (greedy reduction of the claiming phase) — exchange/induction argument.
  2. Lemma P (duplicate-pair invariance) and its corollary Lemma P-zero (pairs contribute
     0 to e = L−X) — by direct algebra from Lemma P.
  3. Lower bound: dyadic construction {2^{n+1-i}/(2^{n+1}-1)}, self-similarity of the
     sequence under top-piece peeling — by induction on n (open gap: full resistance to
     ALL of XY's responses, not just the cascading one).
  4. Upper bound, revised: strong induction on n proving jointly (A) e ≤ e_n·S (sum form)
     and (B) e ≤ a_1/2^n (max form). Case (i) a_1≥2a_2 closes via bisection + Lemma
     P-zero + form (B) — DONE modulo write-up. Case (ii) a_1<2a_2 (match a_1 to a_2, via
     Lemma P-zero) remains open, narrowed to a bounded hand computation.
Key lemmas (claim + mechanism):
  - Lemma G — swap-domination exchange argument, standard.
  - Lemma P / Lemma P-zero — removing a duplicate pair shifts lower ranks by an even
    amount (parity-preserving); in e-terms the pair's own contribution cancels exactly.
  - Max-normalized form (B): e ≤ a_1/2^m — because bisecting the top piece always creates
    a duplicate pair independent of the rest of the multiset, so e transfers to the
    residual with a clean halving via a_2 ≤ a_1/2.
Open gaps: Case (ii) of Step 4 (the a_1<2a_2 regime) — concrete next action: hand-verify
n=2 (3 pieces, 2 free parameters after normalizing sum=1) via closed-form 2-variable
Lagrange/boundary analysis over the case-ii region, confirming the true max of e equals
e_2=1/7 attained only at the dyadic point, BEFORE attempting n=3 or general n. Step 3
(lower bound resistance to all XY responses, not just cascading) is separately open.
Cases to cover: Case (i) vs Case (ii) in Step 4 (former closed, latter narrowed as above);
XY's single-cut vs multi-cut vs multi-piece responses in Step 3.
Watch out for: do NOT attempt the general-n Case (ii) algebra or an unbounded/exhaustive
search directly — this is the likely cause of the round-1 hang. Follow the ordered bounded
sub-steps (n=2 by hand first) in the file. Also still needs: the "fewer than full budget
never helps" lemma, and correct handling of ties in Lemma G's induction.

elementary-exchange-smoothing: advance (revised in place this round)
Target: same c(n) = 2^n/(2^{n+1}-1), via a local two-piece exchange/smoothing argument
directly on LB's partition (no explicit adversary strategy construction), proving the
dyadic ratio-2 sequence is the unique optimal LB partition.
Technique: extremal/smoothing argument (perturb-and-derive-necessary-condition), using
Lemma P / Lemma P-zero to compute the exact effect of small perturbations.
Skeleton:
  1. Reduction (Lemma G) + duplicate-pair invariance (Lemma P, Lemma P-zero) — shared
     prerequisites, import once certified.
  2. Two-piece exchange lemma: near a fixed partition a, XY's optimal response pattern is
     locally constant (genericity/transversality argument, still open).
  3. Revised: derive the local slope of e = 2g−S (not g directly) under a mass-shift, in
     the fully explicit, bounded n=2 (3-piece, 2-parameter) case by hand, reusing whichever
     of dyadic-cascade-induction's Case (ii) computation or this file's own derivation
     closes first — both approaches are now converging on the same underlying 2-variable
     computation, so whichever finishes it first should be imported by the other rather
     than re-derived.
  4. Conclude uniqueness of the ratio-2 optimum from Step 3, evaluate at the dyadic point.
Key lemmas: Lemma G, Lemma P/P-zero (shared); local-pattern-constancy lemma (open,
plausible); two-sided improving-shift lemma (open, now scoped to the bounded n=2 case).
Open gaps: Step 2's genericity claim; Step 3's exact slope formula — narrowed to a single
finite computation rather than general-n conjecture; boundary case (fewer than n+1
positive pieces) needs a short separate monotonicity argument.
Cases to cover: interior stationary point (main case) vs. boundary (fewer than n+1 pieces).
Watch out for: do NOT attempt a general-n symbolic slope derivation or an unbounded fine
grid search directly (likely cause of the round-1 hang) — do the bounded n=2 (2-parameter)
closed-form computation first, and check dyadic-cascade-induction's file for overlapping
progress before duplicating effort.

potential-weighting-upper-bound: advance (revised in place this round)
Target: same c(n), attacking only the upper-bound direction via a global potential/weight
invariant, as a hedge on dyadic-cascade-induction's Step 4.
Technique: potential/monovariant argument, now with the weight function pinned down.
Skeleton:
  1. Reduction (Lemma G) — shared prerequisite.
  2. Set Φ := L − X = 2L − S exactly (previously undetermined/dismissed as circular; now
     justified via Lemma P-zero — duplicate pairs contribute exactly 0 to Φ, which IS new
     structural information, not a disguise of L).
  3. Bisecting the current largest piece a_1 gives Φ(after) = Φ(residual) exactly (no
     approximation) — this is the "uniform per-move decrease," now an exact identity,
     resolving the case a_1 ≥ 2·(second largest) completely.
  4. Extremal/majorization sub-claim (dyadic sequence is LB's best initial partition) —
     reduces to the same "evaluate at the extremal a_1" bookkeeping as
     dyadic-cascade-induction Step 4 Case (i); not independently open.
  5. Combine to get L ≤ c(n)·S.
Key lemmas: Φ = L−X (justified, not circular); Lemma P-zero (shared).
Open gaps: the case a_1 < 2·(second largest) — the SAME shared gap as the other two
approaches above; import whichever approach closes it first rather than re-deriving.
Cases to cover: a_1 ≥ 2a_2 (closed) vs a_1 < 2a_2 (open, shared).
Watch out for: don't re-derive the shared a_1<2a_2 case independently in three files —
check dyadic-cascade-induction's progress each round first.

concavity-minimax-duality: advance (light touch, unchanged priority — lowest of the four)
Target: same c(n), via convex-analysis/minimax characterization (Sion's theorem for
existence, subgradient stationarity for the maximizer), no explicit strategies constructed.
Technique: minimax/concavity + KKT-type stationarity.
Skeleton: unchanged from round 1 (reduction via Lemma G; formalize g(a) = min over XY
responses; prove g concave as an infimum of affine functions over finitely many response
patterns; characterize the maximizer via subgradient optimality, conjectured to force
ratio 2; recover the explicit value).
Key lemmas: concavity of g (open); stationarity forces ratio 2 (open).
Open gaps: Step 3's "finitely many patterns" claim now has a concrete candidate
enumeration — XY's two elementary moves are exactly "bisect the top piece" (always
available) and "match the top piece to the second" (available when comparable), the same
two moves used in the other three approaches' e/Lemma-P-zero mechanism — but the actual
concavity/stationarity algebra is still not carried out. Deprioritized: not selected for
this round's build set.
Cases to cover: none beyond the two-move enumeration noted above.
Watch out for: highest-risk/most-abstract entry; don't invest build time here unless the
other three approaches stall on the shared Case (ii) gap for several more rounds.

---

Recommended build set for this round: dyadic-cascade-induction,
elementary-exchange-smoothing (unchanged from round 1's outline-reviewer selection — both
now have concrete, bounded next actions instead of the vague general-n gaps that likely
caused the hang). potential-weighting-upper-bound is a strong candidate to add to the
build set this round since its central gap (undetermined weight) is now resolved and it
shares the same narrowed remaining gap — but that call belongs to the outline-reviewer.

Builder safety instruction (applies to all approaches above): the shared open gap (Case
(ii), a_1 < 2·a_2) must be attacked via the ORDERED bounded steps given in each file — n=2
by hand (2 free parameters, closed-form/Lagrange, not search), then n=3, before ANY
general-n symbolic derivation or exhaustive/fine-grid numeric search. This is the
concrete fix for the round-1 hang.
