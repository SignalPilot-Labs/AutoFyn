import numpy as np
from scipy.optimize import fsolve
exec(open('/tmp/round-1/imo2026_02_probe.py').read().split("# Triangle 1")[0])

A = np.array([0.0,3.0])
B = np.array([-1.5,0.0])
C = np.array([2.2,0.0])
M = (A+B)/2
N = (A+C)/2
angleB = angle_between(A-B, C-B)
angleC = angle_between(A-C, B-C)

guess=(1.0,1.0)
print(f"{'phi':>8} {'R=OA':>8} {'OB':>8} {'OC':>8} {'angBAK':>8} {'angCAL':>8} {'angKAL':>8} {'AK/AB':>8} {'AL/AC':>8} {'BK':>8} {'CL':>8}")
for phi in np.linspace(0.05*min(angleB,angleC), 0.95*min(angleB,angleC), 12):
    rvec, ier, dB, dC, M, N = solve_config(A,B,C,phi, guess=guess)
    if ier==1:
        rK, rL = rvec
        if rK>0 and rL>0:
            K = B+rK*dB
            L = C+rL*dC
            O = circumcenter(A,K,L)
            R = np.linalg.norm(O-A)
            OB = np.linalg.norm(O-B)
            OC = np.linalg.norm(O-C)
            angBAK = angle_between(B-A,K-A)
            angCAL = angle_between(C-A,L-A)
            angKAL = angle_between(K-A,L-A)
            AB = np.linalg.norm(A-B); AC=np.linalg.norm(A-C)
            AK = np.linalg.norm(A-K); AL=np.linalg.norm(A-L)
            BK = np.linalg.norm(B-K); CL=np.linalg.norm(C-L)
            print(f"{phi:8.4f} {R:8.4f} {OB:8.4f} {OC:8.4f} {angBAK:8.4f} {angCAL:8.4f} {angKAL:8.4f} {AK/AB:8.4f} {AL/AC:8.4f} {BK:8.4f} {CL:8.4f}")
            guess=(rK,rL)

print("\nAngle A =", angle_between(B-A,C-A))
