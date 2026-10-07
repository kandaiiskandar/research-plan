# III. Governance Contract, Criterion and Metric

Measuring that combination requires the governed object to be stated explicitly. We take it to be *A*<sub>AI</sub>(*S*), the set of recommendation types admissible when the classified operating state is *S*. Each evaluated hour is assigned one of three states, SAFE, CAUTION or UNSAFE, and FULL denotes the unrestricted recommendation set {Go, Delay, DepartureTime, Duration}. Table I states the contract. The admissible sets contract monotonically across the three states by construction. Participation gating is the special case in which the admissible set is empty, and so requires no separate formalism here.

*A*<sub>AI</sub>(CAUTION) = {Go, Delay} is a researcher-defined design choice used to instantiate a strict intermediate contraction for the evaluation. It is not empirically validated, shown correct, shown optimal, or established as safer or more beneficial. As Section III-E makes explicit, the measurement reported in this paper does not validate it.

**TABLE I**
*Admissible recommendation set by safety state. FULL = {Go, Delay, DepartureTime, Duration}.*

| State | *G* | *A*<sub>AI</sub>(*S*) |
|---|---|---|
| SAFE | 1 | FULL |
| CAUTION | 1 | {Go, Delay} |
| UNSAFE | 0 | ∅ |

*G* is determined by emptiness of *A*<sub>AI</sub> and is shown for readability only. *A*<sub>AI</sub>(CAUTION) = {Go, Delay} is researcher-defined; it is not empirically validated, shown optimal, or established as safer.

Following the functional interpretation of levels set out above, we evaluate a declared state through the recommendation set it permits.

**Criterion.** A declared risk level changes governance behaviour only if it changes the admissible recommendation set. Two configurations that assign identical admissible sets at every state denote the same governance function, irrespective of how many states each declares.

This is an operational measurement rule rather than a result. It restates, for a declared state, the position already established in the levels-of-automation literature that a level is meaningful through the function allocation it changes [PARASURAMAN].

Table II defines four configurations over the same classifier. C0 applies no restriction. C1 gates participation alone. C2 is the evaluated intermediate-scope configuration. C3 declares three states without contracting scope at the intermediate one.

C1 and C2 are identical at SAFE and identical at UNSAFE, and differ only at CAUTION, where C1 admits FULL and C2 admits a strict subset of FULL. Any difference between them therefore arises exactly where the intermediate state contracts the admissible set, which supplies the isolation structure used below. Ablation across governance configurations is established practice [MILLER]; what it is used for here is the isolation of one declared level.

C1 and C3 assign identical admissible sets at every state. Under the criterion they denote the same governance function, and their pairwise difference is zero by construction. The replayed value reported later is an executable conformance check on the implementation rather than an empirical finding, and it is not evidence that three-state designs are ineffective.

**TABLE II**
*Four governance configurations. C1 and C3 assign identical admissible sets at every state and therefore denote the same governance function.*

| Configuration | *A*<sub>AI</sub>(SAFE) | *A*<sub>AI</sub>(CAUTION) | *A*<sub>AI</sub>(UNSAFE) |
|---|---|---|---|
| C0 Ungated | FULL | FULL | FULL |
| C1 Participation-only | FULL | FULL | ∅ |
| C2 Evaluated intermediate-scope | FULL | {Go, Delay} | ∅ |
| C3 Three-state topology | FULL | FULL | ∅ |

C3 ports the governance topology of [FLEHMIG] onto an environmental conditioning variable. [FLEHMIG] condition on AI degradation rather than environmental state. C3 is not a reproduction or evaluation of their system and does not imply that their framework is deficient.

Let *N*<sub>eval</sub> be the number of evaluated departure-window hours and *N*<sub>restricted</sub> the number of those hours in which one configuration admits a strictly smaller set than another. The difference rate between two configurations is

Δ = (*N*<sub>restricted</sub> / *N*<sub>eval</sub>) × 100%.

The isolated quantity is

Δ<sub>L2</sub> = (C0↔C2) − (C0↔C1).

Here C0↔C1 captures participation gating alone and C0↔C2 captures participation gating together with the intermediate contraction, so their difference isolates the increment associated with the intermediate level under this comparator construction. A direct C1↔C2 comparison is computed as an implementation cross-check.

