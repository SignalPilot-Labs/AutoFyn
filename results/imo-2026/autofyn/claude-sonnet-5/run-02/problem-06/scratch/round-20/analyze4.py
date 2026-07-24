import pickle, math
from sympy import factorint

for label in ["4807","11305"]:
    with open(f"/tmp/round-20/data_{label}.pkl","rb") as f:
        D = pickle.load(f)
    a = D["a"]; XA=D["XA"]; XB=D["XB"]; S0=D["S0"]; outside=D["outside"]
    print(f"=== seed {label} ===")
    # pick a few m_B with |outside|=2
    cands = [m for m in XB if len(outside[m])==2][:5]
    for m_B in cands:
        val_mB = a[m_B-1]
        classes = {}
        for x in XA:
            if x==m_B: continue
            g = math.gcd(val_mB, a[x-1])
            classes.setdefault(g, []).append(x)
        sizes = sorted(classes.items(), key=lambda kv: -len(kv[1]))
        print(f" m_B={m_B} outside={outside[m_B]} classes(sorted by count)={[(d,len(xs)) for d,xs in sizes]}")
