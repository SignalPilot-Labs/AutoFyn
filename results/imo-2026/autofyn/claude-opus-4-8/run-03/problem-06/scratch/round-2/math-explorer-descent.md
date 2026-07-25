## imo-2026-06 (lens: descent / monovariant route to Finite Alphabet)

### Setup recap (certified, not re-derived)
Everything except the **Crux (Finite Alphabet)** is proved: F_n=primes(a_n), 𝓐_∞ =
⊆-minimal elements of 𝓕={F_n}, A={c : c meets every F∈𝓐_∞}, s=min-successor on A.
`a_{n+1}=s(a_n)` for ALL n≥1 (no transient). If 𝓐_∞ is finite, periodicity with
explicit T=|ρ(A)|, L=∏Π follows completely. Free lemmas L1–L4 (Anchor, Gap≤M,
Distance–prime, Pairwise-intersecting) are certified and framing-agnostic.
**Recorded refutation, respected here:** confinement `p|L ⇒ p≤M` is FALSE
(a_1=375 ⇒ 19|L=3990, M=15). No sub-opening below relies on a bound `p≤M`.

### Distinct sub-openings for the descent/monovariant route

**(D1) Density monovariant on A — NEW, genuinely different from all three existing
approaches.** Facts (a_{n+1}−a_n≤M, unconditional, from L2) show A (which by the
certified no-transient lemma equals exactly the term-set {a_k}∩[a_1,∞), enumerated
in order — no skipped elements) has **natural density ≥ 1/M > 0**. If 𝓐_∞ were
infinite, one might hope inclusion–exclusion density of "meets every F∈𝓐_∞" forces
density(A)→0, contradicting density≥1/M. **This is the natural monovariant
candidate: density of the admissible set as a function of how many minimal
constraints are imposed.**

