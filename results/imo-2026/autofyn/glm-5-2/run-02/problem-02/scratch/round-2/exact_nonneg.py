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
P_e3=sp.Poly(e3_sub,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
P_D0=sp.Poly(D0,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
_,r3=sp.div(P_e3,P_D0)
e3_line=sp.expand(r3.as_expr())
et2=sp.expand(sp.Poly(e3_line,t).nth(2))
et1=sp.expand(sp.Poly(e3_line,t).nth(1))
et0=sp.expand(sp.Poly(e3_line,t).nth(0))
Delta=sp.expand(et1**2-4*et2*et0)
P_Delta=sp.Poly(Delta,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
_,rD=sp.div(P_Delta,P_D0)
Delta_red=sp.expand(rD.as_expr())

# Specialize b=1, u=0, v=2, lx=-2
spec={b:sp.Rational(1),u:sp.Rational(0),v:sp.Rational(2),lx:sp.Rational(-2)}
D0_pt=sp.expand(D0.subs(spec))
Delta_pt=sp.expand(Delta_red.subs(spec))   # quadratic in ly (remainder mod cubic, deg<=2)
print("D0(b=1,u=0,v=2,lx=-2) =",D0_pt,"  (as a function of ly)")
print("Delta_red(b=1,u=0,v=2,lx=-2) =",Delta_pt,"  (quadratic in ly)")
# Verify D0_pt is a cubic in ly with sign change between 1 and 2
P_D0pt=sp.Poly(D0_pt,ly)
print("\nD0 as poly in ly, coeffs:",P_D0pt.all_coeffs())
print("D0 at ly=1:", D0_pt.subs({ly:sp.Rational(1)}), " (<0?)")
print("D0 at ly=2:", D0_pt.subs({ly:sp.Rational(2)}), " (>0?)")
# IVT -> real root ly0 in (1,2)
# Delta_red at that root: the quadratic Delta_pt is <0 for all real ly iff
# leading coeff <0 and discriminant <0 (no real roots, always negative).
P_Dpt=sp.Poly(Delta_pt,ly)
print("\nDelta_red quadratic: coeffs (a,b,c) =",P_Dpt.all_coeffs())
a_q,b_q,c_q = [sp.Rational(c) for c in P_Dpt.all_coeffs()]
disc_q = sp.expand(b_q**2 - 4*a_q*c_q)
print("quadratic discriminant =", disc_q, " (<0 ? -> no real roots)")
print("value at ly=0:", c_q, " (sign of the quadratic everywhere)")
print("leading coeff a =", a_q)
# If a<0 and disc<0 -> quadratic always negative. (leading<0, no roots => always negative)
print("\nConclusion: a<0 and disc<0 => quadratic always <0 for all real ly.")
print("=> at the real root ly0 in (1,2) of D0=0 (cubic), Delta_red(lx=-2,ly0)<0.")
print("=> Delta_red is NOT a square in K=Q(b,u,v,lx,ly)/(D0).")

# Cross-check: compute the ACTUAL discriminant Delta (unreduced) at lx=-2, mod cubic, equals Delta_pt
# i.e. Delta(-2,ly) mod D0(-2,ly) == Delta_pt. Verify:
Delta_spec_full = sp.expand(Delta.subs(spec))
P_full=sp.Poly(Delta_spec_full, ly, domain=sp.QQ)
P_cub=sp.Poly(D0_pt, ly, domain=sp.QQ)
_, rem = sp.div(P_full, P_cub)
print("\nCross-check: Delta(lx=-2,ly) mod D0(lx=-2,ly) (over QQ) =",
      sp.expand(rem.as_expr()), "== Delta_red?", sp.simplify(rem.as_expr()-Delta_pt)==0)
