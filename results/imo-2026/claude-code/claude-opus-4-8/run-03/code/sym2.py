import sympy as sp
B,C,beta,delta=sp.symbols('B C beta delta',positive=True)
A=sp.pi-B-C
a=sp.Integer(1)  # half-base; BC=2
def apex(tB,tC):
    BK=2*a*sp.sin(tC)/sp.sin(tB+tC)
    return sp.Matrix([-a+BK*sp.cos(tB), BK*sp.sin(tB)])
Apt=apex(B,C)
Kpt=apex(B-beta, C-beta-delta)
P=sp.Matrix([0,0])
def Psi(X):
    return 2*(X-Apt).dot(X-Apt)+(X-sp.Matrix([-a,0])).dot(X-sp.Matrix([-a,0]))+(X-sp.Matrix([a,0])).dot(X-sp.Matrix([a,0]))-(Apt-sp.Matrix([-a,0])).dot(Apt-sp.Matrix([-a,0]))-(Apt-sp.Matrix([a,0])).dot(Apt-sp.Matrix([a,0]))
# Phi = (X-P).(X-A)/cross(C-B, X-A)
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
Bp=sp.Matrix([-a,0]);Cp=sp.Matrix([a,0])
def Phi(X):
    return (X-P).dot(X-Apt)/cross(Cp-Bp, X-Apt)
PhiK=sp.simplify(Phi(Kpt))
print("PhiK (no constraint) =")
sp.pprint(PhiK)

# constraint (I): sinC sinδ sin(A+2β+δ) - 2 sinA sin(β+δ) sin(C-β-δ) = 0
Fc=sp.sin(C)*sp.sin(delta)*sp.sin(A+2*beta+delta)-2*sp.sin(A)*sp.sin(beta+delta)*sp.sin(C-beta-delta)
Fc=sp.simplify(sp.expand_trig(Fc))
print("\nConstraint F=")
sp.pprint(sp.simplify(Fc))
