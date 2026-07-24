## imo-2026-05

### Headline finding (overturns the naive "f=identity" guess)
Testing f(x) = x + c (constant shift, not the multiplicative family cx) symbolically in sympy shows **both** inequalities reduce to the SAME perfect square:
```
(x^2+f(y)^2)/2 - ((f(x)+y)/2)^2 = (x - y - c)^2/4  >= 0      (A)
((f(x)+y)/2)^2 - x f(y)          = (x - y - c)^2/4  >= 0      (B)
```
identically, for ANY real c. So f(x) = x + c satisfies both inequalities for every x,y, for **every real constant c**, not just c=0. The only extra requirement is the codomain: f: R_>0 -> R_>0 forces x + c > 0 for all x > 0, i.e. **c >= 0**. Verified numerically too (random sampling + explicit grid scan for c = 0.01 … 10, no violation, margin matches (x-y-c)^2/4 exactly).

**Conclusion: the answer is almost certainly the whole family f(x) = x + c for c >= 0, not the single function f(x) = x.** This is the single most important correction for the outliner: do not aim the proof at "f(x)=x is forced," aim it at "f(x)-x is a non-negative constant." (I did not find this recorded in current.md / any approach file — there is no prior progress in the repo yet, so this may not have been noticed.)

By contrast, the purely multiplicative ansatz f(x) = cx forces c = 1 exactly (via (c^2-1)^2 <= 0 from minimizing the quadratic form in t = x/y coming from squaring (A)) — so among *multiplicative* rescalings only identity works, but that's a red herring/sub-case; the affine family is the real answer shape.

### Key algebraic relation (clean, one-substitution, exact — the crux move for this route)
Plug **x = f(t), y = t** into the *whole* three-term chain (not A or B separately):
```
sqrt((f(t)^2 + f(t)^2)/2) >= (f(f(t)) + t)/2 >= sqrt(f(t)*f(t))
```
LHS collapses to f(t) exactly (sqrt(f(t)^2) = f(t)), and the RHS-of-B collapses to f(t) exactly too (sqrt(f(t)^2) = f(t)). So the chain becomes
```
f(t) >= (f(f(t))+t)/2 >= f(t)
```
forcing equality throughout:
```
f(f(t)) = 2 f(t) - t   for all t > 0.      (*)
```
This is exact (an equation, not an inequality) and only needs ONE substitution into the given chain — cheap, robust, and reusable. It should be the first lemma in any outline for this route.

### Bootstrap giving one-sided bound f(x) >= x (rigorous, not just conjectural)
Let x_0 = t, x_n = f^n(t) (n-th iterate). (*) says x_{n+2} = 2x_{n+1} - x_n exactly, i.e. **the orbit is an exact arithmetic progression**: x_n = t + n·d(t) where d(t) := f(t) - t.
- If d(t) < 0, then for N large enough x_N := t + N d(t) <= 0. But x_N = f(x_{N-1}) is a value of f on the positive input x_{N-1} (well-defined and positive by minimality of N), so x_N must be > 0 by the codomain constraint f: R_>0 -> R_>0 — contradiction.
- Hence **d(t) >= 0 for all t, i.e. f(x) >= x for every x > 0.** This is a genuine, fully rigorous bootstrap/iteration argument using only positivity of the codomain, no continuity assumed.

This matches the c >= 0 half of the conjectured answer family exactly (d(t) is playing the role of "c" pointwise; the remaining gap is showing d(t) is the SAME constant for every t).

