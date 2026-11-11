# AAI 2026 — Citation and Evidence Lock v2

**Date:** 2026-09-24
**Mode:** Bibliographic verification and evidence consolidation only.
**Supersedes:** `aai-2026-citation-evidence-lock.md` (v1) — v1 decisions are retained except where listed in §2.
**Authority:** primary papers are authoritative for claims about themselves; publisher/registry records are authoritative for bibliographic metadata; `aai-2026-threat-verification-v2.md` is authoritative for the current audit decision where supported by the primary papers.

🔒 **Research-chain status carried forward: V2 STATUS — ORIGINAL GAP SURVIVES.** The gap is not rewritten here. No locked document is edited by this task.

---

## 1. Status and authority

**The gap, unchanged and verbatim:**

> *"No empirical characterisation identified of how often an intermediate advisory-scope level changes the admissible set relative to a participation-only gate over a multi-year environmental record."*

🔒 **The qualifier *"within the reviewed literature"* must accompany every absence-of-prior-work statement in the manuscript.** It is load-bearing: this audit examined five supplied sources and is not an exhaustive search.

🔴 **Forbidden universalisations** (binding on all downstream work): *no prior work exists · first study · novel · unprecedented · never studied · none has ever* — or any other claim that ranges beyond the reviewed set.

---

## 2. Changes from Citation Lock v1

| # | Change | Reason |
|---|---|---|
| 1 | **+3 required references** — Aarab (ICHCAI 2026), Miller (MAKE 2026), Kim et al. (npj Digit. Med. 2026) | v2 audit: three near-neighbours must be conceded |
| 2 | **Prior-art boundary rewritten** — five concepts moved to ESTABLISHED PRIOR ART | v2 §10 |
| 3 | **Two items reclassified** as MEASUREMENT QUALIFICATION, not contributions | v2 §10 items 8–9 |
| 4 | 🔴 **Technique/estimand split introduced** for activation-frequency and threshold-sensitivity | v2 correction C4/C5 — v1 of the *threat* audit collapsed these |
| 5 | Gap-B entry annotated *"survives; re-tested against five primary sources"* — **not reversed** | v2 §11 |
| 6 | IPoSCI rule unchanged | Still accepted, not confirmed published |
| 7 | Required count **14 → 17** | §12 |

---

## 3. Publisher-verified bibliographic records

**Verification method:** DOI resolution to publisher record (MDPI, Nature) and Crossref registry metadata (IEEE). ⚠️ IEEE Xplore's own page could not be fetched directly (access-restricted); the IEEE record below is **VERIFIED FROM CROSSREF REGISTRY METADATA**, which is authoritative for title, authorship, venue, pagination and publisher.

### R-A — Legitimacy Layer

| Field | Verified value |
|---|---|
| Title | The Legitimacy Layer: A Runtime Governance Architecture for Human Oversight in AI-Assisted Critical Decision Systems |
| **Author** | **Hamza Aarab — SINGLE AUTHOR** |
| Conference | 2026 1st International Conference on Human Centric Artificial Intelligence (**ICHCAI**) |
| Event | Halden, Norway, 27–28 May 2026 |
| Pages | **1–10** |
| Publisher | IEEE |
| DOI | **10.1109/ICHCAI70183.2026.11607581** |
| Status | **Published** · Proceedings article |
| Stable URL | https://doi.org/10.1109/ICHCAI70183.2026.11607581 |
| Verification | **VERIFIED FROM CROSSREF REGISTRY METADATA**; author, affiliation and ORCID 0009-0006-0061-3888 corroborated by the primary text (p1) |

🔴 **CORRECTION TO THE TASK BRIEF.** The suggested wording in the brief reads *"Aarab et al."* — **this is wrong. Aarab is the sole author.** Cite as **"Aarab"**. Using "et al." for a single-author paper is a visible error that a reviewer familiar with the work will notice.

### R-B — Controlled Agentic AI Systems (CAIS)

