# Per-role rules for math-explorer

ALWAYS: for a "blackboard/board process" problem filed under `number_theory` in
problems.jsonl, also search the crux corpus's **combinatorics** domain
(subtopics `invariants-and-monovariants`, `processes-and-algorithms`) — this
genre is filed mostly under combinatorics in the corpus even when the surface
content is number theory (round 1, imo-2026-01: only 2 NT hits for
`invariants-and-monovariants` vs 229 combinatorics hits for the same
subtopic-family; the best partial analogs found were all combinatorics-filed).

ALWAYS: for a "replace two board entries m,n with f(m,n),g(m,n)" problem built
from gcd/lcm, reformulate via p-adic valuation per prime immediately — gcd/lcm
become coordinatewise min/max on exponents, and the whole process decouples
into independent per-prime combinatorial recursions all driven by the same
sequence of move-positions. This reformulation is usually the actual unlock
(round 1, imo-2026-01: turned an opaque gcd/lcm rule into the elementary
transform `(x,y) -> (min(x,y), |x-y|)` per prime, which is literally the
subtractive Euclidean algorithm and immediately suggests both the termination
potential and the invariant).

ALWAYS: stress-test a conjectured board/process invariant or monovariant with
randomized-move-order full-process simulation (many trials x many distinct
initial configurations), not just 1-2 hand-worked examples, before reporting it
as a strong lead — cheap in Bash/python and catches errors hand-algebra misses
(round 1: 330 full-process random-order simulations across 11 initial
multisets, 0 mismatches against a closed-form conjecture, gave real confidence;
a separate 20,000-random-pair check caught a wrong case-boundary in my own hand
derivation that "looked obviously right").

NEVER trust a hand-derived case-boundary in a monovariant argument (e.g. "which
exact condition makes the counter tick down vs stay flat") without a numeric
cross-check across many random inputs — round 1 mis-stated a boundary (thought
"count stays flat" required `gcd(m,n) < min(m,n)` strictly; the true condition
is just `gcd(m,n) > 1 and m != n`, which also covers the divides-exactly case
`gcd(m,n) = min(m,n)`) and only caught it via a 20,000-pair randomized check.

NEVER assume "gcd of the whole board" (or "lcm of the whole board") is
invariant, or even monotonic in a useful direction, in a >=3-number gcd/lcm
exchange process — refuted numerically in round 1 (board `(128,64,32)`: one
move on the first two entries drops the overall board gcd from 32 to 2). The
real invariant for such problems is generally a per-prime / per-coordinate
quantity combined multiplicatively across primes, not a single running gcd.

NEVER fetch the problem's actual AoPS/competition solution thread even when
`problems.jsonl` supplies a live URL and network access is available — this
defeats the benchmark's purpose of testing genuine derivation. Rely only on
`knowledge_base.md`, the crux corpus, and your own reasoning/numerical probing
(round 1, imo-2026-01 had a real AoPS URL in its `url` field; deliberately not
fetched).
