## Status
partial

## Approaches tried

- **Direct explicit bound on d_n = a_{n+1}-a_n via a fixed covering set (this
  round).** Outcome: **succeeds, cleanly, and better than the outline
  anticipated** — a complete, rigorous proof that d_n ≤ rad(a_1) (the product
  of the distinct primes dividing a_1) for *every* n ≥ 1, obtained directly
  from Free Lemma P with no density/Mertens machinery needed at all. This
  closes Step 2 of the outline in full, and specifically refutes the outline's
  worry that "a single interval-density argument can't account for
  simultaneous compatibility with all earlier terms" — see the Current best
  section for exactly why that worry does not apply to this particular bound.

- **Attempt to upgrade the bound to a genuinely finite/backbone-agnostic
  state for Step 3 (this round).** Outcome: **dead end, located precisely.**
  I pushed the covering-set idea further (the "trace / hitting-set"
  refinement below) to see whether boundedness alone, or a slightly sharper
  density-style argument, forces a *finite deterministic state* without first
  pinning down which extra primes beyond rad(a_1) are ever recruited. It does
  not: the refinement reduces the problem to exactly the same
  backbone-finiteness question that `backbone-existence-crt` and
  `intersecting-family-covering-construction` are already attacking (whether
  a finite set of primes beyond rad(a_1) is eventually — or from the start —
  *permanently sufficient*), and I could not find a density-only argument
  that resolves *which* extra primes get recruited or that only finitely many
  ever are. This is reported honestly below as the located failure point,
  together with a worked example (a_1 = 65) showing concretely where a purely
  density/counting approach runs out of traction. So this approach's
  distinguishing promise — "bound first, without ever identifying the
  backbone" — does not survive past the boundedness step; genuine periodicity
  needs the same backbone-identification content the other two approaches
  need, just reached from a different entry point.

## Current best

### Setup and the two shared preliminaries

Let a_1 > 1 be given, and let a_1, a_2, a_3, ... be the sequence defined in
the problem: a_{n+1} is the smallest integer greater than a_n with
gcd(a_{n+1}, a_i) > 1 for every i = 1, ..., n.

**Free Lemma P (permanent hub).** For every n ≥ 2, gcd(a_n, a_1) > 1.
*Proof.* This is the instance i = 1 of the defining condition applied to
a_{n} for n ≥ 2 (i.e. a_n was chosen, at the step producing it, to satisfy
gcd(a_n, a_i) > 1 for every i < n, in particular i = 1). ∎
Write P_1 = rad(a_1) = {p_1, ..., p_k} for the set of distinct primes
dividing a_1 (k ≥ 1), and let L = p_1 p_2 ⋯ p_k (the product, equivalently
the lcm, of the distinct primes in P_1 — this is the *radical* of a_1 as an
integer; I will write rad(a_1) for this integer L when the context is clear
and P_1 for the underlying prime set).

**Free Lemma Q (prime-power base case).** If k = 1, i.e. a_1 = p^m for a
single prime p, then a_n = a_1 + p(n-1) for every n ≥ 1; in particular
T = 1, L = p exactly, from n = 1.
*Proof.* Induct on n. The case n = 1 is trivial. Suppose a_1, ..., a_n are
all multiples of p (true for n=1, and a_1 = p^m is a multiple of p). For
1 ≤ j ≤ p-1, a_n + j is not a multiple of p, so gcd(a_n+j, a_1) =
gcd(a_n+j, p^m) = 1 (since p ∤ a_n+j and p is a_1's only prime factor);
hence a_n + j fails the i=1 condition and is inadmissible. On the other
hand a_n + p is a multiple of p, so for every i ≤ n (all of which are
multiples of p by the inductive hypothesis), gcd(a_n+p, a_i) is a multiple
of p, hence > 1: a_n + p is admissible. Since a_n+1,...,a_n+p-1 are all
inadmissible and a_n+p is admissible, a_{n+1} = a_n + p, and a_n+p is again
a multiple of p, closing the induction. ∎

This disposes of every a_1 that is a prime power (in particular every even
a_1, taking p = 2) completely and exactly. **From here on assume k = |P_1| ≥ 2.**

### Step 2 (closed): an explicit, uniform bound on every gap

**Lemma 1 (uniform gap bound).** For every n ≥ 1, d_n := a_{n+1} - a_n ≤ L,
where L = rad(a_1) = p_1⋯p_k as above.

*Proof.* Fix n ≥ 1. Let x_0 be the smallest multiple of L that is strictly
greater than a_n; since consecutive multiples of L are L apart,
a_n < x_0 ≤ a_n + L.

I claim x_0 is an admissible candidate at step n, i.e. gcd(x_0, a_i) > 1 for
every i = 1, ..., n. Fix such an i.

- If i = 1: a_1's prime factors are exactly the elements of P_1 (by
  definition of P_1 = rad(a_1)), so some p_j ∈ P_1 divides a_1. Since L is
  the product of all of P_1, p_j | L | x_0. Hence p_j divides both x_0 and
  a_1, so gcd(x_0, a_1) ≥ p_j > 1.
