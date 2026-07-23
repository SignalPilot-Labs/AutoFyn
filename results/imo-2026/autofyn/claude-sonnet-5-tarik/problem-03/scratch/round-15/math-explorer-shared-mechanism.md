## imo-2026-03 — dedicated lens: is Gap 1a's Per-Partner Domination induction the SAME mechanism as Gap 1c's half-step lemma?

**Verdict up front: YES, confirmed — this is a real, previously-only-suspected shared mechanism, now
directly tested and verified positive (0 violations once scoped correctly), with a precise
characterization of exactly what scope discipline makes it work. This is not a full proof, but it
is a decisive, load-bearing structural finding that should reshape next round's build plan.**

### Setup / what I read
`results/imo-2026-03/approaches/potential-weighting-upper-bound.md` §17.2 (definition of the scope
family `\mathcal F`), §13.2 (Generalized Multi-Background Peeling Lemma / DELETE-KEEP-MATCH
trichotomy), §21.1/§21.3/§22.1/§22.2 (Gap 1a's Per-Partner Domination Lemma, proved for `q<=3`, and
Gap 1c's half-step lemma), plus `lemmas/shrink-list-monotonicity.md` and
`lemmas/general-rank-extraction-identity.md`. Also read round 14's raw harness
(`/tmp/round-14/work/build_F.py`, `defs.py`) to recover the EXACT computational definition of
"genuine `\mathcal F`-provenance" the round-14 explorer used for the half-step's `0/3400+` claim —
this was essential (see below, it resolved an apparent contradiction in my own first tests).

### Key correction, read carefully (this matters for the outliner)
`\mathcal F`'s own base generator (§17.2, item 1) is **`(B_1,Z_1,+1)`** — i.e. `k^*`'s **own already-
matched** sub-instance (`B_1=\{b_0,d_{k^*}\}`, `Z_1=Z_0\setminus\{z_1,z_{k^*}\}`) — **NOT** the raw
top-level `(B_0,Z_0,+1)` triple. Gap 1a's `A_{3,l}=\mathrm{OPT}_{+1}(\{b_0,d_l\},Z_0\setminus
\{z_1,z_l\})` is *exactly* `\mathrm{OPT}_{+1}(B_1,Z_1)` when `l=k^*`. This means **Gap 1a's
Deletion-Suffices-for-`k^*`, in its exact form `M=D$, is literally the claim "Claim A / Match-Free
Recovery holds throughout the entire subtree of `\mathcal F` rooted at `(B_1,Z_1,+1)`"** — i.e. Gap
1a *is* a (rooted) instance of the same general theorem Gap 1c's half-step lemma is trying to help
prove, not merely "structurally similar." I mis-set-up my first computational tests using
`(B_0,Z_0,+1)` as the root (matching the literal English of "base-generator top-level match") and
got **massive** failure rates (69–91%) for the half-step there — this is a real, useful negative
data point (see below) but is a red herring for the "same mechanism" question until the root is
fixed to `(B_1,Z_1,+1)` per §17.2's own definition.

### Direct computational test (exact `Fraction`, small bounded cases, `q<=6`)
Built an independent brute-force `OPT_\sigma(C,W)` (full DELETE/KEEP/MATCH selection enumeration,
cross-checked against the file's recursive trichotomy — used the *direct* enumeration throughout to
avoid trusting any recursive shortcut). Tested the half-step lemma
`\mathrm{OPT}_{+1}(C\cup\{d\},X)\ge\mathrm{OPT}_{+1}(C,X)` applied **inside `(B_1,\mathrm{Res})`'s
own further recursion** — i.e. peeling `\mathrm{Res}:=Z_0\setminus\{z_1,z_l\}`'s own top element
`u_1` and matching it with some `u_i\in\mathrm{Res}`, leaving `X=\mathrm{Res}\setminus\{u_1,u_i\}`
(genuinely nonempty once `q\ge5`, since `|\mathrm{Res}|=q-2`):

- **At `q=5` (`|X|=1`), restricting `l` to an arbitrary partner achieving the min-trigger comparison
  but not requiring true global-argmin-ness:** `7216` checks, **`1067` violations (`\approx15\%`)**
  — matches round 14's own reported "FALSE ~15% the instant `\mathcal F`-provenance is dropped"
  finding almost exactly, confirming my harness reproduces theirs.
