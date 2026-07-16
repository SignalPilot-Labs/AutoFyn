# Reproduction / verification script for the complex-reality-conditions proof
# of IMO 2026 P2 (prove OM = ON).  Every algebraic identity used in the proof
# is checked here symbolically; a numerical configuration is checked too.
import sympy as sp
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')  # kb=conj k, etc.

# --- reality conditions cleared of denominators: E_i = numerator of C_i - conj(C_i) ---
E1 = sp.expand(b*c*(kb-bb)*(lb-cb) - bb*cb*(k-b)*(l-c))
E2 = sp.expand((k-b)*(2*l-c)*cb*(lb-bb) - (kb-bb)*(2*lb-cb)*c*(l-b))
E3 = sp.expand(b*(k-c)*(lb-cb)*(2*kb-bb) - bb*(kb-cb)*(l-c)*(2*k-b))

# (a) each E_i is affine in the monomials (X,Y,Z)=(kb*lb, kb, lb)
def coeffs(E):
    a=E.coeff(kb,1).coeff(lb,1); p=E.coeff(kb,1).coeff(lb,0)
    q=E.coeff(kb,0).coeff(lb,1); d=E.coeff(kb,0).coeff(lb,0)
    assert sp.expand(E-(a*kb*lb+p*kb+q*lb+d))==0
    return a,p,q,d
rows=[coeffs(E) for E in (E1,E2,E3)]
print("(a) each E_i is affine in (kb*lb, kb, lb): OK")
A=sp.Matrix([[r[0],r[1],r[2]] for r in rows]); rhs=sp.Matrix([-r[3] for r in rows])

# (b) det A = b*bb*c*cb*P4
detA=sp.expand(A.det())
print("(b) det A factors as:", sp.factor(detA))

# Cramer solution (X,Y,Z)=(kb*lb, kb, lb)
sol=A.LUsolve(rhs); Xs,Ys,Zs=[sp.cancel(sol[i]) for i in range(3)]

# --- target TN (OM=ON  <=>  TN=0) ---
D=k*lb-kb*l
TN=2*k*l*(lb-kb)*(cb-bb)+2*kb*lb*(k-l)*(c-b)-(c*cb-b*bb)*D

# substitute solved conjugates; consistency relation Rnum
num =sp.expand(sp.numer(sp.cancel(sp.together(TN.subs({kb:Ys,lb:Zs})))))
Rnum=sp.expand(sp.numer(sp.together(sp.cancel(Ys*Zs-Xs))))
G   =sp.expand(sp.gcd(num,Rnum))
qN  =sp.expand(sp.cancel(num/G))

# (c) the two certified identities
print("(I)  Rnum = (b-k)(c-l)*G      :", sp.expand(Rnum-(b-k)*(c-l)*G)==0)
print("(II) num  = qN*G (qN a poly)  :", sp.expand(num-qN*G)==0 and sp.denom(qN)==1)
print("     deg G =", sp.Poly(G,k,l,b,c,bb,cb).total_degree())
print("     qN =", qN)

# --- numeric configuration (audited scalene, alpha = 15 deg) ---
vals={b:complex(-0.5,-1.5),c:complex(1.5,-1.5),
      k:complex(-0.2531182195716988,-1.1260806200681075),
      l:complex(0.7866438932120947,-1.0881436597179395)}
vals[bb]=vals[b].conjugate(); vals[cb]=vals[c].conjugate()
vals[kb]=vals[k].conjugate(); vals[lb]=vals[l].conjugate()
print("--- numeric check on audited configuration ---")
for nm,e in [('E1',E1),('E2',E2),('E3',E3),('G',G),('num',num),('TN',TN),
             ('b*cb-bb*c (NC)',b*cb-bb*c),('b-k (ND)',b-k),('c-l (ND)',c-l),
             ('D (NL)',D),('qN',qN),('P4 (detA factor)',detA/(b*bb*c*cb))]:
    print(f"  {nm:22s} = {complex(sp.N(e.subs(vals))):.3e}")