The identity governing interpretation follows from the mappings rather than from the data. C1 and C2 agree at SAFE and at UNSAFE and differ at CAUTION, where C2 admits a strict subset of FULL. The two configurations therefore differ on exactly the CAUTION hours, so that

Δ<sub>L2</sub> ≡ *P*(*S* = CAUTION)

for the evaluated mappings. This is a metric-interpretation identity, not a result.

Two consequences follow. One is that the value of Δ<sub>L2</sub> is invariant to the content of *A*<sub>AI</sub>(CAUTION), provided that set remains a strict subset of FULL: replacing one strict subset with another leaves the binding frequency unchanged when the state classification is unchanged. The other is that Δ<sub>L2</sub> measures how often the intermediate restriction binds, not how much the recommendation set contracts. It does not indicate whether {Go, Delay} is correct or optimal, whether the restriction improves safety or decision quality, or whether human oversight is effective.

Because the identity holds, the CAUTION base rate yields the same number and the comparator ladder is not required to compute it. The ladder serves a different purpose. It separates participation gating from the intermediate contraction, it makes the isolation structure explicit, it establishes the identity rather than assuming it, and it supplies the cross-check noted above.

# IV. Evaluation Design

The replay covers one deployment site, Kota Kinabalu, Sabah, a low-resource coastal-fisheries setting, with a small-vessel baseline under 10 GRT.

Two environmental-data configurations are evaluated. The PRIMARY configuration covers January 2020 to December 2024, comprising 43,848 hourly records with wave data from ERA5-Ocean at approximately 50 km resolution, giving a departure-window denominator of 9,135 hours. The RESOLUTION configuration covers October 2021 to December 2024, comprising 28,501 hourly records with wave data from MFWAM at approximately 8 km resolution, giving a denominator of 5,935 hours. Records were retrieved through the Open-Meteo archive [OPEN-METEO], [ERA5].

The evaluation window is 05:00–09:00, which defines *N*<sub>eval</sub>. This window is an evaluation-policy choice rather than an observed departure period, and other denominators are defensible.

Each hour is assigned a state using the maximum severity among the available component classifications, covering wind, rainfall, marine warning, ocean state and time. Vessel class parameterises the ocean-state component rather than contributing an independent severity term.

Threshold provenance is separated from design choice. The wind boundary follows Malaysian Meteorological Department strong-wind criteria [MET-WIND], and the rainfall UNSAFE boundary follows the same department's thunderstorm criteria [MET-THUNDERSTORM]. The ocean-state boundary for the small-vessel class follows the operational ceiling reported by [YAAKOB], and the day boundary follows COLREGs Rule 20(b) [IMO-COLREG]. The rainfall CAUTION boundary is source-supported through the DID light-rainfall limit [DID-RAINFALL] but is not a Meteorological Department threshold, since no criterion is published below the thunderstorm level. Source provenance indicates where a boundary comes from; it does not establish that it is optimal. Researcher-defined choices are the three-state cardinality, *A*<sub>AI</sub>(CAUTION), the policy treating non-daylight hours as UNSAFE, the evaluation window, and the declared exclusion described next.

The marine-warning component has no usable historical archive for the replay period. It is handled by declared exclusion rather than imputation, and held at its least-severe value throughout. Because the classifier aggregates by maximum severity, a non-least-severe marine-warning observation could only maintain or raise the resulting severity. Intermediate-or-higher state activation frequencies reported later are therefore interpreted as lower bounds under this exclusion, which is a qualification on the measurement rather than a method.

Classification remains total under the exclusion: every evaluated hour receives a state from the available component rules and the declared treatment of the excluded component.

The replay is a deterministic census of all evaluated departure-window hours in the specified records. No sampling inference is performed, and no p-values, confidence intervals or significance claims apply. Ranges reported later are deterministic configuration ranges rather than confidence intervals. Implementation checks confirmed the configured admissible-set mappings were applied as specified.

---

## Micro-Revision Audit

