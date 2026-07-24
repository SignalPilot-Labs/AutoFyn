## imo-2026-03 (lens: direct conservation/invariant route on the tied-vertex GAP-L residual)

- **Headline finding (the useful one): the illustrative residual example is NOT a genuine
  local minimum.** `current.md`/`self-similar-recursion.md` present `{4/3,4/3,4/3,2,1}`
  (from `W_2={1,2,4}`, two cuts trisecting the top piece "4") as a "stable" tied
  non-degenerate minimizer with `f=5/3`, stationary because Lemma I's *single-slide*
  one-sided derivatives vanish on it. I checked this **exactly** with rational arithmetic
  (not floats) and found a **strictly f-decreasing joint perturbation**: move both cut
  points on the "4"-piece simultaneously in opposite directions (shrink the two flanking
  thirds, grow the middle third by the same total). Exact computation: with cut fractions
  `p1=1/3, p2=2/3`, perturbing to `(p1-δ, p2+δ)` gives `f(δ) = 5/3 - 8δ` **exactly linear**,
  confirmed identically at `δ=10^-3, 10^-5, 10^-7` (ratio `diff/δ = -8` exactly every time —
  this is a genuine nonzero one-sided directional derivative, not a numerical artifact or a
  higher-order effect). So the point is a **saddle**, not a local min: Lemma I's
  single-adjacent-slide stationarity is *necessary but not sufficient* for local minimality;
  this point fails a *joint* two-parameter perturbation that Lemma I never tests.

- **Why this matters / candidate route to CLOSE (not just narrow) the residual.** The
  failing direction is a specific structural move: within one tie-block of size `k≥2` formed
  by splitting a SINGLE original dyadic piece into `k` (here 3) equal/tied sub-pieces
  occupying consecutive ranks, "squeeze mass from the two flanking members into an interior
  member" reassigns which member sits at the (negative-sign) top of the block and which at
  the bottom, and to first order this is **not** flat like a same-direction transfer between
  two block members is (Lemma I only computes flat transfers between exactly two adjacent
  members holding the rest fixed — a 1-parameter subfamily of the actual `(k-1)`-parameter
  freedom). Conjectured strengthening (not proved, this is the opening to hand the outliner):
  **any non-degenerate tie-block of size ≥2 arising from splitting one original piece can
  always be perturbed to strictly decrease `f`** — i.e. within-piece ties never survive as
  genuine ambient local minima; they are dominated by more bisection-like (fewer distinct
  values) redistributions, consistent with Theorem G's cascade being the true attractor. If
  provable in general (I did not attempt the general proof — out of scope for this report),
  this makes the "non-degenerate minimizer pinned at a within-piece rank tie" case **vacuous**,
  which would close GAP-L outright (combined with the already-certified tie-free and
  degenerate cases).

- **Numerical support (exhaustive-ish, not proof).** I wrote an exact search over `W_n`,
  `n=2,3`, all cut-count patterns summing to the budget, many random restarts per pattern,
  each candidate verified as a genuine local min by testing ~150 random JOINT perturbation
  directions across the FULL parameter vector (all cuts on all pieces at once, not just
  single slides). Result: **every verified genuine local minimum found was tie-free with
  f = 1 exactly** (some are degenerate, i.e. a cut length →0). Zero non-degenerate tied
  genuine local minima were found in either exhaustive search. This is consistent with — and
  somewhat stronger than — the "min f = 1" numerics already in `current.md`; it specifically
  targets the tied-vertex case the residual worries about and still finds none.

- **What the squeeze argument does NOT (yet) cover — the honest remaining gap.** The squeeze
  trick needs a shared mass-conservation budget between the tied members (they must be
  sub-pieces of the *same* original piece, so redistributing among them is legal). It does
  **not** directly attack a hypothetical **cross-piece tie**: two sub-pieces of *different*
  original dyadic blocks that happen to take the same real value `v` and land at adjacent
  ranks. There is no shared budget to redistribute between them by a squeeze. However: if
  either side of such a cross-tie itself has further internal freedom (i.e., that original
  piece was cut into ≥2 sub-pieces), Lemma I's single-slide analysis on THAT piece alone
  already forces monochromaticity-type constraints (as in Lemma J), so the interesting case
  is only when BOTH tied members are entirely uncut singletons from two different original
  pieces (e.g., two original dyadic values that coincide, or one dyadic piece equal to a
  sub-piece of another) — this is measure-zero/coincidental and did not appear in my
  searches. Flag this as the true residual-residual if the outliner pursues the "within-piece
  ties are vacuous" route.

