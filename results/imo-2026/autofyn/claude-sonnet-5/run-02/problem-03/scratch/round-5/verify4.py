from fractions import Fraction as F

def A(S):
    S = sorted(S, reverse=True)
    return sum((-1)**i * S[i] for i in range(len(S)))

# dyadic-band-occupancy counterexample, n=4
n=4
D=31
p1=F(16,31); p2=F(8,31); p3=F(4,31); p4=F(2,31); p5=F(1,31)
T=[p2,p3,p4,p5]
x0 = p2 + F(1,1000)
a1 = F(9969,77500); b1=F(19907,155000)
a2 = F(39969,310000); b2=F(39721,310000)
print("sum check split1:", x0+a1+b1, p1, x0+a1+b1==p1)
print("sum check split2:", x0+a2+b2, p1, x0+a2+b2==p1)
print("a1,b1 in band(2/31,4/31)?", p4<a1<p3, p4<b1<p3)
print("a2,b2 in band(2/31,4/31)?", p4<a2<p3, p4<b2<p3)

A1 = A([x0,a1,b1]+T)
A2 = A([x0,a2,b2]+T)
print("A1=",A1,"expect 3781/38750:", F(3781,38750), A1==F(3781,38750))
print("A2=",A2,"expect 15031/155000:", F(15031,155000), A2==F(15031,155000))
print("A1 != A2 ?", A1!=A2)