| # | Check | Result |
|---|---|---|
| 1 | Edit 1 applied | **YES** |
| 2 | "with a rationale drawn from the domain literature" absent | **YES** |
| 3 | *A*<sub>AI</sub>(CAUTION) still explicitly researcher-defined | **YES** — retained in prose and in the Table I footnote |
| 4 | Non-validation qualification preserved | **YES** — *"It is not empirically validated, shown correct, shown optimal, or established as safer or more beneficial."* byte-identical |
| 5 | Edit 2 applied | **YES** |
| 6 | "Severity-based quantities reported later" absent | **YES** |
| 7 | Lower-bound claim scoped to intermediate-or-higher state activation frequencies | **YES** |
| 8 | *g*<sub>m</sub> exclusion logic unchanged | **YES** — no archive; declared exclusion rather than imputation; held at least-severe value; maximum-severity aggregation means a non-least-severe observation could only maintain or raise severity. All four steps byte-identical |
| 9 | Lower bound still a measurement qualification, not a method | **YES** |
| 10 | Section III prose word count | **704** (target 680–720) ✅ |
| 11 | Section IV prose word count | **434** (target 400–430) ⚠️ **+4 — declared below** |
| 12 | Δ definition unchanged | **YES** |
| 13 | Δ<sub>L2</sub> definition unchanged | **YES** |
| 14 | Δ<sub>L2</sub> ≡ *P*(*S* = CAUTION) unchanged | **YES** — with *"a metric-interpretation identity, not a result"* intact |
| 15 | C0–C3 mappings unchanged | **YES** — all four Table II rows byte-identical |
| 16 | C1/C3 zero-by-construction interpretation unchanged | **YES** — *"zero by construction"* and *"executable conformance check"* both intact |
| 17 | Comparator-ladder interpretation unchanged | **YES** — *"not required to compute it"* and the four stated purposes intact |
| 18 | PRIMARY dataset facts unchanged | **YES** — Jan 2020–Dec 2024; 43,848; ERA5-Ocean ~50 km; 9,135 |
| 19 | RESOLUTION dataset facts unchanged | **YES** — Oct 2021–Dec 2024; 28,501; MFWAM ~8 km; 5,935 |
| 20 | Threshold provenance unchanged | **YES** — including the non-MET status of the rainfall CAUTION boundary |
| 21 | No new citation introduced | **YES** — key set identical: DID-RAINFALL · ERA5 · FLEHMIG · IMO-COLREG · MET-THUNDERSTORM · MET-WIND · MILLER · OPEN-METEO · PARASURAMAN · YAAKOB |
| 22 | MFWAM manuscript wording unchanged | **YES** — *"wave data from MFWAM at approximately 8 km resolution"*, untouched |
| 23 | MFWAM citation-resolution task carried forward | **YES** — recorded below |
| 24 | IPoSCI absent | **YES** |
| 25 | "pre-inference" absent | **YES** |
| 26 | Unintended substantive change | **NONE** — see the diff check |

### Diff check

A sentence-level comparison against `aai-2026-manuscript-v1-phase2.md` reports **exactly two substantive changes**, both intended:

**CHANGE 1** — Section III, CAUTION design-choice wording.
**CHANGE 2** — Section IV, lower-bound scope wording.

No other manuscript-body difference of any kind was detected. Tables, equations, footnotes, citation keys and all dataset values are byte-identical.

### Declared word-budget overrun

**Section IV is 434 prose words against a 400–430 target, an overrun of four words.**

The overrun is caused directly by the mandated Edit 2 replacement, which is four words longer than the text it replaces (*"Intermediate-or-higher state activation frequencies reported later are therefore interpreted as lower bounds"* versus *"Severity-based quantities reported later are therefore lower bounds"*).

**No third edit was made to recover it.** Trimming elsewhere would have introduced a manuscript-body change beyond the two authorised, and the brief both caps the edits at two and warns against adjusting text to reach an exact count. The overrun is 0.9% of the section and immaterial to the page budget; Section III remains inside its target, so the Phase-2 total moves by four words in total. If the four words must be recovered, the compression target identified in the pre-draft feasibility check remains Section V rather than Section IV.

### Carried forward

**CITATION-RESOLUTION TASK — MFWAM.** MFWAM is named as the RESOLUTION wave source but has no verified bibliographic record in Citation Lock v2. Per instruction, no search was performed, no citation was invented, no placeholder was added, and the wording was left unchanged. **Verify the bibliographic source for MFWAM before final manuscript or camera-ready preparation.** This is not a Phase-2 methodological blocker.

---

PHASE 2 REVISION STATUS: READY FOR PHASE 3
