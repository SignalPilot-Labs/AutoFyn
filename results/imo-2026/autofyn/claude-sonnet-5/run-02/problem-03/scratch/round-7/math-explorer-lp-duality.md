# Explorer report: pushing lp-duality-certificate toward general-n

Lens: push the n=2 (17-cell) and partial n=3 certificate toward a general-n
recursion or closed form. Read `problems.jsonl`, `knowledge_base.md`,
`results/imo-2026-03/current.md`, `results/imo-2026-03/approaches/
lp-duality-certificate.md` (full), and `results/imo-2026-03/lemmas/
odd-run-reduction-lemma.md`. Did NOT attempt a proof; this is terrain-scouting
with exact/numeric computation, findings below.

## 1. Structure of the existing n=2 certificate (17 cells)

The 17 cells all reduce to at most **two** elementary nonnegative terms with
coefficients in $\{0,\frac12,1\}$, plus (in 5/17 cells) a fixed additive
constant of exactly 1. Every term is one of: (Type I) a raw fragment value
$\ge0$, (Type II) an *adjacent* order-defining fact from the sorted cell
(never a transitively-implied, non-adjacent fact stated directly), or (Sym)
the WLOG "larger fragment first" convention. The $\frac12$ coefficient
appears exactly when a Sym fact ($p_1-p_2\ge0$, itself half of a fixed sum)
is the vehicle. This is a real, verified structural fact, not new — it's
already on file — but worth restating precisely since it's the basis for
extrapolation.

## 2. Attempted a fuller n=3 certificate (numeric + exact-symbolic, not just the on-file one-composition check)

I went beyond the file's single tested composition `(1,1,0,0)`. Using Monte
Carlo sorted-order enumeration (200k–400k trials per composition) plus
`sympy` for exact symbolic Phi-8 derivations on the resulting order-patterns,
I tested three further n=3 compositions:

