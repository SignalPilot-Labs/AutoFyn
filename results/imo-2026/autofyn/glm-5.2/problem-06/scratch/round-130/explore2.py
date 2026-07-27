import math
from itertools import combinations
from collections import defaultdict

def factor(m):
    f=set(); n=m; d=2
    while d*d<=n:
        while n%d==0: f.add(d); n//=d
        d+=1
    if n>1: f.add(n)
    return f

def gen_sequence(a1, max_terms=2000, cap=10**8):
    a=[a1]; F=[frozenset(factor(a1))]
    Mn=[F[0]]
    promo_log=[]
    maxMsize=1; maxMcount=1
    while len(a)<max_terms:
        an=a[-1]; Mn_cur=Mn
        m=an+1
        while m<=cap:
            Pm=frozenset(factor(m))
            if all(Pm & M for M in Mn_cur):
                break
            m+=1
        if m>cap: break
        Pm=frozenset(factor(m))
        dominated = any(M <= Pm for M in Mn_cur)
        if not dominated:
            refines = [M for M in Mn_cur if Pm < M]
            new_Mn=[M for M in Mn_cur if not (Pm < M)]
            new_Mn.append(Pm)
            Mn=new_Mn
            promo_log.append((len(a)+1, m, set(Pm), 'refine' if refines else 'incomp'))
            maxMsize=max(maxMsize,len(Pm))
            maxMcount=max(maxMcount,len(Mn))
        a.append(m)
    return a, Mn, promo_log, maxMsize, maxMcount

if __name__=='__main__':
    seeds=[15,35,77,91,105,143,175,195,323,385,429,1001,1155,1365,2145,5005,4199,
           15015, 3927, 7469, 10659, 5187, 25025, 37961, 46189, 62491, 96577]
    print(f"{'a1':>8} {'Pa1':>4} {'terms':>5} {'#pr':>4} {'#ref':>4} {'#inc':>4} {'maxsz':>5} {'max|M|':>6} {'final|M|':>8} {'#enter':>6} {'maxenter':>8}")
    for a1 in seeds:
        a,Mn,pl,msz,mc=gen_sequence(a1,1500)
        nref=sum(1 for p in pl if p[3]=='refine')
        ninc=sum(1 for p in pl if p[3]=='incomp')
        allp=set()
        for _,_,s,_ in pl: allp|=s
        Pa1=factor(a1); entering=sorted(allp-set(Pa1))
        stable = len(pl)==0 or all(len(p[2])<=4 for p in pl)
        print(f"{a1:>8} {len(Pa1):>4} {len(a):>5} {len(pl):>4} {nref:>4} {ninc:>4} {msz:>5} {mc:>6} {len(Mn):>8} {len(entering):>6} {(max(entering) if entering else 0):>8}")
