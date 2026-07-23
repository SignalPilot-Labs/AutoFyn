import sympy
from sympy import factorint, gcd

def brute_gen(a1, N):
    terms = [a1]
    while len(terms) < N:
        c = terms[-1] + 1
        while not all(gcd(c, t) > 1 for t in terms):
            c += 1
        terms.append(c)
    return terms

# --- Verify 4199 witnesses ---
print("=== a1=4199 ===")
terms = brute_gen(4199, 100)
P1 = set(factorint(4199).keys())
print("P1 =", P1)
for idx in [1,2,4,8,10,11,81,91]:  # 0-indexed: a_2=index1, a_5=index4, a_9=index8, a_12=index11, a_82=index81,a_92=index91
    pass

def show(idx1based):
    v = terms[idx1based-1]
    f = factorint(v)
    print(f"a_{idx1based} = {v} = {f}, core(P1-part) = {set(f.keys())&P1}, comp = {set(f.keys())-P1}")

for i in [2,5,9,11,12,82,92]:
    if i <= len(terms):
        show(i)
    else:
        print(f"a_{i} not in first {len(terms)} terms, need more")
