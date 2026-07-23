## imo-2026-06

### Headline finding (important correction to the assigned hypothesis)
The literal claim **"only finitely many distinct primes ever divide any term of the
sequence"** is numerically FALSE for composite (multi-prime) starting values. I
generated the greedy sequence (math.gcd-based simulation, a_1 in {6,15,35,105,231,
1155}, 600-800 terms) and factored every term: the *set of primes appearing
somewhere in some a_n's factorization* keeps growing without bound — by term 600 it
already includes essentially every prime up to ~600-670 (e.g. for a_1=6: 110 distinct
primes among the first 600 terms, growing roughly like π(a_600)). So a naive
"finite prime support" claim is refuted by direct computation; the outliner must
not build the proof on that literal statement.

### The correct (weaker, still very useful) claim, verified computationally
What *is* true, and is the real content behind the "finite primes" intuition: there
is a small **finite "backbone" set of primes P\*** (the *load-bearing* primes) such
that restricting every term's factorization to P\* still suffices to satisfy
**every** pairwise constraint gcd(a_i,a_j)>1 for i<j, for the *entire* sequence
(not just an initial segment) — i.e. P\* is a genuine, permanent "covering system."
Any *other* prime dividing a specific a_n is incidental/non-load-bearing: it never
needs to be shared with anything, it's just extra multiplicity that happens to make
that particular integer the smallest one satisfying the P\*-based covering.

Verified examples (`explore5.py`/`explore7.py`/`explore9.py` in this session):
- a_1=15=3·5: P\*={2,3,5} suffices for 1000 terms (P\*={3,5} alone fails at n=3).
  Gaps are **purely periodic from the start**: period T=8, L=30, block
  `[3,2,4,6,6,4,2,3]`. Residues (mod2,mod3,mod5) repeat exactly with period 8 —
  literally a covering system mod 30 using primes {2,3,5} (verified: a_n mod 30
  cycles through exactly 8 of the 30 residues, each hit by 2, 3, or 5).
- a_1=35=5·7: P\*={2,5,7} FAILS (fails at n=4 vs n=3); P\*={2,3,5,7} succeeds for
  1000 terms.
- a_1=105=3·5·7: P\*={3,5,7} (primes(a1) alone) FAILS at n=3; P\*={2,3,5,7} succeeds.
- a_1=1001=7·11·13: primes(a1) alone fails; adding just {2} succeeds.
- a_1=231=3·7·11: P\*={2,3,7,11} succeeds; in fact this case is trivial — gap is
  constantly 3 forever (T=1, L=3): once 3 (which divides a_1) also ends up dividing
  *every* subsequent term, the recursion collapses to "smallest multiple of 3
  greater than a_n," giving immediate arithmetic-progression behavior (the "one
  prime handles everything" degenerate case, same as any prime-power start).
- a_1=247=13·19 (two large odd primes, no small ones): here primes(a1)∪{2,3} is
  NOT enough — a genuine extra prime 7 is load-bearing at an early pair
  (gcd(273,266)=7, i.e. 273=3·7·13 and 266=2·7·19 share only 7). Backbone
  P\*={2,3,5,7,13,19} (6 primes) DOES work for 2000+ terms with zero failures.
  No single prime among {2,3,5,7,13,19} has density →1 in the first 3000 terms
  (13 hits 65%, 2 hits 85%, 7 only 24%) — so this is genuinely a multi-prime
  covering pattern, not a collapse to one dominant prime. Periodicity of the gap
  sequence was NOT detected by direct search up to period 999 within the first
  15000 terms (last term ≈431015) — either the eventual period/transient is much
  longer here, or my search window was still inside the transient. This is the
  hardest test case found and worth flagging to the outliner as a stress test for
  any proposed bound on T, L.
- Prime-power starts (a_1 ∈ {3,5,7,9,11,13,25,33,49,...}): P\*={p} (the single
  prime), and the sequence is *exactly* the arithmetic progression p, 2p, 3p, ...
  (T=1, L=p) from the very first step. This is the trivial base case.
- a_1=2 or any even a_1: 2 always works as sole backbone prime — sequence is
  exactly the even numbers ≥ a_1 (T=1, L=2), trivial.

