import sympy as sp

t1,s2,u,a,b,cc = sp.symbols('t1 s2 u a b cc', real=True)
sinb = 2*u/(1+u**2); cosb = (1-u**2)/(1+u**2)
A = sp.Matrix([0,0]); B = sp.Matrix([a,0]); C = sp.Matrix([b,cc])
M=(A+B)/2; N=(A+C)/2
Rbeta = sp.Matrix([[cosb,-sinb],[sinb,cosb]])
K = B + t1*sp.Matrix([-cosb,sinb])
L = C + s2*Rbeta*(A-C)

def dot(V1,V2): return sp.expand(V1.dot(V2))
BL=L-B; BK=K-B; NL=L-N; NC=C-N; CL=L-C; CK=K-C; MB=B-M; MK=K-M

def sq(V1,V2,V3,V4):
    lhs=(V1.dot(V2))**2*(V3.dot(V3))*(V4.dot(V4))
    rhs=(V3.dot(V4))**2*(V1.dot(V1))*(V2.dot(V2))
    return sp.expand(lhs-rhs)

eq2 = sq(BL,BK,NL,NC)
q2,r2 = sp.div(eq2, t1**2, t1); assert r2==0
g2 = sp.factor(q2)
print("g2 factored:", g2)
