import numpy as np
from scipy.optimize import fsolve

def ang(P,Q,R):
    v1 = np.array(P)-np.array(Q); v2 = np.array(R)-np.array(Q)
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    return np.arccos(np.clip(c,-1,1))

def dang(P,Q,R):
    v1 = np.array(P)-np.array(Q); v2 = np.array(R)-np.array(Q)
    a1 = np.arctan2(v1[1],v1[0]); a2 = np.arctan2(v2[1],v2[0])
    d = a2-a1
    while d>np.pi: d-=2*np.pi
    while d<=-np.pi: d+=2*np.pi
    return d

def point_in_triangle(P,A,B,C):
    def sign(P1,P2,P3):
        return (P1[0]-P3[0])*(P2[1]-P3[1]) - (P2[0]-P3[0])*(P1[1]-P3[1])
    d1=sign(P,A,B); d2=sign(P,B,C); d3=sign(P,C,A)
    has_neg=(d1<0) or (d2<0) or (d3<0); has_pos=(d1>0) or (d2>0) or (d3>0)
    return not (has_neg and has_pos)

def inside_angle(P,V,X,Y):
    aXY=dang(X,V,Y); aXP=dang(X,V,P)
    if aXY>=0: return 0<=aXP<=aXY
    else: return aXY<=aXP<=0

def L2(P,Q): return np.linalg.norm(np.array(P)-np.array(Q))

# Very scalene triangle
A = np.array([0.0,4.5])
B = np.array([-3.0,0.0])
C = np.array([5.0,0.3])
M=(A+B)/2; N=(A+C)/2

def eqs(vars, kx):
    ky,lx,ly = vars
    K = np.array([kx,ky]); L=np.array([lx,ly])
    e1 = ang(K,B,A)-ang(A,C,L)
    e2 = ang(L,B,K)-ang(L,N,C)
    e3 = ang(L,C,K)-ang(B,M,K)
    return [e1,e2,e3]

# search for an initial valid solution via a coarse grid + fsolve with random guesses
import itertools
found=None
rng = np.random.default_rng(1)
for kx in np.linspace(-2.5,1.5,60):
    for trial in range(6):
        guess = [rng.uniform(0.2,2.5), rng.uniform(0.5,4.0), rng.uniform(0.2,3.0)]
        sol, info, ier, msg = fsolve(eqs, guess, args=(kx,), full_output=True, xtol=1e-12)
        if ier==1:
            resid = np.max(np.abs(eqs(sol,kx)))
            if resid < 1e-8:
                K=np.array([kx,sol[0]]); L=np.array([sol[1],sol[2]])
                c1=point_in_triangle(K,B,M,C); c2=point_in_triangle(L,B,N,C)
                c3=inside_angle(K,B,L,A); c4=inside_angle(L,C,A,K)
                if c1 and c2 and c3 and c4:
                    found=(kx,K,L); break
    if found: break

print("seed found:", found)

K0,L0 = found[1],found[2]
kx0 = found[0]
valid=[]
Kc,Lc = K0.copy(),L0.copy()
for kx in np.linspace(kx0, kx0+1.8, 40):
    guess=[Kc[1],Lc[0],Lc[1]]
    sol,info,ier,msg = fsolve(eqs,guess,args=(kx,),full_output=True,xtol=1e-13)
    if ier==1 and np.max(np.abs(eqs(sol,kx)))<1e-9:
        K=np.array([kx,sol[0]]); L=np.array([sol[1],sol[2]])
        c1=point_in_triangle(K,B,M,C); c2=point_in_triangle(L,B,N,C)
        c3=inside_angle(K,B,L,A); c4=inside_angle(L,C,A,K)
        if c1 and c2 and c3 and c4:
            valid.append((kx,K,L))
            Kc,Lc=K,L

print(f"valid: {len(valid)}")
AB=L2(A,B); AC=L2(A,C)
print("AB/AC=",AB/AC)
print(f"{'kx':>8} {'AK/AL':>10} {'MK/NL':>10} {'BK/CL':>10} {'BAK':>8} {'CAL':>8}")
for kx,K,L in valid:
    AK=L2(A,K);AL=L2(A,L);MK=L2(M,K);NL=L2(N,L);BK=L2(B,K);CL=L2(C,L)
    bak = ang(B,A,K); cal = ang(C,A,L)
    print(f"{kx:8.3f} {AK/AL:10.6f} {MK/NL:10.6f} {BK/CL:10.6f} {bak:8.4f} {cal:8.4f}")

# verify central identity holds here too
def circumcenter(P,Q,R):
    ax,ay=P; bx,by=Q; cx,cy=R
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])
print("\ncentral identity check:")
for kx,K,L in valid[::5]:
    O=circumcenter(A,K,L)
    print(kx, L2(O,M)-L2(O,N))

print("\n--- Search for similar triangles among {A,B,C,K,L,M,N,Q} robust across family ---")
import itertools
pts_names = ['A','B','C','K','L','M','N','Q']

def get_points(K,L):
    Qshift = (np.dot(C-A-(B-A),C-A+(B-A)))/(2*np.dot((C-A)-(B-A),(C-A)-(B-A))) * ((C-A)-(B-A))
    Q = A + Qshift
    return {'A':A,'B':B,'C':C,'K':K,'L':L,'M':M,'N':N,'Q':Q}

triangles = list(itertools.combinations(pts_names,3))

