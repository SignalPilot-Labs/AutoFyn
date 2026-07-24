## imo-2026-03 — lens: n=4 chamber census (p1<T/2 residual)

- Distinct openings (routes for the outliner to hand to builders):
  1. **"Free transplant first" opening.** Before deriving anything new, assemble
     the three pieces that already transplant to n=4 verbatim (see below) to
     shrink the open box as much as possible for zero cost, then only census
     the genuinely residual strip. This is the cheapest possible next move and
     should be built even if the chamber census itself waits a round.
  2. **"Reuse the n=3 minimal 5-chamber family as a template, not a citation"
     opening.** Take the *shape* of each certified n=3 case-(b2) chamber
     (Bisect{1,4}, Bisect{1,2}, DS-Above, Triple-Pin, R22.1.1) and re-derive
     each one index up (5 pieces $p_1,\dots,p_5$, budget 4 cuts), tracking
     exactly which chambers gain a genuinely new sub-case because of the new
     piece $p_5$ (expect some old chambers to split into two, mirroring how
     n=3's "Chamber B" itself split into B1/B2, and DS-Below/Above already
     needed an explicit non-coverage caveat). Do **not** assume the n=3 count
     (20 chambers) transplants 1:1 — the round-28 density signal (28%→64%
     uncovered-by-simple-templates growth from n=3→n=4) suggests materially
     more chamber types will be needed, not the same 20 re-indexed.
  3. **"Measure the residual first" opening.** Since the fully general
     Bisect-Subset Lemma (see below) is *already proved for arbitrary $m$* and
     costs nothing to instantiate at $m=5$, the single cheapest diagnostic
     move is to numerically grid/sample the actual open box
     ($p_1<T/2$, $T/31<p_2<8T/31$, $m=5$) against just the $2^5-2=30$
     Bisect-Subset chambers (exact `Fraction`, same style as round 24's
     `coverage6.py`/`coverage5.py`) to get a real coverage-fraction number
     before committing to hand-deriving new pin/tie chambers. This tells the
     next round how large the residual census really is (round 24 did exactly
     this at n=3 first, with the 15 Bisect-Subset chambers alone, before
     deriving the other 5).

- Candidate technique(s): the whole apparatus is already built and
  n-parametrized in principle: `cross-piece-sign-assignment-identity` +
  `odd-run-reduction-lemma` (evaluate any tie/pin construction in closed
  form) → `p-space-chamber-vertex-theorem` + `within-chamber-affinity-theorem`
  (chamber ⇒ finite-vertex reduction) → `feasibility-suffices-for-upper-bound`
  (only need feasibility+success at one point per chamber, not global
  optimality) → Farkas-style nonnegative-combination certificates (round 25's
  method) to prove a finite chamber family covers a box. This machinery is
  *n-general* already; only the actual list of chamber constructions (which
  pieces get cut, which fragments get pinned to which untouched values) is
  n=3(m=4)-specific and needs redoing for m=5.

