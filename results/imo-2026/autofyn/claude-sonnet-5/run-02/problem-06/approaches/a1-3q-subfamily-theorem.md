## Status
solved (round 22: the open gap — Case (b), `n` even, `k≥1` — is closed. See
"Round 22 build: closure of the open gap" and "Full proof" below.)

## Approaches tried
- (round 20, first build) Self-contained strong induction generalizing
  `prime-power-seed-literal-periodicity-theorem.md` from `|Q|=1` to `|Q|=2`
  for `a_1=3q`. Fully closed: the base structure (illegality of `a_n+1`,
  legality of `a_n+3`, illegality of `a_n+2` in "Case (a)" `q∤(a_n+2)`), a
  new clean **parity witness** that resolves "Case (b)" (`q|(a_n+2)`)
  completely whenever `n` is **odd**, and a fully rigorous closed-form
  analysis of the very first Case-(b) occurrence (`n=n0`, the "`k=0`" term)
  that pins down **exactly** `q=7` and `q=11` as the only primes where that
  first occurrence is even at risk, verifies both by hand, and gives a
  clean, provable, non-numeric explanation of why `q=5` is genuinely
  excluded (the same mechanism, but for `q=5` the witness search provably
  has only one candidate and it fails). Outcome: **real, unconditional
  progress**, but the general case "Case (b), `n` even, `k≥1`" is NOT
  closed — see Current best / open gap below. Explored (and rejected as
  insufficient) three witness mechanisms: `a_2` alone (refuted by
  outline-reviewer, parity coincidence), fixed pair `{a_2,a_3}` (refuted,
  12 counterexamples), and a naive full-period pigeonhole bound using
  `rad(a_n+2)` as the required window (proved WAY too weak: a deliberately
  adversarial `(q,n)` constructed via CRT so that `a_n+2` is divisible by
  11 distinct primes, giving `rad(a_n+2) ≈ 1.16×10^13`, nonetheless has an
  ACTUAL witness at index `i=9` — showing the true required window is far
  smaller than the naive bound, but I could not prove *why*, elementarily,
  in general).
- (round 21, second build) Attempted to close Case (b), `n` even, `k≥1` via
  the round-21 outline's crude-Jacobsthal-bound strategy. Formalized and
  confirmed the outline-reviewer's Step-4 uniformity fix (conditional on
  Step 1); found the natural AP-based repair to the broken two-halves
  induction only reproduces the already-insufficient radical bound (dead
  end, precisely diagnosed); **definitively refuted**, via an explicit
  verified CRT construction (`q=40153,k=3335,K=2·5·7·11·13=10010`, minimal
  witness offset exactly `10`), the natural fallback idea that a small fixed
  window independent of `q,k` always suffices. Step 1 (the crude bound
  itself) remains unproved elementarily. Outcome: real negative progress,
  gap not closed, Status stays `partial`.
- (round 22, third build) Attempted Option (a) of the round-22 outline (the
  Chebyshev/primorial-chain sieve). Found a genuinely simpler route than the
  outline anticipated: a direct Legendre/inclusion-exclusion sieve estimate
  (`legendre-sieve-gap-bound.md`) replaces the broken/insufficient
  "two-halves induction" entirely (Step 1), and a one-line "primes grow at
  least linearly with their index" argument (`primorial-floor-bound.md`)
  replaces the heavier Chebyshev-binomial-coefficient machinery the outline
  expected to need (Steps 2–3). Combined with an explicit finite check for
  the residual small-`k` band (`k∈{1,2,3,4,7,8,9,10,11}`, uniform across all
  `q`), this **closes Case (b), `n` even, `k≥1`, completely and
  elementarily**. Outcome: the gap is closed; the full `a_1=3q` theorem
  (literal `T=1,L=3` periodicity for every `n≥1`) is now proved
  unconditionally for every prime `q≥7,q≠5`. See "Round 22 build" and "Full
  proof" below.

## Current best

### What is fully proved (unconditionally, for every prime `q ≥ 7`, `q ≠ 5`)

Fix `q` prime, `q ≥ 7`, `q ≠ 5`, `a_1 = 3q`. Strong induction hypothesis at
step `n`: `a_i = 3q+3(i-1) = 3(q+i-1)` for every `i = 1,…,n` (so `3 | a_i`
for every such `i`, and `P(a_1) = \{3,q\}` since `q` is a prime `\neq 3`).

**(0) Base case** `n=1`: `a_1 = 3q` by definition of the sequence, matching
`3q+3(1-1)`.

**(1) Illegality of `a_n+1`.** `a_n` and `a_n+1` are consecutive integers,
hence coprime (`gcd(x,x+1)=1` for every integer `x`); in particular
`gcd(a_n+1,a_1)=1`, so `a_n+1` fails the `i=1` legality check — illegal.

**(2) `3 ∤ (a_n+2)`.** Since `3 | a_n` (induction hypothesis), `a_n+2 ≡ 2
\pmod 3`.

**(3) Illegality of `a_n+2`, Case (a): `q ∤ (a_n+2)`.** Any common divisor of
`a_n+2` and `a_1=3q` divides `3q`, hence (as `3,q` are the only prime
factors of `a_1`) is built from `\{3,q\}`. By (2), `3` does not divide
`a_n+2`; by the Case-(a) hypothesis neither does `q`. So `\gcd(a_n+2,a_1)=1`
— illegal via `i=1`.

**(4) Illegality of `a_n+2`, Case (b), sub-case `n` odd.** This is the new
mechanism found this round; it covers Case (b) (`q | (a_n+2)`) completely
for **odd** `n`, with **no case split on `q`, on `k`, or on the size of
anything** — a single clean argument. Set `N := a_n+2 = 3q+3n-1`. By the
induction hypothesis, `a_n = N-2`. Directly, `\gcd(N,a_n) = \gcd(N,N-2) =
\gcd(N,2)` (a standard consequence of `\gcd(x,y)=\gcd(x,x-y)`, applied with
`x=N,\ y=a_n`, giving `\gcd(N,a_n) = \gcd(N, N-a_n) = \gcd(N,2)`). Now,
`N=3q+3n-1 = 3(q+n)-1`; since `3(q+n)` and `q+n` have the same parity, `N`
is **odd** iff `q+n` is **even**, i.e. (as `q` is an odd prime, `q\ge 7`)
iff `n` is **odd**. So: whenever `n` is odd, `N` is odd, so `\gcd(N,2)=1`,
so `\gcd(N,a_n)=1` — i.e. `a_n+2` is illegal, witnessed by `i=n` (which is
always a valid index, `1\le i=n\le n`, and `a_n` is already fixed by the
induction hypothesis). This argument uses only the induction hypothesis and
basic gcd identities — no reference to `q,K` factorizations, no case split,
and applies regardless of whether we are in Case (a) or Case (b) (it simply
subsumes Case (a) too, when `n` is odd; Case (a) is handled separately in
(3) anyway since it needs no parity restriction).

