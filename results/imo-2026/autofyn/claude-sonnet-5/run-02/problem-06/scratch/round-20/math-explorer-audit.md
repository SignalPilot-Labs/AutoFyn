## imo-2026-06

### 1. Audit of the Master Conditional Theorem chain — result: GENUINELY GAP-FREE, no discrepancy found

I traced every citation in `results/imo-2026-06/current.md`'s "Current best" (round-16
picture) and in `approaches/n1-periodicity-reconciliation.md` §0–§2 to its actual
certified lemma file, and cross-checked hypotheses/conclusions:

- `free-facts-gcd.md`, `persistent-type-pigeonhole.md`, `finite-core-theorem.md`,
  `extended-persistent-type-pigeonhole.md` — read in full; `extended-persistent-
  type-pigeonhole.md` is stated generically "at any finite core S₀ ⊇ Q", exactly as
  §0.4 of the reconciliation file uses it "at level S" for arbitrary S (including
  S* later) — this generic-core reuse is legitimate, not smuggled.
- `self-absorbing-core-theorem.md` — statement, proof (Sufficiency/Landing/
  Assembling), and its two disclosed open sub-gaps (a) existence/termination of
  S*, (b) N(S*)=0, match exactly what §0.5 and §1 (H1, H2) of the reconciliation
  file say. The round-14 "Precision note" proving "FAH at every element of 𝒫'(S*)"
  ⟺ "FAH at disjoint-base-type pairs only" is present and correctly cited — this
  closes what could otherwise have been a hidden strengthening of H1.
