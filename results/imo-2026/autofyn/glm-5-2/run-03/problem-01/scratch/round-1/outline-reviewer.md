# Outline review — imo-2026-01 (round 1)

Problem: 2026 integers >1 on a blackboard. Move (m,n)→(gcd, lcm/gcd). Prove (a) terminates with exactly one M>1; (b) M is choice-independent.

Three approaches proposed. I read the problem, both explorer reports, the outliner field, and the three skeletons. I tested the load-bearing identities with Python (gcd-preservation, the Ω-difference identity, the terminal-formula M=∏p^{d_p}, and uniqueness of the normal form on 300 random triples). Findings below.

---

## perprime-gcd-lexmonovariant — APPROVE (one arithmetic slip to fix)

The strategy is sound and essentially complete; both parts are settled by elementary tools. Verified empirically:
- gcd(min(α,β),|α−β|)=gcd(α,β): 10000/10000 cases pass. (Euclidean identity, KB line 86.)
- Terminal M = ∏_p p^{d_p} where d_p = gcd of the multiset of initial p-exponents: 3000/3000 random plays match. (Note M ≠ gcd of the numbers — the skeleton flags this correctly; {2,3}→M=6.)
- Move case analysis (coprime / non-coprime m≠n / m=n) is exhaustive: the g=1, m=n case is impossible (m=n>1 ⇒ gcd=m>1), correctly noted. (Ω,K) strictly lex-decreases in all three cases; Ω ∈ ℕ, K ∈ [0,2026] both bounded below ⇒ well-founded ⇒ termination.
- "Exactly one" via d_p: terminus K=0 ⇒ all d_p=0 ⇒ initial all-ones, contradicting a_i>1. Airtight. Equivalently d_p≥1 for some p ⇒ M>1 at terminus ⇒ K≥1; combine with stuck⇒K≤1.
- The coupling subtlety (moves fire on all primes simultaneously) is correctly handled: (b)'s invariant is per-prime and unaffected by coupling; (a)'s termination is global via (Ω,K), NOT via per-prime Euclidean completion. The skeleton explicitly warns the builder not to attempt per-prime Euclidean-to-completion. Good.

**One fix required (CHANGES-style, do it while building):** the key-lemma description states
  Ω(m)+Ω(n) − [Ω(gcd)+Ω(lcm/gcd)] = 2·Ω(gcd) ≥ 0, equality iff gcd=1.
This is **wrong**. The correct identity (verified 10000/10000) is
  Ω(m)+Ω(n) − [Ω(gcd)+Ω(lcm/gcd)] = Ω(gcd)  (≥1 iff gcd>1).
Reason: Ω(lcm/gcd)=Ω(lcm)−Ω(gcd)=Ω(m)+Ω(n)−2Ω(gcd), so Ω(gcd)+Ω(lcm/gcd)=Ω(m)+Ω(n)−Ω(gcd). The skeleton's step-3 conclusion ("Ω drops by Ω(g)≥1") is itself correct — the error is only in the intermediate "2Ω(g)" parenthetical. The monovariant still strictly decreases (Ω drops by Ω(g)≥1 when gcd>1; Ω fixed and K drops when gcd=1). Builder: write the identity as Ω(g), not 2Ω(g). Flagged honestly, not a fatal flaw.

All other items (well-foundedness statement, stuck⇔K≤1, gcd(e,0,…,0)=e convention, finiteness of the prime set, the {12,18,30,7,100,9,25}→210 verification) are appropriately listed as gaps to close. KB lines 86/117/191/184 all verified present.

---

## exponent-multiset-dershowitz — RETHINK (fatal: the multiset-decrease lemma is false)

The load-bearing lemma of step 3 — that every legal move strictly decreases the multiset of exponent vectors in the Dershowitz–Manna order induced by the componentwise partial order — is **false**. Concrete counterexample:

  m=4 (=2²), n=9 (=3²). Exponent vectors (primes 2,3): u=(2,0), v=(0,2).
  Move: gcd(4,9)=1, lcm/gcd=36. New vectors: min-cw=(0,0), |u−v|=(2,2).
  Removed multiset {(2,0),(0,2)}; added multiset {(0,0),(2,2)}.

In the DM multiset order (M>_DM N iff N is obtained from M by replacing some nonempty X⊆M with Y where every y∈Y is strictly below some x∈X, componentwise): the added vector (2,2) is **not** strictly below either removed vector — (2,2)≮(2,0) and (2,2)≮(0,2); in fact (2,2) dominates both. So {(2,0),(0,2)} ≯_DM {(0,0),(2,2)}. The multiset actually *grows* in the componentwise-max sense.

