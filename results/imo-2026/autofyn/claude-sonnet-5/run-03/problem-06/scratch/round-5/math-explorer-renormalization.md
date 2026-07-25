## imo-2026-06 (lens: renormalization-induction-on-seed — alternative induction measures)

- **Distinct openings surfaced this pass:**
  1. **Diagnosis of why "locking" is the wrong target notion (new, from direct
     computation).** I extended the eventual-period computation for
     `a1=35`, `a1=65`, `a1=15`, `a1=375` far past what the approach file
     reports. Eventual period sums: `a1=15 → L=30=2·3·5`; `a1=35 →
     L=210=2·3·5·7`; `a1=65 → L=390=2·3·5·13`; `a1=375 → L=3990=2·3·5·7·19`
     (found only after running the sequence to `N=20000` terms and finding
     period `T=852` — much longer transient than anything previously
     computed for this instance). **Key structural fact**: `p=5` for
     `a1=35` stops dividing *every* term after index 2 (the "lock" breaks,
     exactly as the certified `bounded-lookahead-insufficiency.md` shows),
     yet `5` is still a factor of the *eventual period sum* `L=210` — i.e.
     `5` remains permanently "active" in the sense of dividing a
     periodically-recurring residue class of positions, just not *every*
     position from some point on. This means the renormalization
     approach's core definitional notion — "locked from index `n0`" =
     "divides every `a_n` for `n≥n0`" — is **strictly stronger than what
     the true eventual structure requires**, and is why every locking-based
     induction attempt (naive, bounded-lookahead) breaks: the real
     invariant object is a *periodic residue-class pattern* per prime
     (matching `lemmas/periodicity-of-residue-class-union.md` from
     `state-compactness-pigeonhole`), not a permanently-true divisibility.
     **Recommendation: any further renormalization attempt should redefine
     "locked" as "divides a periodic union of residue classes eventually,"
     not "divides every sufficiently large term" — the latter is refuted by
     its own certified counterexamples and no fix of it (bounded or
     otherwise) can work, because it is asking for something false about
     the actual eventual structure.**
  2. **A genuinely different architecture found in the crux corpus:
     scalar monovariant instead of set/prime bookkeeping (aimo-0678,
     "IMO-type gcd/lcm coupled recurrence, eventually periodic").** Its
     crux move: define a frozen invariant `s_n` (there, `a_n+b_n`, frozen
     exactly on the "boring" steps) and `w_n := min{m ≥ a_n : m ∤ s_n}`
     (the least value at or above the current term that breaks the frozen
     invariant); prove `w_n` is **non-increasing** (Claim 1: on a boring
     step `w` doesn't change; on an "exceptional" step `w_n` strictly
     drops to at most the current `a_n`), hence eventually constant by
     well-ordering, and periodicity falls out once it stabilizes. This is
     architecturally exactly what this lens was asked to scout: a
     **potential-function / monovariant that adapts (not a fixed
     lookahead)**, bounded below and non-increasing, with NO need to
     pre-guess a finite `Q`. It is a genuinely different top-level
     framing from both (a) the population's shared "construct one global
     Q" architecture and (b) `renormalization-induction-on-seed`'s own
     "lock one prime, induct on ω(a1)" framing. **This is not a direct
     transplant** — our problem has no natural companion sequence `b_n` or
     obvious frozen sum invariant, and the "boring step" in aimo-0678
     is `a_n | b_n` (a divisibility fact), while ours is "the greedy
     increment equals `rad`-multiple `p`" (a coprimality fact) — so
     translating requires real new work, not copying. But the *shape* of
     the technique (bound a min-of-a-set statistic tied to a frozen
     quantity, show it's non-increasing) is worth an explicit new approach
     slot, distinct from renormalization-on-seed.
  3. **Reduce to a well-founded measure on the *set of currently-open
     primes*, not on ω(a1).** Since `Nec` (certified in
     `nec-necessity.md`) can include primes outside `R(a1)` (confirmed
     again this round for `a1=375`: eventual `Q={2,3,5,7,19}`⊋rad(375)'s
     support `{3,5}`), any induction keyed to `ω(a1)` is measuring the
     wrong quantity — the actual state space that needs to shrink is
     "primes not yet decided as locked-forever-or-excluded," which is not
     determined by `a1` alone. A cleaner induction target: strong
     induction on `|Q_min|` for the actual (unknown a priori) minimal
     self-sufficient `Q`, i.e. do the induction *after* hypothetically
     fixing `Q` rather than fixing `a1` — but this is circular with the
     central existence gap (as `current.md` already flags) unless paired
     with an independent finiteness argument. Not a new working idea, but
     clarifies exactly *why* seed-`ω` induction was doomed: `ω(a1)` and
     `|Q_min|` are not comparable in general (`Q_min` can strictly exceed
     `R(a1)` in size, as the fresh `a1=375` computation shows), so
     shrinking `ω(a1)` via renormalization does not obviously shrink the
     real state space that governs periodicity.

- **Candidate technique(s):** (i) redefine "locked" as eventual periodic
  covering by residue classes and try to combine renormalization with
  `state-compactness-pigeonhole`'s Lemma P machinery instead of treating
  them as rival architectures (§5 of the approach file already gestures at
  this, calling it "interleaving," but doesn't attempt it); (ii) the
  aimo-0678-style scalar monovariant (`w_n = min{m≥a_n : m fails some
  frozen test}`, proven non-increasing) as a wholly new architecture,
  worth its own approach slot; (iii) infinite descent / minimal
  counterexample on `a1` combined with a *shift-invariant* recurrence
  fact (needs first solving the "renormalized tail is not itself an
  instance of the problem" obstruction flagged in §2 of the approach
  file — I did not find a fix for this in the time available; it remains
  a genuine structural obstacle, not just an unproved lemma).

- **Cheap-kill candidates:** none new found for the general problem. One
  useful negative-result generalization confirmed numerically but not
  proved: for every squarefree two-prime seed tested (`p<q≤37`, 66 pairs,
  reused from the certified Third-Term Dichotomy computation), the min
  prime `p:=min R(a1)` is *never* permanently locked from step 1 whenever
  `k'=k/p^{v_p(k)}>1` with `k=q+1` having a prime factor `<` some bound —
  this is exactly the dichotomy already proved, no new cheap kill beyond
  what's certified.

- **Knowledge-base entries to use:** none of `knowledge_base.md`'s Number
  Theory entries (LTE, Zsigmondy, Bertrand, Dirichlet, three-gap theorem,
  linear recurrences mod m) directly apply to this problem's specific
  greedy/gcd structure — this has been the consistent finding across all
  prior rounds and remains true. The one entry with real resonance is
  "**Linear recurrences: … sequences are eventually periodic mod m**" as
  the *target statement's* natural analogue, not a proof tool.

- **Analogous past problems (cruxes):**
  - **`aimo-0678`** (coupled `gcd`/`lcm` recurrence, IMO/ISL flavor,
    subtopics `size-bounding-and-descent` / `modular-arithmetic-and-CRT` /
    `invariants-and-monovariants`): the closest *structural* analog found
    this round — a greedy-flavored integer recurrence proved eventually
    periodic via a **non-increasing min-of-a-set monovariant tied to a
    frozen invariant**, then a finite-state pigeonhole finish (mod
    `M=lcm` of bounded values) as an alternate solution. Genuinely
    promising as a technique to adapt (see opening #2 above), not a
    direct transplant (no natural analogue of `b_n` or the frozen sum
    exists yet for our problem).
  - **`aimo-0886`** (`a_{n+2m} | a_n+a_{n+m}` ⟹ eventually periodic,
    ISL-style, subtopics involve divisibility/AP-of-indices arguments):
    its crux — "for each divisor `d`, the index set `{n : d | a_n}` is an
    exact arithmetic progression; combine over all divisors via
    `D=∏ d_s` to get periodicity of the whole sequence" — is the *same
    general strategy* already being pursued by `state-compactness-pigeolhole`'s
    Lemma P (residue-class-union periodicity), so it corroborates that
    approach's framing is "the right shape" for a solution, but does not
    give a new mechanism for *this* problem's harder step (existence of a
    finite generating `Q`); not directly transplantable because the
    divisibility-transfer Lemma 1 there relies on the specific additive
    "midpoint" relation `a_{n+2m} | a_n + a_{n+m}`, which our gcd-greedy
    recurrence does not have an analogue of.
  - **`aimo-0477`** (sum-of-ratios-is-integer forces eventually constant
    sequence): its crux tracks `d_n = gcd(a_1,a_n)` and shows it's
    eventually non-decreasing and bounded, hence stabilizes — the same
    general "bounded monotone integer sequence stabilizes" shape as
    aimo-0678, reinforcing that the monovariant idea (opening #2) is a
    recurring, well-tested technique in this problem family, worth a
    dedicated attempt. Not directly transplantable (relies on the sum
    being an integer, no analogue here) but useful corroboration that
    "track `gcd(a_1, a_n)`-style quantities and show eventual
    monotonicity" is a proven-productive pattern for *this class* of
    "prove eventually periodic/constant integer sequence" problems.

- **Prior progress:** as recorded in `current.md`/approach file — free
  base case (prime-power seeds, §3) and the fully general, algebraically
  proved Third-Term Dichotomy Lemma for squarefree two-prime seeds (§4.2),
  both unconditional and certified. General inductive step open.

- **Dead ends (do not retry):**
  - Naive "lock `p=min R(a1)` from the start, renormalize the quotient
    tail" — refuted, `a1=35` (round 4, reconfirmed via closed form this
    round in §4.3).
  - "Bounded lookahead certifies permanent locking" (check `k` steps
    ahead for any fixed `k`, even `k=2`) — refuted, `a1=65`
    (`bounded-lookahead-insufficiency.md`).
  - (Re-confirmed this round, not previously stated this explicitly)
    "Locked forever" (divides *every* sufficiently large term) is not
    even the right target notion in general — `a1=35`'s `p=5` stops
    dividing every term after index 2 yet remains a permanent factor of
    the eventual period `L=210` via periodic (not universal) recurrence.
    Any future renormalization attempt that defines its induction
    hypothesis via "divides every term from some point on" is targeting a
    **false** general fact and will hit the same wall as the two already-
    refuted mechanisms above, for the same underlying reason.

- **Small-case / intuition notes (all labeled conjecture except where
  marked "proved"):**
  - **Proved (direct computation, not simulation-dependent claims):**
    eventual periods: `a1=15→T=8,L=30`; `a1=35→T=34,L=210`;
    `a1=65→T=58,L=390`; `a1=375→T=852,L=3990` (this last one is new
    data this round — previously the population only knew `a1=375`
    breaks the `{p≤rad(a1)}` hitting-set conjecture at `(a3,a7)`, not its
    eventual period; the long transient `T=852` itself is a striking data
    point re: how far from "small bounded lookahead" this problem's
    dynamics actually are).
  - **Conjecture, strongly suggested by the above four data points plus
    round-4's `a1=194287` finding:** `L` (the eventual period sum) is
    always squarefree and equal to the product of `R(a1)` together with a
    (possibly empty, possibly containing primes `>rad(a1)`) finite set of
    "recruited" primes; the recruited primes are frequently small (`2`,
    `3`) but not always bounded by `rad(a1)` (confirmed exception:
    `19>15=rad(375)`). No monovariant or closed-form rule for exactly
    which primes get recruited was found this round; this remains the
    honest core of the central open gap, now with one more concrete data
    point (`a1=375`'s full eventual `Q={2,3,5,7,19}` and its unusually
    long transient `T=852`) for whichever future approach attempts a
    monovariant or covering-density argument.
