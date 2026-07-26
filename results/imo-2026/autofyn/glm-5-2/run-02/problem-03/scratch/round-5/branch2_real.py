from fractions import Fraction
import random

# n=3 (level 3) Branch 2: m1<a1=4 (in 1/15 units). M=8. rest={m1,m2,m3,m4,2,1}.
def A_of(mp):
    rest = sorted(mp + [2,1], reverse=True)
    A = 4
    for i,v in enumerate(rest):
        if i%2==0: A -= v
        else: A += v
    return A

random.seed(0)
minA = 999; mincfg=None; viol=0; N=2000000
for _ in range(N):
    # 3 random cut points in (0,8)
    cuts = sorted(random.random()*8 for _ in range(3))
    mp = [cuts[0], cuts[1]-cuts[0], cuts[2]-cuts[1], 8-cuts[2]]
    mp.sort(reverse=True)
    if mp[0] >= 4: continue  # branch 2 only
    A = A_of(mp)
    if A < 1: viol += 1
    if A < minA:
        minA = A; mincfg = mp[:]
print(f"Branch2 (n=3) reals: N={N}, violations={viol}, min A (in 1/15 units) = {minA}")
print(f"  min cfg (1/15 units): {mincfg}, real A = {minA}/15")
# also check min evensum(rest) and structure
