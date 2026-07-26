# proof-builder — two-coincidence-periodicity (round 5)

## What I proved

**Lemma 1 (promotable): the `aimo-0907` coincidence criterion, re-proved from scratch.** Two parts, using only single-valuedness of a map f:X→X (no finiteness):
- (A) ONE self-coincidence f^a(x)=f^b(x) ⇒ the orbit (f^n(x)) is eventually periodic with period b−a. Proof: apply f^k to both sides.
- (B) TWO between-orbit coincidences f^n(x)=f^m(y), f^p(x)=f^q(y) with distinct offsets n−m≠p−q ⇒ O(y) eventually periodic (contradiction if O(y) infinite). Proof: compose the two equalities to get f^{p+m}(y)=f^{p+m+Δ}(y), Δ=(n−m)−(p−q)>0, then invoke (A). This is exactly `aimo-0907` Case 2's argument; it ports verbatim because only single-valuedness is used.

**Diagnostic (rigorous): the route collapses to Gap A.** The outline-reviewer's mechanism-confusion flag is confirmed and resolved:
- For a SINGLE forward-deterministic orbit, part (A) shows ONE coincidence already gives periodicity — the "second coincidence" is redundant for the orbit. The genuine two-coincidence content (part B) is a BETWEEN-ORBITS mechanism and does not transfer to one greedy orbit.
- The route's true antecedent is "exhibit a finite forward-deterministic DETERMINING statistic α" (forward-deterministic so a pigeonhole self-coincidence propagates by (A); determining so α-periodicity lifts to d-periodicity). This antecedent is EXACTLY Gap A (finiteness of the determining state = L-periodicity of B_∞ = finiteness of governing primes). The route does NOT go around Gap A as the outliner claimed — Step 3's pigeonhole IS a finiteness assumption.
- The f(M_1)-bounded sub-case is FENCED by the round-5 T-unbounded-in-M_1 impossibility (rad-77 witness: a_1=77→T=18 vs a_1=847→T=1744 at the same M_1=77). Such an α would force T ≤ |alphabet| ≤ f(M_1), contradiction.

## Computational probe (ran it, /tmp/round-5/probe_coincidence.py)

Naive correct gcd-greedy on a_1 ∈ {15,35,77,91,175} (a_1=385 too slow at N=1500, period not reached). d_n ≤ M_1 re-confirmed in every case (linchpin-and-gap-bound). For each candidate abstraction α (witness-prime-tuple, d_n itself, a_n mod M_1):

| a_1 | T(d) | T(α_a) | α_a realized | α_a fwd-det conflicts | α_a determines-d conflicts |
|-----|------|--------|--------------|----------------------|---------------------------|
| 15  | 8    | 4      | 2            | 2 (every state)      | 2 |
| 35  | 34   | 34     | 2            | 2                    | 2 |
| 77  | 18   | 18     | 2            | 2                    | 2 |
| 91  | 20   | 10     | 2            | 2                    | 2 |
| 175 | 274  | 274    | 3            | 3                    | 3 |

Read-out: EVERY named abstraction is NOT forward-deterministic (every realized symbol has ≥2 distinct successors). The witness-prime word's period is a proper divisor of T(d) when smaller (15: 4|8; 91: 10|20) — the structural sub-period leak — so its self-coincidences do not pin position within T and cannot lift to d-periodicity. d_n itself is not forward-deterministic. a_n mod M_1 is the round-3 fenced residue statistic. So no candidate meets the antecedent of Lemma 1(A); the "second coincidence" (GAP A3) is moot — there is no first propagating coincidence to double.

## Gaps remaining (Status = partial)

- The load-bearing antecedent (∗): exhibit a finite forward-deterministic determining statistic α that is NOT f(M_1)-bounded (to escape the impossibility) yet still finite-alphabet (for pigeonhole). No such α identified; named candidates all fail forward-determinism. This is Gap A in coincidence-doubling costume.
- The "second coincidence" (outline GAP A3) is shown to be REDUNDANT for a single orbit, not load-bearing as claimed; the genuine load is forward-determinism + determining of α, which is the wall.

## Lemma proposal

Proposing Lemma 1 (aimo-0907 coincidence criterion, parts A+B) for certification into results/imo-2026-06/lemmas/. Statement and full proof in the approach file, Step 1. Reusable by any approach that needs a deterministic-process periodicity criterion; the consumer supplies the forward-deterministic map antecedent.

## Recommendation

The route is honest-partial; it does NOT bypass Gap A. One reusable lemma (aimo-0907 criterion) is the positive deliverable. If no genuinely non-f(M_1)-bounded finite determining statistic can be exhibited (none on the table), the route should be retired and the run should consolidate.

Files:
- /home/agentuser/repo/results/imo-2026-06/approaches/two-coincidence-periodicity.md
- /tmp/round-5/probe_coincidence.py (computational probe)
