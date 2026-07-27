import sympy as sp
mu,beta,Bs,Cs=sp.symbols('mu beta B C',positive=True)
As=sp.pi-Bs-Cs
nu=As-mu
# delta from R': cot(delta) = sin(beta-mu)/(2 sin mu sin beta)
# epsilon from Ceva/AK-eq:  sinC sinbeta / sin(beta+mu) = sinB sin eps / sin(eps+nu)
# => cot eps = sinB sin(beta+mu)/(sinC sinbeta sin nu) - cot(nu)
coteps = sp.sin(Bs)*sp.sin(beta+mu)/(sp.sin(Cs)*sp.sin(beta)*sp.sin(nu)) - sp.cos(nu)/sp.sin(nu)
cotdelta = sp.sin(beta-mu)/(2*sp.sin(mu)*sp.sin(beta))
# constraint eps = beta + delta  <=>  cot(eps) = cot(beta+delta)
# cot(beta+delta) = (cotbeta*cotdelta - 1)/(cotbeta+cotdelta)
cotbeta=sp.cos(beta)/sp.sin(beta)
cotbetadelta=(cotbeta*cotdelta-1)/(cotbeta+cotdelta)
# CON = coteps - cot(beta+delta) ; constraint is CON=0
CON = sp.together(coteps - cotbetadelta)
CON_num = sp.fraction(CON)[0]   # numerator
# TARGET
T = 2*sp.sin(Cs)*sp.sin(mu)*sp.cos(beta+mu)*sp.sin(As+beta) - sp.sin(As)*sp.sin(beta+mu)*sp.sin(Cs-beta-mu)
# Check ratio CON_num / T
CON_num2=sp.expand_trig(CON_num)
T2=sp.expand_trig(T)
r=sp.cancel(CON_num2/T2)
print("cancel(CON_num/T) =")
sp.pprint(sp.simplify(r))
