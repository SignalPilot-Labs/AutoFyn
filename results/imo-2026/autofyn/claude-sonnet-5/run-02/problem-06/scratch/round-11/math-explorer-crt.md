# math-explorer report — CRT / multiplicative-structure lens on FAH (round 11)

## Assignment
Investigate whether the multiplicative/CRT structure of `a_1` (residues of small
numbers mod primes in `Q`, CRT class of `a_1` mod `∏Q`, exponents in `a_1`'s
factorization, or the *order* in which primes get recruited) encodes
identity-level information that could pin down which prime `q` divides an
arbitrary far term of a rogue pair's absorbed type — i.e. a genuinely new
mechanism for FAH / Symmetric FAH / Cofinite FAH.

## What I did
Reconstructed the certified pipeline from scratch in Python (independent
implementation, not copy-pasted from any approach file): greedy sequence
generator, `Q = P(a_1)`, base types `τ(n) = P(a_n)∩Q`, persistence via
tail-frequency, `N_0`, minimal witnesses `m_B`, core `S₀ = Q ∪ ⋃(P(a_{m_B})\Q)`
per the Finite Core Theorem, extended types `ρ(n) = P(a_n)∩S₀`, extended
persistence, rogue pairs (disjoint extended-persistent types with different base
types), Lemma-G witness indices `n_A<n_B`, and the Lemma-G prime `q`. Verified my
reconstruction against the workspace's own numbers on `a_1=4807`
(`a_6=4845=3·5·17·19`, `a_7=4862=2·11·13·17`, exact match) — confidence the
pipeline is faithful.

Tested on the assigned seeds `4807, 11305, 209, 247, 175`, plus `12, 45, 50, 63,
99` (small non-squarefree/varied seeds to probe exponent effects), `N` up to
8000 terms.

## Findings

**1. `q` is not a function of `a_1`'s CRT/residue data alone — it is dynamically
determined.** Across every rogue pair found (209→q=7, 247→q=3, 4807→q=17), `q`
is the *same single prime* for every rogue pair sharing a given `a_1`, but there
is no algebraic formula from `Q` or `a_1`'s residues that predicts it: it is not
"smallest prime outside `S₀`" (fails on 4807: 13∉S₀ is smaller than q=17 but is
not the Lemma-G witness because `13 ∤ a_6`, only `a_7`), nor any simple
CRT-residue rule I could find (`a_1 mod q` gives 209 mod 7 ≡ −1, 247 mod 3 ≡ 1,
4807 mod 17 ≡ 13 — no common pattern). `q` is whatever prime the greedy process
*happens* to place at both canonical witness indices `n_A, n_B`; that placement
is a consequence of the full trial-by-trial minimality search, not of `a_1`'s
factorization read off in isolation. This directly matches — and gives an
independent, 4th-style confirmation of — the workspace's existing diagnosis
(`same-type-free-facts-vacuity.md`): any tool built from `gcd` of two
**same-type** occurrences only ever recovers primes already in the type (hence
in `S₀`), never `q`. A CRT argument trying to *derive* `q`'s identity from `a_1`
algebraically is chasing something the dynamics — not the arithmetic of `a_1`
alone — decides.

**2. A genuinely interesting empirical regularity — but it turns out to be
periodicity in disguise, not new information.** Tracking consecutive
occurrences of the same rogue extended type `A'`, the **value gaps
`a_{n_{k+1}} − a_{n_k}` are always exact multiples of a fixed unit**
`U_{A'} = 2·q·rad(A'\{2})` (i.e. `2` times the product of the odd primes of
`A'` times `q`):
- `a_1=209`, `A'={3,11}`, `q=7`: unit `= 2·3·7·11 = 462`; observed gaps
  `462, 924, 462, 924, ...` (exact multiples, 218 occurrences checked).
- `a_1=247`, `A'={7,13}`, `q=3`: unit `= 2·3·7·13 = 546`; observed gaps
  `546, 1092, 1638, ...` (319 occurrences, all exact multiples).
- `a_1=4807`, `A'={3,5,19}`, `q=17`: unit `= 2·3·5·17·19 = 9690`; observed gaps
  `9690, 19380, 29070` (11 occurrences, all exact multiples).

