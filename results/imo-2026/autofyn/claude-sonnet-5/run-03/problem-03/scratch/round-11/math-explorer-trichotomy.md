## imo-2026-03 (lens: the `self-similar-induction-on-n` j>=2 trichotomy, and gap (b)(ii))

### What Proposition C / Reduction B / the middle regime precisely state
(re-derived from `results/imo-2026-03/approaches/self-similar-induction-on-n.md`,
lines ~744-1130; these are exactly the definitions, verified against the file,
not paraphrased loosely)

Setup: fix `m>=1`, assume `T(m-1)` holds. `B={b_1>=...>=b_{j+1}}` (`j>=1`)
partitions `2^m`; `S` is an actual refinement of `Gamma_{m-1}` using `c` cuts,
`j+c<=m`; `mu:=max(S)<=2^{m-1}`. Target: `OddSum(B∪S)>=2^m`. The exhaustive
trichotomy on `b_1` vs `mu` vs `2^{m-1}`:

1. **`b_1>=2^{m-1}` (Proposition C's Case A).** Peel `b_1`; the residual
   target `U(m,k): OddSum(B'∪S)<=2^m-1` (`B'=B\{b_1}`, sum `<=2^{m-1}`) is
   shown, via the z-trick (Lemma Z: `EvenSum(X)=OddSum({z}∪X)-z` for
   `z>=max(X)`, applied with `z=2^{m-1}`), to be **logically equivalent** to
   `OddSum(B''∪S)>=V''` where `B'':={2^{m-1}}∪B'` has `j+1` parts (one MORE
   than `B`'s `j+1`... actually one more than `B'`'s `j`, same count as `B`)
   and `V''=2^{m-1}+sum(B')∈[2^{m-1},2^m]`. **Proved circular**: reduces to
   an equally-hard-or-harder instance of the same family `G(m,k;V)`, not a
   smaller one. This is a genuine, fully proved dead end for the "peel top
   fragment, bound residual by one more application of the same trick" idea.

2. **`b_1<mu` (Case B, `Reduction B`).** `mu=max(S)` is the global max; peel
   it instead (peel from the TAIL side): `OddSum(B∪S)=mu+EvenSum(B∪S')`
   (`S'=S\{mu}`), giving the exact equivalence `OddSum(B∪S)>=2^m <=>
   OddSum(B∪S')<=2^m-1` =: `Case-B(m,k)`. This reduction IS proved (clean
   algebra, reviewer-independently-checkable), but the resulting target
   `Case-B(m,k)` itself is **not proved**, only numerically supported (round
   5's near-miss search, best found `62.02` vs target `63` at `m=6`).

3. **`mu<=b_1<2^{m-1}` (the middle regime).** Neither mechanism applies:
   Case A's z-trick needs `b_1>=2^{m-1}` specifically (so that
   `sum(B')<=2^{m-1}` and `z=2^{m-1}>=max(B')` holds); Case B's peel needs
   `b_1<mu` specifically (so `mu` is the unique global max). This band is
   **genuinely open, not even reduced to a candidate target** — the weakest
   point of the whole trichotomy, and the file is explicit no reduction has
   been found here at all (as opposed to Case B, which at least has a
   reduced-but-unproved target).

The round-10 finding (gap (a) of the window) shows the endpoint-optimality
of Branch I.A reduces EXACTLY to `OddSum(D∪Gamma_{ell-2})>=2^{ell-1}`, which
IS an instance of this same `j>=2`, tail-untouched, top-split-into-`|D|`-
fragments family (i.e. it lands specifically in a mix of regimes 2/3 above,
one level down at `m=ell-1`), confirming these are the same wall.

### Is the round-7 "no additive/per-piece decomposition survives" diagnostic still valid here? Yes, and it explains *why* regime 3 is stuck
Both Case A (circular) and Case B (reduced-but-open) are single-scalar-peel
arguments: peel one designated element (either `b_1` or `mu`), and bound the
`EvenSum` of everything else by comparing to a SINGLE global threshold
(`2^{m-1}` or `mu`). Regime 3 is exactly the band where **no single
peel-then-bound-the-rest choice is available** — both `b_1` and `mu` are
simultaneously "too large to ignore, too small to dominate." This is a
structural instance of the round-7 diagnostic: a bound decomposable into "one
extracted term + one bound on the remainder" cannot see the interaction
between `B`'s internal structure and `S`'s internal structure once neither
side dominates the merge outright.

### A genuinely different mechanism: LP/vertex framing (this round's new finding, numerically checked)
**Key structural observation (verified computationally below, not previously
used in this approach file):** for FIXED `S` (or fixed `T`), and varying `B`
(resp. `D`) subject to `sum(B)=V` fixed and a fixed *interleaving pattern*
between `B`'s sorted values and `S`'s sorted values (i.e. fixed relative rank
positions — which "cell" of the arrangement `B` sits in), `OddSum(B∪S)` is an
**affine-linear function of `B`'s coordinates** (a 0/1-coefficient sum
picking out exactly the elements of `B` landing at odd merged rank). This is
the *same* structural fact — cell-wise affineness of a rank-based sum under a
finite-candidate-list of ordering functionals — that underlies the
`global-lp-vertex-sufficiency` approach's now-largely-closed **Finite-Cell
Affine-Vertex Reduction Theorem** and **Region-Vertex Classification
Theorem** (`lemmas/finite-cell-vertex-reduction-and-region-classification.md`).
Consequently: maximizing `OddSum(B∪S)` over `B` in the polytope `{sum(B)=V,
b_i>0, b_1<2^{m-1}$ (or $\ge\mu$, whichever regime), $\le j{+}1$ parts}` within
one interleaving cell is a genuine **linear program**, so the maximum is
attained at a **vertex** of that cell — a configuration with as many active
ties as the dimension allows (ties among `B`'s own coordinates, or `B`
touching a cap/floor boundary, or matching a value of `S`). This gives a
concrete, checkable route into the middle regime that is NOT another
scalar-peel argument: enumerate the finitely many cell/vertex types for a
GIVEN small `j` (piece count of `B`) and `S`-structure, and evaluate `OddSum`
exactly at each vertex, exactly as `global-lp-vertex-sufficiency` did for its
own (different) polytope.

**Numerical stress-test done this round (evidence, not proof).** Random
search for the maximizer of `OddSum(D∪T)` at fixed budget `W` (the
gap-(a)/gap-(b)(ii) setting, `ell=3`, `T=Gamma_2=(4,2,1)`, `eps=0.3`) over
admissible `D` with `|D|=2` and `|D|=3` at several `W` in the window: the
numerically-found maximizers consistently collapse to **near-tied
configurations** (e.g. at `W=W_top=4.3`: best `D≈(2.15,2.15)` for `|D|=2`,
best `D≈(2.00,1.15,1.15)` for `|D|=3` — two of the three coordinates tied),
i.e. vertex-like structure with active ties among `D`'s own coordinates
(consistent with, and a first piece of direct evidence FOR, the LP-vertex
picture — a genuinely new observation for this approach, not previously
noted). The achieved values (`~7.15` for both `|D|=2,3`) sit strictly below
the claimed bound `2^ell+eps-1=7.3`, consistent with (not a proof of) the
still-open claim, and matching the already-proved `Theorem W` endpoint margin
`eps/2=0.15` (`7.3-7.15=0.15`) almost exactly — a good sanity check that the
search is finding the true extremum, not an artifact.

**Caveat, honestly stated:** this is a genuinely different *mechanism*
(vertex/LP framing vs. scalar peeling), and the numerical evidence supports
that it is the right lens, but **no vertex classification for this specific
polytope family (varying `j`, varying `S`-structure across all `m`) has been
attempted or completed this round** — it is a real opening, not a result.
The main open technical question to hand the outliner: does the interleaving-
cell count stay bounded (or grow tamely) as `m,j` grow, the way
`global-lp-vertex-sufficiency`'s region-only candidate list did (that
approach's own remaining obstruction, the `Sigma`-shape part of `Q`, is
precisely "no bound on the candidate/cell count as a function of `n`" — the
SAME open question would likely recur here). This is worth flagging as a
structural parallel: **the two approaches' hardest remaining gaps
(`self-similar-induction-on-n`'s middle regime / gap-(a)/(b)(ii), and
`global-lp-vertex-sufficiency`'s `Sigma`-shape candidate classification) may
be the same underlying combinatorial-classification problem in different
notation** — worth having the outliner or a future explorer check this
directly (do the two approaches' "cells"/"Sigma-shapes" correspond under the
`p_i <-> piece values` dictionary?).

### Gap (b)(ii) specifically (piece-cap-saturated sub-case)
Precise statement (from the file, lines 2295-2360): given `D` admissible at
budget `W_1` with `|D|=ell` (cap saturated — TPI's "add a new tiny piece"
move is unavailable since it would exceed the piece cap), and `W_2>W_1` in
the window, must show some admissible `D'` at `W_2` (still `|D'|<=ell`) has
`OddSum(D'∪T)>=OddSum(D∪T)`. The file notes the natural move ("increase an
existing element") is unsafe in general because increasing a value at an
EVEN rank can strictly decrease OddSum — already diagnosed (certified
Schur-monotonicity dead end) as not simply true.

**New angle from the LP-vertex framing:** if the maximizer of `f(W)` at
`W=W_1` is (per the LP-vertex picture above) a *vertex* of its cell — i.e.
has several tied coordinates — then "increasing an existing element" should
specifically target the SMALLEST tied group (the one furthest from the
budget-cap boundary) so that the move stays inside a single cell (no rank
crossings) as long as possible; a rank crossing is exactly where OddSum can
drop. This suggests the right sub-mechanism is: (1) show the maximizer at
`|D|=ell` is a vertex with a *specific* tie pattern (needs the vertex
classification above); (2) show the specific "add mass to the smallest
element" move, followed if needed by one exact single-insertion correction
(reusing the ALREADY-CERTIFIED Single-Insertion Lemma from Round 4, which
gives the exact `Delta(AltSum)` for inserting/moving one value at an
arbitrary sorted position) exactly compensates any rank crossing. This is
speculative — not attempted or verified numerically this round beyond the
vertex-collapse observation above — but it directly reuses two
already-certified tools (Single-Insertion Lemma, TPI) instead of introducing
new machinery, which is attractive given time budget.

### Cheap-kill / sanity checks done
- Reconfirmed `Theorem W`'s margin `eps/2` numerically via a fresh,
  independent random search (not reusing the approach file's own script),
  `ell=3, eps=0.3`: found max `OddSum(D∪T)≈7.15` at `W_top=4.3` vs. claimed
  bound `7.3` — margin `≈0.15=eps/2`, matches exactly. This is a genuine,
  independent cross-check of already-certified `Theorem W`, not new content,
  but confirms the certified lemma is trustworthy as a base for further work.
- Checked that `Case-B(m,k)`'s near-miss numeric evidence (round 5's
  `62.02` vs `63` at `m=6`) is consistent with the observed pattern here
  (small margins, ~1-2% of `2^m`), suggesting the true extremal
  configurations across all three regimes are "near-boundary vertices," not
  interior points — further circumstantial support for the LP-vertex framing
  over trying yet another scalar bound.

### Candidate technique(s) to hand the outliner
1. **LP/vertex framing (new opening, this round):** treat `OddSum(B∪S)`
   (resp. `OddSum(D∪T)`) as cell-wise affine in `B` (resp. `D`) and reduce
   the middle regime / gap (b)(ii) to a finite vertex enumeration, directly
   reusing the machinery-style (not the literal lemmas, since the domain
   differs) of `global-lp-vertex-sufficiency`'s Finite-Cell Affine-Vertex
   Reduction Theorem and Region-Vertex Classification Theorem. This is a
   genuinely different mechanism from every scalar-peel attempt so far and
   has first-pass numerical support (vertex-like maximizers observed).
2. Reuse of already-certified tools within the new framing: Single-Insertion
   Lemma (exact `Delta AltSum` for one-value insertion at any rank) as the
   "one-unit-move" primitive for gap (b)(ii)'s tie-shifting argument.
3. Do NOT retry: Schur-monotonicity / majorization-based "shift mass toward
   larger element" arguments for gap (b)(ii) (already certified dead end,
   round 10 file); abstract dual-sum bounds like Lemma X′ (round 2, disproved);
   the literal peel-of-current-max-in-AltSum-language (round 4, shown
   identical to Proposition C, no new content).

### Knowledge-base / cross-approach entries to use
- `results/imo-2026-03/lemmas/finite-cell-vertex-reduction-and-region-classification.md`
  (the Finite-Cell Affine-Vertex Reduction Theorem + Region-Vertex
  Classification Theorem — the template mechanism to adapt).
- `results/imo-2026-03/lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`
  (Companion Peeling Lemma, still needed for the endpoint reductions).
- Round-4's Single-Insertion Lemma and AltSum reformulation (in the approach
  file itself, not yet a separate certified lemma file — check before
  reusing whether it needs re-certification).
- KB `General Proof Methods` — "Pigeonhole / extremal" and "Constructive vs.
  existence" are the closest generic KB entries; the LP-vertex mechanism
  itself is not a named KB entry, it is a cross-approach borrow from
  `global-lp-vertex-sufficiency`'s own custom machinery.

### Analogous past problems (crux corpus)
Searched `combinatorics`/`algebra` domains, subtopics `extremal-principle`,
`games-and-strategy`, `inequalities-SOS-and-convexity` for merge/rank/vertex/
linear-program language. Best candidate:
- **`aimo-0146`** (`extremal-principle`) — "When a relaxed optimum exceeds
  the target by a fixed gap and is attained only at one profile, close the
  gap by re-imposing on that exact profile a structural constraint the
  relaxation discarded" and "verify a local-rerouting move never decreases a
  vertex-degree functional." This is the crux already flagged and partially
  used in round 9 (Single-Insertion Lemma as the "unit-move" primitive); it
  remains the best analogue for the "vertex + local move preserves/improves
  functional" flavor needed for gap (b)(ii)'s tie-shift argument, though it
  is a graph problem, not a merge/OddSum problem, so the move itself must be
  reproven from scratch (per CLAUDE.md — crux is a hint, not a citation).
No corpus entry found that is a direct analogue of "maximize an odd-rank sum
of a merge of two constrained multisets" (a fairly bespoke combinatorial-
game object); the closest generic pattern is standard LP-vertex/extremal-
principle reasoning, not a specific matched problem.

