## imo-2026-05 (lens: equality cases & the sandwiched middle)

### Distinct openings surfaced this route

1. **The collapsing substitution x = f(y).** Plugging x = f(y) into the original
   chain sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x f(y)) makes BOTH outer terms
   collapse to the same value f(y):
   - Left: sqrt((f(y)²+f(y)²)/2) = f(y).
   - Right: sqrt(f(y)·f(y)) = f(y).
   So the chain reads f(y) ≥ (f(f(y))+y)/2 ≥ f(y), forcing **equality throughout**:
   `f(f(y)) = 2f(y) − y` for all y > 0. (Verified algebraically above — this is
   an exact identity, not a conjecture.) This is the single most productive move
   found on this lens; it directly matches the "feed output back as input" idea
   in the prompt.

2. **Consequence: f is injective.** From f(f(y))=2f(y)-y, if f(y1)=f(y2) then
   f(f(y1))=f(f(y2)) ⟹ 2f(y1)-y1 = 2f(y2)-y2 ⟹ y1=y2 (since f(y1)=f(y2)).

3. **Orbit/arithmetic-progression structure.** Let d(y) = f(y) − y. The identity
   f(f(y))=2f(y)-y rearranges to f(f(y))−f(y) = f(y)−y, i.e. **d(f(y)) = d(y)**:
   d is invariant along forward f-orbits, and f^n(y) = y + n·d(y) is an exact
   arithmetic progression. Since f maps R_{>0}→R_{>0} for all n, positivity of the
   whole forward orbit forces d(y) ≥ 0 for every y (if d(y)<0 the orbit would
   eventually go negative). So **f(x) ≥ x for all x** — a clean one-line
   consequence of this substitution, no case work needed.

4. **CANDIDATE ANSWER (important correction to the run-state guess):** testing
   f(x) = x + c for a constant c ≥ 0 in the ORIGINAL (untouched) inequality gives,
   after expansion, both sides reducing to perfect squares:
   - Right ineq. (f(x)+y)² − 4x f(y) = (x+c+y)² − 4x(y+c) = (x−y−c)² ≥ 0.
   - Left ineq. 2x²+2f(y)² − (f(x)+y)² = 2x²+2(y+c)² − (x+y+c)² = (x−y−c)² ≥ 0.
   Both are literal identities (x−y−c)² ≥ 0, true for EVERY c ≥ 0 and every x,y>0
   (need c≥0 only so f(y)=y+c>0 for all y>0, including y→0⁺). I verified this
   numerically too (2000 random trials per c, all pass; see Small-case notes).
   **This means the answer is very likely the whole one-parameter family
   f(x) = x + c, c ≥ 0 — NOT just f(x)=x.** The run_state.md baseline note
   ("Likely answer: f(x)=x") should be corrected/broadened for the outliner.
   Equality in the ORIGINAL problem's sandwich occurs simultaneously in both
   inequalities exactly when x = y + c.

5. **Ruling out multiplicative family f(x)=kx.** Right inequality reduces to
   (kx−y)²≥0 (always true, any k>0). Left inequality reduces to a quadratic form
   in x,y with determinant −2(k²−1)² ≤ 0, PSD only at k=1 (boundary, giving
   (x−y)²≥0). So k=1 (i.e. f=id, the c=0 case of family 4) is the only
   multiplicative solution — no new family there, consistent with 4.