- Cheap-kill candidates (do these before any new hand-derivation):
  1. **`unconditional-p2-threshold-closure`** is stated and certified for
     *general* $n$ (`lemmas/unconditional-p2-threshold-closure.md`: "Fix
     $n\ge1$... true for every $n\ge1$"). At $n=4$ this closes
     $p_2\le T/D_4=T/31$ **for free, zero new proof needed** — literal
     instantiation. This is the (b1) analog.
  2. **Case (a) analog bootstraps for free too**, already flagged in round 26
     ("$n=4$'s case (a) bootstraps for free... noted, not built"): peel $p_1$
     against $p_2$ via `generalized-peel-identity` (Theorem B$_k$, general
     $m$, general $k$ — certified, no $n$-restriction), reducing to the
     4-element tail $\{p_1-p_2,p_3,p_4,p_5\}$, which is now a fully general
     n=3 instance dischargeable **unconditionally** by round 27's
     just-completed milestone (`gap-filler-four-chamber-covering` +
     `case-b2-n3-covering-closure`, i.e. the complete $c(3)\le8/15$ for
     *every* legal marking). This closes $p_2\ge a_4T/2=8T/31$ for n=4 for
     free — it only needs to be *written up*, not re-derived. Recommend
     assigning this as a trivial "close it out" task to whichever builder
     picks up the census, since it further shrinks the open box before any
     new chamber work starts.
  3. **`p1-geq-half-closure-n4`** (round 28, already certified) closes
     $p_1\ge T/2$ in full.
  4. Combining 1–3: after these three free closures, the *only* genuinely
     open territory at $n=4$ is $p_1<T/2$ **and** $T/31<p_2<8T/31$ — this is
     the true, minimal target for the "fresh chamber census," strictly
     smaller than "all of $p_1<T/2$." State this explicitly in the outline so
     the builder doesn't accidentally re-attack already-closed sub-strips.
  5. **`bisect-subset-lemma`** is proved for *arbitrary* $m$ and *arbitrary*
     $S\subseteq\{1,\dots,m\}$ with $|S|\le n$ — literally, not by analogy
     (`lemmas/bisect-subset-lemma.md`, statement quantifies over general $m$).
     At $n=4,m=5$ this instantiates to all $2^5-2=30$ non-empty-cut,
     non-full-budget subsets, each giving a closed form
     $\Phi_S=(T+A(R))/2$, $R=$ complement — **zero new derivation**, purely
     mechanical substitution of $m=5$. This is by far the single biggest
     ready-made head start for the census and should be the first thing
     instantiated/tested, exactly as round 24 did at $n=3$ before finding it
     insufficient alone.

- Knowledge-base entries / already-certified lemmas to use (not knowledge_base.md
  generic entries — this problem's toolbox lives entirely in
  `results/imo-2026-03/lemmas/`):
  - `unconditional-p2-threshold-closure` (general $n$ — transplants free)
  - `generalized-peel-identity` (Theorem B$_k$, general $m,k$ — transplants free)
  - `gap-filler-four-chamber-covering`, `case-b2-n3-covering-closure`
    (the complete n=3 upper bound — needed as the tail-bound for the
    case-(a) analog's peel argument)
  - `p1-geq-half-closure-n4` (already closes $p_1\ge T/2$ at n=4)
  - `bisect-subset-lemma` (general $m$ — transplants free, 30 chambers at m=5)
  - `cross-piece-sign-assignment-identity`, `odd-run-reduction-lemma`
    (the evaluation engine every chamber derivation uses)
  - `p-space-chamber-vertex-theorem`, `within-chamber-affinity-theorem`,
    `feasibility-suffices-for-upper-bound` (the general finite-reduction
    framework that justifies "check finitely many chambers/vertices suffices")
  - The n=3-specific (NOT directly transplantable, need re-derivation at m=5):
    `double-sandwich-chambers` (Below/Above), `triple-pin-and-chamber-b1-b2`
    (Triple-Pin, Chamber B1/B2, P1P2-tied-to-p3), and the round-27
    Gap-Filler chambers (A, B, C, E via `pair-insensitivity-corollary`) — all
    explicitly stated as "$n=3$ ($m=4$) specific... not yet stated/verified
    for general n" in their own certification notes. Expect the m=5 analogs
    to be a *superset* in kind (e.g. a possible "Quad-Pin," 3 cuts on $p_1$
    pinned to $p_2,p_3,p_4$, is the natural one-index-up analog of
    Triple-Pin, using the extra cut budget n=4 provides over n=3's 3 cuts).

- Analogous past problems (crux corpus): searched `combinatorics` /
  `games-and-strategy` (39 cruxes) for anything resembling a
  Stackelberg cut-and-respond optimization on a sorted geometric/ladder
  sequence. **None found that are genuinely analogous** — the corpus's
  games-and-strategy entries are almost all pairing/mirroring/invariant
  strategies on discrete boards or token games, not continuous-value
  splitting optimization with a chamber/vertex LP structure. `aimo-0117`
  (dyadic-sequence + defer-commitment) surfaces on a naive keyword match but
  was already tried and rigorously ruled out (round 4, `claiming-order-
  invariant`, verdict RETHINK) — do not re-attempt. No crux move is
  recommended as a transplant for the chamber-census task itself; this is a
  case where the corpus genuinely has nothing close, consistent with prior
  rounds' finding that the core difficulty is a bespoke finite-covering/LP
  question, not a known combinatorial-games trick.

- Prior progress: see `results/imo-2026-03/current.md` and
  `approaches/lp-duality-certificate.md` (~6900 lines) for full detail.
  Summary relevant to this lens: $n=3$ upper bound $c(3)\le8/15$ is fully,
  non-numerically closed for every legal marking (round 27). At $n=4$: the
  $p_1\ge T/2$ half is fully closed (round 28, `p1-geq-half-closure-n4`, via
  Theorem A + Theorem C' reusing the complete $P(4)$/n=3 result as the
  one-level-down tail bound). The $p_1<T/2$ half is completely untouched.

- Dead ends (do not retry):
  - Dropping the $p_1<T/2$ restriction from the n=3 5-chamber family —
    refuted with an explicit counterexample
    ($p=(3/5,9/40,29/200,3/100)$, round 26) — the Triple-Pin chamber's
    formula derivation genuinely uses $p_1<T/2$ to pin an ordering; expect
    the same care to be needed at n=4 (i.e. do not assume any n=3 chamber's
    formula survives verbatim outside its stated ordering hypotheses).
  - `box-corner-tail-vertex-decomposition` (refuted at both $n=3,4$ by direct
    computation, round 22) — do not re-attempt a "reduce case (b2)/(p1<T/2)
    to the box corner" shortcut.
  - `bijective-mersenne-pairing`, `integer-lattice-reduction` (round 6 dead
    ends on an unrelated front of the problem, not this lens, but flagged so
    no one re-imports their mechanism into the chamber census either).
  - `claiming-order-invariant` / `aimo-0117` transplant (round 4, RETHINK) —
    irrelevant to chamber census specifically, but surfaces on keyword search
    so flagging again here to save a wasted look.

- Small-case / intuition notes (conjectural, not proved):
  - The round-24-style coverage tests at n=3 needed 20 chambers (15 free
    Bisect-Subset + 5 hand-derived) to hit exact zero-residual on ~5000
    exact-`Fraction` points. At n=4/m=5 there are 30 free Bisect-Subset
    chambers (vs. 15 at n=3) — a bigger free head start in absolute count —
    but the box itself is also higher-dimensional (3 free coordinates
    $p_1,p_2,p_3$ given $p_4,p_5$ determined by descending order + total,
    vs. 2 free coordinates at n=3), so **conjecture, not yet checked**: the
    coverage-fraction from Bisect-Subset alone may be lower at n=4 than at
    n=3, consistent with the round-28 explorer's 28%→64% uncovered-density
    growth signal cited in `current.md`. This should be checked numerically
    as the very first step (opening 3 above) rather than assumed either way.
  - No small-case (e.g. $n=1,2$) sanity check is needed here since the
    machinery (Bisect-Subset, threshold closures) is already certified
    general-$n$ and re-verified at $n=1,2,3$ elsewhere in the file; the open
    question is purely "how big is the m=5 hand-derived residual family,"
    which is an empirical/derivational question, not a small-case one.
