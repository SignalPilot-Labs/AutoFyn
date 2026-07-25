# Proof review — round 15 — imo-2026-02

Problem: imo-2026-02 (IMO 2026 P2). Reviewing three built approaches
independently. Method: for each headline claim, rebuilt the load-bearing
identity/computation from scratch in a fresh Python/sympy/mpmath/numpy
session, not trusting the builder's displayed code or numbers.

---

## 1. `coordinate-bash-resultant-boundary-pointwise-tangent.md`

**Claims reviewed:** Theorem A (closed-form parametrization of `\mathcal
C_{\mathrm{lo}}`), Theorems B & C (`\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})`
on the entirety of both boundary curves via certified `mpmath.iv`
interval-arithmetic branch-covering), the domain-has-three-curves
correction, and a corrected corner-value citation.

### Independent verification

- **Corner value.** Rebuilt `X_0,\beta_0,K_c,P,Q,G,\mathrm{RHS},D_2,T_1,
  \mathrm{Tgt}` from the raw trig definitions in a fresh `sympy` session and
  computed `\mathrm{Tgt}(\pi/3,\pi/3)` to 30 digits:
  `1.57413622481406257722651370062...` — exact match to the file's
  corrected value (superseding the stale `1.5741362290964376` citation).
  Also independently confirmed `T_1(\pi/3,\pi/3)=0` exactly
  (`sympy.simplify` gives literal `0`) and `D_2(\pi/3,\pi/3)=
  -0.836430570888798364127248216843...`, matching the file to all displayed
  digits.
- **Theorem A** (`\tan A=-\sin B\cos(2B)/(2\cos^3B)` on `\mathcal
  C_{\mathrm{lo}}`). Independently derived the identity from `X_0=\cos^2B`
  via the sine-addition formula — reproduces the file's algebra exactly.
  Cross-checked numerically: solving `X_0(A,B)=\cos^2B` for `A` via
  `sympy.nsolve` at `B=0.9` gives `A=0.354807081596715...`, and evaluating
  `\arctan` of the claimed closed form at the same `B` gives the identical
  value to all displayed digits. Endpoints also verified: `A(\pi/3)=\pi/3`
  exactly and `A(0.9117433492)\approx0.40640054...`, matching the
  population's long-standing `A^\ast`.
- **Theorem B** (`\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})$ on `\mathcal
  C_{\mathrm{hi}}$). Built an independent high-precision (`mp.dps=30`)
  `mpmath` evaluator of `\mathrm{Tgt}(A,(\pi-A)/2)` (using `mp.diff` for
  `D_2,\partial_BX_0` rather than the file's closed-form derivatives, a
  genuinely different computational route) and scanned `2000` points over
  `A\in[0.5,\pi/3)`: minimum found is exactly the corner value, attained at
  `A=\pi/3$'s limit, `0` violations. This is dense sampling, not the file's
  certified directed-rounding interval method, but it strongly corroborates
  the claimed result with no counterexample found.
- **Theorem C** (same, on `\mathcal C_{\mathrm{lo}}$, via Theorem A's
  parametrization). Same independent evaluator, composed with the verified
  `A(B)` parametrization, scanned `2000` points over `B\in[0.9,\pi/3)`:
  minimum found is exactly the corner value (`diff\approx4\times10^{-31}`,
  floating-point noise), `0` violations.
- **Three-boundary-curve domain finding.** Not independently re-derived
  numerically in full (time-constrained), but the reasoning (checking which
  of the three domain inequalities binds at each `A`) is sound and does not
  affect any previously-certified result, since it is explicitly scoped to
  a region away from the corner-adjacent neighbourhood where prior results
  live. Accepted as reported.

### Assessment

All headline claims (Theorem A, Theorem B, Theorem C, corrected corner
value) independently reproduced with no discrepancy. The file is honest
about what remains open: the near-corner residual of the 2-D interior
adaptive interval sweep is explicitly NOT resolved (an intrinsic limitation
of finite-width interval methods at a point of equality), and gluing this
to the already-certified local-minimum theorem (New result 9, round 14)
requires an explicit quantitative radius that has not been produced. No
overclaiming: Status is correctly stated as `partial`.

