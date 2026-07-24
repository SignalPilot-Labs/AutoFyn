## imo-2026-06 (lens: extremal / monovariant / minimal-counterexample on the essential-prime set)

### HEADLINE FINDING — a near-exact crux match that likely closes (HS/MCL) outright

**The sequence `(a_n)` in this problem is *literally* the "good numbers" sequence of
IMO-2016-style problem `aimo-0030`** ("Ana and Banana" game of numbers, ISL/IMO 2016,
Italy). Read the full statement/solution via
`past_problems_database.json` (`problem_id = aimo-0030`); the crux move is filed under
`domain=number_theory`, `subtopic ∈ {divisibility-and-gcd, size-bounding-and-descent}`.

- **The identification.** aimo-0030's Comment 2 gives an explicit recursive construction
  of the "good numbers" `b_0 < b_1 < ...` for fixed threshold `k`: *`b_0 = k`; `b_{n+1}`
  is the smallest `b > b_n` coprime to **none** of `b_0,...,b_n`* — i.e. `gcd(b,b_i)>1`
  for every `i ≤ n`. **This is verbatim our recurrence**, with `k ↔ a_1`. Comment 3
  even computes the example `k=15`: "the sequence of good numbers begins with
  `15,18,20,24,30,36,40,42,45`" — this EXACTLY matches the numeric data already in
  `results/imo-2026-06/approaches/admissible-set-periodicity.md` for `a_1=15`
  (`15,18,20,24,30,36,40,42,45,48,50,...`, period `T=8, L=30`). Verified by hand — not
  a coincidence, a structural identity.
- **The proved theorem that maps onto our gap.** The official aimo-0030 problem proves:
  *if `n,n'` share the same set of primes `≤ k`, both are good or both are bad*. Along
  the way (Solution 2, Claim 5, "size-bounding-and-descent" + minimal-counterexample) it
  proves the *stronger*, more directly useful fact:
  > **Claim 5. Any two good numbers have a common prime factor `≤ k`.**

  This is **exactly (HS/MCL)** for our problem, with the finite hitting set
  `S = {primes p : p ≤ a_1}` (manifestly finite since `a_1` is a fixed integer)! If this
  transfers, (HS) is closed immediately, and by the certified reduction in
  `lemmas/finite-hitting-set-periodicity.md` / `admissible-set-periodicity.md`
  Lemmas 4–6, the ENTIRE problem is solved (this `S` need not be minimal — any finite
  hitting set suffices per the certified machinery).

### The transferable mechanism (extremal / minimal-counterexample — matches this round's lens)

Two-step argument from aimo-0030 Solution 2 (translate "good number" → "term of `(a_n)`",
"`m` coprime to none of `b_0..b_n`" → "`m ∈ A`" in the `admissible-set-periodicity`
notation; "small prime" → "prime `≤ a_1`"; "big prime" → "prime `> a_1`"):

**Step 1 (extremal witness / compression, their Claim 4).** For every term `b` (which by
Lemma 1 of our reduction shares a prime with `a_1`, hence has *some* prime `≤ a_1`
dividing it), construct a companion integer `x` with:
  - `x` divisible by exactly the same *small* primes (`≤ a_1`) that divide `b`, and by
    NO prime `> a_1`;
  - `a_1 ≤ x ≤ b`.
  Construction: let `p` be a small prime factor of `b`, `q` a big prime factor of `b` (if
  none, take `x=b`), `α` = product of all small primes dividing `b`; let `x = p^n α` for
  the least `n≥0` with `x ≥ a_1`. The inequality `x ≤ b` is proved by a clean size chain:
  minimality of `n` gives `x < p·a_1`; `p ≤ α` (as `p | α`); `a_1 < q`; hence
  `x < α q ≤ b` (since `αq` is a product of *distinct* primes dividing `b`). **This is the
  extremal device**: among all integers with `b`'s exact small-prime footprint, take the
  *least* one `≥ a_1` — a genuinely extremal (minimality) construction, not a counting
  argument.
