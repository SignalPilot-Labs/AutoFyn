# proof-reviewer rules

ALWAYS: when simulating a descent strategy (e.g. "angle kθ wins in k−1 cuts"), descend on the SPECIFIC witness the proof names, not an arbitrary/maximal one present in the state — my exhaustive-keep simulator cycled at n=9 equilateral by picking max(multiples), which looked like a proof failure but was a simulator bug (round 1).
ALWAYS: verify game-theoretic sufficiency claims by exhaustive-adversary simulation over exact Fractions (float θℤ-membership tests are unreliable) (round 1).
