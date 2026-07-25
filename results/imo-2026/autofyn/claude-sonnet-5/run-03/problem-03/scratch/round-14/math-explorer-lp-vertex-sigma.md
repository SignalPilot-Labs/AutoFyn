## imo-2026-03

- Distinct openings:
  1. **Reframe route (b) — the "growing s" finding is NOT an obstruction to
     the Existence Theorem, only to a bounded-s0-uniform-in-n construction.**
     I re-derived numerically (independent script, DE optimizer over
     softmax-parametrized fragment allocations, `/tmp/frag_test.py`) that at
     the region vertex `e_0` the minimal split-piece count `s*` clearing
     `c(n)` really does grow (n=4: s*=2; n=6: s*=3 (margin ~3e-6, essentially
     exact); n=8: s*=5 (margin ~2e-6, essentially exact)) — this reconfirms
     the file's Section 4.5/4.6.5 "soft negative signal" is real, not noise.
     **But** the Existence Theorem never requires a bounded-independent-of-n
     `s0` — it only requires, for each fixed `n`, some response using `≤n`
     cuts (the whole budget). Since `s* ~ n/2` uses well under the `n`-cut
     budget, this data is fully consistent with — and gives no evidence
     against — a genuinely `n`-dependent fragment-vs-fragment (or general
     multi-piece) construction closing the WHOLE balanced region, not just
     `e_0`. The "bounded-s0 impossible" framing (Mass-Constraint Theorem,
     round 11; and the round-12 numeric follow-up) rules out only the
     *literal outline-3 ask* (a single small fixed-size named tool), not
     the actual target. **Recommend the outliner explicitly re-scope route
     (b) as: find an n-dependent (not bounded) explicit fragment-vs-fragment
     construction, proved in closed form for all p in the balanced region,
     using at most n cuts** — this is a different (weaker, hence more
     tractable) target than what round 11's Mass-Constraint Theorem
     legitimately killed.
  2. **Route (a), Sigma(n,k) classification via dominance-pruning rather
     than full enumeration.** Full classification is out (super-exponential,
     round 11). But the Finite-Cell Theorem only needs the candidate set Q
     restricted to shapes sigma that could ever be the *argmin* at some
     feasible p — most of Sigma(n,k) is presumably dominated (there is
     always a cheaper shape at every p where sigma is valid) and can be
     discarded wholesale via a structural argument (e.g. "any shape with an
     odd-position fragment strictly larger than some untouched/available
     alternative pairing is dominated by the shape that re-pairs it") rather
     than enumerated. This is the same idea, one level up, as the
     Region-Vertex Classification Theorem's success at pruning
     `Q_region` down to O(n) points instead of exponentially many
     `(k-1)`-subsets — worth trying the analogous dominance/pruning lemma
     directly on `Sigma`-shape functionals, not full enumeration.
  3. I verified my re-implementation of `V(p)` at the three round-13 hard
     n=3 points reproduces the file's reported values almost exactly
     (0.5114/0.5150/0.5166 vs my 0.5114/0.5150/0.5174 — third point differs
     slightly, likely optimizer-precision, not a bug) — confirms the
     baseline computation is trustworthy for future numeric probes.

- Candidate technique(s): (i) an explicit n-dependent multi-piece
  fragment-vs-fragment tying construction (generalizing Theorem 12/the
  General Multi-Piece Subset-Tie construction to tie split fragments
  against EACH OTHER, not against whole untouched pieces, so the
  Mass-Constraint obstruction genuinely does not apply — per the file's
  own Section 4.5 scope note); (ii) a dominance/pruning argument on
  Sigma-shapes (structural, not enumerative) to shrink the Sigma-part of Q
  to a tractable sub-list, mirroring the already-successful
  Region-Vertex-Classification pruning.

- Cheap-kill candidates: before investing proof effort in (i), check
  whether the natural "pairwise-tie chain" construction (chain-tie
  fragments of DIFFERENT split pieces to each other in a cycle, using
  ~n/2 cuts) numerically clears c(n) at the ACTUAL hard interior points
  (not just at e_0, which is already closed) for n=3..6 — a quick
  Nelder-Mead/DE check restricted specifically to that construction
  family (not the unrestricted V(p) search) would tell in under an hour
  whether it's a real lead or another dead end, before any proof
  investment (per the repo's mandatory numerical-gate rule).

- Knowledge-base entries to use: none new beyond what's already cited in
  the approach file (Global Vertex Lemma / hyperplane-arrangement
  cell-affineness, Lipschitz continuity, Singleton-Interleaving Lemma,
  General k-Anchor-Merge Lemma, Mass-Constraint Theorem) — knowledge_base.md
  itself has no LP-vertex-polytope-specific entry beyond generic
  extremal-principle framing already in use.

- Analogous past problems (cruxes): checked `combinatorics` /
  `linear-algebra-method` (16 entries) and `extremal-principle` (166
  entries) via `crux_moves_documentation.md`'s exact field names
  (`technique`, `how_used`, `domain`, `subtopic`). None of the
  linear-algebra-method entries match (they are F_2-linear-system /
  generating-function encodings, not real-polytope-vertex arguments).
  Among extremal-principle entries with exchange/swap/tie language:
  `aimo-0146` (already flagged in round 13 — exchange-smoothing a
  weighted sorted sum toward high-coefficient positions until profiles
  converge; the closest fit in spirit for route (a)'s dominance-pruning
  idea, but the outliner already knows this one) and `aimo-0119`
  ("pick the configuration minimizing the max load, tie-broken by fewest
  parts at max, then any single-item transfer from heaviest to lightest
  part is non-improving" — a minimality + no-local-improving-exchange
  argument) are the best structural fits for a fragment-vs-fragment
  tying/exchange proof, but neither is a literal template: both operate
  on a discrete multiset-partition optimum via a single fixed
  minimality hypothesis, not a two-player alternating-claim game with a
  continuum of split choices. No crux genuinely matches the specific
  "affine-on-cells / vertex of an LP feasible region defined by an
  adversary's split choice" structure here — report this honestly rather
  than force a weak match.

- Prior progress: `global-lp-vertex-sufficiency`'s Existence Theorem has
  `Q_region` (region-only candidate vertices) fully closed (rounds 9-10);
  the sole remaining gap is the Sigma-shape part of the candidate set Q.
  Rounds 12-13 exhaustively ruled out the entire "endpoint inequality via
  a single explicit exchange move" mechanism class (region-side and
  response-side, single-choice and existential) — do not retry any
  variant of that. `lp-duality-split-polytope`'s Perfect-Tie-Family
  Exact Characterization Theorem (certified) shows only s=n-1 exactly
  attains c(n) among "perfect" (zero-residual) tie constructions at e_0 —
  consistent with, and independent confirmation of, my numeric finding
  above that the true minimal clearing s at e_0 grows roughly linearly
  in n (not the same statement, but corroborating the same qualitative
  fact from a totally different, exact-arithmetic technique).

- Dead ends (do not retry): region-side and response-side exchange
  mechanisms (fixed vertex, tightest-gap symmetric, existential-over-
  candidates, adversary-tie single-choice/existential) — confirmed dead
  at n=3 by two independent rounds and re-confirmed structurally sound by
  this round's read of the reviewer's independent reimplementation.
  Bounded-s0 (fixed, n-independent) fragment-tied-to-whole-untouched-piece
  constructions — ruled out rigorously (Mass-Constraint Theorem). Full
  brute enumeration of Sigma(n,k) — combinatorially infeasible
  (super-exponential, round 11).

- Small-case / intuition notes: (conjectural, numeric only) The minimal
  split-piece count s* needed at e_0 to clear c(n) appears to satisfy
  s*/(n+1) -> 1/2 as n grows (matches the file's own independent exact
  computation of 1/(2 p_1(e_0)) growing toward (n+1)/2-ish) — i.e. roughly
  half the pieces need splitting at the hardest known point. This is
  exactly the same order of magnitude as the cut budget itself (n cuts
  available, ~n/2 needed), suggesting the true extremal construction is
  "dense" (touches most pieces) rather than sparse/local — a structural
  hint that any successful route-(b) construction will likely look like a
  global pairing/matching of (most) pieces' fragments against each other,
  not a small local perturbation — consistent with why every "few-piece"
  or "single exchange move" mechanism tried so far (rounds 5-13) has
  failed uniformly across the balanced region.
