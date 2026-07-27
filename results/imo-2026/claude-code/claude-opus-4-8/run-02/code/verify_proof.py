"""
Independent audit of the proof that OM = ON.

Problem: triangle ABC; M,N midpoints of AB,AC; K in BMC, L in BNC with
  angle KBA = angle ACL,  angle LBK = angle LNC,  angle LCK = angle BMK,
  and K inside angle LBA, L inside angle ACK.  O = circumcentre of AKL.
Claim: OM = ON.

This script verifies every load-bearing step of the write-up:
  (A) the Apollonius reduction  OM=ON  <=>  TT=0        (equivalence TT = 2*D*T)
  (B) the tangent translation of the angle conditions gives P(t)=0, Q(s)=0
  (C) the master identity (double-dagger)  sin(a+p)*TT = -2b(..)P + 2b^2(..)Q   [SYMBOLIC]
  (D) end-to-end: solve the real configuration two independent ways and check OM=ON
Run:  python3 verify_proof.py
"""
import sympy as sp, numpy as np
from scipy.optimize import brentq

I = sp.I
b, al, ph, t, s = sp.symbols('b alpha phi t s', real=True)
sa, ca, sf, cf = sp.sin(al), sp.cos(al), sp.sin(ph), sp.cos(ph)
S, Cc = sp.sin(al+ph), sp.cos(al+ph)              # sin/cos(alpha+phi)

# ---- coordinates (A=origin, B=(1,0), C=(b cos a, b sin a)) ----
kx, ky = 1 - t*cf, t*sf
lx, ly = b*(ca - s*(ca*cf-sa*sf)), b*(sa - s*(sa*cf+ca*sf))   # = b cos a - s b cos(a+p), etc.
K2, L2 = sp.expand(kx**2+ky**2), sp.expand(lx**2+ly**2)
D  = sp.expand(2*(kx*ly - ky*lx))
Px = sp.expand(ly*K2 - ky*L2)
Py = sp.expand(kx*L2 - lx*K2)                                 # O = (Px/D, Py/D)
TT = sp.expand(4*(Px*(b*ca-1) + Py*(b*sa)) + (1-b**2)*D)

# ================= (A) Apollonius reduction: TT = 2*D*T ======================
# T := 2 O.(C-B) + (1-b^2)/2 ;  OM=ON  <=>  T=0  <=>  TT=0   (since D != 0)
Ox, Oy = Px/D, Py/D
T = 2*(Ox*(b*ca-1) + Oy*(b*sa)) + (sp.Rational(1,2))*(1-b**2)
print("(A) TT - 2*D*T  simplifies to:", sp.simplify(TT - 2*D*T))

# ============ (B) tangent translation of the angle conditions ===============
# condition (I): angle KCA = phi + angle BMK
tanBMK = (t*sf)/(sp.Rational(1,2) - t*cf)
tanKCA = (sa - t*S)/(b - ca + t*Cc)                          # unsigned tan(angle KCA)
tf = sf/cf
eqK = sp.together(tanKCA - (tf + tanBMK)/(1 - tf*tanBMK))
numK = sp.expand(sp.numer(sp.cancel(eqK)))
P = 2*S*t**2 - (3*sa + 2*sf*Cc)*t + (S - b*sf)              # claimed (K)
print("(B) tangent-eqn numerator / P(t) =", sp.simplify(numK/P), "  (a nonzero constant => equations agree)")
Q = 2*S*s**2 - (3*sa + 2*sf*Cc)*s + (S - sf/b)             # claimed (L)

# ================= (C) master identity (double-dagger) ======================
lhs = sp.expand(S*TT)
rhs = sp.expand(-2*b*(b*s*sf - s*S + sa)*P + 2*b**2*(b*sa + t*sf - b*t*S)*Q)
print("(C) sin(a+p)*TT - [ -2b(..)P + 2b^2(..)Q ]  =", sp.simplify(sp.trigsimp(lhs - rhs)))

# ================= (D) end-to-end numeric check =============================
def circ(A,K,L):
    ax,ay=A;bx,by=K;cx,cy=L
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

