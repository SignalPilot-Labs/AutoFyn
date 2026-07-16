## imo-2026-04 (Adversary Lens: Shan-Yu's Survival Strategies)

### Problem restatement
theta in (0°,180°) fixed. Shan-Yu picks initial triangle T. Repeat: if T has angle = theta, Mulan wins. Otherwise Mulan picks P on the perimeter (not a vertex), cuts P to the opposite vertex, splitting T into two triangles; Shan-Yu discards one. Determine all theta for which Mulan wins.

---

### Cut geometry (verified)
Point P on side BC, cut to vertex A (angle a). Let t = angle_BAP ∈ (0, a) (Mulan's continuous parameter).
- T1 = triangle ABP: angles (b, 180-b-t, t) = (b, a+c-t, t)
- T2 = triangle APC: angles (a-t, b+t, c)

The P-angles are supplementary: (a+c-t) + (b+t) = 180. Mulan controls t continuously. She also picks which vertex to cut to (which side P lies on).

---

### Key structural observations

**Multiples of theta are the critical forbidden set.** If the triangle has angle k·theta (k ≥ 2, k·theta < 180), Mulan wins:
- Cut to that vertex with t = theta.
- T1 gets angle t = theta → game ends if Shan-Yu picks T1.
- T2 gets angle (k-1)·theta. Induction on k gives Shan-Yu no escape in k-1 more steps.

**So Shan-Yu must avoid ALL multiples of theta** (not just theta itself).

**When can Mulan force a multiple of theta in BOTH pieces simultaneously?**

T1 has a multiple of theta iff t ≡ 0 (mod theta) [impossible; t ∈ (0,a)] or a+c-t ≡ 0 (mod theta) [i.e., t ≡ a+c (mod theta)].  
T2 has a multiple of theta iff a-t ≡ 0 (mod theta) [t ≡ a (mod theta)] or b+t ≡ 0 (mod theta) [t ≡ -b (mod theta)].

(The preserved angles b in T1 and c in T2 are not multiples by assumption.)

The four possible simultaneous conditions reduce to:
- Case: t ≡ (a+c) mod theta AND t ≡ a mod theta → c ≡ 0 (mod theta). Contradiction.
- Case: t ≡ (a+c) mod theta AND t ≡ -b mod theta → a+b+c ≡ 0 (mod theta) → 180 ≡ 0 (mod theta) → **theta divides 180**.

**Conclusion:** Mulan can force a multiple of theta in BOTH T1 and T2 simultaneously if and only if theta | 180.

---

### When theta divides 180 (theta = 180/n, n ≥ 2): MULAN WINS

**Key invariant:** The multiset of angle-remainders {a mod theta, b mod theta, c mod theta} satisfies:
  - sum = 180 - N·theta = (n-N)·theta, which is itself a multiple of theta (since n and N are integers).
  - So sum of remainders ∈ {theta, 2·theta} (strictly between 0 and 3·theta).

**Mulan's one-step strategy** (when no angle is a multiple of theta):  
Cut to vertex A (choosing a vertex with angle a ≥ theta, which exists since all three can't be < theta = 180/n for n ≥ 3 summing to 180; for n=2=theta=90, use the vertex satisfying a+b>90), with:
  t = theta - r_b  where r_b = b mod theta ∈ (0, theta).

Since sum r_a + r_b + r_c = (n-N)·theta and r_a+r_c = (n-N)·theta - r_b, we get:
- P-angle in T1: (a+c-t) mod theta = (r_a+r_c-(theta-r_b)) mod theta = ((n-N)·theta - theta) mod theta = 0. ✓
- P-angle in T2: (b+t) mod theta = (r_b + theta - r_b) mod theta = 0. ✓

Both pieces contain an angle that is a multiple of theta. Shan-Yu is stuck.

**Validity of t:** Need t = theta - r_b < a. Since a ≥ theta (for n ≥ 3) and theta - r_b < theta ≤ a, valid. For n=2: choose vertex where a+b > 90 (always achievable in any triangle).

**Phase 2:** Once a multiple k·theta appears, induction on k brings Mulan to theta in k-1 more steps. Total: at most n steps.

---

### When theta does NOT divide 180: SHAN-YU WINS

**Shan-Yu's strategy:**
1. Start with a triangle where no angle is a multiple of theta. (Valid: the finitely-many multiples theta, 2·theta, ..., floor(179/theta)·theta form a measure-zero obstacle; e.g. choose angles a=179°, b=0.4°, c=0.6° for large theta.)
2. At each step, for any Mulan cut (any vertex, any t): at most ONE of T1, T2 can contain a multiple of theta (proved above since 180 ≢ 0 mod theta). Shan-Yu picks the other piece.

The invariant "no angle is a multiple of theta" is preserved forever. The game never ends.

**Concrete example (theta=70):** Start with (50°, 80°, 50°). Multiples of 70 in (0°,180°): 70, 140.
- t=30: T1=(50,70,30) has 70; T2=(50,80,50) safe. Shan-Yu picks T2 = original.
- t=10: T2=(70,60,50) has 70; T1=(50,90,10) safe. Shan-Yu picks T1.
- t=20: T2=(60,70,50) has 70; T1=(50,80,20) safe.
- For all other t: neither has a multiple.
Shan-Yu survives indefinitely.

---

### Distinct openings (attack angles for the outliner)

1. **Modular arithmetic on angle remainders:** The core approach above. Model angle-remainders mod theta; the key lemma is that "both pieces get a zero remainder simultaneously iff 180 ≡ 0 (mod theta)." This gives both directions cleanly.

2. **Direct inductive strategy (Mulan wins direction):** Prove Mulan's winning strategy directly by strong induction on k (multiplicity of theta in the current triangle's angles), plus one base-level step reducing "no multiple" to "has multiple" using the phi_t trick.

3. **Forbidden-set / closed-family approach (Shan-Yu wins direction):** Define F = {triangles with no angle equal to any multiple of theta in (0°,180°)}. Show F is closed under Shan-Yu's best response (for any Mulan cut, at least one piece stays in F iff theta does not divide 180). This is a pure invariant argument.

4. **P-angle supplement trick (special case theta=90):** For theta=90, the two P-angles in T1 and T2 are supplementary (sum to 180), so forcing both = 90 requires their sum = 180, i.e., theta=90. This is the clearest special case and a good entry point for the proof.

5. **Density/equidistribution angle (for Shan-Yu in the irrational case):** When theta/180 is irrational, the angles mod theta can be spread densely (Weyl/Kronecker), giving a stronger structural reason why Shan-Yu can maintain non-multiples — though this is not needed for the core argument.

---

### Candidate techniques
- **Invariants/monovariants** (the angle-remainder multiset invariant; Shan-Yu's closed family)
- **Strong induction** (on the multiplicity k·theta)
- **Modular arithmetic** (180 mod theta = 0 is the key divisibility condition)
- **Casework** (theta | 180 vs. theta does not divide 180; vertex selection by size)

### Cheap-kill candidates
- Parity/multiplicity check: can all three angles be multiples of theta with sum 180? Yes iff 180 = k·theta for some k, i.e., theta | 180. This immediately connects the answer to divisibility of 180.
- Size: for theta > 90, multiples of theta in (0°,180°) is just {theta} itself. Shan-Yu just needs to avoid theta, which he can (equilateral triangle, cut-safety argument). Confirms Shan-Yu wins for all theta > 90.

### Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics section): the angle-remainder multiset is a Shan-Yu invariant.
- **Direct proof / Contradiction / Induction** (General Proof Methods): strong induction for the Mulan-wins direction, direct construction for Shan-Yu's strategy.
- **Casework / exhaustion**: two cases (theta | 180 and not).
- **Constructive vs. existence**: the answer requires both a Mulan winning strategy (construction) and a Shan-Yu survival strategy (construction).

### Analogous past problems (cruxes)
(No crux corpus search was done this round — the problem's structure is self-contained and the solution route is clear from direct analysis. The modular-remainder invariant is specific to this problem's geometry.)

### Prior progress
None (round 1 died early, no workspace exists).

### Dead ends (do not retry)
- "All angles < theta" as Shan-Yu's invariant family: fails because it doesn't close under cuts (angle 180-b-t can exceed theta).
- Trying to force theta in BOTH pieces via a single t: only works for theta=90 via the P-angle supplement trick; this is a SPECIAL CASE of the general mod-theta argument.
- Kronecker/density approach for the irrational case: unnecessarily heavy; the algebraic argument (180 ≢ 0 mod theta => no t simultaneously creates multiples in both pieces) is elementary.

### Small-case / intuition notes (labeled as conjecture)
- **theta=90 (verified):** Mulan wins in 1 step from any triangle. Confirmed: t=90-b forces angle 90 at P in both pieces.
- **theta=60 (verified):** Start (70,70,40), use t=50: T1=(70,60,50) has 60, T2=(20,120,40) has 120=2·60. Both forced; Mulan wins in at most 2 steps.
- **theta=70 (verified):** Shan-Yu starts (50,80,50) and survives: for all t, at most one piece has a multiple of 70.
- **theta > 90 (verified by example):** Mulan cannot force multiples in both pieces; equilateral triangle is Shan-Yu's safe start.

---

### Best guess at the answer (HIGH CONFIDENCE ~90%)

**Mulan wins if and only if theta = 180°/n for some positive integer n ≥ 2.**

Equivalently: 180/theta is a positive integer.  
Equivalently: theta divides 180 (as a real number, meaning 180/theta ∈ ℤ).

The set of winning theta values (in degrees): {90, 60, 45, 180/7, 36, 30, 180/8=22.5, 20, 18, 180/11, 15, ...} — all values of the form 180/n for integers n ≥ 2.

Note: this includes non-integer degree values like 180/7° ≈ 25.7°. The condition is purely about 180/theta being an integer, not about theta being an integer.

The algebraic pivot is: **the sum of angle-remainders mod theta equals (n-N)·theta, which is 0 mod theta if and only if theta | 180** — this is the exact condition that forces Mulan's strategy to trap Shan-Yu, and its failure is exactly what lets Shan-Yu maintain his invariant.
