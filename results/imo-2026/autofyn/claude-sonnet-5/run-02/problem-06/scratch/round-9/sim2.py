import sys
sys.path.insert(0,'/tmp/round-9')
from sim import analyze, rogue_pairs, P
found=[]
seeds = list(range(1001,1400,2)) + list(range(2001,2200,2)) + [4807, 11305, 6545, 7735, 8855, 10465, 13585, 5005, 5005*2-1]
tested=0
for a1 in seeds:
    if a1 % 2 ==0: continue
    try:
        d = analyze(a1, 3500, min_hits=6)
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
