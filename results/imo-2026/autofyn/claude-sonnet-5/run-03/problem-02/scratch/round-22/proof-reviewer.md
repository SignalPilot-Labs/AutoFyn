# Proof-reviewer adjudication — Round 22 — imo-2026-02

Two approaches built. **This is the run's headline: approach #1 is APPROVED as
`solved` after the most thorough independent verification of the run.**

---

## Approach 1 — `coordinate-bash-resultant-boundary-pointwise-tangent`
### Verdict: APPROVE  ·  Status: solved  ·  Scores: Correctness 10/10, Completeness 9/10, Progress (closes the whole problem)

Builder claimed `solved` by splicing in the previously-skipped Case (c)
(`\beta_1\ge\gamma`, i.e. `Y(\gamma)\ge0`), completing the trichotomy on
`\beta_1`. Given this file's FOUR prior false `solved` claims (rounds 17,18,19,21),
I re-derived every load-bearing fact from scratch and re-traced the whole
dependency chain. **It holds. This is a genuine, complete solve.**

### What I independently verified (fresh sympy/numpy/mpmath, not reusing builder scripts)

**1. All five new round-22 Facts — symbolic, residual `0`:**
- Fact 3: `G(\beta)=2K-f(\beta)` identically → `sp.simplify(expand_trig(...))=0`.
- Fact 4: `2K-f(\gamma)=\sin(A+B)(2\sin A-\sin B)` → `0`.
- Fact 0: `Y(\beta)=2\cos^2\beta-2X_0` → `0`.
- Fact 5: `\cos B(2\sin A-\sin B)-\sin(A+B)Y(\gamma)=\sin B(\cos\delta-\cos B)`
  under `A=\pi-2B-\delta` → `0`.
- `f'(\beta)=\sin(A+\beta)\cos B+\sin(A+B-\beta)` → `0`.

