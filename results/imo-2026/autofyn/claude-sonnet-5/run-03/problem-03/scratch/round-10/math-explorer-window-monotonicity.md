## imo-2026-03 — lens: self-similar-induction-on-n's window lower-bound gap (Theorem W optimality + (‡) monotonicity)

### Recap of exactly what's open (confirmed by re-reading the file)
Theorem W (`lemmas/theorem-w-window-endpoint-witness.md`) is certified: at the
window's left endpoint $c_1=2^{\ell-1}$, the witness $C=\{2^{\ell-1}\}\cup
(\Gamma_{\ell-2}\setminus\{1\})\cup\{r,r\}$, $r=1+\varepsilon/2$, achieves
$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})=2^\ell+\varepsilon/2$ exactly (proved via
the certified General Insertion Lemma, Theorem 4). Two gaps remain, reduced to
the clean $c_1$-independent form $(\ddagger)$: writing $D:=C\setminus\{c_1\}$,
$T:=\Gamma_{\ell-1}$, $W:=\mathrm{sum}(D)$,
$$\max\{\mathrm{OddSum}(D\cup T): D\text{ admissible, sum}=W\}\le 2^\ell+\varepsilon-1\quad\forall W\in(2^{\ell-1}-1+2\varepsilon,\,2^{\ell-1}+\varepsilon].$$
(a) optimality of Theorem W's witness at the single largest $W=2^{\ell-1}+\varepsilon$;
(b) that this max, as a function of $W$, is non-decreasing (so the endpoint
case, once (a) is settled, implies every smaller $W$).

### Distinct openings
1. **Exchange-smoothing on the fixed-$W$ slice (closes gap (a)).** This is
   *literally* the crux-corpus pattern from `aimo-0146`: "maximize a fixed
   weighted sum of a sorted sequence under a sum constraint by exchange-
   smoothing weight toward the higher-coefficient positions until free
   coordinates equalize, then enumerate surviving profiles." Here the
   "weighted sum" is $\mathrm{OddSum}(D\cup T)$ (weight $1$ at odd global
   rank, $0$ at even) and the sequence is $D$'s entries merged into $T$'s
   fixed slots; the constraint is $\mathrm{sum}(D)=W$, $|D|\le\ell$,
   $\max(D)<2^{\ell-1}$. The natural exchange move is exactly the certified
   **Single-Insertion Lemma** (`altsum-reformulation-and-single-insertion.md`)
   applied as a "move mass from one $D$-coordinate to another, watch the
   $\Delta\mathrm{OddSum}$" primitive — this is the *right* tool (as the
   round-9 file itself notes) but was not assembled into a full argument.
   **Caution, found this round**: this must NOT be done as "increase one
   coordinate, argue OddSum can't decrease" in general — see the Schur dead
   end below, which shows exactly this style of naive per-move monotonicity
   claim is false in general for OddSum-type weight patterns. The exchange
   argument needs to move mass *toward the current odd-rank slot*, not just
   "toward the top," and terminate at a genuine KKT/vertex characterization
   (finitely many "profiles" as in aimo-0146), not an ad hoc greedy claim.

2. **Recognize $(\ddagger)$ as the same finite-cell affine-vertex LP that
   `global-lp-vertex-sufficiency` is building for the *other* open gap
   (upper-bound direction).** For $D$ ranging over a fixed "interleaving
   cell" relative to $T$'s fixed breakpoints $(2^{\ell-2},\ldots,2,1)$,
   $\mathrm{OddSum}(D\cup T)$ is *affine* in $D$'s coordinates (the
   odd/even assignment is locally constant within a cell). So $(\ddagger)$
   is exactly "maximize an affine functional, cell by cell, over the bounded
   polytope $\{D:\mathrm{sum}(D)=W,\ 0<d_i<2^{\ell-1},\ |D|\le\ell\}$" — a
   direct instance of the sibling approach's Global Vertex Lemma /
   cell-wise-affine-vertex-reduction machinery (Lemma 4.1/4.2 in
   `global-lp-vertex-sufficiency`, currently *partial* with one narrow found
   gap — the missing $p_k\ge0$ functional). If that machinery is finished
   (a small, already-diagnosed fix per `current.md`), it would give a
   **finite candidate vertex list** for $D$ at each $W$, turning both gap
   (a) and gap (b) into a finite (if unbounded-in-$\ell$) case check rather
   than an open-ended smoothing argument — worth flagging as a genuine
   cross-approach reuse opportunity, not previously connected in either
   approach's file.

