## imo-2026-06

**Shared context for all four approaches below (do not re-derive; cite).**
Certified, importable without re-proof: Lemma P/P′ (pairwise intersecting
radicals), Lemma Q/S′ (Case I fully solved), Lemma 1 (linear gap bound,
`a_n ≤ a_1+(n-1)L`, `L:=rad(a_1)`), Domination Lemma, Lemma C, Theorem 5.1
(FCBC ⟹ whole problem, exact, from `n=1`), Theorem V / Theorem V-MRS
(`𝓥` finite ⟺ (MRS)), Theorem CD (`𝓥` finite ⟺ `𝓥_S` finite for every
nonempty `S⊆P_1`, an unconditional partition by `S(C):=C∩P_1`), Lemma TC
(`𝓥_{P_1}={P_1}`, the top core is trivial), Channel Assembly Theorem +
Channel Splitting Lemma (global FCBC ⟸ local `(LMRS_{S,S'})` for every
channel ⟺ `(MRS_S)` for every nonempty `S⊆P_1`), Finite-class direct
covering (channels touching a finite imprint class need no conditional
machinery). **The sole remaining gap, agreed by every live approach and by
`current.md`'s round-5 update, is: finiteness of `𝓥_S` (equivalently
`(MRS_S)`) for each of the `≤2^k-2` remaining *proper* nonempty cores
`S⊊P_1`** (`k:=ω(a_1)=|P_1|`). All four approaches below attack exactly
this, via four different mechanisms, per this round's explorer findings.

