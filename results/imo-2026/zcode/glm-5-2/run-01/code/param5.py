import sympy as sp
from sympy import symbols, cos, sin, tan, simplify, trigsimp, expand_trig, Rational, sqrt, expand, factor, together, cancel, fu, FU

R = symbols('R', positive=True)
th = symbols('theta', positive=True)
a,b,g = symbols('a b g', positive=True)

SK = (R*sin(a+g) - sin(a+g+th))/sin(2*a+g+th)
SL = (R*sin(a) - sin(a+th))/sin(2*a+b+th)
Kx = 1 - SK*cos(a); Ky = SK*sin(a)
Lx = 1 - SL*cos(a+b); Ly = SL*sin(a+b)
Mx=Rational(1,2); My=0
Nx = R*cos(th)/2; Ny = R*sin(th)/2
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def dot(u,v): return u[0]*v[0]+u[1]*v[1]

NL = (Lx-Nx, Ly-Ny); NC=(R*cos(th)-Nx, R*sin(th)-Ny)
condA = expand(cross(NL,NC) - dot(NL,NC)*tan(b))
MB = (Rational(1,2), 0); MK = (Kx-Mx, Ky-My)
condB = expand(cross(MB,MK) - dot(MB,MK)*tan(g))

# Multiply condA by sin(2a+b+th) to clear that denom; simplify
from sympy import fraction
condA2 = trigsimp(fu(fu(expand(condA*sin(2*a+b+th)*4*cos(b)))))
condB2 = trigsimp(fu(fu(expand(condB*sin(2*a+g+th)*4*cos(g)))))
print("condA*4 cos b sin(2a+b+th):")
sp.pprint(condA2)
print()
print("condB*4 cos g sin(2a+g+th):")
sp.pprint(condB2)
print()

# Now compute OM^2 - ON^2 and reduce using these two relations (treat as linear in tan(b), tan(g)?)
# Actually let's express the target.
ox,oy = symbols('ox oy')
# circumcenter of A=(0,0),K,L: solve ox*Kx+oy*Ky=(Kx^2+Ky^2)/2, ox*Lx+oy*Ly=(Lx^2+Ly^2)/2
seq=[ox*Kx+oy*Ky-(Kx**2+Ky**2)/2, ox*Lx+oy*Ly-(Lx**2+Ly**2)/2]
sol=sp.solve(seq,[ox,oy])
ox=sol[ox]; oy=sol[oy]
OM2=(ox-Rational(1,2))**2+oy**2
ON2=(ox-Nx)**2+(oy-Ny)**2
diff=expand(OM2-ON2)
diff=simplify(diff)
print("OM^2-ON^2 raw simplified:")
print(diff)
