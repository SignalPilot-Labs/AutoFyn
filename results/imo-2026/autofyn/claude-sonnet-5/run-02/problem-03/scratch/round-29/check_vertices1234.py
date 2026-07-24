from fractions import Fraction as F

def A(vals):
    vals = sorted(vals, reverse=True)
    s = F(0)
    for i,v in enumerate(vals):
        if i % 2 == 0: s += v
        else: s -= v
    return s

for m in [3,4,5,6]:
    f = F(1)
    q = [F(2)**(m+1-i)*f for i in range(1, m+2)]
    q1 = q[0]; tail = q[1:]
    # sample many x in (0, q1/2]
    bad = []
    for num in range(1, 2000):
        x = q1*F(num, 4000)
        if x <= 0 or x > q1/2: continue
        S = [x, q1-x] + tail
        for c in [F(0), q1, x, q1-x]:
            B = [c] + S
            val = A(B)
            if val < f:
                bad.append((m,x,c,val))
    print(m, "violations:", len(bad), bad[:3])
