## imo-2026-02

coordinate-bash-resultant-boundary-pointwise-tangent: advance
Target: the problem's actual claim `OM=ON`, via this route's full chain
(already-certified Gap 5 + Gap 6 + the remaining Case (a) fact, Gap 7,
closed this round per this outline) — i.e. this outline is meant to
complete the ENTIRE proof via this route, not just a sub-lemma.
Technique: reuse Theorem A's own already-certified derivative computation
at an *extended* scope (it was proved for all of `(0,γ)`, not just
`(β₀,γ)`, but only ever *invoked* on `(β₀,γ)`) + a short, fully general,
gap-free elementary trig lemma (`sinB≤sinC` for `B≤C` in any triangle) to
pin the needed endpoint value, then glue via the Mean Value Theorem
(standard real analysis, already "in-house" in this population via
`lemmas/mvt-lipschitz-reduction-case-b.md`).

**Which explorer's sub-argument to use — reconciliation.** Two candidate
elementary facts were found this round for the reduced target
`f(0)=sinA(2sin(A+B)-sinB)≥0`:
- Explorer gap7a's `sinB≤sinC` two-case argument (Case `C≤π/2`: `B≤C≤π/2`,
  `sin` increasing on `[0,π/2]` gives `sinB≤sinC` directly; Case `C>π/2`:
  `π-C<π/2`, and `A>0` forces `B=π-A-C<π-C`, so `B,π-C∈(0,π/2)` with
  `B<π-C`, giving `sinB<sin(π-C)=sinC`) is a **complete, gap-free proof
  covering the ENTIRE triangle domain** — no residual sub-case, no
  numeric-only piece. This directly gives `2sinC≥sinB` (in fact
  `2sinC-sinB≥sinC>0`), hence `f(0)≥sinA·sinC>0` unconditionally.