- If 2 ≤ i ≤ n: by Free Lemma P, gcd(a_i, a_1) > 1. Any common divisor of
  a_i and a_1 that is greater than 1 has a prime factor, and any prime
  factor of a common divisor of a_i and a_1 is in particular a prime
  factor of a_1, i.e. lies in P_1. So there is a prime p_j ∈ P_1 with
  p_j | a_i (and p_j | a_1, though we only need p_j | a_i here). Again
  p_j | L | x_0, so p_j divides both x_0 and a_i, giving gcd(x_0, a_i) ≥
  p_j > 1.

So x_0 satisfies gcd(x_0, a_i) > 1 for every i = 1, ..., n, i.e. x_0 is an
admissible candidate for a_{n+1}. Since a_{n+1} is defined as the *smallest*
integer greater than a_n satisfying this property, a_{n+1} ≤ x_0 ≤ a_n + L.
Hence d_n = a_{n+1} - a_n ≤ L. Since n was arbitrary, this holds for every
n ≥ 1. ∎

This closes the outline's Step 2 completely, with an explicit, effective
bound D(a_1) = rad(a_1) depending only on a_1 (not on n). Numerically
checked (Python, greedy simulation against `math.gcd`, 400 terms) against
the stress test a_1 = 247 = 13·19: rad(247) = 247, and the observed maximum
gap through 400 (and, per the explorer's run, through 1500) terms is 78 ≤
247, consistent; likewise for a_1 ∈ {65, 91, 143, 15, 105} the observed
maximum gap never exceeds rad(a_1). This is a sanity check only, not part
of the proof — Lemma 1 above is a self-contained proof requiring nothing
beyond Free Lemma P and the definition of L.

**Why this resolves the outline's stated worry.** The outline flagged, as
the likely fatal issue: "a naive density bound only shows *some* window
contains an integer divisible by a chosen prime of P_1 — it does not by
itself guarantee compatibility with every one of the n-1 other earlier
terms simultaneously." Lemma 1's proof shows this worry does not apply to
the bound at hand: the candidate x_0 is not divisible by "a chosen prime"
of P_1 but by *every* prime of P_1 simultaneously (x_0 is a multiple of
L = p_1⋯p_k), and Free Lemma P guarantees that *every* earlier term a_i
(i = 1, ..., n, for every n, not just some) is divisible by *at least one*
prime of P_1. So compatibility of x_0 with every earlier term is not an
extra density assumption — it follows automatically from Free Lemma P being
a statement about *every* n, which is exactly the "multi-term" strength the
outline worried a density argument would lack. This is the genuine,
non-obvious content of this round's work: the multi-term-compatibility
obstacle the outline predicted at Step 2 does not actually occur there.

### Step 3 (open, located precisely): why boundedness does not hand us a
finite state

Lemma 1 gives d_n ≤ L for all n, hence a_n ≤ a_1 + (n-1)L, so the sequence
grows at most linearly and (trivially) has bounded gaps. The outline's Step
3 hoped this alone — via a "window state" (a_n, a_n mod m) for "an
appropriately chosen finite modulus m" — would give a finite deterministic
state, hence eventual periodicity by pigeonhole, *without* first
identifying which primes beyond P_1 the process ever needs. I attempted to
make this precise and it fails, for a reason sharper than "the modulus
isn't obviously known": the admissibility test genuinely depends on
unboundedly many earlier terms, and boundedness of the gap sequence does
not by itself bound how much of that history is relevant. I pushed the
covering-set idea one level further to see exactly how far it goes before
this bites.

**Refinement: reduce admissibility (via P_1 alone) to finitely many "trace
types."** For a positive integer x, let T(x) = {p ∈ P_1 : p | x} (its trace
on P_1). For i ≥ 1, T(a_i) is nonempty: for i = 1 this is P_1 itself
(a_1's prime factors are exactly P_1); for i ≥ 2, Free Lemma P gives some
p_j ∈ P_1 dividing a_i, so T(a_i) ⊇ {p_j} ≠ ∅. Since P_1 has only k
elements, T(a_i) ranges over a set of at most 2^k - 1 possible nonempty
values as i varies. Define, for n ≥ 1, 𝒮_n := {T(a_i) : 1 ≤ i ≤ n} ⊆
2^{P_1} \ {∅}; this is non-decreasing in n and bounded in size by 2^k - 1,
so it stabilizes: there is a finite N_1 (depending on the whole sequence)
and a finite family 𝒮_∞ = 𝒮_{N_1} = 𝒮_n for all n ≥ N_1, with 𝒮_n ⊆ 𝒮_∞
for every n (including n < N_1).

*Claim:* if T(x) ∩ S ≠ ∅ for every S ∈ 𝒮_∞ (i.e. T(x) is a "hitting set"
for the finite family 𝒮_∞), then gcd(x, a_i) > 1 for **every** i ≥ 1 (not
just i ≤ n for some fixed n) with T(a_i) determined this way — because
T(a_i) ∈ 𝒮_i ⊆ 𝒮_∞ for every i, so T(x) meets T(a_i), giving a common prime
factor of x and a_i. This is a strictly sharper sufficient condition than
Lemma 1's "x divisible by all of P_1" (T(x) = P_1 trivially hits every
S), and in general needs only a hitting set of 𝒮_∞, which can be a proper
subset of P_1 when 𝒮_∞ does not contain every singleton {p_j}.

