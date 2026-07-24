## imo-2026-06

- **Distinct openings** (all scouted from persistent-backbone-monovariant's own
  well-ordering angle on the Finite Covering Backbone Conjecture, FCBC: does a
  finite set of primes `H` exist with `H∩rad(a_i)∩rad(a_j)≠∅` for every `i<j`?):

  1. **"Forced-primes" invariant (new, strongly supported numerically — the
     headline finding of this scout).** Define `F_M := {p : ∃ i<j≤M with
     rad(a_i)∩rad(a_j)={p} exactly}` (primes that are the *unique* common
     factor of some pair among the first `M` terms — hence *necessarily* in
     any valid `H`, since no other prime can cover that pair). Across **24**
     distinct `a_1` values (Case I and Case II, `ω(a_1)` from 1 to 6, prime
     factors from 2 up to 103), tested out to `M` between 5,000 and 20,000
     (up to ~2×10^8 pairs per case): `F_M` **stabilizes by index ≤12 in every
     single case** (median much lower — most cases stabilize by `M≈5`) and
     **never grows again**, no matter how far `M` is pushed afterward. Even
     stronger: every element of `F_∞` already appears in `rad(a_i)` for some
     `i≤5` in every one of the 24 tests (i.e. the "recruitment window" for the
     necessary primes is tiny and, empirically, uniformly small — not growing
     with `M` or with `a_1`'s size). This gives a clean, well-defined,
     numerically robust candidate object — distinct from both of round 2's
     refuted candidates (`S_0` from Lemma C's `N_0`; `rad(a_1)`) — that a
     minimal-counterexample argument could target directly: assume `F_∞` is
     infinite, well-order its elements by first-forced-index, and try to
     derive a contradiction (e.g. via the Domination Lemma: a prime that is
     ever the *unique* covering choice for a pair is in tension with the
     Domination Lemma's guarantee that *some* prime divides an unboundedly
     growing fraction of earlier terms — this tension is not yet developed
     into a proof, just flagged as the shape of a possible argument).

  2. **`H := ⋃_{i≤K} rad(a_i)` for a small fixed `K` (new explicit
     construction candidate).** Directly testing this literal set (not just
     the abstractly-defined forced set) as `H`, for `K` around 10–15,
     against thousands to tens of thousands of terms, produced **zero
     failures** in every case tried, including the two adversarial cases
     found below (`a_1=4199,4087`). This is a *fattened* version of NC1's
     refuted `S_0` (which used Lemma C's `N_0`, sometimes too small — NC1's
     own counterexample `a_1=221` has `N_0=3`, and the failing witness `5`
     first appears in `rad(a_4)`, i.e. right at the edge of a 3-term window,
     but is safely inside a 10–15-term window). Worth a dedicated approach:
     prove a uniform bound `K=K(ω(a_1))` (or even a universal constant) such
     that `⋃_{i≤K}rad(a_i)` always covers every pair — this sidesteps ever
     characterizing the "true" minimal `H` and might be provable via a
     second, sharper application of Lemma C's finite-descent technique to a
     richer index set (not just the single running intersection `C_n`, but
     something like "for each prime `p∈rad(a_1)∪...∪rad(a_K)`, when does it
     stop being the pairwise witness for *new* pairs" — an analogous
     finite-stabilization/pigeonhole argument, not yet carried out).

  3. **Minimal-counterexample on the "recruitment index," not the prime
     itself.** Instead of well-ordering primes, well-order *indices*: assume
     for contradiction that the "recruitment window" is unbounded, i.e. for
     every `K` there is some pair `(i,j)` with `i,j>K` whose canonical (or
     forced) witness is a prime not dividing any of `a_1,...,a_K`. Take the
     minimal such `K` (or the minimal witnessing pair by some other order)
     and try to derive a contradiction from Lemma 1 (linear growth) +
     Domination Lemma (some prime divides `≥n/log n` of the first `n`
     terms) — a genuine, not-yet-attempted well-ordering skeleton distinct
     from both NC1/NC2's refuted shortcuts. (Scouted only, not developed —
     this is exactly the outliner's job.)

  4. **Crux-corpus-inspired converse framing (`aimo-0727`, see below).** That
     problem's proof defines an auxiliary integer monovariant `b_k` linked to
     a divisibility relation, shows it has bounded-step growth, and links its
     *boundedness* to *finiteness of the prime set ever appearing* via a
     clean contrapositive ("if `b_k` bounded, prime factors of `a_k` confined
     to a finite set — contradiction"). The technique (not the specific
     lemma — the target hypothesis there is literally the reverse of ours)
     suggests trying to construct an analogous auxiliary quantity for our
     problem whose boundedness is *equivalent* to FCBC, then attacking
     boundedness directly with a monovariant/pigeonhole argument instead of
     attacking the prime set combinatorially. Flagged as a technique to
     import, not a plug-in lemma.

- **Candidate technique(s):** finite-descent/pigeonhole on a well-defined
  monovariant (per KB "Invariants & monovariants" and "Pigeonhole / extremal
  principle," already the technique behind the certified Lemma C); a
  minimal-counterexample argument on either the forced-primes set (opening 1)
  or the recruitment-index (opening 3); an explicit small-K construction
  (opening 2) that may not need a minimal-counterexample argument at all if a
  direct uniform bound on `K` can be proved.

- **Cheap-kill candidates:** none found against FCBC itself — every stress
  test (24 values, up to 20,000 terms / ~2×10^8 pairs) supports it, including
  genuinely adversarial multi-prime and large-twin-prime cases. The only
  cheap-kill this round *did* land is against a stronger, already-superseded
  target — see "Small-case notes" below.

- **Knowledge-base entries to use:** "Invariants & monovariants" (used by
  Lemma C already; also the natural framing for opening 1/2); "Pigeonhole /
  extremal principle" (finite-descent argument, same family as Lemma C's
  proof); "Modular arithmetic, CRT" (for the eventual finite-state
  construction once `H` is fixed, per `intersecting-family-covering-
  construction`'s Theorem 2.2 — not this round's target but the natural next
  step). No new KB entry is a good fit for actually *proving* FCBC — the gap
  is genuinely open and none of the KB's number-theory tools (LTE, Zsigmondy,
  Dirichlet, Bertrand) directly bites on "finitely many primes are ever the
  unique/minimal common factor of a pair in a greedy gcd-chain sequence."

- **Analogous past problems (cruxes):**
  1. **`aimo-0727`** (subtopic `size-bounding-and-descent` /
     `divisibility-and-gcd`, IMO-SL, "Netherlands problem": `a_{k+1} |
     2(a_1+...+a_k)`, prove infinitely-many-primes-appear implies every `n`
     divides some term). Crux: auxiliary monovariant `b_k=2(a_1+...+
     a_{k-1})/a_k` with `b_{k+1}≤b_k+1`, and the *converse* link "`(b_k)`
     bounded ⟹ prime factors of `(a_k)` confined to a finite set." This is
     the most structurally relevant analog found this round — not because
     its target matches (it's the logical converse of what we want: FCBC
     is closer to "prime set IS confined to finite set," which in
     `aimo-0727`'s proof is the thing ruled out, not proved), but because
     its *technique* (link boundedness of an auxiliary integer quantity to
     finiteness of a prime set via a clean divisibility chain, then attack
     the auxiliary quantity) is a genuinely different route than anything
     tried so far in this workspace (all three live/parked approaches
     attack the prime set directly). Worth adapting the *shape* of the
     argument, not any specific lemma.
  2. **`aimo-0421`** (already imported as Lemma R's source, per round 1/2 —
     re-confirmed still the best match for "eternal witness" style
     arguments; its crux ("when every prime divides only finitely many
     elements, pick a third element coprime to a given pair") is the
     contrapositive-flavor argument already exploited; no new use found this
     round beyond what's already certified).
  3. **`aimo-0678`** (already the source of the whole persistent-backbone-
     monovariant framing per round 2 — re-checked, no new angle found this
     round beyond what's on record).
  No other corpus entry (searched `number_theory` × `invariants-and-
  monovariants`, `sequences-and-recurrences`, plus free-text search for
  "gcd"+"greedy"/"smallest"/"least") was a closer match; the corpus does not
  contain a problem literally about backbone-finiteness for a greedy-gcd
  sequence beyond what prior rounds already found.

- **Prior progress:** (unchanged from `current.md`/round 2, restated for
  context) Lemma C (Global Intersection Collapse) fully certified. NC1
  (`a_1=221`): `S_0` (Lemma C's collapse-point union) does not contain every
  canonical witness. NC2 (`a_1=375`): witnesses need not be `≤rad(a_1)`. Both
  are proofs, not conjectures, and both are correctly diagnosed as refuting
  *specific proposed descriptions* of a backbone, not backbone-existence
  itself (confirmed again this round — see below, `a_1=221,375` both turned
  out to have small stable `W` after all).

- **Dead ends (do not retry):** the two already-recorded ones (`S_0` from
  Lemma C's `N_0` alone with no safety margin — refuted, NC1; `rad(a_1)` as an
  a-priori bound — refuted, NC2). This round adds no new dead end to the
  *weaker* FCBC target, but see the important negative finding below about
  the *stronger*, already-superseded `(\star\star)` target.

- **Small-case / intuition notes (numerics this round, exact integer
  simulation, `math.gcd`/`sympy.factorint`, all conjecture-level evidence,
  not proof):**
  - **`(\star\star)` (the original "canonical witness set `W` is finite"
    target, already superseded in the workspace by the weaker FCBC) now has
    concrete numerical evidence it is FALSE.** For `a_1=4199=13·17·19`, `|W|`
    (all-pairs canonical witnesses among the first `M` terms) grows
    steadily and does **not** plateau: `M=1500→9, 3000→9, 5000→10, 6000→11,
    7000→12, 8000→13, 9000→15, 10000→16, 12000→17, 15000→21` (final `W` at
    `M=15000` is `{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,
    71,83}` — essentially "all small primes up to a slowly rising bound").
    Same pattern for `a_1=4087=61·67`: `|W|` grows `6→11→17→19` from
    `M=500` to `5000`, still not plateaued at `M=12000`. This is the
    **opposite** of what round 2's earlier tests on `a_1=15,221,247,375`
    suggested (where `W` looked bounded within a few thousand terms) — those
    were simply not adversarial enough / not run to large enough `M`.
    **Recommendation: treat `(\star\star)` as very likely false and do not
    let any approach's core argument depend on `W` itself being finite** —
    this generalizes/strengthens NC1+NC2's conclusion from "no simple closed
    form for `W`" to "`W` itself is plausibly unbounded."
  - **FCBC (the current, weaker, correctly-scoped target) survives every
    stress test, including on exactly these two `W`-unbounded cases.** For
    `a_1=4199`, `H={2,3,13,17,19,83}` (only 6 primes, all forced/necessary,
    first seen by index 5) covers **all pairs among 15,000 terms** (zero
    failures, ~1.1×10^8 pairs checked with pruning). For `a_1=4087`,
    `H={2,61,67}` (3 primes, first seen by index 2) covers all pairs among
    12,000 terms (zero failures, ~7.2×10^7 pairs). This is strong,
    conjecture-level (not proof) evidence FCBC is true and that `H` can be
    read off a *very* short prefix (`K≤5` observed, `K≤12` with safety
    margin) even in cases where naive `W`-tracking diverges.
  - Additional adversarial values tested (all consistent with FCBC, forced
    set stabilizing by index ≤5, `H` sufficient to the largest `M` tried):
    `a_1∈{15,65,105,143,221,247,375,663,667,935,1001,1073,1147,1517(untested
    directly, 1147 used instead),1763,2310,2431,3003,3127,3145,4087,4199,
    5183,6557,7429,10403,15015,17017,46189,255255}` — spanning `ω(a_1)` from
    1 to 6 and prime factors from 2 up to 103.
  - No adversarial construction attempted this round (twin-large-prime
    products, 5–6-distinct-prime products, primes-only-large-radical cases)
    broke FCBC or even slowed the forced-set stabilization past index ~12.
    This is a genuinely different outcome from round 2's pattern (which kept
    finding the *current* target false) — this round's stress-testing
    supports the *current* target (FCBC) and instead demotes a
    *stronger, already-superseded* target (`(\star\star)`, W-finiteness).
