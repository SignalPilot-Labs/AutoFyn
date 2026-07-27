import sympy as sp, sys, time, math
from sympy import symbols,together,fraction,expand,cancel,groebner,prem,div,Poly,sqrt
log=print
def flush(): sys.stdout.flush()

sa,ca,sb,cb,sg,cg,sA,cA = sp.symbols('sa ca sb cb sg cg sA cA')
# trig atoms
saa=sa*cA+ca*sA; caa=ca*cA-sa*sA          # sin/cos(alpha+A)? wait sin(al+A)=sa*cA+ca*sA ; cos(al+A)=ca*cA-sa*sA
sag=saa*cg+caa*sg; cag=caa*cg-saa*sg        # sin/cos(al+A+ga)
sab=saa*cb+caa*sb; cab=caa*cb-saa*sb        # sin/cos(al+A+be)  -- wait sin(al+A+be)=sin(al+A)cb+cos(al+A)sb
# careful: sin(al+A) = saa, so sin(al+A+be)=saa*cb+caa*sb ; cos=caa*cb-saa*sb. ok
sA2ag = (saa*cg+caa*sg)  # = sin(al+A+ga) = sag already. We need sin(A+2al+ga):
# sin(A+2al+ga) = sin((A+al)+(al+ga)). sin(A+al)=saa, cos(A+al)=caa. sin(al+ga)=sa*cg+ca*sg, cos(al+ga)=ca*cg-sa*sg
salag=sa*cg+ca*sg; calag=ca*cg-sa*sg
sA2ag=saa*calag+caa*salag                  # sin(A+2al+ga)
sA2ab=saa*(ca*cb-sa*sb)+caa*(sa*cb+ca*sb)   # sin(A+2al+be): cos(al+be)=ca*cb-sa*cb? no cos(al+be)=ca*cb-sa*sb ; sin(al+be)=sa*cb+ca*sb
sAag=sag  # sin(A+al+ga)=sag
sAab=sab  # sin(A+al+be)=sab

# K = BK(pi-al) ∩ MK(ga), with B=(c,0) set c=1, M=(1/2,0).
# Param in prior rounds (scan.py): kx=1-sg*ca/(2*sag); ky=sg*sa/(2*sag)  -- uses c=1.
# Let me recompute K generally with c=1.
# Line BK from B=(1,0) dir (pi-al): direction (-cos al, sin al)=(-ca, sa). point: (1,0)+u*(-ca,sa)
# Line MK from M=(1/2,0) dir ga: (cos ga, sin ga)=(cg,sg). point: (1/2,0)+v*(cg,sg)
# solve: 1-u*ca = 1/2 + v*cg ; u*sa = v*sg.  v=u*sa/sg. 1-u*ca=1/2+u*sa*cg/sg => 1/2 = u*ca + u*sa*cg/sg = u*(ca+sa*cg/sg)=u*(ca*sg+sa*cg)/sg = u*sin(al+ga)/sg = u*sag/sg
# u = sg/(2*sag). Kx=1-u*ca=1-sg*ca/(2*sag); Ky=u*sa=sg*sa/(2*sag). OK matches.
kx=1-sg*ca/(2*sag); ky=sg*sa/(2*sag)
# L = CL(A+pi+al) ∩ NL(A-be), C=(b cA, b sA) set b kept; N=(b cA/2, b sA/2).
# scan.py: lx=cA - sb*cAa/(2*sab); ly=sA - sb*sAa/(2*sab)  with cAa=cos(A+al)=caa, sAa=sin(A+al)=saa
# This is with b=1. We'll keep b symbolic -> multiply. Actually K,L homogeneous: K depends on c (=1), L on b.
# With b symbolic: L = b*(lx_unit, ly_unit) where lx_unit=cA - sb*caa/(2*sab); ly_unit=sA - sb*saa/(2*sab)
lxu=cA - sb*caa/(2*sab); lyu=sA - sb*saa/(2*sab)
# So with c=1: B=(1,0), C=(b*cA,b*sA), K=(kx,ky) (c=1), L=b*(lxu,lyu)
# A' solves A'.K=|K|^2, A'.L=|L|^2.  A' linear in b. Let me compute symbolically keeping b.
b = sp.symbols('b')
Kx,Ky=kx,ky
Lx,Ly=b*lxu,b*lyu
K2=sp.cancel(Kx**2+Ky**2); L2=sp.cancel(Lx**2+Ly**2)
detKL=sp.cancel(Kx*Ly-Ky*Lx)
Ax=sp.cancel((Ly*K2-Ky*L2)/detKL); Ay=sp.cancel((Kx*L2-Lx*K2)/detKL)
log("A' assembled ops",sp.count_ops(Ax),sp.count_ops(Ay)); flush()
# B=(1,0), C=(b*cA,b*sA). theta=pi/2-A-al. R_theta(C-B):
# cos(pi/2-A-al)=sin(A+al)=saa ; sin(pi/2-A-al)=cos(A+al)=caa
# R_th(C-B): (cos th * (C-B)_x - sin th*(C-B)_y, sin th*(C-B)_x + cos th*(C-B)_y)
CBx=b*cA-1; CBy=b*sA
Rx=saa*CBx - caa*CBy
Ry=caa*CBx + saa*CBy
ABx=sp.cancel(Ax-1); ABy=sp.cancel(Ay)
G=sp.cancel(ABx*Ry - ABy*Rx)
log("G ops",sp.count_ops(G)); flush()
G=sp.expand(G)
# G is rational in b and the trig atoms. Collect in b.
Gp=sp.Poly(G,b)
log("G degree in b:",Gp.degree()); flush()
for i,co in enumerate(Gp.all_coeffs()):
    log(f"  coeff b^{Gp.degree()-i}: ops {sp.count_ops(co)}"); flush()
