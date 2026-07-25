## imo-2026-02 (lens: q1<0 / r0<0 termwise-sufficient decomposition — β1-elimination)

### Headline finding: β1 CAN be eliminated algebraically — a genuinely new symbolic
reduction, not just re-confirmed numerics. Concretely:

Notation as in `lemmas/case-b-e-lt-0-t-factorization.md` /
`approaches/coordinate-bash-resultant-boundary.md` (round 11 section): `c=cosA,
s=sinA, d=cosB, t=sinB`, `X0 = ct/(2(ct+ds))`, `β1 = arccos(√X0)` (so
`x:=cosβ1=√X0, y:=sinβ1=√(1-X0)`), `γ=min(B,C)`, and `q1(σ,τ), r0(σ,τ)` the
degree-(4,3) polynomials in `σ=sin²A,τ=sin²B` from the certified factorization
lemma.

**Step 1 (verified numerically to <6e-15 on 200k samples, and it's a direct
trig identity so it is exact): a closed, β1-free formula for the domain
condition `sin(A+3β1)`:**
$$\sin(A+3\beta_1) = s(4X_0-3)\,x + c(4X_0-1)\,y,\qquad x=\sqrt{X_0},\ y=\sqrt{1-X_0}.$$
(Derivation: `cos3β1=4x³-3x`, `sin3β1=3y-4y³`; substitute `x²→X0,y²→1-X0` inside
the cubic terms — since `x,y≥0` this substitution is licit — giving exactly the
above. This removes the "3β1" triple-angle transcendence; only the single
square roots `x,y` of the already-algebraic `X0` remain.)

**Step 2 (verified numerically, 20M-sample sweep, restricted to the true
`Case-(b)∧E<0` sub-region): in this sub-region `C≫B` always (the observed
`(A,B)`-window is `A∈(0.407,0.537), B∈(0.912,1.091)`, giving
`C=π-A-B∈(1.51,1.82)≫B`), so `γ=min(B,C)=B` identically — no case split on
`γ` is needed inside this sub-region.**