*Where it breaks (important, tested carefully, not just asserted):* the poset
counterexample already on file (§7(b) of `redundant-constraint-antichain`),
`{{p*}∪{q} : q large prime}` for a fixed p*, is an infinite ⊆-antichain, yet
`A = {c : ∀q, p*|c or q|c}` collapses to **exactly** the multiples of p* (any c not
divisible by p* would need to be divisible by *every* q in an infinite family,
impossible), so density(A)=1/p* — no contradiction. Worse: the certified pigeonhole
fact **(c) in §7 of `redundant-constraint-antichain`** ("if 𝓐_∞ is infinite, by
pigeonhole on the finite set P=primes(a_1), infinitely many minimal supports share a
fixed p*∈P") shows this *is exactly the scenario forced* if 𝓐_∞ is ever infinite —
not a pathological edge case to dismiss. **So the naive density argument does not
close the crux; it structurally cannot, because the only way 𝓐_∞ can be infinite is
via this p*-anchored family, and that family does not drive density to 0.**

**This failure mode is itself the most useful finding of this pass**: it exposes
that "𝓐_∞ finite" may be a **strictly stronger, harder statement than what the
theorem actually needs**. In the counterexample scenario, even though 𝓐_∞ is
(hypothetically) infinite, A itself is *still* eventually a single residue class mod
p* — i.e. still finitely-generated / periodic. **Sub-opening (D1′): reformulate the
crux directly as "A is a finite union of residue classes mod some finite L"
(equivalently, A is a periodic subset of ℤ) rather than "𝓐_∞ is finite."** This is
weaker (𝓐_∞ finite ⇒ A periodic via Lemma 9, but not conversely — the p*-family
shows a strict gap) and may be provable by a direct compactness/density argument on
A itself, sidestepping the combinatorics of antichains entirely. This is a genuinely
different top-level target the outliner should consider as its own approach, not a
patch to the antichain one — it changes what must be proved.

**(D2) Distance–prime + counting/energy bound on "new large-prime recruitments."**
For a prime q to become a sole witness linking two terms a_i,a_j (i<j), L3 forces
j−i ≥ q/M (roughly, since a_n=Θ(n)). So a large prime q can be "freshly used" between
a bounded number of term-pairs per window of N terms: at most O(N/q) opportunities
in the first N terms. Total prime-incidences needed to keep the pairwise-intersecting
property (L4) alive for all C(N,2) pairs is bounded by N·(avg number of prime
factors) ~ N log N (by trivial factor-count bounds), while each large prime q>M
contributes protection to at most O(N/q) pairs. Summing 1/q over "new" primes that
must appear gives a harmonic-type bound — **but this only bounds total pair-covering
demand, and pairwise-intersecting is not literally what's driving new supports into
𝓐_∞ (a pair can be covered by an OLD small prime just as well); this line does not
by itself bound the number of *minimal* supports** (an old small-prime cover doesn't
prevent a later term from having a new-prime-only support). Flagging as a partially
promising but currently **inconclusive** counting sketch — worth a further pass, but
do not present it as more than a sketch; the reduction from "pair covering demand" to
"antichain size" is the missing link.

**(D3) Churn monovariant on the finite-prefix antichains 𝓐_k (empirically strong,
mechanism not yet proved).** Numerically (§ below) the antichain of the first k
supports, 𝓐_k := minimal elements of {F_1,...,F_k}, **stabilizes** (stops changing)
after a bounded number of updates, and the total churn (number of k at which 𝓐_k
changes) is small and seems tied to the number of distinct prime factors of a_1.
Mechanism candidate: a support F_i containing a large prime q gets **dominated**
once a later term's support becomes a subset of F_i (e.g. once the "small companion"
prime-set of some other multiple of q — or an unrelated small-support term — appears
as ⊆ F_i). This matches §7(a) of `redundant-constraint-antichain` exactly ("small
companion eventually dominated"). **No proof of why domination must eventually
happen for every large-prime support; this is the same content as the stated Crux,
just viewed as a churn-finiteness claim instead of a set-finiteness claim** — so D3
is a reformulation, not a new attack, but it does suggest the right monovariant
*shape*: "number of antichain updates so far" as a quantity to try to bound above by
an explicit function of the primes in P=primes(a_1) (finite data), which would prove
finiteness of 𝓐_∞ directly by termination of updates.

### Cheap-kill candidates
- **Density lower bound ≥ 1/M is free and unconditional** (from L2, already
  certified) — usable as the "target contradiction" for any density-based route.
  Cheap to state, does not need re-proving.
- **Pigeonhole-on-P is free** (§7(c), already certified as a partial fact): IF 𝓐_∞
  is infinite, infinitely many of its members share a common p*∈P (P is finite,
  from a_1). This immediately rules out attacking the Crux by contradiction "assume
  𝓐_∞ infinite, derive primes escaping to infinity independently" — they are NOT
  independent; they are all anchored through a shared p*. Any approach that doesn't
  route through this anchoring structure is attacking a strictly easier (and false
  to assume) sub-case.
- **No M-threshold anywhere.** Confirmed still false; don't let any sub-opening
  smuggle back a "large primes are p>M" cutoff (D2 above deliberately avoids this,
  using q/M as a *pair-distance* bound, not a threshold on q itself — that distinction
  matters and should be kept explicit in any writeup).

### Knowledge-base entries to use
- **Modular arithmetic / CRT** entries — for making the "A is periodic mod L"
  reformulation (D1′) rigorous: A determined by finitely many prime congruences is
  exactly a CRT statement.
- **Pigeonhole / extremal principle** entries — underlie the certified §7(c) fact
  and any churn-bound (D3).
- **Invariants and monovariants** general heading — the natural home for D1/D3, but
  note the KB doesn't have a ready-made density-of-covering-system lemma; this would
  need to be built from scratch (elementary inclusion–exclusion / CRT, not exotic).
- Nothing in the KB currently packages "density of the set avoiding a covering
  system of congruence-defined constraints" as a named tool — this is the gap where
  a new small lemma (not a KB citation) would have to be built if D1/D1′ is pursued.

### Analogous past problems (cruxes)
- **aimo-0421** (gcd of infinite set): crux "gcd of a fixed element with infinitely
  many varying partners takes only finitely many values ⇒ pigeonhole a constant gcd
  subfamily." Analogous *technique* (pigeonhole on divisors of a fixed quantity) but
  the problem itself (structure of gcd-multisets in infinite sets) is not close to
  ours — no periodicity, no greedy process. Weak analogy, technique-only.
- **aimo-0275** (f with a−b | f(a)−f(b), prove infinitely many primes divide values):
  crux "if only finitely many primes p_1..p_m divide all values, pick an argument
  divisible by a high power of each to force two values equal, contradiction." This
  is the *mirror image* of our crux (they prove a prime set is infinite; we want to
  prove one is finite) but the proof mechanics — using p-adic valuation sandwiching
  against a divisibility hypothesis to derive a forced coincidence — is a genuinely
  transplantable idea IF our problem had an analogous "difference divides" structure.
  Ours only has "shares a prime with," which is weaker (no valuation control), so
  this crux does **not** port directly; flagging as the most conceptually-similar
  hit in the corpus but ultimately **not a match** — do not force it.
- **aimo-0212** (rad(f(n)) | rad(f(n^rad(n)))): crux "every prime dividing values
  lies in a fixed finite set ⇒ polynomial is constant." Same "finite prime set"
  target shape as our Crux, but the mechanism (iterating n ↦ n^rad(n) and Fermat's
  little theorem) is specific to polynomial evaluation and doesn't transplant to a
  greedy integer sequence. **No genuine match**; noting only because the target
  shape (finite prime divisor set) rhymes.
- **Conclusion: no crux in the corpus is a genuine analog of this problem.** The
  problem's greedy/gcd-covering-system structure appears to be sui generis in the
  corpus (searched combinatorics `processes-and-algorithms`, NT `pigeonhole`,
  `modular-arithmetic-and-CRT`, `divisibility-and-gcd`, `size-bounding-and-descent`,
  `invariants-and-monovariants`, plus keyword search for "greedy/gcd/covering
  system/density/smallest positive integer" — nothing resembling a greedy
  covering-congruence sequence with periodicity conclusion turned up).

### Prior progress
Reduction to the single Crux (Finite Alphabet) is complete and certified (see
`current.md`, `lemmas/free-lemmas.md`, `lemmas/no-transient-fixed-successor.md`).
No new proof progress from this pass — this report is reconnaissance only, per
instructions (no full proof attempted).

### Dead ends (do not retry)
- **M-threshold confinement `p|L⇒p≤M`** — FALSE (a_1=375 counterexample). Certified
  refutation; already recorded, respected here.
- **Naive density-driven contradiction ("𝓐_∞ infinite ⇒ density(A)→0")** — refuted
  above by the p*-anchored antichain family, reinforced by the certified pigeonhole
  fact showing that family is exactly what infiniteness of 𝓐_∞ would force. Do not
  attempt this exact contradiction; if density is used, it must be combined with the
  reformulated target (D1′: A periodic, not 𝓐_∞ finite) to have any chance.
- **"Distance-prime + pair-covering counting ⇒ antichain size bound" (D2 as stated)**
  — the link from pair-covering demand to antichain-size is currently missing; do
  not present D2 as more than an unverified sketch.

### Small-case / intuition notes (conjecture, from simulation this round)
- For seeds 105, 385, 1155, 35, 15, 375, 5005 (up to 400–600 terms), the finite-prefix
  antichain 𝓐_k **always stabilizes** after a bounded number of steps (churn count
  42 for a1=1155 over 600 steps, last change at k=75; 56 for a1=5005, last change at
  k=104) and never changes again — strong (but non-proof) evidence for finiteness of
  𝓐_∞ in every tested case, and specifically for the "eventual domination" mechanism
  in D3.
- Notably for a1=1155, the antichain at k=50 had **13 members including large primes
  23,29,43,47,53,59,83,89**, all of which got dominated and vanished by k=100,
  leaving the final 5-element antichain {2,3,5,7,11}. This is direct numerical
  confirmation that large primes recruited early are typically *transient* in the
  antichain (get dominated later) — consistent with, but not a proof of, the Crux.
  This is exactly the phenomenon any successful monovariant (D3) needs to explain.
- No simulated seed produced the pathological p*-anchored infinite-family behavior
  (D1's counterexample) — it remains a purely hypothetical poset obstruction, not
  witnessed dynamically. This is weak evidence that the actual greedy dynamics never
  realize it, but it is NOT a proof that they can't; ruling it out (or absorbing it
  via D1′) is exactly the open mathematical content.
