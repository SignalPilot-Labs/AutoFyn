## imo-2026-06

**Assignment.** Investigate whether a bespoke, ad hoc argument closes FAH specifically
in the `|F''|=2`, multiplicity-1 case (Reduced-Alphabet Corollary's `|D_bad(q*)|=1`
shape), rather than the general `|F'|,|F''|≥2` case.

### What I verified computationally (fresh, independent reimplementation)

I regenerated both standing `|F''|=2` seeds from scratch (plain Python, `math.gcd`,
no reuse of prior scripts) to N≈30,000–40,000 terms each, factored every term with
sympy, and directly recomputed the rogue pair / `S₀` / `F'`/`F''` data:

- **a_1=4807**: `S₀={2,3,5,11,19,23}`, `a_6=4845=3·5·17·19` (`n_A=6`, `A'={3,5,19}`),
  `a_7=4862=2·11·13·17` (`n_B=7`, `B'={2,11}`), `F'={17}` (singleton — resolves the
  B'-side via Singleton-Side FAH), `F''={13,17}`, `b=221=13·17`, `D_bad(17)={13}` —
  exactly reproducing the certified lemma's numbers. Checked **all 62** later
  A'-type occurrences up to n≈2223 (extended run to N=40000, `a_N≈702886`): **0/62**
  land in `D_bad` (the bad class `13`-only never occurs); **0** land in "neither"
  (i.e. Confined-GCD's `g_n|b, g_n>1` prediction is confirmed exactly, no violations).
- **a_1=11305**: `S₀={2,3,5,7,13,17,19,23,29,37,43,101}`, `a_4=11319=3·7³·11`
  (`n_B=4` in time, `B'={3,7}`, singleton side prime is `q*=11`), `a_7=11330=2·5·11·103`
  (`n_A=7` in time, `A'={2,5}`), `F'={11,103}`, `F''={11}`, `b=1133=11·103`,
  `D_bad(11)={103}` (matches `cofinite-window-capacity-bound`'s corrected computation
  — the file's earlier "D_bad=∅" line is a stale/mis-simplified intermediate
  statement it itself corrects two lines later to `D_bad={103}`; do not cite the
  "∅" phrasing). Checked **all 913** later A'-type occurrences to N=30000
  (`a_N≈253022`): **0/913** land in `D_bad` (bad class `103`-only never occurs), 0
  in "neither."

So across **975 total tested occurrences over two independently-verified seeds**, the
bad class is **never** hit — stronger than "cofinite," looking like literal FAH with
zero exceptions in both concretely-tested instances (this is *evidence*, not proof —
sample sizes are still small relative to "for all n").

### Distinct openings tried for a bespoke |F''|=2 mechanism

1. **"Universal-prime-vs-single-culprit" multi-witness pigeonhole** (my own idea,
   specific to this narrow case): since `F'` (or `F''`) is a singleton `{q'}`,
   Singleton-Side FAH gives `q'|a_m` for *literally every* later occurrence `m` of
   the opposite type, not just the anchoring witness. So a hypothetical bad index
   `n` (of the open-side type, with `q*∤a_n`) must, to satisfy Free Facts against
   **every** one of the (growing, unboundedly many as `n→∞`) prior opposite-type
   occurrences individually, find *some* outside-`S₀` prime shared with each one —
   and since `a_n` has only finitely many prime factors while the number of prior
   witnesses grows, pigeonhole forces some prime of `a_n` to cover a growing number
   of them. This looked promising at first (it uses the *stronger*, all-occurrences
   form of Singleton-Side FAH, not just the one-witness Confined-GCD/Bounded-Witness
   form other approaches have used) — **but it collapses into exactly the same
   already-dead mechanism**: `Q := P(a_1)` is fixed by definition
   (`persistent-type-pigeonhole.md`) and is *not* defined as "primes dividing a
   positive density/infinitely many terms," so a prime covering many prior
   occurrences need not already be in `Q` or in the current `S₀` — it is exactly the
   "recruit a new prime" step of the covering-system-construction's recruitment
   process, already shown (round 9, Recruitment-Budget Lemma) to fail: the escaping
   prime can differ occurrence-to-occurrence with nothing forcing it to stabilize
   into a single universal culprit. Verified this is the same wall by checking the
   argument against the certified **Escape-Cost Vacuity Theorem**'s class-blind
   diagnosis — my pigeonhole step never actually reads off `g_n`'s specific value,
   only existence of *some* covering prime, so it is existential, not the needed
   class-sensitive "always/only this one" statement. **Dead — do not retry.**
2. **Small-alphabet 2-coloring / finite-automaton idea**: since `D_bad(q*)` is a
   single divisor class, one might hope to encode "type-A' occurrence divisible by
   `q*`" vs "not" as a 2-state automaton on the residue-mod-`L₀` graph and show the
   bad state is transient. This is EXACTLY the `EEA`/subword-complexity framing
   already certified this workspace (round 12, `eea-implies-periodicity.md`): "safe"
   residues give a deterministic successor, and proving a *given* ambiguous residue
   becomes safe after recruitment is, after unwinding, again literal (non-cofinite)
   FAH for that instance (round 12 §5, independently reconfirmed). Restricting the
   alphabet to `|D_bad|=1` does not change this — the automaton's transition
   function is still undetermined at the ambiguous residue for exactly the same
   reason (the successor depends on gcd against *all* earlier terms, which the
   finite core does not summarize). **Same wall, no shortcut from alphabet size.**
3. **Size/parity argument on the two primes `p=q*, r` themselves** (checked and
   ruled out as a possible cheap win): tested whether `p<r` or `p>r` correlates with
   which one "wins" — no: 4807's winning prime is 17 (the *larger* of {13,17}),
   11305's winning prime is 11 (the *smaller* of {11,103}). No monotone
   size/parity pattern to exploit; this specific cheap-kill idea is falsified by
   the two available data points (not the sought mechanism).

### Cheap-kill candidates
None found that work — checked size ordering of `{q*, r}` (falsified, no pattern),
multiplicity structure (both cases squarefree `b=p·r`, `e_p=e_r=1`, no further
structure to exploit beyond what Reduced-Alphabet Corollary already extracts).

### Candidate technique(s)
None beyond what's already certified. The narrowing from "finite alphabet `D_bad`"
to "singleton alphabet" is a genuine simplification in *degree* (one class to rule
out instead of several) but not in *kind*: every certified screening tool
(Escape-Cost Vacuity, Same-Type Free Facts Vacuity, EEA's equivalence-to-FAH) applies
identically regardless of `|D_bad|`, and my own fresh attempt (multi-witness
pigeonhole using the *all-occurrences* strength of Singleton-Side FAH, not just the
single-witness Confined-GCD form) reduces to the same dead
existential-to-universal-promotion obstruction.

### Knowledge-base entries to use
None beyond what's already imported (Pigeonhole, CRT — both already fully deployed
in the certified stack). Nothing in `knowledge_base.md` on covering systems /
Dirichlet gives a new class-sensitive linking fact between `g_n` at different `n`;
this is consistent with all 16 confirmed-dead mechanisms in the workspace.

### Analogous past problems (cruxes)
Did not run a fresh corpus query this round (my lens was bespoke-computation, not
corpus search) — defer to other explorers' corpus findings this round; the shared-gap
diagnosis (need a fact linking two *different* later occurrences' gcd values, not
obtainable from pigeonhole/magnitude/counting alone) is unusual enough that I would
not expect a close analogue without a fresh corpus pass.

### Prior progress
Unchanged from `current.md`/round 12: FAH/Cofinite FAH (≡ EEA at a finite core)
remains the sole open crux, now 15 mechanisms confirmed dead. This round's bespoke
`|F''|=2` attempt is a **16th** dead mechanism (my multi-witness pigeonhole idea),
though it does sharpen the empirical picture: the bad class is not just "rare," it
is **empirically zero** across 975 tested occurrences in the two known instances —
worth flagging to the outliner as slightly stronger-than-"cofinite" computational
support (literal FAH, not just cofinite FAH, may be the right target to conjecture
and eventually prove in this narrow regime, though of course still unproven).

### Dead ends (do not retry)
- My own new idea this round: "multi-witness pigeonhole via Singleton-Side FAH's
  all-occurrences strength" — reduces to the round-9 Recruitment-Budget Lemma's
  refuted mechanism (escaping prime not forced to stabilize). Do not re-attempt
  without a genuinely new ingredient forcing a *single* prime across *all* bad
  occurrences (not just each occurrence individually needing *some* prime).
- 2-state/finite-automaton bespoke framing for the singleton `D_bad` alphabet —
  collapses to the already-certified EEA equivalence (round 12); restricting
  alphabet size does not remove the "successor depends on all earlier terms"
  obstruction.
- Size/parity pattern between `q*` and the bad prime `r` — falsified by the two
  available data points (4807: winner is the larger prime; 11305: winner is the
  smaller prime).

### Small-case / intuition notes (conjecture only)
- Both known `|F''|=2`, multiplicity-1 seeds show **literal, zero-exception** FAH
  on the open side (975/975 occurrences resolved), not merely "cofinite" — this is
  new precision (prior rounds only tracked coarse divisibility rates like "~6%" or
  "~14%" at un-recruited cores; at the **properly recruited** `S₀` used here, the
  rate is 100%, 0 exceptions, in both seeds tested this round with much larger N
  than before, 40000/30000 vs prior rounds' ~1000–4000). This is consistent with
  (but does not prove) literal FAH being true in general, and suggests that IF a
  bespoke `|F''|=2` proof is ever found, it may be provable as a **literal**
  (all-n) fact rather than requiring the weaker cofinite-sufficiency machinery —
  potentially a simpler target for a future round than chasing "eventually" language.
  Still, no mechanism was found this round that supplies the missing class-sensitive
  ingredient; the narrow case is **not shown tractable** by anything discovered here.