6. **Cross-orbit rigidity (the real remaining gap for exhaustiveness).** The
   exact identity f(f(y))=2f(y)-y and d(f(y))=d(y) only constrain d to be
   constant *along a single forward orbit*; a priori different orbits could
   carry different constants a=d(x), b=d(y). Substituting x or y from the SAME
   orbit into the original inequality always trivializes to a manifest square
   ((n−1)²d² ≥ 0 etc. — checked for several such substitutions, all vacuous).
   The informative constraint must come from mixing TWO DIFFERENT orbits.
   Rewriting the left (QM) inequality with a=d(x), b=d(y):
   `(x−y)² − 2a(x+y) + 4by − a² + 2b² ≥ 0` for all x,y>0 (exact, using
   f(x)=x+a, f(y)=y+b). I confirmed **numerically** that piecewise/discontinuous
   d (e.g. d(y)=0 for y≤1, d(y)=ε for y>1, even tiny ε=0.01) makes this fail at
   a concrete cross-orbit pair (x≈1.05 with a=ε, y≈0.90 with b=0): the *left*
   (QM) inequality is violated, not the right one. This is strong evidence the
   left inequality is exactly the tool that forces d to be a GLOBAL constant,
   completing exhaustiveness — but I have NOT produced the fully general
   algebraic argument (only the identity + a numerical falsification of
   non-constant d); that is the gap for the outliner/builder to close.

### Candidate technique(s)
- The "feed f(y) back as x" substitution (item 1) — direct, rigorous, cheap.
- Orbit/telescoping arguments on f^n(y) (cf. crux below) to pin exact identities.
- Algebraic SOS reduction (both original inequalities reduce to a single square
  (x−y−c)² for the conjectured family) — suggests trying an SOS/complete-the-square
  approach on the general (non-constant-d) case directly, rather than only via
  orbit combinatorics.

### Cheap-kill candidates
- **x=y substitution is a dead end** — both inequalities collapse to the trivial
  (f(x)−x)² ≥ 0 regardless of f; carries zero information distinguishing valid
  from invalid f. Don't waste a round on it.
- x=f(y) (or y=f(x), tried too — also trivializes once the exact identity is
  already known) is the one substitution that is NOT a dead end — it's the
  crux move (item 1).
- Multiplicative ansatz f(x)=kx is easily killed (item 5) — confirms the
  family is additive-shift, not multiplicative, and rules out other simple
  ansätze (e.g. affine f(x)=kx+c with k≠1 should also be cheap to rule out by
  the same SOS-of-quadratic-form method if the outliner wants a quick check).

### Knowledge-base entries to use
- **Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM** and "equality cases pin
  down the extremal configuration" (Algebra & Polynomials section) — directly
  the lens's premise, though note the actual algebra here is *not* literally
  AM-GM/QM-AM of the pair (x,f(y)); it is a bespoke identity that happens to
  reduce to (x−y−c)² — worth flagging so the outliner doesn't force-fit the
  classical QM-AM-GM equality condition (x=f(y)) as *the* answer pin; the real
  equality condition of the ORIGINAL problem is x = y + c.
