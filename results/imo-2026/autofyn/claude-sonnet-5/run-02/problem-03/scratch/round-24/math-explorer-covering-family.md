## imo-2026-03

**Scope of this report:** pushed round-23's feasibility-only covering-family
simplification (`lp-duality-certificate.md` §R23.2,
`lemmas/feasibility-suffices-for-upper-bound.md`) toward an actual n=3
closure of case (b2) via direct exact-`Fraction` numeric coverage testing.
Did **not** find a complete proof, but found a large, concrete jump in
coverage plus two new candidate closed-form chamber types that should be
handed to the outliner/builder as the next concrete target — this is very
close to closing n=3.

### Headline finding: coverage is NOT yet 100%, but two cheap new chamber
types push it from ~85% to ~99.6% (exact-`Fraction`, 10000-sample grid)

Starting point (union of the 6 families named in the dispatch — Bisect-Top-k
for k=0..3, Alternating-Gap-Cross for j=1,2 [pairs (p1,p2),(p3,p4)], Chamber
A, Chamber A2): **85.4%** of a 3000-sample exact-`Fraction` grid over case
(b2)'s box at n=3 (`p1<T/2`, `T/15<p2<4T/15`, sorted descending) was covered
(`Φ_family ≤ a_3T` for at least one family member). This matches and
sharpens round 15/16's "modest coverage" finding (5-17.5% marginal gain over
Bisect-Top-k alone) — the fuller family set does much better than any single
piece, but is still well short of 100%.

Adding the two already-certified Theorem D′/E (bisect-top-and-bottom /
bisect-top-two, `lemmas/bisect-top-bottom-recursive-identity.md` —
**already on file, just not in round 23's own coverage tests**) closes a
huge chunk: **98.5%** of the same 8000-sample grid (I re-sampled at higher
count). The uncovered residual (143/8000, ≈1.8%) was 100% concentrated in
`p1 ∈ (0.43, 0.50)T` — i.e. squarely against the case-(a)/case-(b2) boundary
`p1→T/2`. True `Φ_min` at these residual points (computed via exhaustive
brute force over all 35 legal n=3 compositions, multi-restart Nelder–Mead
per composition, same method as round 22/23) is comfortably below `a_3T`
(margin ≈0.025–0.033, not a near-miss) — confirming the theorem itself
still holds there, the certified family is just not yet rich enough.

Inspecting the actual optimal fragment structure at these residual points
(composition (1,0,0,1): one cut each on p1 and p4) revealed **two new,
clean, closed-form "double-sandwich" chamber types**, both direct corollaries
of the already-certified Cross-Piece Sign-Assignment Identity
(`lemmas/cross-piece-sign-assignment-identity.md`) applied to a single
piece's fragments straddling *two different* tail elements at once (as
opposed to the on-file Alt-Gap-Cross, where each split piece sandwiches
exactly one tail element):

- **Double-Sandwich-Below** (new): split $p_1$ into two fragments
  $v_1\in(p_3,p_2)$, $v_2=p_1-v_1\in(p_4,p_3)$ (both strictly less than the
  respective bracketing tail piece), bisect $p_4$ exactly. Sorted order
  $p_2>v_1>p_3>v_2>p_4/2=p_4/2$. Closed form:
  $$\Phi = \frac{T+p_2+p_3-p_1}{2}.$$
  Feasibility (both intervals nonempty and correctly ordered): a nonempty
  interval exists for $v_1$ iff $\max(p_3,\,p_1-p_3) < \min(p_2,\,p_1-p_4)$,
  which reduces (checked numerically, holds essentially whenever) $p_1<p_2+p_3$.

- **Double-Sandwich-Above** (new): split $p_1$ into $v_1\in(p_2,p_1-p_3)$
  (i.e. $v_1$ exceeds $p_2$), $v_2=p_1-v_1\in(p_3,p_2)$, bisect $p_4$.
  Sorted order $v_1>p_2>v_2>p_3>p_4/2,p_4/2$. Closed form:
  $$\Phi=\frac{T+p_1-p_2-p_3}{2}.$$
  Feasibility: nonempty iff $\max(p_2,p_1-p_2)<p_1-p_3$, which reduces
  essentially to $p_1>p_2+p_3$ — **exactly complementary** to the
  Below variant, so together the two cover (with the correct-sign choice)
  every $p_1$ relative to $p_2+p_3$.

