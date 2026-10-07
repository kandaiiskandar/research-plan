# III. Governance Contract, Criterion and Metric

Measuring that combination requires the governed object to be stated explicitly. We take it to be *A*<sub>AI</sub>(*S*), the set of recommendation types admissible when the classified operating state is *S*. Each evaluated hour is assigned one of three states, SAFE, CAUTION or UNSAFE, and FULL denotes the unrestricted recommendation set {Go, Delay, DepartureTime, Duration}. Table I states the contract. The admissible sets contract monotonically across the three states by construction. Participation gating is the special case in which the admissible set is empty, and so requires no separate formalism here.

*A*<sub>AI</sub>(CAUTION) = {Go, Delay} is a researcher-defined design choice with a rationale drawn from the domain literature. It is not empirically validated, shown correct, shown optimal, or established as safer or more beneficial. As Section III-E makes explicit, the measurement reported in this paper does not validate it.

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

The marine-warning component has no usable historical archive for the replay period. It is handled by declared exclusion rather than imputation, and held at its least-severe value throughout. Because the classifier aggregates by maximum severity, a non-least-severe marine-warning observation could only maintain or raise the resulting severity. Severity-based quantities reported later are therefore lower bounds under this exclusion, which is a qualification on the measurement rather than a method.

Classification remains total under the exclusion: every evaluated hour receives a state from the available component rules and the declared treatment of the excluded component.

The replay is a deterministic census of all evaluated departure-window hours in the specified records. No sampling inference is performed, and no p-values, confidence intervals or significance claims apply. Ranges reported later are deterministic configuration ranges rather than confidence intervals. Implementation checks confirmed the configured admissible-set mappings were applied as specified.

---

## Drafting Audit