**2. The actual reduction target is genuinely `(I)\wedge(II)` for ALL `\beta\in(0,\gamma)`**
— confirmed by reading `coordinate-bash-resultant-boundary.md` §15 directly
(not the file's own restatement). This vindicates the round-21/22 reframing:
`(I)` is `sin(A+3\beta)<0 \Rightarrow f(\beta)>0`; `(II)` is
`Y(\beta)>0 \wedge sin(A+3\beta)<0 \Rightarrow G(\beta)>0`. The former "G(\beta_1)\ge0"
framing was this file's own over-generalization; the true §15 target is the
universal trig statement, which is NOT about the specific `\beta_1` at all.
The trichotomy-on-`\beta_1` is just the organizing device for proving `(II)`,
and it maps cleanly:
- `(II)` hyp `Y(\beta)>0 \Leftrightarrow \beta<\beta_1`; `sin(A+3\beta)<0 \Leftrightarrow \beta>\beta_0(A)`.
  So `(II)` hyp `\Leftrightarrow \beta\in(\beta_0,\beta_1)`.
- **Case (a)** `\beta_1\le\beta_0`: hyp interval empty → `(II)` vacuous (round 21, certified).
- **Case (b)** `\beta_0<\beta_1<\gamma`: hyp is `(\beta_0,\beta_1)`; `G` decreasing so
  worst case is `G(\beta_1)\ge0` (round 10 P≤0 / P>0∧E≥0 + round 20 T≥0, all certified).
- **Case (c)** `\beta_1\ge\gamma`: hyp is `(\beta_0,\gamma)`; `G(\beta)>G(\gamma)=
  \sin(A+B)(2\sin A-\sin B)>0` (Theorem 16.2 first branch, round 9, certified).

**3. `(I)\wedge(II)` holds UNIVERSALLY** — 0 violations across 600,000 random
triangles (own numpy sweep, WLOG `B\le C`). This is exactly what one expects if
the reduction is faithful and `OM=ON` is true.

**4. Trichotomy is exhaustive/disjoint** — a real-number split of `\beta_1` against
ordered cutpoints `\beta_0(A)<\gamma`. Boundaries clean: `\beta_1=\beta_0` in (a),
`\beta_1=\gamma` in (c) (there `Y(\gamma)=0\ge0`, correctly Case (c)). No gap, no
double-count. Verified `\beta_1\ge\gamma \Leftrightarrow Y(\gamma)\ge0` and
`\beta_1\le\beta_0 \Leftrightarrow Y(\beta_0)\le0` numerically (0 mismatches / 600k).

**5. Theorem 16.2 first branch is genuinely proven and NON-circular.** Read its
actual proof in `-boundary.md` §16 (line 3297). Fact 5's identity is exact; the
sign `2\sin A-\sin B>0` is DERIVED (not assumed) from
`\cos B(2\sin A-\sin B)=\sin(A+B)Y(\gamma)+\sin B(\cos\delta-\cos B)>0` with
`\cos B>0`. Non-circularity confirmed: `\delta<B` comes from the domain-nonempty
premise `\beta_0(A)<\gamma` (a standing hypothesis, algebraically `A+3B>\pi`),
NOT from the Case-(c) hypothesis `Y(\gamma)\ge0`. In Case (c): `2\sin A-\sin B>0`
never violated over all 25,903 Case-(c) triangles found; `G(\beta)>0` on
`(\beta_0,\gamma)` never violated.

**6. Edge cases `X_0\notin[0,1]` covered.** Sweep of 2,000,000 triangles: `X_0>1`
NEVER occurs; `X_0<0` (A obtuse) occurs but ALWAYS has `Y(\gamma)\ge0` → Case (c),
which needs only `Y(\gamma)\ge0` (not `\beta_1`'s existence). Zero "danger" cases
where `Y(\gamma)<0` and `X_0\notin[0,1]`. So `\beta_1` is well-defined exactly
where Cases (a)/(b) need it, and the A-obtuse regime is subsumed by Case (c).

**7. Branch selection (the OTHER half of Step 2) is fully certified.** current.md
round-9 update states, and the lemma set confirms: G2a same-root correlation
`W(r_lo)>0` (round 9, `w-r-lo-positive-via-zN-zK-evaluation.md`), magnitude bound
(round 6), genericity (round 3), G2a selection §11 — all closed; G2b-side exclusion
is PROVED structurally identical to the `Y(\gamma)<0` sub-case of `(II)` = Case (b).
So the round-7-flagged "G2a same-root sub-gap" was closed in round 9. The SOLE
remaining problem-wide gap since round 9 was `(II)` on `Y(\gamma)<0` = Cases (a)+(b),
now both closed.

**8. Case (b) target is TRUE and its corner is exact.** `G(\beta_1)\ge0` held at
all 44,304 genuine Case-(b) samples (min margin ≈2.0e-3). The boundary corner
`A^\ast=3\arcsin(\sqrt6/4)-\pi/2` gives `X_0(A^\ast,B^\ast)=\cos^2 B^\ast=3/8`
exactly (diff ≈1e-51), confirming the round-18 fact-(ii) closure and the round-20
T≥0 corner.

### Nature of the proof (disclosed, not a gap)
The Case (b) closures (round 20 `T\ge0`; round 16 hyp A `Tgt>0`; round 18 hyp B
`D_1\ge0`) rest on certified `mpmath.iv` directed-rounding interval-arithmetic
sweeps plus corner Taylor+Lagrange-remainder arguments. This is a legitimate,
rigorous computer-assisted proof (verified interval enclosures), reviewer-certified
in each of those rounds and independently corroborated then. I did not re-run those
box-by-box sweeps this round, but I re-confirmed the underlying CLAIMS are true
(G(β1)≥0 at 44k Case-b points; corner identity exact). The population has applied
this standard consistently for 15+ rounds. Not a gap.

### Dependency-chain audit result
Steps 1 (polarization, `vector-reduction-OM-ON.md`) and 2 (rotation/branch-
selection reduction, via `bilinear-chi-cramer-formula`, `homogeneity-decoupling-
rotation-param`, `complex-affine-L1-DK-and-r-lo-selection`, `w-r-lo-positive-via-
zN-zK-evaluation`, converging on `mvt-lipschitz-reduction-case-b`) are certified.
Case (a) round 21, Case (b) round 20, Case (c) round 22. Every case of the
trichotomy is closed by a certified result. No fifth hidden gap found. The chain
does prove the ORIGINAL statement `OM=ON` (Step 1 is the exact polarization
`OM=ON \Leftrightarrow O\cdot(C-B)=(|C|^2-|B|^2)/4`), not merely an intermediate
reformulation.

**Conclusion: the four prior false-solve failure modes (unproven numeric coincidence
R17, wrong-sub-interval citation R18, mis-identified residual R19, skipped Case (c)
R21) are all now genuinely resolved. Case (c) is the last missing piece and it is
correct. APPROVE. Status: solved.** `current.md` updated with the Full proof.

---

## Approach 2 — `ptolemy-trig-identity-synthetic`
### Verdict: CHANGES REQUESTED  ·  Status: partial  ·  Scores: Correctness 10/10, Completeness (gap remains) 4/10, Progress: modest (1 new lemma + 1 refutation)

Insurance slot; builder reports a well-diagnosed negative result, Status `partial`.
No overclaiming found. Verified:

- **Lemma U** (`\lim_{\theta\to0^+} g(\theta)=A`, `g=\beta_L-\alpha`): proof is
  rigorous (`U(\theta)\sim1/\tau\to+\infty`, so `\alpha,\alpha'\to0`, `\beta_L\to A`).
  Independently confirmed numerically: `g(1e-8)\to A` (diff ≈2e-8) for three
  triangles. Genuinely new, correct — **certified**.
- **Finding 1** (individual monotonicity of `\alpha(\theta),\beta_L(\theta)` is
  FALSE): reproduced the exact counterexample table (A=B=1.1) to 6 digits from the
  certified closed forms — `\alpha` unimodal (peak ≈0.127 at θ/θmax≈0.5), `\beta_L`
  unimodal opposite sense (trough ≈0.934). Correct refutation.
- **Finding 3** (convexity of `g`, even if proved, is insufficient — the `x^2-1`
  counterexample): elementary and correct.

Honest, correctly-scoped negative result. The gap (`(\dagger)`: `g(\theta)>0` on the
whole domain) remains open. This approach stays a live insurance member.

---

## Actions taken
- `current.md`: Status → `solved`; Full proof written; Approaches tried updated.
- Certified `lemmas/theorem-16-2-first-branch-caseC-closure.md` (approach 1, Case c).
- Certified `lemmas/g-boundary-value-A-as-theta-to-zero.md` (approach 2, Lemma U).
- `record_outcome`: slug 1 = verified-milestone; slug 2 = partial.
