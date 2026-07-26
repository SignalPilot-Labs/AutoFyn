"""Final cross-checks: norm product identity and a numeric inert-point check."""
import sympy as sp
import numpy as np
b,u,v,lx,ly,t = sp.symbols('b u v lx ly t')
kx,ky = sp.symbols('kx ky')
A=(0,0); Bpt=(b,0); Cpt=(u,v); M=(b/2,0); Npt=(u/2,v/2)
def sub(P,d): return (P[0]-d[0],P[1]-d[1])
def cross(p,q): return p[0]*q[1]-p[1]*q[0]
def dot(p,q): return p[0]*q[0]+p[1]*q[1]
Kp=(kx,ky); Lp=(lx,ly)
BK=sub(Kp,Bpt);BA=sub(A,Bpt);CA=sub(A,Cpt);CL=sub(Lp,Cpt)
e1=sp.expand(cross(BK,BA)*dot(CA,CL)-cross(CA,CL)*dot(BK,BA))
BL=sub(Lp,Bpt);NL=sub(Lp,Npt);NC=sub(Cpt,Npt)
e2=sp.expand(cross(BL,BK)*dot(NL,NC)-cross(NL,NC)*dot(BL,BK))
CK=sub(Kp,Cpt);MB=sub(Bpt,M);MK=sub(Kp,M)
e3=sp.expand(cross(CL,CK)*dot(MB,MK)-cross(MB,MK)*dot(CL,CK))
Ksq=kx**2+ky**2;Lsq=lx**2+ly**2;Csq=u**2+v**2;Bsq=b**2
detKL=kx*ly-ky*lx
Q=sp.expand(2*(Ksq*ly-Lsq*ky)*(u-b)+2*(kx*Lsq-lx*Ksq)*v-detKL*(Csq-Bsq))
sx,sy=sp.symbols('sx sy')
e1s=sp.expand(e1.subs({kx:b+sx,ky:sy}));e2s=sp.expand(e2.subs({kx:b+sx,ky:sy}))
a1=sp.expand(e1s.coeff(sx,1));b1c=sp.expand(e1s.coeff(sy,1))
a2=sp.expand(e2s.coeff(sx,1));b2c=sp.expand(e2s.coeff(sy,1))
D=sp.expand(a1*b2c-b1c*a2);D0=sp.expand(-(4*D)/(b*(u**2+v**2)))
kx_sub=b+t*b1c;ky_sub=t*(-a1)
e3_sub=sp.expand(e3.subs({kx:kx_sub,ky:ky_sub}))
Q_sub =sp.expand(Q.subs({kx:kx_sub,ky:ky_sub}))
P_e3=sp.Poly(e3_sub,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
P_Q =sp.Poly(Q_sub ,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
P_D0=sp.Poly(D0,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
_,r3=sp.div(P_e3,P_D0); _,rQ=sp.div(P_Q,P_D0)
e3_line=sp.expand(r3.as_expr()); Q_line=sp.expand(rQ.as_expr())
et2=sp.expand(sp.Poly(e3_line,t).nth(2))
et1=sp.expand(sp.Poly(e3_line,t).nth(1))
et0=sp.expand(sp.Poly(e3_line,t).nth(0))
Qt2=sp.expand(sp.Poly(Q_line,t).nth(2))

# Norm identity: res = et2^2 * Q_line(t1)*Q_line(t2) (up to sign).
# Verify symbolically via the standard resultant formula for two quadratics.
# res(f,g) for f=a2 t^2+a1 t+a0, g=b2 t^2+b1 t+b0 is:
# a2^2*b0^2 - a2*a1*b0*b1 + a2*a0*(b1^2-2*b0*b2) + a1^2*b0*b2 - a1*a0*b1*b2 + a0^2*b2^2 ... (use sp.resultant)
# Instead verify: res / et2^2 == product Q_line at roots of e3_line, by comparing
# res/et2^2  with  Qt2^2 * et0^2 - Qt2*Qt1*et0*et1 + ... (the resultant of e3_line into Q_line divided by et2^2)
# Standard: res_t(f,g) = a2^deg_g * prod_i g(t_i). So res = et2^2 * Q_line(t1)*Q_line(t2).
# Q_line(t1)*Q_line(t2) = Qt2^2 * t1 t2 stuff... compute via symmetric functions:
# t1+t2 = -et1/et2, t1*t2 = et0/et2.
# Q_line(ti) = Qt2*ti^2 + Qt1*ti + Qt0.
# prod = Qt2^2*(t1t2)^2 + Qt2*Qt1*(t1^2 t2 + t1 t2^2) + ... let's just use resultant of Q into f:
# res_t(f,g) = (-1)^(deg f deg g) * res_t(g,f) = res_t(g,f) (deg 2*2 even).
# res_t(g, f) = Qt2^2 * f(s1)*f(s2) where s1,s2 roots of g. Symmetric.
# Let's just verify numerically at a random specialization that res = et2^2 * Q_line(t1)*Q_line(t2).
P_e3t=sp.Poly(e3_line, t, domain=sp.QQ.frac_field(b,u,v,lx,ly))
P_Qt=sp.Poly(Q_line, t, domain=sp.QQ.frac_field(b,u,v,lx,ly))
res=sp.resultant(P_e3t,P_Qt)

rng=np.random.default_rng(5)
ok=True
for _ in range(8):
    bn=float(rng.uniform(3,7));un=float(rng.uniform(-3,5));vn=float(rng.uniform(3,7))
    lxs=float(rng.uniform(-2,5))
    cc=[2.0,-3*vn,-bn*un+2*lxs**2-2*lxs*un+un**2+vn**2, bn*lxs*vn-lxs**2*vn]
    roots=np.roots(cc)
    real_roots=[r.real for r in roots if abs(r.imag)<1e-6]
    if not real_roots: continue
    lyn=max(real_roots)  # pick one
    e2c=float(et2.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
    if abs(e2c)<1e-9: continue
    # roots of e3_line
    e1c=float(et1.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
    e0c=float(et0.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
    disc=e1c**2-4*e2c*e0c
    if disc<0: continue
    t1=(-e1c+np.sqrt(disc))/(2*e2c); t2=(-e1c-np.sqrt(disc))/(2*e2c)
    # Q_line at t1, t2
    Q1=float(Q_line.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn,t:t1}))
    Q2=float(Q_line.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn,t:t2}))
    resv=float(res.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
    lhs = (e2c**2)*Q1*Q2
    if abs(lhs - resv) > 1e-3*max(1,abs(resv)):
        ok=False; print("MISMATCH", bn,un,vn,lxs,lyn, resv, lhs)
        break
print("Norm identity res = et2^2 * Q_line(t1)*Q_line(t2) verified at random points:", ok)

# Also confirm at the non-split witness specialization b=1,u=0,v=2,lx=-2:
spec={b:sp.Rational(1),u:sp.Rational(0),v:sp.Rational(2),lx:sp.Rational(-2)}
# find real root of D0 in (1,2)
from sympy import nsolve
D0s=sp.Poly(D0.subs(spec),ly)
ly0=sp.nsimplify(sp.nsolve(sp.Poly(D0s.as_expr(),ly).as_expr(),1.5),rational=False)
print("Approx real root ly0 in (1,2):", float(ly0))
print("D0(1,0,2,-2,ly0)=", float(D0.subs(spec).subs({ly:float(ly0)})))
print("Delta_red at ly0:", float((et1**2-4*et2*et0).subs({**spec,ly:float(ly0)})), "(should be <0)")