- **Step 2 (minimal-counterexample descent, their Claim 5).** Suppose some pair of terms
  shares NO prime `≤ a_1`. Take such a pair `(b,b')`, WLOG `b ≤ b'`, with `b'` **minimal**
  among all violating pairs (this is the extremal/well-ordering step the lens asked for).
  Since `b` and `a_1` are both terms, they share a prime `p` (Lemma 1 of our reduction);
  `p ≤ a_1` automatically (it divides `a_1`). Apply Step 1 to `b` to get `x` (same small
  primes as `b`, no big primes, `a_1≤x≤b`). By the violating-pair hypothesis, `b'` shares
  no small prime with `b`, hence none with `x` (x's primes ⊆ b's small primes) — so
  `gcd(x,b')=1`. Since `b' ` is a term, and `x` is in the range `[a_1,b')` and coprime to
  it, `x` **cannot itself be a term** (else `x,b'` would be two terms with `gcd=1`,
  contradicting Lemma 1 pairwise non-coprimality) — so `x ∉ A`. Being `∉A`, some earlier
  term `a_i` has `gcd(x,a_i)=1`... *(here the aimo-0030 argument actually uses the
  game's forward "good/bad" recursion, i.e. that `x` failing to be good forces a specific
  earlier good number `b*` reachable from `x`; the direct analogue in our static-set
  language needs a short bridge lemma — see Gap 1 below)* — the upshot in aimo-0030 is a
  **strictly smaller violating pair** `(b*, b)` with `b* < b ≤ b'` and `b*` also a term,
  contradicting minimality of `b'`. This closes Step 2.

### What must still be built (gaps for the outliner, not attempted here)

- **Gap 1 — bridge the two "static admissible-set" formulations.** aimo-0030's proof
  leans on the *game* recursive good/bad dichotomy (`n` bad iff `∃` good `m<n` coprime to
  it); our reduction instead has the purely static set `A = {x>1 : gcd(x,a_i)>1 ∀i}` and
  Lemma 2 (`a_{n+1} = min(A ∩ (a_n,∞))`, already certified). These *should* be
  equivalent (Comment 2 of aimo-0030 asserts as much for the "good numbers" sequence
  specifically, restricted to `x ≥ b_0`), but the outliner/builder must **prove this
  bridge from scratch** — likely short, via strong induction matching our Lemma 2 exactly
  — rather than importing the game framework wholesale. Concretely: show that for
  `x ≥ a_1`, `x ∈ A ⟺ x` is a "good number" in the aimo-0030 sense with `k=a_1` — or,
  better, **skip the game language entirely** and redo Claim 4 + Claim 5's argument
  purely in terms of `A` and minimality of the greedy step (`a_{n+1} = min(A∩(a_n,∞))`),
  which is likely cleaner since we already have Lemma 1/2 certified. The one place the
  game's "bad → has a move to a good number" idea is used (finding `b*`) should translate
  to: "`x ∉ A` means some `a_i` is coprime to `x`; but also (key point, needs proof) `x`
  fails admissibility specifically **at the greedy step where it was rejected in favor of
  some actual term `b*`** — i.e. `x` lies strictly between two consecutive terms, and the
  term `a_i` that kills `x`'s admissibility, combined with minimality of the greedy
  choice, produces the smaller pair." This is the one place real new work is needed; it
  is a **combinatorial/extremal argument about consecutive terms**, not a counting
  argument, so it fits this round's lens and should NOT re-hit the density wall.
- **Gap 2 — double check `x`'s role needs "term", not just "`∈A`".** In our framework
  `A` already IS the full admissible set (matches "good numbers" exactly, since
  `A ∩ [a_1,∞) = \{a_n\}$` by Lemma 2). So `x ∈ A ⟺ x` is a term (once `x ≥ a_1`), which
  *simplifies* the aimo-0030 argument: we don't need a separate "bad ⟹ move to good"
  step — we directly get "if `x ∈ [a_1,b')` and `gcd(x,b')=1`, then since `b'` is a term
  (`∈A`) and `A` requires `gcd>1` with *every* other element of `A` (this is exactly
  Lemma 1: pairwise non-coprimality of terms, ALREADY CERTIFIED), `x ∉ A` is forced only
  if `x` genuinely fails against SOME `a_i`" — this is consistent, but the descent step
  (producing a *smaller* violating pair) still needs the "which term kills `x`, and how
  does that give a smaller pair" argument spelled out newly in our notation. This looks
  achievable directly from Lemma 1 + Lemma 2 (both certified) without extra machinery —
  flag as the concrete task for next round's outliner/builder.
