# Audit Investigation — M-2: Does Δ<sub>L2</sub> Distinguish Active Advisory Restriction from Complete AI Withdrawal?

**Scope:** Finding M-2 only.
**Manuscript:** `publications/active/aai-2026/drafts/aai-2026-manuscript-v6-rewrite-v2.docx`
**Investigation date:** 8 October 2026
**Mode:** read-only. Nothing modified, no experiment re-run. Derivations and counterexamples only.

---

## A. Executive Finding

**Overall classification: PARTIALLY CONFIRMED. The mathematics of M-2 is correct; the inference I drew from it was overstated in two specific ways, and I withdraw it in that form.**

**What is correct.** Δ<sub>L2</sub> is invariant across *every* choice of A<sub>AI</sub>(CAUTION) other than FULL — including ∅. Verified from the implementation, which represents recommendation sets as explicit `frozenset` objects and compares them with set inequality (`condition_comparison.py:85–87, 169–171, 198`). The participation gate `G` appears nowhere in the metric computation. So as a measuring instrument, Δ<sub>L2</sub> cannot discriminate an active contracted set from a withdrawal at CAUTION.

**What I got wrong.**

1. **The architecture does separate participation from advisory scope — formally, prominently, and as its stated contribution.** `appendix-c-formalisation.md` C.3 defines a primitive participation gate `G(S)`; C.5 names Level 1 (participation) and Level 2 (advisory scope); C.6 constrains them; and line 1178 states that the contribution is "the **governance pair (G(S), A_AI(S))** — a mechanism that separates two questions existing architectures conflate into one binary: *whether* the AI participates, and *what it may recommend*." My audit asserted that "the metric cannot see the property the positioning turns on", which conflated the **metric's discriminative capability** with the **architecture's expressive capability**. Those are different questions and I ran them together.

2. **A non-emptiness requirement already exists.** **Corollary C.2 (Strict Monotonicity)**, `appendix-c-formalisation.md:876`: *"The inclusions in Cases 1 and 2 are strict: A_AI(UNSAFE) ⊊ A_AI(CAUTION) ⊊ A_AI(SAFE)."* Since A<sub>AI</sub>(UNSAFE) = ∅, this is exactly ∅ ⊊ A<sub>AI</sub>(CAUTION). The remedy I proposed was already a theorem of the architecture. Case B is not an admissible instance of the canonical architecture at all.

**What survives, and is worth fixing.** Three narrow defects, each a one-line import of something the canonical record already contains:

- **The manuscript states only the upper half of the containment chain.** §III requires "a strict subset of FULL"; the architecture requires ∅ ⊊ A<sub>AI</sub>(CAUTION) ⊊ FULL. As written, the invariance sentence describes a class of configurations wider than the architecture admits.
- **A genuine asymmetry in C.6.** The *Advisory Restriction Constraint* bounds A<sub>AI</sub>(CAUTION) from above (⊂ A<sub>AI</sub>(SAFE)) but imposes no lower bound. Non-emptiness is a **corollary of the canonical instantiation**, not a **constraint on admissible instantiations**. This is the real formal gap, and the auditor did not identify it.
- **Table I's footnote misdescribes G.** It says *"G is determined by emptiness of A_AI"*. C.3 defines G by **state** (0 if S = UNSAFE, 1 if S ∈ {SAFE, CAUTION}); the emptiness at UNSAFE follows from C.6's Participation Constraint. The footnote inverts the dependency. `G` is also never defined in the manuscript body — it appears only inside Table I.

**Crucially: the manuscript nowhere claims Δ<sub>L2</sub> discriminates active contraction from withdrawal.** It says the opposite — *"Δ<sub>L2</sub> measures how often the intermediate restriction binds, not how much the recommendation set contracts"* — and it tells the reader directly that the metric is content-blind. **There is no overclaim to correct.** The defect is an under-specified condition, not a false statement.

**Submission risk: LOW.** No numerical result changes, no metric redesign is warranted, and no new measurement is needed. **About 15 words.**

---

## B. Evidence Inventory

