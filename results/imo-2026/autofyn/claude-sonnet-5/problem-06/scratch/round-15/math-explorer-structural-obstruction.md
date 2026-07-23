## imo-2026-06

**IMPORTANT CROSS-REFERENCE (read this before the "stuck channels" claims
below):** a parallel round-15 explorer (`/tmp/round-15/math-explorer-
alternative-mechanism.md`) found (a) a very strong crux-corpus match
(`aimo-0030`, IMO-SL 2013 N5) that may give a full general proof bypassing
this whole apparatus, and (b) a "Common-Recruiter Reuse" argument that
applies the SAME 4 witnesses already on file (not Corollary MSF's stricter
subset-match requirement, just direct repeated application of Lemma WF) to
close **5 of a_1=21528751's 6 channels** — including `(\{103\},\{1061\})`
and `(\{197\},\{1061\})`, which I (below) mistakenly flagged as "stuck"
using the narrower Corollary-MSF-specific lens. **Correction/reconciliation:**
my "stuck" finding for those two channels is an artifact of checking only
the stricter Corollary MSF mechanism (needs a subset match comp(a_j0)⊆P);
the more general direct Lemma WF application the other explorer used does
NOT need that — it only needs comp(a_k) to intersect the recruiting witness's
companion set for every k, which is satisfied unconditionally. **Treat my
"stuck: ({103},{1061}) and ({1061},{103,197})" framing below as SUPERSEDED
for the first of those two pairs by the other explorer's finding; only the
6th channel, `(\{1061\},\{103,197\})`, is confirmed genuinely still open by
both explorers independently** (I via the "prime 11 never a singleton"
diagnosis, they via "core `\{103,197\}` isn't disjoint from either
recruiting core, so Lemma WF can't be aimed at it that way" — two
independent, consistent diagnoses of the same real obstruction). My own
computational data below (the exact companion-floor tracking, the
singleton-prime census, the exact-floor-recurrence finding) remains valid
and gives additional mechanistic detail for WHY this last channel resists,
complementary to their diagnosis.