3. **Direct induction on $W$ (a discretized/coupling monotonicity proof).**
   Rather than a general exchange argument, try to construct, for any
   admissible $D$ at $W_1<W_2$, an explicit admissible $D'$ at $W_2$ with
   $\mathrm{OddSum}(D'\cup T)\ge\mathrm{OddSum}(D\cup T)$, by adding the
   extra mass $W_2-W_1$ (always $<1-\varepsilon<1$, since the whole window's
   $W$-range has width $1-\varepsilon$) either (i) as a new tiny piece if
   $|D|<\ell$ (safe: $<1<2^{\ell-1}$ for $\ell\ge2$, so the max-cap is never
   an issue for this move), placed just below the current minimum — this
   changes at most one rank (the new smallest element's own rank), so
   $\mathrm{OddSum}$ is unchanged or increases (never decreases) by the
   *same* Peeling-Lemma-style rank-counting already certified elsewhere; or
   (ii) if $|D|=\ell$ (cap already saturated), added to $D$'s current
   smallest element — this is the genuinely open sub-case (may cause a rank
   swap with a neighboring element, and per the Schur dead end this is
   *not* automatically safe). This isolates the *entire* remaining
   difficulty to the single sub-case "$D$ already uses all $\ell$ pieces
   and every element that could absorb extra mass sits right below a
   rank-boundary" — a much narrower target than a general monotonicity
   claim, and worth stating explicitly as the reduced gap.

4. **Give up on generalizing Theorem W's exact witness family and instead
   prove $(\ddagger)$ as a pure upper bound (no witness needed for
   non-endpoint $W$).** Numerics below show the "duplicate-the-rest" witness
   scaled naively to smaller $W$ is *not* the maximizer away from the
   endpoint (a different, unidentified family does better at low $W$, though
   still safely under target) — so any proof of $(\ddagger)$ for general $W$
   should not assume Theorem W's specific witness shape generalizes; it only
   needs an upper bound, which could come from Lemma S (Subadditivity of
   OddSum, `perfect-pairing-subadditivity-and-general-insertion.md`) combined
   with a *sharper*-than-trivial bound on $\mathrm{OddSum}(D)$ alone (the
   naive $\mathrm{OddSum}(D)\le\mathrm{sum}(D)=W$ is checked below to be far
   too weak — it fails by a wide margin, consistent with the file's own
   diagnosis that subadditivity alone won't close this).

### Candidate technique(s)
Exchange-smoothing / extremal-principle (crux `aimo-0146` mechanism) driven by
the certified Single-Insertion Lemma, cross-checked against / potentially
subsumed by the sibling LP-vertex machinery (`global-lp-vertex-sufficiency`).

### Cheap-kill candidates
- Direct computation (below) refutes the *naive* subadditivity bound
  ($\mathrm{OddSum}(D)\le W$ plugged into Lemma S) as a route to $(\ddagger)$:
  it is far too weak for large $\ell$ (gap grows, not just a constant).
- The Schur-monotonicity dead end (already certified,
  `schur-monotonicity-criterion-and-majorization-dead-end.md`) is a cheap
  kill on any *naive* "increasing one coordinate can't decrease OddSum"
  style argument for the exchange step — must be built more carefully
  (track which rank is being fed), not asserted.
- None found that fully closes gap (a) or (b) cheaply; the piece-cap-
  saturation sub-case (Opening 3(ii) above) is the sharpest isolation of
  the true remaining difficulty found this round.

### Knowledge-base entries to use
- `knowledge_base.md` "General Proof Methods" — Pigeonhole/extremal principle
  (take the maximal element / vertex of a polytope).
- Certified problem-local lemmas: General Insertion Lemma (Theorem 4) and
  Subadditivity Lemma (Lemma S), both in
  `perfect-pairing-subadditivity-and-general-insertion.md`; Single-Insertion
  Lemma in `altsum-reformulation-and-single-insertion.md`; Schur-monotonicity
  criterion (dead-end warning) in
  `schur-monotonicity-criterion-and-majorization-dead-end.md`; Global Vertex
  Lemma / cell-wise-affine-vertex reduction (partial, one narrow found gap)
  in `global-vertex-lemma-and-lipschitz-continuity.md` and the round-9
  Section 4 of `approaches/global-lp-vertex-sufficiency.md`.

### Analogous past problems (cruxes)
- **`aimo-0146`** (combinatorics, `extremal-principle`): "Maximize a fixed
  weighted sum of a sorted nonnegative integer sequence under a sum
  constraint by exchange-smoothing weight toward the higher-coefficient
  positions until the free coordinates equalize and the tail drains, then
  enumerate the few surviving profiles." This is the closest analog found —
  same shape of problem (maximize an alternating/positional weighted sum
  under a budget constraint with box caps) — already flagged by the round-9
  dispatch and correctly identified as the right mechanism; it was not
  fully assembled, and this round's finding is that the *naive* version of
  "move mass to the top" fails (see Schur dead end), so the actual
  `aimo-0146`-style argument needs the more careful "move to the specific
  rank with weight 1" version, which its own file describes as needing
  "several rounds of reasoning even in its own simpler linear-functional
  setting" — a fair warning this is not a one-round closure.
- No other crux in `extremal-principle`/`inequalities-SOS-and-convexity`
  found to be a closer structural match (skimmed ~15 more entries in
  `extremal-principle`; most are graph-degree or geometric extremal
  problems, not budget-constrained alternating-rank-sum maximization).

### Prior progress
Theorem W (certified) settles $(\ddagger)$ exactly at $W=2^{\ell-1}+\varepsilon$
with margin $\varepsilon/2$. The $c_1$-independence reduction $(\ddagger)$
itself is proved (algebraic identity). Both gaps (a) optimality-at-endpoint
and (b) monotonicity-in-$W$ are open, per `current.md` and the approach file.

### Dead ends (do not retry)
- Schur-monotonicity / majorization-monotonicity of OddSum: **proved false**
  in general (`schur-monotonicity-criterion-and-majorization-dead-end.md`,
  exact counterexample). Any argument for gap (b) that reduces to "$D'$
  majorizes $D$ implies $\mathrm{OddSum}(D'\cup T)\ge\mathrm{OddSum}(D\cup T)$"
  is unsound as stated and must not be used without tracking the *specific*
  rank being fed (matches this round's independent finding that a bare
  "add mass to top element" move is not automatically safe).
- Naive subadditivity ($\mathrm{OddSum}(D\cup T)\le\mathrm{OddSum}(D)+
  \mathrm{OddSum}(T)$ with $\mathrm{OddSum}(D)\le W$): confirmed this round
  (see below) to be far too weak to give $(\ddagger)$ — do not pursue as
  the main mechanism, though Lemma S itself remains valid and could still
  play a role if combined with a genuinely sharper bound on
  $\mathrm{OddSum}(D)$ specific to the max-cap/piece-cap constraints.
- Peel+scalar-bound and order-statistics routes on this exact window: already
  diagnosed as wrong-direction/insufficient in rounds 6–7 (per the approach
  file); not re-examined this round, no new reason found to revisit.

### Small-case / intuition notes (all conjecture/numeric, exact-Fraction and float scripts, not proofs)
- **Confirmed exactly** (exact `Fraction`, reproducing Theorem W independently):
  witness value $2^\ell+\varepsilon/2$ at $\ell=3,4,5,6$, $\varepsilon\in
  \{0.1,0.3,0.5,0.7,0.9\}$ — matches file's claim exactly, zero deviation.
- **Local hill-climbing/simulated-annealing search** (piece-splitting/merging
  moves, thousands of iterations) starting from Theorem W's witness at the
  endpoint $W=2^{\ell-1}+\varepsilon$ found **no improvement** over the
  witness's exact value, for $\ell=3,4,5,6$ and several $\varepsilon$ —
  consistent with (but not proof of) gap (a): the witness is the true
  maximizer at that $W$.
- **Simulated-annealing sweep of $W$ across the whole range** (7 sample
  points, several $(\ell,\varepsilon)$ pairs) found the max-over-$D$ of
  $\mathrm{OddSum}(D\cup T)$ to be **numerically non-decreasing in $W$** in
  every trial (no violation found), consistent with gap (b)'s conjectured
  monotonicity, and consistently landing *below* target
  $2^\ell+\varepsilon-1$ with slack shrinking to exactly $\varepsilon/2$ at
  the top endpoint (matching Theorem W) — the annealed values slightly
  undershoot the true optimum away from the endpoint (random search, not a
  certified computation) but never exceed the target anywhere probed.
- **New negative finding (not previously recorded): the "generalized
  duplicate-the-rest" witness (Theorem W's family scaled to smaller $W$ by
  adjusting $r$) is NOT the true maximizer away from the endpoint.** At
  $\ell=3,\varepsilon=0.3$, the naive scaled-$r$ family gives values
  $6.80,6.85,\ldots,7.15$ across the $W$-grid, while simulated annealing
  independently found strictly larger values ($\approx 7.00$ flat) at the
  *low* end of the range — i.e. a genuinely different (unidentified) $D$
  structure dominates there, though it still stays safely under the (larger,
  at low $W$) target. **Implication for the outliner**: any general-$W$
  proof of $(\ddagger)$ should not assume Theorem W's exact witness shape
  extends verbatim to interior $W$ — either a genuinely $W$-dependent
  extremal family needs to be identified (plausibly related to the "just
  don't disturb T's ranks" baseline construction, worth a dedicated
  follow-up search), or the proof should be a pure upper bound not tied to
  exhibiting the exact maximizer at every $W$.
- Confirmed the naive subadditivity route is too weak: plugging
  $\mathrm{OddSum}(D)\le W$ into Lemma S requires
  $W+\mathrm{OddSum}(T)\le 2^\ell+\varepsilon-1$ at the endpoint
  $W=2^{\ell-1}+\varepsilon$, i.e. $\mathrm{OddSum}(\Gamma_{\ell-1})\le
  2^{\ell-1}-1$ — but $\mathrm{OddSum}(\Gamma_{\ell-1})\approx
  \tfrac23\cdot2^\ell\gg2^{\ell-1}-1$ for large $\ell$ (exact closed form:
  $(2^{\ell+1}-1)/3$ or $(2^{\ell+1}-2)/3$ by parity, derivable from the
  already-certified $\mathrm{AltSum}(\Gamma_m)$ formula in
  `altsum-reformulation-and-single-insertion.md` via
  $\mathrm{OddSum}=(\mathrm{sum}+\mathrm{AltSum})/2$) — so this bound fails
  by a growing margin, confirming it cannot be the mechanism.
