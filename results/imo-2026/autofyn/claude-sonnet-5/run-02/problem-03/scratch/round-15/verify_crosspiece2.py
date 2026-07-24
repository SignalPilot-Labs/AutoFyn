from fractions import Fraction as F
from collections import Counter
import random

def A(vals):
    s = sorted(vals, reverse=True)
    a = F(0); sign=1
    for v in s:
        a += sign*v; sign=-sign
    return a

def phi(vals):
    return (sum(vals)+A(vals))/2

def odd_run_reduce_with_origin(items):
    # items: list of (value, piece_id)
    from collections import defaultdict
    by_val = defaultdict(list)
    for v,pid in items:
        by_val[v].append(pid)
    out = []
    for v, pids in by_val.items():
        if len(pids) % 2 == 1:
            out.append((v, pids[0]))  # arbitrary surviving owner; owner choice doesn't matter for A itself
    return out

def check_monochromatic_and_eval(items):
    # items: list of (value, piece_id), representing final multiset with piece attribution
    # Step 1: odd-run reduce (pair off equal values across ANY pieces)
    reduced = odd_run_reduce_with_origin(items)
    # Step 2: sort reduced by value descending (all distinct by construction of odd-run-reduce)
    reduced_sorted = sorted(reduced, key=lambda t: -t[0])
    # group ranks by piece id present in reduced
    piece_ranks = {}
    for idx,(v,pid) in enumerate(reduced_sorted):
        r = idx+1  # 1-indexed rank
        piece_ranks.setdefault(pid, []).append(r)
    # check monochromatic: each piece's ranks share parity
    eps = {}
    mono = True
    for pid, ranks in piece_ranks.items():
        parities = set(r % 2 for r in ranks)  # 1 = odd rank -> sign +1 ; 0 = even rank -> sign -1
        if len(parities) != 1:
            mono = False
            break
        eps[pid] = 1 if ranks[0] % 2 == 1 else -1
    if not mono:
        return None
    # q_i = sum of surviving values attributed to piece i (from reduced set)
    q = {}
    for v,pid in reduced_sorted:
        q[pid] = q.get(pid, F(0)) + v
    predicted_A = sum(eps[pid]*q[pid] for pid in eps)
    actual_vals = [v for v,pid in items]
    actual_A = A(actual_vals)
    return predicted_A, actual_A, eps, q

random.seed(42)
tests_run = 0
tests_checked = 0
for trial in range(20000):
    m = random.randint(2,6)
    p = sorted([F(random.randint(1,30), random.randint(1,10)) for _ in range(m)], reverse=True)
    # choose random subset to split into 2 fragments each (using nice split points to try to hit ties sometimes)
    items = []
    for i,val in enumerate(p):
        if random.random() < 0.5 and val > 0:
            # split into two fragments
            num = random.randint(1, 1000)
            frac = F(num, 1001)
            f1 = val*frac
            f2 = val - f1
            items.append((f1, i))
            items.append((f2, i))
        else:
            items.append((val, i))
    # occasionally force an exact cross-piece tie by copying a value from one item to another
    if random.random() < 0.3 and len(items) >= 2:
        a,b = random.sample(range(len(items)), 2)
        va, pa = items[a]
        vb, pb = items[b]
        items[b] = (va, pb)
    tests_run += 1
    res = check_monochromatic_and_eval(items)
    if res is not None:
        tests_checked += 1
        predicted_A, actual_A, eps, q = res
        assert predicted_A == actual_A, (items, predicted_A, actual_A)

print(f"Ran {tests_run} random constructions, {tests_checked} were monochromatic and verified exactly (zero mismatches).")
