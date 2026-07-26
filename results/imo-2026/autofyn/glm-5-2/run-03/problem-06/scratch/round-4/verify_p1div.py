import math

def greedy_seq(a1, N):
    a = [a1]
    while len(a) < N:
        m = a[-1] + 1
        while True:
            if all(math.gcd(m, x) > 1 for x in a):
                a.append(m); break
            m += 1
    return a

# a1=15, P_1={3,5}, M_1=15. Governing r=2 (not in P_1).
# Check: every cofactor k = a_n/2 (for 2-multiple terms) divisible by 3 or 5?
a = greedy_seq(15, 400)
fails = 0
for n in range(len(a)):
    if a[n] % 2 == 0:
        k = a[n] // 2
        if k % 3 != 0 and k % 5 != 0:
            fails += 1
            if fails <= 5:
                print("FAIL:", a[n], k)
print(f"a1=15, r=2: {fails} cofactor failures out of {sum(1 for x in a if x%2==0)} 2-multiples")

# a1=35, P_1={5,7}, M_1=35. Governing r=2.
a = greedy_seq(35, 200)
fails = 0
for n in range(len(a)):
    if a[n] % 2 == 0:
        k = a[n] // 2
        if k % 5 != 0 and k % 7 != 0:
            fails += 1
print(f"a1=35, r=2: {fails} cofactor failures")

# a1=35, governing r=3 (3|L=210)
a = greedy_seq(35, 200)
fails = 0
for n in range(len(a)):
    if a[n] % 3 == 0:
        k = a[n] // 3
        if k % 5 != 0 and k % 7 != 0:
            fails += 1
            if fails <= 5: print("FAIL r=3:", a[n], k)
print(f"a1=35, r=3: {fails} cofactor failures out of {sum(1 for x in a if x%3==0)} 3-multiples")

# Verify Schur AP structure for a1=35, r=3
a = greedy_seq(35, 400)
# T=34, L=210 for a1=35
T, L = 34, 210
ok = all(a[n+T] == a[n]+L for n in range(len(a)-T))
print(f"a1=35 T={T}L={L} periodic:", ok)
idx = [n for n in range(len(a)) if a[n] % 3 == 0]
cof = [a[n]//3 for n in idx]
s = sum(1 for n in range(T) if a[n] % 3 == 0)
Lr = L // 3
ap_ok = all(cof[i+s] == cof[i] + Lr for i in range(len(cof)-s))
print(f"a1=35 r=3: s={s} L/r={Lr} AP holds:", ap_ok)
