## imo-2026-03

### Part A — `layer-cake-parity-reframing`: revive or deprioritize?

**Verdict: formally deprioritize (do not rebuild further as a standalone
approach), but keep its 4 certified lemmas as reusable tools.** Reasoning:

1. Its unique content is (a) the layer-cake identity `AltSum(X) =
   ∫1[N_X(t) odd]dt`, (b) per-piece additivity of `N`, (c) the resulting
   exact equivalence `T(n) ⟺ AltSum(refinement) ≥ 1/D`, and (d) a proved
   Coupling Obstruction killing "independent per-cut budget" as the closing
   mechanism.
2. I checked whether (a)-(c) genuinely diversify the field or duplicate
   existing content. They duplicate: `self-similar-induction-on-n` round 4
   independently proved the **identical** `T(n) ⟺ AltSum ≥ 1` reduction
   (its "Lemma AS", see `approaches/self-similar-induction-on-n.md` line
   ~492-519 — same two-line `(∗)`-style derivation from `OddSum+EvenSum=sum`,
   just without going through the threshold-integral detour). Worse,
   `self-similar-induction-on-n` then built a **strictly more general** tool
   on top of the same reduction — the **Single-Insertion Lemma**, an exact
   formula for `AltSum`'s change under inserting *any* single value at *any*
   sorted position (not just bisecting a whole piece into two, which is all
   Lemma 3 here handles), verified on 2000+ random instances. That lemma has
   since been the actual engine behind this round's biggest wins on the
   lower bound (Theorem 2 closing Case-B(m,k) to a width-1 sliver). So
   layer-cake's threshold/integral machinery adds an elegant alternative
   *derivation* of the same reduction but no additional *power* over what is
   already being exploited successfully elsewhere.
