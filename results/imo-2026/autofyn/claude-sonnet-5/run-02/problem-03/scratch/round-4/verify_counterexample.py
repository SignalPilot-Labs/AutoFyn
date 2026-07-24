from fractions import Fraction as F

def phi(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

p,q,r,s = F(3,8), F(1,4), F(1,4), F(1,8)
assert p+q+r+s == 1
target = F(8,15)

# T1: bisect p
T1 = phi([p/2,p/2,q,r,s])
# T2: bisect p,q
T2 = phi([p/2,p/2,q/2,q/2,r,s])
# T3: bisect p,q,r
T3 = phi([p/2,p/2,q/2,q/2,r/2,r/2,s])
# D1: bisect s
D1 = phi([p,q,r,s/2,s/2])
# D2: bisect r,s
D2 = phi([p,q,r/2,r/2,s/2,s/2])
# D3: bisect q,r,s
D3 = phi([p,q/2,q/2,r/2,r/2,s/2,s/2])
# trisect p equally (composition (2,0,0,0), equal thirds)
Tri = phi([p/3,p/3,p/3,q,r,s])

print("p,q,r,s =",p,q,r,s)
print("T1",T1,"T2",T2,"T3",T3,"D1",D1,"D2",D2,"D3",D3,"Tri",Tri)
print("min of these:", min(T1,T2,T3,D1,D2,D3,Tri), " target:",target)
print("as floats:", float(min(T1,T2,T3,D1,D2,D3,Tri)), float(target))
