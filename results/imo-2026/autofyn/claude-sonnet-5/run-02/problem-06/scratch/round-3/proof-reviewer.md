# Proof review — round 3 — imo-2026-06

## Summary of verdicts
- **covering-system-construction** — Status: partial. Verdict: **CHANGES REQUESTED**.
- **greedy-exchange-cost-potential** — Status: partial. Verdict: **CHANGES REQUESTED**.
- **witness-depth-bound** — Status: partial. Verdict: **RETHINK**.

None reach `solved`; both builders' self-reported `partial` Status is accurate this
round (no overclaiming found). `current.md` rewritten to merge all genuine progress and
record a new independent finding (below).

---

## 1. The two claimed new lemmas — independently re-verified, CERTIFIED

**Canonical-Refinement Lemma** (built independently in both
`covering-system-construction` Step 4d and `greedy-exchange-cost-potential`'s restated
"Lemma D"): for disjoint persistent base types A, B with canonical extended refinements
A_can = A ∪ F_A, B_can = B ∪ F_B, every extended-persistent refinement A' of A meets
B_can (in fact meets F_B), and symmetrically.

I re-derived this from scratch, independent of the builders' write-ups:
- The sub-claim B_can = B ∪ F_B is a direct set-algebra computation:
  ρ(m_B) = P(a_{m_B})∩S₀ splits as τ(m_B) ∪ (P(a_{m_B})\Q ∩ S₀) = B ∪ (F_B ∩ S₀), and
  F_B ⊆ S ⊆ S₀ by construction of S, so F_B ∩ S₀ = F_B. Correct, no gap.
- The main claim reduces to one application of the certified Bounded Witness Lemma with
  witness m = m_B: for n with ρ(n) = A' (so τ(n) = A), the Lemma gives a_n divisible by
  a prime of F_{A,B} = P(a_{m_B})\Q = F_B — note this set depends only on B (the witness),
  not on A, exactly as `bounded-witness-lemma.md` states. Since this prime lies in F_B ⊆
  S₀, it lies in ρ(n) = A'. This is correct and does not smuggle in anything about the
  open gap (†) — I checked it invokes only Free Facts + Bounded Witness Lemma, both
  already certified and unconditional.