| Path | Location | Evidence | Strength |
|---|---|---|---|
| `docs/canonical/appendix-c-formalisation.md` | **C.3, lines 749–759** | **`G(S) = 0 if S = UNSAFE; 1 if S ∈ {SAFE, CAUTION}`** — a primitive, state-indexed participation gate. *"This gate controls AI participation, but it does not define the scope of AI recommendations."* | **Direct — formal definition** |
| same | C.4, lines 765–792 | `R = {Go, Delay, DepartureTime, Duration}`; A<sub>AI</sub>(SAFE) = R, A<sub>AI</sub>(CAUTION) = {Go, Delay}, A<sub>AI</sub>(UNSAFE) = ∅; containment chain **A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅** | **Direct — formal definition** |
| same | **C.5, lines 798–818** | **Two-level governance.** Level 1 – Participation Governance: `G(S)`. Level 2 – Advisory Scope Governance: `A_AI(S)`. *"the AI decision system is governed by the pair (G(S), A_AI(S))"* | **Direct — formal definition** |
| same | **C.6, lines 823–835** | **Participation Constraint: `G(S) = 0 ⇒ A_AI(S) = ∅`** (one direction only). **Advisory Restriction Constraint: `S = CAUTION ⇒ A_AI(CAUTION) ⊂ A_AI(SAFE)`** (upper bound only) | **Direct — formal constraints; the asymmetry is visible here** |
| same | C.6, line 844 | **Theorem C.2 (Monotonicity of A_AI):** for all S₁, S₂, if S₁ ≻ S₂ then A_AI(S₁) ⊆ A_AI(S₂) | **Direct — theorem** |
| same | **line 876** | **Corollary C.2 (Strict Monotonicity): "A_AI(UNSAFE) ⊊ A_AI(CAUTION) ⊊ A_AI(SAFE)"** — with A_AI(UNSAFE) = ∅ this *is* the non-emptiness requirement | **Direct — the decisive finding** |
| same | lines 106–108 | State definitions: SAFE "G(S) = 1 and A_AI(S) = R"; **CAUTION "G(S) = 1 and A_AI(S) ⊊ R"**; UNSAFE "G(S) = 0 and A_AI(S) = ∅" | **Direct — formal definition** |
| same | line 420 | *"Where graduation lives"* — graduation holds **because** of the strict chain, "and because CAUTION is reachable in 𝒮" | **Direct — interpretive anchor** |
| same | **line 1178** | *"The contribution is the **governance pair (G(S), A_AI(S))** — a mechanism that separates two questions existing architectures conflate into one binary: whether the AI participates, and what it may recommend."* | **Direct — the project's own contribution statement** |
| same | line 1019 | *"G(S) sets participation; A_AI(S) sets admissible advisory scope."* | **Direct** |
| same | line 1146 | Symbol table: **G(S) | AI participation gate | C.3** | **Direct** |
| same | — | **No non-emptiness *axiom* anywhere.** A targeted search for "non-empty", "≠ ∅", "⊋ ∅" returns only unrelated hits about the declared exclusion set D | **Direct — negative finding, searched** |
| `scripts/condition_comparison.py` | **lines 85–87** | `FULL = frozenset({"Go","Delay","DepartureTime","Duration"})`; `RESTRICTED = frozenset({"Go","Delay"})`; `EMPTY = frozenset()` — **recommendation sets are explicitly represented, not encoded as state labels** | **Direct — code** |
| same | lines 92–106 | The four configurations as explicit state→set maps, with comments: C1 *"Participation gated; scope never restricted while active"*; C2 *"The proposed architecture. Scope contracts at the intermediate state."* | **Direct — code** |
| same | lines 169–171 | `def admissible(states, cond): table = A_AI[cond]; return [table[s] for s in states]` | **Direct — code** |
| same | **line 198** | **`diff = sum(1 for x, y in zip(sets[a], sets[b]) if x != y)`** — **set inequality**, not strict subset | **Direct — the decisive implementation line** |
| same | lines 191–192 | Printed header: *"Pairwise admissible-set divergence (% of hours the two conditions permit DIFFERENT recommendation sets)"* | **Direct — code** |
| same | — | **`G` is never computed, stored or referenced in the metric path.** It appears only in docstring prose (lines 9, 14) | **Direct — negative finding, searched** |
| `data/c8/canonical-results-post-migration.txt` | lines 215–226, 249–260 | Stored execution output: PRIMARY CAUTION 531 / n 9,135 / C1↔C2 5.81%; RESOLUTION CAUTION 266 / n 5,935 / C1↔C2 4.48% | **Direct — stored artefact** |
| manuscript §III | — | *"the value of Δ<sub>L2</sub> is invariant to the content of A<sub>AI</sub>(CAUTION), **provided that set remains a strict subset of FULL**"* | **Direct — the sentence at issue** |
| manuscript §III | — | *"Δ<sub>L2</sub> measures how often the intermediate restriction binds, **not how much the recommendation set contracts**"* | **Direct — the manuscript's own guard** |
| manuscript Table I note | — | *"G is determined by emptiness of A<sub>AI</sub> and is shown for readability only."* — **contradicts C.3**; `G` appears nowhere else in the manuscript | **Direct — defect** |

---

## C. Canonical Formal Definitions

### C.1 What is formally defined

