## imo-2026-03 — lens: the "all-cycles" D/M-completeness gap (lower-bound direction)

- **Distinct openings** (rival ways the outliner could attack this specific gap):
  1. **Pigeonhole "guaranteed untouched original" opening (new, not yet in the population).**
     In the tight regime relevant to the theorem (`m` cuts, `k=m+1` original pieces — the
     regime the Superincreasing No-Early-Zero Lemma actually needs promoted), every cut in a
     physical cut-forest traces back to exactly one root original piece of `A`, so the number
     of *distinct* originals touched by any genuine cut is `≤ m = k-1 < k`. Hence **at least
     one original piece of `A` is always left completely untouched** by any `≤m`-cut strategy.
     This is a cheap, rigorous, previously-unstated fact (I did not find it written anywhere in
     `dm-completeness-partial.md` or the approach files — they discuss untouched pieces
     case-by-case for small `m` but never state the general pigeonhole guarantee). It gives a
     structural resource (`≥1` always-available escape target) that any resolution of the
     all-cycles case should exploit — a cycle among the *touched* pieces still has to compete
     against configurations that route through the guaranteed-untouched piece.
  2. **"Multiple simultaneous global minimizers" opening (supported by direct computation
     below).** Instead of trying to prove *the* specific cyclic-tie minimizer configuration is
     itself peelable (Step 8.3–8.4's approach, which is where it's stuck), try to prove: whenever
     a cross-tie-cycle configuration attains the minimum value, **some other, differently-shaped,
     acyclic configuration attains the identical value** (existential, not universal, over
     minimizers) — or even, more radically, that the value `h(A,m)` is always attained by a
     *completely different* canonical D/M route (e.g. a simple greedy "subtract the two current
     largest" chain) that never needs to correspond to the same physical cut-forest at all. This
     is a strictly weaker (easier) target than full completeness and is directly supported by a
     computation below: an instance where a genuine 2-piece cross-tie configuration ties the
     global optimum, but the actual D/M witness reaching that same value uses a totally
     unrelated sequential-`M`-chain, not a "peeling" of that geometric configuration.
  3. **Piecewise-linear breakpoint / joint extreme-value argument (a sharper form of the
     existing Vertex-Lemma machinery, not yet applied at this level).** For the minimal
     "2-cycle" building block (two different, differently-valued original pieces `a1≠a2`, each
     cut once, with an untouched third piece `a3` present), I checked analytically and
     numerically (see below) that the *value* of the pure cross-tie sub-family
     `e(\{a_1-t,a_2-t,a_3\})` (`t1=t2=t`, Lemma P cancels the duplicate `t`'s) is a
     **piecewise-linear function of `t` alone**, whose minimum over the open interval is
     *always* attained either at a breakpoint (exactly where the sort order changes, i.e.
     exactly where `a_1-t=a_3` or `a_2-t=a_3` — a **tie to the untouched original**, breaking
     the cycle) or at a domain boundary (a degenerate/fewer-cut limit). So for this minimal
     building block, a genuinely *isolated, non-escapable* 2-cycle optimum cannot occur whenever
     an untouched third piece is present (which, by opening 1, is *always* the case in the tight
     regime for `k=3`). This is a real, checkable mini-lemma for the base case; generalizing it
     to longer cycles / more pieces (a joint multi-variable version of the Vertex Lemma's
     extreme-value argument) is exactly the open technical work, but the base case has a clean
     argument sketch nobody in the population has written down yet.
  4. **Confluence-style / adjacent-exchange framing (from the crux corpus, see below).** Reframe
     "does the choice of which tie to peel first change the reachable value" as a **local
     rewiring / exchange argument**: show any two "adjacent" tie choices in a cycle can be locally
     re-targeted (one of the two rerouted to an untouched original or to a bisection) without
     changing `e`, then induct on cycle length the way `aimo-0003`'s solution reduces "invariant
     under all orderings" to "invariant under one adjacent transposition." This is a genuinely
     different technique from the topological-peeling argument already in `dm-completeness-
     partial.md` and has not been tried by any approach in the population yet.

- **Candidate technique(s):** pigeonhole/counting (opening 1), an existential "alternate
  minimizer" argument in place of the universal "every minimizer is peelable" claim (opening 2),
  a joint (multi-variable) extreme-value/piecewise-linearity argument generalizing the already-
  certified Vertex Lemma (opening 3), and a local-exchange/confluence-style induction (opening 4,
  crux-inspired). All four are compatible with (build on top of) the already-certified Vertex
  Lemma, Lemma D/M, and Lemma P — none require new machinery, only a different combination of the
  existing certified lemmas.

- **Cheap-kill candidates:** the pigeonhole count (opening 1) is essentially free — `#touched
  originals ≤ m` is a one-line argument — and should be stated explicitly as a standing fact
  before any attempt to resolve the cycle case; it immediately rules out the naive worry that
  *every* original piece could be entangled in an inescapable cycle simultaneously (there's
  always at least one that provably isn't touched at all).

- **Knowledge-base entries to use:** "Invariant / monovariant" and "Pigeonhole / extremal"
  (`knowledge_base.md`, General Proof Methods section) — generic names for openings 1 and 3/4
  respectively. No KB entry specifically addresses confluence/rewriting-order-independence; that
  idea comes from the crux corpus (below), not the KB.

- **Analogous past problems (cruxes):**
  - **`aimo-0003`** (combinatorics, `invariants-and-monovariants`) — genuinely the best analog
    found. Problem: show a chord-count statistic is independent of the ordering used to run a
    greedy matching process. Crux moves: (a) *"Reduce an 'invariant under all orderings' claim to
    invariance under a single adjacent transposition, since adjacent transpositions generate the
    symmetric group"* — directly suggests opening 4 above (reduce "any tie-breaking order reaches
    the same reachable set" to a *local* 2-move exchange check); (b) a second crux in the same
    problem, *"encode a matching-count invariant as an extremal (min) value of a running ±1 tally,
    proved by induction that deletes an innermost matched pair"* — structurally close to the
    existing certified machinery (the `e` = alternating-sum tally, and the leaf-parent/innermost-
    pair peeling already used in `dm-completeness-partial.md` Step 8.3), so it corroborates that
    peeling-innermost-first is the right general technique, while (a) is the genuinely *new*
    idea not yet tried here.
  - No stick/segment-cutting-and-claiming crux was found in the corpus (searched both databases
    for "stick"/"segment"/"claim piece" — no hits); this problem's specific game structure has no
    direct precedent in the corpus. Only the abstract "order-independence" and "innermost-pair
    induction" techniques from `aimo-0003` transfer, not the problem content itself.

- **Prior progress:** `lemmas/dm-completeness-partial.md` (certified round 4) proves `g(A,m) =
  h(A,m)` unconditionally *except* when the joint global minimizer's tie-dependency graph (edges
  `c→c'` when cut `c` ties to a value produced by cut `c'`) is a nonempty union of directed
  cycles — the "all-cycles" case, precisely isolated but neither proved impossible nor exhibited.
  `lemmas/superincreasing-no-early-zero.md` (round 5) proves the D/M-sequence-restricted bound
  `h(D_m,m) ≥ e_m·S(D_m)` unconditionally for every `m`; promoting to the true physical bound
  `g(D_m,m) ≥ …` is blocked *only* by this same gap.

- **Dead ends (do not retry):** none newly identified this round for this specific gap. The
  existing "candidate potential `Φ`" search (`concavity-minimax-duality` §9–11, Candidates 1–2,
  `min(t,1)`, `min(t,2)`) is a *different*, independent route to the lower bound (avoiding
  D/M-completeness entirely) and its refutations are already correctly recorded — not duplicated
  here, and not a dead end *for this gap* since it was never attempting to resolve the all-cycles
  case in the first place.

- **Small-case / intuition notes (all labeled conjecture, backed by exact-`Fraction` computation,
  bounded search `m ≤ 3`):**
  - Reconstructed the minimal "2-cycle" building block concretely: two *different* original
    pieces `a1≠a2` (not duplicates — ruled out the naive duplicate-pair construction, e.g.
    `A=(5,3)`, since bisecting duplicate/near-duplicate pieces is itself a `D`-move that reduces
    to deleting the piece for free by Lemma P, so a naive "cut two equal pieces identically"
    example is *degenerate*, not a genuine cycle — the true bisect-to-zero strategy dominates it,
    e.g. for `A=(5,3),m=2`: bisecting both gives `e=0`, strictly beating the cross-tie value `2`).
  - Built a genuine (non-degenerate) candidate: `a1≠a2`, one cut each, tying at a common value
    `t=t1=t2` (Lemma P cancels the duplicate `t`'s), third piece `a3` present and untouched.
    Checked by exact-fraction search over **8 random integer triples** `(a1,a2,a3)`,
    `m=2` (the tight `k=m+1` regime): in every trial the *shape-restricted* pure-cross-tie value
    sometimes *is* the best value achievable within its own 1-cut-per-piece pairing family (e.g.
    `A=(21,13,9)`: cross-tie at `t=12` gives `e=1`, matching two different pairings simultaneously),
    but the **global minimum over all shapes always exactly equals the D/M-BFS value `h`** (zero
    mismatches in 8/8 trials) — e.g. for `A=(21,13,9),m=2`: `g=h=1` in all cases, verified exactly.
  - **Key finding:** for `A=(21,13,9)`, traced the actual D/M-BFS witness achieving `e=1` and it
    is `M(21,13)=8` then `M(9,8)=1` — a **completely different combinatorial route** (a simple
    sequential subtract-chain) from the "cut `a1` at `12`, cut `a2` at `12`" cross-tie physical
    configuration that *also* achieves `e=1` continuously. This is concrete evidence (conjecture,
    one instance) for opening 2: even where a cross-tie configuration ties the optimum, a D/M
    sequence reaches the same value via an unrelated mechanism, not by "realizing" that specific
    minimizer.
  - Extended the check to `k=4,m=3` (tight regime for the next size up) with 4 random integer
    quadruples via a randomized physical-cut search (float, 60k trials/instance, cross-ties
    included as an explicit move) against the exact D/M-BFS value: all 4 matched (`h=0,1,1,1`
    vs. `g≈0.0000,1.0000,1.0000,1.0000`) — weaker (non-exact, non-exhaustive) evidence but
    consistent with `g=h` continuing to hold, no violation found.
  - **Conjecture, not proved:** the all-cycles obstruction is likely *vacuous in practice* for
    every `A,m` (matches the "never observed to occur" honest status already recorded), and the
    most promising resolution mechanism is the *existential* one (opening 2 / breakpoint argument
    of opening 3), not a universal "every minimizer peels" argument — the latter is what Steps
    8.3–8.4 already tried and got stuck on, and 3+ rounds of the population sitting on that same
    formulation is itself a signal (per CLAUDE.md) to route around it with a genuinely different
    top-level target for this sub-gap, not a variation of the same peeling technique.

- **Which approaches own this gap:** `concavity-minimax-duality` owns `dm-completeness-partial.md`
  (its own §8, certified) and is the natural home for closing this gap directly. `dyadic-cascade-
  induction` is the approach that *needs* this gap closed to promote its (fully proved,
  unconditional) D/M-sequence lower bound to the true physical theorem — it should not re-attempt
  the completeness proof itself (that's `concavity-minimax-duality`'s certified lemma to extend),
  but could independently sanity-check any proposed resolution against `D_m` specifically.
  `potential-weighting-upper-bound` is upper-bound-direction only and does not own this gap.
  `elementary-exchange-smoothing` is formally retired (round 4) — do not dispatch to it.
