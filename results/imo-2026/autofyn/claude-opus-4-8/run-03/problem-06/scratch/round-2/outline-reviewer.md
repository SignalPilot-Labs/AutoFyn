# Outline review — imo-2026-06, round 2

Problem: greedy gcd-sequence, prove ∃T,L with a_{n+T}=a_n+L ∀n. Whole problem is
certified-reduced to ONE crux (Finite Alphabet: 𝓐_∞ = ⊆-minimal prime-supports finite,
equiv. Π = primes(L) finite). No transient step needed (certified). Field = 3 attacks on
that crux. I numerically stress-tested each central claim with sympy on real simulated
sequences before ruling.

---

## redundant-constraint-antichain (advance) — APPROVE

Certified infrastructure (free-lemmas L1–L4, no-transient fixed-successor §1–§5) is sound and
reviewer-verified. §8 is the round-2 crux-attack skeleton. I checked its quantitative claims:

- §8.2 "no bare {q} large-prime singleton is minimal" — SOUND and verified. If {q}∈𝓐_∞ then
  every term meets {q} (i.e. q|a_k ∀k), so by L3 q ≤ |a_1−a_2| ≤ M, contradicting q>M. Simulation
  confirms: for a_1=375 the minimal supports are {2,3},{2,5,7},{2,5,19},{3,5},{3,7,19} — 19 is
  always paired with a small anchor, never a singleton. §8.1 anchor-collapse (pigeonhole to a
  fixed p*) is the certified §7c argument.
- §8.4 is the SOLE open gap and is HONESTLY flagged as such ("THE HARD STEP / the precise open
  gap"): show a pure-companion-S term must eventually appear for all but finitely many G_k. No
  step assumes the conclusion; the difficulty is correctly localized to the simultaneous
  interaction of all minimal supports (why intersecting-only structure fails, §7b). It does NOT
  reintroduce the refuted p≤M threshold.

Verdict: sound skeleton, clearly-delineated single gap, strongest line. Build it. The concrete
target for the builder: the n-independent per-window bound on simultaneously-active companions
(the naive log₂(a_n) count grows with n and does NOT close it — flagged in §8.4 and by the
density explorer). This is the real content; if it can't be made n-independent, that must be
reported as still-open, not papered over.

## a-periodic-sole-witness (new) — RETHINK (cut, not registered)

Central selling point: reframe to the "strictly weaker" target "A periodic ⟺ Q finite" (Q =
sole-witness primes), claimed to dodge the p*-obstruction because on the hypothetical p*-family
Q={p*} while 𝓐_∞ is infinite. TWO fatal problems:

1. **The distinguishing weakness is VACUOUS on real sequences — the single-gap trap.** I computed
   Q (sole-witness primes: ∃c∈A, F∈𝓐_∞ with primes(c)∩F={p}) directly for every real simulated
   sequence:
   ```
   a1=105 : Q={2,3,5,7}       = Π   ✓
   a1=375 : Q={2,3,5,7,19}    = Π   ✓   (incl. the M-exceedance prime 19)
   a1=385 : Q={2,3,5,7,11,19} = Π   ✓
   a1=1155: Q={2,3,5,7,11}    = Π   ✓
   a1=35  : Q={2,3,5,7}       = Π   ✓
   a1=15  : Q={2,3,5}         = Π   ✓
   ```
   Q = Π in EVERY realizable case. So "Q finite" and "Π finite" are the SAME statement on the
   actual problem; proving Q finite IS proving the antichain Finite-Alphabet crux. The p*-family
   that supposedly makes the target weaker is a hypothetical intersecting family, NOT a realizable
   greedy sequence, so the "dodge" buys nothing. This is exactly the recorded NEVER rule: a
   far-out approach whose distinguishing mechanism reduces to another approach's exact crux is the
   single-gap trap in disguise.

2. **The density monovariant (Step 3) is a non-sequitur even granting its lemma.** The plan is
   "each new sole-witness prime p costs density ε_p, and Σε_p ≤ 1−1/M ⇒ |Q|<∞." A convergent
   bounded sum with ε_p→0 is fully compatible with INFINITELY many primes (e.g. ε_p=2^-p). Finite
   count needs ε_p ≥ δ>0, which is not established and is implausible for large p (a large sole
   witness plausibly costs ~1/p density). The approach's own "watch out" ("ε_p may shrink with p;
   convergence must be argued") concedes the very fact that breaks the finite-count conclusion.
   The recorded-DEAD "sum per-prime density caps" wall is not escaped by the sole-witness
   relabelling.

Direction back to the outliner: this is not a distinct framing — it collapses onto the antichain
crux (Q=Π). If a genuinely different framing is wanted, it must NOT route through Π/Q/𝓐_∞
finiteness at all (the monovariant-descent slug already attempts that).

## monovariant-witness-descent (new) — CHANGES REQUESTED (registered, kept for diversity)

Genuinely far framing (no poset, no density; extremal descent à la aimo-0678). Honestly flagged
as a research gamble with three unconstructed gaps (G1 freezing invariant, G2 witness
monotonicity, G3 recruitment descent). I stress-tested the proposed witness:

- The naive first-failure witness w_n = min{t∈{1..M}: a_n+t∉A} (and the stage-n variant) is
  **degenerate = constant 1** on a_1=375 (verified n=200..400): a_n+1 is essentially always
  outside A. It is "non-increasing" only because it is pinned at the floor 1 immediately, which
  pins NO modulus and carries zero information. So G2's naive candidate is useless as written —
  confirming the approach's own honesty note.

This does not kill the framing (the value of keeping it is diversity: cutting it too would
collapse the field to the single antichain wall — the plateau trap CLAUDE.md warns about). But the
builder is on notice: the FIRST task is to construct a NON-degenerate state-statistic (e.g. a
recruitment counter, or the witness measured against the running modulus R_n rather than a_n, or a
direct "next new-prime index" quantity) that is both non-trivial and provably non-increasing. If
after one build attempt no non-degenerate monovariant with a real descent can be exhibited, this
must go RETHINK — do not dress up G3 (which is the crux in monovariant clothing) as proved.

---

## Field diversity note (for the orchestrator)

After cutting a-periodic-sole-witness, only TWO framings remain: order-theory/domination
(antichain) and extremal-descent (monovariant). These are genuinely far apart (different method,
different failure mode). The density/counting framing keeps collapsing onto the antichain crux
(a-periodic was density-in-disguise and reduced to Q=Π). If monovariant fails to produce a
non-degenerate witness next round, the field is at risk of collapsing to the single antichain
line — at that point the orchestrator should seed a NEW framing that does not touch prime-support
finiteness at all (candidates the explorers flagged but nobody has built: a self-referential
bootstrap on the greedy choice rule itself, or a direct combinatorial cap on simultaneously-active
constraints per length-M window proved n-independently).

build set: redundant-constraint-antichain, monovariant-witness-descent
