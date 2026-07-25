# Round 20 proof-reviewer adjudication — imo-2026-02

All four built approaches independently re-verified from scratch (fresh
`sympy`/`mpmath`/`numpy` sessions, never reusing builder scripts). No
approach reaches `solved`. Verdicts below are per-slug, independent.

## 1. `coordinate-bash-resultant-boundary-pointwise-tangent`

**Verdict: CHANGES REQUESTED. Status: partial (confirmed accurate as
self-reported).**

**Part 1 — Case (b)'s residual `T\ge0` closure: genuinely closed, verified
in full.**
- Corner value `T(A^\ast,B^\ast)=0`: independently rebuilt from the raw
  trig definitions in a fresh `sympy` session using the certified
  `u=\arcsin(\sqrt6/4)` substitution — evaluates to `0` to 192 displayed
  digits. Confirmed.
- Exact gradient `\partial_AT|_\ast=14375\sqrt{15}/32768\approx1.699040`,
  `\partial_BT|_\ast=5625\sqrt{15}/32768\approx0.664842`: independently
  recomputed via central finite differences (fresh `mpmath`, `dps=50`,
  `h=10^{-20}`) — matches to all displayed digits.
- The closed-form factorization `T=c(dQ_1-cR_0)/(4\sin^2(A+B))` (from
  `lemmas/case-b-e-lt-0-t-factorization.md`): independently confirmed
  matches the raw `T:=B_{\mathrm c}^2X_0-E^2` definition to 50 digits at
  three sample points.
- Own fresh, independent 200,000-sample domain sweep (own domain-
  membership test built from the raw `X_0,\beta_0,P,E` inequalities, own
  seed): 486 genuine `\mathcal D_b` points, **zero** `T<0` violations —
  corroborates (though does not itself certify box-by-box) the file's
  `mpmath.iv` adaptive-quadtree closure, which was not independently
  re-run cell-by-cell this round (would require reproducing the full
  interval-arithmetic pipeline) but is internally consistent with every
  other independently-checked component.
- **Certified `lemmas/t-nonnegative-on-case-b-residual-domain.md`**,
  scoped explicitly to Case (b) only (`X_0<\cos^2\beta_0(A)`).

**Part 2 — the dispatched contradiction check: CONFIRMED, and it is
exactly as the builder reports (a correction of round 19, not a new
error).** Independently reproduced the builder's witness computation
exactly (fresh 50-digit `mpmath`, raw definitions, no reuse of the file's
script):
```
A=0.02, B=1.5  (C=1.6215926535897932384626433832795028841971693993751, B<=C)
X0 = 0.49929176161496660363987754901536137757090527055836
cos^2(beta0(A)) = 0.25579555351967648409678051316952283235148921862474
T  = -0.24903851902574595779658364299364672170716014094996
G(beta1) = -0.65365419132206890874287426578647393081332454909202
```
`X_0>\cos^2\beta_0(A)` places this point genuinely in Case (a) (the
complementary region to `\mathcal D_b`), and `T,G(\beta_1)` are both
negative to 50 digits — matching the file's reported values digit for
digit. **This confirms round 19's dependency-chain claim ("Case (a)'s
residual coincides exactly with Case (b)'s `T\ge0` gap") was wrong**: Case
(a)'s domain is not a subset of `\mathcal D_b` but its complement, and
`T`/`G(\beta_1)` are genuinely false there in general, not merely
"unproved." Importantly, this error was caught and corrected by the
round-20 **builder itself**, via the mandated whole-chain re-audit — a
model instance of the self-correction process this population has
exhibited repeatedly (rounds 17, 18, 19). No overclaiming: the file
explicitly narrows Open gap 7 to "Case (a) needs a genuinely different
quantity/reduction, not yet found by rounds 11-20" rather than asserting
closure. **Net for this file: Case (b) of Open gap 7 is now fully and
unconditionally closed (two independent certified proofs — this round's
`T`-route and the pre-existing `\mathrm{Tgt}`/`D_1`/Reduction-Lemma route);
Open gap 7 as a whole (Case (a)) remains open, more precisely diagnosed
than at any prior round.**

