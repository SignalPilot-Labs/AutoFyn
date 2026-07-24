import sympy
from math import gcd
from collections import Counter, defaultdict

def build_sequence(a1, N):
    a = [a1]
    while len(a) < N:
        an = a[-1]
        cand = an + 1
        while True:
            if all(gcd(cand, x) > 1 for x in a):
                a.append(cand)
                break
            cand += 1
    return a

def primes_of(x):
    return frozenset(sympy.factorint(x).keys())

def persistent_types(vals, tail_frac=0.5, min_count=3):
    n = len(vals)
    cnt = Counter(vals)
    tail = Counter(vals[int(n*tail_frac):])
    return set(t for t,c in cnt.items() if tail.get(t,0) >= min_count)

def analyze(a1, N=6000, verbose=True):
    a = build_sequence(a1, N)
    Q = primes_of(a1)
    tau = [primes_of(x) & Q for x in a]  # 1-indexed via a[i-1]
    P_base = persistent_types(tau)
    # N0: last index (1-indexed) with tau not persistent
    N0 = 0
    for i,t in enumerate(tau, start=1):
        if t not in P_base:
            N0 = i
    # witnesses m_B for each persistent base type
    mB = {}
    for B in P_base:
        for i in range(N0, N):  # i is 0-indexed position -> n=i+1
            n = i+1
            if n <= N0: continue
            if tau[i] == B:
                mB[B] = n
                break
    S = set()
    for B, m in mB.items():
        S |= (primes_of(a[m-1]) - Q)
    S0 = Q | S
    rho = [primes_of(x) & S0 for x in a]
    Pext = persistent_types(rho, min_count=3)
    # rogue pairs: disjoint extended-persistent types, different base types
    rogue_pairs = []
    Pext_list = sorted(Pext, key=lambda s: sorted(s))
    for i in range(len(Pext_list)):
        for j in range(i+1, len(Pext_list)):
            A, B = Pext_list[i], Pext_list[j]
            if A & B:
                continue
            baseA, baseB = A & Q, B & Q
            if baseA == baseB:
                continue
            rogue_pairs.append((A,B))
    results = []
    for A,B in rogue_pairs:
        nA = next(n for n in range(1,N+1) if rho[n-1]==A)
        nB = next(n for n in range(1,N+1) if rho[n-1]==B)
        if nA > nB:
            nA, nB = nB, nA
            A, B = B, A
        commonprimes = (primes_of(a[nA-1]) & primes_of(a[nB-1])) - S0
        if not commonprimes:
            continue
        q = sorted(commonprimes)[0]
        # test FAH: for n>nB with rho(n)=A, does q | a_n?
        occs = [n for n in range(nB+1, N+1) if rho[n-1]==A]
        fails = [n for n in occs if a[n-1] % q != 0]
        results.append(dict(A=A,B=B,nA=nA,nB=nB,q=q,ncand=commonprimes,
                             n_occ=len(occs), n_fail=len(fails), fails=fails[:10],
                             aA=a[nA-1], aB=a[nB-1]))
    return dict(a=a, Q=Q, S0=S0, P_base=P_base, Pext=Pext, N0=N0, mB=mB, rogue=results)

if __name__ == "__main__":
    for a1 in [4807, 11305, 209, 247, 175]:
        res = analyze(a1, N=6000)
        print("="*70)
        print("a1=",a1,"Q=",sorted(res['Q']),"S0=",sorted(res['S0']))
        print("num rogue pairs:", len(res['rogue']))
        for r in res['rogue']:
            print(f"  A={sorted(r['A'])} B={sorted(r['B'])} nA={r['nA']} nB={r['nB']} q={r['q']} cand={sorted(r['ncand'])} occ={r['n_occ']} fails={r['n_fail']} failidx={r['fails']}")
