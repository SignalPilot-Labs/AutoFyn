import sympy, math

def gen(a1, N):
    a = [a1]
    while len(a) < N:
        c = a[-1] + 1
        while True:
            ok = all(math.gcd(c, x) > 1 for x in a)
            if ok:
                a.append(c)
                break
            c += 1
    return a

def primes(x):
    return set(sympy.primefactors(x))

N = 8000
a1 = 11305
seq = gen(a1, N)
S0 = {2,3,5,7,13,17,19,23,29,37,43,101}
rho = [primes(x) & S0 for x in seq]

A = frozenset({2,5})
B = frozenset({3,7})
Aidx = [i+1 for i,t in enumerate(rho) if frozenset(t)==A]
Bidx = [i+1 for i,t in enumerate(rho) if frozenset(t)==B]
print("num A occ:", len(Aidx))
print("num B occ:", len(Bidx))

print("a_4=", seq[3], "outcore:", primes(seq[3])-S0)
print("a_7=", seq[6], "outcore:", primes(seq[6])-S0)

sig_counts = {}
for i in Aidx:
    outcore = primes(seq[i-1]) - S0
    sig_counts.setdefault(frozenset(outcore), []).append(i)
for sig, idxs in sig_counts.items():
    if len(sig)==1:
        print("singleton A sig:", set(sig), "count:", len(idxs), "first idx:", idxs[0])

q=11
badA = [n for n in Aidx if n>103 and seq[n-1]%q!=0]
badB = [n for n in Bidx if n>4 and seq[n-1]%q!=0]
print("bad A:", len(badA), badA[:5])
print("bad B:", len(badB), badB[:5])
