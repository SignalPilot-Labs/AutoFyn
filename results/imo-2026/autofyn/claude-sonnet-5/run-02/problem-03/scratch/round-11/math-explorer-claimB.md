## imo-2026-03 (lens: Claim (B), ℓ(F)=1 restricted — the three round-10 open items)

- Distinct openings:
  1. **Consolidate branch-by-branch closure into one clean strong induction.**
     Direct inspection of the proofs (not just the summary) shows the three
     "still open" items are not independent obstacles — they are literally
     the *same* statement recurring at a smaller n:
     - The `v<s` complement of Proposition 24 fails at exactly the step
       "`[0,v) contains all of u_{R'}'s support`" (needs `v>=s`); when
       `v<s` this becomes a *partial*-integral bound `∫_0^v u_{R'}` against
       a refinement of the (n-2)-ladder — structurally the identical
       "`v<p_2`" problem, one level down, with the (n-2)-ladder playing the
       role of the n-ladder and `v` playing the role of the original
       residual. (Confirmed by direct derivation: the algebra up to
       `A(F∪G')=p_2-v+A(R')` is unaffected by `v` vs `s`; only the
       "`∫_0^v u_{R'}=A(R')`" step needs `v>=s`.)
     - Proposition 25's uncovered branch `w'<p_3` is, by the identical
       substitution used inside its own proof (`Q=τ/r` is the (n-1)-ladder,
       `w=w'/r`, `q_2=p_3/r`), *exactly* Proposition 24's `v<p_2` problem
       posed one level up (at n-1 instead of n-2).
     - The other uncovered branch of Proposition 25 (`p_3` itself cut by
       `G'`) is, by the same reasoning, the `p_2`-cut-complement problem
       (Proposition 25's own target) recursed one level down.
     This is not a new observation in isolation (round 10's own writeup and
     memory rule #15 already flag "self-similar one level down" for Prop 22)
     but it has not yet been exploited structurally: instead of proving each
     branch as its own proposition with its own induction hypothesis
     `(⋆_{n-2})`, the outliner should set up **one** strong induction on `n`
     whose inductive hypothesis is the *entire* restricted Claim (B) for
     `ℓ(F)=1` (not just Claim A) at every level `<n`, and prove the
     inductive step by casing on `v` vs `p_2`, then (in the `v<p_2` branch)
     recursively invoking the *same* IH one level down rather than deriving
     a fresh proposition. Concretely: define the strengthened statement
     `P(n)`: "for every legal `F` with `ℓ(F)=1` and every legal tail
     refinement `G'`, `A(F∪G')>=f(n)`" and prove `P(n)` assuming `P(n-1)`
     and `P(n-2)` (both needed, since the two recursion depths appear:
     `p_2`-untouched branches drop 2 levels, `p_2`-cut branches drop 1
     level via the rescaled-(n-1)-ladder substitution). This turns three
     separately-chased sub-propositions into one induction with two
     recursive calls — a genuine reduction in bookkeeping, and crucially it
     removes the open-ended "keep finding new branches" pattern (every
     branch found so far is provably an instance of `P(n-1)` or `P(n-2)`,
     so once the induction is set up correctly there should be no more
     branches to discover, only the base cases `n<=4` to nail down exactly
     as Proposition 22/24 already do unconditionally).
  2. **Attack the partial-integral sub-problem directly via a clipped
     multiset reduction**, as an alternative/complementary route to (1):
     for `v<s` (or `w'<p_3`), the obstruction is bounding
     `∫_0^v u_{R'}(x)dx` where `R'` refines a smaller ladder. Note
     `∫_0^v u_{R'}(x)dx = A(\mathrm{clip}_v(R'))` where `clip_v` replaces
     every fragment `>=v` by the literal value `v` (elements `<v` are
     untouched, since `N_{clip}(x)=N_{R'}(x)` for `x<v` and `=0` for `x>=v`,
     matching Lemma 2's integral exactly on `[0,v)` and vanishing on
     `[v,∞)`). This turns the partial integral into a *full* `A`-value of a
     modified (but no longer literally a legal-refinement) multiset, to
     which `dominant-element-removal-identity` / `sharp-dominant-removal-
     identity` might apply directly if the clipped value `v` dominates the
     rest — worth checking as a shortcut that avoids explicitly invoking
     the recursive IH at all in some sub-cases. This is a genuinely
     different (non-recursive) mechanism from opening (1) and should be
     tried in parallel, not instead of it.
  3. **ℓ(F)>=2**: the "merge two residuals" exchange move correctly failed
     (not mass-preserving) per round 10. A different framing worth trying:
     directly generalize Propositions 20/24/25's machinery from a single
     threshold to a *window*. For `ℓ(F)=2` with residuals `v_1>v_2`,
     `u_F(x)=1[v_2<=x<v_1]` (already derived in the round-10 writeup's
     Sub-target-3 section via the generalized leftover formula), so
     `cross-term-identity-threshold` gives
     `A(F∪G') = (v_1-v_2) + A(G') - 2∫_{v_2}^{v_1} v_{G'}(x)dx`.
     This windowed integral is exactly the same shape `half-window-
     vanishing-lemma` / Safe-Window already handle for a *single* boundary
     (`∫_0^{p_2}`); the fresh content needed is bounding a window
     `[v_2,v_1)` instead of `[0,v_1)` — i.e. subtract off the `[0,v_2)`
     part, `∫_{v_2}^{v_1}v_{G'} = ∫_0^{v_1}v_{G'} - ∫_0^{v_2}v_{G'}`, and
     each piece is *already* the exact object Propositions 20/24/25 bound
     (a single-threshold integral against `v_{G'}` at thresholds `v_1,v_2`
     respectively). This suggests `ℓ(F)=2` may close as a **direct corollary
     of the already-proved `ℓ(F)=1` machinery applied twice and subtracted**,
     rather than needing its own new lemma or an exchange/collapse
     argument — a genuinely more promising route than the round-10 attempt
     (which tried an illegal literal "merge" move) since it works entirely
     within the existing threshold-based toolkit. Worth a full attempt next
     round rather than another numeric-only check.

- Candidate technique(s): strong induction on `n` unifying Claim (B)'s
  `ℓ(F)=1` sub-branches into a single two-step recursive hypothesis
  (opening 1); "clip-at-threshold" reduction of a partial integral to a
  full `A`-value, enabling direct reuse of `dominant-element-removal-
  identity`/`sharp-dominant-removal-identity` without explicit induction
  (opening 2); window-difference decomposition of a length-2 odd-run
  indicator into two single-threshold integrals, reducing `ℓ(F)=2` to two
  applications of the already-certified `ℓ(F)=1` toolkit (opening 3).

- Cheap-kill candidates: before any heavy proof effort, check by exact
  computation whether the "clip" reduction in opening 2 actually preserves
  dominance (i.e. whether `v` [or `w'`] genuinely dominates
  `Total(clip_v(R'))` at the relevant thresholds for small `n`) — a 10-line
  exact-`Fraction` script, cheaper than developing the full lemma; if
  dominance fails even numerically, opening 2 is dead and only opening 1
  (recursive consolidation) is viable. Similarly, for opening 3, numerically
  verify the window-difference identity itself (`∫_{v_2}^{v_1}v_{G'} =
  ∫_0^{v_1}v_{G'}-∫_0^{v_2}v_{G'}`, which is just linearity of the integral
  and should hold trivially — but verify the two single-threshold integrals
  really do match Propositions 20/24/25's exact closed forms when `v_1,v_2`
  land in different regimes, e.g. `v_1>=p_2>v_2`, mixed-regime cases are
  the real risk).

- Knowledge-base entries to use: no separate `knowledge_base.md` generic
  entry beyond what's already cited throughout this approach (the project's
  own accumulated lemma library is the operative toolkit at this point,
  not fresh knowledge-base retrieval — this matches every prior round's
  finding that the KB has no strong game-theoretic analog for this specific
  problem). The load-bearing already-certified lemmas most relevant to these
  three openings: `cross-term-identity-threshold`, `safe-window-lemma`,
  `single-residual-indicator`/`single-residual-exact-peel-identity`
  (Lemma 19/Prop 20), `general-ladder-dominance` (Lemma 23),
  `level-2-dominance-identity` (Lemma 24), `tail-self-similarity`,
  `dominant-element-removal-identity`, `sharp-dominant-removal-identity`,
  `odd-run-reduction-lemma` (needed for the `ℓ(F)=2` indicator formula).

- Analogous past problems (cruxes): filtered `combinatorics` domain,
  subtopics `extremal-principle`, `induction-and-construction`,
  `size-bounding-and-descent`, `sequences-and-recurrences`,
  `inequalities-SOS-and-convexity`, `games-and-strategy`,
  `processes-and-algorithms` (497 candidates), keyword-filtered for
  self-similar/recursive/geometric-doubling framings (45 hits). Best
  matches, genuinely analogous in *structure* (not just domain):
  - `aimo-0439` — "when a forced boundary edge's isosceles menu contains
    only the two 'ear' triangles, each ear removes one vertex and fuses its
    two incident edges into a single next-scale edge; iterate to reduce the
    instance to the same problem on the alternate-vertex sub-polygon." The
    crux move here is exactly opening (1)'s shape: recognizing that a
    "new" sub-case is *literally* the same problem at a smaller scale, and
    setting up the induction to consume that fact directly rather than
    treating each iterate as a fresh case. Adapt the *shape* of this move
    (fold the recursive self-similarity into the induction's structure,
    not into a chain of separately-proved propositions), not any
    domain-specific content (this crux is about polygon dissection, no
    numeric content transfers).
  - `aimo-0560` — "replace the adversary with a strictly stronger surrogate
    whose reply is pointwise at least as damaging, so a win against the
    surrogate transfers down and the reply collapses to a finite per-region
    menu." Weakly relevant to the ℓ(F)>=2 numeric-only finding (round 10's
    coordinate-descent search converges toward the already-characterized
    cascading/rescaled-ladder boundary family) — if a *pointwise-dominance*
    argument could show every `ℓ(F)>=2` response is weakly dominated by
    some already-analyzed `ℓ(F)<=1` or cascading-family response, this
    crux's "surrogate adversary" framing is the right vocabulary — but this
    is speculative, no direct technical transfer found, and round 10 already
    tried the closest natural version (residual-merging) and it failed to
    even be a legal move. Flag only as a framing hint, not a ready-to-use
    lemma.
  - No true analog found for the specific partial-threshold-integral /
    superincreasing-ladder-recursion obstruction itself (opening 2) — this
    remains, as every prior round has found, a from-scratch combinatorial
    fact about this specific superincreasing sequence, not something the
    corpus has solved before in this form.

