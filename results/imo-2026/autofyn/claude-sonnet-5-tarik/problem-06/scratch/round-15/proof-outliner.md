## imo-2026-06

### similarity-dichotomy-crux-adaptation  (NEW — primary build target this round)

Target: the WHOLE problem, for EVERY `a_1` — exhibit explicit `T,L` with
`a_{n+T}=a_n+L` for every `n≥1`. If this approach's Dichotomy Theorem
(Step 4 below) is proved, Status → solved.

Technique: adapt the officially-proved similarity-dichotomy from crux
`aimo-0030` (IMO Shortlist 2013 N5, "Ana and Banana") — whose own
recursive rule (`b_0=k`; `b_{n+1}`= smallest `b>b_n` sharing a factor
with every one of `b_0,...,b_n`) is verbatim identical to imo-2026-06's
`a_1,a_2,...` — to a **direct, from-scratch periodicity argument that
bypasses the entire FCBC / Conjecture (JW) / (WCE) / Corollary-MSF
apparatus this workspace has built over 14 rounds.** This is a
genuinely different top-level route: it does not go through FCBC,
Theorem 5.1, or any covering-set `H` at all — it classifies individual
integers as "terms" or "non-terms" via their divisibility signature by
the FIXED finite prime set `{p : p ≤ a_1}`, then gets periodicity as an
elementary fact about interleaved arithmetic progressions.

Per CLAUDE.md, the crux is a hint to adapt, never a citation — every
step below must be re-derived from scratch in imo-2026-06's own
notation before this approach can be trusted; several steps are marked
**RECON ONLY (not yet re-proved)**.

Skeleton:
1. **Setup.** Let `k:=a_1`. Let `P:=∏_{p≤k, p prime} p` (finite, only
   finitely many primes `≤k`). For any integer `n≥k`, define its
   *signature* `sig(n) := {p≤k : p∣n}` — the (finite, ⊆{p≤k}) set of
   small primes dividing `n`. Note: if `n≡n' (mod P)` then `sig(n)=
   sig(n')`, because `n≡n' (mod p)` for every prime `p∣P` (i.e. every
   `p≤k`), so `p∣n ⟺ p∣n'` for each such `p`. — elementary, no gap.
2. **Claim 1 (multiple of a term is a term) — ALREADY PROVED FROM
   SCRATCH this round** by the alternative-mechanism explorer, reusing
   only this workspace's own certified Lemma P′ / Corollary P″
   (`lemmas/lemma-P-prime-pairwise-intersecting.md`): if `a_i` is a term
   and `m≥k` is a multiple of `a_i`, then `m` is also a term. Proof: if
   not, some term `a_j<m` (`j` least witnessing non-membership) has
   `gcd(a_j,m)=1`; since `a_i∣m`, `gcd(a_j,a_i)=1` too; but `a_i,a_j`
   are both terms of the sequence so Corollary P″ forces `gcd(a_i,a_j)>1`
   — contradiction. **Builder: re-verify this 3-line proof independently
   before citing it as done; do not just copy it.**
3. **Claims 2/3 (companion moves) — RECON ONLY, must be re-derived from
   scratch.** Locate `aimo-0030`'s full official solution (both given
   solutions if two are recorded) in the crux corpus
   (`past_problems_database.json` / `past_crux_moves_database.json`,
   `problem_id=aimo-0030`) and translate its remaining building-block
   claims into imo-2026-06's `a_n`/"term" language (NOT the game's
   "good/bad" language — Claim 1 above shows the translation can produce
   a *shorter* proof than the original once Lemma P′ is available, so do
   not assume every step imports unchanged). Concretely (paraphrased
   from this round's explorer reports, UNVERIFIED — the builder must
   read the actual official text, not rely on this paraphrase):
   - "Claim 2": if `rs` is not a term and `r,s` are coprime, then `r²s`
     is also not a term.
   - "Claim 3": if `p` is a prime `>k` and `n` is not a term, then `np`
     is also not a term.
   Each needs its own from-scratch proof in this workspace's notation
   (using only already-certified lemmas — Lemma P′/Corollary P″, Lemma
   XC — plus whatever elementary number theory the official proof uses).
   Numerically spot-checked only (115+77 checks, zero violations,
   `a_1=15`) — **not a proof**.
4. **Main Dichotomy Theorem — RECON ONLY, the hard core, must be
   re-derived from scratch.** For `n,n'≥k` with `sig(n)=sig(n')`: `n` is
   a term of the sequence iff `n'` is. This is the crux's headline
   result (Part (a) of the official solution). Numerically tested
   directly (not just via consequences) on `a_1=15` (46 signature
   classes, zero mixed) and `a_1=21` (163 classes, some of size 1541,
   zero mixed) — strong evidence, **not a proof**. The builder must
   assemble Claims 1-3 (or whatever the official chain actually is) into
   a complete induction/case-argument establishing this in full
   generality for imo-2026-06's own sequence.
5. **Periodicity Corollary — genuinely NEW content beyond the crux
   (not in its official solution, which only needs the dichotomy for a
   different conclusion), needs to be derived once Step 4 is in hand.**
   By Step 4, for each residue class `r (mod P)`, either every `n≥k`
   with `n≡r (mod P)` is a term, or none is (since all such `n` share
   `sig(n)=sig(r)` by Step 1's observation). Let `T:=` the number of
   "good" residues `r∈{0,...,P-1}` (i.e. `1≤T≤P`; `T≥1` since `k` itself,
   `k mod P`, is a term). The set of terms restricted to `[k,∞)` is
   therefore EXACTLY the union of `T` full congruence classes mod `P`.
   **Elementary interleaving fact (prove directly, no citation needed):**
   sorting the union of `T` full arithmetic progressions with common
   difference `P`, each based at its representative in `[k,k+P)`, gives
   a strictly increasing sequence `g_1<g_2<...` satisfying
   `g_{n+T}=g_n+P` for literally EVERY `n≥1` (not just eventually) —
   because the first `T` terms `g_1,...,g_T` are exactly the sorted
   base representatives in `[k,k+P)`, one per good class, and every
   subsequent block of `T` terms is the previous block shifted by `P`
   (each class contributes its next element, exactly `P` above the
   previous one, in the same sorted order). Since `k=a_1` is itself in
   `[k,k+P)` and every `a_n = g_n` (the sequence of terms), this gives
   `T,L:=P` satisfying the problem's conclusion EXACTLY, from `n=1`,
   without invoking Theorem 5.1, FCBC, or any covering set at all.
6. **Sanity check the whole chain against a_1=15 by hand/Python**
   (already partially done: sequence match confirmed character-for-
   character against the crux's own worked example, period 30 matches
   this workspace's own certified `L=30`) — the builder should verify
   `T` and `P` computed via Step 5's formula for `a_1=15` reproduce
   `T=8,L=30` exactly (both already certified in this workspace from an
   independent route), as an end-to-end check before trusting the
   general argument.

Key lemmas (claim + mechanism):
- Claim 1 (multiple-of-a-term-is-a-term) — because a hypothetical
  smallest non-term multiple would force a coprimality contradiction
  with its own divisor via the certified unordered pairwise-gcd fact
  (Corollary P″). DONE.
- Signature depends only on residue mod P — because `p∣P ⟺ p≤k`, and
  divisibility by each such `p` is determined by residue mod `p`,
  hence by residue mod `P` (CRT). DONE (elementary).
- Main Dichotomy (same signature ⟹ same term-status) — mechanism TBD,
  must reconstruct the official aimo-0030 argument (Claims 2/3 chain,
  or whatever the alternate solution uses) from scratch. OPEN, RECON.
- Periodicity-from-interleaving — because a union of `T` full residue
  classes mod `P`, sorted, is a deterministic "round-robin" merge that
  repeats its increment pattern every `T` terms by construction, no
  asymptotic/eventual caveat needed. DONE (elementary, but builder must
  write the short formal proof, not just assert it).

Open gaps: Step 3 (Claims 2/3 translation and proof) and Step 4 (the
main Dichotomy Theorem) are the entire remaining content — everything
else (Steps 1,2,5,6) is either already done or elementary. **This is an
all-or-nothing gap**: if Step 4 fails to transfer, this approach's
entire route collapses (there is no partial credit toward the general
theorem the way FCBC's incremental instance-closures gave partial
credit) — but a failed Step 4 attempt would still be valuable negative
information (which part of the official proof needs `k`-specific
structure this problem's hypotheses don't literally match, if any).

Cases to cover: none — this route, if it works, is uniform in `a_1`
(no case split on Case I/Case II, on `|P_1|`, or on core pairs at all;
that entire case-structure is an artifact of the FCBC apparatus that
this route bypasses).

Watch out for:
- **Do not conflate "recon numerically checked" with "proved."** Steps
  3-4 are flagged RECON ONLY for a reason — the outline-reviewer and
  builder must independently re-derive them from the actual official
  aimo-0030 solution text, not merely trust the paraphrase or numerics
  in the explorer reports.
- **Verify the official Claims 2/3 do not secretly depend on the
  game-theoretic framing in a way that doesn't translate** (e.g. a move
  legality condition specific to "Ana and Banana" that has no
  imo-2026-06 analogue) — the alternative-mechanism explorer flagged
  this as an open 10-minute check not yet done.
- **Double check "for every n≥1" vs "eventually"**: Step 5's argument
  as sketched gives exact periodicity from n=1 directly from the
  interleaving structure, which would be a STRONGER and SIMPLER result
  than Theorem 5.1's (which needed a separate backward-sharpening
  argument, conditional on FCBC). If the builder finds this claimed
  simplicity doesn't actually hold (e.g. a subtlety in how `k` itself,
  or very early terms, fit into the interleaving), that's a real gap to
  surface, not paper over.
