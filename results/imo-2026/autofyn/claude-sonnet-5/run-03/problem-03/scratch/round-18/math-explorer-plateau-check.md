## imo-2026-03

- Distinct openings:
  1. **GT(m) odd-excess residual (lower-bound side).** After round 17's
     correction, the *only* remaining hole in sub-case (i) of GT(m) is:
     for odd excess $e=1$ (and possibly all odd $e\ge1$, unconfirmed for
     $e\ge3$), $a_1\in[2^{k-1}+1,2^k]$ (outside the width-1 window), under
     GT(m)'s own cardinality cap $|D|\le m+1$. This is a discrete
     telescoping/peeling-identity problem: track the coupled pair
     $(O_j,E_j)$ through $e$ steps and show the resulting closed form
     beats $2^k-a_1$ at the true worst case $a_1=2^k$ (not just inside the
     window, which round 17 already covered). The needed tool is almost
     certainly a *cap-aware* refinement of the Large-Sum Closure
     Theorem/Even-target Companion Peeling identity — i.e. push the
     existing certified machinery one more step rather than reframe.
  2. **Sigma-shape / Flat-Edge maximizer classification (upper-bound
     side).** The Existence Theorem's residual is now understood via the
     certified Flat/Kink Parity Lemma (slope
     $[\mathrm{rank}(x)\ \text{odd}]-[\mathrm{rank}(y)\ \text{odd}]$) as a
     genuine dichotomy (sharp kink vs. flat plateau), but there is still
     no proved rule for *where* the true global maximizer $p^*$'s
     Flat-Edge/Self-Bisection-Crossover face sits as a function of $p$ —
     opening: try to directly characterize $p^*$'s optimal shape via the
     parity lemma itself (e.g. show the maximizer must always sit at a
     kink, never strictly inside a flat plateau, which would collapse the
     search to isolated points) rather than continuing to hunt families.
  3. **lp-duality-split-polytope's necessity direction — a genuinely
     different counting mechanism (double-counting/interface-sum, see
     below) as a cheap-kill before further mass-constraint refinement.**
  4. **A "prove it structurally can't be worse than s≈N/2" abandonment
     opening**: since the mass-counting technique is now *proved* (not
     just observed) to cap at $s\gtrsim N/2$, treat the $s\ge n-1$
     necessity conjecture as requiring an entirely different invariant
     (not a strengthening of Generalized Mass-Constraint) — a global
     count over *all* legal responses simultaneously, in the style of
     aimo-0091/aimo-0178 below, rather than a per-response mass bound.

- Candidate technique(s): (1) cap-aware coupled $(O,E)$-pair telescoping,
  reusing `even-target-companion-peeling-and-corrected-qzero-chain.md`
  and `half-sum-corollary-and-large-sum-closure-theorem.md` — extend
  the Large-Sum Closure Theorem's proof to also cover $a_1=2^k$ exactly
  (the true worst case), likely needs the Even-target twin invoked at the
  *last* step of the chain rather than only for parity bookkeeping; (2)
  for Sigma-shape, push the Flat/Kink Parity Lemma toward a "maximizer
  avoids interior flat points" argument (perturb along the flat direction
  and show a competing branch beats it strictly outside the interior,
  i.e. an LP-vertex-style boundary-attainment argument specific to Flat
  regions); (3) for lp-duality necessity, a double-counting/"sum of
  per-seam minimums" style global argument (see cruxes below) as an
  alternative to Mass-Constraint.