**New tool available to every approach this round: Lemma FOM (First-
Occurrence Minimality).** For `C` a nonempty finite set of primes, define
`T_C := min{x∈ℤ : x>a_1, rad(x)=C}` (well-defined: `(∏_{p∈C}p)^t` has radical
`C` for every `t≥1` and is unbounded). **Claim:** if `n≥2` is the first index
with `rad(a_n)=C` (no `i<n` has `rad(a_i)=C`), then `a_n=T_C` exactly.
*Proof sketch (elementary, verified by this round's fan-structural explorer
on 6000+ instances, zero exceptions — still needs a from-scratch proof in
whichever approach certifies it first):* admissibility of a candidate integer
against a fixed prefix depends only on its radical, not its magnitude.
Suppose `a_n≠T_C`; since `T_C≤a_n` by minimality of `T_C` among radical-`C`
integers `>a_1`, and `T_C` cannot equal any earlier term (that would
contradict "`n` is the first occurrence"), `T_C` falls in a unique gap
`a_i<T_C<a_{i+1}` with `i+1≤n`. Since `a_n`'s own admissibility gives
`C∩rad(a_j)≠∅` for every `j<n` (in particular `j≤i`), and `rad(T_C)=C`, `T_C`
is admissible against `a_1,…,a_i` too, and `T_C>a_i`, so by greedy
minimality `a_{i+1}≤T_C`; combined with `T_C≤a_{i+1}` this forces
`a_{i+1}=T_C`, contradicting `n` being `C`'s first occurrence unless
`i+1=n`, i.e. `a_n=T_C`. ∎ **Corollary (fan-size bound, conditional on
absorption happening).** If `C'` first occurs at index `m` (so `a_m=T_{C'}`
by FOM), then every earlier-realized value `C'∪{q}` (`q∉C'`, appearing at
some `i<m`) satisfies `q·∏(C')≤a_i<a_m=T_{C'}`, i.e. `q<T_{C'}/∏(C')` — an
explicit, finite, `a_1`-and-`C'`-computable bound on the number of distinct
"companion" primes recruited before `C'` is absorbed, **given that `C'` is
in fact eventually realized**. This does **not**, by itself, bound (i) how
many distinct absorbing `C'`s a channel ever cycles through, or (ii) whether
a fan can grow forever without ever being absorbed — those are exactly the
open content each approach below attacks differently. **Watch out (flagged
explicitly by this round's narrow-framing explorer):** do NOT present "a
finite absorbing set eventually gets hit for every generation" as a new
sufficient condition on its own — restated generally, that is circular,
the same trap as the already-refuted `H=rad(L_per)` characterization
(round 5). FOM is legitimate, provable, *specific* progress (an exact
closed-form value and a conditional bound); the termination argument (why
generations stop) is the genuinely open part in every approach below.

---

persistent-backbone-monovariant: revise
Target: the problem's exact headline conclusion `a_{n+T}=a_n+L` for every
`n≥1` (via the imported Theorem 5.1, conditional only on FCBC, which follows
from `𝓥` finite via the imported Theorem V + Theorem CD chain this approach
already owns).
Technique: direct global collapse-count / generation-growth argument on
`𝓥_S`, built on this approach's own already-certified No-Resurrection Lemma,
Interval Lemma, and Record Characterization Lemma — i.e. work with `𝓥_S`
as a static union and try to bound its cardinality by a counting argument on
successive "generations" (chains of ever-shrinking absorbing cores), not by
an induction on core structure (that is approach `core-depth-induction`,
kept genuinely separate) and not by a companion-count-style pigeonhole (that
is approach `imprint-automaton-periodicity`, kept genuinely separate).
Skeleton:
  1. Import Theorem CD + Lemma TC (already certified, cross-approach): `𝓥`
     finite ⟺ `𝓥_S` finite for every proper nonempty `S⊊P_1` — restate in
     this file's own notation (already uses `𝓥`, matches Theorem CD's object
     exactly, no translation needed).
  2. **Certify Lemma FOM in full** (first formal write-up in the population;
     the statement and proof sketch above, made rigorous) — natural home
     here since it strengthens this file's own already-certified Record
     Characterization Lemma (freshness ⟺ first-occurrence-of-a-minimal-value)
     with an *exact value*, not just an existence/membership fact.
  3. **New: Generation-Chain Lemma.** Fix a proper core `S`. Call a sequence
     `C_1⊋C_2⊋⋯⊋C_r⊇S` (`r≥1`) realized in channel `S` a *domination chain*
     if each `C_{i+1}` is, at the moment it is inserted into `𝓥`, a
     strict-subset dominator of `C_i` (i.e. `C_i` leaves `𝓜_n` because
     `C_{i+1}` appears). By the No-Resurrection Lemma (already certified),
     domination chains have strictly decreasing `|C_i|`, so **any single
     chain starting from a fixed `C_1` is automatically finite** (bounded by
     `|C_1|-|S|`) — this is a three-line consequence of already-certified
     material, not new difficulty. **The open content is not chain length
     but chain COUNT**: how many distinct maximal chains (equivalently, how
     many distinct elements ever enter `𝓥_S` at all, whether they end up
     dominated or are the eventual survivor) can channel `S` produce. State
     this precisely as the open target, replacing the vaguer "generation"
     language from the explorer reports with this formal chain definition.
  4. **Attempt (open, this round's genuine content): Growth-Budget Lemma.**
     Candidate mechanism: use Lemma 1 (`a_n≤a_1+(n-1)L`) to bound `T_{C'}`
     for any candidate absorbing core `C'` realized by index `n` (since
     `T_{C'}≤a_n` if `C'` is realized by then), giving `∏(C')≤a_1+(n-1)L`,
     hence only finitely many `C'` with `∏(C')` below any fixed threshold are
     *available* by any finite time `n` — try to convert this into a bound
     on total distinct chains by showing consecutive distinct maximal chains
     within `S` must have strictly growing `∏(C_1)` values (the "entry"
     radical of a new chain) at a rate incompatible with `a_n`'s linear
     growth, i.e. a counting/density contradiction if infinitely many chains
     occur. **This is not proved** — the reduction from "finitely many
     available at time `n`" to "finitely many total, ever" is exactly the
     kind of density argument round 4's `forced-primes-well-ordering`
     already showed is insufficient in isolation (pointwise-in-`n` control
     does not give cumulative finiteness) — flag this explicitly and do not
     present the Growth-Budget Lemma as closing the gap; it is the concrete
     next sub-target, not a proof.
Key lemmas (claim + mechanism):
  - Lemma FOM — because admissibility depends only on the radical, not the
    magnitude, of a candidate, so the first term realizing a given radical
    must be the globally-minimal such integer consistent with everything
    already fixed.
  - Fan-size corollary — because every earlier fan sibling is a strictly
    smaller (pre-absorption) term, hence `<T_{C'}`, forcing its companion
    prime below an explicit ratio.
  - Generation-Chain Lemma (chain length finite) — because No-Resurrection
    (already certified) forces strict `⊋`-decrease along any single chain,
    bounded below by `|S|≥1`.
Open gaps: the Growth-Budget Lemma (Step 4) — does not exist yet even as a
correct conjecture, only as a candidate shape of argument; this is honestly
the approach's full remaining content. Equivalently: bound the total number
of distinct domination chains (not their individual lengths) per proper
core `S`.
Cases to cover: Case I fully closed (imported Lemma S′/Theorem CI, no new
work). Case II: reduces via Theorem CD to the `≤2^k-2` proper cores, this
approach's Step 4 is the open content for each.
Watch out for: do not conflate "chain length finite" (already proved, cheap)
with "chain count finite" (the actual gap) — the round-5 population's own
Negative finding 2 (non-monotone `|𝓜_n|`) shows a naive cardinality
monovariant fails; Step 4 must produce a genuinely new counting mechanism,
not resurrect that refuted one.

---

core-depth-induction: new
Target: same headline conclusion as above, same conditional chain (FCBC via
`𝓥` finite via Theorem CD's core decomposition), via a genuinely different
top-level architecture: **strong induction on `|S|`** (the size of the
proper core, `1≤|S|≤k-1`, well-founded since bounded by the fixed finite
integer `k=ω(a_1)`), rather than a flat counting/order argument on `𝓥`
itself. This is the architecture explicitly flagged by this round's
narrow-framing explorer's "Opening A" generalization and by the dispatch as
the candidate escape from the recursive/circular trap: circularity becomes
legitimate strong induction once there is a strictly-decreasing well-founded
measure (`|S|`, bounded by `k`), which the raw "generation" language alone
lacked.
Technique: strong induction on core size `|S|`, from the base case `|S|=1`
(singleton cores) up through `|S|=k-1`, with the depth-`(d-1)` case's
finiteness result used as an explicit ingredient for the depth-`d` case —
NOT a flat re-application of the same lemma at every level (that would be
Opening A's refuted-as-circular restatement); the induction must show the
depth-`d` case's open content genuinely *reduces to* finitely many
depth-`(d-1)`-scale sub-problems.
Skeleton:
  1. Import Theorem CD + Lemma TC exactly as `persistent-backbone-
     monovariant` does: `𝓥` finite ⟺ `𝓥_S` finite for `1≤|S|≤k-1`.
  2. **Base case `|S|=1` (singleton cores `S={p}`, `p∈P_1`) — attempt a
     direct, self-contained finiteness proof, NOT importing Theorem CI
     verbatim** (Theorem CI solves genuine Case I, where `p` divides *every*
     term of the *whole* sequence; a singleton core `S={p}` here only means
     `p` divides every term with imprint *exactly* `{p}` — the subsequence
     `(a_i)_{i∈I_{\{p\}}}` is not an arithmetic progression and has no known
     closed form, so Theorem CI's mechanism does not transfer verbatim).
     Candidate mechanism (this round's genuinely new attempt, using Lemma
     FOM — cite from `persistent-backbone-monovariant` once certified, or
     reprove inline if built first): every element of `𝓥_{\{p\}}` is, by
     FOM, an exact value `T_C` for some `C⊇{p}`; show the set of `C` that
     can ever be `n`-minimal within this channel is controlled by which
     "companion" primes `q` first co-occur with `p` in an admissible term —
     **this is the approach's open content for the base case**, not closed
     this round; state the target precisely: "only finitely many distinct
     `C⊇{p}` are ever `n`-minimal for some `n`, restricted to indices with
     imprint `{p}`."
  3. **Inductive step (`|S|=d≥2`, assuming `𝓥_{S'}` finite for every proper
     core `S'` with `|S'|<d`) — attempt reduction, open this round.**
     Candidate mechanism, following this round's `a_1=21528751`,
     `S={197,103}` example (depth `2`, absorbed via two events with
     radicals `{2,103,197}`,`{3,103,197}` — each of the *shape* `S∪{q}` for
     a single extra companion `q`, structurally identical to a singleton-
     core absorption): conjecture that every element of `𝓥_S` (`|S|=d`) is
     either (i) `S` itself (if `S=∩` some sub-hub — check against Lemma TC's
     mechanism, which is the `S=P_1` case of a more general phenomenon), or
     (ii) of the shape `S∪Q` for `Q` a *finite* set of "extra" primes with
     `|Q|` bounded by the fan-size corollary once its absorption event is
     known to occur — and that bounding the number of distinct extra-prime
     sets `Q` that ever get absorbed reduces, index-by-index, to a
     **depth-1-style problem on the restricted index set** `I_S` (imprint
     exactly `S`), i.e. the exact base-case machinery of Step 2 applied one
     level up. **This reduction is NOT formalized or proved this round** —
     write it as the precise open conjecture (see "Open gaps"), not as an
     established step; the explorer flagged this exact temptation as
     circular if stated loosely, so the outline must isolate precisely what
     new fact would make it non-circular: a genuine bijection or injection
     from "generations at depth `d`" into "generations at depth `<d`" (not
     merely a structural resemblance).
  4. Conclude: if Steps 2–3 both close, `𝓥_S` finite for every `1≤|S|≤k-1`
     by induction, giving `𝓥` finite (Theorem CD), FCBC (Theorem V/Lemma
     MS), and the whole problem (Theorem 5.1).
Key lemmas (claim + mechanism):
  - Base-case reduction (Step 2) — because FOM pins every realized value to
    an exact, computable integer `T_C`, converting "is the channel's
    antichain history finite" into a concrete question about which `C⊇{p}`
    values are ever admissible, rather than an unstructured combinatorial
    search.
  - Depth-reduction conjecture (Step 3) — because the empirically-observed
    absorbing radicals at depth `d` are always of the shape `S∪{q}`
    (one companion at a time, matching the base case's shape exactly), so
    IF this shape is provably exhaustive (not yet shown), the depth-`d`
    problem literally restricted to `I_S` becomes formally identical to a
    depth-1 problem on a different ambient index set.
Open gaps: both Step 2 (base case) and Step 3 (inductive step) are open;
Step 3 additionally needs a NON-circular formalization of "reduces to
depth-`(d-1)`" — the mere numerical resemblance found by this round's
explorer is not yet a proof and must not be treated as one.
Cases to cover: Case I imported/closed. Induction covers `|S|=1,…,k-1`
exhaustively once both steps close — note `k` itself varies with `a_1`, so
the induction is over a family of statements parametrized by `a_1` too
(state this precisely: for EACH fixed `a_1`, induct on `|S|` from `1` to
`ω(a_1)-1`, a finite induction since `ω(a_1)` is one fixed integer).
Watch out for: (a) do not let the inductive step secretly assume the
depth-`(d-1)` result answers a *different* question (e.g. about a different
index set or a different notion of "core") than what is actually needed —
the reduction must be an honest logical implication, stated as precisely as
Theorem CD's own partition, not an analogy; (b) `a_1=21528751`'s `S={197}`
example (this round's narrow-framing report) shows a depth-1 channel whose
single absorbing radical already bundles THREE extra primes at once
(`{2,3,7,197}`), not one — so the "one companion at a time" shape assumed
in Step 3 is not universal even at depth 1; any base-case or inductive-step
lemma must handle multi-companion bundling, not just the single-companion
shape seen in the other examples.

---

imprint-automaton-periodicity: revise
Target: same headline conclusion, via the imported Theorem V-MRS + Theorem
CD + Lemma TC chain this approach already owns (certified here: Lemma PS,
Lemma NR, Theorem V-MRS, Theorem CD, Lemma TC).
Technique: direct combinatorial bound on the **companion-count** — the
number of distinct "absorption events" (times a genuinely new minimal
radical with a new companion prime becomes `n`-minimal and later survives or
is itself absorbed) that occur within a single proper-core channel — using
the already-certified DM-multiset-order tool (Step 1 of this file's round-5
outline, still valid and unused for the final gap) together with the new
Lemma FOM, kept genuinely distinct from `core-depth-induction`'s structural
induction and from `persistent-backbone-monovariant`'s chain-count
counting argument: this approach targets a single SCALAR quantity (the
companion-event count) directly, conjectured empirically bounded by 4 across
every tested channel (this round's narrow-framing explorer), rather than
building a recursive or chain-based apparatus.
Skeleton:
  1. Import Theorem CD + Lemma TC (already certified in this file):
     `𝓥` finite ⟺ `𝓥_S` finite for `S⊊P_1` proper nonempty.
  2. **Define the companion-event count formally.** For a proper core `S`,
     let `𝒜_S` be the (a priori possibly infinite) set of distinct radicals
     `C⊇S`, `C≠S`, that are ever `n`-minimal for some `n` restricted to
     indices with `S(rad(a_i))=S` (i.e. `C∈𝓥_S\{S}` in Theorem CD's
     notation, if `S` itself is ever realized — cite Lemma TC's proof
     technique to check whether an analogous "`S` itself is realized"
     dichotomy holds for general proper `S`, not just `S=P_1`). Restate the
     open target as: `𝒜_S` is finite for every proper nonempty `S⊊P_1`
     (equivalent, by Theorem CD, to `𝓥_S` finite, since `𝓥_S=𝒜_S∪(𝓥_S∩{S})`
     and the second part is a single set of size `≤1`).
  3. **Attempt (open, this round's genuine content): Companion-Count Bound.**
     Candidate mechanism, using the already-certified DM-multiset-order
     fact (any single collapse event is a strict multiset-order decrease)
     together with Lemma FOM (cite/import once certified): show that each
     element of `𝒜_S` either (i) is eventually dominated by a strictly
     smaller element (a DM-decrease, already well-founded per-chain by the
     Generation-Chain Lemma's argument, shared cite with
     `persistent-backbone-monovariant`), or (ii) survives forever (a
     permanent member of `𝓥_S`) — and attempt to bound the total count of
     type-(ii) survivors directly via Lemma P′ (pairwise intersection):
     **any two distinct permanent survivors of the same channel `S` must
     intersect** (Lemma P′, since both are radicals of actual terms), so if
     there are `≥2` permanent survivors `C_1≠C_2` in `𝓥_S`, `C_1∩C_2⊇S∪
     (C_1∩C_2\setminus S)≠∅` automatically (trivially true via `S` itself,
     since `S⊆C_1∩C_2` — **this alone gives NO new constraint**, an honest
     dead-end noted explicitly so the builder does not waste time on it;
     the real content must come from bounding *how many* distinct
     `C\supsetneq S` companions attach to `S` before the channel's growth
     phase provably ends, which Lemma P′ alone does not supply). **Flag
     precisely**: this mechanism, as stated, does not yet produce a bound;
     the concrete open sub-question is whether the fan-size corollary (from
     Lemma FOM, giving a bound *conditional on* absorption) can be combined
     with a pigeonhole on the finitely many primes below some `a_1`-
     dependent threshold (Lemma 1's linear growth) to force **either**
     absorption within a bounded number of steps **or** an explicit
     contradiction with minimality of the greedy rule (unproved).
Key lemmas (claim + mechanism):
  - Companion-event reformulation (Step 2) — because Theorem CD's partition
    already isolates exactly the transient companions from the (at most one)
    permanent value `S` itself.
  - Permanent-survivor pairwise-intersection observation (Step 3) — because
    Lemma P′ applies to any two realized radicals unconditionally; explicitly
    flagged as **insufficient alone** (trivially satisfied via `S`, giving no
    new bound) so a future round does not re-attempt this exact dead end.
Open gaps: the Companion-Count Bound itself (Step 3) — no working mechanism
found this round or in the dispatch's cited explorer report; only the
target quantity (a small integer, empirically ≤4) is sharply identified.
Cases to cover: Case I imported/closed. Every proper core `S` needs Step 3;
no case-split within Case II beyond the `1≤|S|≤k-1` cores already organized
by Theorem CD.
Watch out for: do not let the builder present the "permanent survivors
pairwise intersect via `S`" observation as if it were progress — it is a
tautology (any two supersets of `S` intersect in `S`), explicitly a dead
end, recorded here so it is not silently smuggled into a "proof."

---

forced-primes-well-ordering: revise
Target: same headline conclusion, via this approach's own Channel Assembly
Theorem + Channel Splitting Lemma (already certified here): global FCBC
follows from `(MRS_S)` (single-class antichain `𝓜_n^S` eventually constant)
for every nonempty `S⊆P_1`, with finite-imprint-class channels already fully
and unconditionally resolved (§D).
Technique: a **structural dichotomy** on proper cores — "Permanent Freeze
vs. Bounded Absorption" — using cross-channel inadmissibility (a
genuinely different mechanism from counting/induction: an extremal argument
showing certain "too-bare" absorbing targets can *never* be realized at
all, which shrinks the space of candidate absorbers a channel could ever
need, rather than bounding how many absorbers occur). This generalizes
Lemma TC (`S=P_1` forces `𝓥_{P_1}={P_1}$, i.e. total freeze at the trivial
value) down to general proper cores, using this round's fan-structural
explorer's `a_1=247` finding (`S={13}`, `S={19}` each freeze permanently at
3 elements, zero collapse events ever, because the "bare" target
`T_{\{13\}}=13^3` can never become admissible once a `{19}`-imprint term
exists).
Skeleton:
  1. Import Channel Assembly Theorem + Channel Splitting Lemma (already
     certified here): FCBC ⟸ `(MRS_S)` for every nonempty `S⊆P_1`; finite
     imprint classes already unconditionally resolved (§D).
  2. **New: Permanent-Inadmissibility Lemma.** If some index `j` exists with
     `rad(a_j)∩C=∅` for a candidate radical `C` (i.e. `C` and `a_j`'s
     radical are disjoint), then no term with radical exactly `C` can ever
     appear at any index `>j` (admissibility against `a_j` alone already
     fails permanently, and admissibility only adds constraints as `n`
     grows — a one-line consequence of the greedy rule's definition, not
     needing FOM). **Certify this in full**, it is elementary and
     unconditional.
  3. **New: Freeze Criterion.** For a proper core `S`, let `j_S` be the
     first index (if any) with `rad(a_{j_S})∩S=∅` witnessing that some
     *other* channel `S'` (disjoint from `S`) is active. If, for **every**
     `C⊋S` with `∏(C)` small enough that `T_C≤a_{j_S}` could conceivably
     matter, `rad(a_{j_S})∩C=∅` also holds (i.e. the same witness blocks
     every "too-bare" extension of `S`), then by the Permanent-
     Inadmissibility Lemma those `C` can never be realized after `j_S`, so
     `𝓥_S` can only contain values realized **before** `j_S` — a *finite*
     prefix of the sequence, automatically bounding `𝓥_S`. **This is the
     approach's open content**: prove that `j_S` always exists (channel `S`
     is not the whole sequence, i.e. some other channel is eventually
     active — true whenever `S≠P_1`, since `P_1`'s other primes must be
     realized somewhere by Lemma P′/pigeonhole, needs a short unconditional
     argument, likely easy) **and** that the blocking condition on "too-bare
     extensions" (not just the single value `T_S` itself, as in the `a_1=
     247` example, but every intermediate `C` with `S⊊C⊊` some richer
     survivor) actually holds in general, not just in the one worked
     example. **Not proved this round** — the `a_1=247` case is a single
     data point; the mechanism must be checked (and will likely fail as
     stated) against cases where the channel does NOT freeze but genuinely
     absorbs (e.g. `a_1=2747`, `S={41}`, which has 8 companions before
     absorbing at `n=163` — here freezing does NOT happen, so the Freeze
     Criterion's hypothesis must fail in that case; verify this explicitly
     as a sanity/consistency check before trusting the mechanism further).
  4. **Dichotomy conclusion (conditional on Step 3 closing in each
     sub-case):** every proper core `S` either satisfies the Freeze
     Criterion (giving `𝓥_S` finite directly, no absorption needed) or does
     not — in the latter case, the approach falls back to needing an
     absorption-count bound (the same open content as the sibling
     approaches; **do not re-derive it here**, just note the fallback and
     hand off).
Key lemmas (claim + mechanism):
  - Permanent-Inadmissibility Lemma — because admissibility is a
    conjunction of ever-more constraints as `n` grows, so any single
    failure is permanent, never revisited by the greedy rule.
  - Freeze Criterion (candidate, open) — because if EVERY potential
    absorbing extension of `S` is already permanently blocked by an
    existing disjoint-imprint witness, no further growth of `𝓥_S` is
    possible after that point, by direct application of the Lemma above.
Open gaps: whether `j_S` exists and blocks *every* relevant `C` (not just
`T_S` itself) is unproved and, per the explicit self-check requested in
Step 3, must be reconciled with `a_1=2747`'s non-freezing `S={41}` example
before being trusted; the non-freezing fallback case still needs the same
absorption-count bound left open by the sibling approaches.
Cases to cover: proper cores that freeze (candidate mechanism above) vs.
proper cores that genuinely absorb (falls back to the shared open gap) —
the builder must determine, for each tested `a_1`, which case a given `S`
falls into, not assume freezing is universal.
Watch out for: the `a_1=247` example is small (`|P_1|=2`, no multi-level
nesting); do not generalize the Freeze Criterion from this one case without
testing it against a nested/deep example (`a_1=21528751`) where it may need
substantial repair or may simply not apply to most channels (most channels
in the hard cases DO absorb rather than freeze, per this round's explorer
data) — be honest if the mechanism turns out to only ever apply to "easy"
channels that were already trivial by other means.

---

intersecting-family-covering-construction: advance (no file changes — top
Elo, complete conditional on the shared gap above)
Target: unchanged — already gives the complete, gap-free "FCBC ⟹ whole
problem, exact, from n=1" derivation (Theorem 5.1). Not revised this round
per explicit dispatch instruction; automatically inherits whichever of the
four approaches above (if any) closes `𝓥_S`-finiteness / `(MRS_S)`, via the
already-certified Theorem V/Theorem CD/Lemma TC/Channel Assembly chain
feeding into its own Theorem 5.1.

build set: persistent-backbone-monovariant, core-depth-induction, imprint-automaton-periodicity, forced-primes-well-ordering
