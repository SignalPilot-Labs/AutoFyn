from fractions import Fraction as F
import random, itertools

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]  # p_1..p_{n+1}

def A(S):
    S = sorted(S, reverse=True)
    return sum((1 if i%2==0 else -1)*v for i,v in enumerate(S))

# Lemma 23: p_i > sum_{j>i} p_j ; p_i = 2 p_{i+1}
for n in range(1,9):
    p = ladder(n)  # p[0]=p_1,...
    for i in range(1, n+2):  # i=1..n+1
        tail = sum(p[i:])  # sum_{j>i} p_j (0-indexed p[i] = p_{i+1})
        assert p[i-1] > tail, (n,i,p[i-1],tail)
    for i in range(1, n+1):
        assert p[i-1] == 2*p[i], (n,i)
print("Lemma 23 OK")

# Lemma 24: p2 - s = f(n), s = sum(p3..p_{n+1})
for n in range(2,9):
    p = ladder(n)
    fn = F(1, 2**(n+1)-1)
    s = sum(p[2:])  # p_3.. (0-indexed p[2]=p_3)
    p2 = p[1]
    assert p2 - s == fn, (n, p2-s, fn)
print("Lemma 24 OK")
