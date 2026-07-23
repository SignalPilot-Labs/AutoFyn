# Outline review — imo-2026-01, round 1

Problem: 2026 integers >1 on a board; repeatedly replace (m,n) with (gcd(m,n), lcm(m,n)/gcd(m,n))
until <2 entries are >1. (a) process terminates with exactly one entry M>1; (b) M is independent
of the choices made.

Both candidate outlines target the whole problem end to end (not a sub-lemma, not a slice of a
shared proof), so the "whole attempt" bar is satisfied by both.

I ran a numerical sanity check (Python, 2000 random trials, n in [2,6], values up to 60, 3
independent random play orders per board): the claimed closed form M = ∏_p p^{gcd_i v_p(x_i)}
matched the simulated terminal value in every trial, and the process always terminated with
exactly one survivor. This corroborates the core mechanism used by both outlines (see script run
in this review session). No contradiction found.

## prime-valuation-invariant — APPROVE

Technique: per-prime p-adic valuation bookkeeping. Correct choice — a move on (m,n) acts on the
exponent pair (α,β) of every prime independently via (α,β)↦(min(α,β),|α−β|), by the standard
v_p(gcd)=min, v_p(lcm)=max identities. This is exactly the right elementary tool
(knowledge_base.md "Invariants & monovariants" / "Invariant / monovariant"); no heavy or
inapplicable machinery is invoked.

Checked each step:
- Step 2 (Euclidean identity gcd(min(α,β),|α−β|)=gcd(α,β)): correct, proof by case split
  α=β / α<β / α>β with the α=β=0 boundary explicitly via gcd(0,0)=0 convention. Verified
  numerically and by the standard "common-divisor-set" argument for gcd(a,b)=gcd(a,b−a).
- Step 3 (per-prime multiset-gcd g_p invariant): correct; relies only on associativity of gcd
  over a multiset (trivial, flagged by outliner as needing one citation line — fine as a
  CHANGES-REQUESTED-level polish item, not fatal).
- Step 4 (termination via lexicographic (Ω,C)): correct and the case split (gcd=1 vs gcd>1) is
  exhaustive and the two sub-cases are argued correctly (Ω flat + C strictly drops in the
  coprime case; Ω strictly drops in the non-coprime case). Well-founded descent on ℕ×ℕ is valid.
- Step 5 (≥1 survivor always): correct — g_{p0} of the initial board is positive for any prime
  p0 dividing x1, and invariance (step 3) keeps it positive forever, which is incompatible with
  an all-zero exponent vector for p0 at any (in particular the terminal) state.
- Steps 6–8 (assembly of (a) and (b)): valid; C=1 exactly follows from steps 4–6, and the closed
  form for M follows cleanly from evaluating g_p at the terminal state (a multiset with all
  zeros except one slot) and equating it to g_p(initial) via invariance.

No unjustified leaps, no circularity, no missing case. The naive false guesses M=gcd(x_i) and
M=∏p^{max_i v_p(x_i)} are explicitly and correctly rejected. Open gaps listed by the outliner
(multiset-gcd associativity one-liner, explicit "gcd of nonempty set not all zero is positive"
one-liner, note that n=2026 is not special) are genuine but trivial polish items, not fatal —
appropriate for the builder to close inline while writing, not a RETHINK-level flaw. This outline
is close to solved already; verdict APPROVE.

## confluence-newman — APPROVE (with a required change)

Technique: rewriting-system framing, Newman's Lemma (termination + local confluence ⇒ global
confluence / unique normal form) for part (b), reusing the identical termination monovariant for
part (a). This is a legitimate, different top-level architecture for uniqueness (diamond-lemma
style vs. direct closed-form computation) — the kind of framing diversity the run is asking for,
and Newman's Lemma is a standard, correctly-stated tool for this purpose (the setup matches its
textbook form: terminating ARS + locally confluent ⇒ Church–Rosser/unique normal form).

Checked each step:
- Step 1 (termination): identical, correct monovariant, imported not re-derived — fine, avoids
  duplicating proof work.
- Step 2 (part (a) assembly): correct, same survivor argument, correctly scoped as "imported,
  local, one-move fact," independent of which top-level uniqueness strategy is chosen.
- Step 3 (Newman's Lemma statement): correctly stated (termination + local confluence ⇒ unique
  normal form). Correct application target (the initial board).
- Step 4 (disjoint-move local confluence): correct and trivial — edits to disjoint coordinates
  commute regardless of the function applied.
