# proof-outliner role memory

ALWAYS: for imo-2026-06, two tools are elementary & fully provable and should anchor every approach — (T1) every multiple of a_1 is admissible ⇒ gaps ≤ a_1; (T2) gcd(a_i,a_j)>1 for ALL i≠j ⇒ every term hits every clause. The "for every n" finish is then clean: a_{n+1}∈A is the min of the larger set A_n ⇒ sequence = greedy enumeration of the periodic set A from n=1. (verified computationally, round 1)

ALWAYS: for imo-2026-06 the ENTIRE difficulty is one crux — stabilization (finitely many essential primes / A_n eventually constant mod M). Empirically every essential prime ≤ maxpf(a_1) and maxgap ≤ a_1. Don't waste approach diversity on the finish; diversify the ATTACK ON THE CRUX. (round 1)

ALWAYS: register_approach is idempotent (refreshes summary if slug exists); ranker functions are plain importable python in .autofyn/approach_ranker.py (no CLI/argparse) — call via `python3 -c "import sys; sys.path.insert(0,'.autofyn'); import approach_ranker"`. (round 1)

NEVER: for this problem, claim A = {m : some prime of a_1 divides m}; A is the finer TRANSVERSAL set (e.g. a_1=35 ⇒ A={10|m or 15|m or 35|m or 42|m}). (round 1)

ALWAYS: for imo-2026-06, the finiteness-crux ground set is {primes ≤ a1}, NOT {primes ≤ P1=maxpf(a1)} (because Lemma S with P1 is FALSE: a1=385 has essential prime 19>P1=11; the corrected Lemma S' "two clauses share a prime ≤ a1" holds 0 violations and gives clean Prop 1' via Cor E.1, round 2).
ALWAYS: verify a candidate crux lemma computationally BEFORE outlining an approach on it (round 1's Lemma S was outlined false and cost a whole round; a 20-line sympy check caught the correct threshold in round 2).
NEVER: let all rival approaches bottom out on the identical sub-claim; imo-2026-06 all three hinge on "bound distinct large essential primes" — I split them into 3 distinct walls (direct-descent proving S', extremal gap-count, witness-cascade) so they don't die together (round 2).
