from fractions import Fraction
import itertools, random

# n=3 unrefined-R: level-3 dyadic, D=15, M=8, R=(4,2,1), alpha=1
# Branch 2: m_1 < a_1 = 4. All m_i < 4, sum 8. rest = {m1,m2,m3,m4,2,1}
# Want A = 4 - A_rest >= 1, i.e., A_rest <= 3, i.e., evensum(rest) >= 4.

# Brute force over integer-grid m's to find min A in Branch 2
def A_of(m1,m2,m3,m4):
    # m1>=m2>=m3>=m4, sum 8, m1<4 (branch 2)
    rest = sorted([m1,m2,m3,m4,2,1], reverse=True)
    # a1=4 is rank 1
    A = 4
    for i,v in enumerate(rest):
        if i%2==0: A -= v
        else: A += v
    return A

best = None
bestcfg = None
count = 0
viol = 0
# integer grid: m1+m2+m3+m4=8, m1>=m2>=m3>=m4>=0, m1<4
for m1 in range(0,9):
    for m2 in range(0,m1+1):
        for m3 in range(0,m2+1):
            m4 = 8-m1-m2-m3
            if m4 < 0 or m4 > m3: continue
            if m1 >= 4: continue  # branch 2
            if m1 < 0: continue
            count += 1
            A = A_of(m1,m2,m3,m4)
            if A < 1:
                viol += 1
                print("VIOLATION:", (m1,m2,m3,m4), "A=", A)
            if best is None or A < best:
                best = A
                bestcfg = (m1,m2,m3,m4)
print(f"Branch 2 (n=3) integer grid: {count} configs, {viol} violations, min A = {best} at {bestcfg}")
