# Proof-builder report — sunflower-bundle-closure, round 12

Task: attempt to close Conjecture (JW) for "Case B" pairs (`247:(13,19)`,
`4199:(13,17)`) via the round-12 outline's Step 4′ idea (apply the
already-certified Lemma NIDF injection argument directly to the
escape-prime set of a clashing trace-type pair), per the outline-reviewer's
scoping. Result: **Status stays `partial`** — the gap is not closed, but
two pieces of genuine new rigorous content were produced this round.

## What was done

1. Read the full approach file (`results/imo-2026-06/approaches/
   sunflower-bundle-closure.md`, 1953 lines pre-round), `current.md`, the
   round-12 outline-reviewer report, and the certified lemma files
   (`lemma-CB-core-blocking.md`, `lemma-XC-NIDF-FT-cross-companion-
   transversal.md`, `lemma-ERD-realized-blocked-dichotomy.md`).
2. Built a fresh, independent greedy-sequence generator (own Python +
   `sympy.factorint`) and reproduced the file's own §7.5 numbers exactly
   (`a_1=247`: `|I_{13}|=10764,|I_{19}|=6910` at `N=20000`) before trusting
   any new computation.
3. Re-derived round 11's refuted `Π` counterexample from scratch
   (`i=51,j=739`, escape prime `3`, `Π=\{2,5,7\}`) — exact match, confirms
   the generator and the "do not reuse" instruction.
4. Attempted the Step 4′ idea directly: for the fixed candidate `Π=\{2,5,7\}`,
   computed all ~9.5M clashing cross-pairs and their escape-prime
   multiplicities; found prime `3` alone accounts for 100% of clashes
   (matching the known fact `Π'=\{2,3,5,7\}` has zero violations). Drilled
   into a specific fixed trace-type pair (`τ=\{7\},τ'=\{2\}`, 2.5M
   sub-pairs) and found the same 100%-coverage-by-`3` phenomenon there too.
5. Attempted to turn this into a general proof via the NIDF-pigeonhole
   injection technique (fixing one side's index, bounding escape primes by
   a fixed companion set) and identified precisely why it does not
   generalize: the technique only bounds witnesses through ONE fixed
   reference index on one side; nothing in the certified toolkit (Lemma
   P′, XC, NIDF, FT, CB, Escape-Confinement) relates companion sets of two
   different indices on the same side, so the union over the whole
   infinite class is not controlled. Wrote this up as the "Row-Restriction
   Obstruction" (§9.2 of the approach file) — a genuine structural
   diagnosis, not just a numeric stall, and explained why Case B pairs
   (by their defining lack of a class-wide backbone) specifically block
   the shortcut that closes Case A.
6. Built a new, concrete refinement attempt: **Matched-Witness
   construction** — using the already-certified Lemma CB + Escape-
   Confinement Lemma but with smarter witness selection (search for
   witnesses with companion set exactly `\{2,3\}`, rather than round 11's
   "first witness found," which gave mismatched sets). Found matched
   witnesses (`\{2,3\}=\{2,3\}`) on BOTH mandatory Case B instances
   independently (`247:(13,19)`: witnesses `a_6=312,a_7=342`; `4199:(13,17)`:
   witnesses `a_2=4212,a_{11}=4332`). Verified one-sided coverage is
   exhaustive (zero exceptions) on both tested ranges.
7. **Refuted** the matched candidate `Π_mw=\{2,3\}` on both instances with
   explicit, small, hand-verifiable counterexamples: `247`: `a_2=260=
   2^2\cdot5\cdot13`, `a_5=285=3\cdot5\cdot19`, `\gcd=5\notin\{2,3\}`.
   `4199`: `a_9=4316=2^2\cdot13\cdot83`, `a_5=4233=3\cdot17\cdot83`,
   `\gcd=83\notin\{2,3\}`. All factorizations and gcds independently
   re-verified via `sympy.factorint`/`math.gcd` (exact match to hand
   computation, shown in the file).

## Outcome

Status remains `partial`. No new certifiable lemma promoted this round —
the two new results (Row-Restriction Obstruction, Matched-Witness
construction + refutation) are instance-specific/diagnostic content
directly tied to Case B's open gap, not general-purpose reusable lemmas in
the sense of this workspace's lemma cache. The gap is honestly reported as
open, with the precise missing ingredient restated (§9.5 of the approach
file): a cross-index linking fact between companion sets of different
indices on the same side, not derivable from any currently certified tool.

Files touched:
- `results/imo-2026-06/approaches/sunflower-bundle-closure.md` (updated in
  place; +420 lines, new §9 with full proofs, updated headline/Approaches-
  tried sections; Status unchanged at `partial`).

No `results/imo-2026-06/lemmas/*.md` file was added this round.
