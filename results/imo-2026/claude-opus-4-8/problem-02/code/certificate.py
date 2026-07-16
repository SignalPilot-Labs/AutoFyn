# Unconditional polynomial certificate closing the detA=0 gap for
# complex-reality-conditions (IMO 2026 P2).  Works on the PHYSICAL (real) variety:
# conjugates are forced (kb=conj k, ...), WLOG b=1 by similarity/homogeneity.
# Certifies  W * Im(TN)  in  ( Im E1, Im E2, Im E3 )  with W a product of
# non-degeneracy factors, NONE of which is detA.  Exact (symbolic) throughout.
import sympy as sp

c1,c2,k1,k2,l1,l2 = sp.symbols('c1 c2 k1 k2 l1 l2', real=True)
I = sp.I
b = sp.Integer(1); bb = sp.Integer(1)            # WLOG B = 1 (real)
c = c1+I*c2;  cb = c1-I*c2
k = k1+I*k2;  kb = k1-I*k2
l = l1+I*l2;  lb = l1-I*l2

# reality-condition numerators E_i (= C_i - conj C_i, cleared);  each has the
# form  z - conj(z), hence is purely imaginary
E1 = b*c*(kb-bb)*(lb-cb) - bb*cb*(k-b)*(l-c)
E2 = (k-b)*(2*l-c)*cb*(lb-bb) - (kb-bb)*(2*lb-cb)*c*(l-b)
E3 = b*(k-c)*(lb-cb)*(2*kb-bb) - bb*(kb-cb)*(l-c)*(2*k-b)
D  = k*lb - kb*l
TN = 2*k*l*(lb-kb)*(cb-bb) + 2*kb*lb*(k-l)*(c-b) - (c*cb-b*bb)*D

def re(z): return sp.expand(sp.re(sp.expand(z)))
def im(z): return sp.expand(sp.im(sp.expand(z)))

# (0) E1,E2,E3,TN are purely imaginary (real parts vanish identically)
print("Re(E1),Re(E2),Re(E3),Re(TN) all 0 :",
      re(E1)==0, re(E2)==0, re(E3)==0, re(TN)==0)

iE1,iE2,iE3,iTN = im(E1),im(E2),im(E3),im(TN)

# non-degeneracy factors (each nonzero on an admissible configuration):
nv1 = sp.expand((k1-1)**2 + k2**2)          # |B-K|^2 > 0            (ND: K != B)
nv2 = sp.expand((l1-c1)**2 + (l2-c2)**2)    # |C-L|^2 > 0            (ND: L != C)
NL  = sp.expand(sp.im(sp.expand(kb*l)))     # Im(conj(k) l) != 0     (NL: A,K,L noncollinear)
NC  = sp.expand(sp.im(sp.expand(bb*c)))     # Im(conj(b) c) != 0     (NC: A,B,C noncollinear)
W   = sp.expand(nv1*nv2*NL*NC)

# (1) ideal membership: W * iTN in (iE1,iE2,iE3)  (saturation power N=1)
G = sp.groebner([iE1,iE2,iE3], k1,k2,l1,l2,c1,c2, order='grevlex')
print("N=0: iTN in ideal? ", G.reduce(iTN)[1]==0)
print("N=1: W*iTN in ideal?", G.reduce(sp.expand(W*iTN))[1]==0)

# (2) the cofactors f1,f2,f3 with  W*iTN = f1 iE1 + f2 iE2 + f3 iE3  exist because the
#     reduction to remainder 0 succeeds (Buchberger's algorithm is an exact decision
#     procedure for ideal membership); the reduction against the Groebner basis is exact:
q, r = sp.reduced(sp.expand(W*iTN), list(G.exprs), k1,k2,l1,l2,c1,c2, order='grevlex')
print("remainder after division by GB is 0:", sp.expand(r)==0)

# (3) numeric cross-check on the audited configuration (normalized to B=1). SANITY ONLY.
Bc=complex(-0.5,-1.5); Cc=complex(1.5,-1.5)
Kc=complex(-0.2531182195716988,-1.1260806200681075)
Lc=complex(0.7866438932120947,-1.0881436597179395)
Cn,Kn,Ln=Cc/Bc,Kc/Bc,Lc/Bc
vals={c1:Cn.real,c2:Cn.imag,k1:Kn.real,k2:Kn.imag,l1:Ln.real,l2:Ln.imag}
print("audited (B=1): iE1,iE2,iE3,iTN =",
      [float(sp.N(e.subs(vals))) for e in (iE1,iE2,iE3,iTN)], " W =", float(sp.N(W.subs(vals))))
