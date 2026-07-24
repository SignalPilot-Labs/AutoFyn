## imo-2026-03 (lens: THE UPPER BOUND, GAP-U only)

### Setup recap (all certified, do not re-derive)
LB's `≤n+1` pieces sum to 1; XY has `≤n` cuts. By Lemma 0 (`lemmas/endgame-greedy.md`)
LB's payoff is `Odd(P) = (1+f(P))/2`; by the layer-cake identity
(`lemmas/layer-cake-alt-sum.md`) `f(P) = M(P) = measure{t : c_P(t) odd}` where
`c_P(t) = #{pieces > t}`. The claim reduces to `max_LB min_XY M = 1/D_n`,
`D_n = 2^{n+1}-1`. **GAP-U is: for every LB marking (≤n+1 pieces, total 1), XY has a
≤n-cut response with `M ≤ 1/D_n`.** All three round-1 approaches independently derive
the identical matching reformulation: `M = min-weight perfect matching cost of the
pieces on the line (adjacent pairing, phantom 0 if odd count)`. Two atomic moves are
proved: bisection deletes a piece from the matching (P1/P2), and "top-match" (cut piece
`p1` into `(p2, p1-p2)`) replaces `{p1,p2}` by `{p1-p2}` (P4). Neither alone suffices
(both over/under-shoot — see Dead ends). This is the *shared gap* across all three
approaches; the field needs a genuinely new angle, not another variant of P2/P4.

### Distinct openings for GAP-U

