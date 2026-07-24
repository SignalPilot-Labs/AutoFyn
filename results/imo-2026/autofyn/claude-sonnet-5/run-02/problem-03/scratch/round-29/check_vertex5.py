from fractions import Fraction as F
import random

def A(vals):
    vals = sorted(vals, reverse=True)
    s = F(0)
    for i,v in enumerate(vals):
        if i % 2 == 0: s += v
        else: s -= v
    return s

def run(m, trials=3000):
    f = F(1)
    q = [F(2)**(m+1-i)*f for i in range(1, m+2)]
    q1 = q[0]; tail = q[1:]
    worst = None
    for _ in range(trials):
        num = random.randint(1, 999)
        x = q1 * F(num, 2000)
        S = [x, q1 - x] + tail
        for t in tail:
            B = [t] + S
            val = A(B)
            if worst is None or val < worst[0]:
                worst = (val, x, t)
    return worst, f

for m in [3, 4, 5]:
    w, f = run(m)
    print("m=", m, "worst=", w, "target f=", f, "OK" if w[0] >= f else "VIOLATION")
