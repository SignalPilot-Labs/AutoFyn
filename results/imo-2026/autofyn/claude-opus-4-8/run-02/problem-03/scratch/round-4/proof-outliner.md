## imo-2026-03

The whole problem is ONE gap from solved: UB `c(n) ≤ 2^n/D_n` certified; LB reduces to
**(LBL): for `W_n={2^0,…,2^n}` every ≤n-cut refinement has `f≥1`**, closed except the
non-degenerate rank-tied minimizer. All three explorers converge: the illustrative residual
`{4/3,4/3,4/3,2,1}` (f=5/3) is NOT a minimizer — it slides continuously down to f=1. I verified
by exhaustive rational search (n=2,3, denom 3/6/12): **min f = 1 in every case**, and every
minimizer has integer f=1. Two correctness facts that shape the outline:
- The residual is a *proof-writing* gap (the tied vertex retracts onto closed cases), not a
  mathematical obstruction. Numerics strongly confirm.
- **CAUTION (verified this round):** non-degenerate minimizers with cross-piece ties that are
  NON-monochromatic AND have integer f=1 DO exist (found many, n=2,3). So the cross-tie case
  CANNOT be finished by "no within-piece tie ⇒ monochromatic ⇒ f=Σε_k2^k" (that implication is
  FALSE at cross-ties). Cross-ties must be *broken*, or f bounded another way. This is the honest
  crux and both approaches below flag it. Also: naive "same-cut-pattern integer normalization"
  does NOT dominate f (12–46/400 fail) — do not route through it.

---

self-similar-recursion: advance
Target: `c(n) = 2^n/(2^{n+1}-1)` — the whole problem, end to end. UB certified; this closes the
final LB residual (LBL at the tied non-degenerate minimizer).
Technique: local exchange/retraction on the piecewise-affine `f` over the compact cut polytope —
from ANY tied non-degenerate minimizer, a weakly-`f`-decreasing feasible path to a CLOSED terminal
(degenerate ⇒ cut-count induction, or tie-free non-deg ⇒ certified Lemma J). Builds directly on
certified Lemmas I, J, F already in the file.
Skeleton:
  1. Minimizer exists (Weierstrass, compact polytope, finitely many cut patterns); take global
     minimizer `P*`. Degenerate ⇒ cut-count induction; tie-free non-deg ⇒ Lemma J ⇒ `f≥1`.
     Remaining: `P*` non-deg with a rank tie — by LP-vertex reduction WLOG a rational vertex
     pinned purely by ties (min of affine `f` over compact rational polytope is at a vertex).
  2. Block-decomposition identity (NEW Lemma BD): a rank-contiguous block of `r` sub-pieces of ONE
     piece `2^k` contributes `σ_a·f_block` to `f`, `f_block` = alternating sum of the block's own
     values (sum `2^k`) — because `σ_{a+j-1}=σ_a(-1)^{j-1}`. Generalizes the certified top-band
     decoupling (Lemma A/B) to an arbitrary band.
  3. WITHIN-PIECE ties: if a tie-block has ≥2 sub-pieces of the same piece, vary that piece on its
     simplex — `f = const + σ_a·f_block` is affine, so its min is at a simplex vertex: a sub-piece
     →0 (degenerate, closed) or a value crosses an external one (chamber boundary). Weakly
     decreasing `f`. So eliminate every within-piece tie (squeeze / joint perturbation — explorers
     verified the symmetric split is a saddle, e.g. `5/3 - 8δ` strict descent).
  4. CROSS-PIECE ties (THE gap): with no within-piece tie left, break each cross-tie by a
     weakly-`f`-decreasing feasible slide via the odd/even tie-block dichotomy of Lemma I:
     `σ_a−σ_b = 0` (odd block) ⇒ a within-piece member-slide is flat ⇒ break the tie free;
     `σ_a−σ_b = ±2` (even block) ⇒ a member-slide strictly lowers `f` ⇒ contradicts minimality
     unless infeasible = blocked by degeneracy. Each cross-tie touches ≥1 CUT piece (the `2^k` are
     distinct ⇒ two uncut originals cannot tie), which supplies the needed internal freedom.
     Terminate by a lexicographic tie-multiplicity monovariant (finitely many sort-chambers, `f`
     constant along flat moves ⇒ no cycles) at tie-free non-deg (Lemma J) or degenerate. Then
     `f(P*) ≥ f(terminal) ≥ 1`.
Key lemmas (claim + mechanism):
  - Lemma BD (block-decomposition): block contributes `σ_a·f_block` — because
    `σ_{a+j-1}=σ_a(-1)^{j-1}` factors the sign out of the contiguous band. NEW, one line.
  - Lemma I′ (joint / non-adjacent cut-slide derivative): extend certified Lemma I (adjacent
    slides only) to a coordinated multi-cut family — the 1-parameter restriction of `f` is again
    piecewise-affine with slope a telescoping sum of traversed rank-signs. NEW, load-bearing for
    the squeeze in Step 3 and the tie-break in Step 4.
  - Within-piece squeeze descent: symmetric same-piece tie-blocks are saddles, not minima — a
    joint "spread the middle" move strictly lowers `f` (explorers: exact `5/3−8δ`, and the
    even-block `−2ε` slide). Mechanism: BD makes the block's own `f_block` want a simplex vertex.
  - Cross-tie finite retraction: odd blocks give flat tie-breaks, even blocks give strict descent;
    monovariant (tie multiplicity) + finite chambers ⇒ termination at a closed case.
