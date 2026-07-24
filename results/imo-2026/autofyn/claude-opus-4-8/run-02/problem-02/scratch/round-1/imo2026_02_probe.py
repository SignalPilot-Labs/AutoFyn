import numpy as np
from scipy.optimize import fsolve, brentq

def unit(v):
    return v/np.linalg.norm(v)

def angle_between(u,v):
    # signed magnitude 0..pi
    cu = np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))
    cu = max(-1,min(1,cu))
    return np.arccos(cu)

def solve_config(A,B,C, phi, guess=(1.0,1.0)):
    M = (A+B)/2
    N = (A+C)/2
    uB = unit(A-B)  # BA direction
    vB = unit(C-B)  # BC direction
    uB_perp = unit(vB - np.dot(vB,uB)*uB)
    def dirB(phi):
        return np.cos(phi)*uB + np.sin(phi)*uB_perp

    uC = unit(A-C)  # CA direction
    vC = unit(B-C)  # CB direction
    uC_perp = unit(vC - np.dot(vC,uC)*uC)
    def dirC(phi):
        return np.cos(phi)*uC + np.sin(phi)*uC_perp

    dB = dirB(phi)
    dC = dirC(phi)

    def eqs(rvec):
        rK, rL = rvec
        K = B + rK*dB
        L = C + rL*dC
        # angle LBK at vertex B between BL and BK
        angLBK = angle_between(L-B, K-B)
        # angle LNC at vertex N between NL and NC
        angLNC = angle_between(L-N, C-N)
        # angle LCK at vertex C between CL and CK
        angLCK = angle_between(L-C, K-C)
        # angle BMK at vertex M between MB and MK
        angBMK = angle_between(B-M, K-M)
        return [angLBK-angLNC, angLCK-angBMK]

    sol = fsolve(eqs, guess, full_output=True)
    rvec, info, ier, msg = sol
    return rvec, ier, dB, dC, M, N

def circumcenter(P1,P2,P3):
    ax,ay = P1; bx,by=P2; cx,cy=P3
    d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy = ((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

# Triangle 1: scalene
A = np.array([0.0,3.0])
B = np.array([-1.5,0.0])
C = np.array([2.2,0.0])

M = (A+B)/2
N = (A+C)/2

angleB = angle_between(A-B, C-B)
angleC = angle_between(A-C, B-C)
print("angle B, angle C (rad):", angleB, angleC)

results=[]
guess=(1.0,1.0)
for phi in np.linspace(0.05*min(angleB,angleC), 0.95*min(angleB,angleC), 15):
    rvec, ier, dB, dC, M, N = solve_config(A,B,C,phi, guess=guess)
    if ier==1:
        rK, rL = rvec
        if rK>0 and rL>0:
            K = B+rK*dB
            L = C+rL*dC
            O = circumcenter(A,K,L)
            OM = np.linalg.norm(O-M)
            ON = np.linalg.norm(O-N)
            AK = np.linalg.norm(A-K)
            AL = np.linalg.norm(A-L)
            results.append((phi,rK,rL,K,L,O,OM,ON,AK,AL))
            guess=(rK,rL)

print(f"{'phi':>8} {'rK':>8} {'rL':>8} {'OM':>8} {'ON':>8} {'AK':>8} {'AL':>8}")
for phi,rK,rL,K,L,O,OM,ON,AK,AL in results:
    print(f"{phi:8.4f} {rK:8.4f} {rL:8.4f} {OM:8.4f} {ON:8.4f} {AK:8.4f} {AL:8.4f}")

# Check O lies on perpendicular bisector of MN precisely, and test second triangle
print("\n--- check perpendicular bisector of MN ---")
midMN = (M+N)/2
dirMN = unit(N-M)
for phi,rK,rL,K,L,O,OM,ON,AK,AL in results:
    v = O-midMN
    perp_component = np.dot(v, dirMN)
    print(f"phi={phi:.4f}  O-midMN . dirMN = {perp_component:.10f}  (should be 0)")

print("\n--- Second triangle (different shape) ---")
A2 = np.array([0.3,2.1])
B2 = np.array([-2.0,0.0])
C2 = np.array([1.0,0.0])
M2 = (A2+B2)/2
N2 = (A2+C2)/2
angleB2 = angle_between(A2-B2,C2-B2)
angleC2 = angle_between(A2-C2,B2-C2)
print("angle B2, angle C2:", angleB2, angleC2)
guess=(1.0,1.0)
res2=[]
for phi in np.linspace(0.05*min(angleB2,angleC2), 0.95*min(angleB2,angleC2), 10):
    rvec, ier, dB, dC, Mx, Nx = solve_config(A2,B2,C2,phi, guess=guess)
    if ier==1:
        rK, rL = rvec
        if rK>0 and rL>0:
            K = B2+rK*dB
            L = C2+rL*dC
            O = circumcenter(A2,K,L)
            OM = np.linalg.norm(O-M2)
            ON = np.linalg.norm(O-N2)
            res2.append((phi,rK,rL,OM,ON))
            guess=(rK,rL)
print(f"{'phi':>8} {'rK':>8} {'rL':>8} {'OM':>8} {'ON':>8}")
for phi,rK,rL,OM,ON in res2:
    print(f"{phi:8.4f} {rK:8.4f} {rL:8.4f} {OM:8.4f} {ON:8.4f}")
