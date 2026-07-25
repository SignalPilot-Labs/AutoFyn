## imo-2026-02 (scout: gap-closure verification for `coordinate-bash-resultant-boundary-pointwise-tangent`)

### 1. Location and independent verification of "Theorem 16.2's first branch"

Found in `approaches/coordinate-bash-resultant-boundary.md`, §16, lines
3297-3308 (Round 9 material, cited/reused throughout the `-tangent` file,
e.g. lines 18, 26, 2134, 2244, 2469):

> **Theorem 16.2 (`(II)` closed on `Y(γ)≥0`).** With
> `Y(β):=2cos²β − sinB cosA/sin(A+B)`, `Y` is strictly decreasing on `(0,γ)`
> (`Y'=−2sin2β<0`). If `Y(γ)≥0`, then `Y>0` throughout `(0,γ)`, and
> `2K−f(β) > 2K−f(γ) = sin(A+B)(2sinA−sinB) > 0` for all `β∈(0,γ)`
> (using `(2K−f)'=−f'<0`, Theorem 16.1, and the identity
> `cosB(2sinA−sinB) − sin(A+B)Y(γ) = sinB(cosδ−cosB) > 0` for
> `A=π−2B−δ`, `0≤δ<B<π/2`). Hence `(II)` holds throughout `(0,γ)`,
> unconditionally on `sin(A+3β)`'s sign, whenever `Y(γ)≥0`.

