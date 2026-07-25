import math, random
from fractions import Fraction

def altsum(vals):
    vals = sorted(vals, reverse=True)
    s = 0.0
    for i,v in enumerate(vals):
        s += v if i%2==0 else -v
    return s

def w(v, s):
    if v <= 0: return 0.0
    return v * (2.0 ** (-abs(math.log2(v) - s)))

def total_charge(vals, s_of_rank):
    vals = sorted(vals, reverse=True)
    return sum(w(v, s_of_rank(i+1)) for i,v in enumerate(vals))

# candidate s(rank) definitions to test
def s_neg_rank(i): return -i
def s_pos_rank(i): return i
def s_neg_rank_shift(i): return -(i-1)

candidates = {
    's=-i': s_neg_rank,
    's=i': s_pos_rank,
    's=-(i-1)': s_neg_rank_shift,
}

random.seed(1)

def test_split_invariance(vals, split_idx, frac, s_of_rank, label):
    vals = sorted(vals, reverse=True)
    before = total_charge(vals, s_of_rank)
    v = vals[split_idx]
    v1 = v*frac
    v2 = v-v1
    newvals = vals[:split_idx] + vals[split_idx+1:] + [v1, v2]
    after = total_charge(newvals, s_of_rank)
    print(f"{label}: before={before:.6f} after={after:.6f} delta={after-before:.6f}  vals={vals} -> split idx{split_idx} frac{frac}")

print("=== Test 1: geometric partition n=3, p=(8,4,2,1)/15, split top piece ===")
base = [8.0,4.0,2.0,1.0]
for name, sf in candidates.items():
    test_split_invariance(base, 0, 0.6, sf, name)
    test_split_invariance(base, 0, 0.5, sf, name)

print()
print("=== Test 2: geometric partition, split a MIDDLE piece ===")
for name, sf in candidates.items():
    test_split_invariance(base, 2, 0.5, sf, name)

print()
print("=== Test 3: random multisets, random split, many trials -> report max |delta| ===")
for name, sf in candidates.items():
    maxdelta = 0
    for trial in range(3000):
        n = random.randint(2,6)
        vals = [random.uniform(0.05, 5.0) for _ in range(n)]
        idx = random.randrange(n)
        frac = random.uniform(0.05,0.95)
        vals_sorted = sorted(vals, reverse=True)
        before = total_charge(vals_sorted, sf)
        v = vals_sorted[idx]
        v1=v*frac; v2=v-v1
        newvals = vals_sorted[:idx]+vals_sorted[idx+1:]+[v1,v2]
        after = total_charge(newvals, sf)
        d = abs(after-before)
        if d > maxdelta:
            maxdelta = d
            worst = (vals_sorted, idx, frac, before, after)
    print(f"{name}: max|delta| over 3000 random single-cut trials = {maxdelta:.6f}")
    print(f"   worst case: {worst}")
