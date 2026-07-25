# Approach: value-stream-double-freeze

## Status
partial

## Idea in one line
Transplant the **two-stage well-ordering** closing move of crux-corpus `aimo-0678`
(ISL 2015 N4) onto the **chosen VALUES** `a_n`: freeze a value monovariant (Stage 1,
certified Lemma B max-gap `Γ*`), then read the value stream through a finite automaton
(Stage 2) whose eventually-periodic orbit gives the gap-word `d_n=a_{n+1}−a_n` periodic
and hence `a_{n+T}=a_n+L`. This round establishes the reduction and Stage 1 rigorously,
and proves the exact **equivalence** *(Stage-2 automaton is finite-state)* ⟺ *(Π finite)*,
which pins the route's single open gap to the shared crux with an honest, concrete
obstruction (`380=2²·5·19` on `a₁=375`).

## Approaches tried
- **R3 (this round), value-stream-double-freeze:** built the skeleton into a rigorous
  partial. PROVED: (K1′) the certified endgame gives *(Π finite) ⇒ theorem for all n≥1*;
  (Stage 1) the max-gap monovariant `Γ*` freezes at a finite index (certified Lemma B);
  (K-equiv, NEW) the value-stream automaton whose orbit would yield gap-word periodicity is
  **finite-state iff Π is finite** — both directions proved — so the automaton framing does
  **not** bypass the Π-finite crux, it is logically equivalent to it. Documented the
  determinism obstruction concretely (`380` admissible only via the large prime `19` against
  the later support `{3,7,19}`), and the NEW structural observation that the certified
  A_n-obstruction family `{p*,q_k}` **violates self-blocking (E2⇒)**, hence is not a realizable
  greedy sequence, so real sequences carry the extra self-blocking constraint. OUTCOME:
  partial — the route provably reduces to **Π finite** (same wall as the field); Stage 2's
  finiteness/determinism is that crux, left as an explicit GAP with its exact equivalent form.
  (Keep prior R3-skeleton entry below.)
- **R3 skeleton (registered):** transplanted aimo-0678 shape; flagged K3 (bounded active
  supports per window) and the determinism secondary gap. Superseded by the build above.

## Current best

Throughout, the certified infrastructure is used verbatim:
`M=rad(a₁)`; `L1` (Anchor: every term has a prime in `P=primes(a₁)`); `L2`
(gap `d_n=a_{n+1}−a_n∈{1,…,M}`, `a_n=Θ(n)`); `L3` (Distance–prime: `q|a_i, q|a_j ⇒ q≤|a_i−a_j|`);
`L4` (pairwise-intersecting); the no-transient identity `a_{n+1}=s(a_n)` for **all** `n≥1`
with `A={c:c meets every G∈𝓐_∞}`, `s(x)=min{c∈A:c>x}`; `E1` (`{a_n}=A∩[a₁,∞)`); `E2`,
`E2(⇒)` (every minimal support is a minimal transversal of `𝓐_∞`); `E3` (private witness);
and Lemma B (max-gap `γ_n∈{1,…,M}` non-decreasing, hence frozen at `Γ*` from some `N₀`).
`Π:=⋃_{G∈𝓐_∞}G`.

### 1. Reduction of the theorem to Π finite (PROVED — K1′)

**Claim.** If `Π` is finite, then `∃ T,L` with `a_{n+T}=a_n+L` for **all** `n≥1`.

*Proof.* This is the certified endgame (`no-transient-fixed-successor.md`), restated for
completeness. Put `L₀=∏_{p∈Π}p`. Membership `c∈A` is the condition "`c` meets every
`G∈𝓐_∞`", i.e. "for every `G∈𝓐_∞` some `p∈G` divides `c`". Each such `p∈Π`, so the truth
value of `c∈A` depends only on the residue class of `c` modulo `L₀` (which `p∈Π` divide `c`).
Hence `A` is an **exact** union of residue classes mod `L₀`: `c∈A ⟺ c+L₀∈A`, with no
transient. By `E1`, `{a_n}=A∩[a₁,∞)`, and the sequence enumerates this set in increasing
order. Let `ρ(A)` be the set of residues `r mod L₀` with `r∈A` and `T:=|ρ(A)|`; since `A` is
`L₀`-periodic, each period `[x,x+L₀)` (for `x≥a₁`) contains exactly `T` elements of `A`.
Therefore the `(n+T)`-th element of `A∩[a₁,∞)` equals the `n`-th plus `L₀`:
`a_{n+T}=a_n+L₀` for all `n≥1`. Take `L=L₀`. ∎

