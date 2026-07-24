# Outline review — round 15 (imo-2026-06)

Verified independently (fresh Python, fresh crux-corpus queries, hand-derived
missing lemma) before committing a build cycle. Verdicts below are per-slug,
per CLAUDE.md's per-approach routing.

## similarity-dichotomy-crux-adaptation (NEW) — CHANGES REQUESTED, top priority

**Crux match re-verified myself, exact.** Pulled `aimo-0030` directly from
`past_problems_database.json`: the problem is IMO-SL 2013 N5 ("Ana and
Banana"). Both official solutions are present in full in the `solutions`
field, and — critically — so are **Comments 2–4**, appended after solution 2.
Comment 2 states verbatim: *"b_0=k; if b_n has just been defined, b_{n+1} is
the smallest number b>b_n that is coprime to none of b_0,...,b_n"* — this
recursion is character-for-character imo-2026-06's own rule. Comment 3 gives
the mod-`P` (`P:=∏_{p≤k}p`) periodicity-of-the-word claim and the worked
`k=15` example (period 30) that the explorers cited — confirmed present,
not fabricated/misremembered. **This means the outline's claim that the crux
corpus contains the full relevant machinery is correct, and the "RECON"
Claims 1–3 + main Dichotomy are literally the two official solutions' text**
(not a paraphrase the builder has to reconstruct from nothing) — a from-
scratch *translation* task (game "good/bad" → imo-2026-06 "term/non-term"),
not a from-scratch *discovery* task. This materially de-risks Steps 3–4
relative to how the outline (correctly, conservatively) scopes them.

**Claim 1's 3-line proof (via Lemma P′/Corollary P″): traced myself, correct.**
No gap. Matches Corollary P″'s exact statement (`lemmas/lemma-WF-witness-
forcing-and-theorem-FW-instances.md`, itself citing certified `lemma-P-
prime-pairwise-intersecting.md`).

**Found and closed the one load-bearing gap the outline itself doesn't name
explicitly: the "IN/OUT recursive characterization" bridge.** The outline
assumes Claims 1–3 transfer "with just a vocabulary swap," but the crux's
Claims 1–3 use the game's own recursively-defined `good`/`bad` dichotomy
(`n bad iff ∃ good m, k≤m<n, gcd(m,n)=1`), which is NOT literally the same
statement as "n is a term of imo-2026-06's `a_n` sequence" until you prove
they coincide (this is exactly Comment 2's unstated content). I proved this
bridge myself from scratch, directly from the problem's recursive
definition (no game needed):
  - (⟸) If `∃` a term `m<n`, `gcd(m,n)=1`, then `n` is not a term — trivial
    (if `n=a_j`, minimality/definition forces `gcd(n,a_i)>1` for every
    earlier term, including `m`, contradiction).
  - (⟹) If `n` is not a term (`n>a_1`), let `a_j` be the largest term `<n`.
    Then `a_j<n<a_{j+1}` (strict both sides, else `n` would itself be a
    term). Since `a_{j+1}` is BY DEFINITION the smallest integer `>a_j`
    satisfying `gcd(·,a_i)>1` for all `i≤j`, and `n` is a smaller candidate
    in that gap that was NOT chosen, `n` must fail that condition: `∃ i≤j`,
    `gcd(n,a_i)=1`. Take `m:=a_i` (a term, `<n`, coprime to `n`). Done.
  This is exactly the missing arithmetic fact needed to run Claims 1–3 in
  `a_n`-language with zero game machinery — **builder should state and
  prove this explicitly as its own numbered lemma** (call it Lemma REC),
  not skip straight to "Claim 2/3 transfer."

**Numerically re-verified the Dichotomy on 3 FRESH `a_1` values no explorer
this round used** (`a_1=65, 77, 91` — chosen deliberately since `65` already
broke other frameworks in round 2): generated 3000 terms each, checked every
integer from `a_1` to the max generated value against its small-prime
signature. Zero mixed classes: `65` (1313 classes), `77` (1876 classes),
`91` (2345 classes). Also re-verified Claim 1 (multiple of a term is a
term) on the same 3 fresh cases: zero violations across ~10,000 checks each.

**Found a real, fixable error in the outline's own Step 6 sanity check.**
Step 6 says the builder should verify Step 5's formula "reproduce `T=8,
L=30` exactly" for `a_1=15`. I computed it directly: `P=∏_{p≤15}p=30030`
(not 30), and the number of good residues mod `P` is `T=8008` (not 8), and
`a_{n+8008}=a_n+30030` holds exactly for all checked `n` (verified). This
IS consistent with the workspace's already-certified minimal period
`(T0,L0)=(8,30)` — `30030=1001·30`, `8008=1001·8`, i.e. Step 5's `(T,L)` is
a (large, non-minimal) integer multiple of the true fundamental period,
which is fine (the problem only asks for *some* valid `T,L`, not minimal
ones) — but the outline's literal wording ("reproduce T=8,L=30") is
**factually wrong and will confuse the builder** if followed literally
(they'll compute `T=8008,L=30030`, not `8,30`, and might wrongly conclude
the argument is broken). **Fix for the builder**: check instead that the
computed `(T,L)` is a positive-integer multiple of the independently-
certified `(8,30)` — this is the correct, and in this case verifiably true,
sanity check.

**Also spot-checked Claim 2's translation by hand** (not just numerically):
translating "rs bad, x good witness ⟹ x coprime to r,s individually ⟹ x
coprime to r²s ⟹ r²s bad" into IN/OUT language goes through verbatim using
only Lemma REC (above) + elementary gcd facts, no game-specific content.
Did not fully re-trace Claim 3's more involved minimal-counterexample
argument line-by-line (time-boxed), but its key step ("x has to be
divisible by p") reduces to exactly Corollary P″ (already certified) + my
Lemma REC — strong evidence it also translates cleanly, not proof.

**Verdict rationale**: technique is sound (not a dead end — the crux really
is the same object, the full official proof text is in the corpus, Claim 1
+ the setup + the periodicity corollary are done/elementary, and I closed
the one silently-missing bridge lemma myself). Gaps remain (Claims 2/3 full
write-up, Main Dichotomy assembly, Claim 3's detailed transfer, and the
Step 6 wording fix) — hence CHANGES REQUESTED, not APPROVE outright, but
this is the single most promising line the workspace has had in 15 rounds:
if Step 4 closes, Status → solved for the WHOLE problem, not another
instance. **Top priority for this round's build.**

## forced-primes-well-ordering (ADVANCE) — CHANGES REQUESTED, build

**Re-verified Common-Recruiter Reuse / Corollary CRR myself, mechanically,
end to end.** Lemma WF's certified statement (`lemmas/lemma-WF-witness-
forcing-and-theorem-FW-instances.md`) has hypothesis "S, S′ disjoint
nonempty cores, `i_0` has core `S′`" and concludes `comp(a_k)∩comp(a_{i_0})
≠∅` for **every** `k∈I_S` — nothing in the hypothesis or proof references
which specific `S` was originally intended, so re-aiming the same witness
at every OTHER core disjoint from `S′` is a correct, free corollary, exactly
as claimed (not hand-waved).

Re-derived by hand which of `a_1=21528751`'s 6 disjoint core-pair channels
this closes, using the 4 witnesses on file (`a_1405,a_11812,a_27832` — core
`{103}`, singleton comps `2,3,7`; `a_2575` — core `{197}`, comp exactly
`{2,3,7}`): the `{103}`-singletons give FULL containment `{2,3,7}⊆comp(a_k)`
for every `k` in the 3 cores disjoint from `{103}` (`{197}`,`{1061}`,
`{197,1061}`); the `{197}`-witness gives the weaker `comp(a_k)∩{2,3,7}≠∅`
for every `k` in the 3 cores disjoint from `{197}` (`{103}`,`{1061}`,
`{103,1061}`). Combining full-containment-on-one-side with intersects-on-
the-other-side gives universal pairwise intersection for every one of the
4 claimed new channels: `({103},{1061})`, `({103},{197,1061})`,
`({197},{1061})`, `({197},{103,1061})` — **I get exactly this list
independently**, matching the outline precisely. The un-closed 6th channel
`({1061},{103,197})` is correctly diagnosed: target core `{103,197}` is not
disjoint from either recruiting core, so Lemma WF cannot be aimed at it via
these witnesses — genuinely open, honestly scoped, not glossed over.

No issues found. Build as scoped; the (4a) `W={2,3,7,11,97}` speculation for
the 6th channel is correctly flagged as conditional on an unproven "only
escape bundle" claim — do not let the builder silently assume it.

## witness-chaining-universal-existence (ADVANCE) — CHANGES REQUESTED, DEFER this round

Sound content (choice-function/up-set reduction is a standard, correctly-
described finite-lattice fact; the MSF-refuted-in-narrow-form-vs-general-
mechanism-still-open distinction is the right careful reading, consistent
with the round-14 standing rule). No flaw found. However: this shares the
same Lemma WF / Chaining Sufficiency Theorem toolkit as
`forced-primes-well-ordering` (its target — general existence — is a
different scope of the *same* mechanism family, not a different mechanism),
and its main open questions (Bounded Forced-Set Existence) risk becoming
moot if `similarity-dichotomy-crux-adaptation` closes the whole problem via
an unrelated route this round or next. Given CLAUDE.md's "few strongest,
normally 1–3" guidance and this round's field already having 4 outlines,
**defer (not cut) this slug** — it stays registered/live for next round,
its Elo reflects continued real progress, but this round's builder effort
is better spent on the higher-leverage crux-adaptation line plus
`forced-primes-well-ordering`'s cheap, already-verified 4-channel win.

## intersecting-family-covering-construction (ADVANCE, diversity slot) — CHANGES REQUESTED, build

No new explorer finding targets this approach's gap this round (as the
outline itself says); kept live per CLAUDE.md diversity requirement — it
remains the only structurally-independent mechanism (density/minimality on
`G`) besides the brand-new crux-adaptation route, and it is the field's
highest-Elo, most mature approach (9 rounds of certified content). Build to
keep the population from collapsing onto the witness-chaining family while
the higher-risk crux-adaptation line is being tested.

## Diversity / redundancy check (CLAUDE.md single-gap-trap)

- `forced-primes-well-ordering` and `witness-chaining-universal-existence`
  share one mechanism (Lemma WF / Chaining Sufficiency Theorem) at two
  different scopes (instance/channel closure vs. general existence) — this
  is the same shape already accepted in rounds 13–14, not a new problem;
  addressed this round by deferring the latter rather than building both.
- `similarity-dichotomy-crux-adaptation` is genuinely orthogonal to the
  entire FCBC/(JW)/(WCE)/Corollary-MSF apparatus (does not go through
  Theorem 5.1, covering sets, or core decomposition at all) — real,
  substantive diversity, not a relabeling; independently confirmed by
  tracing its mechanism myself rather than trusting the outline's framing.
- `intersecting-family-covering-construction` remains the sole live
  density/minimality-mechanism approach — correctly kept for diversity per
  CLAUDE.md even with a quiet round.
- No approach this round repeats a recorded dead end (checked against
  run_state.md Rules: EBS, Realized-Backbone/UCR for 4199:(13,17), matched-
  witness refinement, Lemma W3 compression, global-recruiter-finiteness,
  |S|-induction, bounded-modulus/CRT minimality — none re-attempted).

## Ranker actions taken

- Registered `similarity-dichotomy-crux-adaptation` (new, cold-start 1500).
- `update_ranking` with 6 comparisons anchoring the newcomer against the
  established field (win over `witness-chaining-universal-existence`,
  `core-depth-induction`, `persistent-backbone-monovariant`; draw against
  `forced-primes-well-ordering`; plus `forced-primes-well-ordering` and
  `intersecting-family-covering-construction` each beating
  `witness-chaining-universal-existence`, reflecting this round's
  deferral). Post-update Elo: intersecting-family-covering-construction
  1765.7 (top), forced-primes-well-ordering 1650.8,
  similarity-dichotomy-crux-adaptation 1553.7 (new),
  persistent-backbone-monovariant 1503.1, witness-chaining-universal-
  existence 1493.7 (deferred), core-depth-induction 1430.7 (parked).

build set: similarity-dichotomy-crux-adaptation, forced-primes-well-ordering, intersecting-family-covering-construction