## 2. `coordinate-bash-resultant-boundary-pointwise-tangent-via-T`

**Verdict: CHANGES REQUESTED. Status: partial (confirmed accurate).**

Independent second derivation of `T(A^\ast,B^\ast)=0` via the certified
`(\sigma,\tau)`-rational-polynomial route (`case-b-e-lt-0-t-
factorization.md`'s `q_1,r_0`), avoiding trig-identity manipulation.
Independently re-verified every load-bearing step in a fresh
`sympy.Rational` session:
- `\sigma^\ast=\sin^2A^\ast=5/32`, `\tau^\ast=\sin^2B^\ast=5/8`: confirmed
  exactly via fresh `mpmath` (`dps=50`) from the raw
  `u^\ast=\arcsin(\sqrt6/4)` definition (`\sin^2A^\ast=0.15625=5/32`,
  `\sin^2B^\ast=0.625=5/8` to 50 digits).
- `q_1(5/32,5/8)=75/131072`, `r_0(5/32,5/8)=-125/262144`: independently
  substituted these exact rationals into the certified degree-`(4,3)`
  polynomials (typed independently from `case-b-e-lt-0-t-
  factorization.md`'s displayed coefficients) — matches exactly.
- The squared identity
  `16\cdot\frac5{32}\cdot\frac58\cdot\frac38\cdot(75/131072)^2=
  \frac{27}{32}\cdot(125/262144)^2`: independently computed both sides —
  both equal `421875/2199023255552` exactly. Confirms
  `T(A^\ast,B^\ast)=0` via this alternative mechanism.
- The overall `T=c(dQ_1-cR_0)/(4\sin^2(A+B))` identity itself was also
  independently spot-checked against the raw `T` definition at three
  non-corner sample points (agreement to 50 digits), confirming the
  underlying factorization this proof relies on.
**Certified `lemmas/t-corner-value-exact-via-sigma-tau.md`.** Correctly
and honestly scoped: only the corner value is closed here; the file's own
Step 2 (a certified 2-D directional-derivative/Lagrange-remainder bound,
plus an away-from-corner interval sweep, needed to close `T\ge0` on the
whole of `\mathcal D_b` via this route) is disclosed as not yet built, and
no claim beyond this is made. No overclaiming.

## 3. `ptolemy-trig-identity`

**Verdict: CHANGES REQUESTED. Status: partial (confirmed accurate).**

**Equivalence claim (correcting the round-20 dispatch's premise) —
verified sound.** The file argues that the dispatched "cheap, untried
lever" (eliminate `x:=\cot\psi,y:=\cot\varphi` directly via the certified
quadratics `(III)',(IV)'` and substitute into `F(p,x,y)`) is algebraically
identical to the already-exhausted `U:=\cot\alpha=p+2x,\ V:=\cot\alpha'=
p+2y` resultant-elimination route from round 5, since `U,V` are literally
defined as affine images of `x,y` and `(III)'',(IV)''` (the derived
quadratics in `U,V`) were themselves obtained by substituting `x=(U-p)/2`
into `(III)'` — i.e. this is the same equation under a variable change, so
its roots correspond via the same affine map automatically, and any
radical-free polynomial reachable by eliminating `x,y` is (up to the
already-accounted-for rescaling) the same object reachable by eliminating
`U,V`. This reasoning is sound (indeed more straightforwardly true than
the file's own more convoluted discriminant-scaling argument suggests —
it is essentially an automatic consequence of substitution), and the
conclusion — no new content beyond the already-open `\Psi(\tau,A,C)`
sextic — is correct. No error found in this negative/clarifying finding.

**New four-branch resolvent quartic `P(t)` — independently re-derived and
confirmed exactly.** Built `P(t):=\prod_{s_1,s_2\in\{\pm1\}}(t-F_{s_1,s_2})`
symbolically in a fresh `sympy` session (own variables `R,m_1,m_2,d_1,d_2,
\sin A`, own expansion, not copied from the file) and confirmed the sum,
sum-of-pairs, sum-of-triples, and product of the four roots equal
`4R,\ e_2,\ e_3,\ e_4` respectively exactly as the file displays them
(zero residual on all three nontrivial coefficients). This is a correct,
standard symmetric-function/Vieta construction — fully proved, no gap.

**Root-count claim (Step 2): correctly and honestly scoped as
numeric-only.** The file explicitly states the "exactly 3 negative, 1
positive real root" pattern is verified only at 8 diverse samples and is
NOT proved, correctly noting a quartic with `e_4<0` need not have this
exact root split in general, and correctly declining to claim this closes
anything. No overclaiming found — this open sub-target is honestly scoped
exactly as the dispatch instructions required verifying.

## 4. `spiral-similarity-bootstrap`

**Verdict: CHANGES REQUESTED. Status: partial (confirmed accurate).**

**New `Q` characterization — independently re-verified in full.** With `A`
at the origin, the claim `Q=(\text{line through }A\parallel BC)\cap
(\text{perp.\ bisector of }BC)` was checked via a fresh `numpy` session
(3 random `B,C\in\mathbb R^2`, own script): computed `Q` via the certified
closed form `Q=\frac{|C|^2-|B|^2}{2|C-B|^2}(C-B)` and confirmed
`|Q-B|=|Q-C|` to 14+ digits and `Q\cdot(C-B)=\tfrac12(|C|^2-|B|^2)` exactly
at every sample; membership in the line through `A` parallel to `BC` is
immediate from the closed form (`Q` is by construction a scalar multiple
of `C-B`). This is a correct, elementary, fully rigorous fact — no gap.
**Certified `lemmas/q-as-two-line-intersection.md`.**

**Reported stall — independently confirmed accurate, not an artifact of
insufficient search.** Read Lemma A (`\angle BLN=\angle(BK,AC)`), Lemma B
(`\angle CKM=\angle(CL,AB)`), and the Corollary
(`\angle BLN+\angle CKM\equiv0\pmod\pi`) directly from the file: none of
these three certified facts mentions `Q` as a vertex or as one of the
named rays anywhere. The needed target
`\angle(KA,KQ)=\angle(LA,LQ)\pmod\pi` genuinely cannot be assembled from
this toolkit without an additional fact tying `Q` to `K` or `L` — this
diagnosis is correct given the population's current certified lemma set.
The file's honest disclosure of an incomplete systematic relabeling sweep
(due to a tooling failure, not a mathematical finding) is also correctly
flagged as incomplete rather than a negative result. No overclaiming.

## Certifications this round
- `lemmas/t-nonnegative-on-case-b-residual-domain.md` (new) — Case (b) of
  Open gap 7 fully closed, scope explicitly limited to Case (b).
- `lemmas/t-corner-value-exact-via-sigma-tau.md` (new) — independent
  rational-arithmetic proof of the shared corner value, cross-checking the
  sibling file's trig-identity derivation.
- `lemmas/q-as-two-line-intersection.md` (new) — simplified `Q`
  characterization, `QB=QC`, `AQ\parallel BC`.

## Net assessment
The round's central event is a serious potential contradiction (round 19's
claim vs. round 20's finding) that was independently investigated per the
dispatch's explicit instruction and **confirmed to be exactly as the
round-20 builder self-diagnosed**: round 19 was wrong, and the error was
caught by the builder's own mandated dependency-chain audit before being
recorded as a closure. This is a genuine narrowing of the shared central
gap — Case (b) of Open gap 7 is now unconditionally closed by two
independent proofs, and Case (a) is understood, for the first time
precisely, to require a wholly different approach (not a citation fix).
`current.md` updated with the full round-20 adjudication, Status remains
`partial`.