So the entire theorem follows once `Π` is finite. The gap-word statement is the same fact:
`a_{n+T}=a_n+L ∀n ⟺ d_{n+T}=d_n ∀n` (telescoping `d_n=a_{n+1}−a_n`, since
`a_{n+T}−a_n=∑_{i=0}^{T-1}d_{n+i}` and `a_{(n+1)+T}−a_{n+1}=a_{n+T}−a_n ⟺ d_{n+T}=d_n`).
This is the sense in which the route "targets the gap-word directly": producing a genuine
period `(T,L)` valid from `n=1` is exactly producing the periodic gap-word, and by the above
both are delivered by (and only by) `Π` finite.

### 2. Stage 1 — the value monovariant freezes (PROVED)

The Stage-1 freeze is certified **Lemma B**: the largest gap `γ_n` between consecutive
elements of the periodic admissible set `A_n=\{c:gcd(c,a_i)>1 ∀ i≤n\}` satisfies
`γ_n∈\{1,…,M\}`, is non-decreasing (deleting points only enlarges gaps) and bounded above by
`M` (multiples of `M` are always admissible). By well-ordering of a bounded non-decreasing
integer sequence, `γ_n` is eventually constant: there is a finite index `N₀` and a value
`Γ*≤M` with `γ_n=Γ*` for all `n≥N₀`. This is the Stage-1 well-ordering freeze on data read
from the actual sequence (`a_1,…,a_n` determine `A_n`), completed. It is a genuine
finite-time freeze (unlike the density monovariant, which only converges — see the
Obstruction lemma).

*Numerical anchor (a₁=375):* `M=15`, `γ_n:3→3→6→6→…` freezes at `Γ*=6` (certified sim).

### 3. Stage 2 — the value-stream automaton, and the exact obstruction (K-equiv, PROVED equivalence; Π-finite left as GAP)

Stage 2 wants a **finite** state `W_n` read from a bounded window of the value stream such
that `n↦W_n` is the orbit of a deterministic finite-state map, whence (pigeonhole on a finite
state set) the orbit is eventually periodic and `d_n` eventually periodic. The honest content
of this round is to determine **exactly** when such a finite automaton exists.

**Lemma (K-equiv). The Stage-2 value-stream automaton is finite-state and deterministic
if and only if `Π` is finite.**

*Proof.* We make "the automaton" precise as: a state `W_n` together with a transition
`W_n↦W_{n+1}` and an output `W_n↦d_n=a_{n+1}−a_n=s(a_n)−a_n`, such that (i) `W_n` ranges over
a finite set and (ii) `W_{n+1}` and `d_n` are functions of `W_n` alone. We show any such data
exists ⟺ `Π` finite.

(⇐) If `Π` is finite, take `W_n:=(a_n \bmod L₀)` with `L₀=∏_{p∈Π}p` (a finite set of size
`≤L₀`). By §1, `A` is exactly `L₀`-periodic, so `s(a_n)−a_n` depends only on `a_n\bmod L₀`
(the position of the next admissible residue after `a_n\bmod L₀` is a function of the residue),
i.e. `d_n` and `a_{n+1}\bmod L₀=W_{n+1}` are functions of `W_n`. Finite, deterministic. Done.