- Step 5 (overlapping-move local confluence, the hard case): the reduction to a 3-slot sub-board
  and the "at most one forced continuation" argument is sound reasoning. BUT the one substantive
  claim — that the two forced terminal 3-tuples coincide — is left as an explicit open gap, and
  the outline's own suggested closing tactic is to import the *sibling approach's* per-prime
  multiset-gcd invariance lemma. That means, as currently written, this approach's one hard step
  is not actually independent of prime-valuation-invariant's core lemma — it plans to borrow
  exactly the same arithmetic fact (gcd(a,b)=gcd(a,b−a)) applied to 3 values instead of the
  whole board. This is mathematically fine (both approaches may legitimately share a primitive)
  and I confirmed by direct check that the 3-variable identity is in fact just the n=3 case of
  the same multiset-gcd invariant, so it is real progress and not circular. But it does mean the
  two approaches are less diverse than they appear: if the shared Euclidean-subtraction identity
  or its multiset extension turned out to be wrong (it isn't, per my numerical check), both
  approaches would die at the same wall. Flagging this per the diversity-check instruction: the
  approaches diverge in packaging/architecture (direct invariant vs. confluence) but converge on
  one shared core lemma as their real engine.

Required change for the builder (CHANGES REQUESTED components folded into the approve, since the
architecture is sound and only the gap-closing needs discipline):
1. First attempt to close Step 5's 3-variable identity directly and self-containedly (a short,
   independent 3-exponent case analysis on (α,β,γ)), rather than immediately reaching for the
   sibling's lemma — this preserves genuine independence between the two population members.
   Only if a clean direct proof doesn't materialize should the builder fall back to explicitly
   citing (with attribution, not silently) the shared Euclidean/multiset-gcd identity — this is
   already the outline's own fallback plan, just make the attempt-first-then-fallback order
   explicit in the writeup.
2. Newman's Lemma should get its short inductive proof (a few lines, standard) in the final
   writeup rather than a bare citation, per the "name your tools" / "no hand-waving" rule — it's
   flagged as minor by the outliner but the rigor rules require it spelled out, not just cited.
3. The general-n closure of Step 5 (chains of overlapping positions beyond a single shared index)
   needs the one sentence of structural-induction care the outliner already flagged — make sure
   it's actually written, not just noted as an open gap.

None of these are fatal — the architecture is sound, Newman's Lemma is the right tool, and the
one hard step has a concrete, verified closing mechanism (either directly or via the sibling
lemma). Verdict APPROVE, build this round with the above three items as explicit requirements
for the builder to close (not defer again).

## Diversity assessment

The two approaches share the termination half (identical monovariant, imported/cited rather than
re-derived in confluence-newman — appropriate, not a flaw) and, at the hard-step level, plan to
share the same core arithmetic identity (gcd(a,b)=gcd(a,b−a) / the min,|diff| substitution). They
genuinely diverge in the *proof architecture for part (b)*: one computes the closed form directly
via a global per-prime invariant, the other proves path-independence abstractly via Newman's
Lemma without needing the closed form as the engine. This is legitimate technique diversity, not
a cosmetic relabeling — but it is NOT framing diversity at the level of "a totally different
attack on the problem" (e.g., neither uses generating functions, extremal/potential arguments
unrelated to per-prime valuations, or a structural bijection). Both approaches are fundamentally
"track p-adic valuations + a monovariant." If both stall, the next round should be told to bring
in an approach that does NOT go through per-prime valuations at all (e.g., a direct
multiplicative/structural argument, or an explicit strong-induction-on-board-size argument that
avoids decomposing by primes) to genuinely diversify the field. For this round, though, both
outlines are technically sound and worth building — prime-valuation-invariant is essentially
complete already and is the stronger, more self-contained candidate.

## Dead ends check

`results/imo-2026-01/current.md` has Status `unsolved`, no approaches tried yet — nothing to
avoid repeating. No conflicts with recorded dead ends (there are none yet).

## Ranking

Registered both slugs (cold-start Elo 1500 each, no prior population). Ranked
prime-valuation-invariant > confluence-newman head-to-head: the former is essentially a complete,
gap-free proof already (only trivial one-line polish items remain), while the latter has one
genuine open computational step (Step 5) still pending closure, even though its architecture is
sound. Updated Elo: prime-valuation-invariant 1516, confluence-newman 1484.

build set: prime-valuation-invariant, confluence-newman