- `universal-early-intersection-lemma.md` — unconditional (no FAH needed), proves
  P(a_j) ∩ B ≠ ∅ for j ≤ N(S*), B ∈ 𝒫'(S*); this is exactly what §0.6 claims and
  is exactly the ingredient §7's extension proof (in `literal-n1-periodicity-
  theorem.md`) needs to cover the new range n+1 ≤ N(S*) in Landing's second
  conjunct. Checked: no circularity (it does NOT use FAH, only Free Facts + the
  bare infinite-occurrence definition of persistence).
- `literal-n1-periodicity-theorem.md` — same two hypotheses as the Self-Absorbing
  Core Theorem verbatim (no new hypothesis introduced), extends the conclusion
  from n ≥ N(S*) to n ≥ 1. Matches §0.7 exactly.
- `termination-criterion-lemma.md` — genuine iff (S_k terminates ⟺ N(S_k)
  bounded), fully unconditional, matches §0.8/§1(H2) exactly; the (⟸) direction's
  "fixed P*_M built only from a_1..a_M, not from S_k" non-circularity claim is
  correct on inspection (the induction step correctly upper-bounds S_{k+1} using
  N(S_k) ≤ M, not any property of S_k itself beyond monotonicity).
- The final assembly (§2, Master Conditional Theorem) is a one-paragraph
  chaining: H2 + Termination Criterion ⟹ some S* is self-absorbing; H1 (stated
  relative to that specific S*) + Self-Absorbing Core/Literal-n=1 Theorem's two
  hypotheses ⟹ conclusion. This is a correct instantiation, not a new claim.

**Conclusion: the chain is exactly as advertised — every step traced to a real,
independently-certified file, hypotheses match how they're invoked, no
discrepancy, no hidden strengthening, no circularity in the *conditional* chain
itself.** (The circularity flagged by round 19's reviewer is in the *separate*,
NOT-yet-certified §7 Generalized Class-Blindness Obstruction meta-lemma, which is
explicitly NOT part of the Master Conditional Theorem chain and does not affect
its correctness — confirmed this is accurately reflected in current.md's Status.)

Also independently spot-verified Theorem A (`even-seed-literal-periodicity-
theorem.md`) and Theorem B (`prime-power-seed-literal-periodicity-theorem.md`):
both are fully self-contained (no dependence on H1/H2/the S₀/S*/FAH apparatus at
all), and their stated non-overlap-except-at-`a_1=2^k` claim is correct by
direct inspection of their hypotheses (`2|a_1` vs `a_1=p^k`).

### 2. NEW candidate third subfamily found and numerically hardened: `a_1 = 3q`, q prime, q ≠ 5

Distinct from the round-19-refuted `a_1=p*q, q≫p` family (that refutation used
larger p, e.g. p=13, and found "messy, no monotone threshold" behavior). I tested
the SMALLEST possible p specifically, p=3 (the smallest odd prime — one step up
from the already-solved p=2 case), against every prime q:

**Numerical evidence (independently run, scripts described below).**
- For `q ∈ {7,11,13,...,113}` (all primes in [5,120) except checking q=5
  separately): computed the literal sequence `a_n = a_1+3(n-1)` matches the true
  greedy sequence for **all 400 terms tested**, with **zero exceptions** except
  at `q=5` (`a_1=15`, the already-documented Odd-Prime Non-Trivialization
  counterexample from round 18/19 — `n1-periodicity-reconciliation` §6.1).
- Extended to `q ∈ [131,151]` (5 more primes) at 600 terms: clean, zero
  exceptions.
- Extended to `q ∈ [150,500)` (all primes in that range) at 150 terms: clean,
  zero exceptions.
- **Total: every tested prime q ≥ 7 gives EXACT literal periodicity
  `a_n = 3q + 3(n-1)` for all n in the tested window (T=1, L=3), i.e. the SAME
  shape of result as the certified `a_1=p^k` theorem, but for a genuine
  `|Q|=2` seed.** q=5 is the unique tested exception (and it is exactly the
  seed already flagged as a genuine, structurally-explained counterexample to
  naive `p|a_1` trivialization in §6.1 of `n1-periodicity-reconciliation`).

**Mechanism (conjectural structural sketch — NOT a proof, flagged as such).**
For `a_1=3q`: candidate `a_n+1` is illegal by consecutive-integer coprimality
(universal, no assumption). Candidate `a_n+2` (the ONLY intermediate candidate,
since `p=3` gives exactly `p-2=1` such candidate — the minimal nonzero amount
above the already-solved p=2 case) is illegal against `a_1=3q` unless
`q | (a_n+2)`. I confirmed computationally that even when this DOES occur
(which it must, periodically with density `1/q`, once n is large enough — e.g.
for q=151 with 600 terms tested, roughly 4 such coincidences are expected to
occur within the window), the candidate `a_n+2` is STILL illegal overall,
because it then fails against some OTHER earlier term `a_i` (2 ≤ i < n) whose
own prime factorization does not happen to overlap with `a_n+2`'s. This is
structurally the same "full legality against literally every earlier term, not
just a_1" mechanism that makes the general FAH crux hard — so a full proof of
"3 | a_n for all n whenever a_1=3q, q≠5 prime" is NOT guaranteed to be cheap; it
may need an actual argument (not just "singleton P(a_1)" as in the p^k case,
since here |Q|=2). It is a **genuinely new, tighter, and more tractable-looking
special case** than the general `|Q|=2` regime (only ONE forbidden-candidate
slot to control, vs. p-2 slots for general p, and vs. the fully unconstrained
two-huge-primes regime already refuted) — worth a dedicated attempt, but
**not yet proved**, and I did not attempt to prove it (per my mandate).

**Recommendation.** This is a stronger, more clearly bounded candidate than the
refuted `p·q, q≫p` family: fix the SMALL prime at p=3 specifically (not
"p small, q large" in general), and the empirical failure count is exactly one
seed (q=5) out of 60+ tested. A future round could:
(a) attempt a full proof of "3 ∤ ever fails, i.e. `a_1=3q ⟹ a_n=3q+3(n-1)` for
all `n`, for every prime `q ≥ 7`" as a genuine THIRD certified subfamily
theorem (structurally analogous to, but strictly harder than, the p^k
theorem, since P(a_1) is not a singleton here); or
(b) if that proof turns out to hit the same universal-quantifier wall as FAH
itself (plausible, given the "must survive ALL earlier terms" structure found
above), it should at minimum be recorded as a sharply narrower, better-tested
open question than general FAH — worth trying before spending more rounds on
FAH in full generality.
I explicitly did NOT attempt this proof — flagging it as a lead only, consistent
with my mandate (audit, not proof-attempt).

I did NOT re-explore `a_1=p*q` for general larger p (already definitively
refuted by round 19, per the dispatch's explicit instruction not to re-pursue
it) — this p=3 finding is a genuinely different, narrower candidate, not a
retry of that refuted family.

### 3. Recommendation for the "insurance" write-up (if H1/H2 remain unsolved)

The workspace already has the ingredients for a maximally clean partial
deliverable; `current.md`'s `## Current best` (round-16 block, lines 1039–1194)
is close but could be tightened. Concretely, the cleanest final write-up should
contain, in this order:

1. **State the problem's actual claim** up front (existence of T, L with
   a_{n+T}=a_n+L for every n ≥ 1) so the write-up is self-contained.
2. **The floor deliverable, stated as a clean union-of-subfamilies theorem**,
   exactly as `n1-periodicity-reconciliation.md` §8 already assembles it:
   "For every a_1 with `2 | a_1` OR `a_1 = p^k` for a prime p, the claim holds
   with T=1 and L = 2 or p respectively" — cite Theorem A/B by name, restate
   both short proofs inline (they are short enough — under 15 lines each — to
   reproduce in full rather than merely cite, which makes the write-up
   self-contained without requiring the reader to open lemma files).
3. **The Master Conditional Theorem** (§2 of the reconciliation file) stated
   as the general reduction: "for every other a_1, the claim follows from H1
   and H2, both stated with full mathematical precision" — reproduce H1, H2's
   exact statements (§1) so a reader does not need the whole lemma stack to
   understand exactly what remains open.
4. **An honest one-paragraph summary of why H1 (FAH) resisted 19+ rounds**:
   name the mechanism families tried and killed (existential/pigeonhole
   competitor-construction, magnitude-sandwich, CRT-glue, the entire
   statistical/probabilistic family via the Generalized Class-Blindness
   Obstruction — but flag that this last one is NOT yet certified per round
   19's reviewer, so word it as "argued, not certified" if it remains
   uncertified when the write-up is finalized), automaton/Morse–Hedlund
   (proven equivalent-in-difficulty, not a bypass), and the underlying
   diagnosis (an existential single-witness fact needs promotion to a
   universal cofinite fact, and every tried route either needs the realized
   prime-identity data the recursive rule structurally never exposes, or
   reduces back to the same open content).
5. If pursued and completed, **the new `a_1=3q` (q prime ≥7) finding** (§2
   above) should be added as a THIRD certified floor subfamily, extending the
   union in item 2 — this is the single most promising concrete next step to
   grow the honest "solved" floor before the write-up is finalized.
6. **Explicitly do NOT claim `Status: solved`** for the general problem;
   `Status: partial` is correct and should stay that way unless H1 AND H2 are
   both closed. The write-up should present items 2–3 as the complete,
   defensible partial result: a strictly-conditional-but-gap-free reduction of
   the general problem to two named, precisely-stated open hypotheses, plus an
   unconditional infinite floor subfamily (extendable to a third if item 5 is
   completed).

This structure requires no new mathematics beyond what's already certified
(items 2–4) plus, optionally, one new theorem (item 5) — it is achievable by a
single consolidation-focused builder round if H1/H2 remain unresolved by the
time the run needs to close out.

### Candidate technique(s) for next round(s)
- For the new a_1=3q lead: an induction similar to the p^k theorem's, but the
  "a_n+2 illegal" step needs a genuine new argument (not just "P(a_1) is a
  singleton" — it is not, here) — likely needs to show the SPECIFIC prime
  factorization of a_2=3(q+1) (or a fixed early witness) obstructs a_n+2
  whenever q | (a_n+2), i.e. an "early-witness blocks the coincidental escape"
  argument, structurally close to the workspace's existing Universal Early
  Intersection Lemma machinery (self-absorption at a very small, explicit
  core) — worth trying that exact machinery on this restricted, much simpler
  target before attempting a from-scratch proof.

### Cheap-kill candidates
- Before committing serious effort to `a_1=3q`: check whether the "a_n+2
  illegal via a_2" argument alone (gcd(a_n+2, a_2)=1 whenever q ∤ (q+1)-related
  coincidences) already suffices for ALL n, which would make this a very short,
  fully elementary proof (analogous in spirit to Theorem A/B) — this is the
  first thing a builder should check before reaching for the S*/FAH machinery.