def tri_angles(P,Q,R,pts):
    a = ang(pts[Q],pts[P],pts[R])  # angle at P
    b = ang(pts[P],pts[Q],pts[R])  # angle at Q
    c = np.pi - a - b
    return (P,a),(Q,b),(R,c)

# for each valid config, compute angle-at-vertex dict for each triangle (labeled by vertex)
records = []
for kx,K,L in valid:
    pts = get_points(K,L)
    d = {}
    for tri in triangles:
        angs = tri_angles(*tri, pts)
        for vertex,a in angs:
            d[(tri,vertex)] = a
    records.append(d)

# Now find pairs (tri1,vertex-correspondence) vs (tri2,vertex-correspondence) with matching all 3 angles across ALL configs
# We'll compare triangle tri1 with vertex order (v1,v2,v3) to tri2 vertex order (w1,w2,w3): matches if angle(v1)=angle(w1) etc for all configs
def get_full_angle_triple(tri, pts):
    P,Q,R = tri
    a = ang(pts[Q],pts[P],pts[R])
    b = ang(pts[P],pts[Q],pts[R])
    c = np.pi-a-b
    return np.array([a,b,c])

# Precompute angle triples (in fixed vertex order) for each triangle & config
all_perms_pairs = []
data = {tri: [] for tri in triangles}
for kx,K,L in valid:
    pts = get_points(K,L)
    for tri in triangles:
        data[tri].append(get_full_angle_triple(tri,pts))
for tri in triangles:
    data[tri] = np.array(data[tri])  # shape (nconfig,3)

matches = []
tri_list = triangles
for i in range(len(tri_list)):
    for j in range(i+1,len(tri_list)):
        t1,t2 = tri_list[i],tri_list[j]
        if set(t1)==set(t2): continue
        d1,d2 = data[t1],data[t2]
        for perm in itertools.permutations(range(3)):
            diff = d1 - d2[:,perm]
            if np.max(np.abs(diff)) < 1e-4:
                matches.append((t1,t2,perm))
print(f"found {len(matches)} matching angle-triple correspondences (excluding trivial)")
for t1,t2,perm in matches:
    print(t1, "~", tuple(np.array(t2)[list(perm)]))

print("\n--- Check BKLC concyclic, and various concurrency guesses ---")
def concyclic_det(P1,P2,P3,P4):
    def f(P): return [P[0],P[1],P[0]**2+P[1]**2,1]
    return np.linalg.det(np.array([f(P1),f(P2),f(P3),f(P4)]))

def line_intersect(P1,P2,P3,P4):
    # intersection of line P1P2 and P3P4
    x1,y1=P1; x2,y2=P2; x3,y3=P3; x4,y4=P4
    d = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if abs(d)<1e-12: return None
    px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d
    py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d
    return np.array([px,py])

for kx,K,L in valid[::5]:
    r_bklc = concyclic_det(B,K,L,C)
    X = line_intersect(B,K,C,L)  # BK cap CL
    print(f"kx={kx:.3f} BKLC_det={r_bklc:.4e}  BK∩CL={X}")

print("\n--- AK*AL vs AB*AC, AM*AN; angle KAL vs BAC ---")
AM=L2(A,M); AN=L2(A,N)
print("AB*AC=",AB*AC,"AM*AN=",AM*AN)
BAC = ang(B,A,C)
for kx,K,L in valid[::4]:
    AK=L2(A,K); AL=L2(A,L)
    KAL = ang(K,A,L)
    print(f"kx={kx:.3f} AK*AL={AK*AL:.4f} AK*AL/(AB*AC)={AK*AL/(AB*AC):.4f} KAL={KAL:.4f} KAL/BAC={KAL/BAC:.4f}")

print("\n--- Ptolemy on A,K,Q,L: determine order + verify relation ---")
def get_Q():
    b=B-A;c=C-A
    return A + (np.dot(c-b,c+b))/(2*np.dot(c-b,c-b))*(c-b)
Qp = get_Q()
for kx,K,L in valid[::6]:
    AK=L2(A,K);AL=L2(A,L);KL=L2(K,L);AQ=L2(A,Qp);KQ=L2(K,Qp);LQ=L2(L,Qp)
    # check order by angle from A
    def angle_from(P): 
        v=P-A; return np.arctan2(v[1],v[0])
    order = sorted([('A',A),('K',K),('Q',Qp),('L',L)], key=lambda t: angle_from(t[1]) if t[0]!='A' else -999)
    # Ptolemy candidate: AK*LQ + AL*KQ =? AQ*KL  (order A,K,Q,L)
    lhs = AK*LQ + AL*KQ
    rhs = AQ*KL
    print(f"kx={kx:.3f} order={[o[0] for o in order]}  AK*LQ+AL*KQ={lhs:.5f}  AQ*KL={rhs:.5f}  diff={lhs-rhs:.2e}")

print("\n--- Ptolemy correct order A,K,L,Q: diagonals AL,KQ; sides AK,KL,LQ,QA ---")
for kx,K,L in valid[::6]:
    AK=L2(A,K);AL=L2(A,L);KL=L2(K,L);AQ=L2(A,Qp);KQ=L2(K,Qp);LQ=L2(L,Qp)
    lhs = AL*KQ
    rhs = AK*LQ + KL*AQ
    print(f"kx={kx:.3f}  AL*KQ={lhs:.5f}  AK*LQ+KL*AQ={rhs:.5f}  diff={lhs-rhs:.2e}")
