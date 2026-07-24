## imo-2026-03

- Distinct openings:
  1. **Exact reduction of Phase 3 (claiming subgame) to a closed formula.** The claiming
     game on a fixed multiset of piece lengths has a known value: sort the pieces
     descending `x_1 ≥ x_2 ≥ … ≥ x_m`; the greedy strategy "always take the current
     largest remaining piece" is optimal for *both* players simultaneously (a Nash
     equilibrium / minimax solution), and the first player's total is exactly
     `x_1+x_3+x_5+…` (sum of odd-rank pieces), the second player's is `x_2+x_4+…`.
     I verified this by brute-force game-tree search (minimax over all play orders)
     against the greedy prediction for random multisets of size 1–6 — exact match in
     every trial. This turns the whole problem into a **pure combinatorial minimax**
     over interval-cutting: no more game-tree reasoning needed for Phase 3 at all.
  2. **A trivial but useful structural fact:** since `x_{2i-1} ≥ x_{2i}` termwise (and
     there may be one unpaired smallest piece with `x_{2n+1} ≥ 0`), the first player's
     total is *always* `≥ 1/2` of the total stick length, **for any cut set whatsoever**
     — this holds even if Liu Bang places 0 points. So `c(n) ≥ 1/2` for all `n` is a
     one-line cheap-kill/sanity fact; the real content of the problem is *how much
     above* `1/2` Liu Bang can force.
  3. **The adversary's "neutralize by pairing / sliver" mechanism** (the real crux,
     found empirically, see below): Xiang Yu's most powerful move is not to make many
     small pieces but to use a cut to create an **exact size-match** with an existing
     piece (turning a piece Liu Bang would win outright into a tied pair, which splits
     50/50 regardless of who picks it first), or to shave a **near-zero sliver** off a
     piece he can't otherwise neutralize (this "wastes" one of Liu Bang's late picks on
     a near-zero value while creating another matched pair). Both moves push the local
     contribution toward the trivial `1/2` floor. This is the mechanism the outliner's
     upper-bound argument (Xiang Yu's strategy) should be built around, and it is also
     exactly what any construction (Liu Bang's strategy) must be proven **resistant**
     to.
  4. **A recursive/self-similar construction shape** (conjectural, not proven): treat
     Liu Bang's `n`-point strategy as "cut off one small end-piece, then recurse with
     the `(n-1)`-strategy on the remaining big piece, rescaled." This is the natural
     generating idea behind the numbers found (see Small-case notes) and is a concrete
     top-level target for the outliner's construction; the matching upper bound would
     need a dual recursive argument bounding Xiang Yu's best sabotage by the same
     recursion.

- Candidate technique(s): reduce Phase 3 via the greedy/order-statistics lemma (name
  it "greedy selection is optimal in an unstructured take-turns item game" — this is a
  classical exchange-argument result, not literally in `knowledge_base.md` but provable
  by the standard swap/domination argument the KB's Meta-Strategy section gestures at).
  Then attack the resulting minimax purely as an extremal/adversarial interval problem:
  **invariants/monovariants** (KB: "Invariants & monovariants") tracking `L - X = sum of
  (x_{2i-1}-x_{2i}) + leftover`; **pigeonhole/extremal principle** for the adversary's
  best local move; possibly an inductive/recursive argument on `n` (KB: "Induction:
  ... for 'for all n' constructions, build step n from step n-1").

- Cheap-kill candidates: `L ≥ 1/2` always (proven above, one line, termwise domination
  of paired order statistics) — use to sanity-check any claimed formula: `c(n)` must
  satisfy `c(n) ≥ 1/2` and `c(n) → 1/2` as `n → ∞` is very plausible (Xiang Yu's
  pairing power grows with his budget). Also: total final piece count is at most
  `2n+1` (odd if both use full budgets); a "perfect pairing" of *all* pieces is
  therefore never fully achievable in one shot — there is always at least one
  structurally left-over piece, which is the seed of Liu Bang's advantage.

- Knowledge-base entries to use: "Invariants & monovariants" (combinatorics section);
  "Pigeonhole / extremal principle"; "Induction... for 'for all n' constructions, build
  step n from step n−1" (General Proof Methods); Meta-Strategy's "check small cases
  first" (heavily used here). No entry in `knowledge_base.md` directly names a
  take-turns-selection-game lemma — the greedy-optimality fact for Phase 3 needs to be
  stated and proved from scratch by the outliner/builder (exchange argument: if it's
  ever optimal to not take the current max, swapping that pick with the max piece
  weakly improves the mover and weakly hurts no one, standard induction on `m`).

- Analogous past problems (cruxes): Searched `past_crux_moves_database.json` filtered
  to `domain=combinatorics, subtopic=games-and-strategy` (39 entries) and by keyword
  (`pick/select/greedy/claim/pair`). No corpus problem is literally "cut a stick,
  alternately claim pieces" — nothing is a close structural match. The closest in
  *spirit* (not directly reusable, but suggestive of the pairing mechanism Xiang Yu
  exploits):
  - `aimo-0596` (pairing/involution take-turns card game) — crux "In a pairing/misère
    take-turns game, have the responder answer each opponent pick with its fixed
    involution-partner... so whatever coset value the final invariant lands on is a
    card the responder is guaranteed to already hold." This is the general pattern
    behind Xiang Yu's "create a matched pair to neutralize" move I found, though the
    setting (XOR/coset game) is unrelated to interval cutting.
  - `aimo-0115` / `aimo-0854` (domino/cell pairing-response strategies) — same generic
    "respond in the partner cell" idea, again only useful as a structural analogy for
    "pairing neutralizes first-mover advantage," not a reusable lemma.
  None of these should be cited as a technique source beyond this analogy — the actual
  claiming-game value formula and the adversarial minimax must be derived from scratch.

- Prior progress: none (`results/imo-2026-03/current.md` is still `unsolved`, no
  approaches filed yet — this is round 1).

- Dead ends (do not retry):
  - **Equal-partition construction** (Liu Bang divides into `n+1` equal pieces of
    `1/(n+1)`): exactly refuted. For `n=1` this gives value → `1/2` in the limit
    (Xiang Yu just needs to slice one half unevenly), far worse than the true optimum
    `2/3`. For `n=2`, equal thirds `{1/3,1/3,1/3}` numerically bottoms out at ≈`0.5003`
    (i.e. exactly `1/2` in the limit) — Xiang Yu fully neutralizes it. **Never propose
    equal partition as Liu Bang's strategy.**
  - **Any construction with two equal initial pieces** (e.g. `{0.2,0.4,0.4}` for
    `n=2`): exactly computable, gives **exactly** `0.5` (not a limit — Xiang Yu splits
    the odd piece `0.2` into two `0.1`s using only *one* of his two cuts, producing
    `{0.4,0.4,0.1,0.1}`, a perfectly pairable 4-piece set, first-mover total exactly
    `0.5`). Any repeated piece length is an immediate, cheap, exact win for Xiang Yu —
    **Liu Bang's initial pieces must be pairwise distinct and, more strongly, must
    avoid any exact or asymptotic size-matching that Xiang Yu can complete with a
    bounded number of cuts.**
  - **Naive "arithmetic progression" construction `{n, n+1, …, 2n}/S` (S = 3n(n+1)/2)**:
    worked beautifully for `n=1` (`{1,2}/3`, value `2/3`) and `n=2` (`{2,3,4}/9`, value
    exactly `5/9` — verified three independent ways by hand, see below) — **but fails
    at `n=3`**: numerically, `{3,4,5,6}/18` collapses to exactly `0.5` (Xiang Yu fully
    neutralizes it with his 3 cuts). **Do not extrapolate this specific piece pattern
    past `n=2`** — whatever the true general construction is, it is not simply "pieces
    proportional to consecutive integers `n..2n`."

- Small-case / intuition notes (all labeled as computed/derived evidence, upper-bound
  optimality of Xiang Yu's response NOT rigorously proven beyond n=1):
  - **n=1: `c(1) = 2/3`, rigorously derived** (full case analysis, not just numerics).
    Liu Bang cuts at `1/3` (pieces `{1/3, 2/3}`). Exhaustively checking Xiang Yu's only
    two structural options (split the `1/3` piece, or split the `2/3` piece, over all
    continuous cut positions) shows the worst case is exactly `2/3`, attained when
    Xiang Yu splits the `2/3` piece exactly into two `1/3`s, giving three equal `1/3`
    pieces (Liu Bang claims 2 of 3). Confirmed numerically via brute-force grid/optimize
    (`p=1/3` maximizes the worst-case value, matches `2/3` to 4 decimal places).
  - **n=2: `c(2) = 5/9` (`≈0.5556`), very strong numeric + hand-verified evidence, not
    a full proof.** Construction: pieces `{2,3,4}/9`. Xiang Yu's best found response
    (found independently three ways: splitting the `2/9` piece into `(~0, 1/9, 1/9)`;
    matching `4/9→(3/9,1/9)` then `2/9→(1/9,1/9)`; matching `4/9→(2/9,2/9)` directly
    with the existing `2/9`) all give **exactly** `5/9`. A 2-D outer optimization
    (Nelder–Mead, 5 different starting points) independently converges to essentially
    this same piece ratio (`≈0.222,0.333,0.444`) with value `≈0.5556`, giving good
    confidence this is at least a strong local optimum for Liu Bang.
  - **Conjectured general closed form:** `c(n) = 1/2 + 1/(2·3^n) = (3^n+1)/(2·3^n)`.
    This fits `n=1` (`2/3`) and `n=2` (`5/9`) *exactly*, and fits the natural boundary
    case `n=0` (no points allowed at all ⇒ whole stick is one piece ⇒ Liu Bang claims
    everything ⇒ `c(0)=1`, and the formula gives `1/2+1/2=1` ✓). It is motivated by a
    guessed recursive structure `c(n) = 1/2 + (c(n-1)-1/2)/3` (a contraction by `1/3`
    per additional point, self-similar cut-off-a-small-piece-and-recurse idea).
    **However, my n=3 numerics are inconclusive**: high-dimensional adversarial
    minimax search (3 cuts among 4 pieces, many cut-allocation cases) is numerically
    hard — coarse optimization runs found values in the range `0.52–0.5235` for
    various candidate constructions, in the right neighborhood of the conjectured
    `14/27 ≈ 0.5185` but not tight enough to confirm or refute it (Xiang Yu's true best
    response was likely under-optimized by the crude search, since his optimal
    sabotage in the `n=2` case required exact size-matching to 3+ decimal places,
    which coarse grids/Nelder–Mead with few restarts systematically miss/overestimate).
    **Treat `c(n) = (3^n+1)/(2·3^n)` as the leading conjecture and target closed form,
    but flag it explicitly as unconfirmed for `n≥3`** — the outliner should try to
    prove it via the recursive-construction idea + a matching recursive adversary
    bound, and should sanity-check the formula against any independently-derived upper
    bound before committing to it as the final answer.