- **If Step 4 (the Dichotomy) turns out false or unprovable as stated**,
  do NOT silently weaken it and claim partial credit toward the general
  theorem — report the precise point of failure so a future round can
  judge whether a repaired/weaker dichotomy still gives periodicity via
  Step 5's interleaving mechanism (it plausibly could with a relaxed
  hypothesis, e.g. "same signature for primes ≤ some threshold larger
  than `a_1`" or "eventually same status" — but that is new content for
  a future round, not to be invented ad hoc mid-build without flagging
  it as a deviation from this outline).

---

### forced-primes-well-ordering  (ADVANCE — apply this round's cheap
Common-Recruiter Reuse finding to close more channels of `a_1=21528751`)

Target: the whole problem (unchanged) — via the already-certified
Theorem SW → Theorem 5.1 chain, plus concrete instance/channel
closures using Lemma WF as the mechanism (unchanged top-level route,
same file as rounds 13-14; this round adds a cheap corollary + a new
worked closure, not a new mechanism).

Technique: unchanged (finite low-index witness-chaining via Lemma WF /
Chaining Sufficiency Theorem), but this round packages a genuinely
cheap generalization found independently by two of this round's
explorers: **Common-Recruiter Reuse** — the SAME finite witness set
already used to close one channel closes EVERY OTHER disjoint-core
channel whose two sides are each either equal to, or disjoint from,
one of the two original recruiting cores, for free (no new search, no
new witnesses).

