# Outline review — imo-2026-06 (round 1)

Numerically de-risked the whole outline before judging (600-term greedy sims):
exact-from-n=1 confirmed with `a_{n+T}=a_n+L` for **every** n in range, and
L=∏S for a finite recruited prime set S: a_1=15→(8,30,S={2,3,5}); 105→(58,210,{2,3,5,7});
143→(64,858,{2,3,11,13}); 65→(58,390,{2,3,5,13}); 1001→(282,2002,{2,7,11,13}).
Two facts the whole field must respect are thereby confirmed: (i) S is NOT supp(a_1) —
recruited primes 2,3 appear and are essential; (ii) the exact period down to a_1 needs
the FULL essential set including near-start primes (for a_1=143 the tail minimal period
drops 13 to L=22, but exactness from n=1 requires 13 AND 3, giving L=858). Any approach
that upgrades "eventual" to "exact" by using only the tail's minimal prime set is WRONG.

## Shared-nucleus assessment (the orchestrator's flagged concern)

All three approaches share ONE deep crux: **only finitely many primes are ever the sole
connector (essential)**. This is not a defect of the outlining — it is the genuine heart
of this IMO P6; there is no route to the theorem that avoids proving finite essential S
(even a direct translation-by-L induction must first pin down L=∏S, i.e. finiteness).
So "diversity of framing" here can only mean **diverse attacks on finiteness** plus
**diverse exactness mechanisms**, and the field does deliver both:
- crux attack: density/interval-occupancy counting (admissible-set L3, essential-counting L2)
  vs. constraint-coverage / "old constraints die in a bounded window" (finite-state GAP A/D);
- exactness: static periodic set (free) vs. enlarge-L covering vs. finite-state reversibility.

This is acceptable breadth for round 1. **Flag for the orchestrator:** if all three stall
on finiteness for 3+ rounds, the field is genuinely collapsed to one nucleus and the *only*
real lever is a sharper/different proof of finiteness — route around it is impossible, so
next round should push a genuinely new finiteness argument (e.g. the explorer's "two fixed
primes give bounded gaps ⇒ numbers coprime to S get too sparse" density angle), not a new
finish.

---

## admissible-set-periodicity — APPROVE (primary; Elo 1531)

Cleanest whole-problem attack; exactness comes for free. Skeleton is logically sound and
non-circular:
- Step 1 (each a_n∈A): correct — gcd(a_m,a_n)>1 for m>n is the defining condition, symmetric
  in n, so a_n shares a prime with every OTHER term (past and future); A is defined w.r.t.
  the already-existing infinite sequence, so membership is well-defined. No circularity.
- Step 2 / L1 (enumeration a_{n+1}=min(A∩(a_n,∞))): sound. A⊆{satisfies finite F_n} gives
  min(A∩(a_n,∞))≥a_{n+1}; a_{n+1}∈A (Step 1) gives ≤. Equality. Write the induction cleanly.
- Steps 5–6 (exactly ∏S-periodic down to a_1 ⇒ shifted enumeration): this is the strongest
  exactness handling in the field — A_S is a union of residue classes mod L=∏S over ALL
  integers, so periodicity holds down to a_1, not just in a tail. Confirmed by the numerics.
- Step 4 / L3 (finite essential S): THE gap. Mechanism stated (essential prime ⇒ two terms
  divisible by p connecting only via p; a_n=Θ(n) from bounded gaps ⇒ p divides O(window/p)
  terms; Σ over large p converges). This is the right tool and honestly flagged.

Issues to close while building: (a) the counting in L3 must be made rigorous — the
convergent sum must actually bound the NUMBER OF DISTINCT essential primes, not just their
density; state exactly why a large essential prime forces a coincidence that can happen only
finitely often across all large p. (b) L3's final step "A∩[a_1,∞)=A_S" is correct but spell
it out: if x∈A hit some supp(a_i) only via a non-S prime p, then supp(x)∩supp(a_i)={p} makes
p essential — contradiction; hence every hit uses an S-prime.

## essential-prime-counting — APPROVE (Elo 1500)

Same spine, but headlines the finiteness crux with an explicit sieve bound — valuable because
its L2 counting lemma is exactly what admissible-set L3 also needs, so once certified it
becomes a shared lemma both static approaches import. Building it in parallel is complementary,
not redundant.

Issues to close: (a) Step 3 conflates two different things — "large primes are rare
CO-FACTORS" (a_n=2·p noise) vs "large primes are rarely SOLE CONNECTORS." Only the latter is
essentiality. The greedy-undercut worry in the watch-out (a large-prime multiple being the
smallest admissible x) is about gap structure, NOT essentiality: a_n=2·p has 2 as connector,
so p is not essential. Make the counting count sole-connection events, and this worry
dissolves. (b) The exactness in Step 5 goes "eventual, then enlarge L to L'": acceptable, but
it must invoke finiteness of S over ALL of [a_1,∞) (including near-start essential primes) —
at which point it coincides with admissible-set's clean periodicity. Don't stop at the tail's
minimal S (numerics: 143 needs 13 near start). State P's dependence on R explicitly; no
"large primes are rare" hand-waving (rigor rule).

## finite-state-reversible — CHANGES REQUESTED (Elo 1469; NOT in build set this round)

Not doomed, but strictly the heaviest: it carries the SAME finiteness crux (GAP D) PLUS three
extra gaps (bounded window A, well-defined state B, reversibility C). Its distinctive
contribution — reversibility to upgrade eventual→exact (aimo-0514) — attacks a problem that
the static route DISSOLVES for free (Steps 5–6 of admissible-set give exactness with no
reversibility argument). So its headline machinery is spent on the easy part.

Concrete concerns: (1) GAP C reversibility may be genuinely false in naive form — the
constraint set GROWS forward, so the "back-map = largest admissible residue below on the
shifted window" is not obviously injective; it is only defensible on the stabilized recurrent
state, which requires A and D first. (2) GAP A (bounded live-constraint window) is itself
non-trivial; its tractable form is the observation that the family 𝒯={S∩supp(a_i)} has only
finitely many DISTINCT members (subsets of finite S) — reorder so this rides on finite S/𝒯,
not on an independent "old constraints die" claim.

Its ONE real asset is the constraint-coverage angle on finiteness (a different flavor from
pure density counting). Keep it live in the population as the diversification lever if the two
counting approaches stall on the crux — but do not spend a builder on it this round while its
unique exactness mechanism is redundant. Registered and live; sample it next round if the
static crux attack plateaus.

---

## Ranking (this round)

1. admissible-set-periodicity — 1531 (cleanest skeleton, exactness free, sound)
2. essential-prime-counting — 1500 (explicit crux lemma, feeds the field)
3. finite-state-reversible — 1469 (most gaps, redundant exactness mechanism)

build set: admissible-set-periodicity, essential-prime-counting
