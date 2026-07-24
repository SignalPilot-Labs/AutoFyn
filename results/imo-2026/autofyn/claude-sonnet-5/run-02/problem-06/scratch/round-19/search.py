from sim2 import simulate, factorize
import collections

def analyze(seq, S0):
    types = collections.defaultdict(list)
    outsig = {}
    for i,a in enumerate(seq):
        n=i+1
        f = factorize(a)
        rho = frozenset(f & S0)
        out = frozenset(f - S0)
        types[rho].append(n)
        outsig[n] = out
    return types, outsig

def recruit_core(a1, seq, N, min_occ=15, max_rounds=6):
    Q = factorize(a1)
    S = set(Q)
    for rd in range(max_rounds):
        types, outsig = analyze(seq, S)
        persistent = {t:v for t,v in types.items() if len(v)>=min_occ}
        newS = set(S)
        for t, occs in persistent.items():
            first = occs[0]
            f = factorize(seq[first-1])
            newS |= f
        if newS == S:
            break
        S = newS
    types, outsig = analyze(seq, S)
    persistent = {t:v for t,v in types.items() if len(v)>=min_occ}
    return S, persistent, outsig

def find_rogue_pairs(a1, N=8000, min_occ=15):
    seq = simulate(a1, N)
    S, persistent, outsig = recruit_core(a1, seq, N, min_occ=min_occ)
    Q = factorize(a1)
    results = []
    types = list(persistent.items())
    for i in range(len(types)):
        for j in range(i+1, len(types)):
            A, occA = types[i]
            B, occB = types[j]
            if (A & Q) and (B & Q) and (A & Q) != (B & Q) and not ((A&Q) & (B&Q)):
                # disjoint base types
                Fp = set()
                for n in occA[:1]:
                    Fp |= outsig[n]
                Fpp = set()
                for n in occB[:1]:
                    Fpp |= outsig[n]
                results.append((A,B,len(occA),len(occB), Fp, Fpp))
    return S, results, outsig, persistent

if __name__=="__main__":
    import sys
    a1 = int(sys.argv[1])
    N = int(sys.argv[2]) if len(sys.argv)>2 else 8000
    S, results, outsig, persistent = find_rogue_pairs(a1, N)
    print("a1=",a1,"core S=",sorted(S), "num persistent types", len(persistent))
    for A,B,cA,cB,Fp,Fpp in results:
        print(f"  A={sorted(A)}(n={cA}) B={sorted(B)}(n={cB}) F'(canon)={Fp} F''(canon)={Fpp}")