**Step 3 (proved via monotonicity of cos on `(0,π/2)`, both sides shown
`≥0` numerically throughout — an easy, essentially free step): with `γ=B`,**
$$\beta_1<\gamma=B \iff \cos\beta_1>\cos B \iff x>d \iff X_0>d^2$$
**(squaring valid since `x,d` both shown `≥0`, in fact `d>0` strictly per
round 11's finding). This turns the `β1<γ` domain condition into the purely
polynomial condition `X0>d²`, with NO `arccos` or `β1` appearing at all.**

**Step 4 (the load-bearing numeric discovery this round, 20M-sample sweep,
zero violations): on the locus `{X0>d²}∩{E<0}` (both now already β1-free,
polynomial conditions), the two coefficients from Step 1's formula are
SIGN-DEFINITE:**
$$p:=s(4X_0-3)<0\quad\text{and}\quad q:=c(4X_0-1)>0\qquad\text{always, on }
\{X_0>d^2\}\cap\{E<0\}$$
(equivalently `X0<3/4` and `X0>1/4` on this locus — confirmed the observed
`X0` range there is `(0.348,0.662)`, comfortably inside `(1/4,3/4)`; this is
itself NOT yet proven symbolically, but is now a clean two-inequality
algebraic target purely in `c,s,d,t`, not a "sign of an entangled
combination" problem).

**Step 5 (the punchline — full β1-elimination, contingent only on Step 4):
given `p<0,q>0`, the condition `sin(A+3β1)<0`, i.e. `px+qy<0`, becomes
`qy<-px=|p|x`, both sides now `≥0`, so squaring is valid and gives**
$$\sin(A+3\beta_1)<0 \iff q^2(1-X_0)<p^2X_0 \iff X_0>\frac{q^2}{p^2+q^2}$$
**— a fully rational (no radicals, no arccos) condition in `c,s,d,t` alone.
Verified: 100% agreement with the true `sin(A+3β1)<0` condition on 43,330
independent samples of the restricted sub-domain.**

**Net result: modulo Step 4 (X0∈(1/4,3/4) on `{X0>d²}∩{E<0}`, itself now a
concrete 2-inequality polynomial claim, not yet proven), the ENTIRE
transcendental domain description `{β1<γ, sin(A+3β1)<0}` collapses exactly
to two polynomial inequalities in `c,s,d,t`:**
$$X_0>d^2\qquad\text{and}\qquad X_0>\frac{q^2}{p^2+q^2}\ \ (\text{i.e. }
p^2X_0>q^2(1-X_0)).$$
**This is precisely the "β1-elimination" the task asked for. The remaining
work to close `q1<0,r0<0` is now a genuine (if still nontrivial) semialgebraic
positivity problem in finitely many polynomial inequalities over `c,s,d,t`
(equivalently `A,B` via `σ,τ`) — NOT a transcendental/arccos problem anymore.**

### What's still open (do not overclaim this as solved)
1. Step 4 itself (`X0<3/4` and `X0>1/4` given `X0>d²∧E<0`) is unproven
   symbolically — it is the new sharpest sub-target. It's a strictly smaller,
   purely-algebraic claim than the original q1/r0 goal, likely tractable by
   direct resultant/Gröbner elimination since `X0,d,E` are all explicit
   rational functions of `c,s,d,t` subject only to `c²+s²=1,d²+t²=1`.
2. Even granting Steps 1-5, q1<0 and r0<0 must still be shown on the resulting
   2-inequality semialgebraic region in `(σ,τ)` (after eliminating the
   remaining `c,s,d,t`-vs-`σ,τ` sign ambiguities) — this is a smaller,
   fully-polynomial target than before but not yet attempted with this
   sharper domain description.
3. All of Steps 1,3,5 are exact algebraic identities/equivalences (Step 1
   numerically confirmed to 1e-15, Steps 3/5 are direct valid-squaring
   arguments given the established sign facts) — genuinely provable, not
   just numeric. Step 2 (γ=B, i.e. C>B throughout) and Step 4 (X0 sign bounds)
   remain numeric-only and are the two new symbolic sub-gaps to close.
4. Did not attempt Step 2's symbolic proof (C>B on the sub-domain) this round;
   it may follow quickly from known relations `A∈(0.4,0.54),B∈(0.91,1.09)`
   already established, or may need its own short argument.

### Candidate technique(s) for next steps
- Resultant/Gröbner elimination of `c,s,d,t` (mod `c²+s²=1,d²+t²=1`) applied
  to the two polynomial inequalities from Step 4/5, using the same style of
  reduction that produced the `T` factorization (`case-b-e-lt-0-t-factorization.md`)
  and Theorem 16.1/16.2's `D(x)` monotonicity machinery.
- Sturm-sequence / sign-variation counting on the univariate slices once one
  variable (e.g. `A`) is fixed, given the sub-domain is very narrow
  (`A∈(0.407,0.537)`) — may make direct interval-arithmetic-style symbolic
  bounding tractable.

### Cheap-kill candidates
- None found that fully close q1<0/r0<0 this round, but Step 3/5's squaring
  arguments ARE cheap, already-closeable sub-lemmas (rely only on already-
  established sign facts `d>0`, `x,y≥0`) — worth certifying immediately as
  free lemmas even before Step 4 closes, since they are unconditionally true
  identities/equivalences (Step 3 always valid since `γ=B` is a separate,
  numerically-supported fact but the squaring itself needs no further
  hypothesis once `γ=B,d>0` are known).
- Parity/sign check: `P>0` is automatic given `Case-(b)∧E<0` (already known,
  round 11) — re-confirmed this round, not a new fact.

### Knowledge-base entries to use
- No new named KB theorem beyond what's already invoked (resultant/Gröbner
  elimination, Weierstrass-style algebraization of trig conditions) — this
  problem's whole remaining machinery is bespoke computer algebra, as in
  prior rounds; the KB has no geometry-specific entries for this problem
  (confirmed absent since round 1).

### Analogous past problems (cruxes)
- Not reinvestigated this round (out of scope for this narrow lens); prior
  rounds (1, 5, 8, 10) already confirmed the crux corpus has no geometry-
  domain entries relevant here. No new crux search performed.

### Prior progress
- `lemmas/case-b-e-lt-0-t-factorization.md`: exact factorization
  `T=c(dQ1-cR0)/(4sin²(A+B))`, `Q1=-4st·q1(σ,τ)`, `R0=r0(σ,τ)`, certified.
- Round 11 (`coordinate-bash-resultant-boundary.md`): numeric-only finding
  that `q1<0,r0<0` individually throughout the true restricted sub-domain
  (25,568+40,790+4,923 samples, 0 violations); `d>0,c>0,P>0` established on
  this sub-domain; sub-domain window pinned to `A∈(0.407,0.537),
  B∈(0.912,1.091)`.
- THIS ROUND (new): the β1-elimination itself is now done in principle
  (Steps 1,3,5 above are provable identities/equivalences given two
  remaining sign facts), reducing the whole transcendental domain
  description to two polynomial inequalities in `c,s,d,t`. This is real,
  reproducible symbolic progress beyond round 11's pure numerics — but Step
  4 (the `X0∈(1/4,3/4)` sub-claim) and Step 2 (`γ=B`, i.e. `C>B`) are still
  themselves only numerically confirmed, so the overall q1<0/r0<0 claim is
  NOT proven — only reduced to a smaller, purely algebraic residual.

### Dead ends (do not retry)
- Direct rectangular-box sampling of `(σ,τ)` (round 10/11): confirmed again
  this round that `X0>d²` alone (without `E<0`) is far from sufficient
  (only ~53-62% q1<0) — do not treat any single one of `{X0>d², E<0,
  sin(A+3β1)<0}` as sufficient alone; all three (plus the derived Step-4
  sign facts) are needed jointly.
- Do not attempt to prove `q1<0,r0<0` on the naive bounding box
  `σ∈[0.1,0.3],τ∈[0.6,0.8]` (round 11 already found only ~80.7% there) —
  the true domain is a genuinely curved sub-region, now precisely
  characterized by Steps 3+5 above (not the old vague "transcendental"
  description).

### Small-case / intuition notes (all labeled conjecture except where noted
exact/proved above)
- Numerically (20M-sample sweep, this round), the exact residual sub-domain
  in `X0`-space is very narrow: `X0∈(0.348,0.662)` under `{X0>d²,E<0}`, and
  further narrows to `X0∈(0.348,0.395)` once the full `sin(A+3β1)<0`
  condition is also imposed — consistent with round 11's observation that
  the whole sub-case sits near a single extremal corner point
  `(A*,B*)≈(0.406,0.912)` shared with the `-pointwise` sibling's `(⋆)` target.
  This conjecturally suggests `q1,r0→0` exactly at that corner (round 11's
  observation, not re-tested here) — if so, a corner-local (Taylor/Hessian)
  argument, once it works for the sibling's `(⋆)`, plausibly transfers here
  too, exactly as round 11 flagged.
- The clean rational threshold `X0>q²/(p²+q²)` (Step 5) is a new explicit
  formula not present in any prior round's writeup — recommend the outliner
  splice Steps 1–5 verbatim into `coordinate-bash-resultant-boundary.md` as
  the next round's concrete elimination target (Step 4 + the residual
  `q1<0,r0<0`-on-the-now-fully-polynomial-domain claim).
