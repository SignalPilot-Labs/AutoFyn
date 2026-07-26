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

print("=== D0 irreducibility over Q(b,u,v,lx)[ly] (cubic in ly) ===")
P_D0=sp.Poly(D0, ly, domain=sp.QQ.frac_field(b,u,v,lx))
print("D0 as poly in ly:", P_D0.all_coeffs())
# factor over the function field
fac = sp.factor(D0, domain=sp.QQ.frac_field(b,u,v,lx))
print("factor(D0) over QQ(b,u,v,lx):", fac)
# Also try as a bivariate poly
fac2 = sp.factor(D0)
print("factor(D0) (default):", fac2)

print("\n=== Confirm prefactor, R, et2 not divisible by D0 ===")
# prefactor
pref = (b**8/16)*v**2*(u**2+v**2)*(u**2+v**2-b**2)
P_pref=sp.Poly(sp.expand(pref), ly, domain=sp.QQ.frac_field(b,u,v,lx))
q_p, r_p = sp.div(P_pref, P_D0)
print("prefactor mod D0 zero? (should be False -- prefactor is constant in ly)", r_p.is_zero)

# R (from resultant factorisation)
Rexpr = (-b**2*u**2 - b**2*v**2 - 3*b*lx**2*u - 3*b*lx*ly*v + 4*b*lx*u**2
         + b*lx*v**2 + 3*b*ly*u*v - b*u**3 - b*u*v**2 + 9*lx**2*u**2
         + 18*lx*ly*u*v - 12*lx*u**3 - 12*lx*u*v**2 + 9*ly**2*v**2
         - 12*ly*u**2*v - 12*ly*v**3 + 4*u**4 + 8*u**2*v**2 + 4*v**4)
P_R=sp.Poly(sp.expand(Rexpr), ly, domain=sp.QQ.frac_field(b,u,v,lx))
q_R, r_R = sp.div(P_R, P_D0)
print("R mod D0 zero? (should be False)", r_R.is_zero)

# et2
e3_sub=sp.expand(e3.subs({kx:b+t*b1c,ky:t*(-a1)}))
P_e3=sp.Poly(e3_sub,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
_,r3=sp.div(P_e3,P_D0)
e3_line=sp.expand(r3.as_expr())
et2=sp.expand(sp.Poly(e3_line,t).nth(2))
P_et2=sp.Poly(et2, ly, domain=sp.QQ.frac_field(b,u,v,lx))
q_e, r_e = sp.div(P_et2, P_D0)
print("et2 mod D0 zero? (should be False)", r_e.is_zero)
print("et2 mod D0 =", sp.factor(r_e.as_expr()))

print("\n=== exact resultant prefactor + R / 16 structure (reconfirm) ===")
# recompute res and factor once more
et1=sp.expand(sp.Poly(e3_line,t).nth(1)); et0=sp.expand(sp.Poly(e3_line,t).nth(0))
Q_sub=sp.expand(Q.subs({kx:b+t*b1c,ky:t*(-a1)}))
P_Q=sp.Poly(Q_sub,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
_,rQ=sp.div(P_Q,P_D0)
Q_line=sp.expand(rQ.as_expr())
Qt2=sp.expand(sp.Poly(Q_line,t).nth(2))
P_e3t=sp.Poly(e3_line, t, domain=sp.QQ.frac_field(b,u,v,lx,ly))
P_Qt=sp.Poly(Q_line, t, domain=sp.QQ.frac_field(b,u,v,lx,ly))
res=sp.simplify(sp.resultant(P_e3t, P_Qt))
print("res factored:", sp.factor(res))
# verify res = pref * D0^2 * R
claim = sp.expand(pref * D0**2 * Rexpr)
print("pref*D0^2*R == res?", sp.simplify(sp.together(res-claim))==0)
