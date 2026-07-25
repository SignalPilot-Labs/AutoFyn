# Proof review — round 8, imo-2026-02

Adjudicated all 4 built approaches. Independently rebuilt every load-bearing
claim from scratch in fresh `sympy`/`numpy` sessions (own code, own variable
names — never re-ran or trusted a builder's script). No approach reaches
`solved`. Status stays `partial`. Verdicts below are per-approach, per
CLAUDE.md's per-slug routing.

## 1. `coordinate-bash-resultant-boundary` — Verdict: **CHANGES REQUESTED**
(Status: partial — matches file's own claim)

**Independently re-derived and confirmed exactly** (own `sympy` session,
own symbols, not copying the file's `Q(m)` formula's internal steps beyond
its bare definition):
- `disc(Q) = β1² − 4αγ1` for `Q(m)=m²sin(A+β)−4m sinβ−4sin(A−β)` collapses
  to `16sin²A` exactly (`sympy.simplify` residual 0), using the product-to-
  sum identity `sin(A+β)sin(A−β)=sin²A−sin²β` (elementary, checked by hand).
- The exact factorization `Q(m)=sin(A+β)(m−r1)(m−r2)` with the displayed
  `r1,r2` closed forms: residual 0.
- **The claimed counterexample to `M0≤r2` is real, not a computational
  artifact.** Independently recomputed at the file's own witness
  `A≈1.4829, B≈0.1626, β≈0.1611`: got `C≈1.4961` (`A+B+C=π` ✓, `β<min(B,C)`
  ✓), `M0=2cos²β/cosA≈22.197`, `r2=2(sinβ+sinA)/sin(A+β)≈2.319`. This
  matches the file's reported numbers to the stated precision — **a
  genuine, large-margin (factor ~9.6) counterexample**, not a rounding
  artifact. This corrects a lever the outliner had proposed; the file's
  self-correction is honest, precise, and independently confirmed.
- The Law-of-Sines reformulation (I),(II): independently spot-checked at
  12,588 fresh samples (own script, own seed, filtering `sin(A+3β)<0` for
  (I) and additionally `Y>0` for (II)): **0 violations of either**,
  corroborating (not proving) the file's own larger sweeps.

Both (I) and (II) remain unproved symbolically — honestly disclosed as such,
no overclaiming. Certified `lemmas/q-quadratic-discriminant-and-roots.md`
(the disc/roots/factorization fact — clean, unconditional, reusable). The
`M0≤r2`-is-false finding and the (I)/(II) reformulation are recorded as
promotable "negative result + sharper target" content in the file itself
(round-8 Promotable-lemmas section), which I reviewed and found accurately
scoped (no claim of proof where only numerics exist).

## 2. `coordinate-bash-resultant-boundary-pointwise` — Verdict: **CHANGES
REQUESTED** (Status: partial — matches file's own claim)

**Independently rebuilt from the raw vector definitions** (own script, not
copying the file's `L1`, `D_K` polynomials): computed `cross(d,v)` and
`dot(d,v)` directly for `d=(-cosβ,sinβ)`, `v(s2)=L(s2)−B`, and confirmed
their `s2`-slopes are exactly `b sin2β+cc cos2β` and `b cos2β−cc sin2β`
respectively (residual 0 both). Confirmed these trig-identify exactly as
`AC sin(2β+∠A)` and `AC cos(2β+∠A)` (using `b=AC cosA, cc=AC sinA`,
elementary angle-addition — residual 0). This independently confirms the
Step 0 identity `d̄·v(s2) = D_K(s2)+iL1(s2)` (via the standard complex-
number fact `Re(d̄v)=dot(d,v)`, `Im(d̄v)=cross(d,v)`).

**Confirmed `sin(2β+∠A)>0` unconditionally**: `β<min(∠B,∠C)≤(∠B+∠C)/2` ⟹
`2β<∠B+∠C` ⟹ `2β+∠A<π`; trivially `2β+∠A>∠A>0`. Elementary, no gap.

**Verified the "which root" argument (r_lo lemma) is logically sound**,
given the already-population-certified fact `L1(r1)L1(r2)<0`
(`lemmas/cross-product-sign-selection-G2a.md`, independently reverified by
this population in round 5): an increasing continuous function with a
unique real zero straddled by two given points is negative at the smaller
and positive at the larger of those two points — this is the correct,
complete logic, no missing case. This is a genuine, unconditional
strengthening of Theorem 11.8 (existence/uniqueness → explicit identity of
the root). Certified as
`lemmas/complex-affine-L1-DK-and-r-lo-selection.md`.

**Honest-disclosure check (per dispatch instruction): PASSED.** The further
progress toward `W(r_lo)>0` (the `D_N(m0)` trig-fit identity, matched by 20
numeric substitutions but not `sympy.simplify=0`) is explicitly and
correctly flagged in the file as "not yet elevated to a certified symbolic
identity" — not counted toward closing anything, and I concur it should
not be certified. Good practice, no overclaim found.

## 3. `fixed-point-concyclic` — Verdict: **CHANGES REQUESTED** (Status:
partial — the route's own remaining content is now fully collapsed onto
the shared bottleneck, but the whole problem remains open)

This is the round's most consequential claim, and I gave it the most
scrutiny per dispatch instruction: **independently rebuilt the ENTIRE
pipeline from scratch**, not re-running the builder's code and not even
reusing its displayed intermediate polynomials:
1. Built `eq2` (hypothesis 2: ∠LBK=∠LNC) and `eq3` (hypothesis 3:
   ∠LCK=∠BMK) directly from the raw vector definitions, using my own
   `cross_eq`-style squared-cosine construction
   (`dot1²·|V3|²|V4|² − dot3²·|V1|²|V2|² = 0`) with my own choice of test
   vectors (`V1=L−B,V2=K−B,V3=L−N,V4=C−N` for hyp 2;
   `V1=L−C,V2=K−C,V3=B−M,V4=K−M` for hyp 3).
2. Confirmed (own polynomial division) `eq2` divisible exactly by `t1²`
   with `t1`-independent quotient, and `eq3` by `s2²` with `s2`-independent
   quotient — independently re-confirming the homogeneity-decoupling lemma.
3. Factored both quotients (`sympy.factor`) and identified `G2a` (deg 4 in
   `u`, deg 2 in `s2`) and `G3a` (deg 4 in `u`, deg 2 in `t1`) by their
   degree signature.
4. Built the circumcenter `O` of `A,K,L` from scratch (own perpendicular-
   bisector Cramer's-rule system, not copying anyone's formula) and the
   central target `T`; ran `sympy.groebner([G2a,G3a],...)` (own basis,
   18 generators — **matches the certified count exactly**) and
   `gb.reduce(T)`: **remainder 0** — this independently re-confirms
   `lemmas/symbolic-genericity-certificate.md` as a byproduct, from my own
   fully independent `G2a,G3a`, not the file's.
5. Built `Q = (C C̄−B B̄)/(2(C̄−B̄))`, `χ=L(K−Q)/(Q(K−L))`, and `χ−χ̄` (own
   denominator-clearing convention, differing from the file's — mine is not
   byte-identical to the file's `T2`, but is a legitimate numerator of the
   same rational function `χ−χ̄`). Confirmed `(χ−χ̄)/i` is purely real (no
   residual `I`-dependence) — matches the file's claim that this quantity
   is purely imaginary.
6. **Reduced my own `T2` against my own Gröbner basis of `⟨G2a,G3a⟩`:
   remainder 0.** Confirmed nonzero remainder modulo `⟨G2a⟩` alone or
   `⟨G3a⟩` alone (ruling out the degenerate single-generator pitfall).

**This is a full, independent, from-scratch reproduction of Theorem 8 —
not merely spot-checking the builder's numbers.** The claim is confirmed:
`Rem=0` (χ real) genuinely is a free formal polynomial corollary of
`G2a=G3a=0`, requiring no further sign/positivity content. Certified as
`lemmas/rem-zero-free-corollary-of-genericity-branch.md`.

**Honest-disclosure check: PASSED.** The file correctly and explicitly
states this does NOT close the whole problem — only that this route's own
remaining content collapses entirely onto the pre-existing, still-open
branch-selection gap (G2a=G3a=0 vs. G2b=G3b=0). No overclaiming found;
Status `partial` is exactly right.

## 4. `inversion-at-A-collinearity` — Verdict: **CHANGES REQUESTED** (Status:
partial — a correct, complete negative result, honestly reported; not a
broken/wrong approach, so not RETHINK, but nothing further to build on this
specific lever)

**Independently verified the central claim exactly**: with `K,L,Q` free
symbols (own `sympy` session), `ρ − χ` where
`ρ=(1/Q−1/K)/(1/L−1/K)` and `χ=L(K−Q)/(Q(K−L))` simplifies to `0`
identically. This confirms the file's claim is not merely "equivalent in
difficulty" but **literally the same rational function**, term for term —
a stronger and more useful negative result than the outline anticipated,
correctly triggering the outline's own fail-fast instruction. The file's
Step 2 (concyclic-through-origin ⟺ inverted images collinear, via the
explicit `z z̄+p̄z+pz̄=0` circle equation) is a standard, correctly-executed
elementary derivation (not a black-box citation) — checked by hand, no
gap. Certified as an addendum to
`lemmas/cross-ratio-real-concyclic-criterion.md`.

This is a genuinely useful, correctly-scoped negative result (dispatch
question #4 answered: the identity holds **exactly**, not just
equivalent-in-difficulty) — not a false negative. Recorded via
`record_outcome` as `dead-end` (as an independent route; the approach
itself correctly diagnosed its own exhaustion) rather than `advanced`,
since it produces no further leverage on the problem, but this is not a
mistake or a wasted round — precisely the kind of honest negative result
CLAUDE.md values.

## Does anything close the whole problem this round?

**No.** Status remains `partial`. But this round produces a structurally
important, independently-certified fact: **every live framing in the
population (coordinate/resultant, fixed-point/bilinear-Cramer, and now
inversion) is proved — not merely observed numerically — to reduce to the
identical branch-selection condition** `G2a=G3a=0` vs. `G2b=G3b=0` (more
precisely: (a) `coordinate-bash-resultant-boundary`'s two-part trig
inequality (I)/(II) for `G2b` exclusion, and (b)
`coordinate-bash-resultant-boundary-pointwise`'s `W(r_lo)>0` question for
the `G2a`-internal same-root correlation). This convergence is now a
certified structural fact (via `Rem=0`'s proof as a free corollary, and
`ρ=χ`'s exact identity), not a coincidence of numerics — I have recorded
this explicitly in `current.md`'s new "Round 8 update" section, and
recommend future rounds shift priority from "diversify framing further"
(largely exhausted this round — inversion collapsed into the existing
target) to "attack the shared polynomial-sign target itself" (e.g. Sturm's
theorem / sign-variation counting on the now-fully-explicit trigonometric
inequalities (I),(II) and the `σ_K,σ_N` sign questions), since another new
framing is likely to collapse into the same target again.

## Lemmas certified this round

- `lemmas/q-quadratic-discriminant-and-roots.md` (new)
- `lemmas/complex-affine-L1-DK-and-r-lo-selection.md` (new)
- `lemmas/rem-zero-free-corollary-of-genericity-branch.md` (new — the
  round's strongest result)
- `lemmas/cross-ratio-real-concyclic-criterion.md` (addendum: `ρ=χ` exact
  identity)

## `current.md`

Updated: new "Round 8 (this round)" entry under `## Approaches tried`
(prior round entries renumbered/preserved as "Round 7 (preserved)" etc.,
unchanged in content); new "## Round 8 update" section before `## Full
proof`, describing the certified convergence fact; `## Full proof` closing
paragraph updated to reflect the round's findings. `## Status` remains
`partial` — no overclaiming.

## record_outcome calls made

- `coordinate-bash-resultant-boundary` → `partial`
- `coordinate-bash-resultant-boundary-pointwise` → `partial`
- `fixed-point-concyclic` → `advanced`
- `inversion-at-A-collinearity` → `dead-end`
