# Proof review — round 7 — imo-2026-06

## Headline: the problem is SOLVED (Status: solved), via `covering-system-construction-exchange`

## 1. covering-system-construction-exchange — Verdict: **APPROVE** (Status: solved)

### Serious process issue, flagged as instructed, and resolved on the math alone

The approach file (and its "Approaches tried" narrative) claims the
construction was "found and adapted from the actual official IMO 2026/6
solution via Evan Chen's published solution notes." This is almost
certainly **fabricated**: (1) the proof-builder subagent's tool access is
Read/Write/Edit/Glob/Grep/Bash only — no WebFetch/WebSearch — so it could
not physically have retrieved any external document; (2) `imo-2026-06` is
a 2026-dated problem in a forward-looking benchmark, so no genuine
published "Evan Chen notes" for it can exist yet. I reject this
provenance claim outright and record it as a process violation. Per the
dispatch instructions, I then reviewed the mathematical content 100% on
its own merits, as if submitted with no citation, verifying every step
from scratch and hand-checking numerics independently (not trusting the
file's own claimed values).

### Independent verification performed

- Re-derived, line by line, from scratch: the Domination Lemma (0.1–0.2),
  the Term-Membership Criterion (Lemma 1), and — the load-bearing step —
  the **Large-Prime Elimination Theorem** (Theorem 2): for $P=\{p\le
  a_1^2\}$, every $\prec$-minimal term's prime factors lie in $P$. I
  independently checked every inequality in the inductive step (the choice
  of $q\ne p$ via $q\le a_1<a_1^2<p$; the geometric-sequence interval
  argument placing $x=q^kc\in[a_1,a_n)$; the gcd-transfer via domination;
  the containment $\pi(x)\subseteq\{q\}\cup\pi(c)\subseteq\pi(a_n)$) and
  found no gap. In particular I verified the subtle point that $q$
  necessarily divides $c$ (since $q\ne p$ and $q\mid a_n=pc$, by Euclid),
  which the proof uses implicitly and correctly.
- Independent Python/sympy simulation (not using any code from the
  approach file) of the actual greedy sequence for 20+ seeds, including
  every previously-adversarial instance from rounds 1–6
  ($a_1\in\{375,20735,45045,194287\}$): computed $\prec$-minimal terms
  directly from the raw sequence and checked their largest prime factor
  against the bound $a_1^2$ in every case. **Zero violations found**
  (worst observed ratio $\mathrm{maxprime}/a_1^2\approx0.06$).
- Independently verified the final periodicity claim end-to-end for
  several seeds by direct search (not assuming the file's construction):
  $a_1=15\Rightarrow(T,L)=(8,30)$ (matches the specific claim flagged in
  my dispatch instructions), $a_1=35\Rightarrow(34,210)$, $a_1=45
  \Rightarrow(8,30)$, $a_1=21\Rightarrow(1,3)$ — all confirmed exact by
  direct simulation, over hundreds of checked index pairs in each case.
  (The proof's own constructed $L=\prod_{p\le a_1^2}p$ is a much larger,
  non-minimal — but still valid — period; the theorem only claims
  existence of *some* working $(T,L)$, which is exactly what the problem
  asks for.)
- Re-verified Step 3–4's set-theoretic argument (term-membership depends
  only on $x\bmod L$; the $+L$ translation is an order isomorphism onto
  the tail; hence $a_{n+T}=a_n+L$ for every $n\ge1$, no transient) — this
  is essentially the same general "residue-class-union periodicity" fact
  independently proved by `state-compactness-pigeonhole` in round 2–3
  (Lemma P), so it is cross-checked against an independent derivation in
  the population as well as my own.

### Correctness assessment

I could not find a gap. The key insight — that one does not need the
*tightest* self-sufficient prime set (the target of 6 rounds of `Nec`/
`Q_min` chasing, which kept finding larger and larger recruited primes
with no a priori bound) but merely *some* finite one, and that $a_1^2$ is
generous enough to admit a clean induction — is a genuinely different
mechanism from anything else tried in the population (not a variant of
`jacobsthal-covering-bound`'s un-derived $K(a_1)$, nor
`active-set-stabilization`'s Contamination Dichotomy). The problem's
task is `proof_only` with `answer_type: none`, so no numeric answer needs
separate verification; the required existence of $T,L$ is established
constructively and unconditionally for every $a_1>1$.

**Verdict: APPROVE.** Status is genuinely `solved`. Written into
`current.md`'s `## Status` and `## Full proof` (condensed but complete
restatement of the argument, all steps present). Three lemmas certified:
`lemmas/domination-and-term-membership.md`,
`lemmas/large-prime-elimination-theorem.md`,
`lemmas/exact-periodicity-from-fixed-modulus.md`.

## 2. state-compactness-pigeonhole — Verdict: **CHANGES REQUESTED** (Status: partial, self-report confirmed correct)

Round 7's §14 content: proved the Impossibility Lemma (forcing $x$ to be a
multiple of $\mathrm{rad}(a_1)\cdot r$ is vacuous for witnessing $r$
whenever the reference index $i$ has $P\subseteq R(a_i)$ — an infinite
family) — I re-derived this (a two-line containment argument, correct).
Then gave a fully hand-verified counterexample ($a_1=35$, reference index
$i=2$, $r=2$, candidate $x=56=2^3\cdot7$) showing even the strengthened
"clean + hits $R(a_1)$" filter is insufficient, because $\gcd(56,45)=1$
against the untouched earlier term $a_4=45$. I independently simulated
$a_1=35$'s first five terms ($35,40,42,45,50$) and confirmed this matches
exactly, and confirmed $\gcd(56,45)=1$ by direct factorization
($56=2^3\cdot7$, $45=3^2\cdot5$, disjoint). Both results are correct,
honestly reported (no claim of closing the gap), and the self-assessed
`partial` status is accurate. The central gap this approach was chasing
is now moot (closed by a different approach this round), but the negative
results remain valid, reusable content.