### Knowledge-base entries to use
- "Pigeonhole / extremal principle" (`knowledge_base.md`, already cited
  throughout the certified lemma stack for Persistent-Type/Extended-Persistent-
  Type Pigeonhole).
- CRT (Chinese Remainder Theorem), used in `self-absorbing-core-theorem.md`'s
  `sig(r)` construction and the original covering-system finish.
- No new KB entries are needed for the a_1=3q lead beyond elementary number
  theory (already the toolkit used for Theorems A/B).

### Analogous past problems (cruxes)
Not separately queried this round (audit-focused dispatch; prior rounds'
explorers have already searched the crux corpus for FAH-analogous problems and
found "no genuinely analogous precedent" per round 19's fresh-framing explorer,
cited in `n1-periodicity-reconciliation.md` §9). No new crux search performed.

### Prior progress
See §1 above — confirmed intact and gap-free: 2 certified unconditional
subfamily theorems (2|a_1 and a_1=p^k, both T=1 literal from n=1) plus a
gap-free Master Conditional Theorem reducing the general case to H1 (FAH) and
H2 (absorption-chain termination), both still open after 19+ rounds.

### Dead ends (do not retry)
- `a_1 = p*q` with q ≫ p, general p — DEFINITIVELY REFUTED (round 19): no
  monotone threshold, messy behavior (e.g. p=13, q=47 fails while q=43,53+
  succeed). Do not re-attempt in this general form.
- Generalizing the `2|a_1` H1-trivialization trick to arbitrary odd `p|a_1` —
  refuted (round 18, `a_1=15,45`, §6.1 of `n1-periodicity-reconciliation.md`).
- Treating `|Q|=2` as an "easy warm-up" for H1 — refuted (round 18, §6.2): the
  workspace's own canonical hardest test seeds (187,209,221,247) already live
  in `|Q|=2`.
- The entire "statistical method" family (density, second moment,
  Borel–Cantelli, finite-Fourier, LP-relaxation) as a route to H1 — argued dead
  by the Generalized Class-Blindness Obstruction (round 19), but **NOTE: this
  specific meta-lemma is NOT yet certified** — round 19's reviewer found a
  genuine circularity in its "two scenarios agree" step (no explicit
  construction of two divergent legal continuations is supplied). Future
  rounds should either (i) supply the missing construction, or (ii) restrict
  the meta-lemma's scope to genuinely ambient/decoupled-from-realized-data
  statistics (where it IS correct per the reviewer's own restricted-version
  check) and accept the weaker, correct scope.
- 19+ other FAH mechanism attempts across rounds 6–19 (competitor-construction,
  magnitude-sandwich, CRT-glue, EEA/automaton, extremal graph theory on
  witness structure) — all independently confirmed dead; see `current.md`'s
  round-by-round history for full detail, not re-summarized here.

### Small-case / intuition notes (conjecture, not proof)
- `a_1=3q` for prime `q ≥ 7` empirically gives literal T=1, L=3 periodicity
  (60+ seeds tested, zero exceptions besides q=5) — strong numerical support
  for a genuinely new, narrow, tractable-looking third subfamily, structurally
  distinct from (and much cleaner than) the already-refuted general `p·q`
  family, because fixing p=3 minimizes the number of "escape candidates" per
  step to exactly 1.
- q=5 is uniquely bad because it's small enough (relative to the period-3
  growth of the sequence) that coincidental divisibility by q, combined with
  weak early-term factorizations, actually succeeds in producing a legal
  escape — consistent with the already-documented period-4 alternation for
  a_1=15,45.
