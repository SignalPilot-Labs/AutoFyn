## imo-2026-05

Prior workspace: none existed (first round). Opened `results/imo-2026-05/approaches/`
with 4 new approaches, all sharing the rigorously-derived background
(f(f(y))=2f(y)-y via the equality-forcing substitution x=f(y); f(y)>=y via the
orbit/arithmetic-progression positivity argument; injectivity) but diverging in the
*mechanism* used to close the single shared gap all three explorers flagged: proving
S(x):=f(x)-x is a GLOBAL constant (not just constant along each f-orbit). Target
answer for every approach: **f(x) = x + c for every constant c >= 0** (NOT f=identity
alone — verified algebraically by all three explorers and rechecked here: for
f(x)=x+c, both squared inequalities reduce to the identity (x-y-c)^2 >= 0).

quadratic-difference-chaining: new
Target: all f: R_{>0}->R_{>0} solving the sandwich; claim {f(x)=x+c : c>=0}.
Technique: derive a genuinely new two-variable, non-orbit inequality by substituting
X=f(x) (not X=x) into the GM-side inequality and using the exact identity
f(f(x))=2f(x)-x, producing
  -(x-y)^2/(4f(x)) <= S(x)-S(y) <= (x-y)^2/(4f(y))   for ALL x,y>0     (KEY),
