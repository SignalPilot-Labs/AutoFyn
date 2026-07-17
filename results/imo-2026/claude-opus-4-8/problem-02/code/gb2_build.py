import sympy as sp
cA,sA,cC,sC,cth,sth,t,s=sp.symbols('cA sA cC sC cth sth t s')
cB=sA*sC-cA*cC; sB=sA*cC+cA*sC
kx=cB*cth+sB*sth; ky=sB*cth-cB*sth
AX=sC*cB; AY=sC*sB
p0=sC*cth-cC*sth; p1=-(cC*cth+sC*sth)
c2=cth**2-sth**2; s2=2*sth*cth
q0=sA*c2+cA*s2; q1=cA*c2-sA*s2
m=p0
pb0=sB*cth-cB*sth; pb1=-(cB*cth+sB*sth)
cg=1-t**2; sg=2*t
BKden=q0*cg+q1*sg
Kx=(p0*cg+p1*sg)*kx; Ky=(p0*cg+p1*sg)*ky
Ux=sA*Kx-AX*BKden; Uy=sA*Ky-AY*BKden
cbN=1-s**2; sbN=2*s
BLdenN=q0*cbN+q1*sbN
dLxN=kx*cbN+ky*sbN; dLyN=ky*cbN-kx*sbN
Lx=m*dLxN; Ly=m*dLyN
Vx=sA*Lx-AX*BLdenN; Vy=sA*Ly-AY*BLdenN
DK=sA*BKden; DL=sA*BLdenN
TN=sA*2*((Ux**2+Uy**2)*Vy*DL-(Vx**2+Vy**2)*Uy*DK)-(Ux*Vy-Uy*Vx)*DK*DL*(sA-2*AX)
TN=sp.expand(TN)
P=sp.expand(sg*sC*(q0*cg+q1*sg)-2*sA*(sth*cg+cth*sg)*(p0*cg+p1*sg))
Q=sp.expand(sbN*sB*(q0*cbN+q1*sbN)-2*sA*(sth*cbN+cth*sbN)*(pb0*cbN+pb1*sbN))
