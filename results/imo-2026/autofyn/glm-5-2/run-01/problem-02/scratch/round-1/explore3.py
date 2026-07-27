import numpy as np, math
from numpy import sin,cos
from scipy.optimize import fsolve
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def build(A,al,be,ga,b,c):
    A_=A; al_=al; be_=be; ga_=ga
    B=np.array([c,0.0]); C=np.array([b*cos(A_),b*sin(A_)])
    M=B*0.5; N=C*0.5
    def isect(P,a,Q,d):
        ca_,sa_=cos(a),sin(a); cd_,sd_=cos(d),sin(d)
        det=ca_*sd_-sa_*cd_
        u=((Q[0]-P[0])*sd_-(Q[1]-P[1])*cd_)/det
        return P+u*np.array([ca_,sa_])
    K=isect(B, np.pi-al_, M, ga_)
    L=isect(C, A_+np.pi+al_, N, A_-be_)
    Kx,Ky=K; Lx,Ly=L
    K2=K@K; L2=L@L; detKL=cross(K,L)
    Ax=(Ly*K2-Ky*L2)/detKL; Ay=(Kx*L2-Lx*K2)/detKL
    return B,C,M,N,K,L,np.array([Ax,Ay])
def incid(A,al,be,ga,b,c):
    A_=A; B,C,M,N,K,L,Ap=build(A,al,be,ga,b,c)
    dCK=np.array([cos(A_+np.pi+al+ga),sin(A_+np.pi+al+ga)])
    incK=cross(K-C,dCK)
    dBL=np.array([cos(np.pi-al-be),sin(np.pi-al-be)])
    incL=cross(L-B,dBL)
    return incK,incL
def dang(u,v): return math.degrees(math.atan2(cross(u,v),u@v))
def dirang(v): return math.degrees(math.atan2(v[1],v[0]))
def get_config(Ad,ald,b,c,g0=15,b0=15):
    A_=np.radians(Ad); al_=np.radians(ald)
    def f(x):
        be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
    x,inf,ier,msg=fsolve(f,[b0,g0],full_output=True)
    return A_,al_,np.radians(x[0]),np.radians(x[1]),x[0],x[1],np.max(np.abs(inf['fvec']))

def tri_angles(A,B,C):
    a_=np.linalg.norm(B-C); b_=np.linalg.norm(C-A); c_=np.linalg.norm(A-B)
    Bang=math.degrees(math.acos((c_**2+a_**2-b_**2)/(2*c_*a_)))
    Cang=math.degrees(math.acos((a_**2+b_**2-c_**2)/(2*a_*b_)))
    return math.degrees(A) if hasattr(A,'__len__') else A, Bang, Cang

def fsp(P): return P+np.array([P[1],-P[0]])
def concyc(P1,P2,P3,P4):
    M=np.array([[p[0],p[1],p[0]**2+p[1]**2,1] for p in [P1,P2,P3,P4]])
    return np.linalg.det(M)

