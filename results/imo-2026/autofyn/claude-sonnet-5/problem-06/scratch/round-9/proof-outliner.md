## imo-2026-06

### Headline judgment call (read first)

Round 9's three explorers, independently, pushed simulation ~100-400x past
round 8's tested range (n up to 1.3M) and found strong, reproducible evidence
that **`(UB_S)`** — the single hypothesis round 8 unconditionally reduced the
*entire* problem to (`theorem-UBS-sufficiency.md`) — is **very likely FALSE**:
companion-bundle size keeps setting new records (ω=8 confirmed for both
`a_1=247` at `n=408816` and `a_1=2747` at `n=374037`, via a reproducible
"primorial-skip-sibling-prime" mechanism) with **zero blocking witness found
in 1.3M terms** even under a targeted search. This is the CLAUDE.md plateau
break, with a *principled reason* (not just round-count): the `(MRS)`
reformulation chosen in round 4 specifically to make FCBC "more tractable" is
itself the thing that's unbounded.

**Critical reframing, not a dead problem.** This does **not** mean FCBC (the
actual remaining gap: does a *fixed finite* prime set `H` hit
`rad(a_i)∩rad(a_j)` for *every* pair, `lemmas/theorem-5.1-master-conditional-
theorem.md`'s hypothesis `(†')`) is false — `(UB_S)`/`(MRS)` was only ever
proved *sufficient* for FCBC (`lemmas/lemma-MS-minimal-radical-stabilization-
sufficiency.md`), never necessary; FCBC does not require bounding an
individual companion bundle's *size*, only that *pairs* share *some* fixed
witness. Indeed, re-reading the round-9 data with this distinction in mind
flips its interpretation: explorer 3's "0/1,300,000 terms have radical
disjoint from `{2,3,5,7,11,13}`" is **direct evidence FOR** a small explicit
covering set (every term, however large its ω, keeps touching the same
handful of small primes) — the "growth" phenomenon is ω(a_n) accumulating
*more* small primes, not switching to fresh large ones. So the right response
per CLAUDE.md's reframe rule is: stop routing more machinery at `(UB_S)`
itself (a proven-likely-false target), and open approaches that attack FCBC
(or the whole problem) through a route that does not require `𝓥_S`/`(MRS)`/
`(UB_S)`-style finiteness at all — while keeping exactly one approach
finishing the job of *rigorously* settling `(UB_S)`'s truth value (a
refutation is real, redirecting content, per round 2/3's precedent).

**Numeric-claim correction flag (for the reviewer, not a proof step):**
`current.md`'s round-8 "max ω(a_n) stays single-digit" claim (`247→6`,
`2747→6`, `21528751→7`) is now a confirmed `N`-too-small artifact — true
values found this round within reach: `247→8` (n=408816), `2747→8`
(n=374037), 21528751 not yet pushed past 7 (needs much larger `N` since its
top-core primes are far bigger). The proof-reviewer should correct this in
`current.md` after this round's builds.

### Field this round (4 approaches: 3 revised, 1 advanced/redirected)

---

explicit-window-backbone-construction: revise
Target: the whole problem (`a_{n+T}=a_n+L` for every `n≥1`), via FCBC
(`(†')`) established **directly**, with no `𝓥_S`/`(MRS)`/`(UB_S)`-style
finiteness claim anywhere in the chain.
Technique: constructive small-explicit-covering-set argument (greedy-
minimality / "cheapest-cover" analysis), combined with the already-certified
Lemma W1 (Key-Lemma-window ⟺ FCBC exactly) and Theorem 5.1 (FCBC ⟹ whole
problem, already gap-free). This is a genuinely different mechanism from
rounds 4-8's pigeonhole/Δ-system/reachability machinery: it never bounds a
bundle's *size*, only asks whether *pairs* share a fixed small witness.
Skeleton:
  1. Fix the finite set `P_1=rad(a_1)`. By the problem's own defining rule
     (taking `i=1` in `gcd(a_{n+1},a_i)>1` for `1≤i≤n`), `rad(a_m)∩P_1≠∅`
     for **every** `m≥2` — free, unconditional (already implicit in Lemma
     P/Lemma FN). This handles every pair `(1,j)` for free but *not* pairs
     among `j,k≥2` with disjoint imprints — that is FCBC's real content.
  2. Candidate explicit `H := P_1 ∪ {2,3,5,7,11,13}` (or, if the builder's
     own stress tests need more, `P_1 ∪ {first B primes}` for a **fixed**,
     `a_1`-independent-in-shape `B` — keep `B` a concrete small constant the
     builder pins down empirically first, then tries to prove suffices).
     This directly formalizes round-9 explorer 3's finding (`0/1.3M` terms
     disjoint from `{2,3,5,7,11,13}`).
  3. **Key Lemma (Small-Uniform-Hit).** For every `m`, `rad(a_m)∩H≠∅`. —
     because the greedy-minimality rule (already-certified Domination
     Lemma + growth bound `a_{n+1}-a_n≤rad(a_1)`, `lemmas/lemma-1-uniform-
     gap-bound.md`) makes reusing an already-recruited *small* prime the
     cheapest way to satisfy the growing number of prior-term constraints;
     round 9's mechanism explorer showed this is not incidental but the
     actual engine producing the observed near-primorial records. This is
     the *individual*-term half of what's needed; **not sufficient alone**.
  4. **Key Lemma (Pairwise Small-Sharing).** For every pair `i<j`,
     `H∩rad(a_i)∩rad(a_j)≠∅` — i.e. not just that each of `a_i,a_j`
     separately touches `H`, but that they touch `H` in the **same**
     element. — because companion bundles are observed (11/11 record
     instances, both tested `a_1`) to be *nested* ("prefix-like": each new
     record bundle is the previous one plus the next unused small prime),
     so any two realized bundles for cores whose imprints intersect share
     their common smaller-prime prefix; for cores with *disjoint* imprints
     (the genuinely hard case — this is exactly why rounds 3-8 built the
     whole `Λ_S`/companion-bundle machinery), the claim is that BOTH
     bundles, being built from the same shared pool of small primes, still
     intersect in that pool with very high structural likelihood — this is
     the one real remaining gap, stated honestly below, not papered over.
  5. Conclude FCBC via Step 4, then invoke the already-certified Theorem
     5.1 (`lemmas/theorem-5.1-master-conditional-theorem.md`) unconditionally
     to finish the whole problem.
