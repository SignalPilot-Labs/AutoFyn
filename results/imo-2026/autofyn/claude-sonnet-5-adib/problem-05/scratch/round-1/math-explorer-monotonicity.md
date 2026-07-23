## imo-2026-05
(workspace `results/imo-2026-05/` did not exist yet — confirmed empty, no prior population.)

### Distinct openings
1. **Equality-forcing substitution x = f(y).** Setting x = f(y) makes both outer bounds
   collapse: QM(f(y),f(y)) = f(y) = GM(f(y),f(y)), so the whole sandwich squeezes to an
   **exact equality**: `f(f(y)) = 2f(y) - y` for every y > 0. This is the single most
   powerful move available — it converts the inequality into a genuine functional
   *equation* on the iterate f∘f, and is rigorous (no case-splitting, holds unconditionally).
   I verified this by direct computation:
   - x=f(y): left side = sqrt((f(y)²+f(y)²)/2) = f(y); right side = sqrt(f(y)·f(y)) = f(y).
   - So f(y) ≥ (f(f(y))+y)/2 ≥ f(y) forces (f(f(y))+y)/2 = f(y), i.e. f(f(y)) = 2f(y)−y.
2. **Orbit / arithmetic-progression argument for a lower bound f(y) ≥ y.** Fix y0, let
   a_n = f^(n)(y0) (n-fold iterate, a_0 = y0). From f(f(y))=2f(y)-y, the sequence a_n
   satisfies the linear recurrence a_{n+1} - a_n = a_n - a_{n-1} (constant second
   difference), so a_n = y0 + n·c is an **exact arithmetic progression** where
   c = f(y0) - y0. Since f maps R_{>0} → R_{>0}, every a_n must stay positive for all
   n ≥ 0. If c < 0 the progression → -∞, contradiction for large n. Hence c ≥ 0 for
   every y0, i.e. **f(y) ≥ y for all y > 0** (rigorous, proven — not just conjectured).
   This mirrors the crux technique in aimo-0710 (see below): iterate a one-step
   substitution along the orbit of f, telescope the gaps, use positivity to kill the
   wrong sign.
3. **Injectivity via the iterate equation.** From f(f(y))=2f(y)-y, if f(y1)=f(y2) then
   f(f(y1))=f(f(y2)) gives 2f(y1)-y1 = 2f(y1)-y2, so y1=y2. **f is injective** — clean,
   rigorous, follows immediately.
4. **Sufficiency family via QM–AM–GM collapse.** Write d(x) := f(x) - x. The middle
   term (f(x)+y)/2 equals AM(x, f(y)) + (d(x)-d(y))/2. If d is a **constant** c, the
   correction term vanishes and the whole inequality becomes exactly the standard
   QM(x,y+c) ≥ AM(x,y+c) ≥ GM(x,y+c), which is *always* true. This proves **f(x) = x+c
   is a valid solution for every constant c ≥ 0** (algebraically verified, not just
   numerically — see below). This is a genuinely different top-level target than
   "prove f = identity": the real claim is a **one-parameter family**, and any approach
   assuming uniqueness (f≡id) will be chasing a false target.
5. **Necessity of d(x) constant (the remaining gap).** Need to show every solution has
   d(x)=f(x)-x constant. We already know d(f(y)) = d(y) for all y (constant along
   f-orbits, from opening 1: f(f(y))-f(y) = f(y)-y). Numerically, non-constant
   deviations (sinusoidal shift, growing shift, step shift) all produced clear
   inequality violations (see Small-case notes) — strong evidence d must be globally
   constant, not just orbit-wise constant. A plausible route: use the near-equality
   perturbation x = f(y)+ε (ε small) to bound d(f(y)+ε) - d(y) by O(ε²) via the
   width of the [GM,QM] interval around AM, forcing local constancy of d near every
   point of range(f); combined with the forward-orbit density/injectivity this might
   force global constancy — but this remains a genuine open gap, not yet a proof.

### Candidate technique(s)
- Equality-forcing substitution (plug in the value that makes QM=GM, collapsing the
  sandwich to an exact functional equation) — this is the crux move, analogous to
  standard "squeeze via extremal substitution" for functional inequalities.
