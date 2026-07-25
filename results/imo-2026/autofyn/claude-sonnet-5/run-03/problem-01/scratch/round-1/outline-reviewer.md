## imo-2026-01 — round 1 outline review

### Verification performed
- Re-derived and numerically checked (Python, 10000 random trials) the two core
  identities every approach relies on: `min(a,b)^2+|a-b|^2 ≤ a^2+b^2` and
  `gcd(min(a,b),|a-b|)=gcd(a,b)` and `max(a,b)=min(a,b)+|a-b|`. All hold.
- Simulated the actual Confucius process on random small boards (200 trials, random
  move order each trial) and confirmed: (i) it always terminates with exactly one
  entry `>1`, (ii) that survivor always equals `∏_p p^{gcd_i v_p(a_i)}`, matching the
  `G_p`-invariant formula used by all four approaches. This is strong evidence the
  shared mechanism (per-prime subtractive-Euclidean reduction + gcd-of-exponents
  invariant) is the *correct* technique, not a plausible-looking dead end.

### Per-approach verdicts

**lex-potential-gcd-invariant — APPROVE**
The strongest and most complete outline. Per-prime reduction is correctly derived.
Part (a)'s `(N,Σ)` lexicographic potential is well-founded, the N-drop case split
(gcd=1 vs gcd>1, including m=n as a sub-case of gcd>1) is exhaustive, and the
"N can't skip 2→0" argument correctly nails down "exactly one" (not "at most one").
Part (b)'s `G_p` invariance argument is correct (checked the Euclidean identity and
multiset-gcd associativity claim; both hold) and correctly reconstructs `M` via
unique factorization. The self-flagged watch-out (don't conflate `G_p` with
`min_i v_p(a_i)`) is real and correctly caught with a concrete counterexample
`{2,3}→M=6`. No structural gap — only write-up rigor remains (spell out the
associativity-over-a-multiset one-liner, state lex well-foundedness explicitly).
This is essentially a complete proof skeleton for both parts.

**omega-linear-monovariant — APPROVE, but redundant with the above for build-set purposes**
Mathematically sound (the `Ω(g)+Ω(q)=Σ max(v_p(m),v_p(n))` identity is exact and
checked numerically). Its only distinguishing content vs. the primary approach is
swapping the quadratic potential `Σ` for the linear one `T=ΣΩ(a_i)` in part (a); part
(b) is verbatim identical to lex-potential's. The outliner itself flags this as a
near-twin whose value is presentation only. Register it (it's a valid, independently
correct approach and a legitimate hedge if the sum-of-squares write-up trips on
something), but it does not diversify the field's *framing* — same reduction, same
target, same invariant, just a different termination potential. Do not treat two
builds of this pair as independent confirmation.

**token-multiset-crt-reconstruction — CHANGES REQUESTED**
Same underlying mechanism, reorganized into a "per-prime lane" decomposition with
Lemma A (decoupled single-lane invariant) + Lemma B (cross-lane termination,
identical to lex-potential's part a). Mathematically this doesn't add anything beyond
lex-potential — it's an expository reshuffling, correctly self-identified as such by
the outliner ("purely organizational/expository ... legitimate candidate to fold into
or drop"). One concrete fix needed before build: the "CRT-style reconstruction"
label is inaccurate (it's unique factorization, not CRT) — the outline already flags
this but the builder must not let "CRT" survive into the write-up as a cited theorem
name (KB rule: name your tools correctly). Approve the underlying content but keep
this out of this round's build set — it is not distinct enough in framing to be worth
a parallel build against lex-potential, and its terminology needs correcting first.

**induction-on-active-count — CHANGES REQUESTED (not RETHINK)**
This is the one approach with a genuinely different proof *strategy* (induction on
active-entry count vs. a single global potential), so it's valuable for diversity —
but the self-flagged gap is real and worth scrutinizing closely, as instructed.

Gap analysis: the sub-lemma (isolating a pair and playing only that pair) is correct
and cleanly proved (it's just the k=2 instance of the same identities). But the
inductive step as sketched only shows termination for the *specific* strategy "fully
resolve one pair before touching any other" — this is an existence argument, and the
problem is universally quantified over Confucius's play. The outline is honest about
this and does not try to disguise it as complete, which is the correct thing to do
(overclaiming would have been a RETHINK-worthy circular-reasoning violation; honest
gap-flagging is not).

However, the gap looks *fixable without abandoning the induction framing*, contrary
to the outline's pessimistic "may collapse back into the primary approach" concern.
The fix: induct on the state reached after the *first* move actually played (whichever
pair Confucius happens to choose), not on "isolate and fully resolve a pair." Concretely:
strong induction on `k` (active count) with hypothesis "any board with `<k` active
entries, played to completion by ANY sequence of legal moves, terminates at the unique
`∏p^{G_p}`." For the inductive step: take an arbitrary board with `k` active entries and
an arbitrary infinite (or maximal) sequence of Confucius's moves; look at the *first*
move, which touches some pair `(m,n)` and replaces them with `(g,q)`. This first move
alone drops the active count to `k-1` or `k-2` (same case split already in the outline:
gcd=1 drops by 2, gcd>1 drops by 1) — this holds regardless of what Confucius does next,
because it's a statement about one move, not about the rest of the game. Apply the
induction hypothesis to the *resulting* `(k-1)`- or `(k-2)`-active board and the
*remaining* (still arbitrary) sequence of moves. This closes the interleaving gap
without reintroducing the global `(N,Σ)` potential over all 2026 entries — the only
potential-like argument needed is local well-foundedness of `k` itself (a strictly
decreasing sequence of naturals, trivially well-founded), which is a genuine
simplification over the primary approach's `Σ` bookkeeping. This is a concrete,
buildable fix — send it to the builder as a required correction, not a RETHINK.

Required changes for the builder: (1) replace "isolate and fully resolve a pair, then
induct" with "induct on the first move of an arbitrary sequence," as above; (2) keep
the existing two-entry sub-lemma (still correct and still useful, now only needed for
computing what the *first* move's pair collapses to a set of active entries, not for
a full self-contained sub-game); (3) part (b) unchanged (already correct, imported).

### Diversity assessment
Three of the four approaches (lex-potential, omega-linear, token-multiset) are the
*same* proof — same per-prime reduction, same `G_p` invariant, same problem
decomposition — differing only in termination-potential bookkeeping or expository
packaging. This is not the "single-gap trap" the orchestrator warns about in the
dangerous sense (there is no unresolved shared gap — the shared mechanism appears to
be fully correct, verified numerically above), but it is a real lack of framing
diversity: if a subtle error were later found in the per-prime reduction step itself,
all three would fail together. `induction-on-active-count` is the only approach that
attacks part (a) via a structurally different route (local induction vs. a global
potential), so it is worth funding this round specifically for that reason, once its
gap-fix is applied.

### Build set selection
Send `lex-potential-gcd-invariant` (most complete, no structural gap, write it up
rigorously) and `induction-on-active-count` (genuinely different strategy, gap is
identified and has a concrete fix — worth a round to see if the "first-move induction"
repair closes cleanly, which would give the population a second, independently
structured route to part (a) and reduce single-mechanism risk). Hold
`omega-linear-monovariant` and `token-multiset-crt-reconstruction` in the population
(registered, ranked) but do not spend a builder round on them yet since they are
expository near-twins of `lex-potential-gcd-invariant` with no distinguishing
mathematical content — revisit if `lex-potential-gcd-invariant`'s write-up hits an
unexpected snag.

build set: lex-potential-gcd-invariant, induction-on-active-count
