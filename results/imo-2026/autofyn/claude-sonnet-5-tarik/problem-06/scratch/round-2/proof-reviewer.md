# proof-reviewer — imo-2026-06, round 2

Reviewed both round-2 builds independently, per CLAUDE.md's per-approach
routing. Both are `partial`; both get **CHANGES REQUESTED**. No RETHINK, no
APPROVE this round. `results/imo-2026-06/current.md` updated (Status remains
`partial`); 6 new lemmas certified into `results/imo-2026-06/lemmas/`.

---

## 1. `persistent-backbone-monovariant` — Status: partial — Verdict: CHANGES REQUESTED

### What I independently re-derived / re-checked (not taken on faith)

**Lemma C (Global Intersection Collapse).** Re-derived all three parts from
scratch: (a) `C_{n+1}=C_n\cap P_{n+1}\subseteq C_n` trivially; (b) a bounded
non-increasing integer sequence stabilizes — standard; (c) the "iff Case I"
characterization. I re-checked the crux step myself: nesting gives
`C_\infty\subseteq C_n` for **every** `n\ge1` (not just `n\ge N_0`), since
`C_\infty=C_{N_0}\subseteq C_n` for `n\le N_0` (nesting) and `C_n=C_\infty`
for `n\ge N_0` (stabilization). Both directions of the iff then follow
cleanly from this single fact. No gap found. I also independently re-verified
the `a_1=65` sharpness example by direct simulation (`a_1..a_4 = 65,70,75,
78`, matching claimed radical sets and `C_1={5,13}, C_2={5}, C_3={5},
C_4=∅` exactly) — `N_0=4>k+1=3`, confirming `N_0` is not boundable purely by
`k=|P_1|`.

**Proposition NC1 (`a_1=221` counterexample).** I ran an independent Python
simulation of the problem's exact recursive rule for `a_1=221` and obtained
`a_1..a_5 = 221, 234, 238, 255, 260`, matching the approach's hand-trace
term-for-term and prime-factorization-for-factorization. Recomputing `C_1=
{13,17}, C_2=\{13\}, C_3=\varnothing` (so `N_0=3`, `S_0=\{2,3,7,13,17\}`) and
`w(4,5)=\gcd`-witness `= \{3,5,17\}\cap\{2,5,13\} = \{5\}`: `5\notin S_0`.
Confirmed exactly as claimed.

**Proposition NC2 (`a_1=375` counterexample).** Same independent simulation
for `a_1=375`: `a_1..a_7 = 375,378,380,384,390,396,399`, matching the trace
exactly. `C_1=\{3,5\}, C_2=\{3\}, C_3=\varnothing` (`N_0=3`, Case II
confirmed by Lemma C). `\mathrm{rad}(a_3)\cap\mathrm{rad}(a_7)=\{2,5,19\}\cap
\{3,7,19\}=\{19\}`, so `w(3,7)=19>15=\mathrm{rad}(a_1)`. Confirmed exactly.

**The `O(\log n)` bound derivation** (Domination Lemma + Lemma 1 attempt).
Re-derived: `q^*\le r\cdot a_n/n`, `a_n/n\le a_1+L`, `r\le\log_2(a_1+nL)`,
giving `q^*\le(a_1+L)\log_2(a_1+nL)`. Algebra checks out; this genuinely
grows with `n` (not a fixed bound), so the claimed negative conclusion
("this route does not close the gap") is correct, not just asserted.

### Verdict rationale

