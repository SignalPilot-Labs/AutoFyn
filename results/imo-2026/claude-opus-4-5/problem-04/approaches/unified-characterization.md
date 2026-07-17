# Approach: Unified Characterization

## Status
solved

## Target
**Complete characterization: Mulan wins if and only if theta = 180/n for some integer n >= 2.**

## Approaches tried
- Unified characterization via pair-sum constraint and cascade strategy -- worked; full proof below.

## Current best
Complete proof of the characterization.

## Full Proof

**Theorem.** Mulan can guarantee victory in finitely many steps if and only if theta = 180/n for some integer n >= 2.

We prove both directions.

---

### Preliminaries: Cut Mechanics

**Setup.** Let triangle T have vertices A, B, C with angles alpha = angle CAB, beta = angle ABC, gamma = angle BCA, where alpha + beta + gamma = 180. Mulan chooses a point P on edge BC (strictly between B and C) and cuts from P to vertex A. This produces two sub-triangles:

- T_1 = triangle ABP with vertices A, B, P
- T_2 = triangle ACP with vertices A, C, P

**Angle analysis.** Let t = angle BAP (the portion of angle alpha that goes to T_1). Since P lies strictly between B and C on edge BC, we have t in (0, alpha). The angles of the sub-triangles are:

For T_1 (triangle ABP):
- Angle at A: t
- Angle at B: beta (unchanged from T)
- Angle at P: 180 - t - beta

For T_2 (triangle ACP):
- Angle at A: alpha - t
- Angle at C: gamma (unchanged from T)
- Angle at P: 180 - (alpha - t) - gamma = 180 - alpha + t - gamma = beta + t (using alpha + beta + gamma = 180)

**Key observation.** The angles at P in T_1 and T_2 are:
- In T_1: angle_1 = 180 - t - beta
- In T_2: angle_2 = beta + t

Adding these: angle_1 + angle_2 = (180 - t - beta) + (beta + t) = 180.

**Lemma (Supplementary Angles at Cut Point).** The two angles created at P (one in each sub-triangle) sum to exactly 180 degrees.

*Proof.* This follows from the fact that P lies on line segment BC. The angles angle APB (in T_1) and angle APC (in T_2) are supplementary since B, P, C are collinear. Explicitly: angle APB + angle APC = 180. Done.

---

### Part A: Necessity (If 180/theta is not an integer >= 2, Shan-Yu wins)

**Definition.** For theta in (0, 180), define the "safe set":
S_theta = {triangles T : no angle of T equals k*theta for any positive integer k}

**Lemma A1 (Pair-Sum Constraint).** Suppose Mulan makes a cut that produces sub-triangles T_1 and T_2. If T_1 has an angle equal to j_1*theta and T_2 has an angle equal to j_2*theta, where both j_1, j_2 are positive integers and these angles are the "new" angles created at the cut point P, then:

j_1*theta + j_2*theta = 180, i.e., (j_1 + j_2)*theta = 180.

*Proof.* From the cut mechanics, the only "new" angles are those at P. The angles at the original vertices A, B, C either remain unchanged (B in T_1, C in T_2) or are portions of alpha (namely t in T_1 and alpha-t in T_2). 

For Mulan to force multiples of theta into BOTH sub-triangles, she must either:
(a) Create them at the cut point P in both triangles, OR
(b) Have some original angle already be a multiple of theta, OR
(c) Choose t such that t or alpha-t is a multiple of theta.

Suppose the original triangle T is in S_theta (no angle is a multiple of theta). Then (b) is ruled out. For (c), Mulan controls t, but she can make at most ONE of {t, alpha-t} a multiple of theta -- if t = j*theta, then alpha - t = alpha - j*theta, which is a multiple of theta only if alpha itself is a multiple of theta, contradicting T in S_theta.