**(5) Illegality of `a_n+2`, Case (b), sub-case `n` even, restricted to
`k=0` (the very first Case-(b) occurrence for each `q`).** Case (b) means
`q | (3n-1)` (since `a_n+2 \equiv 3n-1 \pmod q`, using `a_1=3q\equiv0`).
Because `\gcd(3,q)=1` (as `q\neq3`), `3` is invertible mod `q`, so the set
of `n` with `q|(3n-1)` is exactly one residue class mod `q`; let `n_0\in
\{1,\dots,q-1\}` be its least positive representative (`n_0\ge1` since
`3\cdot0-1=-1\not\equiv0`), so all Case-(b) indices are `n = n_0+kq`,
`k=0,1,2,\dots`.

  - *Exact value of `n_0` and `K_0 := (a_{n_0}+2)/q`.* Since `n_0\in
    \{1,\dots,q-1\}`, `3n_0-1 \in \{2,\dots,3q-4\}`, and `q | (3n_0-1)`
    forces `3n_0-1 \in \{q,2q\}` (the only multiples of `q` in that range,
    as `3q-4<3q`), i.e. `s_0:=(3n_0-1)/q \in \{1,2\}`. Concretely: if
    `q\equiv2\pmod3` then `s_0=1`, `n_0=(q+1)/3`; if `q\equiv1\pmod3` then
    `s_0=2`, `n_0=(2q+1)/3` (direct check: `3\cdot\frac{q+1}3-1=q` needs
    `3|(q+1)`, i.e. `q\equiv2\pmod3`; `3\cdot\frac{2q+1}3-1=2q` needs
    `3|(2q+1)`, i.e. `q\equiv1\pmod3` — these are the only two residues, as
    `q\neq3`). Writing `K_0 := 3+s_0`, we get `K_0=4` (`q\equiv2\pmod3`) or
    `K_0=5` (`q\equiv1\pmod3`), and `a_{n_0}+2 = q\cdot K_0`.
  - *Sufficient-window criterion.* For a general Case-(b) index `n` with
    `K:=(a_n+2)/q`, the candidates `a_2,\dots,a_n` give `m:=q+i-1` ranging
    over the `n-1` consecutive integers `q+1,\dots,q+n-1`. If `n-1\ge q-1`
    is false (i.e. the window is short, `n\le q-1`) then **every** `m` in
    the window satisfies `q\nmid m` automatically (as `0<m-q<q`), so for
    such `n`, `\gcd(a_n+2,a_i)=\gcd(N,3(q+i-1))=\gcd(N,q+i-1)`
    (`3\nmid N`) `=\gcd(K,q+i-1)` (since `\gcd(q+i-1,q)=1` removes the
    common factor `q` of `N=qK` cleanly: if `d\mid(q+i-1)` and `d\mid qK`
    then, as `\gcd(d,q)\mid\gcd(q+i-1,q)=1`, `d\mid K`, and conversely
    `\gcd(K,q+i-1)\mid \gcd(qK,q+i-1)`; so the two gcds coincide). If in
    addition `n-1\ge K`, the `n-1\ge K` consecutive integers
    `q+1,\dots,q+n-1` contain a full residue system mod `K`
    (any `K` consecutive integers hit every residue mod `K` exactly once),
    hence contain at least one of the `\phi(K)\ge1` residues coprime to
    `K` — giving a witness `i`. So: **whenever `n\le q-1` and `n-1\ge K`,
    a witness exists** (this is an elementary, fully rigorous argument,
    no case split on primes of `K` needed).
  - *At `k=0`, this criterion needs `n_0 - 1 \ge K_0`.* Substituting the
    explicit `n_0,K_0` above: `q\equiv2\pmod3\Rightarrow n_0-1=(q+1)/3-1=
    (q-2)/3`, need `(q-2)/3\ge4\Leftrightarrow q\ge14`, i.e. (as
    `q\equiv2\pmod3` prime, `q\ge7`) `q\ge17`. So `q=11` (the only prime
    `\equiv2\pmod3` in `[7,14)`) is the sole possible exception in this
    residue class. `q\equiv1\pmod3\Rightarrow n_0-1=(2q+1)/3-1=(2q-2)/3`,
    need `(2q-2)/3\ge5\Leftrightarrow q\ge8.5`, i.e. `q\ge10`, so (as
    `q\equiv1\pmod3` prime, `q\ge7`) `q=7` is the sole possible exception
    (next candidate is `q=13\ge10`, fine).
  - *Direct resolution of the two exceptions.* `q=7,n_0=5`:
    `a_5+2=3\cdot7+3\cdot5-1=35=7\cdot5`, `K_0=5`. Candidates `i=2,3,4,5`
    give `m=8,9,10,11`; `\gcd(5,8)=1` — witness `i=2`. `q=11,n_0=4`:
    `a_4+2=3\cdot11+3\cdot4-1=44=11\cdot4`, `K_0=4`. Candidates `i=2,3,4`
    give `m=12,13,14`; `\gcd(4,13)=1` — witness `i=3`. Both directly
    verified.
  - *For `k\ge1` (i.e. `n=n_0+kq`, `k\ge1`), the sufficient-window
    criterion's SECOND half (`n-1\ge K`) always holds, uniformly in `q`.*
    Here `n=n_0+kq\ge q+1>q-1`, so the FIRST half of the criterion (window
    entirely below `2q`) may fail — but a direct comparison shows it is
    unnecessary: `K = (a_n+2)/q = 3+(3n-1)/q = 3+s_0+3k = K_0+3k\ge K_0+3
    \ge7`. And `n-1 = [q(K-3)+1]/3 - 1` (from `3n=q(K-3)+1`, i.e.
    `n=[q(K-3)+1]/3`, obtained by substituting `a_n+2=3q+3n-1=qK`); solving
    `n-1<K` gives (dividing by `q-3>0`) `K\le(3q-1)/(q-3)=3+8/(q-3)\le
    3+8/4=5` (as `q\ge7\Rightarrow q-3\ge4`). Since `K\ge7>5` whenever
    `k\ge1`, the inequality `n-1<K` is **never** satisfied for `k\ge1`,
    i.e. `n-1\ge K` always holds. This handles the "`q\nmid m`" concern
    too: since we no longer need the window confined below `2q`, we must
    re-derive coprimality to `q` directly. (**This is exactly where the
    proof is incomplete — see the open gap below: I have NOT closed the
    `q|m` complication for `k\ge1`, `n` even.**)

### OPEN GAP (honestly unresolved)

For Case (b) with **`n` even** and **`k\ge1`** (i.e. every Case-(b)
occurrence past the very first one for each `q`, when `n` is even), the
argument above shows the *quantity* `n-1` needed for a naive "`K`
consecutive integers" pigeonhole is available, but:

1. The window `q+1,\dots,q+n-1` used for that pigeonhole is no longer
   automatically free of multiples of `q` (since `n-1` can now exceed `q`),
   so a witness `m` found via "coprime to `K`" is not automatically
   coprime to `q` too, and the correct test is `\gcd(m, qK)=1`
   (equivalently `m` coprime to **both** `q` and `K`), not merely
   `\gcd(m,K)=1`.
2. A literal full-period pigeonhole for `\gcd(m,qK)=1` needs a window of
   length `\ge \mathrm{rad}(qK)`, which can be as large as `q\cdot K`
   itself (when `K` is squarefree with all prime factors `\neq q`) — and
   `q\cdot K` is **larger** than the actually-available window `n-1\approx
   qK/3`. So the naive pigeonhole genuinely fails to close this case; a
   finer bound is needed.