- **Distinct openings for the outliner:**
  1. **Kill the within-piece tied case entirely** by generalizing the squeeze-perturbation
     computation into a lemma: "a tie-block of size ≥2 from one original piece is never
     stationary under the full joint perturbation" (extends Lemma I/Lemma J's stationarity
     test from single-slides to the full local chamber gradient). This looks like the
     highest-value next step — it directly targets and likely eliminates the stated residual.
  2. Separately handle the (apparently vacuous / measure-zero) cross-piece coincidental-tie
     case, probably via a genericity/perturbation argument (perturb `n` slightly so that no
     two originally-different dyadic values can coincide after cutting, since the dyadic
     values `2^k` are rationally independent in the relevant sense) — or show it reduces to
     the monochromatic case whenever either side has internal cuts.
  3. (Not pursued/rejected) treating the unconstrained relaxation (any multiset of fixed sum
     and piece-count, ignoring per-piece origin) as a proxy — this is INVALID: it achieves
     lower `f` values than the true game (e.g. 5 pieces of `7/5` each give `f=7/5<5/3`, not
     reachable by legal within-piece cuts of `W_2`), because it drops the essential per-piece
     conservation constraint `Σ(sub-pieces of 2^k)=2^k`. Do not recommend this route.

- **Candidate technique(s):** local KKT/exchange-argument on the piecewise-affine chamber
  structure (already the framework of Lemma I/J); this round's addition is testing JOINT
  (not just single-slide) directional derivatives at tie-blocks — an exchange/majorization-
  style argument ("squeeze toward the interior strictly helps"), analogous in spirit to
  standard "any non-improving transfer contradicts extremality" arguments.

- **Cheap-kill candidate:** before deep-diving, check whether the general squeeze
  perturbation's sign is UNIFORM (always favorable to squeeze inward) across all block sizes
  `k` and both parities of the block's starting rank — if the sign flips depending on parity
  it might not universally kill ties and would need casework. I verified only `k=3` (this
  round's time budget); the outliner/builder should check `k=2,4,5` symbolically before
  claiming full generality.

- **Knowledge-base entries to use:** none of `knowledge_base.md`'s named entries directly
  cover this move (no majorization/convexity entry found — grepped for
  "majoriz|convex|alternat|rearrange", no hits). The relevant certified in-house lemmas are
  `lemmas/layer-cake-alt-sum.md` (f=M identity, matched-pair invisibility P1) and the
  in-approach Lemma I (`self-similar-recursion.md` §4, one-sided cut-slide derivative) which
  this finding shows is *necessary-but-insufficient* for detecting non-minimality at ties.

- **Analogous past problems (cruxes):** searched `combinatorics` subtopics
  `games-and-strategy`, `extremal-principle`, `invariants-and-monovariants` (386 cruxes) for
  cutting/alternating-sum/tie-adjacent moves. Best partial analogy: **aimo-0119** — "Pick the
  configuration minimizing the maximum part load, tie-broken by fewest parts attaining that
  maximum, so that any single-item transfer from the heaviest to the lightest part is
  non-improving" — the same *exchange-argument* flavor (extremal config ⇒ every legal
  transfer is non-improving; here we found a transfer that IS improving, contradicting
  supposed extremality). Not a solution template to copy (different problem entirely) but
  the general proof pattern ("assume minimality, exhibit a strictly improving move,
  contradiction") is exactly the shape needed to kill within-piece ties. No other corpus
  entry resembles the stick-cutting alternating-sum game closely enough to be more than this
  generic exchange-argument analogy.

- **Prior progress:** GAP-U fully proved and certified (round 3). GAP-L complete on every
  tie-free non-degenerate minimizer (Lemma J + odd-integer floor) and every degenerate
  minimizer (cut-count induction). Sole open case: non-degenerate minimizers pinned at a
  rank tie.

- **Dead ends (do not retry):** the "dual-price / one-shot LP-duality route to GAP-L" (dead,
  recorded in `alternating-sum-threshold-potential`). The blanket "cutting a non-max piece
  never helps XY" (FALSE, 28k counterexamples). Parity-of-*pieces* for non-integer cuts
  (dead, admits `f=1/3` under `d=3` scaling). NEW this round: do not treat the unconstrained
  (origin-blind) relaxation of the alternating-sum minimization as informative — it
  underestimates `f` and is not a valid relaxation of the actual game (see opening 3 above).

- **Small-case / intuition notes (labeled conjecture):** Conjecture — no genuine non-degenerate
  local minimum of `f` over any `N`-cut refinement chamber of `W_n` has a rank-tie whose
  members originate entirely from splitting one single dyadic piece; all such candidate points
  are saddles dominated by a squeeze toward fewer/more-unequal values, ultimately bottoming at
  the tie-free odd-integer floor `f≥1`. Support: exact rational verification of the strict
  improving direction at the concrete `{4/3,4/3,4/3,2,1}` example (linear in the perturbation,
  confirmed at three different scales), plus an exhaustive-ish numerical search over `n=2,3`
  and all cut-count patterns finding zero genuine non-degenerate tied local minima. Not yet
  proved in general; cross-piece coincidental ties remain a (likely vacuous, unverified)
  loose end.