- I additionally spot-checked this numerically for a_1 = 35 (F_{{5}} ∩ F_{{7}} = {2},
  matching the proof's shared-prime mechanism) — consistent, not that the algebraic proof
  needed it.

**F_A ∩ F_B ≠ ∅**: a one-line consequence of Free Facts (gcd(a_{m_A}, a_{m_B}) > 1, the
shared prime can't be in Q since A, B disjoint). Correct; and, as both files honestly
note, strictly subsumed by the Canonical-Refinement Lemma (the both-canonical special
case) — no new content beyond it.

**Scope, verified correct**: neither lemma says anything about pairs where BOTH sides
are non-canonical refinements ("rogue pairs"). Both files state this limitation
explicitly and do not overclaim more. I checked this is the actual logical content —
correct.

**Action taken**: certified once each, as canonical shared lemmas (both files'
independent derivations verified identical in content), crediting both approach files:
- `results/imo-2026-06/lemmas/canonical-refinement-lemma.md`
- `results/imo-2026-06/lemmas/canonical-witness-intersection.md` (F_A∩F_B≠∅, marked
  superseded-in-generality by the first, per the memory rule about not double-listing
  strictly-weaker lemmas as independently useful — kept as a named file since it has a
  clean standalone one-line proof some future approach may cite directly).

**Not certified**: `greedy-exchange-cost-potential`'s "Lemma F" (minimality bounds
magnitude, not type). I read its "proof" carefully: it is not a general mathematical
impossibility theorem — it is a description of what the two currently-certified
magnitude lemmas (Bounded Gap Lemma, Generalized Bounded Gap Lemma) do and do not
construct ("no certified lemma in this workspace constructs X"). This is a true and
useful *documentation* of why one specific proof strategy fails with the *current*
lemma set, but it is not a portable, general theorem suitable for the shared lemma
cache (its truth is contingent on which lemmas have been proved so far, which will
change). I decline to certify it as a standalone lemma file; it remains valid content
inside `greedy-exchange-cost-potential.md` itself, correctly scoped there.

---

## 2. covering-system-construction's Step 4f — two claimed obstructions to the
minimal-counterexample attack — verified genuine, not "gave up"

Setup: fix a minimal-μ violating pair (A'_0, B'_0) ∈ V (μ = |A'|+|B'|), apply the
Generalized Bounded Witness Lemma's Corollary to recruit a new prime q, forcing
A'_0 ∪ {q} to be S₀^(1)-persistent.

- **Route 1 (direct μ-decrease) genuinely fails.** The produced object A'_0 ∪ {q} has
  size |A'_0| + 1, strictly LARGER than |A'_0|, and lives in 2^{S₀^(1)}, not 2^{S₀} — it
  is not comparable to any element of the original finite family 𝒫' that μ ranges over.
  I checked whether some other pairing trick could still produce a μ-decrease (e.g.
  comparing A'_0 ∪ {q} against some other existing element of 𝒫' of smaller size sharing
  base type A) — no such comparison is licensed by any certified lemma; the recruitment
  operation is a "grow-only" refinement (confirmed also by the round-2 catalogue: refining
  by a new prime never shrinks a type's signature). This failure is structural, correctly
  diagnosed.
- **Route 2 (force q into the witness side) genuinely fails.** The Corollary's pigeonhole
  is over occurrences of A'_0 (the side "being reconciled"), producing recurrence of q on
  that side only; it says nothing about whether q recurs across B'_0's own infinitely many
  occurrences (only one occurrence — the fixed witness m' — is guaranteed to carry q). I
  attempted to patch this myself (e.g. via a joint/simultaneous pigeonhole treating both
  sides' occurrences at once) in the time available and could not produce one either —
  this matches the diagnosis in the file ("this is precisely the obstruction... a
  structural feature of the problem's difficulty").

Both obstructions are genuine, specific, and correctly documented — not hand-waving or
"ran out of time" placeholders. This satisfies the CLAUDE.md rigor bar for a partial
proof (real progress + honestly isolated gap).

---

## 3. greedy-exchange-cost-potential's Lemma F — assessed correct but weak/non-portable

The claimed content ("no exchange argument built solely from Lemma A / the Bounded Gap
Lemma can force a rogue type to be avoided, because these lemmas only ever construct
LARGE safe candidates, never small ones") is logically valid given what it's actually
asserting, but — as noted in §1 above — it is a meta-statement about the current lemma
set's capabilities, not a self-contained mathematical impossibility result about the
problem itself. I verified its two supporting sub-claims are each individually correct
(both certified magnitude lemmas do construct candidates of gap Θ(modulus) ≥ Θ(a_1),
with no mechanism for a smaller controlled-type candidate) and that the file states this
honestly (does not claim to close (†), explicitly frames it as ruling out one specific
proof-attempt family). Verdict: correct content, correctly scoped, but not certifiable
as a portable shared lemma (see §1).

---

## 4. witness-depth-bound's "scope observation" — verified correct; RETHINK

Checked the argument line by line:
- The Finite Core Theorem (`finite-core-theorem.md`) proves S finite using only that 𝒫 is
  finite (pigeonhole) and each P(a_{m_B}) is the factor set of one fixed integer (hence
  finite) — no numeric bound on m_B is used anywhere in that proof. Confirmed by rereading
  the certified lemma file.
- Gap (†), per `current.md`'s Step-4c framing (also unchanged this round in its Step-4d
  localized form), is about whether the *recruitment process starting from S₀^(0) = Q∪S*
  halts — a question about behavior strictly beyond S, triggered by violations of the
  extended-type intersection property, not by anything about how m_B was found or how
  large it is.
- Therefore an explicit f(a_1) bound on first-occurrence indices, even if fully proved,
  would only make the ALREADY-finite S more explicit (a strengthening in kind, e.g. useful
  for an explicit L, T later) — it does not touch whether further recruitment rounds are
  needed. This is a correct, valid logical point, not hand-waving.

Given this, the approach's original goal ("bypass (†) entirely" per the outline) cannot
succeed as set up, independent of whether the depth-bound conjecture itself is provable.
This meets the bar for **RETHINK**: the approach as currently framed cannot close the
target gap even in the best case. The file itself recommends two ways forward (accept
the narrower scope as a standalone strengthening, or re-aim at bounding the depth of ALL
recruitment rounds, not just the original witnesses) — I agree the second is the only
version of this idea that could still matter for (†), and it was not attempted this
round (correctly disclosed, not silently skipped).

No promotable lemma from this file (the one proved fact, τ(1) = Q, is a correctly-flagged
trivial one-liner, not worth a standalone certified file — I agree with the builder's own
assessment not to submit it).

---

## 5. Independent verification / new finding: (†) genuinely fails at the naive
"zero further rounds" stage for a previously-untested seed

Per the standing reviewer rule (always independently re-simulate before trusting a
"computationally supported, N seeds, zero violations" claim), I ran my own simulation
across several a_1 not in either builder's tested seed lists. Using
`a_1 = 175 = 5²·7`, Q = {5,7}:

- Simulated ~2500 terms via a fast greedy generator (prime-factor-set gcd check, not
  raw `sympy.gcd`, for tractable runtime).
- Persistent base types (long tail, ≥1500 terms in): {5}, {7}, {5,7} — as expected.
- Built S via one canonical witness per base type (same recipe as the Finite Core
  Theorem / both approaches' computational checks): S₀ = {2,3,5,7,11}.
- Found extended-persistent types including **{2,7}** (refining base type {7}) and
  **{3,5}** (refining base type {5}) — disjoint base types, disjoint extended types:
  a genuine violation of (†) at this S₀.
- Confirmed this pair is exactly a **"rogue pair"** per the Canonical-Refinement Lemma's
  own scope (canonical refinements are {7}_can = {2,3,7,11} ≠ {2,7} and
  {5}_can = {2,3,5} ≠ {3,5}) — so this does NOT contradict the certified lemma; it
  confirms the residual set V the lemma leaves open is genuinely non-vacuous, not merely
  a hypothetical possibility as both builders' 15/10-seed checks (which did not include
  a_1 = 175) suggested.
- Applied the Generalized Bounded Witness Lemma's Corollary to this pair: it recruits
  prime **13**, confirmed by direct counting (13 divides all 27 sampled {2,7}-type terms
  in the tail).
- Independently computed the true eventual period by direct gap-sequence periodicity
  search: **T = 274, L = 2730 = 2·3·5·7·13** — the recruited prime 13 is exactly the
  missing factor. This is positive evidence the recruitment-process mechanism is the
  right one, while simultaneously falsifying the "usually zero further rounds needed"
  empirical conjecture both builders reported.

This does not overturn any certified lemma or claimed proof — both approaches always
correctly labeled "zero further rounds" as an unproved conjecture, not an established
fact — but it is important new information for the next round: the recruitment process
genuinely needs to fire in general, so a future round should not spend effort trying to
prove "S from the Finite Core Theorem always already suffices" (now empirically false),
and should instead attack termination of the (possibly multi-round) process directly, or
find the joint/simultaneous-pigeonhole mechanism both builders flagged as the likely
missing ingredient. Recorded in `current.md`.

---

## current.md — updated

Rewritten in full: `## Status` (partial, unchanged), `## Approaches tried` (all five
approaches, with this round's per-slug verdicts stated explicitly), `## Current best`
(merged lemma list 1–12, including the two newly certified lemmas, plus the independent
a_1=175 falsification finding), `## Full proof` (absent, with a concrete next-round
target list including "do not re-attempt the now-falsified zero-further-rounds
conjecture").

## Lemma certification actions
- Certified: `results/imo-2026-06/lemmas/canonical-refinement-lemma.md` (dedup of
  covering-system-construction Step 4d + greedy-exchange-cost-potential Lemma D).
- Certified: `results/imo-2026-06/lemmas/canonical-witness-intersection.md` (dedup of
  Step 4e + Lemma E; marked as subsumed-in-generality by the first).
- Declined: greedy-exchange-cost-potential's "Lemma F" — correct but a toolkit-bound
  meta-observation, not a portable general theorem; left in the approach file, not
  promoted to the shared cache.

## Ranking outcomes recorded
- `covering-system-construction`: advanced.
- `greedy-exchange-cost-potential`: advanced.
- `witness-depth-bound`: dead-end.
