import sympy
from sympy import primefactors, gcd, factorint
from collections import Counter

def gen_sequence(a1, N):
    a = [None, a1]
    while len(a) <= N:
        n = len(a)-1
        prev = a[-1]
        c = prev+1
        while True:
            ok = True
            for i in range(1, n+1):
                if gcd(c, a[i]) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a

a1 = 4807
N = 1500
a = gen_sequence(a1, N)
S0 = {2,3,5,7,11,19,23,73,127}
Q = set(primefactors(a1))
qstar = 17  # the actual canonical prime from our found rogue pair

smallest_j_counter = Counter()
shared_class = Counter()
branch_counter = Counter()
n_used = []
for n in range(20, N+1, 3):
    an = a[n]
    if an % qstar == 0:
        continue  # only test q ∤ a_n cases, per Lemma K's hypothesis
    c = qstar*(an//qstar)
    if c <= a[n-1]:
        branch_counter['a']+=1
        continue
    branch_counter['b']+=1
    n_used.append(n)
    for i in range(1,n):
        if gcd(c,a[i])==1:
            smallest_j_counter[i]+=1
            shared = set(primefactors(an)) & set(primefactors(a[i]))
            for p in shared:
                if p in Q: shared_class['Q']+=1
                elif p in S0: shared_class['S0\\Q']+=1
                else: shared_class['outside_S0']+=1
                if p == qstar:
                    shared_class['EQUALS_QSTAR']+=1
            break

print("branch counts (q=qstar=17):", branch_counter)
print("smallest-j distribution (top 15):", smallest_j_counter.most_common(15))
print("shared-prime class of smallest blocker:", shared_class)
