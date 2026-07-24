# Proof review — imo-2026-06, round 1

Problem: IMO 2026 P6. Sequence a_1 > 1, a_{n+1} = smallest integer > a_n with
gcd(a_{n+1},a_i)>1 for all i≤n. Prove eventual periodicity a_{n+T}=a_n+L for ALL n≥1
(not just eventually — the problem explicitly demands it from n=1).

Two approaches built this round. Both self-report Status `partial`. I independently
re-derived the load-bearing steps of each (not just read them) and ran numerical
checks in Python (`sympy`, direct greedy simulation up to n=20000 for several seeds).

---

## 1. amortized-charging-budget

### Lemmas checked line by line

- **Lemma 1 (Free fact, gcd(a_n,a_1)>1 for n≥2).** Correct, one-line consequence of
  the definition (index i=1 is always in range 1..n-1 for n≥2).
- **Lemma 2 (Bounded Gap Lemma, a_{n+1} ≤ a_n + a_1).** I re-derived this from scratch
  independently: let r = smallest multiple of a_1 exceeding a_n. For i=1, a_1 | r
  gives gcd(r,a_1)=a_1>1. For i=2..n, gcd(a_i,a_1)>1 (Lemma 1) gives a common prime
  q_i | a_1 | r and q_i | a_i, so q_i | gcd(r,a_i). Hence r is a valid candidate and
  minimality forces a_{n+1} ≤ r ≤ a_n+a_1. This is correct and matches numerics: for
  a_1 ∈ {15,35,143,1001} I measured max observed gaps of 6, 10, 22, 14 respectively,
  all ≤ a_1, consistent with (and not saturating) the bound. **Verified correct.**
- **Lemma 3 (Recurrent-pattern pigeonhole).** Trivial infinite pigeonhole on the
  finite set 2^Q \ {∅}. Correct.
- **Lemma 4 (Forced-linking-prime lemma).** Uses the *general* pairwise-gcd fact
  (gcd(a_i,a_j)>1 for ALL i<j, not just i=1) — this general fact is not stated as a
  separate named lemma here but is correctly derivable exactly as Lemma 1's proof
  generalizes (apply the defining property at index max(i,j)-1, taking the smaller
  index in its range). The proof then correctly applies finite pigeonhole on the
  fixed finite set P(a_i) against the infinite index set J_A. **Verified correct**,
  modulo the missing but easily-supplied general pairwise-gcd statement (this should
  be stated explicitly as its own lemma in a revision — a minor rigor gap, not a
  correctness gap, since the fact is true and the proof sketch given actually
  establishes it inline).

### The Core Lemma (Section 5) — the open gap

Correctly flagged as NOT proved. My assessment: this is the genuine crux of the
problem. Beyond being merely unproven, the **statement itself is not rigorously well
formed** — it says S must be "self-sufficient... whenever π(i),π(j) are such a pair
actually requires linking outside Q," which is not a crisp mathematical condition (the
phrase "actually requires linking" is not defined). This matters because Section 6's
"conditional finish" then partly just unpacks the Core Lemma's own built-in
self-sufficiency clause rather than deriving periodicity from an independently
checkable hypothesis (see e.g. the proof of Claim 6b, which twice invokes "this is
exactly the content of the Core Lemma we are assuming" for the two directions of the
inclusion). This is weaker evidence of progress than the write-up presents it as: the
"fully proved conditional" claim for Section 6 is true only in a fairly trivial sense,
since much of what it needs is smuggled into the Core Lemma's own (vague) statement.

**Compare to the sibling approach's (†):** covering-system-construction isolates
essentially the same gap but in a crisp, checkable form (see below). I recommend any
continuation of this approach adopt (†) as the target instead of the current Core
Lemma.

### n=1 boundary gap

Correctly and honestly flagged as unresolved, secondary, and downstream of the Core
Lemma. No proof attempted. This matches the true situation — the problem statement
requires the identity for every n≥1, and neither approach proves the eventual period
extends back to n=1.

### Verdict

Genuine, correct, non-trivial partial progress (Lemmas 1–4 hold up under independent
re-derivation and numerical spot-checks). The reported Status `partial` is accurate,
not overclaimed. The Core Lemma is not close to closing as currently stated — it needs
to first be reformulated into a crisp mathematical statement (adopt (†) below) before
it can even be attacked properly.

---

## 2. covering-system-construction

### Lemmas checked line by line

- **Free Facts 1–2.** Same as amortized-charging-budget's Lemma 1, but here the
  *general* pairwise-gcd fact (Free Fact 2) is stated and proved explicitly and
  correctly — this is strictly more careful than the sibling approach. Correct.
