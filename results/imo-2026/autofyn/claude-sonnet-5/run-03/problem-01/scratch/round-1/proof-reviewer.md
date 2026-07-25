# Proof review — imo-2026-01, round 1

Note on scope: `imo-2026-01`'s `difficulty_level` in `problems.jsonl` is `"medium"`
(`difficulty_rating: 5`), not `"hard"`. Per CLAUDE.md ("We target the hard problems
only... Ignore the easy and medium problems"), this run appears to be attacking a
problem outside the intended benchmark scope. Flagging this for the orchestrator;
proceeding with the requested review regardless since that's out of my remit to fix.

## Verdict summary
- `induction-on-active-count`: **APPROVE** — Status **solved**. Complete, correct,
  rigorous. No gap found.
- `lex-potential-gcd-invariant`: **CHANGES REQUESTED** — Status **partial** (builder
  claimed `solved`; overridden). Contains one false intermediate identity in the
  Setup section; otherwise complete and structurally sound.

`current.md` has been written with Status `solved`, using
`induction-on-active-count`'s full proof (verified correct end to end). Both
approach files are annotated; `lex-potential-gcd-invariant.md`'s Status field
corrected from `solved` to `partial` with a reviewer note explaining the exact
false claim and pointing to the one-line correct fix.

---

## `induction-on-active-count.md` — APPROVE (solved)

**Load-bearing step identified and independently re-derived:** the per-prime
identity `(v_p(g),v_p(q)) = (min(a,b),|a-b|)` (immediate from unique factorization,
`v_p(gcd)=min`, `v_p(lcm)=max`), and on top of it, Lemma SM's dichotomy (Drop:
active count `k` drops by exactly 1; Stall: `k` unchanged but the quadratic
potential `Σ = Σ_i Σ_p v_p(a_i)^2` strictly decreases). I recomputed both Lemma I1
(`min(a,b)^2+|a-b|^2 ≤ a^2+b^2`, equality iff `min(a,b)=0`) and Lemma I2
(`gcd(min(a,b),|a-b|)=gcd(a,b)`) from scratch by hand and by `python3` spot checks
(`gcd.py` sanity: `m=4,n=6→g=2,q=6,gq=12=lcm(4,6)`, `m=12,n=18→g=6,q=6,gq=36=lcm`,
etc.) — both hold exactly as stated. Lemma L1 (`g,q` not both `1`, via `gq=lcm(m,n)
≥ m>1`) is derived correctly and directly from the definition `q:=lcm(m,n)/g`
(no detour through the false `gq=mn` claim the sibling approach makes — see below).

