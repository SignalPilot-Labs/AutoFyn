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

# Try triangle b=1, u=0, v=2. Scan real points of D0=0 for Delta_red<0.
spec={b:sp.Rational(1),u:sp.Rational(0),v:sp.Rational(2)}
D0s=sp.expand(D0.subs(spec))
Ds=sp.expand(Delta_red.subs(spec))
print("D0(b=1,u=0,v=2) =",D0s)
print("Delta_red(b=1,u=0,v=2) =",Ds)

rng=np.random.default_rng(1)
neg=None
for _ in range(20000):
    lxs=float(rng.uniform(-3,5))
    # cubic in ly: D0s as Poly
    P=sp.Poly(D0s.subs({lx:lxs}),ly)
    cc=[float(c) for c in P.all_coeffs()]
    if len(cc)<4 or abs(cc[0])<1e-12: continue
    roots=np.roots(cc)
    for r in roots:
        if abs(r.imag)<1e-6:
            lyn=r.real
            dv=float(Ds.subs({lx:lxs,ly:lyn}))
            if dv<-0.01:
                neg=(lxs,lyn,dv,float(D0s.subs({lx:lxs,ly:lyn})))
                break
    if neg: break
if neg:
    print("\nFOUND negative Delta_red:")
    print(f"  lx={neg[0]}, ly={neg[1]}")
    print(f"  D0={neg[3]} (should be ~0)")
    print(f"  Delta_red={neg[2]} (<0)")
else:
    print("No negative found in scan for b=1,u=0,v=2. Trying more triangles.")
    for (bn,un,vn) in [(2,1,3),(3,1,4),(1,0,3),(4,1,3),(3,0,4),(2,0,3)]:
        spec2={b:sp.Rational(bn),u:sp.Rational(un),v:sp.Rational(vn)}
        D0s2=sp.expand(D0.subs(spec2)); Ds2=sp.expand(Delta_red.subs(spec2))
        for _ in range(20000):
            lxs=float(rng.uniform(-4,7))
            P=sp.Poly(D0s2.subs({lx:lxs}),ly)
            cc=[float(c) for c in P.all_coeffs()]
            if len(cc)<4 or abs(cc[0])<1e-12: continue
            roots=np.roots(cc)
            for r in roots:
                if abs(r.imag)<1e-6:
                    lyn=r.real
                    dv=float(Ds2.subs({lx:lxs,ly:lyn}))
                    if dv<-0.01:
                        neg=(bn,un,vn,lxs,lyn,dv,float(D0s2.subs({lx:lxs,ly:lyn})))
                        break
            if neg: break
        if neg: break
    if neg:
        print(f"\nFOUND: triangle b={neg[0]},u={neg[1]},v={neg[2]}")
        print(f"  lx={neg[3]}, ly={neg[4]}")
        print(f"  D0={neg[6]} (~0)")
        print(f"  Delta_red={neg[5]} (<0)")