| Field | Verified value |
|---|---|
| Title | Controlled Agentic AI Systems: A Governance-Driven Architecture for Auditable and Reproducible Decision Pipelines |
| **Author** | **Tymoteusz Miller — SINGLE AUTHOR** |
| Affiliations | Institute of Marine and Environmental Sciences, University of Szczecin, Poland; Faculty of Data Science and Information, INTI International University, Nilai, Malaysia |
| Journal | Machine Learning and Knowledge Extraction |
| Volume / issue / article | **8(5), 125** |
| Published | **8 May 2026** |
| Publisher | MDPI |
| DOI | **10.3390/make8050125** |
| Status | **Published** (CC BY) |
| Official citation | *Mach. Learn. Knowl. Extr.* **2026**, *8*(5), 125 |
| Verification | **VERIFIED FROM PUBLISHER RECORD** (mdpi.com/2504-4990/8/5/125) |

✅ The brief's *"Miller"* is correct — sole author, no "et al.".

### R-C — SA-ROC

| Field | Verified value |
|---|---|
| Title | **Defining operational safety in clinical artificial intelligence systems** *(publisher uses sentence case — reproduce as printed)* |
| **Authors, in order** | **Young-Tak Kim, Hyunji Kim, Manisha Bahl, Michael H. Lev, Ramon Gilberto González, Michael S. Gee, Synho Do** (7) |
| Journal | npj Digital Medicine |
| Volume / article | **9, 281** |
| Published | **20 February 2026** |
| Publisher | Nature Publishing Group |
| DOI | **10.1038/s41746-026-02450-7** |
| Status | **Published**, open access |
| Verification | **VERIFIED FROM PUBLISHER RECORD** (nature.com/articles/s41746-026-02450-7); author order corroborated by the primary text (p1) |

✅ The brief's *"Kim et al."* is correct — first author Young-Tak Kim, seven authors.

---

## 4. Evidence card — Legitimacy Layer (Aarab, 2026)

**VERIFIED RECORD:** see R-A.

**WHAT IT ESTABLISHES**
- Runtime governance modes constrain which execution directives may be issued: *"it dynamically constrains which routing directives the Legitimacy Controller may issue under prevailing operational conditions"* (§IV-B, p4).
- Normal Autonomy is the permissive mode: *"the controller may issue execute or execute_async for decisions meeting signal thresholds, full routing capability is available"* (§IV-E, p6).
- **Reduced Autonomy is a genuine intermediate contraction with operation continuing:** *"the execute directive is restricted to low-impact decisions, asynchronous execution remains available for reversible decisions… as the system continues operating under tighter governance constraints"* (§IV-E, p6).
- Human Oversight Required: *"both execute and execute_async are suppressed and all decisions are routed through escalate"* (§IV-E, p6).
- Safe Halt: *"all execution is suspended… and only halt is permitted"* (§IV-E, p6).
- ⇒ **Graduated runtime contraction of permitted directives is ESTABLISHED PRIOR ART.**

**WHAT IT DOES NOT ESTABLISH**
- 🔴 It does **not** measure how often Reduced Autonomy binds. The 1,000-instance directive distribution (Table IV, p8) was *"conducted under Normal Autonomy mode assumptions"* (§V-G, p8).
- No Normal-versus-Reduced comparison; Table V (p8) varies **input regimes** (uncertainty distribution × contestation probability), not governance configurations.
- No ablation removing the intermediate mode; no participation-only comparator; no marginal isolation — the 82.9% is decomposed by **rule**, not by mode (§V-G, p8).
- Table I (p7) records mode transitions as **qualitative Pass/Fail logical traces** under injected adversarial conditions. Table VI (p9) is *"a manually constructed decision sequence designed to traverse all four governance states"*. The author states *"This minimal simulation does not constitute empirical validation"* (§V-G, p9).

**✅ SAFE MANUSCRIPT WORDING** *(refined from the brief; "et al." removed)*
> *"Aarab specifies graduated runtime autonomy modes in which the permitted execution directives contract as governance severity increases while operation continues [ref]. The reported directive-frequency simulation is conducted under the permissive mode rather than as a comparison of graduated governance configurations."*

