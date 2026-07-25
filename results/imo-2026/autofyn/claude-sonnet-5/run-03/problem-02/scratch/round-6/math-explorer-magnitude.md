## imo-2026-02

### (1) The magnitude bound t1<t1max(β) — precise status

**What t1, t1max(β) mean.** In the rotation parametrization (§§1–2 of
`coordinate-bash-resultant-boundary.md`), `K=B+t1·d(β)` with
`d(β)=(-cosβ,sinβ)` the direction of ray BK and `t1=BK>0` a free magnitude.
Hypothesis 3 (`∠LCK=∠BMK`) determines `t1` as a function of `β` via the
quadratic `G_{3a}(t1)=0` (on the presumed-genuine branch). Separately, "K
inside triangle BMC" is a containment condition on the actual point
`K=B+t1 d(β)`, not just on the ray direction. §8 proves rigorously that for
`β∈(0,∠ABC)` the *direction* `d(β)` stays strictly inside the angle
`∠MBC=∠ABC` (i.e. K is on the correct side of both lines BM and BC) — but a
point on a valid-direction ray only lies inside the *finite* triangle BMC if
its distance from B is less than the distance to where that ray crosses the
third edge MC. `t1max(β)` := that crossing distance (explicit as the
intersection of ray `B+t·d(β)` with line MC, a rational function of
`β,a,b,cc`). The open gap is: prove the actual root `t1(β)` of `G_{3a}=0`
(the one selected, going forward, by Theorem 11.8's sibling for hypothesis 3)
satisfies `t1(β)<t1max(β)` for every β in the valid range and every
triangle. This has only been checked numerically (§4/§9's multi-triangle
sweeps show K always lands inside BMC on sampled points) — no proof exists.

**Does §11's (Theorem 11.8/11.10) cross-product-sign machinery supply this
for free? No — it is a genuinely different sign test, needs independent
work, BUT the same technique looks directly transferable.** §11's test is
`cross(BK,BL)<0` (relates K to L, an inter-point condition coming from
hypothesis "K inside angle LBA"), reduced via Lemma 11.1's three-cross-product
angle test but specifically the *middle* cross product between two rays from
B (BK and BL), not a side-of-a-line test against a fixed segment like MC. It
does not touch the point M, N, or the edge MC/NB at all, so it cannot be read
off as a byproduct — it is a logically independent fact.

However, the **containment-against-edge-MC test is structurally the exact
same species of computation** as §11's machinery, and this is a concrete,
promising *new* opening (not previously flagged this precisely in the
population):
- "K on the correct (B-)side of line MC" ⟺ `cross(C-M, K-M)` has the same
  sign as `cross(C-M, B-M)` — a standard affine half-plane test (same
  primitive as Lemma 11.1, applied to a different pair of points).
- `K-M = (B-M) + t1·d(β)` is **affine-linear in `t1`**, exactly the shape
  Lemma 11.5 exploited for `L_1(s2)=P+s2 Q`. So `cross(C-M,K-M) =: N_1(t1) =
  P'(u) + t1 Q'(u)` for explicit `P',Q'` (a short, mechanical `sympy`
  computation, not yet done).
- Since `t1` is a root of the quadratic `G_{3a}(t1)=0`, one can attempt the
  identical resultant/Vieta argument: compute
  `Res_{t1}(G_{3a}, N_1) = (\text{explicit factors})`, and try to pin its
  sign throughout the valid range (as Lemma 11.6/11.7 did for `F_1,F_2,A_2`)
  to conclude the two roots of `G_{3a}` split the "correct side of MC" test
  the same way Theorem 11.8 split "K inside angle LBA."

If this transfer works, it would very likely need to be **combined**, not
run independently, with Theorem 11.8/11.10's existing sign test (the
genuine root must satisfy *both* the cross(BK,BL) test *and* the
cross(C-M,·) test simultaneously) — worth flagging to the outliner as a
natural extension of §11 rather than a wholly separate lemma. This is not
yet attempted by anyone in the population; it is a concrete, mechanically
tractable next step (a few `sympy.resultant` calls plus a sign case-split
in the style of Lemma 11.7), not a vague hope.

