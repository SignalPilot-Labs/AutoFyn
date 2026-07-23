import sympy as sp

x, theta, b, c, alpha0 = sp.symbols('x theta b c alpha0', real=True)

A = sp.Matrix([0,0])
B = sp.Matrix([c,0])
C = sp.Matrix([b*sp.cos(alpha0), b*sp.sin(alpha0)])

k = c*sp.sin(theta)/sp.sin(x+theta)
K = sp.Matrix([k*sp.cos(x), k*sp.sin(x)])
K1 = B - K

def concyclic_det(P,Q,R,S):
    rows = []
    for X in [P,Q,R,S]:
        rows.append([X[0], X[1], X[0]**2+X[1]**2, 1])
    return sp.Matrix(rows).det()

det = concyclic_det(A,K,C,K1)
det_simpl = sp.simplify(det)
print("raw det simplified:")
sp.pprint(det_simpl)