**🔴 PROHIBITED / OVERSTATED**
- ✗ *"Aarab **et al.**"* — single author
- ✗ that the paper measured how often Reduced Autonomy binds
- ✗ that it compared Normal versus Reduced, isolated the intermediate level, or evaluated a participation-only comparator
- ✗ that it empirically validated graduated-mode activation frequency
- ✗ any claim that graduated contraction is new to our work

**PRIMARY-SOURCE LOCATIONS:** §IV-B p4; §IV-E p6; Algorithm 1 p5; Table I p7; Tables IV–V p8; Table VI and §V-G p9.

---

## 5. Evidence card — CAIS (Miller, 2026)

**VERIFIED RECORD:** see R-B.

**WHAT IT ESTABLISHES**
- A governance operator transforms proposed actions into admissible executed actions (abstract, p1).
- Three configurations, §3.4 (p16): **ungoverned baseline** *"at = ρ(dt)"*, *"without any constraint enforcement"*; **approval-only gating** *"admissible proposals are executed unchanged but inadmissible proposals trigger a conservative fallback a⋆"*; **projection-based repair** onto `A_C(s_t)`.
- Explicit systematic ablation: *"enabling a systematic ablation study"* (§3.4, p16).
- Statistical comparison: Mann–Whitney U with Cliff's δ, n=30 per mode (Tables 3 and 5, pp21–22).
- ⇒ **Governance-configuration ablation against an ungoverned baseline is ESTABLISHED PRIOR ART.**

**WHAT IT DOES NOT ESTABLISH**
- 🔴 These are **governance operator configurations, not graduated risk levels.** No risk-level structure exists anywhere in the paper.
- No FULL → FULL → NONE configuration; no FULL → RESTRICTED → NONE configuration.
- No intermediate governance state is isolated.
- No contraction-binding frequency is measured. Metrics are **violation rate** — *"Fraction of time steps where executed action violates at least one constraint"* (Table 1, p17) — and **decision drift** δt = Δ(at, ρ(dt)), *"Measures intervention cost"*. Mean drift conflates intervention frequency with intervention magnitude and the two are not separable from the reported statistics.
- Data are simulated (multi-agent and federated environments, abstract p1).

**📌 RESULT DIRECTION — LOCKED.** Violation rate (Table 2, p21): `none` **1.0000**, `gate_fallback` **0.0333**, `project` **0.8317**. Decision drift (Table 4, p22): `none` **0.0000**, `gate_fallback` **10.3659**, `project` **12.7434**.
🔴 **Projection performs WORSE on compliance than approval-only gating and costs more drift.** Never imply projection improves compliance.

**✅ SAFE MANUSCRIPT WORDING** *(refined from the brief)*
> *"Miller evaluates alternative governance operators — an ungoverned baseline, approval-only gating, and projection-based repair — through systematic ablation with statistical comparison [ref]. Those configurations compare enforcement operators rather than graduated risk levels, and do not measure the frequency with which an intermediate active scope contraction binds."*

**🔴 PROHIBITED / OVERSTATED**
- ✗ that CAIS evaluates FULL → FULL → NONE or FULL → RESTRICTED → NONE
- ✗ that it isolates an intermediate governance state
- ✗ that it measures contraction-binding frequency
- ✗ that projection improves compliance
- ✗ *"Miller et al."* — single author
- ✗ any claim that comparator/ablation methodology is new to our work

**PRIMARY-SOURCE LOCATIONS:** abstract p1; §3.4 p16; §3.5 p16; Table 1 p17; Tables 2–3 p21; Tables 4–5 p22.

---

## 6. Evidence card — SA-ROC (Kim et al., 2026)

**VERIFIED RECORD:** see R-C.