- **At `q=5` (`|X|=1`), restricting `l` to the TRUE global argmin `k^*` of the base instance (i.e.
  `l\in\arg\min_l A_{3,l}`, exactly `\mathcal F`'s own defining condition), `1362` genuine trigger
  instances: `3270` checks, `0` violations.**
- **At `q=6` (`|X|=2`), same true-argmin restriction: `163` genuine trigger instances, `690` checks,
  `0` violations.** (Time-capped at ~1500 random `q=6` trials; consistent with `q=5`.)

**This directly demonstrates the mechanism is shared, and pins down the exact scope needed:** the
half-step lemma, when it is actually asked to do the job Gap 1a's general-`q` induction needs (bound
the MATCH branch of `\mathrm{Res}`'s own recursion inside `k^*`'s matched sub-instance), holds
cleanly — but **only when the background element feeding it (`d_{k^*}=z_1-z_{k^*}`) came from the
TRUE global argmin, not merely "some partner that satisfies the top-level trigger."** Testing at an
arbitrary (non-argmin) partner reproduces almost exactly round 14's own "~15% failure outside
`\mathcal F`" number — i.e. **round-14's own negative control on the half-step (arbitrary partner)
IS the same phenomenon as testing Gap 1a's mechanism with the wrong hypothesis** — one more
confirmation these are the same underlying fact, not two coincidentally-similar ones.

### Answering the three dispatched questions directly
1. **Do they reduce to the same underlying inequality?** Yes — literally the same statement
   (`\mathrm{OPT}_{+1}(C\cup\{d\},X)\ge\mathrm{OPT}_{+1}(C,X)`), applied at the same type of node
   (`C=B_1$, a background built from a genuine global-argmin match), once §17.2's own definition of
   `\mathcal F`'s root is used consistently. Not "resembles" — literally the same computation, verified
   by constructing the `q=5,6` instances from Gap 1a's own machinery and checking the half-step's
   exact hypotheses against them.
2. **Would a proof of one give the other for free, or via a short reduction?** **One direction, yes,
   via a short (not free) reduction; the other direction, no.** Proving the half-step lemma in full
   generality (for genuine `\mathcal F`, i.e. `C` descended through a true-argmin chain) supplies
   *exactly* the missing MATCH-branch sub-case of Gap 1a's general-`q` induction: peel
   `\mathrm{Res}`'s own top element via the already-certified Generalized Multi-Background Peeling
   Lemma trichotomy (DELETE/KEEP close via the IH plus the certified Rank-Extraction Identity — same
   machinery as the `q=3` proof; MATCH closes via half-step chained with the certified Shrink-List
   Monotonicity Lemma, exactly the two-step chain already written down in §21.3). **But this does
   NOT instantly close Gap 1a**: the induction *also* needs generalized free bounds on `A_1` (the
   `q=3` proof used `A_1\le b_0` and `A_1\le|b_0-w|`; general `q` needs the flagged family
   `A_1\le\mathrm{OPT}_{+1}(\{b_0\},\mathrm{Res}\setminus S)` for small `S`, §22.2's own recommended
   next step (ii)) — a separate, likely-easier (Shrink-List-flavored) piece not covered by the
   half-step itself. So: **half-step `\implies` (most of) Gap 1a's hard case, via a concrete,
   short, spelled-out mechanical reduction — not a free corollary, but a real simplification of what
   remains.** The reverse (Per-Partner Domination `\implies` half-step) is NOT evident — the
   half-step is more naturally its own self-contained strong induction on `|X|`, and nothing in
   Gap 1a's `q\le3` proof obviously supplies it.
3. **Does the F-provenance restriction on the half-step suggest the right restriction/invariant for
   Gap 1a's induction to close for general `q`?** **Yes, precisely and now confirmed, not just
   suspected.** The exact invariant is: **at every recursive depth, the augmenting background value
   must have been produced by matching the CURRENT list's TRUE global argmin, not merely a partner
   that beats a local trigger comparison.** This sharpens (rather than merely restates) round 14's
   own §21.1 diagnosis that `k^*`'s *global* argmin-ness (not just the trigger `M<A_1`) is
   load-bearing — my tests show this same global-argmin-ness requirement must be propagated
   **recursively, one level deeper**, into the half-step's own use inside `\mathrm{Res}`'s
   recursion, not just asserted once at the top. A correct general-`q` proof of either gap must
   therefore carry an inductive hypothesis of the shape "`(C,W)` arose via a chain of true-argmin
   matches" (stronger than merely "`(C,W)\in\mathcal F`" as currently defined by DELETE/KEEP closure
   alone in §17.2 — note `\mathcal F`'s own generation rule does *not* mention argmin-ness past the
   base generator, which may itself be an under-specification worth flagging to the outliner).

### A genuinely new, concrete, bounded finding: `q=4` is likely easier than `q\ge5`, contradicting the flat "q>=4 open" framing
At `q=4`, `|\mathrm{Res}|=2`, so matching `\mathrm{Res}`'s own top element consumes **both**
remaining elements — `X=\emptyset` always. This means Gap 1a's `q=4` case's MATCH sub-case is a
plain `e()` computation on a 4-element set (background `B_1$ plus one new inserted difference),
**structurally identical in kind to the already-solved `q=3` proof** (which handled a 3-element
`e()` via the Rank-Extraction case split) — it does **not** need the half-step lemma's genuinely
nonempty-`X` content at all. The half-step's real, load-bearing difficulty (and hence the genuine
link to Gap 1c) only bites starting at **`q=5`** (`|\mathrm{Res}|=3`, first point where a MATCH
inside `\mathrm{Res}` leaves something over). **Recommendation: a future builder should first close
`q=4` directly by the `q=3` technique (one more Rank-Extraction case split, no new lemma needed) —
cheap, likely mechanical — before attacking `q\ge5` via the half-step reduction above.** This
refines round 14's flat "`q\ge4` open" note into "`q=4` easy/mechanical, `q\ge5` is where the
half-step becomes necessary."

