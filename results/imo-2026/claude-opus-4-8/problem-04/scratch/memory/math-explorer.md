ALWAYS: For combinatorial game problems, look for a "closed safe set" S** such that the game can cycle if Shan-Yu stays in S**, and characterize when the set is NOT closed (because <this> reveals the exact answer criterion, round 1).

ALWAYS: In angle-cutting triangle games, the two new angles at the cut point P are supplementary (sum to 180°). This is the key structural constraint on what Mulan can force in one step (because <it limits the "both children have θ" cases>, round 1).

ALWAYS: Check whether "rational theta" vs "theta divides 180" are the same — they are NOT. θ=72° is rational but NOT 180/N for integer N, and Mulan CANNOT win for θ=72°. The correct criterion is 180/θ ∈ ℤ (round 1).

NEVER: Conflate "θ rational" with "Mulan wins" in angle-partition games — the criterion is specifically θ | 180° (180/θ a positive integer), not just rationality (because θ=72°=2*36° is rational but losing for Mulan, round 1).
# Math Explorer Role Notes

ALWAYS: For geometry/angle games, the KEY structural question is "when can BOTH sub-triangles simultaneously have the target angle?" — this determines Mulan's forcing condition. (round 1)

ALWAYS: For angle-bisection games (like imo-2026-04), compute when theta appears in BOTH sub-triangles of a cut: it requires the vertex being split to have angle 2*theta. This is the "both-have-theta condition." (round 1)

ALWAYS: Check if the impossibility direction has a simple "degree argument" — for theta > 90, 2*theta > 180° makes Mulan's forcing mechanism impossible in ONE line. (round 1)

ALWAYS: For "characterization" problems with real-valued games, look for the rational/irrational dichotomy as a candidate answer — it naturally splits into (a) Mulan wins using arithmetic of rationals, (b) Shan-Yu maintains Q·180 invariant for irrationals. (round 1)

ALWAYS: Verify small cases computationally BEFORE writing the final report — theta=30, 36, 45, 60, 90 are natural test cases for this problem. (round 1)

NEVER: Confuse "theta < 90 implies Mulan wins" with the correct answer — theta < 90 is NECESSARY but RATIONALITY is also required (irrational theta < 90 seems not winnable). (round 1)

ALWAYS: For imo-2026-04, the answer is theta = 180°/k for integer k ≥ 2. The key invariant (Shan-Yu direction): safe set S = {no angle is a multiple of theta} is preserved by any cut when theta ≠ 180/k. The triangle {theta/2, theta/2, 180-theta} is in S iff theta ≠ 180/k (since 180-theta is a multiple of theta exactly when theta=180/k). (round 1)