**WHAT IT ESTABLISHES**
- Reliability targets α⁺ and α⁻ yield score cutoffs partitioning predictions into **Rule-in Safe Zone**, **Rule-out Safe Zone** and **Gray Zone** (p3).
- Gray Zone cases *"are designated for mandatory human expert review"* (p3); Fig. 1c labels it *"essential human review"* (p2).
- **ΓArea quantifies non-automated workload:** *"To quantify this non-automated workload, we introduce the Gray Zone Area (ΓArea), a metric measuring the operational cost of indecision"* (p1).
- **Policy-parameter sensitivity is real and substantial:** Safety Profile Curves *"comparing the two models across levels ranging from 50% to 100%; top: percentage of cases in the Gray Zone; bottom: corresponding ΓArea values"* (Fig. 3c, p4). Zones defined at α = 90%, 95%, 100% with 95% CIs.
- **Real clinical data:** two FDA-cleared mammography AI solutions; AI #2 *"ruled out 290 true negative cases, which safely removed 29.0% of the entire patient cohort from the radiologist's workload"* versus AI #1's 167 (16.7%), difference 123 (95% CI 87.0–150.0) (p4). Radiologist outcomes analysed per zone (Fig. 4, p5).
- ⇒ **Activation/burden measurement against a policy target, and threshold-sensitivity characterisation, are ESTABLISHED PRIOR ART.**

**WHAT IT DOES NOT ESTABLISH**
- 🔴 **The Gray Zone is abstention with transfer of authority, not contracted AI scope.** The paper nowhere describes the AI issuing a narrower set of recommendations there; it measures **human** accuracy within the zone (Fig. 4, p5) and uses elimination language: *"the AI eliminates its ability…"* (p5).
- No participation-only comparator — the comparison is **between two FDA-cleared models**, not between governance configurations.
- No marginal isolation of the intermediate zone.
- ΓArea measures **occupancy/burden**, reported alongside a separate *"% of Cohort in Gray Zone"*; it is not a contraction measure of an admissible AI action set, and the paper asserts **no identity** between the two metrics.

**✅ SAFE MANUSCRIPT WORDING** *(refined from the brief)*
> *"Kim et al. quantify the operational burden of an intermediate Gray Zone requiring mandatory human review, and characterise that burden across reliability targets on real clinical data [ref]. That measures abstention and non-automated workload rather than the frequency with which an active system's admissible recommendation set contracts."*

**🔴 PROHIBITED / OVERSTATED**
- ✗ that SA-ROC shares the Δ_L2 estimand
- ✗ that the Gray Zone is FULL → RESTRICTED
- ✗ that SA-ROC evaluates participation-only versus intermediate scope
- ✗ that ΓArea measures contraction of an admissible AI recommendation set
- ✗ any claim that activation-frequency measurement or threshold sensitivity is new to our work
- ⚠️ Reproduce the title in **sentence case** as the publisher prints it

**PRIMARY-SOURCE LOCATIONS:** abstract p1; zone definitions p3; Fig. 1c p2; Fig. 3c and case study p4; Fig. 4 and utility policies p5.

---

## 7. Updated prior-art boundary

🔒 **Binding. Status labels are restricted to the four below. "Novel", "first", "unique", "unprecedented" are prohibited throughout.**

