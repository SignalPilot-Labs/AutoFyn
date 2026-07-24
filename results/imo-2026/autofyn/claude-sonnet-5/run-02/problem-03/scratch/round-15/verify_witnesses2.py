from fractions import Fraction as F

def A(vals):
    s = sorted(vals, reverse=True)
    a = F(0); sign=1
    for v in s:
        a += sign*v; sign=-sign
    return a

def phi(vals):
    return (sum(vals)+A(vals))/2

# n=3 witness (use exact fractions matching the reported decimals to reasonable precision, normalize to T=1 exactly)
p1,p2,p3,p4 = F(4468,10000), F(2591,10000), F(2251,10000), F(691,10000)
T = p1+p2+p3+p4
p1,p2,p3,p4 = [x/T for x in (p1,p2,p3,p4)]
T = p1+p2+p3+p4
assert T==1
a3 = F(8,15)
print("n=3: p1..p4 =", p1,p2,p3,p4, "sum", T, "a3T=",a3)

# Construct our own split realizing p1a>p2>p1b>p3a>p4>p3b, using j=2 alternating cross-bisect construction
# Need: max(p2, p1-p2) < f1 < p1  for p1's split (f1=p1a, p1-f1=p1b), want p1b < p2 i.e. f1 > p1-p2, and f1>p2 (p1a>p2)
lo1 = max(p2, p1-p2)
assert lo1 < p1
f1 = (lo1 + p1)/2   # midpoint, guaranteed in range
p1a, p1b = f1, p1-f1
print("p1a,p1b=",p1a,p1b, "check p1a>p2>p1b:", p1a>p2>p1b)

# Need p3 split: max(p4, p3-p4) < f3 < p3, want p3a < p1b and p3a > p4 (p3a in (p4, p1b)), and p3b<p4
lo3 = max(p4, p3-p4)
hi3 = min(p3, p1b)
assert lo3 < hi3, (lo3,hi3)
f3 = (lo3+hi3)/2
p3a, p3b = f3, p3-f3
print("p3a,p3b=",p3a,p3b, "check p1b>p3a>p4>p3b:", p1b>p3a>p4>p3b)

vals = [p1a,p1b,p2,p3a,p3b,p4]
Phi = phi(vals)
predicted = (T + p1-p2-p3+p4)/2
print("Phi actual=",Phi," predicted=",predicted," equal:",Phi==predicted)
print("Phi vs a3T:", Phi, a3, Phi<a3)
