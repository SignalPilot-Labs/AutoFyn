## imo-2026-03

**Lens: a framing for f≥1 at the tied minimizer that avoids integrality of any block value entirely.**
Verdict up front: **no genuine escape found.** All three assigned candidates ((a) SOS/quadratic
certificate, (b) direct game-strategy bypass, (c) count-profile/cut-budget Case-B) either were
already tried and recorded as collapsing onto the same wall, or — for the ones I re-derived myself
this round — provably cannot avoid controlling `det(U)` (or its lattice generalization), which IS
the minimality⇒benign-U fact both live routes already isolated. This is a *confirmation*, not a
new dead end record (the underlying facts were already flagged in `/tmp/memory/math-explorer.md`
round-6 rules); I add one concrete algebraic proof of *why* no real-valued bypass exists, plus one
new actionable idea from the crux corpus.

- **Distinct openings evaluated (all traced to ground, none escape):**
  1. **(a) SOS / quadratic dual certificate directly on `f` over the cut polytope.** `f` is
     piecewise-AFFINE (gradient in `{−2,0,2}`) on each sort-chamber, so any genuine "quadratic"
     certificate of nonnegativity degenerates to a family of *linear* per-chamber certificates —
     exactly the one-shot LP-dual-price route that round 2 PROVED DEAD (`alternating-sum-threshold-
     potential`: any fixed length-only price is forced `≤0` by equal-piece feasibility). Re-verified
     the logic: a quadratic form can only certify nonnegativity of a function with curvature; `f`
     has none within a chamber, so the "SOS" collapses to the same discredited linear dual. **Dead,
     confirmed (not new).**
  2. **(b) Direct explicit Liu-Bang pairing/mirroring strategy on the actual claiming game,
     bypassing `f` altogether.** Checked whether this could be a genuinely different *target*, not
     just a different *proof* of the same target. It cannot: `endgame-greedy` (certified) makes the
     claiming phase **fully deterministic** — Liu Bang's payoff on any final multiset `P` is exactly
     `Odd(P) = (Σ(P)+f(P))/2`, with no strategic freedom left once `P` is fixed. So "LB guarantees
     `≥ 2^n`" is *definitionally* `f(P) ≥ 1`, not a separate combinatorial fact reachable by a
     pairing/mirroring argument on cards or cells (unlike the crux-corpus games I checked — see
     below — which have a genuinely separate combinatorial payoff structure). Any "explicit
     strategy" proof is a *reformulation*, already executed by `game-value-recursion` (dormant,
     Elo lower), which reaches the identical open sub-claim (there called BNF / Case B). **Confirmed
     same wall, per round-6 rule — do not re-seed as new.**
  3. **(c) Count-function-profile / cut-budget Case-B route.** Already built (`cut-budget-jacobsthal-
     recursion`, partial, dormant this round). It proves a clean two-band per-cut identity and
     REFUTES its own proposed per-cut monovariant driver (a single cut can drop `f` by 12.27 with
     zero Jacobsthal budget, `n=4` explicit instance). Its own writeup explicitly states the residual
     "(D)/(LBL-B)" needs the *global odd-band profile* of the reachable config, and that this is "as
     hard as (LBL) directly... not a genuinely new sub-problem." I re-checked this claim rather than
     trusting it: tried to see whether an "uncut-survivor peeling" induction (peel at ANY level with
     a surviving original piece, not just the top) could give a clean decomposition — it fails for
     the same reason Case B is hard: cutting the top piece can produce sub-pieces that are *smaller*
     than lower-level uncut originals, so the rank-order interleaves across levels and no clean
     `f(Q) = f(top part) "+" f(bottom part)` decomposition survives (this is exactly the "budget
     non-fungibility" (BNF) obstruction `game-value-recursion` already names). **Confirmed same
     wall.**

- **New structural finding this round (algebraic, not previously written up explicitly): why NO
  real-valued (non-integrality) bypass of Gap A/D can exist.** At the Φ-maximal minimizer, `w` is
  the *unique* solution of `Uw = b` (since `ker U = {0}`, full column rank ⇒ at most one solution;
  consistency ⇒ exactly one), so by Cramer's rule `f = sᵀw = N / det(U)` for some *integer* `N`
  (built from `s`, `b`, and the integer cofactors of `U`) whenever `U` is square (`p = n+1`; the
  non-square case is the analogous integer-lattice statement, Gap D). Verified numerically on the
  known `{2,4/3,4/3,4/3,1}` non-minimizer instance: `det(U) = 3`, `f = 5/3`, and `f·det(U) = 5`
  (integer), exactly as Cramer's rule predicts. **Consequence:** any proof of `f ≥ 1` — even one
  that never says the word "integer" and only wants the *real* inequality `f ≥ 1` — is *forced* to
  control `|det(U)|` (equivalently the denominator of the rational number `N/det(U)`), because
  without such control `f` could equal `1/|det(U)|` for `|det(U)|` arbitrarily large, and no purely
  real/continuous argument (convexity, SOS, exchange) can rule that out without arithmetic input on
  `U`. This makes precise round 6's "Smith-normal-form duality" claim: **the plateau is a genuine
  mathematical fact about the problem, not an artifact of any one framing** — every approach that
  reaches `f = sᵀw` with `Uw=b` must eventually bound `det(U)` (primal) or the GCD of its maximal
  minors (dual), and I could not find a route around this necessity.

- **Cheap-kill candidates:** none obvious beyond what's already certified (isolated-cycle-exclusion,
  S-core). The Cramer's-rule observation above is itself a useful cheap framing device: for any
  proposed *new* approach, first compute `det(U)` (or minors) on the specific instance and check
  `f·det(U) ∈ ℤ` — this is a fast sanity/triage tool, not a proof route.

