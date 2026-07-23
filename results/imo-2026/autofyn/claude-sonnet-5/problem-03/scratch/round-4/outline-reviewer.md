# Round 4 outline review — imo-2026-03

All four approach files were revised this round. Independently re-verified the outliner's
claimed skeletons via exact-`Fraction` computation (not trusted from prose). Summary verdict:
**three CHANGES REQUESTED, one retirement confirmed.** Found one significant, previously
undisclosed logical gap shared by two of the three revised skeletons (see "Cross-cutting
finding" below) — this is new information not caught by this round's outliner or explorers,
and must be added to both builders' task lists.

---

## Cross-cutting finding (affects `dyadic-cascade-induction` §5.2' AND `concavity-minimax-duality` §7)

Both revised skeletons restate their target (Step 0 in each file) as:

> "By certified **Lemma D/M**, XY's response to `D_m` **is exactly** a legal sequence of `≤m`
> D(bisect)/M(match) operations on the active-value multiset... Restate the target purely in
> this language, dropping 'which piece is physically `a_1`' language entirely."

This is an **overclaim**, and it directly contradicts the certified lemma's own stated scope.
`lemmas/dm-operation-reformulation.md` ("Consequence" section) explicitly says:

> "This is **not** claimed to capture Xiang Yu's *entire* strategy space in general (whether
> every jointly-optimal multi-cut response reduces to a D/M sequence is a separate, open
> structural question)... only that D/M sequences are always *achievable*, which is all that
> is needed for **upper-bound** arguments."

`potential-weighting-upper-bound`'s use of Lemma D/M is fine — the upper-bound direction only
needs *some* achievable sufficient strategy, exactly what the lemma proves. But
`dyadic-cascade-induction`'s §5.2' and `concavity-minimax-duality`'s §7 are both attacking the
**lower-bound** direction: "for **every** XY response, `e(\text{final})\ge e_m`." That is a
*universal* claim over XY's full physical strategy space, not just the D/M-achievable subset.
Restating the target as "for every D/M sequence" silently **replaces the true universal claim
with a weaker one** (quantifying only over a subset of strategies) unless completeness of the
D/M operation space *specifically against `D_m`* is separately established — which it is not,
anywhere in the population.

