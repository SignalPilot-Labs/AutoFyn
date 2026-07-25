## imo-2026-06

Context read: `results/imo-2026-06/current.md`, all 5 `approaches/*.md`, all 25
`lemmas/*.md` (skimmed), and this round's three explorer reports
(`math-explorer-extremal-Q.md`, `math-explorer-alt-framing.md`,
`math-explorer-computational.md`). Round 3's Reduction Lemma (certified,
`lemmas/reduction-lemma-ss1-vs-unified-claim.md`) collapsed the whole
remaining proof to one unified target, the **Unified Central Claim**: does
there exist a finite set of primes $Q\supseteq R(a_1)$ such that every pair
of terms $a_i,a_j$ shares a prime factor in $Q$? Four mechanisms are dead
(see run_state.md Rules) and were not re-proposed.

All revisions below are **persisted directly into `approaches/*.md`** via
Edit/Write (not just described here) — verified by re-reading the diffs
after writing.

### state-compactness-pigeonhole: advance (new mechanism, §10 added)

Target: the problem's actual claim (existence of $T,L$ with $a_{n+T}=a_n+L$
for all $n\ge1$), via the Unified Central Claim.
Technique: **Hitting-Set Reformulation** — proved (new, fully rigorous,
§10.1) that "Unified Central Claim for $Q$" is *exactly equivalent* to "$Q$
is a finite hitting set for the family $\{W(i,j):=R(a_i)\cap R(a_j) :
i,j\ge1\}$ of nonempty prime sets." This converts the whole remaining gap
into a pure set-hitting problem and yields a free corollary: $Q_0=R(a_1)$
already hits every $W(1,j)$ (all pairs through index 1 are free; the
difficulty is confined to pairs $i,j\ge2$).
Skeleton: (1) Hitting-Set Lemma [proved] — (2) incremental recruitment
construction $Q^{(0)}=Q_0\subsetneq Q^{(1)}\subsetneq\cdots$, adding one
witnessing prime per unhit pair, ordered by smallest $\max(i,j)$ — (3) open
target: does this process terminate? A concrete, numerically-checkable
termination criterion is stated (recruiting pairs' indices bounded by a
function of $|Q^{(k)}|$ alone, tied to the type-stabilization index
$n_1(Q^{(k)})$).
Key lemmas: Hitting-Set Lemma (proved) — because it's a one-line unwinding
of $\mathrm{Good}_Q$'s definition via CRT-independence already in the file.
Open gaps: termination of the incremental recruitment process (the central
gap, now stated as a concrete, checkable combinatorial question).
Cases to cover: none beyond existing.
Watch out for: the recruitment order (smallest $\max(i,j)$ first) matters
for any termination argument; don't let the builder silently switch orders
mid-proof.

### jacobsthal-covering-bound: revise (new mechanism, §7 added)

