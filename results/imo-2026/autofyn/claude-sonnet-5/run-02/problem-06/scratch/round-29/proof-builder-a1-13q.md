## a1-13q-subfamily-theorem — round 29 build report

Status: solved.

Built the complete, gap-free proof of literal T=1,L=13 periodicity for
a_1=13q, every prime q>13, q not in Bad(13)={17,19,23,47}, by instantiating
the certified p-uniform machinery (Generalized K0-Boundedness, gcd-difference
Witness Lemma, Legendre Sieve Gap Bound, Primorial Floor Bound, Universal
Look-Back r=1 corollary) at p=13, mirroring the certified a1-11q template
exactly.

Every number was independently recomputed from the raw definitions via
Python/sympy, not copied from the outline or explorer reports:
- 132-cell (j,r,s0,K0) table (max K0=25).
- k=0 layer: 112 below-threshold (j,r,q) candidates (r=2..12); 107 resolved
  by explicit witness, exactly 5 with no witness: the 4 genuine exceptions
  (4,4,17),(6,6,19),(8,8,47),(10,10,23) plus the moot duplicate (12,6,19).
- The q=19 moot-cell claim is explicitly PROVED (not asserted): direct
  greedy simulation shows a_3=266 (not 273) for q=19, so H(3) (which the
  (12,6) band's analysis presupposes) never holds in the real sequence;
  confirmed q=19 is the only prime with two EXC entries among the 112
  candidates.
- All 4 genuine exceptions verified permanent via full factorization
  hand-checks (every smaller candidate illegal via i=1, N legal against
  every earlier term).
- k>=1 residual band: derived s*=5 threshold
  (s+1)! >= 25 + (13/17)*2^{s+1}*(s+2), proved by induction, reducing to
  residual band k in {1,...,11}; swept all 132*11=1452 cell/k combinations,
  found exactly 29 below-threshold (j,r,k,q) quadruples, split 19 moot
  (q in Bad(13)) / 10 non-moot (q in {29,31,37,41,43,53,59,61}), all 10
  resolved by explicit witness.
- Independent greedy resimulation over primes q in (13,5000): Bad(13)
  exactly reproduced, matching the outline-reviewer's independent q<20000
  check.

File: /home/agentuser/repo/results/imo-2026-06/approaches/a1-13q-subfamily-theorem.md
(Status: solved, Full proof sections 0-9, Promotable lemmas section
documents the p=13 table, s*=5 threshold, Bad(13) permanence, and a
reusable moot-duplicate-cell resolution template for future p-instantiations.)