### Cheap-kill candidates
- Before attempting the general-`q` induction, check `q=4` by hand via the exact `q=3`-style
  Rank-Extraction case split (no computation needed beyond what's already certified) — likely closes
  in well under a page, per the structural observation above.
- When testing the half-step lemma computationally in any future round, ALWAYS build the tested
  instances by (a) generating a genuine top-level trigger+true-global-argmin base generator, (b)
  taking its `k^*`-matched child `(B_1,Z_1,+1)` as the actual root, and (c) further descending via
  DELETE/KEEP/*true-argmin*-MATCH only — testing with an arbitrary (non-argmin) match partner at any
  level reproduces the already-known ~15%+ failure rate and is not evidence against the lemma, just
  evidence the test left `\mathcal F`.

### Knowledge-base entries in play (no new ones needed this round)
- `lemmas/general-rank-extraction-identity.md` — closes DELETE/KEEP branches at every depth (already
  certified, reusable as-is for the general-`q` induction's non-MATCH branches).
- `lemmas/shrink-list-monotonicity.md` — the free half of the half-step's own two-step chain (§21.3),
  and supplies the generalized-`A_1`-bounds family flagged as the remaining non-half-step work.
- `lemmas/forced-swap-inequality.md` — checked whether it could substitute for the half-step in this
  reduction; it bounds *sibling* match-partner values against a top-level argmin, a different shape
  (confirmed again this round, consistent with round 12's dead-end finding) — not directly reusable
  here, do not re-attempt.

### Analogous past problems (crux corpus)
No new crux search performed this round (dispatch scope was the internal shared-mechanism question,
not fresh literature search); round 13's flagged shape (`aimo-0960`/`aimo-0438`/`aimo-0666`,
"extremal witness + secondary tie-break + local rewrite") remains the closest fallback if the direct
half-step induction below stalls, per round 14's own recommendation — not newly evaluated here.

### Prior progress
Per-Partner Domination Lemma proved in full for `q<=3` (round 14, reviewer-reconfirmed). Shrink-List
Monotonicity certified (round 14). Half-step lemma (Gap 1c) corroborated `0/3400+` within genuine
`\mathcal F` (round 14) — **this round's contribution is showing WHY it was clean (correct root +
true-argmin restriction) and that it is the literal missing piece of Gap 1a's `q\ge5` induction, with
`q=4` separable and easier.**

### Dead ends / negative results this round (do not retry)
- Testing the half-step lemma at the RAW `(B_0,Z_0,+1)` triple (rather than `\mathcal F`'s actual
  root `(B_1,Z_1,+1)`) is **not** a valid test of the lemma — it produces massive failure (`1236/1356`
  at depth 0, `69-91%`) that has no bearing on the lemma's truth; this is a scoping artifact, not a
  counterexample to anything on file. Record this so a future round doesn't mistake it for a new
  negative result about the half-step itself.
- Testing either Gap 1a's or Gap 1c's mechanism with `l`/match-partner NOT restricted to the true
  global argmin reproduces the already-known ~15% (Gap 1c) / much higher (my broader sweeps, up to
  91% at shallow depth) failure rates — confirms, does not newly refute, the existing "argmin-ness is
  load-bearing" finding (round 12, round 14).

### Small-case / intuition notes (labeled conjecture where not proved)
- **Conjecture, strongly corroborated (0/3270 at q=5, 0/690 at q=6, exact-Fraction, true-argmin
  scope):** the half-step lemma holds throughout `\mathcal F`'s true-argmin-descended subtree, not
  just at shallow depth — consistent with, and now directly testing one level deeper than, round
  14's own `3400+`-check claim.
- **Conjecture (structural, not yet proved):** the general-`q` Per-Partner Domination Lemma reduces,
  via peeling `\mathrm{Res}`'s top element, to: IH (DELETE) + Rank-Extraction (KEEP) +
  [half-step + Shrink-List] (MATCH) + a generalized `A_1`-bound family — i.e. the four gaps population
  currently tracks as separate (Gap 1a general-q, Gap 1c half-step) are, from `q=5` on, literally one
  combined induction, not two independent proof obligations. This is the single most actionable
  finding to hand to the outliner this round.