(⇒) Suppose a finite-state deterministic automaton exists. The output `d_n=s(a_n)−a_n` must be
determined by `W_n`. But `s(a_n)−a_n` is determined by **which admissible integers lie just
above `a_n`**, i.e. by the admissibility of the integers `a_n+1,a_n+2,…` up to the next
`A`-element; and `c∈A` is decided by *which primes of each `G∈𝓐_∞` divide `c`*. Concretely,
whether `c` is admissible can require knowing `v_q(c)` for a prime `q∈Π` that is
**load-bearing** for `c` — the unique prime of some `G∈𝓐_∞` that `c` meets `G` through.
Suppose `Π` were infinite. By `E3`, for every `q∈Π` there are minimal supports `G,G_q∈𝓐_∞`
with `G∩G_q=\{q\}`, realized (E1) by terms `t,t'` with `gcd(t,t')=q^{≥1}`; thus for the term
`t` the prime `q` is load-bearing for meeting `G_q` (removing `q` from `F(t)=G` leaves a set
disjoint from `G_q`, by minimality/E2⇒). Hence for each of the infinitely many `q∈Π` there is
a value at which the choice `s(·)` depends on divisibility by `q`. A state that determines the
output for all these choices must distinguish residues modulo infinitely many distinct primes
`q∈Π`, so it must take infinitely many values — contradicting finiteness (i). Therefore `Π` is
finite. ∎