Both counterexamples are real and correctly falsify the two natural
conjectures they target. Lemma C is a genuine, non-trivial, fully proved
result. The approach's own honest self-assessment (Status `partial`, core
conjecture — the Finite Covering Backbone Conjecture — still open) matches
what I independently verified: no overclaim. This is real progress (a new
certified lemma, two impossibility results that steer future rounds away
from dead-end mechanisms), but the load-bearing existence claim remains
unproved. **CHANGES REQUESTED**: the gap is exactly the Finite Covering
Backbone Conjecture (existence of a finite `H` with `H\cap\mathrm{rad}(a_i)
\cap\mathrm{rad}(a_j)\ne\varnothing` for every `i<j`) — next round should
attack this directly, not re-attempt the two now-refuted mechanisms (Lemma
C's collapse point `S_0`, or `\mathrm{rad}(a_1)` itself) or the `O(\log n)`
Domination-Lemma route (shown here, not just asserted, to give a growing —
not fixed — bound).

---

## 2. `intersecting-family-covering-construction` — Status: partial — Verdict: CHANGES REQUESTED

### What I independently re-derived / re-checked

**Theorem 2.2 (H-hitting characterization).** Re-derived both inequality
directions from scratch. Direction (a) (`x_H\le a_{n+1}`): for each `i\le n`,
some common prime of `\mathrm{rad}(a_i),\mathrm{rad}(a_{n+1})` lies in `H`
(the file uses `w(i,n+1)\in W=H` specifically), giving a common element for
the hitting condition. Direction (b) (`a_{n+1}\le x_H`): `x_H` hits `\Sigma_n`
so has a common prime with each `\sigma(i)\subseteq\mathrm{rad}(a_i)`, giving
`\gcd(x_H,a_i)>1` for all `i\le n`, i.e. admissibility, so minimality of
`a_{n+1}` forces `a_{n+1}\le x_H`. Both steps check out; no gap.

**A genuine generalization I found (not in the source file):** direction (a)
of the proof never actually needs `h=w(i,n+1)` to be the *minimum* of
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{n+1})` — any common element in `H`
suffices, and direction (b) never references `w(i,j)` at all. So Theorem 2.2
(and, downstream, Lemma 2.3 and Theorem 2.4) hold verbatim for **any** finite
`H` satisfying `persistent-backbone-monovariant`'s weaker Finite Covering
Backbone Conjecture (`H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne
\varnothing`), not just `H=W`. I verified this generalization line-by-line
and certified it as the primary statement in
`lemmas/theorem-2.2-H-hitting-characterization.md` and
`lemmas/theorem-2.4-conditional-eventual-periodicity.md`, crediting both
approaches. **This is real synergy**: it means the two open approaches'
targets are compatible and the weaker one (persistent-backbone-monovariant's
reformulated conjecture) is now known to be *sufficient*, not just
plausible, for the conditional-periodicity bridge.

**Lemma 2.3 (Σ-stabilization).** Standard finite ascending-chain argument on
a bounded-above non-decreasing integer sequence; re-derived, correct.

**Theorem 2.4 (conditional eventual periodicity).** Re-derived the pigeonhole
argument on the functional graph of `G:\mathbb Z/L\mathbb Z\to\mathbb Z/
L\mathbb Z`: `L+1` values `r_0,\dots,r_L` in a domain of size `L` force a
repeat `r_{k_1}=r_{k_2}`, and since `G` doesn't depend on the step index,
this propagates to full periodicity of `(r_k)_{k\ge k_1}` with period
`T=k_2-k_1\le L`. The final step ("sum over one period is rotation-
invariant") is a correct, if terse, elementary fact about periodic sequences.
No gap found.

**The `a_1=35,65` negative-finding numerics.** I independently recomputed
these using Python and reproduced the exact claimed values (`min hitting
Σ_2 after a_2 = 42 = a_3` vs `min hitting Σ_stable after a_2 = 50` for
`a_1=35`; `75=a_3` vs `80` for `a_1=65`). **However**, I found a labeling
error: the file states `H=\mathrm{rad}(35)=\{2,5,7\}` and `H=\mathrm{rad}
(65)=\{2,5,13\}`, but `\mathrm{rad}(35)=\{5,7\}` and `\mathrm{rad}(65)=
\{5,13\}` — neither actually contains `2`. Recomputing with the literal
`\mathrm{rad}(a_1)` (no extra `2`) does **not** reproduce the claimed numbers
(e.g. `w(2,3)=2\notin\{5,7\}` for `a_1=35`, so that `H` doesn't even satisfy
Theorem 2.2's covering hypothesis). The numbers only reproduce with the
literal set `\{2,5,7\}`/`\{2,5,13\}` actually used, i.e. `\mathrm{rad}(a_1)
\cup\{2\}`, not `\mathrm{rad}(a_1)` as labeled. This is a real but minor
sloppiness: the substance of the (explicitly disclosed as exploratory, not
load-bearing) negative finding is unaffected — the numbers used and reported
are internally consistent and correctly computed, just mislabeled. Flagging
this for the builder to fix the label in the next revision; it does not
change the Status or verdict since this section is honestly presented as an
empirical probe, not a proof step, and no theorem in the file relies on the
mislabeled claim.

### Verdict rationale

Theorem 2.2, Lemma 2.3, and Theorem 2.4 are correct, rigorous, and are
genuinely new — the first complete "finite covering set ⟹ eventual
periodicity" bridge produced by this population in two rounds of work. This
is real, substantial progress (I rate it stronger progress than round 1's
content from this same approach). The approach is honest about what remains
open (existence of `H`; periodicity from `n=1`) and does not overclaim —
Status `partial` is correct as self-reported. **CHANGES REQUESTED**: fix the
`rad(a_1)` labeling error in the Gap-2 negative-finding section; then attack
either (a) the Finite Covering Backbone Conjecture directly (now known,
per the reviewer's generalization, to be sufficient — not just `W` finite),
or (b) periodicity-from-`n=1` using a genuinely correct `H` (e.g. wait for
the sibling to supply one, or hand-compute `W` restricted to a small worked
Case-II example beyond `a_1=15`).

---

## Lemmas certified this round

All independently re-derived/re-verified by the reviewer (not just re-read),
written into `results/imo-2026-06/lemmas/`:

1. `lemma-C-global-intersection-collapse.md` — Lemma C, full proof, plus the
   `a_1=65` sharpness example re-verified by simulation.
2. `proposition-NC1-collapse-point-backbone-insufficient.md` — `a_1=221`
   counterexample, re-verified by simulation.
3. `proposition-NC2-witness-not-bounded-by-rad-a1.md` — `a_1=375`
   counterexample, re-verified by simulation.
4. `theorem-2.2-H-hitting-characterization.md` — certified with the
   reviewer-found generalization (weaker "covering set" hypothesis instead
   of `H=W`), proof re-derived line by line, explicitly crediting both
   approaches for the cross-synergy.
5. `lemma-2.3-sigma-stabilization.md` — standard, re-derived, certified.
6. `theorem-2.4-conditional-eventual-periodicity.md` — certified with the
   same generalized hypothesis as (4), proof re-derived in full.

No lemma was rejected this round; all six passed the full bar (sorry-free,
statement correct, no overclaim beyond what was proved).

## `current.md` updates

- Added round-2 entries under "Approaches tried" for both slugs plus the
  cross-approach synergy finding, without deleting round-1 content (renamed
  to "Approaches tried (round 1, unchanged)" for clarity).
- Added a round-2 summary block at the top of "Current best" stating the
  gap count has been reduced from three to two (existence of `H`;
  periodicity-from-`n=1`), pointing to the new conditional theorems, while
  preserving the round-1 "Current best" content below as valid background.
- Status remains `partial`. "Full proof" section unchanged (absent, as
  required for `partial`).

## Outcomes recorded

- `persistent-backbone-monovariant`, round 2: outcome `partial` — "Certified
  Lemma C and two proved-false natural conjectures (NC1, NC2, independently
  reverified); core existence gap (Finite Covering Backbone Conjecture)
  still fully open."
- `intersecting-family-covering-construction`, round 2: outcome `advanced` —
  "Proved (independently reverified) Theorem 2.2 + Lemma 2.3 + Theorem 2.4,
  the first complete conditional bridge to eventual periodicity; reviewer
  found the hypothesis generalizes to the sibling's weaker covering
  conjecture, tightening the shared remaining gap."

## Recommendation for next round

Both approaches now converge cleanly on the same two remaining gaps, with
the first (existence of a finite covering set `H` in the weaker
"persistent-backbone-monovariant" sense) now confirmed sufficient — not just
`W` finite — to unlock the conditional periodicity theorem. Next round
should either (a) put fresh effort directly on the Finite Covering Backbone
Conjecture with a genuinely new mechanism (NC1, NC2, and the `O(\log n)`
Domination-Lemma route are all now ruled out — do not re-attempt), or (b)
if 1-2 more rounds plateau there too, open a genuinely different framing
per CLAUDE.md's plateau-break guidance (the field has now spent 2 rounds on
variations of "find a finite covering/witness set," which is starting to
look like a single shared wall even though the three sibling approaches
reach it via different techniques).
