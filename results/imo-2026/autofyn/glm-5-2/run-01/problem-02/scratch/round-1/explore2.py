import numpy as np, math
from numpy import sin,cos
from scipy.optimize import fsolve
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def build(A,al,be,ga,b=1.0,c=1.0):
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
def incid(A,al,be,ga,b=1.0,c=1.0):
    A_=A; B,C,M,N,K,L,Ap=build(A,al,be,ga,b,c)
    dCK=np.array([cos(A_+np.pi+al+ga),sin(A_+np.pi+al+ga)])
    incK=cross(K-C,dCK)
    dBL=np.array([cos(np.pi-al-be),sin(np.pi-al-be)])
    incL=cross(L-B,dBL)
    return incK,incL
def dang(u,v): return math.degrees(math.atan2(cross(u,v),u@v))
def dirang(v): return math.degrees(math.atan2(v[1],v[0]))

def get_config(Ad,ald,b=1.0,c=1.0):
    A_=np.radians(Ad); al_=np.radians(ald)
    def f(x):
        be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
    x,inf,ier,msg=fsolve(f,[15,15],full_output=True)
    return A_,al_,np.radians(x[0]),np.radians(x[1]),x[0],x[1]

A_,al_,be_,ga_,bed,gad=get_config(60,20)
B,C,M,N,K,L,Ap=build(A_,al_,be_,ga_)
Bang=math.degrees(math.acos((-B@(C-B))/((np.linalg.norm(-B)*np.linalg.norm(C-B))))); Cang=180-60-Bang
print(f"Config: A=60 al=20 be={bed:.4f} ga={gad:.4f} B={Bang:.4f} C={Cang:.4f}")
print(f"BC->BA'={dang(C-B,Ap-B):.6f} (target {math.degrees(np.pi/2-A_-al_):.6f})")
print(f"BK->BA'={dang(K-B,Ap-B):.6f} (target C-90={Cang-90:.6f})")

# f: spiral sim center A=0, f(P)=P+R90(A-P)=P+(P.y, -P.x)
def fsp(P): return P+np.array([P[1],-P[0]])
fK=fsp(K); fL=fsp(L); fB=fsp(B); fC=fsp(C)
print("\n-- right-isosceles & spiral sim --")
print(f"Ap on KfK: {cross(Ap-K,fK-K):.3e} ; Ap on LfL: {cross(Ap-L,fL-L):.3e}")
print(f"|AK|={np.linalg.norm(K):.4f}|KfK|={np.linalg.norm(fK-K):.4f} |AL|={np.linalg.norm(L):.4f}|LfL|={np.linalg.norm(fL-L):.4f}")

# Explore: which lines/segments relate to BAp direction
print(f"\ndir BAp={dirang(Ap-B):.4f}")
print(f"dir BK={dirang(K-B):.4f} dir BL={dirang(L-B):.4f} dir BC={dirang(C-B):.4f} dir BA={dirang(-B):.4f}")
print(f"dir BfK={dirang(fK-B):.4f} dir BfL={dirang(fL-B):.4f} dir BfB={dirang(fB-B):.4f} dir BfC={dirang(fC-B):.4f}")
print(f"dir fKfL={dirang(fL-fK):.4f} dir KL={dirang(L-K):.4f} dir fBfC={dirang(fC-fB):.4f} dir BC={dirang(C-B):.4f}")

# Look for parallelisms / colinearities involving Ap, B
print("\n-- colinearity / parallelism checks --")
checks=[("B,K,Ap",cross(K-B,Ap-B)),("B,L,Ap",cross(L-B,Ap-B)),
        ("B,fK,Ap",cross(fK-B,Ap-B)),("B,fL,Ap",cross(fL-B,Ap-B)),
        ("B,fB,Ap",cross(fB-B,Ap-B)),("B,fC,Ap",cross(fC-B,Ap-B)),
        ("Ap on KL",cross(L-K,Ap-K)),("Ap on fKfL",cross(fL-fK,Ap-fK)),
        ("BAp || fKfL",cross(Ap-B,fL-fK)),("BAp || fBfC",cross(Ap-B,fC-fB)),
        ("BAp || KL",cross(Ap-B,L-K)),("BAp || fBfC",cross(Ap-B,fC-fB)),
        ("Ap,K,fK colin (trivial)",cross(fK-K,Ap-K))]
for nm,v in checks: print(f"  {nm}: {v:.4e}")

# spiral sim at B mapping K->Ap
rB=np.linalg.norm(Ap-B)/np.linalg.norm(K-B); aB=dang(K-B,Ap-B)
print(f"\n-- sim at B: K->Ap ratio={rB:.4f} ang={aB:.4f}")
th=np.radians(aB); Rb=np.array([[cos(th),-sin(th)],[sin(th),cos(th)]])
for nm,P in [("fK",fK),("L",L),("fL",fL),("C",C),("fC",fC),("M",M),("fB",fB)]:
    img=B+Rb*rB@(P-B)
    print(f"  {nm}->{img}  (to known pts: fL={np.linalg.norm(img-fL):.3e} C={np.linalg.norm(img-C):.3e} fC={np.linalg.norm(img-fC):.3e} L={np.linalg.norm(img-L):.3e} fB={np.linalg.norm(img-fB):.3e} fK={np.linalg.norm(img-fK):.3e})")

# is there a spiral similarity centered at Ap mapping K->L, fK->fL?
rA=np.linalg.norm(L-Ap)/np.linalg.norm(K-Ap); aA=dang(K-Ap,L-Ap)
print(f"\n-- sim at Ap: K->L ratio={rA:.4f} ang={aA:.4f}")
th2=np.radians(aA); RA=np.array([[cos(th2),-sin(th2)],[sin(th2),cos(th2)]])
for nm,P in [("fK",fK),("B",B),("C",C),("fB",fB),("fC",fC)]:
    img=Ap+RA*rA@(P-Ap)
    print(f"  {nm}->{img}  (fL={np.linalg.norm(img-fL):.3e} C={np.linalg.norm(img-C):.3e} B={np.linalg.norm(img-B):.3e})")

# concyclicity
def concyc(P1,P2,P3,P4):
    M=np.array([[p[0],p[1],p[0]**2+p[1]**2,1] for p in [P1,P2,P3,P4]])
    return np.linalg.det(M)
print("\n-- concyclicity --")
for nm,Ps in [("A,K,L,Ap",(np.zeros(2),K,L,Ap)),("B,K,fK,Ap",(B,K,fK,Ap)),
             ("B,K,L,Ap",(B,K,L,Ap)),("B,fK,fL,Ap",(B,fK,fL,Ap)),
             ("B,C,K,Ap",(B,C,K,Ap)),("B,C,L,Ap",(B,C,L,Ap)),
             ("B,K,Ap,C",(B,K,Ap,C)),("K,L,fK,fL",(K,L,fK,fL)),
             ("B,fB,fK,K",(B,fB,fK,K)),("B,fB,fL,L",(B,fB,fL,L)),
             ("A,B,fK,fL",(np.zeros(2),B,fK,fL)),("A,B,K,L",(np.zeros(2),B,K,L))]:
    print(f"  {nm}: {concyc(*Ps):.4e}")