Target: same (Unified Central Claim via the problem's actual claim).
Technique: **$\Lambda$-hitting-set candidate.** Reuses the already-certified
finite set $\Lambda$ (`lemmas/lambda-stabilization.md`, confined to
$\{p\le\mathrm{rad}(a_1)\}$) as a concrete, already-finite *candidate* for
$Q$, tested via the new Hitting-Set Lemma (imported from
state-compactness-pigeonhole). Free base case: $\Lambda$ already hits every
adjacent pair $W(n,n+1)$ unconditionally (immediate from the Adjacent-Link
Lemma + monotonicity of $\Lambda_n\subseteq\Lambda$). Open: does $\Lambda$
hit non-adjacent pairs $W(i,j)$, $|i-j|\ge2$?
Skeleton: (1) cheap numerical kill-check first — does $Q=\Lambda$ alone
already hit every pair for hard instances ($a_1=35,65,99$)? (2) if not, try
bounded enlargement $\Lambda^{(2)},\Lambda^{(k)}$ (gap-$k$ link primes),
checking whether these stay inside a fixed universe (unlike the crude
$a_{n+k}-a_n\le kR$ bound, which grows with $k$ and must be checked, not
assumed, against the true observed gap-$k$ gcds).
Key lemmas: reuses Adjacent-Link Lemma + $\Lambda$-stabilization (certified)
— the mechanism is genuinely new (a candidate-testing question, not a set
subtraction), explicitly distinguished in the file from the dead
$\Lambda$-split.
Open gaps: whether $\Lambda$ (or a bounded enlargement) hits every pair.
Cases to cover: the cheap numerical check must be run before any proof
attempt — flagged explicitly as step (1).
Watch out for: this could turn out false fast (explorer flagged real doubt
that $\Lambda^{(k)}$'s universe stays bounded for $k\ge2$) — if the cheap
check fails, report it honestly as a dead mechanism rather than forcing a
proof.

### active-set-stabilization: advance (new mechanism added, before "Recommended direction" section)

Target: same (Unified Central Claim via the problem's actual claim).
Technique: **Antichain (Sperner) bound on minimal types.** Combines the
already-certified Lemma M (minimal-type reduction: acceptance depends only
on $\subseteq$-minimal types) with the classical Sperner theorem (cited as
an external fact, not in `knowledge_base.md`, flagged for the builder to
either prove from scratch or cite/reproduce the standard chain-decomposition
argument): the minimal-type set $\mathcal T^\ast(Q)$ is an antichain in
$2^Q$, so $|\mathcal T^\ast(Q)|\le\binom{|Q|}{\lfloor|Q|/2\rfloor}$.
Skeleton: (1) Lemma M [certified] reduces Unified Central Claim to hitting
only the minimal types — (2) Sperner bounds the antichain's size given
$|Q|$ — (3) open target: an *exchange argument* showing each recruitment
step strictly grows the minimal-type antichain, which would let the Sperner
bound feed back into a termination bound on recruitment.
Key lemmas: Lemma M (certified) + Sperner's theorem (external, cited) —
because minimality of types is exactly an antichain condition.
Open gaps: the exchange argument (does recruitment always grow the
antichain?) is unresolved and is the crux the builder must test first,
numerically, before attempting a general proof.
Cases to cover: none beyond existing.
Watch out for: this is a genuinely different lever (combinatorial poset
size) from state-compactness's recruitment-order construction and
jacobsthal's candidate-testing — do not let it collapse into either; if the
antichain does not provably grow at every recruitment step, this mechanism
is dead and should be reported as such (not forced).

### renormalization-induction-on-seed: new approach (far framing, per dispatch)

Target: the problem's actual claim, via strong induction on $\omega(a_1)$
(number of distinct prime factors of the seed) instead of constructing a
single $Q$ for the whole sequence — a genuinely different top-level
architecture, structurally farthest from the Q/Good_Q machinery of the
other three approaches.
Technique: well-founded induction on a measure of the seed, with an
explicit smaller-instance reduction (per Pólya's "generalize/specialize"
heuristic and the crux move in `aimo-0341`, adapted from static covering
systems to a recursively-generated greedy sequence — a novel adaptation,
not a direct transplant, as no corpus problem shares this exact
greedy-selection structure).
Skeleton: (1) **base case, fully proved**: $a_1=p^k$ a prime power (in
particular every even $a_1$) $\Rightarrow T=1, L=p, a_n=a_1+(n-1)p$ — an
elementary, self-contained, free result needing no $Q$-machinery — (2)
inductive step attempted and its naive form **refuted**: locking one of
$a_1$'s own primes and renormalizing cannot, by itself, explain the general
case, since the concrete counterexample $a_1=35$ has eventual period
$L=210$ recruiting two primes ($2,3$) not dividing $a_1$ at all — (3)
sharper, still-open target stated: any working renormalization must
interleave with a recruitment-bounding argument (connecting back to, not
replacing, the Q-machinery approaches).
Key lemmas: Prime-power base case theorem — because $R(a_1)=\{p\}$ forces
every valid candidate to be a multiple of $p$, making the greedy rule
literally "next multiple of $p$" once one term is known to be a multiple of
$p$ (proved by clean induction).
Open gaps: the general inductive step; naive locking is proved insufficient.
Cases to cover: base case (prime powers) is fully settled; general case
(composite $\omega(a_1)\ge2$ seeds) remains open.
Watch out for: don't let a future round re-attempt the naive "lock the
smallest prime and induct" step — it's now a recorded, checked dead end
(concrete counterexample $a_1=35$) — any revival must explain new-prime
recruitment, not just locking.

### Deprioritized this round (not put in build set)
`bounded-link-invariant` — its central mechanism (windowed $\epsilon_n$
automaton) is proved impossible in general (round 3), and this round's
explorers did not surface a new mechanism specific to its gap/link-sequence
framing that isn't already better captured by jacobsthal's $\Lambda$-based
work above. Not marked RETHINK (per precedent, one refuted mechanism on its
first build doesn't warrant it), but no new content proposed for it this
round — leave it live in the ranker but out of this round's build
recommendation. `growth-rate-contradiction` remains dead (two independently
refuted mechanisms, unchanged).

### Field diversity check (per CLAUDE.md's anti-single-gap-trap rule)
Three of the four approaches above (state-compactness-pigeonhole,
jacobsthal-covering-bound, active-set-stabilization) still target the same
Unified Central Claim — this is intentional per the population's own memory
rule ("still put up multiple approaches attacking the shared hard lemma via
genuinely different mechanisms"), and each uses a genuinely different
combinatorial device this round (hitting-set/recruitment-order construction;
concrete already-finite $\Lambda$-candidate testing; antichain/Sperner
sizing) — not three variants of one idea. The fourth,
renormalization-induction-on-seed, is a structurally distinct top-level
architecture per the dispatch's explicit request, with its own free partial
result (the prime-power base case) independent of all $Q$-machinery.

build set: state-compactness-pigeonhole, jacobsthal-covering-bound, active-set-stabilization, renormalization-induction-on-seed
