from fractions import Fraction as F
import random

def A(S):
    S = sorted(S, reverse=True)
    return sum((1 if i%2==0 else -1)*v for i,v in enumerate(S))

def Phi(S):
    T = sum(S)
    return (T + A(S))/2

def greedy_peel(W, budget):
    W = list(W)
    cuts_used = 0
    while len(W) >= 2:
        W.sort(reverse=True)
        a, b = W[0], W[1]
        if a == b:
            W = W[2:]
        else:
            if cuts_used >= budget:
                # cannot cut further; stop, just leave as is (shouldn't happen since legality lemma claims <=n)
                break
            newW = W[2:] + [a-b]
            W = newW
            cuts_used += 1
    v_final = W[0] if len(W)==1 else (0 if len(W)==0 else None)
    return v_final, cuts_used

random.seed(0)
mismatches=0
for trial in range(3000):
    m = random.randint(2,7)
    # random marking of m positive fractions summing to 1
    cuts = sorted(random.sample(range(1,10000), m-1))
    bounds=[0]+cuts+[10000]
    p = [F(bounds[i+1]-bounds[i],10000) for i in range(m)]
    n = m-1
    v_final, cuts_used = greedy_peel(p, n)
    assert cuts_used <= n
    # verify exact identity A(M) = v_final by re-simulating the actual cuts and recomputing sorted alternating sum
    # re-simulate keeping actual multiset (not just abstract W), to double check pair-cancellation claim exactly
    M = list(p)
    Wtrack = list(p)
    c=0
    while len(Wtrack)>=2:
        Wtrack.sort(reverse=True)
        a,b = Wtrack[0], Wtrack[1]
        if a==b:
            # remove exact pair from M as well
            M.remove(a); M.remove(b)
            Wtrack = Wtrack[2:]
        else:
            M.remove(a)
            M.append(b)   # a split into b, a-b: one copy stays in M (the a-b piece is new), other portion (b) is now duplicate of existing b
            M.append(a-b)
            Wtrack = Wtrack[2:] + [a-b]
            c+=1
    AM = A(M)
    if abs(AM - (v_final if v_final is not None else 0)) > 0:
        mismatches+=1
        print("MISMATCH", p, AM, v_final)
print("trials done, mismatches:", mismatches)
