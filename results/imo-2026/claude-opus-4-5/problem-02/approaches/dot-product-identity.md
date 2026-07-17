# Approach: Dot Product Identity

**Slug:** dot-product-identity  
**Status:** partial  
**Last outcome:** new

## Target
Prove OM = ON, where O is the circumcenter of triangle AKL, and M, N are midpoints of AB, AC respectively.

## Technique
Direct computation: translate OM = ON to a scalar identity 4(B-C).(O-A) = AB^2 - AC^2 (dot product), then derive this from the angle conditions using the circumcenter equations.

## Skeleton

1. **Reformulate OM = ON as a dot product.** Set O_0 = O - A (circumcenter relative to A). Then:
   - OM = |O_0 - M + A| = |O_0 - (B-A)/2| = |O_0 - b/2|  where b = B - A
   - ON = |O_0 - c/2|  where c = C - A
   
   OM = ON iff |O_0 - b/2|^2 = |O_0 - c/2|^2
   iff O_0 . b - |b|^2/4 = O_0 . c - |c|^2/4
   iff **4(b - c) . O_0 = |b|^2 - |c|^2**
   
   In original coordinates: **4(B - C) . (O - A) = AB^2 - AC^2**

2. **Circumcenter equations.** O_0 is the circumcenter of {0, k, l} where k = K - A, l = L - A. It satisfies:
   - 2 k . O_0 = |k|^2   (perpendicular bisector of 0-k)
   - 2 l . O_0 = |l|^2   (perpendicular bisector of 0-l)
   
   Solve: O_0 = (|k|^2 l_perp + |l|^2 k_perp) / (2 det(k,l)) where det(k,l) = k_x l_y - k_y l_x (cross product).

3. **Substitute into target.** Compute (b - c) . O_0:
   
   4(b - c) . O_0 = 2(b - c) . [solution from step 2]
   
   This is a rational expression in k, l, b, c coordinates.

4. **Encode angle conditions.** The three angle conditions constrain k, l:
   - (C1): angle(KBA) = angle(ACL) = alpha
   - (C2): angle(LBK) = angle(LNC) = beta
   - (C3): angle(LCK) = angle(BMK) = gamma

   In vector form (using "angle between vectors" as arg ratios being real):
   - (C1): (b)(c) / ((k-b)(l-c)) is real (or the arg equality)
   - (C2): involves reflection 2l - c (over N)
   - (C3): involves reflection 2k - b (over M)

5. **Derive the identity.** Use (C1), (C2), (C3) to show 4(b-c).O_0 = |b|^2 - |c|^2.

   Key insight: (C2) and (C3) explicitly involve the midpoints M = b/2 and N = c/2 through the "reflection factors" 2k - b and 2l - c. These are the same factors that would appear if we expressed O_0 . b and O_0 . c separately.

6. **Algebraic verification.** This step requires careful computation:
   - Express O_0 in terms of k, l.
   - Use (C1), (C2), (C3) to relate k, l to b, c.
   - Show the LHS 4(b-c).O_0 equals RHS |b|^2 - |c|^2.

## Key lemmas

- **Target identity:** 4(B-C).(O-A) = AB^2 - AC^2 is equivalent to OM = ON. This is the single scalar equation we must prove.

- **Midpoint factors in conditions:** Conditions (C2) and (C3) involve 2l - c and 2k - b, which encode the midpoint structure. This is the mechanism linking M, N to the circumcenter position.

- **Circumcenter formula:** O_0 = (|k|^2 l^perp + |l|^2 k^perp) / (2 det(k,l)) in terms of k = K-A, l = L-A.

## Open gaps

- **Gap 1 (main):** Carry out the algebraic derivation: substitute the angle conditions into the expression 4(b-c).O_0 and show it equals |b|^2 - |c|^2.

- **Gap 2:** Verify the exact form of the angle conditions as algebraic constraints (the "is real" encoding or equivalent).

## Cases to cover
None (single algebraic identity).

## Watch out for
- The dot product (b-c).O_0 in 2D can be computed via x and y components, or via complex numbers with Re((b-c)*conj(O_0)).
- The circumcenter formula has a determinant in the denominator; need det(k,l) != 0 (i.e., K, L, A not collinear).
- Signs matter: use consistent orientation for the triangle.
