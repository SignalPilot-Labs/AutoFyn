import sympy as sp

x, theta, b, c, alpha0 = sp.symbols('x theta b c alpha0', real=True, positive=True)

p = (b*sp.cos(2*theta) - c*sp.cos(alpha0))/2
q = -(b*sp.sin(2*theta) + c*sp.sin(alpha0))/2
D = b/2 - c*sp.cos(alpha0) + sp.Rational(1,2)*c*sp.cos(alpha0+2*theta)

R2 = sp.simplify(p**2+q**2)
print("R^2 =", R2, " i.e. 4R^2=", sp.simplify(4*R2))

Dsimpl = sp.simplify(D)
print("D =", Dsimpl)

# Solve p*cos2x + q*sin2x = -D  for 2x, i.e cos(2x - psi) = -D/R with tan(psi)=q/p... let's just verify numerically instead.
import random
vals = {b:3.0, c:5.0, alpha0:1.1}
for _ in range(3):
    th = random.uniform(0.1,0.5)
    pv = float(p.subs(vals).subs(theta,th))
    qv = float(q.subs(vals).subs(theta,th))
    Dv = float(Dsimpl.subs(vals).subs(theta,th))
    R = (pv**2+qv**2)**0.5
    print("theta=",th,"p,q,D,R:",pv,qv,Dv,R, "  D/R=", Dv/R)
