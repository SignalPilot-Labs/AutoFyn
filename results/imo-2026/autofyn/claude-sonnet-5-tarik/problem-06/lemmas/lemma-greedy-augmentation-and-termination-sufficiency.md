# Greedy Augmentation Lemma + Termination-Sufficiency Lemma

**Source.** `approaches/forced-primes-well-ordering.md`, §I, Steps 1–2 (round 10).

## Setup

Fix a doubly-infinite disjoint core pair `(S,S')` (the exact hypothesis of the
Stabilization Conjecture, per the already-certified
`theorem-SW-stabilization-sufficiency.md`). Write `B_0:=P_1\cup\{2,3,5,7,11,13\}`
(finite). For finite `W\supseteq B_0`, say `W` is **covering** for `(S,S')` if
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W\ne\varnothing` for every `i\in
I_S,j\in I_{S'}`. Covering-ness is monotone in `W`.

## The greedy process

`W_0:=B_0`. While `W_t` is not covering, let `U_t:=\{(i,j)\in I_S\times
I_{S'}:\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W_t=\varnothing\}\ne\varnothing`;
let `m_t:=\min\{\max(i,j):(i,j)\in U_t\}`, `(i_t,j_t)` the lexicographically-least
pair in `U_t` with `\max(i,j)=m_t`; `q_t:=\min\{q\text{ prime}: q\in\mathrm{rad}
(a_{i_t})\cap\mathrm{rad}(a_{j_t}),\,q\notin W_t\}`; `W_{t+1}:=W_t\cup\{q_t\}`. If
`W_T` is covering at some finite `T`, the process halts with output `W_T`.

## Greedy Augmentation Lemma — unconditional, fully proved

(a) `q_t` is always well-defined at a non-halted step. (b) `q_t\notin P_1` for every
`t`. (c) The `q_0,q_1,\dots` produced before halting are pairwise distinct, and
`W_t=B_0\cup\{q_0,\dots,q_{t-1}\}`.

**Proof.** (a) By the already-certified Lemma P′ (`gcd(a_i,a_j)>1` for every
`i\ne j`), `\mathrm{rad}(a_{i_t})\cap\mathrm{rad}(a_{j_t})\ne\varnothing`; since
`(i_t,j_t)\in U_t$, this intersection is disjoint from `W_t`, so the minimum
defining `q_t` is over a nonempty finite set of primes (bounded by `a_{i_t}`).
(b) `\mathrm{rad}(a_{i_t})\cap P_1=S(i_t)=S`, `\mathrm{rad}(a_{j_t})\cap P_1=S(j_t)=S'$
(Theorem CD's core map), and `S\cap S'=\varnothing`, so `\mathrm{rad}(a_{i_t})\cap
\mathrm{rad}(a_{j_t})\cap P_1=\varnothing`; `q_t$ lies in this intersection, hence
`q_t\notin P_1`. (c) Induction on `t`: `q_t\notin W_t=B_0\cup\{q_0,\dots,q_{t-1}\}$
by construction, so `q_t` is distinct from every earlier `q$. $\blacksquare$

## Termination-Sufficiency Lemma — unconditional, fully proved

**Statement.** If there is a finite `K_0` (depending only on `a_1,S,S'`, not on
`t`) with `q_t\in K_0` for every non-halted step `t`, then the process halts at
some `T\le|K_0|`, and `W_T\subseteq B_0\cup K_0` is a finite covering set: the
Stabilization Conjecture holds for `(S,S')`.

**Proof.** If the process ran `|K_0|+1` non-halted steps, `q_0,\dots,q_{|K_0|}`
would be `|K_0|+1` pairwise distinct elements (Greedy Augmentation Lemma (c)) all
lying in the size-`|K_0|` set `K_0` — impossible by pigeonhole. So the process
halts at some `T\le|K_0|`; by construction `W_T` is covering at halting, and
`W_T=B_0\cup\{q_0,\dots,q_{T-1}\}\subseteq B_0\cup K_0`. $\blacksquare$

**Effect.** Converts the Stabilization Conjecture for a fixed doubly-infinite pair
`(S,S')` into the single question: does a fixed finite `K_0` bound every prime the
greedy process could ever recruit? No such `K_0` is established in general this
round (see below); the reduction itself is unconditional.

## What is NOT established (open, honestly reported by the builder)

The literal candidate `K_0:=(S^+_S\setminus P_1)\cup(S^+_{S'}\setminus P_1)`
(intersection-based, from the already-certified `S^+` Necessity+Finiteness Lemma)
is **refuted**: on `a_1=21528751`, `(S,S')=(\{1061\},\{103,197\})`,
`S^+_{\{1061\}}=\{2,3,7,1061\}`, `S^+_{\{103,197\}}=\{103,197\}`, so
`K_0\subseteq B_0` identically (adds nothing), yet `B_0` alone is not covering
(misses bridge prime `97`, needed for 3 disjoint bucket-pairs realizing 94 of
13,181,000 cross-pairs at `N=3{,}000{,}000`). A replacement — the **First-`K`-Prefix
Recruitment Conjecture** (a union, not intersection, over the first `K` realized
members' companion sets on each side) is verified numerically on the same instance
(`K=5` gives a 16-prime covering `W`, zero violations across all 13,181,000 cross
pairs) but **not proved** in general.

## Certification

Certified `solved`-quality (sorry-free, unconditional): both the Greedy Augmentation
Lemma and the Termination-Sufficiency Lemma are pure well-ordering/pigeonhole
arguments with no gaps.

**Independently re-verified by the round-10 proof-reviewer** (fresh script, own
load and re-factorization of the `N=3{,}000{,}000` cache for `a_1=21528751`, not
reusing the builder's script): reproduced `|I_{\{1061\}}|=875`,
`|I_{\{103,197\}}|=15064`, `S^+_{\{1061\}}=\{2,3,7,1061\}`,
`S^+_{\{103,197\}}=\{103,197\}` exactly; reproduced the 3 disjoint `B_0`-bucket-pairs
and their 94 total cross-pairs exactly, and confirmed the shared prime is `97` in
all 94 cases; reproduced the `K=5` construction (`\mathrm{Comp}_5(\{1061\})=
\{2,3,5,7,11,23,47,97\}`, `\mathrm{Comp}_5(\{103,197\})=\{2,3,5,7,11,13,19,41,59,
71,97\}`, union of 16 primes) and its zero-violation check across all 13,181,000
cross pairs, bit-for-bit.

**Open, not to be treated as proved:** the First-`K`-Prefix Recruitment Conjecture
(equivalently: any finite `K_0` bounding the greedy process's recruits in general).
This is the sole remaining gap of this approach.
