## imo-2026-06

### Scope of this report
Pure crux-corpus mining for the "existential -> cofinite/eventual" promotion pattern that
is the sole remaining gap (FAH / Symmetric FAH / Cofinite FAH — see
`results/imo-2026-06/lemmas/cofinite-sufficiency-lemma.md`,
`confined-gcd-lemma.md`, `successor-transport-reduction-lemma.md`). No proof attempted.

### The exact shape of the open gap, restated precisely (for calibration)
Fixed rogue pair (A',B'), witnesses n_A<n_B, prime q*. Let n_1<n_2<... enumerate the
A'-occurrences past n_B. By the Confined-GCD Lemma, g_j := gcd(a_{n_j}, a_{n_B}) lives in
a FIXED FINITE alphabet Div(b) (b = the F''-part of the fixed integer a_{n_B}), and
q*|a_{n_j} iff q*|g_j. Infinite pigeonhole (already used) gives SOME fixed value d in
Div(b) with g_j=d infinitely often; the open step is upgrading this to "the divisor-class
q*|d occurs for ALL but finitely many j" (Cofinite FAH), equivalently the Successor Claim
"eventually g_j divisible by q* implies g_{j+1} divisible by q*" (Successor-Transport
Reduction Lemma). Nine mechanisms have died trying to supply this upgrade from the
currently-certified toolkit (Free Facts / Generalized Bounded Witness / gcd-magnitude /
Critical Prime Dichotomy) — Lemma I's diagnosis (not itself certified, but independently
re-verified each round) is that none of these four tools contains an "identity-forcing"
step, i.e. nothing in the certified stack links g_j to g_{j+1} across different j.

### Distinct openings mined from the corpus (each a genuinely different device for the
same promotion problem — assess plausibility of each honestly)

**1. aimo-0477 (IMO 2018-ish, Mongolia; subtopic divisibility-and-gcd /
p-adic-valuation) — CLOSEST target-shape match, but a load-bearing disanalogy.**
Problem: sum a_1/a_2+...+a_{n-1}/a_n+a_n/a_1 is an integer for all n>=k; prove a_n is
eventually constant. Crux moves: (i) d_n := gcd(a_1,a_n) is proved NONDECREASING as a
divisor of a_1 (v_p(d_n)=min(v_p(a_1),v_p(a_n)) nondecreasing for every p), giving an
ASCENDING divisor chain bounded above by the fixed a_1 — must stabilize; (ii) a genuinely
separate, sharper move: for EACH prime p, the valuation sequence v_p(a_n) is shown
EVENTUALLY MONOTONE (not just "in a finite set") by directly analyzing the two summands
of the integrality identity t_n = a_n/a_{n+1} + (a_{n+1}-a_n)/a_1 at each prime — if the
two summands' valuations differ, integrality forbids the minimum being negative, forcing
a one-directional inequality on v_p(a_n) vs v_p(a_{n+1}) depending on whether v_p(a_n) is
above or below v_p(a_1). This is EXACTLY the "descent/monotonicity refinement beyond
pigeonhole" the dispatch asked me to look for (an actual algebraic identity forces the
valuation to move in a fixed direction, not just to lie in a fixed set).
- Structural match to our problem: our g_j is confined to a fixed divisor alphabet
  Div(b) — same shape as aimo-0477's d_n confined to Div(a_1). Their extra step beyond
  "finite alphabet + pigeonhole" is precisely what our crux lacks.
- **Why it likely does NOT transplant directly, and this must be checked honestly, not
  assumed:** aimo-0477's monotonicity comes from an EXPLICIT ALGEBRAIC IDENTITY relating
  consecutive terms a_n, a_{n+1}, a_1 (the integrality of a specific rational
  expression). Our sequence a_n has NO algebraic recurrence at all — a_{n+1} is defined
  by a minimality/existential search over gcd conditions with all PRIOR terms, not a
  formula in a_n. There is no known identity linking g_j to g_{j+1} the way aimo-0477's
  t_n links v_p(a_n) to v_p(a_{n+1}). Importing the "monovariant per divisor-class" idea
  would require FIRST discovering an analogous identity/inequality tying consecutive
  A'-occurrences of our sequence together — which is exactly the Successor Claim already
  isolated and already stalled. So this crux does not hand over a new tool; it clarifies
  precisely WHAT KIND of missing fact would close the gap (an identity or forced
  inequality linking g_j, g_{j+1}, not merely a finite-alphabet membership fact) — useful
  as a target-shape template, not as a technique to apply as-is. Flag: attempting this
  without first finding a genuine consecutive-term identity would just re-derive one of
  the 9 dead pigeonhole mechanisms.