This refinement is genuine progress in that it isolates *exactly* the
combinatorial quantity — a hitting set of the (a priori unknown, but
finite) family 𝒮_∞ — that determines how "cheap" a P_1-only fallback
candidate can be. But it does **not** close Step 3, for two compounding
reasons, both illustrated concretely by a_1 = 65 = 5 · 13 (k = 2, P_1 =
{5, 13}):

1. **𝒮_∞ can force the hitting set back up to all of P_1.** If both
   singletons {5} and {13} occur as traces of some earlier term (a term
   divisible by 5 but not 13, and a term divisible by 13 but not 5 — both
   occur empirically for a_1 = 65), then any hitting set of 𝒮_∞ ⊇
   {{5}, {13}} must intersect both {5} and {13}, forcing it to contain
   *both* 5 and 13 — i.e. the P_1-only fallback collapses back to Lemma
   1's crude bound (x divisible by all of P_1) with no improvement. So the
   refinement gives no gain exactly in the cases where it would matter
   most for a bound tighter than Lemma 1.
2. **The *actually observed* minimal admissible numbers are smaller than
   even Lemma 1's bound, and empirically use primes outside P_1 (2 and 3
   for a_1 = 65, giving an eventual period with L_period = 390 = 2·3·5·13)
   — so the true greedy process is NOT using the P_1-hitting-set fallback
   at all for many steps.** For this to happen validly, those smaller
   candidates must be achieving compatibility with the singleton-trace
   ({5}-only or {13}-only) earlier terms via some *other* shared prime
   (not necessarily 5 or 13). This can only work systematically — i.e.
   apply to *every* earlier {5}-only term, not just some — if those terms
   share some further common structure (e.g. all being even, or all being
   multiples of 3) that is not implied by anything proved so far. Whether
   such a further common prime is *eventually always available*, and
   whether *only finitely many* such extra primes are ever needed, is
   precisely the backbone-finiteness question that `backbone-existence-crt`
   Step 3 and `intersecting-family-covering-construction` Steps 3-5 are
   already trying to resolve (recruitment of primes beyond P_1, and
   showing the recruitment process terminates). I was not able to find a
   density-only or counting-only argument (Mertens-type Σ 1/p bounds,
   inclusion-exclusion, or any variant) that decides this *without*
   effectively re-deriving which primes get recruited — the recruitment is
   governed by the greedy-minimality *dynamics* of the process (which
   specific small numbers turn out to be admissible at which specific
   steps), not by an a priori density estimate over "the primes available."
   A density bound can show *a* window of the right size contains *a*
   multiple of a covering set (this is exactly what Lemma 1 already gives,
   optimally, using P_1); it cannot, on its own, show that the greedy
   process's actual, dynamically-determined choices settle into a
   permanently-fixed finite covering set, because that requires tracking
   *which* auxiliary primes the specific sequence of earlier terms happens
   to share — an entirely different (combinatorial/dynamical, not
   density) question.

