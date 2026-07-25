# Build report — global-lp-vertex-sufficiency, round 11

## Dispatch executed

1. **Mandatory Section-1 textual fix.** Corrected item 1's degrees-of-
   freedom description from "a single free block designated across the
   whole shape" (contradicted the proof and the cited Two-Piece-Split
   Vertex Lemma) to "one free block per split piece" — matching the proof
   paragraph, verified against the correct mechanism used throughout the
   file.

2. **Intra-branch pairwise-order subtlety (explorer's second flagged
   gap).** Chose the explicit-enlargement route (option (ii) from the
   outline): added all pairwise differences among each shape $\sigma$'s
   own multiset $y_\sigma(p)$ (fragments + untouched pieces) to $L$, and
   proved a new **Rank-Pinning Lemma** — on any cell of the enlarged
   arrangement, the coordinate of $y_\sigma(p)$ at each sorted rank is
   fixed, so $f_\sigma(p)=\mathrm{OddSum}(y_\sigma(p))$ is genuinely a
   single affine formula on the cell (not just assumed). This closes a
   real gap in Lemma 4.1(b)'s proof as it stood through round 10, which
   pinned the *ordering between* branches via $f_\sigma-f_\tau\in L$ but
   never justified that each $f_\sigma$ is itself affine on a cell.
   Verified $L$ stays finite (finitely many $\sigma$, each with a
   bounded-size multiset $y_\sigma$), and that Lemma 4.2 / the Finite-Cell
   Theorem's proof are unaffected (they use only finiteness + affineness
   of $L$'s members, both preserved). Verified $Q_{\text{region}}$
   (already fully closed, round 10) is untouched — it only used region
   functionals, never the boxed group.

3. **Bounded-split-piece-count sufficiency (main new target).** Formalized
   the **General Multi-Piece Subset-Tie construction** (the natural common
   generalization of the certified Theorem 12, `s=1` case, matching
   Section 5's numeric $n=6$ witness's qualitative "tie fragments to
   untouched tail pieces" description) and derived its exact value via
   the certified Singleton-Interleaving Lemma (Theorem 9). Then proved,
   in full exact-arithmetic rigor (not numerically), the **Mass-Constraint
   Theorem**: any legal instance requires the split pieces' total mass
   $\Pi\ge1/2$. Applying this at the already-closed region vertex $e_0$
   (using the exact closed-form coordinates from Section 4.1 and the
   already-established bound $n(n+1)\gamma(n)<1$), this forces $s>(n+1)/3$
   split pieces — **unboundedly many as $n\to\infty$**, ruling out any
   fixed $s_0$ for this construction family. Verified the algebra
   independently in Python (exact `Fraction` arithmetic, $n=2,\dots,20$):
   the derived bound holds at every tested $n$, and the true asymptotic
   ratio $s/(n+1)\to1/2$, consistent with (and confirming, not just
   matching) the proved $>1/3$ bound.

   This is a genuine **negative result**, honestly scoped: it refutes only
   the "tie split-fragment to a whole untouched piece" mechanism, not
   fragment-vs-fragment tying (which Section 5's raw numeric fragment
   values — a near-equal cluster among fragments from *different* split
   pieces, not matched to any single untouched piece — suggests may be
   the real mechanism behind the round-10 numeric witness), nor
   non-tie-based constructions, nor the explorer's independent Opening 2
   (construction-side monotonicity toward the region's own facets). Both
   are flagged as the concrete next targets.

## Status

`partial` (unchanged) — the Existence Theorem itself is not established.
This round's contribution: two genuine soundness/rigor fixes (textual bug,
intra-branch rank-pinning gap) plus one fully rigorous negative result
that correctly rules out a specific, natural construction family and
precisely scopes what remains open.

## Proposed for reviewer certification (not self-certified)

- **Rank-Pinning Lemma** (Section 4) — closes a real gap in the Finite-
  Cell Theorem's proof chain.
- **General Multi-Piece Subset-Tie construction + Mass-Constraint
  Theorem** (Section 4.5) — a self-contained, reusable necessary-mass
  condition for a whole family of tie-based constructions; also a
  concrete negative finding worth recording as a documented dead end
  (analogous to the Candidate Swap Lemma refutation in
  `greedy-reduction-geometric`).

## File written

`/home/agentuser/repo/results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md`
(Status: `partial`) — Sections 1, 4 (definition of $L$ + new Rank-Pinning
Lemma), new Section 4.5, Section 6 ("what remains open"), header
"Approaches tried" and "Round 11 target," and "Promotable lemmas" all
updated in place; Sections 0, 2, 3, 4.1–4.4, 5 unchanged from round 10
(already correct and untouched by this round's fixes).
