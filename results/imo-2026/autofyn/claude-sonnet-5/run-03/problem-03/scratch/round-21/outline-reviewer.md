# outline-reviewer report — round 21, imo-2026-03

## Inputs read

- `/tmp/round-21/proof-outliner.md` (no new approach opened; both live
  approaches revised in place with "Round 21 target" sections).
- `results/imo-2026-03/approaches/self-similar-induction-on-n.md`, new
  section at line 6037 ("Round 21 target: close the General
  Cardinality-Constrained Half-Sum Lemma via the canonical-form
  pigeonhole + pairing route").
- `results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md`, new
  section at line 4054 ("Round 21 target: a genuine two-region
  case-split for $n=3$").
- `results/imo-2026-03/approaches/.ranking.json` (both live approaches
  `stale: true` going into this round, reflecting round-20's recorded
  "advanced" outcomes not yet folded into Elo).
- `results/imo-2026-03/approaches/lp-duality-split-polytope.md` (dormant,
  last round-18 light dispatch; not revised this round, no action needed).
- `results/imo-2026-03/current.md` (Status `partial`, both live
  approaches CHANGES REQUESTED at round 20).

## Soundness vetting of the two new outline steps

### 1. `self-similar-induction-on-n` — Step A/B pigeonhole + pairing sketch

**Step B (Active-Γ-Subset Alternating Sum Lemma) — checked directly, sound.**
For a nonempty subset $A=\{2^{i_1},\dots,2^{i_p}\}$ of distinct powers of
$2$ sorted decreasing $a_1>\cdots>a_p$: for any two distinct powers
$2^i>2^j$, $2^i-2^j=2^j(2^{i-j}-1)\ge 2^j$, so each adjacent pair
contributes $a_{2t-1}-a_{2t}\ge a_{2t}\ge 2^0=1$ whenever the pair's
smaller value is itself $\ge1$ (true since every level value is
$2^{\ge0}=$ integer $\ge1$); if $p$ is odd the leftover term $a_p\ge1$
directly. So the claimed $\ge1$ bound holds by the outline's own
stated mechanism — this sub-step is elementary and correct as sketched,
not a red flag.

**Step A (pigeonhole) — plausible but correctly not yet proved; the
outline's own caution is appropriate.** The sketch (odd $n_j\ge1$ cost
per inactive Γ-level, even $t\ge2$ cost for an inactive free block,
budget $k+1$, parity argument forcing $S$ even when all-inactive) is a
reasonable line of attack, and the outline explicitly (correctly) flags
that the non-integer-$S$ case (when $t\ge1$) is NOT covered by the
explorer's sketch and must be handled separately — this is the right
caution, not an overclaim. No flaw found in the sketch as stated; the
risk is entirely in the unwritten details, which the outline correctly
defers to the builder rather than asserting closed.

**Step C — correctly identified and flagged as the one genuinely open
case, not glossed over.** The outline explicitly warns against assuming
Step B's bound dominates Step C (numeric pattern only, not proof) and
gives two concrete sub-task options (exchange/domination generalizing
General Pairwise Reduction Lemma, or casework generalizing the closed
$k=2$ case). This is honest scoping, not a hidden gap dressed as solved.

**Verdict: sound to build.** No logical flaw found in Steps A/B as
sketched; Step C is honestly left open with concrete sub-tasks, not
assumed. One minor **documentation defect, not a soundness issue**:
the file's very last line (6103) is a dangling fragment — "passed, no
counterexample found); not proved for general $k$." — apparently a
merge artifact from editing, not attached to any sentence. Flagged for
the builder to clean up in passing; does not affect the mathematical
content above it.

### 2. `global-lp-vertex-sufficiency` — two-region case-split for $n=3$

**Coherence of $p^\dagger$ and $c(3)$ — checked against already-certified
facts in the file, consistent.** $p^\dagger=(6/15,5/15,4/15,0)$ sums to
$1$; $g_1=p_1-p_2=1/15$, $g_2=p_2-p_3=1/15$, both equal to
$\gamma(3)=1/(2^4-1)=1/15$ (matches the file's own certified $\gamma(n)$
formula used throughout, e.g. in the $n=2$ closure sections); $g_3=p_3-p_4
=4/15$. And $c(3)=\tfrac12+\tfrac{\gamma(3)}2=\tfrac12+\tfrac1{30}=
\tfrac{8}{15}$, matching the value cited elsewhere in `current.md` and
prior rounds. No internal inconsistency found in the premise.

**Two-region requirement is well-posed and correctly guards against the
single-point trap this exact approach fell into before.** The outline
explicitly requires: (a) an *exact* algebraic boundary between Region I
and Region II (not left at "some $\varepsilon$"), (b) Region I's
construction verified throughout the region, not just at the corner
$p^\dagger$, and (c) explicit boundary-matching to jointly cover all of
$B(3)$. This is exactly the discipline needed given round 20's history
of two "natural" global constructions failing broadly (not at a sliver)
once actually checked by worst-case LP rather than sampling — the
outline does not repeat that mistake; it pre-empts it by making the
region-covering requirement mandatory and explicit.

**The "spare third cut touches $p_4$" idea is untested but not
unreasonable.** All eight prior single-mechanism constructions tried by
this round's explorer left $p_4$ untouched and all eight failed
somewhere — a real, exhaustively-checked (not sampled) finding per the
outliner's report. Using the one spare cut ($n=3$ allows up to 3 cuts;
all eight refuted constructions used only 2) to directly involve $p_4$
is a genuinely new idea not previously attempted, consistent with (not
contradicted by) the diagnosed failure pattern.

**Verdict: sound to build.** No flaw found in the region-split framing;
the explicit demand for an exact (not numeric) boundary and a
whole-region (not point) proof is the correct fix for the exact failure
mode that killed the two previous $n=3$ attempts.

## Ranking

Both live approaches carried `stale: true` from round-20's recorded
"advanced" outcomes (self-similar-induction-on-n: closed the flagged
cross-gap-same-parity gap via three certified lemmas, general-$k$
closure still open; global-lp-vertex-sufficiency: fully closed the $n=2$
Existence Theorem plus a genuine $n=3$ negative result). Both are
real, independently-verified, certified milestones of comparable
weight — one closes an internal combinatorial gap exactly as flagged,
the other closes an entire finite sub-case end-to-end plus narrows the
next case. Folded as a **draw** via `update_ranking` (no other approach
had a fresh outcome to fold this round — `lp-duality-split-polytope` and
the rest are untouched/dormant):

| slug | elo (post-update) | stale |
|---|---|---|
| self-similar-induction-on-n | 1610.23 | false |
| global-lp-vertex-sufficiency | 1599.57 | false |

Both remain the top two of the field by a wide margin over the dormant
approaches (next highest: `greedy-reduction-geometric` 1698.6 — note
this is stale-but-untouched since round 12, not re-evaluated this round
per the outliner's plateau-check finding of no shared-wall plateau
justifying reopening it now; `lp-duality-split-polytope` 1532.5).

No new approach registered this round (outliner opened none; the
plateau-check explorer found no dead plateau justifying a third slot,
per CLAUDE.md's own instruction not to open one without real
justification).

## Build set

Both new outline steps pass soundness vetting — no logical flaw found in
either; both correctly and honestly scope their genuinely-open residual
(Step C for self-similar; the exact-boundary derivation and
whole-region proof for global-lp) rather than assuming it closed.

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency
