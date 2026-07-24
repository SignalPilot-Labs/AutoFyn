import sys
sys.path.insert(0,'.')
from search_rogue import analyze, rogue_pairs, P, factorize

d = analyze(11305, 8000)
print("Q=",d['Q'],"S=",d['S'],"S0=",d['S0'])
rp = rogue_pairs(d)
print("num rogue pairs:", len(rp))
for (Ap,Bp) in rp:
    nA=d['nmin'][Ap]; nB=d['nmin'][Bp]
    Fp = P(d['a'][nA]) - d['S0']
    Fpp = P(d['a'][nB]) - d['S0']
    inter = Fp & Fpp
    qstar = min(inter) if inter else None
    occ = [n for n in range(max(nA,nB)+1, 8001) if d['rho'][n]==Ap]
    fails = [n for n in occ if qstar is not None and qstar not in P(d['a'][n])]
    print("A'=",Ap,"B'=",Bp,"nA=",nA,"nB=",nB,"F'=",Fp,"F''=",Fpp,"q*=",qstar,
          "occ=",len(occ),"fails=",len(fails))
