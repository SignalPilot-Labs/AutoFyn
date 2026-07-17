## imo-2026-01

- Distinct openings (all within the per-prime lens, but genuinely different top-level targets):
  1. **Per-prime GCD invariant → explicit formula for M (recommended primary route).** For a fixed
     prime `p`, write `a=v_p(m)`, `b=v_p(n)` for the two chosen board numbers. Then
     `v_p(gcd(m,n)) = min(a,b)` and `v_p(lcm(m,n)/gcd(m,n)) = max(a,b)-min(a,b) = |a-b|`, confirming
     the assigned map `(a,b) -> (min(a,b), |a-b|)`. The elementary Euclidean identity
     `gcd(min(a,b), |a-b|) = gcd(a,b)` (WLOG `a≥b`: `gcd(b,a-b)=gcd(a,b)`) shows that **the pairwise
     gcd of the two exponents is preserved by the move**, and since a move only touches the two chosen
     positions, **the gcd of the *entire* exponent multiset `{v_p(n_1),…,v_p(n_2026)}` across all 2026
     board entries is a global invariant of the whole process, for every prime `p` separately** — no
     need to worry about cross-prime coupling for this part at all, since the invariance argument is
     local to one move and one prime, and every move only ever changes two exponents whose *pairwise*
     gcd (hence the multiset gcd, since the rest are untouched) is preserved. Once part (a) establishes
     the terminal state is `{1,1,…,1,M}`, the terminal exponent multiset for `p` is `{0,…,0,v_p(M)}`,
     whose gcd is `v_p(M)` itself (or 0 if `p∤M`). Hence
     **`v_p(M) = gcd_i v_p(n_i)` for every prime `p`**, i.e.
     `M = ∏_p p^{gcd(v_p(n_1),…,v_p(n_2026))}`. This simultaneously (i) pins down M exactly
     (answers "what is M", useful even though this is proof_only/answer_type none — gives the
     explicit invariant to cite) and (ii) gives part (b) — independence of choices — directly, since
     the formula never references any move sequence. **This is confirmed numerically** (see
     Small-case notes) across 20 random 6-number boards with fully random move orders — always
     matches `∏_p p^{gcd of initial exponents}`.
  2. **Termination via a lexicographic monovariant (needed for part (a), independent of route 1).**
     Let `Ω(n) = Σ` (exponents with multiplicity) be the number of prime factors of `n` counted with
     multiplicity. For the two chosen numbers, `Ω(m)+Ω(n) - Ω(gcd) - Ω(lcm/gcd) = (a+b) - min(a,b) -
     |a-b| = min(a,b)` (sum over all primes). So the total `S = Σ_i Ω(n_i)` over the whole board is
     **non-increasing**, strictly decreasing exactly when `gcd(m,n) > 1`. When `gcd(m,n)=1`, `S` is
     unchanged but the move sends `(m,n) ↦ (1, mn)` — since `m,n>1` were both `>1` before and exactly
     one of the two resulting numbers is `1` after — so the **count of board entries equal to 1
     strictly increases by exactly 1** whenever a coprime move is made. Hence the pair `(S, 2026 -
     #{ones})` decreases lexicographically (in `ℕ×ℕ`, well-founded) at every move: this is a clean
     termination monovariant, verified numerically (see below) and avoiding any need to track
     per-prime counts of nonzero exponents (`c_p`) which turned out messier (`c_p` decreases only
     when the two chosen exponents at `p` are *equal and positive*, and is otherwise either constant
     or can even not shrink on a raw per-prime view — the `S`/`ones` pair sidesteps this).
  3. **Non-vanishing of the prime support (why exactly one, not zero, number survives).** For a fixed
     prime `p` present somewhere on the board (`v_p(n_i)>0` for some `i`), check: if a move's pair
     `(a,b)` has `a=b>0`, new pair is `(a,0)` — `p` still present (carried by the position that got
     `min=a`). If `a≠b` with both positive, new pair `(min,|a-b|)` has both entries positive (since
     `|a-b|>0` when `a≠b`, and `min>0` when both were positive) — `p` still present, possibly on both
     positions. If exactly one is 0, new pair is `(0,max)` — `p` migrates but doesn't vanish. **So no
     move can ever eliminate a prime that is present somewhere on the board** — the union of prime
     supports across the whole board is itself invariant (never shrinks, and never grows since gcd/lcm
     factors only involve primes already dividing `m,n`). Combined with termination (route 2) — which
     forces the process to stop with at most one number `>1` — this proves **at least one number
     remains `>1`** whenever the initial board has any prime present (true since all 2026 numbers are
     `>1`), settling the "exactly one" (not "zero") half of part (a) cleanly.

