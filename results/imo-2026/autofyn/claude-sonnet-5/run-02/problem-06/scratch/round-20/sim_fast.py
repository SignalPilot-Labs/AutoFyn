import math, time

def build_seq_fast(a1, N):
    a = [None, a1]
    while len(a) <= N:
        prev = a[-1]
        cand = prev + 1
        while True:
            ok = True
            for i in range(1, len(a)):
                if math.gcd(cand, a[i]) == 1:
                    ok = False
                    break
            if ok:
                a.append(cand)
                break
            cand += 1
    return a

def primefactors(m):
    fs = set()
    d = 2
    mm = m
    while d*d <= mm:
        if mm % d == 0:
            fs.add(d)
            while mm % d == 0:
                mm //= d
        d += 1
    if mm > 1:
        fs.add(mm)
    return fs

def scan_branch_b(a1, N, core=None):
    a = build_seq_fast(a1, N)
    Pfac = [None]*(N+1)
    for n in range(1, N+1):
        Pfac[n] = primefactors(a[n])
    Q = Pfac[1] if core is None else core
    hits = []
    for n in range(2, N+1):
        outside = Pfac[n] - Q
        for qprime in outside:
            e=0; tmp=a[n]
            while tmp % qprime==0:
                tmp//=qprime; e+=1
            c = tmp
            if c <= a[n-1]:
                continue
            for i in range(1,n):
                if Pfac[i] & Pfac[n] == {qprime}:
                    hits.append((n,qprime,i))
                    break
            else:
                hits.append((n,qprime,"ERROR-no-rescuer"))
    return a, hits

t0=time.time()
total_checked=0
found=[]
for a1 in range(4, 400):
    a, hits = scan_branch_b(a1, 300)
    total_checked+=1
    if hits:
        found.append((a1,hits[:5]))
print("time", time.time()-t0)
print("checked", total_checked, "a1 values, found nonempty branch-b in:", len(found))
for f in found[:20]:
    print(f)