Skeleton:
1. **Formalize Common-Recruiter Reuse as a corollary of the
   already-certified Lemma WF** (not a new mechanism — a bookkeeping
   observation about which target classes a fixed witness's Lemma-WF
   conclusion applies to): if witness `a_{i_0}` (companion set `C`
   disjoint from core `S`) forces `C∩comp(a_k)≠∅` (or `q∣a_k` if
   singleton) for every `k∈I_{S'}` with `S'` disjoint from `S` — this
   holds for literally EVERY core `S'` disjoint from `S`, not only the
   one core the witness was originally chosen to close. State this
   explicitly as **Corollary CRR** and give its 1-line proof (Lemma WF's
   own hypothesis is exactly "target core disjoint from witness's
   core" — nothing else about the specific target core is used).
2. **Apply Corollary CRR to `a_1=21528751`'s 4 already-on-file
   witnesses** (`a_{1405},a_{11812},a_{27832}` — core `{103}`, singleton
   companions `2,3,7` respectively; `a_{2575}` — core `{197}`, comp
   exactly `{2,3,7}`) against every target core disjoint from `{103}`
   or `{197}` (not just the originally-closed `{197}` vs `{103}`
   channel): this gives, unconditionally, `{2,3,7}⊆comp(a_k)` for every
   `k∈I_{\{197\}}∪I_{\{1061\}}∪I_{\{197,1061\}}`, and
   `comp(a_k)∩\{2,3,7\}≠∅` for every `k∈I_{\{103\}}∪I_{\{103,1061\}}`.
   Conclude: 4 more disjoint-core-pair channels close for free —
   `(\{103\},\{1061\})`, `(\{197\},\{1061\})`,
   `(\{103\},\{197,1061\})`, `(\{197\},\{103,1061\})` — bringing
   `a_1=21528751` to **5 of its 6 disjoint-core-pair channels closed**.
3. **Re-verify the numerical claim independently** (builder must
   re-derive, not copy, the explorer's `N=100,000` check: zero
   exceptions to `{2,3,7}⊆comp` on `I_{197}` (1695/1695), `I_{1061}`
   (30/30), `I_{197,1061}` (2/2); zero exceptions to
   `comp∩{2,3,7}≠∅` on `I_{103}` (97677/97677), `I_{103,1061}` (92/92)).
4. **Honestly scope the 6th channel** `(\{1061\},\{103,197\})` as NOT
   closed by this mechanism: the target core `\{103,197\}` is not
   disjoint from either recruiting core `\{103\}`/`\{197\}`, so Lemma
   WF/Corollary CRR cannot be aimed at it via those witnesses; the only
   disjoint recruiter is `\{1061\}` itself, whose class is sparse
   (30/100000) with no singleton witnesses and a companion floor that
   always includes one extra prime beyond `\{2,3,7\}` (varies:
   `11,17,13,19,...`). This channel needs either (a) a genuinely new
   witness search targeting the escape structure of core `\{103,197\}`
   (already-certified Permanent Bundle Lemma names `Q=\{11,97\}` as one
   permanent escape bundle for this exact core — check whether
   `W=\{2,3,7,11,97\}` closes it, i.e. does EVERY member of
   `I_{\{103,197\}}` have `comp∩\{2,3,7,11,97\}≠∅`?), or (b) leave open
   and report as the sole remaining channel of this instance.
5. **If (4a) succeeds**, this would be the workspace's SIXTH fully
   solved concrete instance (`21528751`) — a major addition since this
   has been the longstanding hardest recurring test case (flagged
   rounds 6-11). Check exhaustiveness (`|P_1|=3` gives `2^3-1=7`
   nonempty subsets, `15` intersecting-with-both-sides pairs `+` the `6`
   disjoint-core pairs enumerated above `=21` total pairs, matching
   the workspace's own established `4199` exhaustiveness-count
   template) before claiming the instance closed.

Key lemmas (claim + mechanism):
- Corollary CRR — because Lemma WF's proof only uses "witness's
  companion set is disjoint from the TARGET core," a hypothesis that
  doesn't reference which specific target core was originally intended
  — so the same witness's conclusion holds against every core disjoint
  from it, for free.
- (4a)'s candidate `W=\{2,3,7,11,97\}` closing channel 6 — because the
  Permanent Bundle Lemma already certifies `\{11,97\}` as one exhaustive
  escape route past `\{2,3,7\}` for core `\{103,197\}`; IF it is the
  ONLY escape route (open, not yet proven), the union closes the
  channel. **This "if" is the crux of whether channel 6 is easy or
  hard — flag explicitly, do not assume it.**

Open gaps: whether channel 6 closes (step 4/5); if not, it remains the
sole open channel of this instance, same status as before this round
but now precisely isolated (nothing else about `21528751` is open).

Cases to cover: the 21-pair exhaustiveness count (15 intersecting + 6
disjoint) must be re-verified for `a_1=21528751`'s `P_1=\{103,197,
1061\}` before claiming full closure.

Watch out for: do not claim the general Bounded Forced-Set Existence
Conjecture is supported just because Common-Recruiter Reuse is cheap
and works here — this is instance-specific bookkeeping, not a general
existence proof (see witness-chaining-universal-existence below for
the general-existence angle).

---

### witness-chaining-universal-existence  (ADVANCE — attack Bounded
Forced-Set Existence Conjecture using this round's calibration data
and reusable witness-search tool)

Target: the whole problem (unchanged) — via a GENERAL proof (not
instance-by-instance) that Corollary MSF / the Chaining Sufficiency
Theorem's hypothesis (some finite closing witness collection) is
satisfied for EVERY `a_1` and disjoint core pair (Conjecture WCE /
Bounded Forced-Set Existence). This is the sharpest general target per
round 14's recommendation, still open.

Technique: unchanged top-level target, but this round formalizes the
general-unification explorer's validated **witness-search tool**
(`/tmp/round-15/gen.py`, `/tmp/round-15/wce_search3.py` — a provably
exact, faster-than-powerset procedure for checking the Chaining
Sufficiency Theorem's success condition via minimal-hitting-set/
choice-function enumeration) as a certifiable **decision-procedure
lemma**, then uses it to sharpen exactly which class of pairs resist.

Skeleton:
1. **Certify the witness-search reduction as a lemma**: for a fixed
   dedup'd pool of witness companion-sets per side, checking whether
   SOME sub-collection satisfies the Chaining Sufficiency Theorem's
   success condition is equivalent to checking only choice-function-
   generated candidate collections (not the full powerset) — because
   the success predicate `T_S(R)` is an up-set in the witness-collection
   lattice, so its minimal witnesses are exactly realized by choice
   functions over the defining family. Builder must write this proof
   formally (the explorer verified it holds numerically/reproduces
   published closures exactly for `247`,`4199`, but did not write a
   formal up-set proof — that's the gap to close here).
2. **Recalibrate the Bounded Forced-Set Existence Conjecture against
   this round's sharper negative data**: `a_1=21528751`'s classes
   `\{197\}`,`\{1061\}`,`\{197,1061\}` have a companion-floor/min-comp-
   size that is FROZEN EXACTLY (not just "no smaller example found")
   across a 3.3x-8x depth increase (`N=150,000→500,000` and
   `N=27,832→250,000` respectively, two independent explorers). State
   precisely: this refutes the conjecture **in its MSF-singleton-shaped
   form** for these classes (a companion set of size ≤2 or exactly-
   floor-achieving-with-few-primes will not appear for `\{1061\}`-type
   classes from this data) but does NOT bear on whether the full
   Chaining Sufficiency Theorem (larger, non-singleton, disjunctive
   witness collections — the general mechanism, not MSF's special
   case) still succeeds — this is the correct, careful reading per this
   workspace's own standing rule (never confuse a refuted sufficient
   mechanism with a refutation of the target).
3. **Run the certified witness-search tool (once formalized) against
   the 6th channel of `a_1=21528751`** (`\{1061\}` vs `\{103,197\}`,
   confirmed still open by both this round's structural-obstruction and
   alternative-mechanism explorers via independent diagnoses) and
   against the fresh instance `a_1=20677=23·29·31` (found by the
   general-unification explorer this round, deliberately checked NOT to
   degenerate to Case I, 5/6 pairs closed by the bounded search) — a
   concrete new candidate 7th solved instance if the last pair
   `\{23\}`/`\{29\}` also closes.
4. **Honestly report whichever of the following actually happens**:
   (a) the tool finds a closing collection for the previously-stuck
   pairs (real progress, extends the toolkit's reach); (b) the tool
   fails to find one within a reasonable search bound (evidence only
   about this specific bounded search per the explorer's own
   documented caution — `4199` needed witnesses beyond this bound for
   3/6 pairs even though it's fully solved); (c) neither — report a
   sharper, still-open recalibrated statement of Bounded Forced-Set
   Existence.

Key lemmas (claim + mechanism):
- Choice-function reduction — because the success predicate is
  monotone (an up-set) in the collection of witnesses used, so testing
  minimal elements via choice functions over the defining families
  suffices; this is a standard finite-lattice fact, needs a short formal
  write-up, not new machinery.
- Refuted-in-MSF-form vs. general Chaining Sufficiency distinction —
  because MSF is a strictly narrower special case (singleton-heavy
  witnesses) of the general theorem (arbitrary finite witness
  collections via full Boolean case-split), so evidence against the
  narrow mechanism is silent on the general one (already the workspace's
  own standing methodological rule, applied here to fresh data).

Open gaps: the general existence question (Conjecture WCE / Bounded
Forced-Set Existence) itself remains fully open — this round's work is
calibration + tooling + possibly 1-2 more concrete closures, not a
proof of the general conjecture.

Cases to cover: none beyond the specific instances/channels attempted.

Watch out for: do not let a successful bounded search on `a_1=20677`
or partial channels of `21528751` create pressure toward believing the
general conjecture is close — per the round-14 standing rule, instance
count is not evidence about the general theorem's truth.

---

### intersecting-family-covering-construction  (ADVANCE — no new
finding this round from the 3 explorers directly targets this
approach's open gap; keep live for population diversity and because it
is the top-Elo, structurally most-independent route)

Target: the whole problem (unchanged) — via the already-certified
Theorem 5.1/Theorem SW/Theorem PD-Conditional chain; this approach's
own remaining open content is `(PD_{S,S'})`/`BRL(S')`/`G`-eventual-
periodicity, unchanged from round 14 (Theorem MO/Prop MO-2 retire two
extreme minimality-selection mechanisms, narrower than a full
impossibility proof).

Technique: unchanged — density/minimality argument on the coarse core
sequence `G`, structurally independent of the witness-chaining
mechanism the other 3 approaches (and the new crux-adaptation attempt)
use; kept live specifically because CLAUDE.md requires the population
not collapse onto one mechanism even while the crux-adaptation route is
prioritized.

Skeleton: unchanged from round 14's file (Lemma WO++/Theorem MO/
Proposition MO-2 already certified) — this round's directive is:
formalize the "intermediate pigeonhole/density mechanism" gap Theorem
MO's own scope correction left open (some, not every, type-`S'`
candidate in each window is admissible against the accumulated
history) — this is a genuinely different, not-yet-attempted mechanism
shape from the two already-ruled-out extremes, per round 14's own
Recommendation (iii).

Key lemmas (claim + mechanism): none new proposed this round beyond
what round 14 already flagged as the next concrete step (the
intermediate mechanism gap) — builder should attempt to close it or
prove a third impossibility case, extending Theorem MO's scope.

Open gaps: `(PD_{S,S'})`/`BRL(S')`/`G`-periodicity itself; whether the
intermediate pigeonhole mechanism (round 14's open Recommendation (iii))
can be ruled out or made to work.

Cases to cover: none beyond the existing Theorem MO case split.

Watch out for: do not let this approach's slower cadence (no explorer
lens targeted it directly this round) cause it to be silently dropped
— it remains the only structurally-independent live mechanism besides
the new crux-adaptation attempt, and per CLAUDE.md diversity is
required even while other approaches advance faster.
