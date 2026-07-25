## imo-2026-06 (lens: prime-free scalar-difference / syndeticity gap)

- Distinct openings surfaced this round:
  1. **Morse–Hedlund subword-complexity reformulation.** The gap sequence
     $d_n:=a_{n+1}-a_n$ already lives in the finite alphabet $\{1,\dots,R\}$
     (certified `bounded-gap-via-rad-a1.md`). Morse–Hedlund's theorem (a
     one-sided sequence over a finite alphabet is eventually periodic **iff**
     its factor-complexity function $p(k)$ (number of distinct length-$k$
     factors) satisfies $p(k)\le k$ for *some* $k$ — equivalently iff $p$ is
     bounded as $k\to\infty$, since $p$ is always non-decreasing) gives an
     exact restatement of the WHOLE theorem purely in terms of $(d_n)$, with
     no prime bookkeeping. This is structurally different from the killed
     `windowed-epsilon-automaton-failure.md` mechanism: that lemma only rules
     out a FIXED, small window size determining the next symbol; Morse–
     Hedlund only needs boundedness of the complexity function for SOME
     (possibly large, not a priori fixed) window length $k$. Caveat (see
     below): I do not have a route to prove $p(k)$ is bounded that avoids the
     same underlying difficulty — flagging it as vocabulary/reformulation,
     not a proven shortcut.
  2. **Explicit-candidate domination/majorization comparison.** Rather than
     pigeonholing an abstract recurring scalar, build an EXPLICIT candidate
     periodic sequence $\hat a_n$ (e.g. defined directly from $Q_{\min}$ or
     from an empirically-observed period, if one could be pinned down
     independently) and prove a monovariant/majorization statement — "the
     true greedy sequence can never produce a term smaller than $\hat a_n$,
     and if it ever produces a strictly larger one at some index the excess
     is absorbed and does not propagate" — using the same "least
     prefix-index where majorization first breaks" technique seen in the
     crux corpus (see below). This targets syndeticity/eventual-equality via
     a two-sequence comparison instead of a one-sequence pigeonhole; nobody
     in the population has tried a comparison-sequence argument yet (all 8
     approaches to date pigeonhole or induct on a single sequence's own
     state).
  3. **Sharpen "positive upper density" to "positive LOWER density / bounded
     gaps between recurrences" directly**, by tracking not just $c_v(N)$ but
     the actual GAP sequence between consecutive elements of $Y_T$ as its own
     new finite/growing-alphabet object and re-running the identical
     Lemma-3-style limsup/subadditivity argument one level up (i.e. pigeonhole
     on *that* gap sequence too, recursively) — this is a cheap, mechanical
     extension of the already-certified argument that has not been tried; it
     would need a boundedness input on the between-recurrence gap itself,
     which is not yet available, but is worth flagging as the natural next
     mechanical step from Lemma 3 before reaching for heavier machinery.

- Candidate technique(s): Morse–Hedlund / subword (factor) complexity theory
  from combinatorics on words (new to this population); majorization/
  domination comparison-sequence induction (technique family seen in crux
  corpus, e.g. `aimo-0718`, `aimo-0626`); iterated pigeonhole on the
  between-recurrence gap sequence (mechanical extension of the population's
  own certified `positive-density-upgrade.md`).

- Cheap-kill candidates: none obvious found this round beyond what's already
  certified — I looked for a parity/size obstruction specific to $g_n(T)$ or
  $r_n=a_n\bmod R$ that would immediately kill syndeticity or immediately
  prove it, and found none; the alphabet-size bound $[T,TR]$ is already the
  sharpest cheap structural fact available (Lemma 1/positive-density-upgrade
  route). No new pruning found.

- Knowledge-base entries to use: none of `knowledge_base.md`'s generic
  theorems appear to add anything beyond what the population has already
  invoked (pigeonhole, Fekete's subadditive lemma — already checked and ruled
  inapplicable, §4 move 1 of `scalar-difference-pigeonhole.md`). Consider
  citing Morse–Hedlund explicitly by name if the outliner adopts opening (1)
  — it is a classical, citable theorem (not currently in `knowledge_base.md`;
  recommend the outliner add it if used, per CLAUDE.md's "name your tools"
  rule).

- Analogous past problems (cruxes):
  - `aimo-0678` (number_theory, modular-arithmetic-and-CRT) — already the
    population's closest analog (per memory rule #22): "once one coordinate
    of a coupled recurrence is bounded, reduce mod lcm of the bounded
    coordinate's values for a finite-state pigeonhole." Already tried and
    shown NOT to transplant (`aimo-0678-mechanism-inapplicability.md`,
    round 5) — do not re-attempt verbatim; only its high-level
    "bounded-coordinate → reduce mod lcm" *shape* is relevant, and that shape
    is exactly what the $Q$/Nec line (not this scalar line) is already
    pursuing.
  - `aimo-0718` (combinatorics, invariants-and-monovariants) — crux move:
    "to show a fixed comparison sequence keeps majorising an evolving one,
    take the least prefix index where majorisation would first break." This
    is genuinely analogous in SHAPE (not in problem content) to opening (2)
    above: it is the standard technique for proving two sequences (one
    explicit, one adaptively-defined) stay in a fixed order relation forever
    by contradiction at the first failure index. Worth adapting as a
    template if the outliner wants to try the comparison-sequence route.
  - `aimo-0907` (algebra, functional-equations) — crux move: "when two
    orbits provably merge (agree from some point on), define the common
    iterate-index offset between them as an invariant." Analogous in SHAPE to
    the "transient-free-finishing-theorem" already certified (defining
    $T,L$ once agreement is known) — not a new lever, but confirms the
    population's existing finishing-move choice is the standard one for this
    problem shape.
  - No crux in the corpus attacks a genuine "smallest-integer-satisfying-a-
    growing-coprimality-constraint-set" recurrence (re-confirmed this round,
    consistent with memory rule #22's prior finding) — searched
    `sequences-and-recurrences`, `processes-and-algorithms`,
    `pigeonhole`/`invariants-and-monovariants` subtopics for "greedy",
    "smallest", "eventually periodic", "syndetic": found only shape-level
    analogs (above), no content-level match. Treat this as a confirmed
    corpus gap, not a missed search.

