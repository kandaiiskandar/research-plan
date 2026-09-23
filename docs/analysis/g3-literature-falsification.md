# G3 Adversarial Falsification Against the Existing Literature Collection

**Date:** 2026-09-21
**Task:** Attempt to falsify G3 — "explicit observation-quality and exclusion semantics" — using only sources already held in this repository.
**Posture:** Adversarial. Every held source treated as a potential counterexample.
**Report status:** `experiment-report-delta-l2.md` **UNCHANGED**.

---

## A. G3 definition under test

| Sub-property | Claim being tested |
|---|---|
| **G3.1 Invalid** | Observation explicitly represented as invalid, with a defined consequence |
| **G3.2 Missing** | Absent observation distinguished from a valid one |
| **G3.3 Stale** | Observation *age* reasoned about explicitly (distinct from model/certification staleness and concept drift) |
| **G3.4 Structurally unmeasured** | A conceptually required variable, unavailable in deployment, **declared excluded**, with a formal consequence for interpreting results |
| **G3.5 Resolution / fidelity** | Spatial/temporal resolution or measurement fidelity explicitly reasoned about |
| **G3.6 Fail-safe resolution** | Unusable observation automatically resolves toward the safer state |
| **G3.7 Explicit unknown** | UNKNOWN distinguished from SAFE rather than collapsed into it |
| **G3.8 Propagation into governance** | Observation-quality state actually changes participation, scope, or admissibility downstream |

---

## B. Search coverage

| Item | Count |
|---|---|
| PDFs extracted to text | **120** (all repository PDFs, `papers/`, `papers/sources/`, `papers/scopus/`, `papers/books/`, root) |
| Extraction notes included | **118** (`notes/*.md`) |
| Total documents searched | **238** |
| Search terms | 8 dimension groups, ~45 regex patterns: invalid, validity, implausible, out-of-range, reasonableness check, data integrity, missing, absent, unavailable, incomplete observation, stale, freshness, timestamp, timeout, latency, expired, data age, excluded, unmeasured, spatial/temporal resolution, fidelity, measurement uncertainty, sensor precision, coarse, fail-safe, fail-closed, fail-operational, conservative fallback, safe default, worst-case, degraded mode, pessimistic, unknown, indeterminate, insufficient evidence, sensor fault/failure, fault detection, fault tolerance, redundancy, partial observability, sensor fusion |
| Documents matching ≥4 of 8 dimensions | **39** |
| Documents opened and read in context | **9** |
| Documents coded in the matrix | **7** |

Method: whitespace-normalised full text, ±100-character context windows around every match, manual inspection of surrounding sections. Absence claims below rest on this sweep, not on the extraction notes.

---

## C. G3 evidence matrix

