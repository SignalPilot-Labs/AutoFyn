# proof-builder report: triangle-critical-dichotomy-witness (round 20)

## Mandatory equivalence check (result: NOT a duplicate)
Compared against `triangle-consistency-pigeonhole`'s existence gap. The
sibling's object is a *global* gcd-value pigeonholed over many later
occurrences of the OTHER type at one fixed early witness (forward). This
approach's object was a *local, pairwise* prime-intersection fact
`P(a_i)∩P(a_n)={q'}` between one later term and one specific earlier
rescued index of unconstrained type (backward). These do not collapse
under relabeling — confirmed genuinely distinct constructions, matching the
outline-reviewer's read.

## Stronger, decisive finding (supersedes the equivalence question)
Proved unconditionally: for every n≥2 and every prime p|a_n with
e:=v_p(a_n), c:=a_n/p^e ≤ a_{n-1} (Universal Branch-(a) Dominance Theorem).
Proof uses only the certified Bounded Gap Lemma (a_{m+1} ≤ a_m+a_1) and
strict monotonicity of (a_n): for n≥3, a_{n-1}>a_1 forces a_n<2a_{n-1}
strictly, and p^e≥2 gives c<a_{n-1}; for n=2 (boundary), a_2≤2a_1=2a_{n-1}
and p^e≥2 gives c≤a_{n-1} (equality attainable, e.g. a_1=5, a_2=10, p=2).

Consequence: branch (b) ("sole rescuer") of the certified Critical Prime
Dichotomy Lemma NEVER fires — for any n, any prime, any core. Confirmed
computationally with zero exceptions: both known hard seeds a_1=4807
(N=3000, 2997 checked instances) and a_1=11305 (N=2500, 2087 instances) at
their recruited cores, plus 1996 additional seeds a_1∈{4,...,1999} at
N=800 each. Scripts at /tmp/round-20/sim_dichotomy2.py, sim_fast.py,
sim_fast2.py, sim_ratio.py.

## Verdict
This approach's entire mechanism (outline Step 2: invoke branch (b) to get
a rescued index) has no legitimate instance to act on. Recommend RETHINK
for this slug (dead, not merely stalled) — independent of the equivalence
check outcome. Also flagged for the reviewer: the certified
`lemmas/critical-prime-dichotomy.md` Scope paragraph's hypothetical
("nothing prevents two distinct primes... each satisfying branch (b)")
describes a scenario now shown to be vacuous; recommend an added
corollary/note there.

## Status
unsolved — but genuine, fully proved, reusable negative content delivered
(Universal Branch-(a) Dominance Theorem), proposed under Promotable lemmas
for reviewer certification.

File: /home/agentuser/repo/results/imo-2026-06/approaches/triangle-critical-dichotomy-witness.md
