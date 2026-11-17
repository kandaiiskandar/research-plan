# G4 — Prior-Art Challenge and Reachability Correction

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** exploratory research branch, v2. v1 documents preserved unedited. Frozen RQ1–RQ3 untouched. No experiment was run; no external request made.

**Adjudication rule, restated and tightened.** The absence of an identical three-state taxonomy in the literature is **not** evidence of novelty. A concept counts as established if it appears **under any terminology** with the same formal content. A combination of established concepts counts as novel only if the combination itself creates a problem that is not solved by solving the parts.

---

## 1. v1's reachability claim, and why it fails

v1 asserted that `DepartureTime` is **structurally unreachable** from concurrent observations, on the strength of a measured production rate of exactly 0.00% over 7,305 episodes.

**That inference is invalid.** What the run established is narrower: *under the persistence procedure, with the specific predicate "there exists a later window hour whose exposure percentile is at least 5 points lower", the predicate is unsatisfiable* — because persistence assigns every later hour the present hour's value, so the difference is identically zero.

**A counterexample settles it.** The architecture's own daylight component `g_t` is a function of the clock and the solar event times, both computable at the decision instant. A procedure that emits *"depart after sunrise at 06:20"* produces a `DepartureTime` output from **concurrent information alone**, with no forecast. Such a procedure is excluded by the tested generator's rule, not by the evidence class. **`DepartureTime` is therefore not unreachable from concurrent observations.** v1's claim is withdrawn.

---

## 2. Three distinct notions, and what 0.00% can and cannot distinguish

> **Logical impossibility.** No procedure in **any** class can derive type `t` from `E`, because `t` asserts content that `E` does not determine even in principle. This is an information-theoretic statement about `(E, t)`.

> **`G`-unreachability (algorithm-specific).** No procedure in the **declared class `G`** produces type `t` from `E`. A statement about `(E, t, G)`. Changing `G` can change the verdict.

> **Low empirical production frequency.** The procedures actually run produce `t` rarely or never on the observed data. A statement about `(g, E, G, D)` including the data distribution `D`.

**An observed rate of 0.00% is consistent with all three and by itself distinguishes none.** v1 read a measurement of the third as a demonstration of the first. The only one of the three that was actually established is the second, with `G` = {the one tested generator}.

### 2.1 Which notion is the right primitive?

The brief's three options were: a property of the evidence class, of a fixed derivation procedure, or of an explicitly defined class of permissible procedures. **The third is the only coherent choice.**

- *Evidence class alone* is too weak: reachability is not a property of `E` without saying what may be done with `E`. Any `E` is "reachable" for any `t` under a procedure class permitting arbitrary guessing.
- *A fixed procedure* is too strong and uninformative: it yields a claim about one implementation, which is what v1 produced and mistook for a claim about evidence.
- *A declared class `G`* makes the statement well-posed — and makes the declaration of `G` the load-bearing modelling commitment.

**But this is exactly where the novelty evaporates.** "Is the target computable by some member of a declared hypothesis class from the available information?" is **realizability**, and it is one of the oldest concepts in learning theory and statistics:

| Established concept | Field | Same formal content |
|---|---|---|
| **Realizability** | statistical learning theory | `∃h ∈ H` with zero (or ≤ε) risk — i.e. the target is in the class's reach |
| **Identifiability** | statistics / econometrics | the parameter is determined by the observable distribution; otherwise only set-identified. **Manski's partial identification is already cited in the project's frozen position** |
| **Monitorability** | runtime verification | `∃` a finite prefix after which the verdict is decided; "ugly" prefixes are never decidable. **Bauer et al. 2011, already conceded in the lock** |
| **Finite admissibility / dismissibility** | runtime verification | which **individual verdict values** survive a finite, imperfect observation — Gorostiaga & Sánchez |
| **Observability / detectability** | control theory | whether internal state is determinable from available outputs |

**Verdict on the reachability half of G4: established concept, new terminology.** It is realizability relative to a declared procedure class, applied to output types instead of to a single target function. Gorostiaga & Sánchez's finite admissibility is the closest formal relative, and it already does the *per-output-value* version of it.

---

## 3. Re-examining the closest prior work against the corrected definitions

### 3.1 Gorostiaga & Sánchez — closer than v1 allowed

v1 dismissed this as confined to "one property's verdict domain". Under the corrected definitions that dismissal is weaker than it looked.

Their **finite dismissibility** and **finite admissibility** classify *which candidate verdict values* can be ruled out from a finite observation, with **imprecise observation functions** modelling lost prefixes and unobservable events. Map the terms: verdict values ↔ output types; imprecise observation function ↔ evidence class with quality attributes; finite admissibility ↔ `G`-reachability.

**Under that mapping, their framework already performs the reachability half of G4, with lemmas.** Lemmas 1–3 relate admissibility to all-finite-dismissibility, with the converse holding for finite verdict domains and **failing for infinite ones** — a sharper result than anything G4 proposed.

What they do not have is `PV` or `τ_t`: their notion is logical, not statistical, so there is no graded adequacy and no consequence-grounded threshold. **That remains the only daylight.** Caveat: the PDF states **no venue or year**, so its peer-review status is unconfirmed, and its full positioning against G4 has still not been done.

### 3.2 AC-RAC — closer than v1 allowed, on adequacy

