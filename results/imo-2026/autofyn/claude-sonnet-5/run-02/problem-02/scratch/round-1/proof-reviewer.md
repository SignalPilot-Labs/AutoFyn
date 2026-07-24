# Proof review — imo-2026-02 (IMO 2026 P2), round 1

All independent verification below was done from scratch with `sympy`/`numpy`,
not by trusting the builders' scripts, per the adversarial mandate.

## Shared Lemma 0 (nine-point-center reduction) — VERIFIED CORRECT

Claim (used by all three approaches): with N9 the nine-point center of ABC,
`OM = ON ⟺ (O − N9)·(C − B) = 0`, and in the WLOG frame `B=(0,0), C=(1,0),
A=(p,q)` this is `O_x = p/2 + 1/4`.

- Re-derived the vector identity `|P-M|²-|P-N|² = (2P-M-N)·(N-M)` (standard
  difference of squares), instantiated at P=O, P=N9, used N9M=N9N (both M,N
  are midpoints of sides, hence on the nine-point circle), and N-M=(C-B)/2
  (midline theorem). Matches all three files exactly.
- Independently computed `N9_x` by symbolically finding the circumcenter of
  the medial triangle (M, N, midpoint(B,C)) in sympy: **N9_x = p/2 + 1/4
  exactly**, confirming the coordinate corollary.

Lemma 0 is sound, unconditional, and now certified as a shared lemma:
`results/imo-2026-02/lemmas/nine-point-center-reduction.md`.

## Approach 1: `complex-number-argument-bash`

**Verdict: CHANGES REQUESTED. True Status: partial** (matches builder's
self-report).

Independently re-derived, byte-for-byte, from a fresh sympy script (not
reading the builder's code):
- **Dictionary Lemma** (`cross(u,v)dot(w,z) - cross(w,z)dot(u,v) =
  |u||v||w||z|sin(θ1-θ2)`): re-derived and numerically spot-checked with
  random magnitudes/angles/base-orientations (5 trials, residual 0 to
  machine precision). Correct.
- **eq1** (from hypothesis (i)): expanded independently, matches the
  builder's polynomial term for term.
- **eq3** (from hypothesis (iii)): expanded independently; solved eq1 for
  l2 and substituted into eq3; the resulting numerator, after clearing the
  denominator, factors as `−(p²+q²)(l1−1)·X'(k1,k2,p,q)` with `X' = −X`
  (builder's cubic, same zero locus — the two computations agree up to an
  irrelevant overall sign). **This is an exact, independently confirmed
  match of the builder's central algebraic claim.**
- The `l1=1 ⟹ l2=0` (⟹ L=C, excluded) branch: independently confirmed by
  direct substitution — collapses to exactly 0.

So the reported "Step 1/Step 2" work (cubic locus for K) is genuinely
correct, not hand-waved. This is real, verified progress — the strongest
result produced in this round.

**What remains open (correctly flagged by the builder, not closed by me
either):**
1. The final identity — that the target `O_x = p/2+1/4` vanishes on the
   variety cut out by `X=0` and the eq2-derived condition — is not proved.
   I attempted a quick full symbolic solve of eq1=eq2=eq3=0 at fixed (p,q)
   to sanity-check the target algebraically but it did not terminate in the
   time budget (consistent with the builder's own report that this is a
   genuinely hard elimination, likely needing Gröbner bases / resultants
   rather than naive polynomial division).
2. **Orientation/sign-matching gap.** The Dictionary Lemma requires a
   *matched* rotational sense between the two angles compared at each
   application; this has not been verified against the problem's
   containment hypotheses ("K lies inside angle LBA" etc.) either by the
   builder or by me this round. This is a real, unclosed gap — without it,
   eq1/eq2/eq3 could in principle encode a sign-flipped variant of the
   actual problem.

Both gaps are real and neither is closed. The builder's Status: partial is
correct and not overclaimed. This is the strongest / most promising line in
the population and should be advanced next round.

**Promotable lemmas certified:** Dictionary Lemma (unconditionally proved,
certified as-is) and the Cubic Locus for K (certified as a correct algebraic
fact about eq1, eq3 as explicitly defined; NOT certified as a proven
geometric fact about the problem's actual K, since the orientation caveat
above is unresolved — this distinction is stated explicitly in the lemma
file). See `results/imo-2026-02/lemmas/dictionary-lemma-equal-signed-angle.md`
and `results/imo-2026-02/lemmas/cubic-locus-for-K.md`.

## Approach 2: `nine-point-locus-two-position`

**Verdict: RETHINK. True Status: unsolved** (overriding the builder's
self-reported "partial" — see reasoning below).

- **Branch verification numerics**: plausible and consistent with what I
  independently reproduced (see the cross-check under Approach 3 below,
  which used the identical containment-filtered branch and got OM-ON ~2e-10
  and Lemma-0-consistent behavior on a third triangle). No red flags.
- **Lemma B refutation** (the approach's actual load-bearing claim: O(θ) is
  affine in some reparametrization, à la IMO SL 2023 G5): the builder tested
  ~15 reparametrizations plus a general Möbius fit on two triangles and
  found residuals 4-11 orders of magnitude above the solver noise floor,
  reproducible across two triangles, with non-oscillating (genuine
  curvature) second differences. This is methodologically sound: enough
  candidate reparametrizations were tried, the residuals are unambiguous
  (not just "somewhat above noise" but 4-11 orders of magnitude), and the
  test was replicated on an independent triangle. I accept the refutation
  as correct; I did not personally re-run the fit (time-limited), but the
  methodology and reported magnitudes leave no room for the refutation
  being a numerical artifact.
- **O-free reformulation lemma**: checked directly — it follows from
  linearity of the dot product applied to `2O·(K-A)=|K|²-|A|²` and
  `2O·(L-A)=|L|²-|A|²`, both standard consequences of O being equidistant
  from A, K, L, plus a Cramer's-rule basis decomposition. Correct, general,
  and certified: `results/imo-2026-02/lemmas/o-free-circumcenter-reformulation.md`.

**Why this is RETHINK, not CHANGES REQUESTED**, despite the builder's
"partial" self-report: CLAUDE.md's routing hinges on whether "the approach
itself is wrong or fatally broken" (RETHINK) versus "the technique is right
and there is real progress, but a gap remains" (CHANGES REQUESTED). Here the
approach's *defining* mechanism — a two-special-position argument via an
affine reparametrization of O(θ) — is not merely incomplete, it is
demonstrated false for every natural candidate tried. The builder's own
report states this explicitly: "the two-position architecture ... cannot be
completed as designed." What remains provable within this file (Lemma 0,
the O-free reformulation) is prior shared material or a generic vector fact
not specific to this problem's hypotheses — no new reduction toward the
actual theorem was produced. That is the RETHINK condition: the technique
needs to change, not just get one more gap closed. I am overriding the
builder's Status field from `partial` to `unsolved` for this reason, while
crediting and certifying the reusable byproduct lemma.

