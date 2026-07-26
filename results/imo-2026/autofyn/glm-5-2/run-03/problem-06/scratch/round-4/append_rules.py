import os
path = "/tmp/memory/math-explorer.md"
existing = ""
if os.path.exists(path):
    with open(path) as f:
        existing = f.read()
addition = """

ALWAYS: when scouting a substitution/morphism or combinatorics-on-words framing for an increment sequence, first ask whether the framing is CIRCULAR — every periodic word is trivially morphic (σ: w→ww), so "is (d_n) a fixed point of a substitution" presupposes the periodicity it's asked to prove; morphic ≠ periodic (Thue-Morse, Fibonacci), so morphicity alone never closes the gap (round 4, substitution-morphism lens on imo-2026-06).

NEVER: cite Morse-Hedlund (bounded subword complexity ⇔ periodic) as a non-circular proof lever without first checking the threshold n where p(n)≤n — for a primitive periodic word of period T the threshold is exactly T, so MH gives back the period, not a shortcut (round 4, imo-2026-06: tested 10 cases, all first-n-with-p(n)≤n equals T).

NEVER: claim a "palindrome / reflection symmetry of the increment period" as a greedy-dynamic invariant without checking universality — for imo-2026-06 it holds only in ~half the cases (15,77,91,105,1001 yes; 35,65,143,1309,2085,385 no) and is a CONSEQUENCE of B_∞ being L-periodic + closed under negation, not an independent route to it (round 4).

ALWAYS: before recommending a "finite-state transducer / window-state substitution" framing, verify the transition is finitely determined — the imo-2026-06 window-state σ_n→σ_{n+1} leaks the free-rider (non-P_1) primes of a_{n+1}, which is exactly Gap A; the minimal functional modulus for d_n is the full period L itself (round 4, re-confirms round 3).

ALWAYS: search the crux corpus HONESTLY for combinatorics-on-words results — for imo-2026-06 there are NONE (no substitution/morphic/Cobham/automatic/Morse-Hedlund/EKG/Recamán crux; all "substitut" hits are algebraic variable substitution, all "automatic" hits are the English word, all "morphic" hits are graph-morphism contexts). Do not force a wrong match (round 4).
"""
if "round 4" not in existing:
    with open(path, "w") as f:
        f.write(existing + addition)
    print("appended")
else:
    print("already has round-4 rules")