3. I attempted to test whether the true minimal witness index nonetheless
   stays uniformly bounded (independent of how composite `K` is) by
   deliberately constructing, via CRT, a prime `q=11` and an index `n`
   with `a_n+2` divisible by **11 distinct primes**
   `\{2,5,7,11,13,17,23,29,41,47,53\}` simultaneously (so
   `\mathrm{rad}(a_n+2)\approx1.16\times10^{13}`). The *actual* minimal
   witness (found by exhaustive search over `i=2,\dots,n` against the
   TRUE value `a_n+2`, no shortcuts) was still just `i=9` — far smaller
   than the naive pigeonhole bound would suggest, and consistent with the
   outline-reviewer's finding that observed witness indices stay small.
   This is strong evidence that a genuine (much sharper) gap-existence
   theorem is true here, in the spirit of Jacobsthal's function
   (`g(m)`, the maximal gap between consecutive integers coprime to `m`,
   known to be far smaller than `\mathrm{rad}(m)` — e.g.
   `g(m)=O(\omega(m)^2(\log\omega(m))^2)` unconditionally, by Iwaniec-type
   results), but I was **not able to prove**, from scratch and
   elementarily, a bound of this shape (or any sufficient substitute)
   within the scope of this round. This is a genuinely deep fact, not a
   routine olympiad pigeonhole, and I do not consider it established here.
