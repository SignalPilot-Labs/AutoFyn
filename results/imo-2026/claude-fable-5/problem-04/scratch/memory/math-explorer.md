# Math Explorer Per-Role Rules

ALWAYS: For triangle-cutting games, model angle-remainders mod theta as the game state — the key invariant is often the multiset {a mod theta, b mod theta, c mod theta} (because t and a-t both arise from the same angle, and their remainders add to a mod theta). (because the angle remainder multiset turned out to be exactly the right invariant for imo-2026-04, round 2)

ALWAYS: For game problems asking "for which theta does player X win," test the critical cases theta=90° (supplement trick), theta=60° (equilateral start), and one theta not dividing 180 (e.g., 70°) before theorizing. Concrete cases pin down the answer quickly. (because this round the concrete cases immediately revealed the pattern, round 2)

ALWAYS: When a game cut creates two pieces T1 and T2, look for conditions under which BOTH pieces satisfy a property simultaneously — this is the "Mulan can win from both" condition and usually gives a clean algebraic identity. (because for this problem, the condition reduced to 180 ≡ 0 mod theta, round 2)

ALWAYS: The correct Shan-Yu invariant is "no angle is ANY positive integer multiple of theta" (i.e., {theta, 2*theta, 3*theta, ...}), not just {theta} or the doubling orbit. The 4-case exhaustive argument uses arbitrary j,k ∈ ℤ>0, and the contradiction 180 = (j+k)*theta requires j+k = 180/theta ∈ ℤ. The doubling orbit is strictly weaker and insufficient. (because the full integer-multiple invariant is what the 4-case proof needs, round 2)

ALWAYS: For "for which theta does player X win" game characterizations, test whether the answer is "theta = 180/n for integer n>=2" before testing "rational multiples of 180" — many rational-multiple theta values are Shan-Yu wins (e.g., 40°, 72°, 120°). (because the simulation clearly separated 180/n from other rationals, round 2)

ALWAYS: When building a minimax BFS for a game with continuous parameters, set depth >= n/2 where n = 180/theta, because the number of moves needed can be ~n/2. Shallow depth gives false negatives for small theta. (because theta=1 needs ~90 steps but depth-4 returns False, round 2)
