# Lemma WO++ (Joint CRT Independence) + Theorem MO (Minimality
Obstruction) + Proposition MO-2 (Enrichment Collapse)

**Source.** `approaches/intersecting-family-covering-construction.md`,
Part 13 (round 14). Depends only on already-certified Lemma WO
(`lemmas/lemma-WO-window-occupancy-and-proposition-BI.md`), Lemma XC, and
Lemma NIDF(a) (`lemmas/lemma-XC-NIDF-FT-cross-companion-transversal.md`).

## Lemma WO++ (Joint CRT Independence) — certified as stated, unconditional

**Statement.** For any finite set of primes `W` disjoint from `P_1`,
modulus `M:=L_0\cdot\prod_{q\in W}q`, nonempty `S'\subseteq P_1`, and any
joint-residue event `E\subseteq\prod_{q\in W}\mathbb Z/q\mathbb Z`: every
window of `M` consecutive integers contains exactly `c_{S'}\cdot|E|`
integers of `P_1`-type `S'` with joint residue mod `W` in `E`, independent
of the window's location.

**Proof.** Direct CRT bijection extending Lemma WO's own argument by one
extra coordinate block (the primes of `W` are pairwise distinct from `P_1`
and from each other by hypothesis). **Reviewer independently re-derived
this by hand** (elementary, no gap) **and independently re-verified
numerically**: `P_1=\{13,19\}`, `S'=\{19\}` (`c_{S'}=12`), `q=5`, window
`(1000,1000+1235]` — got exactly `12` per residue class mod `5` in all `5`
classes, exact match. `\blacksquare`

**Corollary (Admissibility-Blindness).** The fraction of type-`S'`
integers in a window divisible by at least one prime of `W` is
`1-\prod_{q\in W}(1-1/q)`, independent of `S'`.

## Theorem MO (Minimality Obstruction) — certified as stated, unconditional

**Statement.** Fix a doubly-infinite disjoint core pair `(S,S')` and fix
any `i\in I_S`. No function of `S(y)` alone determines or biases whether a
type-`S'` candidate `y` is admissible against `a_i`: the fraction of
type-`S'` integers admissible against `a_i` in a large window equals the
fraction among ALL integers, `1-\prod_{q\in\mathrm{comp}(a_i)}(1-1/q)`.

**Proof.** By Lemma XC (`S(y)=S'` disjoint from `S(a_i)=S`), `\gcd(y,a_i)
>1\iff y` divisible by some prime of `W:=\mathrm{comp}(a_i)` (nonempty by
Lemma NIDF(a)). Apply Lemma WO++'s Corollary with this `W`. `\blacksquare`
Reviewer re-derived this composition by hand — correct, no gap.

## Proposition MO-2 (Enrichment Collapse) — certified as stated,
unconditional

**Statement.** If a finite prime set `W_0` (disjoint from `P_1`) secures
type-`S'` admissibility against `I_S` for EVERY integer `y` of type `S'`
(not just realized sequence terms) and every `i\in I_S`, then `W_0`, in
particular restricted to actual members of `I_{S'}`, is a covering witness
set for the Stabilization Conjecture's pair `(S,S')` (Theorem SW sense).

**Proof.** Trivial specialization (`y:=a_j` for `j\in I_{S'}`) of a
universally-quantified hypothesis. `\blacksquare` Reviewer confirms this
is correct and adds no unstated assumption.

## Scope correction (reviewer, load-bearing — read before citing the
approach file's headline claim)

The approach file's headline states Theorem MO "rigorously proves an
entire technique family (bounded-modulus/CRT minimality selection) cannot
resolve `BRL(S')`/`G`-periodicity." **The three individual results above
are each independently correct and certified as stated** — but this
headline synthesis is broader than what is formally established. What is
rigorously proven is a **two-point dichotomy**, not an exhaustive
impossibility over every conceivable bounded-modulus mechanism:

1. A tool built from the bare `P_1`-alphabet alone (Lemma WO's raw
   material) is provably powerless for a *single fixed witness*
   `a_i` — Theorem MO. This is airtight (an exact CRT-independence fact).
2. A tool using a *fixed enriched* set `W_0` strong enough to guarantee
   admissibility for *every* type-`S'` integer against *every* `i\in I_S`
   collapses to the covering-witness condition itself (Proposition MO-2)
   — also airtight (trivial specialization).

**Not formally ruled out**: an intermediate mechanism — e.g. a fixed
finite `W_0` combined with a *pigeonhole/density* argument establishing
only that *some* type-`S'` candidate within each window of bounded length
is admissible against the accumulated history so far (not that *every*
type-`S'` integer is admissible, and not restricted to *one* fixed prior
witness `a_i`). The approach file's own "Remark" and "Weaker version"
paragraphs in Part 13.3 give a plausible informal argument for why such an
intermediate mechanism would, in the presence of round 8-9's certified
`(UB_S)`-false-in-Case-II result (companion-prime sets can be unbounded
across a class), likely also collapse into either case 1 or case 2 above
— but this argument is discursive, not a third formal theorem. **The
certified content retires the two tested extremes of the technique
family, with a well-reasoned (but not fully formalized) case for why the
gap between them is empty — not a complete impossibility proof for every
conceivable bounded-modulus mechanism.** Future work wanting to close this
gap fully would need to formalize the intermediate case explicitly.

## Certification

Certified `solved`-quality (sorry-free) for Lemma WO++, Theorem MO, and
Proposition MO-2 exactly as individually stated above. The approach file's
broader "retires an entire technique family" headline is **downgraded to
partial** in this certification record: correct for the two proven
extremes, not (yet) a complete formal impossibility proof covering every
intermediate bounded-modulus mechanism. `BRL(S')`/`G`-periodicity itself
remains open, correctly not claimed resolved or refuted by this content.
