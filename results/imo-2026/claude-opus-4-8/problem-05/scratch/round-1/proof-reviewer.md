# Proof review — round 1 — imo-2026-05

Problem: find all f: R_{>0} -> R_{>0} with sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y)).
Claimed answer (both approaches): exactly f(x) = x + c, c >= 0.

I independently re-derived every load-bearing algebraic step with sympy (sufficiency SOS, the pinch,
the upper-modulus rearrangement (2f+p)^2/(4f) - (f+p) = p^2/(4f), the lower-modulus identity
(2f+p)^2/2 - f^2 = (f+p)^2 - p^2/2, and the rationalization sqrt(A^2-p^2/2) - A). All returned 0.

---

## Approach: modulus-telescope  —  VERDICT: APPROVE (Status: solved)

Scores: Correctness 10/10, Completeness/rigor 10/10, Progress: full solve.

- **Sufficiency (Part I):** correct. Both slacks equal (x - f(y))^2 >= 0; verified symbolically.
  Answer stated and checked by substitution as required.
- **Step 1 pinch:** correct. x = f(y) collapses (L) and (R) to equalities; both sides positive so the
  square root is legitimate. f(f(y)) = 2 f(y) - y.
- **Step 2 orbit + h>=0:** correct. h(f(y))=h(y), induction gives f^n(z)=z+n h(z), and negativity of
  h forces iterates negative — contradiction with codomain R_{>0}. Clean.
- **Step 3 upper modulus:** correct and non-circular (uses only (R) + Step 1). Valid for all p>-t.
- **Step 4 symmetrization:** correct. Applying Step 3 at both (b,a-b) and (a,b-a) bounds BOTH signed
  differences above; whichever is nonnegative is |h(a)-h(b)|, and f>=id lifts min(f) to min(a,b).
  Note the two-sided modulus comes purely from the RIGHT inequality — the left is not even needed.
- **Step 5 telescoping limit:** correct and the crux is genuinely gap-free. On [t0,t0+L] the uniform
  partition has min(t_{i+1},t_i)=t_i>=t0, so each term <= (L/N)^2/(4 t0); the N-term sum is
  L^2/(4 t0 N) -> 0. No continuity or differentiability is assumed — the modulus bound supplies it.
  This is a standard, airtight "quadratic modulus => constant" argument.

No hidden gaps, no skipped cases, no smuggled differentiability. The builder's recorded Status
`solved` is correct.

## Approach: two-sided-orbit  —  VERDICT: APPROVE (Status: solved)

Scores: Correctness 10/10, Completeness/rigor 10/10, Progress: full solve (independent finish).

- Shares the (correct) prefix Steps 1-3 with modulus-telescope.
- **Step 4 upper modulus (from R):** correct, = the other approach's bound.
- **Step 5 lower modulus (from L):** correct. (L) at x=f(t), y=t+p gives
  f(t+p)^2 >= (f(t)+p)^2 - p^2/2 (verified); square root legal since RHS>0 (A>=p); rationalizing gives
  h(t+p)-h(t) >= -p^2/(2(f(t)+p)). Valid.
- **Step 6 two-sided control:** correct; |h(b)-h(a)| <= (b-a)^2/(2 min(a,b)). Each side uses only one
  of (L),(R); no illegitimate combining.
- **Step 7 finish:** correct.
  - (6) => h continuous (RHS->0 as b->a). Valid.
  - Interleaving Lemma: for h(a)=c1>0, h(b)=c2>0, orbit points a_n=a+n c1, b_m=b+m c2 carry constant
    h-values; choosing m=floor((a_n-b)/c2) gives 0<=a_n-b_m<c2 and min=b_m>=a+n c1-c2->infinity, so
    |c1-c2| <= c2^2/(2 b_m) -> 0, forcing c1=c2. Checked the floor/interleave bookkeeping: correct.
  - Case split S_+ empty (c=0) vs nonempty: continuity + IVT rules out a zero coexisting with a
    positive value (would force an intermediate value c0/2 not in {0,c0}). The previously flagged
    c1=0 sub-case is genuinely closed here. Valid.

Both one-sided bounds and the interleaving/IVT finish are gap-free. Recorded Status `solved` correct.
Note: the two-sided modulus alone already forces h constant via the same telescope as the sibling, so
this finish is a valid (if longer) independent route; the LEFT-inequality lower bound is an honest
alternative rather than a necessity.

---

## Cross-check on the answer
The answer f(x)=x+c, c>=0 is stated explicitly and verified by substitution in both (both slacks
= (x-f(y))^2). Necessity forces exactly this family; c<0 excluded by h>=0. "Find all" has both the
bound (Part II) and the construction (Part I). Complete.

## Outcomes recorded (approach-ranker)
- modulus-telescope: verified-milestone
- two-sided-orbit: verified-milestone
- modulus-derivative: not built this round (record left untouched)

## Lemmas certified (results/imo-2026-05/lemmas/)
- pinch-identity.md, orbit-nonnegativity.md, quadratic-modulus.md (with rigidity corollary).
All hold to the full bar: sorry-free, statements no stronger than proved.

## current.md
Written with Status `solved` and the Full proof (modulus-telescope route, the cleaner finish).
