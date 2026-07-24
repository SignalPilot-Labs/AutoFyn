## imo-2026-06 (lens: covering-system / CRT forcing)

### Setting (recap, not re-derived — already reviewer-certified in round 1)
Whole problem reduces exactly (Lemmas A–D / 1–6, `lemmas/enumeration-and-bounded-gaps.md`,
`lemmas/finite-hitting-set-periodicity.md`) to one open statement:

> **(HS/MCL).** There is a finite set of primes S such that every pair of terms shares a prime
> in S. Equivalently Π = {min(supp(aᵢ)∩supp(aⱼ)) : i<j} is finite.

R = rad(a₁), S₀ = supp(a₁). Already proved: gaps a_{n+1}-a_n ≤ R (fixed constant from a₁ alone);
**every** term (not just pairs) is divisible by some prime of S₀ (this is a one-sided cover, proved
inside Lemma A/3's proof — stronger than just "gaps bounded"). This one-sided cover is the natural
starting point for a covering-system attack, and is worth restating explicitly since it wasn't
flagged as a standalone fact in round 1's approach files.

### Distinct openings

**1. [NEGATIVE / obstruction — report to prevent wasted effort] Literal finite-prime covering of
ℤ is impossible.** The dispatch's literal question — "does the small-prime set already form a
covering system of the integers, so every sufficiently large integer is divisible by some p ∈ P"
— is **false for any finite set of primes P**, by an elementary density/CRT argument: the density
of integers coprime to every p ∈ P is ∏_{p∈P}(1−1/p) > 0 (finite product of factors < 1 is never
0), and by CRT this density is realized exactly and periodically mod ∏P — e.g. x = 1 + ∏_{p∈P}p is
explicitly coprime to all of P, and such x recur with bounded gap ≤ ∏P. So no finite prime set can
"cover" (in the naive divisibility sense) even a single residue-window fully; there are always
integers avoiding all of S₀ (or any finite S) arbitrarily often. **This kills the literal
covering-system mechanism as stated** — it cannot be the load-bearing fact. What actually holds
(and is already proved, Lemma 3/A) is the *weaker, correct* fact: every multiple of R = ∏S₀ lies
in the admissible set A (not "every integer near aₙ," just the R-spaced multiples of R). This
weaker fact is what gives the bounded-gap Lemma A/3, and it is already fully exploited. Do not
re-attempt the literal "cover all integers" version.

**2. [Refined CRT idea — profile/color reduction over the *fixed* alphabet S₀, not a growing
prime set] "S₀-profile" finite-alphabet reduction.** Define for each term aₙ its S₀-profile
π(n) = supp(aₙ) ∩ S₀ ⊆ S₀, a nonempty subset of the *fixed* finite set S₀ (|S₀| = ω(a₁)). There
are only 2^{|S₀|}−1 possible profiles — a genuinely finite alphabet fixed from n=1, independent of
how many primes ever get recruited. Two terms with **intersecting** profiles are already
mutually admissible via S₀ alone (no extra prime needed). The only terms requiring an
extra/recruited connector prime are those with **pairwise-disjoint** profiles (e.g. profile {11}
vs {13} for a₁=1001). This is exactly the object essential-prime-counting's (P2) and
admissible-set-periodicity's cross-class analysis already isolate — but the profile alphabet
being *finite from the start* (not growing) is worth restating as the clean CRT-object: the
open gap (HS) is equivalent to "only finitely many primes are ever needed to additionally hit
pairs whose S₀-profiles are disjoint." This does not by itself close the gap (same wall as
before) but reframes it as a finite-alphabet covering-design problem: does the (finite) family of
occurring S₀-profiles admit a finite "resolving" prime set at all, and can CRT be used to
construct one explicitly rather than prove existence abstractly?

