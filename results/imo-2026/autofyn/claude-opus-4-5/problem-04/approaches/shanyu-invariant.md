# Approach: Shan-Yu's Winning Strategy via Invariant

## Target
**Shan-Yu wins if theta != 180/n for any integer n >= 2.**

Equivalently: if 180/theta is not a positive integer (including irrational theta and rational theta = 180p/q with p >= 2), then Shan-Yu can maintain a triangle with no angle equal to theta, forever.

## Technique
Invariant method (KB: "Invariants & Monovariants"). Shan-Yu maintains the invariant "no angle of the current triangle is a positive multiple of theta."

## Skeleton

### Step 1: Define the Invariant

Let S_theta = {triangles T : no angle of T is k*theta for any positive integer k}.

Shan-Yu's goal: maintain T in S_theta for all time.

### Step 2: Shan-Yu Can Initialize the Invariant

**Claim:** There exists a triangle with no angle equal to k*theta for any k >= 1.

**Proof sketch:** The set {k*theta : k >= 1} intersect (0, 180) is a discrete subset of (0, 180). Pick angles A, B, C summing to 180 that avoid this discrete set. E.g., for most theta, the equilateral triangle (60, 60, 60) works.

**[GAP 2]:** Need to verify that Shan-Yu can always find such an initial triangle. The issue is: what if theta = 60 (then equilateral fails)? But theta = 60 = 180/3 is excluded by hypothesis. Still need careful verification.

### Step 3: The Invariant is Closed Under Shan-Yu's Choices (Key Lemma)

**Claim:** If 180/theta is not a positive integer, and T in S_theta, then for any cut Mulan makes, at least one of the two resulting sub-triangles is also in S_theta.

**Proof skeleton:**
- Suppose both sub-tris have a multiple of theta as an angle.
- Sub-tri 1 has angle j1*theta; sub-tri 2 has angle j2*theta.
- By the cut mechanics, these angles are "complementary" in the sense that j1*theta + j2*theta must equal 180 (they sum to the vertex angle being cut to, plus the edge sum constraint).
- So (j1 + j2)*theta = 180, meaning 180/theta = j1 + j2, an integer.
- Contradiction with hypothesis 180/theta not in Z.

**[GAP 3]:** The pair-sum argument needs careful verification. Which pairs of angles in the sub-triangles must sum to 180? Need to identify the exact geometric constraint.

### Step 4: Conclusion

By induction on the number of turns:
- Base: Shan-Yu picks T_0 in S_theta.
- Step: After Mulan cuts, at least one sub-tri is in S_theta; Shan-Yu keeps it.

Hence Mulan never wins.

## Key Lemmas

1. **Existence Lemma:** For theta != 180/n, there exists a triangle with no angle equal to any positive multiple of theta. -- Because the multiples form a discrete set, and the space of triangles is 2-dimensional; specifically, can perturb any triangle to avoid finitely many bad angle values.

2. **Invariant Closure Lemma:** If 180/theta is not a positive integer, and T has no angle k*theta, then Mulan cannot force BOTH sub-triangles to have angles that are multiples of theta. -- Because such forcing requires j1*theta + j2*theta = 180 for some integers j1, j2, implying 180/theta = j1 + j2 in Z.

3. **Irrational Theta Lemma:** If theta is irrational, then (j1 + j2)*theta = 180 has no integer solution. -- Because 180 is rational and theta is irrational, so (j1+j2)*theta is irrational for any integer j1+j2 > 0.

## Open Gaps

- **[GAP 2]:** Careful verification that initial triangle avoiding all k*theta exists.
- **[GAP 3]:** Rigorous proof of the pair-sum constraint from cut mechanics.

## Cases to Cover

1. **Irrational theta:** (j1+j2)*theta = 180 has no solution; Shan-Yu wins trivially.
2. **Rational theta = 180p/q with p >= 2:** (j1+j2)*theta = 180 implies j1+j2 = q/p, not an integer for p >= 2.
3. **theta > 90:** Even if theta = 180/n for some n, we have n < 2, so n = 1, but theta < 180 so n > 1, contradiction. Actually theta > 90 means 180/theta < 2. If 180/theta is an integer >= 2, then theta <= 90. So theta > 90 falls under "not 180/n for n >= 2."

## Watch Out For

- The cut mechanics analysis: which specific angles in the sub-triangles are constrained.
- Edge case: theta = 90 is 180/2, so Shan-Yu does NOT win; must exclude correctly.
- The "both sub-tris have multiples" condition: need to pin down which angles we're comparing.