**Concretely, where this could fail:** Operation `D(x)` removes `x` from the active multiset
and inserts nothing back — the two `x/2` copies it creates are *never* available for a later
operation to target. So "bisect a piece, then later re-split just one of the two resulting
(equal) halves" is a real physical XY strategy that is **not** literally expressible as a D/M
sequence, unless the untouched half happens to exactly coincide with some other reachable
active value (in which case it can be re-expressed as an `M` instead of a `D`). I checked the
one worked example both files lean on (the `m=3` "bisect `a_1`, then bisect one resulting
half" tying case, `(a_2,a_3,a_3)=(4/15,2/15,2/15)`) and confirmed by hand/`Fraction` that it
*does* reduce cleanly — because `D_m` is exactly dyadic (`a_1=2a_2=4a_3=\dots`), so
`a_1/2=a_2` **exactly**, making `D(a_1)` and `M(a_1,a_2)` produce the identical residual, and
the "re-split half" trick is secretly just `D(a_1)` followed by `D(a_2)` (both cuts landing on
values that coincide with genuine active elements). This is real corroborating evidence that
completeness *might* hold for the dyadic-specific input via this self-similarity — but it is
exactly the **`i=2`, already-closed degenerate case** that `dyadic-cascade-induction`'s own
Step 4 flags as trivial; it says nothing about deeper fragments (e.g. a leftover
`\ell=a_1-a_i` for `i\ge3`, itself later bisected and re-split) where no such neat coincidence
is evident.

```python
from fractions import Fraction as F
def e_of(M):
    M = sorted(M, reverse=True); t = F(0)
    for i,x in enumerate(M): t += x if i%2==0 else -x
    return t
D3 = [F(8,15),F(4,15),F(2,15),F(1,15)]
final = [F(4,15), F(4,15), F(2,15), F(2,15), F(2,15), F(1,15)]  # bisect a1, then bisect ONE half
print(e_of(final))  # 1/15 == e_3, confirmed — but this is the i=2 (already-trivial) case
```

**Required fix (must be added to both builders' task lists, not optional polish):** before
Step 4 (`dyadic-cascade-induction`) or Steps 2–4 (`concavity-minimax-duality`) can be trusted
as actually proving the theorem's lower bound (rather than a D/M-restricted weaker statement),
one of the two builders must either (a) prove D/M-completeness specifically against `D_m`
(leverage the dyadic self-similarity property `a_1=2a_2=4a_3=\dots`, which is the plausible
mechanism, generalizing the worked `i=2` example to arbitrary re-split depth and to fragments
created by `M`, not just `D`), or (b) explicitly scope Step 0's claim down to "D/M sequences
are a *sufficient, not necessarily complete*, witnessing family for `D_m`" and separately argue
(e.g. via the certified vertex lemma) that no non-D/M-expressible strategy can ever help XY.
Whichever builder proves this first should write it up as a new certified lemma so the other
approach can import it rather than re-deriving. **This is not a reason to RETHINK either
approach** — the gap is very plausibly closeable (strong corroborating evidence from the
dyadic self-similarity structure, and the underlying numeric searches over the *full* physical
strategy space at `m=2,3,4` found no violation anywhere) — but it is a genuine, previously
uncaught prerequisite that must be made explicit, not silently assumed.

---

## `dyadic-cascade-induction` — CHANGES REQUESTED

**Verified correct (independently re-checked):**
- The claimed `m=3` telescoping equivalence (§5.2' motivating example, reused above) — exact
  `Fraction` check confirms `e=1/15=e_3`, and the claimed reduction to "D(a1) then D(a2)" is
  algebraically correct (see above). Steps 1 (commutativity of disjoint operations) and 2
  (case split by content, not location) are short and essentially mechanical, as the outline
  itself says — no issues found.
- Step 4 (the flagged "genuinely hard" sub-claim, dominance-preservation for `i\ge3`) is
  honestly scoped: the outline explicitly shows the naive `𝒟_j` class check fails
  (`a_1-a_i\ge2a_2 \iff a_i\le0`, false in general) rather than hiding this — this is exactly
  the discipline the "watch out for" note in the dispatch asked for; it does **not** silently
  re-derive the falsified "merging monotonicity" lemma (confirmed: the outline explicitly
  distinguishes its narrower, minimal-counterexample-restricted form (ii) from the falsified
  unconditional form, and flags this distinction explicitly).
- **Does §5.2' collapse back to the falsified "merging monotonicity" mechanism?** No — Step 3's
  `𝒟_j` claim and Step 4's two fallback routes are a genuinely different mechanism (a
  broadened induction *class*, closed either by a weaker dominance ratio or by a
  minimal-counterexample/local-exchange argument restricted to an assumed violator), correctly
  distinguished from the previously-falsified *unconditional* merging inequality over arbitrary
  side-multisets. This is a real, structurally different attempt, not the same claim in
  disguise.

**Issue (new, this round's independent finding):** Step 0's D/M-completeness overclaim — see
"Cross-cutting finding" above. Must be fixed before Step 4's resolution (however it comes out)
actually proves the theorem's lower bound.

**Required for the builder:** (1) address the Step-0 completeness gap (new task, not in the
outline); (2) attempt Step 4's dominance-preservation sub-claim via route (i) first (relaxed
dominance ratio) as instructed, falling back to (ii) if needed.

## `potential-weighting-upper-bound` — CHANGES REQUESTED

No new issues found. The round-4 queued mechanism (§4, induction-loading / richer-IH shape for
Case (ii) at general `m`) is correctly scoped: it targets the *upper*-bound direction, where
Lemma D/M's proven "achievability" (sufficiency) scope is exactly what's needed — **no
completeness gap applies here**, unlike the two lower-bound approaches above. The diagnostic
task (Step 2, tabulate what structural fact about the residual the true optimal first move
needed on the two known counterexamples) is a sound, bounded, well-defined next step, and the
outline correctly forbids re-proposing Rule 1/Rule 2 in disguise. The candidate 2-level-lookahead
refinement (Step 3) is explicitly flagged as untested/to-be-verified, not assumed — appropriate.
Approve as scoped; proceed with the bounded diagnostic + candidate test as planned.

## `concavity-minimax-duality` — CHANGES REQUESTED

**The repurposing itself is sound and genuinely diverse.** The new §7 monovariant/potential-
method plan (P1–P3 properties) is a structurally different mechanism from
`dyadic-cascade-induction`'s induction-loading (no recursion-depth case split at all, a single
global inequality chain) — this is real diversity of thought, not a rephrasing, consistent
with what the round-4 altframing explorer independently recommended. The decision to abandon
the (correctly, definitively) falsified global-concavity mechanism and not re-attempt the
`a_1\ge1/2`-restricted salvage this round (since it reuses the same edge-normal machinery every
sibling already has) is correct per CLAUDE.md's diversification guidance.

**Issue 1 (shared with `dyadic-cascade-induction`):** Step 0 has the identical D/M-completeness
overclaim — see "Cross-cutting finding" above.

**Issue 2 (new, this round's independent finding): the concrete Step-3 candidate
`\Phi(M,r):=S(M)/(2^{|M|}-1)` is refuted immediately, more severely than the outline
anticipated.** The outline's own "known caveat" only worried about failure on *unreachable*
multisets (e.g. an arbitrary tied pair). I checked it directly against `D_2`'s own canonical
extremal trajectory (the dyadic point itself, `m=2`) and it fails on the **very first move**:

```python
from fractions import Fraction as F
D2 = [F(4,7), F(2,7), F(1,7)]
Phi = lambda M: sum(M)/(2**len(M)-1)
print(Phi(D2))                                   # 1/7  (normalization P1, correct)
after_D = sorted([F(2,7)]*3 + [F(1,7)], reverse=True)   # bisect a1
print(Phi(after_D))                              # 1/15 < 1/7 -- (P2) FAILS immediately
after_M = [F(2,7), F(1,7)]                        # match a1 to a2 instead
print(Phi(after_M))                               # 1/7 -- (P2) holds for this move
```

So `\Phi` is monovariant under `M` operations (verified: stays exactly `1/7`) but **strictly
decreases** under the `D` (bisect) operation, immediately, on the top-level dyadic point — not
merely on some exotic non-reachable state. This candidate is dead on arrival; the builder
should **not** spend time tabulating it against the `m=2,3,4` intermediate-tie data as the
outline's Step 3 instructs (that step is now superseded by this cheaper, decisive check) — go
straight to Step 3's own fallback (Step 4 in the file: build `\Phi` from Fact 2's exact
identity as a worst-case amortized recursive bound) or propose a genuinely different `\Phi`
shape that is monovariant under `D` specifically (the diagnosis above — fails on `D`, passes on
`M` — narrows the search: any fix must make `\Phi` insensitive to, or compensate for, the pure
size-growth-without-value-change that a bisection causes).

**Required for the builder:** (1) same Step-0 completeness fix as `dyadic-cascade-induction`
(coordinate with that builder — whichever proves it first should certify it as a shared lemma);
(2) skip the specific `S(M)/(2^{|M|}-1)` candidate (already refuted above) and go straight to a
`D`-aware correction or the Step 4 fallback.

## `elementary-exchange-smoothing` — retirement confirmed sound, no build

Independently verified: this file's Step A ("tie-or-degenerate lemma") and
`dyadic-cascade-induction`'s §3 ("vertex lemma") are the same statement (piecewise-linearity of
a single cut, minimizer always at a tie/bisect/degenerate breakpoint), proved independently by
two different builders in two different rounds — confirmed by direct comparison of the two
proofs (both use the identical crossing/rank-change argument). Step A's "Corollary (iterated
cuts)" is genuinely the more explicit/complete write-up of the multi-cut consequence that
`dyadic-cascade-induction` §3 only gestures at. The outliner's recommendation — certify one
canonical `lemmas/vertex-lemma.md` merging Step A's corollary with `dyadic-cascade-induction`
§3's base statement, and retire this slug as an independent whole-attempt (its own remaining
goals, full Case (ii) global coverage and the `a_2/a_3=2` condition, are already fully and
unconditionally subsumed by `dyadic-cascade-induction` §2c's complete n=2 Case (ii) closure) —
is correct and should be carried out as housekeeping, not a builder dispatch. Step C's
convex-hull certificate technique (`λ=(2/7,1/7,4/7)`) is a fine reusable pattern to keep on
record informally; no separate certification needed (it's a standard convex-analysis fact, the
value is the worked computation, already captured in the approach file itself for any future
reference).

