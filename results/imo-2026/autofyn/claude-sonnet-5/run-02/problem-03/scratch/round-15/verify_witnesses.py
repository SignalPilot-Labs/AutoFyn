from fractions import Fraction as F

def A(vals):
    s = sorted(vals, reverse=True)
    a = F(0); sign=1
    for v in s:
        a += sign*v; sign=-sign
    return a

def phi(vals):
    return (sum(vals)+A(vals))/2

# n=3 witness, exact fractions (using outline-reviewer's exact split, but we just need p_i as fractions)
p1,p2,p3,p4 = F(4468,10000), F(2591,10000), F(2251,10000), F(691,10000)
T = p1+p2+p3+p4
print("n=3 witness T=",T, "(should be close to 1, not exactly 1 since these are rounded decimals)")
p1,p2,p3,p4 = p1/T,p2/T,p3/T,p4/T
T=F(1)
a3 = F(8,15)

# construct explicit legal split realizing the sign pattern p1a>p2>p1b>p3a>p4>p3b
# choose p1a close to p1, p1b small but > p3a; p3a between p4 and p1b
# use same exact split as outline-reviewer found
a = F(2101077,12500000)  # p1a? let's check magnitude vs p1
b = F(3483923,12500000)
c = F(817113,12500000)
d = F(1996637,12500000)
print("a+b vs p1:", a+b, p1, a+b==p1)