- Prior progress: Proposition 25 closes `w'>=p_3, p_3`-untouched
  unconditionally; Proposition 24 closes `v∈[s,p_2)`, `p_2`-untouched,
  conditional on `(⋆_{n-2})` / unconditional for `n<=4`; both certified.
  `ℓ(F)=0` (fully-paired) and `ℓ(F)=1, v>=p_2` are fully closed
  (`cross-term-vanishing-lemma`, Proposition 20-22 modulo the same
  `n<=4`-unconditional / general-conditional caveat). See
  `results/imo-2026-03/lemmas/` for the full certified list.

- Dead ends (do not retry): the literal "merge the two largest residuals
  into one fragment of size `v_1-v_2`" exchange move for an `ℓ(F)-Collapse
  Lemma` — confirmed round 10 to not even be mass-preserving, hence not a
  legal Xiang-Yu move under any framing; do not resurrect this exact merge
  operation. (The window-difference idea in opening 3 above is a genuinely
  different, non-merge route to the same `ℓ(F)=2` target and is not ruled
  out by this dead end.)

- Small-case / intuition notes (all conjecture/numeric, not proof): fresh
  exact-`Fraction` random search (20,000 trials/`n`, this round,
  `/tmp/round-11/probe.py`) on the `v<s`, `p_2`-untouched branch at
  `n=3,4,5,6` found zero violations of `A(F∪G')>=f(n)` (worst found margin
  over `f(n)`: `n=3`: `1001/15000`; `n=4`: `1007/31000`; `n=5`:
  `1307/63000`; `n=6`: `2869/127000` — margins shrink but stay strictly
  positive, consistent with the conjecture but not exhaustive/boundary-
  seeking, so this is *not* new evidence beyond what rounds 9-10 already
  found, just an independent re-confirmation with a different random
  sampler). This corroborates (does not newly establish) that the `v<s`
  branch is a real but not-yet-proved true fact, and is fully consistent
  with opening (1)'s diagnosis that it is the same recursive obstruction
  one level down (the shrinking margin as `n` grows matches the pattern
  every other sub-case in this project shows as `a_n` tightens toward the
  worst case).
