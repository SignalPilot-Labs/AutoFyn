import sympy as sp, sys, time, math
from sympy import symbols,together,fraction,Poly,div,cancel,expand,groebner
from numpy import sin,cos

v = sp.Symbol('v')
sa,ca,sb,cb,sA,cA = sp.symbols('sa ca sb cb sA cA')
sAa = sA*ca + cA*sa;   cAa = cA*ca - sA*sa
sA2a = sAa*ca + cAa*sa; cA2a = cAa*ca - sAa*sa
sab = sa*cb + ca*sb;    cab = ca*cb - sa*sb
sAab = sAa*cb + cAa*sb
sA2ab = sA2a*cb + cA2a*cb  # bug? fix below
sA2ab = sA2a*cb + cA2a*sb
sg = 2*v/(1+v**2); cg = (1-v**2)/(1+v**2)
sag = sa*cg + ca*sg; sAag = sAa*cg + cAa*sg; sA2ag = sA2a*cg + cA2a*sg
def log(*a): print(*a); sys.stdout.flush()
t0=time.time()
kx = 1 - sg*ca/(2*sag); ky = sg*sa/(2*sag)
lx = cA - sb*cAa/(2*sab); ly = sA - sb*sAa/(2*sab)
K2 = sp.cancel(kx**2+ky**2); L2 = sp.cancel(lx**2+ly**2)
kxl = sp.cancel(kx*ly-ky*lx); kxcA = sp.cancel(kx*sA-ky*cA); lxcA = sp.cancel(lx*sA-ly*cA)
P = sp.cancel(2*sag**2); Q = sp.cancel(-(2*sAag*sag - sg*sA2ag))
R = sp.cancel(2*sab*sAab - sb*sA2ab); Sg = sp.cancel(-2*sab**2)
numHp = sp.cancel(2*Q*Sg*L2*kxcA - 2*P*Sg*(L2*ky - K2*lxcA) - 2*R*P*K2*ly)
Hp = numHp/kxl + (R*P - Q*Sg)
C = sp.cancel(P*Sg - Q*R)
log("assembled t",round(time.time()-t0,2))
# Clear ALL denominators (in v and symbols) to a single polynomial each.
# Hp = numHp/kxl + (RP-QS). H_poly = numHp + kxl*(RP-QS)  ( = Hp*kxl ), poly once v-denoms cleared.
Hsemi = sp.cancel(numHp + kxl*(R*P - Q*Sg))   # = Hp * kxl, rational in v (denoms (1+v^2) powers)
Csemi = C
# get full polynomials: together then numerator
Ht=together(Hsemi); Hn,Hd=fraction(Ht); Hn=expand(Hn)
Ct=together(Csemi); Cn,Cd=fraction(Ct); Cn=expand(Cn)
log("cleared. Hn ops",sp.count_ops(Hn),"Cn ops",sp.count_ops(Cn),"t",round(time.time()-t0,2))
# numeric sanity: Hn vanishes on locus
def evp(e,vals):
    f=sp.lambdify((sa,ca,sb,cb,sA,cA,v),e,'numpy'); return float(f(*vals))
ad=math.radians(20);bd=math.radians(35.2414494241406);gd=math.radians(17.963453537582254);Ad=math.radians(60)
vals=(sin(ad),cos(ad),sin(bd),cos(bd),sin(Ad),cos(Ad),math.tan(gd/2))
log("Hn(on locus)=",evp(Hn,vals)," Cn(on locus)=",evp(Cn,vals))
# Groebner of [Cn, pyth1, pyth2, pyth3], reduce Hn.
pyth = [sa**2+ca**2-1, sb**2+cb**2-1, sA**2+cA**2-1]
gens = [cA,sA,cb,sb,ca,sa,v]
t1=time.time()
log("computing groebner...")
try:
    G = groebner([Cn]+pyth, gens, order='lex')
    log("groebner done t",round(time.time()-t1,2),"len",len(G))
    nf = sp.Poly(Hn, gens, domain='ZZ').div([sp.Poly(g,gens,domain='ZZ') for g in G])
    log("nf rem ops",sp.count_ops(nf[1].as_expr()))
    log("nf rem==0?", nf[1].is_zero)
except Exception as e:
    log("groebner failed:",repr(e),"t",round(time.time()-t1,2))
