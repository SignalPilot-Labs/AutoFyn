import numpy as np
A = np.array([0.0,3.2])
B = np.array([-2.3,0.0])
C = np.array([2.7,0.0])
M=(A+B)/2; N=(A+C)/2
G=(A+B+C)/3

def d(P,Q): return np.linalg.norm(P-Q)
print("GM,GN:", d(G,M), d(G,N))  # check if centroid on perp bisector of MN

# circumcenter of ABC
def circumcenter(A,B,C):
    ax,ay=A; bx,by=B; cx,cy=C
    dd = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/dd
    uy = ((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/dd
    return np.array([ux,uy])
Ocirc = circumcenter(A,B,C)
print("circumcenter ABC dist to M,N:", d(Ocirc,M), d(Ocirc,N))

# midpoint of BC, and its distance
Mbc = (B+C)/2
print("midpoint BC dist to M,N:", d(Mbc,M), d(Mbc,N))

# check line MN perpendicular bisector direction: should be perpendicular to MN (which is parallel to BC)
dirMN = N-M
perp = np.array([-dirMN[1], dirMN[0]])
print("MN dir", dirMN, "BC dir", C-B)  # check parallel
midMN = (M+N)/2
print("midpoint of MN:", midMN)

# Is midpoint of AG (or A and circumcenter) on line? test the foot of altitude from A? 
# Let's just check the general formula: is the locus PB^2-PC^2 = AB^2-AC^2 the same as PM=PN?
import random
AB2 = d(A,B)**2; AC2=d(A,C)**2
for _ in range(3):
    P = np.random.randn(2)*3
    lhs = d(P,B)**2-d(P,C)**2
    print("check random P: (PB2-PC2)-(AB2-AC2)=", lhs-(AB2-AC2), "  PM2-PN2=", d(P,M)**2-d(P,N)**2)
