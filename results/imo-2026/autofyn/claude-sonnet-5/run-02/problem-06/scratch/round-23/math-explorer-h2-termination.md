## imo-2026-06 (lens: H2 self-absorbing-core termination, route DIFFERENT from one-prime-at-a-time adjoin)

### What H2 precisely claims (from current.md's Master Conditional Theorem + certified lemmas)

Fix Q = P(a_1), S₀ ⊇ Q the explicit finite core from the certified **Finite Core
Theorem** (`lemmas/finite-core-theorem.md`): S₀ := ⋃_{B∈𝒫} (P(a_{m_B})\Q), a union
over each persistent base type B of the prime factors (outside Q) of one canonical
witness index m_B. For any finite S ⊇ Q, ρ_S(n):=P(a_n)∩S, 𝒫'(S) the (certified,
generic-in-S) finite set of S-persistent extended types, N(S):=max exceptional index
(0 if none). Absorption operator S⁺ := S ∪ ⋃_{j=1}^{N(S)} P(a_j). S is
**self-absorbing** if S⁺=S. **H2 = "∃ finite self-absorbing S* ⊇ S₀"** (existence),
which by the certified **Termination Criterion Lemma** is *equivalent* to
boundedness of the adaptive chain's threshold sequence (N(S_k))_{k≥0},
S_{k+1}:=S_k⁺, S_0 as above. Given H2 (+ H1=FAH at level S*), the certified
**Self-Absorbing Core Theorem** delivers periodicity for n ≥ N(S*) (and, via the
certified **Literal n=1 Periodicity Theorem**, actually from n=1). **H2 is
logically independent of H1**: it is a statement about *when* extended types
stabilize (an onset/pigeonhole-threshold question), not about *whether stabilized
types intersect each other* (H1's content) — this independence was explicitly
checked, not just assumed, in rounds 15/19/20, and no reduction either direction
has ever been found.

### The dead route (confirm the round-19 RETHINK is real, not just labeled)

`core-growth-monotonicity` tried, twice (round 16 on the adaptive chain S_k, round
19 on an explicit monotone family S_M := S₀∪⋃_{j≤M}P(a_j)), a **one-prime(or
one-term)-at-a-time inductive/recursive** attack: derive an exact recursion for how
N(S) changes when the core grows by one prime (Binary Refinement Lemma; Threshold
Recursion Bound Lemma, both certified, correct), then try to bound the resulting
per-type "last exception" quantity M_B. This is proved dead, not just
stalled: **Proposition 3 (Non-Constructivity of M_B)**, re-checked by me — the
argument is genuinely a "two consistent finite-prefix extensions" construction (for
any K, both "p divides a_n for all n∈I_B beyond K" and "p divides a_n at exactly one
arbitrarily-late n₀>K" are consistent with any fixed data on [1,K]), so **no
function of bounded-prefix data can compute or bound M_B, period** — this is a
structural fact about induction on finite prefixes, not a workspace-tooling gap. I
re-derived this from scratch and it holds: any future attack that tries to
*inductively bound the core's growth one recruitment step at a time from finite
data* will hit exactly this wall. This is the strongest-confirmed dead end in the
whole H1/H2 landscape — stronger than any single H1 mechanism's death, because it's
a **proof of impossibility for an entire technique family** (bounded-prefix
induction), not just one failed instance.

### A genuinely different route: attack N(S₀)=0 (or Exc(S₀)=∅) DIRECTLY as a single concrete claim, not via chain induction

This is the one opening I found that is structurally distinct from the
adjoin-one-prime induction, and it has NOT been attempted as its own target
anywhere in the workspace (grep of `approaches/` and `lemmas/` for "N(S_0)"/"N(S₀)"
returns only the abstract lemma files, never a dedicated attack on the concrete
claim for the EXPLICIT S₀).

The key distinction: Proposition 3's non-constructivity wall applies to bounding
M_B (a quantity produced by an INDUCTIVE recursion built up one prime at a time
from an a priori unknown starting point). It says nothing about whether a **direct,
non-inductive, structural argument** can show the single concrete, already-fully-
specified set S₀ (no free parameter — S₀ is pinned down explicitly by the Finite
Core Theorem's own canonical-witness construction) is itself self-absorbing, i.e.
that Exc(S₀) = ∅ (or at least that S₀⁺ = S₀, which is weaker and suffices).

Why this might be tractable via a DIFFERENT mechanism than induction: S₀'s
definition already bakes in, for every persistent base type B, a canonical witness
m_B whose full factorization is folded in. The certified round-3 **Canonical
Refinement** finding (see `math-explorer` rule 4 in `/tmp/memory/math-explorer.md`)
showed m_B's own extended type is exactly B ∪ F_B "for free," and the Bounded
Witness Lemma is valid for ALL n with τ(n)=A (not just m_B), which is exactly the
kind of *closed-form, non-adaptive* fact (holds by direct computation from the
Finite Core Theorem's construction, no recursive chain) that could power a direct
argument that ρ_{S₀}(n) is persistent for every sufficiently structured n, avoiding
the "does p divide a_n infinitely often" binary-tail question that killed the M_B
route. I did NOT attempt to write this proof (out of scope for exploration) — I
flag it as the concrete gap for the outliner: **can Exc(S₀)=∅ (or S₀⁺=S₀) be shown
directly from the Finite Core Theorem's own witness construction, without ever
asking "is I_B^0 or I_B^1 infinite" for some newly-adjoined prime?**

### Numeric support for this direct target (already on record, re-verified reading, not re-run by me this pass)

Rule 21 in `/tmp/memory/math-explorer.md` (round 17 finding): once the sampling
window is large enough (20,000–30,000 terms, not the earlier 6,000–12,000 that gave
a false "still growing" read), **N(S₀)=0 for 9/9 tested seeds** with |Q|≤4
(15,35,105,175,320,1001,2431,4807,11305 — including BOTH of the workspace's only
two known genuinely hard, properly-recruited-core FAH seeds, 4807 and 11305). Only
the one |Q|=5 seed (15015) is inconclusive even at 60,000 terms (proxy becomes
unreliable once |S| passes ~500–3500 primes — a sampling-depth issue, not
counter-evidence). This is real, if incomplete, conjecture-level support (labeled
as such, NOT proof) for exactly the "attack S₀ directly, it's probably already
self-absorbing with zero exceptions" target above, on the workspace's two hardest
known cases. If this direct claim is true, H2 essentially collapses to nothing —
S*=S₀ trivially, and periodicity would even hold from n≥1 for free via the already-
certified Literal n=1 Periodicity Theorem, once H1/FAH at level S₀ is separately
established. Note: this reuses the round-21/22 exact-period-detection tooling
(bitmask sieve + Z-function O(N) detector) as the right instrument for a deeper,
larger-window check on the |Q|=5 case if the outliner wants stronger evidence before
committing a builder.

### Is H2 more tractable than H1 right now?

Honest assessment: **not clearly**, but for a different reason than "equally hard."
H2's *known* attack family (bounded-prefix chain induction) is now **provably
dead as a technique class** (Proposition 3), which is actually a *stronger*, more
conclusive negative result than anything H1 has (H1 has 31+ individually-dead
mechanisms but no proof that no mechanism can work). The direct-S₀ route above is
genuinely untried and structurally different (non-inductive), and the numeric
evidence (N(S₀)=0 on both known hard seeds) is at least as strong as any positive
evidence currently backing an H1 mechanism. I'd rate it a **plausible, concrete, and
underexplored target for a plateau-break approach slot**, distinct from all
existing H1-focused approaches — worth one build-set slot, not a replacement for
continued H1 work.

### Other candidate mechanisms considered and their status

- **Finiteness/compactness on the union of ALL ever-recruited primes.** Dead:
  rule 23 in `/tmp/memory/math-explorer.md` shows this is circular with H2 itself
  (no independent finiteness source; the certified fact that total prime SUPPORT of
  the sequence is unbounded, round 2, applies with equal force). Do not re-propose.
- **Ordinal/well-ordering argument on the absorption chain.** No natural ordinal
  rank is apparent (the chain's steps are not literally decreasing anything; N(S_k)
  is not monotone under enlargement per certified **Proposition 5 / Non-Monotonicity
  Gap** in `core-growth-monotonicity.md` — self-absorption is NOT known preserved
  under further core enlargement). An ordinal-rank argument would need exactly the
  monotonicity fact Prop 5 shows is currently unavailable; not viable as stated
  without first supplying that missing monotonicity theorem (itself an open,
  possibly-hard sub-target).
- **Reusing Legendre Sieve Gap Bound / Primorial Floor Bound (round 22, certified)
  in a termination-counting role.** These are inclusion-exclusion sieve bounds on
  "how long can a residue-class-covering process go before some fixed modulus M is
  hit," used in the a1-3q proof to bound gap sizes given a FIXED covering modulus.
  Speculative but plausible reuse: if S₀ (or S_M) can be shown to induce, via CRT, a
  *fixed* covering system over ⋃_p{residues divisible by p, p∈S₀} that the sequence
  must eventually land in cofinitely, a sieve-style DIRECT global counting bound
  (not an inductive per-prime chain) could in principle bound N(S₀) without ever
  asking the binary "infinite tail" question that killed M_B — this is the same
  spirit as the direct-S₀ target above, just naming a candidate tool. Not verified
  to actually apply; flagging as a technique to try, not a proven route.
- **Crux corpus.** Filtered `number_theory`+`combinatorics` subtopics
  `processes-and-algorithms`, `invariants-and-monovariants`, `pigeonhole`,
  `size-bounding-and-descent` (124 candidates) for termination/absorption/greedy
  keywords. `aimo-0477` (divisor-chain-bounded-by-a-fixed-integer) is already
  imported and dead (rule 9). `aimo-0077` (minimal-index-in-a-cycle / minimal
  counterexample) is structurally the same shape as the workspace's several already-
  dead minimal-counterexample/well-ordering attempts (rounds 3, 5) — not
  recommended without a genuinely new angle. `aimo-0264` (ordinal-rank via nested
  exponential tower) is intriguing in the abstract but I found no natural
  monotone-decreasing quantity in this problem to hang such a rank on — would
  require first solving the Non-Monotonicity Gap above. No crux in the corpus is a
  close structural analog to "does a greedy-recruited finite core of primes
  eventually stop growing" — this problem's process (existentially/adaptively
  defined recruitment against an infinite deterministic tail) doesn't match the
  corpus's termination cruxes, which are almost all either (a) explicit
  monovariant/potential arguments on a FINITE, fully-visible state (not applicable:
  our "state" — the eventual tail behavior — is exactly what's unknown), or
  (b) algebraic-recurrence induction (already ruled out for this problem per rule
  12, no closed-form recurrence exists here).

### Cheap-kill candidates
None obvious for H2 itself beyond what's already found (the circularity check on
"total prime support finite," rule 23). No new cheap kill found this pass.

### Analogous past problems (cruxes)
None found that are genuinely analogous (not just same-subtopic) — see corpus
discussion above. `aimo-0477` is the closest match and is already imported/dead.

### Dead ends (do not retry)
- One-prime-at-a-time / bounded-prefix-data inductive attack on N(S) or M_B for
  H2 (Proposition 3, `core-growth-monotonicity.md` — a proof of impossibility for
  the whole technique class, not just one instance). Includes both the adaptive
  S_k chain (round 16) and the explicit monotone S_M chain (round 19).
- "Total prime support of the whole sequence is bounded" as an H2 shortcut —
  circular (rule 23).
- Compactness/König's-lemma-style arguments for H2 without a genuine finite-
  branching bound on the recruited-prime pool (rule 20 — no such bound exists;
  the recruited pool IS the unbounded object in question).

### Small-case / intuition notes (conjecture, not proof)
Numeric evidence (round 17, re-verified this pass as still-standing per the memory
rules, not independently re-simulated by me this round due to time budget) supports
the conjecture **N(S₀) = 0 for essentially every a₁** (9/9 tested seeds with |Q|≤4,
including both known hard FAH seeds 4807/11305), i.e. the Finite Core Theorem's own
canonical S₀ is *already* self-absorbing with zero exceptions, making H2 trivial in
practice even though no proof exists. This suggests H2's real difficulty is not
"the core keeps growing forever" (which the evidence argues against) but "proving
zero growth is needed" without an inductive/bounded-prefix argument — exactly the
gap the direct-S₀ route above targets.