| # | Claim / concept | Status | Required citation | ✅ Safe wording | 🔴 Forbidden wording |
|---|---|---|---|---|---|
| 1 | Runtime restriction of permitted behaviour | **ESTABLISHED PRIOR ART** | ASTM F3269-21; Aarab; Miller | "bounding permitted behaviour at runtime is established practice" | "we introduce runtime restriction" |
| 2 | Graduated risk / autonomy levels | **ESTABLISHED PRIOR ART** | Aarab; Parasuraman et al. | "graduated autonomy levels are established" | "we propose graduated levels" |
| 3 | FULL → RESTRICTED → NONE topology | **ESTABLISHED PRIOR ART** | Aarab §IV-E | "this topology is established in runtime governance" | "our graduated topology"; "a new three-level design" |
| 4 | Activation-frequency measurement *as technique* | **ESTABLISHED PRIOR ART** | Kim et al. | "measuring how often a governance boundary binds is established" | "we introduce activation-frequency measurement" |
| 4b | Frequency with which an **active intermediate contraction** binds *as estimand* | **SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET** | — | "within the reviewed literature we did not identify this measurement" | "the first measurement of"; "no one has measured" |
| 5 | Threshold-sensitivity measurement *as technique* | **ESTABLISHED PRIOR ART** | Kim et al. (α = 50–100%) | "sweeping a policy parameter is established" | "we introduce sensitivity characterisation" |
| 5b | Sensitivity of a **contraction rate** to its governing threshold | **SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET** | — | as 4b | as 4b |
| 6 | Governance comparator / ablation *generally* | **ESTABLISHED PRIOR ART** | Miller §3.4 | "governance-configuration ablation against an ungoverned baseline is established" | "we contribute a comparator methodology" |
| 7 | Operational governance measurement *generally* | **ESTABLISHED PRIOR ART** | Kim et al.; Miller | "operational measurement of governance is established" | "governance is rarely measured" |
| 8 | **Participation-only vs intermediate-scope isolation** | **SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET** | — | "within the reviewed literature, none isolates an intermediate contraction against a participation-only configuration differing only at that level" | "the first isolation of"; "uniquely isolates" |
| 9 | **Δ_L2 ≡ P(S = CAUTION) interpretation** | **SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET** | — | "we state the identity and its consequence that the measure is invariant to the content of the restriction" | "a novel identity"; "previously unrecognised" |
| 10 | Contraction-specific threshold sensitivity | **SUPPORTED AS DISTINCTIVE WITHIN REVIEWED SET** | — | as 8 | as 8 |
| 11 | Denominator-policy sensitivity | **MEASUREMENT QUALIFICATION** | — | "the reported rate depends on the denominator policy; both are reported" | "we contribute denominator-policy analysis" |
| 12 | Missing-component / lower-bound interpretation | **MEASUREMENT QUALIFICATION** | — | "because aggregation is by maximum severity and the excluded component can only raise severity, all figures are lower bounds" | "we contribute a lower-bound method"; "partial identification" |

---

## 8. Gap-B evidence lock

🔒 **Gap B survives. The entry below records why, against the three near-neighbours.**

| Paper | Has | Lacks | Therefore |
|---|---|---|---|
| **Aarab** | Intermediate **active** contraction (Reduced Autonomy, §IV-E p6) | Participation-only comparator; any measurement of how often that intermediate contraction binds — its directive distribution is measured under the permissive mode alone (§V-G p8) | Does not close the gap |
| **Miller** | Governance-configuration ablation incl. ungoverned baseline, with statistical isolation (§3.4 p16; Tables 3, 5) | Any graduated risk level; any intermediate contraction-frequency estimand — metrics are violation rate and drift | Does not close the gap |
| **Kim et al.** | Real-data intermediate-zone burden measurement and parameter sensitivity (ΓArea; Fig. 3c p4) | Active scope contraction — the Gray Zone is mandatory human review (p3); and any participation-only comparator | Does not close the gap |

**Locked conclusion:**

> **Within the reviewed literature**, none of these three performs the specific combination of **active intermediate scope contraction + participation-only comparator + marginal isolation + binding-frequency measurement.**

🔴 **This is a statement about the reviewed set only.** It must never be written as a claim that no paper anywhere performs this combination.

---

## 9. Existing citation decisions retained

| Source | Decision | Unchanged from v1 |
|---|---|---|
| **NIST AI RMF** (NIST AI 100-1, DOI 10.6028/NIST.AI.100-1) | Use conservatively — supports testing before deployment and monitoring in operation, and analysis of *"AI risk and related impacts"*. **Does not** state a control-effectiveness criterion. Never "requires" | ✅ |
| **ASTM F3269-21** (DOI 10.1520/F3269-21) | Runtime-assurance concession, **title-and-scope citation only**. No clause-level claim — full text not read | ✅ |
| **Alshiekh et al. 2018** (AAAI-18, pp. 2669–2678) | Use **"preemptive"** / *"before the agent selects an action"*. 🔴 **"pre-inference restriction" remains prohibited** | ✅ |
| **Parasuraman, Sheridan & Wickens 2000** (DOI 10.1109/3468.844354) | Concede **both** the individuation point and levels 2–4 graduated contraction of offered alternatives | ✅ |
| **Manski** | **NOT REQUIRED** — the bound follows from monotone aggregation | ✅ |
| **TSO-C151c** | **DROP** | ✅ |
| **DSA-SafetyBench** | **DROP** from the governance citation set. Classification/ranking/calibration ≠ governance-scope contraction | ✅ (v2 confirmed) |
| **A⁴-Gov** | **OPTIONAL / drop** — no evaluation; framing duplicated by Aarab | ✅ |

