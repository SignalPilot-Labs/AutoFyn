import sys
sys.path.insert(0,'/tmp/round-9')
from sim import analyze, rogue_pairs, P
found=[]
seeds = [1155,1365,1785,2145,2415,2805,3003,3315,3465,3689,3927,4199,4331,4757,4807,
         5005,5187,5313,5555,5865,6069,6205,6545,6825,7055,7315,7735,7999,8855,9345,
         9709,10465,11305,11951,12155,12673,13585,14231,14535,15015]
tested=0
for a1 in seeds:
    if a1 % 2 == 0: continue
    try:
        d = analyze(a1, 2000, min_hits=5)
    except Exception as e:
        continue
    tested+=1
    rp = rogue_pairs(d)
    for (Ap,Bp) in rp:
        nA=d['nmin'][Ap]; nB=d['nmin'][Bp]
        Fp = P(d['a'][nA]) - d['S0']; Fpp = P(d['a'][nB]) - d['S0']
        if len(Fp)>=2 or len(Fpp)>=2:
            found.append((a1,Ap,Bp,nA,nB,Fp,Fpp))
            print(a1, "A'=",Ap,"B'=",Bp,"nA=",nA,"nB=",nB,"F'=",Fp,"F''=",Fpp)
print("tested", tested, "found", len(found))
