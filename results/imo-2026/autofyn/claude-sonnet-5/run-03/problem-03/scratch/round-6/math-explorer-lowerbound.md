## imo-2026-03 (lower-bound side, three named open regions)

### (a) The width-1 sliver `2^(m-1)-1 < b1 < 2^(m-1)` in Case-B(m,k)

**New finding this round (numeric, high-confidence conjecture, not yet a proof):** the reduced
target for the sliver — `OddSum(B'∪T) ≥ 2^(m-1)` where `sum(B')=2^(m-1)+eps`,
`max(B')≤2^(m-1)-eps`, `T=Γ_{m-2}`, `eps=2^(m-1)-b1∈(0,1)` — appears to hold with an
**exact closed-form margin of `eps/2`**, not merely "some positive slack." I ran a
multi-restart Nelder–Mead global search (parametrizing the simplex via squared-and-normalized
coordinates, box-constraining `max ≤ cap`) over `B'` for `m=4,5,6` (clean, well-converged) and
`m=7,8` (less reliably converged at higher dimension — flagged below). At `m=6`, across
`eps∈{0.02,0.1,0.5,0.9,0.99}` and `nparts∈{m-1,m}` (the full allowed budget), the found global
minimum was **exactly** `2^(m-1)+eps/2` in every single trial (10/10 clean matches to 6 decimal
places) — i.e. the target holds with margin exactly `eps/2 > 0` for every `eps` in the open
sliver. At `m=4,5` the same clean `eps/2` pattern held. At `m=7,8` the optimizer sometimes got
stuck at *worse* (larger, hence still-safely-positive) local minima at higher `nparts` — this is
optimizer non-convergence, not evidence against the pattern (every found value, converged or
not, was still `> 2^(m-1)`; no violation was ever found across any trial at any `m` tested).

**The extremal-minimizer shape** (read off from the converged `m=4,5,6` optima): `B'` is a
scaled/shifted echo of the certified extremal boundary configuration `B*` one level down — a
geometric run `(2^(m-2), 2^(m-3), \ldots, 2^{q})` for the top entries, with the *bottom* two
entries tied at `(2^{q-1}+eps)/2` each (a symmetric split of one geometric level, mirroring
exactly how `B*` splits `T`'s bottom element). This is the same self-similar shape that made
`B*` extremal at the outer boundary (`eps=0` limit reproduces `B*` up to the missing outer
`{2^{m-1}}` piece already peeled off) — strong structural evidence the sliver is governed by the
*same* extremal family, one recursion level in.

**Candidate technique to actually prove the `eps/2` margin:** the extremal shape being an exact
echo of `B*` suggests the sliver should close by **applying Theorem 2's own two-sub-case
dichotomy recursively, one level down**, rather than by a single scalar refinement (Two-Level
Half-Bound) of the *whole* residual `B'∪T` at once. Concretely: split `B'` itself by its own
top fragment `b1'` vs. `max(T)=2^(m-2)` — this is literally a smaller instance of the same
tail-untouched dichotomy Theorem 2 already solved, but now the "outer sum" is `2^(m-1)+eps`
(not exactly `2^(m-1)`) and the cap is `2^(m-1)-eps` (not the a-priori `2^(m-1)`). A **one-more
free-parameter generalization of Theorem 2** (target value `V=2^(m-1)+eps` instead of exactly
`2^(m-1)`, and a matching cap parameter) is exactly the kind of extra degree of freedom
`self-similar-induction-on-n`'s own `G(m,k;V)` machinery (Round 4) was built for — this is a
concrete, not-yet-tried synthesis: **re-derive Theorem 2's proof with `V` as a free parameter
(not fixed at `2^m` or `2^(m-1)`) and prove the margin scales like `(V-2^(m-1))` linearly**,
which is exactly what the numerics show (margin `= eps/2 = (V-2^(m-1))/2` where
`V=2^(m-1)+eps`).

### (b) The general middle regime `μ ≤ b1 < 2^(m-1)` (round-4 trichotomy, non-tail-untouched)

This is strictly harder than (a): here `S` is a genuine refinement of `Γ_{m-1}` (not the fixed
`Γ_{m-1}` itself), so `μ=max(S)` ranges freely over `(0,2^{m-1}]`, making this a genuinely
2-dimensional open region (not a width-1 sliver). No approach has yet reduced this to a
concrete target the way Theorem 2 reduced the tail-untouched sliver. The most promising route
is the same `G(m,k;V)`-style generalization: the middle regime's natural reduction (by the same
peel-the-max-then-Companion-Peel mechanism used in Theorem 7 / Reduction B) should land on a
target of the shape `OddSum(B''∪S'') ≥ V''` for some `V''` depending on `μ` and `b1`, not
exactly `2^(m-1)` — i.e. this region *is* an instance of the still-unclosed general `G(m,k;V)`
family, not a separate problem. Nobody has carried out this reduction explicitly yet; it is the
natural next step, not a new mechanism.