- Cheap-kill candidates: for gap 1, before any new proof effort, run an
  exact-`Fraction` sweep of the true worst case ($a_1=2^k$ exactly, or
  arbitrarily close) at several $(k,e)$ with $e$ odd, $e\ge3$, under the
  cap — round 17's current.md only reports this checked cleanly for
  $e=1$ (145,546 trials) and reports $e\ge3$ "not established by the
  file's proof either" though 140,245 stress trials found no
  counterexample; a fresh, larger, adversarially-seeded sweep at $e=3,5$
  specifically targeting $a_1$ near $2^k$ (not generic random $a_1$)
  would either find a genuine counterexample (killing "closed for all
  odd $e$" before investing in a general proof) or strengthen confidence
  enough to justify the general proof attempt. For gap 3 (lp-duality
  necessity), a cheap symmetric/double-counting sketch: fix $n$, sum a
  per-piece "must each active piece contribute at least X mass" bound
  over all $n+1$ pieces simultaneously (not just at $e_0$) and see if a
  cyclic/symmetric argument (à la aimo-0178's $N_x+N_y\ge n$ summed over
  3 axes) forces $s\ge n-1$ directly — 30 minutes of hand algebra would
  tell you fast whether this is a dead end or has legs.

- Knowledge-base entries to use: none beyond what's already cited by the
  live approach files (this problem's own certified lemma cache is the
  effective "knowledge base" at this stage); no generic knowledge_base.md
  entry not already in use was found relevant to either specific
  remaining gap.

- Analogous past problems (cruxes): searched `combinatorics` subtopics
  `sequences-and-recurrences`, `extremal-principle`,
  `inequalities-SOS-and-convexity`, plus a keyword sweep across all
  domains for "coupled recursion" / "alternating" / "minimum number of"
  style moves.
  - **aimo-0678** (number_theory, coupled gcd/lcm recursion,
    "form the sum of the two coupled sequences as an invariant... once
    one coordinate is bounded, reduce the other") — surface-level
    resemblance to tracking a coupled $(O_j,E_j)$ pair, but its actual
    target (eventual periodicity of an integer sequence via a bounded
    monovariant) is a completely different genre from our closed-form
    telescoping inequality; **not a real match**, don't force it.
  - **aimo-0091** (combinatorics, double-counting/coloring-and-parity,
    "sum the forced minimum number of straddling tiles over every
    interior grid line and compare against board area") and **aimo-0178**
    (combinatorics, extremal-principle/double-counting, "sum a full
    symmetric cycle of pairwise lower bounds and halve to bound the
    total", used to prove a beam-count lower bound of $3n/2$ in a cube)
    — a genuinely different mechanism family (global additive/cyclic
    double-counting forcing a minimum count) from anything tried so far
    on the $s\ge n-1$ necessity conjecture (which has only ever used a
    single-point mass-counting argument at $e_0$). Flagged as a **cheap,
    30-minute-scale thing to try** for `lp-duality-split-polytope`'s
    stuck necessity direction, not a confirmed fit — the target objects
    (grid seams / cube beams vs. split-fragment masses) are structurally
    different enough that this is a genuine gamble, not a strong analogy.
  - No corpus match found for the GT(m) odd-excess gap specifically — it
    is a self-contained closed-form telescoping-inequality problem with
    no obvious crux parallel; the existing certified machinery
    (Companion Peeling / Threshold-Pair-Peeling / AltSum identities) is
    already the right toolkit, this is a "push it one more step" problem,
    not a "need new outside technique" problem.

- Prior progress: see current.md's round 17 entry in full. Summary:
  GT(m) sub-case (i) is closed for even excess $e\ge2$ (whole range) and
  for the width-1 window at every $e\ge1$ (both parities); the ONLY open
  piece of sub-case (i) is odd excess, outside the window, under the
  cap — concretely open at every $k\ge2$, $e=1$ (and unresolved, not
  refuted, for odd $e\ge3$). Sigma-shape: Flat/Kink Parity Lemma fully
  proved and certified (`lemmas/flat-kink-parity-lemma.md`), unifying
  Self-Bisection-Crossover and Flat-Edge as one mechanism, but no
  predictive rule for where $p^*$'s own maximizer sits. lp-duality's
  Generalized Mass-Constraint Theorem gives one genuine impossibility
  instance ($n=8,s=4$) and is proved (via an explicit asymptotic
  argument, not just numerically) to structurally cap at $s\gtrsim N/2$
  — cannot reach $s\ge n-1$ by refinement.

- Dead ends (do not retry): (a) the naive one-step $\mathrm{Odd}\to
  \mathrm{Odd}$ telescoping of a $q=0$-chain (round 16's Step 0) — false,
  must use the coupled $(O,E)$-pair recursion instead (round 17, fixed).
  (b) Any refutation of GT(m) using $D$ with $|D|>m+1$ — out of scope,
  not a real counterexample (round 17). (c) All 4 previously-tested
  bounded tie-topology families for Sigma-shape (cyclic pairwise-tie
  chain, star/tree, descending fragment chain, generic exhaustive-search
  restricted-to-natural-orderings) — refuted, do not re-attempt variants.
  (d) Region-geometry/fixed-target-vertex exchange mechanisms for the
  Existence Theorem — refuted at $n=3$ (round 12-13). (e) Mass-Constraint
  refinements aimed at literally reaching $s\ge n-1$ — proved structurally
  incapable via the asymptotic argument (round 17); don't spend another
  round trying to sharpen the same counting object, a different
  invariant is needed (see opening 4 above).

- Small-case / intuition notes: (1) [conjecture] Sub-case (i)'s odd-excess
  outside-window region is very likely true — 145,546 targeted trials at
  $(k,e)=(2,1)$ under the cap found zero violations, and it is exactly
  the same "shape" as the already-proven even-excess and window cases,
  so the remaining work is plausibly a proof-writing gap, not a
  false-statement risk, though this has NOT been verified for odd
  $e\ge3$ with the same rigor as $e=1$ — a fresh round should not assume
  $e\ge3$ is safe without its own targeted sweep near $a_1=2^k$ first.
  (2) The two remaining gaps are NOT converging into one wall: gap 1 is
  a discrete integer-telescoping identity on the Liu-Bang (lower-bound)
  side with a hard cardinality cap; gap 2 is a continuous
  perturbation/LP-vertex classification on the Xiang-Yu (upper-bound)
  side with no cap at all. Round 14's "secretly the same unbounded
  combinatorial-growth wall" hypothesis was explicitly not adopted then
  and still does not hold up on inspection now — this round's check
  confirms round 13's and round 17's finding stands: two genuinely
  different obstructions, no plateau-break needed on this basis. (3)
  lp-duality-split-polytope's necessity direction specifically (not the
  approach as a whole, which still produces useful general lemmas like
  Even-Multiplicity Equality Criterion) should be treated as a stalled
  sub-target: recommend either a genuine change of counting mechanism
  (the double-counting/cyclic-sum idea above, worth one cheap try) or
  formally deprioritizing the $s\ge n-1$ necessity conjecture as this
  approach's headline target while keeping the file "light/secondary"
  exactly as CLAUDE.md's framing already has it — do not invest a full
  round refining Mass-Constraint further, that specific technique is
  provably tapped out.
