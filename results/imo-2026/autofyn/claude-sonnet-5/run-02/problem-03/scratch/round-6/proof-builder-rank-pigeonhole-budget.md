# Proof-builder report — rank-pigeonhole-budget, round 6

## What was done
Per the round-6 outliner's note ("apply this same §3 reduction again to
(3.4) itself... will either terminate in finitely many rounds or reveal
exactly which sub-range is the genuine obstruction"), generalized round 5's
single-step reduction into a clean **strong induction on tail length $m$**
(Theorem GC($m$), new §3 of the approach file).

**Result: Claim (A)'s Case II is now fully closed for every $n$,
unconditionally — no numerics needed.** This retires round 5's
"numerically confirmed for $n\le5$/$6$ only" status for inequality (3.4).

Proof sketch: base case $m=1$ is a 3-element median computation (direct).
Inductive step peels the dominant fragment $f_1$ via the already-certified
`sharp-dominant-removal-identity`, then a general rank-shift identity
(sum of even-rank elements of $U$ equals $\Phi$ of $U$ minus its strict
unique max — proved in full generality, reusable) reduces the target
exactly to GC($m-1$) applied to the one-level-smaller tail. The $\le m+1$
part-count budget is essential and threads correctly through the
recursion (tail length and budget shrink together by exactly 1 each level);
proved this is NOT droppable via an explicit 3-part counterexample when the
budget is violated.

Cross-checked with 200,000 exact-`Fraction` trials (random $m=1..7$, random
tails, random budgets/masses/partitions): zero violations, confirming both
the new Case II theorem and Case I numerically.

## Case I: not closed, but precisely diagnosed as the real wall
Attempted the symmetric peel for Case I (no dominant $F$-fragment; peel the
tail's own top $\tau_1$ instead). Showed this requires proving
$$A(F\cup\tau'')\ \le\ R(\tau'')+2\tau_1-s \tag{4.1}$$
— an **upper** bound on $A$ of a smaller same-shape instance. This is
exactly the ingredient missing from every approach in the population for
5+ rounds ($(\star\star)$ in `rank-tie-vertex-reduction`, the general
Missing Inequality in `greedy-halving-adversary`). So Case I is not an
easier residual of Claim (A) — it's a repackaging of the project's central
open obstruction. Ran an additional adversarial local-search (float
hill-climbing, not just uniform random) specifically hunting for a Case I
counterexample across $m=1..5$: worst margin found was $-1.4\times10^{-14}$
(floating-point noise, not a real violation). Strongly consistent with
Case I being true, but no proof found.

Recommended next step (written into the approach file): Case I's gap (4.1)
is exactly what an LP-duality certificate (`lp-duality-certificate`) or an
exact digit/carry evaluation (`integer-lattice-reduction`) would supply if
either succeeds — recommend this slug defer Case I to whichever sibling
produces an upper-bound tool, then re-import it to finish Claim (A) via
(4.1) in one line.

## File state
- `## Status`: still `partial` (Case I remains open, and Claim (B) is the
  sibling's job, untouched here).
- New promotable lemma written into the file: **Case-II Closure Theorem
  GC($m$)** — general (not ladder-specific), fully proved, not yet
  reviewer-certified. Recommend the proof-reviewer verify it and, if
  correct, promote to `lemmas/case-ii-closure-theorem.md` so
  `greedy-halving-adversary` and `rank-tie-vertex-reduction` can import it
  directly instead of re-deriving Case II.
- Open gaps section rewritten: gap (3.4) marked CLOSED; Case I is now the
  sole remaining gap in Claim (A), with its precise diagnosis (4.1) on
  file.

Full updated file: `results/imo-2026-03/approaches/rank-pigeonhole-budget.md`.