**Part (a) — termination for ARBITRARY move order (the crux requirement).** This is
the part I scrutinized hardest, since the round-1 self-reported history flags a
prior draft that only handled a specific strategy ("isolate and resolve one pair at
a time"), not arbitrary interleaving. The fixed version proves `Theorem P(k)`:
"for every board `B` with `k(B)=k`, there is no infinite sequence of legal moves
starting at `B`" — this is a statement quantified over ALL boards with active count
`k` and, implicitly, over the first move of an ARBITRARY sequence `σ` from any such
board (not a fixed strategy). The induction is:
- Outer: strong induction on `k` (standard, well-founded on `ℤ≥0`).
- Inner (nested, for fixed `k`): strong induction on `Σ(B)`, invoked exactly when a
  move Stalls (`k` unchanged).
Given an arbitrary `σ` from `B`, its first move (whichever pair Confucius picks) is
governed by Lemma SM: either Drop (apply outer IH to the resulting `k-1`-board) or
Stall (apply inner IH to the resulting same-`k`, smaller-`Σ` board). Both branches
conclude the tail of `σ` is finite (since the corresponding IH asserts NO infinite
sequence exists from that board — a universal statement over all boards of that
type, so it applies regardless of which specific board `Move₁` produced, hence
regardless of which pair Confucius chose). This is the correct fix: the induction
never assumes anything about *which* pair is chosen at any step, at any depth of the
recursion — genuinely closing the interleaving gap. I checked the base cases
(`k=0,1`: no legal move exists, trivial) and the case-exhaustiveness of Lemma SM
(Drop vs Stall are the only two options, and are mutually exclusive by definition)
— both correct.

**Part (b).** `Lemma GP` (`G_p(B) = gcd` of the board's `p`-adic valuations is
invariant under every move) is proved via Lemma I2 plus the standard
"gcd of a multiset union = gcd of the gcds of its parts" fact (itself justified via
the common-divisor-set characterization, the same technique as Lemma I2 — not
black-boxed). Reconstruction of `M = ∏_p p^{G_p}` at the terminal board (one active
entry `M`, 2025 entries `=1`, so the multiset of `p`-valuations there is
`{v_p(M),0,...,0}`, whose gcd is `v_p(M)`) is correct, and well-definedness/
finiteness of the product (`G_p=0` for all but finitely many `p`, namely those
dividing some initial `a_i`) and `M>1` are explicitly verified, not asserted.

**No gaps found.** All theorems invoked are named (Fundamental Theorem of
Arithmetic, Euclidean algorithm identity, associativity of gcd over a multiset,
strong induction). No skipped cases. Both parts (a) and (b) are proven for
arbitrary Confucius play, not a special strategy. Final answer `M = ∏_p p^{G_p}` is
stated explicitly and verified via unique factorization + the invariant argument.
This meets the `solved` bar as defined in CLAUDE.md.

---

## `lex-potential-gcd-invariant.md` — CHANGES REQUESTED (partial, not solved)

Structurally this approach is nearly identical in strength to the sibling: a
lexicographic potential `(N,Σ)` (`N` = active count, `Σ` = same quadratic exponent
sum) for part (a), and the same `G_p`-invariant (via a general "multiset-gcd
decomposition" Lemma 3) for part (b). Lemma 1 and Lemma 2 (identical in content to
I1, I2 above) are correct, independently re-verified. The lex-order termination
argument (Claim 1/2/3) correctly handles arbitrary move choice: Claim 1 is proved
for an arbitrary single move (any `m,n`), so the strictly-decreasing-potential
argument applies regardless of Confucius's choices at every step — this is a valid
route to closing the interleaving requirement (an alternative but equally valid
strategy to the sibling's nested induction; well-ordering of the lex product on
`ℤ≥0 × ℤ≥0` is proved from first principles, not asserted).

**The flaw.** In the Setup section, immediately after defining a move, the proof
asserts:
> "Note `gq = gcd(m,n)·lcm(m,n) = mn` (standard identity, itself immediate from
> `v_p(g)+v_p(q) = min(a,b)+max(a,b) = a+b = v_p(m)+v_p(n)`... hence `gq=mn` by
> unique factorization)."

I re-derived this from scratch. `v_p(g)=min(a,b)` and `v_p(q)=|a-b|` (both stated
correctly earlier in the same Setup). So `v_p(g)+v_p(q) = min(a,b)+|a-b|`. This
equals `max(a,b)` (since `|a-b| = max(a,b)-min(a,b)`), **not** `min(a,b)+max(a,b) =
a+b`, unless `min(a,b)=0`. The proof's displayed chain silently swaps `|a-b|` for
`max(a,b)`, which is only valid when `min(a,b)=0`. The correct conclusion is
`v_p(g)+v_p(q) = max(a,b) = v_p(lcm(m,n))`, i.e. `gq = lcm(m,n)` — which is in fact
immediate from the definition `q := lcm(m,n)/gcd(m,n)`, requiring no valuation
argument at all.

I verified numerically that `gq=mn` is FALSE in general:
```
m=4, n=6:  g=gcd=2, q=lcm/gcd=12/2=6, gq=12,  lcm(4,6)=12,  mn=24   (gq=lcm, gq≠mn)
m=12,n=18: g=6, q=36/6=6,           gq=36,  lcm(12,18)=36, mn=216  (gq=lcm, gq≠mn)
```
(The true general identity is `gcd(m,n)·lcm(m,n)=mn` — a *different* product,
`g·lcm(m,n)`, not `g·q`.)

**Where this is used, and severity.** The false `gq=mn` claim is invoked twice:
1. In sub-case (i) (`g=1`) to conclude `q=mn`. Here the numeric conclusion happens
   to be correct — when `gcd(m,n)=1`, `lcm(m,n)=mn` by the true identity
   `gcd·lcm=mn`, so `q=lcm(m,n)/1=mn` — but the *stated justification* (division by
   the false general identity `gq=mn`) is invalid outside this special case.