Open gaps: (i) Lemma I′ (joint/non-adjacent slides — Lemma I is certified only for adjacent
sub-pieces); (ii) the cross-tie termination monovariant (rule out infinite flat-sliding — finitely
many chambers + `f` constant on flat moves, needs a clean lexicographic decrease); (iii) checking
the even-block strict-descent sign is uniform across block size `k` and rank parity (explorer only
verified `k=3`; check `k=2,4,5` symbolically). Steps 1–3 machinery is largely in hand; Step 4
cross-tie is the residual.
Cases to cover: degenerate (done); tie-free non-deg (done, Lemma J); within-piece tie (Step 3);
cross-piece tie (Step 4). LP-vertex ⇒ these exhaust non-degenerate minimizers.
Watch out for: cross-tie minimizers are NON-monochromatic with integer f=1 (verified) — do NOT try
to finish them by monochromaticity; must break the ties. Do NOT delete `{v,v}` and induct on piece
count (breaks `Σ(sub-pieces of 2^k)=2^k`, recorded dead end). Do NOT use parity-of-pieces at
non-integer cuts (`d=3` gives f=1/3). Do NOT assume Lemma I applies to non-adjacent slides — it
does not without Lemma I′.

---

block-recursion-tievertex: new
Target: `c(n) = 2^n/(2^{n+1}-1)` — whole problem. Imports certified UB + all LB machinery
(Lemmas I, J, F, layer-cake); differs only in HOW it closes the tied residual — a genuinely
different architecture from the retraction path (a de-risking second framing on the same gap).
Technique: STRONG INDUCTION on total sub-piece count via the block-decomposition identity — treat
a tied block as a strictly smaller *self-similar copy* of the same alternating-sum extremal
problem, recursing into the block (keeping its sum `2^k`, so conservation is preserved) instead of
walking a global monotone path. Structural recursion, not an analytic retraction.
Skeleton:
  1. Reduce (LBL) to a global minimizer `P*` (Weierstrass); degenerate/tie-free legs closed as in
     self-similar-recursion. Remaining: non-deg tied.
  2. Lemma BD (block-decomposition identity) — same NEW lemma as above.
  3. Within-piece tie: apply BD to the same-piece block; `f = const + σ_a·f_block` is a smaller
     instance of the SAME extremal problem (minimize if `σ_a=+1`, maximize if `σ_a=-1`), both
     governed by `0≤f_block≤Σ` (Lemma 0) and Lemma J/degenerate recursion at block level. Strong
     induction on sub-piece count closes it — the recursion bottoms at a block vertex (degenerate,
     or a value crossing external → cross-tie / integer).
  4. Cross-piece tie: the recursion's bottom. Same crux as self-similar Step 4 but attacked as an
     integer/parity terminal: show the fully-retracted block-vertices are integer configs (Theorem
     F closes them) or tie-free (Lemma J). Flag the cross-tie integrality as the open sub-claim.
Key lemmas (claim + mechanism):
  - Lemma BD (as above).
  - Self-similar block reduction: minimizing `f` over one piece's freedom = optimizing that
    piece's own alternating sum `f_block` on its simplex — the SAME problem one level down, so
    strong induction on sub-piece count applies. Mechanism: BD factorization.
  - Cross-tie bottom-out: every non-symmetric (cross-crossing) block vertex is integer (verified
    numerically n=2,3) ⇒ Theorem F ⇒ `f≥1`; the purely-symmetric internal vertex is dominated
    (Step 3). Load-bearing open claim: prove the cross-tie block-vertices are integer in general.
Open gaps: the same two hard facts as the retraction route, reached from the other side — (a) the
recursive within-piece reduction terminating cleanly; (b) cross-tie block-vertex integrality
(numerically true n=2,3, unproven in general). Kept far from the retraction route in *proof
architecture* (structural induction vs monotone path) so they do not share a termination argument.
Cases to cover: degenerate; tie-free; within-piece tie (block recursion); cross-piece tie
(integer/parity bottom-out).
Watch out for: BD requires the block be rank-CONTIGUOUS (a tie guarantees this locally, but track
it when a block value crosses an external one). Do NOT treat the origin-blind relaxation as a valid
lower bound (explorer: 5 pieces of 7/5 give f=7/5<5/3, unreachable — drops per-piece conservation).
Same recorded dead ends as above.

---

Field summary for the reviewer: advance `self-similar-recursion` (primary — retraction path,
builds on its own certified Lemmas I/J/F) and build `block-recursion-tievertex` (new — same gap,
different architecture, de-risking hedge). Both hinge on the NEW block-decomposition identity
(Lemma BD, easy) and both flag the cross-piece-tie termination as the honest residual; they attack
it from opposite sides (monotone retraction vs structural induction) so a wall on one need not stop
the other. If either closes the cross-tie step, (LBL) is proved, the LB is complete, and with the
certified UB the problem is SOLVED.
build set: self-similar-recursion, block-recursion-tievertex
