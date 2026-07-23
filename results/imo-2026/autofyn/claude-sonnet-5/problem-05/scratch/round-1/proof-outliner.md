## imo-2026-05
Spec review: required
Technique: Direct/constructive characterization proof (both directions). Necessity: forced-equality substitution -> exact functional equation (already proved), then a second substitution into the GM-inequality yielding a quadratic-defect inequality, then a telescoping/Archimedean squeeze over a fine partition to force global constancy of d(x)=f(x)-x. Sufficiency: direct algebraic identity reducing to classical QM-AM-GM (already proved).

Full outline (skeleton, key lemmas with mechanism, cases, and watch-outs) has
been written directly into `results/imo-2026-05.md`, in the new section
"## Proof outline (proof-outliner, round 2)" (inserted between "Current best"
and "Full proof"). See that file for the complete outline; summary below.

Skeleton:
  1. (already proved) FE: f(f(y)) = 2f(y) - y, via substituting x=f(y) into
     the original 3-term chain (re-verified: legitimate direct computation,
     not a misapplied "QM=GM => a=b" claim) — by direct evaluation of QM/GM
     of a repeated value.
  2. (already proved) f(x) >= x for all x, via the orbit y_n = y+n*d(y)
     staying positive for all n >= 0 (from the FE).
  3. (NEW key lemma) Quadratic-defect inequality (E):
     4 f(x) (d(x)-d(y)) + (y-x)^2 >= 0 for all x,y>0 — derived by
     substituting x -> f(x) into the GM-inequality (f(x)+y)^2 >= 4x f(y) and
     eliminating f(f(x)) via the FE. Algebra verified symbolically with
     sympy (exact polynomial identity, diff = 0).
  4. (NEW finishing squeeze) Fix a<b. Partition [a,b] into N pieces of size
     Delta=(b-a)/N. Apply (E) to consecutive pairs both ways; use f(x_i)>=x_i>=a
     (step 2) to bound each local increment by Delta^2/(4a); telescope to get
     |d(b)-d(a)| <= (b-a)^2/(4aN) for every N; let N->infty to force
     d(a)=d(b). Since a<b arbitrary, d is a global constant c>=0.
  5. (already proved) Sufficiency: f(x)=x+c, c>=0, satisfies both
     inequalities since f(x)+y = x+f(y) identically, reducing the chain to
     classical QM-AM-GM for (x, f(y)). c>=0 also forced independently by the
     codomain requirement f(x)>0 for all x>0.
  6. Conclude: solution set is exactly {f(x)=x+c : c>=0}, state explicitly.

Key lemmas (claim + mechanism):
  - FE f(f(y))=2f(y)-y — because x=f(y) makes both outer QM/GM terms of the
    chain literally equal to f(y) (QM/GM of a repeated value), forcing the
    trapped middle term to equal them too.
  - f(x)>=x — because the forward orbit under f is an AP with common
    difference d(y); a negative difference would force eventual negativity,
    contradicting f: R_{>0} -> R_{>0}.
  - (E) 4f(x)(d(x)-d(y))+(y-x)^2>=0 — because x->f(x) substituted into the
    GM-inequality, combined with the FE to kill f(f(x)), turns a product-type
    inequality into a quadratic form in d(x)-d(y).
  - d(a)=d(b) for all a<b — because telescoping (E) over an N-partition of
    [a,b] gives a bound on d(b)-d(a) (and its negative) that is O(1/N) for
    every N, hence forced to 0 by the Archimedean property (a fixed real
    number that is <= a null sequence for every N must be <=0).
  - Sufficiency identity f(x)+y=x+f(y) for f(x)=x+c — because f is an
    additive shift, both sides equal x+y+c identically, collapsing the chain
    to textbook QM-AM-GM.

Cases to cover: none (no casework in x,y; the argument is uniform over all
a<b in R_{>0}; c=0 is just a special case of c>=0, no separate treatment
needed).

Watch out for:
  - Do not conflate lemma (E)'s derivation (x->f(x) in the GM-inequality)
    with the earlier x=f(y) substitution in the original chain (step 1) —
    keep them as clearly separate derivations.
  - (E)'s derivation needs only the FE, not injectivity or the orbit-AP fact
    — don't let the builder waste effort re-deriving those as prerequisites.
  - Sufficiency direction must be written out algebraically (identity
    f(x)+y=x+f(y), named QM-AM-GM theorem, explicit c>=0 domain check), not
    asserted.
  - State the final answer explicitly per CLAUDE.md ("f(x)=x+c for some
    constant c>=0"), with both directions (necessity steps 1-4, sufficiency
    step 5) clearly labeled as proved.
  - x_i ranges over [a,b] subset of R_{>0} with a>0 strictly, so f(x_i)>=x_i>=a>0
    is always a valid, nonzero denominator in the telescoping bounds.
