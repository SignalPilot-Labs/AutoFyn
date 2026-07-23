# Slack Collapse Lemma — the upper-bound induction reduces to the tight case k=m+1

**Certified by:** proof-reviewer, round 5, from approach `potential-weighting-upper-bound`
(round-5 builder, §7.1). Independently re-verified by the reviewer (direct re-derivation from
the already-certified Fact 5, plus independent recomputation of the two worked instances
cited as sanity checks).

**Depends on:** the already-certified `lemmas/insertion-and-cascade-facts.md` (Fact 5,
chain-cancellation: any `L`-element multiset can be driven to `e=0` exactly using exactly `L`
physical cuts) and Fact 1 (`e(M)\ge0` always, in `lemmas/dominant-extraction.md`).

## Statement

Let `A=(a_1\ge\dots\ge a_k)` be any sorted multiset of nonnegative reals (no restriction to
any case split), with `k\le m`. Then Xiang Yu can force `e(\text{final})=0` using `\le m`
cuts; consequently `g(A,m)=0\le e_m\cdot S(A)` trivially (since `e_m>0`, `S(A)\ge0`).

**Corollary.** The entire upper-bound induction (both Case (i) and Case (ii), at every level
`m`) reduces to the single tight sub-case `k=m+1` — every configuration with `k<m+1` (i.e.
Liu Bang left some of his marks unused) is disposed of immediately, with no casework and no
invocation of any inductive hypothesis.

## Proof

Apply Fact 5 to the multiset `\{a_1,\dots,a_k\}` itself (`L:=k`): this gives an explicit
sequence of exactly `k` physical cuts (applied only to fragments of the `k` given pieces)
producing a final multiset with `e=0` exactly. Since `k\le m`, Xiang Yu has `\le m` cuts
available and uses exactly `k\le m` of them — the remaining `m-k` cuts simply unused, which
is legal since the problem requires only "at most `n`" (here `m`) marked points, not exactly
`n`. Since `e_m>0` and `S(A)\ge0`, `0\le e_m\cdot S(A)` holds trivially. `\blacksquare`

The Corollary follows immediately: the theorem's claim `g(A,m)\le e_m\cdot S(A)` is only
non-trivial when `k=m+1` (Liu Bang has used every one of his `n` marks); whenever `k<m+1`,
this Lemma closes it unconditionally, independent of which case (i)/(ii) the configuration
falls into or the specific values `a_1,\dots,a_k`.

## Verification

Independently re-derived by the proof-reviewer as an immediate corollary of the already
twice-independently-verified Fact 5 (no new computation needed for the general statement).
As a spot check, re-ran the underlying Fact 5 chain-cancellation construction independently
(2000 random trials, exact `fractions.Fraction`, sizes 0–6) confirming `e=0` is always
achieved using exactly `L` cuts — the mechanism this Lemma directly invokes.

## Reusable by

Any approach running an induction over Liu Bang's opening configurations that wants to
restrict attention to the tight case `k=m+1` without separately handling `k<m+1` — directly
applicable to `dyadic-cascade-induction`'s Case (i)/(ii) closures and its open Step-4
multi-cut gap (all of which could cite this Lemma to skip ad hoc handling of slack
configurations), and to any future approach's own upper-bound induction. **Scope note:** this
closes only the *slack* regime (`k<m+1`); the genuinely hard case `k=m+1` (where every prior
counterexample and open sub-case in this population's history already lives) is untouched by
this Lemma and remains open.
