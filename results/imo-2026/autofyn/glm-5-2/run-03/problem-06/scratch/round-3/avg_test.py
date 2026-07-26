import sympy
from sympy import factorint

def greedy_seq(a1, N):
    a = [a1]
    supports = [set(factorint(a1).keys())]
    for n in range(N-1):
        an = a[-1]
        m = an + 1
        while True:
            ok = True
            for s in supports:
                shared = False
                for p in s:
                    if m % p == 0:
                        shared = True; break
                if not shared:
                    ok = False; break
            if ok:
                break
            m += 1
        a.append(m)
        supports.append(set(factorint(m).keys()))
    return a, supports

def avg_floor(a, a1):
    # b_n = floor((a_n - a1)/(n-1)) for n>=2 ; running average of d_k
    b = []
    S = 0
    for n in range(1, len(a)):
        S = a[n] - a1  # sum_{k=1}^{n-1} d_k
        if n >= 2:
            b.append(S // (n-1))
        else:
            b.append(None)
    return b

def is_eventually_const(seq, tail=100):
    t = [x for x in seq[-tail:] if x is not None]
    return len(set(t))==1, (t[0] if t else None)

def is_monotone(seq):
    s = [x for x in seq if x is not None]
    nondec = all(s[i]<=s[i+1] for i in range(len(s)-1))
    noninc = all(s[i]>=s[i+1] for i in range(len(s)-1))
    return nondec, noninc

for a1 in [6,15,35,77,91,105,143,385,1309,2085,145,116,1001,847,175,35,65,221,667,1763]:
    a,_ = greedy_seq(a1, 400)
    b = avg_floor(a, a1)
    ec, val = is_eventually_const(b, tail=80)
    nd, ni = is_monotone(b[:200])
    print(f"a1={a1:>5}  avgfloor_ev_const={ec} val={val}  nondec={nd} noninc={ni}  b_tail={b[-5:]}")