### The key subtlety flagged by the dispatch: different primes witness different pairs
Confirmed directly: for a_1=15, gcd(a_1,a_2)=gcd(15,18)=3 but gcd(a_1,a_3)=
gcd(15,20)=5 — *different* primes witness the constraint against a_1 at different
later steps, and neither of those primes need witness the OTHER pairs (e.g.
gcd(a_2,a_3)=gcd(18,20)=2, a third prime). So the structure is genuinely a
**covering-system / hypergraph-covering** problem: a_{n+1} must, for each i≤n, be
hit by *some* prime from a possibly-varying finite palette, not by one universal
common prime. This is exactly the technique used in crux `aimo-0447`
("Encode a 'gcd>1 for every pair of shifts' hypothesis by placing in cell (i,j) a
prime dividing the gcd, turning the condition into a complete prime-covering of a
grid") — a strong structural analogy (see below), even though that problem's
2-D grid geometry differs from our 1-D increasing-sequence geometry.

### Mechanism sketch for periodicity, GIVEN a finite backbone P* (not fully proven — this is what the outliner needs to close)
If a finite P\* can be shown to exist (permanently sufficient to cover all pairwise
constraints), then: the "state" relevant to picking a_{n+1} is only the vector of
residues of the last several terms modulo the primes of P\* (or more precisely,
which primes of P\* divide which of the (finitely many, since P\* is finite)
*recent* terms whose constraint isn't yet "automatically" satisfied by density).
Since there are only finitely many possible residue-state combinations mod
L=lcm(P\*), a greedy deterministic process operating on a bounded-memory state must
revisit a state (pigeonhole), forcing the *rule* that produces a_{n+1} from a_n to
repeat — giving eventual periodicity of the gap sequence with T = (state-space
size) and L = (sum of one full period of gaps, itself a multiple structure tied to
lcm(P\*)). This is the "mechanism" the outliner should target, but note the HARD
gap is proving (a) P\* is finite and permanent (not just "so far, up to N=15000, no
new backbone prime was needed" — that is only numerical evidence) and (b) that the
relevant state truly has bounded memory (i.e., satisfying old constraints against
a_i for i≪n eventually becomes "free"/automatic once i falls out of a bounded
window, rather than requiring bespoke primes forever).

### Cheap-kill / structural observations worth using
- gcd(a_n, a_1) | a_1 always (a_1 fixed), so gcd(a_n,a_1) takes only finitely many
  values (divisors of a_1) as n→∞: this is a free, rigorous pigeonhole fact (matches
  crux `aimo-0421`'s move) — infinitely many n share the same value g=gcd(a_n,a_1).
  This alone does NOT give the full backbone (constraints against a_2,...,a_{n-1}
  remain), but it's a clean, provable finiteness fact to build on.
- gcd(a_i,a_{i+1}) | (a_{i+1}-a_i) = gap, so any prime witnessing consecutive terms
  divides the gap itself — ties prime structure directly to the gap sequence
  (matches crux `aimo-0503`'s "gcd divides difference" move).
- Every a_n (n≥2) must be divisible by *some* prime of a_1 for the i=1 constraint
  alone (since the only primes that can divide gcd(a_n,a_1) are divisors of a_1,
  a_1's factor set is fixed and finite). This is the ONE guaranteed piece of the
  backbone that is trivially proven; the rest of P\* (extra primes like 2,3,5,7,
  or 7 in the a_1=247 case) is the hard, empirically-observed-but-unproven part.
- All the computed examples have max gap between consecutive terms staying quite
  small relative to a_n itself EXCEPT the "two big odd primes, no small common
  structure" case (a_1=247), where gaps ranged up to 78 within 800 terms — this is
  a sign the transient before backbone-lock is longer/more delicate when a_1 has
  no small prime factors at all.

### Candidate technique(s)
- Pigeonhole on gcd(a_n,a_1) | a_1 (finite divisor set) — crux `aimo-0421` style.
- "gcd | difference" to link witnessing primes to gaps — crux `aimo-0503` style.
- Grid/interval prime-covering counting (bound how many distinct primes can be
  "load-bearing" across a window of size n, via Σ 1/p type counting) — crux
  `aimo-0447` style; would need adaptation from the 2-D grid to the 1-D
  increasing-sequence covering-system setting.
- CRT / covering-system periodicity once backbone finiteness is established
  (knowledge_base.md "Modular arithmetic, CRT" and "Order of an
  element... eventual periodicity of products of a sequence mod m" entries).

### Cheap-kill candidates
None found that immediately dispatch the whole problem — this is a genuine hard
covering-system/pigeonhole argument, not a size/parity trick. The one clean,
free structural fact (gcd(a_n,a_1) | a_1 ⇒ finitely many values) is a legitimate
first lemma to bank, but by itself doesn't finish anything.

### Knowledge-base entries to use
- "Modular arithmetic, CRT" (knowledge_base.md line ~59-60): combine residues mod
  primes of the backbone via CRT once finiteness is secured.
- "Order of an element, Fermat/Euler... eventual periodicity of products of a
  sequence mod m" (line ~65-66) and "Linear recurrences... sequences are
  eventually periodic mod m" (line ~79-80): the generic template for turning
  bounded-state pigeonhole into eventual periodicity — needs adaptation since our
  recursion isn't linear, it's a greedy min-search, but the "bounded state ⇒
  eventual periodicity" logic is the same shape.
- "Pigeonhole / extremal principle" (line ~108, ~188): generic pigeonhole template
  for the state-repeats argument.
- "Divisor analysis" (line ~86-87): gcd structure / divisor-count bounding, useful
  for bounding backbone size via divisors of a_1.

### Analogous past problems (cruxes)
- `aimo-0447` (number_theory, divisibility-and-gcd / size-bounding-and-descent):
  "Prove ∃c>0 s.t. gcd(a+i,b+j)>1 for all i,j∈{0,...,n} ⇒ min{a,b}>(cn)^{n/2}."
  **Best structural analog found.** The crux move — encode the "gcd>1 for every
  pair" hypothesis as a grid where cell (i,j) is filled by a witnessing prime, then
  bound via Σ 1/p (interval-length) how many cells small primes can cover, forcing
  large/many-distinct primes elsewhere — is the exact flavor of counting argument
  our problem needs to bound how many *distinct* primes can be simultaneously
  load-bearing across a window of the sequence. Geometry differs (2-D grid of two
  independent APs vs. our 1-D self-referential increasing sequence with a *growing*
  covering requirement against ALL past terms), so this is a hint to adapt, not
  reuse directly.
- `aimo-0421` (number_theory, divisibility-and-gcd): "S infinite, some
  gcd(v,w)≠gcd(x,y) ⇒ ∃ a,b,c∈S distinct with gcd(a,b)=gcd(a,c)≠gcd(b,c)." Crux
  move: gcd(a, ·) with a fixed only takes finitely many values (divisors of a) ⇒
  pigeonhole over an infinite index set. Directly reusable as the free lemma
  "gcd(a_n,a_1) takes finitely many values" noted above.
- `aimo-0503` (number_theory, divisibility-and-gcd/size-bounding-and-descent):
  "gcd(a_i,a_{i+1})>a_{i-1} for a strictly increasing sequence ⇒ a_n≥2^n." Less
  directly analogous (that problem is a growth-rate lower bound via gcd|difference,
  ours is an eventual-periodicity claim), but the gcd|difference move is reusable
  local machinery.
- Not a match, but noted: `aimo-0224` (encode coprimality patterns by assigning
  distinct primes to elements of a ground set) — this is the *opposite* direction
  (constructing a sequence with a prescribed gcd pattern) and not applicable since
  our sequence is uniquely determined by the greedy rule, not free to construct.

### Prior progress
None — this is round 1, results/imo-2026-06/ has no approaches yet.

### Dead ends (do not retry)
- **Do not assume/assert "only finitely many primes ever divide any a_n"** as a
  literal global claim — refuted computationally (see headline finding). Any
  approach built on that exact statement will fail to match the data and should be
  abandoned immediately if proposed. The correct, weaker, and still apparently true
  claim is the "finite covering backbone P\*" version above — the outliner should
  build around THAT, and flag explicitly that establishing P\*'s existence/finiteness
  rigorously (not just up to N=15000 numerically) is the central remaining gap.
- Attempting to fix backbone size a priori as `primes(a_1) ∪ {2,3}` (small,
  universal) does NOT work in general — refuted by a_1=247, which needs an extra
  prime (7) not predictable purely from a_1 and the two smallest primes. Any
  approach claiming a fixed formula like "backbone = primes(a_1) ∪ {2,3,5,7}"
  should be treated as unproven conjecture at best, and the outliner should not
  present a specific small backbone as definitely sufficient without proof — the
  a_1=247 case may plausibly need even more or different primes at higher n (I did
  not find a period within 15000 terms for that case, so its long-run backbone is
  still unconfirmed even numerically).

### Small-case / intuition notes (all conjectural, verified only up to a few thousand terms per example)
- Prime-power / single-small-common-prime starts are always eventually (indeed
  immediately) T=1 arithmetic progressions — the "trivial" regime.
- Multi-prime starts with at least one small prime factor (2,3,5) settle into
  short-period (T≤~10), small-L purely-periodic-from-the-start gap patterns very
  quickly (a_1=15, 35, 105, 1155 all settled essentially immediately).
- Multi-prime starts with ONLY large prime factors (a_1=247=13·19, no factor
  ≤11) show a much longer, more erratic transient (gaps up to 78 within 800 terms,
  no detected periodicity within 15000 terms / period search to 999) — the true T,L
  for this case are plausibly much larger, consistent with the problem only
  promising existence of T,L (no bound on their size), but this is the case most
  likely to break a naive/small proposed backbone and is a good stress test for
  whatever mechanism the outliner proposes.
- Conjecture (unproven): for every valid a_1, a finite covering backbone P\*
  exists and is reached after a transient of length polynomial (or at least finite
  and effectively bounded) in a_1; L is then some structured combination
  (not simply lcm(P\*), since not every residue class mod lcm(P\*) is used — only a
  covering subset of them, as seen concretely for a_1=15: only 8 of the 30 residues
  mod 30 are used per period).