---

## 10. IPoSCI publication-status rule

🔒 **Carried forward unchanged. The IPoSCI 2026 extended abstract is ACCEPTED but NOT confirmed published in proceedings.**

- ✗ Do not list it as a published bibliographic reference.
- ✗ Do not call it *previously published*, *previously reported*, or a *prior publication*.
- ✗ Do not write *"reported in [15]"* unless a stable citable proceedings version exists at final submission.
- ✗ **Do not renumber it into the bibliography to preserve the old [15] placeholder.** The numbering below omits it entirely.
- ✅ Retain as **internal provenance**. Material developed for the earlier study must not be presented as newly created for AAI — enforced by the architecture's §11 differentiation control, which remains the primary safeguard.
- ✅ 5.81% / 4.48% are reported as outputs of the evaluation this paper describes, with **no claim about when they were first computed**.
- 🔴 **Re-check publication status immediately before submission.** If published: add the proceedings citation and an explicit relationship sentence. If not: invent no citation; disclose in the submission form or cover letter.

---

## 11. Required / optional / dropped references

### REQUIRED (17)

| # | Reference | Required because… |
|---|---|---|
| 1 | AI governance systematic literature review (AI & Ethics, 2024, DOI 10.1007/s43681-024-00653-w) | …it evidences the implementation-and-validation gap that positions the paper |
| 2 | NIST AI RMF 1.0 (NIST AI 100-1) | …it supplies the measurement-in-operation premise without which the positioning is the authors' assertion alone |
| 3 | ASTM F3269-21 | …the runtime-assurance mechanism must be conceded on page 1 or the paper reads as claiming it |
| 4 | Alshiekh et al., AAAI-18, 2669–2678 | …preemptive restriction of the available action set is prior art and must not appear to be ours |
| 5 | FAA AC 20-151C | …advisory-type inhibition by external state is the mechanism's certified precedent |
| 6 | Parasuraman, Sheridan & Wickens 2000 | …it sources both level individuation and graduated contraction of offered alternatives |
| 7 | Flehmig et al. 2024 | …C3's topology is ported from it and the provenance must be stated with its fairness qualification |
| 8 | **Aarab 2026 (ICHCAI)** | …it is the closest graduated runtime contraction topology and leaving it unconceded is the largest single novelty exposure |
| 9 | **Miller 2026 (MAKE 8(5):125)** | …it establishes governance-configuration ablation against an ungoverned baseline, which our comparator ladder otherwise appears to introduce |
| 10 | **Kim et al. 2026 (npj Digit. Med. 9:281)** | …it establishes binding-rate measurement against a policy target on real data, which our sensitivity work otherwise appears to introduce |
| 11 | Yaakob et al. 2015 | …it sources the wave threshold and the two readings giving 5.81% and 9.22% |
| 12 | MET Malaysia — strong-wind criteria | …wind boundary provenance |
| 13 | MET Malaysia — thunderstorm criteria | …rainfall UNSAFE boundary provenance |
| 14 | JPS/DID rainfall categorisation | …the CAUTION rainfall boundary is sourced but non-MET, and the gap in the source material must be documented |
| 15 | COLREGs Rule 20(b) | …the time boundary's source, with the abstention policy declared researcher-defined |
| 16 | Zippenfenig 2023 (Open-Meteo) | …data source |
| 17 | Hersbach et al. 2023 (ERA5) | …reanalysis source |