then an n-fold subdivision/telescoping argument (classical "O(Δ^2)-difference forces
constant" lemma) to promote (KEY) to global constancy of S.
Skeleton:
  1. Square the sandwich into (A) 2x^2+2f(y)^2>=(f(x)+y)^2 and (B) (f(x)+y)^2>=4xf(y).
  2. x=f(y) collapses QM=GM ⟹ f(f(y))=2f(y)-y exactly (equality case of KB
     "Standard inequalities... equality cases pin down the extremal configuration").
  3. Orbit y_n=f^n(y) is an exact AP with common difference S(y); positivity of all
     iterates forces S(y)>=0.
  4. f(a)=f(b) ⟹ 2f(a)-a=2f(b)-b ⟹ a=b (injectivity).
  5. Plug X=f(x) into (B), use f(f(x))=2f(x)-x, expand — derive (KEY) (hand-verified
     twice, algebra: (x+y+2S(x))^2>=4f(x)f(y) ⟹ (x-y)^2+4f(x)(S(x)-S(y))>=0; swap
     x,y for the companion bound).
  6. Subdivide [min(x,y),max(x,y)] into n pieces, apply (KEY) to each consecutive
     pair (f(t_i)>=t_i>=min(x,y)>0 throughout by step 3), telescope: |S(x)-S(y)| <=
     (y-x)^2/(4·min(x,y)·n) -> 0 as n->infinity. Hence S is globally constant = c>=0.
  7. Sufficiency: f(x)=x+c gives (A),(B) as the identity (x-y-c)^2>=0 for both.
Key lemmas: f(f(y))=2f(y)-y (equality-forcing substitution); f(y)>=y (AP positivity);
(KEY) two-sided quadratic bound (X=f(x) substitution + the exact identity, giving a
non-orbit, all-pairs estimate — this is the genuinely new move, distinct from what any
explorer already tried); S constant (n-fold subdivision/telescoping, KB "telescoping").
Open gaps: full line-by-line algebra of step 5 and full epsilon/n rigor of step 6 are
the builder's job (mechanism and answer are pinned down; execution remains).
Cases to cover: none (single continuum family, both directions covered).
Watch out for: don't present f=identity alone as the answer; state the c>=0 domain
constraint explicitly (c<0 breaks codomain R_{>0}).

monotonicity-first: new
Target: same as above.
Technique: prove f strictly increasing directly from the two-variable inequality
(order-theoretic, not an equality substitution or a quadratic estimate), then use
order-preservation of the AP-orbits from f(f(y))=2f(y)-y to compare *different*
orbits (not just bound one orbit's positivity) and force S monotone, then constant.
Skeleton: shared background (steps 1-4 as above) + (2) f increasing via comparing
(A)/(B) at special values y=x1,y=x2 for candidate x1<x2 with f(x1)>=f(x2) assumed,
deriving a contradiction (open — builder must complete the special-value chase);
(3) order-preservation of two AP-orbits started at x<y forces n(S(x)-S(y)) < y-x for
all n, so as n->infinity, S(x)<=S(y) (S weakly non-decreasing); (4) OPEN: a second,
independent argument for the reverse inequality (S non-increasing) is needed to
finish — candidates listed (reflect the argument, or re-run it on inequality (A)
instead of (B)); if none found, cross-cite quadratic-difference-chaining's (KEY).
Key lemmas: f strictly increasing (special-value comparison, open); S non-decreasing
(two-orbit order-preservation + telescoping-to-infinity, proven modulo step 2); S
non-increasing (open, the harder direction).
Open gaps: step 2 (monotonicity itself) and step 4 (the reverse direction) are both
unproved — flag as RETHINK if step 2 doesn't close quickly.
Cases to cover: none.
Watch out for: do not assume monotonicity without proving it; state the induction
justification for "order-preserving map preserves orbit order" explicitly.

cauchy-boundedness: new
Target: same as above.
Technique: recast S as an (approximately) additive Cauchy-type function and invoke
the classical rigidity theorem "additive + bounded-below (or monotone) ⟹ linear,"
then use S>=0 everywhere to force the linear coefficient to 0, i.e. S constant.
Skeleton: shared background + attempt to extract an exact/approximate additive
relation S(y+t)-S(y) = phi(t) independent of y from a direct x=y+t substitution into
(A)/(B), or by reinterpreting quadratic-difference-chaining's (KEY) bound in the
h->0 limit (heuristically S'(x)=0 everywhere, though this needs a non-smooth
epsilon-delta upgrade to be rigorous); if additivity is real, invoke the standard
Cauchy-equation boundedness theorem to finish.
Key lemmas: additive relation for S (OPEN, largest gap — may not exist cleanly since
(KEY) is quadratic not linear in (x-y)); boundedness-forces-linear rigidity theorem
(standard, once additivity is established).
Open gaps: the core additive extraction (step 2) is unproven and may not be the right
structural fit at all; builder should attempt one focused pass then mark
RETHINK/merge into quadratic-difference-chaining if it doesn't yield quickly — this is
the weakest/most speculative of the four approaches, kept for diversity per the
plateau-breaking rule, not because it is currently the most promising route.
Cases to cover: none.
Watch out for: don't fake rigor by assuming differentiability of S to get S'=0 — that
is illustrative only, not a valid final proof step.

extremal-supinf: new
Target: same as above.
Technique: extremal principle (KB "Pigeonhole / extremal principle") — take the
sup/inf of S over a shrinking interval around a point, use the (KEY) bound to force
the local sup and inf together as the interval diameter -> 0, giving local constancy,
then use connectedness of R_{>0} to promote to global constancy.
Skeleton: shared background + import/re-derive (KEY); take near-inf and near-sup
sequences within a shrinking interval I_k=[x-1/k,x+1/k]; (KEY) forces
diam(I_k)^2 -> 0 to squeeze sup_{I_k}S - inf_{I_k}S -> 0, giving S locally constant
at every x; connectedness of R_{>0} (interval) then forces S globally constant.
Key lemmas: (KEY) (imported/re-derived); local constancy via shrinking-interval
squeeze (open, needs careful epsilon/k rigor); global constancy from local constancy
(standard connectedness fact).
Open gaps: step 3's shrinking-interval argument is sketched, not completed; likely to
converge to a more complicated restatement of quadratic-difference-chaining's direct
subdivision — builder should mark RETHINK and consolidate if so, rather than force a
weaker duplicate.
Cases to cover: none.
Watch out for: infimum/supremum need not be attained — argue via sequences, not
minimizers; don't conflate local constancy with mere continuity.

---

Recommendation for build set: quadratic-difference-chaining is the strongest/most
complete approach (the (KEY) lemma and the subdivision finish are both fully derived
in outline form, hand-verified algebra) and should be built first/primarily. The other
three (monotonicity-first, cauchy-boundedness, extremal-supinf) are put up per
CLAUDE.md's diversity/plateau-breaking rule — they attack the same shared gap (global
constancy of S) via genuinely different mechanisms (order theory, Cauchy rigidity,
extremal principle) rather than 3 near-identical orbit-based approaches, satisfying
the dispatch instruction to diversify. If the outline-reviewer's build-set budget is
limited, prioritize quadratic-difference-chaining, then monotonicity-first (its
one-sided S non-decreasing result is real progress even if step 4 stays open), and
treat cauchy-boundedness / extremal-supinf as lower-priority / likely-to-merge.