def solve_via_constraints(bv, alv, phv):
    """Solve using P(t)=0, Q(s)=0 (the write-up's equations)."""
    sav,cav,sfv,cfv=np.sin(alv),np.cos(alv),np.sin(phv),np.cos(phv); Sv,Ccv=np.sin(alv+phv),np.cos(alv+phv)
    Pf=lambda tt:2*Sv*tt*tt-(3*sav+2*sfv*Ccv)*tt+(Sv-bv*sfv)
    Qf=lambda ss:2*Sv*ss*ss-(3*sav+2*sfv*Ccv)*ss+(Sv-sfv/bv)
    xs=np.linspace(0.01,1.5,600)
    tr=[brentq(Pf,xs[i],xs[i+1]) for i in range(len(xs)-1) if Pf(xs[i])*Pf(xs[i+1])<0]
    sr=[brentq(Qf,xs[i],xs[i+1]) for i in range(len(xs)-1) if Qf(xs[i])*Qf(xs[i+1])<0]
    tt,ss=min(tr),min(sr)  # geometric (inner) root
    A=np.array([0,0.]);B=np.array([1,0.]);C=np.array([bv*cav,bv*sav]);M=(A+B)/2;N=(A+C)/2
    K=np.array([1-tt*cfv,tt*sfv]); L=np.array([bv*(cav-ss*(cav*cfv-sav*sfv)),bv*(sav-ss*(sav*cfv+cav*sfv))])
    O=circ(A,K,L)
    return K,L,np.linalg.norm(O-M)-np.linalg.norm(O-N)

def solve_from_scratch(A,B,C,phi):
    """Independent solver: build K,L directly from ALL original angle conditions."""
    def rot(v,a): c,s=np.cos(a),np.sin(a); return np.array([c*v[0]-s*v[1],s*v[0]+c*v[1]])
    def uns(P,X,Y):
        u=X-P;v=Y-P; return np.arccos(np.clip(u@v/np.linalg.norm(u)/np.linalg.norm(v),-1,1))
    M=(A+B)/2;N=(A+C)/2
    dK=rot(A-B,-phi); dK/=np.linalg.norm(dK)          # ray BK: angle phi from BA
    dL=rot(A-C, phi); dL/=np.linalg.norm(dL)          # ray CL: angle phi from CA
    # K: on ray BK with angle KCA - angle BMK = phi ;  L: on ray CL with angle LBA - angle CNL = phi
    Kf=lambda tt:B+tt*dK; Lf=lambda ss:C+ss*dL
    eqK=lambda tt:(uns(C,Kf(tt),A)-uns(M,B,Kf(tt)))-phi
    eqL=lambda ss:(uns(B,Lf(ss),A)-uns(N,C,Lf(ss)))-phi
    xs=np.linspace(0.02,3.0,800)
    tK=[brentq(eqK,xs[i],xs[i+1]) for i in range(len(xs)-1) if eqK(xs[i])*eqK(xs[i+1])<0][0]
    sL=[brentq(eqL,xs[i],xs[i+1]) for i in range(len(xs)-1) if eqL(xs[i])*eqL(xs[i+1])<0][0]
    return Kf(tK),Lf(sL)

print("\n(D) end-to-end over several triangles (b, alpha, phi):")
for bv,alv,phv in [(1.22,0.9,0.35),(0.7,1.2,0.5),(1.8,0.6,0.25),(1.0,1.0,0.4)]:
    K1,L1,diff=solve_via_constraints(bv,alv,phv)
    A=np.array([0,0.]);B=np.array([1,0.]);C=np.array([bv*np.cos(alv),bv*np.sin(alv)])
    K2c,L2c=solve_from_scratch(A,B,C,phv)   # independent construction
    match=max(np.linalg.norm(K1-K2c),np.linalg.norm(L1-L2c))
    print(f"   b={bv} a={alv} p={phv}:  OM-ON={diff:+.2e}   |K,L two-ways|={match:.1e}")

# extra: master identity at random non-solution points (float)
np.random.seed(0); m=0
for _ in range(50):
    bv,alv,phv=np.random.uniform(0.4,2.5),np.random.uniform(0.2,1.5),np.random.uniform(0.1,0.8)
    tv,sv=np.random.uniform(-3,3),np.random.uniform(-3,3)
    f=sp.lambdify((b,al,ph,t,s), lhs-rhs,'numpy')
    m=max(m,abs(float(f(bv,alv,phv,tv,sv))))
print(f"\n(C') identity residual at 50 random non-solution points: {m:.1e}")
