# Proof review — round 20 — imo-2026-03

Two built slugs reviewed adversarially, each with independent from-scratch
exact-`Fraction` verification scripts (not reusing the builders'). Full
scripts under `/tmp/round-20/scripts/`.

---

## 1. `self-similar-induction-on-n`

**Verdict: CHANGES REQUESTED. True Status: `partial` (matches the
builder's self-report).**

### What was checked and how

The dispatch specifically asked me to check whether the new **General
Pairwise Reduction Lemma** genuinely covers the different-Γ-gap,
same-rank-parity case the round-20 outline-reviewer flagged as
unaddressed by round 19's Lemma LNI and the outline's single-gap
pigeonhole.

I wrote an independent script (`verify_general_lemma4.py`) that:
1. Builds random feasible $R$ for $\mathrm{GCH}(k)$, $k=2,\dots,6$.
2. Picks two random distinct active free values.
3. Computes the **exact** maximal affine interval $[t_{\min},t_{\max}]$
   via exact breakpoint algebra (not a coarse numeric grid — my first
   attempt used a grid-stepping heuristic and produced ~7% spurious
   "violations," traced to grid-resolution artifacts near the domain
   boundary $\{0,\mathrm{cap}\}$; rewritten with exact algebra, this
   resolved cleanly). Also had to add the "coordinate reaching exactly
   $0$ or $\mathrm{cap}$ is removed from the multiset" handling
   explicitly (the proof's own case (ii)) — an initial version left a
   literal `0` in the reduced multiset, producing spurious infeasibility.
4. Moves to the theorem's prescribed endpoint and checks: AltSum
   non-increasing, active-free-value count strictly decreasing,
   feasibility preserved, sum preserved.
5. Classifies every trial by (same-gap/diff-gap) × (same-parity/
   diff-parity).

**Result: 59,952 trials, zero violations in every category**, including
**22,632 trials specifically in the flagged different-gap-same-parity
configuration** — a large, targeted sample of exactly the case in
question, not incidental coverage. I also reproduced the file's own
hand-built $k=6$ worked example ($x_0=20,y_0=3$): confirmed
$\mathrm{AltSum}=22$ exactly constant on the true maximal interval
$t\in(-1,1)$ and confirmed the value genuinely jumps to $23$ at $t=-3/2$,
which lies **outside** that true interval — the file's Step 0 prose lists
$t=-3/2$ among values it says give "$22$... within the segment's feasible
range," which is loosely worded (that $t$ is outside the range) but the
theorem's actual boundary claim ($t=\pm1$) is exactly correct — a
documentation looseness, not a mathematical error.

I additionally verified the **Finite Reduction Theorem** end-to-end:
4,000 trials of full iterated reduction to termination (`Fraction`
exact), zero non-monotonicity, zero infeasibility, zero non-termination,
max observed steps 6 (theorem bound: $\le k+1\le7$).

I re-verified the **achievability overclaim fix** (k≥3 chain+pair witness
vs. the separate k=2 witness $\{2,b,b\}$) is now internally consistent:
independently re-derived both closed forms in exact arithmetic
($k=3,\dots,7$ for the chain+pair formula, and $k=2$ for the separate
witness) — both give $\mathrm{AltSum}=1$ exactly in every tested instance,
matching the source file's corrected (split-by-$k$) claim precisely, with
no remaining cross-reference to the retracted round-19
internal-inconsistency.

### One error found (non-load-bearing, flagged for correction)

The source's own "why this closes the flagged gap" paragraph asserts
"same gap, same parity — vacuous, since two distinct values in one gap
are automatically adjacent hence opposite parity." **This is false when
$\ge3$ distinct active free values occupy one Γ-gap** (the two
*non-adjacent* outer values can share parity — e.g., three collinear free
values $x_1>x_2>x_3$ in one gap have parities $p,p+1,p\pmod2$, so $x_1,
x_3$ tie in parity). My stress test independently confirms this occurs
in practice (3,301 of the 59,952 trials fall in exactly this "same-gap,
same-parity" category) and confirms the Lemma still holds there (zero
violations) — because the Lemma's actual proof (the $\sigma=0/\sigma\ne0$
dichotomy) never invokes that vacuity claim; it is a purely descriptive
mis-classification in the exposition, not a gap in the mathematics. It
should be corrected in the source text (delete or fix the "vacuous"
sentence) but does **not** threaten the Lemma or Theorem's certification.

### Certification

**Certified** into
`results/imo-2026-03/lemmas/invisible-block-skip-fact-and-general-pairwise-reduction.md`:
- Invisible-Block Skip Fact (elementary, proved in full).
- General Pairwise Reduction Lemma (proved in full, strictly generalizes
  the certified Lemma LNI, independently confirmed to cover the flagged
  cross-gap same-parity case).
- Finite Reduction Theorem (proved in full via the above two plus a
  strictly-decreasing-potential termination argument).

### What remains open

The resulting finite combinatorial claim (AltSum $\ge1$ for the
"at-most-one-active-free-block" family, general $k$) is **not proved**
for general $k$ (proved $k=2$, numerically corroborated $k=3,4,5$) —
unchanged diagnosis from round 18/19: needs a genuinely more general
two-parameter family, not a single-parameter induction on $k$. This is
honestly scoped by the file, not overclaimed.

---

## 2. `global-lp-vertex-sufficiency`

**Verdict: CHANGES REQUESTED. True Status: `partial` (matches the
builder's self-report; the overall Existence Theorem for general $n$ is
not solved, but a genuine complete sub-milestone for $n=2$ is now
closed).**

### Task (a): $n=2$ achievability closure — independently re-verified, holds

Wrote a from-scratch exact-`Fraction` fine-grid search
(`verify_n2_shapes.py`) over each of the ten finite response shapes at
$p^*=(4/7,2/7,1/7)$, built directly from each shape's definition (not
from the file's algebra or the builder's script): 400-step grids for the
1-parameter shapes, 80-subdivision 2-simplex grids for the
triple-fragment shapes, $120\times120$ grids for the two-cut-different-
piece shapes.

**Result: the observed global minimum matches the file's claimed exact
value digit-for-digit in all ten shapes** — $5/7,4/7,5/7,9/14$ (single-
cut group), $4/7,5/7,9/14$ ($(2,0,0),(0,2,0),(0,0,2)$), $4/7,4/7,9/14$
($(1,1,0),(1,0,1),(0,1,1)$) — zero violations of $\ge c(2)=4/7$ anywhere.
Since each shape's $\mathrm{OddSum}$ is piecewise-linear, hitting the
exact claimed rational value on an independently-built fine grid across
all ten shapes is strong, not merely consistent, corroboration of the
casework proof. Combined with the already-certified upper-bound witness
(round 19), this genuinely closes $V(p^*)=c(2)$ exactly, both directions
— **a real, complete milestone: the full $n=2$ Existence Theorem.**
**Certified** into `results/imo-2026-03/lemmas/n2-achievability-theorem.md`.

### Task (b): $n=3$ negative finding — independently re-verified, holds (after fixing my own script bug)

Verified the $p_2,p_3$-pairing infeasibility point exactly
($p_2+p_3=0.5001>p_1=0.365\Rightarrow r<0$, confirmed).

For the $p_3,p_4$-pairing's closed form $\mathrm{OddSum}(M')=1-p_1$: my
**first** independent stress test (`verify_n3_negative.py`) omitted the
region $B(3)$'s own hypothesis $p_1<1/2$ and found ~43% of "feasible"
trials with $r'>p_2$ — apparently contradicting the file's claim that
this branch is vacuous. **This was my own script bug**, not a flaw in the
file: re-running with $p_1<1/2$ correctly enforced
(`verify_n3_negative2.py`) gives **zero** occurrences of $r'>p_2$ across
23,265 region-valid trials, and zero mismatches of the closed form
$\mathrm{OddSum}(M')=1-p_1$ — confirming the file's claim exactly. (This
reproduces a pattern flagged in prior-round reviewer notes: always
extract *every* side-constraint from the proof text, including
hypotheses stated elsewhere in the file, before writing a stress-test
harness.)

Independently reproduced the exact counterexample point
($p=(12821/36000,2077/7200,61/288,1723/12000)$, sum $=1$ exactly, all
gaps $>\gamma(3)=1/15$, $\mathrm{OddSum}(M')=23179/36000\approx0.6439>
c(3)=8/15\approx0.5333$ — confirmed digit-for-digit) and the hand-derived
LP worst case ($\inf p_1=16/45$ subject to feasibility) via an
independent `scipy.optimize.linprog` run (`verify_lp.py`): matches
$16/45\approx0.35556$ exactly.

**Conclusion**: both natural pairings of the 2-cut/6-fragment
single-piece-split construction are genuinely refuted as universal
$n=3$ upper-bound witnesses — a real, precisely-scoped negative result.
Correctly not proposed as a standalone lemma (matches the builder's own
scoping; negative/diagnostic findings are not independently certifiable
per established discipline).

### What remains open

$n\ge3$'s Existence Theorem (both directions) remains open; this round's
negative result narrows, but does not close, the search for an $n=3$
construction.

---

## Certification summary

- `lemmas/invisible-block-skip-fact-and-general-pairwise-reduction.md`
  — **certified** (new).
- `lemmas/n2-achievability-theorem.md` — **certified** (new).
- No lemma rejected this round (the one error found in
  `self-similar-induction-on-n` is a non-load-bearing prose
  mis-classification, corrected in the certified lemma writeup and
  flagged for the source file, not a rejection of the underlying
  theorem).

## `current.md`

Updated (I own this file). Prepended a "round 20" entry recording both
approaches' verdicts, certifications, and the residual gaps, ahead of the
existing round 19 history. Top-level `## Status` remains `partial`
(neither approach closes the problem's actual claim — determine $c$ for
general $n$ — only the $n=2$ instance is now fully closed).

## Ranker outcomes recorded

- `self-similar-induction-on-n`: `advanced` — closed the round-20
  outline-reviewer's flagged same-parity cross-gap case in full
  (certified), general-$k$ combinatorial closure still open.
- `global-lp-vertex-sufficiency`: `advanced` — closed the full $n=2$
  Existence Theorem (certified) plus a genuine $n=3$ negative result;
  $n\ge3$ remains open.
