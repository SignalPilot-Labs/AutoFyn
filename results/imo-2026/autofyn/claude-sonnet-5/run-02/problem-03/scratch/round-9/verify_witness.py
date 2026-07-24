from fractions import Fraction as F

def phi(S):
    S = sorted(S, reverse=True)
    tot = F(0)
    for i,x in enumerate(S):
        if i%2==0: tot+=x
    return tot

p1,p2,p3,p4 = F(2,5), F(3,10), F(1,5), F(1,10)
T = p1+p2+p3+p4
print("T=",T)

# Theorem D' (bisect p1,p4, recurse optimal on middle {p2,p3})
# middle = {p2,p3}, exact optimum via Theorem A (full match): since p2>=p3, phi_min(middle)=p2 (full match trivial, m'=2)
Phi_mid = p2
val_Dprime = (p1+p4)/2 + Phi_mid
print("Theorem D' value:", val_Dprime, float(val_Dprime))

# Theorem E: bisect p1,p2, recurse on {p3,p4}
Phi_mid2 = p3  # full match m'=2, phi=p3 since p3>=p4
val_E = (p1+p2)/2 + Phi_mid2
print("Theorem E value:", val_E, float(val_E))

# claimed optimal strategy: peel p1 against p4 (Theorem B_k, k=4): cut p1 into (p4, w4=p1-p4), 
# then apply strategy on S'_4 = {w4} U {p2,p3} (since p4 removed, w4 added)
w4 = p1-p4
Sp = [w4, p2, p3]
print("S'_4 =", Sp)
# then bisect p3 (which piece? per description: cutting p3=1/5 into (1/10,1/10))
# w4 = 2/5-1/10=3/10 = matches p2! and p3=2*p4=2/10=1/5 matches.
final = [p2, p2, w4, p3/2, p3/2, p4]  # wait let's just directly build final multiset per description
final = [F(3,10), F(3,10), F(1,10), F(1,10), F(1,10), F(1,10)]
print("final multiset:", final, sum(final))
print("phi(final) =", phi(final))