4. I explicitly checked (per the reviewer's instruction) whether a fixed,
   uniformly bounded window (e.g. `i\in\{2,\dots,6\}`, independent of `q`
   and `k`) could be proven to suffice for `n` even, `k\ge1` — I could not
   prove this, and the adversarial construction above is evidence (though
   not a disproof, since a witness at `i=9` was still found — a bounded
   window may in fact exist, just not one I could pin down and prove
   correct within the available time) that even if true, its proof is not
   a simple parity/window trick like the ones that closed cases (3)-(5)
   above.

**This gap is now CLOSED — see "Round 22 build: closure of the open gap"
below.** The paragraphs immediately below (through "Honest summary of the
gap") are kept verbatim as the round-20/21 historical record of the gap
before closure; they are superseded by the round-22 closure, not retracted
(the diagnosis of *why* the gap was hard is still accurate and is exactly
what the round-22 closure resolves).

**Honest summary of the gap (historical, round 20/21):** the theorem "`a_1=3q` (prime `q\ge7,
q\neq5`) gives literal `T=1,L=3` periodicity for all `n`" remains, in this
approach, proved **unconditionally for**: `n=1`; every `n` with Case (a)
(`q\nmid(a_n+2)`); every **odd** `n` in Case (b); and every `n` in Case (b)
with `k=0` (i.e. the very first Case-(b) occurrence for the given `q`) —
**for every prime `q\ge7,q\neq5`**. The remaining open case is Case (b)
with `n` even and `k\ge1`. Numerically this case is fully consistent with
the conjectured periodicity (see the outline-reviewer's exhaustive
simulation, and my own spot checks including the adversarial CRT
construction above), but I have not closed it with a rigorous elementary
proof.

## Round 22 build: closure of the open gap

**Summary: the gap is CLOSED.** Case (b), `n` even, `k≥1` is now proved for
every prime `q≥7, q≠5`, completing the `a_1=3q` theorem unconditionally.
The route taken is Option (a) of the round-22 outline (a real elementary
sieve argument), but via a **simpler mechanism than the outline anticipated**
— a direct Legendre/inclusion-exclusion sieve estimate plus a one-line
prime-growth bound, in place of the Chebyshev-binomial-coefficient chain the
outline expected to need.

### (A) Two new elementary lemmas

**Lemma A (Legendre Sieve Gap Bound).** For integer `M≥2` with `r:=ω(M)`,
any window of `L` consecutive integers with `L ≥ 2^r(r+1)` contains an
integer coprime to `M`. Proved in full from scratch via the Legendre/
inclusion-exclusion sieve identity `S = L·∏_{p|M}(1-1/p) + E`, `|E|<2^r`,
combined with the elementary telescoping bound `∏_{i=1}^r(1-1/p_i) ≥
∏_{i=1}^r i/(i+1) = 1/(r+1)` (using only that the `i`-th smallest prime
factor `p_i ≥ i+1`, itself immediate from "a strictly increasing sequence of
integers starting at `≥2` has `i`-th term `≥i+1`"). Full proof, and an
independent numerical sanity check against known Jacobsthal-function values
(`g(30030)=22≤448`, etc.), certified as **`lemmas/legendre-sieve-gap-bound.md`**.
This *replaces* the round-20/21 "two-halves induction" (which had the
`M=6`-collision gap) entirely — it is a direct counting argument, not an
induction, so that failure mode does not arise.

**Lemma B (Primorial Floor Bound).** If `ω(M)=r` then `M≥(r+1)!`. Proved in
one line from the same `p_i≥i+1` fact used in Lemma A. A corollary (proved by
an explicit induction, base case `s=4` checked directly, inductive step a
two-line algebraic estimate using `(s+2)^2≥2(s+3)` for `s≥1`) gives: for
`s≥4`, `(s+1)! ≥ (3/7)2^{s+1}(s+2)+5`. Certified as
**`lemmas/primorial-floor-bound.md`**. This is a much lighter substitute for
the round-21-outline's planned Chebyshev/binomial-coefficient chain — it
needs no prime-counting estimate at all, only that primes listed in
increasing order grow by at least `1` each step.

### (B) Applying the lemmas to close Case (b), `n` even, `k≥1`

Fix prime `q≥7,q≠5`, and a Case-(b) index `n=n_0+kq` (`k≥1`, `n` even), with
`K:=(a_n+2)/q = K_0+3k` (`K_0∈\{4,5\}` per branch of `q\bmod3`, from item (5)
above). Write `N:=a_n+2=qK`. The available witness window is
`m=q+1,\dots,q+n-1`, i.e. `L:=n-1` consecutive integers; a value `m` in this
window with `\gcd(m,qK)=1` gives a witness `i=m-q+1\in\{2,\dots,n\}`, since
(as already established: `3\nmid N`, so `\gcd(N,a_i)=\gcd(N,3(q+i-1))=
\gcd(N,q+i-1)=\gcd(qK,m)`). So it suffices to find `m` coprime to `M:=qK` in
this window.

**Case `s:=ω(K)≥4`.** By Lemma B's corollary, `K≥(s+1)!≥(3/7)2^{s+1}(s+2)+5`.
Since `K=K_0+3k≤3k+5` (as `K_0≤5`), this gives `3k≥K-5≥(3/7)2^{s+1}(s+2)`,
i.e. `7k≥2^{s+1}(s+2)`. Since `r:=ω(qK)≤ω(K)+1=s+1` (adjoining one prime `q`
adds at most one new distinct prime factor) and `2^r(r+1)` is increasing in
`r`, `2^r(r+1)≤2^{s+1}(s+2)≤7k`. And `L=n-1=n_0-1+kq≥kq≥7k` (as `n_0≥1`,
`q≥7`). So `L≥7k≥2^r(r+1)`: Lemma A applies directly, giving a witness. This
holds for **every** `k≥1` for which `ω(K)≥4` happens to occur — no upper
bound on `k` is needed; the argument is entirely driven by `K`'s size via
Lemma B, not by an a priori restriction to "large `k`".

**Case `s=ω(K)≤3`.** Then `r=ω(qK)≤4`, so `2^r(r+1)≤2^4\cdot5=80`. If
`k≥12`, `L≥7k≥84≥80≥2^r(r+1)`: Lemma A applies directly. This leaves only
`k\in\{1,2,\dots,11\}` needing separate treatment — but Lemma B already
guarantees `ω(K)≤3` is automatic for all such `k` in any case (since for
`k≤38`, `K=K_0+3k≤119<120=5!`, so `s=ω(K)≥4` is impossible by Lemma B — the
case split above is exhaustive), so the residual band to check directly is
exactly `k\in\{1,\dots,11\}`.

**Residual band `k\in\{1,\dots,11\}`: exact finite verification.** For each
of these `k` values, `K=K_0+3k` is a *specific, small, fixed* integer
(independent of `q`!), so `\omega(K)` can be computed exactly rather than
merely bounded. Tabulating `K,\omega(K)` for `k\in\{1,2,3,4,7,8,9,10,11\}`
and both branches `K_0\in\{4,5\}` (18 cases; `k=5,6` are not in this list —
see below):

| `k` | `K_0=4`: `K,\omega(K)` | `K_0=5`: `K,\omega(K)` |
|---|---|---|
| 1 | `7,\ \omega=1` | `8,\ \omega=1` |
| 2 | `10,\ \omega=2` | `11,\ \omega=1` |
| 3 | `13,\ \omega=1` | `14,\ \omega=2` |
| 4 | `16,\ \omega=1` | `17,\ \omega=1` |
| 7 | `25,\ \omega=1` | `26,\ \omega=2` |
| 8 | `28,\ \omega=2` | `29,\ \omega=1` |
| 9 | `31,\ \omega=1` | `32,\ \omega=1` |
| 10 | `34,\ \omega=2` | `35,\ \omega=2` |
| 11 | `37,\ \omega=1` | `38,\ \omega=2` |

In every one of these 18 cases, `\omega(K)\le2`, so the *generic* bound
(`q\nmid K`, giving `r=\omega(K)+1\le3`) is `2^r(r+1)\le2^3\cdot4=32`. Since
`L(q):=n-1=kq+n_0(q)-1` is an explicit **strictly increasing affine function
of `q`** (for `K_0=4`: `L(q)=q(k+\tfrac13)+\tfrac13-1`; for `K_0=5`:
`L(q)=q(k+\tfrac23)+\tfrac13-1`; both have strictly positive slope since
`k\ge1`), solving `L(q)\ge32` (or `\ge12` when `\omega(K)=1`, generic
`r\le2`) for `q` gives an **explicit threshold `q_{\mathrm{thresh}}`** past
which every larger valid prime `q` in the branch automatically satisfies the
generic bound, by monotonicity — and crucially, using the *generic* (largest
possible) `r=\omega(K)+1` as the threshold is safe regardless of whether the
particular `q` happens to divide `K` (dividing `K` only *decreases* the
actual `r`, hence only *decreases* the actual required bound below the
generic one). Computing `q_{\mathrm{thresh}}` explicitly for all 18 cases
(verified by direct computation) gives `q_{\mathrm{thresh}}<15` in every
single case. Since the smallest admissible `q` in either branch is `q=7`
(`K_0=5`) or `q=11` (`K_0=4`), **at most the first one or two primes in each
branch can possibly fall below `q_{\mathrm{thresh}}`**, and direct
enumeration finds only three (`k,K_0,q`) instances with `q<q_{\mathrm{thresh}}`:

- `k=1,K_0=5,q=7` (`q_{\mathrm{thresh}}=7.6`): `n=12`, `L=11`,
  `M=qK=7\cdot8=56=2^3\cdot7`, exact `r=\omega(56)=2`, exact bound
  `2^2\cdot3=12>11=L` — Lemma A's sufficient condition genuinely fails here.
  **Direct witness:** `a_3=3(7+2)=27=3^3`; `\gcd(56,27)=1`. So `i=3` is a
  valid witness (`2\le3\le12`), confirmed directly (not via Lemma A).
- `k=2,K_0=4,q=11` (`q_{\mathrm{thresh}}=14.0`): `n=26`, `L=25`,
  `M=qK=11\cdot10=110=2\cdot5\cdot11`, exact `r=\omega(110)=3`, exact bound
  `2^3\cdot4=32>25=L` — again Lemma A's sufficient condition fails.
  **Direct witness:** `a_3=3(11+2)=39=3\cdot13`; `\gcd(110,39)=1`. So `i=3`
  is a valid witness, confirmed directly.
- `k=3,K_0=5,q=7` (`q_{\mathrm{thresh}}=8.91`): `n=26`, `L=25`,
  `M=qK=7\cdot14=98=2\cdot7^2`. Here `q=7` **divides** `K=14`, so the exact
  `r=\omega(98)=2` (not the generic `3`), giving exact bound `2^2\cdot3=12\le
  25=L`: Lemma A **applies directly** here (this is a case where `q|K`
  strictly helps, as noted above), no separate witness needed.

For **every other** `(k,K_0)` pair among the 18, `q_{\mathrm{thresh}}` is
below the smallest admissible `q` in that branch (`7` or `11`), so Lemma A
applies directly at the smallest `q` and, by the proven monotonicity of
`L(q)`, at every larger admissible `q` in the branch too — no exceptions.

For `k=5,6`: `K\le23<24=4!`, so `\omega(K)\le2` by Lemma B (regardless of
branch), giving `r\le3`, bound `\le32\le35=7\cdot5\le L`: Lemma A applies
directly via the same generic argument used for `k\ge12`, no per-case table
entry needed.

**Conclusion:** across every `k\ge1`, every branch `K_0\in\{4,5\}`, and every
admissible prime `q\ge7,q\ne5`, a witness for the illegality of `a_n+2`
exists — either via Lemma A directly, or (in exactly the two cases
`(k,K_0,q)=(1,5,7)` and `(2,4,11)`) via the explicit witness `i=3`, verified
directly above. This closes Case (b), `n` even, `k\ge1`, completely.

### (C) Independent numerical confirmation

Re-simulated the true greedy sequence from scratch (correct legality rule:
`a_{n+1}` is the least integer `>a_n` with `\gcd(a_{n+1},a_i)>1` for
**every** `i\le n`) for `a_1=3q`, `q\in\{7,11,13,17,19,23,29,31,37,41,43,47\}`,
`800` terms each: **zero mismatches** against the predicted closed form
`a_n=3(q+n-1)` in all `9{,}600` checked terms, including at the two
hand-resolved exceptional indices `n=12` (`q=7`) and `n=26` (`q=11`) found
above (both are within the 800-term simulation window and match exactly).

### Exclusion of `q=5`: precise, proved mechanism

`q=5\equiv2\pmod3`, so by the `K_0` formula in (5), `n_0=(5+1)/3=2`,
`s_0=1`, `K_0=4`, and `a_2+2 = 3\cdot5+3\cdot2-1 = 20 = 5\cdot4`. The
window of available witness candidates at this step is `i=2,\dots,n_0=2`,
i.e. **only the single candidate `i=2`**, `m=q+1=6`. Directly:
`\gcd(a_2+2,a_1)=\gcd(20,15)=5>1` (Case (b): `q=5` divides `20`, so `i=1`
is not a witness) and `\gcd(a_2+2,a_2)=\gcd(20,18)=2>1` (the only other
available index, `i=2`, also fails: `\gcd(K_0,m)=\gcd(4,6)=2\neq1`). So
**no** `i\in\{1,2\}` witnesses the illegality of `a_2+2=20`: for every
`i=1,2`, `\gcd(20,a_i)>1`. Hence `20` **is** legal at this step (it also
needs `20>a_2=18`, true), and since `19` is illegal (`\gcd(19,15)=1`,
`i=1`), and `20` is legal, minimality forces `a_3=20`, matching the
directly-simulated true sequence `15,18,20,24,\dots` and **breaking** the
conjectured `3+3(n-1)` pattern at `n=3` (predicted `21`, actual `20`).
This is exactly the boundary/degenerate instance of the general `k=0`
analysis in (5) — the only difference between `q=5` and `q=7,11` is that
for `q=5` the witness window at `n_0` genuinely has size `1` and its only
candidate fails, whereas for `q=7,11` the window (sizes `4` and `3`
respectively) has enough candidates that one succeeds. This gives a
complete, non-numeric, mechanism-level proof of why `q=5` is excluded (not
merely an empirical observation).

## Round 21 build: attempted closure, honest result — gap NOT closed

**Summary of outcome:** Status remains `partial`. I confirmed and formalized
the outline-reviewer's Step 4 fix (the uniformity concern is a non-issue,
conditional on Step 1), but Step 1 itself — an elementary, from-scratch proof
of a crude Jacobsthal-type bound `g(M) ≤ f(ω(M))` with `f` sub-linear — resists
proof, and I found a **new, decisive, fully-verified numerical construction**
that kills the natural fallback idea (a fixed, `q`-independent bounded window
of small constant size) outright, so there is no way to route around Step 1's
difficulty. This is real, precise negative progress: it forecloses an entire
alternative strategy for future rounds, in addition to the outline-reviewer's
earlier finding that the naive two-halves induction is broken.

### (A) Step 4 (uniformity), formalized and confirmed correct — CONDITIONAL on Step 1

Restating precisely, since the outline-reviewer's finding was correct but
informal: for `n = n_0+kq` (`k ≥ 1`), the available witness window has length
`n-1 = n_0-1+kq ≥ kq ≥ 7k` (using `q ≥ 7`). Write `K := K_0+3k`
(`K_0 ∈ {4,5}` per the branch of `q mod 3`, established in item (5) above).
**Claim (conditional):** if some crude bound of the shape `g(M) ≤ 2^{ω(M)+1}`
holds for the modulus `M := qK` (or the sharper `M:=K` when `q|K` can be
excluded — see the sub-case note below), then the required inequality for a
witness to exist is exactly `7k ≥ 2^{ω(qK)+1}`, and since `ω(qK) ≤ ω(K)+1`
always (adding at most one new prime `q`), it suffices to check
`7k ≥ 2^{ω(K)+2}`. This expression depends on `q` **only through which of the
two residue classes** `q` falls in mod 3 (fixing `K_0∈\{4,5\}`), **not on the
numerical size of `q`** — so a single finite check (over `k=1,\dots,k^*` for
each of the two `K_0` values) plus one tail argument (`ω(K)` grows strictly
slower than `k` — see (B) below — so `2^{ω(K)+2}` is eventually beaten by
`7k`) closes this inequality **simultaneously for every prime `q ≥ 7, q\neq5`**.
I directly verified the finite part by exhaustive computation: for
`K_0=4`, the inequality `7k ≥ 2^{ω(K)+2}` fails only at `k=1,2` (`K=7,10`);
for `K_0=5`, it fails only at `k=1` (`K=8`); it holds for all `k` up to `80`
checked (well past where the asymptotic argument in (B) kicks in) for both
branches. **This confirms the outline-reviewer's Step-4 finding in full and
gives it a precise, checkable form.** However, this entire claim is
CONDITIONAL on Step 1 (the crude bound itself), which is not established —
see (C).

*Sub-case note (Step 2 of the outline, resolved trivially):* whether `q|K` or
not, `ω(qK) \le ω(K)+1` always holds (a prime divides `qK` iff it divides `q`
or `K`, at most one more prime than `ω(K)`), so the bound `7k\ge2^{ω(K)+2}`
above is safe (slightly generous) regardless of which sub-case occurs — no
separate case split is actually needed here, contrary to the outline's Step 2
concern.

### (B) The asymptotic comparison (`ω(K)` grows slower than `k`) — genuinely elementary, and correct as far as it goes

`K = K_0+3k \le 3k+5`. Since each new distinct prime factor requires
multiplying by a further factor `\ge 2`, `2^{ω(K)}\le K` trivially (elementary,
no advanced input) — this alone is NOT enough (checked directly: `2^{ω(K)+2}
\le 4K \le 4(3k+5) = 12k+20`, and `12k+20` is NOT `\le 7k` for any `k>0`, so
this trivial bound is too weak, confirming the file's own earlier diagnosis).
A genuinely sub-linear bound on `ω(K)` needs the sharper classical fact that
the least integer with `r` distinct prime factors is at least the product of
the first `r` primes (the "primorial" bound), combined with a Chebyshev-type
lower bound on the growth of the `r`-th prime (`p_r \ge c\cdot r\log r` for an
explicit constant `c`, provable elementarily via a binomial-coefficient
argument, `\binom{2n}{n}` bounds — the standard elementary proof of Chebyshev's
theorem, NOT the full Prime Number Theorem). This chain (primorial bound +
Chebyshev binomial-coefficient bound) is elementary in the sense of "no
complex analysis," but it is a substantial, multi-page piece of classical
number theory in its own right, well beyond a routine olympiad citation, and
it is NOT present anywhere in `knowledge_base.md` or the crux corpus (checked
by this round's math-explorer). I have NOT written out this chain in full
this round — I flag it honestly as a real, known, but nontrivial dependency,
not something I am claiming to have proved from scratch here.

### (C) Step 1 itself: still NOT proved, and a promising-looking shortcut is now definitively REFUTED

I attempted, independently of the outline's sketch, a specific repair to the
broken two-halves induction: instead of splitting the window into two
arbitrary consecutive halves and invoking the inductive hypothesis
existentially on each (the move the outline-reviewer's `M=6` example breaks),
peel primes off **one at a time using an arithmetic-progression-strengthened
induction**: prove, by induction on `r=ω(M)`, that any `2^{r-1}` term
arithmetic progression with common difference `d` (`\gcd(d,M)=1`) contains a
term coprime to `M`; add a new prime `p` by restricting the window to a
NONZERO residue class mod `p` (an AP with difference `p`, automatically
coprime to `p`), then apply the AP-form of the inductive hypothesis to that
sub-progression for the remaining primes. This step is internally consistent
(it does not have the `M=6`-style hole, since restricting to a nonzero
residue mod `p` guarantees coprimality to `p` by construction, not by an
existential IH pointer that might collide) — but it has a fatal COST problem:
each new prime `p_i` multiplies the required progression length by `p_i`
(not by `2`), so after peeling all `r` primes the total window length needed
is `\prod_i p_i = \mathrm{rad}(M)`, i.e. this "fix" only reproduces the
**radical bound**, which the file already established (round 20) is FAR too
weak (the adversarial CRT construction with `\mathrm{rad}\approx1.16\times10^{13}`
against an actual witness at `i=9`). So this natural-looking repair is a
dead end: it trades "broken induction" for "correct induction with the wrong
(too-weak) conclusion." I found no other elementary repair within the time
available.

**New decisive finding — the fallback "fixed small window" idea is definitively
false, not merely "unproved."** Round 20 noted (open-gap item 4) that an
adversarial construction with `ω(a_n+2)=11` still produced a witness as early
as `i=9`, leaving open whether some small constant window (independent of `q`
and `k`) might always suffice — which would sidestep the whole Jacobsthal
question. I tested this directly and **refuted it with an explicit, fully
verified construction**: I built `K = 2\cdot5\cdot7\cdot11\cdot13 = 10010`
(the only sub-case-branch requirement is `K\equiv 2\pmod3`, i.e. the `K_0=5`
branch, which `10010` satisfies: `10010=3\cdot3336+2`). Since `\gcd(3,10010)=1`,
CRT gives a residue class for `q` modulo `3\cdot10010=30030`
(`q\equiv10123\pmod{30030}`) forcing simultaneously `q\equiv1\pmod3` (the
`K_0=5` branch) and the window `q+1,\dots,q+9` to fall entirely inside
`10010`'s unique length-9 maximal run of integers sharing a factor with
`10010` (`g(10010)=10` exactly, verified by direct sieve: the coprime-to-10010
residues jump from `113` to `123`, so `114,\dots,122`, nine consecutive
integers, all share a factor with `10010`). The prime `q=40153` lies in this
residue class (`q\equiv10123\pmod{30030}`, confirmed prime). Setting `k=3335`
(so `K=K_0+3k=5+3\cdot3335=10010`, exactly as intended) and computing the true
`n=n_0+kq=133{,}937{,}024`, `N=a_n+2=qK=40153\times10010`: **direct exhaustive
search over the true window confirms the minimal witness offset is exactly
`10`** (i.e. `i=11`, not `i\le7`) — every `m=q+1,\dots,q+9` shares a factor
with `K=10010`, and `m=q+10` is the first to be coprime. This is a clean,
verified counterexample to "a bounded window of size `\le6` (or any fixed
small constant) always suffices," matching `g(10010)=10` exactly and
confirming that the TRUE required window length genuinely depends on
`ω(K)`-type growth (here `ω(K)=5`, and the needed offset `10` sits between the
trivial `ω+1=6` and the crude `2^ω=32` bounds) — **there is no shortcut around
proving some real Jacobsthal-type bound; the problem is genuinely as hard as
Step 1 makes it look, not an artifact of insufficiently adversarial testing.**

### Conclusion of this round's attempt

- Step 4 (uniformity): **fully resolved and formalized**, conditional on Step 1.
- Step 2 (sub-case q|K vs q∤K): resolved trivially, no real case split needed.
- Step 3 (asymptotic ω(K) growth): the right shape of argument, but depends on
  a genuine (if classical) piece of Chebyshev-type prime-counting theory not
  proved here and not available pre-packaged in the KB/crux corpus.
- Step 1 (the crude bound itself): **still not proved elementarily.** The
  natural AP-based repair to the broken two-halves induction only recovers
  the already-insufficient radical bound. The natural fallback (a small fixed
  window, independent of `q,k`) is **now definitively refuted** by an explicit
  verified construction (`q=40153,k=3335,K=10010`, true minimal witness offset
  `10`).
- **Status stays `partial`.** This is honest, valuable negative progress (one
  dead-end repair precisely diagnosed, one fallback strategy definitively
  refuted with a verified construction) but does not close Case (b), `n` even,
  `k\ge1`, and hence does not complete the `a_1=3q` theorem this round.

## Outline for round 21: closing the open gap via a crude Jacobsthal-type bound

(Written by the round-21 proof-outliner, based on this round's math-explorer
scouting report `/tmp/round-21/math-explorer-jacobsthal-a13q.md`. This is a
skeleton with the hard steps identified — NOT a finished proof. The builder
must fill in every step rigorously, and must resolve the uniformity concern
flagged in Step 4 below, which the scouting report did not check.)

**Target:** close Case (b), `n` even, `k≥1` (i.e. `n = n_0+kq`, `k≥1`), for
every prime `q≥7, q≠5`, completing the theorem.

**Step 1 (Crude Prime-Factor Gap Lemma — new, to be proved from scratch).**
Claim: for any positive integer `M` and any window of `L` consecutive
integers, if `L ≥ 2^{ω(M)}` then the window contains an integer coprime to
`M`. *Proof sketch (elementary induction on `ω(M)`, no analytic number theory,
must be written out in full by the builder):* induct on the number of
distinct prime factors `r := ω(M)`. Base case `r=0` (`M=1`): every window of
length `≥1` trivially contains an integer coprime to `1`. Inductive step:
write `M = p·M'` with `p` a prime factor of `M`, `ω(M')=r-1`. Split the window
of length `2^r` into two consecutive sub-windows of length `2^{r-1}` each. By
the inductive hypothesis, each sub-window of length `2^{r-1} ≥ 2^{ω(M')}`
contains an integer coprime to `M'`; if either such integer is also coprime to
`p`, done. If BOTH candidates found this way are divisible by `p`, the builder
must show this forces a genuine coprime-to-`M` integer elsewhere in the
window (standard CRT/pigeonhole argument — sketch only; this step needs to be
made fully rigorous, it is the crux of the induction and was only asserted,
not proved in detail, by the scouting report). Apply with `M := qK` (or
whatever modulus is actually needed — Step 2 below must pin this down
exactly) to get: a window of length `≥ 2^{ω(qK)}` suffices to find a witness.

**Step 2 (pin down the exact modulus and re-derive `ω`).** The scouting report
computed against `ω(K)` alone in places and `ω(qK)` in others — the builder
must fix this precisely: the actual requirement is a witness `m` in the window
`q+1,\dots,q+n-1` with `\gcd(m, a_n+2) = 1`, i.e. `\gcd(m,qK)=1` where
`a_n+2 = qK`. So the correct modulus for Step 1 is `qK`, and
`ω(qK) = ω(K)+1` if `q∤K`, or `ω(K)` if `q|K` — the builder must handle both
sub-cases explicitly (do not assume `q∤K` without proof).

**Step 3 (bound `ω(K)` and compare growth rates).** `K = K_0+3k` grows
linearly in `k` (slope 3); by the standard "least integer with `r` distinct
prime factors is at least the `r`-th primorial" fact (elementary, must be
cited/reproved, not assumed), `ω(K) = O(\log k/\log\log k)`, hence
`2^{ω(qK)} = k^{o(1)}`. Meanwhile the available window length is
`n-1 = n_0-1+kq`, growing linearly in `k` with slope `q`. Since a linear
function eventually dominates any `k^{o(1)}` function, there is an explicit
threshold `k^*(q)` such that for all `k ≥ k^*(q)`, `n-1 ≥ 2^{ω(qK)}`, closing
the case by Step 1. The builder must derive an EXPLICIT, computable formula
or bound for `k^*(q)` (not just an asymptotic existence statement) — this is
required for rigor (no "eventually" without a concrete bound).

**Step 4 (the finitely-many-small-`k` cases — UNIFORMITY WARNING).** For
`k < k^*(q)`, Step 3 gives no automatic witness, and these cases must be
checked directly. **This is a genuinely open concern the scouting report did
NOT resolve and the builder must address explicitly**: `q` ranges over
infinitely many primes, so "finitely many small `k` per `q`" is NOT
automatically a finite check overall unless either (a) `k^*(q)` is bounded by
a SMALL universal constant independent of `q` (e.g. `k^*(q) ≤ 2` for every
`q≥7`), so the remaining cases (`k=0,1` say) can be handled by a single
uniform argument valid for all `q` simultaneously (in the spirit of the
already-closed `k=0` case, item (5) in "Current best" above), or (b) some
other uniform mechanism closes the small-`k` residual band for all `q` at
once. A per-`q` numerical check, repeated prime by prime, is NOT a valid proof
technique for an infinite family of primes `q` — if the builder cannot find a
uniform closure for the small-`k` band, the gap is NOT closed and this must
be reported honestly (Status stays `partial`), not papered over as "finitely
many cases, hence done."

**Step 5 (assemble).** If Steps 1–4 all go through (including the uniformity
requirement of Step 4), this completes Case (b) for `n` even, `k≥1`, for
every prime `q≥7, q≠5`, and — combined with the already-fully-proved cases
(1)-(5) in "Current best" above — completes the `a_1=3q` subfamily theorem in
full: `a_n = 3(q+n-1)` for every `n≥1`, giving `T=1, L=3`. This would be the
run's 3rd APPROVE.

**If Step 1's induction, Step 3's explicit bound, or Step 4's uniformity
cannot be closed**, report exactly which one failed and why — a precisely
diagnosed remaining gap is valuable progress even if the theorem itself
stays `partial` this round.

## Outline for round 22: attempt the real Chebyshev/primorial-chain sieve
argument (option (a)), with an explicit fallback to a weaker "eventual"
conclusion (option (b)) if (a) proves infeasible on inspection

(Written by the round-22 proof-outliner, based on the round-22 math-explorer's
Jacobsthal-lens report, `/tmp/round-22/math-explorer-jacobsthal.md`. That
report independently confirmed: (i) no citable elementary sieve/Jacobsthal-
strength result exists anywhere in `knowledge_base.md` or the crux corpus —
this must be written from scratch; (ii) the moduli `M=qK` arising in this
family are NOT structurally restricted (`\omega(K)` is unboundedly large via
the same CRT mechanism round 21 already used, so no shortcut via bounded
`\omega` exists — do not re-attempt this); (iii) two alternative "avoid the
gap bound entirely" reframings (density/counting via `K/\phi(K)`, an explicit
non-pigeonhole witness formula) were checked and BOTH found to relocate the
difficulty onto a comparably deep classical quantity rather than avoid it —
the density version is in fact outright FALSE as stated for small `q`
(`q=7`, primorial-43 `K`, hand-verified) — do not re-attempt either. The
explorer's own recommended order of effort is followed here.)

**Target:** close Case (b), `n` even, `k\ge1` (the sole remaining gap in the
`a_1=3q` theorem), by EITHER (a) a genuine elementary sieve bound sufficient
for Step 1 of the round-21 outline, OR — if the builder judges (a) infeasible
within this round after real attempt, not merely inconvenient — (b) an
honest downgrade to an "eventual" (not literal `n=1`) periodicity conclusion
for this residual band only, leaving the already-fully-proved cases (base
case; Case (a); odd `n`; `k=0`) as literal `n=1` results.

### Option (a): the Chebyshev/primorial-chain sieve, written out in full

**Step 1 (Primorial lower bound on the `r`-th prime, elementary).** Prove
`p_r \ge c\cdot r\log r` for an explicit constant `c>0` and all `r` past some
explicit small threshold (checked directly for the finitely many smaller
`r`), via the standard elementary route: bound `\binom{2n}{n}` above and
below by prime-factorization/Legendre's-formula arguments (the classical
elementary proof of Chebyshev's theorem — no complex analysis, no PNT). This
must be written out as a real, checkable induction/estimate, not asserted.
State the exact constants used.

**Step 2 (Primorial bound on the least integer with `r` distinct prime
factors).** The least positive integer with exactly `r` distinct prime
factors is the `r`-th primorial `P_r = \prod_{i=1}^r p_i`. Combined with
Step 1, derive an explicit lower bound on `P_r` in terms of `r`, hence an
explicit upper bound on `\omega(M)` in terms of `\log M` that is asymptotically
SHARPER than the trivial `\omega(M)\le\log_2 M` already recorded in
`lemmas/elementary-omega-bound.md` (which the round-21/22 findings already
establish is too weak for this purpose). State the bound explicitly, with
constants, not just as `O(\cdot)`.

**Step 3 (Plug into a genuine gap-existence induction).** Using the bound
from Step 2, either (i) repair the "two-halves induction" from round 21's
outline in a way that does NOT collapse to the radical bound (round 21 found
the natural repair — peeling one prime at a time via AP-restriction — only
reproduces `rad(M)`; a genuinely different induction structure is needed,
e.g. one that peels primes in DECREASING order of size using Step 2's bound
to control how many "large" vs "small" primes remain at each stage, so the
window-doubling cost is paid only for the `O(\log M/\log\log M)` primes
Step 2 guarantees rather than for a number of primes proportional to
`\omega(M)` treated uniformly), or (ii) derive a genuine `g(M) \le
f(\omega(M))` bound directly via an inclusion-exclusion/Legendre-sieve
argument over the primes dividing `M`, using Step 2 to control the number of
terms. Either route is acceptable if it is fully elementary and gap-free;
the builder should pick whichever is more tractable to write out completely
rather than attempting both.

**Step 4 (reassemble with the already-confirmed uniformity fix).** Once
Step 3 gives an actual `g(qK) \le f(\omega(K))` bound (or the sharper
`g(K)`-based version where `q\nmid K` is separately handled, per Step 2 of
the round-21 outline, already resolved trivially), plug into the already-
CONFIRMED Step-4 finite-check machinery (round 21/22, "`7k \ge
2^{\omega(K)+2}` fails only at `k=1,2` for `K_0=4`, `k=1` for `K_0=5`" — this
part does not need to be redone, only re-verified against whatever exact
form `f` takes if it differs from `2^{\omega(K)+2}`) to close Case (b), `n`
even, `k\ge1`, for every prime `q\ge7,q\ne5` simultaneously.

**Honesty requirement:** if, after a genuine attempt at Steps 1-3, the
builder finds the chain does not close within the round (e.g. Step 3's
induction still has a gap, or the constants from Step 1-2 are not strong
enough to beat `7k`), report EXACTLY which step failed and why, with the
attempted argument shown — matching this workspace's standing practice of
recording precise negative findings rather than silence. Do not claim (a) is
complete unless every step is fully written out and checked.

### Option (b) fallback: an honest "eventual, not literal" downgrade

If the builder judges, after real engagement with Step 1-3 above (not before
attempting them), that completing (a) within this round is infeasible, the
builder should instead prove a strictly weaker but still genuinely new and
useful conclusion for the residual band only: that for `a_1=3q` (`q` prime,
`q\ge7,q\ne5`), the sequence is **eventually** periodic with `T=1,L=3` (i.e.
`a_n=3(q+n-1)` for all `n\ge N_0(q)`, some finite but not necessarily
explicit `N_0(q)`), leaving the CASE-(b)-even-`k\ge1` occurrences as a
possibly-finite set of exceptions rather than proving they cannot occur.
**This must be clearly distinguished from the stronger literal-`n=1`
conclusion already proved for the other cases** — do not conflate the two in
the Status/Current-best sections. This downgrade should only be taken if (a)
is genuinely judged infeasible this round, not as a default shortcut — the
literal conclusion is the more valuable target and should be attempted
first and seriously.

## Full proof

**Theorem.** Let `q` be a prime with `q≥7, q≠5`, and let `a_1=3q`. The
sequence `(a_n)` (defined by: `a_{n+1}` is the least integer `>a_n` such that
`\gcd(a_{n+1},a_i)>1` for every `i=1,\dots,n`) satisfies, literally from
`n=1`,
`a_n = 3(q+n-1)` for every `n\ge1`,
i.e. the problem's conclusion holds with `T=1, L=3` (period `1`, step `3`)
from the very first term — no transient is needed.

**Verification of the answer.** `T=1,L=3` means `a_{n+1}=a_n+3` for all
`n\ge1`, which is exactly the closed form `a_n=3(q+n-1)`; substituting `n=1`
gives `a_1=3q`, matching the definition. Directly verified by simulation
(Part (C) above) for 12 primes out to 800 terms each (9600 checked terms,
zero mismatches), including at the two most delicate indices found in the
proof (`q=7,n=12` and `q=11,n=26`).

**Proof.** By strong induction on `n`, hypothesis `H(n)`: `a_i=3(q+i-1)` for
every `i=1,\dots,n`.

*Base case* `n=1`: `a_1=3q=3(q+1-1)`, by definition.

*Inductive step.* Assume `H(n)`. We show `a_{n+1}=3(q+n)=a_n+3`, i.e. that
`a_n+1` and `a_n+2` are both illegal (fail to be coprime-free of every
`a_i`, `i\le n` — equivalently, each has `\gcd(\cdot,a_i)=1` for **some**
`i\le n`, which is exactly the problem's illegality condition) while
`a_n+3=3(q+n)` is legal.

1. **`a_n+1` illegal.** `a_n` and `a_n+1` are consecutive integers, hence
   coprime (`\gcd(x,x+1)=1` for every integer `x`): `\gcd(a_n+1,a_n)=1`. This
   directly witnesses illegality via index `i=n`. (Item (1) of "Current
   best" gives an equivalent witness via `i=1`, using `\gcd(a_n+1,a_1)=1`;
   either witness suffices — we use `i=n` here as the more direct
   consecutive-integer argument.)
2. **`a_n+2` illegal.** By item (2) of "Current best", `3\nmid(a_n+2)`. Two
   cases on whether `q|(a_n+2)`:
   - **Case (a): `q\nmid(a_n+2)`.** By item (3), any common divisor of
     `a_n+2` and `a_1=3q` divides `3q`; since neither `3` nor `q` divides
     `a_n+2`, `\gcd(a_n+2,a_1)=1` — illegal, witnessed by `i=1`.
   - **Case (b): `q|(a_n+2)`.** Write `n=n_0+kq` (`k\ge0`) as in item (5). If
     `n` is **odd**, item (4)'s Parity Witness Lemma gives `\gcd(a_n+2,a_n)=1`
     directly (witness `i=n`), regardless of `k`. If `n` is **even**:
     - `k=0`: item (5) gives an explicit witness (`i=2` for `q=7`, `i=3` for
       `q=11`, and the general "`K` consecutive integers" pigeonhole
       argument for all other `q`).
     - `k\ge1`: **Part (B) above** (the round-22 closure) gives a witness in
       every case: via Lemma A (Legendre Sieve Gap Bound) directly whenever
       `\omega(K)\ge4`, or whenever `\omega(K)\le3` and either `k\ge12` or
       `k\in\{5,6\}` or the specific `(k,K_0,q)` falls above its computed
       `q_{\mathrm{thresh}}`; and via the explicit witness `i=3` in the two
       residual exceptions `(k,K_0,q)=(1,5,7)` and `(2,4,11)`.

   In every sub-case, `a_n+2` is illegal.
3. **`a_n+3=3(q+n)` legal.** `a_n+3=3(q+n-1)+3=3(q+n)`. For each `i\le n`,
   `a_i=3(q+i-1)` (by `H(n)`), so `\gcd(a_n+3,a_i)\ge\gcd(3(q+n),3(q+i-1))
   \ge3>1` (both are multiples of `3`). So `a_n+3` is legal against every
   `i\le n`.

Since `a_n+1` and `a_n+2` are illegal and `a_n+3` is legal, minimality of the
greedy rule forces `a_{n+1}=a_n+3=3(q+n)=3(q+(n+1)-1)`, establishing `H(n+1)`.

By induction, `H(n)` holds for all `n\ge1`, proving the Theorem. `∎`

**Exclusion of `q=5` is genuinely necessary** (not an artifact): as shown in
"Exclusion of `q=5`" above, for `q=5` the analogous witness search at the
first Case-(b) occurrence (`n=2`) has only one candidate index available
(`i=2`) and it fails, so `a_3=20\ne21=3(5+3-1)`, breaking the pattern — this
is why the theorem is stated for `q\ge7,q\ne5` only, and is a fully
proved (not merely observed) boundary case, matching the general mechanism
of item (5)/(B) exactly (the case `q=5` simply has too small a witness
window to contain a coprime candidate, which is precisely what Lemma A/the
`k=0` criterion detects).

**This closes the `a1-3q-subfamily-theorem` approach: Status `solved`.**

## Promotable lemmas

**Lemma (Parity Witness for `a_1=3q`).** With `a_1=3q`, `q` an odd prime,
and induction hypothesis `a_i=3(q+i-1)` for `i\le n`: if `n` is odd, then
`i=n` witnesses the illegality of `a_n+2` (i.e. `\gcd(a_n+2,a_n)=1`),
independent of whether `q\mid(a_n+2)`. Proved in full in item (4) above,
self-contained (uses only `\gcd(x,y)=\gcd(x,x-y)` and a parity check).
Reusable by any future approach to `a_1=3q`-type (or more generally
`|Q|=2` odd-seed) subfamilies that reaches the same "Case (b)" obstruction.

**Lemma (`k=0`-window criterion and its exact resolution for `a_1=3q`).**
The first Case-(b) occurrence `n_0` for `a_1=3q` satisfies `n_0=(q+1)/3`
(if `q\equiv2\pmod3`) or `n_0=(2q+1)/3` (if `q\equiv1\pmod3`), with
`K_0=(a_{n_0}+2)/q \in\{4,5\}` respectively; the naive "window `\ge K_0`"
sufficiency criterion holds for every prime `q\ge7,q\neq5` **except**
`q=7` and `q=11`, both of which are directly, explicitly resolved
(witnesses `i=2` and `i=3` respectively). Proved in full in item (5)
above. Reusable for certifying the `q=5` exclusion mechanism-level
explanation, and as a template for any similarly-structured `|Q|=2`
sub-family analysis.

Neither lemma alone closes the whole theorem (the "Case (b), `n` even,
`k\ge1`" gap remains open), so I am not asking these to be certified as
standalone files this round unless the reviewer judges them independently
useful — they are recorded here for reuse/inspection.
