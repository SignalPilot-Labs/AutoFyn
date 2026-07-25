# Proof review — imo-2026-06, round 3

All four just-built approaches independently reviewed, adversarially, each
against its own claimed lemmas and negative results. Independent
verification performed via (a) re-derivation of every load-bearing step by
hand and (b) exact-integer Python simulation of the actual greedy sequence
for several values of $a_1$ (15, 21, 35, 77), cross-checked against every
concrete numerical claim made in the four files.

No approach claims Status `solved`; all four correctly self-report
`partial`. I confirm all four self-assessments are accurate (no
overclaiming found, no hidden gap presented as closed). None reach
`solved`, so no APPROVE this round.

---

## 1. active-set-stabilization — Verdict: CHANGES REQUESTED (Status: partial, confirmed)

**Self-Type-Compatibility Lemma.** Re-derived from scratch: for finite
$Q\supseteq R(a_1)$ and index $i$ with $R(a_i)\subseteq Q$, pairwise
non-coprimality (certified) gives a common prime $p\mid a_i,a_j$; since
$R(a_i)\subseteq Q$, $\tau_i=R(a_i)$, so $p\in\tau_i\cap\tau_j$. Correct,
no gap. Corollary ($n=1$ never an obstruction) and Corollary 2
(propagation) both follow immediately and correctly.

**Soundness Lemma** ($\widehat a_{n+1}\ge a_{n+1}$ for any finite
$Q\supseteq R(a_1)$, unconditional). Re-derived: any $Q$-hitting candidate
$m$ automatically satisfies the true recursive test (shares a prime with
every earlier $a_i$, $i\le n$, via a prime of $Q$), so it's a valid
candidate for the true minimum, giving $a_{n+1}\le m$ for every such $m$,
in particular the $Q$-minimum itself. Correct, elementary, no gap.

**Exact-Correctness Criterion.** A direct iff sandwiching $\widehat
a_{n+1}$ between the true value via Soundness in one direction and direct
membership in the other. Both directions re-verified; correct.

**Refutation of the aimo-0680-style finish.** The claim is that no
relation "$k\mid a_{n+k}-a_n$ for all $n,k$" holds for this sequence,
witnessed by $a_1=15$: $a_3-a_1=5$, $k=2$, $2\nmid5$.
**Independently re-simulated**: exact greedy simulation for $a_1=15$
gives $a_1,a_2,a_3=15,18,20$, so $a_3-a_1=5$ exactly as claimed, and
$2\nmid5$. The counterexample is correct and the file's explanation of
*why* the aimo-0680 mechanism's load-bearing hypothesis (an unconditional
per-function divisibility fact, valid because that problem's process is
Markov) does not transplant here (this process is not Markov before
self-sufficiency) is sound reasoning, appropriately hedged with a caveat
about restricted/modified versions rather than an overclaim of total
impossibility.

**Gap remaining.** The central self-sufficiency gap (existence of a
correct finite $Q$) and the prefix-extension gap remain completely
untouched by this file, exactly as the builder states (by design — this
file's job per the division of labor was periodicity-given-Q, not Q's
existence). No overclaim; Status `partial` is correct.

## 2. state-compactness-pigeonhole — Verdict: CHANGES REQUESTED (Status: partial, confirmed) — **round's key structural result**

**Reduction Lemma** (Hypothesis SS$(Q,1)$ $\iff$ every accepted term is
$Q$-Good). This is the sharpest and most load-bearing new claim of the
round; I re-derived both directions independently from scratch rather
than trusting the write-up:

- (a)$\Rightarrow$(b): For $n=1$, $\mathrm{Good}_Q(a_1)$ holds
  unconditionally (Self-Type-Compatibility Corollary, re-verified above).
  For $n=k+1\ge2$: under (a), $a_{k+1}$ is *defined* as the minimum of a
  set characterized by $\mathrm{Good}_Q$, so trivially satisfies
  $\mathrm{Good}_Q$. Correct, no induction even needed.
- (b)$\Rightarrow$(a): Using the independently-re-verified **Fact D**
  ($a_{n+1}=\min\{m>a_n:\mathrm{Good}(m)\}$ for every $n\ge1$ — I checked
  the index-range argument that $\{i:a_i<m\}=\{1,\dots,n\}$ for
  $m\in(a_n,a_{n+1}]$ and confirmed it holds by monotonicity) and
  Soundness, both inequalities $\mu\ge a_{n+1}$ and $\mu\le a_{n+1}$
  ($\mu:=\min\{m>a_n:\mathrm{Good}_Q(m)\}$) check out exactly as claimed.

