# proof-outliner role memory

ALWAYS: when bounding "essential primes", use Q = {primes ≤ a_1} (the cheap bound from gcd(a_n,a_1)>1), NOT Q = {primes dividing a_1} — the latter is too coarse (drops 2 for odd a_1 like 15, collapsing the residue structure and giving a wrong L_0) (happened in round 1 scouting of imo-2026-06).

ALWAYS: flag the transient/"for all n" ambiguity explicitly. The problem statement "for every positive integer n" requires a_{n+T}=a_n+L for ALL n≥1, but numerics (a_1=1001, 315·385) show transients can be long/nonzero. Every approach that proves EVENTUAL periodicity must address how to absorb the transient (enlarge T,L or argue the quantifier allows the tail) (round 1, imo-2026-06).

NEVER: build any approach on "stabilize the set of ALL primes appearing" — it is INFINITE (proven for a_1=15 via the periodic sub-sequence a_{8k+6}=6(6+5k); generalizes). The right invariant is the ESSENTIAL-prime set (primes that are the unique shared factor with some earlier term); free-rider cofactor primes are infinite but irrelevant (round 1, imo-2026-06).

NEVER: assert P(a_i+L)=P(a_i) (prime-divisor preservation under translation) without weakening — it is FALSE in general. The correct weakening for greedy problems: old primes persist (a_i+L ≡ a_i mod p for p|L ⟹ p still divides a_i+L), and NEW primes only ADD connections (never remove), so the GREEDY MIN decision is preserved upward. Asserting the strong form breaks the proof (round 1, imo-2026-06 translation-self-similarity approach).

ALWAYS: when the field has collapsed to one shared crux and no framing escapes it, satisfy the diversity mandate by fielding genuinely different PROOF ROUTES to the crux itself (descent, propagation, counting) — NOT by re-framing the whole problem (round 2, imo-2026-06). The alt-framing explorer confirmed escape-framing is impossible when the crux is a real structural fact; the descent explorer + corpus explorer supplied the distinct crux-attack mechanisms.

NEVER: field two descent approaches simultaneously (single-gap trap) — when the crux-descent explorer recommends a new descent approach AND the alt-framing explorer recommends a descent-coprime-shift twin, absorb the descent route into the existing leader as its named gap-attack rather than opening a rival descent slug (round 2, imo-2026-06).

NEVER: assert that grid-counting proves Lemma 4 for the FIXED R — aimo-0447's "large prime > interval length" gives large = > (N−1)R (grows with N), so the counting only yields a growing-window analogue (≤(N−1)R), NOT the fixed-R Lemma 4 (round 2, imo-2026-06 grid-counting explorer).

ALWAYS: certify cheap partial lemmas that narrow the counterexample search into `lemmas/` even when the full crux stays open — e.g. "a_j mult of R ⟹ Lemma 4 holds for (a_i,a_j)" narrows counterexamples to a_j mod R ≠ 0 (round 2, imo-2026-06 crux-descent explorer).