- **Step 1 (persistent types, double pigeonhole).** Correct: finite codomain 2^Q\{∅},
  infinite pigeonhole gives at least one persistent type; the complement argument
  (types not persistent occur finitely often each, finitely many such types, so
  finite total exceptional set, hence a threshold N_0) is a valid, careful double
  pigeonhole with no gap.
- **Bounded Witness Lemma (Step 2).** I re-derived this independently: fix A,B
  disjoint persistent types, ANY index m with τ(m)=B. For n>m with τ(n)=A, Free Fact 2
  gives gcd(a_n,a_m)>1, so a common prime p exists; if p∈Q then p∈τ(n)∩τ(m)=A∩B=∅,
  contradiction, so p∈P(a_m)\Q =: F_{A,B}, a FIXED finite set depending only on m (not
  n). **Verified correct**, and this is genuinely a stronger, cleaner result than
  amortized's Lemma 4: one arbitrary witness certifies ALL later same-type terms via a
  fixed finite set, with no need for pigeonhole over an unbounded family of witnesses.
  This is the round's best new lemma and I certify it as the preferred tool going
  forward (see `results/imo-2026-06/lemmas/bounded-witness-lemma.md`).
- **Finite Core Theorem (Step 3).** Direct, correct application of the Bounded Witness
  Lemma to one fixed witness m_B per persistent type B∈𝒫 (|𝒫| ≤ 2^{|Q|}-1 many),
  giving an explicit finite union S. **Verified correct** — no growth-rate or density
  argument is smuggled in, contrary to the outline's earlier heuristic approach; this
  really is a closed-form, one-pass construction.

### The gap (†) — precisely diagnosed and correctly identified as open

I checked whether the Finite Core Theorem's conclusion ("a_n meets S for each disjoint
persistent B, n large") is enough to finish, and confirmed the builder's own diagnosis
is correct: the theorem only shows a_n meets the SPECIFIC witness-derived set F_{A,B}
for each B individually; it does not show a SINGLE fixed extended type ρ(n)=P(a_n)∩S_0
(which subsumes reconciliation with every disjoint B simultaneously) is realized
consistently across all n with τ(n)=A. Several distinct extended-persistent
refinements of the same base type A could in principle coexist without pairwise
intersecting. This is a real, unclosed gap — I did not find a way to close it in the
time available, and I do not believe it is a routine finish (see numerical exploration
below).

**Independent numerical exploration (this review, not in the builder's report):** for
a_1=15 (Q={3,5}), I tabulated the "extended patterns" (P(a_n) \ Q) for all terms of
type {3} and of type {5} among the first 3000 terms: there are hundreds of distinct
extended patterns for each base type (476 for type {3}, 286 for type {5}), i.e. the
naive "extended type" space does NOT collapse to a small finite set of literal
patterns P(a_n)\Q — confirming (†) is not a shallow finiteness fact about the full
factorization. However, restricting to S_0 = Q ∪ {2} (the actual reconciling prime
found in this case), essentially every large term shares the prime 2 with every other
large term of a different singleton type, EXCEPT for a stable ~1/8 fraction of odd
terms per period (I verified the odd-term frequency converges to exactly 1/8, matching
the reported true period (T,L)=(8,30) for this seed, over n up to 20000). This
confirms the qualitative structure behind (†) is real and finite in practice, but also
shows the actual reconciling mechanism is subtler than "eventually always divisible by
2" — some terms are never linked via 2 and must be linked via Q itself (i.e., some odd
terms of type {3} must reconcile with type {5} terms directly through — this needs
further inspection but is out of scope for this review). This numerical evidence
supports that (†) is TRUE for at least this seed, but gives no route to a general
proof; the extended-type space is large and only "effectively" collapses via the
actual periodic structure, which is what we are trying to prove in the first place —
so no non-circular numerical shortcut is available.

### Step 5 (CRT + cyclic pigeonhole, conditional on (†))

Checked this derivation for internal validity, GIVEN (†) as a clean hypothesis: CRT
reduces S_0-divisibility to residues mod L=∏S_0; G := residues whose S_0-signature is
extended-persistent; the greedy rule restricted to G is well-defined and cycles with
period T=|G|, giving a_{n+T}=a_n+L for n beyond a threshold. This derivation is
correctly structured and, unlike the sibling approach's Section 6, does NOT smuggle
the needed content into the hypothesis's own wording — (†) is used honestly as an
external input. Minor residual hand-wave: "the finitely many early/transient terms...
a finite, checkable exceptional list" is asserted rather than spelled out, but this is
a genuinely finite, mechanical claim (unlike (†) itself) and is a reasonable thing to
leave to a routine follow-up. Not a correctness issue, just an unfinished detail.

### n=1 boundary gap

Same status as the sibling approach: honestly flagged, unresolved, downstream of (†),
supported only by numerical evidence on 4-5 seeds (I also confirmed it holds for
a_1=15 up to n=20000 in my own simulation, though I did not check it constitutes a
proof — it is not one).

### Verdict

Genuine, correct, and comparatively sharper progress than the sibling approach: the
Bounded Witness Lemma and Finite Core Theorem are both fully rigorous, self-contained,
and strictly upgrade the analogous results elsewhere. The gap (†) is the cleanest
available statement of the problem's true crux produced so far this round. Status
`partial` is accurate.

---

## Cross-approach comparison and recommendation for next round

Both approaches converge on the same underlying crux, but covering-system-construction
states it more precisely (†) and with fewer hidden circularities than
amortized-charging-budget's Core Lemma. Recommend:

1. Certify and promote (already done, see `results/imo-2026-06/lemmas/`): Free Facts,
   Bounded Gap Lemma, Persistent-Type Pigeonhole, Bounded Witness Lemma (preferred over
   the weaker Forced-Linking-Prime Lemma, which is also certified but flagged
   superseded), Finite Core Theorem.
2. Both approaches' remaining gap ((†) / Core Lemma) is the same underlying wall and
   has now resisted two independent, careful attempts. It is very plausibly the actual
   IMO-hard content of this problem (difficulty 9/10), not a bookkeeping gap. The
   orchestrator's "break a shared-gap plateau" guidance applies: the population should
   NOT spend round 2 just patching (†) with more pigeonhole bookkeeping — that is
   demonstrably where both current approaches independently got stuck.
3. Suggest a genuinely different framing for at least one new round-2 approach, e.g.:
   a minimality/exchange argument showing directly that the greedy rule, once it has
   linked two disjoint persistent types via some prime, can never thereafter prefer a
   candidate that reintroduces a fresh unlinked extended type (a monovariant on
   "distance to the nearest good residue," rather than trying to bound the raw set of
   primes used); or a direct approach via known structure of "covering systems" /
   Bertrand-type gap estimates comparing the density of multiples of a candidate
   reconciling prime vs. the sequence's own growth rate (using the certified Bounded
   Gap Lemma as the growth input) to force reuse of a bounded prime pool. Neither
   approach's builder attempted a monovariant/exchange argument; this is the most
   promising unexplored angle.
4. Do not re-attempt amortized-charging-budget's Core Lemma in its current vague
   wording — first replace it with (†) or an equally crisp statement before any
   further build round.

---

## current.md

Updated `results/imo-2026-06/current.md` (reviewer-owned) to Status `partial`, merging
the two approaches' certified lemmas into "Current best," stating the crux gap (†) in
its cleanest form, and recording the secondary n=1-boundary gap and the numerical
evidence gathered in this review.

## Promotable lemmas — certification decisions

All lemmas flagged as promotable by both builders were checked against the full bar
(no hidden `sorry`/hand-wave, statement no stronger than proved) and admitted:

- `results/imo-2026-06/lemmas/free-facts-gcd.md` — ADMITTED (merges amortized Lemma 1
  + covering Free Facts 1–2 into the general pairwise-gcd statement).
- `results/imo-2026-06/lemmas/bounded-gap-lemma.md` — ADMITTED (amortized Lemma 2).
- `results/imo-2026-06/lemmas/persistent-type-pigeonhole.md` — ADMITTED (merges
  amortized Lemma 3 + covering Step 1).
- `results/imo-2026-06/lemmas/bounded-witness-lemma.md` — ADMITTED (covering Step 2;
  the strongest, preferred version).
- `results/imo-2026-06/lemmas/finite-core-theorem.md` — ADMITTED (covering Step 3),
  with an explicit caveat appended warning downstream users that it does NOT establish
  (†).
- `results/imo-2026-06/lemmas/forced-linking-prime.md` — ADMITTED (amortized Lemma 4)
  but flagged superseded by `bounded-witness-lemma.md`; kept for the record since it is
  independently correct, not because it should be preferred.

No lemma was rejected — both builders' promotable claims held up under independent
re-derivation and are correctly scoped (none claims more than what its proof
establishes).

---

verdict: amortized-charging-budget = CHANGES REQUESTED
verdict: covering-system-construction = CHANGES REQUESTED
