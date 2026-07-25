import sympy as sp

t1,s2,cb,sb,a,b,cc = sp.symbols('t1 s2 cb sb a b cc', real=True)
# cb=cos(beta), sb=sin(beta), with cb**2+sb**2=1 as a side relation

A = sp.Matrix([0,0]); B = sp.Matrix([a,0]); C = sp.Matrix([b,cc])
M = (A+B)/2; N = (A+C)/2
Rbeta = sp.Matrix([[cb,-sb],[sb,cb]])
K = B + t1*sp.Matrix([-cb, sb])
L = C + s2*Rbeta*(A-C)

def dot(V1,V2):
    return sp.expand(V1.dot(V2))

BL=L-B; BK=K-B; NL=L-N; NC=C-N; CL=L-C; CK=K-C; MB=B-M; MK=K-M

def sq(V1,V2,V3,V4):
    lhs=(V1.dot(V2))**2*(V3.dot(V3))*(V4.dot(V4))
    rhs=(V3.dot(V4))**2*(V1.dot(V1))*(V2.dot(V2))
    return sp.expand(lhs-rhs)

eq2 = sq(BL,BK,NL,NC)   # hyp2 angle LBK = angle LNC
eq3 = sq(CL,CK,MB,MK)   # hyp3 angle LCK = angle BMK

# reduce using sb**2 = 1-cb**2 repeatedly won't factor nicely automatically; let's just divide by t1**2
q2, r2 = sp.div(sp.Poly(eq2, t1), sp.Poly(t1**2,t1))
print("r2==0?", r2)
g2 = sp.expand(q2.as_expr())
print("g2 has sb up to power:", sp.degree(sp.Poly(g2, sb)) if sb in g2.free_symbols else 0)

q3, r3 = sp.div(sp.Poly(eq3, s2), sp.Poly(s2**2, s2))
print("r3==0?", r3)
g3 = sp.expand(q3.as_expr())

# Now let's directly attempt: eq for hyp2 is a quadratic in s2 (deg2), and true branch is
# BL.BK/|BK| ... actually simpler: the TRUE (unsquared) hypothesis is
#   (BL.BK)*|NL|*|NC| = (NL.NC)*|BL|*|BK|      [could be + or - depending sign of both sides... actually both dot products can be any sign]
# Let's directly derive the *branch selection* condition algebraically:
# hyp2 says angle(BL,BK) = angle(NL,NC). This is equivalent to:
#   BL.BK / (|BL||BK|) = NL.NC/(|NL||NC|)   ... i.e. cos of the two angles equal (not just squared)
# Cross-multiplying (all norms positive):  (BL.BK)|NL||NC| = (NL.NC)|BL||BK|
# whereas the "spurious" branch has a sign flip on one side.
# We can test: is BL.BK and NL.NC forced to have the SAME SIGN by the true equation (before squaring)?
print()
print("NL.NC (recap) sign form: -b^2 s2 cb/2 ... etc computed before")
