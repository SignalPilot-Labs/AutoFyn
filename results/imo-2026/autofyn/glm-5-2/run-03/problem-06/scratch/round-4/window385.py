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
    return a

a = fast_greedy(385, 12000)
d=[a[i+1]-a[i] for i in range(len(a)-1)]
n=len(d)
print(f"n={n}, T=5088, checking window determinism on the PERIODIC part (indices {n-5088*2}..{n-1})")

# On the periodic part, window map is trivially functional. 
# The REAL test: does a SMALL window (W << T) determine d_{n+1} in the periodic part?
# i.e., are there few distinct windows of size W, and is the map functional?
start = n - 5088  # one full period at the end
for W in [1,2,3,4,5,8,12,20,40]:
    seen={}
    conflict=0
    for i in range(start+W, n-1):
        key=tuple(d[i-W:i])
        if key in seen:
            if seen[key]!=d[i]:
                conflict+=1
        else:
            seen[key]=d[i]
    print(f"W={W}: #distinct windows={len(seen)}, conflicts={conflict}")

print("\n--- larger W ---")
for W in [100, 500, 2000, 4500, 5087]:
    seen={}; conflict=0
    for i in range(start+W, n-1):
        key=tuple(d[i-W:i])
        if key in seen:
            if seen[key]!=d[i]: conflict+=1
        else: seen[key]=d[i]
    print(f"W={W}: #distinct windows={len(seen)}, conflicts={conflict}")
