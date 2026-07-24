# Lemma (per-prime gcd-of-valuations invariant) — CERTIFIED round 1

Core identity: for all nonnegative integers a,b (conventions gcd(x,0)=x, gcd(0,0)=0),
```
gcd(min(a,b), |a-b|) = gcd(a,b).
```
Proof: WLOG a≤b; gcd(a,b-a)=gcd(a,b) by subtractive Euclid (common divisors of {a,b} = common
divisors of {a,b-a}). Edge cases a=b (→gcd(a,0)=a) and a=0 (→gcd(0,b)=b) covered.

Consequence (lifted by associativity/commutativity of gcd over the board list): for every prime p,
```
g_p = gcd(v_p(x_1),…,v_p(x_N))
```
is invariant under every move. Hence the terminal single survivor M satisfies v_p(M)=g_p for all p,
i.e. M = ∏_p p^{g_p} = ∏_p p^{gcd_i v_p(x_i^init)}, depending only on the initial multiset.

Certified by proof-reviewer, round 1 (identity checked exhaustively for 0≤a,b<30; closed form
confirmed on 3000 random boards × 15 random move-orders).
Source: perprime-valuation §3 (Lemmas 3–4) / descent-induction §3.
