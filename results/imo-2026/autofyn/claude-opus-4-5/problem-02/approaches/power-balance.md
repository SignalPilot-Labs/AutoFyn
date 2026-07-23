# Approach: Power Balance

**Slug:** power-balance  
**Status:** partial  
**Last outcome:** partial (round 1)

## Target
Prove OM = ON, where O is the circumcenter of triangle AKL, and M, N are midpoints of AB, AC respectively.

## Technique
Power of a point combined with parameterization k = bp, l = cq to establish equal powers of M and N with respect to circumcircle of AKL.

## Approaches tried
- Power-balance approach (round 1) — partial progress; key reformulation established, parameterization k = b*p, l = c*q discovered, target identity verified numerically to machine precision for multiple triangles and alpha values. The algebraic proof that C1, C2, C3 jointly imply the target identity remains to be closed rigorously.

## Current best
The goal OM = ON is rigorously equivalent to Power(M) = Power(N) w.r.t. the circumcircle omega_AKL. The parameterization k = bp, l = cq with p = 1 - mu*exp(-i*alpha), q = 1 - nu*exp(i*alpha) is established. The target identity is verified numerically to hold for all (mu, nu) satisfying C2 and C3. The remaining gap is the algebraic derivation of this identity from the constraints.

## Full proof (INCOMPLETE - gap at Step 9)

### Setup and Notation

Let triangle ABC have midpoints M of AB and N of AC. Points K and L are inside triangles BMC and BNC respectively, satisfying:
- (i) K lies inside angle LBA
- (ii) L lies inside angle ACK  
- (iii) angle KBA = angle ACL (= alpha)
- (iv) angle LBK = angle LNC (= beta)
- (v) angle LCK = angle BMK (= gamma)

Let O be the circumcenter of triangle AKL, and let omega_AKL denote its circumcircle.

### Step 1: Power Reformulation

**Claim:** OM = ON if and only if Power(M, omega_AKL) = Power(N, omega_AKL).

**Proof:** Let R denote the circumradius of triangle AKL. Then:
- Power(M, omega_AKL) = |MO|^2 - R^2
- Power(N, omega_AKL) = |NO|^2 - R^2

Therefore |MO|^2 - R^2 = |NO|^2 - R^2 if and only if |MO| = |NO|. QED.

### Step 2: Coordinate Setup with A at Origin

Place A at the origin in the complex plane. Let B = b and C = c (complex numbers). Then:
- M = b/2 (midpoint of AB)
- N = c/2 (midpoint of AC)

Let K = k and L = l (complex numbers).

### Step 3: Circumcenter Formula

The circumcenter O of triangle {0, K, L} = {A, K, L} satisfies the perpendicular bisector equations:
- Re(O * conj(k)) = |k|^2 / 2
- Re(O * conj(l)) = |l|^2 / 2

Let D = Im(conj(k) * l) = k_x * l_y - k_y * l_x (twice the signed area of triangle AKL).

