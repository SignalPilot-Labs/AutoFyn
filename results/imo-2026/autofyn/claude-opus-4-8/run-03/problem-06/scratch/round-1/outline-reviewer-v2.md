# Outline review v2 — imo-2026-06 (ranking gate, second pass)

## Headline
The re-plan does NOT repeat the refuted premise. Last pass killed "primes q > P_max never
change the greedy successor" (P_max = max primes(a_1)). The new field thresholds at
**M = ∏ primes(a_1)**, a strictly larger cutoff, and the 385 counterexample dissolves under
it: 19 < M = 385, so the 406→418 shortcut is NOT an exception for any of the new approaches.
Two of the three are sound reductions with genuinely open (not false) cruxes. The third
re-imports the refuted unbounded-memory wall under a new label and is cut.

## Free lemmas — all three verified CORRECT (I re-derived + simulated)
- **Anchor** (every term shares a prime with a_1, so has a prime in P, all ≤ M): correct.
- **Gap bound** (every multiple of M is admissible ⇒ gap ≤ M ⇒ a_n = Θ(n)): correct.
- **Distance–prime** (q|a_i, q|a_j ⇒ q | a_i−a_j ⇒ q ≤ |a_i−a_j|): correct.
- **Structural fact 1** (q∤L ⇒ q divides exactly one k-class mod q of each phase ⇒ q divides
  ∞-many terms): correct; confirms "recurrent primes" is infinite and the only finite object
  is primes(L).
- **Confinement (p|L ⇒ p ≤ M)**: I simulated every seed that reaches a period
  (6,10,12,14,15,20,21,22,26,33,34,35,38,39,45,55,65,77,91,105,143,1155-partial). Confinement
  held in 100% of periodic cases; never violated. It is open-but-true, correctly flagged as a
  gap, not smuggled as free.

## Simulation findings that drove the verdicts
- Greedy simulator + period finder + anomaly counter (threshold M) over ~2000 terms/seed.
- **Anomalies (prime > M as sole witness) = 0** on every seed tested, including a_1 = 385
  (M = 385: 19 < M, not an anomaly) and 105, 1155. The phenomenon the outline fears is empirically
  absent under the M threshold — favorable for anomaly-count, and it confirms the M cutoff, not
  P_max, is the right dividing line.
- **Post-anomaly stabilization is AUTOMATIC.** Every term's ≤M-support is a nonempty subset of
  the fixed finite set {p ≤ M} (nonempty by Anchor). The family of distinct ≤M-supports is a
  monotone-increasing subset of a finite power set, hence eventually constant — no separate
  stabilization crux is needed for anomaly-count. This makes its reduction tighter than the
  outline claims.
- **Minimal-support alphabet** (antichain approach) over full runs: 105→{2,3,5,7}=primes(L);
  385→{2,3,5,7,11,19}; 1155→{2,3,5,7,11}. Finite in every run — consistent with Crux Lemma 1.

## Verdicts

### anomaly-count-terminates — APPROVE  (rank 1, Elo 1516)
Reduction is airtight. I checked the endgame independently: after the last anomaly, admissibility =
"c mod K ∈ U" for a FIXED residue set U (K = ∏_{p≤M} p, U fixed once the ≤M-support family
stabilizes — which is automatic, above). The successor map on Z/KZ is well defined; its orbit is
eventually periodic; the increment over a residue period is a multiple of K, giving a valid (T,L).
No-transient follows from injectivity. Note the map yields a NON-minimal (T,L) — that is fine, the
problem only asks for existence, not the minimal period (I checked: for 105 the true (58,210) is
finer than the mod-K period, but a valid larger (T,L) still exists, no contradiction).
- Sole open crux: **anomaly finiteness** (GAP-1). The rigidity half is sound (a persistent
  sole-witness q would divide L, so q ≤ M, contradiction), so anomalies cannot recur in the
  periodic regime; the honest missing piece is a monovariant forcing the transient to END. This is
  a real, attackable, single crux — the strongest reduction in the field.
