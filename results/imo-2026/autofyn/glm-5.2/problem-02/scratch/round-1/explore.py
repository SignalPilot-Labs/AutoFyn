import numpy as np, math
from numpy import sin,cos
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def build(A,al,be,ga,b=1.0,c=1.0):
    A_=np.radians(A); al_=np.radians(al); be_=np.radians(be); ga_=np.radians(ga)
    B=np.array([c,0.0]); C=np.array([b*cos(A_),b*sin(A_)])
    M=B*0.5; N=C*0.5
    def isect(P,a,Q,d):
        ca_,sa_=cos(a),sin(a); cd_,sd_=cos(d),sin(d)
        det=ca_*sd_-sa_*cd_
        u=((Q[0]-P[0])*sd_-(Q[1]-P[1])*cd_)/det
        return P+u*np.array([ca_,sa_])
    K=isect(B, np.pi-al_, M, ga_)
    L=isect(C, A_+np.pi+al_, N, A_-be_)
    K2=K@K; L2=L@L; detKL=cross(K,L)
    Ap=(L2*K-K2*L)/detKL if abs(detKL)>1e-9 else None
    return dict(B=B,C=C,M=M,N=N,K=K,L=L,Ap=Ap,Aang=A_,al=al_,be=be_,ga=ga_)
def dang(u,v):
    a=math.atan2(cross(u,v),u@v); return math.degrees(a)
def dirang(v): return math.degrees(math.atan2(v[1],v[0]))

# Known good interior config from scan.py
A,al=60,20
be,ga=35.2414494241406,17.963453537582254
d=build(A,al,be,ga)
B,C,M,N,K,L,Ap,A_=d['B'],d['C'],d['M'],d['N'],d['K'],d['L'],d['Ap'],d['Aang']
Bang=math.degrees(math.acos((-B@(C-B))/((np.linalg.norm(-B)*np.linalg.norm(C-B))))); Cang=180-A-Bang
print(f"A={A} al={al} be={be:.4f} ga={ga:.4f} | B={Bang:.4f} C={Cang:.4f}")
print(f"BC->BA' = {dang(C-B,Ap-B):.6f}  target 90-A-al = {90-A-al}")
print(f"BK->BA' = {dang(K-B,Ap-B):.6f}  target C-90 = {Cang-90:.6f}")
print(f"check Ap on perp-bis BC: |ApB|={np.linalg.norm(Ap-B):.6f} |ApC|={np.linalg.norm(Ap-C):.6f}")

# Now explore synthetic structure
def fsp(P): return P+np.array([P[1],-P[0]])  # f(P)=P+R90(A-P), A=0
fK=fsp(K); fL=fsp(L); fB=fsp(B); fC=fsp(C)
print("\n-- spiral sim f --")
print(f"Ap on KfK line: cross(Ap-K, fK-K)={cross(Ap-K,fK-K):.3e}")
print(f"Ap on LfL line: cross(Ap-L, fL-L)={cross(Ap-L,fL-L):.3e}")
print(f"|AK|={np.linalg.norm(K):.4f} |KfK|={np.linalg.norm(fK-K):.4f} |AL|={np.linalg.norm(L):.4f} |LfL|={np.linalg.norm(fL-L):.4f}")

# right-isosceles triangles AKfK (right at K), ALfL (right at L)
# Explore: the LINE BAp. What is its relation to fK, fL, K, L, fB, fC?
print(f"\n-- direction of BAp = {dirang(Ap-B):.4f}")
print(f"dir BK={dirang(K-B):.4f} dir BL={dirang(L-B):.4f} dir BC={dirang(C-B):.4f}")
print(f"dir BfK={dirang(fK-B):.4f} dir BfL={dirang(fL-B):.4f} dir BfB={dirang(fB-B):.4f} dir BfC={dirang(fC-B):.4f}")

# KEY: maybe Ap is intersection of KfK and LfL; consider quadrilateral K L fL fK or the spiral similarity
# center mapping BK->? Look for similar triangles
# A' is on KfK and LfL. Triangle A'KfK is right-iso? No: A'K perp AK, fK-K perp AK, so A',K,fK colinear. Degenerate.
# Try: is BAp parallel to some line between {fK,fL,K,L,fB,fC}?
print(f"\n-- which segments are parallel to BAp? --")
for nm,U,V in [("fKfL",fK,fL),("fKfC",fK,fC),("fLfC",fL,fC),("fKfB",fK,fB),("fBfC",fB,fC),("fBfL",fB,fL),("fBfK",fB,fK),("KL",K,L),("fB K",fB,K),("fC L",fC,L),("fC K",fC,K),("fB L",fB,L),("fK B",fK,B)]:
    seg=V-U
    print(f"  {nm}: cross(BAp,seg)={cross(Ap-B,seg):.3e}  dang={dang(Ap-B,seg):.4f}")

# Is Ap the image of B or C under some spiral sim centered at A'? at K? at B?
# Try: similarity at B mapping K -> Ap ? then fB->?
print(f"\n-- spiral sim at B mapping K->Ap --")
# ratio |BAp|/|BK|, angle dang(BK,BAp)
rB=np.linalg.norm(Ap-B)/np.linalg.norm(K-B); aB=dang(K-B,Ap-B)
print(f"  ratio={rB:.4f} angle={aB:.4f} (target C-90={Cang-90:.4f})")
# apply to fK: B + rot(aB)*rB*(fK-B)
th=np.radians(aB); Rb=np.array([[cos(th),-sin(th)],[sin(th),cos(th)]])
imgfK=B+Rb*rB@(fK-B)
print(f"  B+sim(fK)= {imgfK}  (is it fL? fC? L? Ap?) | to fL={np.linalg.norm(imgfK-fL):.4e} to C={np.linalg.norm(imgfK-C):.4e} to fC={np.linalg.norm(imgfK-fC):.4e}")
imgL=B+Rb*rB@(L-B)
print(f"  B+sim(L)= {imgL}  to fC={np.linalg.norm(imgL-fC):.4e} to fL={np.linalg.norm(imgL-fL):.4e}")
imgC=B+Rb*rB@(C-B)
print(f"  B+sim(C)= {imgC}  to ?")

# spiral sim at B mapping fK->fL (if it exists, single center B):
rB2=np.linalg.norm(fL-B)/np.linalg.norm(fK-B); aB2=dang(fK-B,fL-B)
print(f"\n-- sim at B: fK->fL ratio={rB2:.4f} ang={aB2:.4f} ; apply to K: {B+(np.array([[cos(np.radians(aB2)),-sin(np.radians(aB2))],[sin(np.radians(aB2)),cos(np.radians(aB2))]])*rB2)@(K-B)} to L?={np.linalg.norm(B+np.array([[cos(np.radians(aB2)),-sin(np.radians(aB2))],[sin(np.radians(aB2)),cos(np.radians(aB2))]])*rB2@(K-B)-L):.4e}")
