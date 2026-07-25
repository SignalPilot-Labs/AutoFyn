# Round 14 proof-reviewer report — imo-2026-02

All three built approaches independently rebuilt from scratch (own fresh
sympy/mpmath sessions, not reusing any builder's displayed intermediate
polynomials). No overclaiming found in any of the three. Verdict for every
approach: **CHANGES REQUESTED** (Status: `partial`), no APPROVE this round.

## 1. `coordinate-bash-resultant-boundary`

**Claim checked:** corrected parity-basis element `B₆`, and infeasibility of
the smallest natural 3-term linear ansatz for `-q₁` using `B₁,B₄,B₆`.

**Independent verification.** Rebuilt all six `(0,0)`-graded products
`B₁,…,B₆` from the raw definitions of `G₀, E_num, Num` (own `sympy` session:
`sympy.reduced` modulo `⟨c²+s²-1,d²+t²-1⟩`, then the averaging parity
projector `f₀₀=1/4(f(c,s,d,t)+f(-c,s,d,t)+f(c,s,-d,t)+f(-c,s,-d,t))`,
rewritten in `σ=s²,τ=t²`). Result: `B₁`–`B₅` match the builder/explorer's
displayed formulas exactly (zero residual). `B₆` — the file explicitly
disputes the round-14 explorer's claimed `2σ²(σ-1)(τ-1)(2τ-1)(2τ+1)` — my
own from-scratch computation confirms the builder's **correction**,
`B₆ = 2σ²(σ-1)(τ-1)(4τ-1)`, exactly (zero residual against the raw
definition `sd·(-Num)`).

Also independently re-ran the smallest exact linear ansatz
`-q₁ = Σ_{i∈{1,4,6}} λ_i(σ,τ)·B_i` with degree-matched monomial multipliers
(own `sympy.linsolve` on the 12-monomial coefficient system): confirmed
**empty solution set**, matching the builder's honest negative finding.

The claimed structural finding about raw Gröbner-ideal-membership being
"structurally vacuous" for zero-constant-term targets against this
generator set is correct and elementary (the basis `{s²,d²-1,st,t²,c+1}`
trivially kills `q₁,r₀` since every monomial of `q₁,r₀` has a factor of `s²`
or `t²` — this is a sound observation, not re-derived independently in full
but the underlying arithmetic fact is immediate).

**Verdict:** No error found. The corrected `B₆` and the infeasibility result
are genuine, verified progress; the central `-q₁,-r₀` Positivstellensatz
certificate is honestly reported as still not found. **CHANGES REQUESTED.**
Certified `lemmas/parity-basis-b1-b6-corrected.md`.

## 2. `coordinate-bash-resultant-boundary-pointwise-tangent`

**Claims checked:** (a) `D₂(π/3,π/3) ≤ -0.8 < 0` via a self-contained
rational Taylor+Archimedes bound; (b) `(π/3,π/3)` is a strict local minimum
of `Tgt` via a tangent-cone directional-derivative argument.

