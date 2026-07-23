# Lemma 1 (uniform explicit gap bound)

**Statement.** With `(a_n)` as in the problem, let `L:=\mathrm{rad}(a_1)` (the
product of the distinct primes dividing `a_1`, equivalently `\mathrm{lcm}` of that
same prime set). Then for every `n\ge1`, `d_n:=a_{n+1}-a_n\le L`. Consequently
`a_n\le a_1+(n-1)L` for every `n\ge1` (linear growth, unconditionally, with no
assumption about which primes beyond `\mathrm{rad}(a_1)` are ever "recruited").

**Proof.** Fix `n\ge1`. Let `P_1=\{p_1,\dots,p_k\}=\mathrm{rad}(a_1)`, so
`L=p_1\cdots p_k`. Let `x_0` be the smallest multiple of `L` strictly greater than
`a_n`; since consecutive multiples of `L` are `L` apart, `a_n<x_0\le a_n+L`.

*Claim: `x_0` is an admissible candidate at step `n`, i.e. `\gcd(x_0,a_i)>1` for
every `i=1,\dots,n`.* Fix such an `i`.
- If `i=1`: some `p_j\in P_1` divides `a_1` (indeed every one does, by definition of
  `P_1`), and `p_j\mid L\mid x_0`, so `\gcd(x_0,a_1)\ge p_j>1`.
- If `2\le i\le n`: by Lemma P, `\gcd(a_i,a_1)>1`, so some prime `p_j` divides both
  `a_i` and `a_1`; since `p_j\mid a_1`, `p_j\in P_1`, hence `p_j\mid L\mid x_0`. So
  `p_j` divides both `x_0` and `a_i`, giving `\gcd(x_0,a_i)\ge p_j>1`.

So `x_0` satisfies the admissibility condition for every `i=1,\dots,n`. Since
`a_{n+1}` is by definition the *smallest* integer greater than `a_n` with this
property, `a_{n+1}\le x_0\le a_n+L`. Hence `d_n=a_{n+1}-a_n\le L`. $\blacksquare$

The consequence `a_n\le a_1+(n-1)L` follows by summing `d_1,\dots,d_{n-1}`.

**Source.** Proved in full in `approaches/bounded-gap-density-covering.md` ("Lemma 1
(uniform gap bound)", Step 2). Verified numerically by the round-1 proof-reviewer
against `a_1\in\{15,65,105,143,247\}` (max observed gap never exceeds
`\mathrm{rad}(a_1)`; e.g. `a_1=247=13\cdot19`, `\mathrm{rad}=247`, observed max gap
`78\le247` over 400 terms) — a sanity check only, not part of the proof, which is
self-contained and needs only Lemma P.

**Certification.** Depends only on Lemma P (certified separately) and the definition
of `L`; no gaps. Certified `solved`-quality (sorry-free) by the round-1 proof-reviewer.

**Important cross-approach consequence (new observation by the round-1 reviewer, not
in the original build).** Combined with the Domination Lemma (also certified in this
folder), Lemma 1 fully resolves gap (a) flagged in `backbone-existence-crt.md`
Section 5: since `a_{n+1}\le a_1+nL=O(n)`, we get `\log_2 a_{n+1}=O(\log n)`, so the
Domination Lemma's bound `\max_j D_n(q_j)\ge n/\log_2 a_{n+1}` gives
`\max_j D_n(q_j)\to\infty` as `n\to\infty` — i.e. the dominant prime at step `n`
provably divides an unboundedly *growing number* of earlier terms, unconditionally
(no need to separately establish a growth bound on `a_n`, since Lemma 1 already
supplies one). This was numerically confirmed by the reviewer (e.g. for `a_1=247`,
`n/\log_2(a_{n+1})` grows from `\approx1.1` at `n=10` to `\approx126` at `n=1999`).
This still leaves gap (b) (concentration of dominance onto only *finitely many*
distinct primes across all `n`) as the sole remaining open content of "backbone
finiteness" — gap (a) alone is now closed by combining these two already-certified
lemmas.
