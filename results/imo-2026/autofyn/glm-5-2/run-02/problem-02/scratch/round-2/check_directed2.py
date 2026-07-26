"""
Properly test: do ordinary-angle-equalities configs satisfy the directed
mod-pi encoding e1=e2=e3=0?  Compare directed angles directly.
"""
import numpy as np
from scipy.optimize import least_squares

def dvec(p, q):  # q - p
    return (q[0]-p[0], q[1]-p[1])
def cross(p, q): return p[0]*q[1]-p[1]*q[0]
def dot(p, q): return p[0]*q[0]+p[1]*q[1]
def dir_angle(p, q):  # directed from p to q, mod pi, in (-pi/2, pi/2] via atan2 cross,dot mod pi
    return np.arctan2(cross(p,q), dot(p,q))  # in (-pi, pi]; mod pi below
def dir_angle_modpi(p, q):
    a = np.arctan2(cross(p,q), dot(p,q))
    return np.mod(a, np.pi)  # in [0, pi)
def ord_angle(p, q):
    return np.arctan2(abs(cross(p,q)), dot(p,q))  # [0, pi]

# verified config
A=(0.0,0.0); B=(4.0,0.0); C=(1.0,3.0); M=(2.0,0.0); N=(0.5,1.5)
K=(2.8, 0.49465); L=(1.0479, 2.3099)

# angle 1: ∠KBA = ∠ACL.  directed: ∡(BK,BA) vs ∡(CA,CL)
BK=dvec(B,K); BA=dvec(B,A); CA=dvec(C,A); CL=dvec(C,L)
print("Angle 1 (KBA = ACL):")
print("  ord ∠KBA =", np.degrees(ord_angle(BK,BA)), " ord ∠ACL =", np.degrees(ord_angle(CA,CL)))
print("  dir ∡(BK,BA) (raw, -pi,pi]) =", np.degrees(np.arctan2(cross(BK,BA),dot(BK,BA))))
print("  dir ∡(CA,CL) (raw) =", np.degrees(np.arctan2(cross(CA,CL),dot(CA,CL))))
print("  dir mod pi ∡(BK,BA) =", np.degrees(dir_angle_modpi(BK,BA)))
print("  dir mod pi ∡(CA,CL) =", np.degrees(dir_angle_modpi(CA,CL)))
print("  e1 sign check: cross(BK,BA)/dot(BK,BA) =", cross(BK,BA)/dot(BK,BA),
      " cross(CA,CL)/dot(CA,CL) =", cross(CA,CL)/dot(CA,CL))

# angle 2: ∠LBK = ∠LNC.  directed: ∡(BL,BK) vs ∡(NL,NC)
BL=dvec(B,L); NL=dvec(N,L); NC=dvec(N,C)
print("\nAngle 2 (LBK = LNC):")
print("  ord ∠LBK =", np.degrees(ord_angle(BL,BK)), " ord ∠LNC =", np.degrees(ord_angle(NL,NC)))
print("  dir mod pi ∡(BL,BK) =", np.degrees(dir_angle_modpi(BL,BK)))
print("  dir mod pi ∡(NL,NC) =", np.degrees(dir_angle_modpi(NL,NC)))

# angle 3: ∠LCK = ∠BMK.  directed: ∡(CL,CK) vs ∡(MB,MK)
CL3=dvec(C,L); CK=dvec(C,K); MB=dvec(M,B); MK=dvec(M,K)
print("\nAngle 3 (LCK = BMK):")
print("  ord ∠LCK =", np.degrees(ord_angle(CL3,CK)), " ord ∠BMK =", np.degrees(ord_angle(MB,MK)))
print("  dir mod pi ∡(CL,CK) =", np.degrees(dir_angle_modpi(CL3,CK)))
print("  dir mod pi ∡(MB,MK) =", np.degrees(dir_angle_modpi(MB,MK)))