### SHOULD KEEP (1)
Shamsujjoha et al. 2025 (ICSA, DOI 10.1109/ICSA65012.2025.00014) — multi-layered guardrail concession.

### OPTIONAL (2)
Gyllenhammar et al. 2025 (fail-safe / MRC); a runtime-verification source for the one-sentence totality claim.

### DROPPED
Manski · TSO-C151c · Simplex (Sha) · Puterman · selective prediction / reject-option · EU AI Act · ISO/IEC 42001 · ISO/IEC 23894 · Indykov et al. · Hevner et al. · Gao 2024 · Rahim et al. 2024 · Jeong & Im 2023 · contemporary shielding · **DSA-SafetyBench** · **A⁴-Gov** · **IPoSCI extended abstract** *(status, not relevance)*.

---

## 12. Reference budget

| Class | Count |
|---|---|
| REQUIRED | **17** |
| SHOULD KEEP | 1 |
| OPTIONAL | 2 |
| **Total range** | **17 – 20** |

✅ Within the 20–24 target, at the lean end. ⚠️ **The margin is now thin: only three references are discretionary.** No further reference may be added without dropping one. Every entry above has a stated job; none is retained for having appeared in an earlier search.

---

## 13. Safe manuscript wording bank

**Positioning**
- *"Reviews of AI governance report that published frameworks frequently lack real-world implementation detail and validation [1]."*
- *"Risk-management guidance directs that AI systems be tested before deployment and monitored while in operation [2]."*
- *"Whether a declared governance level changes what a system is permitted to do is, on this view, a property to be measured rather than assumed."* ← authors' own inference, attributed to neither source

**Page-1 concession**
- *"Bounding the behaviour of a system containing complex functions by an independently assured run-time architecture is established aviation practice, and is standardised [3]."*
- *"A shield may compute the set of safe actions and remove unsafe ones before the agent selects, rather than correcting the action afterwards [4]."*
- *"Certified collision-avoidance avionics progressively inhibit advisory types as an externally measured state worsens [5], and the canonical levels-of-automation model already describes graduated contraction of the alternatives presented to a human [6]."*
- *"This paper contributes none of these mechanisms."* ← mandatory closing sentence

**Near-neighbour concessions**
- *"Aarab specifies graduated runtime autonomy modes in which permitted execution directives contract as governance severity increases while operation continues [8]; the reported directive-frequency simulation is conducted under the permissive mode rather than as a comparison of graduated governance configurations."*
- *"Miller evaluates alternative governance operators — an ungoverned baseline, approval-only gating, and projection-based repair — through systematic ablation with statistical comparison [9]; those configurations compare enforcement operators rather than graduated risk levels."*
- *"Kim et al. quantify the operational burden of an intermediate Gray Zone requiring mandatory human review and characterise that burden across reliability targets on real clinical data [10]; that measures abstention rather than contraction of an active system's admissible recommendation set."*

**Gap statement**
- *"**Within the reviewed literature**, we did not identify a measurement in which an intermediate level that contracts the admissible recommendation set while the system remains active is isolated against a participation-only configuration differing from it only at that level."*

**Results qualification**
- *"…5.81% of departure-window hours, as a lower bound, within a sourced-threshold envelope of 5.67–9.56%."*
- *"…97.6% attributable to a single environmental component."*
- *"The evaluation is a deterministic census of a predefined window; no confidence intervals or significance tests apply."*

---

## 14. Prohibited wording bank

**Universal-absence claims** — no prior work exists · first · novel · unique · unprecedented · never studied · none has ever · no one has measured.

**Mechanism claims** — we introduce runtime restriction · our graduated topology · we propose graduated levels · a new three-level design · we contribute a comparator methodology · we introduce activation-frequency measurement · we introduce sensitivity characterisation.

**Terminology** — pre-inference / before model inference / before the forward pass · AI behaviour or system behaviour meaning generated output · human-centred · meaningful human control · trustworthy · ethical · safe/safer/risk-reducing · optimal/validated/correct · robust *(unqualified)* · stable · significant *(statistical sense)* · confidence interval · ± notation · partial identification.