### The real remaining gap: global constancy of d(x) = f(x) - x
(*) rearranges (with g(x):=f(x)-x) to g(f(x)) = g(x): **g is invariant along the orbit of any single x** (not surprising — it's automatic since the orbit is an exact AP with fixed common difference). This alone does NOT force g to be the same constant across *different* starting points x, y whose orbits don't obviously interact. Numeric probing confirms this is the crux difficulty:
- Directly testing whether an isolated pair (x,y) and its swap (y,x) pin down a = g(x), b = g(y) to be equal: NO — grid search over (a,b) in [-3,3]^2 satisfying all four inequalities (A,B at (x,y) and at (y,x), x=1,y=5) leaves a large 2-D feasible region (a-b ranges over roughly [-2.1, 1.0]) — so a *local*, two-point argument is not enough by itself.
- Testing a genuinely **non-constant** g (a step function: g=1 for x<=1, g=3 for x>1) against the full inequalities over a large random grid **breaks both A and B badly** (margins down to about -1 and -0.45) — strong numerical evidence that global constancy really is forced by the problem, it's just not visible from an isolated pair; it needs a global argument.
- **Likely next-step idea (not developed, per instructions):** compare the orbits of two different seeds x1, x2 with (conjecturally) different d1 = d(x1) ≠ d2 = d(x2). Their iterates x1+n·d1 and x2+n·d2 diverge/converge linearly in n. Plugging the pair (x1 + n d1, x2 + n d2) into the original chain for large n and examining the leading asymptotic order (each side is Θ(n) with computable leading coefficients depending on d1, d2) may force d1 = d2 by comparing leading coefficients as n -> infinity. This is an asymptotic/bootstrap comparison across orbits, distinct from the per-orbit argument already used — a natural second attack for the outliner to formalize.
- Alternative angle: try to establish injectivity or strict monotonicity of f first (from A/B directly, not via the orbit), then use it to link g at nearby points via a squeeze / limiting argument (e.g., as y -> x^-).

### Distinct openings surfaced (for the outliner to pick / combine)
1. **The (*) relation + forward-orbit positivity bootstrap** — proven above, gives f(x) >= x rigorously. Cheapest, most complete piece so far.
2. **Backward-orbit / surjectivity-based bound for f(x) <= x**: if f had a preimage y0 with f(y0) = x, relation (*) forces y0 = x - d(x) uniquely (since f(y0)=x and f(x)=2x-y0 must hold by (*) at t=y0, i.e. relation gives f(f(y0))=2f(y0)-y0 => f(x) = 2x - y0 => y0 = x-d(x)). If d(x) is not globally constant and grows unboundedly as we chase preimages, could give an upper bound contradiction — but this route needs surjectivity (or partial surjectivity) of f established first, which is NOT yet shown. Flag as an open sub-goal, not yet resolved.
3. **Cross-orbit asymptotic comparison** (described above) to force global constancy of d(x) directly, bypassing the surjectivity requirement of opening 2.
4. **Direct two-variable algebraic manipulation**: treat g(x), g(y) as unknowns for a generic (not orbit-linked) pair and derive the strongest possible joint constraint from A and B together (the two inequalities as a system in a,b); the SymPy factorizations above give the exact quadratic forms to work with — factor them fully to look for a hidden identity that only two isolated points miss but that combined with the orbit-invariance (g(f(x))=g(x)) becomes airtight.

### Candidate technique(s)
- Substitution at "self-referential" points (x=f(t), y=t) to collapse the QM/GM bounding to equality — this is the crux move, essentially a discrete dynamical-systems / iterate argument on top of a functional inequality.
- Bootstrap/monovariant argument via iterated orbit + codomain positivity (proves f(x)>=x).
- (Needed, not yet found) an argument forcing d(x) to be globally constant — likely an asymptotic/limiting comparison of orbits, or an injectivity+squeeze argument.

### Cheap-kill candidates
- None found for pruning cases — the structure is continuous/algebraic, not combinatorial. The useful "cheap" move actually already fired: plugging x=f(t), y=t collapses the whole 3-term chain to equality in one line; that's the single biggest simplification available and should be lemma #1 in any outline.
- Parity/pigeonhole-style pruning: not applicable (real-valued continuous domain).

### Knowledge-base entries to use
- `knowledge_base.md` "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases..." — directly explains why A and B individually are almost-trivial QM-AM / AM-GM statements EXCEPT the arguments are cross-matched (f(x) paired with y, not with itself) — that's exactly why they're not automatically true and carry real content.
- `knowledge_base.md` "Functional equations: test special values, check injectivity/surjectivity." — matches the general method; injectivity/surjectivity of f is exactly the missing ingredient identified above (opening 2/4).

### Analogous past problems (cruxes)
- `aimo-0010` (algebra domain would be number_theory here but techniques transfer) — "Find all f: Z>=0 -> Z>=0 with f(f(f(n))) = f(n+1)+1." Crux moves: "Compute one higher iterate two ways to collapse a triple composition into a clean shift recurrence," and "sum the per-point displacement delta(n)=h(n)-n over a full residue system, evaluate two ways to pin the constant." This is genuinely analogous in *shape*: it also derives an exact iterate recurrence (there: f^4(n)=n+c) and then must pin down the constant c using a global (summing/counting) argument rather than a pointwise one — same difficulty pattern as our "orbit gives d(x)>=0 pointwise, but need d constant globally." The displacement-summing trick doesn't port directly (our domain is R_>0, continuous, no residues), but the *meta-move* — "derive an exact affine iterate law, then use a global averaging/counting argument, not a pointwise one, to pin the constant" — is the right template to imitate.
- `aimo-0089` — "Find all f:R->R satisfying a convexity/secant-slope inequality." Crux move: reinterpret the inequality as a supporting-line / supergradient bound. Less directly analogous (different inequality shape) but shares the flavor "a two-sided real inequality that is almost — but not quite — a standard inequality (Jensen/AM-GM) becomes an exact identity once you plug in the right anchor point." Worth a glance if the "global constancy" gap resists the orbit approach; the supporting-line idea may suggest treating d(x) as a slope-like quantity to be pinned via a similar anchor trick.
- No other close analogs found in the algebra/functional-equations subtopic that share the QM-AM-GM sandwich structure specifically.

### Prior progress
None recorded in `results/imo-2026-05/` — `current.md` and `approaches/` are empty; this appears to be the first exploration round.

### Dead ends (do not retry)
- Assuming/proving the answer is uniquely f(x)=x: **wrong target**. The correct answer is (very likely) the family f(x) = x + c, c >= 0. Any approach that tries to derive a contradiction from f(x) ≠ x for a single point x (without accounting for the constant-shift family) will fail because f(x)=x+c for c>0 is a genuine counterexample to "f(x)=x is forced."
- Multiplicative ansatz f(x) = cx as a stand-in for "general shape": only useful as a warm-up (it does correctly single out c=1), but does not reveal the affine family, so treating it as the main line of attack is a dead end / distraction.
- Naive combination of the two one-sided bounds derived at self-referential points (f(x)^2 >= x f(f(x)) from B, and x^2+f(f(x))^2 >= 2f(x)^2 from A used separately) collapses to the trivial (f(x)-x)^2>=0 when combined — **this route is a dead end for extracting new information**; the two inequalities must instead be combined via the *exact* substitution x=f(t),y=t (which sandwiches to equality) rather than combined algebraically after separate derivation.

### Small-case / intuition notes (labeled conjecture except where proven above)
- **Proven** (via sympy + bootstrap argument): f(x) = x + c satisfies both inequalities identically for every real c, and is a legitimate solution of the problem for every c >= 0 (positivity of codomain requires c>=0).
- **Proven**: f(x) >= x for all x (orbit/bootstrap argument, rigorous).
- **Conjectured** (strong numerical evidence, not yet proven): d(x) = f(x)-x is globally constant, i.e. the full solution set is exactly {f(x) = x+c : c >= 0}. Non-constant candidate g's fail badly numerically (margins as negative as -1), suggesting this is true and provable, but the mechanism (which two-variable identity forces global constancy) is not yet found — flagged as the key remaining gap for the outliner.
- Multiplicative family f(x)=cx: only c=1 works (proven via minimizing a quadratic form in t=x/y after squaring inequality A); this is consistent with but weaker than the affine finding (c=1, additive-c=0 is the overlap point x itself).
