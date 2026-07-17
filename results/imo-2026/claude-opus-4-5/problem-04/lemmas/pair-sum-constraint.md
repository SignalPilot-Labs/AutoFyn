# Pair-Sum Constraint for Triangle Cutting Games

## Statement

In a triangle T with no angle equal to any positive multiple of theta, if Mulan makes a cut and both resulting sub-triangles have positive multiples of theta as angles, then those multiples must both be at the cut point P, and they sum to 180/theta.

More precisely: if angle_1 = j_1 * theta in T_1 and angle_2 = j_2 * theta in T_2 where both are at the cut point P, then (j_1 + j_2) * theta = 180.

## Proof

Let T have vertices A, B, C with angles alpha, beta, gamma (none is a multiple of theta). Cut from P on BC to A with parameter t = angle BAP.

The angles in T_1 (ABP): beta, t, 180 - t - beta
The angles in T_2 (ACP): gamma, alpha - t, beta + t

Since beta, gamma, alpha are not multiples of theta:
- If T_1's multiple is at A (t = j*theta) and T_2's is at P (beta + t = j_2*theta), then beta = (j_2 - j)*theta, contradiction.
- If T_2's multiple is at A (alpha - t = k*theta) and T_1's is at P (180 - t - beta = j_1*theta), then gamma = (j_1 - k)*theta, contradiction.

Therefore both multiples must be at P: j_1*theta = 180 - t - beta and j_2*theta = beta + t.
Adding: (j_1 + j_2)*theta = 180.

## Corollary

For Mulan to force multiples of theta into both sub-triangles from a "safe" triangle, she needs 180/theta to be an integer >= 2.

## Domain
combinatorics, game theory

## Source
imo-2026-04 (Mulan's Triangle Game)
