import random
from fractions import Fraction as F

def A_of(vals):
    s = sorted(vals, reverse=True)
    total = F(0)
    for i,v in enumerate(s):
        total += v if i%2==0 else -v
    return total

def construct(pieces, j):
    m = len(pieces)
    if 2*j > m:
        return None
    tail = pieces[2*j:]
    # process split pairs i=j down to 1, assigning actual a_i,b_i
    # bound_above: the value that b_i must be less than (from the more-central side, i.e. previous constructed a)
    # bound_below: from tail or nothing
    split_info = []  # (i, p_odd, p_even) for split pairs, index order 1..j
    for i in range(1, j+1):
        p_odd = pieces[2*i-2]
        p_even = pieces[2*i-1]
        split_info.append((i, p_odd, p_even, p_odd != p_even))
    # Build from innermost (largest i) outward
    lower_bound_for_b = tail[0] if tail else F(0)  # b_j must be > this (if tail nonempty); if empty, just >=0
    chain_frags = {}  # i -> (a_i,b_i) for split pairs
    prev_b = None  # b_{i+1} not used; we need a_i < b_{i-1}, process forward instead
    # We must choose in order i=j,...,1 the b_i, ensuring a_i < b_{i-1} eventually.
    # Let's track the "ceiling" that the NEXT (smaller i) pair's a must be below: that's b_i (once chosen)
    ceiling = None  # ceiling on a_i imposed by b_{i+1}... actually a_i < b_{i-1}, so ceiling applies going the other way.
    # Redo: process i = j downto 1. For pair i, need:
    #   a_i in (max(p_even,p_odd-p_even), p_odd)
    #   b_i = p_odd - a_i
    #   if i==j and tail nonempty: b_i > tail[0]
    #   if i>1 : a_{i-1} < b_i  (set as ceiling for pair i-1)
    # Also for pair i (i<j, i.e. not last), if pair i+1 exists and is EQUAL (not split), that's fine (no constraint from it, skip to next split for ceiling chain)
    # We'll just track "current ceiling" = the b of the most recent split pair processed (smaller-index side)
    current_ceiling = None  # constraint on next a (from larger i side) -> smaller i's a must be less than this b
    results = {}
    ok = True
    for i in range(j, 0, -1):
        p_odd = pieces[2*i-2]
        p_even = pieces[2*i-1]
        if p_odd == p_even:
            continue  # no cut, no ordering constraint at all (pair-cancellation-identity)
        lower = max(p_even, p_odd - p_even)
        upper = p_odd
        if current_ceiling is not None:
            upper = min(upper, current_ceiling)
        if lower >= upper:
            ok = False
            break
        # additionally if this is the pair closest to tail (i.e., no split pair yet processed with smaller "closeness", meaning tail bound applies if no other split constraint yet set OR always if i==j... )
        # Actually tail bound only directly constrains the LAST split pair before the tail in final chain order,
        # which is the split pair with the LARGEST i among 1..j (since pairs are in order 1,2,...,j then tail).
        # We must apply the tail bound to whichever split pair is currently the "closest to tail" -- since we
        # process i descending and tail bound was already the initial current_ceiling target... let's just apply:
        if current_ceiling is None and tail:
            upper = min(upper, F(10**9))  # no additional shrink; tail bound is on b, not a, so handle after choosing a
        a_i = (lower + upper) / 2
        b_i = p_odd - a_i
        if tail and current_ceiling is None:
            # this is the last split pair before tail; ensure b_i > tail[0]
            if not (b_i > tail[0]):
                # try to push a_i down (increase b_i) within (lower, upper)
                # b_i > tail[0]  <=>  a_i < p_odd - tail[0]
                new_upper = min(upper, p_odd - tail[0])
                if lower >= new_upper:
                    ok = False
                    break
                a_i = (lower + new_upper) / 2
                b_i = p_odd - a_i
        results[i] = (a_i, b_i)
        current_ceiling = b_i
    if not ok:
        return None
    final = []
    splitcount_total = 0
    gap_sum = F(0)
    split_rank = 0
    for i in range(1, j+1):
        p_odd = pieces[2*i-2]
        p_even = pieces[2*i-1]
        if p_odd == p_even:
            final.append(p_odd)
            final.append(p_even)
        else:
            split_rank += 1
            a_i, b_i = results[i]
            final.append(a_i)
            final.append(p_even)
            final.append(b_i)
            sign = 1 if split_rank % 2 == 1 else -1
            gap_sum += sign * (p_odd - p_even)
            splitcount_total += 1
    final += list(tail)
    return final, gap_sum, splitcount_total

random.seed(2)
tested = 0
mismatches = 0
infeasible = 0
for trial in range(30000):
    m = random.randint(2, 10)
    if m < 2:
        continue
    j = random.randint(1, m//2)
    vals = [F(random.randint(1,80), random.randint(1,9)) for _ in range(m)]
    vals.sort(reverse=True)
    for i in range(j):
        if random.random() < 0.45:
            avg = (vals[2*i] + vals[2*i+1]) / 2
            vals[2*i] = avg
            vals[2*i+1] = avg
    vals.sort(reverse=True)
    res = construct(vals, j)
    if res is None:
        infeasible += 1
        continue
    final, gap_sum, jprime = res
    A_direct = A_of(final)
    tail = vals[2*j:]
    A_tail = A_of(tail)
    predicted = gap_sum + (F(-1)**jprime) * A_tail
    tested += 1
    if predicted != A_direct:
        mismatches += 1
        if mismatches <= 8:
            print("MISMATCH", vals, "j=",j,"jprime=",jprime, "A_direct=",A_direct,"predicted=",predicted)

print(f"tested={tested} infeasible={infeasible} mismatches={mismatches}")

# specific counterexample check
vals = [F(45),F(45),F(31),F(27)]
res = construct(vals, 2)
print("counterexample construct:", res)
if res:
    final, gap_sum, jprime = res
    print("A_direct=", A_of(final), "predicted=", gap_sum + (F(-1)**jprime)*A_of(vals[4:]))
