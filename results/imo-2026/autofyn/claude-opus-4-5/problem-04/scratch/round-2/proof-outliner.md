## imo-2026-04

mulan-cascade: new
Target: Mulan wins for theta = 180/n (n >= 2) -- constructive strategy forcing theta to appear
Technique: Two-phase cascade: Phase 1 uses pair-sum trick to inject a multiple of theta; Phase 2 bisects down to 2*theta then wins
Skeleton:
  1. For theta = 180/n, choose j1=1, j2=n-1 with j1+j2=n -- arithmetic
  2. From any triangle, cut to create j1*theta and j2*theta in sub-tris -- pair-sum construction
  3. Shan-Yu keeps one with a multiple of theta -- forced by both having multiples
  4. Bisect the multiple-of-theta vertex repeatedly -- halving until 2*theta
  5. Cut vertex 2*theta with t=theta; both subs have theta -- terminal win
Key lemmas (claim + mechanism):
  - Pair-sum forcing: both sub-tris get multiples because (j1+j2)*theta = 180 exactly when theta = 180/n
  - Bisection forcing: setting t = A/2 puts A/2 in both sub-tris, since A-t = t = A/2
  - Terminal win: vertex 2*theta cut with t=theta gives both subs angle theta, since A-t = theta
Open gaps: Phase 1 cut validity (t in legal range for all triangles); multiple persistence through Shan-Yu's choices in cascade
Cases to cover: theta = 90 (instant win, n=2); theta = 60 (n=3); general n >= 3
Watch out for: thin triangles where max angle < theta; ensuring the "level" is monotone

shanyu-invariant: new
Target: Shan-Yu wins for theta != 180/n -- maintains "no angle is k*theta" invariant forever
Technique: Invariant method; the safe set is closed under Shan-Yu's choices when 180/theta is not an integer
Skeleton:
  1. Define S_theta = {triangles with no angle equal to k*theta for any k >= 1} -- definition
  2. Shan-Yu picks initial T in S_theta (exists by discreteness) -- existence lemma
  3. After any cut, at least one sub-tri is in S_theta -- closure lemma
  4. Shan-Yu keeps that sub-tri; invariant maintained forever -- induction
Key lemmas (claim + mechanism):
  - Invariant closure: if both subs have multiples, j1*theta + j2*theta = 180 is required, which needs 180/theta integer
  - Existence: multiples of theta form a discrete set; triangles form a 2D continuous family; avoidance possible
  - Irrational case: (j1+j2)*theta = 180 impossible since LHS irrational, RHS rational
Open gaps: Rigorous derivation of pair-sum constraint from cut mechanics; careful existence proof for initial triangle
Cases to cover: irrational theta; rational theta = 180p/q with p >= 2; theta > 90
Watch out for: cut mechanics analysis; theta = 60 or 90 are 180/n so excluded from this direction

unified-characterization: new
Target: Complete characterization: Mulan wins iff theta = 180/n for integer n >= 2
Technique: Bidirectional proof unified by pair-sum constraint; constructive strategy (sufficiency) + invariant (necessity)
Skeleton:
  1. (Necessity) Define safe set; show it's closed when 180/theta not integer -- invariant argument
  2. (Necessity) Shan-Yu initializes and maintains invariant; Mulan never wins -- induction
  3. (Sufficiency) Phase 1: inject multiple of theta via pair-sum cut -- construction
  4. (Sufficiency) Phase 2: cascade via bisection to 2*theta -- iteration
  5. (Sufficiency) Terminal: cut 2*theta to force theta in both subs -- win
Key lemmas (claim + mechanism):
  - Pair-sum dichotomy: j1*theta + j2*theta = 180 solvable iff 180/theta in Z_>=2 -- pure arithmetic
  - Safe set non-empty: bad angles discrete, triangle space continuous -- topological
  - Cascade termination: bisection halves exponent; finite steps to 2*theta -- logarithmic bound
Open gaps: Pair-sum constraint derivation from geometry; Phase 1 cut validity; multiple persistence
Cases to cover: theta = 90 (special instant-win); theta = 180/n for n >= 3; theta > 90; irrational; rational non-180/n
Watch out for: pair-sum derivation is the crux for both directions; thin triangle edge cases

---

Build set recommendation: unified-characterization (most complete, subsumes both directions), mulan-cascade (backup if unified stalls on one direction)