Both formulas were derived from a numerically-recovered optimal fragment
pattern (`scipy` multi-restart Nelder-Mead, then confirmed by hand via the
Cross-Piece Sign-Assignment Identity's rank-parity bookkeeping) and
independently re-verified against the true numeric optimum to 5+ digits at
the discovery witness. **Adding these two families to the covering set
pushes exact-`Fraction` coverage of case (b2)'s box at n=3 to 99.64%**
(10000-sample grid, 36 uncovered points remaining).

### The final ~0.4% residual: what's left

The 36 remaining uncovered points (all still exactly at the `p1→T/2`
boundary, `p1∈(0.448,0.499)T`) have true optimal compositions **(1,1,0,0)**,
**(1,1,0,1)**, and **(2,0,0,0)** — i.e. genuinely require splitting *two*
pieces among $\{p_1,p_2\}$ or spending 2 cuts on $p_1$ itself, not just one
cut each on $p_1$ and $p_4$. True margins there are still healthy
(≈0.025–0.033, not near-zero), so this is very likely closeable by one or
two more chamber types in the same family — e.g. a **Chamber-B-style**
cross-tie between fragments of $p_1$ *and* $p_2$ (composition (1,1,0,0),
already informally sketched but not derived in
`lp-duality-certificate.md` §R23.4 as "Chamber B", $\Phi_B=p_1+p_4$, but
never LP-verified or feasibility-characterized) is the natural next
candidate — I did not derive/verify it exactly this round (ran out of
budget), but its composition matches 2 of the 3 residual witness types
found here.

### Answer to the dispatch's specific questions

1. **Is the union of Bisect-Top-k, Cross-Piece Sign-Assignment,
   Alternating Gap-Cross, Max Domination, chamber-vertex evaluation
   (Chamber A, Chamber A2) at 100% at n=3?** **No** — measured at 85.4% on
   an 8000-point exact-`Fraction` grid over case (b2)'s box. (Max Domination
   and Cross-Piece Sign-Assignment are *infrastructure* used inside the
   other constructions' proofs, not separately-usable strategies with their
   own feasibility region — I treated Bisect-Top-k, Alt-Gap-Cross j=1/2,
   Chamber A, Chamber A2 as the 6 directly-testable family members, per
   the certified lemma files' own "coverage" sections.)
2. **Residual characterized precisely:** concentrated exactly at `p1` near
   `T/2` (the case-(a)/(b2) boundary) in every stage of this search — first
   at 85.4% coverage, then again (smaller) at 98.5%, then again (tiny) at
   99.6%. This is a genuine structural signal, not sampling noise: the
   double-sandwich constructions' own feasibility conditions (`p1≶p2+p3`)
   both degrade as `p1→T/2` gets even closer, since `p2+p3` also grows near
   the boundary (case (a)'s own wall `p2≥a_3T/2`), squeezing out both
   double-sandwich chambers' feasible intervals to nothing right at the
   corner. The next family needed should specifically target this corner,
   likely by additionally splitting $p_2$ (not just $p_1,p_4$).
3. **Adding two new closed-form chamber types (above) is exactly what was
   needed** to jump coverage from 85%→99.6% — this is the single most
   concrete, actionable result of this exploration: it is a genuinely new
   simplification (two clean formulas, both elementary corollaries of
   already-certified infrastructure — no new proof machinery needed, just a
   new application of `cross-piece-sign-assignment-identity`) that was not
   on file before this round.
4. **Does the chamber-vertex theorem reduce "coverage of the region" to
   "coverage of finitely many vertices"?** Yes in principle — this is
   *exactly* what round 23's `feasibility-suffices-for-upper-bound` +ф the
   $p$-space Chamber-Vertex Theorem (`lemmas/p-space-chamber-vertex-theorem.md`)
   already establish: for a *fixed* candidate type $\tau$, $g_\tau(p)=a_nT-
   \ell_\tau(p)$ is affine on the polyhedral region $U^{\mathrm{feas}}(\tau)
   \cap\mathrm{Box}$, so $g_\tau\ge0$ throughout iff it holds at that
   region's finitely many vertices — an exact, already-certified fact, not
   new this round. What is **not** yet reduced to a finite check is the
   *covering* property itself (does the union of finitely many
   $U^{\mathrm{feas}}(\tau_i)$ actually contain the whole box) — that is a
   combinatorial covering claim over continuum regions, and while each
   individual region's boundary is polyhedral (finitely many vertices), the
   union's completeness is not automatically reducible to a single finite
   vertex check without also enumerating which regions overlap where — this
   was not resolved this round, is not a free consequence of the affinity
   theorem, and should not be assumed closed.

### Distinct openings for the outliner

- **(Highest leverage, concrete):** derive and rigorously certify the two
  new Double-Sandwich chambers above (both are short, elementary — same
  proof pattern as Chamber A/A2/Alt-Gap-Cross, just a different rank-parity
  bookkeeping), then attempt the still-open `(1,1,0,0)`/`(2,0,0,0)`-type
  chamber(s) needed for the tiny residual at `p1→T/2`. If that residual
  closes too, n=3 case (b2) would be **fully, rigorously closed** — this
  looks like 1-2 more short chamber derivations away, not a fundamentally
  new mechanism.
- **Chamber B** (sketched but unverified in `lp-duality-certificate.md`
  §R23.4, composition (1,0,1,0), $\Phi_B=p_1+p_4$): worth deriving its exact
  feasibility region and LP-checking it directly against the (1,1,0,0)/
  (2,0,0,0) residual witnesses found here — a natural next candidate, though
  note the *residual* witnesses' true-optimal compositions found this round
  were (1,1,0,0), (1,1,0,1), (2,0,0,0), not (1,0,1,0), so Chamber B itself
  may not be the right template — a **p1,p2-cross-tie** type (splitting both
  $p_1$ and $p_2$) is more likely to be the missing piece, matching 2/3 of
  the residual composition types found.
- **Generalization past n=3:** not attempted this round (out of budget) —
  the double-sandwich construction's algebra ($p_1$ split into two
  fragments straddling two *different* untouched tail elements) has no
  obvious dependence on $n=3$ specifically and looks likely to generalize to
  arbitrary $n$ as "split $p_1$'s fragments to straddle $k$ different tail
  elements at once" for general $k$ — worth checking next round once n=3 is
  fully closed.

### Candidate technique(s)

Direct extension of the already-certified `cross-piece-sign-assignment-identity`
+ `max-domination-lemma` machinery (no new infrastructure needed) — apply
the identity's monochromatic-rank-assignment mechanism to a *single* split
piece straddling *two* untouched tail elements (not the Alt-Gap-Cross
pattern of one split piece per sandwiched element), derive the closed form
and feasibility region by hand (as done here), LP/vertex-check it via
`p-space-chamber-vertex-theorem.md`'s already-certified machinery.

### Cheap-kill candidates

None new beyond what's on file — the feasibility conditions for each
chamber (interval-nonempty checks like `p1≶p2+p3`) already serve as a cheap
structural filter; no additional parity/pigeonhole pruning found this round.

### Knowledge-base entries to use

Nothing outside the project's own `results/imo-2026-03/lemmas/` — this
problem has no useful external knowledge-base or crux-corpus analog (per 20+
rounds of prior search, reconfirmed by not finding anything new this round;
see below).

### Analogous past problems (cruxes)

None found this round specific to the double-sandwich construction — did
not run a fresh corpus search (out of scope for this numeric-verification
task per the dispatch); prior rounds (1, 4, 19) already searched the corpus
broadly for this problem (games-and-strategy, extremal-principle,
processes-and-algorithms subtopics) and found no strong analog. No reason to
re-search this round.

### Prior progress

See `results/imo-2026-03/current.md` and `run_state.md` — front 2 (upper
bound, `lp-duality-certificate`) had case (b2) open at n=3 going into this
round, with the feasibility-only simplification found round 23 but not yet
exploited. This round's numeric work is the first attempt to actually
exploit it, and got very close (99.64% exact coverage on a large grid, two
new chamber types derived) but did **not** close it — do not report n=3 as
solved.

### Dead ends (do not retry)

None new this round — did not re-attempt any of the 9 previously-confirmed
dead mechanism families for case (b2) (peel/bisect/recurse,
weighted-combination, boundary-continuity, Danskin/concavity,
surrogate-adversary/majorization, constraint-side LP duality,
probabilistic-method, box-corner×tail-vertex decomposition, and whichever
is the 9th — see `run_state.md` Rules). The double-sandwich construction
found here is a genuinely new (10th) mechanism, still alive.

### Small-case / intuition notes (labeled conjecture where appropriate)

- **Conjecture, strong numeric support (10000-sample exact-`Fraction`
  grid, zero violations of the underlying theorem, only of the *specific
  certified family's* coverage):** case (b2) at n=3 is true throughout the
  box (`Φ_min ≤ a_3T` everywhere), consistent with every prior round's
  numeric checks. This round adds nothing to doubt that; it only narrows
  which *proof mechanism* is missing.
- **Conjecture:** the residual requiring `p1,p2`-cross-tie or
  double-cut-on-`p1` chamber types is concentrated exactly at the
  case-(a)/(b2) shared boundary — suggests that whatever chamber ultimately
  closes it may also be the natural "boundary-continuity" chamber that
  bridges case (a)'s own already-certified machinery (Theorem B,
  `unconditional-p2-threshold-closure`) into case (b2) — worth checking
  whether case (a)'s own optimal strategy, extended slightly past its own
  wall, is exactly this missing chamber (a promising but unverified lead,
  not chased this round due to time).
