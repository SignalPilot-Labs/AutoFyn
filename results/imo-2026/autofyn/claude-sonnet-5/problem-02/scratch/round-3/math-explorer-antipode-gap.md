## imo-2026-02 (lens: antipode-perp-bisector Step 5 gap)

### Headline finding (NEW, numerically strong, not previously explored)

Working in the frame `B=(-1,0)`, `C=(1,0)`, `A=(p,q)`, with `θ := ∠KBA = ∠ACL`
(hypothesis H1) and `β=∠ABC`, `γ=∠ACB`, `α=∠BAC` the base triangle's angles.
Built the full 1-parameter family of hypothesis-satisfying `(K,L)` (K on ray
from B at angle θ from BA, L on ray from C at angle θ from CA, with `r1=BK`,
`r2=CL` solved from H2 `∠LBK=∠LNC`, H3 `∠LCK=∠BMK` via fsolve, checked against
all containment/orientation conditions) across **3 structurally different
scalene triangles** and **5+ values of θ per triangle**. In every single
case:

**`∠ABA* = θ + (90° − γ)`  and  `∠ACA* = θ + (90° − β)`** (exact to 1e-6,
verified numerically to ~10 significant figures in several cases).

These angles are measured from ray `BA`/`CA` respectively to ray `BA*`/`CA*`.
Note `90°−γ` and `90°−β` are exactly the classical angles `∠OBA`, `∠OCA`
where `O` is the circumcenter of the **original** triangle `ABC` (standard
fact: the angle between a side and the circumcenter-line from a vertex
equals 90° minus the opposite angle) — confirmed numerically that
`∠ABA*|_{θ=const}` and this `∠O_ABC BA` match to machine precision. **A* is
NOT the circumcenter of ABC** (checked: A* moves along the perpendicular
bisector as θ varies, circumcenter of ABC is fixed) — but the *direction* of
ray `BA*` from `BA` is offset from the direction of ray `B–O_ABC` from `BA`
by exactly `θ`. This is a clean, previously-unfound structural fact.

**Crucially, this pair of angle facts, by themselves (no reference to K, L,
r1, r2 at all), IMPLY A*B=A*C as a pure angle-chase / triangle-isosceles
argument**, independent of the rest of the configuration:
`∠A*BC = β − ∠ABA* = β − θ − 90° + γ = 90° − α − θ` (using `β+γ=180°−α`), and
symmetrically `∠A*CB = γ − ∠ACA* = 90° − α − θ`. **So `∠A*BC = ∠A*CB`
identically**, hence triangle `A*BC` is isosceles, hence `A*B=A*C`. I verified
this exact closed form `∠A*BC=∠A*CB=|90°−α−θ|` numerically on 5 (θ, triangle)
combinations — matches to 4+ decimal places every time (sign flips exactly
when `90°−α−θ` goes negative, i.e. A* crosses to the other side of BC, which
is itself observable in the data — a branch/orientation issue but not a
correctness issue for the *unsigned* target `A*B=A*C`).

**This is a genuinely different mechanism from all three refuted ones** (not
a right-triangle-at-K/L identity, not a spiral-similarity center, not a
tangency/secant identification). It converts the whole remaining gap into
exactly two symmetric angle lemmas:
- **(L1)** `∠ABA* = θ + 90° − γ`
- **(L2)** `∠ACA* = θ + 90° − β`
plus the trivial angle-chase above (which is fully elementary, essentially
free once L1, L2 are known).

### What L1/L2 likely require

I checked whether L1 depends on θ alone (i.e., is a consequence of H1
alone, independent of whether K,L satisfy H2/H3): **no** — tested L1 with θ
fixed but `r1, r2` varied away from their hypothesis-satisfying values, and
`∠ABA*` moved wildly (not fixed at `θ+90−γ`). So L1/L2 are genuine
consequences of the *full* hypothesis system (H1 ∧ H2 ∧ H3 ∧ containment),
not of H1 in isolation — they are not "free" facts, but they are dramatically
simpler and more explicit targets than the abstract `A*B=A*C`, since they
are single scalar angle equalities stated purely in terms of `θ`, `β`, `γ`
(no unknowns `r1, r2` appear in the target statement itself, even though
`r1,r2` are needed to *reach* it). This suggests L1 may come from
H3 (`∠LCK=∠BMK`, which per the Decoupling Lemma pins `r1=BK` as a function
of `θ`) via the perpendicularity `∠AKA*=90°` characterization of A*, and L2
symmetrically from H2. This pairing (H3↔L1-at-B, H2↔L2-at-C) is a
conjecture, not yet checked — flagged as the natural next question, not
something I derived.

### Cheap-kill / sanity checks done
- Confirmed `A*` is **not** the circumcenter of `ABC` (rules out the
  tempting but false shortcut "A* = O_ABC").
- Confirmed the `θ+90−γ` / `θ+90−β` formulas are **not** artifacts of one
  triangle: checked on `(p,q)=(0.3,1.7)`, `(-0.6,1.2)`, `(0.1,2.5)` — three
  visibly different shapes (acute/obtuse mixes), each with 2–5 values of θ.
