import numpy as np
from scipy.optimize import fsolve

def angle_at(P, Q, R):
    # angle QPR at vertex P between rays P->Q and P->R
    v1 = Q-P; v2 = R-P
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    c = max(-1,min(1,c))
    return np.arccos(c)

def rotate(v, ang):
    c,s = np.cos(ang), np.sin(ang)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def circumcenter(A,B,C):
    ax,ay=A; bx,by=B; cx,cy=C
    d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy = ((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

def build(theta, rK, rL, A,B,C, sign_orient):
    M=(A+B)/2; N=(A+C)/2
    # direction B->A
    dirBA = (A-B)/np.linalg.norm(A-B)
    # rotate towards interior of triangle (towards C) by theta
    dirBK = rotate(dirBA, -sign_orient*theta)  # sign chosen to point into triangle
    K = B + rK*dirBK
    dirCA = (A-C)/np.linalg.norm(A-C)
    dirCL = rotate(dirCA, sign_orient*theta)
    L = C + rL*dirCL
    return K,L,M,N

def residuals(x, theta, A,B,C, sign_orient):
    rK, rL = x
    K,L,M,N = build(theta, rK, rL, A,B,C, sign_orient)
    ang1 = angle_at(B, L, K)   # angle LBK at B
    ang2 = angle_at(N, L, C)   # angle LNC at N
    ang3 = angle_at(C, L, K)   # angle LCK at C
    ang4 = angle_at(M, B, K)   # angle BMK at M
    return [ang1-ang2, ang3-ang4]

# triangle
A = np.array([0.0, 3.0])
B = np.array([-2.0, 0.0])
C = np.array([2.5, 0.0])

sign_orient = 1  # try to get correct orientation; will check region validity

for theta_deg in [20,30,40,50]:
    theta = np.radians(theta_deg)
    guess = [1.0,1.0]
    try:
        sol = fsolve(residuals, guess, args=(theta,A,B,C,sign_orient), full_output=True)
        x, info, ier, msg = sol
        rK,rL = x
        K,L,M,N = build(theta, rK, rL, A,B,C, sign_orient)
        O = circumcenter(A,K,L)
        OM = np.linalg.norm(O-M)
        ON = np.linalg.norm(O-N)
        print(theta_deg, "ier=",ier, "rK,rL=",rK,rL, "OM=",OM,"ON=",ON, "diff=",OM-ON)
    except Exception as e:
        print(theta_deg, "error", e)

print("---- power of point check & second intersection ----")
theta = np.radians(30)
rK,rL = fsolve(residuals,[1,1],args=(theta,A,B,C,sign_orient))
K,L,M,N = build(theta, rK, rL, A,B,C, sign_orient)
O = circumcenter(A,K,L)
R = np.linalg.norm(O-A)
powM = np.dot(M-O,M-O) - R**2
powN = np.dot(N-O,N-O) - R**2
print("powM",powM,"powN",powN)

# second intersection of line AB with circle(A,K,L)
def second_intersection(A, dirvec, O, R):
    u = dirvec/np.linalg.norm(dirvec)
    t2 = -2*np.dot(u, A-O)
    return A + t2*u, t2

Xpt, tX = second_intersection(A, B-A, O, R)
Ypt, tY = second_intersection(A, C-A, O, R)
AB = np.linalg.norm(B-A); AC=np.linalg.norm(C-A)
AM = AB/2; AN=AC/2
# pow(M) = AM*(AM - tX) since M is at parameter AM along unit(B-A)
print("AM*(AM-tX)=", AM*(AM-tX), " vs powM=",powM)
print("AN*(AN-tY)=", AN*(AN-tY), " vs powN=",powN)
print("tX (chord A-X length signed)=",tX,"tY=",tY)
print("AB",AB,"AC",AC)

print("---- check clean identity AO.BC = (AC^2-AB^2)/4 ----")
AO = O-A
BC = C-B
lhs = np.dot(AO,BC)
rhs = (AC**2-AB**2)/4
print("lhs=",lhs,"rhs=",rhs)

print("---- tangency checks: is BK tangent to circle(AKL) at K? is CL tangent at L? ----")
OK = K-O
BKvec = K-B
print("OK . BK (should be ~0 if tangent):", np.dot(OK,BKvec), " |OK|=",np.linalg.norm(OK),"|BK|=",np.linalg.norm(BKvec))
OL = L-O
CLvec = L-C
print("OL . CL (should be ~0 if tangent):", np.dot(OL,CLvec))

# also check pow(B) = BK^2 if tangent, compare to OB^2-R^2
powB = np.dot(B-O,B-O)-R**2
powC = np.dot(C-O,C-O)-R**2
print("powB=",powB," BK^2=",np.dot(BKvec,BKvec))
print("powC=",powC," CL^2=",np.dot(CLvec,CLvec))
print("powB-powC=",powB-powC," (AB^2-AC^2)/2=",(AB**2-AC**2)/2)
