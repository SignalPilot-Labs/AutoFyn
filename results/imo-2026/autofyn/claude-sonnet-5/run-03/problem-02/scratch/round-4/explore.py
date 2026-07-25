import sympy as sp

t1,s2,u,a,b,cc = sp.symbols('t1 s2 u a b cc', real=True, positive=False)

sinb = 2*u/(1+u**2); cosb = (1-u**2)/(1+u**2)
A = sp.Matrix([0,0]); B = sp.Matrix([a,0]); C = sp.Matrix([b,cc])
M = (A+B)/2; N = (A+C)/2
Rbeta = sp.Matrix([[cosb,-sinb],[sinb,cosb]])
K = B + t1*sp.Matrix([-cosb, sinb])
L = C + s2*Rbeta*(A-C)

def dot(V1,V2):
    return sp.expand(V1.dot(V2))

# The four dot products whose sign = acute/obtuse
BL = L-B; BK = K-B
NL = L-N; NC = C-N
CL = L-C; CK = K-C
MB = B-M; MK = K-M

d_LBK = dot(BL,BK)
d_LNC = dot(NL,NC)
d_LCK = dot(CL,CK)
d_BMK = dot(MB,MK)

for name,expr in [("BL.BK",d_LBK), ("NL.NC",d_LNC), ("CL.CK", d_LCK), ("MB.MK", d_BMK)]:
    print(name, "=", sp.factor(expr))
    print()
