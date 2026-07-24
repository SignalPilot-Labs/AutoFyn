## Lemma: EEA ⟹ Periodicity (Theorem C, certified with a wording correction)

**Source.** `subword-complexity-periodicity`, round 12, §4. Certified by the
proof-reviewer (round 12) with a corrected definition of "safe residue" — see
**Reviewer correction** below; the mathematical content used elsewhere is
unaffected.

**Depends on (certified).** `bounded-gap-lemma.md`, `finite-core-theorem.md`,
`gap-periodicity-equivalence.md` (Lemma A), `red-k-periodicity-lemma.md` (Lemma B,
used only for the underlying mechanism, not invoked directly).

**Setup.** Fix a finite `S₀ ⊇ Q`, `L₀ := ∏_{p∈S₀} p`, `r_n := a_n mod L₀`. Since
`S₀`-primes divide `a_n` according to `r_n` alone, the extended type
`ρ(n) = P(a_n)∩S₀` is a function of `r_n` only. Call a reachable residue `r` (one
occurring as `r_n` for infinitely many `n`) **safe** if there is a value `f(r)` such
that `g_n = f(r)` for **every** `n` with `r_n = r` (zero exceptions — see Reviewer
correction), and **ambiguous** otherwise (some two visits `n, n'` with `r_n = r_{n'}
= r` but `g_n ≠ g_{n'}`).

**Reviewer correction (to the source file).** The source's prose defined "safe" as
"all its infinitely many visits `n` *eventually* agree on `g_n`," suggesting
finitely many early exceptions are tolerated, while its crisp negation ("ambiguous
= some two visits differ") is the strictly stronger zero-tolerance reading (any one
differing pair already makes `r` ambiguous). These are inconsistent; the source
proof contains a self-flagged digression ("wait, we must double check…") trying to
reconcile them. **This certified version adopts the zero-tolerance reading**
(forced by the stated negation): `r` safe means `g_n = f(r)` for literally every
visit. Under this reading the digression is unnecessary — the proof below omits it.

**EEA (Eventual Escape from Ambiguity) at level `S₀`.** There exists `N` such that
`r_n` is a safe residue for every `n ≥ N`.

**Theorem C.** If EEA holds at some finite `S₀ ⊇ Q`, the problem's primary target
(`∃T,L` with `a_{n+T}=a_n+L` for all sufficiently large `n`) holds, with an
explicit `T ≤ L₀`.

**Proof.** By EEA, fix `N` with `r_n` safe for all `n ≥ N`; by the (zero-tolerance)
definition of safe, `g_n = f(r_n)` for every such `n`. Define
`h : (safe residues) → ℤ/L₀ℤ` by `h(r) := (r + f(r)) mod L₀`. For `n ≥ N`:
`r_{n+1} ≡ a_{n+1} ≡ a_n + g_n ≡ r_n + f(r_n) ≡ h(r_n) (mod L₀)`,
and `r_{n+1}` is itself safe (`n+1 ≥ N`), so `h` maps safe residues to safe
residues, and `(r_n)_{n≥N}` is exactly the orbit of `r_N` under iterating `h` on
the finite set of safe residues (size `≤ L₀`). By pigeonhole applied to the
`L₀+1` values `r_N, r_{N+1}, …, r_{N+L₀}` drawn from a set of size `≤ L₀`, two
coincide: `r_{N+s} = r_{N+t}` for some `0 ≤ s < t ≤ L₀`. Since `h` is a fixed
deterministic function, `r_{N+s+m} = r_{N+t+m}` for all `m ≥ 0` by induction (each
equals `h` applied `m` times to the same starting value). With `T := t-s ≤ L₀`,
`r_{n+T} = r_n` for all `n ≥ N+s`, and `g_{n+T} = f(r_{n+T}) = f(r_n) = g_n` for the
same range (both `r_n, r_{n+T}` safe, both computed via `f`). By Lemma A
(Gap–Periodicity Equivalence), the problem's primary target holds with this `T`
(`≤ L₀`) and the corresponding `L`. ∎

**Status.** Correct, complete, no gaps under the corrected "safe" definition;
independently re-derived by the reviewer. **Conditional on EEA** (EEA itself is
NOT proved — see `subword-complexity-periodicity` §5 / `current.md` round-12
section for the argument that EEA, once unpacked, requires the same content as the
standing FAH/Cofinite-FAH crux). The implication "EEA ⟹ periodicity" itself is
unconditional and reusable — an explicit, self-contained alternative presentation
of the certified CRT/cyclic-pigeonhole finish's true underlying sufficient
hypothesis. Certified alongside (not in place of) the existing finish.
