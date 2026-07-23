# Generalized Lemma C (arbitrary index-subsequence version)

**Statement.** Let `I = {i_1<i_2<i_3<⋯}` be **any** infinite subsequence of
`ℕ`. Define `C^I_m := ⋂_{l=1}^m rad(a_{i_l})`. Then `(C^I_m)` is
non-increasing and stabilizes: there is a finite `m_0` with
`C^I_m = C^I_{m_0} =: C^I_∞` for all `m≥m_0`.

**Proof.** `C^I_{m+1} = C^I_m ∩ rad(a_{i_{m+1}}) ⊆ C^I_m` directly from the
definition of intersection, so `|C^I_m|` is non-increasing, bounded above by
`|C^I_1| = |rad(a_{i_1})|` (finite, since `a_{i_1}` is a fixed integer) and
below by `0`. A non-increasing sequence of nonnegative integers can strictly
decrease only finitely many times, so it is eventually constant from some
finite `m_0`; combined with nesting `C^I_m⊇C^I_{m+1}`, constancy of `|C^I_m|`
for `m≥m_0` forces `C^I_m=C^I_{m_0}` exactly for all `m≥m_0`. `∎`

**Discussion / negative finding (kept for the record).** This is a direct
generalization of the already-certified Lemma C (Global Intersection
Collapse) to any infinite index subsequence, not just `1,2,3,…`. One natural
application — for a doubly-infinite `P_1`-imprint class `S` (see Lemma FX2),
apply this to `I=I_S` to get a stable "extended imprint" `S^+ ⊇ S`, and
conjecture that for every channel `(S,S')` between two doubly-infinite
classes, `S^+∩S'^+≠∅` — was tested by direct computation and found **FALSE
in general**: for `a_1=247` (`P_1={13,19}`), the classes `S={13}`, `S'={19}`
have `S^+={13}`, `S'^+={19}` exactly over the first 4000 terms (no
enlargement), so `S^+∩S'^+=∅`, yet the channel `({13},{19})` is empirically
forced-finite anyway. **This specific closing mechanism (extended-imprint
overlap) does not explain observed finiteness and should not be re-attempted
without a new idea.**

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
(round 3).

**Certification.** The stabilization lemma itself is correct and reusable
(same proof template as the already-certified Lemma C, verified line by
line, no gap). The negative finding about extended-imprint overlap is
recorded as a flagged dead mechanism, not a new open claim. Certified
`solved`-quality for the lemma statement; the negative finding is descriptive
context, not itself a theorem requiring separate certification.
