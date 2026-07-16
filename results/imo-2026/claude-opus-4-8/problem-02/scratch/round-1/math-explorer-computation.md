## imo-2026-02

### COMPUTATION LENS REPORT

**Lens:** Coordinates / trig / numerical experiment

---

### Numerical Setup and Verification

**Configuration.** Fix scalene triangle ABC with M = midpoint(AB), N = midpoint(AC). Parametrize K and L by:

- **alpha = angle_KBA = angle_ACL** (free parameter, condition 1 built in by choice of ray directions)
- K lies on ray from B making angle `alpha` with BA, at distance `t_K` from B
- L lies on ray from C making angle `alpha` with CA, at distance `t_L` from C

Given `alpha`, conditions 2 (angle_LBK = angle_LNC) and 3 (angle_LCK = angle_BMK) give **two equations in two unknowns** (t_K, t_L), yielding a **1-parameter family** parametrized by alpha in (0, angle_ABC).

**Solver:** `scipy.optimize.fsolve` on the 2×2 nonlinear angle system. Verified residuals < 1e-8 and that K ∈ triangle(BMC), L ∈ triangle(BNC), plus the qualitative conditions K inside angle LBA and L inside angle ACK. All passed in all cases.

**Triangles tested:**
- Scalene 1: A=(0.5,1.5), B=(0,0), C=(2,0)
- Scalene 2: A=(1,2), B=(0,0), C=(3,0)
- Scalene 3: A=(0.3,1.2), B=(0,0), C=(1.5,0)
- Scalene 4 (general orientation): A=(0.7,1.1), B=(0.2,0.1), C=(1.8,0.3)

**Result:** OM = ON confirmed to within 1e-10 across ALL triangles and ALL parameter values tested (6–10 values of alpha per triangle). The verification script is saved at `results/imo-2026-02/verify_config.py`.

---

### Key Structural Finding: O on Perpendicular Bisector of MN

The most important numerical fact: **O always lies on the perpendicular bisector of MN**.

In coordinates with BC horizontal: O_x = (M_x + N_x)/2 = exact constant, to 1e-11 precision.

In general position (Scalene 4): the projection of (O - midpoint(MN)) onto the direction (N - M) is 0 to 1e-10 precision.

Since MN || BC (midsegment), the perpendicular bisector of MN is perpendicular to BC. The condition OM = ON is EQUIVALENT to O lying on this perpendicular bisector. Algebraically: (N − M) · (O − midpoint(MN)) = 0, i.e., (C − B) · O = (C − B) · (2A + B + C)/4.

---

### Reusable Parametrization (Law of Sines Form)

Let alpha, beta, gamma denote the three angle values:
- alpha = angle_KBA = angle_ACL (free)
- beta = angle_LBK = angle_LNC (constrained)
- gamma = angle_LCK = angle_BMK (constrained)

From the triangles KBC and LBC (law of sines with ∠KBC = B − alpha, ∠KCB = C − alpha − gamma, ∠LBC = B − alpha − beta, ∠LCB = C − alpha):

- BK = BC · sin(C − alpha − gamma) / sin(A + 2*alpha + gamma)
- CL = BC · sin(B − alpha − beta) / sin(A + 2*alpha + beta)

From condition 3 (∠BMK = gamma, using BM = AB/2, ∠MBK = alpha trivially):
- BK = (AB/2) · sin(gamma) / sin(alpha + gamma)

Setting these equal: **Constraint (I)**: sin(C) · sin(gamma) · sin(A + 2alpha + gamma) = 2 sin(A) · sin(C − alpha − gamma) · sin(alpha + gamma)

From condition 2 (∠LNC = beta, using CN = AC/2, ∠NCL = alpha trivially):
- CL = (AC/2) · sin(beta) / sin(alpha + beta)

Setting equal: **Constraint (II)**: sin(B) · sin(beta) · sin(A + 2alpha + beta) = 2 sin(A) · sin(B − alpha − beta) · sin(alpha + beta)

Note: Constraints (I) and (II) are DECOUPLED: (I) relates only alpha and gamma; (II) relates only alpha and beta. This means for each alpha, gamma is independently determined by (I) and beta by (II). The system is highly structured.

---

### Power-of-a-Point Reformulation

OM = ON is equivalent to: **pow(M, circumcircle(AKL)) = pow(N, circumcircle(AKL))**.

Let A' = second intersection of line AB with circumcircle(AKL), A'' = second intersection of line AC with circumcircle(AKL). Since M is midpoint of AB: MA = AB/2 = MA (distance from M to A). Similarly NA = AC/2.

Then pow(M) = MA · MA' and pow(N) = NA · NA''.

For OM = ON: MA · MA' = NA · NA'', i.e., MA'/MA = NA''/NA, i.e., **MA' / (AB/2) = NA'' / (AC/2)**.

Numerically verified: MA' / NA'' = AC/AB = b/c for ALL tested solutions. This is the algebraic identity the conditions enforce.

