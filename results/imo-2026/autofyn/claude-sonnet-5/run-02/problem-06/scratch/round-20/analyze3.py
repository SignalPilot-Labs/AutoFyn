import pickle, math
from sympy import factorint

def is_prime_power(d):
    if d<=1: return None
    f = factorint(d)
    return len(f)==1

for label in ["4807","11305"]:
    with open(f"/tmp/round-20/data_{label}.pkl","rb") as f:
        D = pickle.load(f)
    a = D["a"]; XA=D["XA"]; XB=D["XB"]; S0=D["S0"]; outside=D["outside"]
    print(f"=== seed {label}: B witnesses, classes over XA ===")
    count_nonpp = 0
    count_total = 0
    examples_composite = []
    for m_B in XB:
        val_mB = a[m_B-1]
        classes = {}
        for x in XA:
            if x==m_B: continue
            g = math.gcd(val_mB, a[x-1])
            classes.setdefault(g, []).append(x)
        sizes = sorted(classes.items(), key=lambda kv: -len(kv[1]))
        d_star, xs = sizes[0]
        pp = is_prime_power(d_star)
        count_total += 1
        if not pp:
            count_nonpp += 1
            examples_composite.append((m_B, outside[m_B], d_star, factorint(d_star), len(xs), len(XA)))
    print(f"Non-prime-power dominant class count: {count_nonpp}/{count_total}")
    for e in examples_composite[:10]:
        print("  composite example:", e)

    # also check |F'| (outside-core) sizes for witnesses
    print("Distribution of |outside(m_B)| over XB:")
    from collections import Counter
    c = Counter(len(outside[m]) for m in XB)
    print(dict(c))
    print("Distribution of |outside(m_A)| over XA:")
    c2 = Counter(len(outside[m]) for m in XA)
    print(dict(c2))