### (c) The Leftover-Fragment Obstruction (interleaved top-tail-level-split case)

The obstruction is precisely: after peeling `b1` and then the partially-split top tail level's
own max `μ1`, the residual `S\{μ1}` still carries the *rest* of that level's fragments (summing
to `2^{m-1}-μ1`, an unknown quantity with unknown interleaving) — this residual is **not** of
the clean "Dominance-Chain `B''` plus untouched-top-levels refinement" shape Theorem 7 needs, so
the induction leaves its own hypothesis class.

**Candidate fix, concrete and not yet tried:** track the leftover mass `L:=2^{m-1}-μ1` as an
explicit extra parameter in a strengthened statement — i.e. prove a joint generalization
`Theorem 7'(m,k;L)` where the top tail level is allowed to be split into `(μ1, \text{rest})`
with `rest` summing to `L` and *of otherwise arbitrary further-split shape*, and show the
target degrades by at most a controlled function of `L` (plausibly linear, by analogy with (a)'s
`eps/2` finding). This is the same "extra degree of freedom" idea as (a) and (b) — **the three
open regions of the lower-bound problem all reduce, independently, to needing one additional
free parameter (`V` for the sliver / middle regime, `L` for the leftover fragment) tracked
through the peeling induction**, not three unrelated gaps. This is the strongest cross-cutting
finding of this round: the outliner should consider dispatching **one unified approach** that
builds `G(m,k;V,L)` or equivalent, rather than three separate patches, since the same missing
ingredient (a linear-in-the-extra-parameter refinement of the peeling/Lemma-B machinery) seems
to be needed in all three places.

### Cheap-kill candidates
None obvious for (b)/(c) — this is genuine casework, not something a parity/pigeonhole
shortcut resolves. For (a), the `eps/2`-margin conjecture, if it is exactly right, would itself
be a clean "cheap" closing lemma (a single linear-in-`eps` refinement of Lemma B) once proved —
worth a focused proof attempt before anything heavier, since the numeric pattern is unusually
clean (exact `eps/2` to 6 decimal places, not just "positive").

### Candidate technique(s)
- A **parametrized generalization of Theorem 2 / Lemma B with target `V` (not fixed at
  `2^m`/`2^(m-1)`)**, proving the margin is linear in `V-2^(m-1)` — directly reuses
  `self-similar-induction-on-n`'s own `G(m,k;V)` framework (Round 4), which was left almost
  entirely unexplored for `V<2^m`.
- For (c): the same idea applied to `greedy-reduction-geometric`'s Theorem 7, tracking leftover
  mass `L` as an explicit parameter through the induction.
- Both point at the same underlying tool: a **strengthened Peeling/Lemma-B pair with an extra
  free real parameter**, not a fundamentally new mechanism.