- Orbit/iterate telescoping to pin sign of f(x)-x (matches KB "Invariants &
  monovariants" and the aimo-0710 crux pattern below).
- Injectivity-forcing via composition (KB "Functional equations: test special values,
  check injectivity/surjectivity").
- AM–QM–GM equality/near-equality analysis (KB "Standard inequalities: AM-GM,
  Cauchy-Schwarz, QM-AM... Equality cases pin down the extremal configuration").

### Cheap-kill candidates
- Plugging x=y gives only the trivial QM≥AM≥GM fact for (x,f(x)) — no information;
  don't waste time exploring x=y as a lead (it's automatically true for ANY f>0).
- Power-function ansatz f(x)=x^k: forces k=1 only (shown by direct AM–GM comparison
  x^{k-1} vs y^{k-1} needing to hold for all x,y). Confirms f=identity is in the
  family but does not by itself rule out the additive-shift family.
- f(x)=c/x fails immediately (y→0 blows up the GM bound while the QM bound stays
  bounded) — rule this out without further work.

### Knowledge-base entries to use
- **Standard inequalities** (AM-GM, QM-AM; equality cases pin the extremal
  configuration) — directly drives the x=f(y) collapse and the sufficiency proof for
  f(x)=x+c.
- **Functional equations**: test special values, check injectivity — used for the
  x=f(y) substitution and the injectivity derivation.
- **Invariants & monovariants** (Combinatorics section, but applicable): d(x)=f(x)-x
  invariant along f-orbits is exactly this kind of structure.

### Analogous past problems (cruxes)
- **aimo-0710** (algebra, functional-equations) — "x(f(x)+f(y)) ≥ (f(f(x))+y)f(y) for
  all x,y ∈ R_{>0}", answer `f(x)=c/x`. **Strong analogy**: same domain/codomain
  (R_{>0}→R_{>0}), same shape (a two-variable functional inequality involving f∘f),
  and the crux techniques there are essentially a direct template for our problem:
  (1) "iterate a one-step substitution along the orbit of f so a single inequality
  becomes a shift-invariant relation between consecutive iterate-gaps" — exactly what
  I did in Opening 2; (2) "telescope a chain of iterate-gaps into a bound linear in
  step count, pit against a fixed bound to force the base gap to vanish" — forces
  f²(y)=y there (an involution), analogous to our forced-sign / equality result;
  (3) "feed the derived relation back into the original inequality to collapse it
  into a symmetric two-variable inequality, then swap x,y to force a product/quantity
  constant" — exactly the shape of move needed to finish Opening 5 (constancy of d).
  Read `results/imo-2026-05` builders should look at this crux's full solution
  structure closely; it is the best available template despite different final
  answer (c/x there vs x+c here — different because their inequality forces f²=id,
  ours forces d constant).
- Other functional-equation cruxes (aimo-0399, aimo-0290, aimo-0787, aimo-0761,
  aimo-1022) share generic moves (feed value back into equation, drive free variable
  to infinity/zero for contradiction, sandwich arguments) but are less structurally
  close than aimo-0710 — worth a skim but not as directly reusable.

### Prior progress
None — fresh workspace.

### Dead ends (do not retry)
- Assuming the unique answer is f(x)=x (plain identity): **numerically and
  algebraically wrong to present as the final answer** — f(x)=x+c for any c≥0 also
  satisfies the inequality exactly (verified both by direct algebra reducing to
  QM-AM-GM of (x,y+c), and empirically with random sampling over x,y ∈ [1e-4,1e4],
  worst-case violation ≈ 0 to numerical precision for c ∈ {0.001,...,5}). Do not let
  an approach converge on "prove f=id" as the target; the correct top-level claim is
  the family f(x)=x+c, c≥0.
- x=y substitution: gives nothing (trivial AM-GM/QM-AM tautology for any positive f).

### Small-case / intuition notes
- Verified by direct algebra (not just numerics) that f(x)=x+c satisfies the
  inequality for every c ≥ 0, with equality iff x = y+c (i.e. x=f(y)).
- Verified numerically (python, ~few×1e5 random trials, x,y spanning 1e-4..1e4) that:
  - f(x)=x+c (constant shift) never violates the inequality for c ∈
    {0.001,0.01,0.1,0.5,1,2,5} — consistent with the algebraic proof.
  - f(x)=x+1+0.5sin(x)² (non-constant shift, bounded oscillation) **violates** the
    inequality (found a point with left-mid <0, i.e. QM bound fails), e.g. worst
    violation ≈ -0.25 at (x,y)≈(3.14,1.60).
  - f(x)=1.1x+1 (non-constant, linearly growing shift) violates badly (worst
    violation ≈ -8.3 at large x,y≈(994,744)) — consistent with the earlier power-law
    check (only k=1 works).
  - A step-function shift (d(x)=2 for x<1, d(x)=1 for x≥1) violates sharply
    (≈ -0.5) — even a single discontinuity in d breaks it.
  - These are strong (but not yet proof-level) evidence that **d(x)=f(x)-x must be
    globally constant**, i.e. the full answer set is conjectured to be exactly
    `f(x) = x + c` for constants `c ≥ 0`.
- f(y) ≥ y for all y is *proved* (not conjectured) via the orbit/arithmetic-progression
  argument (Opening 2). f is *proved* injective (Opening 3). f(f(y))=2f(y)-y is
  *proved* exactly (Opening 1). The remaining gap is proving d constant globally
  (only proved constant along f-orbits so far) — this is the crux the outliner should
  target, and aimo-0710's third crux move (symmetrize by swapping x,y after
  substituting the derived structural fact back into the original inequality) is the
  most promising template to close it.