The skeleton's step 3 only checks that the *min* is strictly below the max-cw; it forgets that the *diff* vector (= max-cw when u,v have disjoint supports, as in any coprime pair) need not be below any removed element. This is exactly the coprime case the approach claimed to avoid case-splitting on — and the case split is precisely what makes the (Ω,K) route work. Without it, no natural single-coordinate multiset order decreases (Ω of the diff vector = Ω(m)+Ω(n)−2Ω(g) equals Ω(m)+Ω(n) when g=1, i.e. Ω is also unchanged — the very reason the direct route needs the secondary K coordinate).

The natural salvage (use Ω as the per-vector key, then add K) collapses this approach into the (Ω,K) lex route — a technique-clone of perprime-gcd-lexmonovariant, not a different framing. Per the dispatch's anti-clone rule, this should not be kept as a rival. The approach cannot be built as outlined; it must go back to the outliner for a genuinely different framing (or be dropped). Do not register.

---

## confluence-newman — CHANGES REQUESTED (diversity bet; the hard lemma is an unproven hand-wave)

The framing is genuinely different — it reframes (b) as "the rewriting system has a unique normal form" and attacks it via Newman's lemma (terminating + locally confluent ⇒ confluent), NOT by computing M. This is real diversity of thought, not a technique-clone: the direct route's (b) is an invariant computation; this route's (b) is a rewriting-theorem consequence. It reuses (Ω,K) for termination and d_p for "exactly one," but its distinct contribution (b-via-confluence) is independent of the direct route's (b)-via-invariant.

Uniqueness of the normal form verified empirically (300 random triples, 0 multi-normal failures) — so the critical-pair joinability is very likely true; the route is not doomed.

**Honest flags (builder must close):**
- The load-bearing lemma — local confluence for overlapping critical pairs (step 3, case B: state {a,b,c}, moves on (a,b) and (a,c)) — is **named without a mechanism**. The skeleton says "empirically verified on 20+ random triples; the algebraic proof is the open gap." That is an unverified hand-off. The builder must exhibit the explicit common reduct of the two branches {g_ab,h_ab,c} and {g_ac,h_ac,b} by named moves and verify equality via gcd/lcm algebra. If the algebra does not close, the approach dies on step 3 (on a DIFFERENT gap than the direct route — that is the point of the diversity bet). This is the genuine risk and it is load-bearing.
- Newman's lemma is NOT in knowledge_base.md — must be stated precisely as a named theorem of abstract rewriting theory (terminating + locally confluent ⇒ confluent) or the reviewer rejects it.
- The (Ω,K) monovariant should be at least sketched or imported as a certified lemma so step 2 is not a bare assertion.
- "Normal form = stuck state = ≤1 entry >1" must be pinned so confluence yields "all reachable stuck states are the same multiset."
- Verify no other critical-pair shape exists (disjoint redexes commute — case A; same-pair redexes coincide — not a critical pair). Exhaustive over two-redex configurations.

Worth building as the diversity bet. It is the long shot — the direct route is far more likely to solve (b) — but it is the field's only non-invariant-based framing of (b), and the dispatch explicitly wants framing diversity.

---

## Field diversity note

After cutting exponent-multiset-dershowitz, the field has two framings: invariant/monovariant (perprime) and rewriting-theory (confluence). These are genuinely different routes to (b). The Dershowitz line, had it worked, would have been a *third* (a)-engine — but it collapsed into the (Ω,K) route and its central lemma is false, so it is not a real third framing. If the confluence route's critical-pair algebra fails next round, the orchestrator should ask next round's outliner for a *different* (b)-framing (e.g., a probabilistic/distributional invariant, or a constructive greedy strategy exhibiting a canonical move sequence), not another monovariant variant.

---

## Registration and ranking

perprime-gcd-lexmonovariant and confluence-newman are new; register both. exponent-multiset-dershowitz is RETHINK — not registered (a cut approach never enters the pool).

Head-to-head (no outcomes yet; rank by promise/rigor, anchored to terrain):
- perprime-gcd-lexmonovariant > exponent-multiset-dershowitz (fatal counterexample vs complete correct route).
- perprime-gcd-lexmonovariant > confluence-newman (complete & rigorous vs long-shot with unproven hard gap; both sound, but perprime is closer-to-solved and more rigorous).
- confluence-newman > exponent-multiset-dershowitz (unproven-but-plausible gap vs fatal counterexample; confluence at least has empirical backing and a viable framing).

build set: perprime-gcd-lexmonovariant, confluence-newman