**Recommend:** proof-reviewer (or a lemma-housekeeping step) creates
`lemmas/vertex-lemma.md` merging the two write-ups; no proof-builder dispatched to this slug
this round.

---

## Diversity assessment

Genuine diversity across the three live approaches: `dyadic-cascade-induction` (case-split
induction-loading on a broadened multiset class), `potential-weighting-upper-bound`
(operation-space policy search / richer-IH lookahead, upper bound only),
`concavity-minimax-duality` (global monovariant/potential, no case split at all) are three
structurally distinct mechanisms, not variants of one framing — this satisfies CLAUDE.md's
diversity requirement. The one real risk: two of the three (`dyadic-cascade-induction`'s §5.2'
and `concavity-minimax-duality`'s §7) both target the *same* underlying gap (multi-cut-inside-
dominant-piece) and, as just found, both silently share the *same* unaddressed prerequisite
(D/M completeness against `D_m`) at their common Step 0 — this is exactly the "shared hard
structural claim deeper in the proof" pattern CLAUDE.md warns about, not the shared top-level
reduction (Lemma G/P), which remains a legitimate common prerequisite. Flagging this explicitly
so next round's outliner/builders don't let both slugs independently re-discover and
re-derive the same completeness lemma — whichever proves it first should certify it for the
other to import.

## Small-case sanity checks performed this round
- Re-verified the `m=3` telescoping example (§5.2') by exact `Fraction` computation: confirmed.
- Re-verified `concavity-minimax-duality`'s Step-3 candidate `\Phi` fails at `m=2`'s own
  dyadic point under a `D` operation (`1/7\to1/15`), while holding under an `M` operation
  (`1/7\to1/7`): confirmed, a sharper diagnosis than the outline had.
- Spot-checked `dyadic-cascade-induction`'s §2d closed-form `a_1^*=2^m/(2^{m+1}-1)` and
  Sub-case B's strict-domination claim: unchanged from round 3, not re-derived here (round 3's
  reviewer already independently verified these and this round did not revise them).

---

build set: dyadic-cascade-induction, potential-weighting-upper-bound, concavity-minimax-duality
