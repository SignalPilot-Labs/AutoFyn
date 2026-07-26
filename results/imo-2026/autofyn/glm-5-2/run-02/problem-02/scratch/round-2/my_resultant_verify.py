"""
Independent verification of analytic-resultant-cert's key claims:
1. res_t(e3_line, Q_line) factors with D0^2 exact (multiplicity 2).
2. D0 irreducible over Q(b,u,v,lx)[ly].
3. Non-split Lemma 9: at b=1,u=0,v=2,lx=-2, D0 becomes 2ly^3-6ly^2+12ly-12
   (real root in (1,2)), and Delta_red = -101/4 ly^2 + 89 ly - 175/2
   (discriminant -1833/2 < 0, leading coeff < 0 => < 0 for all real ly).
4. The norm identity res = et2^2 * Q_line(t1)*Q_line(t2) sign/magnitude.
"""
import sympy as sp

b, u, v, lx, ly, t = sp.symbols('b u v lx ly t')
kx, ky = sp.symbols('kx ky')
A = (0,0); Bpt=(b,0); Cpt=(u,v); M=(b/2,0); Npt=(u/2,v/2)
def sub(P,d): return (P[0]-d[0], P[1]-d[1])
def cross(p,q): return p[0]*q[1]-p[1]*q[0]
def dot(p,q): return p[0]*q[0]+p[1]*q[1]
K=(kx,ky); L=(lx,ly)
BK=sub(K,Bpt); BA=sub(A,Bpt); CA=sub(A,Cpt); CL=sub(L,Cpt)
e1=sp.expand(cross(BK,BA)*dot(CA,CL)-cross(CA,CL)*dot(BK,BA))
BL=sub(L,Bpt); BK2=sub(K,Bpt); NL=sub(L,Npt); NC=sub(Cpt,Npt)
e2=sp.expand(cross(BL,BK2)*dot(NL,NC)-cross(NL,NC)*dot(BL,BK2))
CL3=sub(L,Cpt); CK=sub(K,Cpt); MB=sub(Bpt,M); MK=sub(K,M)
e3=sp.expand(cross(CL3,CK)*dot(MB,MK)-cross(MB,MK)*dot(CL3,CK))
Ksq=kx**2+ky**2; Lsq=lx**2+ly**2; Csq=u**2+v**2; Bsq=b**2
detKL=kx*ly-ky*lx
Q=sp.expand(2*(Ksq*ly-Lsq*ky)*(u-b)+2*(kx*Lsq-lx*Ksq)*v-detKL*(Csq-Bsq))

sx,sy=sp.symbols('sx sy')
e1s=sp.expand(e1.subs({kx:b+sx,ky:sy})); e2s=sp.expand(e2.subs({kx:b+sx,ky:sy}))
a1=sp.expand(e1s.coeff(sx,1)); b1c=sp.expand(e1s.coeff(sy,1))
a2=sp.expand(e2s.coeff(sx,1)); b2c=sp.expand(e2s.coeff(sy,1))
D=sp.expand(a1*b2c-b1c*a2)
D0=sp.expand((b*lx*v-b*ly*u+2*lx**2*ly-lx**2*v-2*lx*ly*u+2*ly**3-3*ly**2*v+ly*u**2+ly*v**2))
assert sp.simplify(D+(b/4)*(u**2+v**2)*D0)==0
kx_sub=b+t*b1c; ky_sub=t*(-a1)
e3_sub=sp.expand(e3.subs({kx:kx_sub,ky:ky_sub}))
Q_sub=sp.expand(Q.subs({kx:kx_sub,ky:ky_sub}))
F=sp.QQ.frac_field(b,u,v,lx,t)
P_e3=sp.Poly(e3_sub,ly,domain=F); P_Q=sp.Poly(Q_sub,ly,domain=F); P_D0=sp.Poly(D0,ly,domain=F)
_,r3=sp.div(P_e3,P_D0); _,rQ=sp.div(P_Q,P_D0)
e3_line=sp.expand(r3.as_expr()); Q_line=sp.expand(rQ.as_expr())
et2=sp.expand(sp.Poly(e3_line,t).nth(2))
et1=sp.expand(sp.Poly(e3_line,t).nth(1))
et0=sp.expand(sp.Poly(e3_line,t).nth(0))
Qt2=sp.expand(sp.Poly(Q_line,t).nth(2))