| # | Check | Result |
|---|---|---|
| 1 | Section III prose word count | **702** (target 680–720) ✅ — tables, captions, footnotes and equations excluded |
| 2 | Section IV prose word count | **430** (target 400–430) ✅ |
| 3 | Table I included | **YES** |
| 4 | Table II included | **YES** |
| 5 | *A*<sub>AI</sub>(*S*) defined | **YES** — as the set of recommendation types admissible when the classified state is *S* |
| 6 | *G*(*S*) omitted as an independent formal object | **YES** — named once as the empty-set special case; in Table I only, with the footnote stating it is determined by emptiness of *A*<sub>AI</sub> and shown for readability |
| 7 | *A*<sub>AI</sub>(CAUTION) identified as researcher-defined | **YES** — in prose and in the Table I footnote, both stating it is not validated, optimal or safer |
| 8 | Criterion labelled only as a criterion | **YES** — no theorem, proposition, lemma or guarantee language anywhere |
| 9 | Criterion grounded in Parasuraman rather than claimed as new | **YES** — *"an operational measurement rule rather than a result… restates… the position already established"* |
| 10 | C1/C2 differ only at CAUTION | **YES** |
| 11 | C1/C3 equivalence stated as by construction | **YES** — *"zero by construction"* |
| 12 | C1↔C3 = 0 treated as entailed/conformance | **YES** — *"executable conformance check on the implementation rather than an empirical finding"*, with the added guard that it is not evidence three-state designs are ineffective |
| 13 | C3/Flehmig fairness qualification | **YES** — Table II footnote, locked wording preserved |
| 14 | Δ<sub>L2</sub> defined | **YES** — Δ = (*N*<sub>restricted</sub>/*N*<sub>eval</sub>)×100%; Δ<sub>L2</sub> = (C0↔C2) − (C0↔C1) |
| 15 | Direct C1↔C2 cross-check mentioned | **YES** |
| 16 | Identity stated before any numerical result | **YES** — Section III-E; no result value appears anywhere in Phase 2 |
| 17 | Identity treated as metric interpretation | **YES** — *"a metric-interpretation identity, not a result"* |
| 18 | Invariance to the content of *A*<sub>AI</sub>(CAUTION) stated | **YES** — with the strict-subset proviso |
| 19 | Measures HOW OFTEN, not HOW MUCH | **YES** — stated explicitly, followed by the four things it does not indicate |
| 20 | Ladder NOT claimed necessary | **YES** — *"the CAUTION base rate yields the same number and the comparator ladder is not required to compute it"* |
| 21 | Ladder role stated as decomposition + isolation + identity establishment + cross-check | **YES** — all four given |
| 22 | No 5.81 / 4.48 / 42.88 / 48.69 disclosed | **YES** — scan confirms no result value of any kind |
| 23 | PRIMARY period / records / denominator correct | **YES** — Jan 2020–Dec 2024; 43,848; 9,135 |
| 24 | RESOLUTION period / records / denominator correct | **YES** — Oct 2021–Dec 2024; 28,501; 5,935 |
| 25 | 05:00–09:00 as researcher-defined evaluation policy | **YES** — *"an evaluation-policy choice rather than an observed departure period"* |
| 26 | Threshold provenance separated from design choice | **YES** — one sentence opens the separation, four sourced boundaries follow, researcher-defined choices enumerated at the close |
| 27 | Rainfall CAUTION boundary source-supported but non-MET | **YES** — with the reason (no criterion published below the thunderstorm level) |
| 28 | No universal "official thresholds" claim | **YES** |
| 29 | No optimal-threshold claim | **YES** — *"provenance indicates where a boundary comes from; it does not establish that it is optimal"* |
| 30 | *g*<sub>m</sub> exclusion stated | **YES** — declared exclusion rather than imputation |
| 31 | Lower-bound logic stated | **YES** — maximum-severity aggregation, least-severe holding, could only maintain or raise |
| 32 | Lower bound treated as qualification | **YES** — *"a qualification on the measurement rather than a method"* |
| 33 | Manski absent | **YES** |
| 34 | Deterministic census stated | **YES** |
| 35 | No p-values / confidence intervals / significance | **YES** |
| 36 | Sensitivity ranges identified as deterministic configuration ranges | **YES** |
| 37 | No safety / effectiveness / optimality claim | **YES** |
| 38 | No full architecture introduced | **YES** — components named in one sentence; no layer diagram, no *S* = *f*(*E*) presentation |
| 39 | No second RQ introduced | **YES** — the token "RQ" does not appear in Phase 2 |
| 40 | Phase 1 wording untouched | **YES** — Phase 2 is a separate file; `aai-2026-manuscript-v1-phase1-revised.md` was read only, and the superseded `-phase1.md` was not opened |
| 41 | "pre-inference" absent | **YES** |
| 42 | IPoSCI absent | **YES** |

**43. Unsupported citation placeholders.** One. **MFWAM** is named as the RESOLUTION wave source in prose but carries **no citation key**, because Citation Lock v2 §11 holds no bibliographic record for it. It is written as a data-source name only. `[OPEN-METEO]` and `[ERA5]` cover retrieval and the reanalysis dataset. If a reviewer requires MFWAM to be cited, a record must be located and verified; no reference was invented here. All other keys used — DID-RAINFALL, ERA5, FLEHMIG, IMO-COLREG, MET-THUNDERSTORM, MET-WIND, MILLER, OPEN-METEO, PARASURAMAN, YAAKOB — are present in Citation Lock v2.

**44. Deviation from the patched locked research chain.** None. Every evaluation fact matches §11 verbatim, and the provenance split matches §8 verbatim, including the non-MET status of the rainfall CAUTION boundary.

**45. Claims deferred to Results.** All numerical findings; the sensitivity envelope; the alternative source reading; the wave-onset perturbation range; component attribution; vessel-class variants; the daylight-only denominator; and the replayed C1↔C3 conformance value. Section IV states only that ranges reported later are deterministic configuration ranges.

### Declared editorial notes

**Enumerator removed for token compliance.** Section III-E originally read *"First… Second…"* when listing the two consequences of the identity. The drafting contract prohibits the token *first*. Although the usage was an enumerator and not a novelty claim, the phrasing was changed to *"One is that… The other is that…"* so that an automated scan cannot flag it. No meaning changed.

**P2 containment.** Represented by a single clause, *"The admissible sets contract monotonically across the three states by construction."* No containment property is named, numbered or proved. P1 totality appears as one sentence in Section IV as instructed. P3 is not formalised. P4 is not labelled; its content is carried by the criterion and the C1/C3 construction.

### Final self-check

**Section III — can a reviewer conclude all four?**

A. **Yes.** C1 and C2 are stated identical at SAFE and UNSAFE and differing only at CAUTION, with the consequence drawn explicitly.
B. **Yes.** The identity is derived in prose from those mappings and stated as Δ<sub>L2</sub> ≡ *P*(*S* = CAUTION).
C. **Yes.** The invariance paragraph states that the value does not indicate whether {Go, Delay} is correct or optimal, and the Table I footnote repeats that the set is researcher-defined.
D. **Yes.** The closing paragraph states the base rate yields the same number and the ladder is not required to compute it, then gives the four purposes the ladder does serve.

**Section IV — can a reviewer distinguish the four categories?** **Yes.** Externally sourced boundaries are enumerated with citation keys; researcher-defined choices are enumerated in a single closing sentence; the unavailable component has its own paragraph with the exclusion and its bound; and the deterministic evaluation choices are stated in the closing paragraph.

---

PHASE 2 STATUS: READY FOR REVIEW
