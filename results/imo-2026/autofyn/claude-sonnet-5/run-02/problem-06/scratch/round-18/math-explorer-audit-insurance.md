## imo-2026-06 — Audit / Insurance-Deliverable Stock-Take (round 18, audit lens)

This is a stock-take, not a proof attempt. No new mechanism is proposed as a
build target beyond one flagged, unproved empirical lead (see §3).

### 1. Audit of the Master Conditional Theorem chain — is it airtight? Can H1/H2's scope shrink further?

**Chain re-verified independently, no new gap found.** I re-read
`n1-periodicity-reconciliation.md` (§0–§2, the Master Conditional Theorem) and
the two load-bearing certified lemmas it cites for its final assembly step —
`lemmas/self-absorbing-core-theorem.md` and
`lemmas/literal-n1-periodicity-theorem.md` — line by line. Both proofs
(Sufficiency / Landing / Assembling, then the extension to n≥1 via the
Universal Early Intersection Lemma) are self-contained, cite only
already-certified unconditional facts (Free Facts Lemma, Extended
Persistent-Type Pigeonhole, the FAH-at-S* hypothesis itself), and match their
own stated hypotheses exactly — I did not find the citation-gap pattern that
bit rounds 13–14 (a broader conclusion cited from a narrower construction).
The §2 assembly step (H1 + H2 ⟹ problem's claim) is a one-paragraph chain with
no smuggled content: H2 → Termination Criterion Lemma gives a finite terminal
S*; H1 stated exactly at that S*; both hypotheses of Literal n=1 Periodicity
Theorem are then literally satisfied. **Verdict: the chain is airtight as
audited** — this matches (does not contradict) 3 prior rounds' independent
re-verifications (rounds 14, 15, 16 proof-reviewers).

**Can the scope of H1/H2 shrink further via a special sub-case beyond 2|a_1?**
Tested three candidate directions computationally (all via direct greedy-sequence
simulation, `math.gcd` + trial division, not sympy, per workspace convention):

- **"Does p | a_1 trivialize FAH the way 2 | a_1 does, for odd p?"** — **NO,
  concretely refuted.** For a_1=15=3·5 and a_1=45=3²·5, only 75% of terms are
  divisible by 3 (not literally forced like the 2-case): the sequence exhibits
  a genuine persistent 4-term-period alternation between base types {3} and
  {5} (fail-indices 3,7,11,15,... exactly period 4), i.e. real FAH-relevant
  structure, not vacuous triviality. This is a clean, hand-verifiable
  counterexample to the naive generalization — the 2-case's mechanism is
  special to p=2 precisely because the gap between "definitely illegal"
  (a_n+1, killed by bare consecutive-integer coprimality) and "next multiple
  of p" (a_n+p) is only 1 residue when p=2, so there are zero intermediate
  candidates to worry about; for p≥3 there are p−2≥1 intermediate candidates
  that can succeed via a *different* prime of a_1, exactly as observed.
  (This matches and computationally reconfirms — with a sharper example — the
  already-certified §4.2 negative finding in `n1-periodicity-reconciliation.md`
  that "2|a_1 trivializes H2" fails; my finding additionally shows the
  analogous naive extension of the *H1/even-a1* mechanism itself, not just H2,
  fails for odd p.)

- **"Is |Q|=1 (a_1 a prime power, any prime, not just 2) already unconditionally
  solved?"** — **YES, but this is old news, not a new deliverable.** By Free
  Facts alone (gcd(a_n,a_1)>1 for all n, and a_1=p^k has only one prime
  factor), p | a_n is forced for every n unconditionally; then by the same
  "a_n+1 illegal (consecutive), a_n+jp for 1≤j<p illegal since it shares no
  prime with a_1, a_n+p legal" argument, a_n = a_1+p(n-1) for every prime p,
  not just p=2. This case is already implicitly covered in the workspace
  (referenced as the pre-round-16 "|Q|=1 special case" in
  `even-a1-full-periodicity-theorem.md`'s own scoping section) — it does not
  extend the certified-solved subfamily beyond what's already known, and
  `even-a1-full-periodicity-theorem`'s actual contribution was specifically
  generalizing p=2 from prime-powers to ALL even a_1 (not extending to other
  primes, which the file explicitly and correctly disclaims).

- **"Is |Q|=2 (a_1 = pq, two distinct primes) a tractable general subfamily?"**
  — **NO, genuinely hard, matches existing documentation exactly.** Swept
  a1=pq for p,q ∈{3,...,31} (36 seeds) and searched for literal periodicity
  from n=1 with a widened window (up to 6000 terms, T up to 600). Result:
  the great majority resolve to literal periodicity from n=1 (confirming, not
  extending, the round-15/17 Literal n=1 Periodicity conjecture), but the
  *time to resolve* is highly seed-dependent and unpredictable from p,q alone
  — e.g. a1=187=11·17 needs T=484 (period found only with window >3000,
  exactly matching round-17's independently-recorded empirical figure — a
  useful cross-check that my simulation code is correct), a1=209=11·19 needs
  T=528 (also matches round 17 exactly), and a1=247=13·19 still shows no
  detected period even at window 6000/T-search 600. **These are precisely the
  canonical hard rogue-pair test seeds already used throughout rounds 6–17**
  (187, 209, 221, 247 all appear repeatedly in the workspace's own history) —
  |Q|=2 does NOT trivialize FAH; it is the genuinely open general case in
  miniature, exactly as documented. No shortcut found.

**Conclusion on §1:** the chain itself is sound and I could not find any way
to shrink H1/H2's required generality via a bespoke special-case argument
beyond what's already certified (2|a_1, prime powers). All three probed
directions either concretely fail (odd-p trivialization) or reproduce already-
known hard territory (|Q|=2).

### 2. Independent re-verification of certified-lemma citations

Spot-checked two of the most load-bearing citations directly against their
lemma files (not just trusting the approach file's summary):

- `self-absorbing-core-theorem.md`: confirmed the Sufficiency/Landing/
  Assembling proof genuinely only uses (i) self-absorption of S* (P(a_j)⊆S*
  for j≤N(S*)), (ii) FAH-at-S* (pairwise intersection of 𝒫'(S*)), (iii) the
  unconditional Free Facts Lemma and Extended Persistent-Type Pigeonhole — no
  circular or undisclosed dependency on H1/H2 themselves. The "Precision note"
  correctly derives (not just asserts) that "every two elements of 𝒫'(S*)
  intersect" ⟺ standard disjoint-base-type FAH, via Q⊆S* and ρ_S(n)∩Q=τ(n).
  Confirmed correct.
- `literal-n1-periodicity-theorem.md`: confirmed it introduces NO new
  hypothesis beyond the parent theorem's two — the extension to n≥1 uses only
  the unconditional Universal Early Intersection Lemma (itself dependent only
  on self-absorption, not on FAH) for the new n≤N(S*) range. Confirmed
  correct, matches its own "Status of conditionality" disclosure exactly.

No silent gap or overclaim found in either file. This matches (rather than
merely repeats) three independent rounds of prior review; I did not find
anything those reviews missed.

### 3. One unproved empirical lead worth flagging (not a claim, not build-ready)

While computationally sweeping |Q|=2 seeds a1=pq, I noticed an apparent
pattern: whenever q is sufficiently large relative to p (roughly q>2p, though
NOT exactly — a1=11·31=341 with q−2p=9>0 is a clean counterexample to the
naive "q>2p ⟹ trivial T=1,L=p" hypothesis, confirmed by direct inspection of
its gap sequence, which shows a genuine mixed 11/22-gap recurring pattern, not
literal a_n=a_1+p(n-1)), the sequence often locks into the trivial arithmetic
progression a_n=a_1+p(n-1) forever (e.g. 21,33,39,51,57,69,55,85,115,253,319,
377,403 all verified trivial to 150+ terms). The intuitive mechanism (when q
is "large enough," any candidate that would need to borrow legality from q
against ALL earlier p-only terms is farther away than the next multiple of p,
so the greedy process never needs to introduce q at all) is plausible but the
exact threshold is NOT q>2p as the 341 counterexample shows — the true
criterion (if one exists at all, as opposed to being seed-specific/chaotic) is
unresolved. **This is not proposed as a build target this round** — it is an
unproved, only-partially-characterized empirical curiosity, flagged per the
"no hand-waving" rule as a possible but unworked future lead, not a
cheap-kill or trivializer. A future round attacking it would need to (a) find
the exact threshold condition (if one exists), (b) prove it rigorously for
the trivial cases, and (c) address why 341-type near-boundary cases fail —
this is real, nontrivial work, likely comparable in difficulty to a fresh FAH
sub-case, not a shortcut.

### 4. Strongest achievable insurance deliverable if H1/H2 stay open

If rounds 18–19 cannot crack H1 or H2 in general, the run already has, and
should present, exactly this three-part deliverable (no further work strictly
required to state it, though a final consolidation write-up would help):

1. **A fully solved, unconditional infinite subfamily**: `2 | a_1` ⟹
   `a_n = a_1+2(n-1)` for all n≥1 (T=1,L=2, literally from n=1) — APPROVE'd,
   certified, `lemmas/even-seed-literal-periodicity-theorem.md`. (Also,
   trivially and for completeness, the `a_1` a prime power case, any prime,
   already implicit in the workspace though never separately certified as its
   own headline lemma — cheap to add as a one-paragraph corollary if a final
   write-up wants a second concrete infinite family stated explicitly.)
2. **A complete, gap-free conditional reduction of the FULL general problem**
   (every a_1>1) to exactly two named, precisely stated open hypotheses H1
   (FAH at the terminal absorption core) and H2 (absorption-chain
   termination) — the Master Conditional Theorem, §2 of
   `n1-periodicity-reconciliation.md`, independently re-audited this round
   with no gap found (§1–2 above).
3. **A precise account of what would resolve each hypothesis**: H1 has 18+
   independently-confirmed-dead general mechanisms across 12 rounds (6–17),
   with a stable diagnosis (class-blindness of every certified magnitude/
   counting tool; the missing ingredient is a class-*discriminating* source of
   information no current technique family supplies). H2 has the Termination
   Criterion Lemma (iff-reduction to N(S_k) boundedness), the Vacuous/Weak
   Self-Absorption Lemma (N(Q)≤1 ⟹ zero rounds), and the open NTBT conjecture
   (N(Q)≤1 for every a_1, strongly but not conclusively supported
   empirically, ~50 seeds, zero counterexamples after correcting for
   window-artifact false positives).

**What would still be missing** even with this packaged as the final
deliverable: an actual proof (not just a reduction) of H1 or H2 for a single
new nontrivial case beyond 2|a_1/prime-powers — i.e., the run's "solved"
status for the *general* problem is unreachable without either (a) a
genuinely new FAH mechanism (19th+ attempt, no candidate currently on the
table per rounds 15/17's exhaustive fresh-framing sweeps), or (b) a proof of
NTBT for H2 (also no candidate mechanism currently on the table — both
attempted proof routes in `self-absorbing-by-construction.md` are dead ends,
class-blindness and no-known-FAH-reduction). Absent either, the honest
strongest claim is exactly the three-part package above: `partial`, with a
fully solved infinite subfamily and a complete, audited conditional reduction
of the rest.

### Recommendation for round 18/19 dispatch

- Do not re-dispatch "does p|a_1 trivialize for odd p" — concretely refuted
  above with a hand-verifiable example (a_1=15,45).
- Do not re-dispatch "|Q|=2 general case is easy" — concretely refuted above;
  it reproduces the exact same hard canonical test seeds (187,209,221,247)
  already used as the standard evidence base since round 6.
- If a math-explorer wants a genuinely fresh (not-yet-tried) numeric/small-
  case angle, the q>2p-ish "large second prime" empirical pattern (§3) is the
  one new, honestly-unresolved thread this round surfaced — worth one
  dedicated round of investigation (find the exact threshold, or show none
  exists / it's seed-chaotic) before deciding whether it's buildable, but
  it is NOT ready to hand to an outliner as a proof target yet.
- Otherwise, per the round-15/17 escalation guidance already in force: continue
  treating the three-part conditional package (§4) as the run's floor
  deliverable, and keep pushing for a genuinely new H1 or H2 mechanism family
  (not a variant of the 18 dead ones) if wall-clock remains.
