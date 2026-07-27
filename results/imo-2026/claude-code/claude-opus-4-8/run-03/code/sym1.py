import sympy as sp

B,C,beta,delta,gamma=sp.symbols('B C beta delta gamma',positive=True)
a=sp.Integer(1)
A=sp.pi-B-C

def apex(thetaB,thetaC):
    # triangle base B=(-a,0), C=(a,0), base angles thetaB at B, thetaC at C. Return apex (x,y).
    BK=2*a*sp.sin(thetaC)/sp.sin(thetaB+thetaC)
    x=-a+BK*sp.cos(thetaB)
    y=BK*sp.sin(thetaB)
    return sp.Matrix([x,y])

# A apex with base angles B, C
Apt=apex(B,C)
# K apex with base angles (B-beta),(C-beta-delta)
Kpt=apex(B-beta, C-beta-delta)
# L apex with base angles (B-beta-gamma),(C-beta)
Lpt=apex(B-beta-gamma, C-beta)

def hval(X):
    # h = X_y + X_x*(A_x-X_x)/(A_y-X_y)
    return X[1]+X[0]*(Apt[0]-X[0])/(Apt[1]-X[1])

hK=sp.simplify(hval(Kpt))
print("hK=",hK)
