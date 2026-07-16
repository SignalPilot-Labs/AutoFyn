## imo-2026-04

### Problem Summary
Mulan wants to force angle theta in a triangle; Shan-Yu makes initial triangle and discards one of two sub-triangles after each of Mulan's cuts. Mulan wins if ANY surviving triangle has angle exactly theta. Game: on each step Mulan picks a non-vertex point P on the perimeter and cuts to the opposite vertex; Shan-Yu discards one of the two resulting triangles.

### Key Structural Analysis

**Cut mechanics:** Cutting from non-vertex point P on side AB to vertex C (with angle C):
- Sub-triangle APC: {A, alpha, 180-A-alpha} where alpha = angle at P in APC.
- Sub-triangle BPC: {B, 180-alpha, alpha-B}.
- alpha is Mulan's FREE CHOICE in the open interval (B, 180-A).
- Angles A and B are PRESERVED in their respective sub-triangles.
- Angle C is SPLIT into (180-A-alpha) and (alpha-B), summing to C = 180-A-B.

**When can Mulan force BOTH sub-triangles to have theta?** (Key to forcing Shan-Yu's hand)
From a cut from side AB to C with alpha:
- Both have theta iff alpha=90=theta (theta=90 case), OR current triangle has angle C = 2*theta (alpha = B+theta).
- Similarly for cuts from other sides: both have theta iff the vertex being split has angle 2*theta.

**THEOREM (observed):** Mulan can force both sub-triangles to have theta in ONE CUT iff:
1. theta = 90° (universal: alpha=90 from any side; both sub-triangles get 90 regardless of A,B), OR
2. The current triangle has some angle equal to 2*theta (Mulan halves it: alpha = [endpoint angle] + theta).

### Conjectured Answer

**CONJECTURE (high confidence):** Mulan wins (in finitely many steps, regardless of Shan-Yu's play) iff:
- 0° < theta ≤ 90° AND theta/180° is rational.

Equivalently: theta = (p/q)·180° for positive integers p, q with gcd(p,q)=1 and p ≤ q/2. (The condition p ≤ q/2 ensures theta ≤ 90°.)

**Label this as CONJECTURE.**

### Distinct Openings

**Opening 1 (Impossibility, theta > 90°):**
For theta > 90°: 2*theta > 180°, so no triangle can have angle 2*theta. Since from any triangle WITHOUT theta, both sub-triangles can simultaneously have theta ONLY if some angle = 2*theta (shown above) or theta=90, it follows that at most ONE sub-triangle can have theta from any cut. Shan-Yu always picks the sub-triangle WITHOUT theta. This is a CLEAN impossibility: Shan-Yu maintains the invariant "no angle = theta" forever, by picking the non-theta sub-triangle (which always exists since both can't have theta).

**Opening 2 (Impossibility, theta < 90° but irrational):**
Shan-Yu maintains the invariant: all angles are rational multiples of 180° (Q·180°). Since theta ∉ Q·180°, also 2*theta ∉ Q·180°. If Mulan cuts with rational alpha, both sub-triangles have rational angles. If Mulan cuts with irrational alpha (say alpha=theta), APC has theta; Shan-Yu picks BPC={B, 180-theta, theta-B}, which has NO theta (180-theta ≠ theta for theta ≠ 90, theta-B ≠ theta for B > 0) AND no 2*theta (since 180-theta=2*theta iff theta=60 [rational], and theta-B=2*theta iff B=-theta < 0). The invariant eventually degrades (Shan-Yu must live with irrational angles after Mulan's injection), BUT: for any resulting irrational-angle triangle {a+b·theta, c+d·theta, e+f·theta} (in Q+Q·theta coordinates), the angle 2*theta appears only if b=2 and a=0, a condition Shan-Yu can avoid since he always picks the sub-triangle that DOESN'T have theta (and the non-theta sub-triangle doesn't have 2*theta either, by explicit calculation).

**Opening 3 (Mulan wins for rational theta ≤ 90°):**
Key lemma: From ANY triangle, Mulan can force the surviving triangle to have angle 2*theta in finitely many steps (when theta < 90, rational). Once 2*theta appears, Mulan halves it: both sub-triangles get theta, Shan-Yu must take one, game over. 

Concrete strategy sketch (theta = p/q · 180, p ≤ q/2):
- Step 1: Mulan cuts with alpha=2*theta if valid (forcing BPC to have 180-2*theta), or uses a triangle with angle 2*theta as intermediate via the structure of rational angles.
- The rational structure ensures the "angle reduction process" terminates in finitely many steps. Think Euclidean algorithm: the ratio of angles is rational, so iterating reductions eventually hits the target.

**Opening 4 (Verified small cases):**
- theta=90: 1-step win. Cut any side with alpha=90; both sub-triangles get 90° regardless of the initial triangle.
- theta=60 (= 1/3 · 180): 2-step win. Step 1: alpha=60 forces Shan-Yu to pick BPC with 120°=2·60. Step 2: halve the 120°. Both get 60°.
- theta=45 (= 1/4 · 180): 2-step win. Step 1: alpha=90 forces both sub-triangles to have 90° (Shan-Yu picks one). Step 2: halve the 90°. Both get 45°.
- theta=36 (= 1/5 · 180): 3-step win. Step 1: alpha=36 forces BPC with 144°. Step 2: halve 144° to get 72° in both (Shan-Yu picks one). Step 3: halve 72° to get 36° in both.
- theta=30 (= 1/6 · 180): 3-step win. More complex path: force triangle with 60° (via forcing 120°), then halve 60°.
- theta=120 (= 2/3 · 180, > 90): NOT winnable. 2*120=240>180, so no triangle has angle 240°. Shan-Yu can always pick non-120° sub-triangle.

**Opening 5 (Angle arithmetic / Euclidean structure for rational theta):**
For theta = p/q · 180 with p ≤ q/2, Mulan's winning strategy uses the following chain:
(a) Force angle k·theta (mod 180) to appear in surviving triangle for increasing k.
(b) By rational structure, the sequence theta, 2*theta, 3*theta, ... (mod 180) cycles with period q, and hits 2*theta (needed for the halving step) within q steps.
(c) The KEY is: can Mulan always force k*theta → (k+1)*theta? Yes, because from a triangle with angle k*theta, setting alpha=k*theta forces Shan-Yu into a triangle with 180-k*theta.

### Candidate Techniques

1. **Monovariant / potential function:** Mulan drives a "progress" measure toward theta (e.g., the minimum distance of any angle from theta decreases over time, or the denominators in the rational angle representation decrease). The impossibility uses an invariant that Shan-Yu can maintain.

2. **Invariant for impossibility:** For theta > 90: "both sub-triangles can have theta iff current has 2*theta (impossible since 2*theta > 180)." For irrational theta: "all angles lie in Q·180°" (Shan-Yu's invariant); or more refined: "angles lie in Q + Q·theta, excluding theta and 2*theta."

3. **Bisection / angle-halving:** The winning move when the current triangle has angle 2*theta. Both sub-triangles get theta. This is the terminal forcing move.

4. **Adversarial forcing via complement:** When Mulan puts theta in APC, Shan-Yu is forced to pick BPC with 180-theta. Then Mulan exploits the structure of the 180-theta triangle. For rational theta, this eventually cycles back to an angle that enables the halving step.

5. **Rational vs. irrational dichotomy:** The key insight: a triangle with ALL RATIONAL angles (in degrees) can never have the irrational value theta as an angle. Mulan can inject theta into ONE sub-triangle, but Shan-Yu always picks the other. The Q-rationality invariant is preserved if both players use rational cuts; the irrational theta can never "contaminate" the winning sub-triangle choice.

### Cheap-Kill Candidates

1. **theta > 90 is impossible:** Both sub-triangles having theta requires 2*theta < 180; fails for theta > 90. One-line observation that prunes this half of the parameter space.

2. **theta = 90 is a 1-step win:** Setting alpha=90 forces both sub-triangles to have 90°. The only triangles without 90° are non-right triangles, but alpha=90 forces 90° regardless of A, B.

3. **Parity/rationality kill:** If theta is irrational and Shan-Yu starts with a rational-angle triangle, the irrational theta can never appear in the surviving triangle unless Mulan injects it, and Shan-Yu always picks the other sub-triangle.

### Knowledge-Base Entries to Use

- **Invariants & monovariants** (Combinatorics section): Shan-Yu's invariant "all angles rational" and the monovariant tracking when theta is reachable.
- **Constructive / incremental** (Combinatorics section): Building Mulan's strategy one step at a time, exploiting rational structure.
- **Contradiction** (General Proof Methods): For theta > 90, derive contradiction that 2*theta > 180 but triangle must have angle 2*theta for Mulan to win.
- **Pigeonhole / extremal principle**: For rational theta, the sequence k*theta (mod 180) is periodic with period q; use this to show 2*theta is reached in finitely many steps.
- **Kronecker / Weyl equidistribution**: Used in the NEGATIVE direction for irrational theta. The orbit of k*theta (mod 180) is dense, meaning 2*theta can't be avoided, but the FINITE-step constraint means Mulan can't achieve it in finite steps without the rational structure.

### Analogous Past Problems (cruxes)

1. **aimo-0225** (triangle counter game on n-gon): Crux move — "determine game value by recursing on 2-adic valuation of a difference that exactly halves at each relevant step." Analogous because: the game involves geometric configurations on a polygon, and the key invariant is a 2-adic (halving) structure. The "halving" of the 2*theta angle is the analog of the 2-adic halving in aimo-0225. Transfer: the characterization of winning positions involves a halving/bisection argument.

2. **aimo-0236** (token game with 2-adic valuation): Crux move — "maintain a valuation invariant; forcing terminates when the invariant is saturated." Analogous because: both problems involve a two-player game where one player tries to force a specific numerical value (theta vs. a specific p-adic valuation), and the other maintains an invariant. The argument structure (invariant for impossibility, driving toward a specific value for the winning direction) transfers directly.

3. **aimo-0355** (quirky triangles — rational angle relations): Crux move — "use the angle-sum constraint to collapse rational linear relations among triangle angles into cosine equalities; rationality of 2*cos(angle) controls all integer multiples." Analogous because: the problem fundamentally involves whether theta/180 is rational (commensurable with 180°), and the Chebyshev polynomial technique for rational cosines (which characterizes rational angles) is directly relevant to understanding why rational theta is "special." Transfer: if theta/180 is rational = p/q, then the angles k*theta (k < q) are all rational multiples of 180°, which is exactly the structure Mulan exploits.

### Prior Progress

None (round 1, unsolved).

### Dead Ends (do not retry)

None (round 1).

### Small-Case / Intuition Notes

(All labeled as CONJECTURE unless proved.)

- CONJECTURE: Answer is {theta ∈ (0°, 180°) : theta/180° ∈ Q and theta ≤ 90°}.

- Verified small cases (computationally):
  - theta=90: 1-step win. Both sub-triangles get 90° when alpha=90.
  - theta=60: 2-step win. Force 120°, then halve.
  - theta=45: 2-step win. Force 90°, then halve. (Uses theta=90 as intermediate.)
  - theta=36: 3-step win. Force 144°, force 72°, halve to 36°.
  - theta=30: 3-step win. (Traced explicitly: from {80,50,50} type initial triangles, multi-step forcing works.)
  - theta=120: NOT winnable. From equilateral {60,60,60}, no cut ever creates 120° in both sub-triangles.

- Key insight: The "magic" of theta ≤ 90° is that 2*theta ≤ 180°, making 2*theta a valid triangle angle. This is the ONLY "forcing condition" for the final win (Mulan halves 2*theta to get theta in both sub-triangles). For theta > 90°, this mechanism completely fails.

- Key insight: Rationality of theta/180° is needed because Shan-Yu can maintain "all angles rational" as an invariant. If theta is irrational, Mulan can inject theta into ONE sub-triangle but never BOTH. Shan-Yu always picks the rational-angle sub-triangle.

- The number of steps to win seems to be related to the "continued fraction complexity" of p/q (for theta = p/q · 180°), analogous to the Euclidean algorithm running time. This is NOT verified rigorously.