**Attribution errors** — *"Aarab et al."* (single author) · *"Miller et al."* (single author) · implying projection improves compliance in Miller · implying Aarab measured graduated-mode frequency · implying Kim et al. share the Δ_L2 estimand.

**Publication status** — previously published · previously reported · prior publication · in proceedings *(of the IPoSCI abstract)* · we introduce/propose/develop *(applied to the architecture, the three states, or the graduated advisory-scope concept)*.

---

## 15. Consistency check against the locked research chain

| Locked element | Consistent? | Note |
|---|---|---|
| Problem (§2) | ✅ | Unaffected |
| Gap B (§5) | ✅ | Survives; evidence lock at §8 above |
| Primary RQ (§6) | ✅ | Unaffected |
| Supporting criterion (§7) | ✅ | Unaffected — still a method criterion, not an RQ |
| Central claim (§14) | ✅ | Claims activation at a site, not novelty of technique |
| Non-claims (§17) | ✅ | All prohibitions reinforced |
| **Contribution ledger (§13)** | ⚠️ **INCONSISTENT** | Lists comparator design and sensitivity envelope as PRIMARY components. Both are now **ESTABLISHED PRIOR ART as technique**. The estimand and the isolation carry the contribution |
| **Contribution ledger (§13)** | ⚠️ **INCONSISTENT** | Lists denominator dependence and lower-bound status as contribution components. Both are **MEASUREMENT QUALIFICATIONS** |
| **§21 attack 16** | ⚠️ **INCONSISTENT** | *"what is not anticipated"* now has three named near-neighbours |
| Architecture §5 related work | ⚠️ **INCOMPLETE** | Requires a fourth cluster naming Aarab, Miller, Kim et al. |

🔴 **Four inconsistencies recorded. None is edited by this task.** They are precision defects in how the contribution is *described*, not defects in the problem, gap, RQ or claim. The contribution remains representable, **within the reviewed set**, as the measurement assembly around participation-only versus intermediate-scope isolation, the Δ interpretation as contraction-binding frequency, contraction-specific threshold sensitivity, and component attribution.

---

## 16. Remaining unresolved evidence

| # | Item | Severity |
|---|---|---|
| 1 | IEEE Xplore's own page for Aarab could not be fetched (access-restricted). Record verified via **Crossref registry**, corroborated by the primary text. Sufficient for citation; confirm page range 1–10 against Xplore if access becomes available | 🟢 Low |
| 2 | Author list for reference [1] (AI-governance SLR) still not captured — read from the corpus note before drafting | 🟠 Medium |
| 3 | Optional runtime-verification source for the P1 totality sentence not selected | 🟢 Low |
| 4 | ASTM F3269-21 full text not read — title-and-scope citation only; **no clause numbers may be added later** | 🟠 Medium |
| 5 | **IPoSCI publication status** — re-check immediately before submission | 🔴 **High** |
| 6 | Aarab's prototype repository may contain an unreported multi-mode frequency run; if so §4's "does not establish" list would need revisiting | 🟠 Medium |
| 7 | SA-ROC Supplementary Note 1 and Supplementary Tables 1–2 were not in the extraction | 🟢 Low |
| 8 | This audit covers five supplied sources and is **not exhaustive**; the *"within the reviewed literature"* qualifier is load-bearing | 🔴 **High** |

---

## 17. Pre-drafting readiness verdict

All three near-neighbour concessions are supported by publisher-verified records and primary-source quotation. The Gap-B evidence lock is complete and rests on distinctions verified against the papers themselves. No unresolved item prevents either.

**CITATION LOCK v2 STATUS: READY FOR PRECISION PATCH**

---

*Citation and evidence lock v2 complete. Bibliographic metadata verified against MDPI, Nature and Crossref registry records. No manuscript text drafted. No locked document edited — §15 records four inconsistencies for the author to decide upon.*
