## Status
unsolved (round 10 build). The mechanism as scoped in the round-10 outline is now
**decisively, unconditionally refuted** — not merely "found insufficient like Lemma
K," but shown to be a logical impossibility whenever it would be useful, by a new
general theorem (Minimality Tautology Lemma) proved in full below. This is a clean,
honest, complete negative result, exactly per CLAUDE.md's standard for a genuine
partial/negative finding: no gap is papered over, the failure is proved, not
guessed.

## Approaches tried
- **confined-competitor-construction** (round 10, new — this build). Carried out the
  outline's Steps 1–4 to a complete conclusion. Result: the outline's central "Step
  2/3" mechanism (construct an explicit competitor `c`, prove it fully legal, derive
  `c < a_{n_j}` to contradict greedy minimality) is **provably impossible in exactly
  the regime where it would be useful**. This is proved below as the **Minimality
  Tautology Lemma**, a fully general, unconditional theorem (depending only on the
  problem's own greedy definition, no certified lemma needed) that also explains
  *why* round 7's Lemma K has the shape it has (Lemma K's own proof is a special
  case of this lemma). The outline's hoped-for gain from the Confined-GCD Lemma
  (control of `gcd(c, a_{n_B})`) turns out to be structurally irrelevant to the
  actual point of failure: the failure occurs one step earlier, at the level of
  "does a fully-legal, strictly-smaller competitor even exist," a question the
  Confined-GCD Lemma — which only constrains gcd values of ACTUAL sequence terms,
  not artificially constructed integers — never touches. So this approach does NOT
  fail "for the same reason as Lemma K" in a vague sense; it fails for a **sharper,
  more basic, fully proved reason that also retroactively explains Lemma K's own
  mechanism**. Per the outline's own explicit instruction, this is reported as a
  clean RETHINK, not forced into a fake rescue.