### (2) Sanity check: are G2b-exclusion / sextic-positivity really the *sole*
remaining sub-gaps?

**No — for the coordinate route, "G2b-exclusion" undersells what's still
open; there are at least four distinct, only-partly-overlapping open
sub-pieces**, all explicitly flagged in `coordinate-bash-resultant-boundary.md`
itself (§6, §8, §9, §10, and the "What §11 does and does not establish"
paragraph at the end of §11):

1. **G2b exclusion** (§11 end): the extraneous branch's leading coefficient
   `B2` does not have a fixed sign across triangles (checked numerically,
   3000 samples), so the clean "always splits" argument of Theorem 11.8
   does not transfer to G2b — ruling G2b out as a competing valid solution
   (jointly with hyp-3 and full containment) is open.
2. **Magnitude bound t1<t1max(β)** (§8, this round's assigned focus) —
   distinct from (1): even granting G2a/G3a are the "genuine algebraic
   branch" and their sign-selected roots pass the direction test, no one
   has shown the actual *point* stays inside the finite triangle (not just
   the correct angular sector). See (1) above for a candidate technique.
3. **F3/F3' crossings-harmless-in-general** (§9): a genuine counterexample
   shows these un-shared resultant factors DO have roots strictly inside
   the valid β-range for many triangles (not "always outside" as earlier
   rounds assumed); numerics (2 traced crossings in high resolution, plus
   spot checks) strongly suggest the genuine branch survives these
   crossings undisturbed, but no proof exists. This is logically prior to
   (1)-(2) if one insists on the continuity/IVT framing — see the new idea
   below for a way to route around needing it at all.
4. **Extra-hypothesis range restriction** (§10): whether "K inside angle
   LBA" / "L inside angle ACK" cut the valid β-range shorter than
   `(0,min(∠B,∠C))` is not fully resolved — §11 gives a *pointwise*
   selection criterion (for each fixed β, which root is valid), but this is
   not the same as confirming the whole range stays connected/nonempty
   under the joint constraint of hyps 1–3 plus both containments plus the
   two extra "inside angle" conditions simultaneously.

These are related but NOT literally the same gap — a builder closing (1)
alone would not automatically close (2)-(4). The outliner should treat this
as a small cluster of sub-lemmas, not a single atomic gap, when scoping next
round's build tasks. (For the Ptolemy route: the "sextic positivity Ψ>0"
framing genuinely IS the sole remaining gap, per current.md and the file
itself — no hidden sub-gaps found there in this pass; other explorers are
covering it in depth.)

### A genuinely fresh idea: replace continuity/IVT with a direct pointwise
exclusion, potentially bypassing gap (3) [F3/F3'] entirely

The population's whole "continuity/IVT" framing (§4, §9) exists because the
plan was: fix a base point (anchor β), verify G2a is genuine there, then
argue the "genuine branch" label can't flip except at resultant-zero
crossings, so if none of those crossings actually flip it, G2a=0 stays
genuine throughout the range. This requires classifying *every* resultant
factor's crossing behavior (F1, F2, F3, and their hyp-3 counterparts) — a
combinatorial burden that's exactly gap (3).

**An alternative, avoiding continuity altogether**: Theorem 11.8 already
gives, *for each individual β* (no continuity needed), a specific
sign-selected root of G2a satisfying "K inside angle LBA" (given
L∈△BNC). If one can similarly show, **pointwise, directly** (no IVT):
(a) the *other* root of G2a fails the sign test or fails containment
(already implied by Theorem 11.8's "exactly one root" statement — the other
root literally fails "K inside angle LBA"), and
(b) **both** roots of G2b fail at least one of: the sign test, the
magnitude bound, or hypothesis-3's joint constraint (for every β, not just
generically) —
then G2a's selected root is the *unique* candidate satisfying every
hypothesis, for every single β independently, with no need to ever discuss
what happens at F1=0, F2=0, F3=0 crossings, whether they're "harmless," or
range-connectedness at all. This would fully retire gap (3) as irrelevant
(not just close it) and reduce the remaining work to two purely algebraic,
per-β sign computations (in the style of Lemma 11.7's case-split), which is
exactly the kind of computation §11 already demonstrated is tractable for
G2a. This is worth proposing to the outliner as a genuinely different
framing of the SAME target (still "coordinate route branch selection") that
sidesteps the specific F3/F3' obstruction the population has been stuck
circling since round 4 — a shift from "track branch labels along a
continuous path" to "algebraically test all four candidate roots (2 from
G2a, 2 from G2b) against every hypothesis, independently at each β." It is
untested — no one has yet tried computing G2b's roots' behavior under the
magnitude/full-containment test — but is a concrete, mechanically
well-defined next step, distinct from anything flagged as a dead end.

### Candidate technique(s)
- Extend §11's resultant/Vieta cross-product-sign machinery (already proved
  correct and reusable) to the MC/NB edge containment test, for the
  magnitude bound.
