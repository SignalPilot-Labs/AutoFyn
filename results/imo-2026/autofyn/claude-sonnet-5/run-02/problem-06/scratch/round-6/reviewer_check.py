import sys
from math import gcd
from sympy import primefactors
from collections import defaultdict

def gen(a1, N):
    a = [None, a1]
    while len(a) <= N:
        prev = a[-1]
        c = prev + 1
        while True:
            ok = True
            for x in a[1:]:
                if gcd(c, x) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a

def P(x):
    return set(primefactors(x))

def analyze(a1, N=2500, tail_frac=0.5, min_hits=8):
    a = gen(a1, N)
    Q = P(a1)
    tau = {}
    for n in range(1, N+1):
        tau[n] = P(a[n]) & Q
    # persistent base types via tail window
    tail_start = int(N*tail_frac)
    counts = defaultdict(int)
    for n in range(tail_start, N+1):
        counts[frozenset(tau[n])] += 1
    persistent_base = set(t for t,c in counts.items() if c >= min_hits)
    # canonical witness = earliest occurrence over whole range
    m = {}
    for t in persistent_base:
        for n in range(1, N+1):
            if frozenset(tau[n]) == t:
                m[t] = n
                break
    S = set()
    for t in persistent_base:
        S |= (P(a[m[t]]) - Q)
    S0 = Q | S
    rho = {}
    for n in range(1, N+1):
        rho[n] = P(a[n]) & S0
    counts2 = defaultdict(int)
    for n in range(tail_start, N+1):
        counts2[frozenset(rho[n])] += 1
    persistent_ext = set(t for t,c in counts2.items() if c >= min_hits)
    nmin = {}
    for t in persistent_ext:
        for n in range(1, N+1):
            if frozenset(rho[n]) == t:
                nmin[t] = n
                break
    return a, Q, tau, persistent_base, m, S, S0, rho, persistent_ext, nmin

def rogue_pairs(persistent_ext, nmin):
    pairs = []
    lst = list(persistent_ext)
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j: continue
            Ap, Bp = lst[i], lst[j]
            Abase = Ap & Q_glob
            Bbase = Bp & Q_glob
            if Abase and Bbase and (Abase & Bbase == set()) and (Ap & Bp == set()):
                pairs.append((Ap,Bp))
    return pairs

for a1 in [187, 209, 4807, 385]:
    print("="*60)
    print("a1 =", a1)
    a, Q, tau, persistent_base, m, S, S0, rho, persistent_ext, nmin = analyze(a1, N=3000)
    Q_glob = Q
    print("Q =", Q, "S =", S, "S0=", S0)
    print("persistent_ext count:", len(persistent_ext))
    # find rogue pairs (disjoint base types, A' cap B' = empty)
    lst = list(persistent_ext)
    found = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j: continue
            Ap, Bp = lst[i], lst[j]
            Abase = Ap & Q
            Bbase = Bp & Q
            if Abase and Bbase and Abase.isdisjoint(Bbase) and Ap.isdisjoint(Bp):
                found.append((frozenset(Ap), frozenset(Bp)))
    # dedupe unordered but keep track since (A,B) direction matters (n_A<n_B convention)
    print("num rogue extended-type ordered pairs found:", len(found))
    checked = set()
    for (Ap,Bp) in found:
        key = frozenset([Ap,Bp])
        if key in checked: continue
        checked.add(key)
        nA, nB = nmin[Ap], nmin[Bp]
        if nA > nB:
            Ap,Bp = Bp,Ap
            nA,nB = nB,nA
        # find Lemma G shared prime q outside S0 dividing both a[nA], a[nB]
        common = (P(a[nA]) - S0) & (P(a[nB]) - S0)
        if not common:
            print("  NO shared outside prime found for pair (bug?)", Ap, Bp)
            continue
        q = sorted(common)[0]
        Fprime = P(a[nB]) - S0
        # check FAH: q | a_n for every n>nB with rho(n)=Ap
        failA = 0; totA=0
        for n in range(nB+1, len(a)):
            if (P(a[n]) & S0) == Ap:
                totA += 1
                if q not in P(a[n]):
                    failA += 1
        # check symmetric FAH: q|a_n for every n>nA with rho(n)=Bp
        failB=0; totB=0
        for n in range(nA+1, len(a)):
            if (P(a[n]) & S0) == Bp:
                totB += 1
                if q not in P(a[n]):
                    failB += 1
        print(f"  pair A'={set(Ap)} B'={set(Bp)}  nA={nA} nB={nB} F'={Fprime} q={q}")
        print(f"    FAH (A'-side after nB): fails {failA}/{totA}")
        print(f"    Symmetric FAH (B'-side after nA): fails {failB}/{totB}")
