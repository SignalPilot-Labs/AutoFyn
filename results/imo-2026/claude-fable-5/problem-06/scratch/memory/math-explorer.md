ALWAYS: For IMO-level "sequence is eventually periodic" problems, track both the "minimal prime-set antichain" AND the "effective valid set" (periodic mod L) — they can diverge (antichain can keep growing while valid set stabilizes, as in a1=210 all-even case). (round 1, imo-2026-06)

ALWAYS: For greedy sequence problems, compute T and L numerically from the first several terms to confirm the period parameters, then verify "all n" (not just eventually). The period often starts from n=1. (round 1, imo-2026-06)

ALWAYS: In gcd/prime problems, the key lemma "every term has a prime in P*" (P* = primes appearing infinitely often) follows immediately from: if all primes of a_i were finitely-frequent, eventually no term shares a prime with a_i, contradiction. State this early. (round 1, imo-2026-06)

NEVER: Assume the minimal prime-set antichain directly stabilizes without first checking the "self-reinforcing" property (every valid hitting set dominated by some element). The antichain can grow indefinitely while the effective constraint doesn't change. (round 1, imo-2026-06)

ALWAYS: For greedy gcd sequences, verify computationally that every pair of terms shares an S-prime (core prime from L's factorization). Run random pair checks — this is the KEY LEMMA for the quasi-periodicity proof. (imo-2026-06, round 1)

NEVER: Assume large primes stop appearing in greedy gcd sequences. They appear roughly once per period at shifting positions. The S-prime "skeleton" is what's truly periodic; large primes are decoration. (imo-2026-06, round 1)