| Object | Definition | Location |
|---|---|---|
| Safety state S | `S ∈ {SAFE, CAUTION, UNSAFE}`, `S = f(E)`, total (Theorem C.1) | C.2 |
| Severity order | `UNSAFE ≻ CAUTION ≻ SAFE` | C.1 |
| Recommendation universe | `R = {Go, Delay, DepartureTime, Duration}` | C.4 |
| **Participation gate** | **`G(S) = 0` if S = UNSAFE; `1` if S ∈ {SAFE, CAUTION}** — defined on the state, independently of A<sub>AI</sub> | **C.3** |
| Admissible recommendation space | `A_AI(SAFE) = R`, `A_AI(CAUTION) = {Go, Delay}`, `A_AI(UNSAFE) = ∅` | C.4 |
| Governance pair | `(G(S), A_AI(S))` — Level 1 and Level 2 | C.5 |
| Participation Constraint | `G(S) = 0 ⇒ A_AI(S) = ∅` | C.6 |
| Advisory Restriction Constraint | `S = CAUTION ⇒ A_AI(CAUTION) ⊂ A_AI(SAFE)` | C.6 |
| Monotonicity | `S₁ ≻ S₂ ⇒ A_AI(S₁) ⊆ A_AI(S₂)` | Theorem C.2 |
| **Strict monotonicity** | **`A_AI(UNSAFE) ⊊ A_AI(CAUTION) ⊊ A_AI(SAFE)`** | **Corollary C.2** |
| Configuration disagreement | **implemented** as set inequality over the per-hour admissible sets | `condition_comparison.py:198` |
| Δ<sub>L2</sub> | `(C0↔C2) − (C0↔C1)` | manuscript §III |

### C.2 What is assumed rather than defined

1. **A non-emptiness constraint on A<sub>AI</sub>(CAUTION).** It is *derived* (Corollary C.2) for the canonical instantiation, never *imposed*. C.6 bounds A<sub>AI</sub>(CAUTION) from above only. **A configuration with A<sub>AI</sub>(CAUTION) = ∅ satisfies both C.6 constraints** — ∅ ⊂ R is true, and the Participation Constraint is vacuous since G(CAUTION) = 1 — while violating Corollary C.2. The architecture is internally consistent but its *constraint set* is weaker than its *theorems*.
2. **The ↔ operator.** The manuscript writes a symmetric arrow and defines N<sub>restricted</sub> as *"the number of those hours in which one configuration admits a strictly smaller set than another"* — a **directional, strict-subset** reading. The implementation counts **set inequality**. Within this architecture every admissible set is a subset of R, so "≠ FULL" ⟺ "⊊ FULL" and the two coincide for all four configurations; but the definitions are not the same, and the prose one is narrower than the code.
3. **The relation between G and A<sub>AI</sub> emptiness.** The manuscript's Table I footnote asserts a biconditional the formalisation does not state and whose direction it reverses.

---

## D. State-by-State Derivation

Derived from the canonical mappings, not assumed. Let p<sub>S</sub>, p<sub>C</sub>, p<sub>U</sub> be the proportions of evaluated hours classified SAFE, CAUTION, UNSAFE, with p<sub>S</sub> + p<sub>C</sub> + p<sub>U</sub> = 1. Write D(X,Y) for the proportion of hours on which X and Y admit different sets.

| State | C0 | C1 | C2 | C3 | C0 vs C1 | C0 vs C2 | C1 vs C2 | C1 vs C3 |
|---|---|---|---|---|---|---|---|---|
| SAFE | FULL | FULL | FULL | FULL | same | same | same | same |
| CAUTION | FULL | FULL | {Go, Delay} | FULL | same | **differ** | **differ** | same |
| UNSAFE | FULL | ∅ | ∅ | ∅ | **differ** | **differ** | same | same |

Therefore:

```
D(C0,C1) = p_U
D(C0,C2) = p_C + p_U
D(C1,C2) = p_C
D(C1,C3) = 0

Δ_L2 = D(C0,C2) − D(C0,C1) = (p_C + p_U) − p_U = p_C = P(S = CAUTION)      ∎
```

**Check against the stored artefact.** PRIMARY: p<sub>U</sub> = 3,917/9,135 = 42.88% = D(C0,C1) ✔; p<sub>C</sub> + p<sub>U</sub> = 4,448/9,135 = 48.69% = D(C0,C2) ✔; p<sub>C</sub> = 531/9,135 = 5.81% ✔. RESOLUTION: 2,438/5,935 = 41.08% ✔; 2,704/5,935 = 45.56% ✔; 266/5,935 = 4.48% ✔. The derivation and the implementation agree exactly.

**Assumptions the identity requires:**