- **Candidate technique(s):** none new found that avoid `det(U)`/minor control. The problem's
  residual genuinely requires an arithmetic fact about `U` (unimodularity at minimizers, primal) or
  equivalently coprimality of its maximal minors (dual) — confirming, not contradicting, round 6.

- **Knowledge-base entries relevant:** `Sum of squares (SOS)/completing the square` and `Quadratic
  forms are PSD iff SOS` (both in `knowledge_base.md`) — checked and ruled inapplicable here because
  `f` has no curvature within a chamber (see above); `Extremal graph theory` entry not directly
  applicable (our incidence structure isn't a simple graph-threshold question, it's a coprime-minors
  question).

- **Analogous past problems (crux corpus):**
  1. **`aimo-0281`** (pentagon solitaire game, `linear-algebra-method`/`combinatorics`) — genuinely
     useful crux, **not previously surfaced in this workspace**: its third move is *"the same mod-`p`
     condition that forces the invariant-selected winner to be unique is EXACTLY the condition that
     certifies the dual linear system has an integer solution."* I.e. rather than proving "integer
     solvability" and "positivity/selection" as two *separate* facts (which is what
     `dual-integer-certificate` currently does — Gap D and Pos as independent gaps), that problem's
     solution finds **one unified congruence invariant that does both jobs simultaneously**. This is
     a concrete, actionable idea for `dual-integer-certificate`: look for a single minimality-derived
     congruence/invariant on `(U, s)` that forces `s ∈ Uᵀℤ^{n+1}` (Gap D) AND `f ≠ 0` (Pos) at once,
     rather than attacking them as two isolated gaps. This is worth flagging to the outliner as a
     genuinely new sub-tactic *within* the dual route (not a new top-level approach — it's a lever on
     an existing live route, offered here as diversity within that route's toolkit).
  2. Checked `games-and-strategy` pairing/mirroring cruxes (`aimo-0066`, `aimo-0115`, `aimo-0596`,
     `aimo-0854`) — all are "block/pair/mirror the opponent's discrete move" games with a
     structurally different payoff (parity of a pattern, not sum-maximization of claimed lengths);
     none transfer as a bypass of the deterministic-greedy claiming phase already certified here.
     **Not analogous enough to use** (their pairing strategies answer a different kind of adversary
     goal — completing/avoiding a pattern — not a magnitude sum).

- **Prior progress:** unchanged from `current.md` — upper bound fully proved/certified; lower bound
  reduced to the tied-minimizer residual = Gap A (primal, non-isolated cycles) ∪ Gap B (μ=3 leaf) =
  Gap D-at-minimizers ∪ Positivity (dual). 19 lemmas certified. `min f = 1` numerically confirmed
  `n≤4`.

- **Dead ends (do not retry, confirmed again this round):** SOS/quadratic certificate on `f`
  (collapses to the round-2 dead linear dual-price route); explicit game-strategy as a *bypass* of
  `f≥1` (it is definitionally the same statement once `endgame-greedy` is applied — confirmed via
  Cramer's-rule argument that any route through `f=sᵀw, Uw=b` needs `det(U)`/minor control regardless
  of framing); cut-budget's per-cut Jacobsthal-decrement driver (already refuted, re-confirmed its
  residual (D)/(LBL-B) is genuinely as hard as the top-level problem, not a shortcut).

- **Small-case / intuition notes (conjectural where marked):** Numerically re-confirmed
  `f·det(U) ∈ ℤ` on the known non-minimizer instance (`f=5/3`, `det(U)=3`, product `5`) — this is an
  exact algebraic fact (Cramer's rule), not a conjecture, and it is the crispest evidence that
  *every* route to `f≥1` must ultimately bound `|det(U)|` (or the GCD of maximal minors in the
  non-square case) by `1` (or, short of that, prove `f ≥ 1` some other arithmetic way entirely
  independent of size — no such alternative was found). This reinforces: round 7's crispest target
  remains **minimality ⇒ benign-U** (unchanged from round 6's "Next" note); no genuinely different
  top-level framing exists that avoids it. Recommend the outliner spend the round's new-idea budget
  on the `aimo-0281`-style **unified-invariant** lever for Gap D + Pos (item above) rather than on
  seeding a fourth top-level approach — a fourth framing would very likely re-derive the same
  Cramer's-rule obstruction shown here.
