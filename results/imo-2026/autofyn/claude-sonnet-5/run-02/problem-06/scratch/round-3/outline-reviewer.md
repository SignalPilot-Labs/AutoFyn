# Round 3 outline review — imo-2026-06

Reviewed `/tmp/round-3/proof-outliner.md` against `results/imo-2026-06/current.md`,
the certified lemma files, and the round-3 dispatch's specific ask to scrutinize the
two "new framing" proposals against the single-gap trap.

## covering-system-construction (revise) — APPROVE

Steps 1–3, 5 unchanged and already certified. The two new pieces:

- **Canonical-Refinement Lemma**: mechanism checked and correct. `P(a_{m_B}) ∩ S₀ = B ∪
  F_{A,B}` exactly follows from the definitions of S (Finite Core Theorem) and F_{A,B}
  (every prime of `P(a_{m_B})` outside Q is in S by construction, so intersecting with
  S₀ ⊇ S loses nothing). Combined with the already-certified Step 4 fact
  `A' ∩ F_{A,B} ≠ ∅`, the chain `A' ∩ B'_can ⊇ A' ∩ F_{A,B} ≠ ∅` is valid, non-circular,
  and correctly scoped (only closes pairs where at least one side is canonical — the
  file explicitly disclaims the general case, which is the right level of honesty).
- **F_{A,B} ∩ F_{B,A} ≠ ∅**: mechanism (Free Fact 2 forces a shared prime; it can't be
  in Q since A∩B=∅) is a straightforward, correct corollary. The file correctly states
  this does NOT finish (†) — good, no overclaiming.
- **Residual localization (Step 5)**: this is now the ONLY open piece — non-canonical ×
  non-canonical pairs. The proposed minimal-counterexample mechanism is honestly
  flagged as unproved, not smuggled in.

No hand-waving, no case gaps, technique is right (this is exactly the kind of
set-refinement argument the knowledge base's covering-system material supports). Build.

## greedy-exchange-cost-potential (advance) — APPROVE

Correctly imports the new lemmas rather than re-deriving. The cost-boundedness
conjecture is explicitly labeled NOT proved, and the file is instructed not to
resurrect the two previously-refuted bounds (cost≤1, cost≤|𝒫|−1) — good discipline,
consistent with the round-2 falsification. This is a genuinely different vocabulary
(counting/exchange vs. set-refinement) attacking the same localized residual — legitimate
technique diversity on a shared crux, acceptable since it's paired with a leader
approach rather than substituting for real framing diversity. Build.

## witness-depth-bound (new) — CHANGES REQUESTED, with a falsified core claim to fix before building

This is a genuinely different top-level reduction (a priori index-depth bound instead
of recruitment-process termination) — real framing diversity, not a rehash. However,
I numerically tested its central claim before approving it as a build target (per
prior-round rule: falsify quantitative claims at outline time, not build time):

The outline states first-occurrence index of a persistent type is "bounded by an
explicit function f(|Q|) alone" — independent of a_1's magnitude. I simulated this
directly (trial-division greedy sequence generator, no sympy):

- `a_1 = 1155 = 3·5·7·11` (|Q|=4): max first-occurrence index across all persistent
  types = 113.
- `a_1 = 210 = 2·3·5·7` (|Q|=4): max first-occurrence index = 35.
- `a_1 = 96577 = 13·17·19·23` (|Q|=4, same size, larger primes): max first-occurrence
  index = **488**.
- `a_1 = 5005 = 5·7·11·13` (|Q|=4): max first-occurrence index = 213.

Same `|Q|=4` in all four cases, first-occurrence depth ranges from 35 to 488 — clearly
NOT a function of `|Q|` alone; it scales with the magnitude of the primes in Q. **The
claim as literally stated is false.** This must not be handed to the builder unmodified
(same failure mode as round 2's "universal glue prime" — a plausible-looking bound that
breaks once you vary prime magnitude, not just |Q|).

The good news: this does not kill the approach. The stated purpose was to get a bound
independent of *n* (the sequence's runtime behavior) to avoid circularity — and Q's
element values (not just |Q|) are known immediately from a_1 at n=1, before watching any
tail behavior. So a corrected claim — "first-occurrence index bounded by an explicit
function of a_1 (equivalently, of Q as a set including its element sizes), not of n" —
is still a priori, still non-circular, and still delivers the intended bypass of the
recruitment-process framing. Require the builder to restate the key lemma this way
before attempting to prove it, and to re-run a similar magnitude-scaling numeric check
themselves before investing in the pigeonhole-window mechanism.

Register and build with this correction attached — it is real diversity per the
dispatch's ask, not a rehash of the shared wall, provided the corrected (weaker, but
still useful) claim is what gets attempted.

## minimal-counterexample-glue (new) — RETHINK as a standalone population member

This is the one to scrutinize hardest per the dispatch. Its own file text gives the
game away: "this approach's target and the covering-system-construction's residual are
THE SAME underlying mathematical fact (†) restricted to non-canonical × non-canonical
pairs... if one builder closes it, the other approach should import the result rather
than re-deriving." That is not a rival approach to the *problem* — it is a second
attempted proof technique for one specific already-identified lemma inside
covering-system-construction's Step 5 (well-ordering/extremal vs. forward induction).
Every step outside that one lemma (Steps 1–4, the CRT finish) is imported verbatim.

Per CLAUDE.md: "Approaches that only differ in technique are too close: they hit the
same wall and fail together" and the single-gap-trap warning against splitting one
proof's dependency across sibling slugs. This is the mirror image of that trap: instead
of splitting one proof across slugs, it duplicates one slug's unresolved sub-lemma as a
second slug. If the residual (†) is genuinely hard, minimal-counterexample-glue's
"success" IS covering-system-construction's success and vice versa — they are not
independent population members, so ranking them separately inflates the appearance of
diversity without adding any.

The well-ordering/minimality idea itself has real merit (it grants an extra hypothesis —
"no smaller violation exists" — that forward induction never gets to use, a classic
technique flip that sometimes cracks a stuck induction). But the right place for it is
as an alternative sub-attempt on covering-system-construction's own Step 5, in the same
file, not a separately-ranked slug. Do not register it. Recommend the outliner fold the
minimal-counterexample mechanism into covering-system-construction's Step 5 next time
(or have that approach's builder try it as an alternative to the extremal-pair sketch
already there) instead of spending a build slot on a nominally-separate approach whose
outcome is definitionally identical to a sibling's.

This is exactly the failure mode the round-3 dispatch asked me to watch for — confirmed
present in one of the two "new" proposals, not the other.

## Diversity assessment (for the orchestrator)

- witness-depth-bound is genuine framing diversity (bypasses (†) rather than closing it),
  but its core claim needed a correction caught here rather than in the build round.
- minimal-counterexample-glue is NOT genuine diversity — it is a duplicate target of
  covering-system-construction's residual gap, wearing a different technique label.
  Declined as a standalone population member this round.
- The field otherwise still shares one crux ((†) / its non-canonical residual) across
  all three built lines. If witness-depth-bound's corrected claim also fails cleanly
  next round, the orchestrator should insist on a fourth, structurally distinct framing
  (e.g. something that avoids "persistent Q-type" language altogether) rather than a
  third technique variant on the same residual.

## build set: covering-system-construction, greedy-exchange-cost-potential, witness-depth-bound