- Consider replacing the continuity/IVT branch-selection strategy with a
  fully pointwise (per-β) 4-candidate-root exclusion argument, to make the
  F3/F3' crossing question moot rather than resolved.

### Cheap-kill candidates
None new found this pass beyond what's already in the population (Lemma
11.6/11.7-style sign case-splits on b≥0 vs b<0 remain the main tool). Worth
a quick numeric check next round: evaluate `B2` (G2b leading coeff) plus a
prospective magnitude-bound cross product at G2b's roots on a handful of
triangles, to see if G2b's roots fail containment/magnitude outright even
without a sign-splitting theorem — a cheap pre-check before investing in the
full symbolic pointwise-exclusion argument above.

### Knowledge-base entries to use
- Resultants for common-root/ideal-membership tests (already the backbone
  of §3, §4, §11) — knowledge_base.md's resultants + polynomial
  ideal-membership entries (Cox–Little–O'Shea, as cited in the file).
- Standard cross-product/signed-area "point inside triangle/angle" test
  (already used throughout; same primitive needed for the MC-edge test).

### Analogous past problems (cruxes)
Per prior rounds' finding (still valid, confirmed again by scanning
`crux_moves_documentation.md`'s subtopics list): the crux corpus has no
geometry-domain entries, so no genuinely analogous crux move exists for
this problem's specific coordinate-bash/resultant-branch-selection
machinery. None found this pass either — did not re-run the full corpus
query since this is an established, previously-verified negative (see
`/tmp/memory/math-explorer.md` rule 3); no reason to expect it changed.

### Prior progress
See current.md / approach file for the full record (summarized above).
Headline still-standing facts: gap 1 (genericity) fully closed; isosceles
case fully closed; Theorem 11.8/11.10 (G2a/G3a root-splitting via
cross(BK,BL)) fully closed and independently reproduced. Remaining: the
4-item cluster above for the coordinate route; sextic positivity for the
Ptolemy route.

### Dead ends (do not retry)
- Acute-angle-bound branch selection (refuted, round 4, obtuse
  counterexamples up to 123.5°).
- Naive "F1,F2 are the only relevant resultant factors" assumption (refuted,
  round 4, F3/F3' have interior roots on many triangles).
- Literal transfer of Ptolemy's IVT+quadratic-degree technique to the
  coordinate route (confirmed round 5, type mismatch — quartic vs
  quadratic).
- The three ruled-out auxiliary circles (nine-point, circle-through-BC,
  target circle itself) for the Ptolemy-synthetic route (round 5) — not
  relevant to this lens but noted per run_state's do-not-retry list.

### Small-case / intuition notes
No new numerics run this pass beyond re-reading the file's own reported
sweeps (16 points across 4 triangles, all consistent with G2a/G3a genuine,
K/L inside their triangles). The proposed MC-edge cross-product transfer
and the pointwise-exclusion reframing are both untested conjectural next
steps, not yet checked even numerically — flagging as the concrete
actionable items for next round's outliner/builder, with a recommendation
to first do a cheap numeric sanity pass (a handful of triangles) on the
MC-edge sign formula and on G2b's roots' containment/magnitude behavior
before committing to the full symbolic proof.