1. **Dominance-regime split on the top piece (new insight this round, verified by hand
   example, NOT in any prior approach file).** Split on whether the top piece `a1`
   dominates the rest (`a1 ≥ Σ(rest)`, forcing `a1` to remain rank-1 forever no matter
   how `rest` is cut, since every sub-piece of `rest` stays `≤ Σ(rest) ≤ a1`). In this
   regime, by the `k=1` identity (Lemma 0's proof line), `final M = a1 - M(rest_final)`
   for whatever XY does to `rest` and to `a1` if `a1` stays uncut. Since XY is
   *minimizing* the final `M`, in this uncut-top sub-case XY wants `M(rest_final)`
   **large**, i.e. the *opposite* of its usual cancel/bisect instinct. I verified by
   direct computation that a single cut CAN increase `M` of a sub-multiset (not just
   decrease it): `rest={0.06,0.04}` has `M=0.02` uncut; bisecting the smaller piece
   `0.04→{0.02,0.02}` gives `M=0.06-0.02+0.02=0.06`, i.e. `M` **triples**. This is the
   opposite of what P2 (bisection deletes a piece, "always shrinks M") suggests when
   naively over-applied to a sub-block — P2 shrinks `M` only when the piece being
   bisected is what's directly under the alternating sum's own top rank, not when it's
   embedded under a bigger dominant piece. **This exactly explains why the recorded
   dead-end "duplicate-the-top" / iterated-P4 strategies overshoot**: they blindly
   apply cancellation moves to every sub-block without checking whether the local top
   of that sub-block is itself in the "dominant" regime, where the correct play is the
   reverse (preserve or even amplify asymmetry, not cancel it). **This is a genuinely
   different attack angle**: build the whole recursive argument around classifying
   *every* piece (recursively) as "dominant" (⟹ freeze structure below it, recurse with
   reversed objective) vs. "balanced" (⟹ apply the cancel toolkit), rather than a single
   global bisect/match rule. Nobody has written this regime-split down yet.

2. **Direct threshold/stopping-rule construction keyed on the *target* `1/D_b`
   recursively** (the framing self-similar-recursion.md gestures at but does not close):
   define the strategy by strong induction on remaining budget `b`: XY looks at `a1`
   vs. the geometric threshold `2·D_{b-1}/D_b · Σ(rest)`-type comparison (the same ratio
   that makes the dyadic weights `2^j` tight — each equals `D_{j-1}+1`). The stopping
   condition should be: **stop cutting entirely once the currently-achievable `M` of the
   untouched remainder already sits `≤ 1/D_b` for the current budget `b`** — this is
   the "adaptive... and STOP" rule flagged in the dispatch; nobody has written the exact
   comparison test that decides "is it already ≤ target" without first paying a cut to
   find out.

3. **LP/matching-duality angle:** since `M` = min-weight perfect matching cost, `M ≤
   1/D_n` for *some* cutting is equivalent to *exhibiting one explicit matching* whose
   cost is `≤ 1/D_n` after `≤n` cuts — i.e., XY doesn't need to find the optimal
   matching, just *any* sufficient one. This suggests constructing the response
   directly as "assign each of the `≤n+1` LB pieces a canonical dyadic-scale target
   slot, cut each piece to match its slot's expected partner" rather than an iterative
   greedy — a direct constructive (existence, not optimality) argument, which may be
   easier to make airtight than proving optimality of a greedy process. This is the
   least-explored opening; worth a dedicated approach.

4. **Reverse the objective entirely: bound `Σ(rest)` relative to `a1` recursively as a
   "capacity" argument.** Since `M ≤ Σ(rest)` always when top is left uncut (as `M = a1
   - M(rest) ≥ a1 - Σ(rest)`, and separately `M ≤ a1` trivially when top uncut since
   `M(rest)≥0`), a cheap sufficient (if lossy) global strategy is: recursively peel the
   current max piece; if `a1 ≤ 1/D_b` already (current budget `b`), STOP (don't even
   need matching — a single piece contributes at most itself to `M`, so bounding the
   *residual sum*, not just the top piece, once residual total drops below `1/D_b`
   might let XY freeze without spending remaining cuts). This gives a **cheap sufficient
   stopping test** worth checking first: if `Σ(rest) ≤ 1/D_b` at any point (budget `b`
   remaining), STOP — since then trivially `M(final) ≤ M(a1) + Σ(rest) `... (needs
   care, `M` isn't simply subadditive over disjoint scale bands in general, only true
   under the "no piece in rest exceeds `a1`" dominance condition — same regime as
   opening 1). Flag as a candidate cheap-kill, not yet verified rigorously.

### Candidate technique(s)
Recursive/adaptive strategy defined by strong induction on the cut-budget `b`, with an
explicit **regime split** at each recursive level (dominant top piece vs. balanced
pieces) rather than one uniform rule (bisect-all or match-all). The matching
reformulation (`M` = min-weight adjacent-pairing cost) is the right computational
handle; the missing piece is the *case analysis* governing when to cancel (P2/P4) vs.
when to freeze/amplify (opening 1).

### Cheap-kill candidates
- Check whether `Σ(rest) ≤ 1/D_b` (residual-sum threshold) lets XY stop immediately in
  the dominant regime — a size-bound / pigeonhole-style cheap test (opening 4). Not yet
  verified for general multi-level nesting; needs care but is cheap to check per case.
- Symmetry: WLOG by Lemma 0's proof, only "take current largest" matters, so all
  strategy analysis can be restricted to the sorted list without loss — already used
  throughout, but worth restating as a reduction that keeps case counts down (only ever
  need to reason about the descending list, never arbitrary claim order).

### Knowledge-base entries to use
- `knowledge_base.md` general proof methods: induction/strong induction, extremal
  principle (the problem is exactly a minimax/extremal-principle statement).
  `Invariants and monovariants` section is the natural fit for the regime-split
  argument (an invariant tracked recursively: "is the current sub-block dominant").
  (I did not find a named KB entry specific to layer-cake/parity potentials or
  min-weight-matching duality — those were built from scratch in round 1 and are now
  cached as `lemmas/layer-cake-alt-sum.md`; treat that as the reusable "theorem" going
  forward rather than re-deriving.)

### Analogous past problems (cruxes)
- **aimo-0117** (Dutch TST 2021, problem 4) — crux: *"Assign the played values as a
  two-sided geometric (dyadic) sequence so that the single largest value strictly
  exceeds the sum of all the others"* and a companion move *"defer committing the
  extreme value... to hold an invariant."* This is a genuine structural analogue of
  opening 1 above: it is exactly the "dominant top piece" property (`2^j >
  2^{j-1}+...+2^0`) that our dyadic LB marking also has, and the *invariant-tracking*
  style of argument (maintain "is the current largest value in a safe state") is the
  right shape for the regime-split recursion GAP-U needs — though that problem is a
  black/white-box game, not a stick-cutting game, so the mechanics don't transfer
  directly; it's a framing analogue, not a technique to import verbatim.
- No other crux in `games-and-strategy` (combinatorics, 39 entries scanned) or in a
  keyword search for "stick/segment/split/cut/alternat" (116 problems, mostly geometry
  noise) is a genuine structural match for a continuous-cutting alternating-sum game.
  Nothing else recommended; do not force a weaker match.

### Prior progress
See `results/imo-2026-03/current.md` and the three approach files: reduction to
`max_LB min_XY M = 1/D_n` fully proved; `n=1` fully solved both directions; lower-bound
Case 1 (top uncut) fully proved. GAP-U itself: no correct general argument yet in any
approach; all three converge on the same matching toolkit (P1–P4) and record the same
"iterated cancellation overshoots" failure.

### Dead ends (do not retry)
- **"Bisect current max `n` times" (fixed, non-adaptive)** — overshoots the cap (e.g.
  `[~1,~0]` config at `n=2` gives `0.75 ≫ 4/7`... wait `4/7≈0.571` target for the LB
  payoff; in `M`-terms the blind-bisection value is well above `1/D_n`). Confirmed by
  all three approaches.
- **"Subset-bisection alone" (P3)** — `max_config min_K M(K) ≈0.167 > 1/7` at `n=2`;
  insufficient alone (confirmed, reused check: taking `K` = smallest single piece is not
  always ≤ target).
- **"Iterated top-match alone" (P4 / duplicate-the-top recursion)** — catastrophic on
  top-heavy configs `[1,ε,...]`, and separately shown to violate the cap numerically
  from `n=3` on with value `≈0.074 > 1/15` vs. true optimum `≈0.002`. Confirmed by two
  independent approaches.
- **"Blanket non-max-cut domination"** — false in general (28k counterexamples found by
  outline-reviewer); only true restricted to the dyadic config (and even there is
  exactly the content of the still-open GAP-LB, not GAP-U).
- My own dominance-regime observation (opening 1) is **new**, not previously tried —
  flagging it as an opening, not a dead end.

### Small-case / intuition notes (conjectural / hand-verified)
- Hand-verified (not full proof): a single cut can *increase* a sub-block's `M`
  (`{0.06,0.04}`: `M=0.02` uncut → `M=0.06` after bisecting the smaller piece into
  `{0.02,0.02}`). This is the concrete counterexample to "cutting always helps XY
  locally," and pins down exactly why naive greedy cancellation strategies overshoot:
  they must NOT apply cancellation moves inside a dominant sub-block.
  Labeled: **hand-verified numeric fact**, not yet a general lemma.
- Conjecture (numerically confirmed `n≤3` by prior rounds): dyadic `W_n` is the *unique*
  maximizer of `min_XY M` over LB markings, with value exactly `1/D_n`; the optimal XY
  response against dyadic is the self-similar bisection cascade, which is consistent
  with, but does not by itself establish, the general upper bound for arbitrary
  (non-dyadic) LB markings — that's precisely GAP-U.
- The exponentially small target `1/D_n = 1/(2^{n+1}-1)` strongly suggests the final
  multiset XY must reach is forced to be *close to* the dyadic shape itself regardless
  of the starting configuration — i.e. GAP-U is roughly "prove dyadic-like refinement is
  always reachable/dominant within budget `n`," reinforcing that opening 2 (recursive
  threshold construction keyed to `D_b`) and opening 1 (regime split) are two views of
  the same needed argument, and openings 3/4 are the least-explored alternatives.
