"""
Scrutinize the claim that ordinary-angle equality + inside hypotheses
=> directed-mod-pi encoding e1=e2=e3=0.

Use the verified config from power-secant-product (found via fsolve on the
ORDINARY angle equalities) and check whether e1,e2,e3 (directed encodings) vanish.
"""
import sympy as sp
import numpy as np

b, u, v, lx, ly, t = sp.symbols('b u v lx ly t')
kx, ky = sp.symbols('kx ky')

A = (0, 0); Bpt = (b, 0); Cpt = (u, v); M = (b/2, 0); Npt = (u/2, v/2)
def sub(P, d): return (P[0]-d[0], P[1]-d[1])
def cross(p, q): return p[0]*q[1] - p[1]*q[0]
def dot(p, q): return p[0]*q[0] + p[1]*q[1]

K = (kx, ky); L = (lx, ly)
BK = sub(K, Bpt); BA = sub(A, Bpt); CA = sub(A, Cpt); CL = sub(L, Cpt)
e1 = sp.expand(cross(BK, BA)*dot(CA, CL) - cross(CA, CL)*dot(BK, BA))
BL = sub(L, Bpt); BK2 = sub(K, Bpt); NL = sub(L, Npt); NC = sub(Cpt, Npt)
e2 = sp.expand(cross(BL, BK2)*dot(NL, NC) - cross(NL, NC)*dot(BL, BK2))
CL3 = sub(L, Cpt); CK = sub(K, Cpt); MB = sub(Bpt, M); MK = sub(K, M)
e3 = sp.expand(cross(CL3, CK)*dot(MB, MK) - cross(MB, MK)*dot(CL3, CK))

e1_fn = sp.lambdify((b,u,v,kx,ky,lx,ly), e1, 'numpy')
e2_fn = sp.lambdify((b,u,v,kx,ky,lx,ly), e2, 'numpy')
e3_fn = sp.lambdify((b,u,v,kx,ky,lx,ly), e3, 'numpy')

# verified config from power-secant-product (ordinary angle equalities to 1e-12)
# A=(0,0), B=(4,0), C=(1,3), K=(2.8, 0.49465), L=(1.0479, 2.3099)
Kv = (2.8, 0.49465); Lv = (1.0479, 2.3099)
print("At verified ordinary-angle-equalities config:")
print(" e1 =", e1_fn(4, 1, 3, Kv[0], Kv[1], Lv[0], Lv[1]))
print(" e2 =", e2_fn(4, 1, 3, Kv[0], Kv[1], Lv[0], Lv[1]))
print(" e3 =", e3_fn(4, 1, 3, Kv[0], Kv[1], Lv[0], Lv[1]))

# also generate fresh ordinary-angle configs via fsolve across several triangles
from scipy.optimize import fsolve
def ordinary_angle(p, q):
    cr = p[0]*q[1]-p[1]*q[0]; dt = p[0]*q[0]+p[1]*q[1]
    return np.arctan2(abs(cr), dt)  # ordinary angle in [0,pi]

def residual(X, Bn, Cn):
    kxv, kyv, lxv, lyv = X
    K_=(kxv,kyv); L_=(lxv,lyv); A_=(0.0,0.0)
    Mn=((Bn[0])/2,0.0); Nn=(Cn[0]/2, Cn[1]/2)
    a1 = ordinary_angle((K_[0]-Bn[0], K_[1]-Bn[1]),(A_[0]-Bn[0],A_[1]-Bn[1])) \
       - ordinary_angle((A_[0]-Cn[0],A_[1]-Cn[1]),(L_[0]-Cn[0],L_[1]-Cn[1]))
    a2 = ordinary_angle((L_[0]-Bn[0],L_[1]-Bn[1]),(K_[0]-Bn[0],K_[1]-Bn[1])) \
       - ordinary_angle((L_[0]-Nn[0],L_[1]-Nn[1]),(Cn[0]-Nn[0],Cn[1]-Nn[1]))
    a3 = ordinary_angle((L_[0]-Cn[0],L_[1]-Cn[1]),(K_[0]-Cn[0],K_[1]-Cn[1])) \
       - ordinary_angle((Bn[0]-Mn[0],Bn[1]-Mn[1]),(K_[0]-Mn[0],K_[1]-Mn[1]))
    return [a1,a2,a3]

def in_tri(P,V1,V2,V3):
    def s(p,q,r): return (p[0]-r[0])*(q[1]-r[1])-(q[0]-r[0])*(p[1]-r[1])
    d1=s(P,V1,V2);d2=s(P,V2,V3);d3=s(P,V3,V1)
    neg=(d1<0)|(d2<0)|(d3<0); pos=(d1>0)|(d2>0)|(d3>0)
    return not(neg and pos)

rng = np.random.default_rng(7)
configs_ord = []
for _ in range(2000):
    bn=float(rng.uniform(3,7)); un=float(rng.uniform(-2,4)); vn=float(rng.uniform(2,6))
    Bn=(bn,0); Cn=(un,vn); Mn=(bn/2,0); Nn=(un/2,vn/2)
    x0=[bn*0.6+rng.uniform(-0.5,0.5), rng.uniform(0.1,vn*0.3),
        un*0.5+rng.uniform(-0.5,0.5), vn*0.6+rng.uniform(-0.3,0.3)]
    sol,info,ier,msg = fsolve(residual, x0, args=(Bn,Cn), full_output=True, xtol=1e-14)
    if ier!=1: continue
    r = np.sqrt(np.sum(np.array(residual(sol,Bn,Cn))**2))
    if r>1e-10: continue
    K_=(sol[0],sol[1]); L_=(sol[2],sol[3])
    if not (in_tri(K_,Bn,Mn,Cn) and in_tri(L_,Bn,Nn,Cn)): continue
    configs_ord.append((bn,un,vn,K_,L_))
    if len(configs_ord)>=15: break

print(f"\nFound {len(configs_ord)} ordinary-angle configs.")
maxe=[0,0,0]
for cfg in configs_ord:
    bn,un,vn,K_,L_ = cfg
    e1v=float(e1_fn(bn,un,vn,K_[0],K_[1],L_[0],L_[1]))
    e2v=float(e2_fn(bn,un,vn,K_[0],K_[1],L_[0],L_[1]))
    e3v=float(e3_fn(bn,un,vn,K_[0],K_[1],L_[0],L_[1]))
    # normalize by magnitudes
    s1=abs(e1v); s2=abs(e2v); s3=abs(e3v)
    maxe[0]=max(maxe[0],s1); maxe[1]=max(maxe[1],s2); maxe[2]=max(maxe[2],s3)
print("max |e1|,|e2|,e3| over ordinary configs:", maxe)