Key lemmas (claim + mechanism):
  - Small-Uniform-Hit (Step 3) — because greedy minimality reuses cheap
    small primes to cover many constraints at once (Domination Lemma
    already proves the pigeonhole half; round 9 supplies the empirical
    confirmation this bites in practice, not just in the worst case).
  - Pairwise Small-Sharing (Step 4, the real crux) — conjectured because
    realized companion bundles are empirically *nested* prefixes of the
    ordered prime list (not literally always — round 9 showed one early
    counterexample, `a_1=247, n=2, rad={2,5,13}` skips `3` — so state the
    needed claim as the WEAKER "eventually, for `n` large, any two
    realized bundles of size ≥2 share a prime ≤ some fixed bound," not the
    stronger literal nesting invariant, and flag this explicitly as the
    open gap for the builder).
Open gaps: Step 4 (Pairwise Small-Sharing) is the sole open gap — everything
else (Steps 1,2,3,5) is either free or an empirical/structural claim with a
named mechanism. The builder must either (a) prove Pairwise Small-Sharing
for a concrete, `a_1`-computable `H`, possibly by strengthening `H` with a
finite, explicitly-constructed extra set of "bridge primes" (one per pair of
disjoint proper cores, of which there are only finitely many — at most
`2^{|P_1|}` — so this is a FINITE, not open-ended, patch), or (b) find and
report a genuine counterexample (two disjoint-core realized bundles sharing
no prime ≤ any tested bound), which would itself be valuable negative
content.
Cases to cover: pairs within the same core (imprint intersects — easy, Step
1-style); pairs across genuinely disjoint proper cores (the hard case, Step
4); pairs involving the top core `I_{P_1}` (free, `P_1⊆H`).
Watch out for: do NOT resurrect the literal "prefix-closure for every term"
invariant as if proven — round 9's own data (`a_1=247,n=2`) already refutes
the strongest form; use only the weaker eventual/bounded-bridge version.
Do NOT confuse "every term individually touches `H`" (Step 3, easy) with
"every *pair* shares the *same* `H`-element" (Step 4, hard) — this exact
conflation is the trap this file's skeleton is written to avoid.

---

