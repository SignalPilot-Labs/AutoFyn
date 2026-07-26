import sys, time
sys.path.insert(0, '/tmp/round-6')
from fast_greedy_correct import greedy_fast, rad

def naive_greedy(a1, N):
    import math
    a=[a1]
    for _ in range(N-1):
        prev=a[-1]; m=prev+1
        while True:
            if all(math.gcd(m,x)>1 for x in a):
                break
            m+=1
        a.append(m)
    return a

for a1,N in [(15,40),(77,60),(35,80)]:
    f=greedy_fast(a1,N)
    n=naive_greedy(a1,N)
    same = f==n
    print(f"a1={a1} N={N} fast==naive: {same}")
    if not same:
        for i,(x,y) in enumerate(zip(f,n)):
            if x!=y:
                print(f"  first diff idx {i}: fast={x} naive={y}")
                break