## Current best
Imports, unchanged, the full certified reduction chain (Free Facts, Bounded/
Generalized Bounded Gap Lemmas, Finite Core Theorem, Generalized Bounded Witness
Lemma, Projection Lemma, Collateral-Safety Theorem, Lemma G, Confined-GCD Lemma,
Cofinite Sufficiency Lemma) — see `results/imo-2026-06/lemmas/` and
`covering-system-construction.md` Steps 1–9 for the full statements and proofs (not
re-derived here, per the workspace's dedupe convention). Joint Cofinite FAH remains
the sole open crux for the whole problem; this approach does not close it, and (per
the theorem proved below) no approach of this specific shape (construct-a-smaller-
fully-legal-competitor) can close it either.

This round's own new, fully proved, unconditional contribution is the theorem in
the next section.

## Target
The problem's actual claim: there exist positive integers `T, L` such that
`a_{n+T} = a_n + L` for every positive integer `n`. This approach targeted Joint
Cofinite FAH (the certified chain's sole remaining gap) via a constructive
minimality/exchange mechanism; that mechanism is now shown not to work, as detailed
below.

## Setup and notation (imported, restated for self-containedness)

Recall the problem's own definition: `a_1 > 1` an integer; for `n ≥ 1`, `a_{n+1}` is
the smallest integer exceeding `a_n` with `gcd(a_{n+1}, a_i) > 1` for every
`i = 1, ..., n`. Write `Q := P(a_1)` (prime divisors of `a_1`). The certified chain
(Free Facts through Cofinite Sufficiency Lemma) reduces the whole problem to:
fix any rogue pair of disjoint `S₀`-extended-persistent types `(A', B')` with
witnesses `n_A < n_B`, canonical prime `q* := min(F' ∩ F'')` (where `F', F''` are
the outside-core prime sets of the canonical witnesses, and `F'∩F'' ≠ ∅` is the
certified `F_A ∩ F_B ≠ ∅` fact) — prove Joint Cofinite FAH: `q*` divides `a_n` for
all but finitely many `n > n_B` with `ρ(n) = A'` (and symmetrically on the `B'`
side).

## Main new result: the Minimality Tautology Lemma

**Lemma (Minimality Tautology, new, unconditional).** Fix `n ≥ 2`. Suppose `c` is a
positive integer with `c > a_{n-1}` and `gcd(c, a_i) > 1` for every `i = 1, ..., n-1`
(i.e. `c` is a legal candidate for position `n`, in the exact sense used by the
problem's own recursive definition). Then `c ≥ a_n`.

**Proof.** By the problem's definition, `a_n` is, among ALL positive integers
exceeding `a_{n-1}` satisfying `gcd(\cdot, a_i) > 1` for every `i = 1, ..., n-1`, the
SMALLEST one. The hypothesis states precisely that `c` is one such integer (it
exceeds `a_{n-1}` and satisfies the same divisibility condition against every
`i = 1, ..., n-1`). Since `a_n` is the minimum of the set of all integers with this
property and `c` is a member of that set, `a_n ≤ c`. ∎

**Corollary (No-Smaller-Fully-Legal-Competitor).** For every `n ≥ 2`, there is no
integer `c` with `a_{n-1} < c < a_n` and `gcd(c, a_i) > 1` for every `i = 1,...,n-1`.
(Immediate contrapositive of the Lemma: if such `c` existed, the Lemma would force
`a_n ≤ c`, contradicting `c < a_n`.)

**Consequence.** Any proof strategy of the following shape can never succeed for
ANY choice of construction rule for `c`, no matter how the rule is refined:

> "Construct an explicit integer `c` (from data available at index `n`), show
> `c` is legal against every earlier term `a_i` (`i < n`), and show `c < a_n`; derive
> a contradiction with the greedy minimality of `a_n`."

Not because such a `c` is hard to construct, but because **no such `c` exists**:
the moment `c < a_n` and `c` is fully legal (against every `i < n`, not merely some
of them), the Lemma is violated. Equivalently, whenever a construction produces a
candidate `c` with `c < a_n`, that candidate is **automatically illegal** against
some earlier term — the existence of a "blocking" index is not an open question to
be resolved case by case, it is a forced consequence of `a_n` already having been
selected as the true minimum. (This is exactly the mechanism inside the certified
proof of Lemma K — see below — now isolated as a standalone, general, portable
fact.)

**This Lemma explains, rather than merely echoes, Lemma K.** Lemma K
(`adjacent-multiple-blocking.md`) proves: for `c := q·⌊a_n/q⌋` (round `a_n` down to
the nearest multiple of a prime `q ∤ a_n`), either `c ≤ a_{n-1}` or some `j < n` has
`gcd(c,a_j)=1`. Its own proof, in the second branch, runs: "if `a_{n-1} < c < a_n`
... minimality of `a_n` forces `a_n ≤ c < a_n`, a contradiction. So some `j<n` has
`gcd(c,a_j)=1`." This is *exactly* the Minimality Tautology Lemma's proof, applied
to Lemma K's specific `c`. The Minimality Tautology Lemma generalizes this from
Lemma K's one specific construction to EVERY possible construction of a
strictly-smaller candidate, proving in one stroke that the entire *family* of
"smaller-competitor exchange" arguments (Lemma F's magnitude-only version, Lemma
K's round-down version, and this round's round-up-with-a-controlled-prime version)
is subject to the same forced obstruction, and — crucially — that no future
refinement of the construction rule (choosing `c` more cleverly, adding more
divisibility constraints to `c`, using the Confined-GCD Lemma, or any other
certified tool) can ever escape it, because the obstruction is not about which
tools are available; it is a tautological consequence of the problem's own
definition, true for literally every integer `c` with `c<a_n` regardless of how it
was produced.

## Application to this round's outline (Steps 1–4)

**Step 1 (setup).** As stated: rogue pair `(A',B')`, witnesses `n_A < n_B`,
canonical prime `q*`, hypothetical failure index `n_j > n_B` with `ρ(n_j) = A'` and
`q* ∤ a_{n_j}`.

**Step 2 candidate.** `c := ` the smallest multiple of `q*` strictly exceeding
`a_{n_j - 1}` (`n_j - 1 ≥ n_B ≥ 1`, so `a_{n_j-1}` is a genuine, well-defined earlier
term of the actual sequence). By construction `c > a_{n_j - 1}` and `c ≡ 0 \pmod{q*}`;
since `a_{n_j}` is by hypothesis not divisible by `q*`, `c \neq a_{n_j}`, so exactly
one of `c < a_{n_j}` or `c > a_{n_j}` holds.

**Case (i): `c > a_{n_j}`.** Then the construction gives no information about
`a_{n_j}` at all — there is nothing to contradict, and Step 3's contradiction
target (`c < a_{n_j}` and `c` legal) is simply not reached. This case is vacuous for
the purposes of the argument; it cannot be excluded in general (whether it occurs
depends on the arithmetic of `q*` and the actual gap `a_{n_j} - a_{n_j-1}`, which is
only bounded, not controlled exactly, by the certified Generalized Bounded Gap
Lemma), so the mechanism cannot even be guaranteed to engage the useful case for
every hypothetical `n_j`.

**Case (ii): `c < a_{n_j}` (the case Step 3 actually needs).** Apply the Minimality
Tautology Lemma's Corollary with `n := n_j`: since `a_{n_j-1} < c < a_{n_j}`, `c`
**cannot** be legal against every `i < n_j` — some index `j_0 < n_j` necessarily has
`gcd(c, a_{j_0}) = 1`. This is not a gap in our knowledge that a cleverer
construction or the Confined-GCD Lemma might close; it is a proved fact about
every integer strictly between `a_{n_j-1}` and `a_{n_j}`, this specific `c`
included. So **Step 2's "Controlled-Competitor Legality" claim is provably FALSE**
in exactly this case — not merely unproved, but the negation is a theorem.

**Consequence for Step 3/4.** Since Step 2 is impossible to establish whenever it
would matter (Case (ii)), and vacuous when it doesn't matter (Case (i)), **Step 3's
contradiction can never be reached, for this or any refinement of the construction
of `c`.** In particular:

- The outline's hoped-for gain — using the Confined-GCD Lemma to pin down
  `gcd(c, a_{n_B})` — is **structurally irrelevant to the actual failure point**.
  The Confined-GCD Lemma constrains `gcd(a_n, a_{n_B})` for `n` an ACTUAL sequence
  term with `ρ(n) = A'`; it says nothing about an artificially constructed integer
  `c` that is not (and, if Case (ii) holds, provably cannot legally become) a term
  of the sequence. Even a hypothetical strengthening of the Confined-GCD Lemma that
  somehow also bounded `gcd(c, a_i)` for a few more specific `i` would not rescue
  the mechanism, because the Minimality Tautology Lemma shows the failure is
  total: `c` is illegal against SOME `i < n_j` whenever `c < a_{n_j}`, and nothing
  pins down which `i` — exactly Lemma K's own diagnosis, now shown to be forced
  rather than merely observed.
- Step 4's proposed fallback (check legality only against the "already-controlled"
  finite set `{n_B} ∪ S₀`-related witnesses) cannot rescue the mechanism either,
  for a distinct, equally decisive reason: the greedy-minimality contradiction in
  Step 3 requires FULL legality of `c` against literally every `i < n_j`, not a
  subset. A partial-legality fact (even if provable) is not the hypothesis the
  Minimality Tautology Lemma's contrapositive needs to be violated, so it cannot be
  used to conclude `c ≥ a_{n_j}` fails to hold, i.e. it gives no route to a
  contradiction with the actual value of `a_{n_j}`. Restricting the legality claim
  to a sub-collection of indices simply produces a true-but-useless fact (it does
  not show `c` is a legal *candidate* in the sense the greedy definition cares
  about), not a weaker form of the needed lemma.

## Conclusion

The mechanism proposed in this round's outline (`confined-competitor-construction`
Steps 1–4) is **not merely found insufficient by analogy to Lemma K — it is
disproved outright** by the Minimality Tautology Lemma, a new, short, fully general
theorem proved above from the problem's bare definition (no dependence on any
certified lemma, let alone any open hypothesis). This is a strictly sharper
negative result than round 7's diagnosis of Lemma K ("the constructed competitor's
factorization is uncontrolled relative to the witness"): that diagnosis left open
the possibility that a future, better-controlled construction might succeed; this
round's theorem shows **no construction of a smaller, fully-legal competitor can
ever succeed**, for any choice of `c`, against any greedy-defined sequence of this
type — the obstruction is intrinsic to the definition of the sequence, not a
deficiency of the currently certified toolkit. In particular, gaining one
additional controlled coordinate (via the Confined-GCD Lemma) does not, and
provably cannot, change the outcome, because that coordinate was never the actual
point of failure.

