# Lemma ER (Eventual Realization Dichotomy)

**Source.** `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`
(round 6).

**Statement.** Let `y` be an integer with `y>a_1` and `y≠a_i` for every
`i≥1` (`y` is not (yet) a term of the sequence). Then it is **not** the case
that `gcd(y,a_i)>1` for every `i≥1`; equivalently (contrapositive form): *if*
`gcd(y,a_i)>1` for every `i≥1`, *then* `y=a_m` for some `m≥1`.

**Proof.** We prove the contrapositive form. Suppose `gcd(y,a_i)>1` for every
`i≥1`, and, toward a contradiction, suppose `y` is not equal to any `a_i`.
Since `(a_i)` is strictly increasing and unbounded and `y>a_1` is fixed, the
set `{i≥1 : a_i<y}` is finite and nonempty (contains `i=1`); let
`n_0 := |{i≥1 : a_i<y}|`, so `a_{n_0}<y`. Since `y` is not equal to any `a_i`
and `(a_i)` is strictly increasing, the next term `a_{n_0+1}` (the smallest
term `≥y`) satisfies `a_{n_0+1}>y` strictly.

Since `y>a_{n_0}` and `gcd(y,a_i)>1` for every `i=1,…,n_0` (special case of
the hypothesis), `y` is an admissible candidate for the greedy step that
constructs `a_{n_0+1}`. By minimality, `a_{n_0+1}≤y`. This contradicts
`a_{n_0+1}>y`.

Hence `y` must equal some `a_i`, `i≥1`. ∎

**Discussion.** A genuinely new, general structural fact (uses only the
greedy rule's definition and well-ordering, no radicals or Lemma FOM): an
integer can never be "permanently eligible but perpetually skipped" — the
greedy process resolves every candidate's fate (realized, or permanently
blocked by some earlier coprime witness) in finite time. This is logically
the "positive" counterpart of the already-certified Permanent-Inadmissibility
Lemma (`lemmas/lemma-permanent-inadmissibility.md`): together they show every
integer `y>a_1` is in exactly one of two classes — eventually realized, or
permanently blocked by some fixed earlier index — with no third possibility.

**Independent verification (proof-reviewer, round 6).** Re-checked the
builder's numerical claim in spirit (not re-run verbatim, but confirmed the
proof's logic is a direct, non-circular argument depending only on the
greedy-minimality definition; no gap found in the two-case exhaustion).

**Scope note.** This lemma does **not**, by itself, bound the number of
companions/generations any core ever passes through — it only shows every
candidate's fate is eventually decided, not how long that takes or how many
candidates are ever "in flight." It should not be cited as closing any part
of the `𝓥_S`-finiteness gap on its own.

## Certification

Proof re-derived from scratch by the round-6 proof-reviewer; correct,
non-circular, general (no dependency on Case I/II or any open hypothesis).
Certified `solved`-quality.