| Requirement | Needed? | Why |
|---|---|---|
| C1 and C2 agree at SAFE | **Yes** | Otherwise the SAFE term does not cancel |
| C1 and C2 agree at UNSAFE | **Yes** | Otherwise the p<sub>U</sub> terms do not cancel |
| C1 and C2 differ at CAUTION | **Yes** | Otherwise Δ<sub>L2</sub> = 0 |
| C0 admits FULL at every state | **Yes** | Makes D(C0,·) count exactly the states where · ≠ FULL |
| State classification identical across configurations | **Yes** | All four share one classifier (`condition_comparison.py` classifies once, then applies four maps) |
| **A<sub>AI</sub>(CAUTION) non-empty** | **No** | ∅ ≠ FULL, so the CAUTION cell still differs |
| **A<sub>AI</sub>(CAUTION) a strict subset of FULL** | **No** — only that it ≠ FULL | Within this architecture every set ⊆ R, so ≠ FULL ⟺ ⊊ FULL; the subset relation is incidental |
| **Specific elements retained** | **No** | Only set identity is tested |
| **Cardinality** | **No** | {Go} and {DepartureTime, Duration} give the same result |
| **Magnitude of restriction** | **No** | The indicator is binary per hour |
| Frequency of CAUTION | — | **This is what Δ<sub>L2</sub> *is*** |

**Metric property vs architectural property.** Content-independence is a property of the **metric**: a per-hour binary indicator cannot carry magnitude. Non-emptiness at CAUTION is a property of the **architecture** (Corollary C.2). The two are independent, and M-2's error was to treat the metric's blindness as evidence that the architecture lacks the distinction.

---

## E. Counterexample Analysis

All configurations hold C0, C1, C3 fixed and vary only A<sub>AI</sub>(CAUTION) in C2. "Admissible?" means: permitted by the canonical architecture (C.6 constraints **and** Corollary C.2).

| Case | A<sub>AI</sub>(CAUTION) | Participation active at CAUTION (G = 1, set ≠ ∅)? | Strict subset of FULL? | Differs from C1 at CAUTION? | Δ<sub>L2</sub> | Metric distinguishes from Case A? | Admissible under the architecture? |
|---|---|---|---|---|---|---|---|
| **A** canonical | {Go, Delay} | **Yes** | Yes | Yes | **p<sub>C</sub>** | — | **Yes** |
| **B** complete withdrawal | **∅** | **No** — gate open, nothing admissible | Yes (∅ ⊊ FULL) | Yes | **p<sub>C</sub>** | **No** | **No** — violates Corollary C.2 (∅ ⊊ A<sub>AI</sub>(CAUTION) fails). *Satisfies both C.6 constraints, which is the gap.* |
| **C** minimal non-empty | {Go} | Yes | Yes | Yes | **p<sub>C</sub>** | **No** | Yes |
| **D** equal cardinality, different content | {DepartureTime, Duration} | Yes | Yes | Yes | **p<sub>C</sub>** | **No** | Yes, by the letter of C.6; arguably contrary to intent (C.4 states CAUTION withholds *timing and duration* guidance specifically) |
| **E** no restriction | FULL | Yes | **No** | **No** | **0** | **Yes** | **No** — C.6 Advisory Restriction Constraint requires proper containment |
| **F** singleton outside R | {Go, Abort} | Yes | **No** — not a subset of FULL at all | Yes | **p<sub>C</sub>** under the implementation (≠); **0** under the manuscript's "strictly smaller" prose | **No** (implementation) | **No** — A<sub>AI</sub>(S) ⊆ R by C.4 |
| **G** C1 also contracted | C1 CAUTION = C2 CAUTION = {Go, Delay} | Yes | Yes | **No** | **0** | **Yes** | Not the evaluated comparator — C1 is defined as participation-only |

**Reading.** The metric partitions all configurations into exactly two classes: **A<sub>AI</sub>(CAUTION) = FULL → Δ<sub>L2</sub> = 0**, and **everything else → Δ<sub>L2</sub> = p<sub>C</sub>**. Cases A, B, C and D are mutually indistinguishable. The auditor's Case B is therefore real **as a statement about the metric** and unreachable **as a statement about the architecture**.

Case F is a side-finding: it is the one configuration on which the manuscript's prose definition and the implementation disagree. It is excluded by C.4 (A<sub>AI</sub>(S) ⊆ R), so nothing turns on it here, but it shows the prose definition is not the implemented one.

---

## F. Participation Versus Advisory Scope

### F.1 Does the architecture separate them? **Yes — explicitly, and as its named contribution.**

The separation is not implicit, not an assumption, and not reconstructible only from the configuration table. It is a labelled two-level structure:

- **Level 1, Participation Governance:** `G(S)`, defined in C.3 **on the state**, with its own semantics (*"G(S) = 0 → AI disabled; G(S) = 1 → AI enabled"*) and the explicit disclaimer *"This gate controls AI participation, but it does not define the scope of AI recommendations."*
- **Level 2, Advisory Scope Governance:** `A_AI(S)`, defined in C.4.
- **The pair `(G(S), A_AI(S))`** is the governed object (C.5), the subject of the Safety Dominance analysis (C.7), and is named at line 1178 as the contribution itself.

Participation is represented as **a separate state-dependent Boolean function**, not as non-emptiness, not as a procedural rule, and not implicitly. The coupling runs one way only: C.6's Participation Constraint says a closed gate forces an empty set, not that an empty set closes the gate.

### F.2 Is the manuscript's central distinction genuinely represented? **Yes.**

The manuscript's positioning against [9] — *"that zone withdraws automated action rather than retaining an active contracted recommendation set"* — maps onto a real architectural difference: at CAUTION the architecture has **G = 1 and A<sub>AI</sub> ≠ ∅**, whereas a withdrawal would be **G = 0 and A<sub>AI</sub> = ∅**. Those are different points in the (G, A<sub>AI</sub>) space, and the architecture distinguishes them.

### F.3 Does Δ<sub>L2</sub> measure both? **No — it measures one, and only its operational frequency.**

Δ<sub>L2</sub> is a function of A<sub>AI</sub> alone. `G` is never computed in the metric path. The comparator construction does encode the participation/scope distinction **at the configuration level** — C1 is participation-only, C2 adds scope contraction, and their difference isolates the Level-2 increment — so Δ<sub>L2</sub> is correctly described as *the incremental effect of adding Level 2*. What it cannot do is report *which* Level-2 mapping produced that increment.

**The honest formulation:** Δ<sub>L2</sub> measures the **operational frequency** of the Level-2 increment under the evaluated C2 mapping. It does not measure the **character** of that increment. The architecture supplies the character (via G and Corollary C.2); the metric reports the frequency. That division of labour is coherent — it is simply not stated in the manuscript.

---

## G. What Δ<sub>L2</sub> Measures

| # | Candidate interpretation | Classification | Reasoning |
|---|---|---|---|
| **1** | Frequency of CAUTION-state occupancy | **MATHEMATICALLY ESTABLISHED** | Derived in §D from the mappings alone: Δ<sub>L2</sub> = p<sub>C</sub>. Requires only that C1 and C2 agree at SAFE and UNSAFE and differ at CAUTION — true for every configuration in the evaluated family. The manuscript states this identity and correctly labels it *"a metric-interpretation identity, not a result."* |
| **2** | Frequency of incremental configuration disagreement attributable to the CAUTION-specific mapping | **MATHEMATICALLY ESTABLISHED** | This is the most precise description available, and the only one that is exactly what the implementation computes (`condition_comparison.py:198`, set inequality over per-hour admissible sets). |
| **3** | Frequency of **active** intermediate advisory restriction | **TRUE ONLY UNDER THE CANONICAL CONFIGURATION** | True of the evaluated architecture, because Corollary C.2 forces A<sub>AI</sub>(CAUTION) ≠ ∅ and C.3 gives G(CAUTION) = 1. **Not** a property the metric verifies: Case B returns the identical value. The word "active" is carried by the architecture, not by Δ<sub>L2</sub>. |
| **4** | Magnitude of recommendation-set contraction | **FALSE** | A per-hour binary indicator has no magnitude. Cases A, C and D have contraction magnitudes of 2, 3 and 2 elements respectively and identical Δ<sub>L2</sub>. **The manuscript already states this correctly**: *"Δ<sub>L2</sub> measures how often the intermediate restriction binds, not how much the recommendation set contracts."* No correction needed. |
| **5** | Degree of AI participation | **NOT ESTABLISHED** | Δ<sub>L2</sub> is computed from A<sub>AI</sub> without reference to G. Since Δ<sub>L2</sub> = p<sub>C</sub> and G(CAUTION) = 1, it happens to count hours in which participation is permitted — but it measures the frequency of a *state*, not any property of participation, and it would return the same value if participation were withdrawn at that state. |
| **6** | Improvement in safety | **FALSE** | No incident or outcome record exists for the site. The manuscript says so repeatedly and makes no such claim. |
| **7** | Improvement in decision quality | **FALSE** | No generated advice is evaluated; the metric ranges over admissible recommendation *types*, not over recommendation content. The manuscript says so explicitly. |

