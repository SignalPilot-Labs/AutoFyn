import math, signal
from sympy import factorint
exec(open('/tmp/round-2/sweep6.py').read().split("if __name__")[0])

def count_avoiding(P_ess_list, Mlist, cap=300000):
    c=0
    for _ in avoiding_transversals(P_ess_list, Mlist):
        c+=1
        if c>cap: return '>'+str(cap)
    return c

# trace #avoiding-transversals and #all-transversals over promotions
for a1 in [187, 221, 35, 65, 15]:
    M=[frozenset(primes_of(a1))]; P_ess=sorted(M[0]); a=a1
    print(f"a1={a1}:")
    for r in range(50):
        av=count_avoiding(P_ess,[set(m) for m in M])
        alltr=sum(1 for _ in all_transversals(P_ess,[set(m) for m in M]) if _ ) if len(P_ess)<=14 else '?'
        print(f"  r{r}: a={a} |Pess|={len(P_ess)} |M|={len(M)} #avoiding={av}")
        if av==0:
            print("  -> STABLE"); break
        res=next_promo(a,P_ess,[set(m) for m in M])
        if res is None: print("  -> stable"); break
        m,Ts,Pnew=res; old=set(P_ess)
        newM=[set(mm) for mm in M if not(Pnew<=set(mm))]; newM.append(set(Pnew))
        M=[frozenset(x) for x in newM]; P_ess=sorted(set(P_ess)|Pnew); a=m
