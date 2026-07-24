## Status
unsolved

## Approaches tried
(none yet — new approach, round 1)

## Current best
Empty — nothing built yet. This file records the OUTLINE only; the builder fills in the proof.

## Full proof
(absent — Status is not `solved`)

---

## Outline (proof-outliner, round 1)

**Target.** Same as all approaches: prove `c(n) = 2^n/(2^{n+1}-1)` for every
positive integer `n`, with a full minimax proof (matching upper bound and
construction).

**Technique (spine).** **Strong induction directly on `n`**, via a "first-move
reduction": show that Liu Bang's optimal first cut splits `[0,1]` into a piece
of size exactly `2^n/(2^{n+1}-1)` (which he can simply claim/protect) and a
remainder of size `(2^n-1)/(2^{n+1}-1)`, and that the game restricted to the
remainder — with `n-1` points left for each player — is *strategically
equivalent* (after rescaling the remainder to length 1) to the `(n-1)`-point
version of the SAME game, whose value is `c(n-1)` by the inductive hypothesis.
This is a genuinely different top-level architecture from a direct global
potential-function argument: instead of one invariant covering all `n` at
once, it reduces size-`n` to size-`(n-1)` and closes with the algebraic
recursion `c(n) = 2^n/(2^{n+1}-1) = f(c(n-1))`.

**Skeleton.**
1. **Import the claiming-subgame reduction lemma** (shared across all
   approaches — sum of odd sorted ranks is the claim-game value; prove once,
   by the exchange argument, and cite/import if another approach's builder has
   already certified it in `lemmas/`).
2. **Base case `n=1`.** Prove directly (already done analytically by all three
   explorers): Liu Bang marks `x=1/3`; case analysis on Xiang Yu's single
   response point gives Liu Bang exactly `2/3` in the worst case, and no other
   `x` does better. `c(1) = 2/3 = 2^1/(2^2-1)`. ✓.
3. **Inductive setup.** Assume `c(n-1) = 2^{n-1}/(2^n - 1)` is proved (both
   directions) for the `(n-1)`-point game on a unit stick. We must show
   `c(n) = 2^n/(2^{n+1}-1)` for the `n`-point game.
4. **Lower bound via the recursive construction.** Liu Bang's first point cuts
   off a piece of size `p = 2^n/(2^{n+1}-1)` from one end, leaving a remainder
   of size `1-p = (2^n-1)/(2^{n+1}-1)`. On the remainder (rescaled to length 1),
   Liu Bang recursively plays his optimal `(n-1)`-point strategy from the `n-1`
   case (by IH, guaranteeing himself `≥ c(n-1) = 2^{n-1}/(2^n-1)` of the
   *rescaled* remainder, i.e. `≥ c(n-1)·(1-p)` of the original stick — this is
   exactly the `2^{n-1},…,2,1` ladder scaled onto `[p,1]`, reproducing the full
   `n`-point ladder from Step-elsewhere). **Key claim to prove**: no matter what
   Xiang Yu does — including cutting INTO the size-`p` first piece rather than
   only into the remainder — Liu Bang's total is still `≥ p + c(n-1)(1-p)`. This
   requires ruling out the possibility that Xiang Yu profitably "attacks" the
   protected first piece `p` instead of playing only in the remainder — the
   gap: show that any Xiang-Yu cut inside `[0,p]` is weakly dominated (for
   Xiang Yu) by instead spending that point in the remainder, i.e. an exchange
   argument transplanting Xiang Yu's cuts.
