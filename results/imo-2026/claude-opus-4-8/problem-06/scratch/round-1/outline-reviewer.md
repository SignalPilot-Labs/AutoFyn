# Outline review — imo-2026-06 (round 1)

## Cross-cutting check first: the shared foundation and finish are SOUND

I verified the two proved tools and the shared finish that all three approaches rely on, and they hold up:

- **T1 (gaps ≤ a_1):** correct. Every multiple of a_1 hits every S_i because a_1 and a_i share a prime; each length-a_1 window has one. Computationally maxgap ≤ a_1 confirmed.
- **T2 (pairwise gcd>1):** correct by symmetry of the defining condition.
- **The "for every n" upgrade is genuinely clean and does NOT need any extra machinery.** Given the eventual admissible set A = ∩_i A_i is periodic mod a finite M: every term a_n ∈ A (T2 → a_n hits every minimal clause), and a_{n+1} = min(A_n∩(a_n,∞)) with A ⊆ A_n and a_{n+1} ∈ A gives a_{n+1} = min(A∩(a_n,∞)) for ALL n. Since a_1 ∈ A (T2), the sequence is the increasing enumeration of A from n=1, so a_{n+T}=a_n+L with L=M, T=|A mod M|. This step-by-step check passes.

**Consequence for review: the ENTIRE difficulty of the problem is the single crux — A has finitely many essential primes (is periodic mod a finite M). Everything else is genuinely trivial once that is in hand.** This is exactly the single-shared-gap situation the orchestrator warns about, and all three approaches sit on it. See the diversity flag at the end.

**Empirical confirmation of the crux target (computational, this round):** I simulated the sequence for a_1 ∈ {6,9,15,21,35,77,91,105,143,187,209,221,247,299,323,391,437,1001}. Every case that ran long enough became exactly periodic (a_{n+T}=a_n+L), and in EVERY case the prime factors of L were ≤ maxpf(a_1) — including new essential primes not dividing a_1 (e.g. a_1=143 → L=2·3·11·13; a_1=77 → L=2·7·11). So clique-descent's target bound "essential primes ≤ maxpf(a_1)" is not chasing a false lemma; it is empirically true. Good.

---

## clique-descent — APPROVE (build)

**Verdict: strongest of the field.** It attacks the actual crux head-on with a concrete, empirically-confirmed target (essential prime ≤ P₁ = maxpf(a_1)) and a stated non-circular mechanism (a large prime q>P₁ in supp(a_k) is redundant because supp(a_k) contains a strictly smaller clause, so q never sits in a MINIMAL clause). The mechanism is plausible and the difficulty is honestly flagged ("producing that dominating sub-clause from the bounded-gap dynamics" is unwritten). The finish (steps 4–6) is complete and correct as checked above.

Issues to fix while building (none fatal):
- **Step 3 (A is a GCD-clique) is dead weight — drop it or demote it.** It is proved (all elements of A are terms, hence pairwise non-coprime by T2 — I confirmed the tail is pairwise non-coprime), but steps 4–6 never use it (step 4 uses T2 on minimal clauses, not the clique property). Carrying it adds the delicate "lift a coprime pair by periodicity above a_N" sub-argument for no payoff. Remove it to shrink the surface area.
- **The crux (step 1) is the whole proof.** The builder must produce the domination/redundancy argument, not restate the empirical bound. A useful lever already available: every term shares a prime ≤ P₁ with a_1 (T2 with i=1), so every term has a prime factor ≤ P₁ — this is the natural starting point for showing the large prime is never in a minimal clause. State it as such.
- Any finite bound suffices (approach already notes this); the explicit P₁ bound is a convenience, not a requirement.

## sieve-closure — CHANGES REQUESTED (build)

**Verdict: keep as the second framing, but its independence from the crux is currently illusory and must be made honest.** The vacuous-constraint / fixed-point lemma (a self-consistent A_n is fixed forever) is a genuinely nice, correct structural insight — and self-consistency does hold (every element of A is a term, so pairwise non-coprime by T2). That part is sound.

Issues:
- **The Φ-monovariant does NOT escape the crux.** The approach itself concedes (step 1 and "watch out for") that Φ lives in a space that is finite only if essential primes are finite — i.e. it still needs the SAME bound as clique-descent, and "if that sub-lemma is only available as the prime bound, this approach collapses toward clique-descent." So as written this is not an independent second mechanism; it is a reformulation. The builder must either (a) bound Φ genuinely independently of the essential-prime bound (the only way this earns its keep as a distinct lever), or (b) explicitly import the crux as a shared lemma and present only the closure viewpoint as the contribution. Do not present the monovariant as if it dodges the finiteness.
- **Watch the "A_n becomes self-consistent" claim.** Self-consistency of the eventual A follows from "all its elements are terms," which is a consequence of the finish (stabilization). Guard against using stabilization to prove the thing that is supposed to yield stabilization — spell out that the monovariant argument for "A_n becomes self-consistent" stands on its own (Φ strictly drops on effective steps within a finite space) and does not smuggle in the enumeration finish.

## finite-state-bijection — RANK LAST, not in build set this round

**Verdict: not broken, but it makes no independent progress on the one thing that matters and its novel machinery is unnecessary.** Step 1 imports the crux wholesale (no new attack). Its headline contribution — reversibility/bijection ⇒ pure periodicity from n=1 — solves a problem that the shared min-of-superset finish already solves more simply and rigorously (see the cross-cutting check: "for every n" needs no bijection at all). Its step 4 per-cycle advance accounting is acknowledged to be delicate, and the "safe fix" is to fall back to "each length-M window holds exactly |A| values in order" — which is precisely the plain finish. So the reversibility apparatus adds risk without adding reach.

To earn a build slot in a later round it must offer a genuinely independent attack on the crux (the finiteness of essential primes), not repackage the finish. Kept in the pool for breadth, ranked last.

---

## Diversity flag for the orchestrator (important)

All three approaches share ONE crux — essential-prime finiteness / periodicity of A mod finite M — and the shared finish makes everything else trivial. Their "distinct mechanisms" do not actually diverge on the crux: clique-descent attacks it (number-theoretic domination), sieve-closure reformulates it but concedes it collapses back to the same bound, and finite-state-bijection imports it outright. **The field currently has one wall and three names for it.** If clique-descent's domination argument stalls, the other two stall with it. Next round, if the domination route does not close, put ≥1 approach on the table that attacks the finiteness from a genuinely different framing (e.g. a direct pigeonhole/finiteness on constraint patterns bounded by gaps ≤ a_1, or an argument that bounds the modulus M via the bounded-gap dynamics without ever isolating "minimal clauses") — not another repackaging of "essential primes are bounded."

## Head-to-head ranking (updated, K=32 from 1500)

1. clique-descent — 1531.3 (attacks the crux directly; concrete, empirically-confirmed target; clean finish)
2. sieve-closure — 1500.7 (distinct closure viewpoint, but crux-independence unproven; must not masquerade as dodging the bound)
3. finite-state-bijection — 1468.0 (imports the crux; novel machinery unnecessary — finish already gives "for every n")

build set: clique-descent, sieve-closure
