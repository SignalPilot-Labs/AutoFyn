import sys
from sim import gen

def test(a1, M):
    terms, rads = gen(a1, M)
    P1 = rads[0]
    channels = {}  # (frozenset G_i, frozenset G_j) -> set of external forced primes seen
    forced = set()
    multi_channel_primes = []
    for j in range(1, M):
        rj = rads[j]
        Gj = rj & P1
        for i in range(j):
            ri = rads[i]
            inter = ri & rj
            if len(inter) != 1:
                continue
            p = next(iter(inter))
            forced.add(p)
            if p in P1:
                continue
            Gi = ri & P1
            key = (frozenset(Gi), frozenset(Gj))
            channels.setdefault(key, set()).add(p)
    max_channel_size = 0
    bad = []
    for key, primes in channels.items():
        if len(primes) > max_channel_size:
            max_channel_size = len(primes)
        if len(primes) > 1:
            bad.append((key, primes))
    print(f"a1={a1}, M={M}: |P1|={len(P1)}, #external forced primes={len(forced - P1)}, "
          f"#channels used={len(channels)}, max primes sharing one channel={max_channel_size}")
    if bad:
        print("  channels with >1 external prime:", bad[:5])

if __name__ == "__main__":
    for a1, M in [(15,3000),(65,1500),(105,1500),(143,1500),(221,1500),(247,4000),
                  (375,1500),(4199,4000),(4087,4000),(91,1500),(1001,1500)]:
        test(a1, M)