Solving the linear system (by Cramer's rule):
$$O_x = \frac{|k|^2 l_y - |l|^2 k_y}{2D}, \quad O_y = \frac{|l|^2 k_x - |k|^2 l_x}{2D}$$

### Step 4: Target Condition in Complex Form

**Claim:** Power(M) = Power(N) is equivalent to:
$$\text{Re}((c - b) \cdot \overline{O}) = \frac{|c|^2 - |b|^2}{4}$$

**Proof:** 
With A = 0, we have R = |O| (since A is on the circumcircle).

Power(M) = |M - O|^2 - R^2 = |b/2 - O|^2 - |O|^2
         = |b/2|^2 - 2 Re(b/2 * conj(O)) + |O|^2 - |O|^2
         = |b|^2/4 - Re(b * conj(O))

Similarly, Power(N) = |c|^2/4 - Re(c * conj(O)).

Power(M) = Power(N) iff:
|b|^2/4 - Re(b * conj(O)) = |c|^2/4 - Re(c * conj(O))

Rearranging: Re((c - b) * conj(O)) = (|c|^2 - |b|^2)/4. QED.

### Step 5: Encoding the Angle Conditions

**Condition (iii): angle KBA = angle ACL = alpha**

The directed angle from ray BA to ray BK equals minus alpha (K is below BA), and the directed angle from ray CA to ray CL equals plus alpha (L is above CA). This gives:

arg((K - B)/(A - B)) + arg((L - C)/(A - C)) = 0

With A = 0: arg((k - b)/(-b)) + arg((l - c)/(-c)) = 0

This means (k - b)(l - c)/(bc) is positive real.

**(C1):** $\frac{(k-b)(l-c)}{bc} \in \mathbb{R}_{>0}$, equivalently $\frac{bc}{(k-b)(l-c)} \in \mathbb{R}_{>0}$

**Condition (iv): angle LBK = angle LNC = beta**

This gives (after algebraic manipulation verified in detail):

**(C2):** $\frac{(k-b)(2l-c)}{(l-b)c} \in \mathbb{R}$

Note: The factor (2l - c) = 2(l - c/2) = 2(L - N) encodes the midpoint N.

**Condition (v): angle LCK = angle BMK = gamma**

This gives:

**(C3):** $\frac{b(k-c)}{(l-c)(2k-b)} \in \mathbb{R}$

Note: The factor (2k - b) = 2(k - b/2) = 2(K - M) encodes the midpoint M.

### Step 6: Key Parameterization

**Claim:** From condition C1, there exist positive reals mu, nu such that:
- k = b * p where p = 1 - mu * exp(-i*alpha)
- l = c * q where q = 1 - nu * exp(i*alpha)

**Proof:** 

Let zeta = exp(i*alpha). From C1:
- arg(k - b) = arg(b) + pi - alpha (since K is at angle -alpha from ray BA)
- arg(l - c) = arg(c) + pi + alpha (since L is at angle +alpha from ray CA)

So k - b = -|k-b|/|b| * b * conj(zeta) = -mu * b * conj(zeta) for some mu > 0.

This gives k = b - mu * b * conj(zeta) = b(1 - mu * conj(zeta)) = b*p where p = 1 - mu*conj(zeta).

Similarly, l - c = -nu * c * zeta for some nu > 0, giving l = c(1 - nu*zeta) = c*q. QED.

**Verification of C1:** With u = k - b = -b*mu*conj(zeta) and v = l - c = -c*nu*zeta:

uv = (-b*mu*conj(zeta))(-c*nu*zeta) = bc*mu*nu*|zeta|^2 = bc*mu*nu

Since mu, nu > 0, we have uv/(bc) = mu*nu > 0, confirming C1.

### Step 7: Explicit Formulas for D and [d, l], [d, k]

Let d = b - c, S = [b, c] = Im(conj(b)*c), T = <b, c> = Re(conj(b)*c).

**Cross products:**
- [d, c] = [b - c, c] = [b, c] = S
- [d, b] = [b - c, b] = -[c, b] = S
- <d, c> = <b, c> - |c|^2 = T - |c|^2
- <d, b> = |b|^2 - <b, c> = |b|^2 - T

**Formula for [d, l]:** Using l = c*q and the identity Im(conj(z1)*z2*w) = [z1, z2]*Re(w) + <z1, z2>*Im(w):

[d, l] = [d, c*q] = [d, c]*Re(q) + <d, c>*Im(q)
       = S*(1 - nu*cos(alpha)) + (T - |c|^2)*(-nu*sin(alpha))
       = S - nu*(S*cos(alpha) + (T - |c|^2)*sin(alpha))

**Formula for [d, k]:** Similarly:

[d, k] = [d, b*p] = S*(1 - mu*cos(alpha)) + (|b|^2 - T)*(mu*sin(alpha))
       = S - mu*(S*cos(alpha) - (|b|^2 - T)*sin(alpha))

**Formula for D = [k, l]:**

D = [b*p, c*q] = Im(conj(b*p)*c*q) = Im(conj(b)*conj(p)*c*q)

Let w0 = conj(b)*c, so Im(w0) = S and Re(w0) = T.

With conj(p) = (1 - mu*cos(alpha)) - i*mu*sin(alpha) and q = (1 - nu*cos(alpha)) - i*nu*sin(alpha):

conj(p)*q = A - i*B where:
- A = 1 - (mu + nu)*cos(alpha) + mu*nu*cos(2*alpha)
- B = sin(alpha)*(mu + nu - 2*mu*nu*cos(alpha))

D = Im(w0 * (A - iB)) = S*A - T*B

### Step 8: Target Identity Expanded

The target condition Re((c - b) * conj(O)) = (|c|^2 - |b|^2)/4 becomes (after computation):

$$|k|^2 [d, l] - |l|^2 [d, k] = -D \cdot \frac{|c|^2 - |b|^2}{2}$$

Substituting k = b*p, l = c*q:

$$|b|^2 |p|^2 [d, l] - |c|^2 |q|^2 [d, k] = -D \cdot \frac{|c|^2 - |b|^2}{2}$$

where:
- |p|^2 = 1 - 2*mu*cos(alpha) + mu^2
- |q|^2 = 1 - 2*nu*cos(alpha) + nu^2

### Step 9: THE MAIN GAP

**Gap:** Prove that for any mu, nu > 0 satisfying conditions C2 and C3 (with the parameterization from Step 6), the identity from Step 8 holds.

**What we have established:**
1. The parameterization k = bp, l = cq is valid for all solutions.
2. Conditions C2 and C3 constrain (mu, nu) to a 1D curve.
3. The target identity is a polynomial equation in mu, nu (with coefficients depending on |b|^2, |c|^2, S, T, alpha).

**Numerical verification (strong evidence):**

Tested extensively:
- Triangle A = (0, 4), B = (-3, 0), C = (2, 0) with alpha in {5, 10, 15, 20, 25, 30} degrees
- Triangle A = (1, 5), B = (-4, 0), C = (3, 1) with alpha in {15, 25} degrees
- Multiple additional triangles

In ALL cases (12+ configurations tested):
- C1, C2, C3 satisfied: |imaginary part| < 10^{-12}
- Target identity satisfied: |LHS - RHS| < 10^{-10}
- OM = ON verified: |OM - ON| < 10^{-14}

**Approaches attempted:**
1. Direct Groebner basis computation: Timed out (degree 4 polynomials in 8+ real variables).
2. Explicit algebraic expansion: The target difference is a complicated polynomial in mu, nu with coefficients involving S, T, |b|^2, |c|^2, cos(alpha), sin(alpha). The polynomial is NOT identically zero - it vanishes specifically when (mu, nu) satisfy the C2, C3 constraints.

**Possible completion strategies:**
1. Derive explicit relationship between mu and nu from C2, C3, substitute, and verify.
2. Show the target polynomial lies in the ideal generated by C2 and C3 constraints.
3. Use a continuity/density argument combined with the numerical verification.

### Additional Observations

**Pattern in (mu, nu) relationship:**

For the test triangle A = (0, 4), B = (-3, 0), C = (2, 0):
| alpha | mu      | nu      | mu*nu   | mu/nu   |
|-------|---------|---------|---------|---------|
| 10    | 0.3976  | 0.3681  | 0.1463  | 1.0803  |
| 15    | 0.3591  | 0.3194  | 0.1147  | 1.1243  |
| 20    | 0.3249  | 0.2761  | 0.0897  | 1.1767  |
| 25    | 0.2932  | 0.2359  | 0.0692  | 1.2430  |
| 30    | 0.2624  | 0.1969  | 0.0517  | 1.3327  |

The ratio mu/nu increases with alpha, suggesting a specific functional relationship.

## Promotable lemmas

**Power-circumcenter equivalence:** For two points M, N and a circle omega with center O, we have |OM| = |ON| if and only if Power(M, omega) = Power(N, omega). (Standard result.)

**Parameterization lemma:** Under condition C1 (angle KBA = angle ACL = alpha), there exist positive reals mu, nu such that k = b(1 - mu*conj(zeta)) and l = c(1 - nu*zeta) where zeta = exp(i*alpha).

## Notes

The power-balance approach provides a clean geometric framework and the parameterization k = bp, l = cq is the key structural insight. The "factor of 2" terms in C2 and C3 (encoding midpoints M and N) create the coupling between the parameterization and the target identity. The remaining algebraic verification is the barrier to completion.
