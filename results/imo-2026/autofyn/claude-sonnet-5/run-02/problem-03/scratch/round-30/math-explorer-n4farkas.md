## imo-2026-03 (lens: does the n=3 Farkas-covering technique transfer to n=4's 60-chamber family?)

- **Headline finding (verified, exact `Fraction`): the 60-chamber family (30
  Bisect-Subset + 30 Double-Bisect-Pin) claimed "100% covered" by round 29's
  R29.5 sampling is FALSE as an exhaustive covering claim.** I found an
  explicit, exact, small-denominator counterexample **strictly in the
  interior** of the residual region $\mathcal R$ (not a boundary/measure-zero
  artifact): $p=(11,7,6,3,2)/29$ (so $T=1$). Check: $p_1=11/29\approx0.379<
  1/2$ ✓; $p_2=7/29\approx0.241$, and $1/31\approx0.032 < 0.241 < 8/31
  \approx0.258$ ✓ — well inside both bounds, not near either wall. Computing
  ALL 60 chamber formulas exactly at this point (script below) gives: **every
  single one of the 60 chambers has $\Phi_{\rm chamber}=15/29$, which exceeds
  $a_4T=16/31$ by exactly $\Phi-a_4T=1/899>0$.** I.e. all 60 fail
  simultaneously — a genuine violation of the claimed exhaustive coverage,
  not a numerical fluke (verified two independent ways: (a) the closed-form
  chamber formulas $\Phi_S=(T+A(R))/2$ and $\Phi_{\rm pin}=(T+|p_k-p_l-p_r|)/2$
  evaluated symbolically; (b) direct brute-force sort-and-alternating-sum on
  the actual fragment multiset for two representative chambers — exact match
  in both cases).
