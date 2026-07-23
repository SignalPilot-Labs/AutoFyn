import time
from math import gcd

def generate(a1, N):
    seq = [a1]
    while len(seq) < N:
        cand = seq[-1] + 1
        while True:
            if all(gcd(cand, x) > 1 for x in seq):
                seq.append(cand)
                break
            cand += 1
    return seq

t0=time.time()
seq = generate(21528751, 1200)
print("N=1200 done in", time.time()-t0, "s, maxterm=", seq[-1], "range=", seq[-1]-21528751)
