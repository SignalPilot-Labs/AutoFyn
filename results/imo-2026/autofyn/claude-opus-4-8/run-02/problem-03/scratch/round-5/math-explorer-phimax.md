## imo-2026-03 — LENS: Φ=Σx²-maximal minimizer integrality route

### Distinct openings

1. **(Primary, new this round) Generalized incidence-graph (drop Lemma W's narrow leaf
   restriction).** Re-examined the *exact* counterexample that killed Lemma W/S/T
   (`piece1={1},piece2={2},piece4={2,2},piece8={2,3,3}`, n=3, f=1). Built its full
   piece↔value incidence multigraph honestly (allowing multiplicity edges anywhere, not just
   at `r_k=2` bisection leaves as Lemma W wrongly assumed):
   `piece1—comp(1) [μ=1]`, `piece2—comp(2) [μ=1]`, `piece4—comp(2) [μ=2]`,
   `piece8—comp(2) [μ=1]`, `piece8—comp(3) [μ=2]`.
   **This graph IS a forest** (2 tree-components, 7 nodes, 5 edges, no cycle) even though it
   has a multiplicity-2 edge (`piece8—comp(3)`) sitting at a piece of degree 2, *not* a leaf —
   exactly the configuration Lemma W's statement said couldn't happen. Generalized leaf-peeling
   (peel piece4, a genuine degree-1 leaf with μ=2: `2·w=4 ⇒ w=2`; substitute into piece8's
   equation `w(comp2)+2·w(comp3)=8 ⇒ 2+2w(comp3)=8 ⇒ w(comp3)=3`) reproduces the *correct*
   integer values `2,3` with no contradiction. **So Lemma W's proof-breaking counterexample does
   NOT actually break a suitably generalized Lemma S/T** — it only breaks the overly narrow
   *statement* of Lemma W (which wrongly restricted multiplicity-2 edges to bisection-leaf
   pieces). The real open question is whether (a) the kernel/cycle-exclusion half of Lemma S
   generalizes cleanly to a general-multiplicity incidence matrix `U` (not just 0/1 or
   0/1-plus-bisection-leaf), and (b) whether Φ-maximality still forbids cycles in this bigger
   graph. Neither is yet proved, but neither is refuted either — this is a genuinely new,
   unexplored angle that the round-4 rejection did not investigate (the reviewer only checked
   that Lemma W's *stated claim* was false, not whether the underlying forest/kernel machinery
   survives a corrected, more permissive formulation).
   **Caveat found:** leaf-peeling divides by the edge multiplicity `μ`; this stays integral only
   if `μ | 2^k` for the piece `2^k` at that leaf. For `μ=2` this always holds (`k≥1`); for an
   **odd multiplicity ≥3** (e.g. a piece split into 3 *equal* parts) it generally fails — matches
   the known non-integer example `{4/3,4/3,4/3,2,1}` (piece4 split into 3 equal thirds, `μ=3`,
   `4/3∉ℤ`). Checked: that specific config has `f=5/3 ≠ 1`, i.e. it is **not itself a global
   minimizer** (consistent, not a counterexample to the route) — but a live open question is
   whether an odd-multiplicity **equal** split could ever occur at an actual `f=1` minimizer. An
   equal split *minimizes* Φ locally (for fixed sum and count, equal parts minimize Σx²), so it
   is a natural conjecture that Φ-maximality (a global condition) disfavors it — but this is
   intuition, not a proof; needs to be established as a lemma before trusting the route.

