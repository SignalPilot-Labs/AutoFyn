# Approach: Sigma Symmetry + Isoceles Reduction

**Slug:** sigma-symmetry  
**Status:** partial  
**Last outcome:** new

## Target
Prove OM = ON, where O is the circumcenter of triangle AKL, and M, N are midpoints of AB, AC respectively.

## Technique
Exploit the sigma-symmetry (swap B <-> C, K <-> L, M <-> N) that leaves triangle AKL invariant. Reduce the general case to the isoceles case via a deformation or normalization argument.

## Skeleton

1. **Define the sigma involution.** sigma: (A, B, C, K, L, M, N) -> (A, C, B, L, K, N, M). Under sigma:
   - Condition (C1) angle(KBA) = angle(ACL) is self-conjugate (swaps to itself).
   - Conditions (C2) and (C3) swap with each other.
   - Triangle AKL maps to triangle ALK -- the SAME triangle, so O is fixed.
   - M <-> N under sigma.

2. **Isoceles case is trivial.** When AB = AC, sigma is the reflection over the perpendicular bisector of BC (which is also the perpendicular bisector of MN, passing through A). This reflection fixes O and swaps M, N, so OM = ON immediately.

3. **General case reduction.** For general ABC, sigma is NOT a geometric isometry. However:
   - The perpendicular bisector of MN is parallel to BC (since M, N are midpoints).
   - The angle conditions are sigma-self-conjugate as a system.
   
   Consider a continuous deformation from isoceles (AB = AC) to general ABC. The identity OM = ON is:
   - A polynomial identity in the coordinates.
   - Holds at AB = AC.
   - The angle conditions define a smooth family of (K, L) pairs.

4. **Use algebraic continuity / identity principle.** The function f(ABC, K, L) = |OM|^2 - |ON|^2 restricted to the constraint manifold (the locus of valid (K, L) satisfying conditions) is a polynomial / rational function. If it vanishes on the isoceles subfamily (a Zariski-dense set within a certain parametrization), it vanishes identically.

5. **Alternatively: direct sigma argument.** For each valid configuration (A, B, C, K, L), the sigma-conjugate (A, C, B, L, K) is also valid. Both give the same O. Compute:
   - OM in original = ON in sigma-image
   - ON in original = OM in sigma-image
   
   If we can show the sigma-image has the same M, N distances (appropriately identified), we get OM = ON.

## Key lemmas

- **Sigma fixes O:** Triangle AKL = triangle ALK, so the circumcenter is the same.

- **Sigma swaps M and N:** M = (A+B)/2 maps to (A+C)/2 = N.

- **Isoceles case:** When AB = AC, sigma is a reflection isometry, forcing OM = ON.

- **Continuity argument (if used):** The constraint manifold (valid K, L) is connected, and OM = ON holds on a dense subset (isoceles limits).

## Open gaps

- **Gap 1:** Make the "continuity / identity principle" argument rigorous. Either:
  (a) Show the constraint manifold is irreducible and the isoceles locus is dense.
  (b) Give a direct algebraic proof that f = |OM|^2 - |ON|^2 = 0 on the manifold.

- **Gap 2:** The "direct sigma argument" in step 5 is incomplete -- sigma maps M to N (in label), but the distances to O are measured in different configurations. Need to show the configurations are related by an isometry.

## Cases to cover
- Isoceles case (AB = AC): trivial by symmetry.
- General case: requires the algebraic/continuity argument.

## Watch out for
- Sigma is NOT a geometric isometry in general; it's a relabeling that preserves the angle conditions but not distances.
- The perpendicular bisector of MN is NOT the same as the perpendicular bisector of BC.
- The argument needs to show OM = ON for ALL valid (K, L), not just that sigma permutes them.
