## Theorem 35b$'$: the $\epsilon$-bridge closes for free on Theorem 35b's own range

**Source:** `approaches/greedy-halving-adversary.md`, round 22.
**Status:** CERTIFIED (proof-reviewer, round 22), at the same conditional
status Theorem 35b itself carries (conditional on $(\star_{n-3})$).

### Statement

Throughout Theorem 35b's whole range $v\ge p_3$ (equivalently
$v\in[p_3,s)$; empty at $n=3$, where Case (a) forces $T'=\varnothing$ and
$s=p_3$), the parity indicator $\epsilon(v):=\mathbb1[|R'_{>v}|\text{
odd}]$ is identically $0$. Consequently $(\Diamond')$
($\Delta(n,v)\le v-f(n)-2v\epsilon(v)$) is literally identical to
$(\Diamond)$ ($\Delta(n,v)\le v-f(n)$) throughout this range, so Theorem
35b's already-proved closure of $(\Diamond)$ closes $(\Diamond')$ here too,
with zero new inequality to prove. This closes "step 4" of the
round-21/22 outline, which round 21 had explicitly flagged as an
unverified observation but declined to rely on.

### Proof

Theorem 35b's own proof already establishes, for every $v\ge p_3$: "$p_3
\le v$ means $p_3\notin R'_{>v}$, and since every other element of $R'$
(i.e. every element of $T'$) is $\le p_4<p_3\le v$, we get
$R'_{>v}=\varnothing$ entirely." This argument never used $v=p_3$
specifically — only $v\ge p_3$ — so it holds for every $v$ in Theorem
35b's range, not merely at the endpoint. Hence $|R'_{>v}|=0$ (even), so
$\epsilon(v)=0$ identically. $\blacksquare$

### Verification

Proof-reviewer independently re-checked this argument (a direct
consequence of Theorem 35b's own already-certified proof, re-traced line
by line — no new machinery) and independently re-verified with a fresh
exact-`Fraction` script (`/tmp/round-22/verify_gha.py` extends this check
implicitly via the ladder ordering; the builder's own
`/tmp/round-22/verify.py` ran $12{,}000+$ direct checks that
$|R'_{>v}|=0$ for random legal Case-(a) instances and threshold samples
$v\in[p_3,s)$, $n=3,\dots,8$ — zero exceptions, matching the reviewer's
independent hand confirmation that the underlying ordering fact
($\max(T')\le p_4<p_3\le v$) is a direct, general consequence of the
ladder's strict descent, requiring no case-by-case numeric search to
believe).