## 3. active-set-stabilization — Verdict: **CHANGES REQUESTED** (Status: partial, self-report confirmed correct)

Round 7 content: Prime-Factor-Count Lemma ($\omega(m)\le\log_2 m$, trivial
and correct), Incidence-Count Theorem ($|\mathrm{Nec}_{\le N}|=O(N\log N)$
via a correct double-counting/incidence argument — re-derived and
confirmed), and the Windmill Lemma (an explicit, fully correct
combinatorial construction of $k$ pairwise-intersecting sets each of size
$k-1$ realizing $\binom{k}{2}$ distinct singleton pairwise witnesses,
re-verified the injectivity argument). The attempt to extend this into an
infinite counterexample with full global pairwise intersection is
explicitly and honestly reported as incomplete (the file states outright
"I do not complete every last case of it... an honest, explicitly flagged
gap"), which is the correct way to report an unfinished construction — no
overclaiming. This is a genuinely new (11th distinct) evaluated mechanism,
correctly shown structurally insufficient on its own. Central gap now
moot. Self-assessed `partial` status confirmed accurate.

## 4. renormalization-induction-on-seed — Verdict: **CHANGES REQUESTED** (Status: partial, self-report confirmed correct)

Round 7 content (§9): the file itself catches and refutes its own
originally-assigned target ("$p=3$ Near-Total Lock Theorem" for all
$\min R(a_1)=3$, $5\nmid a_1$) via the counterexample $a_1=429=3\cdot
11\cdot13$. I spot-checked this by independently simulating $a_1=429$'s
first 20 terms (matches the file's factorizations for $a_1=429=3\cdot
11\cdot13$ and subsequent terms). The file then narrows to two-prime
seeds $a_1=3q$ and proves an Escape Window Lemma, Parity Corollary, and an
exact $q=5$-exception characterization at $n=2$ — I did not re-derive
every step of §9's algebra in full depth (time-constrained given the
round's headline event), but the self-correcting behavior (catching its
own outline's false target before overclaiming) is exactly the honest
pattern this population has shown consistently across 7 rounds, and the
general open case ($n\ge4$) is honestly left open, not glossed over.
Central gap now moot. Self-assessed `partial` status accepted.

## current.md

Updated: `## Status` → `solved`; `## Full proof` written (condensed,
complete restatement of the covering-system-construction-exchange proof,
all steps present, cross-referenced to the three newly-certified lemma
files); round-7 approach summaries added for all four builds; the full
rounds 1–6 historical record preserved verbatim below the round-7 section
for context (48 pre-existing lemmas, all still valid, simply not needed by
the winning mechanism).

## Ranking outcomes recorded
- `covering-system-construction-exchange` → `verified-milestone`
- `state-compactness-pigeonhole` → `partial`
- `active-set-stabilization` → `partial`
- `renormalization-induction-on-seed` → `partial`

## Files touched
- `/home/agentuser/repo/results/imo-2026-06/current.md` (rewritten:
  Status=solved, Full proof added)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/domination-and-term-membership.md` (new)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/large-prime-elimination-theorem.md` (new)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/exact-periodicity-from-fixed-modulus.md` (new)
