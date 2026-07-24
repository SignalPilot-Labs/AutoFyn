import pickle, math
from sympy import factorint

def is_prime_power(d):
    if d<=1: return None
    f = factorint(d)
    return len(f)==1

for label in ["4807","11305"]:
    with open(f"/tmp/round-20/data_{label}.pkl","rb") as f:
        D = pickle.load(f)
    a = D["a"]; XA=D["XA"]; XB=D["XB"]; S0=D["S0"]
    print(f"=== seed {label} ===")
    # forward direction: witness m_A in XA, classes over XB
    for m_A in XA:
        val_mA = a[m_A-1]
        classes = {}
        for x in XB:
            if x==m_A: continue
            g = math.gcd(val_mA, a[x-1])
            classes.setdefault(g, []).append(x)
        # sort by size desc
        sizes = sorted(classes.items(), key=lambda kv: -len(kv[1]))
        top = sizes[0]
        d_star, xs = top
        pp = is_prime_power(d_star)
        print(f" m_A={m_A} |classes|={len(classes)} dominant d*={d_star} count={len(xs)}/{len(XB)} prime_power={pp} factorization={factorint(d_star)}")