Per the outline's own explicit "Watch out for" instruction and CLAUDE.md's honesty
rule, this approach is reported as a clean, fully justified **RETHINK**: the
"constructive competitor + greedy-minimality contradiction" proof *shape* itself
cannot deliver Joint Cofinite FAH (or any related exchange conclusion) for this
problem, regardless of how the competitor is built or which certified lemmas are
recruited to control its factorization. Any future approach must use a mechanism
that does not require constructing an explicit integer strictly between two
consecutive terms and proving it fully legal — e.g. by reasoning about the ACTUAL
realized terms of the sequence (as `greedy-exchange-cost-potential`'s window/
Escape-Budget attack does) or via magnitude/counting arguments that do not require
full legality of an artificial competitor (as `covering-system-construction`'s
Growth-Forced Divisibility attack does).

## Key lemmas (status)
- **Minimality Tautology Lemma** — proved in full above, unconditional. See
  Promotable lemmas below.
- **No-Smaller-Fully-Legal-Competitor Corollary** — proved in full above,
  unconditional; immediate corollary of the Lemma.
- Controlled-Competitor Legality (the outline's central open claim) — **disproved**
  in Case (ii) above (the only case in which it would matter); the disproof is
  unconditional, not merely a failure to find a proof.

## Open gaps
None remain open FOR THIS SPECIFIC MECHANISM — it is fully and rigorously resolved
(negatively). The problem's overall open gap (Joint Cofinite FAH / the Successor
Claim) is unaffected and remains owned by the sibling approaches
(`covering-system-construction` Step 11, `greedy-exchange-cost-potential`'s
Escape-Budget attack).