2. **Global-domination lever (numerically confirmed this round).** Computed exactly: at n=3, the
   {2,3,3} config has `Φ = 1²+2²+2²+2²+2²+3²+3² = 35`. A DIFFERENT (degenerate, fewer-cut)
   global minimizer with the same `f=1` — `{5,4,2,2,1,1}` (piece8 split into `(5,2,1)`, piece4
   left unsplit, only 2 actual cuts) — has `Φ = 25+16+4+4+1+1 = 51 > 35`. So `{2,3,3}` is **not**
   the Φ-global-maximum of the minimizer set `G`; it is beaten by a *degenerate* representative,
   which the induction (`self-similar-recursion` §1, "if `P*` degenerate, delete the zero
   sub-piece, apply `Claim(N−1)`") already handles for free. Random search over the pattern
   containing `{2,3,3}` (piece2 unsplit, piece4 split, piece8 split into 3, 3000000 samples)
   confirms the *local* Φ-max near `f=1` in that pattern approaches exactly the degenerate
   boundary (`Φ→51`), never exceeding it — `{2,3,3}` sits strictly inside as a local pocket, not
   the pattern's own Φ-sup. This is a rigorous confirmation (not just round-4's qualitative claim)
   that the known bad examples are dominated. It does **not** by itself prove the general claim
   ("every within-piece-tie minimizer is dominated in Φ by a tie-free/degenerate one") — that's
   the actual gap to close, but the specific counterexamples that killed Lemma W are consistent
   with it holding in general.
   Similarly recomputed the known non-integer continuum `piece2={a,2−a}, piece8={4,2,2}` (n=3):
   `Φ(a) = 41+a²+(2−a)²`, maximized only at the boundary `a→0` or `a→2` (`Φ→45`, itself still
   below the 51 found above) — confirms round 4's "not Φ-maximal" claim with an exact formula,
   and shows there can be *multiple* higher-Φ competitors, not just one.

3. **Composing the two live routes carefully — a subtlety, not a free win.** The tempting move
   is: use `block-recursion-tievertex`'s §2 (Lemma BD within-piece elimination, *sound*,
   f-preserving/weakly-decreasing, does NOT need Lemma W or Φ at all) to strip within-piece ties,
   landing in case (d) (pure cross-tie, clean 0/1 incidence matrix), and THEN apply
   `self-similar-recursion`'s Lemma S cycle-exclusion (Φ-maximal ⇒ no sum-preserving flat shift ⇒
   forest) to finish, bypassing `block-recursion`'s harder residual UPM-5 (chorded even cycles)
   entirely — because "Φ-max forest" is a *strictly stronger* conclusion than "unique PM despite
   possible cycle," and only needs to hold at the *one* Φ-maximal point, not at all 24/3120
   verified-but-cyclic cross-tie minimizers block-recursion found for n=3,4.
   **However**: Lemma BD's elimination move is NOT shown to be Φ-non-decreasing — it only
   preserves `f=m` (staying in `G`) while reducing within-piece-tie count; it says nothing about
   Φ. So starting from the actual Φ-max point of `G` and applying Lemma BD's move could *leave*
   the Φ-max point and land somewhere with lower Φ, breaking the "Φ-max" hypothesis Lemma S's
   cycle-exclusion needs. The correct order of operations is therefore delicate: either (i) prove
   Lemma BD's elimination move is Φ-non-decreasing (would need its own argument — not yet
   attempted by either approach, but plausible given finding 2 above that concentration ↑ raises
   Φ), or (ii) skip Lemma BD altogether and directly generalize Lemma S/T to the full-multiplicity
   graph as in opening 1 (cleaner, avoids the composition-order issue, but needs the cycle
   argument to handle non-0/1 edges).

### Candidate technique(s)
- Direct extension of Lemma S's kernel/cycle argument to a general-multiplicity bipartite
  incidence graph (no restriction to 0/1-plus-bisection-leaf) — opening 1.
- A "Φ-domination" lemma: any minimizer with a within-piece tie is beaten in Φ by some other
  same-`f`-value point (possibly degenerate, possibly in a different pattern/component of the
  domain) — would make Lemma W unnecessary as a *local* claim (it never needs to hold locally,
  only that ties never survive at the *global* Φ-argmax).
- If either of the above stalls: fall back to `block-recursion`'s Lemma UPM-5 (chorded even
  cycles, algebraic, verified n≤5) — a self-contained, narrower residual not requiring Φ at all.