**3. [New, numerically motivated] "Cheapest-extra-prime" forcing mechanism — a candidate
mechanism for finiteness via greedy minimality + CRT density, not pure counting.** Numerical
experiment (this round, python/sympy, greedy simulation + exact Π computation over 600–1400
terms) computing Π = {min(supp aᵢ∩supp aⱼ)} directly:
```
a1=15   (S0={3,5})       Pi_extra beyond S0 = {2}            max(Pi)=5
a1=105  (S0={3,5,7})     Pi_extra = {2}                       max(Pi)=7
a1=143  (S0={11,13})     Pi_extra = {2,3,5,7}                 max(Pi)=13
a1=1001 (S0={7,11,13})   Pi_extra = {2,3,5}                   max(Pi)=13
a1=858  (S0={2,3,11,13}) Pi_extra = {}                        max(Pi)=2
a1=231  (S0={3,7,11})    Pi_extra = {2}                       max(Pi)=3
a1=385  (S0={5,7,11})    Pi_extra = {2,3,13,19}                max(Pi)=19  <-- exceeds max(S0)=11
a1=1155 (S0={3,5,7,11})  Pi_extra = {2}                       max(Pi)=11
a1=5005 (S0={5,7,11,13}) Pi_extra = {2}                       max(Pi)=13
a1=429  (S0={3,11,13})   Pi_extra = {2,5,7}                   max(Pi)=13
a1=15015(S0={3,5,7,11,13}) Pi_extra = {2}                     max(Pi)=13
a1=323  (S0={17,19})     Pi_extra = {2,3,5,7,11,13}           max(Pi)=19
```
Findings (all CONJECTURE / numeric evidence only): (a) recruited "extra" primes are always small —
never observed beyond the size of max(S₀) by more than a small factor, and re-running a1=385 at
N=1400 (vs N=600) reproduced the *identical* Π = {2,3,5,7,11,13,17,19} — no growth, consistent
with (but not proof of) stabilization; (b) the extra primes recruited are **exactly the small
primes not already in S₀**, recruited roughly in increasing order (2 first, then 3, 5, 7, ... as
needed) — never a "random" large prime; (c) a strong secondary finding: for every tested case,
**every term whose S₀-profile is a proper subset of S₀ (i.e. "deficient") is divisible by 2**
(checked exhaustively over 600 terms for a1 ∈ {15,105,1001,1155}, zero exceptions) — i.e. 2 acts
as a universal "cheap fallback" connector for profile-deficient terms, even when 2 ∤ a₁.
**Candidate mechanism to feed the outliner:** because greedy always picks the *smallest* valid
candidate, and among integers satisfying a fixed partial-profile constraint exactly a 1/p fraction
are additionally divisible by a given prime p, the *cheapest* way to patch a profile deficiency is
to recruit the *smallest* prime not yet forced to be absent — giving a natural well-ordering
argument: if a fresh prime q is ever strictly essential (sole connector, not replaceable by an
already-recruited smaller prime), minimality of the greedy choice should force q to be smaller
than any alternative that would have been tried first — suggesting recruited essential primes
arrive in a bounded, roughly increasing initial segment of the primes, which could plausibly
terminate (only finitely many are ever "cheap enough" to be forced) once the running product of
recruited primes overtakes R and the multiples-of-R fallback (Lemma A) becomes competitive again.
This is NOT yet a proof — it is a mechanism (a monovariant/well-ordering candidate) worth handing
to the outliner as an alternative to the pure-counting approach that is already known to fail.

**4. [Explicit-bound reframing] Attempt an EXPLICIT bound on essential primes instead of abstract
finiteness.** Rather than proving Π finite via compactness/pigeonhole abstractly (which is where
the counting approaches stalled), try to prove a concrete bound: every prime in Π is ≤ f(a₁) for
an explicit function f (e.g. f(a₁) = R, or R², or R·log R). This is a *different target* than
"finite" — a finite explicit bound is easier to attack by direct minimality arguments (bound the
size of the smallest candidate needed to patch a given profile deficiency, in terms of R and the
number of distinct profiles ≤ 2^{|S₀|}), and automatically implies (HS). Caution: numeric evidence
above (a1=385 → prime 19 recruited, exceeding max(S₀)=11, though still < R=385) is consistent with
a bound like "≤ R" but NOT with a bound like "≤ max(S₀)" — so any explicit-bound conjecture must be
in terms of R = rad(a₁) (or a₁ itself), not merely max(S₀). This refines Route D from round 1's
periodicity-lens explorer into something more concrete and falsifiable.

### Candidate technique(s)
- CRT / modular residue-class reasoning (as already used in Lemma 5/D) — but reframed around the
  *fixed, finite* S₀-profile alphabet (opening 2), not an abstract growing prime set.
- Extremal/well-ordering argument on "size of cheapest essential prime" driven by greedy
  minimality (opening 3) — a genuinely different mechanism from the pure density/counting attack
  already shown insufficient.
- Explicit-bound-in-terms-of-R conjecture (opening 4) as a sharper, more falsifiable target than
  abstract finiteness.

