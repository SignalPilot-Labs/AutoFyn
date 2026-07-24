import sympy
from sympy import factorint
from collections import defaultdict, Counter

def gen_seq(a1, N):
    a = [None, a1]
    while len(a) <= N:
        an = a[-1]
        c = an + 1
        while True:
            ok = True
            for i in range(1, len(a)):
                if sympy.gcd(c, a[i]) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a  # a[1..N]

def primeset(x):
    return set(factorint(x).keys())

def analyze(a1, N=4000, tailfrac=0.5):
    a = gen_seq(a1, N)
    Q = primeset(a1)
    tau = [None]*(N+1)
    for n in range(1, N+1):
        tau[n] = frozenset(primeset(a[n]) & Q)
    # persistent base types: occur infinitely often -> approximate by occurring in tail half
    tailstart = int(N*tailfrac)
    tailtypes = set(tau[n] for n in range(tailstart, N+1))
    persistent = tailtypes
    # earliest witness for each persistent base type
    witness = {}
    for n in range(1, N+1):
        if tau[n] in persistent and tau[n] not in witness:
            witness[tau[n]] = n
    # S: extra primes from witnesses
    S = set()
    for t, m in witness.items():
        S |= (primeset(a[m]) - Q)
    S0 = Q | S
    rho = [None]*(N+1)
    for n in range(1, N+1):
        rho[n] = frozenset(primeset(a[n]) & S0)
    tailrhotypes = set(rho[n] for n in range(tailstart, N+1))
    ext_persistent = tailrhotypes
    ext_witness = {}
    for n in range(1, N+1):
        if rho[n] in ext_persistent and rho[n] not in ext_witness:
            ext_witness[rho[n]] = n
    return dict(a=a, Q=Q, tau=tau, persistent=persistent, S0=S0, rho=rho,
                ext_persistent=ext_persistent, ext_witness=ext_witness, N=N)

def find_rogue_pairs(res):
    ext_persistent = res['ext_persistent']
    ew = res['ext_witness']
    pairs = []
    lst = list(ext_persistent)
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j: continue
            A,B = lst[i], lst[j]
            baseA = A & res['Q']
            baseB = B & res['Q']
            if baseA != baseB and (baseA & baseB)==frozenset() and (A & B)==frozenset():
                pairs.append((A,B))
    return pairs

if __name__ == "__main__":
    import sys
    a1 = int(sys.argv[1]) if len(sys.argv)>1 else 209
    N = int(sys.argv[2]) if len(sys.argv)>2 else 3000
    res = analyze(a1, N)
    print("a1=",a1,"Q=",res['Q'])
    print("S0=",res['S0'])
    print("ext_persistent types:", res['ext_persistent'])
    pairs = find_rogue_pairs(res)
    print("num rogue pairs:", len(pairs))
    for p in pairs[:5]:
        print(p)

def walk_analysis(res, A, B):
    a = res['a']; N = res['N']; S0 = res['S0']; rho = res['rho']
    ew = res['ext_witness']
    nA = ew[A]; nB = ew[B]
    if nA > nB:
        # swap so B is later witness per lemma convention (n_B is later)
        A,B = B,A
        nA, nB = nB, nA
    Fpp = primeset(a[nB]) - S0   # F''
    Fp = primeset(a[nA]) - S0    # F'
    common = Fp & Fpp
    qstar = min(common) if common else None
    # b = F''-part of a[nB]
    fac = factorint(a[nB])
    b = 1
    for p,e in fac.items():
        if p in Fpp:
            b *= p**e
    occ = [n for n in range(nB+1, N+1) if rho[n]==A]
    gs = []
    for n in occ:
        g = sympy.gcd(a[n], a[nB])
        gs.append(int(g))
    return dict(nA=nA, nB=nB, Fp=Fp, Fpp=Fpp, qstar=qstar, b=b, occ=occ, gs=gs)

if __name__ == "__main__" and len(__import__('sys').argv)>3:
    pass