# Now: does ordinary equality hold with directed mod pi equality? i.e. are the
# dir mod pi values equal for each pair?  If YES => e1=e2=e3=0.  If NO (they
# differ, e.g. one is alpha and the other pi-alpha) => sign flip => e_i != 0.
print("\n=== fresh ordinary configs via least_squares (3 eq, 4 unk, fix ly) ===")
def residual(X, Bn, Cn, lyfix):
    kxv, kyv, lxv = X; lyv = lyfix
    K_=(kxv,kyv); L_=(lxv,lyv); A_=(0.0,0.0)
    Mn=(Bn[0]/2,0.0); Nn=(Cn[0]/2,Cn[1]/2)
    a1 = ord_angle((K_[0]-Bn[0],K_[1]-Bn[1]),(A_[0]-Bn[0],A_[1]-Bn[1])) \
       - ord_angle((A_[0]-Cn[0],A_[1]-Cn[1]),(L_[0]-Cn[0],L_[1]-Cn[1]))
    a2 = ord_angle((L_[0]-Bn[0],L_[1]-Bn[1]),(K_[0]-Bn[0],K_[1]-Bn[1])) \
       - ord_angle((L_[0]-Nn[0],L_[1]-Nn[1]),(Cn[0]-Nn[0],Cn[1]-Nn[1]))
    a3 = ord_angle((L_[0]-Cn[0],L_[1]-Cn[1]),(K_[0]-Cn[0],K_[1]-Cn[1])) \
       - ord_angle((Bn[0]-Mn[0],Bn[1]-Mn[1]),(K_[0]-Mn[0],K_[1]-Mn[1]))
    return [a1,a2,a3]

def in_tri(P,V1,V2,V3):
    def s(p,q,r): return (p[0]-r[0])*(q[1]-r[1])-(q[0]-r[0])*(p[1]-r[1])
    d1=s(P,V1,V2);d2=s(P,V2,V3);d3=s(P,V3,V1)
    neg=(d1<0)|(d2<0)|(d3<0); pos=(d1>0)|(d2>0)|(d3>0)
    return not(neg and pos)

rng=np.random.default_rng(11)
found=[]
for _ in range(4000):
    bn=float(rng.uniform(3,7)); un=float(rng.uniform(-2,4)); vn=float(rng.uniform(2,6))
    Bn=(bn,0); Cn=(un,vn); Mn=(bn/2,0); Nn=(un/2,vn/2)
    lyfix=float(rng.uniform(0.2, vn-0.2))
    x0=[bn*0.55+rng.uniform(-0.3,0.3), rng.uniform(0.2,vn*0.4), un*0.5+rng.uniform(-0.5,0.5)]
    res=least_squares(residual, x0, args=(Bn,Cn,lyfix), xtol=1e-15, ftol=1e-15)
    if res.cost > 1e-20: continue
    kxv,kyv,lxv=res.x; L_=(lxv,lyfix); K_=(kxv,kyv)
    if not (in_tri(K_,Bn,Mn,Cn) and in_tri(L_,Bn,Nn,Cn)): continue
    # check inside-angle conditions K in angle LBA, L in angle ACK
    # K in angle LBA: K between rays BL and BA at B
    # L in angle ACK: L between rays CA and CK at C
    found.append((bn,un,vn,K_,L_))
    if len(found)>=12: break

print(f"Found {len(found)} ordinary configs (inside tri).")
mismatches=0
for cfg in found:
    bn,un,vn,K_,L_ = cfg
    Bn=(bn,0); Cn=(un,vn); Mn=(bn/2,0); Nn=(un/2,vn/2); A_=(0,0)
    BKv=dvec(Bn,K_);BAv=dvec(Bn,A_);CAv=dvec(Cn,A_);CLv=dvec(Cn,L_)
    BLv=dvec(Bn,L_);NLv=dvec(Nn,L_);NCv=dvec(Nn,Cn)
    CL3v=dvec(Cn,L_);CKv=dvec(Cn,K_);MBv=dvec(Mn,Bn);MKv=dvec(Mn,K_)
    d1 = dir_angle_modpi(BKv,BAv)-dir_angle_modpi(CAv,CLv)
    d2 = dir_angle_modpi(BLv,BKv)-dir_angle_modpi(NLv,NCv)
    d3 = dir_angle_modpi(CL3v,CKv)-dir_angle_modpi(MBv,MKv)
    d1=np.mod(d1+np.pi/2, np.pi)-np.pi/2  # wrap to (-pi/2,pi/2]
    d2=np.mod(d2+np.pi/2, np.pi)-np.pi/2
    d3=np.mod(d3+np.pi/2, np.pi)-np.pi/2
    if abs(d1)>1e-6 or abs(d2)>1e-6 or abs(d3)>1e-6:
        mismatches+=1
        print(f"  MISMATCH: dir-mod-pi diffs (deg) = {np.degrees(d1):.4f}, {np.degrees(d2):.4f}, {np.degrees(d3):.4f}")
print(f"configs where directed mod pi != ordinary: {mismatches}/{len(found)}")
