## imo-2026-06 (lens: a_1=11305 Finite-Window Literalization re-application)

- **Distinct openings**: This is a single, narrow, already-scoped follow-up (not a
  fresh top-level framing) — the round-26 dispatch explicitly asked to check
  whether the certified Finite-Window Literalization Lemma
  (`lemmas/finite-window-literalization-lemma.md`) closes `a_1=11305`'s
  standing rogue pair the same way it closed `a_1=4807`'s. I recomputed the
  whole setup from scratch (own fresh Python, both a slow `math.gcd` correct
  reference simulation and a fast bitmask-based one, cross-checked against
  each other and against the certified `two-sided-singleton-witness-theorem.md`
  data) and confirm: **yes, it is a routine reapplication, same proof shape,
  different constants — no new mathematical content needed.** Full data below.

- **Recomputed setup for `a_1=11305` (own script, verified against certified
  lemma data — exact match):**
  - `Q = P(a_1) = {5,7,17,19}`.
  - Core `S₀ = {2,3,5,7,13,17,19,23,29,37,43,101}` (matches
    `two-sided-singleton-witness-theorem.md` exactly).
  - Rogue pair: `A' = {2,5}`, `B' = {3,7}` (extended types at `S₀`).
  - **Canonical witnesses: `n_A = 7`, `n_B = 4`** — note `n_B < n_A` here,
    the OPPOSITE order from `a_1=4807` (`n_A=6 < n_B=7`). This is the one
    bookkeeping subtlety a builder must handle (see below).
  - `a_7 = 11330 = 2·5·11·103`, so `F' := P(a_7)\S₀ = {11,103}` (NOT a
    singleton, `|F'|=2`) — this matches the round-6-era note ("a_1=11305
    gives F'={11,103}"), and confirms that note was NOT a wrong-core
    artifact after all, at least for this specific fact (it correctly refers
    to the properly-recruited `S₀`, same value as round 18/19's core).
  - `a_4 = 11319 = 3·7³·11`, so `F'' := P(a_4)\S₀ = {11}` — a **singleton**.
    This is the exact analog of `4807`'s `F' = {17}` singleton at its
    canonical witness — except here it is the `B'`-side canonical witness
    (`n_B=4`) that is singleton, not the `A'`-side, because of the `n_B<n_A`
    order swap.

- **Step 1 (free, canonical-witness resolution).** Since `F''_4={11}` is
  already singleton at the *canonical* witness `n_B=4` (no window issue,
  exactly mirroring `4807`'s Step 1), Singleton-Side FAH gives directly:
  `11 | a_n` for **literally every** `n>4` with `ρ(n)=A'` — already literal,
  zero exceptions, no Finite-Window Lemma needed for this side. Verified by
  direct computation: 1366 `A'`-occurrences with `n>4` up to 45,000 terms,
  **zero** violations.

- **Step 2 (the actual reapplication target — `B'`-side).** The residual
  open side is `B'` (since `F'={11,103}` is not singleton at the canonical
  witness). The certified Two-Sided Singleton Witness Theorem already
  recorded (round 19) a non-canonical `A'`-occurrence at `x_2=103` with
  `P(a_103)\S₀={11}` — a singleton. I independently confirmed: `a_103 =
  12100`, `ρ(103)={2,5}=A'`, `P(a_103)\S₀={11}` exactly. Applying
  Singleton-Side FAH with far-side witness `x_2=103` gives `11|a_n` for
  every `n>103` with `ρ(n)=B'` (cofinite, matching the certified theorem's
  stated conclusion). **The Finite-Window Literalization Lemma's finite side
  condition** — is there any `n` with `n_B(=4) < n ≤ x_2(=103)` and
  `ρ(n)=B'`? — I checked exhaustively (own script): **no**, the `B'`-occurrence
  list starts `4, 119, 290, ...` — nothing in `(4,103]`. So the Lemma applies
  directly (via its symmetric instance, swapping the `A'`/`B'` labels so the
  canonical-order hypothesis `n_A<n_B` is satisfied — here relabel
  `Ã':=B', B̃':=A'`, `ñ_A:=n_B=4`, `ñ_B:=n_A=7`, `x̃_1:=x_2=103`; the window
  check needed is `(ñ_B,x̃_1]=(7,103]⊆(4,103]`, already covered by the empty
  check above): `11|a_n` for **literally every** `n>4` with `ρ(n)=B'` — zero
  exceptions, not merely cofinite.

- **Combined conclusion (mirrors `4807`'s Step 4h exactly).** Literal Joint
  FAH holds unconditionally for `a_1=11305`'s standing rogue pair, with
  shared witness prime `q=11` on both sides, from `n>4` (the residual
  divisor-class `d=103` in the `D_bad(11)={103}` alphabet, size 1 by the
  Reduced-Alphabet Corollary — computed via `Div(11·103=1133)={1,11,103,1133}`,
  `d>1, 11∤d ⟹ d=103` — never occurs).

- **Independent computational verification (own scripts, two independent
  implementations cross-checked against each other):**
  - Slow correct `math.gcd`-based simulation to `N=20,000`: 614 `A'`-occ, 206
    `B'`-occ, **zero** violations of `11|a_n` on either side for `n>4`;
    window `(4,103]` empty of `B'`-occurrences.
  - Fast bitmask-based simulation (own from-scratch implementation, careful
    to encode the correct universal "`gcd>1` with EVERY prior term" legality
    — an EARLIER draft of this script had exactly the existential-vs-universal
    bug flagged generically in `/tmp/memory/math-explorer.md` rule 22, caught
    and fixed before trusting any output) to `N=45,000` (matching the exact
    scale of the certified `4807` closure's own cross-check): 1366 `A'`-occ,
    457 `B'`-occ, **zero** violations either side, window confirmed empty.
    Both scripts agree exactly on the first 8 terms and on `n_A=7`, `n_B=4`.

- **Verdict on the dispatch question: routine reapplication, not new content.**
  The proof shape is identical to the certified Finite-Window Literalization
  Lemma's proof (a two-case split: `n>x` vs. finite-window vacancy), applied
  with `q=17→11`, `x_1=72→x_2=103`, and the `A'`/`B'` roles swapped relative
  to the canonical-order convention (because `n_B<n_A` here, opposite of
  `4807`). A builder needs only to: (1) state the symmetric instance of the
  already-certified Lemma (or just re-run the two-case argument directly with
  the swapped labels, to avoid any confusion from blindly substituting into
  the literal `A'`/`B'`-labeled statement); (2) display the finite window
  table `n=5,...,103` (or cite the exhaustive check) showing no `B'`-occurrence
  in `(4,103]`; (3) conclude literal Joint FAH for this one seed. This is a
  bounded, mechanical task — no unproved sub-lemma, no new existence
  hypothesis, no numerical uncertainty (I've already run the check to 45,000
  terms with zero violations, well past what a builder needs to display).

- **Candidate technique(s):** cite `lemmas/finite-window-literalization-lemma.md`
  and `lemmas/singleton-side-fah.md` (already certified); apply with roles
  swapped per above. No new knowledge-base entry needed.

- **Cheap-kill candidates:** none needed — the check IS the cheap kill, and it
  succeeds (no obstruction found). The only "trap" to flag: don't let the
  builder try to literally substitute into the Lemma's stated variable names
  without first checking canonical order `n_A` vs `n_B` — `11305` has them
  swapped relative to `4807`, and a careless verbatim substitution could
  silently produce a wrong window interval.

- **Knowledge-base entries to use:** none beyond the workspace's own certified
  lemmas above (this is entirely internal machinery, not a knowledge_base.md
  citation).

- **Analogous past problems (cruxes):** not applicable — this is a pure
  internal-lemma reapplication task, not a fresh crux-corpus mining question.
  (The relevant crux precedent, aimo-0477's divisor-chain framing, was
  already the source of the underlying Singleton-Side FAH mechanism, credited
  in earlier rounds — nothing further to mine here.)

- **Prior progress:** round 26 closed `a_1=4807`'s residual class `d=13` via
  the Finite-Window Literalization Lemma (certified) and explicitly flagged
  `a_1=11305`'s recorded witness `x_2=103` as the natural next bounded task,
  untried. This round's exploration confirms it closes cleanly.

- **Dead ends (do not retry):** none new. The round-6-era note "`a_1=11305`
  gives `F'={11,103}`" (flagged historically as possibly measured at a wrong
  core) is independently reconfirmed correct at the properly-recruited `S₀`
  — not a dead end, just a fact that happens to also hold at the right core.
  (Separately, `cofinite-window-capacity-bound`'s claim of "`D_bad=∅` for
  `a_1=11305`" at line 2859 was explicitly noted as measured at the WRONG
  core `S₀=Q` in that file — do not confuse it with this round's `D_bad(11)=
  {103}` at the correctly recruited core; they are not in tension, just
  different cores.)

- **Small-case / intuition notes (labeled as conjecture where applicable):**
  The pattern across both known hard test seeds is now: one canonical
  witness is already a natural singleton (giving one side literal FAH for
  free), and a non-canonical witness of the OTHER extended type, located by
  search, is also a singleton with the SAME prime, closing the other side
  via the finite-window trick. This is exactly the same mechanism twice, on
  the only two properly-recruited-core hard seeds known in this workspace.
  It is **not** evidence of a general theorem — both closures are entirely
  ad hoc computational facts about these two specific integers (the
  existence of `x_1=72` / `x_2=103` as matching singleton witnesses is not
  derived from any structural argument, only found by search on this seed).
  **Ceiling assessment (explicitly requested by dispatch):** building this
  out gives a **third data point at best** in a two-seed-and-growing family
  of single-seed literal-FAH closures — it does not touch H1 (general FAH)
  at all, and there are only two known seeds in this category in the whole
  workspace (`4807`, `11305`) after ~26 rounds of search for hard rogue
  pairs. There is no visible route from "close seed #2 too" to "close the
  general theorem" — the mechanism's existence hypothesis (a matching
  singleton witness on the far side) remains exactly as open in general as
  it was before. Given this, I'd rate this as a **low-value builder slot**
  this round if the goal is to move H1/H2 forward: it is essentially free
  (I've already done the whole check above, a builder would just need to
  write it up, ~30-60 min of transcription), so it could be assigned as a
  quick "housekeeping" build if a slot is otherwise idle, but it should NOT
  be prioritized over any approach that has a chance at new structural
  content (e.g. the still-open Minimal-Window Necessity Conjecture on
  `a1-pq-subfamily-theorem`, or a genuinely new H1/H2 corridor). If assigned,
  it should be scoped explicitly as "close `covering-system-construction`'s
  second single-seed instance, no claim beyond that" so the reviewer doesn't
  need to spend much time on it beyond re-checking the (already fully
  displayed above) computation.
