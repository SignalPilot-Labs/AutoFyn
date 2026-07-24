import math

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

def base_type(x, Q):
    return frozenset(factor(x)) & Q

a1 = 175
N = 4000
seq = gen(a1, N)
Q = factor(a1)
print("Q=",Q)

from collections import defaultdict
occ = defaultdict(list)
for i,v in enumerate(seq, start=1):
    t = base_type(v, Q)
    occ[t].append(i)

# find persistent types (occurring often, say >=5 times) among base types (subsets of Q)
persistent = {t:idxs for t,idxs in occ.items() if len(idxs)>=5 and len(t)>0}
for t,idxs in persistent.items():
    print(t, len(idxs), idxs[:8])

A_idx = occ[frozenset({5})]
B_idx = occ[frozenset({7})]
print("m_A candidates:", A_idx[:5])
print("m_A' candidates:", A_idx[5:10])

mA = A_idx[0]
mA2 = A_idx[1]
aA = seq[mA-1]
aA2 = seq[mA2-1]
print("a_mA=",aA,"a_mA2=",aA2, "gcd(e)=", math.gcd(aA,aA2))

from collections import Counter
d1_counts = Counter()
for x in B_idx:
    ax = seq[x-1]
    d1_counts[math.gcd(aA, ax)] += 1
print("d1 distribution (gcd(a_mA, a_x) for x in B_idx):", d1_counts)

d2_counts = Counter()
for x in B_idx:
    ax = seq[x-1]
    d2_counts[math.gcd(aA2, ax)] += 1
print("d2 distribution (gcd(a_mA2, a_x) for x in B_idx):", d2_counts)

# nested pigeonhole: fix d1=3 (most common), restrict, then compute d2 distribution
XB1 = [x for x in B_idx if math.gcd(aA, seq[x-1])==3]
print("len XB1 (d1=3):", len(XB1))
d2_nested = Counter()
for x in XB1:
    ax = seq[x-1]
    d2_nested[math.gcd(aA2, ax)] += 1
print("d2 distribution within XB1:", d2_nested)
print("gcd(d1=3, each d2):", [(v,math.gcd(3,v)) for v in d2_nested])

print("\n--- testing multiple witness pairs (mA,mA') to see if common prime is stable ---")
import itertools
for mA_i, mA2_i in itertools.combinations(A_idx[:8], 2):
    aA_ = seq[mA_i-1]
    aA2_ = seq[mA2_i-1]
    # nested pigeonhole via most common d1
    d1c = Counter(math.gcd(aA_, seq[x-1]) for x in B_idx)
    top_d1 = d1c.most_common(1)[0][0]
    XB1_ = [x for x in B_idx if math.gcd(aA_, seq[x-1])==top_d1]
    d2c = Counter(math.gcd(aA2_, seq[x-1]) for x in XB1_)
    top_d2 = d2c.most_common(1)[0][0]
    g = math.gcd(top_d1, top_d2)
    common_prime = factor(g) if g>1 else set()
    print(f"mA={mA_i},mA2={mA2_i}: top_d1={top_d1}, top_d2={top_d2}, gcd={g}, primes={common_prime}")