| Source | Invalid | Missing | Stale | Excluded/unmeasured | Resolution | Fail-safe | Explicit unknown | Propagates into governance? | Precedent strength |
|---|---|---|---|---|---|---|---|---|---|
| **"The Controllability Trap" — AMAGF, military AI agents** | PARTIAL | **YES** | **YES** — Synchronisation Freshness **SF(t) = t − t_last**, Eq. (5); metric n5 "normalised time since last sync" (Tbl 3) | NO | NO | **YES** — "control quality equals its weakest dimension"; graduated bands contract to "Safe State: predefined safe behaviour; no autonomous actions" (Tbl 4) | PARTIAL | **YES — decisively.** "If a checkpoint is missed or unconfirmed, the agent **enters reduced autonomy mode (reversible actions only)** until synchronisation is restored" | **DIRECT PRECEDENT** for G3.2/3.3/3.6/3.8 |
| **Gyllenhammar et al. (2025) — Road to Safe ADS** | **YES** — "If one configuration is found to be invalid… [Dynamic Safety Management]" | PARTIAL | NO | PARTIAL — ODD is a declared operating envelope | PARTIAL | **YES** — "three fault-tolerance regimes: **fail-operational, fail-degraded and fail-safe**"; "mitigated through a fail-safe state, i.e. by transitioning to a **Minimal Risk Condition (MRC)**" | PARTIAL | **YES.** "run-time monitoring of appropriate triggering conditions for avoiding exiting the ODD"; ODD exit → MRC | **DIRECT PRECEDENT** for G3.1/3.6/3.8 |
| **FAA AC 20-151C (TCAS II)** | **YES** — validity indication required, §§2.3.6.1, 2.3.6.2.6 | PARTIAL | NO — no latency/stale requirement | NO | NO | **NO** — §2.3.5 concedes continued operation without inhibits; "may command maneuvers that may significantly reduce stall margins" | NO | **NO** — validity is annunciated, not propagated into inhibition | **PARTIAL PRECEDENT** (G3.1 only) |
| **Bloomfield & Rushby (2025) — Dependability** | PARTIAL | **YES** — Error→Failure transitions on "unsuccessful or missing fault tolerance" | NO | NO | NO | PARTIAL — Safe/Unsafe failure partition | **YES** — indeterminacy vs epistemicism; known vs unknown unknowns | PARTIAL — conceptual framework, not a runtime mechanism | **SUPPORTING CONCEPT** |
| **Baxi (2026) — CGAE** | NO | NO | **NO for observations** — temporal decay δ(Δt) applies to *certification* staleness | NO | NO | PARTIAL — decay lowers tier | NO | Certification staleness → tier demotion, not observation quality | **SUPPORTING CONCEPT** |
| **Flehmig et al. (2024)** | NO | NO | NO — "degradation" = concept drift, data drift, outliers, adversarial input | NO | NO | PARTIAL — backup at red | NO | Model degradation → supervisory switching | **NOT RELEVANT to G3** |
| **Könighofer et al. (2025) — Shields** | NO | NO | NO | NO | NO | PARTIAL — fallback outside winning region | NO | "Partial observability" appears only in cited titles | **NOT RELEVANT to G3** |

---

## D. Strongest counterexamples

### 1. "The Controllability Trap" (AMAGF) — the most damaging

**What it already does.** A governance framework built on a six-component Control Quality Score aggregated by an explicitly stated **weakest-link** rule — "control quality equals its weakest dimension" — structurally identical to max-severity aggregation over `gᵢ`. One component (n5) is a **formal observation-freshness metric**, SF(t) = t − t_last. A missed or unconfirmed checkpoint **automatically reduces the agent's admissible action set** to reversible actions only. Graduated response bands (Table 4) contract the action set monotonically down to "Safe State: predefined safe behaviour; no autonomous actions." The paper's framing argument is that governance "must move from a binary conception of control to a continuous model" — the same move this project makes.

**What remains different.** Governed object is an autonomous military agent's own actions, not recommendation categories presented to a human decision-maker. The conditioning variables are operator–agent epistemic alignment and synchronisation state — relational and partly AI-internal, not an external environmental classification. Freshness is *synchronisation* freshness, not *environmental observation* freshness. No declared-exclusion set, and no four-way semantic distinction.

### 2. Gyllenhammar et al. (2025) — already one of this project's 18 primary comparators

**What it already does.** Establishes the ODD/MRC pattern: a declared operating envelope, **runtime monitoring of triggering conditions to avoid exiting it**, and fail-operational / fail-degraded / fail-safe regimes with transition to a Minimal Risk Condition on exit. Invalid runtime configurations are explicitly handled under Dynamic Safety Management. This is external-environment-conditioned, classified (in/out of ODD), runtime, and propagates into system behaviour.

**What remains different.** ADS is autonomous control; MRC is a vehicle manoeuvre, not a restriction on advisory categories offered to a human. "Fail-degraded" is a system *capability* regime, not an admissible-recommendation-type set. This source sits in the project's own coding table and was **not** previously recognised as an observation-quality precedent.

### 3. FAA AC 20-151C — a counterexample in the project's favour

TCAS requires validity indication for pressure and radio altitude but mandates **no** conservative consequence; §2.3.5 concedes the system continues without inhibits and may command manoeuvres reducing stall margins. Detection without propagation. This strengthens rather than threatens G3.8.

---

## E. Verdicts on the four formulations