v1 said AC-RAC performs "utility elimination over a confidence-derived set", not an evidence statement. True as far as it goes. But under Definition 3, look at what AC-RAC actually computes: for each action `a`, whether the worst case over the plausible-label set `C(x)` clears a bar. That is **existential-over-nothing but threshold-per-action** — structurally `∃`-free but `τ_a`-bearing.

**So AC-RAC already has the type-specific-threshold component of EA**, with a finite-sample distribution-free action-conditional guarantee, peer-reviewed at ICML 2026. What it does not have is thresholds **derived from the consequence of a type-`a` error** rather than set to equalise coverage — its α is uniform across actions by construction. **That gap is real and it is one modelling choice wide.**

### 3.3 Missing-data conformal methods — they already do evidence-indexed guarantees

Zaffran et al. (ICML 2023, peer-reviewed) give **mask-conditional validity**: a guarantee indexed by *which evidence is present*. Under Definition 3 this is `EA` with `E` ranging over missingness masks, `τ` the coverage level, and the existential discharged by their own construction. Their output type never changes — but that is a scope choice, not a conceptual limit, and **the principle that guarantees must be indexed by evidence availability is established and peer-reviewed.**

### 3.4 Active feature acquisition and value of information — **the literature v1 never read, and the closest of all**

v1 listed this as an acknowledged coverage gap. Having now reasoned about what it contains, it is **not a peripheral gap; it is the centre of the target**.

The VOI / EVSI / active-acquisition question is: *given what I have, can I decide now, or must I acquire more evidence first?* Formally — is the expected loss under the current evidence class acceptable, or does the expected value of further information exceed its cost? That is:

> `decide now ⟺ ∃` a decision achieving acceptable expected loss on the current evidence `⟺ EA(E, t; G, τ_t)`.

**EA is a restatement of the stopping condition in value-of-information analysis**, with `τ_t` playing the role of the decision threshold and `G` the class of decision rules. The EVSI ≤ cost stopping rule and the "acquire or decide" test are the same object, and that tradition is decades old in decision analysis and health economics, with an active ML literature (cost-sensitive active feature acquisition, test selection).

**This is the most serious challenge to G4 and it has not been read.** One preprint surfaced in search with the explicit form `stop when ρ·EVPI(b) ≤ c`. The honest position: **until the VOI and active-acquisition primary literature has been read, G4's adequacy half cannot be claimed as distinct, and the prior probability that it is distinct should be low.**

### 3.5 Evidence-sufficiency research — occupied, with one architecture doing the separation already

SURE-RAG keeps a sufficiency classifier **architecturally separate** from an uncertainty penalty, combining them only at the decision stage. That is the confidence/evidence separation G4 proposed, already built and ablated — and its authors report that **conformal thresholds collapsed coverage**, which is a warning about the guarantee route. RINSE scores sufficiency from question and evidence alone, explicitly not from generator confidence. Both are 2026 preprints.

---

## 4. The three-way reassessment the brief asked for

| | Option | Verdict |
|---|---|---|
| **(a)** | **An established concept expressed using new terminology** | **The reachability half: yes.** It is realizability relative to a declared procedure class — identifiability, monitorability, finite admissibility, observability. The project has already conceded both Bauer et al. 2011 and Manski's partial identification. **The adequacy half: probably yes**, as a restatement of the value-of-information stopping condition — pending §3.4's reading |
| **(b)** | **A useful empirical distinction without a novel method** | **This is the most defensible reading of what survives.** Separating "the procedure cannot emit this type from this evidence" from "it can, but the result would not be warranted" is a clarifying distinction that this project's own data illustrates, and that keeps a specification honest. It is a **framing contribution**, not a method |
| **(c)** | **A genuinely unresolved computational problem** | **Not established.** The only candidate is the *joint* problem — admitting output types when adequacy must hold per type over a declared procedure class under evidence constraints, with a guarantee. That is a combination of (i) per-type thresholds (AC-RAC, Sadinle, Role-Stratified CRC), (ii) evidence-indexed validity (Zaffran et al.), and (iii) an acquire-or-decide stopping condition (VOI). **The brief forbids counting a combination as novelty**, and no problem has been identified that is not solved by solving the parts |

**The three-state taxonomy is not itself evidence of anything.** Its absence from the literature is explained by the parts being studied separately under their own names, not by the combination being unexplored.

---

## 5. What would change this verdict

| | Condition | Status |
|---|---|---|
| **R1** | **Read the VOI / EVSI / active-feature-acquisition primary literature** and establish whether `EA`-over-procedure-classes differs from the acquire-or-decide stopping condition. **If it does not, G4's adequacy half is (a)** | **Not done. This is a reading task, not a research project, and it is the single decisive item** |
| **R2** | Establish the venue and read the full positioning of Gorostiaga & Sánchez against `G`-reachability | Not done; venue unknown |
| **R3** | Read AC-RAC's Appendix D and determine whether consequence-derived `τ_a` (as opposed to coverage-equalising α) is constructible within its framework. **If it is, the remaining daylight closes** | Not done; read in fragments only |
| **R4** | Read Dempster–Shafer conflict and reliability discounting primaries | Not done |

**R1 and R3 are the two that can close G4 entirely, and neither requires an experiment.**