This is a real, clean, CRT-flavored fact (the "recruited" sub-sequence of a
fixed type lives on an arithmetic-progression skeleton with common difference a
multiple of `2·q·rad(A')`). **But it is exactly the shape of the *conclusion* of
the whole IMO problem (eventual periodicity `a_{n+T}=a_n+L`), not a new premise.**
It is already anticipated by `approaches/reversible-transition-map.md`'s
Step 1–3 apparatus (`L=∏_{p∈S₀}p`, state `σ_S(n)=P(a_n)∩S`, residues mod `L`
identified with prime-membership data "by CRT"), which that file already proved
is **logically equivalent to gap (†)/FAH itself**, not an independent route to
it — assuming the type sequence is eventually a fixed-gap arithmetic progression
already presupposes the periodicity the problem asks to prove, and (for `q`'s
persistence specifically) already presupposes FAH. So this regularity is
consistent evidence for FAH/periodicity, but using it as a *proof mechanism*
would be circular — it needs FAH already established to explain why `q` stays
locked into the recruited unit forever, which is the very thing at issue.

**3. Zero FAH counterexamples again, on new/varied seeds too**, reinforcing
prior rounds' finding: no failures in any rogue pair found (0 fails / up to
1913 occurrences per pair, over 3 seeds with rogue pairs; `11305`, `175`, and
the small seeds `12,45,50,63,99` had **no rogue pairs at all** at the computed
`S₀** in the tested range** — i.e. FAH was vacuously/immediately satisfied,
consistent with earlier rounds' report that small/simple seeds tend to resolve
without ever entering the genuinely open regime).

**4. Exponent structure**: all tested seeds are squarefree or have Q built from
squarefree `a_1`'s (12, 45, 50, 63, 99 do have repeated prime factors in `a_1`
itself, e.g. `45=3²·5`) — none of these produced a rogue pair to test, so I got
no signal on whether `a_1`'s *exponents* (as opposed to which primes divide it)
matter. This sub-question is untested, but given finding #1 (that `q`'s
identity is dynamically not algebraically determined) I don't expect exponents
to help either — they're more `a_1`-CRT-class data of exactly the same "no
identity information" character.

**5. Crux corpus.** Queried `past_crux_moves_database.json` filtered to
`number_theory` / `modular-arithmetic-and-CRT` (112 entries) and skimmed for
anything matching "greedy minimal-legal-integer construction" or "decompose a
process prime-by-prime via CRT." Nothing in the corpus attacks a structure
resembling this problem (an iteratively-defined greedy sequence with a
minimality rule); the closest thematically relevant idea (`aimo-0231`:
decomposing a first-hitting-time modulo `N` as an lcm over independent
prime-power components via CRT) doesn't transfer, because in our problem the
"legality" condition (`gcd(a_{n+1},a_i)>1` for *all* previous `i` simultaneously)
is a fundamentally joint, not per-prime-independent, constraint — precisely the
`S-sufficiency` framing `reversible-transition-map.md` already formalized and
showed is equivalent to (†) itself, so a "solve each prime's residue-class
sub-problem independently, recombine by CRT" strategy doesn't have an
independent handle to exploit; it's the same equivalence restated.

## Verdict: dead end for a new mechanism, but a useful independent confirmation

The CRT/multiplicative-structure-of-`a_1` lens does **not** open a genuinely new
route to FAH. Two independent findings converge on why:
- `q`'s identity is fixed by the greedy dynamics (which specific prime lands at
  the two canonical witness indices), not recoverable from `a_1`'s residues,
  exponents, or recruitment order read off in isolation (finding #1).
- The one clean CRT-shaped regularity that *does* exist empirically (fixed-unit
  value gaps within a type, finding #2) is provably equivalent to — not
  independent of — the periodicity/FAH conclusion itself, per the already-
  certified equivalence in `reversible-transition-map.md` Step 2. Using it to
  prove FAH would beg the question.

This is a 5th independently-framed technique family (after: algebraic-magnitude
sandwich, quantitative-window growing-constraint, definitional-tautology,
existential-to-universal counting) landing on the same wall: every tool
available — including CRT/residue structure of `a_1` — only ever supplies
`S₀`-level (type-membership) or single-witness information, never
identity-level information about an outside-core prime `q` at an arbitrary far
index. No counterexamples to FAH were found (reinforcing, not weakening, the
belief that FAH is true); the obstruction is to *proving* it with the currently
available toolkit, CRT included.

## Recommendation for next round
Do not pursue `a_1`-CRT-structure as a standalone new mechanism. If the run
wants a genuinely different framing (per the orchestrator's "break a shared-gap
plateau" rule), it should look for a source of **cross-occurrence** information
that isn't gcd-based existence/magnitude at all — e.g., an extremal/minimality
argument that uses the *greedy* choice of `a_{n+1}` as literally the smallest
legal integer (not yet exploited as an ordering constraint beyond
`minimality-tautology-lemma.md`) to force a contradiction if `q` were ever
absent from a far A'-type term, rather than trying to construct or predict `q`
algebraically in advance.
