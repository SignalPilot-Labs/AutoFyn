## Lemma: Minimality Tautology Lemma (CERTIFIED, round 10, scope-narrowed)

**Source.** `confined-competitor-construction`, round 10.

**Depends on.** Nothing beyond the problem's own defining recursion (no certified
lemma needed).

**Statement (certified form).** Fix `n ≥ 2`. If `c` is a positive integer with
`c > a_{n-1}` and `gcd(c, a_i) > 1` for every `i = 1, ..., n-1`, then `c ≥ a_n`.

**Corollary (No-Smaller-Fully-Legal-Competitor).** For every `n ≥ 2`, there is no
integer `c` with `a_{n-1} < c < a_n` and `gcd(c, a_i) > 1` for every `i = 1,...,n-1`.

**Proof.** By the problem's own definition, `a_n` is the minimum of the set of all
integers exceeding `a_{n-1}` satisfying `gcd(\cdot,a_i)>1` for every `i=1,\dots,n-1`.
The hypothesis states `c` is a member of exactly this set, so `a_n \le c`. The
Corollary is the immediate contrapositive. ∎

**Reviewer verification.** Independently re-derived from the problem statement with
no shortcuts — this is a direct, one-line unpacking of "`a_{n+1}` is the SMALLEST
integer `>a_n` satisfying [condition]" applied to a hypothetical integer that also
satisfies [condition]; no gap, no hidden step. Confirmed correct and unconditional.

**Certified scope — READ CAREFULLY, narrower than the source file's framing.** This
Lemma and its Corollary are certified exactly as stated above: they rule out, for
any index `n`, the existence of an integer strictly between `a_{n-1}` and `a_n` that
is legal (`gcd>1`) against *literally every* earlier term `a_1,\dots,a_{n-1}`. This
correctly kills any proof strategy whose intermediate goal is to establish FULL
legality of an explicitly constructed smaller candidate `c` and derive a direct
contradiction from that (the source file's Steps 2–3 for `confined-competitor-
construction`'s round-10 outline are exactly of this shape, and are correctly killed
by this Lemma).

**What is NOT certified: the source file's broader "kills the whole family of
competitor-construction mechanisms" framing.** The Lemma does *not* show that
strategies which use the *guaranteed existence of a blocking index* `j_0 < n` with
`gcd(c,a_{j_0})=1` (rather than trying to prove full legality) are dead — indeed
round 7's Lemma K (`adjacent-multiple-blocking.md`) is exactly such a strategy,
survives as valid (if insufficient) certified content, and this Lemma correctly
explains *why Lemma K's proof has the shape it has* (Lemma K's internal step is a
direct instance of this Lemma's contrapositive) without contradicting Lemma K's
own certified statement. The reviewer's assessment: the source file's own worked
argument (Steps 1–4, "Application to this round's outline") stays within the
certified scope above and is correct; its summary language in "Watch out for" and
"Promotable lemmas" ("kills this whole family... regardless of how the competitor
is built or which certified lemmas are recruited") overstates the result if read as
covering blocking-index-based (Lemma K-style) mechanisms too — those are a distinct
proof shape not addressed by this Lemma, still open in principle, though separately
diagnosed as insufficient by round 7 for an unrelated reason (uncontrolled
identity of the blocking index). Future rounds should read this Lemma's reach as:
"rules out full-legality-then-contradiction competitor constructions, permanently
and for any construction rule" — not as "rules out all competitor-construction
mechanisms whatsoever."