Geometrically: A' lies between M and B (t_A' ∈ (0.5, 1) on segment AB, i.e., strictly between M and B). A'' lies between N and C.

---

### B ↔ C Symmetry

Under the map B ↔ C, M ↔ N, K ↔ L:
- Condition 1: angle_KBA = angle_ACL maps to angle_LCA = angle_ABK — same condition.
- Condition 2 maps to condition 3 and vice versa.

So the problem is **symmetric under B ↔ C with K ↔ L**. This does NOT prove OM = ON directly (K and L in a specific instance are NOT symmetric about the perp bisector of MN), but it confirms the conditions have an intrinsic left-right pairing.

---

### What the Numbers Rule Out

- **No simple concyclicities found**: MKNL, BKNL, CMKL, BKLC, AMKN, ANLM are all non-concyclic (errors ~0.1–1.0, not approaching zero).
- **No simple spiral similarity**: No spiral centered at A, B, or C maps M→N and simultaneously K→L.
- **K and L do NOT lie on fixed circles** as the parameter varies (least-squares fit to circle gives std_err ~0.005, not fitting exactly).
- **O is not fixed** as the parameter varies; it traces a segment of the perpendicular bisector of MN.

---

### Proof Approach Candidates

**Approach A (Direct trig-law-of-sines bash):**  
Given the decoupled constraints (I) and (II), compute O_x explicitly in terms of alpha using the law-of-sines expressions for BK, BL, K, L. Show O_x = (M_x + N_x)/2 as a trigonometric identity. The decoupling of (I) and (II) is crucial.

**Approach B (Power of a point):**  
Show MA · MA' = NA · NA'' where A' ∈ line(AB) ∩ circ(AKL), A'' ∈ line(AC) ∩ circ(AKL). Use the given angle conditions (via inscribed angle theorem on the circumcircle of AKL) to express MA' and NA'' in terms of the triangle's angles and the parameters.

Key: by the inscribed angle theorem, the angle ∠AKA' (= angle from K looking at A and A') equals ∠ALA' (since A' is on circumcircle). Since A' is on line AB, ∠AA'K = ∠ALK (inscribed angles subtending arc AK). The angle ∠ALK can be expressed via the given conditions.

**Approach C (Angle-bisector / trigonometric Ceva):**  
Use trig Ceva applied to triangle ABC with cevians through K and L to derive a product condition that forces O_x = const. The B ↔ C symmetry of the conditions motivates this.

**Approach D (Identify the hidden invariant geometrically):**  
The condition decouples: (I) relates alpha, gamma only; (II) relates alpha, beta only. This suggests the "left constraint" (on gamma via M) and "right constraint" (on beta via N) act independently. The key geometric insight might be: condition 3 forces the triangle BMK to have a specific shape relative to AB, and condition 2 forces the triangle CNL to have the "mirror" shape relative to AC, with the AB/AC ratio maintaining the balance MA · MA' = NA · NA''.

---

### Locus of O and Boundary Behavior

- As alpha → 0: K → M, L → N, O → circumcenter(AMN) on the perpendicular bisector of MN.
- As alpha → angle_ABC: K → B, L approaches a point on segment BC near C, O moves down the perpendicular bisector of MN.
- O is NOT the circumcenter of AMN in general; it moves along the perpendicular bisector of MN as alpha varies.

---

- **Distinct openings:** (A) Direct trig bash with decoupled constraints; (B) Power-of-a-point via MA·MA'=NA·NA''; (C) Exploit B↔C symmetry with trig-Ceva; (D) Angle chase using the inscribed angle theorem on circumcircle of AKL to identify A' and A''.
- **Candidate technique(s):** Law of sines in triangles KBC/LBC; power of a point (M and N w.r.t. circumcircle of AKL); inscribed angle theorem.
- **Cheap-kill candidates:** The B↔C symmetry plus the decoupling of constraints (I) and (II) is the structural peg; no parity/pigeonhole kill available.
- **Knowledge-base entries to use:** "Synthetic toolkit: angle chasing, power of a point, similar triangles, trig cevians"; "Coordinates / complex / barycentric"; "Trig identities & interval intersection."
- **Analogous past problems (cruxes):** None in corpus (geometry cruxes not extracted).
- **Prior progress:** none (round 1).
- **Dead ends (do not retry):** No simple concyclicities; no spiral similarity maps K→L and M→N; K and L do not lie on individually fixed circles.
- **Small-case / intuition notes:** The decoupling of the constraint equations is the deepest structural fact: (I) involves only alpha,gamma; (II) involves only alpha,beta. This means each midpoint (M or N) independently constrains one of the two secondary angles, which likely causes the left/right "powers" MA·MA' and NA·NA'' to balance via the ratio AB/AC. Conjecture: the proof reduces to showing that the ratio (MA')/(NA'') = b/c = AC/AB follows from constraints (I) and (II).