- **`(2,0,0,0)`** (all 2 cuts on $p_1$, $p_2,p_3,p_4$ untouched): 8 distinct
  sorted-order cells (vs. 4 for n=2's `(2,0,0)`). Every cell admits a
  certificate with **≤2 elementary terms**, coefficient 1, matching the
  n=2 pattern. One cell (`P2,x,y,P3,P4,z`) needed a genuinely non-obvious
  step: the naive order fact alone ($y>2$) is *not* directly a primitive
  facet — it only follows by combining two independent constraints
  ($z<1$ and $x<4$) via the sum identity $x+y+z=8$. I found the exact
  decomposition $y-3=(1-z)+(4-x)$ (verified symbolically and by three
  numeric spot-checks with exact/decimal fractions). This is the first
  concrete instance of a "hidden" (non-adjacent-facet) constraint needing
  reconstruction via the sum identity rather than being read off the order
  directly — still only 2 terms, but a qualitatively new step not present
  in any n=2 cell.

- **`(1,1,1,0)`** (one cut each on $p_1,p_2,p_3$; $p_4=1$ untouched — a
  genuinely different composition shape from the file's tested
  `(1,1,0,0)`): **24 distinct sorted-order cells**, a real jump in
  raw combinatorial count (n=2's richest composition, `(1,1,0)`, had only
  4). Of these, only 3 dip near the target value $\Phi\approx8$ ("near-tight"
  cells); the rest have large slack and need no delicate argument. For the
  near-tight cells I derived exact symbolic certificates:
  - `(1x,1y,2x,2y,3x,P4,3y)`: $\Phi-8=(x_1-4)+(x_2-2)$ — 2 terms, using the
    Sym-derived facts $x_1>4$ (from $x_1>y_1$, sum 8) and $x_2>2$ (same
    style, sum 4). Clean, 2 terms.
  - A thinner cell, `(x,y,z,u,P_3,v,P_4)` (only ~0.13% of samples — i.e. a
    narrow region, plausibly close to an actual multi-way tie), required
    **3 elementary terms, each with coefficient $\frac12$**:
    $$\Phi-8=\tfrac12(x-y)+\tfrac12(z-u)+\tfrac12(u-2),$$
    verified both symbolically and by an exact numeric instance
    ($x{=}3.2,y{=}2.5,z{=}2.3,u{=}2.2,P_3{=}2,v{=}1.8,P_4{=}1$: both sides
    $=0.5$). This is the **first cell found (n=2 or n=3) that actually
    uses the conjectured full budget of $n=3$ terms**, and notably every
    term straddles a different pair of *adjacent* original pieces
    ($p_1$-internal, $p_1$/$p_2$-boundary, $p_2$/$p_3$-boundary) — i.e. the
    certificate's terms are not "one clean term per untouched/cut piece"
    but genuinely track the depth of *interleaving* between different
    pieces' fragments in the sorted order.

- **`(2,1,0,0)`** (2 cuts on $p_1$ + 1 cut refining the tail on $p_2$,
  $p_3,p_4$ untouched) — chosen specifically because this is the composition
  shape that actually instantiates the *open* general lower-bound gap
  (round 6's closed result is $c_1=1$ only; $c_1\ge2$ with tail refinement
  is exactly what's unproved). 32 distinct order-patterns, 7 near-tight. The
  two richest near-tight cells I checked both stayed at 1–2 elementary
  terms ($\Phi-8=v$ in one; $(1-z)+v$ in another) — i.e. on the samples
  checked, no cell yet forced a use of the full $(\star\star)$-style
  window argument. But coverage here is partial (2 of 7 near-tight cells
  checked symbolically, not all 7).

## 3. Is there a visible n=2 → n=3 recursion?

Yes, partially, confirming and slightly extending the file's Step-3 finding:
- Rescaling a cut-composition on $p_1,\dots,p_k$ by 2 and inserting a new
  untouched deepest piece $p_{k+1}$ reproduces the corresponding
  smaller-$n$ certificate's terms almost verbatim, **plus exactly one new
  term for the inserted piece** — confirmed again here on `(2,0,0,0)`
  (rescaled from n=2's `(2,0,0)`), not just the file's `(1,1,0,0)` case.
- BUT this "one clean new term per new piece" picture breaks down once a
  cut *also* refines a second, non-untouched piece simultaneously
  (`(1,1,1,0)`'s thin cell above): there the extra term isn't "one term for
  the new piece," it's a chain of $\frac12$-weighted terms that cross
  piece boundaries, one per adjacent pair in the interleaved sorted order.
  So the recursion is not simply "certificate$(n)$ = certificate$(n-1)$ +
  one clean correction term" in general — it's "+ one term per newly
  active *interleaving boundary*," and the number of those boundaries is
  what grows combinatorially with $n$, not the number of pieces.

## 4. Biggest obstruction, concretely

Two distinct obstructions, now with concrete data behind both:

(a) **Raw cell count grows fast.** n=2's worst composition had 4 cells;
n=3's had up to 32 (`(2,1,0,0)`) and 24 (`(1,1,1,0)`). This is expected for
a polytope-cell enumeration and is not fatal by itself — most cells are
slack (only 3–7 of them per composition are ever near-tight) — but it does
mean a *by-hand, cell-by-cell* certificate (what Step 2/3 did for n=2) is
not a viable strategy for general $n$; only a genuine induction on the
certificate's construction (the file's own "certificate sparsity
conjecture") could work, and that conjecture is exactly as hard as the
original theorem per the approach file's own honest admission — my
computations don't change that assessment, they just make it concrete: I
found a real cell (`(x,y,z,u,P_3,v,P_4)`) that needs the *full* conjectured
budget of $n$ terms with $\frac12$ coefficients throughout, which is
consistent with the conjecture but is also the first evidence the budget
is actually tight (not a loose conservative bound), meaning there is no
slack margin to absorb further complications at $n=4,5,\dots$

(b) **Cross-piece straddling is the real driver of complexity, and it is
exactly $(\star\star)$'s content in different notation.** The thin cell's
certificate needed a term ($z-u$) that compares a fragment of $p_1$'s
split against a fragment of $p_2$'s split directly — not against a fixed
ladder threshold, and not within one piece's own Sym convention. This
cross-piece comparison is structurally the same object $(\star\star)$'s
window-integral argument was built to control (bounding how the tail's own
odd-parity mass interacts with a threshold set by the top piece). I did
not find a case where the certificate *needs* a term that isn't a simple
linear difference (i.e. nothing yet forces a non-elementary $g_k$), so the
certificate hasn't been shown to *fail*— but the terms needed to assemble
it are visibly drawn from the same interleaving structure $(\star\star)$
targets, not a different one. This directly supports the approach file's
own "central risk" (gap 3): the evidence here leans toward "this framing
re-encounters $(\star\star)$'s content in new notation" rather than
"structurally evades it," though it is not a proof either way — no cell
tested yet actually requires arbitrary-$n$-many terms or an unbounded
window sum; a decisive test would be pushing to $n=4$ or $n=5$ on a cell
analogous to `(2,1,0,0)`'s hardest sub-case, or (more efficient) trying to
directly express $(\star\star)$'s own inequality *as* a certificate in this
framework and seeing whether that succeeds cleanly or requires infinitely
many terms as $n\to\infty$.

## Recommendation

Most promising concrete next step: don't keep sampling more n=3
compositions by hand (diminishing returns, as cell counts explode) — instead
directly attempt to write $(\star\star)$ itself (the certified $c_1=1$
closure, `half-window-vanishing-lemma`) as a certificate in this framework's
own vocabulary. If it converts cleanly into a bounded-term Type-I/II/Sym sum,
that's real evidence for a general recursion (and reusable machinery for
$c_1\ge2$). If it provably cannot (e.g. requires a term count growing with
$n$, unlike anything found so far, or needs the window-integral itself as an
irreducible non-elementary primitive), that is the honest negative result
the approach file itself invites as an acceptable outcome — and would let
the project stop re-trying this framing on the general lower bound while
still keeping the certified n=2 (and now broader n=3 partial) results as
reusable case data.
