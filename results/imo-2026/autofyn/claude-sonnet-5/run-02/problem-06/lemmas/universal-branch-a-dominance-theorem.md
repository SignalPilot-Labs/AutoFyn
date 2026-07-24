## Lemma: Universal Branch-(a) Dominance Theorem (CERTIFIED, round 20)

**Source.** `triangle-critical-dichotomy-witness`, round 20, §B.
Independently re-derived and re-simulated from scratch by the round-20
proof-reviewer (fresh Python trial-division greedy generator, distinct from
the builder's scripts; zero violations on seeds 15, 35, 105, 187, 209, 4807
out to 500 terms each).

**Depends on (certified).** `bounded-gap-lemma.md` (`a_{n+1} ≤ a_n + a_1`);
the problem's own defining strict-monotonicity rule (`a_{n+1} > a_n`).

**Statement.** For every `n ≥ 2`, every prime `p | a_n`, with `e := v_p(a_n)
≥ 1` and `c := a_n / p^e`: `c ≤ a_{n-1}`. This holds for *every* prime
factor of `a_n` — not only outside-core primes, and not restricted to any
rogue pair or core.

**Proof.** By Bounded Gap Lemma, `a_n ≤ a_{n-1} + a_1`.
- Case `n ≥ 3`: strict monotonicity gives `a_{n-1} > a_1` (since `n-1 ≥ 2`),
  so `a_n ≤ a_{n-1}+a_1 < 2a_{n-1}`. Since `p^e ≥ 2`,
  `c = a_n/p^e ≤ a_n/2 < a_{n-1}`.
- Case `n = 2`: `a_{n-1}=a_1`, so `a_2 ≤ 2a_1 = 2a_{n-1}`, and
  `c ≤ a_2/2 ≤ a_{n-1}` (non-strict).

In both cases `c ≤ a_{n-1}`. ∎

**Tightness.** Equality is attained at `n=2`, `a_1=5` (`a_2=10`, `p=2`,
`e=1`, `c=5=a_1=a_{n-1}`).

**Consequence.** Specializing to any finite core `S_0 ⊇ Q` and any prime
`q' | a_n` with `q' ∉ S_0`: branch (a) of the certified Critical Prime
Dichotomy Lemma (`critical-prime-dichotomy.md`) *always* holds, so branch
(b) never fires — the Lemma's proof never reaches the case ("suppose (a)
fails") that produces branch (b). Any future mechanism that requires
*locating* a genuine branch-(b) "sole rescuer" instance cannot succeed —
none exist, for any `n`, prime, or core.

**Verification.** Reviewer-independent re-derivation (algebra re-checked
line by line) plus an independent Python re-simulation on 6 seeds (15, 35,
105, 187, 209, 4807), exhaustively checking every `(n, p)` pair for `n` up
to 500 in each case: zero violations, matching the builder's own
~2400-seed / thousands-of-instances sweep.

**Status.** Correct, complete, unconditional — depends only on the already-
certified Bounded Gap Lemma and the problem's own strict-monotonicity
defining rule. Reusable as a definitive negative screen: forecloses, in
general, any future FAH mechanism that requires a genuine branch-(b)
"sole rescuer via a smaller earlier term with `gcd = p'` exactly" instance.
