from search_rogue import analyze, rogue_pairs, P, factorize
import random
random.seed(42)
candidates = []
for a1 in range(1000, 20000):
    Qf = factorize(a1)
    if len(Qf) >= 3:
        candidates.append(a1)
random.shuffle(candidates)
candidates = candidates[:120]

results = []
tested = 0
for a1 in candidates:
    tested += 1
    try:
        d = analyze(a1, 4000)
    except Exception:
        continue
    rp = rogue_pairs(d)
    for (Ap, Bp) in rp:
        nA = d['nmin'][Ap]; nB = d['nmin'][Bp]
        Fp = P(d['a'][nA]) - d['S0']
        Fpp = P(d['a'][nB]) - d['S0']
        if len(Fp) >= 2 or len(Fpp) >= 2:
            inter = Fp & Fpp
            qstar = min(inter) if inter else None
            if qstar is None:
                continue
            occ = [n for n in range(max(nA,nB)+1, 4001) if d['rho'][n] == Ap]
            fails = [n for n in occ if qstar not in P(d['a'][n])]
            results.append((a1, Ap, Bp, nA, nB, Fp, Fpp, qstar, len(occ), len(fails), fails[:20]))
print("tested:", tested, "instances found:", len(results))
for r in results:
    a1, Ap, Bp, nA, nB, Fp, Fpp, qstar, nocc, nfail, failidx = r
    print("a1=",a1,"A'=",Ap,"B'=",Bp,"F'=",Fp,"F''=",Fpp,"q*=",qstar,"occ=",nocc,"fails=",nfail,failidx)
