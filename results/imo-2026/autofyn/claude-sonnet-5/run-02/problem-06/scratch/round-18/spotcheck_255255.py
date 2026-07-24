import time
t0=time.time()

def factor(x):
    fs = []
    d = 2
    y = x
    while d*d <= y:
        if y % d == 0:
            fs.append(d)
            while y % d == 0:
                y //= d
        d += 1
    if y > 1:
        fs.append(y)
    return fs

a1 = 255255
N = 140000
seq = [a1]
prime_masks = {}  # prime -> bitmask of indices (1-based) covered
def add_term(idx, val):
    for p in factor(val):
        m = prime_masks.get(p, 0)
        prime_masks[p] = m | (1 << (idx-1))

add_term(1, a1)
full_mask = (1<<1) - 1  # not used directly; we test coverage via OR check

n = 1
cur = a1
target_mask_len = 1
covered_all = 1  # mask representing indices 1..n covered so far (we need candidate c to cover exactly bits 0..n-1)
covered_all = 1

while n < N:
    need_mask = (1 << n) - 1  # bits for indices 1..n
    c = cur + 1
    while True:
        # compute mask of union of primes dividing c
        u = 0
        for p in factor(c):
            u |= prime_masks.get(p, 0)
        if (u & need_mask) == need_mask:
            break
        c += 1
    seq.append(c)
    add_term(n+1, c)
    cur = c
    n += 1

print("time", time.time()-t0)
Q = set(factor(a1))
target_type = frozenset({5,7,11,13,17})
def base_type(x):
    return frozenset(factor(x)) & Q

occs = [i+1 for i,v in enumerate(seq) if base_type(v)==target_type]
print("occurrences of target type through n=",N,":", occs[:10])