**On binary indicators and magnitude.** A per-hour indicator `1[A ≠ B]` is invariant under any relabelling of the sets that preserves inequality. Measuring contraction magnitude would require a graded functional — |A \ B|, |A|/|B|, or similar — aggregated over hours. Δ<sub>L2</sub> is not such a functional and the manuscript does not present it as one.

---

## H. Implementation Verification

| Question | Finding | Location |
|---|---|---|
| Does the code compare exact admissible sets? | **Yes.** `frozenset` objects per hour per configuration | `condition_comparison.py:85–87, 169–171` |
| Set inequality or strict subset? | **Set inequality**: `if x != y` | line 198 |
| State labels or recommendation sets? | **Recommendation sets.** States are classified once, then mapped through `A_AI[cond]` | lines 169–171 |
| Binary participation flags? | **No.** `G` never enters the metric path — it appears only in docstring prose (lines 9, 14) | searched |
| Cardinality? | **No.** Never computed | searched |
| Hard-coded state→disagreement mapping? | **No.** Disagreement is computed from the sets, not tabulated | line 198 |
| Does the implementation match the formal definition? | **Matches the implemented semantics exactly.** It does **not** match the manuscript's prose definition ("strictly smaller"), though the two coincide for all evaluated configurations because every admissible set ⊆ R | §C.2 item 2 |
| **Do 5.81% and 4.48% depend on the contents of {Go, Delay}?** | **No — only on its difference from FULL.** Substituting any `frozenset` other than `FULL` leaves every `x != y` evaluation unchanged, so the counts, the state distribution and both percentages are identical. This is a property of the code, established by inspection; no re-run was performed. | lines 169–171, 198 |

---

## I. Impact on Novelty and Research Contribution

| Aspect | Impact | Reasoning |
|---|---|---|
| **A. The architecture's ability to express graduated governance** | **None.** | Graduation rests on the strict chain A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ (C.4, Corollary C.2) and on CAUTION being reachable — both hold. `appendix-c:418–422` states this explicitly. A metric's blindness is not an architectural deficiency. |
| **B. The mathematical correctness of Δ<sub>L2</sub>** | **None.** | The identity is derived correctly, holds exactly, and matches the stored artefact to the hour. The manuscript correctly labels it an interpretation identity rather than a result. |
| **C. The empirical validity of the reported frequencies** | **None.** | 5.81% / 4.48% and the underlying counts (531 / 266) are unaffected — they are properties of the classifier and the record, not of A<sub>AI</sub>(CAUTION)'s content. |
| **D. The interpretation of Δ<sub>L2</sub>** | **Narrow effect — this is where M-2 lands.** | "Frequency of active intermediate restriction" is true of the evaluated configuration but is not what the metric verifies. The precise reading is interpretation 2. The manuscript is already close; it needs the non-emptiness condition. |
| **E. The overall novelty claim** | **None.** | The claimed contribution is a measurement assembly — criterion, comparator, deterministic replay, sensitivity and attribution. Δ<sub>L2</sub>'s content-independence is a *property of the assembly that the manuscript itself reports*, not a flaw in it. The paper explicitly disclaims mechanism novelty. |
| **F. The research gap on operationalisation and empirical characterisation** | **None.** | The gap concerns whether anyone has *measured* how often an intermediate scope restriction binds. Whether the measuring instrument also discriminates restriction type is a separate question that the gap statement does not raise and the paper does not answer. |

**On the false dichotomy.** M-2 does not force a choice between "Δ<sub>L2</sub> measures everything" and "the contribution is invalid". The metric measures one thing precisely; the architecture supplies what the metric does not; and the manuscript needs to say which is which in one clause.

---

## J. Assessment of Auditor M-2

| Auditor claim | Verdict | Evidence |
|---|---|---|
| The metric treats any strict subset of FULL as a restriction | **CONFIRMED** | `condition_comparison.py:198`; §D, §E |
| ∅ is also a strict subset of FULL | **CONFIRMED** | Trivially true |
| Replacing {Go, Delay} with ∅ produces the same result | **CONFIRMED** | §E Case B; follows from set inequality |
| Δ<sub>L2</sub> therefore cannot distinguish active participation with a narrowed set from complete withdrawal | **CONFIRMED as a statement about the metric** | §F.3 |
| …and this undermines the manuscript's interpretation of Δ<sub>L2</sub> as a measure of intermediate advisory restriction | **PARTIALLY CONFIRMED** | The manuscript's actual wording — *"measures how often the intermediate restriction binds, not how much the recommendation set contracts"* — is already correct. Only the invariance condition is too permissive. |
| **(Implied) the metric cannot see the property the paper's positioning turns on, so the positioning is undercut** | **NOT SUPPORTED** | The architecture separates participation (C.3, G) from scope (C.4, A<sub>AI</sub>) as its named contribution (line 1178). The positioning rests on the architecture, which does make the distinction, not on the metric, which does not claim to. **This was the error in my audit.** |
| **(Implied) a non-empty-subset requirement is missing** | **PARTIALLY CONFIRMED — and more precisely located than the auditor stated** | Corollary C.2 already requires ∅ ⊊ A<sub>AI</sub>(CAUTION), so the requirement exists as a **theorem**. What is genuinely missing is a **constraint**: C.6 bounds A<sub>AI</sub>(CAUTION) from above only, so Case B satisfies every stated constraint while violating the corollary. The manuscript inherits the weaker half. |

