import sympy as sp
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')
E1 = sp.expand(b*c*(kb-bb)*(lb-cb) - bb*cb*(k-b)*(l-c))
E2 = sp.expand((k-b)*(2*l-c)*cb*(lb-bb) - (kb-bb)*(2*lb-cb)*c*(l-b))
E3 = sp.expand(b*(k-c)*(lb-cb)*(2*kb-bb) - bb*(kb-cb)*(l-c)*(2*k-b))

X,Y,Z = sp.symbols('X Y Z')  # X=kb*lb, Y=kb, Z=lb
def coeffs(E):
    # E = a*kb*lb + p*kb + q*lb + d
    a = E.coeff(kb,1).coeff(lb,1)
    p = E.coeff(kb,1).coeff(lb,0)
    q = E.coeff(kb,0).coeff(lb,1)
    d = E.coeff(kb,0).coeff(lb,0)
    # sanity
    assert sp.expand(E - (a*kb*lb+p*kb+q*lb+d))==0
    return a,p,q,d
rows=[coeffs(E) for E in (E1,E2,E3)]
A = sp.Matrix([[r[0],r[1],r[2]] for r in rows])
rhs = sp.Matrix([-r[3] for r in rows])
detA = sp.factor(A.det())
print("det A factored:")
print(detA)
sol = A.solve(rhs)  # [X,Y,Z]
Xs,Ys,Zs = [sp.cancel(sol[i]) for i in range(3)]
# geometric constraint R = Y*Z - X (times det^2 to clear denom)
sp.srepr  # noop
# numeric check that Y=kb, Z=lb, X=kb*lb, R=0
vals = {b:complex(-0.5,-1.5), c:complex(1.5,-1.5),
        k:complex(-0.2531182195716988,-1.1260806200681075),
        l:complex(0.7866438932120947,-1.0881436597179395)}
vals[bb]=vals[b].conjugate(); vals[cb]=vals[c].conjugate()
kbv=vals[k].conjugate(); lbv=vals[l].conjugate()
print("Y should be kb:", complex(Ys.subs(vals)), "actual kb:", kbv)
print("Z should be lb:", complex(Zs.subs(vals)), "actual lb:", lbv)
print("X should be kb*lb:", complex(Xs.subs(vals)), "actual:", kbv*lbv)
R = sp.cancel(Ys*Zs - Xs)
print("R numeric (should be 0):", complex(R.subs(vals)))
Rnum = sp.numer(sp.together(R))
print("Rnum degree info: ", sp.total_degree(sp.expand(Rnum)) if hasattr(sp,'total_degree') else 'na')
sp.pprint  # 
import pickle
with open('sol.pkl','wb') as f:
    pickle.dump({'Xs':sp.srepr(Xs),'Ys':sp.srepr(Ys),'Zs':sp.srepr(Zs)}, f)
print("saved")
