from analyze import analyze
import sympy

for a1 in [4807, 209, 247]:
    res = analyze(a1, N=8000)
    print("="*70, "a1=", a1)
    for r in res['rogue'][:2]:
        A=r['A']; nB=r['nB']
        occs = [n for n in range(1,8000+1) if (res['a'][n-1],) and (sympy.factorint(res['a'][n-1]).keys() )]
    # recompute occurrences of A' type directly using rho
    a=res['a']; S0=res['S0']
    rho = [ (sympy_primes:=frozenset(sympy.factorint(x).keys())) & S0 for x in a]
    for r in res['rogue'][:3]:
        A = r['A']
        occs = [n for n in range(1,len(a)+1) if rho[n-1]==A]
        gaps = [occs[i+1]-occs[i] for i in range(len(occs)-1)]
        vals = [a[n-1] for n in occs]
        avals = [vals[i+1]-vals[i] for i in range(len(vals)-1)]
        print(f" A={sorted(A)} q={r['q']} occ_count={len(occs)}")
        print("   idx gaps:", gaps[-15:])
        print("   val gaps:", avals[-15:])