Therefore, to force multiples into BOTH sub-triangles from T in S_theta, Mulan must create them at the cut point P. The angle at P in T_1 is angle_1 = 180 - t - beta, and in T_2 is angle_2 = beta + t. If angle_1 = j_1*theta and angle_2 = j_2*theta for positive integers j_1, j_2, then by the Supplementary Angles Lemma:

j_1*theta + j_2*theta = angle_1 + angle_2 = 180.

Therefore (j_1 + j_2)*theta = 180. Done.

**Lemma A2 (Integrality Obstruction).** The equation (j_1 + j_2)*theta = 180 has a solution in positive integers j_1, j_2 if and only if 180/theta is an integer >= 2.

*Proof.* 
(=>) If j_1, j_2 >= 1 satisfy (j_1 + j_2)*theta = 180, then 180/theta = j_1 + j_2 >= 2.

(<=) If 180/theta = n for some integer n >= 2, then j_1 = 1, j_2 = n - 1 satisfy (j_1 + j_2)*theta = n*theta = 180, and both are positive integers since n >= 2 implies n - 1 >= 1.

Done.

**Lemma A3 (Safe Set Existence).** For any theta such that 180/theta is not an integer >= 2, the safe set S_theta is non-empty.

*Proof.* The "bad" angles are {k*theta : k >= 1, k*theta < 180}. This is a finite set (since theta > 0, there are at most floor(180/theta) such values). Call this set B_theta.

A triangle is determined by its angles (alpha, beta, gamma) with alpha, beta, gamma > 0 and alpha + beta + gamma = 180. The space of triangles (up to similarity) is a 2-dimensional simplex.

For the triangle to have an angle in B_theta, one of alpha, beta, gamma must equal some b in B_theta. This constrains the triangle to lie on one of finitely many 1-dimensional slices of the 2-simplex.

Since the 2-simplex is a 2-dimensional manifold and the union of finitely many 1-dimensional slices has measure zero (and is a proper closed subset), there exist triangles avoiding all of B_theta. Thus S_theta is non-empty.

More explicitly: if B_theta = {b_1, ..., b_m}, choose alpha small enough that alpha is not in B_theta and alpha < min(b_i) (possible since B_theta is finite and bounded away from 0). Then choose beta = gamma = (180 - alpha)/2. We only need beta not in B_theta; since B_theta is finite and beta can be adjusted continuously, we can ensure this.

Done.

**Theorem A (Shan-Yu Wins When 180/theta not in Z_{>=2}).** If 180/theta is not an integer >= 2, then Shan-Yu has a winning strategy.

*Proof.* Shan-Yu's strategy:

1. *Initialization:* Choose any triangle T_0 in S_theta. By Lemma A3, such a triangle exists.

2. *Maintenance:* At each turn, suppose the current triangle T is in S_theta (no angle is a multiple of theta). Mulan makes a cut, producing T_1 and T_2. We claim at least one of T_1, T_2 is in S_theta.

   *Proof of claim:* Suppose for contradiction both T_1 and T_2 have angles that are positive multiples of theta. By Lemma A1, if the multiples are at the cut points, then (j_1 + j_2)*theta = 180 for some positive integers j_1, j_2. By Lemma A2, this requires 180/theta in Z_{>=2}, contradicting our assumption.
   
   If one of the multiples is NOT at the cut point, it must be at an original vertex. But the angles at original vertices in T_1 and T_2 are: beta, t, (alpha-t), gamma. Since T in S_theta, we have beta, gamma not multiples of theta. And if t = j*theta, then alpha - t = alpha - j*theta is a multiple of theta only if alpha is, contradicting T in S_theta. So at most one of t, alpha-t can be a multiple of theta. This means at most one sub-triangle can have a multiple of theta at the A-vertex. The other sub-triangle must get its multiple at the cut point P, but then both would need cut-point multiples, returning to the previous case.
   
   Therefore, at least one sub-triangle is in S_theta.

3. Shan-Yu keeps the sub-triangle in S_theta. By induction, the current triangle is always in S_theta.

