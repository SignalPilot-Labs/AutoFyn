from fractions import Fraction as F
import random
def A(vals):
    s=sorted(vals,reverse=True)
    a=F(0);sign=1
    for v in s:
        a+=sign*v; sign=-sign
    return a
random.seed(5)
for _ in range(20000):
    r=random.randint(1,12)
    vals=[F(random.randint(0,100),random.randint(1,10)) for _ in range(r)]
    a=A(vals)
    assert a>=0, (vals,a)
print("A(S)>=0 confirmed for 20000 random nonnegative multisets (elementary pairing argument).")