- **Sum of squares (SOS) / completing the square** — exactly the technique that
  verifies the candidate family and could plausibly close the general
  exhaustiveness gap (rewrite the left-inequality defect as a quadratic form in
  x,y with a,b and show it's forced PSD only when a=b).
- **Functional equations: test special values, check injectivity/surjectivity**
  — injectivity obtained cleanly (item 2).
- **Direct proof / contradiction** (General Proof Methods) for the
  cross-orbit rigidity step.

### Analogous past problems (cruxes)
- **aimo-0710** (`domain=algebra`, `subtopic=functional-equations`) — genuinely
  analogous: same genre exactly (R_{>0}→R_{>0}, single functional INEQUALITY,
  "determine all f", answer a one-parameter family f(x)=c/x). Its crux move:
  substitute y=x to get f²(x) ≤ x, then substitute x=f^{n-1}(y) to get a
  non-decreasing chain of gaps f^n(y)−f^{n+2}(y) ≥ f^{n-1}(y)−f^{n+1}(y) ≥ 0,
  telescope m of them to get y − f^{2m}(y) ≥ m·(y−f²(y)), and since
  y−f^{2m}(y) < y (positivity) for all m, force y−f²(y) = 0, i.e. f is an
  involution (f²=id). Then the inequality collapses to xf(x) ≥ yf(y) for all
  x,y ⟹ xf(x) constant ⟹ f(x)=c/x. **Adaptation note:** our problem's analogous
  identity f(f(y))=2f(y)-y already comes out as an *exact* equality directly
  from one substitution (x=f(y)), stronger than aimo-0710's inequality f²≤y — we
  don't need their telescoping-sum-boundedness trick for that step. But their
  general STRATEGY (turn iterate inequality into an exact global identity, then
  turn the ORIGINAL inequality into a clean statement like "x f(x) is constant")
  is the template for our remaining step: try to show something like
  "f(x) − x is constant" the same way they showed "x f(x) is constant" — i.e.
  look for a clean two-variable inequality (post-substitution) that's exactly
  symmetric/forces equality of a single combined quantity across x,y, rather
  than my current messier a,b quadratic-form route.
- aimo-0290 (functional equation on integers, "squeeze a function constant on
  an arithmetic progression between two one-sided inequalities") — same flavor
  of "sandwich pins constancy" but on ℤ with an exact equation, less directly
  transferable (no natural analogue of R_{>0}/positivity growth argument here);
  worth a skim if the a,b cross-orbit argument stalls, but not a strong match.
- aimo-0399 (real-valued inequality f(x+y) ≤ y f(x) + f(f(x))) — same "iterate
  the inequality along f's own orbit, add two instances to cancel a nested
  term" flavor; distantly relevant as a template for combining L1 at (x,y) and
  (y,x) but I already tried that combination directly (see Dead ends) and it
  trivialized, so treat with caution.

### Prior progress
None — first round, empty population (confirmed: `results/imo-2026-05/approaches/`
and `current.md` do not yet exist / are empty).

### Dead ends (do not retry)
- **x=y diagonal substitution**: both inequalities reduce to (f(x)−x)²≥0 for
  ANY f — carries no information. (Verified by direct algebra above.)
- **Adding L1(x,y)+L2(y,x) [i.e. the left inequality at (x,y) and at (y,x)] and
  combining with R1+R2**: reduces to (x−f(y))² + (y−f(x))² ≥ 0, again vacuous
  for ANY f. Don't retry this combination.
- **Substituting y=f(x) using the already-known identity f(f(y))=2f(y)−y**:
  both resulting inequalities reduce to (f(x)−x)² ≥ 0 (trivial) — no new info
  beyond what item 1 already gives. Confirmed by direct algebra.
- **Same-orbit substitutions** (e.g. x = f^n(y) for the same y, using
  f^n(y)=y+nd(y)): every instance checked reduces to (n−1)²d(y)² ≥ 0 or similar
  trivial squares — the sandwich is exactly tight along any single orbit by
  construction; no contradiction available there. Must use genuinely different
  x,y (different orbits / different d-values) to get traction, per item 6.
- **Multiplicative ansatz f(x)=kx for k≠1**: fails (item 5), don't re-explore
  as a candidate family.

### Small-case / intuition notes
- CONJECTURE (strong, numerically verified over thousands of random trials and
  algebraically confirmed as an exact SOS identity): the full solution set is
  **f(x) = x + c for every constant c ≥ 0** (not merely f(x)=x). c=0 recovers
  the identity.
- CONJECTURE, numerically supported (piecewise f with even a 0.01 jump in
  f(y)−y fails the LEFT/QM inequality at a nearby cross-orbit pair): d(y) =
  f(y) − y must be a single GLOBAL constant, i.e. no other f works. This is the
  needed exhaustiveness step; only heuristic/numeric evidence so far, not yet a
  proof — flag as the key remaining gap.
- The problem is NOT solved by naively invoking classical QM-AM-GM equality
  conditions (x=f(y)) as "the" pinned configuration; the actual equality locus
  of the full original inequality (for the true answer family) is x = y + c,
  a shifted diagonal, not x=f(y) in general (x=f(y) is a useful *substitution*
  for extracting the functional identity, but is a different thing from "where
  equality holds for a fixed valid f").