**Consequence.** The Stage-2 automaton exists ⟺ `Π` finite. Combined with §1, the double-freeze
route is **logically equivalent to proving `Π` finite** — it does not, and provably cannot,
bypass that crux. This is the honest resolution of the reviewer's flag: the automaton cannot be
made finite-state on a *bounded window* of the value stream alone, because load-bearing large
primes outside the window (the reviewer's `380=2²·5·19` on `a₁=375`) genuinely decide choices.

**Concrete determinism obstruction (verified).** For `a₁=375` (`M=15`, `P={3,5}`) the limiting
minimal supports are `𝓐_∞={\{2,3\},\{3,5\},\{2,5,7\},\{2,5,19\},\{3,7,19\}}`, so `Π={2,3,5,7,19}`
(finite here, but `19>M=15`). The term `a_3=380=2²·5·19` is the first term divisible by `19`; it
meets the later support `\{3,7,19\}` **only through `19`** (`{2,5,19}∩{3,7,19}={19}`), and
`{2,5}` (i.e. `F(380)∖{19}`) fails to meet `{3,7,19}`, so `19` is load-bearing in the minimal
support `\{2,5,19\}`. A bounded window state that omits `v_{19}(·)` therefore cannot decide the
admissibility of numbers coprime to `{3,7}` that need `19`. This is why the state must, in the end,
track exactly the residues mod `∏Π` — finite iff `Π` finite. (All facts here are from the R3
simulation, `N=200`.)

### 4. The single remaining gap (Π finite) and how this route sharpens it

**GAP (the crux, shared with the field).** `Π=⋃_{G∈𝓐_∞}G` is finite. Equivalently (`E2`/`E3`
reduction, certified): the primes occurring in ⊆-minimal supports are bounded; the sharp
numerically-tested target is `q≤a₁`, or (antichain ERW) every `q∈Π` divides a term
`≤a₁+K·M` with `K` an `a₁`-computable constant (numerically `K≤0.33`, e.g. `19|380=a₁+5`,
`K=5/15=1/3`). By §3 (K-equiv) this is **exactly** the finiteness of the Stage-2 automaton, so
proving `Π` finite closes the whole route via §1.

**Two rigorous NEW clarifications this round (partial forward progress on the gap):**

(a) **Self-blocking rules out the naive obstruction as a real sequence.** The certified
A_n-Obstruction family `G_k=\{p*,q_k\}` (which freezes/converges all `A_n`-statistics while
having infinite `Π`) is **not realizable** as a greedy sequence: it violates `E2(⇒)`. Indeed
`{p*}` alone meets every `G_k` (all contain `p*`), so `{p*}` is a transversal of the family,
hence `\{p*,q_1\}` is **not** a *minimal* transversal — contradicting `E2(⇒)`, which every real
sequence satisfies. So a real sequence's `𝓐_∞` has the strictly stronger property that *every*
minimal support is a *minimal* transversal (self-blocking / identically self-dual clutter).
This says the crux is not obstructed by the known counterexample family, and any proof of `Π`
finite may **use** self-blocking freely.

(b) **Self-blocking + intersecting alone is not sufficient — arithmetic (L3) is essential.**
Self-blocking pairwise-intersecting antichains of finite sets need not obviously be finite in a
purely set-theoretic sense (e.g. incidence-geometry constructions); the distinguishing
constraint here is the arithmetic `L3` (two terms sharing only `q` are `≥q` apart) together
with the value geometry `a_n=Θ(n)`, gap `≤M`, and `E1`. So a correct proof of `Π` finite must
combine self-blocking (a) with `L3`/value geometry — precisely the ERW formation-window
statement the leader (`redundant-constraint-antichain`) attacks. This route contributes the
**equivalence** (§3) that turns "gap-word periodicity" and "finite automaton" into the *same*
statement as `Π` finite, so no separate finite-alphabet step is created — as designed — but
also no bypass of it is possible.

### Case coverage

- **`|P|=1` (`a₁=p^k`, prime power).** Then `P={p}`, `M=p`; every term is a multiple of `p`
  (L1), and every multiple of `p≥a₁` is admissible (meets every support, each of which
  contains `p` — the only available small prime — so `𝓐_∞=\{\{p\}\}`, `Π=\{p\}`). Hence
  `a_n=a₁+(n-1)p`, `d_n≡p`, `T=1`, `L=p`. The machinery of §1 gives `L₀=p`, `ρ(A)`=one class,
  `T=1`. Verified: `a₁=8→` gaps all `2`; `a₁=9→` gaps all `3`. This case is fully closed.
- **`|P|≥2` (general).** The real case; §1–§3 apply verbatim and reduce it to the single GAP
  (`Π` finite). Not closed.
- **By-product check.** Under `Π` finite, `L=L₀=∏Π`, matching the certified `a₁=105→T=58,
  L=210=2·3·5·7` and `a₁=375→Π=\{2,3,5,7,19\}`, `L₀=3990=2·3·5·7·19` (consistent with the
  recorded `(T,L)=(852,3990)` refuting the false `p|L⇒p≤M` confinement).

## Spec concerns
None for the framing. The route is sound but, as proved in §3 (K-equiv), it is *logically
equivalent* to "Π finite," not a bypass of it. If the orchestrator wants a genuinely
Π-finite-avoiding pole, this equivalence shows the dynamical-automaton framing cannot supply
one; the live leverage is the arithmetic ERW window (leader) fused with self-blocking (§4a).

## Full proof
Not present — Status partial. Remaining gap: **Π finite** (equivalently, by §3, the Stage-2
value-stream automaton is finite-state; equivalently the primes in ⊆-minimal supports are
bounded / the ERW formation window `q|` a term `≤a₁+K·M`). Given that gap, §1 delivers
`a_{n+T}=a_n+L` for all `n≥1` with `T=|ρ(A)|`, `L=∏Π`.

## Promotable lemmas

- **K1′ (Π-finite ⇒ theorem, all n).** If `Π` is finite then `A` is exactly `∏Π`-periodic and
  `a_{n+T}=a_n+L` for all `n≥1`, `T=|ρ(A)|`, `L=∏Π`. *(Proved in §1; this is the certified
  endgame re-derived cleanly with the residue-count `T=|ρ(A)|`. Already essentially certified in
  `no-transient-fixed-successor.md`; listed for cross-reference.)*
- **K-equiv (automaton ⟺ Π finite).** A finite-state deterministic value-stream automaton
  whose orbit outputs `d_n=s(a_n)−a_n` exists **iff** `Π` is finite. *(Proved in §3, both
  directions; new. Certifies that the dynamical/automaton framing is logically equivalent to
  the Finite-Alphabet crux — useful to prevent future "automaton bypass" false starts.)*
- **Self-blocking excludes the A_n-obstruction family (§4a).** The A_n-Obstruction family
  `\{p*,q_k\}` violates `E2(⇒)` (`{p*}` is already a transversal), so it is not realizable as a
  greedy sequence; every real sequence's `𝓐_∞` is self-blocking (each minimal support is a
  *minimal* transversal). *(Proved in §4a; new, small but reusable — any Π-finite proof may
  assume self-blocking and need not fear this counterexample.)*
