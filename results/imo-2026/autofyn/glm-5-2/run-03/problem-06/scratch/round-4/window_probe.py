import sympy
# Verify: when the greedy picks m with a prime q > M_1, m is the unique q-multiple in [a_n+1, a_n+M_1]
# Use LOCK cases (116) where big transients DO appear, to test the window-uniqueness on a real big-prime entry.
def fast_greedy_full(a1, N):
    a=[a1]; minimal=[frozenset(sympy.primefactors(a1))]
    M1 = sympy.prod(sorted(set(sympy.primefactors(a1))))
    events=[]
    for step in range(N-1):
        cur=a[-1]; m=cur+1
        while True:
            ms=frozenset(sympy.primefactors(m))
            if all(ms&S for S in minimal):
                a.append(m)
                if not any(S<=ms for S in minimal):
                    minimal=[S for S in minimal if not(ms<=S)]; minimal.append(ms)
                # check window-uniqueness for any big prime in ms
                for q in ms:
                    if q > M1:
                        # window [cur+1, cur+M1]; how many q-multiples?
                        lo = cur+1; hi = cur+M1
                        first = ((lo + q - 1)//q)*q
                        cnt = 0; x=first
                        while x <= hi: cnt += 1; x += q
                        events.append((step+2, q, m, cur, cnt, sorted(ms)))
                break
            m+=1
    return a, minimal, events, M1

a, minimal, events, M1 = fast_greedy_full(116, 400)
print(f"a1=116 (M1={M1}): big-prime-entry events:")
for ev in events[:20]:
    step, q, m, cur, cnt, ms = ev
    print(f"  step={step}: a_n={cur}, m={m}, q={q}, #q-multiples in window={cnt}, ms={ms}")
print(f"Total big-prime-entry events: {len(events)}")
