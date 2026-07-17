# IMO 2026 P2 — OM = ON

## Status
solved

## Approaches tried
- complex-identity — solved (round 2): polynomial ideal membership proof via complex coordinates; circumcenter identity reduces to T=0 on constraint variety V(C2_q, C3_q), established by explicit certificate F*T = |c|^2(S+mu*H_2)C2_q - |b|^2(S+nu*H_3)C3_q
- power-balance — partial: correct setup but same gap as complex-identity; superseded

## Current best
Complete proof via complex-identity approach.

## Full proof

**Problem.** Triangle ABC with midpoints M (of AB) and N (of AC). Points K and L inside triangles BMC and BNC respectively satisfy:
- (i) angle KBA = angle ACL
- (ii) angle LBK = angle LNC
- (iii) angle LCK = angle BMK

Let O be the circumcenter of triangle AKL. Prove OM = ON.

---

### Step 1: Coordinate Setup

Place the triangle in the complex plane with A at the origin:
- A = 0, B = b, C = c (complex numbers)
- M = b/2, N = c/2

### Step 2: Circumcenter Formula

The circumcenter O of triangle {0, k, l} satisfies:
- x = (|k|^2 l_i - |l|^2 k_i) / D
- y = (|l|^2 k_r - |k|^2 l_r) / D

where D = 2 Im(conj(k) l).

### Step 3: Target Reformulation

OM = ON is equivalent to |O - b/2|^2 = |O - c/2|^2, which simplifies to:

**Target:** T = |k|^2 [d,l] - |l|^2 [d,k] + D(|c|^2 - |b|^2)/2 = 0

where d = b - c and [u,v] = Im(conj(u) v).

### Step 4: Encoding the Angle Conditions

**(C1)** angle KBA = angle ACL: Im(bc conj((k-b)(l-c))) = 0
**(C2)** angle LBK = angle LNC: Im((k-b)(2l-c) conj((l-b)c)) = 0
**(C3)** angle LCK = angle BMK: Im(b(k-c) conj((l-c)(2k-b))) = 0

### Step 5: Parameterization from C1

From C1, parameterize: k = b(1 - mu exp(-i alpha)), l = c(1 - nu exp(i alpha)) with mu, nu > 0.

### Step 6: Decoupling

Under this parameterization:
- C2 = mu |c|^2 C2_q where C2_q = F nu^2 + G nu + H_2 (quadratic in nu only)
- C3 = nu |b|^2 C3_q where C3_q = F mu^2 + G mu + H_3 (quadratic in mu only)
- F = 2 Im(conj(b) c exp(i alpha))
- H_2 = F/2 - |b|^2 sin(alpha), H_3 = F/2 - |c|^2 sin(alpha)

The key: both share the same leading coefficient F.

### Step 7: Polynomial Certificate

**Identity:** F * T = |c|^2 (S + mu H_2) C2_q - |b|^2 (S + nu H_3) C3_q

where S = Im(b conj(c)).

On V(C2_q, C3_q), the RHS = 0, so F * T = 0.

### Step 8: F Nonzero for Valid Configurations

F = 0 iff alpha = arg(b/c) + k*pi for some integer k.

**Case alpha = arg(b/c):** The direction of K - B equals pi + arg(c), pointing toward -c. By barycentric analysis, K cannot lie strictly inside triangle BMC.

**Case alpha = arg(b/c) + pi:** The direction of K - B equals arg(c), pointing toward c. Again, K cannot lie strictly inside triangle BMC.

**Conclusion:** If K is inside triangle BMC (as required), then F is nonzero.

### Step 9: Conclusion

On the constraint variety V(C2_q, C3_q):
- From Step 7: F * T = 0
- From Step 8: F is nonzero
- Therefore: T = 0
- From Step 3: T = 0 implies OM = ON

**QED.**