- **Gap 3 — sanity-check the bound.** `S = {primes ≤ a_1}` is finite but can be much
  larger than the empirically-minimal hitting sets (e.g. `a_1=1001` uses `{2,7,11,13}`
  empirically, vs. `{2,3,5,7,11,13,...,997}` from this bound) — **this does not matter**:
  the certified reduction (Lemma D / Lemmas 4–6) works for *any* finite hitting set, not
  a minimal one, so overshoot is harmless. Confirm this explicitly when writing it up so
  no one mistakenly thinks a *tight* `S` is required.

### Secondary extremal ideas (independent backup, in case Gap 1 stalls)

- **Size bound via `gcd | difference` (own analysis, not from aimo-0030).** If prime `p`
  is a *sole connector* of pair `(a_i,a_j)`, `i<j`, then `p | a_i` and `p | a_j`, so
  `p | (a_j - a_i)`, giving `p ≤ a_j - a_i ≤ (j-i)·R` (using the certified bounded-gap
  Lemma A/3, `R = rad(a_1)`). This is a genuine, cheap extremal fact: **large
  sole-connector primes can only arise from pairs with large *temporal* separation**
  `j - i`. It does not by itself bound `p` (temporal separation is a priori unbounded),
  but it reduces (HS) to bounding how far apart in index a "genuinely new" essential
  prime's connecting pair can be — a genuinely different angle from pure density if
  Gap 1 above turns out to need reinforcement.
- **Personal-prime-set observation.** Any prime connecting `a_i` to anything necessarily
  lies in `supp(a_i)`, a set of size `ω(a_i) = O(log a_i)`. This is definitional (not
  new information) but worth stating explicitly to the outliner as a sanity check: it
  shows `𝒞` (sole-connector primes) is a union, over all indices `i`, of small finite
  slices — the difficulty is only that infinitely many indices could each contribute one
  *new* prime, which is exactly what the aimo-0030-style argument (Step 1–2 above) is
  built to forbid via "any two terms share a *small* (≤ a_1) prime," making the "new"
  large primes companions/never sole.
- **If Gap 1 fails:** a fallback minimal-counterexample framing native to our own
  reduction: assume `Π` (min-common-prime set) is infinite; well-order the primes of `Π`
  that exceed `a_1`; take the *least* index `j*` at which such a prime `p*` first
  becomes the min-common-prime for some pair `(i*, j*)`, `i* < j*`; derive a contradiction
  with minimality of the greedy choice at step `j*` by exhibiting an admissible candidate
  `< a_{j*}` that uses only primes `≤ a_1` (via CRT / the same Step-1 "compression"
  witness `x`) — essentially re-deriving the aimo-0030 argument bottom-up rather than
  importing it. Keep this as Plan B; Plan A (direct transfer) is much shorter if Gap 1
  closes cleanly.

