# Proof review — imo-2026-06, round 1

Problem: infinite sequence $a_1>1$, $a_{n+1}$ = smallest integer $>a_n$ with
$\gcd(a_{n+1},a_i)>1$ for all $i\le n$. Prove $\exists T,L$ with
$a_{n+T}=a_n+L$ for all $n$. (`proof_only`, no numeric answer to verify.)

Reviewed independently: `active-set-stabilization.md`,
`state-compactness-pigeonhole.md`, `growth-rate-contradiction.md`.
(`jacobsthal-covering-bound.md` was not built this round, not reviewed.)

I re-derived the load-bearing claims from scratch (not just read the proofs)
and ran the sequence computationally (Python, `sympy`) for $a_1 \in
\{6,15,21,35,105\}$ up to 150–400 terms to sanity-check the bounded-gap claim
and the behavior of $S$.

## 1. active-set-stabilization.md — verdict: CHANGES REQUESTED (Status: partial, confirmed accurate)

**Lemma 0 (existence).** Correct. Standard: multiples of
$N=\mathrm{lcm}$-of-one-prime-per-earlier-term form an infinite candidate
set, well-ordering gives the minimum. No gap.

**Lemma 1 (gap bound $g(Q)=\min(Q)$).** Correct and trivial (pigeonhole on
$q$ consecutive integers). Reusable but weak.

**Lemma 2 ("every term is S-covered").** I re-derived this independently:
fix $i$; for every $j>i$ the definition (applied at step $j-1\ge i$) forces
$\gcd(a_j,a_i)>1$, so $R(a_j)\cap R(a_i)\neq\emptyset$; $R(a_i)$ is finite,
there are infinitely many $j>i$, pigeonhole gives a single prime $p\in
R(a_i)$ dividing infinitely many $a_j$, i.e. $p\in S$, and $p\in R(a_i)$.
**This checks out exactly as claimed** — holds for every $i\ge1$
unconditionally, no circularity, no assumption on $|S|$.

**Central-gap "negative result."** The builder shows a pure counting
argument (using only "$p\in S \Rightarrow p$ divides infinitely many terms"
+ $\omega(a_n)\le\log_2 a_n$) gives only $K^2 \le N\log_2(a_N)$, never a
contradiction since $N$ is chosen depending on $K$. I re-checked this
algebra: $\omega(m)\le\log_2 m$ is correct since $m\ge 2^{\omega(m)}$; the
counting bound $\sum_k |\{n\le N: p_k\mid a_n\}| \le \sum_{n\le N}\omega(a_n)
\le N\log_2(a_N)$ is correctly derived. The diagnosis that this cannot yield
a contradiction for any growth rate is correct reasoning, honestly presented
as a negative result (not a claimed theorem beyond that). Good, real content.

**Conditional finish (given Hypothesis H).** The periodicity argument (state
= residue mod $L$ + which residues have appeared) is worked out in detail,
but the file's own write-up gets tangled and *explicitly, honestly*
concludes that the "extend from $n\ge n_1$ to all $n\ge1$" step is a second,
unclosed gap — it does not paper over this; the author tried three fixes and
showed each fails, which is correct self-diagnosis rather than a hand-wave.

**Overall:** All claimed unconditional lemmas hold up under independent
re-derivation. No overclaiming — Status `partial` is accurate; the two open
gaps (central: $S$ finite; secondary: prefix extension) are stated with
precision, not vaguely. Real progress this round (Lemma 2 proven in full
generality, dead-end mechanism ruled out and documented). Route:
**CHANGES REQUESTED** — send back to close either the central gap (using
greedy minimality, as the file itself flags) or at least the secondary
prefix-extension gap.

## 2. state-compactness-pigeonhole.md — verdict: CHANGES REQUESTED (Status: partial, confirmed accurate)

**Lemma 0 (existence).** Same correct argument as sibling file. No gap.

