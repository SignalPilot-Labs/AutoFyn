import sympy, itertools

def P(m): return set(sympy.primefactors(m))

def minimal_family(fam_list):
    out=[]
    for S in fam_list:
        if not any((other<S) for other in fam_list if other!=S):
            if S not in out: out.append(S)
    return out

def is_transversal(T, Mfam): return all(T&M for M in Mfam)

def is_minimal_transversal(T, Mfam):
    # T is a transversal of Mfam, and no proper subset of T is.
    if not is_transversal(T, Mfam): return False
    for r in range(1, len(T)):
        for sub in itertools.combinations(T, r):
            if is_transversal(set(sub), Mfam):
                return False
    return True

def run(a1, max_steps=4000):
    a=[a1]; fam=[P(a1)]; Mn=minimal_family(fam); pstar=min(P(a1))
    crashes=[]
    for n in range(1, max_steps):
        m=a[-1]+1
        while True:
            if all(P(m)&Mi for Mi in Mn): break
            m+=1
        Pm=P(m); new_fam=fam+[Pm]; new_Mn=minimal_family(new_fam)
        is_promo = not any(S<=Pm for S in Mn)
        if is_promo:
            # is Pm a minimal transversal of Mn (old family)?
            mt = is_minimal_transversal(Pm, Mn)
            # does Pm have a proper subset that is a transversal of Mn? (free-rider)
            free = any(is_transversal(set(sub), Mn) for r in range(1,len(Pm)) for sub in itertools.combinations(Pm,r))
            crashes.append({'n':n,'a':m,'P':sorted(Pm),'min':min(Pm),'pstar':pstar,
                            'minimal_transversal':mt,'has_free_rider':free})
        a.append(m); fam=new_fam; Mn=new_Mn
        if n>20 and len(Mn)==1 and len(list(Mn)[0])==1: break
        if n>60 and new_Mn==minimal_family(fam[:-1]) and all(not any(S<=P(a[k+1]) for S in Mn) for k in range(n-50,n)):
            break
    return crashes

for a1 in [15,105,175,429,1001]:
    print(f"\n=== a1={a1} p*={min(P(a1))} ===")
    c=run(a1)
    for r in c:
        print(f"  step{r['n']}: a={r['a']} P={r['P']} min={r['min']}<=p*?{r['min']<=r['pstar']} | minTransversal={r['minimal_transversal']} freeRider={r['has_free_rider']}")