| | Formulation | Verdict |
|---|---|---|
| **G3-A** | Prior work does not explicitly handle observation-quality problems | **FALSIFIED.** Validity flags (TCAS), invalid-configuration handling (ADS/DSM), missing-checkpoint handling (AMAGF), missing fault tolerance (Bloomfield & Rushby) |
| **G3-B** | Prior work does not propagate observation-quality state into runtime governance | **FALSIFIED.** AMAGF: missed/unconfirmed checkpoint → reduced autonomy mode, reversible actions only. ADS: ODD exit → MRC. Both propagate an observation-quality condition into a contracted admissible action set |
| **G3-C** | Prior work does not distinguish invalid, absent, stale and structurally unmeasured as four different semantic conditions | **PARTIALLY SURVIVES.** No source in the 238 searched treats all four as distinct semantic conditions with separate consequences. AMAGF has freshness and missingness but not invalidity or structural unmeasurement; ADS has invalidity and envelope exit but no staleness semantics. **However, no source was found attempting and failing to make the distinction** — the absence may reflect that the distinction is not load-bearing elsewhere rather than that it is novel |
| **G3-D** | No mechanism combines heterogeneous external environmental observations, differentiated observation-quality semantics, declared exclusions, fail-safe resolution, and propagation into the admissible recommendation scope of a **human-facing decision-support** system | **SURVIVES AS A COMBINATION GAP**, within the reviewed sources. Every component is individually established. The conjunction was not identified. The load is carried by two elements only: the **human-facing advisory** governed object and the **declared exclusion with epistemic consequence** |

---

## F. Smallest surviving difference

After conceding every precedent above:

> Within the reviewed sources, observation-quality conditions are propagated into the admissible **action** set of an autonomous agent (AMAGF) or into the operating mode of an autonomous vehicle (ODD/MRC). No reviewed source propagates them into the admissible set of **recommendation categories presented to a human decision-maker who retains final authority**; and none declares a structurally unmeasured variable as an explicit exclusion whose consequence is that every reported severity figure is a **lower bound**.

Two elements, not eight. The declared-exclusion-with-epistemic-consequence (G3.4) is the only sub-property with no partial precedent anywhere in the 238 documents searched — a corpus-wide regex for exclusion-linked lower-bound reasoning returned zero hits.

---

## G. Computer-science significance

| Element | Classification | Reasoning |
|---|---|---|
| Validity/missing/stale checking | **Ordinary engineering practice** | Timestamp checks and null rejection are implementation hygiene |
| Fail-safe resolution `gᵢ(⊥) = UNSAFE` | **Established** — not a contribution | Fail-safe/fail-degraded regimes are standard in ADS and AMAGF |
| Four-way semantic differentiation | **Formalisation contribution, modest** | Defensible only if the four conditions demonstrably produce *different* governance outcomes. Currently untested |
| **Totality over the observation space** (Theorem C.1b — classification total over `Obsᵢ`, not just ideal domains) | **Formalisation contribution** | This is the genuinely research-level element: a proved totality property over incomplete observation spaces, with Safety Dominance holding for fault-driven UNSAFE. Not found in the reviewed sources |
| **Declared exclusion with epistemic consequence** (`D = {m}` ⇒ lower bounds) | **Formalisation + methodological contribution** | Connects an architectural exclusion to the interpretation of empirical results. Zero corpus hits |
| Human-facing advisory as governed object under observation-quality conditions | **Runtime-governance contribution** | Established for agent actions, not for human-facing recommendation categories |

**Overall: formalisation contribution, narrow but real** — specifically totality over the observation space plus the exclusion/lower-bound coupling. **Not** an architecture contribution, and **not** the fail-safe mechanism itself.

---

## H. Evidence alignment

| Surviving element | Status |
|---|---|
| Four-way semantic differentiation | **CURRENT EXPERIMENT DOES NOT TEST IT.** `D = {m}` is constant; no hour varies validity, presence or age |
| Totality over the observation space | **CURRENT EXPERIMENT DOES NOT TEST IT.** Proved, not measured. The replay never exercises ⊥ except structurally via exclusion |
| Declared exclusion ⇒ lower bounds | **PARTIALLY SUPPORTED.** The lower-bound status is stated and follows from `g_m` monotonicity, but no run varies `D` to quantify the bound's width |
| Human-facing governed object | **CURRENT EXPERIMENT DOES NOT TEST IT.** Admissible-set level only; no human subjects |
| Level 2 activation frequency (Δ_L2) | **SUPPORTED** — but this evidences the *conceded* gate, not G3 |

