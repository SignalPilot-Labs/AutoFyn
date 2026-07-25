## imo-2026-02 — lens: positivity inequality F(θ,A,B,C)>0

### What F actually is (located in `ptolemy-trig-identity.md`, Round-4 "Step 4")
Setting p=cotθ, x=cotψ (genuine root of quadratic III′), y=cotφ (genuine root
of the symmetric quadratic for IV):
$$F(p,x,y):=\sin A\,(p+2x)(p+2y)-\sin A-\cos A\,(2p+2x+2y).$$
Explicit closed forms (from the file, Steps 2–3):
- x = (−b₁−√D₁)/(2c₁), y = (−b₂−√D₂)/(2c₂), with
  a₁=2cos²θ·sinB − sinC·cosA, b₁=−sinA sinC cos2θ + sin2θ(2sinA cosC+sinC cosA),
  c₁=−2sinA sinθ sin(C−θ), D₁=b₁²−4a₁c₁ (and a₂,b₂,c₂,D₂ = swap B↔C).

**Key structural finding (new this round): F is not a new, independent
inequality — it is algebraically identical to the previously-stuck
geometric claim.** The file's own Step 1 derivation shows
$$F(p,x,y)=\frac{\sin(A-\alpha-\alpha')}{\sin\alpha\,\sin\alpha'},$$
where α=∠BAK, α'=∠CAL, cotα=p+2x, cotα'=p+2y (Step 0's cot-identity).
Since 0<α,α'<A<π (Lemma S3, so sinα,sinα'>0), **F>0 ⟺ α+α'<A**, which is
*exactly* Round 3's "∠BAK<∠BAL" inequality that stumped the population for
two rounds already (it's the same claim, dressed in exact closed-form
cotangents instead of Lemma-2 tan-formulas). So Step 4 has not reduced the
difficulty of the geometric problem — it has produced a fully explicit
rational/radical formula for the same open inequality, which is valuable
(no more implicit root-finding) but the "positivity" gap = the "angular
order" gap from round 3, just re-encoded.

### Investigation 1: SOS / factoring attempts (sympy)
- Directly simplifying D₁=b₁²−4a₁c₁ symbolically (`sympy.simplify`,
  `trigsimp`) does not collapse to a recognizable closed form; expanding in
  independent sin/cos symbols and factoring gives an unenlightening degree-4
  polynomial in (cosθ,sinθ) with sinC as an overall factor — no obvious
  perfect-square or SOS structure found in the time available.
- Full symbolic `simplify` of F itself (with both radicals substituted) does
  not terminate in reasonable time — matches the file's own report.
- **Not attempted this round** (time-boxed out, but identified as most
  promising next step, matching the file's own recommendation): clearing
  the two square roots one at a time (isolate √D₁, square, isolate √D₂,
  square again) to get a fully polynomial (radical-free) sufficient
  inequality in cosθ,sinθ,sinA,cosA,sinB,cosB,sinC,cosC (with the
  sin²+cos²=1 and A+B+C=π constraints) — this converts the problem into a
  genuine real-algebraic-geometry / Positivstellensatz question, tractable
  in principle by an SOS/SDP solver (not by hand or `sympy.simplify` alone).

### Investigation 2: naive containment bound — tested and REFUTED
Since ψ∈(0,C−θ) (Step 3's containment range) and cot is decreasing, one
might hope the crude bound cotψ > cot(C−θ) (hence cotα > cotθ+2cot(C−θ),
giving an upper bound on α without needing the exact quadratic root) is
already strong enough to prove α+α'<A. **Tested numerically over 300,000
random samples: this naive bound is violated in ~10.5% of cases**
(worst margin found ≈ −1.29, i.e. the crude bound is not even close to
sufficient in some regimes). This is useful negative information: **the
exact position of the genuine root within (0,C−θ) matters**, not just its
containment in the interval — so any successful proof must use the
quadratic's actual coefficients (or at least a sharper estimate than "root
lies in the open interval"), not merely the interval bound from Step 3's
IVT theorem.

### Investigation 3: tightness / extremal structure (the most useful finding)
A systematic numerical search for the infimum of F over the entire valid
domain (0<θ<min(B,C), A,B,C>0, A+B+C=π) — via random sampling (300k pts),
grid search near boundaries, and `scipy.optimize.differential_evolution`
(global optimizer, polished) — all agree:
$$\inf F = 4 \text{ exactly, approached only in the degenerate limit } A\to0^+,$$
**never attained for a genuine triangle** (A>0 strictly), and (importantly)
this infimum is reached along *several* different (B,C,θ) directions as
A→0 — e.g. B=C, θ=thmax/2 gives F→4; also B≈2C, θ/thmax≈0.75 gives F→4 —
so it is a genuine codimension-1 boundary limit, not an isolated point.
This is a **much sharper and cleaner numeric fact than the file's reported
"min ≈ 11.3 over 500,000 random samples"** — the random-uniform sampling in
the file evidently never got close enough to the A→0 corner (which is a
small-measure region under naive Dirichlet-style sampling of (A,B,C)) to
see the true infimum.

**This is conjectural (numerical only), but a strong signal:**
$$F(\theta,A,B,C) > 4 \quad\text{strictly, for every genuine triangle configuration},$$
i.e. the true target is not merely "F>0" but the much more specific
"F−4>0" — and F−4→0 exactly as A→0 suggests the natural next move is to
look for a closed form of F−4 or of A·(something) that manifestly vanishes
as A→0 and is otherwise a sum of positive terms. This is a concrete,
sharper target for next round's algebra: try to compute F−4 symbolically
(rather than F) and check if it factors more cleanly (constants often
cancel favorably), or attempt a Taylor expansion of F−4 in a scaled
variable (e.g. set A = εa, α=εu, α'=εv for small ε, and find the limiting
ε→0 inequality — this "blow-up" analysis is a standard technique for
finding the right SOS certificate when the true extremal case is a
boundary/degenerate limit rather than an interior critical point).

### Cheap-kill candidates
None found that immediately settle it; the naive containment bound
(Investigation 2) was the most promising cheap kill and it fails. No
parity/pigeonhole structure applies (this is a continuous inequality).

### Recommendation for next round's builder/outliner
1. **Best framing**: attack "F>4" (backed by strong numerical evidence,
   inf=4 exactly, degenerate-limit-only) rather than "F>0" — a sharper,
   more specific numeric target is more likely to correspond to a clean
   algebraic identity (F−4 = manifestly nonnegative expression) than the
   vague "F>0".
2. Recall F>0 ⟺ α+α'<A exactly (Investigation intro) — so this is literally
   the same open inequality flagged since round 3 (`∠BAK<∠BAL`, later
   reframed as `α+α'<A`). Do not treat "closing Step 4" and "closing
   round 3's K/L-order gap" as two different problems — they are one gap,
   attacked with two different levels of explicitness (implicit angle
   comparison vs. explicit closed-form radical inequality). A synthetic
   proof of α+α'<A (bypassing the messy quadratic-root algebra entirely)
   would close this just as well as an algebraic proof of F>4, and might be
   easier — worth a dedicated synthetic-geometry attempt (e.g. relating K,L
   to the nine-point circle or to a common auxiliary circle, since M,N are
   midpoints and ψ,φ are angles subtended at M,N).
3. If pursuing the algebraic route: isolate/clear the two square roots one
   at a time (as the file itself flags) to get a polynomial sufficient
   condition, then try an SOS certificate via an SDP solver (not just
   `sympy.simplify`) — the sharp-but-unattained infimum of exactly 4 is
   evidence a clean rational/SOS proof of F−4≥0 (with strict inequality for
   A>0) should exist.
4. A blow-up/degenerate-limit analysis around A→0 (Investigation 3) is
   likely to reveal exactly which terms in F−4 need to combine into a
   perfect square or product-of-positives — recommend computing the
   limiting behavior symbolically (Taylor series in A) as a concrete first
   step before attempting the full symbolic clearing.

### Knowledge-base entries to use
- No specific KB entry found tailored to "two-radical trig positivity" —
  general SOS / Schur / AM-GM entries in `knowledge_base.md` (if present)
  are the relevant category; consult it directly for a named
  Positivstellensatz-style technique to cite once a certificate is found.

### Analogous past problems (cruxes)
Not investigated in depth this round (lens was specifically the positivity
inequality, not corpus search) — a genuine crux-corpus query for
"trigonometric positivity via SOS after clearing radicals" or "quadratic
root selection + inequality" (subtopics: algebra/inequalities,
geometry/trig-identities) is recommended for the next explorer round if
this gap persists.

### Prior progress
Steps 0–3 of `ptolemy-trig-identity.md` (cot-identity, quadratic reduction,
IVT branch-selection theorem) are fully proved and independently certified
(`lemmas/ptolemy-trig-branch-selection.md`). Step 4 (positivity) remains the
single open gap for this entire approach.

### Dead ends (do not retry)
- Naive containment-interval bound (cotψ>cot(C−θ) alone) to bound α+α'<A —
  refuted numerically (~10.5% violation rate over 300k samples), do not
  retry without a sharper estimate of the genuine root's exact position.
- Direct `sympy.simplify`/`trigsimp` on the full closed-form F (with both
  radicals substituted) — does not terminate (confirmed independently this
  round, matches the file's own report).

### Small-case / intuition notes (all numerically conjectural, not proved)
- F's global infimum over the entire valid domain is **exactly 4** (not
  ≈11.3 as previously reported — that was an artifact of uniform random
  sampling missing the thin A→0 boundary region), approached only as A→0⁺,
  never attained for a genuine triangle.
- The naive interval bound for ψ,φ is insufficient by a wide margin in
  ~10% of the domain — the exact quadratic root (not just its containing
  interval) is essential to any proof.
- F>0 is provably (not just numerically) equivalent to α+α'<A given the
  already-certified facts (Step 1 + Lemma S3); this is the same inequality
  flagged as open since round 3, now in fully explicit closed form.
