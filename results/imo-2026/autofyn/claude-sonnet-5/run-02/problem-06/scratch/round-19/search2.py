from sim2 import simulate, factorize
import collections, sys

def analyze_at_Q(a1, N):
    seq = simulate(a1, N)
    Q = factorize(a1)
    types = collections.defaultdict(list)
    outsig = {}
    for i,a in enumerate(seq):
        n=i+1
        f = factorize(a)
        rho = frozenset(f & Q)
        out = frozenset(f - Q)
        types[rho].append(n)
        outsig[n] = out
    return Q, types, outsig

def check(a1, N=10000, min_occ=15):
    Q, types, outsig = analyze_at_Q(a1, N)
    persistent = {t:v for t,v in types.items() if len(v)>=min_occ and len(t)>0}
    report = []
    keys = list(persistent.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            A, B = keys[i], keys[j]
            if A & B: continue
            occA, occB = persistent[A], persistent[B]
            sigsA = [outsig[n] for n in occA]
            sigsB = [outsig[n] for n in occB]
            maxA = max(len(s) for s in sigsA)
            maxB = max(len(s) for s in sigsB)
            singA = collections.Counter(next(iter(s)) for s in sigsA if len(s)==1)
            singB = collections.Counter(next(iter(s)) for s in sigsB if len(s)==1)
            match = set(singA) & set(singB)
            report.append((A,B,len(occA),len(occB), maxA, maxB, dict(singA), dict(singB), match))
    return Q, report

if __name__=="__main__":
    a1 = int(sys.argv[1])
    N = int(sys.argv[2]) if len(sys.argv)>2 else 10000
    Q, report = check(a1, N)
    print("a1=",a1,"Q=",sorted(Q))
    for A,B,cA,cB,maxA,maxB,singA,singB,match in report:
        if maxA>=2 and maxB>=2:  # nontrivial, out-of-Q sets can be size>=2
            print(f"  A={sorted(A)}(n={cA},maxOutSig={maxA}) B={sorted(B)}(n={cB},maxOutSig={maxB}) singA={singA} singB={singB} MATCH={match}")
