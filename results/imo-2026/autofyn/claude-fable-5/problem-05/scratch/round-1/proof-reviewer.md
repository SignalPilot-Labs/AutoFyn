# Proof review — round 1 — imo-2026-05

Problem: determine all f: R_{>0} -> R_{>0} with sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y)). Task: compute_and_prove, answer_type: characterization — a full solve needs BOTH sufficiency (every claimed f works) and necessity (no others).

Both candidates claim the same answer: f(x) = x + c, c >= 0 constant. I verified this answer is correct.

---

## Verdict: two-point-pinch — APPROVE (Status: solved)

**Scores.** Correctness 10/10, Completeness/rigor 10/10, Progress 10/10 (from nothing to complete).

**Adversarial verification performed:**
- **Load-bearing step re-derived from scratch:** the pinch. Substituting x = f(y') into the right inequality and using f(f(y')) = 2f(y') - y' gives (y+y'+2u)^2 >= 4(y'+u)(y+v) with u=d(y'), v=d(y). I verified symbolically (sympy) the exact identity LHS - RHS = (y-y')^2 + 4(y'+u)(u-v) = (y-y')^2 + 4 f(y')(d(y')-d(y)). Dividing by 4f(y') > 0 and using f(y') >= y' (Step 2) gives d(y) - d(y') <= (y-y')^2/(4y') for ALL pairs — the two-sided pinch (8) follows by swapping roles. Correct.
- **Step 1 (core identity):** at x = f(y) both outer terms of the chain equal f(y) exactly (sqrt(f(y)^2) = f(y) since f(y) > 0), so the middle is squeezed: f(f(y)) = 2f(y) - y. Airtight; well-definedness of f(f(y)) noted.
- **Step 2 (f >= id):** orbit recurrence y_{n+2} = 2y_{n+1} - y_n proved via (1) at y_n (positivity of orbit by induction, Claim A); AP formula by explicit two-step induction; d(y) < 0 refuted by Archimedean choice of n. No gap.
- **Step 4 (subdivision):** telescoping over k equal subintervals of [a,b] gives |d(a)-d(b)| <= (b-a)^2/(4ak); k arbitrary kills it. min(t_i, t_{i+1}) = t_i >= a justified. a = b trivial, a > b by symmetry of |.|.
- **Sufficiency:** both squared slacks equal (x-y-c)^2 — verified by sympy. Codomain argument correctly excludes c < 0.
- **Squaring legality:** stated and checked at every squaring (all quantities positive/nonnegative).
- **Hidden gaps / circularity / case gaps:** none found. The argument is case-free; no crux-move citations; nothing assumed that is being proven.

Builder's recorded Status `solved` is accurate.

---

## Verdict: marching-orbits — APPROVE (Status: solved)

**Scores.** Correctness 10/10, Completeness/rigor 10/10, Progress 10/10. An independent second complete proof.

**Adversarial verification performed:**
- **Lemmas 1–2** identical in content to the other proof's Steps 1–2; verified (see above).
- **Load-bearing step re-derived: Lemma 3 (marching).** Assume p = d(x) < q = d(y). With n chosen so y_n > max(x+p, p^2/(q-p)) and m = ceil((y_n - x)/p): I checked m >= 2 (since y_n - x > p), and the ceiling bounds give y_n <= x_m < y_n + p, so S = x_m - y_n in [0, p). Slack of (R) at (x_m, y_n): Delta = 4y_n(p-q) + (S+p)^2 - 4Sq — verified symbolically (sympy). Then (S+p)^2 < 4p^2 and -4Sq <= 0 give Delta < -4y_n(q-p) + 4p^2 < 0 by the choice y_n > p^2/(q-p). Contradiction with (R) >= 0. The role-swap for q < p is a genuine relabeling. Correct.
- **Dichotomy:** d >= 0 (Lemma 2) + at most one positive value (Lemma 3) gives range(d) in {0, c}; Cases A/B/C exhaustive and disjoint. Correct.
- **Lemma 4 (exclusion zone):** (a+s)^2 - 4a(s+c) = (s-a)^2 - 4ac — verified. |s-a| >= 2 sqrt(ac) for any s with d(s) = c. Correct; uses f(a) = a exactly, available in Case C.
- **Lemma 5 (propagation):** discriminant (a+c)^2 - (a^2 - c^2 - 2ac) = 4ac + 2c^2 — verified; sqrt(4ac+2c^2) > c so the lower root is < a; the half-open interval [a, a+c+sqrt(4ac+2c^2)) sits strictly inside the parabola's negativity region, so d(x) < c there, hence d(x) = 0 by the dichotomy. Corollary 6's induction (a_{k+1} = a_k + c is inside the Lemma-5 interval of a_k) is sound and gives unbounded fixed points.
- **4c constants checked:** a' >= 16c gives 2 sqrt(a'c) <= a'/2, so alpha >= a'/2 >= b + 1/2 > b (using a' >= 2b+1); beta - alpha = 4 sqrt(a'c) >= 16c > c. Least n* with b_{n*} > alpha exists (b_n -> infinity), n* >= 1, and b_{n*} = b_{n*-1} + c <= alpha + c < beta places a d-value-c point inside the exclusion zone — contradiction with Lemma 4. Case C dead.
- **Sufficiency:** same verified identities. Answer verified numerically at sample points as required by answer_type.

Builder's recorded Status `solved` is accurate.

---

## Lemma certification

- `lemmas/core-identity-ap-orbits.md` — **CERTIFIED**. Statement matches exactly what is proved (no overclaim); proof is sorry-free; re-verified in full. Status header updated.
- `lemmas/two-point-pinch-bound.md` — **CERTIFIED and added** (from two-point-pinch's promotable list; the pinch identity was sympy-verified). Its other two promotables (core identity, f >= id) are subsumed by core-identity-ap-orbits, so no separate files.

## current.md

Created `results/imo-2026-05/current.md` with `## Status: solved` and the full proof (two-point-pinch's, the shorter case-free one, as primary; marching-orbits recorded as an independent verified second proof).

---

## Goal Progress

- **Status: SOLVED** (round 1). Answer: f(x) = x + c, c >= 0 constant — both directions of the characterization proven and independently verified; all load-bearing algebra re-checked with sympy.
- **Ranking snapshot:** two-point-pinch Elo 1531.3 (verified-milestone), marching-orbits Elo 1500.0 (verified-milestone), tangent-envelope Elo 1468.7 (unbuilt reserve, now moot).
- **What remains:** nothing on the mathematics. The run's goal is met; no further building needed. Terminal state per the routing rules (APPROVE is terminal).