- Prior progress: `scalar-difference-pigeonhole.md` has proved, fully
  unconditionally: Lemma 1 (bounded scalar difference,
  $g_n(T)\in[T,TR]$), Lemma 2 (pigeonhole ⟹ some $L(T)$ recurs infinitely
  often), Lemma 3 (Positive-Density Upgrade: some $L(T)$ recurs with
  $\limsup$ upper density $\ge 1/(TR-T+1)$), Lemma 4 (Sharpened Bounded-Gap
  Lemma, residue-dependent refinement $a_{n+1}-a_n\le R-r_n$). It has
  explicitly and correctly identified two stalled next-moves (Fekete/Cesàro
  convergence — inapplicable, no subadditivity relation known; combining
  density with the sharpened gap bound — no established link between
  $n\in Y_T$ and $r_n$). Status: partial, honestly self-assessed, no false
  claim of closure.

- Dead ends (do not retry):
  - Naive local propagation ("two/three consecutive matches propagate
    forever") — refuted, $a_1=99,T=1$ breaks at $n=4$ after matching at
    $n=1,2,3$.
  - ISL-2015-N6/`aimo-0680`-style sandwich using $d\mid a_{n+d}-a_n$ — this
    divisibility hypothesis is FALSE here ($a_1=15$: $a_3-a_1=5$, not
    divisible by $2$); confirmed again this round, do not re-attempt without
    first proving a from-scratch substitute divisibility fact (none exists
    yet).
  - Fekete's subadditive-lemma route to Cesàro-average convergence — no
    subadditivity/superadditivity relation for $(a_n)$ is known or evident
    from the greedy rule (the rule depends on the ENTIRE prefix, not a
    two-term recursion); I could not find one either this round.
  - `windowed-epsilon-automaton-failure.md`'s bounded-window mechanism
    remains dead (confirmed the reasoning holds: the true state needed,
    $a_n\bmod R$, is a cumulative sum over the WHOLE history of gaps mod
    $R$, not expressible from any bounded-size window of recent gaps) — this
    is exactly why opening (1)'s Morse–Hedlund route needs a possibly-large
    but *fixed* window, not a literal bounded/small one; don't conflate the
    two.

- Small-case / intuition notes (all conjecture/evidence, not proof):
  - Re-ran a robust period-finder (candidate transient $n_0$ explicitly
    scanned, $\ge200$–500 confirming terms after) on seeds
    $\{15,35,65,77,91,99,105,143,165,231\}$: **every single one** locks with
    transient $n_0=0$ — periodicity $a_{n+T}=a_n+L$ holds from $n=1$ with NO
    transient, for every seed where a period was found within the tested
    horizon. This reconfirms the round-2/round-3 finding
    (`memory/math-explorer.md` rule #13) with a fresh, independent
    implementation and larger confirming windows (200–500 terms, not just
    ~30–100). This is striking: it suggests the real target may be stronger
    than "syndeticity" — the conjecture is exact periodicity from the very
    first term, always, with zero transient. If true, "eventually always"
    (the framing in this round's dispatch) is the WRONG intermediate target;
    the right one is "exactly always, no transient," matching
    `transient-free-finishing-theorem.md`'s conditional finish.
  - $a_1=375$ and $a_1=385$ still fail to stabilize within a period search up
    to $T=400$, $8000$ terms generated (re-confirms the round-2 finding that
    transient/stabilization length is not a small/bounded function of $a_1$,
    and is NOT simply related to $\mathrm{rad}(a_1)$ or $\omega(a_1)$ in any
    way I could detect from these two data points alone — both have
    $\omega(a_1)=3$, both still unresolved at $8000$ terms, no new
    distinguishing invariant found). This means: whatever mechanism the
    outliner picks, it must NOT assume a horizon of a few hundred/thousand
    terms suffices to witness stabilization for all seeds — consistent with
    the already-certified finding, just re-verified with a bigger horizon.
  - No correlation found (2-point sample only, not a real test) between
    $\mathrm{rad}(a_1)$/$Q_{\min}$-recruitment-index and how fast the SCALAR
    route's own $Y_T$ set achieves visible density in a short simulation —
    ran out of round time to build a proper statistic here; flag as an
    unexplored but cheap numeric check for a future round if the scalar line
    stays live (track $|Y_T\cap[1,N]|/N$ for the seeds' own true minimal $T$
    and see if it visibly trends toward $1$, vs. plateauing at some $<1$
    value, as $N$ grows past the transient).