sunflower-bundle-closure: revise
Target: the whole problem, via rigorously **settling** `(UB_S)`'s truth
value (not just attempting to prove it, as this file's round-8 build did) —
per dispatch's explicit sanctioning, either direction is valuable content;
the round-9 evidence strongly favors attempting the FALSE direction.
Technique: a classical analytic-number-theory density argument — Landau's
theorem (Hardy–Ramanujan-type asymptotic) on the density of integers with a
bounded number of distinct prime factors — combined with this workspace's
own certified linear growth bound (Lemma 1) to derive a contradiction from
`(UB_S)`. This is a genuinely new tool for this workspace (not a repeat of
the count-bounding pigeonhole/Δ-system machinery already exhausted rounds
6-8; confirmed absent from both `knowledge_base.md` and the crux corpus by
this round's dedicated search, so it must be stated and proved from
elementary first principles, not cited as a KB entry).
Skeleton:
  1. Suppose, for contradiction, `(UB_S)` holds for **every** proper core
     `S⊊P_1`: there is a uniform bound `B` with `ω(a_n)≤B` for every
     `n∉I_{P_1}` (finitely many proper cores, `≤2^{|P_1|}-2`, so a uniform
     bound follows from the per-core bounds by taking the max — an easy,
     unconditional step).
  2. **Growth Lemma (already certified, reuse, do not re-prove):**
     `a_n≤a_1+(n-1)·rad(a_1)` for every `n` (`lemmas/lemma-1-uniform-gap-
     bound.md`). So `{a_n:n≤N}⊆[a_1,a_1+(N-1)D]`, `D:=rad(a_1)` fixed —
     `N` distinct integers packed into an interval of length `O(N)`.
  3. **Density Sub-Lemma (needs proof, the real new content):**
     `|I_{P_1}∩[1,N]| = o(N)` as `N→∞` — i.e. the top-core class does not
     have density 1. — because if it did, then (using the already-certified
     Escape-Confinement/companion-bundle machinery) every `a_n` beyond some
     point would be divisible by *all* of `P_1` simultaneously, but this
     workspace has already certified (rounds 3-8, e.g. the Permanent
     Bundle Lemma) the existence of infinitely many indices with **proper**
     imprint for every hard `a_1` tested — so `|I_{P_1}^c∩[1,N]|→∞`; the
     builder needs the *rate*, not just infinitude — likely obtainable from
     the certified `Λ_S`-Reduction/companion-bundle apparatus directly
     (e.g. showing `I_{P_1}^c` has density bounded below by some explicit
     positive or slowly-decaying function), or via a direct combinatorial
     argument using the greedy rule's own local structure.
  4. **Landau/Hardy–Ramanujan Count Lemma (state, prove from elementary
     first principles — sieve/Mertens induction on `k`, do not just cite):**
     for fixed `k`, `|\{m≤X : ω(m)≤k\}| = o(X)` as `X→∞`. — because an
     inductive Mertens-based sieve argument (Σ_{p≤X}1/p→∞, a fact already
     informally used by this workspace's `(GW)`-rejection reasoning, round
     7 Rules) shows the density of `k`-almost-prime-support integers among
     `[1,X]` vanishes; this is classical (Landau 1900) but must be proved
     here from scratch per the rigor rules since it is confirmed absent
     from `knowledge_base.md`/the crux corpus (this round's dedicated
     search).
  5. **Contradiction.** By Step 1, all `N-o(N)` (Step 3) values `a_n` with
     `n∉I_{P_1}` satisfy `ω(a_n)≤B`; by Step 2 they lie in an interval of
     length `O(N)`; by Step 4 (applied with `X=O(N)`, `k=B`) at most `o(N)`
     integers in that interval have `ω≤B`. So `N-o(N)≤o(N)`, i.e.
     `N=o(N)` — contradiction. Hence `(UB_S)` is **false**: for every `B`,
     infinitely many `n∉I_{P_1}` have `ω(a_n)>B`.
  6. **Honest scope note (must appear in the built file):** this refutes
     the round-8 sufficient hypothesis, not the whole problem. Combined
     with `theorem-UBS-sufficiency.md` this shows that theorem's hypothesis
     is not a viable route — future rounds should not spend further effort
     trying to *prove* `(UB_S)`/`(MRS)`/`𝓥_S`-finiteness for any proper
     core; FCBC itself (strictly weaker, per Lemma W1) remains the target,
     to be attacked by the sibling approaches this round.
Key lemmas (claim + mechanism):
  - Density Sub-Lemma (Step 3) — because infinitely many proper-imprint
    indices are already certified to exist; the rate/positivity of their
    density is the concrete open sub-gap.
  - Landau Count Lemma (Step 4) — because Mertens' Σ1/p divergence, applied
    inductively over the (at most `k`) prime "slots" of a bounded-ω
    integer, forces the count of such integers up to `X` to be `o(X)` (the
    classical mechanism: fixing which `≤k` primes divide `m` and summing
    `1/(p_1⋯p_j)`-type series via Mertens gives a vanishing proportion).
Open gaps: Step 3's explicit rate (infinitude of `I_{P_1}^c` is already
implicit in certified content; the *density rate* needs an explicit
argument) and Step 4's from-scratch elementary proof (classical but not
yet written down in this workspace) are the two concrete remaining tasks.
Cases to cover: none (a direct, non-casework contradiction argument) beyond
verifying Step 1's "max of finitely many per-core bounds" step is airtight.
Watch out for: do not conflate `o(N)` with "zero" — Step 5's contradiction
needs only that the density-3 lower bound *beats* the density-4 upper
bound asymptotically, not any exact count; get the quantifiers right (Step
3 needs a LOWER bound on `|I_{P_1}^c|`, Step 4 needs an UPPER bound on
bounded-ω integers — do not accidentally prove the wrong-direction
inequality, a documented risk pattern in this workspace, e.g. round 2's
`H_n` mixup).

