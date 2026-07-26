import sys, math
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import sieve_primes, prime_factors, rad, add_set_to_MT, prune_minimal

def greedy_mt_detail(a1, N, small_primes):
    a=[0]*N; a[0]=a1
    P0=prime_factors(a1,small_primes)
    MT=prune_minimal([{p} for p in P0])
    # track for each prime: first entry n, last entry n, number of times it LEAVES and RE-ENTERS
    prime_history={}  # p -> list of (n, 'in'/'out')
    prev_in=set()
    for p in P0:
        prime_history.setdefault(p,[]).append((0,'in'))
        prev_in.add(p)
    traj=[]  # (n, mpc, |MT|, sum1/q, set_of_mt_primes)
    def cur_mp():
        mp=set()
        for t in MT: mp|=set(t)
        return mp
    mp=cur_mp(); traj.append((0,len(MT),len(mp),sum(1/q for q in mp),frozenset(mp)))
    for step in range(1,N):
        prev=a[step-1]; m=prev+1
        while True:
            Pm=prime_factors(m,small_primes)
            if any(t<=Pm for t in MT): break
            m+=1
        a[step]=m
        MT=add_set_to_MT(MT, prime_factors(m,small_primes))
        mp=cur_mp()
        # record transitions
        for p in mp-prev_in:
            prime_history.setdefault(p,[]).append((step,'in'))
        for p in prev_in-mp:
            prime_history.setdefault(p,[]).append((step,'out'))
        prev_in=mp
        traj.append((step,len(MT),len(mp),sum(1/q for q in mp),frozenset(mp)))
    return a, traj, prime_history

sp=sieve_primes(2_000_000)
for a1 in [77, 847, 385, 175]:
    M1=rad(a1)
    N={77:120, 847:60000, 385:130000, 175:1200}[a1]
    a,traj,ph=greedy_mt_detail(a1,N,sp)
    # count re-entries: primes that leave and come back
    re_entered=[]
    for p,h in ph.items():
        states=[s for (_,s) in h]
        # count 'out' followed by 'in'
        re=0
        for i in range(len(states)-1):
            if states[i]=='out' and states[i+1]=='in': re+=1
        if re>0: re_entered.append((p,re,len(h)))
    # trajectory of mpc: show overshoot
    mpcs=[t[2] for t in traj]
    max_mpc=max(mpcs); final_mpc=mpcs[-1]
    print(f"a1={a1} M1={M1}: mpc trajectory: start={mpcs[0]} max={max_mpc} final={final_mpc}")
    print(f"  first 20 mpc: {mpcs[:20]}")
    print(f"  primes that LEFT then RE-ENTERED MT: {len(re_entered)}")
    if re_entered:
        print(f"  examples: {re_entered[:5]}")
    # is mpc non-decreasing overall? no. is it non-INCREASING? 
    ni=all(mpcs[i+1]<=mpcs[i] for i in range(len(mpcs)-1))
    print(f"  mpc non-increasing overall? {ni}")
    # number of distinct primes that EVER appear in MT
    all_primes=set(ph.keys())
    primes_gt_M1_ever=[p for p in all_primes if p>M1]
    print(f"  distinct primes EVER in MT: {len(all_primes)}; primes>M1 ever: {len(primes_gt_M1_ever)}; sample: {sorted(primes_gt_M1_ever)[:10]}")
    # final MT primes
    final_mp=traj[-1][4]
    print(f"  final MT primes: {sorted(final_mp)}")
    print()