I confirmed there is **no circularity**: $\mathcal T=\{\tau_i:i\ge1\}$ is
defined using the already-well-defined infinite sequence $(a_n)$ (via
`existence.md`), not by assuming periodicity — it is a legitimate (if
non-constructive) mathematical object, and the equivalence is a genuine
theorem about it, not a restatement of the target under a different name.
This equivalence is correct and does genuinely collapse the population's
previously-separately-tracked Gap 1 and Gap 2 into one statement, as
claimed.

**Transient-free finishing theorem.** Re-checked as a valid consequence:
Step 1 ($A=\{m\ge a_1:\mathrm{Good}_Q(m)\}$, both inclusions) is correct
given Hypothesis SS$(Q,1)$ (via the Reduction Lemma); Step 2 (CRT
residue-dependence) is standard; Step 3 correctly applies the
already-certified Lemma P (I independently re-verified Lemma P
computationally with 50 randomized trials, all passing, in addition to
re-checking its bijection proof by hand). The composition is valid and
gives full periodicity for every $n\ge1$ with literally no transient,
exactly as claimed.

**What remains open**, correctly flagged by the builder and confirmed by
me: the existence of a finite $Q\supseteq R(a_1)$ satisfying the Unified
Central Claim is *not* established. The numerical evidence (many $a_1$
values, exhaustive pairwise checks) is real supporting evidence but the
builder is explicit and correct that the check's definition of $Q$ (via
the sequence's own empirically observed period) is circular for an actual
proof — this honest caveat is appropriately worded, not glossed over.
Status `partial` is correct; this is genuine, verified progress
(structural unification), not a closure.

## 3. jacobsthal-covering-bound — Verdict: CHANGES REQUESTED (Status: partial, confirmed)

**Adjacent-Link Lemma.** $\gcd(a_n,a_{n+1})=\gcd(a_n,d_n)\mid d_n\le R$.
Re-verified the identity $\gcd(x,x+d)=\gcd(x,d)$ by hand (standard,
correct via mutual divisibility of the two gcds) and combined with the
certified bounded-gap lemma; correct, holds for every $n\ge1$
unconditionally. Cross-checked numerically for $a_1\in\{15,21,35,77\}$.

**$\Lambda$-stabilization Lemma.** Standard bounded-monotone-sequence
argument on subsets of the fixed finite universe $U=\{p\le R\}$ (itself a
consequence of Adjacent-Link); correct, and correctly distinguished from
the certified `monotonicity-obstruction.md` negative result (that lemma
blocks *specific-state recurrence* claims; this is a *cardinality
stabilizes* claim about subsets of a fixed universe — a genuinely
different, unblocked argument type).

**Claimed refutation that the $\Lambda$-split reduction is tautological.**
I re-derived the set-theoretic lemma independently: for finite $\Lambda$,
$Q\setminus\Lambda$ finite $\iff$ $Q$ finite, via
$Q=(Q\cap\Lambda)\cup(Q\setminus\Lambda)$ and $Q\cap\Lambda\subseteq
\Lambda$ finite. This is elementary and **correct**. I checked this is
not a strawman: the round-3 outline's proposed reduction really did
amount to "split off the known-finite $\Lambda$ and prove the remainder
finite," and the file correctly identifies that $\Lambda$'s finiteness
provides no fixed universe confining $Q\setminus\Lambda$ (unlike $U=\{p
\le R\}$ confining $\Lambda$ itself) — so indeed no difficulty is
removed. This is a genuine, honest negative finding, not a misreading of
the outline.

**Gap remaining.** No monovariant for the central gap has been produced
across this approach's three rounds. Status `partial` correct.

## 4. bounded-link-invariant — Verdict: CHANGES REQUESTED (Status: partial, confirmed)