**Conclusion on Step 3.** The "generic pigeonhole on a bounded window"
step promised by this approach's outline is not actually generic: making
it precise (via the trace/hitting-set refinement above, which is the
natural way to try) shows it requires exactly the same finite-backbone
fact the sibling approaches are built around — this approach does not
avoid identifying the backbone; it just discovers that need one step later,
at Step 3 instead of Step 2. I therefore report Step 3 as an unresolved
gap of the same nature as (not different from, and not solvable
independently of) `backbone-existence-crt`'s Step 3 and
`intersecting-family-covering-construction`'s Steps 4-5, rather than as a
new, independent contribution.

### Honest summary

- Step 2 (uniform explicit bound on d_n): **fully closed** — Lemma 1
  above, D(a_1) = rad(a_1), proved rigorously, no gaps. This is
  genuinely useful and reusable independent of whether this approach's
  Step 3 ever closes (see Promotable lemmas).
- Step 3 (upgrade bounded gaps to a finite deterministic state / eventual
  periodicity, "backbone-agnostically"): **does not close** — the
  approach's central promise (avoid ever identifying the backbone) fails;
  the trace/hitting-set refinement shows precisely that the same
  backbone-finiteness fact used elsewhere is unavoidable once one asks for
  more than the crude L-fallback bound. No progress toward periodicity
  itself (T, L existence) is established beyond Lemma 1's boundedness.
- Step 4 (n=1 sharpening): not reached, moot until Step 3 closes.

Given this, the approach as a whole remains at `partial`: it contributes
one clean, fully proved, reusable lemma (Lemma 1) plus a precise negative
diagnosis of where and why the "bound-first, backbone-agnostic" strategy
runs out, but it does not establish the problem's conclusion (existence of
T, L with a_{n+T} = a_n + L for all n).

## Full proof
(Not applicable — Status is partial, not solved.)

## Promotable lemmas

**Lemma 1 (uniform explicit gap bound).** Let a_1, a_2, ... be the sequence
defined in the problem statement, and let L = rad(a_1) (the product of the
distinct primes dividing a_1). Then for every n ≥ 1, a_{n+1} - a_n ≤ L.

*Where proved:* in full, in the "Step 2 (closed)" section above. Proof
uses only Free Lemma P (gcd(a_n, a_1) > 1 for all n ≥ 2, itself the i=1
instance of the problem's own defining condition) and the definition of L;
no external theorems beyond that are invoked. Fully self-contained,
reusable by any other approach as a starting bound (e.g. to seed a
finite-state argument once/if a correct finite backbone is identified by
another route), and in particular gives Free Lemma Q's exact answer (T=1,
L=p) as the special case k=1 automatically (rad(p^m) = p), which is a good
consistency check on the lemma's statement.
