# Build report — residue-invariant (imo-2026-04), round 1

**Status: solved.** Complete rigorous proof of both directions written to
results/imo-2026-04/approaches/residue-invariant.md.

## What I closed
- **G1 (alignment range-existence — the field's shared wall): closed.** Clean two-regime
  argument instead of a 3-window pigeonhole. Cut from the LARGEST-angle apex $A$; its cut-point
  angle $\angle APB$ fills the open interval $I_A=(\gamma,180-\beta)$ of length $\alpha$, with
  both endpoints non-multiples of θ (since β,γ are non-multiples and $180\equiv0$).
  - Regime $\theta\le60$ ($n\ge3$): max angle $\alpha\ge60\ge\theta$; equality $\alpha=\theta$
    forces equilateral = all angles $=\theta$, excluded by "no angle a multiple of θ", so
    $\alpha>\theta$ and Fact P1 (open interval of length $>\theta$ contains a multiple) applies.
  - Regime $\theta=90$ ($n=2$): only multiple in range is 90; the two base angles at the
    max-angle apex are both $<90$ (at most one angle can be $\ge90$), so $90\in(\gamma,180-\beta)$
    — the altitude cut. No $180/n$ lies strictly in $(60,90)$, so these two regimes are exhaustive.
- **G2:** the aligned multiple is a genuine triangle angle in $(0,180)$, hence a positive
  multiple $m\theta$, $1\le m\le n-1$ — closed.
- **G3:** "good child stays good" written explicitly (untouched base angle keeps its nonzero
  residue; sum stays 180 so $S\not\equiv0$ persists) — closed.
- Necessity: explicit good starting triangle (isosceles $(t,t,180-2t)$ avoiding a finite bad
  set); Lemma A both-children-bad exclusion fully derived for every apex.
- Sufficiency peel (Lemma C): forced $m\to m-1$ with the θ-child as immediate win, double-fork
  at $m=2$; terminates in $\le n-2$ steps.

## Verification done
- sympy/numeric: alignment interval contains a multiple of θ in 200000/200000 random
  (triangle, $n\in2..12$) trials with no angle a multiple of θ (0 failures).
- Facts P1/P2 (interval-contains-multiple) proved from scratch in-text.
- $n=2$ (altitude) and $n=3$ (60/120 split) worked explicitly and match the general strategy.

## Spec concerns
None. Answer $\theta=180/n$ ($n\ge2$) $\Leftrightarrow$ $\theta\mid180$ is exactly the dichotomy;
the stopping rule ("angle $=\theta$", not "multiple of θ") is respected — the peel is what
converts a general multiple down to exactly θ.

## Remaining
Nothing open in this approach. Promotable: Lemmas A (residue survival invariant), B (alignment
existence), C (θ-peel) — all proved in full.
