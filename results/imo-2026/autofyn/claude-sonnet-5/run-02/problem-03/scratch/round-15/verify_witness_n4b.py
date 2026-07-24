from fractions import Fraction as F

def A(vals):
    s = sorted(vals, reverse=True)
    a = F(0); sign=1
    for v in s:
        a += sign*v; sign=-sign
    return a

def phi(vals):
    return (sum(vals)+A(vals))/2

p1,p2,p3,p4,p5 = F(2933,10000),F(2514,10000),F(2131,10000),F(1338,10000),F(1085,10000)
T = p1+p2+p3+p4+p5
p1,p2,p3,p4,p5 = [x/T for x in (p1,p2,p3,p4,p5)]
T = p1+p2+p3+p4+p5
a4 = F(16,31)

r = (p1-p3)/2
frag_tie = p3
frag_pair = r

lo = p5
hi = min(p4, p2-p4)
assert lo<hi, (lo,hi)
b = (lo+hi)/2
a = p2-b
print("a,b=",a,b,"a>p4>b>p5:", a>p4>b>p5)

final = [frag_tie, frag_pair, frag_pair, a, b, p3, p4, p5]
Phi = phi(final)
predicted = (T + p2 - p4 - p5)/2
print("Phi actual=",Phi,float(Phi)," predicted=",predicted,float(predicted),"equal:",Phi==predicted)
print("vs a4T:", float(Phi), float(a4), Phi<a4)
print("sorted:", sorted([float(x) for x in final], reverse=True))
