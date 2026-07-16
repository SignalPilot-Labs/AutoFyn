# imo-2026-05 (Analogy / Prior-Technique Retrieval Lens)

## Problem restatement
Find all f: R_{>0} -> R_{>0} such that
  sqrt((x^2 + f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y))   for all x,y > 0.
This is a sandwich: QM(x, f(y)) >= (f(x)+y)/2 >= GM(x, f(y)).

---

## Answer (strongly conjectured, verified numerically)

**f(x) = x + c for any constant c >= 0.** No other solutions.

Verified: f(x) = x+c satisfies both inequalities because with A=x, B=f(y)=y+c:
- f(x)+y = (x+c)+y = x+(y+c) = A+B, so the middle term IS AM(A,B).
- The sandwich becomes QM(A,B) >= AM(A,B) >= GM(A,B), the classical chain, always true.

Checked against: f(x)=2x+1 (FAILS: L violated for x large, y small), f(x)=0.5x+0.5 (FAILS: both L and R), f(x)=x+c*sqrt(x) for large c (FAILS for small x/y), f(x)=x^2 (FAILS), f(x)=1/x (FAILS). Only f(x)=x+c with c>=0 passes all tests.

---

## Distinct openings

**Opening 1 — Key substitution x=f(y), then orbit analysis.**
Set x = f(y) in the full sandwich. Since QM and GM both collapse to f(y) (because QM(f(y), f(y)) = f(y) and GM(f(y), f(y)) = f(y)), the sandwich becomes:
  f(y) >= (f(f(y))+y)/2 >= f(y).
This forces (f(f(y))+y)/2 = f(y), i.e., **f(f(y)) = 2f(y) - y** for ALL y > 0.
No surjectivity needed — f(y) is always a valid positive input.
The identity means h = f-id satisfies h(f(y)) = h(y): h is CONSTANT ON ORBITS.
Since f^n(y) = y + n*h(y) must stay in R+ for all n, we need h(y) >= 0.
The RIGHT inequality (rewritten as (R*)) then forces h to be globally constant:
  (f(x)-y)^2 >= 4x*h(y) - 4y*h(x) for all x,y > 0.
If h takes two values c < d on two f-invariant arithmetic orbits, for large elements x of the c-orbit (x ~ x0 + n*c, n large), f(x) = x+c grows, and the d-orbit has elements within distance at most d of f(x). But (R*) requires the distance |f(x)-y| >= 2*sqrt(x*(d-c)) which grows ~ sqrt(x), contradiction for large x. So h must be constant c >= 0, giving f(x) = x+c.

**Opening 2 — Rewrite as QM-AM-GM for reparametrized pair.**
Note that for f(x) = x+c: f(x)+y = x+c+y = x+(y+c) = x+f(y). So the middle term equals AM(x, f(y)). The sandwich collapses to QM(x,f(y)) >= AM(x,f(y)) >= GM(x,f(y)), which is classical. The converse: when does (f(x)+y)/2 = AM(x, f(y))? This requires f(x)-x = f(y)-y = constant, i.e., f(x) = x+c. But the problem only SANDWICHES (f(x)+y)/2 between GM and QM of (x,f(y)), not that it equals AM. So this isn't the full characterization — the sandwich gives freedom. The opening: show that lying between GM and QM of (x, f(y)) while also satisfying the SYMMETRIC inequality (swap x,y roles) forces the middle term to actually BE the AM.

**Opening 3 — Functional equation f(f(y)) = 2f(y) - y, then monotonicity argument.**
Once the identity f(f(y)) = 2f(y)-y is derived, if one additionally shows f is monotone increasing (e.g., from the RIGHT inequality showing that increasing f(y) forces increasing (f(x)+y)/2 for fixed x), then h = f-id being constant on orbits + monotonicity forces h to be globally constant.

**Opening 4 — Direct algebraic bounding from both L and R.**
From L: f(x) <= sqrt(2*(x^2+f(y)^2)) - y (upper bound on f(x) in terms of y, f(y)).
From R: f(x) >= 2*sqrt(x*f(y)) - y (lower bound).
Using the identity f(f(y)) = 2f(y)-y and iterating these bounds might squeeze h to zero variation.

---

## Candidate technique(s)

1. **Substitution x = f(y) to pin the sandwich to equality** — the central move: makes both outer terms equal, forcing the middle term to equal them too.
2. **Orbit analysis for arithmetic-sequence orbits** — the structure f^n(y) = y + n*c shows c must be constant via a density/distance argument from the R* inequality.
3. **Analogue of the aimo-0710 iterate-and-telescope technique** — in that problem, iterating x=f(y) substitution led to telescoping sum forcing f^2=id. Here, x=f(y) forces f^2(y)=2f(y)-y, and then a one-step argument (rather than telescoping) pins h to be constant.
4. **"Equality forces the classical mean chain" reversal** — the answer f(x)=x+c comes from the fact that (f(x)+y)/2 = AM(x,f(y)) is the unique value simultaneously satisfying QM >= _ >= GM for ALL (x,y); when the middle term differs from AM(x,f(y)), the constraints from different (x,y) pairs create incompatibilities.

---

## Cheap-kill candidates