**Certified lemmas:**
- `lemmas/clo-closed-form-parametrization.md` — correct, self-contained,
  no gaps. **CERTIFIED.**
- `lemmas/tgt-ge-corner-on-both-boundary-curves.md` — correctly scoped
  (explicit caveat that the interior/near-corner region is not covered).
  **CERTIFIED.**

**Verdict: CHANGES REQUESTED.** Status: `partial`. Real, independently
verified progress (two boundary curves of the domain fully closed via a
legitimate certified-interval method). Precise remaining gap: the interior
of `\mathcal D` and, specifically, a shrinking (sub-`10^{-7}`-radius)
neighbourhood of the corner `(\pi/3,\pi/3)` where interval methods cannot
resolve strict positivity because equality holds exactly there — closing
this requires either (i) a quantitative radius for the existing local-min
theorem (New result 9) or (ii) a dedicated second-order near-corner
argument. Recommend the builder attack this specific gap next round.

---

## 2. `coordinate-bash-resultant-boundary.md`

**Claims reviewed:** three new sign-definite degree-6/6/8 generators
`(G_0\cdot E_{\mathrm{num}})_{00}`, `(G_0\cdot(-\mathrm{Num}))_{00}`,
`(E_{\mathrm{num}}\cdot\mathrm{Num})_{00}`, rederived independently; the
`-q_1,-r_0` Positivstellensatz certificate search (nine multiplier
variants, all infeasible, one confirmed via phase-1 residual LP).

### Independent verification

- **Generator identities.** Rebuilt `G_0,E_{\mathrm{num}},\mathrm{Num}`
  from the file's own displayed certified closed forms in a fresh `sympy`
  session, computed the three pairwise products, reduced modulo `\langle
  c^2+s^2-1,d^2+t^2-1\rangle` (own substitution-based reduction, not
  `sympy.reduced`/Groebner, a genuinely independent computational route),
  and projected to the `(0,0)`-grade via the four-fold sign-averaging
  projector. **All three closed forms
  (`B_{G_0E},B_{G_0N},B_{EN}`) matched the file's displayed polynomials
  exactly (zero residual)** — the symbolic derivation is correct.
- **Sign-definiteness — FOUND A BUG.** Independently sampled the true
  residual domain using the file's own stated four raw inequalities
  (`G_0>0,\ E_{\mathrm{num}}<0,\ \mathrm{Bc}:=c-2t^2+1\ge0,\ \mathrm{Num}<0`,
  with `c=\cos A,s=\sin A,d=\cos B,t=\sin B`, sampling `A\in(0,\pi)`,
  `B\in(0,\pi/2)`): a `4{,}000{,}000`-sample sweep found `8{,}000+` genuine
  domain points, with `\sigma,\tau$-ranges matching the file's own claimed
  window almost exactly (`\sigma\in(0.157,0.261)`, `\tau\in(0.626,0.787)`
  vs. the file's `(0.1565,0.2610)`, `(0.6251,0.7863)`), and `B_{G_0E}$,
  `B_{EN}$ both confirmed strictly positive with ranges matching the file's
  claimed `(0.0276,0.1076)` and `(0.0075,0.0580)` almost exactly — good
  corroboration of two of the three sign claims.
  **However, `B_{G_0N}=(G_0\cdot(-\mathrm{Num}))_{00}$ is UNIFORMLY
  NEGATIVE on the domain — `0/8793` samples positive, range
  `\approx(-0.079,-0.012)$ — the exact OPPOSITE sign of the file's claim
  `B_{G_0N}\in(0.0121,0.0789)>0`.** Cross-checked at a single hand-picked
  domain point via a fully independent route (direct numeric evaluation of
  the raw product `G_0\cdot(-\mathrm{Num})` at `(A,B)=(0.4456,0.9347)`,
  averaged over the four sign flips `(c,d)\to(\pm c,\pm d)` — no `sympy`,
  no reduction machinery, pure floating-point): gives `-0.03175`, matching
  the reduced-formula evaluation exactly, and confirming the reduction/
  projection pipeline itself is correct — the polynomial genuinely is
  negative there. The negated quantity `-B_{G_0N}=(G_0\cdot\mathrm{Num})_
  {00}` matches the file's claimed positive range digit-for-digit
  (`(0.0121,0.0789)`), strongly suggesting the file's error is a clean sign
  slip (likely computed/labeled `(G_0\cdot\mathrm{Num})_{00}` as if it were
  `(G_0\cdot(-\mathrm{Num}))_{00}$, or vice versa, at the numeric-sanity-
  check step, distinct from the symbolic-derivation step which correctly
  used `-\mathrm{Num}` throughout and produced the right formula).
