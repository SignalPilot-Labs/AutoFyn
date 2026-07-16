import sympy as sp, pickle
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')
E1 = sp.expand(b*c*(kb-bb)*(lb-cb) - bb*cb*(k-b)*(l-c))
E2 = sp.expand((k-b)*(2*l-c)*cb*(lb-bb) - (kb-bb)*(2*lb-cb)*c*(l-b))
E3 = sp.expand(b*(k-c)*(lb-cb)*(2*kb-bb) - bb*(kb-cb)*(l-c)*(2*k-b))
X,Y,Z = sp.symbols('X Y Z')
def coeffs(E):
    a=E.coeff(kb,1).coeff(lb,1); p=E.coeff(kb,1).coeff(lb,0)
    q=E.coeff(kb,0).coeff(lb,1); dd=E.coeff(kb,0).coeff(lb,0)
    assert sp.expand(E-(a*kb*lb+p*kb+q*lb+dd))==0
    return a,p,q,dd
rows=[coeffs(E) for E in (E1,E2,E3)]
A=sp.Matrix([[r[0],r[1],r[2]] for r in rows]); rhs=sp.Matrix([-r[3] for r in rows])
detA=sp.factor(A.det())
sol=A.LUsolve(rhs); Xs,Ys,Zs=[sp.cancel(sol[i]) for i in range(3)]
D=k*lb-kb*l
TN=2*k*l*(lb-kb)*(cb-bb)+2*kb*lb*(k-l)*(c-b)-(c*cb-b*bb)*D
num=sp.expand(sp.numer(sp.cancel(sp.together(TN.subs({kb:Ys,lb:Zs})))))
R=sp.cancel(Ys*Zs-Xs); Rnum=sp.expand(sp.numer(sp.together(R)))
fN=sp.factor(num); fR=sp.factor(Rnum)
# extract W as gcd of num and Rnum
W=sp.gcd(num,Rnum)
print("W total degree:", sp.Poly(W,k,l,b,c,bb,cb).total_degree())
# V := num / (-(b*cb-bb*c)*W)
bcb=b*cb-bb*c
Vq,Vr=sp.div(sp.expand(num), sp.expand(-bcb*W), k)
print("num = -(bcb)*V*W exact?", sp.expand(num +bcb*W*Vq)==0 and Vr==0)
# Rnum = (b-k)(c-l)(bcb)*W exact?
print("Rnum = (b-k)(c-l)(bcb)*W exact?", sp.expand(Rnum-(b-k)*(c-l)*bcb*W)==0)
V=sp.expand(Vq)
# numeric checks at geometry
vals={b:complex(-0.5,-1.5),c:complex(1.5,-1.5),
      k:complex(-0.2531182195716988,-1.1260806200681075),
      l:complex(0.7866438932120947,-1.0881436597179395)}
vals[bb]=vals[b].conjugate();vals[cb]=vals[c].conjugate()
P4=detA/(b*bb*c*cb)
print("P4(detA) nonzero:", abs(complex(sp.expand(P4).subs(vals))))
print("W at geometry (should ~0):", abs(complex(W.subs(vals))))
print("V at geometry (nonzero):", abs(complex(V.subs(vals))))
print("bcb at geometry (nonzero):", abs(complex(bcb.subs(vals))))
print("num at geometry (~0):", abs(complex(num.subs(vals))))
# save W, V for writeup
pickle.dump({'W':sp.srepr(sp.expand(W)),'V':sp.srepr(V),'detA':sp.srepr(sp.expand(detA)),
             'Xs':sp.srepr(Xs),'Ys':sp.srepr(Ys),'Zs':sp.srepr(Zs)}, open('final.pkl','wb'))
print("saved")
print("W=",sp.expand(W))