- Explorer gap7b's Opening 1 (`term1+term2` split) only fully closes the
  `A≤π/3` half elementarily; the `A>π/3` half is **numeric-only** (2M
  samples, zero violations, but no algebraic proof) — a real residual gap,
  not closed. Opening 2 (no-interior-critical-point + boundary trace) is a
  genuinely different mechanism but is explicitly left unfinished (the
  compactness/corner argument is "sketched, not completed" per the
  explorer's own report) and would require importing the Taylor+Lagrange-
  remainder machinery to handle the one degenerate corner rigorously — more
  machinery than is needed given gap7a's argument works outright.
**Verdict: use explorer gap7a's `sinB≤sinC` argument as the sole mechanism.**
It is strictly simpler, fully general (no case split on `A` needed), and
leaves no numeric-only residual — the builder should NOT staple gap7b's
partial split on top of it; gap7b's Opening 1 is superseded, not
complementary, and its `A>π/3` gap should not be re-imported. Gap7b's
Opening 3 finding (Theorem B's `β₀`-anchor casework does not transfer to
`β=0`) is a useful confirmation that gap7a's route (working with `f(0)`
directly, not trying to reuse Theorem B's `s`-substitution machinery) is
the right shape of argument.

Skeleton:
  1. Restate Theorem A's own derivative computation from
     `lemmas/claim-I-closed-and-claim-II-caseA-closed.md` at its true,
     already-proved scope: `f'(β)=sin(A+β)cosB+sin(A+B-β)>0` for **every**
     `β∈(0,γ)` (`γ:=∠B≤π/2`, from the file's WLOG `∠B≤∠C`) — by the
     elementary sign facts already in that lemma's proof (`cosB>0` since
     `B<π/2`; `sin(A+β)>0` since `A+β∈(0,A+B)⊂(0,π)`; `sin(A+B-β)>0` since
     `A+B-β∈(A,A+B)⊂(0,π)`), none of which use `β>β₀`. No new derivation —
     cite the existing proof at this extended scope; state it as "Theorem
     A′" (an explicit widening of Theorem A's stated conclusion, same
     proof).
  2. `f(β):=K_c+P\sinβ+Q\cosβ` is a finite sum of `sin`/`cos` compositions,
     hence continuous on the closed-below interval `[0,γ)` including at
     `β=0` — trivial but must be stated (needed for the MVT-corollary step).
  3. Standard real-analysis corollary of the MVT: `f` continuous on
     `[0,γ)`, `f'>0` on `(0,γ)` ⟹ `f` is strictly increasing on `[0,γ)`,
     i.e. `f(β)>f(0)` for every `β∈(0,γ)`. (Same MVT machinery already used
     elsewhere in this population, e.g. `lemmas/mvt-lipschitz-reduction-
     case-b.md` — cite the technique, re-derive the one-line application
     here.)
  4. Compute `f(0)=K_c+Q=2\sinA\sin(A+B)-\sinA\sinB=\sinA(2\sin(A+B)-
     \sinB)`. Substitute `C=\pi-A-B` so `\sin(A+B)=\sinC`, giving
     `f(0)=\sinA(2\sinC-\sinB)`.
  5. **Lemma (triangle sine comparison, elementary, fully general — no
     numerics needed).** For any genuine triangle (`A,B,C>0`,
     `A+B+C=\pi`) with `B\le C`: `\sinB\le\sinC` (in fact strict except in
     a degenerate limit). Proof by two cases on `C`:
     - `C\le\pi/2`: then `B\le C\le\pi/2`; `\sin` is strictly increasing on
       `[0,\pi/2]`, so `\sinB\le\sinC` directly (equality iff `B=C`).
     - `C>\pi/2`: then `\pi-C<\pi/2`. Since `A>0`, `B=\pi-A-C<\pi-C`. So
       `B` and `\pi-C` both lie in `(0,\pi/2)` with `B<\pi-C`; `\sin`
       strictly increasing on `[0,\pi/2]` gives `\sinB<\sin(\pi-C)=\sinC`.
     Both cases give `\sinB\le\sinC`. `\blacksquare`
  6. Combine 4+5: `f(0)=\sinA(2\sinC-\sinB)\ge\sinA(2\sinC-\sinC)=
     \sinA\sinC>0` (strict, since `A,C\in(0,\pi)` for a genuine triangle).
  7. Combine 3+6: for every `β₁\in(0,β₀(A)]\subset(0,γ)` (the exact Case
     (a) range; `(0,β₀(A)]\subset(0,γ)` holds because `β₀(A)<γ` is exactly
     the file's own "Case (a)/(b) domain nonempty" condition), `f(β₁)>f(0)
     >0`, i.e. `f(β₁)>0` — **this is exactly the missing Gap 7 fact**,
     established for the whole sub-range, not just asymptotically.
  8. Splice into "Full proof" Step 3 ("Case (a)"), replacing the current
     unjustified citation of Theorem A's stated `(β₀,γ)`-scoped conclusion
     with steps 1–7 above. Re-verify (mechanically, no new mathematics)
     that Step 3 combined with the already-certified Case (b) closure (Gap
     5 + Gap 6, both certified in prior rounds) and the population's
     already-certified reduction chain (`lemmas/vector-reduction-OM-ON.md`,
     `lemmas/mvt-lipschitz-reduction-case-b.md`,
     `lemmas/claim-I-closed-and-claim-II-caseA-closed.md`) together give
     `G(β₁)\ge0` throughout, hence `OM=ON`, completing the whole problem.

Key lemmas (claim + mechanism):
  - `f'(β)>0` on the WHOLE `(0,γ)`, not just `(β₀,γ)` — because Theorem A's
    existing sign argument (`\cosB>0`, `\sin(A+β)>0`, `\sin(A+B-β)>0`) only
    ever used `β\in(0,γ)`, never `β>β₀`; this is a scope-widening of an
    already-proved fact, not new content.
  - `\sinB\le\sinC` for `B\le C` in any triangle — because `\sin` is
    strictly increasing on `[0,\pi/2]` and, when `C>\pi/2`, the positivity
    of `A` forces the *reflected* angle `\pi-C` to still exceed `B` while
    staying inside `[0,\pi/2]`, so the monotonicity argument still applies
    after reflecting through `\pi/2`.
  - `f` strictly increasing on `[0,γ)` — because a continuous function with
    strictly positive derivative on an interval is strictly monotonic
    there (standard MVT corollary), and `f`'s continuity at the left
    endpoint is immediate from its being a finite trig sum.

Open gaps: none anticipated if steps 1–8 are written out fully and
rigorously — this outline is intended to fully close Gap 7 and thereby
complete the whole route. The builder must still write out step 3 (the
MVT-corollary citation) and step 7 (checking `(0,β₀(A)]\subset(0,γ)`
explicitly against the file's own domain definitions) in full rigor, not
hand-wave them as "standard."

Cases to cover: the two cases of the `sinB≤sinC` lemma (`C≤π/2` vs
`C>π/2`) — both must be written out in full, not just the easier one.

Watch out for:
  - Do NOT re-import explorer gap7b's `A≤π/3` / `A>π/3` split — it is
    strictly subsumed by gap7a's cleaner argument and would leave a
    numeric-only residual (`A>π/3`) if used instead.
  - Double-check the strict-vs-non-strict inequality bookkeeping: the
    lemma gives `\sinB\le\sinC` (non-strict, since `B=C` is allowed when
    `C\le\pi/2`), but `f(0)=\sinA(2\sinC-\sinB)\ge\sinA\sinC` is what's
    actually used, and `\sinA\sinC>0` strictly always holds for a genuine
    (non-degenerate) triangle — so `f(0)>0` strictly regardless of whether
    `\sinB=\sinC` or not; make sure the write-up doesn't accidentally only
    get `f(0)\ge0` with an unresolved equality case.
  - Confirm explicitly (not just assume) that the file's Case (a)/(b) split
    uses `γ:=∠B` (not `∠C`) and `β₀(A)=(\pi-A)/3` exactly as read from the
    file — re-verify against the live file text, since a mismatch in which
    angle is `γ` would silently invalidate the `(0,β₀(A)]\subset(0,γ)`
    containment used in step 7.
  - Once Gap 7 is closed, re-run a full dependency-chain audit one more
    time (the same discipline that caught gap 6 and gap 7 in rounds 17-18)
    before claiming Status `solved` — do not let the pattern of "one
    unflagged citation gap per round" repeat a third time.

spiral-similarity-bootstrap: advance
Target: the problem's actual claim `OM=ON`, via the fully independent
synthetic (directed-angle + spiral-similarity) route, diversifying away
from the coordinate/resultant/SOS cluster entirely.
Technique: directed-angle chase (Lemma A, Lemma B, already certified) +
midline theorem (`MN\parallel BC`) reducing `OM=ON` to a single linear
functional of `O` vanishing + Extended Law of Sines to make that
functional's `φ`-dependence explicit and check it cancels.
Skeleton:
  1. (Already certified.) Lemma A: `∠BLN=∠(BK,AC)` (from H2, one-angle
     directed-angle chain rule). Lemma B: `∠CKM=∠(CL,AB)` (from H3,
     symmetric argument). Corollary: `∠BLN+∠CKM\equiv0\pmod\pi` (combining
     both with H1 to eliminate the free parameter).
  2. New this round — record as an explicit sub-lemma (elementary, exact,
     not numeric): since `M,N` are midpoints of `AB,AC`, `MN\parallel BC`
     (midline theorem), so the perpendicular bisector of `MN` is parallel
     to the perpendicular bisector of `BC`'s direction, i.e. perpendicular
     to `BC`. Hence `OM=ON\iff O` lies on the specific line through
     `\mathrm{midpoint}(A,O_{ABC})`-type point perpendicular to `BC`,
     equivalently (placing `A` at the origin, per the file's own
     coordinate convention) `O\cdot(C-B)=(|C|^2-|B|^2)/4` — a single
     **linear functional of `O`** vanishing, not a 2-D distance equality.
     (This identity is already implicit in the file's "Confirmation of the
     target line ℓ" paragraph; this step makes the reduction explicit and
     names it, converting the target into a form suited to a trigonometric
     computation.)
  3. **Open gap — the genuine next step, not yet attempted in any file.**
     Use the Extended Law of Sines on the circles implicit in Lemma A
     (`∠BLN` as an inscribed angle at `L` subtending chord `BN` of the
     circle through `B,L,N`) and Lemma B symmetrically, to express `AK,AL`
     — or more directly, the projection of `O` onto the `BC`-perpendicular
     direction — as explicit trigonometric functions of `∠A,∠B,∠C` and the
     free family parameter `φ:=∠KBA=∠ACL`. Substitute into step 2's linear
     identity and check whether the `φ`-dependence cancels algebraically
     (it must, since `OM=ON` holds for every `φ` in the family per H1-H3's
     one-parameter freedom, numerically confirmed to `10^{-11}`–`10^{-14}`
     across 15 sample values this round).
Key lemmas (claim + mechanism):
  - `MN\parallel BC\Rightarrow(OM=ON\iff O\cdot(C-B)=(|C|^2-|B|^2)/4)` —
    because `M,N` are midpoints (midline theorem gives the parallelism),
    and the perpendicular-bisector characterization of `OM=ON` converts a
    distance equality into a linear functional once the bisector's
    direction is pinned to `\perp BC`.
  - (Target, not yet proved) the `φ`-dependence of `O`'s projection onto
    the `BC`-perpendicular direction cancels — because H1-H3 fix a genuine
    one-parameter family of valid `(K,L)` configurations all giving the
    same circle `(AKL)$ up to the constraint set, and `O` is the
    circle's center, so if Lemma A/B's inscribed-angle content correctly
    captures the family's structure, the sine-rule expression for `O`'s
    relevant coordinate should be `φ`-independent by construction — this
    is the substantive claim requiring an actual computation, not merely
    a plausibility argument.
Open gaps: step 3 in full — the Extended-Law-of-Sines computation
expressing `O`'s `BC`-perpendicular projection in terms of `∠A,∠B,∠C,φ`
and verifying `φ`-cancellation. Not yet attempted by any builder.
Cases to cover: none additional beyond the file's existing H1-H3 setup
(no casework introduced by this reduction).
Watch out for:
  - Item 3/4 of the diversity explorer's report (bare power-of-a-point /
    side-length-product identities) are confirmed dead ends this round —
    do not re-try `AK\cdot AC=AL\cdot AB`, `BK\cdot AC=CL\cdot AB`, or
    "power of `M`/`N` via second intersections `P_{AB},P_{AC}`" directly
    against `A,B,C`-only ratios; all are either numerically false or
    definitionally circular (restate `OM=ON` rather than bypass it).
  - The file's own **Open gap 2** (the containment/sign-convention
    assumption for the directed-angle setup — `K` between rays `BL,BA`,
    `L` between rays `CA,CK`) is only numerically corroborated so far (15
    sample points, all consistent) — this is a separate open gap from the
    O-M-N bridge and should not be silently assumed proved when the
    builder writes up step 2/3.
  - Do not spend further budget on route (a) (`-pointwise-sos`)'s SDP
    diagnostics this round — the diversity explorer's witness-dependence
    finding weakens the "clean uniform degeneracy" hypothesis, and no new
    lever was found; an enlarged generator/degree ansatz (not diagnostics)
    would be the only justified next spend there, and this round
    prioritizes the two approaches above instead.

build set: coordinate-bash-resultant-boundary-pointwise-tangent, spiral-similarity-bootstrap