print("=== 1. Resultant res_t(e3_line, Q_line) ===")
G2=sp.QQ.frac_field(b,u,v,lx,ly)
P_e3_t=sp.Poly(e3_line,t,domain=G2); P_Q_t=sp.Poly(Q_line,t,domain=G2)
res=sp.simplify(sp.resultant(P_e3_t,P_Q_t))
res_fact=sp.factor(res)
print("res factored:")
print(res_fact)

# Check D0^2 | res exactly (field division over Q(b,u,v,lx)[ly])
F2=sp.QQ.frac_field(b,u,v,lx)
P_res=sp.Poly(sp.together(res),ly,domain=F2)
P_D0sq=sp.Poly(sp.expand(D0**2),ly,domain=F2)
q_r,r_r=sp.div(P_res,P_D0sq)
print("res mod D0^2 zero?", r_r.is_zero)
if r_r.is_zero:
    R=sp.simplify(q_r.as_expr())
    # check R mod D0 nonzero
    P_R=sp.Poly(sp.together(R),ly,domain=F2)
    _,rR=sp.div(P_R,sp.Poly(D0,ly,domain=F2))
    print("R = res/D0^2 ; R mod D0 zero?", rR.is_zero, "(should be False => exact mult 2)")
    # check claimed prefactor
    pref=(b**8/16)*v**2*(u**2+v**2)*(u**2+v**2-b**2)
    print("R/pref factored:", sp.factor(sp.simplify(R/pref)))

print("\n=== 2. D0 irreducible over Q(b,u,v,lx)[ly] ===")
# factor over the field
fD0=sp.factor(D0, domain=sp.QQ.frac_field(b,u,v,lx))
print("factor(D0) over Q(b,u,v,lx):", fD0)
# cross-check specialization b=1,u=0,v=2,lx=-2
D0s=sp.expand(D0.subs({b:1,u:0,v:2,lx:-2}))
print("D0 at b=1,u=0,v=2,lx=-2:", D0s, " =", sp.factor(D0s))

print("\n=== 3. Non-split specialization ===")
Delta=sp.expand(et1**2-4*et2*et0)
P_Delta=sp.Poly(Delta,ly,domain=F)
_,rD=sp.div(P_Delta,P_D0)
Delta_red=sp.expand(rD.as_expr())
print("Delta_red mod D0 zero?", rD.is_zero, "(should be False => unramified)")
# specialize b=1,u=0,v=2,lx=-2
Dr_s=sp.expand(Delta_red.subs({b:1,u:0,v:2,lx:-2}))
print("Delta_red at b=1,u=0,v=2,lx=-2 (BEFORE mod D0_s):", sp.factor(Dr_s))
# reduce mod D0_s = 2ly^3-6ly^2+12ly-12
D0s_poly=sp.Poly(D0s,ly,domain=sp.QQ)
Dr_s_poly=sp.Poly(sp.expand(Dr_s),ly,domain=sp.QQ)
_,Dr_red=sp.div(Dr_s_poly,D0s_poly)
Dr_final=sp.expand(Dr_red.as_expr())
print("Delta_red at spec, reduced mod D0_s:", Dr_final)
# discriminant of this quadratic in ly
P=sp.Poly(Dr_final,ly)
if P.degree()==2:
    a_=P.nth(2); b_=P.nth(1); c_=P.nth(0)
    disc=b_**2-4*a_*c_
    print(f"quadratic: a={a_}, b={b_}, c={c_}")
    print(f"discriminant = {disc} = {float(disc)}")
    print(f"leading coeff sign: {float(a_)}, discrim sign: {float(disc)}")
    # check D0_s real root in (1,2)
    f1=float(D0s.subs({ly:1})); f2=float(D0s.subs({ly:2}))
    print(f"D0_s at ly=1: {f1}, at ly=2: {f2} (sign change => real root in (1,2))")
    # value of Dr_final at, say, ly=1.5
    print(f"Dr_final at ly=1.5: {float(Dr_final.subs({ly:sp.Rational(3,2)}))}")

print("\n=== 4. Norm identity sign check ===")
# res = et2^2 * Q_line(t1)*Q_line(t2)  (deg f=deg g=2, sign +)
# verify: res * (some) == et2^2 * product; hard symbolically, check the formula
# lc(e3_line)=et2, so res_t(f,g) = lc(f)^deg(g) * prod g(roots of f) = et2^2 * g(t1)g(t2)
print("lc(e3_line)=et2, deg Q_line=2, deg e3_line=2, even => sign +. Norm identity standard.")