- Candidate technique(s): **Invariants & monovariants** (knowledge_base.md, Combinatorics section,
  and General Proof Methods) is the exact right entry — this problem is a textbook instance:
  Euclidean-algorithm-flavored pairwise operation on exponent vectors, invariant = gcd of the whole
  multiset, monovariant = `Σ Ω(n_i)` lexicographically refined by count of ones. No number-theoretic
  machinery beyond elementary `v_p`, gcd/lcm identities, and the classical Euclidean subtraction
  identity `gcd(a,b)=gcd(min(a,b),|a-b|)` is needed.

- Cheap-kill candidates: the elementary identity `v_p(gcd)=min`, `v_p(lcm)=max` (standard, cite as
  known) immediately reduces the whole problem to the exponent-pair dynamic per prime — this *is*
  the cheap kill, no heavy machinery (LTE, Zsigmondy, etc.) is relevant here. Also cheap: `2026` (the
  specific count) is a red herring / just needs "≥1 number" and "finitely many primes/positions" —
  no parity or mod-2026 argument is needed; do not let an approach get bogged down trying to use the
  number 2026 combinatorially.

- Knowledge-base entries to use: **"Invariants & monovariants"** (Combinatorics section, line ~117);
  **General Proof Methods → "Invariant / monovariant"** (line ~191); **"Divisor analysis"** (Number
  Theory section, gcd structure) for the elementary `v_p(gcd)=min(v_p(m),v_p(n))`,
  `v_p(lcm)=max(v_p(m),v_p(n))` facts (not spelled out verbatim in the KB but a direct consequence of
  "Modular arithmetic, CRT" / standard `v_p` multiplicativity — worth citing as a basic lemma to
  prove inline, one line, from the definition of gcd/lcm via prime factorizations).

- Analogous past problems (cruxes): searched `number_theory` subtopics `invariants-and-monovariants`,
  `divisibility-and-gcd`, `p-adic-valuation`, and combinatorics `processes-and-algorithms` for
  gcd/lcm-merge-process problems. Found `aimo-0324` (squarefree-part monovariant for a game — same
  flavor of "track the multiplicative structure via an invariant of exponents" but for a very
  different game, not close enough to borrow a concrete step from) and `aimo-0662`/`aimo-0678`
  (gcd/lcm appear in `how_used` text but for different problem shapes — periodicity of a recurrence,
  extremal sandwich argument — not analogous processes). **No crux in the corpus directly matches
  this "repeatedly replace a pair by (gcd, lcm/gcd) until one survives" process.** The closest
  conceptual match is the general pattern in `aimo-0324` (multiplicative-invariant-as-monovariant),
  useful only as a sanity check of style, not as a borrowable step. Recommend treating this problem as
  self-contained via the direct `v_p` computation above rather than forcing a corpus match.

- Prior progress: none — workspace was empty at start of round 1 (no `approaches/`, no `lemmas/`,
  `current.md` empty).

- Dead ends (do not retry): none recorded yet (fresh workspace). One methodological pitfall to flag
  for the outliner: **do not attempt a purely single-prime induction that ignores coupling** — i.e.
  do not try to argue "process terminates for prime p in isolation, therefore terminates overall" by
  running separate arguments per prime and combining naïvely; the moves are coupled (one move
  touches all primes of `m,n` at once), so termination must be argued with a *single global*
  monovariant (route 2 above: `Σ_i Ω(n_i)` plus ones-count), not per-prime counters. This is the one
  place a naive per-prime argument breaks, and it's exactly where an outline should be careful.

- Small-case / intuition notes (numerical, hence conjecture-grade until written as a proof, but
  strongly supported):
  - Verified by hand: `{4,6}` → `{2,6}` → `{2,3}` → `{1,6}`, `M=6=2^{gcd(2,1)}·3^{gcd(0,1)}`, matches
    formula exactly.
  - Verified computationally (Python/sympy, 20 random trials of 6-number boards drawn from
    `{4,6,8,9,10,12,15,18,20,25,27,30}`, fully random move order each time): terminal `M` always
    equals `∏_p p^{gcd_i v_p(n_i)}` — **0 mismatches across 20 independent random-order runs**, i.e.
    order-independence (part b) and the explicit invariant formula both hold on every sample.
  - Verified computationally that `S=Σ Ω(n_i)` is non-increasing every move, strictly decreasing
    exactly when `gcd(m,n)>1`, and that count of ones strictly increases by 1 exactly when
    `gcd(m,n)=1` — confirms the lexicographic monovariant claim in route 2 (5 trials, all assertions
    held, process always terminated in `≤ 15` steps for 6-number boards — consistent with
    `S` decreasing to 0 or the process running out of `>1`-pairs).
  - This is a clean "medium" difficulty problem structurally (matches the `difficulty_rating: 5`
    /`difficulty_level: medium"` tag in `problems.jsonl`, despite being tackled here as the run's
    fixed target problem per `run_state.md`'s explicit override) — the two invariants above appear
    to close both parts with no further heavy machinery required; the outliner's job is mainly to
    write the two arguments (invariant formula for b, lexicographic monovariant + non-vanishing
    support for a) rigorously and combine them, not to search further for a different technique.
