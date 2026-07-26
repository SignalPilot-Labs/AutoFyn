# imo-2026-01 — outline review (round 1)

Two new slugs, both rest on the same verified core (per-prime subtractive-Euclidean
exponent step ⇒ g_p invariant ⇒ M = ∏ p^{g_p}; (W,C) = (ΣΩ, #{>1}) lex-decreases
every move ⇒ termination). The three explorers independently converged on this
core and numerically verified M = ∏ p^{g_p} and termination on ~13 boards
({4,8},{12,18},{16,64},{2,3},{4,16,2},{12,18,6},{6,10,15},{8,8,8},{4,8,16},
{100,75,30},{30,42,70,105},{2,3,5,7},{12,18,24,30}) with ~5000-step runs on
n=2026. I re-ran the simulation: every play-out terminated with a single entry
matching Q. The core is sound.

## Cross-cutting catch (applies to BOTH skeletons) — missing subcase in the (W,C) casework

The three move cases are listed as {coprime (g=1), equal (m=n), intermediate
(g>1, a>1, b>1)}. The "intermediate" case as literally stated is **too narrow**:
it excludes the real subcase **g>1, m≠n, exactly one of a,b = 1** — e.g.
{4,8}→{4,2} (g=4,a=1,b=2), {9,27}→{9,3} (g=9,a=1,b=3), {2,4}→{2,2}
(g=2,a=1,b=2). I verified computationally: in this subcase ΔW = −Ω(g) ≤ −1
and ΔC = 0 (since g>1 and ab = b > 1, so both new entries stay >1) — exactly
the same (W,C) behavior as the listed "intermediate" case. So the descent
conclusion still holds; only the **case description is incomplete**.

**Fix (builder):** broaden the third case from "g>1, a>1, b>1" to
"**g>1 and m≠n**" (equivalently "g>1 and ab>1", equivalently "g>1 and not the
equal case"). The ΔW=−Ω(g), ΔC=0 computation is identical. The three exhaustive,
disjoint cases then become: {g=1}, {m=n}, {g>1 and m≠n}. This is a
CHANGES-REQUESTED-level gap, not fatal — flag it so the builder closes it while
filling the proof.

## invariant-first — CHANGES REQUESTED

Strategy sound; the invariant-first routing (pin M and M≥2 from g_p BEFORE
proving termination, then attach (W,C) for the terminal-state existence, then
bridge termination⇒≤1 + Q≥2 forbids 0 ⇒ exactly one) is valid end-to-end and
targets the full claim (a)+(b). Load-bearing lemmas each carry a stated
mechanism (Euclidean identity gcd(a,b)=gcd(min,|a−b|); ΔW=−Ω(g) via
Ω-additivity on coprime factors; terminal ⟺ ≤1 entry >1 via move legality;
M=Q via the lone-M valuation multiset). No circular reasoning. Dead ends
(gcd-of-numbers, min-of-exponents, level-set count, gcd-lattice, sole-product)
are all correctly recorded as failed — I re-verified {4,8}→{4,2} kills the
first three. The (a,0)→(0,a) sub-case for the invariant is correctly flagged.

Issues to close while building:
1. **Case partition** (see cross-cutting catch above): broaden "intermediate"
   to "g>1 and m≠n".
2. **Step 2/3 gap:** state g_p well-definedness and gcd(0,k)=k convention
   explicitly; show the (a,0)→(0,a) preservation (gcd(a,0)=a=gcd(0,a)).
3. **Step 5 gap:** argue finiteness (only finitely many primes divide the
   finitely many initial entries) and Q≥2 (every initial entry >1 ⇒ some prime
   divides some entry ⇒ g_p≥1 there ⇒ Q≥2).
4. **Step 6 gap:** confirm lcm/gcd is always a positive integer (g|lcm since
   g|both m,n ⇒ g|lcm) and that "no two entries >1" is the sole obstruction to
   a move.
5. **Step 7 gap:** full ΔW=−Ω(g) derivation with the
   Ω(ab)=Ω(a)+Ω(b) coprimality justification, and the explicit three-case
   table (with the broadened third case).
6. **Step 8 gap:** make the contradiction chain explicit (all-1s ⇒ all v_p=0
   ⇒ all g_p=0 ⇒ Q=1, contradicting Q≥2 which is invariant).

## monovariant-first — CHANGES REQUESTED

Strategy sound; the monovariant-first routing (lead with (W,C) lex-descent for
termination and terminal ≤1 entry >1, then bring g_p in only to rule out
all-1s and pin M) is the genuine alternative ordering — it proves part (a)'s
"finitely many moves" purely from the monovariant before the invariant is
introduced, whereas invariant-first relies on the invariant for the "exactly
one" upgrade. Same verified core, same dead-ends recorded, same lemma
mechanisms stated. The factorization m=ga, n=gb with gcd(a,b)=1 and the
lcm/gcd = ab derivation are correctly sketched.

Issues to close while building (mirror the invariant-first list):
1. **Case partition** (see cross-cutting catch above): broaden "intermediate"
   to "g>1 and m≠n".
2. **Step 3 gap:** justify Ω(ab)=Ω(a)+Ω(b) from gcd(a,b)=1 (additivity on
   coprime factors — not "obvious"); confirm the three cases are exhaustive
   and disjoint.
3. **Step 6 gap:** full g_p invariant proof including the (a,0)→(0,a)
   sub-case and gcd(0,k)=k; OR import a certified lemma from
   results/imo-2026-01/lemmas/ if one exists (it does not yet — both builders
   will prove it independently this round; a shared lemma should be proposed
   and reviewer-certified so the other can import it next round).
4. **Step 7 gap:** finiteness + Q≥2 argument.
5. **Step 8 gap:** the contradiction chain.

## Diversity note for the orchestrator

The two approaches are genuinely different **routings** (which half is proved
first) but share the **same core** (g_p invariant + (W,C) monovariant). This
is the single-core-field risk: if a subtle flaw emerges in the shared core
(e.g. the (a,0) sub-case, or the "exactly one" bridge), both die together.
The outliner explicitly investigated and rejected third framings (gcd-lattice
not preserved; magnitude weights fail on coprime moves) as dead ends, so the
honest field is 2 approaches — the core IS the solution. Accept the field for
round 1, but if both stall on the same step for 3+ rounds, push next round's
outliner for a genuinely different framing (the explorer's "per-prime
independent Euclidean game / ideal-theoretic" structural view, route 3 of
math-explorer-invariant.md, is the most distinct framing still alive and could
be branched as a third approach if the shared core hits trouble).

## Ranking

Both registered at cold-start Elo 1500. Both are unproven newcomers sharing one
verified core — a draw is the honest call (no evidence yet to separate them;
their prospects are symmetric). One draw comparison recorded.

## Build set

Both slugs are viable and genuinely different routings; building both in
parallel lets the proof-reviewer compare them adversarially. Dispatch one
proof-builder per slug; each builder must close the cross-cutting case-partition
gap and the per-step gaps listed above.

build set: invariant-first, monovariant-first
