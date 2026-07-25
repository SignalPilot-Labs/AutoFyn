import sympy as sp

t1,s2,beta,a,b,cc = sp.symbols('t1 s2 beta a b cc', real=True)
cosb, sinb = sp.cos(beta), sp.sin(beta)

A = sp.Matrix([0,0]); B = sp.Matrix([a,0]); C = sp.Matrix([b,cc])
M = (A+B)/2; N = (A+C)/2
Rbeta = sp.Matrix([[cosb,-sinb],[sinb,cosb]])
K = B + t1*sp.Matrix([-cosb, sinb])
L = C + s2*Rbeta*(A-C)

def dot(V1,V2):
    return sp.trigsimp(sp.expand(V1.dot(V2)))

BL = L-B; BK = K-B
NL = L-N; NC = C-N
CL = L-C; CK = K-C
MB = B-M; MK = K-M

print("MB.MK =", sp.simplify(dot(MB,MK)))
print("NL.NC =", sp.simplify(dot(NL,NC)))
print()
d_LBK = sp.simplify(dot(BL,BK))
d_LCK = sp.simplify(dot(CL,CK))
print("BL.BK =", d_LBK)
print()
print("CL.CK =", d_LCK)
