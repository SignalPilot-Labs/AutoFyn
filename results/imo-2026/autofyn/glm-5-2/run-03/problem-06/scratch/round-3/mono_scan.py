import sympy
from sympy import factorint

def greedy_seq(a1, N):
    a = [a1]; supports = [set(factorint(a1).keys())]
    for n in range(N-1):
        an = a[-1]; m = an + 1
        while True:
            ok = True
            for s in supports:
                if not any(m % p == 0 for p in s):
                    ok = False; break
            if ok: break
            m += 1
        a.append(m); supports.append(set(factorint(m).keys()))
    return a, supports

# Test: is the running-average floor b_n = floor((a_n-a1)/(n-1)) monotone on a tail?
# Also test cumulative-defect C_n = n*M1 - (a_{n+1}-a1) : non-decreasing? unbounded?
# Also: max gap so far (trivially nondec, ev-const = M1).

def analyze(a1, N=400):
    a, sup = greedy_seq(a1, N)
    M1 = 1
    for p in factorint(a1): M1 *= p
    d = [a[i+1]-a[i] for i in range(len(a)-1)]
    # running avg floor
    b = [None]
    for n in range(1, len(a)):
        S = a[n]-a1
        b.append(S//(n-1) if n>=2 else None)
    bvals = [x for x in b if x is not None]
    # monotone?
    nd = all(bvals[i]<=bvals[i+1] for i in range(len(bvals)-1))
    ni = all(bvals[i]>=bvals[i+1] for i in range(len(bvals)-1))
    # eventually const?
    tail = bvals[-80:]
    ec = len(set(tail))==1
    # cumulative defect
    C = [(n+1)*M1 - (a[n+1]-a1) for n in range(len(a)-1)]
    C_nd = all(C[i]<=C[i+1] for i in range(len(C)-1))
    C_unbounded = C[-1] > C[0] + 50
    print(f"a1={a1:>5} M1={M1:>5}  avgfloor: evconst={ec} val={tail[0] if ec else '?'} nondec={nd} noninc={ni} | C nondec={C_nd} unbounded={C_unbounded} C_final={C[-1]}")

for a1 in [6,15,35,77,91,105,143,385,1309,2085,145,116,1001,847,175,65,221,667,1763,1517,1147,2491]:
    try: analyze(a1, 400)
    except Exception as e: print(f"a1={a1} ERR {e}")