**Corrected legal-baseline lemma** ($b_n=$ gap to next multiple of
$R=\mathrm{rad}(a_1)$). Re-verified: legality against the *entire* prefix
(not just $a_1$) follows because every $a_i$ is divisible by *some* prime
of $R(a_1)$ (certified `prime-factors-a1-cover-forever.md` /
`bounded-gap-via-rad-a1.md`'s internal Fact), and $R$, being divisible by
every prime of $R(a_1)$ simultaneously, is divisible by whichever prime
covers each particular $a_i$ — correctly fixing the flaw the
outline-reviewer found in the prior draft (which only used the single
prime shared with $a_1$, insufficient for $i\ge2$ per the certified
`covering-membership-not-safety-certificate.md` trap). Correct.

**Fully solved instance $a_1=21$: $a_n=3(n+6)$, $T=1$, $L=3$.**
**Independently re-simulated** via exact-integer Python (no reliance on
the file's own claimed simulation): the greedy sequence for $a_1=21$ is
exactly $21,24,27,30,33,36,\dots = 3(n+6)$ for $n=1,\dots,40$, confirming
the closed form exactly. The inductive proof in the file (base cases
$a_1=21,a_2=24$ checked directly; inductive step using that $a_3=27=3^3$
has only prime factor 3, so $3\nmid m\Rightarrow m$ invalid, forcing
$a_n+3$ to be the next candidate) is correct and complete — this
genuinely and fully solves the problem for this one instance.

**General negative theorem** (eventually-constant gap $d^*<R$ implies
$\epsilon_n$ has exact period $R/\gcd(d^*,R)>1$, invisible to any bounded
window). Re-derived the modular-arithmetic argument independently
(orbit of $a_n\bmod R$ under addition of $d^*$ has exact period
$R/g$ in the cyclic group $\mathbb Z/R\mathbb Z$; correct). **Independently
re-simulated** the $a_1=21$ instance's $(d_n,b_n,\epsilon_n)$ sequence in
Python for $n=1,\dots,39$: confirmed $\epsilon_n=0$ exactly when $7\mid
n$ (period 7 exactly, matching $R/g=21/3=7$), matching the file's claim
term-for-term. The refutation of the round-3 outline's central "windowed
automaton" target is correct and not merely an unverified assertion — it
is a proven impossibility, realized concretely.

**Assessment of the approach's viability.** The approach's one
distinguishing idea this round (a windowed automaton on the compressed
relative-gap statistic, without tracking a cumulative/residue invariant)
is now proven incapable of working in general, and the builder honestly
states no replacement mechanism was found. This is the approach's first
build, so per the population's own precedent (a single refuted mechanism
on a first attempt was not sufficient to trigger RETHINK for
jacobsthal-covering-bound in round 2), I do not escalate to RETHINK this
round, but flag explicitly: next round this slug needs either a
genuinely new mechanism (the theorem itself points at tracking $a_n\bmod
R$ directly, which risks collapsing into the same framing as
active-set-stabilization / state-compactness-pigeonhole rather than
offering a diverse alternative) or should be treated as exhausted.

---

## Lemmas certified this round (all independently re-verified)

New files added to `results/imo-2026-06/lemmas/`:
- `self-type-compatibility.md`
- `soundness-and-exact-correctness.md`
- `reduction-lemma-ss1-vs-unified-claim.md` — the round's key structural
  result (unifies Gap 1 and Gap 2)
- `fact-d-recursion-as-good-minimum.md`
- `adjacent-link-lemma.md` (certified once, shared by
  jacobsthal-covering-bound and bounded-link-invariant, per their own
  coordination note)
- `lambda-stabilization.md`
- `finite-subtraction-vacuous.md` (negative)
- `legal-baseline-step.md`
- `windowed-epsilon-automaton-failure.md` (negative, includes the fully
  verified $a_1=21$ realized instance)
- `transient-free-finishing-theorem.md` (CONDITIONAL — labeled as such,
  depends on the still-open Unified Central Claim)

All certified after independent re-derivation and, where numerical claims
were made, independent Python re-simulation (exact integer arithmetic, no
floating point) cross-checked against the files' own reported numbers.
No discrepancies found.

## current.md updated

`results/imo-2026-06/current.md` updated: Status remains `partial`. The
central gap is now recorded in its round-3 unified form (existence of a
finite $Q\supseteq R(a_1)$ with every pair of terms sharing a prime factor
in $Q$) as the single fully open item, with the Reduction Lemma /
transient-free finishing theorem flagged as the round's key structural
advance (real progress in problem structure, not closure). Approaches
tried section extended with round 3 entries for all four slugs, each with
an explicit verdict.

## Ranking outcomes recorded

- active-set-stabilization: `advanced`
- state-compactness-pigeonhole: `advanced`
- jacobsthal-covering-bound: `partial`
- bounded-link-invariant: `partial`

---

**Verdicts summary:**
- active-set-stabilization — CHANGES REQUESTED (Status: partial)
- state-compactness-pigeonhole — CHANGES REQUESTED (Status: partial)
- jacobsthal-covering-bound — CHANGES REQUESTED (Status: partial)
- bounded-link-invariant — CHANGES REQUESTED (Status: partial)

No APPROVE this round; the problem remains unsolved. The central gap
(existence of a finite self-sufficient prime set $Q$) is now sharply and
correctly unified into a single statement but is not yet proved by any of
the four independent framings tried across three rounds.
