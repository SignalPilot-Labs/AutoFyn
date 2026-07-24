import sys
sys.path.insert(0,'/tmp/round-9')
from sim import gen, P

a1 = 11305
N = 6000
a = gen(a1, N)
Q = P(a1)
S0 = {2,3,5,7,11,103}  # from prior recruitment: need to recompute properly
# recompute recruited core properly using analyze()
from sim import analyze, rogue_pairs
d = analyze(a1, N, min_hits=8)
print("Q", d['Q'], "S", d['S'], "S0", d['S0'])
rp = rogue_pairs(d)
for (Ap,Bp) in rp:
    nA=d['nmin'][Ap]; nB=d['nmin'][Bp]
    Fp = P(d['a'][nA]) - d['S0']; Fpp = P(d['a'][nB]) - d['S0']
    print("pair", Ap, Bp, "nA",nA,"nB",nB,"F'",Fp,"F''",Fpp)

S0 = d['S0']
Ap = frozenset({3,7})
Bp = frozenset({2,5})
nA = d['nmin'][Ap]
nB = d['nmin'][Bp]
print("nA",nA,"a_nA",d['a'][nA])
print("nB",nB,"a_nB",d['a'][nB])
rho = d['rho']
# occurrences of A'-type after nB
occA = [n for n in range(nB+1, N+1) if rho[n]==Ap]
print("num A'-type occurrences after nB:", len(occA))
div11 = [n for n in occA if d['a'][n] % 11 == 0]
div103 = [n for n in occA if d['a'][n] % 103 == 0]
divboth = [n for n in occA if n in div11 and n in div103]
neither = [n for n in occA if n not in div11 and n not in div103]
print("div by 11:", len(div11), "div by 103:", len(div103), "both:", len(divboth), "neither:", len(neither))
print("first 20 occA with div11/103 flags:")
for n in occA[:30]:
    print(n, d['a'][n], "11|" if d['a'][n]%11==0 else "  ", "103|" if d['a'][n]%103==0 else "")
# check tail behavior - last 30
print("last 30:")
for n in occA[-30:]:
    print(n, d['a'][n], "11|" if d['a'][n]%11==0 else "  ", "103|" if d['a'][n]%103==0 else "")
