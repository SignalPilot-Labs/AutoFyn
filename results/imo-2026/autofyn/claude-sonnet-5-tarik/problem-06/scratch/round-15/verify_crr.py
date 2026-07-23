from math import gcd
from sympy import factorint

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

a1 = 21528751
print("factor a1:", factorint(a1))
N = 28000
seq = generate(a1, N)
targets = [1405, 11812, 27832, 2575]
for idx in targets:
    val = seq[idx-1]
    print(f"a_{idx} = {val}, factorization = {factorint(val)}")
