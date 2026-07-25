# Outline review — imo-2026-05 (IMO 2026 P5)

Answer under review: **f(x) = x + c, c ≥ 0**, all four approaches share the same
scaffolding (Lemma A f(f(y))=2f(y)−y; Lemma B injective; Lemma C d(y)=f(y)−y orbit-invariant,
fⁿ(y)=y+n·d(y), d≥0) and the same COMPLETE easy direction. I verified the load-bearing algebra
symbolically before ruling on any route.

## Verified facts (sympy)
- Easy direction: for f(t)=t+c, **both** R-defect and L-defect equal exactly ((x−y)−c)². So
  the "easy direction is clean SOS" claim is VALID; positivity of codomain forces c≥0. Sound.
- R-test at (x,y)=(f(p),q): defect = (p−q)²+4(a−b)(p+a), a=d(p),b=d(q). Confirmed exact.
- L-test at (f(p),q): defect = (p−q)²+2(b−a)(a+b+2q). Confirmed exact.
- Lemma A derivation (x=f(y) forces both bounds tight) is correct and non-circular.
- **The residual {0,b} sub-case is closeable** (see orbit-crossing below) — I verified the
  fixed-point band and the boundary contradiction numerically.

---

## orbit-crossing — APPROVE  [STRONGEST, near-complete]
- **Main Lemma (two positive values impossible) is genuinely COMPLETE and sound.** Marching
  Pₘ=p₀+ma→∞ while keeping Qₙ within gap <b, then R-test gives bounded (Pₘ−Qₙ)²<b² ≥
  4(b−a)(Pₘ+a)→∞. The step needs the *smaller* value a>0 (so the orbit marches) — correctly
  flagged. No circularity; the AP-approximation needs only a bounded gap, not density. Valid.
- **Residual {0,b} gap — has a clean closing mechanism the builder should use.** I found and
  numerically confirmed it: for p∈F (fixed) and any x∈G (shift by b), raw L(x,p):
  2(x²+p²) ≥ (x+b+p)² FAILS for every x in the open band ((b+p)−√(4bp+2b²), (b+p)+√(4bp+2b²))
  ∋ p. Hence that whole band must be fixed points ⟹ **F is open**. Since G≠∅ and F≠∅ partition
  the connected (0,∞), F has a boundary point t>0 with t∈G and F-points pₙ→t; raw R gives the
  separation (t−pₙ)²≥4pₙb, so in the limit 0 ≥ 4tb > 0 — contradiction. This retires the sub-case
  without needing monotonicity. Builder: make "F open" and "boundary point t>0 exists" rigorous
  (connectedness of (0,∞) + F clopen ⟹ F=(0,∞) contradicting G≠∅). Candidates (i)–(iii) in the
  file are weaker/vaguer than this; steer to the openness argument.
- Verdict: **APPROVE.** This is essentially a full proof; only the openness write-up remains.

## monotonicity-orbits — CHANGES REQUESTED
- Lemma D (f nondecreasing ⟹ d nondecreasing via orbit overtaking) is sound. Threshold finish
  is sound (it is the boundary contradiction specialised to the monotone case).
- **GAP 1 (f nondecreasing) is the real wall and the proposed lever has a hole.** The plan
  "f(x) = sup_y[2√(x f(y))−y], attained at the y with f(y)=x" needs such a y to EXIST, i.e.
  x in the range of f (surjectivity) — not established. For x outside range(f), R only gives
  f(x) ≥ the envelope, not equality, and "f ≥ increasing sup" does NOT make f increasing.
  The builder must either prove the relevant surjectivity or find another route to monotonicity;
  do not assume continuity. Real risk this route stalls at GAP 1.
- Verdict: **CHANGES REQUESTED** — valid skeleton, but GAP 1's lever is not yet a proof.

## shift-family-sos — CHANGES REQUESTED
- Reduced forms R′ ((x−y)²+a²+2a(x+y)−4bx≥0) and L′ are correct; R′ tight at x=f(y) is correct.
- **The stated pin is mis-aimed.** "Force a=b for ALL x,y directly from R′,L′ … adding two
  mirrored instances must collapse to a=b" cannot work as a purely pointwise identity: a properly
  *separated* two-valued d satisfies every *interior* pairwise R′/L′ instance (I verified the
  only violations occur for pairs straddling the F/G boundary). So the algebra can only bite via
  a *straddling pair* — two nearby points of different d-value near the F/G boundary — which is
  the same boundary/separation mechanism as orbit-crossing, not an independent "one-framing"
  kill. The file's step-2 "let x→y with different d-values" is exactly this straddling pair (a
  single point cannot carry two d-values), so redirect the builder to make that explicit rather
  than seeking a universal a=b identity.
- Verdict: **CHANGES REQUESTED** — correct reductions, but reframe the pin around the boundary
  straddle; the literal "algebraic a=b for all x,y" is unattainable.

## variational-min — CHANGES REQUESTED (weakest)
- Envelope identity (♦) f(y)=min_x (f(x)+y)²/(4x), attained at x=f(y), is CORRECT (R gives ≤,
  Lemma A gives equality at x=f(y)). Elegant.
- Both remaining steps are under-specified and restate hard sub-problems: GAP 1 (monotone
  minimizer) is as hard as monotonicity-orbits' GAP 1; GAP 2's "tangency ⟹ d const" reduces to
  the L-test defect (u−v)²+2(b−a)(a+b+2v)≥0, which is just the same L-test already in the pool
  and only bites near the boundary. No new closing mechanism beyond the shared crux.
- Verdict: **CHANGES REQUESTED** — sound identity, but no route to close that isn't already
  covered better elsewhere.

## Diversity / shared-wall note
All four ultimately converge on ONE crux for the {0,b} residual: F and G cannot be adjacent
(separation + connectedness). orbit-crossing closes it (openness/boundary), monotonicity via a
threshold, shift-family via a straddling pair — genuinely different *packagings* of the same
mechanism, plus the two-positive-values case is independently killed by marching (growth). The
field is not stuck: the crux is already solved inside orbit-crossing. Next round need not force a
new framing; the priority is to finish orbit-crossing rigorously and let the others corroborate.

## Ranking (Elo, this round)
orbit-crossing 1546 > shift-family-sos 1502 ≈ monotonicity-orbits 1499 > variational-min 1454.

build set: orbit-crossing, monotonicity-orbits, shift-family-sos
