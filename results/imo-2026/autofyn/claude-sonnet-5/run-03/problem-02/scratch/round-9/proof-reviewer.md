# Round 9 proof review — imo-2026-02

Two approaches built this round. Both independently rebuilt from scratch
(fresh sympy/numpy sessions, own vector definitions, not copying builder
code or previous displayed formulas).

## 1. `coordinate-bash-resultant-boundary` — CHANGES REQUESTED (Status: partial)

**Claim**: Theorem 16.1 fully closes claim (I) `f(β)>0` unconditionally;
Theorem 16.2 closes claim (II) `2K-f(β)>0` on the `Y(γ)≥0` sub-case only;
`Y(γ)<0` sub-case of (II) left open.

**Independent rebuild (all confirmed exactly, zero symbolic residual)**:
- `f'(β) = sin(A+β)cosB + sin(A+B-β)` — re-derived from `f=K+Psinβ+Qcosβ`
  with the file's `P,Q,K` definitions. Confirmed.
- The unconditional sign argument (`β∈(0,B)`, `B<π/2` since `2B≤B+C<π`,
  `A+β∈(0,π)`, `A+B-β∈(0,π)`) — checked by hand, sound, no gap, applies to
  every triangle (WLOG `B≤C`).
- `f(β0) = 2sinβ0·G(β0,s)`, `G=C1 cos s - C2 sin s`, with the exact
  `C1,C2` closed forms — re-derived via the `A=π-3β0`, `B=β0+s`
  substitution. Confirmed exactly.
- Step (a): `C1 = sin(2β0)(3/2+2cos2β0) > 0` — confirmed.
- Step (b): found a **cosmetic transcription error** — the file displays
  `C2 = 2x²+5/2x+3/2` but the correct polynomial (matching the file's own
  correctly-used factored form `2(x+1)(x+1/4)`) has constant term `1/2`,
  not `3/2`. This is a pure display typo; the factored form actually used
  downstream is correct, so the substantive proof is unaffected. Flagged
  in the certified lemma.
- Both sub-cases of the `C2` sign split, including the exact evaluation
  `G(β0,β0/2) = cosβ0·sin(3β0/2)(4cosβ0-1)` via sum-to-product — confirmed
  exactly, and the positivity of each factor checked by hand.
- Theorem 16.2 (Case (a), `Y(γ)≥0`): `f(γ)=(2sinA+sinB)sin(A+B)`, the key
  identity `cosB(2sinA-sinB) - N = sinB(cosδ-cosB)`, and `N=sin(A+B)Y(γ)`
  — all confirmed exactly via independent sympy sessions.

**Verdict**: This is real, gap-free, independently-verified progress: claim
(I) is now a fully closed theorem for every triangle (no case split beyond
the standing WLOG), and claim (II) is closed on a large, precisely-defined
sub-case. The `Y(γ)<0` sub-case is honestly and correctly left open — no
proof given or claimed for it, matching the file's own disclosure. No
overclaiming found. **Status: partial** (real progress, not solved — the
file's own self-reported status is accurate). **CHANGES REQUESTED.**

Certified: `lemmas/claim-I-closed-and-claim-II-caseA-closed.md`.

## 2. `coordinate-bash-resultant-boundary-pointwise` — CHANGES REQUESTED (Status: partial)

**Claim**: fully closes `W(r_lo)>0` for both `Y>0` and `Y<0` cases via a
new `z_N/z_K` evaluation trick showing `W(r_lo)` is a perfect square in the
harder case — but this only resolves the `G2a`-branch side, NOT the
`G2b`-exclusion question, which remains the sole open gap.

**Independent rebuild (all confirmed exactly, zero symbolic residual)**:
- Re-derived `D_K(s2)`, `D_N(s2)` directly from the raw vector definitions
  (`A=(0,0),B=(a,0),C=(b,cc)`, `d(β)`, `L(s2)=C+s2R(β)(A-C)`, `N=C/2`) —
  matched the file's closed forms `D_K(1+u²)²=P_K+s2Q_K` and
  `D_N=(b²+cc²)/4·(1-2s2cosβ)` exactly.
- Independently re-derived `G_2a` itself from the raw `cross_eq`
  hypothesis-2 construction (own sympy session, `eq2 = cross_eq(L-B,K-B,
  L-N,C-N)`, divided by `t1²`, factored) — this reproduced `G_2a` as a
  factor with leading coefficient in `s2²` exactly matching the
  already-certified `A_2=2(1+u²)(cc(u²-1)-2bu)`. En route, confirmed that
  the `G_2a` polynomial as literally displayed in
  `coordinate-bash-resultant.md` §2 is missing all its `cc`-dependent
  terms — a stale cosmetic transcription bug in an old file, correctly
  flagged by this round's builder; the substantive `A_2,F_2` formulas
  used throughout the certified lemma chain are unaffected.
- Confirmed `G_2a(z_N)/Y = u(u²+1)/(u²-1)²` and `G_2a(z_K)/Y =
  (u²+1)³F_2/Q_K²` exactly (`sympy.simplify`/`factor`, zero residual) —
  these are the two key evaluation identities the whole argument rests on.
- Confirmed `D_K(z_N) = a·cosβ - b/(2cosβ)` and `D_N(z_K) =
  (b²+cc²)Y/(4Q_K)` exactly.
- The interior/exterior classification (via the standard quadratic-sign
  fact `G_2a(x)=A_2(x-r1)(x-r2)`, `A_2<0` certified) and the two-case
  straddle/monotonicity argument (Y>0: `D_N` decreasing + `z_N` interior
  gives `D_N(r_lo)>0`; `D_K` constant sign on `[r_lo,r_hi]` via `z_K`
  exterior, equal to `D_K(z_N)`, sign(Y)=+; Y<0: both `D_K(r_lo)` and
  `D_N(r_lo)` independently reduce to `-sign(Q_K)`, so the product is a
  perfect square) — checked by hand, logically sound, no gap.
- **Additional independent numeric cross-check** (own Python/numpy, not
  reusing any symbolic derivation): 30,000 random triangles, `β`
  restricted to the TRUE valid domain `(0,min(∠B,∠C))` computed from the
  actual vertices, `G_2a`'s roots found via the quadratic formula,
  `D_K(r_lo)D_N(r_lo)` evaluated directly from the raw vector definitions
  — 29,999/30,000 strictly positive, the one "failure" being
  `W≈4×10⁻¹⁰`, a floating-point near-zero artifact at a measure-zero
  boundary, not a genuine counterexample. (Note: an earlier naive sweep
  using `β` uniform over `(0,π/2)`, i.e. NOT restricted to the correct
  domain, did produce an apparent counterexample — this vanished once the
  domain restriction was correctly applied, a useful methodological
  caution recorded in memory.)

**Scope check**: independently confirmed the file's own honest
self-assessment — Lemma P1's logical structure (satisfying conditions
(2)-(4) on `G_2a`'s own roots is a biconditional for a *given* candidate
`s2`) does not by itself rule out a `G_2b` root also satisfying (2)-(4).
So this round's result closes the `G2a`-side same-root correlation fully,
but does NOT touch `G2b` exclusion, which remains the population's sole
shared open gap — exactly as the builder self-corrected and disclosed. No
overclaiming found.

