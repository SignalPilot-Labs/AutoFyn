import sympy, time
def fast_greedy(a1, N):
    a=[a1]; minimal=[frozenset(sympy.primefactors(a1))]
    for _ in range(N-1):
        cur=a[-1]; m=cur+1
        while True:
            ms=frozenset(sympy.primefactors(m))
            if all(ms&S for S in minimal):
                a.append(m)
                if not any(S<=ms for S in minimal):
                    minimal=[S for S in minimal if not(ms<=S)]; minimal.append(ms)
                break
            m+=1
    return a,minimal

for a1,N in [(15,200),(35,2000),(77,2000),(91,2000),(143,3000),(175,6000),(847,12000),(1309,12000),(2085,12000)]:
    t0=time.time()
    a,minimal=fast_greedy(a1,N)
    el=time.time()-t0
    d=[a[i+1]-a[i] for i in range(len(a)-1)]
    # period
    Tfound=None
    for T in range(1, min(N-1, 8000)):
        run=0; i=len(d)-1
        while i-T>=0 and d[i]==d[i-T]: run+=1; i-=1
        if run>=max(3*T, 500):
            L=sum(d[i:i+T])
            Tfound=(T,run,i,L); break
    # all primes in minimal supports
    allp = sorted(set().union(*[set(s) for s in minimal]))
    M1 = sympy.prod(sorted(set(sympy.primefactors(a1))))
    print(f"a1={a1} (M1={M1}): #minimal={len(minimal)}, primes_in_minimal={allp}, max={max(allp) if allp else 0}, <=M1:{allp and max(allp)<=M1}, T={Tfound[0] if Tfound else None}, L={Tfound[3] if Tfound else None} ({sympy.factorint(Tfound[3]) if Tfound else ''})")
print(f"(times excluded for brevity)")
