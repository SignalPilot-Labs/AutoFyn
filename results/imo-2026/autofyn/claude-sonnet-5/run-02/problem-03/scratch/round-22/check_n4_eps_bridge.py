from fractions import Fraction as F
import random

# Ladder values at n=4
D = 2**5 - 1
p2 = F(2**3, D)  # 8/31
p3 = F(2**2, D)  # 4/31
p4 = F(2**1, D)  # 2/31
p5 = F(2**0, D)  # 1/31
s  = p3 + p4 + p5  # 7/31
f4 = F(1, D)  # 1/31

assert p2 - s == f4, (p2-s, f4)

def A(multiset):
    xs = sorted(multiset, reverse=True)
    total = F(0)
    for i, x in enumerate(xs):
        total += x if i % 2 == 0 else -x
    return total

def gt(multiset, v):
    return [x for x in multiset if x > v]

def eps(multiset, v):
    return 1 if (len(gt(multiset, v)) % 2 == 1) else 0

def Delta(Rprime, v):
    return A(Rprime) - 2*A(gt(Rprime, v))

def random_legal_Rprime():
    # budget n-3 = 1 cut total among pieces p3,p4,p5
    # either zero cuts (tau itself) or split exactly one piece into two positive fragments
    base = [p3, p4, p5]
    if random.random() < 0.2:
        return list(base)
    idx = random.randrange(3)
    piece = base[idx]
    # split piece into a, piece-a, a in (0, piece), random rational
    num = random.randint(1, 10**6 - 1)
    a = piece * F(num, 10**6)
    b = piece - a
    if a <= 0 or b <= 0:
        return list(base)
    rest = [base[j] for j in range(3) if j != idx]
    return rest + [a, b]

random.seed(12345)
N = 50000
max_abs_diff = F(0)
mismatches = 0
sharp_margin_min = None
diamond_margin_min = None

for _ in range(N):
    Rprime = random_legal_Rprime()
    # sample v2 in (0, s)  [domain of (Diamond')]
    num2 = random.randint(1, 10**6 - 1)
    v2 = s * F(num2, 10**6)
    # sample v1 in (max(s, p2-v2), p2)  [domain of (sharp') given v2]
    lo = max(s, p2 - v2)
    if lo >= p2:
        continue
    num1 = random.randint(1, 10**6 - 1)
    v1 = lo + (p2 - lo) * F(num1, 10**6)
    if not (v1 > s and v1 < p2):
        continue
    if not (v2 > p2 - v1 and v2 < s):
        continue

    e = eps(Rprime, v2)
    Del = Delta(Rprime, v2)

    # (sharp') margin: RHS - LHS, want >= 0
    sharp_margin = (s - (v1 - v2) - 2*v2*e) - Del
    # (Diamond') margin at v = v2
    diamond_margin = (v2 - f4 - 2*v2*e) - Del

    predicted_diff = p2 - v1
    actual_diff = sharp_margin - diamond_margin
    if actual_diff != predicted_diff:
        mismatches += 1
        if mismatches <= 5:
            print("MISMATCH", Rprime, v1, v2, e, Del, sharp_margin, diamond_margin, predicted_diff, actual_diff)

    if sharp_margin_min is None or sharp_margin < sharp_margin_min:
        sharp_margin_min = sharp_margin
    if diamond_margin_min is None or diamond_margin < diamond_margin_min:
        diamond_margin_min = diamond_margin

print("trials effectively run: N=", N)
print("mismatches (identity margin_sharp' - margin_diamond' == p2-v1):", mismatches)
print("min sharp' margin found:", sharp_margin_min, float(sharp_margin_min))
print("min diamond' margin found:", diamond_margin_min, float(diamond_margin_min))
