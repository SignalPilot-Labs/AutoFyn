import sympy as sp, pickle, random
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')
d = pickle.load(open('sol.pkl','rb'))
Xs=sp.sympify(d['Xs']); Ys=sp.sympify(d['Ys']); Zs=sp.sympify(d['Zs'])
D = k*lb - kb*l
TN = 2*k*l*(lb-kb)*(cb-bb) + 2*kb*lb*(k-l)*(c-b) - (c*cb - b*bb)*D
TN_sub = sp.cancel(sp.together(TN.subs({kb:Ys, lb:Zs})))
num = sp.expand(sp.numer(TN_sub))
R = sp.cancel(Ys*Zs - Xs)
Rnum = sp.expand(sp.numer(sp.together(R)))
# gcd test
g = sp.gcd(num, Rnum)
print("gcd(num,Rnum) total degree:", 0 if g.is_number else sp.Poly(g,k,l,b,c,bb,cb).total_degree())
# random points on Rnum=0 (solve for k), fully generic (bb,cb NOT conj of b,c)
import numpy as np
Rpoly = sp.Poly(Rnum, k)
print("Rnum degree in k:", Rpoly.degree())
cnt_ok=0; cnt=0
for trial in range(6):
    sub = {v: complex(random.uniform(-2,2),random.uniform(-2,2)) for v in (l,b,c,bb,cb)}
    coeffs = [complex(cf.subs(sub)) for cf in Rpoly.all_coeffs()]
    roots = np.roots(coeffs)
    for kr in roots:
        s = dict(sub); s[k]=complex(kr)
        rval = complex(Rnum.subs(s))
        nval = complex(num.subs(s))
        cnt+=1
        if abs(nval)<1e-6*max(1,abs(complex(num.subs({k:complex(0.3,0.4),**sub})))):
            cnt_ok+=1
        print(f"  Rnum={abs(rval):.2e}  num={abs(nval):.3e}")
print(f"random-on-R: {cnt_ok}/{cnt} had num~0")
