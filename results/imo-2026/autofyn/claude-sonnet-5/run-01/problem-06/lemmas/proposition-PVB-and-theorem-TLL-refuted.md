# Proposition PVB (`P′`-Vacuity Barrier) + Theorem TLL-Refuted

**Source.** `approaches/sunflower-inadmissibility-toolkit.md`, §11–13
(round 13).

**Purpose.** Two negative results that jointly rule out an entire family
of "certify Backbone Permanence from a short/moderate observed repeat"
mechanisms for the running companion-set intersection `B_k` of a
doubly-infinite class `I_{S'}` (Lemma BS,
`lemmas/lemma-BS-backbone-stabilization-and-theorem-CAC.md`). Directly
answers this round's own outline question ("can a flat run of the chain
be followed by yet another decrease?") — **yes**, rigorously, with
explicit counterexamples, refuting the "Early/Bounded Stabilization"
(EBS) sub-conjecture as literally proposed this round.

## Proposition PVB (`P′`-Vacuity Barrier)

**Statement.** Let `S'\subseteq P_1` be any core and `i,j\in I_{S'}` two
distinct indices (so `S(i)=S(j)=S'`). Then the already-certified Lemma P′
applied to `\{i,j\}` supplies **no** constraint relating
`\mathrm{comp}(a_i)` to `\mathrm{comp}(a_j)` — its conclusion
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing` holds
automatically, for every possible pair of companion sets, including
completely disjoint ones.

**Proof.** `S'\ne\varnothing`; fix `p\in S'`. `p\in S'\subseteq
\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)` since `S(i)=S(j)=S'`. So `p`
witnesses the intersection independent of the companion sets.
`\blacksquare`

**Corollary.** Lemma UCR's proof mechanism (which extracts information
from Lemma P′'s guaranteed intersection precisely because two *disjoint*
cores force the intersection to come from the companion parts) cannot be
transplanted to a within-class (same-core) permanence claim: the
guaranteed intersection is already fully accounted for by the shared core
itself, leaving zero information about the companion parts. No proof of
EBS/Backbone Permanence can proceed via Lemma P′ or Lemma UCR applied to
a pair of same-class indices.

## Theorem TLL-Refuted (Two-in-a-Row / `K`-in-a-Row Locking Fails)

**Statement.** The "two-in-a-row locks it" dichotomy (and, more
generally, any small a-priori-uniform bound on the running-intersection
stabilization index `k_0`) proposed as a mechanism for EBS is **FALSE**.

**Proof (three independently cross-validated counterexamples).**

1. **`a_1=375` (`P_1=\{3,5\}`, same `|P_1|=2` structure as the mandated
   `2747`, `4087`), core `\{3\}`.** Sequence `375,378,380,384,390,396,
   399,\dots` (independently reproduced exactly, cross-validated against
   a naive brute-force generator, byte-for-byte match). `I_{\{3\}}`
   restricted to `n\le7`: `a_2=378` (`\mathrm{comp}=\{2,7\}`), `a_4=384`
   (`\mathrm{comp}=\{2\}`), `a_6=396` (`\mathrm{comp}=\{2,11\}`), `a_7=
   399=3\cdot7\cdot19` (`\mathrm{comp}=\{7,19\}`). Running intersection:
   `B_1=\{2,7\}`, `B_2=B_3=\{2\}` (two consecutive members agree —
   "two-in-a-row" triggers in its literal strongest form), `B_4=
   \{2\}\cap\{7,19\}=\varnothing` — a proper subset one step later.
2. **`a_1=4199`, core `\{13,19\}`.** `a_{16}=4446` and `a_{90}=5928` both
   have `\mathrm{comp}=\{2,3\}` (literally identical, not merely equal
   running-intersections) — the strongest possible "two-in-a-row." This
   value persists as the running intersection for `24` consecutive class
   members, then breaks: `a_{1854}=41002=2\cdot13\cdot19\cdot83`
   (`\mathrm{comp}=\{2,83\}`), `B_{24}=\{2\}\subsetneq\{2,3\}`.
3. **`a_1=4199`, core `\{17,19\}`.** Running intersection `\{2\}`
   (established at `a_{54}=5168`) persists for `108` consecutive class
   members (`a_{54}` through `a_{3821}=80104=2^3\cdot17\cdot19\cdot31`),
   then breaks at `a_{3840}=80427=3\cdot17\cdot19\cdot83` (odd),
   `B_{109}=\varnothing`.

All twelve cited term values independently confirmed via `sympy.
factorint`. `\blacksquare`

## Independent re-verification (proof-reviewer, round 13)

Wrote a fresh, independent generator (both a naive O(n²) brute-force
version and a fast antichain-optimized version, cross-validated against
each other on the first 30 terms of `a_1\in\{375,4199\}`) and:
- Reproduced `a_1=375`'s full sequence `375,378,\dots,426` exactly (13
  terms), confirmed the `I_{\{3\}}` class membership and companion sets
  for `n=2,4,6,7` exactly as claimed, confirmed `B_1=\{2,7\},B_2=B_3=
  \{2\},B_4=\varnothing` exactly.
- Regenerated `a_1=4199` to `N=4000` terms (0.3s with the fast
  generator), extracted `I_{\{17,19\}}` (115 members to this depth) and
  `I_{\{13,19\}}` (53 members): confirmed the running intersection for
  `\{17,19\}` is `\{2,7\}` at position 0, `\{2\}` from position 1 through
  **exactly** position 108 (`n=3821`, `a=80104`, `\mathrm{comp}=\{2,31\}`),
  breaking at position 109 (`n=3840`, `a=80427`, `\mathrm{comp}=\{3,83\}`)
  — exact match. Confirmed the `\{13,19\}` running intersection is
  `\{2,3\}` from position 0 through position 23 (24 members, `a_{16}`
  through `a_{1804}=40014`), breaking at position 24 (`n=1854`,
  `a=41002`, `\mathrm{comp}=\{2,83\}`) — exact match.

No gap found. Both counterexamples independently and exactly reproduced.

## Certification

Certified `solved`-quality (sorry-free). Reusable as a standing negative
result: rules out an entire family of "certify permanence from a
short/moderate observed repeat" mechanisms for Backbone Permanence,
`(MRS_S)`, or any other running-intersection stabilization claim in this
workspace. Does **not** show Backbone Permanence is false in general, nor
for `2747`/`4087` specifically — only that the specific "two-in-a-row" (or
any small uniform-bound) mechanism cannot certify it. `2747` and `4087`
remain open; a correct proof of Backbone Permanence for them, if one
exists, must be a structural argument specific to their `P_1`, not an
observation-based/finite-descent one.