3. The Coupling Obstruction is a genuine, correctly-proved negative result
   (verified: `+2/15` alone vs `-2/15` after bisecting `p1`, exact rational
   arithmetic, independently reproduced by round-4's reviewer) — but it
   rules out exactly the class of argument ("independent per-cut,
   piece-local bound") that `self-similar-induction-on-n`'s Single-Insertion
   Lemma also does NOT rely on (it tracks each insertion's *exact* signed
   effect relative to the current running sequence, i.e. already a joint,
   order-dependent computation, not a piece-local bound). So the obstruction
   does not actually block the approach that has continued making progress;
   it blocks a strategy nobody live is using anyway.
4. The file's own "what remains open" options — (a) bound the total signed
   effect jointly via a potential/telescoping argument over the threshold
   continuum, or (b) restrict to configurations where sign is determined —
   are, in substance, the *same idea* as what self-similar-induction-on-n's
   ongoing peel-from-tail / trichotomy work is already doing in discrete
   (insertion-sequence) language, just re-expressed in continuous
   (threshold-integral) language. There is no indication the continuous
   reformulation is easier to push through; if anything it has sat idle
   since round 4 with zero further movement while the discrete version has
   closed real ground every round since.

**Recommendation to outliner:** mark `layer-cake-parity-reframing` as
`held/not rebuilt this round` again (do not open a 6th builder slot on it).
Its 4 lemmas stay certified and citable (`layer-cake-identity-and-coupling-
obstruction.md`) — in particular Lemma 1 (layer-cake identity) is a clean,
fully general, reusable fact any future approach could cite for free if a
genuinely new use for the threshold/measure viewpoint appears (e.g. if the
"large gaps everywhere" upper-bound gap turns out to need a measure-theoretic
argument specifically). But do not spend a round re-deriving what
self-similar-induction-on-n already has in strictly stronger form. If it
stays untouched 2+ more rounds with no new lead, treat as formally retired
(not deleted — kept as a certified-lemma source only).

### Part B — is there a genuinely fresh 6th top-level framing?

I searched the crux corpus broadly (games-and-strategy [39],
probabilistic-method [4 in combinatorics], generating-functions [12],
inequalities-SOS-and-convexity, extremal-principle [166]) plus keyword
matches (`rearrangement`, `majorization`, `entropy`, `exchange`, `minimax`,
`root of unity`) across combinatorics+algebra. Findings:

- **`probabilistic-method`/entropy**: only 4 combinatorics hits, none
  resemble an alternating-claim / sorted-rank-sum game. No genuine analogue
  found. An entropy argument doesn't have an obvious foothold here — the
  target `c(n)` is a sharp rational extremal value with an exact equality
  case (LB's geometric partition), which is characteristic of an
  exchange/exact-construction problem, not the kind of problem where entropy
  methods (used for counting/existence bounds, not tight extremal values
  with matching equality) typically apply. **Not recommended.**
- **`generating-functions`/roots-of-unity**: 12 hits, all number-theoretic
  or counting-mod-structure (divisibility of cyclotomic polynomials at roots
  of unity, vanishing-sum arguments for counting). None involve a
  sorted-rank alternating sum or a claiming game. A roots-of-unity filter
  naturally detects "count things ≡ r (mod m)" problems; `OddSum` here is
  parity of *rank*, not of an algebraic residue, so there is no natural
  generating-function object whose coefficients encode this sum (the
  layer-cake framing tested in Part A is the closest thing to this, and is
  already shown not to add power). **Not recommended as a genuinely new
  route** — it would just re-derive the AltSum reduction again.
- **`games-and-strategy`** (39 hits, listed exhaustively above): most are
  discrete combinatorial games (pairing/mirroring strategies, invariant/
  parity arguments, Nim-like valuation games) on graphs or boards, not
  continuous "split a budget then take turns claiming" games. `aimo-0560`
  (surrogate adversary — replace the opponent with a strictly stronger
  surrogate whose reply is pointwise at least as damaging) was already
  flagged in round 2 as the single closest analogue in this subtopic; it
  remains the best game-theoretic crux match but is not a *new* framing —
  it's a proof *technique* (strengthen the adversary, argue against the
  surrogate) that could in principle be tried within the existing
  multiset-minimax reduction (e.g. as a new tool for `universal-halving-
  adversary` or `lp-duality-split-polytope`'s open gap), not a top-level
  reframing away from the reduction. No hit among the 39 resembles a
  sorted-rank claiming game closely enough to lift a full top-level
  strategy from.
- **The one genuinely promising lead**: `aimo-0287` (algebra,
  `double-counting` subtopic, IMO-style: choose `X` minimizing
  `|1 − Σ_{i∈X} a_i|` over a strictly increasing sequence). Its crux move
  is a **majorization/domination partial order** on subsets: define
  `X ⪯ Y` iff `|X ∩ [i,n]| ≤ |Y ∩ [i,n]|` for every suffix `[i,n]`
  (equivalently, a value-dominating injection), which implies
  `Σ_X a ≤ Σ_Y a` for *any* increasing sequence `a`. The proof then argues
  by contradiction: if the optimal `X` were comparable to its complement
  `X^c` under `⪯`, exhibit an *intermediate* set `Y` strictly between them
  (`Σ_X a < Σ_Y a < Σ_{X^c} a`), contradicting minimality; incomparability
  then forces a structural (adjacent-straddling-pair / boundary-exchange)
  characterization of `X`.
  - **Why this is a genuinely different top-level target for imo-2026-03's
    stuck upper-bound gap**, not just a variant of existing framings: all 6
    current approaches attack "does some specific construction/allocation
    beat `c(n)`" via case analysis, potential functions, or vertex/LP
    characterizations of the *specific* worst point. The majorization-order
    idea instead asks: can the space of possible refinement-multisets
    `M` (for a fixed LB partition) be given a partial order `⪯` such that
    (i) `M ⪯ M'` implies `OddSum(M) ≤ OddSum(M')` (a monotonicity lemma,
    analogous to `Σ_X a ≤ Σ_Y a`), and (ii) XY's true optimal response is
    forced, by an incomparability/exchange argument, into a specific small
    family of `⪯`-extremal configurations — collapsing the "balanced,
    large-gaps-everywhere" open sub-case to a few explicitly checkable
    cases rather than an unbounded continuum. This is close in spirit to
    the existing Vertex Pinning Lemma (`dyadic-potential-invariant`) and
    Single-Piece-Split Vertex Lemma (`lp-duality-split-polytope`), which
    also reduce to finite characterizations of the optimum — but those are
    LP-vertex/active-constraint arguments (linear-programming machinery),
    whereas this is a combinatorial rank-domination order with an explicit
    exchange/contradiction argument, a different proof *mechanism* even if
    the target (characterize XY's optimum) rhymes with existing gaps.
  - **Caveat, honestly**: I did not verify a monotonicity lemma of form
    "`M ⪯ M'` (suffix-domination) implies `OddSum(M) ≤ OddSum(M')`" actually
    holds for the specific setting here — `OddSum` is a *fixed*-parity-of-
    rank sum on the whole multiset (not a subset-sum over a chosen index
    set `X`), so the analogy is structural, not a direct transplant; this
    needs its own from-scratch check before an outliner commits to it as a
    7th approach. Flagging it as a **lead worth a light numeric check next
    round**, not a validated new framing.
- **rearrangement inequality direct on the minimax** (as suggested in the
  dispatch): `aimo-0459`'s crux (sort variables, re-pair extreme-with-extreme
  via rearrangement inequality) is a genuinely different technique in
  spirit, but on inspection it doesn't transplant: rearrangement inequality
  bounds a *bilinear pairing* `Σ x_i y_{σ(i)}` over a permutation `σ`, and
  our target `OddSum` is not naturally a bilinear pairing of two sequences —
  it's a fixed alternating selection (odd ranks) of a *single* sorted
  sequence with no second sequence to permute against. **No natural
  transplant found**; not recommended as a route, despite superficial
  "sorting" resemblance.
- **`aimo-0182`** (variance/random-permutation spread bound,
  `symmetric-functions-and-substitution`) is the probabilistic-method-
  adjacent hit closest to a rank-sum problem, but it bounds
  `max_σ − min_σ` of a bilinear form via mean/variance under a **uniformly
  random permutation** of a fixed pair of sequences — again a genuinely
  different object (two sequences paired by a permutation) from our single
  sorted multiset with fixed odd/even rank selection. I do not see how to
  adapt it: our problem has no natural "randomize over permutations" step
  since XY's choice is adversarial/optimized, not averaged, and the target
  is a min (not a spread). **Not recommended.**

**Overall assessment on Part B**: after a genuinely broad corpus sweep
(games-and-strategy, probabilistic-method, generating-functions,
inequalities/rearrangement, majorization/double-counting), I did **not**
find a top-level framing that avoids the AltSum/multiset-minimax reduction
(consistent with round 2's finding that the reduction is forced by the
literal payoff rule, not a technique choice — this remains true; nothing in
this round's search contradicts it). What I did find is one candidate proof
*mechanism* genuinely distinct from the LP-vertex / potential-function /
peel-induction mechanisms already in the field: the majorization/suffix-
domination partial order + incomparability-exchange argument from
`aimo-0287`, worth a light numeric feasibility check next round as a 7th
approach or as new machinery inside an existing one (most naturally
`dyadic-potential-invariant` or `lp-duality-split-polytope`, both already
working on finite-characterization-of-the-optimum arguments for the same
"balanced, large gaps everywhere" gap).

## Summary for outliner

- **Distinct openings this round:** (1) formally deprioritize
  `layer-cake-parity-reframing` — subsumed by `self-similar-induction-on-n`'s
  Lemma AS + Single-Insertion Lemma, which is strictly more general and
  already productive; its Coupling Obstruction blocks a mechanism nobody
  live is using. (2) A new candidate mechanism (not yet a full approach) —
  majorization/suffix-domination partial order + incomparability-exchange
  argument, from crux `aimo-0287` — for the stuck upper-bound "large gaps
  everywhere" balanced-region gap; needs a from-scratch monotonicity-lemma
  check before committing an approach slot to it.
- **Candidate technique(s):** majorization order + boundary-exchange
  argument (aimo-0287-style), as a new tool for the upper-bound gap; no
  viable entropy/generating-function/rearrangement-inequality/pure
  probabilistic route found despite a deliberately broad search.
- **Cheap-kill candidates:** before building a majorization-order approach,
  cheaply test the needed monotonicity lemma ("more spread-out /
  suffix-dominant refinement ⟹ larger OddSum") on random multisets — if it
  fails outright (likely, since OddSum's rank-parity dependence is not
  obviously monotone under suffix-domination the way a plain subset-sum is),
  this mechanism is dead before any proof effort is spent.
- **Knowledge-base entries to use:** none new found specific to
  majorization/entropy/generating-functions for this problem (`grep` for
  those terms in `knowledge_base.md` returned nothing); the relevant
  existing KB entries remain those already in use by the live approaches
  (Invariants & monovariants; general proof-method entries under `General
  Proof Methods`).
- **Analogous past problems (cruxes):** `aimo-0287` (algebra,
  double-counting/majorization — best genuinely-new-mechanism lead, needs
  verification before adoption); `aimo-0560` (combinatorics,
  games-and-strategy — surrogate-adversary technique, previously flagged
  round 2, still the closest game-theoretic analogue but a technique not a
  new top-level framing); `aimo-0459` and `aimo-0182` considered and
  rejected as non-transplantable (bilinear-pairing / permutation-variance
  structure absent from our single-sequence rank-parity target).
- **Prior progress:** see `results/imo-2026-03/current.md` — reduction to
  multiset-minimax fully proved; conjectured closed form
  `c(n)=2^n/(2^{n+1}-1)`; lower bound and upper bound each have one
  precisely-narrowed remaining gap (see current.md's "Open" section, round
  5 state, unchanged as of this report since I did not touch those gaps
  directly this round).
- **Dead ends (do not retry):** `layer-cake-parity-reframing`'s
  "independent per-cut, piece-local bound" mechanism for closing `T(n)`,
  `n≥3` (Coupling Obstruction, proved round 4, re-confirmed still valid and
  still blocking only that one mechanism here) — do not attempt to revive
  this specific mechanism even inside a different approach. Rearrangement-
  inequality-on-bilinear-pairing and permutation-variance approaches (this
  round, ruled out by structural mismatch, not by counterexample — no
  bilinear pairing/permutation object exists in this problem to apply them
  to).
- **Small-case / intuition notes (conjecture only):** none new computed
  this round beyond what's already certified; I focused compute time on
  corpus retrieval/matching rather than re-deriving already-certified small
  cases, per the "don't repeat dead ends / already-certified work" rule.