**2. aimo-0680 (ISL/IMO-style functional-iteration periodicity, Singapore; subtopic
divisibility-and-gcd) — a genuinely different device: "infinite-subset relation forces
all-index relation via a divisibility-vs-bounded-difference squeeze."**
Crux move: to upgrade "f^j(a_x) = a_x + j*T_x" from holding on an infinite index subset Y
to holding for ALL j, they pick y in Y with y-j LARGER than the (a priori bounded)
difference |f^j(a_x) - (a_x+jT_x)|; both f^y(a_x)-f^j(a_x) and f^y(a_x)-(a_x+jT_x) are
shown divisible by y-j; a divisor exceeding a bounded quantity forces that quantity to be
0.
- **Plausibility for our problem: LOW as stated, but worth a careful check.** This
  device needs (a) an a priori BOUND on the discrepancy quantity (here it's a difference
  of integers, bounded independent of the far-away index y), and (b) a divisibility fact
  growing with the gap y-j (here: f^n(m)-m divisible by n, hypothesis (i) of that
  problem, itself a strong given). Our setting has no analogous "the gap y-j necessarily
  divides some fixed discrepancy" mechanism on offer — gcd(a_{n_j}, a_{n_B}) does not
  obviously grow divisibility with the index gap. This looks like it would need genuinely
  new structural input not currently in the certified stack (same verdict as mechanism
  design generally) — flag as a DIRECTION to hunt for (a growing-gap divisibility
  identity) rather than a ready-made tool.

