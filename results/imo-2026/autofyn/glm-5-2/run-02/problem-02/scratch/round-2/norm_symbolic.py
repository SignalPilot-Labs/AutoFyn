"""Symbolic verification of the norm identity res = et2^2 * Q_line(t1)*Q_line(t2)."""
import sympy as sp
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
Qt1=sp.expand(sp.Poly(Q_line,t).nth(1))
Qt0=sp.expand(sp.Poly(Q_line,t).nth(0))

# Q_line(t1)*Q_line(t2) via symmetric functions: S=t1+t2=-et1/et2, P=t1*t2=et0/et2
S = -et1/et2; P = et0/et2
# prod = Qt2^2 * P^2 + Qt2*Qt1*(P*S) + Qt2*Qt0*(S^2 - 2P) + Qt1^2*P + Qt1*Qt0*S + Qt0^2
prod = (Qt2**2)*(P**2) + (Qt2*Qt1)*(P*S) + (Qt2*Qt0)*((S**2)-(2*P)) + (Qt1**2)*P + (Qt1*Qt0)*S + (Qt0**2)
prod = sp.expand(prod)
norm = sp.expand(et2**2 * prod)   # = et2^2 * Q_line(t1)*Q_line(t2)
# compare with resultant
P_e3t=sp.Poly(e3_line, t, domain=sp.QQ.frac_field(b,u,v,lx,ly))
P_Qt=sp.Poly(Q_line, t, domain=sp.QQ.frac_field(b,u,v,lx,ly))
res=sp.resultant(P_e3t, P_Qt)
diff = sp.simplify(sp.together(sp.expand(res - norm)))
print("res - et2^2*Q_line(t1)*Q_line(t2) == 0 (symbolic)?", diff == 0)
# also check sign (res = + et2^2 * prod or - et2^2*prod?)
print("res + et2^2*prod == 0?", sp.simplify(sp.together(sp.expand(res + norm))) == 0)