### Knowledge-base entries to use
Not separately consulted this round beyond what the two approach files already cite (Peeling
Lemma / Companion Peeling Lemma / Lemma B / Tie-neutrality block form) — these are all already
certified lemmas in `results/imo-2026-03/lemmas/`; no new KB entry outside the problem's own
lemma cache looks relevant to this specific casework.

### Analogous past problems (cruxes)
- `aimo-0117` (combinatorics, `games-and-strategy`): a two-player game assigning dyadic
  (`2^i`) values to stones split between two boxes, with the crux "assign values as a two-sided
  geometric sequence so the single largest value strictly exceeds the sum of all others" and
  "defer committing the extreme value until the opponent vacates its target cell, to hold an
  invariant." This is genuinely analogous in *spirit* — same dyadic-dominance mechanism
  (`2^j > 2^{j-1}+\cdots`) that underlies every Peeling-Lemma argument in this problem's own
  proof population — but it does not offer a new closing technique beyond what's already
  certified here (max-dominates-the-rest peeling is already the load-bearing tool in every
  approach). No crux found addressing the specific "prove a strict inequality holds with an
  extra free parameter tracked through an induction" pattern needed for (a)/(b)/(c); searched
  `combinatorics`/`games-and-strategy` (39 entries) and skimmed `extremal-principle`/
  `size-bounding-and-descent` subtopic names — nothing else stood out as closely analogous to
  this specific sliver/vertex-boundary situation. Recommend not over-indexing on the corpus for
  this narrow gap; it looks like genuinely problem-specific casework.

### Prior progress
- Theorem 2 (`self-similar-induction-on-n`, certified in that file though not yet promoted to
  `lemmas/`) closes Case-B(m,k) outside the width-1 sliver `(2^(m-1)-1, 2^(m-1))`.
- Theorem 7 (`greedy-reduction-geometric`) closes the "top-levels-clear" joint Case 2; the
  Leftover-Fragment Obstruction is a precise (proved) diagnosis, not a closure, of why the
  interleaved case resists the identical technique.
- The Two-Level Half-Bound Lemma is proved but numerically shown insufficient alone for the
  sliver (this round's finding above explains *why*: it's a single global refinement of Lemma B,
  but the true extremal structure needs a second application of the same dichotomy one level
  down, not a stronger flat bound).

### Dead ends (do not retry)
- Static Q-priority / tail-priority strategies — refuted by exact game-tree computation.
- Literal / restricted Cut-Reallocation Exchange Lemma — refuted.
- "Refining the tail only helps LB" — false, exact `m=6` counterexample.
- Two-Level Half-Bound Lemma **alone**, applied as a single flat inequality to the whole
  residual `B'∪T` at once — proved insufficient (this round, both by the approach file's own
  `m=4` instance and independently reproduced in spirit by my search above, which shows the true
  minimum sits at exactly `2^(m-1)+eps/2`, strictly above what a single global half-sum-style
  bound of this form can certify for `eps` near `0`). Do not retry the *same flat form*; the
  fix is recursion/parametrization, not a sharper flat constant.

### Small-case / intuition notes (conjectural, numeric evidence only)
- **Conjecture (new, this round, numeric only — not proved):** in the sliver, the exact minimum
  of `OddSum(B'∪T)` over all valid `B'` equals `2^(m-1) + eps/2` where `eps=2^(m-1)-b1`, i.e.
  the Case-B(m,k) sliver target holds with margin exactly `eps/2 > 0` for every `eps∈(0,1)`.
  Verified cleanly at `m=4,5,6` (10/10 trials matching to 6 decimals); at `m=7,8` some
  optimizer runs did not fully converge but never found a violation. This should be treated as
  strong evidence, not a proof — the exact linear form is a good target for a future round's
  algebraic proof attempt (e.g. via the `G(m,k;V)`-with-margin idea above), and if correct it
  fully closes gap (a).
- No new numeric probing was done this round for (b) or (c) beyond reading the existing
  approach files' own reported 30,000+-trial and Nelder–Mead adversarial searches (both report
  zero violations found, consistent with the conjectured closed form throughout).
