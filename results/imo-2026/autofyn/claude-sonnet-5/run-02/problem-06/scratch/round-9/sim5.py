import sys
sys.path.insert(0,'/tmp/round-9')
from sim import analyze, rogue_pairs, P
seeds = [7315,9345,13585,14535,15015,17017,19019,21021,23023,25025,27027,29029,31031,33033,35035,10465,12155,16445,20995]
for a1 in seeds:
    if a1 % 2 == 0: continue
    try:
        d = analyze(a1, 2200, min_hits=5)
    except Exception as e:
        continue
    rp = rogue_pairs(d)
    for (Ap,Bp) in rp:
        nA=d['nmin'][Ap]; nB=d['nmin'][Bp]
        Fp = P(d['a'][nA]) - d['S0']; Fpp = P(d['a'][nB]) - d['S0']
        if len(Fp)>=2 or len(Fpp)>=2:
            print(a1, "A'=",Ap,"B'=",Bp,"nA=",nA,"nB=",nB,"F'=",Fp,"F''=",Fpp)
