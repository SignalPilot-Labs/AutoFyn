import mpmath as mp
mp.mp.dps = 40

def X0(A,B):
    return mp.sin(B)*mp.cos(A)/(2*mp.sin(A+B))

def D2(A,B):
    beta0 = (mp.pi - A)/3
    sinA, cosA = mp.sin(A), mp.cos(A)
    sinB, cosB = mp.sin(B), mp.cos(B)
    Kc = 2*sinA*mp.sin(A+B)
    P = mp.mpf(1)/2*mp.sin(A-B) + mp.mpf(3)/2*mp.sin(A+B)
    Q = -sinA*sinB
    dKc_dB = 2*sinA*mp.cos(A+B)
    dP_dB = -mp.mpf(1)/2*mp.cos(A-B) + mp.mpf(3)/2*mp.cos(A+B)
    dQ_dB = -sinA*cosB
    dG_dB = dKc_dB - mp.sin(beta0)*dP_dB - mp.cos(beta0)*dQ_dB
    return -sinB*mp.cos(beta0) - mp.sin(beta0)*dG_dB

def dX0_dB(A,B):
    return mp.sin(A)*mp.cos(A)/(2*mp.sin(A+B)**2)

def T1(A,B):
    cosB = mp.cos(B)
    sinB = mp.sin(B)
    return (1+cosB)**2*dX0_dB(A,B) - 2*(1+cosB)*sinB*X0(A,B)

def Tgt(A,B):
    return 4*(1+mp.cos(B))**2*X0(A,B)*D2(A,B)**2 - T1(A,B)**2

corner = mp.pi/3
val0 = Tgt(corner,corner)
print("Tgt at corner:", val0)

# gradient by central difference
h = mp.mpf('1e-8')
gA = (Tgt(corner+h,corner) - Tgt(corner-h,corner))/(2*h)
gB = (Tgt(corner,corner+h) - Tgt(corner,corner-h))/(2*h)
print("gA (numeric):", gA)
print("gB (numeric):", gB)