**Finding the auditor did not identify:** Table I's footnote *"G is determined by emptiness of A_AI"* contradicts C.3, which defines G on the state. The dependency runs the other way: G is primitive, and A<sub>AI</sub>(UNSAFE) = ∅ is forced by C.6's Participation Constraint. `G` is also never defined in the manuscript body. Since G is precisely the apparatus that distinguishes participation from scope, defining it correctly is most of the answer to M-2.

---

## K. Recommended Manuscript Action

| Option | Scientifically correct? | Reviewer risk | Impact on contribution | Impact on results | Page cost |
|---|---|---|---|---|---|
| **1. No change** | Incomplete — the invariance condition admits a configuration the architecture excludes, and Table I misdefines G | **Moderate.** A formal-methods reviewer will make exactly the auditor's observation, and the paper has no sentence to point at | None | None | 0 |
| **2. Clarify the configuration** (non-empty strict subset) | Necessary, not sufficient — leaves G misdefined | Low | None | None | ~6 words |
| **3. Narrow the interpretation** | Largely redundant — §III already says Δ<sub>L2</sub> measures frequency, not magnitude | Low | None | None | ~8 words |
| **4. Add a participation indicator** | **Not required.** G already exists in the architecture and in Table I. A *metric* distinguishing B from A would answer a question the paper does not ask | Low, but invites "why is this here?" | **Dilutes** — adds a second measurement to a paper whose contribution is one measurement assembly | None | ~80–120 words + a table row |
| **5. Redesign Δ<sub>L2</sub>** | **Wrong.** Would abandon the identity Δ<sub>L2</sub> ≡ P(CAUTION), which is the paper's analytical anchor, to answer a question outside RQ1 | High — invalidates the comparator construction | **Destroys** the contribution | **All figures change** | Rewrite |
| **6. Combined minimal correction** — state the full containment chain, fix Table I's G footnote | **Correct and complete** | **Lowest** — pre-empts the objection in the reader's own terms | None; strengthens the §II positioning against [9] by making "active" formally grounded | None | **~15 words** |

### Recommendation: **Option 6.**

Options 4 and 5 should be **rejected**, and the reasoning matters. The auditor's remedy (require a non-empty strict subset) addresses the **evaluated configuration**; it does not and cannot make Δ<sub>L2</sub> *intrinsically* capable of discriminating Case B, because a binary set-inequality indicator never can. Those are different things, and conflating them is what would lead a well-meaning author to add a metric they do not need. The right response is to **state the architectural constraint that excludes Case B**, not to rebuild the instrument so it can detect a configuration the architecture forbids.

Answering the task's sub-questions directly:

- **(A) Does requiring A<sub>AI</sub>(CAUTION) ≠ ∅ guarantee the architecture retains active participation at CAUTION?** **Yes** — combined with C.3's G(CAUTION) = 1, which is independent of A<sub>AI</sub>. Together they are exactly "gate open and something admissible".
- **(B) Does it make Δ<sub>L2</sub> intrinsically capable of distinguishing non-empty contraction from withdrawal?** **No.** It restricts the domain so that the undistinguished case does not arise; the metric is unchanged.
- **(C) Would an explicit participation indicator be required to distinguish them mathematically?** **Yes** — and it already exists as G(S). Reporting it as a *measurement* would mean computing something like P(G = 1 ∧ A<sub>AI</sub> ⊊ FULL), which is p<sub>C</sub> again under the canonical architecture. It would carry no new information.
- **(D) Is such a metric necessary for RQ1?** **No.** RQ1 asks *how often* an intermediate advisory-scope level changes the admissible set relative to a participation-only gate. Δ<sub>L2</sub> answers exactly that.
- **(E) Would adding one over-expand a six-page paper?** **Yes** — roughly 100 words plus a table row, to report a quantity identical to one already reported.

---

## L. Exact Proposed Text Changes

### L.1 §III — the invariance sentence *(required)*

**Original:**

