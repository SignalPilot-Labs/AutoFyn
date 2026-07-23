## imo-2026-06

### Headline finding (verified numerically, not just conjectured): the current "backbone finiteness" target as formalized by `backbone-existence-crt` is almost certainly FALSE as stated — the field needs to re-target, not just push harder on the same gap.

`backbone-existence-crt` defines `H_n := P_1 ∪ {q : q is a "recruit" at some pair (i,j), i<j≤n}`,
where q is a recruit at (i,j) iff `q ∈ P_i∩P_j` and `ℓ(i)∩ℓ(j)=∅` (i.e. P_1 alone doesn't
witness that pair's gcd>1). "Backbone finiteness" is defined there as `⋃_n H_n` finite. I
tested this literal definition against `a_1=15`, whose eventual periodicity (T=8, L=30, tail
governed by primes {2,3,5}) is *already independently confirmed* (both in `current.md`'s notes
and by my own simulation below). Result: **`H_n` is unbounded even in this already-solved
case.** Concretely, `a_52 = 204 = 2^2·3·17` and `a_324 = 1224 = 2^3·3^2·17` (both deep in the
confirmed periodic tail, both admissible purely via primes 2,3,5 in their own right) share the
*incidental* prime 17 — a pure coincidence of arithmetic with no causal role in either term's
admissibility. I found **2948 such incidental cross-pair primes outside {2,3,5}** just among
index pairs `50 ≤ i<j ≤ 400` (script below). Since `gcd` between two "random" O(n)-sized
integers shares any fixed small prime `q` with probability `~1/q^2` and there are `Θ(n^2)`
pairs, this incidental-sharing phenomenon is not a fluke of small `n` — it will keep recruiting
"new" primes into `H_n` forever, at a positive rate, even after the sequence has settled into
its true finite periodic pattern. **So `⋃H_n` is (almost certainly, and demonstrably at least
up to n=400) infinite even when the theorem's conclusion already holds.** This means
`backbone-existence-crt`'s Step-3 target, exactly as defined in its Section 3, is not merely
hard — it is very likely an unprovable (false) restatement of what actually needs to be shown.
Continued effort strictly within that literal definition is not a viable path forward; per
CLAUDE.md's plateau-break guidance ("a stuck shared gap for 3+ rounds is a sign the direction
is wrong"), this is concrete evidence the *direction*, not just the technique, needs correcting
— on round 2, one round earlier than the guidance's 3-round trigger, because the flaw is now
demonstrable rather than merely slow.

**The fix is a reformulation, not a new technique**: the quantity that actually matters for the
problem's conclusion is not "the set of primes that ever co-occur in some pair `(i,j)`" but
**the set of primes that divide *cofinitely many* terms** (equivalently: primes governing the
sequence's *eventual, permanent* behavior). Call this `B := {p : p divides a_n for all
sufficiently large n}` — the "persistent backbone." `Lemma R` (eternal-witness-per-index,
already proved and certified in `lemmas/lemma-R-eternal-witness.md`) shows, for each fixed
index `i`, *some* prime of `P_i` divides *infinitely many* later terms — this is close to but
not identical to `B` (it's "infinitely often," not "cofinitely," and it is not shown that the
*same* prime works for every `i`, nor that the union over `i` of these "infinitely-often"
primes is itself finite). The correct open target for the field is:
**(⋆) the set of primes dividing infinitely many `a_n` is finite, and eventually every
sufficiently large `a_n` is divisible by at least one member of this finite set with a
persistent, periodic pattern of *which* member and *when*.**
This is a materially different (and, unlike the literal `H_n` version, plausibly true and
provable) target from what `backbone-existence-crt`'s Section 3 currently pursues. I recommend
the outliner open a rival approach — or amend `backbone-existence-crt` — explicitly built on
(⋆) rather than on "finiteness of ever-co-occurring recruit primes." This also affects
`intersecting-family-covering-construction`, whose Case-II framing ("no finite covering prime
set... found") should likewise be re-targeted at *persistent* covering (primes needed
cofinitely often), not literal exhaustive covering by any primes that ever appear.

### Distinct openings

1. **(Primary recommendation) Re-target "backbone finiteness" as persistent-divisor finiteness
   (⋆) above**, proved via Lemma R plus a growth-rate argument, rather than "recruit-at-a-pair"
   finiteness (shown false/unbounded above). This keeps the general shape of the existing three
   approaches' machinery (Lemma P/P′, Domination Lemma, Lemma 1) but changes *what is being
   counted*, which may be exactly what unsticks the plateau — the existing approaches were
   possibly trying to prove a false statement.

2. **Monovariant framing borrowed from crux `aimo-0678` (= IMO Shortlist 2015 N4, "Suppose
   `a_{n+1}=gcd(a_n,b_n)+1, b_{n+1}=lcm(a_n,b_n)-1`... prove `(a_n)` eventually periodic").**
   This is the closest topical analog in the whole corpus: same phenomenon (gcd/lcm-driven
   integer sequence, prove eventual periodicity), same headline conclusion type. Its Solution 1
   crux move: define `W_n = {m ≥ a_n : m ∤ s_n}` for a quantity `s_n` that is *frozen* during
   "quiet" steps, `w_n = min W_n`, and prove `(w_n)` is non-increasing — giving boundedness of
   `a_n` directly from a monovariant, with no density/counting argument at all. Its Solution 2
   crux move ("Once one coordinate of a coupled recurrence is bounded, reduce the other
   coordinate mod the lcm of the bounded coordinate's attainable values, turning the state pair
   into a deterministic map on a finite set" — exact quote from the corpus) is *literally* the
   strategy `bounded-gap-density-covering`'s Step 3 already tried and diagnosed as a dead end.
   **On inspection this crux does not give a free bypass**: aimo-0678's recurrence is
   memoryless / order-1 (`(a_{n+1},b_{n+1})` is a function of `(a_n,b_n)` alone), which is
   exactly what makes "bound one coordinate, reduce the other mod a finite lcm" work. Our
   problem's recurrence is *not* memoryless — admissibility of `a_{n+1}` is a conjunction over
   *all* `i≤n`, not a bounded window — which is precisely the obstruction
   `bounded-gap-density-covering` already located and that (⋆) above is meant to resolve. So
   Solution 2 of aimo-0678 is not new information; it confirms (independently, from a different
   corpus problem) that the existing diagnosis was correct. **Solution 1's monovariant idea
   (`w_n = min` of a *forbidden* set, shown non-increasing) is more promising as a genuinely new
   mechanism**, because it does not presuppose memorylessness — it works directly by tracking
   how a "first bad value" evolves. Adapting it here would mean: define, for each `n`, some
   "current worst offender" quantity on the *prime* side (e.g. the least prime `> `some
   threshold that is *not yet* a member of the currently-relevant covering set) and show it is
   monotonic. I was not able to construct this analogue within budget — flagging it as an
   opening worth a dedicated approach, not a worked-out route.

3. **Amortized / global double-counting, as opposed to per-step density.** The Domination Lemma
   (certified, `lemmas/domination-lemma.md`) gives a *per-step* existential statement (`some`
   prime of `a_{n+1}` is locally dominant). All three existing approaches try to convert
   "dominant at each step" into "dominant primes form a finite set" via *local* / *density*
   reasoning (which approach `bounded-gap-density-covering` showed cannot work without already
   knowing the backbone). A genuinely different route: sum the Domination Lemma's inequality
   `\sum_{j=1}^{\omega(a_{n+1})} D_n(q_j) \ge n` over a *range* of `n` (telescoping /
   double-counting, cf. crux subtopic `double-counting` in the KB tools list), comparing the
   total "prime-incidence budget" used by primes ever appearing against the total available
   "slots" `\sum_{n\le N} n = \Theta(N^2)`, and bounding the number of *distinct* primes that
   can each individually absorb a linear (`\Theta(N)`) share of that budget. This targets
   finiteness of the *persistent* set (⋆) directly via a global sum rather than per-step
   concentration, sidestepping the objection (raised by `backbone-existence-crt` itself) that
   "one dominant prime per step" doesn't obviously bound the number of distinct dominant primes
   across all steps. Unverified — flagged as an opening, not a completed argument (do not treat
   as more than a plausible next attempt).

4. **Graph/coloring framing (checked, weaker than the above):** treat primes as colors on the
   infinite "conflict-free" hypergraph where each `a_n` is a hyperedge `P_n`; König's-lemma /
   compactness style arguments apply naturally to *infinite* trees of finite branching, but
   here the "branching" (which prime witnesses which pairwise intersection) is not obviously
   finitely-branching without already assuming backbone finiteness, so a raw
   compactness/König argument does not obviously get off the ground independent of (⋆). I did
   not find a corpus precedent that avoids this circularity, so I am not elevating this to a
   primary recommendation.

### Candidate technique(s)
- Reformulate the finiteness target per (⋆) above (finiteness of the *persistent-divisor* set,
  not the *ever-co-occurring* set) — this is a correction to existing framing, not a new
  technique, but it is the most actionable finding.
- The `aimo-0678` monovariant ("min of a currently-forbidden set is non-increasing") as a
  template for a genuinely new prime-side monovariant (opening 2).
- Global/amortized double-counting on the Domination Lemma across a range of `n` (opening 3),
  KB pigeonhole / extremal-principle style.

### Cheap-kill candidates
- **Immediate structural check for any future formalization of "backbone":** before adopting
  any definition of a backbone/covering set `H`, test it against the already-solved `a_1=15`
  case (T=8, L=30, tail primes {2,3,5}) the way I did above — if the candidate definition of
  `H_n` is not eventually stable/bounded even for `a_1=15`, the definition is wrong and should
  be discarded before spending further builder effort on it. This is a cheap, fast (seconds of
  Python) sanity gate that would have caught the flaw in `backbone-existence-crt`'s Section 3
  immediately.
- Any argument that conflates "primes dividing `a_n`" with "primes causally load-bearing for
  `a_n`'s admissibility" is suspect — `a_n`'s value can carry large incidental prime factors
  irrelevant to why it was chosen; only primes that are *forced* (i.e., without which some
  earlier gcd constraint would fail) matter for periodicity.

### Knowledge-base entries to use
I read `knowledge_base.md` (247 lines) in full. Directly relevant entries already invoked by
the population: pigeonhole/extremal principle (Lemma R, Lemma S′ arguments), CRT / modular
finite-state arguments (the `bounded-gap-density-covering` Step-3 attempt, and the `aimo-0678`
analog above). No entry in the KB gives a ready-made "amortized double-counting to bound
distinct dominant actors" template beyond the generic pigeonhole/extremal-principle entries
already cited by the population — opening 3 above would need to be built from scratch using
those generic tools, not a specific named KB theorem.

### Analogous past problems (cruxes)
- **`aimo-0678` (IMO Shortlist 2015 N4)** — closest topical analog in the whole corpus: a
  gcd/lcm-driven integer recurrence, prove eventual periodicity. Crux moves: (a) a monovariant
  `w_n = min{m ≥ a_n : m ∤ s_n}` shown non-increasing, giving boundedness without density
  arguments; (b) "bound one coordinate, reduce the other mod the lcm of its finitely many
  values" to get a finite deterministic state, hence eventual periodicity by pigeonhole. Move
  (b) is the same strategy `bounded-gap-density-covering` already tried and correctly
  diagnosed as blocked (our recurrence is not memoryless/order-1, unlike aimo-0678's); move
  (a)'s monovariant mechanism is structurally different from anything the current three
  approaches try and is the best candidate for a genuinely new opening (opening 2 above),
  though I did not complete an adaptation.
- **`aimo-0680`** (functions `f:Z+→Z+` with `(f^n(m)-m)/n∈Z+` and cofinite image; prove
  `f(n)-n` periodic) — a different genre (orbit/Table decomposition of `Z+` via cofinite image
  and injectivity) that proves periodicity via organizing `Z+` into finitely many
  arithmetic-progression "rows," then a "relation known on an infinite index subset extends to
  all indices" upgrade trick. Interesting as a distant structural cousin (both problems end in
  "eventually periodic / AP shift"), but I could not find a natural way to construct an
  analogous injective self-map or cofinite-image structure from our sequence `(a_n)` — flagging
  it as a considered-but-not-adopted analog, not a recommended route.
- **`aimo-0421`** — already the basis of the certified Lemma R (cited correctly by
  `intersecting-family-covering-construction`); no further mileage found beyond what's already
  extracted.
- I did not find any corpus problem that is genuinely analogous to the *concentration onto
  finitely many dominant primes* sub-question — the corpus's closest precedent (aimo-0678) has
  a structural feature (memoryless order-1 recurrence) that our problem lacks, which is exactly
  why the direct transfer fails and why I am recommending a reformulation instead of a
  technique-swap.

### Prior progress
Certified and reusable: Lemma P/P′ (permanent hub, pairwise intersection), Lemma Q
(prime-power base case, T=1 exactly), Lemma S′ (single-prime saturation ⟹ exact AP, closes
"Case I"), Lemma 1 (uniform gap bound `d_n ≤ rad(a_1)`, unconditional), Domination Lemma
(per-step existential dominance), Lemma R (per-index eternal witness, "infinitely often" not
"cofinitely"). All verified present and (on inspection of their proofs, which I read in full)
methodologically sound. See `results/imo-2026-06/current.md` for the full consolidated
statement — I did not find errors in any of these certified lemmas.

### Dead ends (do not retry)
- `bounded-gap-density-covering`'s Step 3 ("bound gaps, then reduce to a finite state
  backbone-agnostically"): confirmed dead by that approach's own builder, and independently
  reconfirmed here — this is exactly aimo-0678's Solution-2 strategy, which requires the
  memoryless structure our problem does not have.
- **New this round**: `backbone-existence-crt`'s literal Section-3 definition of `H_n` /
  "backbone finiteness" via "recruit at a pair (i,j)" — numerically shown to be unbounded even
  in the already-solved `a_1=15` case (2948 incidental cross-pair primes among indices
  50–400 alone). Do not spend further builder effort trying to prove `⋃H_n` finite *as
  literally defined in that file*; either amend the definition to the persistent-divisor
  version (⋆) or treat it as refuted.

### Small-case / intuition notes (labeled as conjecture except where marked verified)
- **Verified** (simulation, `math.gcd`, exact integer arithmetic, no floating point):
  `a_1=15`'s gap sequence `d_n = a_{n+1}-a_n` becomes exactly periodic with period 8 and sum
  30 from a small index on: repeating block `[3,2,4,6,6,4,2,3]` observed identically across
  indices ~1480–1500 (three full periods checked), matching `current.md`'s claimed `T=8,L=30`.
  This is strong (though still finite-sample) confirmation the theorem's conclusion is
  achievable in Case II, consistent with existing round-1 notes.
- **Verified**: 159 distinct primes appear as factors of *some* `a_n` for `1≤n≤1500` when
  `a_1=15`, growing roughly like `π(a_{1500})≈π(5634)`, i.e. essentially all primes up to the
  sequence's current value appear *somewhere* as an incidental factor — this is expected
  behavior for "random-looking" O(n)-sized composite integers and is **not** evidence against
  backbone finiteness in the correct (persistent-divisor) sense; it is exactly the
  false-signal phenomenon flagged in the Headline Finding above.
- **Conjecture** (not verified beyond the a_1=15 case, and not attempted for a_1=247 within
  budget due to time cost of exact-gcd simulation at that scale): the persistent-divisor set
  `B` (⋆) is finite for every `a_1`, and is generated exactly by the primes that show up as
  *repeated* eternal witnesses (Lemma R primes) rather than by any prime that ever
  incidentally co-occurs in a pair.

### Reproduction (for the outliner/builders, script used above)
```python
import math
from sympy import factorint
def simulate(a1, n_terms):
    a = [a1]; x = a1 + 1
    while len(a) < n_terms:
        if all(math.gcd(x, ai) > 1 for ai in a):
            a.append(x)
        x += 1
    return a
seq = simulate(15, 400)
backbone = {2, 3, 5}
found = []
for i in range(50, 400):
    for j in range(i + 1, 400):
        g = math.gcd(seq[i], seq[j])
        if g > 1:
            extra = set(factorint(g)) - backbone
            if extra:
                found.append((i + 1, j + 1, seq[i], seq[j], extra))
print(len(found))  # -> 2948
```