5. **Upper bound via the recursive spoiling strategy.** Symmetric direction:
   given ANY Liu Bang marking of `n` points, Xiang Yu's strategy is: identify
   the largest piece `M` in Liu Bang's initial cut (breaking `[0,1]` into `≤
   n+1` pieces); bisect `M`... (or: treat the single largest piece as
   `p`-analogue and recursively apply the `(n-1)`-strategy, by IH, to the
   remaining `≤ n` pieces using his remaining `n-1` points, after "neutralizing"
   `M` with his first point). The precise recursive spoiling rule needs to be
   pinned down: **Conjecture** — Xiang Yu's first move bisects the single
   largest piece of Liu Bang's initial partition; this converts the largest
   piece into two pieces each `M/2`, and the resulting `≤ n+2`-piece
   configuration, with `n-1` Xiang Yu points left, is claimed (via IH on the
   *reduced* instance restricted to "everything except one of the freshly
   created `M/2`'s, which Liu Bang is now guaranteed to be able to claim
   outright") to reduce to the `(n-1)`-case upper bound `c(n-1)` applied to the
   rest. **This reduction is not yet made precise and is the main open gap** —
   unlike Step 4 (construction side, more tractable), the upper-bound direction
   does not obviously decompose into "one piece is settled, recurse on the
   rest," because Liu Bang's *arbitrary* initial marking need not have a
   piece of exactly the right size `p` to peel off; the induction must instead
   bound things via inequalities (e.g. show `f(largest piece M, n) ≤
   M·(something) + c(n-1)·(1-M)·(something)` type recursion) rather than a
   clean equality-based peel.
6. **Solve the recursion.** Once Steps 4–5 give matching bounds `c(n) ≥ p +
   c(n-1)(1-p)` and `c(n) ≤` (analogous upper expression), verify algebraically
   that `p = 2^n/(2^{n+1}-1)` and `c(n-1) = 2^{n-1}/(2^n-1)` satisfy `p +
   c(n-1)(1-p) = 2^n/(2^{n+1}-1)` exactly (a direct computation:
   `1-p = (2^n-1)/(2^{n+1}-1)`, so `c(n-1)(1-p) = [2^{n-1}/(2^n-1)] ·
   [(2^n-1)/(2^{n+1}-1)] = 2^{n-1}/(2^{n+1}-1)`, and `p + 2^{n-1}/(2^{n+1}-1) =
   (2^n+2^{n-1})/(2^{n+1}-1)`... **note this arithmetic does NOT immediately
   give `2^n/(2^{n+1}-1)`** — `2^n + 2^{n-1} = 3·2^{n-1} ≠ 2^n` in general, so
   the naive "peel off the top piece, recurse on the rest" recursion as stated
   is WRONG and must be corrected; the actual recursive structure (if it exists)
   is subtler than "first piece is exactly `p`, remainder inherits `c(n-1)`
   verbatim" — this arithmetic mismatch is flagged explicitly as a gap the
   builder must resolve (either find the correct recursive decomposition,
   e.g. peeling off TWO ranks at a time or a different rescaling, or abandon a
   literal recursion in favor of a direct induction on a stronger multi-parameter
   statement).

**Key lemmas (claim + mechanism):**
- Claiming-subgame value formula — shared lemma (see approach
  `greedy-halving-adversary`), reuse.
- Recursive self-similarity of the ladder construction — because the geometric
  ladder scaled onto any sub-interval `[p,1]` with ratio `(1-p)` reproduces the
  `(n-1)`-ladder there, so the lower-bound recursion is natural — **but the
  exact algebraic recursion for `c(n)` in terms of `c(n-1)` must be re-derived
  correctly (see Step 6 — the naive guess is arithmetically false)**.

**Open gaps:**
- Step 4: proving Xiang Yu cannot profitably attack the "protected" first
  piece `p` rather than only playing in the remainder (an exchange/domination
  argument between Xiang Yu's cut locations).
- Step 5: the upper-bound recursive spoiling strategy is not pinned down at
  all — this is the harder, more open-ended gap, since arbitrary Liu Bang
  markings don't hand Xiang Yu a clean "one piece = p, rest = remainder"
  structure to recurse on.
- Step 6: the naive linear recursion `c(n) = p + c(n-1)(1-p)` is ARITHMETICALLY
  WRONG for `p = 2^n/(2^{n+1}-1)` — the builder must find the correct
  recursive relation (if any exists) before this approach can close; this may
  mean the "clean induction on n" framing does not actually work and the
  approach should be marked a likely dead end if no correct recursion is found
  within a round or two — flag this explicitly to the reviewer.

**Cases to cover:** the base case `n=1` (done); the inductive step for general
`n≥2` (open, both directions).

**Watch out for:** the false-recursion trap identified in Step 6 — do NOT
let the builder paper over the `2^n + 2^{n-1} ≠ 2^n` arithmetic gap with
hand-waving; either derive the true recursion (possibly `c(n)` doesn't satisfy
a simple length-1-piece-peel recursion at all, and a different induction
variable / stronger inductive hypothesis is needed) or report this approach as
refuted and pivot.

**Round 6 outline-reviewer note (orphan-file audit):** this file was never
registered in `.ranking.json` and has zero recorded builds — it appears to
be a round-1 outline that was superseded before any builder picked it up.
Its own Step 6 already flags a genuine arithmetic contradiction in the naive
"peel one piece of size $p$, recurse on the remainder" recursion, and its
top-level architecture (reduce size $n$ to size $n-1$ via a single top-piece
peel) is exactly the "reduce to a smaller ladder instance" pattern the
round-6 shared-gap-plateau directive says not to re-open. **Not recommended
for registration or building this round** — if a future round wants an
induction-on-$n$ variant, it should first check whether the arithmetic
mismatch here is fixable (e.g. via a two-rank peel or a stronger multi-
parameter inductive statement) rather than reusing this file's literal
Step 4/5 as stated.