2. In the "remark to close a loose end" (end of Claim 1's proof) to argue `g=1` and
   `q=1` cannot hold simultaneously, i.e. that the three-way case split (`g=1`;
   `g>1,q=1`; `g>1,q>1`) is exhaustive. This is exactly Lemma L1 from the sibling
   approach, and IS load-bearing for Claim 3 (`N` drops by at most 1, hence must
   pass through `N=1` rather than skip it). The stated justification ("since
   `gq=mn>1`") is false as a general argument; the correct one-line fix is
   `gq=lcm(m,n)≥max(m,n)>1` (proved as Lemma L1 in the sibling and now certified in
   `lemmas/euclidean-valuation-lemmas.md`).

Because the actual downstream facts needed (not both `g,q=1`; `q=mn` when `g=1`) are
true and trivially re-derivable via the correct identity, this is NOT a "the
approach is wrong" (RETHINK) situation — the whole route survives with a one-line
fix. But it IS a genuine false mathematical claim asserted as an established
"standard identity" in the body of the proof, not a hedge or a hand-wave the reader
could reasonably discharge themselves; CLAUDE.md's rigor rules are explicit that
"one wrong step sinks the proof" for `solved`. I therefore downgrade this approach's
Status from the builder's claimed `solved` to **partial**, with the exact gap
specified above (replace the false Setup identity `gq=gcd(m,n)·lcm(m,n)=mn` with the
correct, trivial `gq=lcm(m,n)` from the definition of `q`, and re-point the "not both
trivial" remark at the end of Claim 1 to use `gq=lcm(m,n)≥m>1` instead of the false
`gq=mn>1`). No other errors found; Lemma 3 (multiset-gcd decomposition/associativity)
and Claim 4 (`G_p` invariance, part (b)) were independently checked and are correct.

---

## Certified lemmas

Wrote `results/imo-2026-01/lemmas/euclidean-valuation-lemmas.md`, certifying (from
`induction-on-active-count`, since its derivations are fully correct and the
sibling's parallel Lemma 1/2/3 duplicate the same content with the one flaw
isolated above):
- **Lemma I1** (monovariant inequality) — certified, re-verified by hand.
- **Lemma I2** (gcd invariance under one Euclidean step) — certified, re-verified.
- **Lemma L1** (not both `g,q` trivial, via `gq=lcm(m,n)≥m>1`) — certified; this
  lemma file explicitly documents the sibling's `gq=mn` pitfall as a caution for
  future builders (`omega-linear-monovariant`, `token-multiset-crt-reconstruction`
  both reportedly share this mechanism per the ranking summaries, so they should
  check their own write-ups for the same slip before their next build).
- **Lemma SM** (Single-Move Lemma: Drop-or-Stall dichotomy) — certified.
- **Lemma GP** (`G_p`-invariance) — certified.

I did NOT certify `lex-potential-gcd-invariant`'s "Claim 1's exhaustive N-drop case
split" as flagged promotable in that file, since its exhaustiveness argument
currently rests on the false `gq=mn` identity; the equivalent, correctly-derived
content is now certified via Lemma L1 + Lemma SM above instead.

## Outcomes recorded (approach-ranker)
- `induction-on-active-count` — `verified-milestone`: full proof verified correct
  and complete; APPROVE, Status solved.
- `lex-potential-gcd-invariant` — `partial`: false intermediate identity
  (`gq=mn`, actually `gq=lcm(m,n)`) found in the Setup; conclusions drawn from it
  remain true via the correct identity but as written the claim is false; downgraded
  from claimed solved to partial.

## Files touched
- `results/imo-2026-01/current.md` — created/overwritten: Status `solved`, Full
  proof = `induction-on-active-count`'s (verbatim, verified).
- `results/imo-2026-01/approaches/lex-potential-gcd-invariant.md` — Status field
  corrected `solved → partial`, with a reviewer note pinpointing the false identity
  and the fix.
- `results/imo-2026-01/lemmas/euclidean-valuation-lemmas.md` — new, certified
  lemmas I1, I2, L1, SM, GP with a documented pitfall note about the `gq=mn` error.
