## imo-2026-06

**Assigned lens:** p-adic valuation / prime-power monovariant tracking as a route to the
Successor Claim (the crux `covering-system-construction`/`greedy-exchange-cost-potential`
Steps 9 reduce FAH/Cofinite FAH to, per `lemmas/successor-transport-reduction-lemma.md`).

### Setup recap (so the outliner doesn't need to re-derive it)
Fix a rogue pair (A′,B′) (disjoint S₀-extended-persistent types) with earliest witnesses
n_A,n_B (Lemma G), q* ∈ F′∩F″ any prime of the certified-nonempty intersection
(F′:=P(a_{n_A})\S₀, F″:=P(a_{n_B})\S₀). Let n_1<n_2<... enumerate all A′-occurrences past
max(n_A,n_B). **Successor Claim** (open): ∃J s.t. j≥J ⟹ (q*|a_{n_j} ⟹ q*|a_{n_{j+1}}).
By the certified Confined-GCD Lemma, g_n:=gcd(a_n,a_{n_B}) is confined to the FIXED FINITE
set Div(b), b:=F″-part of a_{n_B}, and q*|a_n ⟺ q*|g_n — so this is already a "numeric,
not just binary" quantity ranging over a fixed finite lattice, not an unbounded integer.

### What I tried: track v_{q*}(a_n) (and the full divisor-class g_n) as a genuine numeric
monovariant along the A′-occurrence stream, on the one concretely-documented
|F′|,|F″|≥2 instance (`a_1=11305`, A′={3,7} at index 3 (0-idx), B′={2,5} at index 6,
F′={11}, F″={11,103}, q*=11 — matches current.md's on-record instance exactly, reconfirmed).
Generated 8500 terms (fast pure-Python sieve-free greedy, `math.gcd`), extracted all 85
A′-occurrences and 261 B′-occurrences past max(n_A,n_B), computed v_11(a_n) and g_n=gcd(a_n,
a_{n_B}) for each.

**Result 1 (reconfirms prior rounds, no new claim):** 0/85 and 0/261 failures — literal
(zero-exception) FAH holds throughout this window for q*=11, matching round 9's report
exactly (this seed has no actual failure to study a "successor" event on).

**Result 2 (new, negative): v_{q*}(a_n) is NOT monotone along the occurrence stream, and
g_n is NOT absorbing/one-way.** Concretely: v_11 along consecutive A′-occurrences goes
...,1,1,2,1,1,1,1,3,1,1,... (e.g. index 805→v=2, next occurrence index 863→v=1, a genuine
decrease; index 2067→v=3, next index 2126→v=1). Likewise g_n (the confined-gcd divisor
class) is 11 at almost every occurrence but jumps to 1133=11·103 at index 1551 (a_n also
picks up the OTHER side's recruited prime 103) and then reverts to 11 at the very next
occurrence (index 1665) — i.e. hitting a "richer" divisor class is not absorbing/permanent.
**This directly falsifies, on real data, the most natural valuation-monovariant induction
one would try** ("v_{q*}(a_n) is eventually non-decreasing along same-type occurrences," or
"once g_n enters a q*-divisible-and-more class it stays there") — both are false as stated.
So tracking the *exact* p-adic valuation, rather than just the binary "does q* divide,"
gives **strictly noisier, less structured data**, not a cleaner monovariant. This is a
genuine new negative finding (not identical to any of the 15 listed dead mechanisms, but
directly relevant: it rules out an entire *family* — "exact-valuation monovariant descent/
ascent induction" — before any round wastes a build on it).

### Second experiment: hunting for actual failures to see runs-vs-isolated behavior
Round 9's cheap-kill check (≈270 seeds) found **zero** actual FAH failures at properly
recruited |F′|,|F″|≥2 cores, so it could not test whether failures (if they existed) come
in runs or are isolated. I found a setting where failures DO occur — an **under-recruited**
core (S₀ = Q only, not yet the fully recruited core), on `a_1=4807` (Q={11,19,23}), testing
q*=2 (a hub-type prime, `Hub-Singleton-Batch-Lemma` territory, not a genuine deep F′/F″
instance — flagged explicitly, see caveat below). Result: for pair (19,)-vs-(11,), out of
1603 occurrences the pattern of "does 2 divide a_n" is `0,1,1,1,1,...` — exactly ONE failure,
at the very first occurrence, then unbroken success for the remaining 1602. For pair
(11,19)-vs-(23,), out of 160 occurrences the pattern has exactly ONE isolated `0` in the
*middle* (~position 108), surrounded on both sides by unbroken `1`s. **In every failure case
found, failures are isolated singletons, never runs of 2+, and are never seen to recur after
the point where success resumes** (in the sampled window). This is weak, seed-limited,
hub-prime-only evidence — but it is evidence *for* the qualitative shape the Successor Claim
needs (isolated blips, not runs), and it directly matches round 9's dispatch note that
"scattered failures... would leave transport plausible" (round 9 could not test this because
it found zero failures at all; I found some, in the easier hub-prime/under-recruited regime,
and they are scattered/isolated, not runs). **Caveat, important:** q*=2 here is a hub prime
(dividing almost every term for structural reasons per the certified Hub-Singleton-Batch-
Lemma), and S₀=Q (before the Finite-Core-Theorem recruitment that the real problem's F′/F″
language presumes) — so this is NOT a clean test of the genuine Successor Claim at a properly
recruited core; it is suggestive, not a substitute for a real |F′|,|F″|≥2-at-recruited-core
failure instance (none has ever been found by any round).

### Is there an untried greedy-minimality-as-q-adic-order encoding?
Checked explicitly against Lemma H (Critical Prime Dichotomy): the natural way to encode
"c is illegal" q-adically (write a_n=q*^e·c, e:=v_{q*}(a_n), ask what forces e≥1) is
*exactly* Lemma H's dichotomy (strip q*, ask if c≤a_{n-1} or c is rescued by a unique earlier
term). Round 9 Step 3 already checked this concretely on the consecutive-occurrence object
(not just a single witness) and found branch (a) fires generically and is magnitude-only
(no q*-specific content), branch (b) gives a fact about an unrelated index. Re-deriving this
in fully valuation-flavored language (asking about v_{q*}(a_n) directly rather than binary
divisibility) does not change this: the dichotomy is about whether *stripping the top q*-power*
drops below a_{n-1}, which is a magnitude question independent of what value e takes — **this
IS the same dead mechanism, not a new one**, confirmed by direct inspection, not just citation.

### Verdict on this lens
No new mechanism was found that closes the Successor Claim. The valuation-tracking idea,
worked out concretely rather than asserted, **collapses in two ways**: (1) the exact p-adic
data (v_{q*}(a_n), or the full divisor-class g_n) is demonstrably *not* monotone/absorbing on
real data — ruling out the natural monovariant-induction family outright; (2) the
q-adic-order encoding of the minimality rule is literally Lemma H, already certified dead for
this purpose (round 5/9). The one positive, non-trivial finding — isolated/scattered (not
run-shaped) failure patterns in the one setting where failures could be found at all (hub
primes, under-recruited core) — is genuine new empirical support for the Successor Claim's
plausibility, but is far short of a proof and explicitly caveated as not a clean test of the
real F′/F″ instance.

- **Distinct openings surfaced:** (a) track v_{q*}(a_n) exactly rather than binarily — refuted
  as a monovariant on real data (new negative finding, worth recording so no future round
  re-tries it); (b) track the full confined-gcd divisor class g_n∈Div(b) for
  absorbing/one-way structure — also refuted (jump to 1133 then revert to 11); (c) hunt for
  actual failure instances (none exist at properly recruited |F′|,|F″|≥2 cores per round 9;
  found some at under-recruited/hub cores) to classify scattered-vs-runs — found scattered/
  isolated, supporting but not proving the Successor Claim.
- **Candidate technique(s):** none newly viable under this lens. The exact-valuation/
  divisor-class monovariant family is now empirically dead (not just theoretically stalled).
- **Cheap-kill candidates:** none beyond what's above — the numeric experiments above ARE
  the cheap kill for this lens (both took <1s of actual sequence generation once `math.gcd`
  replaced sympy's slower `gcd`; NOTE for future explorers: use `math.gcd`/manual trial
  division, not `sympy.gcd`/`sympy.primefactors`, which are 10-100x slower and caused a
  timeout in this session before the switch).
- **Knowledge-base entries relevant:** none of `knowledge_base.md`'s generic theorems bear
  directly on this valuation experiment beyond what's already cited in the certified lemma
  stack (Confined-GCD Lemma, Critical Prime Dichotomy/Lemma H, Free Facts).
- **Analogous past problems (cruxes):** did not query the crux corpus this round (out of
  scope for the assigned narrow valuation lens; a general explorer should still check
  `crux_moves_documentation.md` subtopics like "p-adic valuation," "greedy sequences," or
  "eventually periodic sequences" for a genuinely analogous solved problem — I did not find
  time to do this within the valuation-only mandate and do not want to force a weak match).
- **Prior progress:** unchanged from `current.md` — FAH/Cofinite FAH (≡ Successor Claim ≡
  EEA) remains the sole open crux, 15 mechanisms dead. This round's finding adds a 16th:
  exact-valuation/divisor-class monovariant induction, confirmed dead by direct
  counterexample (non-monotone v_{q*}, non-absorbing g_n) on the one genuine |F′|,|F″|≥2
  instance on record (a_1=11305).
- **Dead ends (do not retry):** (i) "v_{q*}(a_n) is eventually monotone along same-type
  occurrences" — false, index 805→863 (2→1) and 2067→2126 (3→1) on a_1=11305; (ii) "the
  confined-gcd divisor class g_n is absorbing once it grows" — false, index 1551 (g=1133)
  reverts to g=11 at index 1665; (iii) re-deriving Lemma H in valuation language — same dead
  mechanism, not new, confirmed by direct inspection.
- **Small-case / intuition notes (labeled conjecture):** the scattered/isolated (never
  run-shaped) failure pattern observed at hub primes/under-recruited cores is weak evidence
  *for* the Successor Claim's truth (consistent with literal FAH just being true and provable
  by some not-yet-found mechanism, as round 9 also concluded), but this is conjecture from a
  non-representative (hub-prime) setting, not a proof-relevant reduction.
