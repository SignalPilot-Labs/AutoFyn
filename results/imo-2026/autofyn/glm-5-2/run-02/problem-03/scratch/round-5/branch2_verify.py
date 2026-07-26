from fractions import Fraction
import random

# Verify Branch 2 n=3 casework logic exhaustively over a fine grid + reals
# Branch 2: m1<4 (1/15 units), M=8, rest5={m2,m3,m4,2,1}, need oddsum(rest5)>=4

def oddsum_rest5(m2,m3,m4):
    pieces = sorted([m2,m3,m4,Fraction(2),Fraction(1)], reverse=True)
    return pieces[0]+pieces[2]+pieces[4]

def A_branch2(m1,m2,m3,m4):
    # full global A
    rest = sorted([m1,m2,m3,m4,Fraction(2),Fraction(1)], reverse=True)
    A = Fraction(4)
    for i,v in enumerate(rest):
        if i%2==0: A -= v
        else: A += v
    return A

# Exhaustive rational grid with denom 60 (subdivisions of 8 into 4 parts)
N=0; viol=0; minA=999; mincfg=None
random.seed(1)
# integer grid step 1 (coarse): m1+m2+m3+m4=8, m1>=m2>=m3>=m4, m1<4
for m1 in range(2,4):  # m1 in {2,3} (<4)
    for m2 in range(0,m1+1):
        for m3 in range(0,m2+1):
            m4 = 8-m1-m2-m3
            if m4<0 or m4>m3: continue
            N+=1
            A = A_branch2(m1,m2,m3,m4)
            o = oddsum_rest5(m2,m3,m4)
            if A < 1 or o < 4:
                viol+=1
                print("VIOLATION int:", (m1,m2,m3,m4), "A=",A, "oddsum5=",o)

# fine rational grid: step 1/30, m1 in [2,4)
step = Fraction(1,30)
m1 = Fraction(2)
while m1 < 4:
    for m2_cnt in range(0, int((8-m1)/step)+1):
        m2 = m1 - m2_cnt*step  # m2 <= m1
        if m2 < 0: break
        for m3_cnt in range(0, int((8-m1-m2)/step)+1):
            m3 = m2 - m3_cnt*step
            if m3 < 0: break
            m4 = 8 - m1 - m2 - m3
            if m4 < 0 or m4 > m3: continue
            N+=1
            A = A_branch2(m1,m2,m3,m4)
            o = oddsum_rest5(m2,m3,m4)
            if A < 1:
                viol+=1
                if A < minA:
                    minA = A; mincfg=(m1,m2,m3,m4)
            if o < 4:
                print("oddsum5<4:", (float(m1),float(m2),float(m3),float(m4)), "o=",float(o))
    m1 += step

print(f"Grid exhaustive: N={N}, A-violations={viol}, minA={float(minA) if minA<999 else 'none'}")
if minA<999: print(f"  min cfg: {mincfg}, A={float(minA)}")

# random reals double-check
random.seed(2)
rv=0; rmin=999
for _ in range(500000):
    cuts=sorted(random.random()*8 for _ in range(3))
    mp=[cuts[0],cuts[1]-cuts[0],cuts[2]-cuts[1],8-cuts[2]]
    mp.sort(reverse=True)
    if mp[0]>=4: continue
    A=A_branch2(Fraction(mp[0]).limit_denominator(10**9),Fraction(mp[1]).limit_denominator(10**9),Fraction(mp[2]).limit_denominator(10**9),Fraction(mp[3]).limit_denominator(10**9))
    # use float
    rest=sorted(mp+[2,1],reverse=True)
    Af=4
    for i,v in enumerate(rest):
        if i%2==0: Af-=v
        else: Af+=v
    if Af<1: rv+=1
    if Af<rmin: rmin=Af
print(f"Reals: 500k, violations={rv}, minA={rmin}")