4. Since every triangle in S_theta has no angle equal to theta, Mulan never wins.

Done.

---

### Part B: Sufficiency (If theta = 180/n for integer n >= 2, Mulan wins)

Fix theta = 180/n for some integer n >= 2.

**Special Case: n = 2 (theta = 90 degrees)**

**Theorem B0 (Instant Win for theta = 90).** If theta = 90, Mulan wins in one move from any starting triangle.

*Proof.* Let the triangle have angles alpha, beta, gamma. Consider cutting from P on edge BC to vertex A with parameter t = 90 - beta.

We need t in (0, alpha). Since alpha + beta + gamma = 180 and all angles positive:
- t > 0 iff 90 > beta iff beta < 90.
- t < alpha iff 90 - beta < alpha iff 90 < alpha + beta iff gamma < 90.

If beta >= 90, then beta is the largest angle. Relabel so beta < 90; i.e., cut from the edge opposite a non-obtuse angle to a vertex with angle < 90. Such a configuration always exists: if the triangle has an obtuse angle, cut to that vertex (the parameter t needed is 90 - beta where beta < 90 is another angle). If the triangle is acute, any vertex works.

More carefully: among the three angles, at most one is >= 90 (since they sum to 180). So at least two angles are < 90. Pick one of these as beta; the opposite edge contains P. Then beta < 90 so t = 90 - beta > 0. For t < alpha: since alpha + beta + gamma = 180, we have alpha > 90 - beta iff alpha + beta > 90 iff gamma < 90. If gamma >= 90, then gamma is obtuse, so alpha, beta < 90. In this case, cut to vertex C (the obtuse angle) instead.

Concretely: let C be the vertex with the largest angle gamma.
- If gamma < 90 (acute triangle): cut with P on BC, to vertex A. Set t = 90 - beta. Since gamma < 90, we have alpha + beta > 90, so t = 90 - beta < alpha. And beta < 90 since all angles < 90, so t > 0.
- If gamma >= 90 (obtuse or right at C): cut with P on edge AB (opposite C) to vertex C. Let t = angle PCA. Set t = 90 - alpha. Then t > 0 iff alpha < 90 (true since gamma >= 90 implies alpha < 90). And t < gamma iff 90 - alpha < gamma iff 90 < alpha + gamma iff beta < 90 (true since gamma >= 90).

In either case, with the appropriate cut, the angle at P in T_1 is 180 - beta - t = 180 - beta - (90 - beta) = 90, and the angle at P in T_2 is beta + t = beta + (90 - beta) = 90.

Both sub-triangles have a 90-degree angle. Mulan wins.

Done.

**General Case: n >= 3 (theta = 180/n with n >= 3)**

Mulan's strategy proceeds in two phases.

**Phase 1: Force a multiple of theta into the current triangle.**

**Lemma B1 (Phase 1 Forcing).** For any triangle T with angles alpha, beta, gamma (all positive, sum 180), if theta = 180/n with n >= 3, Mulan can make a cut such that both resulting sub-triangles contain positive multiples of theta as angles.

*Proof.* Mulan cuts from P on edge BC to vertex A with parameter t. The angle at P in T_2 is angle_2 = beta + t. Mulan wants angle_2 = j*theta for some j in {1, 2, ..., n-1}, i.e., beta + t = j*theta, so t = j*theta - beta.

For t to be valid, we need t in (0, alpha):
- t > 0: j*theta > beta, i.e., j > beta/theta = n*beta/180.
- t < alpha: j*theta - beta < alpha, i.e., j*theta < alpha + beta = 180 - gamma, so j < n - n*gamma/180 = n*(180 - gamma)/180.

So j must satisfy:
n*beta/180 < j < n*(180 - gamma)/180.

The length of this interval is:
n*(180 - gamma)/180 - n*beta/180 = n*(180 - gamma - beta)/180 = n*alpha/180.