> "One is that the value of ΔL2 is invariant to the content of AAI(CAUTION), provided that set remains a strict subset of FULL: replacing one strict subset with another leaves the binding frequency unchanged when the state classification is unchanged."

**Minimal replacement:**

> "One is that the value of ΔL2 is invariant to the content of AAI(CAUTION), provided that set remains a **non-empty** strict subset of FULL: replacing one such subset with another leaves the binding frequency unchanged when the state classification is unchanged. **Non-emptiness is what separates an active contraction from a withdrawal of participation; the metric does not distinguish the two, and the contract in Table I supplies it.**"

**Justification.** The added word closes the gap the auditor identified. The added sentence does the more important work: it tells the reader where the distinction lives, converting a latent objection into a stated design property. Cost: 1 word + 24 words. If space is tight, the word "non-empty" alone is the minimum defensible change.

### L.2 Table I note — the G footnote *(required)*

**Original:**

> "G is determined by emptiness of AAI and is shown for readability only."

**Minimal replacement:**

> "G is the participation gate: G = 1 where AI advisory participation is admissible, 0 where it is withdrawn. The contract is strict at both ends: ∅ ⊊ AAI(CAUTION) ⊊ FULL."

**Justification.** Three defects fixed in one note. G is defined, so it is no longer an undefined symbol in a table (which my pre-submission audit flagged separately as N-1). The dependency is stated correctly — G is primitive, not derived from emptiness. And the strict chain appears in the paper, which is what formally excludes Case B. Net change: +14 words. This note is where the fix belongs, because Table I is the contract.

### L.3 Not recommended

- **§II's "active intermediate scope contraction"** — no change. With L.1 and L.2 in place, "active" is grounded in the stated contract.
- **§III's "Δ<sub>L2</sub> measures how often the intermediate restriction binds, not how much the recommendation set contracts"** — **no change required.** This sentence is already exactly right and is the paper's best defence against interpretation 4.
- **§I's "the frequency with which the active contraction binds"** — no change. It describes the evaluated configuration, which is active by contract.
- **The Δ definition's "strictly smaller" wording** — out of scope for M-2. Noted in §M as a separate, pre-existing imprecision.

### L.4 Numerical results

**None change.** No threshold, count, percentage, envelope or table entry is affected.

---

## M. Unresolved Questions

1. **C.6 bounds A<sub>AI</sub>(CAUTION) from above but not from below.** Non-emptiness is a corollary of the canonical instantiation (Corollary C.2), not a constraint on admissible instantiations. A configuration with A<sub>AI</sub>(CAUTION) = ∅ satisfies both stated C.6 constraints. *This is a gap in the appendix, not in the conference paper*, and the manuscript changes above make the paper correct regardless. Suggested for the thesis, not for AAI 2026: extend the Advisory Restriction Constraint to `A_AI(UNSAFE) ⊊ A_AI(CAUTION) ⊊ A_AI(SAFE)`.

2. **The manuscript's Δ definition ("one configuration admits a strictly smaller set than another") is not the implemented one (set inequality).** They coincide for all four configurations because every admissible set ⊆ R, so nothing in the reported results depends on it. Case F in §E is the only configuration that separates them, and C.4 excludes it. Pre-existing imprecision, outside M-2's remit.

3. **Case D remains formally admissible but arguably contrary to intent.** A<sub>AI</sub>(CAUTION) = {DepartureTime, Duration} satisfies every constraint yet inverts C.4's stated rationale, which is that CAUTION withholds *timing and duration* guidance specifically. Nothing in the formalisation encodes *which* elements the intermediate state should retain. Not a defect for this paper — Δ<sub>L2</sub> is invariant to it either way, and the manuscript already declares A<sub>AI</sub>(CAUTION) researcher-defined and unvalidated.

4. **Whether a reviewer will want the discrimination the metric lacks.** I judge not: RQ1 asks for a frequency and Δ<sub>L2</sub> supplies it. But this is a prediction about reviewers, not a mathematical result.

---

## N. Final Verdict

> ## MINOR CLARIFICATION REQUIRED

One word and one sentence in §III; a rewritten Table I footnote. **About 15 words net.** No numerical result, metric definition or experimental figure changes, and **no new metric should be added**.

**The core of M-2 as I originally wrote it does not stand.** The architecture separates participation from advisory scope explicitly and names that separation as its contribution; the non-emptiness condition I proposed as a remedy already exists as Corollary C.2; and the manuscript makes no claim that Δ<sub>L2</sub> discriminates what it cannot. What remains is a genuine but small defect — the manuscript carries the upper half of a containment chain whose lower half does the work, and defines its participation gate backwards in a table footnote. Both are fixed by importing what the canonical appendix already proves.
