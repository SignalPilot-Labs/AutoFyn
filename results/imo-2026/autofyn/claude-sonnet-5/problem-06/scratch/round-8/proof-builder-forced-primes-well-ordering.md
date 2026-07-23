## imo-2026-06 — forced-primes-well-ordering, round 8 build report

Status: **partial** (unchanged label; real new certified content and one
important honest correction this round).

### What I did

Read the round-8 outline (§ "Round 8 Outline" in the approach file),
outline-reviewer's notes (`/tmp/round-8/outline-reviewer.md`), `current.md`,
the relevant certified lemma files (`lemma-C-generalized-subsequence.md`,
`lemma-lambda-S-reduction-and-single-companion-finiteness.md`, and the
already-in-file §A/§B/§F/§G material), and round 8's math-explorer report
(`/tmp/round-8/math-explorer-cross-bucket-direct.md`) that motivated the
`S^+`/`S^{++}` mandate. Wrote a new `§H` section (~430 lines) plus a
"Round 8 update" headline and updated the end-of-file tracking sections
(`Approaches tried`, `Current best`, `Open gaps`, `Promotable lemmas`).

### Substantive results (all independently computed/verified via Python,
`sympy.factorint`, on the cached sequences `/tmp/round-8/seq_21528751_60k.json`,
`/tmp/round-8/seq_2747_40k.json`)

1. **Freeze-Confinement Domination Lemma — proved in full, certified.**
   Given `(MRS_S)` (the single-class minimal-radical antichain freezes at
   `n^*`), every `i\in I_S` (not just late ones) has `rad(a_i)` containing
   some frozen antichain element. 6-line minimality proof, verbatim
   specialization of the already-certified Local Corollary W3′ (§A). This
   is a real, general, reusable fact and fully retires round 7's "hunt for
   an independent well-founded escape-recursion structure" (§G Step 4).

2. **Honest correction of the outline's own claimed depth-bound formula.**
   The round-8 outline asked me to certify "escape depth `\le
   \max_{C'}|C'\setminus S|`" as a "cheap ~15 line" corollary of domination.
   I attempted the derivation two independent ways and both times produced
   the REVERSE inequality (`d(\kappa)\ge|C'\setminus\kappa|`, a lower bound,
   not an upper bound) — domination constrains what a realized superset must
   *contain*, not how many extra "incidental" primes it may also carry. I
   do **not** certify this formula and report the exact obstruction. This is
   the kind of self-correction this workspace has valued in prior rounds
   (round 6's Freeze Criterion refutation, round 7's "max depth 2"
   correction) — catching an outline's overclaim before it propagates.

3. **Singleton Recruiter Identity — new, sharper, honestly-unproved
   conjecture proposed in place of the failed formula.** When the frozen
   antichain is a singleton `{C'}` (true for both hardest known cores,
   `a_1=21528751,S={197}` and `a_1=2747,S={67}`, freeze indices `n^*=2575`
   and `n^*=3` respectively, both independently recomputed from the cached
   sequences this round), escape depth equals `|C'\setminus\kappa|`
   **exactly** — verified with zero exceptions on all 9 populated-bucket
   data points now on record. This explains round 7's empirical
   "Recruiter-Alignment" pattern (its mysterious `W(a_1)` is `C'\setminus
   S`) but proving it in general looks to be as hard as `(MRS_S)` itself —
   reported honestly as a conjecture, not a theorem.

4. **`S^+` (extended-imprint) Necessity + Finiteness Lemma — proved in
   full, certified.** `S^+:=\bigcap_{i\in I_S}rad(a_i)` lower-bounds every
   exactly-realized bare value of class `S`, and is finite whenever `I_S`
   is infinite — a one-line application of the already-certified
   Generalized Lemma C to `I_S` (previously only applied to the
   *avoiding*-class index set `J_S`, for `D_S`).

5. **`S^{++}` sufficiency fix tested directly against its own motivating
   counterexample (`a_1=21528751,S={1061}`) — found to fail, with a full
   proved explanation, not just a numeric miss.** I recomputed all 19
   members of `I_{1061}` (through `n=60000`) by hand, confirmed `S^+=
   {2,3,7,1061}` and the two populated Coarsening-Lemma buckets both need
   an extra prime `11` beyond `S^+` (matching the round-8 explorer's
   finding). I then tested `S^{++}_\kappa` on both buckets: for `\kappa=
   {2,3,1061}` it degenerates to `S^+` exactly (no improvement) because
   `\kappa\subseteq S^+`; for `\kappa=\{2,19,1061\}` it "succeeds" only
   because the restricted subclass has a single known member (circular, not
   predictive). I proved two new general facts explaining this: the
   **Vacuity Proposition** (`\kappa\subseteq S^+\Rightarrow S^{++}_\kappa=
   S^+` identically) and the **Intersection-Fragility Proposition** (an
   intersection over a class can never recover a prime absent from even one
   member of that class — here, `11` is absent from exactly 1 of 19 known
   members of `I_{1061}`, so no pure-intersection invariant of any kind can
   ever recover it). This is a genuine, structural negative result: it
   rules out the entire *family* of intersection-based mechanisms
   (`S^+`, `S^{++}`, and the already-certified `D_S`) for this sufficiency
   gap, not just the one specific `S^{++}` proposal.

### Honest status of the gap

The core sufficiency gap for proper cores (`(MRS_S)`/local FCBC) is
**unchanged in substance** — still open — but this round narrows what a
correct proof must look like: it cannot be a pure set-intersection
construction over any subclass of `I_S`. A future mechanism needs either a
density/eventual (co-finite) argument robust to finitely many exceptions,
or an entirely different combinatorial tool.

### New lemmas proposed for certification (see "Promotable lemmas" below)

- Freeze-Confinement Domination Lemma (§H Step 1)
- `S^+` Necessity + Finiteness Lemma (§H Step 4)
- Vacuity Proposition + Intersection-Fragility Proposition (§H Step 5)

The Singleton Recruiter Identity (§H Step 3) is explicitly NOT proposed for
certification — it is an open conjecture, clearly labeled as such.

### Files touched

- `results/imo-2026-06/approaches/forced-primes-well-ordering.md` (+604
  lines: new "Round 8 update" headline, new §H section with 5 steps + full
  proofs + numerical tables, updated `Approaches tried`/`Current best`/
  `Open gaps`/`Promotable lemmas`). `## Status` remains `partial`.

All numerical claims in §H were computed by me directly this round (not
copied from the explorer's report without re-derivation) using
`sympy.factorint` on `/tmp/round-8/seq_21528751_60k.json` and
`/tmp/round-8/seq_2747_40k.json`, both cross-validated against round-7
caches before use (per this workspace's standing rule).