---

intersecting-family-covering-construction: advance (redirected)
Target: the whole problem — this file already has Theorem 5.1 (FCBC ⟹
periodicity from `n=1` exactly) fully certified and gap-free; this round
redirects its remaining open content from "wait for FCBC" to **directly
attacking FCBC itself**, using its OWN Universal Hitting Lemma A machinery
as a genuinely different, third, independent technique from the other two
FCBC-attacking approaches this round (necessity-driven rather than
constructive-density-driven).
Technique: necessity/witness-extraction — use Lemma A's proof pattern
(applying `(†')`'s *unrestricted* quantifier) in reverse: instead of
assuming `H` exists and deriving structure, directly construct a candidate
`H` by taking, for each of the finitely many pairs of proper cores
`(S,S')` with `S∩S'=∅`, the (conjecturally finite, by round-9's own
"nested small-prime bundle" data) set of primes that have EVER served as a
common witness for an `(S,S')`-cross pair in the data explored so far, and
prove this candidate set is already complete (no further growth) by a
finite-verification/stabilization argument distinct from `(UB_S)`.
Skeleton:
  1. Reuse Theorem CD (core decomposition, already certified,
     `lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`): every index
     `n` has a well-defined core `S(n)⊆P_1`, only `≤2^{|P_1|}` possible
     cores.
  2. For each of the finitely many **unordered pairs of distinct cores**
     `(S,S')` (including `S=S'`), define
     `W_{S,S'} := ⋃_{i∈I_S,j∈I_{S'},i<j} (rad(a_i)∩rad(a_j))` restricted to
     primes ∉`P_1` (the "cross-witness pool" for that pair of classes).
  3. **Stabilization Conjecture (the real new content, distinct from
     `(UB_S)`):** each `W_{S,S'}` is eventually "witness-complete" — i.e.
     there is a *finite* subset `W_{S,S'}^0⊆W_{S,S'}` such that every pair
     `(i,j)`, `i∈I_S,j∈I_{S'}`, has `rad(a_i)∩rad(a_j)∩W_{S,S'}^0≠∅` — even
     if `W_{S,S'}` itself (the union over ALL pairs) is infinite. This is
     explicitly **not** the same claim as `(UB_S)` (which bounds a single
     bundle's size); it only asks that a finite *subset* of ever-used
     cross-witnesses already suffices for *coverage*, which is compatible
     with individual bundles growing unboundedly (a growing bundle can
     still always contain one fixed small witness, exactly as round 9's
     "0/1.3M avoid `{2,3,5,7,11,13}`" data suggests).
  4. `H := P_1 ∪ ⋃_{S,S'} W_{S,S'}^0` (finite union of finite sets) is then
     a covering set, closing FCBC; invoke Theorem 5.1.
Key lemmas (claim + mechanism):
  - Stabilization Conjecture (Step 3) — because the empirical companion
    data (round 9, all 4 tested `a_1`) shows cross-core witnesses are
    always small (drawn from the same shared pool `{2,3,5,7,11,13,...}`
    that individual bundles also draw from), suggesting the *set of primes
    ever used as cross-witnesses* saturates early even though the
    *individual bundle sizes* keep growing — these are different
    quantities and only the former is needed here.
Open gaps: Step 3 in full — this is the same underlying difficulty as
explicit-window-backbone-construction's Step 4 (Pairwise Small-Sharing),
approached via a different route (witness-pool stabilization vs.
prefix-nesting); the two builders should cross-check whether their
candidate `H`s coincide (round 4 found exactly this kind of convergence
across independently-constructed candidate sets) but should NOT be merged
into one slug — they are genuinely different techniques for the same
target.
Cases to cover: `S=S'` (same-core pairs, likely easy/already handled by
existing companion-bundle machinery); `S,S'` both proper and disjoint (hard
case); either involving the top core (free, via `P_1`).
Watch out for: do not silently reintroduce `(UB_S)` through the back door
by requiring `W_{S,S'}^0` to contain *every* prime that ever appears in a
class-`S` bundle — it only needs ONE per pair, a much weaker requirement.

---

forced-primes-well-ordering: revise
Target: the whole problem, via FCBC directly, using the file's own already-
certified `S^+` necessity machinery (`S^+_S:=⋂_{i∈I_S}rad(a_i)`, proved
necessary and — conditional on `I_S` infinite — finite,
`lemmas/lemma-freeze-confinement-domination-and-Splus.md`) as the seed for
an explicit covering set, **abandoning** the `S^{++}`
sufficiency-via-pure-intersection direction (already rigorously refuted,
Vacuity/Intersection-Fragility Propositions — do not revisit that specific
mechanism).
Technique: seeded construction — `S^+_S` alone is proved insufficient
(refuted on `a_1=21528751,S={1061}`, missing prime `11`), but `11` is a
*small* prime; the new idea is that the deficiency is always repairable by
a bounded, `a_1`-independent-in-size patch of small primes, not by
re-attempting pure intersection.
Skeleton:
  1. For each proper core `S` with `I_S` infinite, `S^+_S` is finite
     (already certified). Candidate `H_S := S^+_S ∪ \{2,3,5,7,11,13\}`
     (same small-prime patch as explicit-window-backbone-construction's
     Step 2, reused deliberately — a shared candidate, not independently
     guessed, so if either builder refutes it with a counterexample both
     files should be updated together per the shared-prerequisite Rule).
  2. **Patch Sufficiency Claim:** for every `i∈I_S`,
     `rad(a_i)∩H_S≠∅` beyond `S^+_S` failing alone — re-verify directly on
     the `a_1=21528751,S={1061}` counterexample (`11∈\{2,3,5,7,11,13\}`,
     so this specific known failure is already repaired by construction;
     the builder must check this is not a coincidence by testing at least
     2 more of this file's own documented `S^+`-failure instances).
  3. Extend to the **pairwise** requirement (`H_S∩rad(a_i)∩rad(a_j)≠∅` for
     `i,j∈I_S`) using the same nesting/shared-pool argument as sibling
     approaches — flag as shared open content, do not re-derive from
     scratch if explicit-window-backbone-construction's Step 4 closes it
     first (cite, don't duplicate).
  4. `H := P_1 ∪ ⋃_S H_S` (finite union over finitely many proper cores)
     is the final candidate; invoke Theorem 5.1.
Key lemmas (claim + mechanism):
  - Patch Sufficiency Claim (Step 2) — because the one documented `S^+`
    failure (missing prime `11`) is itself small, suggesting the gap
    between "necessary primes" and "sufficient primes" is always a small-
    prime patch, not an unboundedly-growing one — this is a genuinely
    testable, falsifiable claim the builder should stress-test on all of
    this file's own prior `S^+`-failure examples before trusting it.
Open gaps: Step 2 (is the patch always small, and always the *same* fixed
patch across every core/`a_1`?) and Step 3 (pairwise, shared with sibling
approaches). If Step 2 fails (a documented `S^+`-gap needing an
arbitrarily large patch found), that would itself be valuable evidence
FCBC's route also needs unbounded machinery — report either outcome
honestly.
Cases to cover: `I_S` finite (already handled elsewhere, `Λ_S`-Reduction
Lemma) vs. infinite (the case this skeleton addresses).
Watch out for: do not re-derive the already-refuted `S^{++}` mechanism
under a new name — this skeleton's `H_S` is a *fixed small patch*, not an
attempt to recover missing primes via further intersection, which is the
specific thing proven impossible (Vacuity/Intersection-Fragility
Propositions).

---

### Not advanced this round (still live, not dropped)

persistent-backbone-monovariant — its remaining hypothesis (NIBC) is a
narrower, weaker descendant within the same `(UB_S)`/`(MRS)` family this
round's finding casts doubt on; per CLAUDE.md's "a refuted framing makes its
same-framing siblings suspect too," redirecting builder effort away from it
this round rather than advancing it further. Not dead — keep in the
population; revisit if the FCBC-direct approaches above stall and a fresh
angle on bundle-count (not size) becomes relevant again.

core-depth-induction, global-recruiter-finiteness, backbone-existence-crt,
bounded-gap-density-covering — unchanged from prior rounds' verdicts
(Step-3 dead / RETHINK / parked); no new content this round bears on them.