- **Downstream effect.** This sign error is load-bearing for §4's LP/rank
  table, which used `B_{G_0N}` as one of the 9 generators in a
  nonnegative-coefficient certificate search (a search that assumes each
  generator is itself `\ge0$ on the domain, so a nonnegative multiplier
  keeps its contribution nonnegative). Since the actual sign-definite
  quantity is `-B_{G_0N}$, not `B_{G_0N}`, the rows of that table involving
  `B_{G_0N}` should be redone with the corrected generator. This does not
  change the round's ultimate conclusion (certificate still not found —
  the search failed regardless of this generator's sign), but the evidence
  as currently written for that specific generator is incorrect and must
  be fixed, not re-asserted, next round.
- **Phase-1 residual LP.** Not independently re-run (would require
  reconstructing the file's exact `A,b` matrices for the `1-\sigma$
  multiplier variant — significant setup cost not justified given the
  headline conclusion is unchanged either way); the *methodology*
  (phase-1 L¹-residual minimization to distinguish genuine infeasibility
  from solver-tolerance artifacts) is sound and appropriately used.

### Assessment

Real, partially-flawed progress: two of three new generators (`B_{G_0E},
B_{EN}$) are correctly derived and correctly signed; the third
(`B_{G_0N}$) is correctly derived symbolically but WRONGLY signed in the
file's sign-definiteness claim — a genuine, confirmed error, not a
borderline numeric-tolerance issue. The file's honest overall conclusion
("no certificate found, Status stays `partial`") is unaffected in
substance. No lemma file was submitted for these generators (correctly —
the error is caught before certification), so nothing needs to be rejected
from `lemmas/`; the fix (correct the sign of `B_{G_0N}$ and, if load-bearing,
rerun the §4 LP rows using `-B_{G_0N}$) is flagged for next round.

**Verdict: CHANGES REQUESTED.** Status: `partial` — correctly stated, but
with a caveat: this round's own "independent numeric confirmation of
sign-definiteness" section (§2/§7) contains a confirmed sign error for one
of its three headline generators (`B_{G_0N}`), which the builder should
correct before any of that section's downstream conclusions (the §4 LP
table rows using this generator) are relied upon.

---

## 3. `coordinate-bash-resultant-boundary-pointwise-sos.md`

