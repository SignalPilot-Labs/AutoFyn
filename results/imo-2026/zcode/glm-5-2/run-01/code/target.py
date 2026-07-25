import pickle, sympy as sp
from sympy import symbols, expand, factor, Poly, groebner, Rational, simplify, together, numer, denom, cancel
with open('/tmp/geom/conds.pkl','rb') as f:
    d=pickle.load(f)
condA=d['condA']; condB=d['condB']
Kx,Ky,Kden=d['Kx'],d['Ky'],d['Kden']
Lx,Ly,Lden=d['Lx'],d['Ly'],d['Lden']
A,P,G,p,q = symbols('A P G p q')
for name in ['condA','condB','Kx','Ky','Kden','Lx','Ly','Lden']:
    d[name]=d[name].subs({str(s):s for s in [A,P,G,p,q]})
condA=d['condA']; condB=d['condB']; Kx=d['Kx']; Ky=d['Ky']; Kden=d['Kden']; Lx=d['Lx']; Ly=d['Ly']; Lden=d['Lden']

# OM^2 - ON^2 with O circumcenter of A=(0,0),K,L.
# O satisfies O·K=|K|^2/2, O·L=|L|^2/2. 
# OM=ON  <=>  |O-M|^2=|O-N|^2  <=>  2 O·(N-M) = |N|^2 - |M|^2.
# M=(1/2,0), N=(p/2,q/2). N-M=((p-1)/2, q/2). |N|^2=(p^2+q^2)/4. |M|^2=1/4.
# |N|^2-|M|^2 = (p^2+q^2-1)/4.
# So OM=ON  <=>  2 O·((p-1)/2, q/2) = (p^2+q^2-1)/4
#            <=>  O·(p-1, q) = (p^2+q^2-1)/4.   (Eq *)
# Express O·(p-1,q) = ox(p-1)+oy q. 
# From O·K = |K|^2/2 and O·L=|L|^2/2, solve ox,oy. 
# K=(Kx/Kden,Ky/Kden), L=(Lx/Lden,Ly/Lden).
# Clearing denoms: let O=(ox,oy). 
#  ox*Kx+oy*Ky = (Kx^2+Ky^2)/(2 Kden).   (mult orig by Kden)
# Wait O·K = ox*(Kx/Kden)+oy*(Ky/Kden) = (Kx^2+Ky^2)/(2 Kden^2). 
# => ox*Kx+oy*Ky = (Kx^2+Ky^2)/(2 Kden).
# Similarly ox*Lx+oy*Ly = (Lx^2+Ly^2)/(2 Lden).
# Solve for ox,oy via Cramer. det = Kx*Ly - Ky*Lx.
DET = expand(Kx*Ly - Ky*Lx)
RHSx = expand((Kx**2+Ky**2)/(2*Kden)); RHSy = expand((Lx**2+Ly**2)/(2*Lden))
# ox = (RHSx*Ly - Ky*RHSy)/DET ; oy = (Kx*RHSy - RHSx*Lx)/DET
ox = expand((RHSx*Ly - Ky*RHSy)); oy = expand((Kx*RHSy - RHSx*Lx))  # numerator; common denom DET
# Target Eq (*): ox(p-1)+oy q = (p^2+q^2-1)/4 * DET
TARGET = expand(ox*(p-1) + oy*q - (p**2+q**2-1)*DET/4)
print("TARGET (should be 0 mod ideal) free symbols:", TARGET.free_symbols)
print("TARGET num terms:", len(expand(TARGET).as_ordered_terms()))
# Save
with open('/tmp/geom/target.pkl','wb') as f:
    pickle.dump(dict(TARGET=TARGET, condA=condA, condB=condB, Kx=Kx,Ky=Ky,Kden=Kden,Lx=Lx,Ly=Ly,Lden=Lden, DET=DET), f)
print("saved target")
