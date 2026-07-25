## Contamination Dichotomy Lemma and Reduction Proposition

**Setup.** Fix $a_1$, $P:=R(a_1)$, and the true sequence $(a_n)$. For
$i<j$, say $(i,j)$ **witnesses** a prime $r$ if $R(a_i)\cap R(a_j)=\{r\}$
(the `nec-necessity.md` definition of membership in $\mathrm{Nec}$); say a
prime $s\ne r$ with $s\in R(a_i)\cap R(a_j)$ is a **contaminant of $(i,j)$
for $r$** if $r\in R(a_i)\cap R(a_j)$ but $(i,j)$ does not witness $r$
because some other shared prime $s$ is also present.

**Contamination Dichotomy Lemma.** For any $i<j$ and any prime
$r\in R(a_i)\cap R(a_j)$, exactly one holds: (a) $(i,j)$ witnesses $r$, or
(b) $(i,j)$ has at least one contaminant for $r$.

*Proof.* Immediate: $R(a_i)\cap R(a_j)\ni r$ either equals $\{r\}$ (case a)
or contains some other element $s\ne r$ (case b); mutually exclusive and
jointly exhaustive. $\blacksquare$

**Definition (Uncontaminated-Witness Existence).** Fix a prime
$r\notin P$ dividing at least one term, and a reference index $i$ with
contaminant set $E_i:=R(a_i)\setminus\{r\}$. Say Uncontaminated-Witness
Existence holds for $(r,i)$ if there is $j\ne i$ with $r\in R(a_j)$ and
$R(a_j)\cap E_i=\emptyset$ — equivalently (by the Dichotomy Lemma), $(i,j)$
witnesses $r$.

**Reduction Proposition.** If, for every prime $r\in\mathrm{Nec}\setminus
P$, there is some index $i$ for which Uncontaminated-Witness Existence
holds at a bounded index $j\le N(a_1)$, then the Bounded-Witness-Index
Conjecture (some computable $N(a_1)$, function of $a_1$ alone, bounds the
first-witness index for every new element of $\mathrm{Nec}\setminus
R(a_1)$) holds with that same $N(a_1)$.

*Proof.* Immediate from the definitions: Uncontaminated-Witness Existence
for $(r,i)$ at index $j$ says exactly that $(i,j)$ witnesses $r$; if this
$j\le N(a_1)$ for every $r$ (choosing, for each $r$, its own witnessing
pair), the Conjecture's conclusion holds by definition. $\blacksquare$

### What this buys
Converts the global existential "does $N(a_1)$ exist for the whole
sequence" into an independent per-prime, per-reference-index search
question. Localizes but does not close the Bounded-Witness-Index
Conjecture — the persistence-of-contamination question (does a fixed
finite avoid-set keep intersecting every sufficiently-late multiple of the
target prime, forever) remains open and is, honestly, not obviously easier
than the original central existence gap: no unconditional independence/
density statement is known that would bound it.

### Caveat
This is an organizing/localizing lemma only; it does **not** close the
central existence gap (finiteness of $\mathrm{Nec}$ / self-sufficiency of
$Q_{\min}$) and should not be cited as doing so. It is elementary (both
parts are essentially restatements from the definitions) but genuinely
useful bookkeeping, independently re-verified.

### Provenance
Proved in `approaches/active-set-stabilization.md`, round 6 ("The
Contamination framework"). Independently re-derived and applied by the
proof-reviewer to the $a_1=20735$ hand-trace (`$r=19$, reference index
$i=4$, obstruction set $\{2,3,7,13\}$, uncontaminated witness at $j=70$`),
confirmed exact by direct simulation.
