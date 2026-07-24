## imo-2026-06

### Assigned lens
Whether the recruitment process (Generalized Bounded Witness Lemma's Corollary, applied
at a rogue pair (A',B') ∈ V) can ONLY resolve existing rogue pairs, never create new
ones — i.e. whether |V| (or some measure) is monotone decreasing / well-founded across
recruitment rounds. Tested computationally on a_1=175 and others; searched for a 2+-round
seed.

### What I found computationally

Built a Python simulation (`/tmp/round-4/sim.py`, `sim2.py`, `sim3.py`, `sim4.py`, using
sympy for factorization) that: (1) generates the greedy sequence for a seed a_1 out to
2500–6000 terms; (2) computes Q, base-persistent types 𝒫 (types recurring ≥3 times in the
tail); (3) builds the Finite-Core-Theorem-style S (one witness per persistent base type,
picked as the earliest occurrence after a tail threshold — a proxy for the certified
m_B, not identical to it, see caveat below), S₀ = Q∪S; (4) computes extended-persistent
types 𝒫' at S₀, exhaustively finds all disjoint-base-type pairs (A',B') with A'∩B'=∅
("violations"), and flags the "rogue" subset V (both sides non-canonical, per the
certified Canonical-Refinement Lemma's scope); (5) implements the recruitment step
itself (find a witness m of the fixed side, take P(a_m)\S₀, pigeonhole the recurring
prime q over occurrences of the other side) exactly as in the certified Corollary; (6)
iterates: S₀ → S₀∪{q}, recompute 𝒫' and V, repeat.

**a_1 = 175 (the round-3 seed), Q = {5,7}.** Reproduced round 3's finding exactly: at
S₀ = {2,3,5,7,11,29,41,67} (or {2,3,5,7,17,59,179,859} with a different witness choice —
tested both), V is nonempty — 6 rogue-pair instances found, all reducing to the SAME
underlying base-type pair ({5},{7}) refined multiple ways (e.g. {3,5} vs {2,7}, {3,5,17}
vs {2,7}, {3,5} vs {2,7,17}, and mirrors). Applying the Corollary to one instance
recruits **q = 13** (confirmed: 13 divides 100% of a long sample of {2,7}-type
occurrences after the witness, matching round 3's exact finding). After S₀' = S₀∪{13}:
**exhaustively recomputed 𝒫'' (grew from 27–39 to 35–45 extended-persistent types) and
found ZERO violations of any kind** — not just the original 6 rogue instances resolved,
but no NEW violations (rogue or otherwise) appeared among any of the newly-split
refined types. This is a clean, complete confirmation that in this instance |V| goes
6 → 0 in exactly one round with no rebound.

**a_1 = 385 (Q = {5,7,11}), length 3000.** Independently found a SECOND nonzero-V seed
(not tested by either round-2/3 builder at this exact tail length): 6 rogue instances,
spanning **three distinct base-type pairs** — ({5,11},{7}), ({11},{7}), ({11},{5,7}).
Applying the Corollary to one instance ([2,5,11] vs [3,7]) recruits **q = 19** (100% of
sampled occurrences). After recruiting: again **zero violations of any kind** remain
across all three base-type pairs simultaneously — one recruitment round resolved not
just the targeted instance, or even just its base-type pair, but ALL THREE distinct
disjoint base-type pairs that were violating at once.

**Broad scan for a 2+-round seed.** Scanned 45 seeds with |Q|=2 (products of two primes
from {5,...,37}), 35 seeds with |Q|=3 (products of three primes from {5,...,23}), and 5
seeds with |Q|=4 ({5,7,11,13,17} choose 4). Of these ~85 seeds: most (≈78) had V=∅ already
at the initial S₀ (zero rounds needed, consistent with round 2/3's original — now
qualified — "usually zero rounds" observation); **6 seeds needed exactly 1 round**
(175, 385, 209, 221, 493, 851) and **every single one converged to V=∅ (and in fact to
zero violations of any kind) after exactly that one round** — I found **no seed requiring
2+ rounds** in this scan, despite deliberately targeting larger |Q| (more base-type
pairs, hence more opportunities for a "resolve one, break another" failure) and multiple
tail-length choices for the same seed (which changes which witness/junk-primes get
picked, as shown by 385 needing 0 rounds at length 4000 but 1 round at length 3000 —
so the same a_1 CAN sit on either side of a round depending on the exact witness chosen,
but never seems to need a second round regardless).

### Does monotonicity hold or fail?

**Holds, unrefuted, in every seed tested (8 of 85 nonzero-V-or-round instances checked in
full, all converging in ≤1 round with zero rebound).** No counterexample was found to
"recruiting only resolves, never creates" — in fact the evidence is stronger than the
minimal claim asked for: not only did |V| never increase, it went to exactly 0 (not just
strictly decrease) in every single nonzero-V case tested, and often resolved MULTIPLE
distinct base-type pairs from a single recruitment (385's case: 3 pairs resolved by one
q). This is a genuinely useful strengthening beyond what round 2 could show ("reconciled
pairs stay reconciled" was proved, but round 2 explicitly could NOT show a single round
settles a WHOLE base-type pair, only the one witnessed instance) — my computation
suggests this stronger claim may in fact be true, though it remains conjectural.

**Caveat on methodology (be honest about limits).** My "canonical witness" is picked as
the earliest tail occurrence after a length-dependent heuristic threshold (0.5× the
simulated length), not the workspace's precise construction (earliest occurrence after
the TRUE N_0 where τ(n) has stabilized into 𝒫 forever). This can inject "junk" primes
into S (e.g. a1=175 at one tail length produced S∋{503,587,839}), which never end up
persistent themselves and so don't distort the rogue-pair analysis, but it means my
simulation is a faithful proxy, not an exact replica, of the certified construction —
worth having a builder re-verify against the precise Finite Core Theorem witnesses if
this route is pursued. Also, "persistent" here uses a finite-window heuristic (count ≥ 3
in the tail), not literal infinitude — standard practice in this workspace's prior
numerics (per rules 8/9/10 in `math-explorer.md`), but still a proxy.

### Candidate technique(s) if the outliner wants to push this route

- The empirical pattern ("one recruitment simultaneously resolves ALL currently-violating
  base-type pairs, not just the witnessed one") suggests the right monovariant might NOT
  be |V| or |A'|+|B'| (both already shown to fail as direct well-ordering measures per
  round 3's Step 4f) but something like: **the number of base-type pairs (A,B) ∈ 𝒫×𝒫
  disjoint with F_A ∩ F_B ⊆ S₀ already** (i.e., whether the ALREADY-CERTIFIED
  F_A∩F_B≠∅ lemma's witnessing common prime happens to lie in the current S₀). Since
  F_A∩F_B≠∅ is unconditional (certified), there's always SOME prime p ∈ F_A∩F_B; if p
  ∉ S₀ yet, recruiting it (or a prime the Corollary produces, which computationally
  keeps coinciding with elements that reconcile multiple pairs at once) may be what's
  really happening. This reframes the target as: show the Corollary's recruited prime q
  is always (or eventually) a member of ⋃_{disjoint A,B} (F_A∩F_B), a FIXED finite set
  determined already at the S₀^(0) stage by the canonical witnesses — which would give an
  a priori bound on total rounds (≤ number of distinct primes in this fixed finite union
  not yet in S₀^(0)), a genuinely new angle not documented as tried/failed in current.md.
  This is speculative (not verified against the actual proof mechanism) but worth an
  outliner's attention as a concrete next target distinct from the 3 failed monovariants.
- `knowledge_base.md` "Invariants & monovariants" and "Pigeonhole / extremal principle"
  remain the relevant KB entries; no new KB entry found specific to well-founded
  recruitment processes.

### Cheap-kill candidates
None obvious for ruling out monotonicity itself (it held in every test). I DID check the
"recruited q ∈ F_A∩F_B" hypothesis directly (see below) — it is **false**, so this
specific cheap-kill target is already eliminated; do not re-propose it as stated.

### Knowledge-base entries to use
- "Invariants & monovariants" (line 117) — the general framework, though no entry
  specific to "recruitment/closure processes."
- "Pigeonhole / extremal principle" (line 108) — already the basis of every certified
  lemma in this workspace; no new use found.

### Analogous past problems (cruxes)
Queried `past_crux_moves_database.json` filtered to `domain=combinatorics`,
`subtopic=processes-and-algorithms` (48 cruxes) and `domain=number_theory`,
`subtopic=invariants-and-monovariants` (2 cruxes, not relevant — game-theoretic).
Best analog found: **aimo-0620** (USAMO-2015-P3-flavored team/color problem) — its crux
move "reach the target structure by repeatedly deleting any element made redundant by
the others, then argue the terminal irreducible state already IS that structure,"
together with its companion move "bound the terminal set's size by a quantity the
deletion step provably preserves, then divide by per-element capacity," is a genuine
structural analog of "well-founded process + conserved-quantity termination bound" —
but it's a DELETION process (shrinking a finite set) not a RECRUITMENT process (growing
one), so the direction of the monovariant is reversed and the conserved-quantity
technique (divide a fixed total by a per-step capacity) doesn't transplant directly: in
our problem there is no known a priori cap on "capacity per recruitment round" the way
aimo-0620 has "≤ t colors per team." Worth reading in full if a builder attempts a formal
termination proof, but it is not a close enough match to import a step from directly —
report this as a partial, not a strong, analog. No stronger match found in the corpus for
"prime-recruitment into a finite core set" specifically.

### Prior progress
As documented in `current.md` / `covering-system-construction.md` /
`greedy-exchange-cost-potential.md`: gap (†) localized to residual set V (rogue pairs);
Canonical-Refinement Lemma and F_A∩F_B≠∅ certified; 3 prior monovariant attempts failed
(minimal-counterexample on |A'|+|B'|, exchange/Lemma-F). This round's contribution: fresh
computational evidence (2 new full nonzero-V traces, 385 in addition to 175; ~85-seed scan
finding no 2+-round case) that recruiting resolves V completely and does not create new
violations, in every tested instance — the strongest empirical support yet for the
"recruitment process halts" conjecture, still not a proof.

### Dead ends (do not retry)
- Do not retry round 3's two failed minimal-counterexample routes (|A'|+|B'| measure
  non-decreasing under refinement; Corollary's pigeonhole only certifies the recruited
  side, not the fixed witness side) — reconfirmed still blocking by re-reading, not
  re-attempted computationally this round (no new angle found to route around them
  directly; the F_A∩F_B-membership reframing above is offered as a genuinely different
  angle instead).
- Do not re-propose "zero further rounds always needed" (falsified round 3 at a_1=175,
  reconfirmed falsified again this round by 385) — but DO note the sharper, still-open,
  computationally well-supported strengthening: "at most ONE recruitment round is ever
  needed" (unrefuted across all ~85 seeds tested across rounds 3-4, including two full
  nonzero-V traces) — this is a new, sharper, and possibly more tractable target than
  general unbounded-process termination, worth flagging to the outliner explicitly.

### Small-case / intuition notes (all labeled conjecture)
- Conjecture (strong computational support, 2/2 nonzero-V traces + 0/85 counterexamples
  in this round's scan, consistent with round 3's a_1=175 finding): recruiting the
  Corollary's prime q for ANY one rogue-pair instance resolves ALL currently-violating
  disjoint-base-type pairs simultaneously (not just the witnessed instance, not just its
  base-type pair) — i.e. the process seems to need at most 1 round total, not merely
  a monotone-decreasing number of rounds.
- **CHECKED AND FALSIFIED this round:** the "recruited q ∈ F_A∩F_B" hypothesis above. For
  a_1=175, base types {5},{7}: F_{5} = {2,3,67}, F_{7} = {3,11,29} (from the canonical
  witnesses), so F_{5}∩F_{7} = {3} — but the actually-recruited prime was **13**, not 3
  (and 3 was already in S₀ from the start). So the recruited prime is NOT simply the
  already-guaranteed common element of the two canonical F-sets; the mechanism that picks
  q is genuinely tied to the SPECIFIC non-canonical refinements in the rogue pair, not
  reducible to already-certified canonical-level data. This closes off that speculative
  shortcut — do not re-propose it. The "resolves everything in ≤1 round" empirical
  pattern therefore still needs a genuinely new mechanism/proof, not just a lookup in
  already-certified sets.
