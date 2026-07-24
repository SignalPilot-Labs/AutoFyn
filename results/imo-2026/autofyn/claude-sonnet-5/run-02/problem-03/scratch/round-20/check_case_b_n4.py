from fractions import Fraction as Fr
import random
n = 4
D = 2**(n+1) - 1
p = lambda i: Fr(2**(n+1-i), D)
p3, p4, p5 = p(3), p(4), p(5)
s = p3 + p4 + p5
u = p5  # = f(4)
def A(mset):
    ms = sorted(mset, reverse=True)
    tot, sign = Fr(0), 1
    for x in ms:
        tot += sign * x
        sign *= -1
    return tot
def Delta(R, v):
    return A(R) - 2 * A([x for x in R if x > v])
random.seed(0)
for _ in range(200000):
    b = Fr(random.randint(1, 999999), 1000000) * (p3 / 2)
    a = p3 - b
    R = [a, b, p4, p5]
    for v in {a, b, u, 2*u, Fr(random.randint(1,999999),1000000)*s}:
        if 0 < v < s:
            assert Delta(R, v) <= v - u
print("zero violations")
