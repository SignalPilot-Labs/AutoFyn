import random
from fractions import Fraction as F

def A_of(sorted_desc):
    s = 0
    for i, v in enumerate(sorted_desc):
        s += v if i % 2 == 0 else -v
    return s

def try_construct(pieces, j):
    # pieces: list of Fraction, sorted descending, 1-indexed conceptually
    m = len(pieces)
    if 2*j > m:
        return None
    frags = []  # (value, pair_index, kind) kind in {'a','b','p2i','tail'}
    jprime = 0
    gamma_prev = None  # supremum available (as Fraction or None=inf)
    # We just directly build a legal chain using midpoint-ish choices within feasible interval,
    # to test the identity numerically (not proving feasibility, just constructing an explicit instance)
    chain = []  # list of values in the intended sorted order (for verification we build multiset)
    gap_sum = F(0)
    split_flags = []
    for i in range(1, j+1):
        p_odd = pieces[2*i-2]  # p_{2i-1}
        p_even = pieces[2*i-1]  # p_{2i}
        if p_odd == p_even:
            split_flags.append(False)
            continue
        split_flags.append(True)
        jprime += 1
        lower = max(p_even, p_odd - p_even)
        upper = p_odd
        if gamma_prev is not None:
            upper = min(upper, gamma_prev)
        if lower >= upper:
            return None
        a_i = (lower + upper) / 2  # midpoint choice within (lower, upper)
        b_i = p_odd - a_i
        chain.append(('a', a_i))
        chain.append(('p2i', p_even))
        chain.append(('b', b_i))
        gap_sum += (F(1) if i%2==1 else F(-1)) * (p_odd - p_even)
        gamma_prev = min(p_odd - p_even, p_even)
    # equal pairs: just leave untouched, contributes two elements each equal to p_odd=p_even
    # need feasibility w.r.t tail too but skip strict check here; just build final tail check separately
    tail = pieces[2*j:]
    if tail:
        if gamma_prev is not None and not (gamma_prev > tail[0]):
            return None
    # Build final multiset
    final = []
    idx = 0
    for i in range(1, j+1):
        p_odd = pieces[2*i-2]
        p_even = pieces[2*i-1]
        if p_odd == p_even:
            final.append(p_odd)
            final.append(p_even)
        else:
            # find matching chain entries
            pass
    # redo properly building final list in order
    final = []
    ci = 0
    for i in range(1, j+1):
        p_odd = pieces[2*i-2]
        p_even = pieces[2*i-1]
        if p_odd == p_even:
            final.append(p_odd)
            final.append(p_even)
        else:
            a_i, p_even_v, b_i = chain[ci][1], chain[ci+1][1], chain[ci+2][1]
            ci += 3
            final.append(a_i)
            final.append(p_even_v)
            final.append(b_i)
    final += tail
    return final, gap_sum, jprime

random.seed(1)
mismatches = 0
tested = 0
infeasible = 0
for trial in range(20000):
    m = random.randint(2, 10)
    j = random.randint(1, m//2) if m>=2 else 0
    if j == 0:
        continue
    # build random pieces sorted descending, force some equal pairs
    vals = [F(random.randint(1,50), random.randint(1,7)) for _ in range(m)]
    vals.sort(reverse=True)
    # force equality in some of first 2j with some probability
    for i in range(j):
        if random.random() < 0.4:
            # force pair i equal
            avg = (vals[2*i] + vals[2*i+1]) / 2
            vals[2*i] = avg
            vals[2*i+1] = avg
    vals.sort(reverse=True)
    res = try_construct(vals, j)
    if res is None:
        infeasible += 1
        continue
    final, gap_sum, jprime = res
    final_sorted = sorted(final, reverse=True)
    A_direct = A_of(final_sorted)
    tail = vals[2*j:]
    tail_sorted = sorted(tail, reverse=True)
    A_tail = A_of(tail_sorted)
    predicted_correct = gap_sum + (F(-1)**jprime) * A_tail
    predicted_buggy = gap_sum + (F(-1)**j) * A_tail
    tested += 1
    if predicted_correct != A_direct:
        mismatches += 1
        if mismatches <= 5:
            print("MISMATCH(corrected)", vals, j, jprime, A_direct, predicted_correct)
print(f"tested={tested} infeasible={infeasible} mismatches(corrected formula)={mismatches}")

# Now specifically test the known bug example (45,45,31,27), j=2
vals = [F(45), F(45), F(31), F(27)]
res = try_construct(vals, 2)
print("bug example result:", res)
if res:
    final, gap_sum, jprime = res
    final_sorted = sorted(final, reverse=True)
    A_direct = A_of(final_sorted)
    tail = vals[4:]
    A_tail = A_of(sorted(tail, reverse=True))
    print("A_direct", A_direct, "predicted corrected", gap_sum + (F(-1)**jprime)*A_tail, "predicted buggy(-1)^j", gap_sum + (F(-1)**2)*A_tail)