- **x = f(y) substitution**: not a kill but immediately yields f(f(y)) = 2f(y) - y with no assumptions. This is the one-line structural reduction.
- **Orbit non-negativity**: f(x) >= x for all x (since h(x) >= 0 by iterate positivity). Quick structural fact.
- **Non-constant h refuted by (R*) at large x**: If h takes two values c < d, the RHS 4xd-4yc ~ 4x(d-c) grows linearly in x while LHS (x+c-y)^2 ~ x^2 when y is far but can be small when y is near f(x) — and the d-orbit DOES have points near f(x) eventually (arithmetic sequences with different steps hit each other's neighborhoods). This is the key structural kill for non-constant h.

---

## Knowledge-base entries to use

- **Standard inequalities: AM-GM, QM-AM** (KB entry "Standard inequalities"): QM(a,b) >= AM(a,b) >= GM(a,b) is the classical chain. The problem is a FUNCTIONAL sandwich around this chain with different argument pairings for the middle term.
- **Functional equations: test special values, check injectivity/surjectivity** (KB entry "Functional equations"): the x=f(y) substitution is exactly "test a special value that collapses an expression."
- **Direct proof** (KB entry "Direct proof"): chain from x=f(y) → f(f(y))=2f(y)-y → h constant on orbits → h constant globally.
- **Induction / infinite descent** (KB entry): the orbit structure f^n(y) = y+nc provides the infinite-iterates positivity argument.
- **Problem-solving heuristics: Specialize** (KB entry "Pólya"): the x=f(y) specialization is the entire key move.

---

## Analogous past problems (cruxes)

**1. aimo-0710** (most analogous): f: R_{>0} -> R_{>0}, functional inequality x(f(x)+f(y)) >= (f(f(x))+y)f(y). Key crux: substitute x=f(y) to get f(y) >= f(f(y)), then use x=y to get f^2(x) <= x; iterate to force f^2 = id; then original inequality collapses to xf(x) = constant giving f(x)=c/x. **Adaptation**: the substitution x=f(y) is the SAME move as in our problem. In our problem, it doesn't give an inequality but an EQUALITY: f(f(y)) = 2f(y)-y. The "iterate to force" step is replaced by an orbit-density argument.

**2. aimo-1022** (partially analogous): f: R+ -> R+, functional equation f(x)=f(f(f(x))+y)+f(x*f(y))*f(x+y). Crux: sandwich iterates between each other (f(x) <= f^3(x) <= f^5(x) and back), forcing an involution f^2=x. **Adaptation**: the technique of "chain iterate inequalities back and forth to force an exact identity" mirrors our derivation of f(f(y))=2f(y)-y. The structure is: both problems use substituting the function's own value as an argument to close a loop.

**3. aimo-0008** (analogous in squeezing mechanism): f: Q_{>0} -> R, superadditive and submultiplicative with f(a)=a for some a>1. Crux: "Convert a one-sided bound into equality by sandwiching against a known exact value, splitting additively and letting the superadditive inequality force each summand tight." **Adaptation**: the "sandwich → equality → propagate" flow is the same structural move. Our problem: once f(f(y))=2f(y)-y is known, we use the original inequality to squeeze the global h to a constant.

---

## Prior progress

None — fresh run, no `results/imo-2026-05/` directory exists.

---

## Dead ends (do not retry)

- Swapping x and y in both L and R and adding/multiplying: always produces tautologies ((x-f(y))^2 + (y-f(x))^2 >= 0 type).
- Setting y=x: always gives QM(x,f(x)) >= AM(x,f(x)) >= GM(x,f(x)) which is tautological.
- Trying to bound f(x) from the y=1 substitution alone: gives weak bounds (linear growth allowed), does not pin h to constant.
- f(x) = x+c*phi(x) for phi != constant: all fail for small x or for cross-orbit constraints; non-constant translation fields are ruled out by (R*).

---

## Small-case / intuition notes (labeled as conjecture)

**Confirmed**: f(x)=x+c for ALL c >= 0 satisfies both inequalities (proved algebraically: both reduce to QM(x,y+c) >= AM(x,y+c) >= GM(x,y+c)).

**Conjectured answer**: f(x) = x+c, c >= 0 are ALL solutions (no others).

**Numerical evidence**: f(x)=2x+1, f(x)=0.5x+0.5, f(x)=x^2, f(x)=sqrt(x), f(x)=x+c*sqrt(x) (c>0), f(x)=x+c*x^2 all FAIL on the test grid {0.001, 0.01, 0.1, ..., 1000} × {same}. Only f(x)=x+c passes.

**Key structural insights** (proved, not just conjectured):
- Substituting x=f(y) gives f(f(y))=2f(y)-y EXACTLY (no inequality).
- This implies f(x) >= x for all x (iterate positivity).
- This means h=f-id is non-negative and constant on arithmetic orbits.
- Two orbits with different h-values c < d: for large x from c-orbit, (R*) requires distance |f(x)-y| >= 2*sqrt(x*(d-c)) growing like sqrt(x), but the d-orbit has elements within fixed distance d of f(x) for arbitrarily large x. Contradiction.

**Trap to flag**: The sandwich only requires (f(x)+y)/2 to lie BETWEEN GM and QM of (x,f(y)), not to equal the AM. Many approaches that just verify "middle lies between the two extremes" miss the KEY POINT that (f(x)+y)/2 for the specific f(x)=x+c becomes exactly AM(x,f(y)), giving a UNIFORM proof. The trap: checking L and R separately at specific substitutions gives tautologies; the constraint binds only across DIFFERENT orbits with different h values.
