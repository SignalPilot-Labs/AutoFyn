ALWAYS: For stick/interval division games with alternating picks, check if the answer involves a geometric sequence (powers of 2) before trying arithmetic sequences. (because imo-2026-03 has answer 2^n/(2^{n+1}-1), round 1)

ALWAYS: When numerically searching for optimal LB strategies, verify each candidate against BOTH (n-1)-mark and n-mark XY strategies, since XY using fewer marks can sometimes be more damaging (parity effect). (because round 1 search initially missed XY 1-mark strategies)

ALWAYS: Double-check code for midpoint calculations — use interval_start + interval_length/2, not a naive offset based on label fractions. (because round 1 verification code had wrong midpoints for n=3)

NEVER: Assume the n-mark game answer is (n+1)/(2n+1) just because it has 2n+1 pieces in the binding case — LB can not create 2n+1 pieces with n marks, so this formula is wrong for this problem class. (because round 1 initially guessed this formula and it was wrong for n=2)