### Cheap-kill candidates
- Before deep casework: for any proposed within-piece-tie survivor at the claimed Φ-max, always
  check whether some *degenerate* (fewer-cut) alternative achieves the same `f`-value with higher
  Φ (as in finding 2) — this killed the `{2,3,3}` and non-integer-continuum "counterexamples" as
  threats to the Φ-max route (they don't survive as the true global argmax) and should be the
  first check on any *new* proposed counterexample before it's trusted.
- Parity/divisibility cheap-kill for opening 1: an odd-multiplicity (`≥3`) EQUAL within-piece
  split at a leaf is only integer-safe if the multiplicity divides the relevant `2^k`; since
  odd numbers never divide a power of 2 (for `k` with `2^k` not a multiple of that odd number,
  which is always for μ≥3 odd unless μ=1), **any leaf with odd multiplicity ≥3 forces
  non-integer values there** — so the route needs to show such leaves never occur at the Φ-max
  minimizer (plausible since equal splits minimize local Φ, but unproved).

### Knowledge-base entries to use
Not separately re-checked this round (terrain is now almost entirely internal to the problem's
own certified lemma stack); the relevant tools are the problem's own certified lemmas rather than
generic KB entries: Lemma L (layer-cake), Theorem F (integer-parity-alt-sum), Lemma I
(cut-slide-derivative), Lemma J (tiefree-minimizer-monochromatic), Lemma BD
(block-decomposition identity, in `block-recursion-tievertex.md` §2, not yet promoted to
`lemmas/`), and the *sound halves* of the rejected Lemma S (cycle⇒kernel via feasible
sum-preserving shift + strict convexity of Φ) and Lemma T (forest/leaf-peeling ⇒ integer, general
version demonstrated to still work on the {2,3,3} example above).

### Analogous past problems (cruxes)
Not queried this round — this lens is deep in problem-specific structure (a bespoke
Φ=Σx²-maximal LP-vertex selection argument tailored to this game's alternating-sum functional);
prior rounds' explorers already searched the corpus for alternating-sum / matching-parity /
unimodularity techniques and did not find a closer analog than the internally-developed machinery.
No new crux search performed here to avoid duplicating that.

### Prior progress
Upper bound fully certified (unchanged). Lower bound complete except the tied-non-degenerate
residual. Both live routes (`self-similar-recursion`'s Φ-max, `block-recursion-tievertex`'s
UPM) remain exactly where round 4 left them: Elo ~1625 and ~1501 respectively, both partial.

### Dead ends (do not retry)
- Lemma W as literally stated ("`r_k≥3` ⇒ no equal sub-pieces of one piece") — FALSE, `{2,3,3}`
  counterexample stands. Do not re-propose this exact statement.
- The 3-variable compensated-shift proof technique used in Lemma W's proof (shift `q,q'` jointly,
  compensate on a third same-piece `q''`) — independently reconfirmed the reviewer's finding: this
  specific move gives a **V-shaped** (`f=m+2|t|`) local min at `{2,3,3}`, not a descent, so this
  exact proof technique cannot be salvaged as-is for the general claim. A *generalized* incidence
  graph (opening 1) sidesteps this by not needing the local perturbation argument at all — it
  instead needs the global sum-preserving-shift argument (Lemma S's mechanism) applied to a
  richer graph, which is untested but structurally different from the failed local move.
- Composing block-recursion's Lemma BD elimination directly before self-similar's Φ-max
  cycle-exclusion **without justifying Φ-monotonicity of the elimination move** — flagged above
  as a subtle ordering trap; do not present this composition as if it were free.
- Global integrality of ALL minimizers (round-4 finding, continuum counterexample) — still dead,
  unaffected by this round's findings (opening 1 only claims integrality at the Φ-max point, not
  globally).

### Small-case / intuition notes (all labeled conjecture except the exact computations above)
- **(Computed exactly, not conjecture)** `{2,3,3}` config: Φ=35, sub-optimal vs. a degenerate
  competitor Φ=51 at the same `f=1`. Non-integer continuum: `sup Φ = 45` at its own boundary,
  also sub-optimal vs. 51. Both "killer" examples are dominated — consistent with, but not proof
  of, the Φ-max route.
- **(Computed exactly)** The generalized (multiplicity-aware) incidence graph of `{2,3,3}` is a
  genuine forest, and generalized leaf-peeling correctly recovers the integer values 2 and 3 —
  i.e. the specific counterexample to Lemma W's *statement* is not a counterexample to a properly
  generalized Lemma S/T. This is the strongest new evidence this round that the Φ-max integrality
  route is still alive and possibly repairable with a broader (not narrower) incidence-graph
  definition, rather than needing an entirely different mechanism.
- **(Conjecture, unproven)** Odd-multiplicity (≥3) equal within-piece splits never occur at the
  Φ-max minimizer, because equal splits are local Φ-minimizers, not maximizers — plausible but
  needs its own lemma (a global, not local, argument, per the "cheap-kill" and "composing" caveats
  above) before the route can close.
- min f = 1 remains numerically confirmed at n=2,3,4 (unchanged from prior rounds; not re-verified
  exhaustively this round beyond the specific examples above).