for (Ad,ald,b,c) in [(70,15,1.4,1.0),(55,25,1.0,1.2),(80,10,1.6,1.1),(45,18,0.9,1.3)]:
    res=get_config(Ad,ald,b,c)
    A_,al_,be_,ga_,bed,gad,r=res
    if r>1e-7: print(f"Ad={Ad} al={ald} b={b} c={c}: solve failed r={r:.1e}"); continue
    B,C,M,N,K,L,Ap=build(A_,al_,be_,ga_,b,c)
    Bang=math.degrees(math.acos((-B@(C-B))/(np.linalg.norm(-B)*np.linalg.norm(C-B)))); Cang=180-Ad-Bang
    print(f"=== Ad={Ad} al={ald} b={b} c={c} | B={Bang:.3f} C={Cang:.3f} be={bed:.3f} ga={gad:.3f} ===")
    print(f"  BC->BA'={dang(C-B,Ap-B):.5f} (tgt {90-Ad-ald:.5f})  BK->BA'={dang(K-B,Ap-B):.5f} (tgt {Cang-90:.5f})  |ApB|-|ApC|={np.linalg.norm(Ap-B)-np.linalg.norm(Ap-C):.2e}")
    fK=fsp(K); fL=fsp(L); fB=fsp(B); fC=fsp(C)
    print(f"  KL||BC? cross={cross(L-K,C-B):.3e}  fKfL||fBfC? cross={cross(fL-fK,fC-fB):.3e}  KL||fBfC? {cross(L-K,fC-fB):.3e}")
    print(f"  dir KL={dirang(L-K):.3f} dir BC={dirang(C-B):.3f} dir fKfL={dirang(fL-fK):.3f} dir fBfC={dirang(fC-fB):.3f}")
    # explore the identity BK->BA' = C-90. The right-isosceles: at K, KA' perp AK, |KfK|=|AK|.
    # A' lies on line KfK. Parametrize A' = K + t*(fK-K) for some real t. Find t.
    tparam=((Ap-K)@(fK-K))/(np.dot(fK-K,fK-K))
    sparam=((Ap-L)@(fL-L))/(np.dot(fL-L,fL-L))
    print(f"  A'=K+t*(fK-K), t={tparam:.6f} ; A'=L+s*(fL-L), s={sparam:.6f}")
    # Is t related to something? |A'K|/|AK| = |t|
    print(f"  |A'K|/|AK|={abs(tparam):.4f}  |A'L|/|AL|={abs(sparam):.4f}")
    # Key: A' on perp-bis of BC. Try to find the angle via spiral sim.
    # Consider triangle B K A'. Right angle at K (KA' perp AK). Want angle at B = C-90 (i.e. 90-C at... )
    # angle BKA' = ? directed (KB,KA') = (KB,KA)+90 = (al+phi)+90 where phi=BAK
    phi=math.degrees(math.acos((K@(-B))/(np.linalg.norm(K)*np.linalg.norm(-B))))  # angle BAK at A
    print(f"  phi=BAK={phi:.4f}  ang at K (KB,KA')= {dang(K-B if False else K-B,Ap-K):.4f}  expected al+phi+90={ald+phi+90:.4f}")
    print(f"  ang at A' in BKA' = {dang(Ap-K,Ap-B):.4f}  sum check (B+K+A')={dang(K-B,Ap-B)+dang(Ap-K,Ap-B)+dang(B-Ap,K-Ap):.4f}")
    # the angle at A': dang(ApK, ApB). Is it -(al+phi+C)? i.e. al+phi+C
    print(f"  -(al+phi+C) = {-(ald+phi+Cang):.4f}  ; al+phi+C = {ald+phi+Cang:.4f}")
    # Look: is A', B, and some reflection related. Check the perpendicular-bisector: midpoint of BC
    midBC=(B+C)/2
    print(f"  Ap-midBC={Ap-midBC}  BC={(C-B)}  dot(Ap-midBC,BC)={(Ap-midBC)@(C-B):.3e}")
    # Spiral similarity at B mapping K->A'. ratio r, angle aB=C-90. What does it do to fK, L, C, fC, fB, M?
    rB=np.linalg.norm(Ap-B)/np.linalg.norm(K-B); aBd=dang(K-B,Ap-B)
    th=np.radians(aBd); Rb=np.array([[cos(th),-sin(th)],[sin(th),cos(th)]])
    print(f"  sim@B K->Ap: r={rB:.4f} ang={aBd:.4f}")
    for nm,P in [("fK",fK),("L",L),("fL",fL),("C",C),("fC",fC),("M",M),("fB",fB),("A",np.zeros(2)),("N",N)]:
        img=B+Rb*rB@(P-B)
        # match to known points
        known={"K":K,"L":L,"Ap":Ap,"C":C,"B":B,"M":M,"N":N,"fK":fK,"fL":fL,"fB":fB,"fC":fC,"A":np.zeros(2)}
        best=min(known.items(),key=lambda kv:np.linalg.norm(img-kv[1]))
        print(f"    {nm}->~{best[0]} (dist {best[1].__class__} ) d={np.linalg.norm(img-best[1]):.3e} img={img}")