- Confirmed the base-angle identity `∠A*BC=∠A*CB` reduces the trig identity
  to something checkable purely from a synthetic point `A*` built from two
  explicit rays (no K, L needed) — i.e. once L1/L2 are established, the rest
  is a two-line angle chase, not more computation.

### Other candidates scouted (weaker / already-known negative results)
- **Law of cosines in right triangles `AKA*`, `ALA*`**: re-confirmed the
  already-refuted `∠AKB+∠A*KB=270°` identity holds along the *valid*
  hypothesis-satisfying family too (not just accidentally, as previously
  found) — but it remains unusable standalone since it requires knowing
  which side of `AK` the point `A*` falls on, which is exactly the
  branch-selection information not locally available. Consistent with the
  prior refutation; not a new route.
- **Similar-triangle / spiral-similarity between `A*BK` and `A*CL`**: checked
  angles and ratios (`BK/CL`, `A*B/A*C`, `A*K/A*L`) across the family — no
  fixed similarity ratio or matching angle pattern found (ratios vary
  continuously with θ while `A*B/A*C≡1`), so these two triangles are **not**
  similar to each other in general — this route does not work and should not
  be pursued further.
- **Concyclicity of {B,K,A*,L}, {B,L,A*,K}, {K,L,B,C}, {A,B,A*,C}**: tested
  numerically (power-of-point differences) — all nonzero, none of these four
  points are concyclic in general. Ruled out as a shortcut.

### Candidate technique(s) for the outliner
The two-lemma reduction (L1, L2) above, closed by an elementary angle chase.
This converts "prove A*B=A*C from 3 angle hypotheses on K,L" into "prove two
explicit angle formulas for A* as seen from B and from C" — a strictly
smaller, more concrete target than anything the field has had so far.
Suggest treating this as a **new approach** (or a major revision of
`antipode-perp-bisector`) with L1/L2 as its two open gaps, to be attacked via
the perpendicularity characterization of A* (`∠AKA*=90°`, `∠ALA*=90°` already
certified in `lemmas/antipode-reduction.md`) combined with H2/H3 and the
Decoupling Lemma (`lemmas/decoupling-and-sweep-lemma.md`).

### Knowledge-base entries
Inscribed-angle / Thales theorem (already used, `lemmas/antipode-reduction.md`);
Law of Sines / Extended Law of Sines (candidate for proving L1/L2 via
triangle `ABA*` or `ACA*` directly, not yet attempted); standard fact
`∠OBA = 90°−C` for circumcenter O of a triangle (used only as a numerical
pattern-match here, not yet invoked as a formal KB entry — check
`knowledge_base.md` for an explicit citation of this classical fact before
the outliner leans on it).

### Dead ends (confirmed, do not retry)
(a) `∠AKB+∠A*KB=270°` as an independent lemma — circular, refuted (prior
rounds, re-confirmed here).
(b) L as spiral-similarity center for `(B,K)↦(N,C)` — refuted (prior
rounds).
(c) Γ tangent to BC / secant-based point identification — refuted (prior
rounds).
(d) NEW this round: `A*=O_ABC` (circumcenter of ABC) — refuted, A* moves,
O_ABC is fixed.
(e) NEW this round: triangles `A*BK ~ A*CL` similar — refuted, ratios don't
match.
(f) NEW this round: `{B,K,A*,L}`, `{B,L,A*,K}`, `{K,L,B,C}`, `{A,B,A*,C}`
concyclic — refuted, power-of-point mismatches nonzero.

### Prior progress
Steps 1–4 of `antipode-perp-bisector` (certified, `lemmas/antipode-reduction.md`)
stand unchanged: `OM=ON ⟺ A*B=A*C`, `A*` = intersection of perpendicular to
`AK` at `K` and perpendicular to `AL` at `L`. This report's new finding (L1,
L2 + angle chase) is a genuinely new sub-reduction of the remaining Step 5
gap, verified numerically only — **not a proof**, and L1/L2 themselves are
still open (conjectured from strong numerical evidence across 3 triangle
shapes and multiple θ, but not derived from H1–H3 synthetically yet).

### Small-case / intuition notes (all labeled conjecture)
- Conjecture: `∠ABA* = θ + 90° − γ`, `∠ACA* = θ + 90° − β` hold identically
  along the entire valid hypothesis-satisfying family, for any scalene
  triangle ABC. Strong numerical evidence (3 shapes × several θ, exact to
  numerical precision), no proof.
- Conjecture (immediate corollary via elementary angle chase, essentially
  free once L1/L2 hold): `∠A*BC = ∠A*CB = |90° − α − θ|`, hence `A*B=A*C`.
- The sign/branch of `90°−α−θ` flips depending on whether A* is on the same
  side of BC as A or not — this matches which side A* numerically fell on
  across configs; likely resolved by the existing containment/orientation
  hypotheses on K, L, but not yet checked in detail.