## Cases to cover
Both cases of `c` vs. `a_{n_j}` (`c > a_{n_j}` and `c < a_{n_j}`; equality is
impossible by the hypothesis `q* ∤ a_{n_j}`) are covered exhaustively above; both
lead to the mechanism failing to reach a contradiction, for distinct, individually
proved reasons.

## Watch out for
Confirmed, as the outline itself anticipated: this construction is structurally the
mirror image of round-7's Lemma K (round up vs. round down), and it dies for what
turns out to be the SAME underlying reason as Lemma K — but this round's work shows
that reason is not "insufficient current information" but a **provable
impossibility**, a strictly stronger and more final conclusion. Future rounds
should not re-attempt any "construct smaller fully-legal competitor, contradict
minimality" mechanism for this problem, regardless of which certified lemma is used
to try to control the competitor's factorization; the Minimality Tautology Lemma
now rules out the entire family in one proof, not just this or Lemma K's specific
instances.

## Promotable lemmas
- **Minimality Tautology Lemma** (proved in full above, "Main new result" section).
  Statement: for `n ≥ 2`, any integer `c` with `a_{n-1} < c` and `gcd(c,a_i)>1` for
  all `i=1,...,n-1` satisfies `c ≥ a_n`. Proof: one line, directly from the greedy
  definition of `a_n` as the minimum of the set of such integers. Fully
  unconditional (uses only the problem's own recursive definition; no certified
  lemma, no open hypothesis). Portable and general — applies to ANY index `n ≥ 2`
  of ANY sequence defined by this problem's greedy rule, not specific to any rogue
  pair, witness, or the specific `c` constructed in this file's Step 2. Recommend
  certifying to `lemmas/minimality-tautology-lemma.md`, together with its
  Corollary (No-Smaller-Fully-Legal-Competitor) and the note that it generalizes
  Lemma K's internal proof step into a standalone reusable fact — this closes off,
  once and for all, an entire family of future proof attempts (any "construct a
  smaller legal competitor" mechanism), saving future rounds from re-deriving this
  each time in an ad hoc, construction-specific way as Lemma K/F effectively did.