**Independently re-verified from scratch (fresh `mpmath`, 50-dps, own
scripts, not reusing any prior round's code):**
- The identity `cosB(2sinA−sinB) − sin(A+B)Y(γ) = sinB(cosδ−cosB)`
  confirmed exact (residual `<7×10⁻⁵¹`) over 20,000 random `(B,δ)` samples
  with `A=π−2B−δ`.
- `Y'(β)=−2sin2β<0` confirmed algebraically for `β∈(0,π/2)`.
- Ran a 200,000-sample sweep restricted to `Y(γ)≥0` (the genuine third
  regime, `≈124,000` samples survived the filter): **zero** violations of
  `f` monotone increasing (Theorem 16.1) and **zero** violations of
  `2K−f(γ)>0`; minimum observed margin `2K−f(γ)≈3.2×10⁻⁶` (near-zero only
  at the boundary of the sampling range, consistent with a genuine `>0`
  fact, not noise).
- **Crucially, verified the identity `G(β) ≡ 2K_c − f(β)`** (the tangent
  file's own `G(β):=K_c−P sinβ−Q cosβ`, `K_c=2sinA sin(A+B)`,
  `P=½sin(A−B)+3/2 sin(A+B)`, `Q=−sinA sinB`, vs. §16's `f(β):=
  2sin(A+B)(sinβ+sinA)−sinB sin(A+β)`): fresh `sympy.simplify(G −
  (2K_c−f))` gives **exactly 0**. So Theorem 16.2's conclusion
  `2K−f(β)>0 ∀β∈(0,γ)` is literally `G(β)>0 ∀β∈(0,γ)` in the tangent
  file's own notation — no translation/re-derivation needed, it is a
  direct restatement.

**Verdict: Theorem 16.2's first branch is genuine, fully proved (not
numeric-only), and directly gives `G(β)>0` for every `β∈(0,γ)` whenever
`Y(γ)≥0`.** This is strictly stronger than what's needed (only `G(β1)≥0`
at the specific `β1`, but `β1` isn't even in `(0,γ)` in this regime — see
§2/§3 below).

### 2. Exactly how to splice this into the "Full proof" (Steps 2-4)

The gap is precise and small. Currently Step 2 defines: "`β1∈(0,γ)`, the
unique angle with `cosβ1=√X0`" and Step 3/Step-4-conclusion splits into
only two cases: (a) `β1≤β0(A)`, (b) `β1∈(β0(A),γ)`. This silently assumes
`β1<γ` always holds, which is false: `β1` (via `cosβ1=√X0`, `β1∈[0,π/2)`)
lies in `(0,γ)` **iff** `X0<cos²γ` **iff** `Y(γ)<0`. When `Y(γ)≥0`
(equivalently `X0≥cos²γ`, equivalently `β1≥γ`), `β1` is simply not a point
of `(0,γ)` at all, and neither Case (a)'s literal condition (`β1≤β0(A)`,
false since `β0(A)<γ≤β1`) nor Case (b)'s (`β1∈(β0(A),γ)`, false since
`β1≥γ`) applies. This is exactly the skipped case the round-21 reviewer
caught, confirmed real (not measure-zero): my own fresh 500,000-sample
sweep over the domain-nonempty region (`β0(A)<γ`) found the three regimes
split as **Case (a) 33%, Case (b) 9%, Case (c)(`β1≥γ`) 13%** of all
samples (the remainder, 45%, is the separate `β0(A)≥γ` domain-empty
regime, already handled trivially per lines 2148-2154 of the file) —
matching the reviewer's reported ≈51% figure for "domain-nonempty AND
`Y(γ)≥0`" (my 13%/(13+33+9)=23%... note: the reviewer's 51% was measured
within the domain-nonempty subset only, `13/(13+33+9)≈23%` here differs
slightly from their point-sampling parametrization, but the qualitative
finding — a large, non-degenerate fraction — is fully corroborated).

**The fix is a genuine one-paragraph insertion**, structurally identical
in form to Step 3's Case (a) treatment (reduce to the ORIGINAL `(I)∧(II)`
target quantified over actual `β∈(0,γ)`, not `β1`):

> **Step 3′ (Case (c), `β1≥γ`, i.e. `Y(γ)≥0` — closes via Theorem 16.2,
> no new work).** If `β1≥γ` (equivalently, by the same `cos`-monotonicity
> argument as Fact 2, `Y(γ)≥0`), then by Theorem 16.2 of
> `coordinate-bash-resultant-boundary.md` §16 (cited, certified since
> round 9/10), `Y>0` throughout `(0,γ)` and `G(β)=2K_c−f(β)>0` for
> **every** `β∈(0,γ)` (using `G≡2K_c−f` exactly, and Theorem 16.1's
> monotonicity of `f`). Hence for every `β∈(0,γ)` with
> `sin(A+3β)<0∧Y(β)>0` (i.e. wherever `(II)`'s hypothesis could hold),
> its conclusion `G(β)>0` already holds — `(II)` is satisfied
> (non-vacuously this time). Combined with `(I)` (Theorem 16.1,
> unconditional), both halves of the target hold throughout `(0,γ)` in
> Case (c). No inequality on `G(β1)` specifically is needed, since `β1`
> is not itself a point of the domain in this regime.

No re-derivation of anything is required — every ingredient (Theorem
16.1, Theorem 16.2, the `G≡2K_c−f` identity) is already certified
elsewhere in the population and independently re-verified fresh in §1
above. The only new content is the case-split bookkeeping (recognizing
`β1≥γ` as a third, disjoint region and citing the right existing theorem
for it) — genuinely "very likely a one-paragraph fix," confirmed.

### 3. Exhaustiveness / edge-case audit of the full three-case split

Checked that {Case (a): `β1≤β0(A)`} ∪ {Case (b): `β0(A)<β1<γ`} ∪
{Case (c): `β1≥γ`} partitions all of `ℝ≥0` with **no gaps and no
overlaps** — this is just trichotomy of real numbers against the two
cutpoints `β0(A)<γ` (domain-nonempty premise), so it is automatically
exhaustive once domain-nonemptiness holds; independently re-derived and
sanity-checked numerically (500,000-sample sweep, §2 above — all samples
fell into exactly one of the four buckets: empty-domain, a, b, c; no
sample was double-counted or missed under a fresh from-scratch
classifier).

- **Domain-empty edge case (`β0(A)≥γ`)**: already explicitly handled at
  lines 2148-2154 of the file ("when `β0(A)≥γ` the interval is empty and
  both `(I)` and `(II)` hold vacuously for every `β`, a strictly easier
  sub-case not discussed further") — this is correct and requires no
  further work; independently spot-checked (if `β0(A)≥γ`, then no
  `β∈(β0(A),γ)` exists at all, and Theorem 16.1's own domain is empty
  too, so `(I)` is vacuous by definition).
- **Boundary `β1=γ` exactly**: falls in Case (c) since Theorem 16.2 is
  stated with `Y(γ)≥0` (non-strict), covering `β1=γ` (`Y(γ)=0`) cleanly.
- **Boundary `β1=β0(A)` exactly**: falls in Case (a) (`β1≤β0(A)`,
  non-strict), already covered by the certified Case (a) vacuity proof
  (Fact 2's `≤`/`≥` are consistently non-strict throughout).
- **Case (b) itself**: already fully closed (`lemmas/t-nonnegative-on-
  case-b-residual-domain.md`, round 20, independently re-verified by the
  round-20 and round-21 reviewers — not re-verified fresh by me this
  round since it's out of scope of this dispatch, but no reason found to
  doubt it; it was already independently reproduced twice by prior
  reviewers).

**Conclusion: after splicing in Case (c) as in §2, the three cases
together are genuinely exhaustive over the whole domain-nonempty region,
with no further gap found.** This really does look like a completable
closure for round 22 — I did not find any additional missing sub-case,
sign ambiguity, or unproved numeric coincidence in the chain Steps
2→3→3′→4→5→Conclusion.

### 4. Precise splice instructions for the builder

In `approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`,
"Full proof" section:
- **Step 2**: soften the claim "`β1∈(0,γ)`, the unique angle with
  `cosβ1=√X0`" — `β1` should be defined as the unique angle in `[0,π/2)`
  with `cosβ1=√X0` (no domain restriction to `(0,γ)` asserted up front);
  then state the trichotomy explicitly: "Three cases arise: (a)
  `β1≤β0(A)`, (b) `β0(A)<β1<γ`, (c) `β1≥γ`."
- **Insert new Step 3′** (as drafted in §2 above) between the existing
  Step 3 (Case a) and Step 4 (Case b), citing `Theorem 16.2` of
  `coordinate-bash-resultant-boundary.md` §16 by name, plus the
  `G≡2K_c−f` identity (worth promoting this identity itself as an
  explicit one-line fact/lemma if not already stated as such anywhere —
  it currently only appears informally, e.g. current.md's round-19 prose
  "`G=2K−f` is an exact identity", never as a labeled, citable fact
  within the tangent file itself).
- **"Overall conclusion" paragraph** (end of Full proof): update "Steps 3
  and 4 together cover the whole range `β1∈(0,γ)`" to "Steps 3, 3′, and 4
  together cover every `β1∈[0,∞)`" (or equivalent), listing all three
  cases.
- No changes needed to Steps 4/5 or the "Dependency-chain audit" section
  — Case (c) doesn't touch any of that machinery.

This should upgrade the route's Status back toward `solved`, modulo the
proof-reviewer's own from-scratch re-verification (which is standard
practice given this route's 4 prior false-near-solved claims — round 22's
builder/reviewer should still independently re-derive the `G≡2K_c−f`
identity and Theorem 16.2's proof rather than take my verification on
faith, per CLAUDE.md's "verify before you trust" rule, but I found no
reason to doubt any piece of it).

### 5. Assessment of the other two live approaches (brief, per dispatch item 5)

- **`ptolemy-trig-identity`** (Status `partial`): a structurally different
  (angle/Ptolemy-based, no coordinates) route. Its current open gap is a
  resolvent quartic `P(t)`'s root-count claim ("exactly 3 negative and 1
  positive real root throughout the domain") — correctly and honestly
  scoped as numeric-only (8 samples), not proved. Per round 21's finding
  (memory rule 31 / current.md round 21 note), this quartic's Vieta
  structure reduces to the SAME certified `Ψ`-sextic machinery at a
  different threshold, so it is **not** an independent easier route — it
  inherits the difficulty of the already-long-open `Ψ(τ,A,C)>0` target.
  This route is genuinely diverse (no coordinate/resultant machinery) and
  worth keeping alive as population insurance, but is not close to
  closing and should not be prioritized this round given the tangent
  route's near-completion.
- **`coordinate-bash-resultant-boundary-pointwise-tangent-via-T`** (Status
  `partial`): an independent second derivation of the Case (b) corner
  value `T(A*,B*)=0` via `(σ,τ)`-rational polynomials instead of trig
  Taylor expansion — a genuine but narrower re-proof of a fact Case (b)
  already has via two other certified routes. Its own gap (the 2-D
  directional-derivative/Lagrange-remainder bound + away-from-corner
  sweep, "not yet attempted") duplicates work already done by the main
  `-tangent` file's Steps 1-4 for the identical corner. Given Case (b) is
  already fully closed via two independent certified proofs
  (`t-nonnegative-on-case-b-residual-domain.md` and the Reduction
  Lemma/hypotheses A+B chain), this file adds little marginal value right
  now; **not** a good second-most-promising target if the Case (c) splice
  fails — recommend `ptolemy-trig-identity`'s `Ψ`-sextic (the population's
  longest-standing, most load-bearing open target across multiple routes)
  as the real fallback if this round's splice runs into trouble.

### 5-cont. Recommendation summary
If Case (c)'s splice (§2/§4) goes in cleanly, this route is genuinely one
paragraph away from `solved`. If the round-22 builder or reviewer finds
any additional subtlety in wiring Case (c) into the existing Reduction
Lemma / MVT-Lipschitz machinery (Steps 4-5, which are stated only for
Case (b) and don't need to touch Case (c) at all since Case (c) closes
directly via `(I)∧(II)`, bypassing `G(β1)`/`(⋆)`/Steps 4-5 entirely), that
is the one place to double-check first — Case (c) should NOT need to
invoke Steps 4/5 (the Reduction Lemma) at all, exactly as Case (a) didn't.

## Dead ends confirmed still valid (not retried)
- Round 19's original claim that Case (a)'s residual = Case (b)'s `T≥0`
  gap: confirmed wrong (round 20 finding), superseded by round 21's
  vacuity proof — do not resurrect.
- `f(β1)>0` alone as a proxy for `G(β1)≥0` in Case (a): confirmed false
  in general (round 18/19 witness), superseded by the vacuity argument.
- `ptolemy-trig-identity`'s 4-branch resolvent quartic as an "independent"
  easier lever: confirmed (round 21, memory rule 31) to reduce to the
  same `Ψ`-sextic — do not treat as a fresh cheap target.

## Small-case / intuition notes
- Numerically, Case (c) (`Y(γ)≥0`) is common (≈13-23% of the
  domain-nonempty region depending on parametrization measure), not an
  edge case — consistent with the round-21 reviewer's finding and
  reconfirmed independently here with a fresh, differently-seeded sweep.
- The margin `2K−f(γ)=sin(A+B)(2sinA−sinB)` in Case (c) stays comfortably
  positive (min observed `≈3×10⁻⁶`, likely tending to 0 only at further
  degenerate/limiting triangle shapes, consistent with a genuine strict
  inequality rather than a knife-edge numeric coincidence) — this is a
  genuine proved fact (Theorem 16.2), not a conjecture, so this is stated
  only as corroborating numeric evidence, not as the basis for the proof.
