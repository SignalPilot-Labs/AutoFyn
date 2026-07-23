# Lemma 2.3 (Σ-stabilization)

**Statement.** Under the same hypothesis as `theorem-2.2-H-hitting-
characterization.md` (`H` a finite, nonempty covering set of primes), the
sequence `(\Sigma_n)_{n\ge1}` of finite families of nonempty subsets of `H` is
non-decreasing (`\Sigma_n\subseteq\Sigma_{n+1}`), as subsets of the finite
universe `\mathcal U:=2^H\setminus\{\varnothing\}` (`|\mathcal U|=2^{|H|}-1=:M`).
Consequently there is a finite index `N_1\le M` such that
`\Sigma_n=\Sigma_{N_1}=:\Sigma_\infty` for every `n\ge N_1`.

**Proof.** `\Sigma_{n+1}=\Sigma_n\cup\{\sigma(n+1)\}\supseteq\Sigma_n` directly
from the definition, so `(\Sigma_n)` is non-decreasing; each `\Sigma_n
\subseteq\mathcal U`, a fixed finite set of size `M`. The integer sequence
`|\Sigma_n|` is non-decreasing, starts at `|\Sigma_1|=1`, and is bounded above
by `M`; such a sequence can strictly increase at most `M-1` times, so it is
constant for `n\ge N_1` for some `N_1\le M`. Since `\Sigma_n\subseteq
\Sigma_{n+1}` with equal finite cardinalities for `n\ge N_1`, equality of sets
follows (containment plus equal cardinality forces equality), giving
`\Sigma_n=\Sigma_{N_1}` for all `n\ge N_1`. `\blacksquare`

**Source.** Proved in full in `approaches/intersecting-family-covering-
construction.md` (round 2), Part 2, Step 2.3.

**Certification.** Independently re-derived; this is a standard finite
ascending-chain / pigeonhole argument (KB "Pigeonhole / extremal principle"),
correctly applied. No gaps. Certified `solved`-quality (sorry-free). Depends
only on `H` being finite (via `theorem-2.2`'s hypothesis, in the generalized
covering-set sense; no dependence on `W` itself being finite beyond that).
