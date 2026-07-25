from fractions import Fraction as F
import random, itertools

def oddsum(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def c(n):
    return F(2**n, 2**(n+1)-1)

# n=6 survivor point (approx, from global-lp-vertex-sufficiency.md)
p_float = [0.3306,0.2791,0.1501,0.1162,0.0904,0.0208,0.0128]
assert abs(sum(p_float)-1) < 1e-9
n = 6
gamma = 1/(2**(n+1)-1)
gaps = [p_float[i]-p_float[i+1] for i in range(len(p_float)-1)]
print("n=",n,"gaps=",gaps,"gamma=",gamma, "c(n)=",float(c(n)))

k_pieces = len(p_float)  # =7 = n+1

def anchor_merge_value(p, pairs):
    # p sorted descending, pairs = list of (i,j) i<j indices into p (0-indexed), i,j not reused
    used = set()
    ells = []
    for (i,j) in pairs:
        used.add(i); used.add(j)
        ells.append(p[i]-p[j])
    rest = 1 - sum(p[i] for i in used)  # not needed directly
    B_sum = 1 - sum(ells)  # from formula: sum(B) = 1 - sum(ell_m)
    return 0.5*(1-sum(ells)) + oddsum(ells)

def random_matching(indices, k):
    idx = list(indices)
    random.shuffle(idx)
    chosen = idx[:2*k]
    pairs = []
    for t in range(0,2*k,2):
        a,b = chosen[t], chosen[t+1]
        i,j = (a,b) if p_float[a]>=p_float[b] else (b,a)
        pairs.append((i,j))
    return pairs

random.seed(0)
for k in range(1, k_pieces//2+1):
    trials = 3000
    vals = []
    for _ in range(trials):
        pairs = random_matching(range(k_pieces), k)
        v = anchor_merge_value(p_float, pairs)
        vals.append(v)
    avg = sum(vals)/len(vals)
    mn = min(vals)
    print(f"k={k}: E[OddSum]~{avg:.6f}  min-of-sample~{mn:.6f}  c(n)={float(c(n)):.6f}  E<=c? {avg<=float(c(n))}  min<=c? {mn<=float(c(n))}")

# also exhaustive best pairing search for k=2,3 to sanity check known finding (k=2 beats, k=3 worse)
def exhaustive_best(k):
    best = None
    idxs = list(range(k_pieces))
    for chosen in itertools.combinations(idxs, 2*k):
        for pairing in all_pairings(chosen):
            pairs = []
            for (a,b) in pairing:
                i,j = (a,b) if p_float[a]>=p_float[b] else (b,a)
                pairs.append((i,j))
            v = anchor_merge_value(p_float, pairs)
            if best is None or v < best:
                best = v
    return best

def all_pairings(lst):
    if not lst:
        yield []
        return
    a = lst[0]
    for i in range(1, len(lst)):
        b = lst[i]
        rest = lst[1:i]+lst[i+1:]
        for sub in all_pairings(rest):
            yield [(a,b)]+sub

for k in [1,2,3]:
    b = exhaustive_best(k)
    print(f"k={k} exhaustive best OddSum = {b:.6f}  vs c(n)={float(c(n)):.6f}  beats? {b<=float(c(n))}")

print("\n--- Generalized Subset-Tie (Theorem 12), all indices i, best greedy J ---")
def subset_tie_value(p, i):
    pi = p[i]
    others = sorted([p[m] for m in range(len(p)) if m != i], reverse=True)
    # greedy: try to build subset T <= pi maximizing T via greedy (largest first that fits) -- heuristic
    # also do exact best-subset-sum <= pi via DP-ish search (small n, feasible by brute force over subsets)
    best_T = 0
    for mask in range(1 << len(others)):
        s = 0
        for b in range(len(others)):
            if mask & (1<<b):
                s += others[b]
        if s <= pi and s > best_T:
            best_T = s
    r = pi - best_T
    return 0.5*(1+r), best_T, r

vals = []
for i in range(k_pieces):
    v, T, r = subset_tie_value(p_float, i)
    vals.append(v)
    print(f"i={i} (p_i={p_float[i]:.4f}): best exact subset-tie OddSum={v:.6f} (T={T:.4f}, r={r:.4f})")

avg = sum(vals)/len(vals)
mn = min(vals)
print(f"E_i[best subset-tie]={avg:.6f}  min_i={mn:.6f}  c(n)={float(c(n)):.6f}")