The alignment problem identified in the verification audit is confirmed and sharpened: **nothing in G3 that survives falsification is evaluated by the current experiment.**

---

## I. Minimum additional experiment, if G3 is retained

Not implemented. The minimum credible test is a **fault-injection replay** over the existing 43,848-hour record, adding conditions that vary observation quality while holding thresholds fixed:

1. **Exclusion sweep.** Re-run with `D = {}`, `D = {m}`, `D = {m, w}`. Report how the Level-2 binding rate and the UNSAFE rate move. This directly quantifies the lower-bound width that is currently asserted but unmeasured.
2. **Staleness injection.** Apply a freshness bound `ageᵢ` (currently unspecified — see `open-decisions.csv` OPEN-B1-1) and re-run with synthetic gaps. Measures whether staleness produces governance outcomes distinct from absence.
3. **Invalidity injection.** Force out-of-range values at a controlled rate; verify fail-safe resolution and measure divergence from the clean trace.

Test 1 is the cheapest and the most defensible — it uses only existing data and existing code paths, and it converts an asserted property into a measured one. It does **not** require `ageᵢ` to be invented, which tests 2 and 3 do, and inventing it would repeat the 7.5 mm/hr error the project already corrected.

---

## J. External search required

The repository does **not** adequately cover the literature most likely to contain further G3 precedents. A later external search should target:

1. **Fault-tolerant sensor fusion** — validity, staleness and fusion-confidence semantics. The corpus holds one maritime fusion review whose text extraction yielded nothing usable.
2. **Fail-operational and fail-degraded architectures** — reached only through Gyllenhammar's secondary citations (Schneider & Trapp; Kapinski et al.; Warg et al. on MRC). These primaries are not held.
3. **Runtime assurance / Simplex architectures under missing observations** — partially covered via Flehmig's adjusted simplex, not directly.
4. **Data-quality-aware and uncertainty-aware environmental decision support** — the closest domain analogue, absent from the corpus.
5. **Belief-state / POMDP treatments of unknown-vs-unsafe** — G3.7 is essentially untested; partial observability appears in the corpus only in reference titles.

Areas 1 and 2 are the highest risk to the surviving claim.

---

## K. Final decision

> ## **G3 SURVIVES ONLY IN NARROWED FORM**

G3 as stated in the verification audit — "observation-resolution and exclusion semantics, not identified in verified sources" — is **falsified in its broad and operational forms** by two sources already in this repository. The Controllability Trap's AMAGF framework propagates a formal observation-freshness metric, SF(t) = t − t_last, into a graduated contraction of an agent's admissible action set, aggregating by an explicitly weakest-link rule and terminating in a predefined safe state. Gyllenhammar et al. — already one of this project's own eighteen primary comparators — establishes ODD-exit monitoring with fail-operational, fail-degraded and fail-safe regimes transitioning to a Minimal Risk Condition. Neither was previously recognised as an observation-quality precedent, and between them they establish G3.1, G3.2, G3.3, G3.6 and G3.8.

What survives is two elements. First, the governed object: every propagation precedent found governs an **autonomous agent's actions or an autonomous vehicle's operating mode**, never the set of recommendation categories offered to a human who decides. Second, the declared exclusion with an epistemic consequence — `D = {m}` entailing that reported severity figures are lower bounds — for which a corpus-wide search returned no hits. The associated formal property, totality of classification over the observation space rather than over ideal domains, is the most defensible research-level element and was not found in the reviewed sources.

This is a **combination gap**, and a narrow one. It should not be described as observation-quality semantics being absent from prior work, because that claim is now demonstrably false against this project's own library. It should be described as the transfer of an established fail-safe observation-governance pattern from autonomous action domains to human-facing advisory-scope governance, formalised with totality over incomplete observations and coupled to an explicit exclusion contract. Whether that is sufficient for a doctoral CS contribution is a supervisor judgement, not one this audit can settle — and it is sharpened by the fact that **none of the surviving elements is evaluated by the current experiment**.
