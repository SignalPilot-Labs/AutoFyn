from fractions import Fraction as F

def A(vals):
    s = sorted(vals, reverse=True)
    a = F(0); sign=1
    for v in s:
        a += sign*v; sign=-sign
    return a

def phi(vals):
    return (sum(vals)+A(vals))/2

p1,p2,p3,p4 = F(4468,10000), F(2591,10000), F(2251,10000), F(691,10000)
T = p1+p2+p3+p4
p1,p2,p3,p4 = [x/T for x in (p1,p2,p3,p4)]
T = p1+p2+p3+p4
a3 = F(8,15)

lo1 = max(p2, p1-p2)
hi1 = p1
# choose f1 close to lo1 (1% of the way toward hi1) to maximize p1b room
f1 = lo1 + (hi1-lo1)*F(1,100)
p1a, p1b = f1, p1-f1
print("p1a,p1b=",p1a,p1b,float(p1a),float(p1b), "check p1a>p2>p1b:", p1a>p2>p1b)

lo3 = max(p4, p3-p4)
hi3 = min(p3, p1b)
print("lo3,hi3", lo3, hi3, float(lo3), float(hi3))
assert lo3 < hi3, (lo3,hi3)
f3 = (lo3+hi3)/2
p3a, p3b = f3, p3-f3
print("p3a,p3b=",p3a,p3b, "check p1b>p3a>p4>p3b:", p1b>p3a>p4>p3b)

vals = [p1a,p1b,p2,p3a,p3b,p4]
Phi = phi(vals)
predicted = (T + p1-p2-p3+p4)/2
print("Phi actual=",Phi,float(Phi)," predicted=",predicted,float(predicted)," equal:",Phi==predicted)
print("Phi vs a3T:", float(Phi), float(a3), Phi<a3)
