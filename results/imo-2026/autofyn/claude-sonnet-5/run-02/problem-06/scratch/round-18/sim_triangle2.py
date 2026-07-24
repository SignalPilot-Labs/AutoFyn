import math
from collections import defaultdict, Counter
import itertools

def gen(a1, n_max):
    a = [a1]
    for n in range(1, n_max):
        c = a[-1] + 1
        while True:
            ok = True
            for prev in a:
                if math.gcd(c, prev) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a

def factor(x):
    fs = set()
    d = 2
    y = x
    while d*d <= y:
        if y % d == 0:
            fs.add(d)
            while y % d == 0:
                y //= d
        d += 1
    if y > 1:
        fs.add(y)
    return fs

a1 = 4807
N = 3000
seq = gen(a1, N)
Q = factor(a1)
print("Q=",Q, "a1=",a1)

occ_full = defaultdict(list)  # full factorization-based extended "signature" restricted to Q ∪ small set? 
# We'll track full factor set (not just Q-part) to find extended persistent types (base type + collateral)
for i,v in enumerate(seq, start=1):
    fs = factor(v)
    occ_full[frozenset(fs)].append(i)

persistent = {t:idxs for t,idxs in occ_full.items() if len(idxs)>=5}
print("num persistent extended types (>=5 occ):", len(persistent))
for t,idxs in sorted(persistent.items(), key=lambda kv: -len(kv[1]))[:15]:
    print(t, len(idxs), idxs[:6])

def base_type(fs, Q):
    return frozenset(fs) & Q

occ_base = defaultdict(list)
vals = {}
for i,v in enumerate(seq, start=1):
    fs = factor(v)
    vals[i] = v
    bt = base_type(fs, Q)
    occ_base[bt].append(i)

A_idx = occ_base[frozenset({11})]
B_idx = occ_base[frozenset({19})]
print("len A (base {11}):", len(A_idx), A_idx[:10])
print("len B (base {19}):", len(B_idx), B_idx[:10])

print("\n--- witness pairs test ---")
for mA_i, mA2_i in itertools.combinations(A_idx[:6], 2):
    aA_ = vals[mA_i]
    aA2_ = vals[mA2_i]
    d1c = Counter(math.gcd(aA_, vals[x]) for x in B_idx)
    top_d1 = d1c.most_common(1)[0][0]
    XB1_ = [x for x in B_idx if math.gcd(aA_, vals[x])==top_d1]
    d2c = Counter(math.gcd(aA2_, vals[x]) for x in XB1_)
    top_d2 = d2c.most_common(1)[0][0]
    g = math.gcd(top_d1, top_d2)
    print(f"mA={mA_i},mA2={mA2_i}: top_d1={top_d1}(freq {d1c.most_common(1)[0][1]}/{len(B_idx)}), top_d2={top_d2}(freq {d2c.most_common(1)[0][1]}/{len(XB1_)}), gcd={g}")
