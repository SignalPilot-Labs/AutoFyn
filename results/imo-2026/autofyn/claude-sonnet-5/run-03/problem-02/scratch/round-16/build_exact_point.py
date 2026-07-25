import pickle, sympy as sp

with open('/tmp/round-15/sos_work/polys.pkl','rb') as f:
    d = pickle.load(f)
Num,n1num,n2num,u,cB,sB = d['Num'],d['n1num'],d['n2num'],d['u'],d['cB'],d['sB']
n4sq = (1+u**2)**3*cB**2 - u**2*(3-u**2)**2

# Exact rational witness point, chosen near the hard numeric point (A,B)~(0.603,1.269):
# cB,sB via rational Pythagorean parametrization with r=tan(B/2)=7/10 -> (cB,sB)=(51/149,140/149)
# u = 93/1000  (approx A = 6*atan(u) ~ 0.5578, close to 0.603; genuine Case(b) domain point)
cBv = sp.Rational(51,149); sBv = sp.Rational(140,149)
uv0 = sp.Rational(93,1000)

Nu = sp.expand(Num.subs({cB:cBv, sB:sBv}))
N1 = sp.expand(n1num.subs({cB:cBv, sB:sBv}))
N2 = sp.expand(n2num.subs({cB:cBv, sB:sBv}))
N4 = sp.expand(n4sq.subs({cB:cBv}))

# sanity: values at u0 all strictly positive (domain membership)
for name,P in [('Num',Nu),('n1',N1),('n2',N2),('n4sq',N4)]:
    val = P.subs(u, uv0)
    print(name, 'at u0:', float(val))

# rescale u -> s via u = c*s, c chosen for conditioning (c=1/10, so s0 = 0.93)
s = sp.symbols('s', real=True)
c = sp.Rational(1,10)
usub = c*s

def rescale(poly):
    p = sp.expand(poly.subs(u, usub))
    return sp.Poly(p, s)

PNu = rescale(Nu)
PN1 = rescale(N1)
PN2 = rescale(N2)
PN4 = rescale(N4)

def coeffs_dict(P):
    cd = P.as_dict()
    return {k[0]: v for k,v in cd.items()}

cNu = coeffs_dict(PNu)
cN1 = coeffs_dict(PN1)
cN2 = coeffs_dict(PN2)
cN4 = coeffs_dict(PN4)

print("deg Num,n1,n2,n4sq:", PNu.degree(), PN1.degree(), PN2.degree(), PN4.degree())
print("s0 =", float(uv0/c))

with open('/tmp/round-16/exact_point_data.pkl','wb') as fh:
    pickle.dump({
        'cBv': cBv, 'sBv': sBv, 'uv0': uv0, 'c': c,
        'Nu_exact': Nu, 'N1_exact': N1, 'N2_exact': N2, 'N4_exact': N4,
        'cNu': cNu, 'cN1': cN1, 'cN2': cN2, 'cN4': cN4,
        'u_sym': u, 's_sym': s,
    }, fh)
print("saved.")