### Candidate technique(s)
- **Minimal-counterexample / extremal-pair descent** (aimo-0030 Claim 5's method) — the
  primary candidate, essentially handed to us by the corpus.
- **Extremal witness construction** (aimo-0030 Claim 4's "smallest same-footprint
  representative `≥ a_1`") — a genuinely extremal (not counting) device.
- CRT / modular residue machinery already certified in `lemmas/`.

### Cheap-kill candidates
- `p | (a_j-a_i)` for a common prime `p` of `a_i,a_j` — cheap, gives the temporal-distance
  bound noted above; not decisive alone but a useful sanity filter for any construction.
- Every term shares a prime `≤ a_1` with `a_1` itself (trivial, since divisors of `a_1`
  are `≤ a_1`) — already implicitly used in Lemma 3/A of the certified reduction; worth
  restating explicitly since it is the seed fact Step 2 above needs (`b,a_1` share a
  small prime).

### Knowledge-base entries to use
- "Pigeonhole / extremal principle: for existence, take the maximal or minimal element"
  (knowledge_base.md, Combinatorics) — exactly the Step-2 descent method.
- "Divisor analysis: gcd structure, bounding a finite search by size" — for the Step-1
  size-chain inequality (`x < p·a_1 < αq ≤ b`).
- "Modular arithmetic, CRT" — already used by the certified periodicity machine; not
  needed again for (HS) itself under this route (the aimo-0030 argument is purely
  divisibility/size, no CRT construction needed to prove HS).
- "Vieta jumping & infinite descent" entry — same descent *flavor* as Step 2, cite if the
  outliner prefers descent-language over minimal-counterexample language.

### Analogous past problems (cruxes) — ranked
1. **`aimo-0030`** (NT, `subtopic` divisibility-and-gcd / size-bounding-and-descent) —
   **not just analogous, essentially the same combinatorial object** (see Headline
   Finding). Crux moves: "extract a same-small-prime-footprint witness `x` with
   `k≤x≤b`" (Claim 4) and "minimal-counterexample descent forcing two good numbers to
   share a small prime" (Claim 5). This is the strongest possible match found across two
   rounds of exploration on this problem — read `past_problems_database.json` entry for
   `aimo-0030` in full (both official solutions) before outlining.
2. `aimo-0447` (grid/interval-occupancy counting) — already used by the sibling
   `essential-prime-counting` approach; documented as *insufficient alone* (density wall)
   — keep as a supporting cheap-kill fact (Step-1's inequality chain is unrelated to this,
   so no conflict), not a replacement for the aimo-0030 route.
3. `aimo-0415` (pigeonhole: too many factors for too few small primes forces a shared
   large-prime-power, then `gcd | difference` contradiction) — same *flavor* of
   size-vs-prime-count argument as the temporal-distance backup idea above; weaker match
   than `aimo-0030`, offered as a secondary technique fragment only.

### Prior progress
Both live approaches (`admissible-set-periodicity`, `essential-prime-counting`) have
fully certified, gap-free reductions of the ENTIRE problem to (HS/MCL): a finite prime
set `S` with `supp(a_i)∩supp(a_j)∩S ≠ ∅` for all `i≠j`. `lemmas/enumeration-and-bounded-gaps.md`
and `lemmas/finite-hitting-set-periodicity.md` are certified and directly reusable — in
particular Lemma 1 (pairwise non-coprimality: **already proves the aimo-0030 fact "any two
terms share *some* common prime," just not yet a *small* one**) and Lemma 3/A (every term
shares a prime with `a_1`, hence a prime `≤ a_1`) are exactly the two facts the aimo-0030
Step 2 argument needs as inputs — they are already sitting in the workspace, certified,
ready to be composed with the new Step 1/Step 2 argument.

### Dead ends (do not retry)
- **Pure counting / density (`Σ1/p²`, interval-occupancy alone)** — proven insufficient
  by both round-1 approaches: bounds the *fraction* of bad pairs but not the *number* of
  distinct essential primes; sparse density-zero disjoint prime-families evade it. The
  aimo-0030 route above is a genuinely different mechanism (size/extremal, not density)
  and does not inherit this failure.
- **finite-state-reversible's Step 5 (GAP C, reversibility)** — separately flagged as
  unsolved/outline-only; unrelated to (HS) itself (it's about exactness-from-n=1 given
  HS, which the OTHER two approaches already get for free via the static-set argument).
  Not superseded by this round's finding, just orthogonal — no need to revisit unless the
  outliner wants a 3rd independent route to exactness (not needed, since Lemma 5/6 of
  `admissible-set-periodicity`/`essential-prime-counting` already give exactness for free
  once HS is known).

### Small-case / intuition notes (labeled conjectural where not yet proved)
- **Confirmed (not just conjectural) by direct match to a published solution's worked
  example:** for `a_1=15`, the sequence and its period (`T=8,L=30`) match aimo-0030's
  Comment 3 example for `k=15` exactly. This is strong independent corroboration (from an
  external published source, not just our own simulation) that the problem's sequence and
  the "good numbers" sequence are the same object, and that periodicity indeed holds with
  the period predicted (Comment 3 also states "the period of `W_15` is 30" — matching our
  `L=30`).
- The fact that `S={primes ≤ a_1}` is only a (large) *sufficient* hitting set, while the
  true minimal hitting sets are much smaller and vary (as already documented by the
  sibling approaches: `{2,7,11,13}` for `a_1=1001`, `{2}` for `a_1=858`), is expected and
  harmless — conjecture (very likely true, matches aimo-0030's Claim 5 exactly) that the
  large bound is real and provable even though not tight.