- Minor: GAP-2 (confinement) is genuinely open but true (verified). Builder should prove it, not
  assume. And the outline's watch-out "385-type: anomalies occur early" is empirically off — 385
  has 0 anomalies under the M threshold; don't rely on 385 as an anomaly witness.

### redundant-constraint-antichain — APPROVE  (rank 2, Elo 1484)
The antichain reduction (admissible ⟺ meet every ⊆-minimal support; F_i⊇F_j ⇒ i redundant) is a
correct, purely set-theoretic step. Crux Lemma 1 (minimal supports use a finite prime alphabet) is
open but not false — simulation shows finite alphabets, and it is a genuinely DIFFERENT statement
from the refuted premise (large primes DO enter minimal supports, e.g. 385's {…,19,…}; the claim is
they get DOMINATED by later small-only supports, not that they never appear).
- Two open gaps rather than one (GAP-1 finite alphabet + GAP-2 stabilize to fixed U mod L), making
  it a hair vaguer than anomaly-count — hence ranked second. Both gaps are legitimate, not circular.
- Watch: Crux Lemma 1's stated mechanism ("a later small-only support ⊆ its small part appears")
  needs the covering/gap argument actually written; do not leave it as "empirically."

### reversible-state-bijection — RETHINK  (cut, not registered)
Two fatal problems, both concrete:
1. **The distinguishing finiteness mechanism is FALSE — it uses distance–prime BACKWARDS.** The
   outline claims "each large prime, by distance–prime, pairs with a term within a bounded number of
   steps and is discharged." Distance–prime gives the OPPOSITE: if q is large and q|a_{n+1} and
   q|a_i (the constraint it satisfies), then |a_{n+1}−a_i| ≥ q, so a_i is ≥ q/M steps back —
   arbitrarily FAR, not within a bounded window. This is exactly the unbounded-memory wall I refuted
   last round (sole-large-witness reached 1453 steps back at N=1500). The "bounded, invertible
   record of recently-introduced large primes" therefore has no valid finiteness justification; it
   is the refuted bounded-memory premise relabeled. The reduction (finite augmented state ⇒
   bijection) is broken because the finite state it acts on is not established.
2. **Even salvaged, it is NOT a diverse third approach — it collapses onto anomaly-count's crux.**
   The large primes that actually need tracking for backward-determinism are precisely those that
   are sole witnesses = anomalies. "Record is bounded" ⟺ "only finitely many anomalies" = exactly
   anomaly-count's GAP-1. So its state finiteness reduces to approach 2's wall; the only extra is
   the injective-inverse endgame, which approaches 1 and 2 already use for no-transient
   (injective finite self-map ⇒ bijection ⇒ from-n=1). It adds a wall, not a framing.
Direction if re-seeded: keep the from-n=1-for-free bijection idea only as an ENDGAME grafted onto a
finite state established by another route; do NOT re-plan a standalone "bounded large-prime record."
For a true plateau-breaker, seed a framing that does NOT route through mod-M/mod-K at all
(potential-function / minimal-counterexample on the first index where from-n=1 periodicity fails, or
a density-increment argument), and verify any new shared premise on a_1 ∈ {385, 5·7·13, 187, 209,
247} — the three-odd-prime seeds where no period was found within 2000 and large shortcuts fire.

## Diversity assessment
Survivors 1 and 2 are two different mechanisms — order-theoretic DOMINATION (antichain) vs analytic
COUNTING + rigidity monovariant (anomaly) — but they are ADJACENT: both aim to control large-prime
witnesses and both depend on confinement (p|L ⇒ p ≤ M). They are not the single-gap trap (their top
cruxes are distinct: "large supports dominated" vs "anomalies finite," and one can fall without the
other), but they are not far apart either. Flag for the orchestrator: if both plateau on
"control large primes / confinement" for 2–3 rounds, next round MUST seed one approach from a
framing that does not route through a fixed modulus at all (see direction above). Cutting the broken
reversible approach removed the field's only far-out framing — restore diversity next round with a
NEW framing, not by resurrecting the bounded-record.

build set: anomaly-count-terminates, redundant-constraint-antichain
