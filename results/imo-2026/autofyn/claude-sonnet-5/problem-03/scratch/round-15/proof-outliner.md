## imo-2026-03

potential-weighting-upper-bound: revise (in place — no split, per CLAUDE.md single-gap-trap rule)
Target: the full theorem — Xiang Yu's optimal cutting-phase value equals `h(A,m)` exactly for the
  dyadic construction and, via the still-open upper bound, this is the extremal value for every `n,m`
  (the lower bound side is already unconditionally closed by the benched `dyadic-cascade-induction`
  approach; this file owns the matching upper bound, reduced via §17's Non-Matching-Witness criterion
  to Claim A / Sharp Argmin Recovery on the scope family `\mathcal F`).
Technique: strong induction inside `\mathcal F`'s DELETE/KEEP/MATCH recursion (Generalized
  Multi-Background Peeling Lemma), now sharpened to induct on TRUE-ARGMIN-DESCENDED nodes specifically
  (a strictly narrower, newly-precise scope discovered this round), reducing Claim A to three named
  sub-lemmas (Gaps 1a/1b/1c) that this round's reconciliation shows are more entangled than previously
  tracked — Gap 1a's general-`q` MATCH branch and Gap 1c's half-step lemma are literally the same
  inequality once correctly scoped.
Skeleton (revised, full detail in `results/imo-2026-03/approaches/potential-weighting-upper-bound.md`
  §17-§23; §23 is this round's new material):
  1. Reduce the theorem's upper bound to Claim A via the certified Non-Matching-Witness Criterion (§18.4,
     proved).
  2. Reduce Claim A to the base-generator "trigger" case via the certified Shrink-List Monotonicity
     Corollary, giving the free half `M<=D` unconditionally (§22.1, proved).
  3. Close the reverse half `M>=D` (Deletion-Suffices-for-k*) via the Per-Partner Domination Lemma
     `A_{3,l}>=min(A_1,D_l)`, proved in full for `q<=3` (§22.2, proved), open for `q>=4`.
  4. NEW this round (§23.1): split `q>=4` into `q=4` (mechanical, extends the `q=3` Rank-Extraction
     technique directly, no new lemma — open gap, not yet attempted with correct framing) and `q>=5`
     (needs the half-step lemma, precisely rescoped to "true-argmin-descended" nodes).
  5. Prove the half-step lemma `OPT_{+1}(C u {d},X) >= OPT_{+1}(C,X)` at true-argmin-descended scope
     (§23.1) — this simultaneously supplies Gap 1a's `q>=5` MATCH branch (via a spelled-out reduction
     chaining half-step + the certified Shrink-List lemma) AND Gap 1c directly. Open gap.
  6. Supply the generalized `A_1`-bound family for Gap 1a's `q>=5` DELETE/KEEP branches (§22.2 next
     step (ii)) — separate from the half-step, still needed. Open gap.
  7. Prove Gap 1b's Sum Bound: base case `w_1>=2|c_1-c_2|` first (§23.3, currently ZERO proof attempts
     on file, only numerically corroborated), then a recursion-DEPTH strong induction (not flat outer
     `|rest|`) for the inductive step, handling argmin-tie out-of-scope (`h=1`) filtering and
     continuous-interval tightness explicitly. Open gap.
Key lemmas (claim + mechanism):
  - Shrink-List Monotonicity (CERTIFIED, `lemmas/shrink-list-monotonicity.md`) — deleting a list
    element is a valid (possibly suboptimal) witness since deleted elements contribute 0 to `e`; one-
    line bijection extension argument.
  - Per-Partner Domination Lemma, `q<=3` (proved in §22.2) — because a singleton residual list has
    only 2 selections (delete/keep), reducing to the certified General Rank-Extraction Identity's 3-way
    case split plus two free `A_1` bounds (`A_1<=b_0`, `A_1<=|b_0-w|`).
  - Half-step lemma (conjectural, §23.1, NEW precise scope this round) — because at the true-argmin-
    descended boundary the "which background value augments C" question has a sharp true/false
    transition (0/3270+0/690 true-argmin-scoped vs ~15-91% wrong-scope), confirmed by directly probing
    both sides; not yet proved, only the correct hypothesis is now pinned down.
  - Background-Release Domination Lemma (NEW, general, unconditional, §23.2) — because releasing one
    background element back to the free list is always a valid witness (min of two explicit candidate
    values); recommend certifying standalone, but NOT load-bearing for Gap 1a's closure — both natural
    chaining routes into Gap 1a are refuted this round (38% and 16% violation rates).
  - Sum Bound base case `w_1>=2|c_1-c_2|` (§23.3) — because the trigger `M<A_1` and k*'s global-argmin-
    ness together should force a factor-2 gap; mechanism not yet identified, zero proof attempts exist,
    flagged as the single most under-attacked "should-be-easy" item in the whole population.
Open gaps: (1) Gap 1a q=4 [likely mechanical]; (2) Gap 1a q>=5 MATCH branch [reduces to half-step, not
  yet executed]; (3) Gap 1a q>=5 DELETE/KEEP branches [generalized A_1-bound family]; (4) the half-step
  lemma itself at true-argmin-descended scope [highest-leverage single item]; (5) Gap 1b base case;
  (6) Gap 1b inductive step as a recursion-depth induction.
Cases to cover: Gap 1a q=4 vs q>=5 split; half-step's own DELETE/KEEP/MATCH induction on |X|; Gap 1b's
  argmin-tie h=0 filtering and zero-slope (flat-interval) breakpoints vs strict breakpoints.
Watch out for: (i) never test/use the half-step lemma outside "true-argmin-descended" scope (§23.1's
  precise def) — wrong-scope tests give spurious ~15-91% failure that is a scoping artifact, not a
  counterexample; (ii) do not resurrect either Background-Release chaining route or the flat
  Rank-Extraction peel of `d_l` out of the whole optimal multiset — all three confirmed dead this round,
  same root cause (substituting a derived value for an original list element breaks monotonicity,
  positional not magnitude-based fix needed); (iii) do not attempt Gap 1b's inductive step before its
  base case is proved; (iv) proving the half-step alone does not close Gap 1a — the DELETE/KEEP branches
  need a separate generalized A_1-bound family.

dyadic-cascade-induction: no action (stays benched)
concavity-minimax-duality: no action (stays benched)
Justification for staying benched: neither this round's three explorer reports (all three scoped to
  potential-weighting-upper-bound's internal Gap 1a/1b/1c) nor any residual signal gives either
  bench-mate new leverage — dyadic-cascade-induction already unconditionally closed the entire lower
  bound (round 8, certified); concavity-minimax-duality's own Local Claim reduction (round 9) was
  already noted to give no new leverage on the theorem's actually-open items (general-`m` upper bound,
  general `n>=4`) even if closed. No un-benching this round.

No 5th slug opened. The population correctly stays at one active build target
(`potential-weighting-upper-bound`) per repeated multi-round confirmation; this round's work is a
same-framing revision (a sharper scope on an existing conjecture, a new lemma candidate, a corrected
induction variable), not a genuinely different top-level route, so it belongs in the existing file, not
a new slug.