- Distinct openings (this lens's contribution — a structural/numerical dissection
  of WHY a_1=21528751, class S={197} resists small-companion witnesses, and
  whether that resistance is a real obstruction or an artifact of under-search):
  1. **The "Small-Companion Existence" framing was already correctly diagnosed
     as the wrong target by round 14's builder** (witness-chaining-universal-
     existence.md) — this round's data reconfirms and sharpens that diagnosis
     with a much deeper search (250,000 terms vs. round 14's 509/136), and adds
     a NEW, more precise characterization of what actually matters: not
     "|comp|<=2" but "does the resistant class ever achieve comp EXACTLY equal
     to (a subset of) its own permanent floor, using ONLY primes that recur
     elsewhere as singleton companions."
  2. **New finding: the resistance is driven by a genuine, apparently-permanent
     per-class "companion floor" (F_S := intersection of comp(a_k) over ALL
     realized k in I_S), not a slowly-shrinking quantity.** For a_1=21528751,
     F_{197}={2,3,7} has been frozen since index 62 (out of 39944 later
     members, all identical) and, pushed this round to N=250,000 (max value
     ~57M, 4237 members of I_197, 8x deeper than round 14's 509-member check),
     remains EXACTLY {2,3,7} with ZERO exceptions and NO downward trend. This
     is a MUCH longer unbroken plateau (4237 members / index-span ~39882 to
     ~250,000) than the workspace's own documented "plateau that later breaks"
     counterexamples (Theorem TLL-Refuted, round 13: 24-member and 108-member
     plateaus for a_1=4199, later confirmed to break) — 40-170x longer by
     member count. This is suggestive of genuine permanence but, per the
     round-9 "100-1000x before trusting" rule and the round-13 precedent, NOT
     proof: a longer plateau is evidence, not certainty.
  3. **New finding: the resistant class DOES regularly achieve its floor
     EXACTLY (no extra incidental primes)** — 10 members of I_197 (out of
     4237, roughly evenly spaced across the whole range) have comp EXACTLY
     {2,3,7}, not just comp ⊇ {2,3,7}. This exact-floor recurrence (not a
     one-off) is precisely what Corollary MSF's j_0 witness needs (comp(a_j0)
     ⊆ P) — and explains, mechanically, WHY the already-proven 21528751
     closure of ({197},{103}) worked despite the "0% small companion" negative
     signal: Corollary MSF never needed |comp| small, only comp ⊆ P for some
     P built from the OTHER side's singletons, and P ended up being exactly
     the floor {2,3,7}, achieved exactly by a_2575 (and 9 other members).
  4. **New, sharper finding — a genuine three-way split among a_1=21528751's
     6 disjoint core-pair channels, computed fresh at N=250,000 for ALL 6, not
     just the closed one:**
     - **"Easy" (data-supports-closure-now):** ({103},{197,1061}) and
       ({197},{103,1061}) — both sides here have either abundant singletons
       (I_103, I_{103,197}, I_{103,1061} all produce singleton witnesses with
       primes EXACTLY {2,3,7}: I_103 has 10 singletons, I_{103,197} has 8,
       I_{103,1061} has 7) or a resistant side that regularly achieves its
       floor exactly using those same 3 primes (I_197 as above; I_{197,1061}
       — only 4 members total even at N=250,000 — has 3/4 members with comp
       EXACTLY {2,3,7}, the 4th {2,3,5,7}). These look closable by the SAME
       Corollary MSF mechanism already used for ({103},{197}).
     - **"Stuck with current data" (genuinely different obstruction, NOT the
       same as the already-refuted "small companion" framing):** ({103},{1061})
       and ({1061},{103,197}) — both involve core {1061}. I_1061's TRUE
       floor is {2,3,7,**11**} (size 4, not 3 as a shallower check suggested —
       every one of its 74 realized members (to N=250,000) contains at least
       one of {11} or the rarer pair {5,97}; NONE has comp ⊆ {2,3,7}). The
       blocking fact: **prime 11 (or a suitable alternative) has NEVER once
       appeared as anyone's singleton companion anywhere in the whole sequence
       to N=250,000** — a direct count over all 250,000 terms found singleton
       companions ONLY for {2 (13x), 3 (8x), 7 (5x)}, zero for any other
       prime including 11. Corollary MSF as literally stated cannot close
       these two channels with currently-available witnesses (no way to build
       a P ⊇ {2,3,7,11} from independent singletons). This is a genuinely
       different, sharper obstruction than the "resistant class has few
       small companions" framing round 14 already retired — it's about
       WHICH primes are ever available as singletons, not how small the
       resistant side's companions get.
     - **"Genuinely hardest" (no mechanism applies at all yet):** ({197},{1061})
       — NEITHER side has ever produced a singleton companion anywhere in the
       observed range (I_197: 0/4237; I_1061: 0/74). Corollary MSF's
       hypothesis (>=1 singleton witness on ONE side) is not even close to
       satisfied for this specific pair with current data. This channel would
       need the heavier, already-certified but not-yet-applied-here Chaining
       Sufficiency Theorem / FW1-FW2-style multi-prime disjunctive case-split
       (both sides contribute multi-element companion sets, combined via a
       finite Boolean case analysis) rather than the "zero case-split" MSF
       shortcut.
  5. **Cross-check against a_1=4199 shows the "restricted-primes" phenomenon is
     NOT universal — it looks like an idiosyncrasy of a_1=21528751, not a
     generic law.** For a_1=4199, singleton companions appear for a much
     richer set of primes: {2 (104x), 3 (30x), 5 (6x), 7 (5x), 11 (4x)}, then
     EVERY prime from 23 up to 181 appears exactly once as a singleton
     (consistent with the workspace's already-documented "primorial skipping
     one core prime" extremal record structure, round 9). This means
     a_1=21528751's failure to ever produce an 11-singleton (in 250,000 terms)
     is very plausibly just an unlucky/slow-converging under-search — NOT
     evidence of a hard mathematical block on prime 11 ever appearing — and a
     deeper search (or a smarter targeted search for "smallest number with
     core X and comp={11}") could plausibly find one. I attempted to push the
     search past N=500,000 for 21528751 but hit a timeout (sympy-factorint
     fallback beyond the sieve limit is too slow at this scale) — this is an
     unresolved practical/computational limitation, not a mathematical
     finding; a future round with a faster large-N generator (bigger sieve,
     or targeted factorization only on admissible-candidate boundary numbers)
     could push this further.
  6. **Which prime a class DOES/doesn't produce as a singleton does NOT
     correlate with simple algebraic invariants of a_1 tested here** — neither
     "smallest prime of P_1" (a_1=4199's generous singleton-rich class is
     I_17, the MIDDLE prime, not I_13 the smallest) nor raw class population
     alone determines it in a simple closed form (though population size does
     correlate directionally: the numerically largest class in both tested
     a_1 — I_103 for 21528751, I_17 for 4199 — is the one that produces
     singletons; this is a useful empirical heuristic, not a proof, and its
     generality across more a_1 is untested this round due to time).

- Candidate technique(s): the toolkit already in the workspace (Corollary MSF
  for the "easy" channels; the full Chaining Sufficiency Theorem/FW1-FW2-style
  multi-witness disjunctive case-split for the "stuck"/"hardest" channels) is
  the right toolkit — no new technique needed. What's needed is (a) either a
  generalization of Corollary MSF that allows the "generous" side's witnesses
  to be non-singleton pairs/triples combined via a finite disjunctive
  case-split (to reach primes like 11 that never appear alone but might
  appear paired, e.g. comp={2,11} or {3,11}), or (b) a genuinely new existence
  argument for why the specific prime(s) a resistant class's floor needs
  MUST eventually appear as an independent witness somewhere (this is exactly
  the open "Bounded Forced-Set Existence Conjecture" from round 14, now with
  much sharper, more concrete failure data to test against).

- Cheap-kill candidates: none new this round for the whole-problem gap. But
  one useful narrow cheap-kill for future rounds: before attempting a full
  general proof of "Bounded Forced-Set Existence," check whether the specific
  primes needed to complete a resistant class's floor (computed directly, as
  above) EVER appear as singletons ANYWHERE in a much larger computational
  search (not just in the specific complementary class) — this is a cheap
  (single pass over the generated sequence) way to triage which of the "6
  channels" style splits are likely tractable now vs. need a genuinely
  different mechanism, before spending builder effort.

- Knowledge-base entries to use: none new beyond what's already cited by the
  live approaches (Lemma WF, Lemma NIDF(a), Theorem CD, Chaining Sufficiency
  Theorem, Corollary MSF) — this exploration is purely computational/
  diagnostic, no new KB entry applies. Re-confirmed (per standing workspace
  rule) that no analytic-density tool in knowledge_base.md bears on "does
  prime p eventually appear as a singleton companion of a recursively-defined
  greedy subclass" — this is exactly the same kind of lower-density-on-an-
  arbitrary-subclass question already ruled out (round 6/9/11, and re-derived
  by round 14's own Part 2 attempt) as inaccessible to classical sieve/Mertens
  tools.

- Analogous past problems (cruxes): did not re-run a fresh crux corpus search
  this round (out of scope for this lens's dispatch, and the workspace's own
  round-6/11 crux searches already exhaustively covered this problem's shape —
  see run_state.md Rules). No new crux surfaced by this purely computational
  investigation.

- Prior progress: 5 solved concrete instances (15, 247, 4199, 2747, 4087) plus
  1 closed disjoint-core-pair channel of a_1=21528751 (({197},{103}), via
  Corollary MSF, round 14). This round's data suggests 2 more of
  21528751's channels (({103},{197,1061}) and ({197},{103,1061})) are very
  likely closable NOW by the same mechanism with witnesses already visible in
  the N=250,000 data — a concrete, low-risk next target for a builder, though
  I have not written out the exact proof (per my mandate, only flagging the
  opening).

- Dead ends (do not retry): do not re-attempt to characterize the resistance
  of I_{197} (or any single resistant class) via "|comp| stays small/shrinks
  over time" — it demonstrably does NOT shrink (floor frozen at exactly
  {2,3,7} for 4237 consecutive members here); and do not treat "Small-Companion
  Existence" (comp size <=2) as the right target at all — round 14 already
  retired it and this round's much deeper search only reconfirms that
  retirement (still 0/4237 for I_197, 0/74 for I_1061, no downward trend).
  Do not re-attempt a full N-push via the sympy-factorint-fallback generator
  beyond ~350,000-400,000 terms for a_1=21528751 without first building a
  faster large-range sieve or a smarter targeted search — it times out (I hit
  this wall at N=500,000/max value ~10^8 within the 60-min budget).

- Small-case / intuition notes (all labeled conjecture — numerical evidence
  only, not proof):
  - **Conjecture A**: for every a_1, every proper core S has a well-defined,
    apparently-permanent "companion floor" F_S (the eventual value of the
    running intersection of comp(a_k) over I_S), and this floor is reached
    very early (within the first few members of the class) and never observed
    to shrink again over spans of thousands to tens of thousands of
    subsequent members. This generalizes (and is evidentially much stronger
    than) the already-refuted "two-in-a-row locks it" claim (Theorem
    TLL-Refuted, round 13) purely by virtue of a much longer observed
    plateau — but per that same theorem's own counterexamples, an even longer
    plateau elsewhere in the workspace's own data DID eventually break, so
    this remains conjectural, not certified.
  - **Conjecture B**: F_S is regularly (not just once) achieved EXACTLY by
    some member of I_S (comp(a_k) = F_S exactly, no extra primes) — this
    "exact-floor recurrence" appears to be the real load-bearing fact behind
    every successful Corollary MSF closure so far (all 6 solved
    instances/channels), not the size of F_S itself.
  - **Conjecture C (sharpest, most useful for round 16)**: whether Bounded
    Forced-Set Existence succeeds for a given disjoint pair (S,S') depends on
    whether the SPECIFIC primes in F_S (or F_{S'}) recur as independent
    singleton (or small, combinable) companions ELSEWHERE in the sequence —
    NOT on the raw size of F_S. For a_1=21528751 this fails for exactly the
    2 channels touching {1061} (needs prime 11, which never appears alone in
    250,000 terms) and fails completely for ({197},{1061}) (neither side ever
    produces a singleton at all). For a_1=4199, by contrast, essentially every
    prime eventually appears as a singleton somewhere, suggesting 21528751 is
    a genuinely harder/slower-converging instance for this specific
    mechanism, not proof of a permanent structural block — a deeper (or
    smarter) search, or a generalization of Corollary MSF to non-singleton
    disjunctive witnesses, is the concrete next step, not a full top-level
    reframing.