**Verdict**: This is a complete, gap-free, independently-verified closure
of the approach's own designated remaining target (`W(r_lo)>0`, both
cases) via a genuinely new and elegant technique. **Status: partial**
(the approach's own algebraic content is now fully closed, but the whole
problem is not solved since G2b exclusion remains open — file's own
Status is accurate). **CHANGES REQUESTED.**

Certified: `lemmas/w-r-lo-positive-via-zN-zK-evaluation.md`.

## current.md

Updated: added a "Round 9 (this round)" section to `## Approaches tried`
(preserving all prior rounds), and updated the `## Full proof` /
current-best summary section to reflect that the `G2a`-side branch
selection is now FULLY closed (both the same-root correlation and claim
(I)/(II)-Case-(a)), leaving the `Y(γ)<0` sub-case (equivalently `G2b`
exclusion) as the SOLE remaining gap for the whole population. `## Status`
remains `partial` — no approach reached `solved` this round.

## Lemmas certified this round

- `results/imo-2026-02/lemmas/claim-I-closed-and-claim-II-caseA-closed.md`
  (new) — `coordinate-bash-resultant-boundary`'s Theorems A (claim (I),
  unconditional), B (endpoint lemma `f(β0)>0`), C (claim (II), sub-case
  `Y(γ)≥0`). All independently re-derived and verified exact.
- `results/imo-2026-02/lemmas/w-r-lo-positive-via-zN-zK-evaluation.md`
  (new) — `coordinate-bash-resultant-boundary-pointwise`'s `W(r_lo)>0`
  theorem, both cases, via the `z_N/z_K` evaluation method. Independently
  re-derived and verified exact, plus a fresh 30,000-sample numeric
  cross-check.

## Overall round-9 assessment

Both approaches close their own previously-open sub-targets with genuine,
independently-verified rigor — the population's branch-selection gap is
now sharper than ever: the `G2a`-side is FULLY closed (round 9), and the
ONLY remaining obstruction, shared by every live framing (coordinate,
fixed-point/bilinear, inversion), is the `G2b`-side exclusion
(equivalently, the `Y(γ)<0` sub-case of claim (II), equivalently the
`(Y,B2,Z)` three-way sign classification). Status of the whole problem:
`partial`. Neither approach is `solved`; neither is `unsolved` (both are
correct, real, gap-closing progress) — both verdicts are **CHANGES
REQUESTED**.

Report paths: `/home/agentuser/repo/results/imo-2026-02/current.md`,
`/home/agentuser/repo/results/imo-2026-02/lemmas/claim-I-closed-and-claim-II-caseA-closed.md`,
`/home/agentuser/repo/results/imo-2026-02/lemmas/w-r-lo-positive-via-zN-zK-evaluation.md`.