For an integer j to exist in the interval, we need the interval length > 1, i.e., n*alpha/180 > 1, equivalently alpha > 180/n = theta.

**Case 1:** If alpha > theta, the interval (n*beta/180, n*(180-gamma)/180) has length n*alpha/180 > 1, so it contains at least one integer j in {1, ..., n-1}. (The bounds are strictly between 0 and n since beta > 0 and gamma > 0.)

**Case 2:** If alpha <= theta for all angles of T, i.e., max(alpha, beta, gamma) <= theta = 180/n, then alpha + beta + gamma <= 3*(180/n). For this to equal 180, we need 3*(180/n) >= 180, i.e., n <= 3. Since n >= 3, this is only possible when n = 3 and alpha = beta = gamma = 60 = theta. But then T already has angle = theta, so Mulan has already won (game stops before Mulan's move).

Therefore, if Mulan has not yet won, some angle of T exceeds theta. Mulan relabels the triangle so that alpha > theta and applies Case 1.

With j chosen, set t = j*theta - beta. Then:
- Angle at P in T_2 = beta + t = j*theta.
- Angle at P in T_1 = 180 - beta - t = 180 - j*theta = (n - j)*theta.

Since j in {1, ..., n-1}, we have n - j in {1, ..., n-1}, so both are positive multiples of theta.

Done.

**Corollary.** After Phase 1, no matter which sub-triangle Shan-Yu keeps, it contains a positive multiple of theta as an angle. Moreover, this multiple is at the vertex P, which becomes a vertex of the kept sub-triangle.

**Phase 2: Cascade down to 2*theta.**

**Definition.** Say a triangle T has "multiple m*theta at vertex V" if the angle at V equals m*theta for some positive integer m.

**Lemma B2 (Multiple at Vertex After Phase 1).** After Phase 1, the kept sub-triangle has a multiple of theta at vertex P.

*Proof.* In Phase 1, we showed both T_1 and T_2 have multiples of theta at the cut point P. In T_1, P is a vertex with angle (n-j)*theta. In T_2, P is a vertex with angle j*theta. Whichever Shan-Yu keeps, the multiple of theta is at vertex P.

Done.

**Lemma B3 (Bisection Forcing).** Suppose T has angle 2^k * theta at vertex A for some k >= 1 (where 2^k * theta < 180). Then Mulan can cut so that both sub-triangles have angle 2^{k-1} * theta at a vertex.

*Proof.* Mulan cuts from P on edge BC to vertex A with parameter t = 2^{k-1} * theta (half of the angle at A).

For t in (0, alpha), we need 0 < 2^{k-1} * theta < 2^k * theta = alpha, which is satisfied since 2^{k-1} < 2^k.

The angles in the sub-triangles:
- T_1 has angle t = 2^{k-1} * theta at vertex A.
- T_2 has angle alpha - t = 2^k * theta - 2^{k-1} * theta = 2^{k-1} * theta at vertex A.

Both sub-triangles have 2^{k-1} * theta at vertex A.

Done.

**Lemma B4 (Terminal Win).** If T has angle 2*theta at vertex A, Mulan wins in one more move.

*Proof.* Mulan cuts with t = theta. Then:
- T_1 has angle t = theta at vertex A.
- T_2 has angle alpha - t = 2*theta - theta = theta at vertex A.

Both sub-triangles have angle theta. Mulan wins.

Done.

**Lemma B5 (Cascade Termination).** Starting from any multiple m*theta at a vertex, Mulan can reach 2*theta in finitely many steps.

*Proof.* We track the exponent. Write the current multiple as 2^a * b * theta where b is odd.

*Case 1:* b = 1, so the angle is 2^a * theta for some a >= 1.
- If a = 1, we're done (angle is 2*theta, apply Lemma B4).
- If a >= 2, apply Lemma B3 to get 2^{a-1} * theta at a vertex. Repeat until a = 1.

*Case 2:* b >= 3 is odd.
- The angle is 2^a * b * theta. We need to reduce this to a power of 2 times theta.
- Mulan uses a different strategy: cut with t = 2^a * theta. Then T_1 has angle 2^a * theta at A, and T_2 has angle (2^a * b - 2^a) * theta = 2^a * (b-1) * theta at A.
- Since b is odd, b - 1 is even. Write b - 1 = 2^c * d where d is odd. Then T_2's angle is 2^{a+c} * d * theta.
- If d = 1, T_2 has angle 2^{a+c} * theta (a power of 2).
- Either way, at least one sub-triangle has a "cleaner" multiple.

More systematically, define the "level" of m*theta as the largest power of 2 dividing m (i.e., the 2-adic valuation v_2(m)).

When Mulan bisects angle m*theta (setting t = (m/2)*theta if m is even, or t = some divisor times theta if m is odd), she creates angles at vertex A in the sub-triangles. 

For simplicity, observe that Mulan can always make progress by the following:
- If the current multiple m is even, bisect to get m/2 in both sub-triangles.
- If m is odd and m >= 3, cut with t = theta to get sub-triangles with angle theta (in T_1) and (m-1)*theta (in T_2). The angle theta means T_1 wins immediately! And if Shan-Yu keeps T_2, the multiple is m-1, which is even.

Therefore:
- From any multiple m*theta, if m is odd, Mulan can either win immediately (if m = 1, the game has already stopped) or force the kept triangle to have (m-1)*theta or theta at a vertex.
- From even m, Mulan bisects to get m/2 at a vertex.

Since m/2 < m and m - 1 < m, and Mulan wins when the angle equals theta, this process terminates.

More explicitly: Let m_0 be the initial multiple after Phase 1. We have m_0 in {1, 2, ..., n-1}.
- If m_0 = 1, Mulan has already won.
- If m_0 >= 2 and even, Mulan bisects; the new multiple is m_0/2.
- If m_0 >= 3 and odd, Mulan cuts with t = theta. T_1 has theta (win!), T_2 has (m_0 - 1)*theta. If Shan-Yu keeps T_2, the new multiple is m_0 - 1 (even).

At each step, the multiple either:
- Becomes 1 (Mulan wins), or
- Decreases (by at least 1 if odd, or halves if even).

Since the multiple is a positive integer that decreases, Mulan wins in at most O(m_0) <= O(n) additional steps.

Done.

**Theorem B (Mulan Wins When theta = 180/n for n >= 2).** If theta = 180/n for some integer n >= 2, Mulan can guarantee victory in finitely many steps.

*Proof.* 
- If n = 2 (theta = 90), apply Theorem B0: Mulan wins in one move.
- If n >= 3: Apply Phase 1 (Lemma B1) to force a multiple of theta at a vertex. Then apply the cascade (Lemma B5) to reach theta. By Lemmas B2-B5, each step maintains control and the process terminates.

The total number of moves is at most 1 (Phase 1) + O(n) (cascade) = O(n), which is finite.

Done.

---

### Conclusion

Combining Theorems A and B:

**Main Theorem.** Mulan can guarantee victory in finitely many steps if and only if theta = 180/n for some integer n >= 2.

Equivalently, the winning values of theta are: 90, 60, 45, 36, 30, 180/7, 22.5, 20, 18, ... degrees -- precisely the angles of the form 180/n for integers n >= 2.

---

## Promotable lemmas

**Lemma: Supplementary Angles at Cut Point**
*Statement:* When a point P on edge BC of triangle ABC is connected to vertex A, the two angles at P (one in triangle ABP, one in triangle ACP) sum to exactly 180 degrees.
*Proof location:* Preliminaries section.

**Lemma: Pair-Sum Constraint**
*Statement:* If a triangle in the safe set is cut and both sub-triangles have positive multiples of theta at the cut point P, then those multiples sum to 180/theta.
*Proof location:* Lemma A1.
