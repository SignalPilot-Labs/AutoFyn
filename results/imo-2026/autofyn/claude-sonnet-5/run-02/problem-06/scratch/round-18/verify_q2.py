import math

def gcd(a,b):
    return math.gcd(a,b)

def gen(a1, N):
    seq=[a1]
    used=set([a1])
    while len(seq)<N:
        c=seq[-1]+1
        while True:
            if c not in used and all(gcd(c,x)>1 for x in seq):
                break
            c+=1
        seq.append(c)
        used.add(c)
    return seq

def P(n):
    fs=set()
    d=2
    m=n
    while d*d<=m:
        while m%d==0:
            fs.add(d)
            m//=d
        d+=1
    if m>1:
        fs.add(m)
    return fs

for a1 in [187,209,221,247]:
    seq = gen(a1, 1500)
    Q = P(a1)
    types = [tuple(sorted(P(x)&Q)) for x in seq]
    from collections import Counter
    c = Counter(types)
    print(a1, Q, c.most_common(6))