**3. aimo-0678 (France, "gcd/lcm coupled recurrence eventually periodic," subtopic
size-bounding-and-descent) — the MIN-OF-A-SET MONOVARIANT device the dispatch
specifically asked about.**
Crux move: define W_n = {m >= a_n : m does not divide the frozen invariant s_n}, w_n =
min W_n; show w_n is non-increasing (constant while a "good" regime holds, and when a
"bad" step occurs, the same value a_n re-enters W_{n+1}, giving w_{n+1} <= a_n = w_n).
Non-increasing positive-integer sequence => eventually constant => bounds a_n.
- **This is a genuine explicit-descent-on-a-set-min device, structurally different from
  plain pigeonhole**, and matches the dispatch's request #2 (monovariant/potential that
  strictly (non-)increases, forcing finiteness of "new classes"). However it critically
  relies on a FROZEN invariant s_n (a quantity literally constant across an entire
  regime, from an explicit algebraic recurrence a_{n+1}=gcd(a_n,b_n)+1 etc.) against
  which "not dividing" is checked — again leaning on an explicit closed-form recurrence
  that our problem does not have. **Assessment: the general PATTERN (find a monovariant
  defined as min of a bad-set, relative to some fixed/frozen background quantity) is
  worth flagging to the outliner as a proof-shape to hunt for, but no candidate frozen
  invariant analogous to s_n is currently visible in the imo-2026-06 workspace** — the
  quantity playing the closest role, b = the F''-part of a_{n_B}, IS already fixed/frozen
  (it's what Div(b) is built from), but the certified Confined-GCD Lemma already exploits
  exactly this fact (g_j confined to Div(b)) — that's precisely the pigeonhole step
  already tried and already stalled. Re-deriving "g_j lies in a bounded set" via a
  min-monovariant restatement would not add new content over Confined-GCD; the missing
  ingredient is still a genuine monotonicity direction on top of the bounded set (as in
  #1), which aimo-0678's story does not supply a general recipe for beyond its own
  specific algebraic recurrence.

**4. aimo-0611 (Austria, primitive-divisor / Zsigmondy-flavored sequence, subtopic
modular-arithmetic-and-CRT / lifting-the-exponent / zsigmondy-and-primitive-divisors) —
propagation of a modular relation by INDUCTION THROUGH THE DEFINING MAP.**
Crux: x_{i+m} = x_i (mod x_m) is proved by ordinary induction because every step applies
the SAME FIXED POLYNOMIAL f, so substituting the induction hypothesis into f (mod x_m)
literally reproduces the base case. This is the induction-through-recurrence device.
- Same disanalogy as #1/#3: needs a fixed algebraic map to substitute through. Our
  sequence's "next term" is defined by a search/minimality condition, not a formula, so
  there is no map to induct through in this literal sense. NOT transplantable as stated.
  This is worth stating explicitly to the outliner as a structural reason the whole
  algebraic-recurrence-induction family (which includes aimo-0477, aimo-0611, aimo-0678,
  aimo-0682, and by name matches round 7's already-refuted "aimo-0678-style
  algebraic-recursion transplant," see Witness Discontinuity Obstruction lemma) is a
  dead family for this problem's actual definitional structure — CONFIRMS, rather than
  contradicts, round 7's prior finding. Do not re-attempt this family without first
  establishing SOME closed-form local recurrence for consecutive A'-occurrences (which,
  if found, would itself likely BE the missing ingredient, making this observation
  circular as a "technique" and better understood as "what a real fix would look like").

**5. aimo-0682 (Brazil ISL-style, subtopic divisibility-and-gcd / p-adic-valuation /
size-bounding-and-descent) — "smooth-part vs large-prime-part" and "growing-modulus
squeeze," a genuinely different flavor.**
Crux: shows a functional congruence holds mod every LARGE-prime-factor modulus by
induction on the modulus size, then separately bounds the SMOOTH part by a pigeonhole
argument over finitely many small primes and finitely many residues, and finally
"bootstraps" an exact equality by choosing a modulus exceeding an a-priori bound on the
discrepancy (same "large-divisor forces vanishing" squeeze as aimo-0680).
- Same core squeeze idea as #2; same verdict: needs a growing-divisibility handle not
  currently present in our certified toolkit. Not directly transplantable, but the
  general SHAPE — split the promotion into "divisible by every large member of a growing
  divisor family" (usually easy/inductive) plus "control the small/smooth leftover by
  finite pigeonhole" (usually the hard direction) — is a decomposition style worth
  flagging: **is there an analogous split available for our g_j sequence**, e.g.
  splitting Div(b) into "primes dividing many consecutive g_j" (an easy/structural part)
  vs "primes that appear only sporadically" (a bounded leftover)? This is speculative and
  NOT verified against the certified lemma stack — flagged as an idea to test, not a
  result.

### Cheap-kill / plausibility check performed
None of mechanisms #1–5 above can be applied as a black-box citation; each requires
either (a) an algebraic recurrence our sequence provably does not have (ruled out
structurally — the recursive definition is an existential/minimality search, confirmed
by re-reading the problem statement and the certified Free Facts / Bounded Gap Lemma,
neither of which produces a closed-form successor map), or (b) a growing-divisibility
handle not present in the certified stack (open, unverified, would be new content if
found). I did not find any crux in number_theory or combinatorics whose "how_used"
supplies a way to promote existential-to-cofinite membership using ONLY finite-alphabet
pigeonhole data (which is all Confined-GCD/Cofinite-Sufficiency currently give) — every
corpus example that achieves this promotion leans on an explicit algebraic map or an
explicit a-priori-bounded discrepancy quantity, neither of which is available here yet.

### Direct search for a matching prior problem
Searched `past_problems_database.json` for statements combining "gcd" with
"smallest"/"least" (the literal shape of this problem's greedy definition) — found no
match (only aimo-0045, an unrelated root-of-unity minimization problem). Confirms this
problem's exact combinatorial shape (greedily recruit the smallest integer maintaining
pairwise gcd>1 with every earlier term) has no close analogue in the 2434-crux corpus;
the corpus's closest matches are all "prove eventual periodicity/constancy of an integer
sequence" targets with a DIFFERENT (algebraic-recurrence) generating mechanism.

### Candidate technique(s) to hand to the outliner
- Not a ready-to-apply crux move. The corpus confirms (via absence of a working example)
  that promoting "infinitely often in a fixed finite alphabet" to "cofinitely in a
  favorable sub-class" via pure pigeonhole is NOT how any solved analogous problem
  achieves this step — every solved analogue instead finds either (i) an explicit
  algebraic recurrence to induct through (unavailable here), or (ii) a genuine new
  monotonicity/identity linking consecutive occurrences (aimo-0477's per-prime valuation
  argument is the cleanest template for what shape this needs to take, even though its
  literal machinery does not transplant).
- Recommend the outliner/next builder explicitly hunt for a DIRECT, non-pigeonhole
  relationship between gcd(a_{n_j}, a_{n_B}) and gcd(a_{n_{j+1}}, a_{n_B}) — e.g. via the
  Bounded Gap Lemma's magnitude bound (a_{n_{j+1}} <= a_{n_j} + a_1) combined with the
  minimality of the greedy step, in the spirit of aimo-0477's "compare valuations at
  consecutive indices via an identity" but built from FIRST PRINCIPLES for this problem's
  actual (non-algebraic) recursive definition, since no corpus crux can be cited as
  supplying this identity ready-made.

### Knowledge-base entries
Not separately re-checked this round (out of lens scope); prior rounds' pointers to
knowledge_base.md's pigeonhole/CRT entries already inform the certified Cofinite
Sufficiency Lemma's finish and are unaffected by this crux-mining pass.

### Analogous past problems (cruxes) — final list
- **aimo-0477** (Mongolia, "eventually a_n=a_{n+1}" from an integrality condition) — the
  single best target-shape analogue (finite-alphabet gcd-chain + per-prime eventual
  monotonicity beating pigeonhole), but its mechanism needs an algebraic identity our
  problem's definition does not supply. Adapt the SHAPE of the argument, not the
  mechanics.
- **aimo-0678** (France, gcd/lcm coupled recurrence eventually periodic) — best template
  for a "min-of-a-bad-set" monovariant, per the dispatch's request #2, but again
  dependent on an algebraic recurrence unavailable here.
- **aimo-0680** (Singapore, functional iteration periodicity) — best template for a
  "divisibility grows faster than a bounded discrepancy" squeeze (dispatch's spirit of
  "use more structure than pigeonhole"), but the specific mechanism (hypothesis (i)'s
  n | f^n(m)-m) has no evident analogue in our problem yet.
No crux in the corpus solves this exact combinatorial shape (greedy pairwise-gcd
recruitment); treat all three as shape-templates to adapt from scratch, not citable
lemmas.

### Prior progress
See `results/imo-2026-06/current.md` (round 9 summary) and the certified lemma files
listed above — unaffected by this report; I did not attempt to advance the proof.

### Dead ends (do not retry)
- All 9 previously-certified-dead pigeonhole-promotion mechanisms (see current.md and
  Lemma I) — confirmed by this pass to be the same family every corpus analogue's
  "easy half" already achieves and stalls at exactly the same "hard half."
- The aimo-0678-style algebraic-recursion transplant — ALREADY explicitly tried and
  refuted in round 7 (Witness Discontinuity Obstruction, certified); this round's
  independent crux-mining reaches the same structural verdict from a different angle
  (no algebraic map exists to induct/recur through), reinforcing rather than
  contradicting round 7's finding. Do not re-attempt any member of the
  algebraic-recurrence-induction family (aimo-0477/aimo-0611/aimo-0678/aimo-0682-style)
  without first establishing a genuine closed-form local recurrence for our sequence's
  consecutive same-type occurrences.

### Small-case / intuition notes
None new this round — this was a pure literature/corpus-mining pass, not a computation
pass. (Conjecture status of FAH/Symmetric FAH/Cofinite FAH is unchanged: strongly
supported empirically across ~450+ tested seeds by prior rounds, still unproved.)
