from sim2 import simulate, factorize
import collections, sys

def check(a1, N, S0, min_occ=100):
    seq = simulate(a1, N)
    Q = factorize(a1)
    types = collections.defaultdict(list)
    outsig = {}
    for i,a in enumerate(seq):
        n=i+1
        f = factorize(a)
        rho = frozenset(f & S0)
        out = frozenset(f - S0)
        types[rho].append(n)
        outsig[n] = out
    persistent = {t:v for t,v in types.items() if len(v)>=min_occ and (t & Q)}
    keys = list(persistent.keys())
    report=[]
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            A,B = keys[i], keys[j]
            if (A&Q) & (B&Q): continue
            occA, occB = persistent[A], persistent[B]
            sigsA=[outsig[n] for n in occA]; sigsB=[outsig[n] for n in occB]
            maxA=max(len(s) for s in sigsA); maxB=max(len(s) for s in sigsB)
            singA=collections.Counter(next(iter(s)) for s in sigsA if len(s)==1)
            singB=collections.Counter(next(iter(s)) for s in sigsB if len(s)==1)
            match=set(singA)&set(singB)
            report.append((A,B,len(occA),len(occB),maxA,maxB,len(singA),len(singB),sum(singA.values()),sum(singB.values()),match))
    return Q, persistent, report

if __name__=="__main__":
    a1=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 15000
    Q = factorize(a1)
    S0 = set(Q) | {2,3,5,7,11,13}
    Q, persistent, report = check(a1,N,S0)
    print("a1=",a1,"Q=",sorted(Q),"S0=",sorted(S0),"n_persistent=",len(persistent))
    for A,B,cA,cB,maxA,maxB,nsA,nsB,tsA,tsB,match in report:
        if maxA>=2 and maxB>=2:
            flag = "MATCH!" if match else "no-match"
            print(f"  A={sorted(A)}(n={cA},maxOut={maxA},distinctSing={nsA},totSing={tsA}) B={sorted(B)}(n={cB},maxOut={maxB},distinctSing={nsB},totSing={tsB}) {flag} sharedprimes={match}")