### Cheap-kill candidates
- The literal "finite prime set covers all sufficiently large integers" mechanism is **provably
  false** (density obstruction, opening 1) — flag to outliner as a mechanism NOT to attempt,
  saving a round.
- Every term (not just pairs) is divisible by some prime of the fixed S₀ = supp(a₁) — already
  proved (inside Lemma A/3), cheap fact worth restating explicitly as the starting "profile" object
  for opening 2/3.

### Knowledge-base entries to use
- "Modular arithmetic, CRT" — for the profile/residue-class Boolean reduction (opening 2), same
  entry already cited by the certified Lemma 5/D.
- "Pigeonhole / extremal principle" — candidate for a well-ordering/minimality argument (opening 3)
  if it can be dressed as "the sequence of first-recruited essential primes is eventually
  non-increasing/bounded," which is a pigeonhole-flavored finiteness argument distinct from the
  density-sum approach already shown insufficient.
- Density-count entries (Σ1/p² style) are the ones ALREADY shown insufficient — do not re-cite as
  a standalone mechanism; they remain useful only as an auxiliary bound, not the closing argument.

### Analogous past problems (cruxes)
Queried `sample_approaches` for existing approaches (see below) and re-checked
`crux_moves_documentation.md`-style corpus filtering already done in round 1
(`math-explorer-priorart.md`, `math-explorer-mechanics.md`) — no new strong matches found this
round beyond what round 1 already surfaced (`aimo-0678` state-compression, `aimo-0447`
interval-occupancy, `aimo-0514` reversibility). None of the corpus entries specifically address a
"cheapest-connector-prime" minimality/well-ordering mechanism (opening 3) — this appears to be a
genuinely novel angle not present in the corpus, consistent with round 1's finding that this
greedy-gcd mechanism has no close structural analogue in the crux database.

### Prior progress
Full reduction to (HS/MCL) is complete and reviewer-certified (see `current.md`,
`lemmas/enumeration-and-bounded-gaps.md`, `lemmas/finite-hitting-set-periodicity.md`). Both live
approaches (`admissible-set-periodicity`, `essential-prime-counting`) reduce to the identical open
gap and both attempted a pure counting/density attack that is proven insufficient (sparse
disjoint-profile families with density zero evade Σ1/p² bounds). `finite-state-reversible.md`
exists in `approaches/` but was not sampled by the ranker this round — worth the outliner checking
its status/reviewer-note directly if reused.

### Dead ends (do not retry)
- Pure pair-counting / interval-occupancy Σ1/p² density bound (both approaches, round 1): proven
  rigorous but insufficient — cannot exclude sparse (density-zero) disjoint essential-prime
  families. Do not re-attempt as a standalone closing argument; it can still serve as an auxiliary
  bound inside a minimality-based argument (opening 3/4).
- (New this round) Literal "finite prime set is a covering system of ℤ" (opening 1) — false by
  density obstruction, do not attempt.

### Small-case / intuition notes (all CONJECTURE, numeric evidence from python/sympy greedy
simulation + direct Π computation this round, 12 starting values, up to 1400 terms)
- Extra (non-S₀) essential primes are always small and recruited in roughly increasing order,
  starting with 2 — strongly suggests a minimality-driven "cheapest patch" mechanism (opening 3)
  rather than an arbitrary/unbounded recruitment process.
- Every profile-deficient term (S₀-profile a proper subset of S₀) was found divisible by 2 in
  every tested case (0 exceptions across 4 different a₁ values, 600 terms each) — a striking
  regularity suggesting 2 (or more generally the least prime not yet "spent") acts as a universal
  fallback connector, worth the outliner probing as a lemma candidate: "if a term's S₀-profile is
  deficient, it must be divisible by the smallest prime not in supp(a₁)" (conjectural, NOT proved;
  counterexample search with adversarial a₁, e.g. a₁ already divisible by 2, should be tried before
  trusting this).
- Recomputing Π at N=600 vs N=1400 for a₁=385 gave the *same* set {2,3,5,7,11,13,17,19} — no
  growth observed, mild evidence for stabilization (finiteness), but only one data point at
  increased N; not strong evidence on its own.
- max(Π) exceeded max(S₀) in one case (a₁=385: 19 > 11), refuting any bound purely in terms of
  max(S₀); all observed max(Π) values stayed well below R = rad(a₁) in every case, consistent with
  (but far from proving) an explicit bound of the form "essential primes ≤ R" (opening 4).