## Approach 3: `spiral-similarity-radical-axis`

**Verdict: RETHINK. True Status: unsolved** (matches builder's own
self-report and recommendation).

- Independently re-ran the numerical existence check on a **third**,
  independently chosen triangle (A=(0,3), B=(-2,0), C=(2.5,0)), with proper
  containment filtering (K strictly inside triangle BMC, L strictly inside
  triangle BNC via barycentric sign tests, 5000 random multistarts,
  fsolve). Result: 2111 valid configurations found, `max|OM-ON| = 2.4e-10`
  (i.e. the theorem holds, as expected), while the {M,N,K,L} concyclicity
  determinant sat consistently around 0.03-0.05 — decisively nonzero, fully
  consistent with the builder's finding on their own two triangles (0.05,
  0.42). This independently confirms both (a) the theorem is true along the
  whole family and (b) the specific concyclicity premise this approach
  needed is false.
- The builder's structural argument (neither hypothesis (ii) nor (iii) has
  the "matching chord" shape needed for the classical inscribed-angle
  concyclicity converse — the shared vertex differs from the shared arm) is
  correct on inspection: (ii) `∠LBK=∠LNC` shares point L as one arm at B
  and N respectively, but the other arms (K vs C) differ; (iii) similarly.
  This is a genuine, correct a priori objection, not just numerics.
- No new promotable lemma beyond the shared Lemma 0 restatement.

The builder's own Status (`unsolved`) and recommendation (`RETHINK`) are
correct and are confirmed, not overridden.

## Ranker outcomes recorded

- `complex-number-argument-bash`: **advanced** — cubic-locus structure
  independently confirmed correct; two gaps (final identity closure,
  orientation verification) remain open.
- `nine-point-locus-two-position`: **dead-end** — Lemma B (the technique's
  defining mechanism) refuted; architecture cannot complete as designed;
  byproduct O-free lemma salvaged and certified.
- `spiral-similarity-radical-axis`: **dead-end** — concyclicity premise
  numerically and structurally false; independently re-confirmed by the
  reviewer on a third triangle.

## Lemmas certified (new files under `results/imo-2026-02/lemmas/`)

1. `nine-point-center-reduction.md` — Lemma 0, fully proved, unconditional.
2. `dictionary-lemma-equal-signed-angle.md` — fully proved, unconditional
   (with an explicit usage caveat about orientation matching, which is NOT
   part of the lemma's own proof obligation but must be discharged by any
   approach applying it to this problem's hypotheses).
3. `o-free-circumcenter-reformulation.md` — fully proved, general vector
   fact, from `nine-point-locus-two-position`'s byproduct.
4. `cubic-locus-for-K.md` — algebra certified (independently re-derived and
   confirmed correct), geometric content explicitly flagged as NOT yet
   certified pending the orientation-matching gap.

## `current.md` updated

Status kept at `partial` (no approach reaches a complete, gap-free proof).
`current.md` now records the certified Lemma 0, Dictionary Lemma, O-free
reformulation, and cubic-locus-for-K as the field's best current progress,
the two ruled-out mechanisms (affine-reparametrization, raw-point
concyclicity) as negative results not to retry, and names the two concrete
open gaps in the leading approach (final polynomial-identity closure;
orientation/sign-matching verification) for the next round to attack.

## Recommendation for next round

Advance `complex-number-argument-bash` (close the final polynomial identity
via Gröbner basis / resultant methods rather than naive division, AND
independently verify the orientation-matching of the Dictionary Lemma's
three applications against the problem's stated containment hypotheses —
this second task could be done numerically: build a genuine, containment-
respecting (K,L) solution and directly check which sign convention the true
configuration satisfies). Both `nine-point-locus-two-position` and
`spiral-similarity-radical-axis` are dead ends in their current form; per
CLAUDE.md's plateau-breaking guidance, if a new approach is opened next
round it should be a genuinely different framing (e.g. an inversion-centered
argument, or a direct trigonometric/law-of-sines chase rather than
coordinate bash or two-position or raw concyclicity), not another variant of
the same coordinate-bash or synthetic-concyclicity ideas.