### Prior progress (recap, all already certified/reported in current.md)
- Gap (b)(i): fully closed (Lemma TPI).
- Gap (a): exactly reformulated (not closed) to
  `OddSum(D∪Gamma_{ell-2})>=2^{ell-1}`, shown to be an instance of the
  same open trichotomy one level down.
- Case A of the trichotomy: proved circular (dead end for scalar peeling,
  not a bug — a genuine structural fact).
- Case B: reduced (proved) to `Case-B(m,k)`, itself open, numerically
  supported (round 5, `m<=6`).
- Middle regime: no reduction at all yet, genuinely the weakest link.
- Gap (b)(ii): open, diagnosed as needing a rank-crossing-safe "mass
  increase" argument; naive Schur/majorization approach already refuted.

### Dead ends (do not retry)
- Case A's z-trick applied a second time / any "peel top fragment then
  scalar-bound the rest via a single power-of-2 landmark" scheme for the
  middle regime or Case B — proved circular in Case A, and the middle
  regime's own obstruction is precisely that no such single landmark `z`
  exists there (neither `z=2^{m-1}` nor `z=mu` works).
- Abstract dual-sum bound "Lemma X′" (round 2, disproved by two explorers).
- Schur-monotonicity / majorization "shift mass toward larger element" for
  gap (b)(ii) (certified dead end per round 10's own note).
- Decoupling fragment count from the real cut budget, or using an abstract
  tail with only a bare OddSum/EvenSum bound instead of genuine geometric
  structure (round 3, explicit counterexamples found — the theorem is false
  in these generalized forms).

### Small-case / intuition notes (labeled conjecture)
- Numerically (this round, `ell=3`, independent script), the maximizer of
  `OddSum(D∪T)` at fixed budget in the window is a near-tied (vertex-like)
  configuration, not an interior generic point — conjectured to generalize:
  the middle regime's and Case-B's true extremal `B`/`D` are always vertices
  of the relevant interleaving-cell polytope (a natural LP-optimality
  conjecture, not proved).
- The margin at the true optimum (`~0.15` at `ell=3, eps=0.3`) matches
  `eps/2` extremely closely even in this different (`|D|=2,3` free) setting,
  suggesting the SAME extremal family (few large near-equal pieces plus
  possibly small leftover) may govern all three regimes of the trichotomy,
  not just Theorem W's specific endpoint witness — worth checking directly
  in the vertex-classification if pursued.
