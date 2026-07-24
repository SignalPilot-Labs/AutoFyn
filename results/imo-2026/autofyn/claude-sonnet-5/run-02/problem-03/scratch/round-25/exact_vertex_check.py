from fractions import Fraction as F
# Candidate exact vertex from LP: p1=2/5, p2=4/15, p3=1/5, p4=2/15
p = (F(2,5), F(4,15), F(1,5), F(2,15))
p1,p2,p3,p4 = p
a3 = F(8,15)
def bisect_f(S):
    idx=[i for i in range(4) if i not in S]
    R=[p[i] for i in idx]
    A=sum((F(1) if k%2==0 else F(-1))*v for k,v in enumerate(R))
    return (F(1)+A)/2
phi14 = bisect_f({0,3})
phi12 = bisect_f({0,1})
print("g14 =", a3-phi14, "g12 =", a3-phi12)
print("p1 vs p2+p3:", p1, p2+p3, "DS-Above/TriplePin feasible?", p1>p2+p3)
print("R22 feas: p1>=2p3?", p1>=2*p3, " p2<=p3+p4?", p2<=p3+p4)
if p1>=2*p3 and p2<=p3+p4:
    phiR22 = p1/2+p3+p4
    print("gR22 =", a3-phiR22)
print("p2 exactly at box wall 4/15?", p2==F(4,15))