**Independent verification of (a).** Rebuilt `D₂(A,B) = ∂RHS/∂B` from the
*raw* definitions (`K_c, P, Q, β₀=(π-A)/3`, own fresh 50-digit `mpmath`
session — not from the file's simplified closed form) and evaluated at
`A=B=π/3`: got `-0.83643057088879836412724821684306…`, matching (to 50
digits) both the file's simplified closed form `(√3/2)(c-s)-(√3/4)sc-(5/4)c²`
(`c=cos(5π/18), s=sin(5π/18)`) and its claimed tight `mpmath.iv` enclosure.
Independently confirmed the rational-bound arithmetic (recomputing the
term-by-term box-corner sum from the file's own stated Taylor interval
endpoints) gives `≈-0.8218`, comfortably `< -0.8`, consistent with (and
looser than) the exact value. This is a genuinely rigorous, hand-checkable
proof (Archimedes' `π` bound + Taylor-with-Lagrange-remainder, all exact
`Fraction` arithmetic, no floating point) — the strongest-rigor result of
the round.

**Independent verification of (b).** Rebuilt `Tgt(A,B) = 4(1+cosB)²X₀D₂² -
T₁²` entirely from the raw closed forms (`X₀, D₂, T₁` via the file's own
formulas, not copied output) and computed the gradient at the corner via
central finite differences (own script, `h=10⁻⁸`, `mpmath`, 40-digit
precision): `g_A ≈ -4.280960123589447`, `g_B ≈ -1.557257079971212` — matching
the file's `mpmath.iv` interval enclosures to 12+ digits, essentially
impossible to match this precisely by coincidence, confirming the analytic
derivation is correct. Also confirmed `Tgt(π/3,π/3) ≈ 1.574136`, matching
`(9/4)·D₂(π/3,π/3)² ≈ 1.574137` (consistent with the claimed `T₁'=0` at the
corner). Verified the tangent-cone argument's arithmetic: with tangent
directions `(-1,t)`, `t∈[-1/4,1/2]` (matching the independently-checked exact
tangent slopes `-1/2, 1/4` of the two boundary curves), the directional
derivative `-g_A+t·g_B` is affine and strictly decreasing in `t` (since
`g_B<0`), with minimum at `t=1/2`: `-g_A+g_B/2 ≈ 3.502 > 0`. This confirms
the strict-local-minimum conclusion is arithmetically sound.

One honestly-disclosed caveat (correctly flagged by the builder, not hidden):
the gradient values feeding the local-min argument rest on `mpmath.iv`
directed-rounding interval arithmetic rather than a fully self-contained hand
derivation like (a)'s — a legitimate, standard rigorous technique, one tier
below (a)'s fully hand-checkable proof, honestly labeled as such.

**Global minimality** over the whole 2-variable domain remains explicitly
open (numeric-only, `2M`-sample domain-correct sweep, no counterexample) —
correctly not claimed as proved.

**Verdict:** No error found; both sub-claims verified independently and
match to high precision. Genuine, rigorous progress; global minimum still
open. **CHANGES REQUESTED.** Certified `lemmas/d2-corner-value-strictly-
negative.md`.

## 3. `coordinate-bash-resultant-boundary-pointwise-sos`

**Claim checked (the round's most decisive):** the exact rational
counterexample `u=1/4` at a rationalized witness `B` (`cosB=808976/2721665`,
`sinB=2598657/2721665`), showing `n₁>0, n₂>0, Num<0` simultaneously, proving
the 2-generator ansatz for `Num≥0` unconditionally infeasible and resolving
a genuine round-13-vs-round-14 SDP contradiction.

**Independent verification.** Rebuilt `Num, n₁, n₂` *completely from
scratch* — not from the file's displayed polynomials — starting from the raw
trigonometric definitions: `X₀ := sinB·cosA/(2sin(A+B))`,
`RHS := (1+cosB)cosβ₀ - sinβ₀·G(β₀)` with `β₀=π/3-A/3`, `K_c,P,Q` as defined
in the file, and the Weierstrass substitution `u=tan(A/6)` (`x=cos(A/3)=
(1-u²)/(1+u²)`, `y=sin(A/3)=2u/(1+u²)`, `cosA=4x³-3x`, `sinA=3y-4y³`,
`cosβ₀ = (1/2)x+(√3/2)y`, `sinβ₀ = (√3/2)x-(1/2)y`). Cleared denominators via
`sympy.together`/`fraction` — the denominator factored exactly as
`-16(u²+1)^{14}h` with the same `h` as the file (independent confirmation of
Theorem 1's structure). Substituting the exact witness rationals and
`u=1/4`:

```
Num(1/4,·)  ≈ -0.0008596575524743493   (file: ≈-0.00086)   ✓ matches
n₁(1/4,·)   ≈  1.2685616043314354      (file: ≈1.2686)     ✓ matches
n₂(1/4,·)   ≈  0.03232250009949713     (file: ≈0.0323)     ✓ matches
```

both `n₁`'s and `n₂`'s denominators independently confirmed positive at this
point (consistent with Theorem 1's unconditional `sin(A+B)>0`-based
positivity). Also independently checked `n₄(1/4,·) = w³cosB - u(3-u²)`
(`w=√(1+u²)`) `≈ -0.4088 < 0`, confirming this witness lies outside the
`n₄≥0` sub-domain, as claimed. Every sign matches the file's claim exactly,
and my own values agree with the file's to the stated precision — this is
independent confirmation from first principles, not a re-run of the
builder's own code, and it fully corroborates the round's headline claim.

The logical argument (SOS ⟹ pointwise nonnegative on ℝ ⟹ `Num(1/4)≥0` given
`n₁(1/4),n₂(1/4)>0`, contradicting `Num(1/4)<0`) is elementary and correct.

**Verdict:** This is a genuine, fully rigorous, independently-reproduced
decisive negative result. It correctly resolves the cross-round contradiction
in round 13's favor and upgrades a numeric finding to an unconditional
theorem. The central gap (`Num≥0` on the true `n₄`-including domain) remains
open, honestly disclosed. **CHANGES REQUESTED.** Certified
`lemmas/n1n2-minimal-ansatz-unconditionally-infeasible.md`.

## Summary

- No regressions, no overclaiming, no RETHINK-worthy errors found in any of
  the three approaches this round.
- Three new lemmas certified: `parity-basis-b1-b6-corrected.md`,
  `d2-corner-value-strictly-negative.md`,
  `n1n2-minimal-ansatz-unconditionally-infeasible.md`.
- `current.md` updated: Status remains `partial`, round-14 section added
  above round 13's, with the per-approach findings summarized.
- `record_outcome` called for all three slugs (`partial`, `advanced`,
  `advanced` respectively).
- The population's shared branch-selection/Positivstellensatz core continues
  to narrow along three related-but-distinct precise sub-targets (see each
  approach's own "Open gaps"/"Net assessment" — `coordinate-bash-resultant-
  boundary`'s `-q₁,-r₀` certificate; `-pointwise-tangent`'s global
  minimality of `Tgt`; `-pointwise-sos`'s `Num≥0` on the `n₄`-extended
  domain).