**Lemma 1 (pairwise non-coprimality, all $i\neq j$).** Verified: this is a
direct, correct unpacking of the definition — $a_j$ (for $j=(j-1)+1$) is
required by definition to have $\gcd(a_j,a_i)>1$ for **all** $i\le j-1$,
which is exactly the claim for any $i<j$. Trivial but true, and a genuinely
useful sharpening to state explicitly (used to fuel Lemma D's pigeonhole).

**Lemma D (every term meets S).** Same statement and same correct proof as
active-set-stabilization's Lemma 2, independently derived. I confirmed both
proofs are mathematically identical and both valid.

**Lemma 2 (type stabilization) + Lemma 3 (conditional finish).** Assuming
Hypotheses F ($S$ finite) and H (S-hitting is eventually necessary, not just
sufficient — correctly identified as the load-bearing unproven claim), the
CRT-based residue reduction is correct: divisibility of $m$ by each fixed
prime of $S$ depends only on $m\bmod L$ ($L=\prod_{p\in S}p$), so "Good"
$\subseteq \mathbb Z/L\mathbb Z$ is well-defined; $d(r)\in[1,L]$ exists since
$0\in$ Good and a full residue system of length $L$ always contains a
residue $\equiv 0$. The deterministic map $g:\mathbb Z/L\mathbb Z\to
\mathbb Z/L\mathbb Z$, pigeonhole on the finite state space, and the
inductive telescoping argument giving $a_{n+T}=a_n+L'$ for $n\ge n_1^*$ are
all correctly derived; I re-checked the induction step and telescoping sum
and found no error. This is a cleaner conditional finish than the sibling
file's, but rests on the same two unproven hypotheses.

**Honesty of Gap 1/Gap 2.** The file correctly identifies that Hypothesis H
(necessity, not just sufficiency, of S-hitting) is exactly the crux still
missing, and — like its sibling — independently notices and honestly
records the same prefix-extension issue (Gap 2) as a second, distinct gap.
No overclaiming.

**Overall:** All claimed lemmas hold up; Status `partial` is accurate.
Route: **CHANGES REQUESTED** — same two gaps as active-set-stabilization
(central: prove Hyp F+H; secondary: prefix extension), stated with equal
precision.

## 3. growth-rate-contradiction.md — verdict: CHANGES REQUESTED (Status: partial, confirmed accurate; approach itself dead-ends on its original mechanism but produces a valid reusable lemma)

**Key Lemma (bounded gap $a_{n+1}-a_n\le \mathrm{rad}(a_1)$).** I
re-derived this from scratch: since $1\le n$ always, $\gcd(a_n,a_1)>1$ for
every $n\ge2$ (and trivially for $n=1$), so every term shares a prime with
$a_1$'s prime set $P$. Taking $M$ = least multiple of $R=\mathrm{rad}(a_1)$
exceeding $a_n$: $M$ is divisible by every prime in $P$ (since $R$ is), and
each $a_i$ ($i\le n$) is divisible by *some* prime of $P$, so $\gcd(M,a_i)>1$
for all $i\le n$; $M\le a_n+R$; hence $a_{n+1}\le M\le a_n+R$. This is
correct, non-circular (uses nothing but $a_1$ always being a live
constraint), and I additionally verified it **computationally**: for
$a_1\in\{6,15,21,35,105\}$, $R=\mathrm{rad}(a_1)\in\{6,15,21,35,105\}$ and
the observed max gap over hundreds of terms was $\{2,6,3,10,6\}$
respectively — always $\le R$, consistent with the bound (and demonstrating
it is not tight in general, which the file doesn't overclaim).

**"Why Lemma B fails" discussion.** The claim that a freshly-recruited large
prime need not force a large gap (because the gap is controlled by $R$
regardless of which incidental extra prime factors a term has) is correct
reasoning and matches my own computation (e.g. for $a_1=15$, primes up to
$\ge 70$ appear only a handful of times each over 400 terms, entirely
consistent with them riding along as incidental factors of terms whose gaps
are controlled by small primes — I could not find, and the file correctly
does not claim, a counting contradiction from this data). This is honestly
recorded as a dead end for the *specific* mechanism, not for the whole
approach's contributed lemma.

**Overall:** The bounded-gap lemma is correct, rigorous, and a genuinely
useful, reusable unconditional ingredient. The file is honest that its
originally-planned finishing mechanism (Lemma B) does not work and offers no
substitute — it does not overclaim progress toward the central gap. Status
`partial` is accurate (arguably borderline `unsolved` for *this specific
route*, since the approach's own intended finishing mechanism is a confirmed
dead end and no alternative is proposed) — I keep it at `partial` because a
genuinely new, correct, and reusable unconditional lemma was produced this
round, which counts as real progress under the file-contract definition of
partial ("a correct reduction or a proven key lemma, but the proof is not
complete"). Recorded in the ranker as outcome `dead-end` for the *original
Lemma B mechanism*, since as an independent route to the central gap this
framing is exhausted — the field should not re-attempt "growth/counting via
fresh-prime density" as a way to bound $|S|$; only the derived bounded-gap
lemma survives as reusable content.
Route: **CHANGES REQUESTED** if the builder wants to pivot this slug to a
new mechanism reusing its lemma; otherwise this line is effectively spent
and should not be re-expanded without a genuinely new idea (per the ranker
note, recorded as `dead-end`).

## Certified lemmas (promoted to `results/imo-2026-06/lemmas/`)

1. `existence.md` — well-definedness of the greedy sequence. Certified:
   proved identically and correctly in both active-set-stabilization and
   state-compactness-pigeonhole.
2. `every-term-meets-recurring-set.md` — every $a_i$ has a prime factor in
   $S$. Certified: proved identically and correctly in both
   active-set-stabilization (Lemma 2) and state-compactness-pigeonhole
   (Lemma D); this is the strongest unconditional structural fact the
   population has established so far.
3. `pairwise-non-coprimality.md` — $\gcd(a_i,a_j)>1$ for all $i\neq j$.
   Certified: proved correctly in state-compactness-pigeonhole (Lemma 1);
   a real, useful sharpening of the raw problem statement.
4. `bounded-gap-via-rad-a1.md` — $a_{n+1}-a_n \le \mathrm{rad}(a_1)$, hence
   $a_n=O(n)$. Certified: proved correctly (and independently verified
   computationally by the reviewer) in growth-rate-contradiction. Flagged
   with an explicit caveat in the lemma file that it does *not* by itself
   help close the central gap (its own author's finding), so future rounds
   don't re-attempt combining it with fresh-prime counting.

`active-set-stabilization`'s Lemma 1 (crude gap bound $g(Q)=\min Q$) was
**not** promoted separately — it's correct but strictly subsumed in
usefulness by the certified bounded-gap lemma above (which gives a concrete,
sharper bound tied to $a_1$); no need for two near-duplicate "gap bound"
lemma files.

## Central open gap for next round (unanimous across all reviewed approaches)

Prove $S=\{p: p\mid a_n \text{ infinitely often}\}$ is finite. Confirmed this
round: naive counting/pigeonhole using only "$p\in S\Rightarrow$ divides
infinitely many terms" + any bound on $\omega(a_n)$ or on gap sizes is
**provably insufficient**, regardless of growth rate (two independent
demonstrations of this, in active-set-stabilization and
growth-rate-contradiction, both mathematically checked and correct). Any
successful proof must exploit **greedy minimality** — that $a_{n+1}$ is the
*smallest* valid candidate — as essential structure, not merely the
divisibility constraints in isolation. A second, smaller, previously
unflagged gap (extending eventual periodicity down to $n=1$) is now also
identified by two independent approaches and should be closed alongside the
main gap.

## Status update

`results/imo-2026-06/current.md` updated: Status remains `partial`
(accurate — no approach is complete). Approaches-tried, Current-best updated
to reflect the two unconditionally-proven shared lemmas and the precisely
stated central + secondary gaps. No `## Full proof` section added (nothing
solved).

## Ranker outcomes recorded
- `active-set-stabilization`: `partial` — closed the S-covering lemma, ruled
  out a counting mechanism for the central gap, still open.
- `state-compactness-pigeonhole`: `partial` — same core progress via a
  cleaner conditional finish, central + secondary gaps still open.
- `growth-rate-contradiction`: `dead-end` — its own intended mechanism
  (growth/counting via fresh-prime recruitment) is confirmed not to work;
  contributes one valid reusable lemma (bounded gap) but no path forward for
  this framing on the central gap.