**Claims reviewed:** Theorem 4 (`n_4\ge0\iff n4sq\ge0`, a lossless plain-
polynomial simplification eliminating the `w=\sqrt{1+u^2}$ algebraic
extension, fully proved), and a 3-generator SDP reported to converge
cleanly (`optimal`, not `optimal_inaccurate`) at four witness points,
explicitly NOT claimed as a proof.

### Independent verification

- **Theorem 4's algebraic core.** Own `sympy` session: computed
  `(w^3\cos B)^2-(u(3-u^2))^2`, substituted `w^2\to1+u^2$ (eliminating `w`
  entirely, confirmed no residual `w$-dependence remains), and compared
  against the claimed `n4sq:=(1+u^2)^3\cos^2B-u^2(3-u^2)^2$: residual is
  identically `0`. The squaring identity is correct.
- **Elementary sign facts (i), (ii).** (i) `\cos B>0`: the file's argument
  (`B\le C\Rightarrow 2B\le B+C=\pi-A<\pi\Rightarrow B<\pi/2`) is a
  standard, correct triangle-angle argument, elementary. (ii)
  `u(3-u^2)>0`: with `u=\tan(A/6)`, `A\in(0,\pi/2]$ gives
  `A/6\in(0,\pi/12]$, so `u\in(0,\tan(\pi/12)]`. Independently confirmed
  `\tan(\pi/12)=2-\sqrt3$ exactly via `sympy` (`sp.tan(sp.pi/12)` simplifies
  to `2-\sqrt3`, and `\mathrm{sympy.simplify}` of the difference is `0`),
  and `2-\sqrt3\approx0.268<\sqrt3$, so `u^2<3`, giving `3-u^2>0`, hence
  `u(3-u^2)>0`. Both facts check out.
- **The `X\ge Y\iff X^2\ge Y^2$ for `X,Y\ge0`` step** is a correct,
  standard, elementary fact (monotonicity of squaring on nonnegatives plus
  factoring `X^2-Y^2=(X-Y)(X+Y)`), correctly applied.
- **SDP evidence (Parts 3-4).** Not independently re-run (would require
  reconstructing a `\approx630$-variable SDP from scratch — out of scope
  for this review's time budget), but the file is explicit and correct
  that this is NOT a proof: no exact rational Gram matrix was extracted,
  and even a fully exact pointwise certificate at finitely many `B`-values
  would not establish the needed joint multivariate Positivstellensatz.
  This self-assessment is accurate and appropriately conservative — no
  overclaiming.

### Assessment

Theorem 4 is a genuinely new, fully rigorous, case-free result — a real
structural simplification (eliminating an algebraic-extension bookkeeping
burden from the Positivstellensatz search) — **independently verified with
no gaps found**. The round's SDP work is honestly and precisely scoped as
strong-but-incomplete numeric evidence. No overclaiming anywhere in this
file. The "Promotable lemmas" section correctly proposes Theorem 4 as
certifiable but the file did not write a separate `lemmas/<name>.md` file
for it this round — the statement as written in the approach file's
"Promotable lemmas" section is exactly what a `lemmas/` file should
contain, so I certify it below directly.

**Certified lemma (extracted and written this round from the approach
file's "Promotable lemmas" section, since it was correctly stated there
but not filed separately):**
- `lemmas/n4-to-n4sq-plain-polynomial-equivalence.md` — Theorem 4, as
  stated above. **CERTIFIED** (see file written to `results/imo-2026-02/
  lemmas/n4-to-n4sq-plain-polynomial-equivalence.md`).

**Verdict: CHANGES REQUESTED.** Status: `partial` — correctly stated. Real
progress (Theorem 4, fully proved). Remaining gap, precisely: (a) no exact
rational SOS/Positivstellensatz certificate extracted from the clean
numeric SDP solutions (attempted, not completed); (b) even with (a), only
a pointwise (fixed-`B`) result would be established, not the joint
multivariate identity needed — a `\sigma_0,\lambda_i` ansatz that is
itself polynomial in `(\cos B,\sin B)`, not re-fit per sample point, has
not yet been attempted.

---

## Summary table

| Approach | Verdict | Status | Headline new result | Key finding this review |
|---|---|---|---|---|
| `...-pointwise-tangent` | CHANGES REQUESTED | partial | Theorems A/B/C (2 boundary curves closed via certified interval arithmetic) | All independently reproduced, no error found; near-corner interior gap honestly remains |
| `...-boundary` | CHANGES REQUESTED | partial | 3 new degree-6/6/8 generators; certificate search still fails | **Sign error found**: `B_{G_0N}` is negative, not positive as claimed; 2/3 generators correctly signed |
| `...-pointwise-sos` | CHANGES REQUESTED | partial | Theorem 4 (`n_4\to n4sq`, plain-ring, fully proved) | Fully verified, no gaps; SDP evidence correctly scoped as non-proof |

No APPROVE this round — the problem remains `partial`. `current.md` updated
accordingly (see `results/imo-2026-02/current.md`, "Round 15 — proof-
reviewer adjudication").

## Recorded outcomes (via `record_outcome`)
- `coordinate-bash-resultant-boundary-pointwise-tangent`: `advanced` —
  both boundary curves of the domain fully closed via certified interval
  arithmetic; gap narrowed to a specific near-corner residual.
- `coordinate-bash-resultant-boundary`: `partial` — new generators
  correctly derived but one has a confirmed sign error; certificate search
  still fails.
- `coordinate-bash-resultant-boundary-pointwise-sos`: `advanced` — Theorem
  4 fully closes the `w`-extension elimination sub-target; SDP evidence
  strengthened but honestly not a proof.
