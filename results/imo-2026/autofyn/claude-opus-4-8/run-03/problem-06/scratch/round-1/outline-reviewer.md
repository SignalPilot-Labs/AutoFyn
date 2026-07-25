# Outline review — imo-2026-06, round 1 (ranking gate)

## Headline: the entire field shares ONE crux premise, and that premise is FALSE.

All three approaches build their whole proof on a single shared claim — "primes q > P_max never
change the greedy successor" (stated three ways: a *reduction lemma*, a *no-large-critical-prime*
counting bound, and a *bounded-memory* window). The outliner flagged this as a possible single-gap
trap and "verified" it numerically on seeds {15,35,77,91,105,143,1155}. That seed set is
non-representative. I re-ran the simulation on adversarial seeds and the premise breaks decisively.

### Counterexample: a_1 = 385 = 5·7·11 (P_max = 11, M = 2310)
The greedy sequence starts 385, 390, 392, 396, **399 = 3·7·19**, 406, **418 = 2·11·19**, 420, ...
At the step a_6 = 406 → a_7:
- Greedy picks **418 = 2·11·19**.
- 418 shares with a_5 = **399 = 3·7·19** ONLY the prime **19 > P_max**. Its small support {2,11}
  is disjoint from 399's small support {3,7}.
- The smallest *small-admissible* candidate (sharing a prime ≤ 11 with every earlier term) is
  **420 = 2²·3·5·7 > 418**.
- So the large prime 19 is the **sole witness** for the constraint from 399, and it strictly
  lowers the greedy value (418 < 420).

This one instance simultaneously refutes all three cruxes. I confirmed with three independent,
non-circular measurements over 385 (N up to 1500):
1. **Reduction / "small-admissible = greedy" (prime-support-reduction GAP-3): FALSE.** The
   small-admissible successor differs from the greedy successor (420 vs 418 at the step above).
   Consequence: a_{n+1} is NOT a function of a_n mod M, so the map g: Z/MZ→Z/MZ (step 5) does not
   exist and the eventual-periodicity pigeonhole collapses.
2. **"No large critical prime" (covering-ap-union GAP-A): FALSE.** 19 > P_max is the unique
   witness of the 399 constraint. The admissible set is therefore NOT a fixed union of residues
   mod M, so CRUX-B (greedy = enumeration of a fixed U mod M) has no fixed U to enumerate.
3. **Bounded-memory window (bounded-gap-finite-memory GAP-2): FALSE, and demonstrably unbounded.**
   I computed the minimal window W(n) such that the successor of a_n computed from only the last
   W terms equals the true successor: W reaches **320 at n = 855** and keeps growing (the
   sole-large-witness constraint reaches as far back as 1453 steps in N = 1500). W is not
   bounded independent of n, so the finite state space of step 3 does not exist and Φ is not a
   well-defined map on the claimed (finite) state — the "state" omits the recent large primes it
   would need, and the needed prime set is unbounded.

The problem's *conclusion* (eventual periodicity) is of course still true — it's a proven IMO
problem — but for 385 the period is very large (no (T,L) found with T ≤ 3500 at N = 9000; the
tail gap-sequence has no period below length ~2000). That large period is precisely the regime
the three approaches' simplification was designed to rule out. The mechanism, not the target, is
dead.

---

## Verdicts

### prime-support-reduction — RETHINK
Anchor (step 1) and Gap/Primorial (step 2) are correct, rigorous, and free — keep them. But the
load-bearing GAP-3 Reduction Lemma is **false** (test 1). Steps 4–6 (finite constraint family,
g: Z/MZ→Z/MZ, eventual periodicity) all depend on a_{n+1} being determined by a_n mod M, which
fails. The route cannot be built.

### bounded-gap-finite-memory — RETHINK
Same free Anchor+Gap. The headline Finite-memory Lemma (GAP-2) is **false and provably unbounded**
(test 3: W grows past 320). Its stated mechanism — "an old term whose only coverage would be via a
large prime is redundant since a multiple-of-M candidate already covers it via a small prime" — is
exactly what 385 violates: the greedy choice deliberately undercuts the multiple-of-M competitor
using a large prime. Without a bounded window the finite state space and the reversibility endgame
(GAP-5) have nothing to act on.

### covering-ap-union — RETHINK
Same free Anchor+Gap. GAP-A ("no prime q > P_max is ever critical") is **false** (test 2: 19 is a
sole witness). The downstream "admissible set = fixed residue union U mod M" (steps 3–3b) and the
guess-and-verify enumeration (CRUX-B) therefore have no fixed target U. The counting intuition
(⌈N/p⌉ divisor bound) proves large primes are *rarely* critical, not *never* — and "rarely" is not
enough, because a single large-critical step derails "greedy = enumeration of a fixed U."

---

## Single-gap-trap assessment (the orchestrator asked)
This is the single-gap trap fully realized — worse than a hard shared wall: the shared wall is a
**false statement**. The three "different mechanisms" are three encodings of the same wrong
simplification (discard primes > P_max). They are NOT far enough apart in framing; they diverge
only in the *endgame* (g-bijection vs Φ-reversibility vs constructive enumeration), which is
downstream of the dead crux and never gets reached. Building any of them means asking a builder to
prove a lemma that is numerically false — it would either fail or produce a wrong proof.

## Direction for next round's outliner (must re-plan from scratch on the crux)
- Keep the two free lemmas (Anchor: every term divisible by a prime of P, so spf ≤ P_max; Gap:
  every multiple of M is admissible, so a_{n+1} − a_n ≤ M). These are correct and shared.
- The correct proof MUST model large-prime shortcuts, not discard them. Facts to exploit:
  a shared prime q between two terms at distance D forces q ≤ D (two numbers within D that share q
  must differ by a multiple of q); and a_n = Θ(n). So the primes that can ever be *critical between
  nearby terms* are constrained, but critical constraints can reach arbitrarily far back — the
  memory really is unbounded, so the argument cannot be a naive finite-state pigeonhole.
- Put on the table genuinely different framings, e.g.: (a) track the **hypergraph of minimal
  prime-sets** {primes(a_i)} and show that although new large primes keep entering, the induced
  successor pattern is eventually periodic via a growth/counting argument on how often a large
  shortcut can fire; (b) a **minimal-counterexample / potential-function** argument on the first
  index where periodicity-from-n=1 would fail; (c) an averaging/growth argument on ∑1/q over primes
  q dividing terms. At least one framing should NOT route through "reduce to mod M."
- When re-outlining, VERIFY any new shared premise against adversarial seeds — specifically
  a_1 = 385, 5·7·13, and other products of three odd primes with no factor 2 or 3, which are the
  regime that triggers large-prime shortcuts.

## Ranking / population
No approach approved. Per the gate rule, RETHINK angles are not registered, so the population
stays empty and there is nothing to rank this round (fewer than 2 registered approaches — ranking
skipped). Next round re-seeds the field from the outliner's new framings.

build set: (none — all three RETHINK; re-outline required before any build)