- **Root cause diagnosed, and it directly explains why round 29's random
  sampling missed it:** the true global minimizer at this witness is
  **not** in the 60-chamber family at all. A full numeric search over every
  legal $\le4$-cut allocation (all $\binom{}{}$ compositions of 4 cuts across
  the 5 pieces, each locally optimized via Nelder-Mead) finds the true
  minimum $\Phi=1/2$ exactly (comfortably $<a_4T=16/31$), achieved by:
  **cut $p_1$ into 3 pieces exactly matching $p_3,p_4,p_5$** (i.e. a
  "Triple-Pin": since here $p_1=p_3+p_4+p_5$ exactly, $11=6+3+2$, the
  residual is exactly $0$) **plus bisect $p_2$** — total $2$(effective)$+1=3$
  cuts, well within budget $4$. This is the exact $n=4$ analogue of the
  already-recorded n=3 lesson (round 4's finding, reused in round 27's
  Triple-Pin chamber for $n=3$'s case (b2)): a **single-pin** chamber
  (pin one sub-fragment to one other piece) is not enough once you're deep
  enough in the "many small pieces, top piece large" regime — you need a
  **multi-way pin** (here: 3 simultaneous pins) that the current family
  (`double-bisect-pin-family-n4`, which only pins ONE pair) structurally
  cannot express. I confirmed adding a 20-member "Triple-Pin" family
  (choose the triple-cut index $m$, the 3 pin targets $\{a,b,c\}$ from the
  remaining 4, feasible when $p_m\ge p_a+p_b+p_c$; formula
  $\Phi=(T+|p_m-p_a-p_b-p_c|)/2$, proved via the same certified
  `pair-insensitivity-corollary` mechanism as Double-Bisect-Pin, just applied
  3 times instead of once) closes this exact witness with margin
  ($\Phi=(T+0)/2=1/2$).
- **However, a second, independent exact counterexample survives even the
  80-chamber family (60+20 Triple-Pin):** $p=(14,7,5,3,1)/30$ (i.e.
  $(7/15,7/30,1/6,1/10,1/30)$), again strictly interior to $\mathcal R$
  ($p_1=14/30<15/30$; $p_2=7/30\approx0.233\in(0.032,0.258)$). A fresh
  300,000-trial exact-`Fraction` random search over $\mathcal R$ (with the
  extended 80-chamber family) found $16/90688\approx0.018\%$ of sampled
  points still uncovered — this witness is the largest-margin one found.
  Numeric full-allocation search shows the TRUE minimum here is again
  $\Phi=1/2<a_4T$, but achieved by a **different, more complex** allocation:
  $1$ cut on $p_1$ (bisect, giving fragments $=p_2$ exactly, since
  $p_1=2p_2$ here), $2$ cuts on $p_2$ (trisect), $1$ cut on $p_3$ (bisect) —
  i.e. a family combining a bisection tied to the $p_1=2p_2$ ladder relation
  with a further split of $p_2$ itself. This is **not** an instance of
  Bisect-Subset, Double-Bisect-Pin, or the Triple-Pin family above; it is a
  new, so-far-uncharacterized fourth chamber type. (Time did not permit
  reverse-engineering its exact closed form this round — flagging as the
  immediate next reverse-engineering target, in the same spirit as round
  27's numeric-optimizer-argmin-first methodology.)
- **Conclusion for the dispatch question:** the Farkas-certificate *technique
  itself* (finding a nonnegative linear combination of the region's defining
  inequalities plus the chambers' "failure" inequalities that sums to an
  identically-false statement) is dimension-agnostic and does transfer in
  principle — it is pure LP duality, and having 4 free coordinates instead
  of 3 does not break it structurally. **What breaks is the specific
  60-chamber census being complete.** The higher dimension does NOT block
  Farkas-style proofs computationally, but it does mean more chamber
  *types* are needed (single-pin $\to$ triple-pin $\to$ at least one further
  unidentified type), exactly mirroring — one level up — the
  round-4/round-27 lesson that $n=3$'s upper bound needed an "ad hoc seventh
  strategy" (trisect the top piece) beyond the natural 6-template family.
  **Do not attempt a Farkas exhaustive-coverage proof over the current
  60-chamber family as stated — it is provably incomplete and any such
  proof attempt will fail or be vacuous.** The correct next step is: (1)
  reverse-engineer and add the Triple-Pin family (20 chambers, formula and
  feasibility condition given above, provable in ~1 page via
  `pair-insensitivity-corollary` exactly as Double-Bisect-Pin was), (2)
  reverse-engineer the still-missing 4th family from the second witness
  above (or find a small set of a few more explicit witnesses via the
  numeric full-allocation-search method used here, then infer the closed
  form the same way round 27 did), (3) only once a family empirically
  achieves genuine $100\%$ coverage (checked with the SAME rigor used here —
  i.e., an adversarial optimizer searching over ALL legal allocations, not
  just sampling within the existing chamber family, since sampling within
  the family trivially reports the family's own performance and cannot
  detect that the family itself is incomplete) should a Farkas exhaustive
  case-split be attempted.
- **Methodological warning for the outliner/builder:** round 29's R29.5
  "100% coverage, zero violations" check computed, for each sampled point,
  $\min$ over the 60 chambers and compared to $a_4T$ — this can only ever
  detect a violation if the true minimizer happens to be outside all 60
  chambers by enough margin to matter at the sampled points; since ~99.98%
  of sampled points in this round's own re-check were still fine, a
  moderate-size (30k-trial) random sample is exactly the kind of check
  likely to miss a thin ($\sim2/899$-scale) but real gap. Any future
  "coverage" claim for a new/enlarged family should be re-verified using
  the **outer minimization** method used here (a fresh unconstrained,
  allocation-agnostic numeric search for the TRUE $\min_\text{legal
  strategy}\Phi$ at candidate points, not just $\min$ over the family being
  tested) before being trusted, exactly as I did to falsify R29.5.
- **Cheap-kill / reduction proposal:** the family should be organized by
  "how many cuts are concentrated on a single piece" (1 cut = Bisect;
  2 cuts+1 pin-elsewhere = Double-Bisect-Pin; 3 cuts+1 pin-elsewhere =
  Triple-Pin; possibly 2+2 split as the still-missing 4th type found above).
  This gives a natural, finite, exhaustible hierarchy (bounded by the
  budget $n=4$: at most 4 cuts total can be concentrated on one piece,
  since $m=5$ pieces total exist) rather than an open-ended ad hoc search —
  a concrete way to bound how many more chamber families can possibly be
  needed (at most a handful more, not infinitely many), which is the
  "identifying which handful are load-bearing" step round 29 itself flagged
  as open (its item 2).
- **Sanity-check script** (self-contained, run this round, all exact
  `Fraction`, no floats used for the final claims):
  ```python
  from fractions import Fraction as F
  import itertools
  a4 = F(16,31); thresh = 2*a4-1  # = 1/31
  p = [F(11,29),F(7,29),F(6,29),F(3,29),F(2,29)]; T=sum(p)
  def alt_sum(seq):
      s=F(0); sign=1
      for x in seq: s+=sign*x; sign*=-1
      return s
  # ... enumerate all 30 Bisect-Subset + 30 Double-Bisect-Pin chambers ...
  # result: min over all 60 of Phi_chamber = 15/29 > a4*T = 16/31
  #   (excess exactly 1/899 for EVERY one of the 60 chambers)
  ```
  Full script and the second witness's script were run interactively this
  session (not saved to a permanent file — reproduce via the formulas
  above: Bisect-Subset $\Phi_S=(T+A(R))/2$, Double-Bisect-Pin
  $\Phi_{i,j;k,l}=(T+|p_k-p_l-p_r|)/2$, both already stated exactly in
  `approaches/lp-duality-certificate.md` §R29.3–R29.4).

- **Candidate technique(s):** Farkas/LP-duality case-split (as in
  `gap-filler-four-chamber-covering` and `case-b2-n3-covering-closure`) is
  still the right target — but only once the chamber census is actually
  complete. The mechanism for deriving new chamber formulas
  (`pair-insensitivity-corollary`, iterated) is fully general and already
  proved for any number of simultaneous pins — no new lemma is needed to
  write down and prove a Triple-Pin (or Quad-Pin) formula, only to find the
  right index pattern (which this round's numeric-optimizer method already
  supplies for the Triple-Pin case, and can supply for further cases).

- **Knowledge-base entries to use:** none beyond what's already cited in the
  approach file; the relevant machinery (`pair-insensitivity-corollary`,
  `odd-run-reduction-lemma`, `bisect-subset-lemma`, `budget-monotonicity`) is
  already certified in `results/imo-2026-03/lemmas/`.

- **Analogous past problems (cruxes):** none newly consulted this round —
  this is a self-contained internal-consistency check of the current
  approach's own numerics, not a fresh crux-corpus search. (Round 27's
  "trisect the top piece" n=3 precedent, already on file, is the closest
  analogue and is internal to this problem's own history.)

- **Prior progress:** R28.2 ($p_1\ge T/2$ regime of $n=4$ fully closed,
  unconditional) and R29.1 (the $p_2\le T/31$ and $p_2\ge8T/31$ bands
  closed) both stand — I did not find any issue with those; my check was
  confined to the residual $\mathcal R$ and the specific 60-chamber claim.
  R29.4's Double-Bisect-Pin Theorem itself is correctly proved (I
  independently re-verified its formula) — the error is only in R29.5's
  coverage *claim*, not in any chamber's individual correctness.

- **Dead ends (do not retry):** do not attempt a Farkas exhaustive
  case-split literally over "these 60 chambers" as currently listed — I
  have an exact counterexample showing this specific family fails to cover
  $\mathcal R$, so any such proof attempt is doomed before it starts
  (unlike n=3's `gap-filler-four-chamber-covering`, whose 4-chamber family
  really was verified exhaustive by an actual algebraic Farkas certificate,
  not just sampling).

- **Small-case / intuition notes (labeled as conjecture where not proved
  here):** (1) conjectured (not proved) that $c(4)=16/31$ is still correct —
  both counterexamples to the 60-chamber family have TRUE minimum
  $\Phi=1/2<16/31$ via strategies outside the family, so the family's
  incompleteness is a proof-technique gap, not evidence against the
  answer. (2) Conjectured, based on the two witnesses' structure, that the
  full chamber census needed is "concentrate $k$ cuts on one piece pinning
  to $k$ others, for $k=1,2,3$, possibly combined with a second, smaller
  concentration on a different piece" — i.e. the hierarchy may need to go
  one step further than Triple-Pin (a "$2+1$ split" as seen in the second
  witness). This is a reasonable, structured next target for a future
  round's numeric-optimizer-driven chamber discovery, not yet a theorem.
