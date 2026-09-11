# Batch 2 Report — Layer 3 Advisory Rule Scientific Specification

**Workstream:** Journal 1 Layer 3 Prototype  
**Batch:** 2 — Concrete Layer 3 Advisory Rule Scientific Specification  
**Closed:** 2026-09-11  
**Branch:** design/journal1-algorithm-specification  
**Outcome:** CLOSED (2026-09-11) — advisory evidence-mapping defects resolved; OPEN-L3-3 resolved under Resolution B (presentation qualifier only) — see `open-l3-3-resolution/`; Batch 3 unblocked on the OPEN-L3-3 axis (other Batch 3 gating conditions remain in force independently).

*(Historical — superseded: REMAINS OPEN (Case B) — OPEN-L3-3 created for unresolved Appendix C CAUTION-Go tension. Superseded by 2026-09-11 Resolution B.)*

---

## 1. What Batch 2 Was Not

The scope of Batch 2 needs to be stated negatively before positively, because the easiest wrong turn here is treating it as an implementation task. Batch 2 was not about building the rule engine. It was not about populating the rule repository to make it look complete. It was not about converting Layer 2 classification thresholds into Layer 3 rules on the grounds that the architecture already uses them.

The task was narrower and harder: determine which advisory rules can be defended with reference to an identifiable scientific source.

---

## 2. The Central Question

OPEN-L3-1, carried forward from Batch 1, asked: what concrete advisory rules can RS(SAFE) and RS(CAUTION) contain?

The question splits into four parts corresponding to the four types in R = {Go, Delay, DepartureTime, Duration}:

- When does the evidence warrant a Go recommendation?
- When does the evidence warrant a Delay recommendation?
- When does the evidence warrant a DepartureTime recommendation?
- When does the evidence warrant a Duration recommendation?

Each question was treated separately. The outcome differs by type.

---

## 3. Evidence Hierarchy

The assessment started by establishing an evidence hierarchy so the criteria were explicit before any rule could be evaluated. Five levels:

- **Level A** — direct normative or operational authority (MET Malaysia, Department of Fisheries, IMO, WMO)
- **Level B** — direct empirical evidence from small-scale fisheries peer-reviewed literature
- **Level C** — strong domain evidence requiring bounded geographic or vessel-type adaptation to reach Kota Kinabalu Zone A fishers
- **Level D** — architecture or design interpretation; definitional only, no empirical basis
- **UNSUPPORTED** — no defensible mapping between evidence and advisory content

The hierarchy appears in full in `rule-evidence-matrix-batch2.csv` and in the specification document at §18.

---

## 4. Evidence Sources

The evidence search produced nine sources (EV-01 through EV-09):

**EV-01 — MET Malaysia Category 1 warning** (Level A). The Category 1 bulletin explicitly describes conditions as "berbahaya kepada bot-bot kecil" — dangerous to small boats. This is a direct normative statement from the Malaysian authority responsible for marine safety guidance. No geographic adaptation is needed for Sabah waters. This is the strongest evidence in the repository.

**EV-02 — Rahim et al. (2024)** [[notes]](../../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) (Level C). 79 small-scale fishing households in coastal Makassar City, Indonesia. Three documented seasonal behavioral regimes: a fishing season with full operations (SAFE analog), an East season with heavy rainfall and restricted operations (CAUTION analog), and a West season with extreme wind and wave conditions and complete halt (UNSAFE analog). The East season documentation — reduced trip frequency and duration, near-shore only — is the most direct empirical evidence for rainfall-driven Delay in the repository.

**EV-03 — Gao (2024)** [[notes]](../../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) (Level C). 25 semi-structured interviews with Zone A gill net fishers in Penang. Tripartite informal classification: go (favourable conditions, full operations), cautious-go (marginal conditions, near-shore and shortened trips), don't go (adverse conditions). The cautious-go tier is the closest behavioral analog to the Delay advisory identified across all studies in the repository. Tide was rated the highest decision factor (4.55/5) — a finding that bears on the DepartureTime gap discussed below.

**EV-04 — Yamin et al. (2025)** [[notes]](../../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia.md) (Level C). 136 small-scale fishers across five Terengganu coastal villages. 95% identify wind and waves as the primary hazard; 91% identify erratic rainfall. The study documents a binary go/no-go behavioral pattern with flexibility as the weakest adaptive capacity domain (58% willingness to consider alternatives). That finding matters for the architecture's claim: flexibility is the weakest adaptive capacity domain in this population, which means the Delay advisory offers fishers a response they do not currently have, not one they already use.

**EV-05 — Jeong & Im (2023)** [[notes]](../../notes/Proposal%20of%20Restrictions%20on%20the%20Departure%20of%20Korea%20Small%20Fishing%20Vessel%20according%20to%20Wave%20Height.md) (Level C). Analysis of 66 capsizing incidents in Korean coastal waters (1999–2022). Vessel-length-dependent departure restriction thresholds derived from the Wolfson Unit formula. For vessels ≤10m LOA, caution proposed at Hs ≥ 1.0m. 38% of all capsizing incidents occurred at Hs ≤ 3m. This is the primary empirical evidence for wave-height-conditioned departure concern below Category 1 thresholds.

**EV-06 — Yaakob et al. (2015)** [[notes]](../../notes/Stability%2C%20Seakeeping%20and%20Safety%20Assessment%20of%20Small%20Fishing%20Boats%20Operating%20in%20Southern%20Coast%20of%20Peninsular%20Malaysia.md) (Level C). Naval architecture assessment of two traditional Malaysian small fishing boats from the Johor coast. Boat A (6.54m LOA) fails NORDFORSK seakeeping criteria at Hs ≈ 1.875m; operational limit approximately 1.25m. Boat B (5.03m LOA) operational limit approximately 0.5m. The only peer-reviewed seakeeping study of actual Malaysian small fishing vessels identified in the repository. Geographic limitation: Johor coast, not Sabah.

**EV-07 — Atacan and Düzbastılar (2023)** [[notes]](../../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) (Level C). Bridge navigation simulator study with 30 Turkish small-scale fishing vessel captains. Heavy weather (5 Beaufort, approximately 17–21 knots sustained wind) substantially elevated accident probability and consequence ratings. The 5 Beaufort lower bound approaches the g_w CAUTION threshold at 21.6 knots. Primarily relevant to g_t and g_w classification logic but provides secondary support for wind-driven Delay.

**EV-08 — dataset-label-derivation.md** (internal synthesis — not an independent empirical source). This document synthesizes EV-02, EV-03, and EV-04 into training label logic for the ML classifier. Section 4 maps: SAFE conditions to Go labels; CAUTION conditions (across four antecedent types) to Delay labels; UNSAFE conditions to AI-off. Section 6.3 defers DepartureTime and Duration label derivation to RQ5 fieldwork. EV-08 provides internal design lineage showing how the project previously synthesized EV-02, EV-03, and EV-04 into Go/Delay label logic. It does not add independent empirical evidence beyond those three sources. See §12 (EV-08 Evidence Status) for the full reclassification.

**EV-09 — appendix-c-formalisation.md semantic definitions** (Level D — definitional only). Section C.4 defines the formal semantic content of Go, Delay, DepartureTime, and Duration. These definitions constrain the meaning of each advisory type but supply no antecedent conditions. They were used for semantic bounding, not for rule justification.

---

## 5. Candidate Rules Derived

### RS_candidate(SAFE)

One candidate rule was identified:

**R-SAFE-001** — IF all five component classifiers return SAFE (g_w(w) == SAFE ∧ g_r(r, κ) == SAFE ∧ g_m(m) == SAFE ∧ g_o(o, v) == SAFE ∧ g_t(t, date) == SAFE) THEN Go.

Status: **CONDITIONALLY SUPPORTED**. Evidence: EV-02, EV-03, EV-04. Evidence level: Level C.

The rule was not derived from the state designation alone. R-REJ-001 documents the rejected version — "IF S == SAFE THEN Go" — which has only architectural permission as its basis. R-SAFE-001 differs: three independent empirical studies (Rahim Fishing season, Gao go tier, Yamin SAFE-equivalent operations) document that favourable operating conditions are associated with fishers proceeding to sea. The canonical all-SAFE antecedent — requiring all five component classifiers in their SAFE bands — is an architecture-level operationalisation of this broader empirical pattern. The studies do not directly observe the exact canonical conjunction; that operationalisation is a design inference.

One limitation deserves attention. The antecedent of R-SAFE-001 is functionally equivalent to S == SAFE: the rule fires when and only when every component is in its SAFE band, which is the defining condition for state SAFE. The risk is MODERATE rather than disqualifying — the empirical grounding is independent of the Layer 2 classification logic. The thresholds coincide because they share the same empirical sources.

Adaptation to Kota Kinabalu conditions from Indonesia, Penang, and Terengganu is required before this rule can be claimed as locally validated.

### RS_candidate(CAUTION)

Four candidate rules were identified:

**R-CAUTION-001** — IF m == advisory THEN Delay.

Status: **CONDITIONALLY SUPPORTED**. Evidence: EV-01 (MET Malaysia Category 1). P_ENV: Level A. P_ADV: Level C (inferred). MET Malaysia's Category 1 bulletin names small boats as the at-risk population and applies to Malaysian waters including Sabah without geographic adaptation — this is the strongest P_ENV evidence in the repository. However, MET does not explicitly prescribe 'delay departure' as the operational response; the Delay advisory is the standard maritime response to an active danger warning, but this inference step is required. Status is CONDITIONALLY SUPPORTED: Level A grounds the environmental premise; the advisory mapping is inferred. See §11 (Evidence Decomposition) for detail.

**R-CAUTION-002** — IF g_o(o, v) == CAUTION THEN Delay.

Status: **CONDITIONALLY SUPPORTED**. Evidence: EV-05, EV-06, EV-08. Evidence level: Level C. The Korean departure restriction framework (Jeong & Im 2023) and the Malaysian vessel seakeeping study (Yaakob et al. 2015) both establish operability concerns within the wave height range corresponding to the small-vessel CAUTION band (1.0–1.25m for small vessels). Geographic and vessel-type adaptation is required.

**R-CAUTION-003** — IF g_r(r, κ) == CAUTION THEN Delay.

Status: **CONDITIONALLY SUPPORTED**. Evidence: EV-02, EV-08. Evidence level: Level C. Rahim et al. (2024) East season documents restricted operations driven primarily by heavy rainfall at rates consistent with the CAUTION band (> 10.0 mm/hr). The East season fishers reduced trip frequency and shifted to near-shore operations — the behavioral pattern most closely analogous to a Delay advisory. The internal note about the source's internally contradictory wind speed description (vigorous winds vs. 5 knots) was verified against the source: heavy rainfall is confirmed as the primary driver, not wind.

**R-CAUTION-004** — IF g_w(w) == CAUTION THEN Delay.

Status: **CONDITIONALLY SUPPORTED**. Evidence: EV-03, EV-07, EV-08. Evidence level: Level C. Gao (2024) cautious-go pattern and Atacan and Düzbastılar (2023) heavy weather risk perception both support restricted operations under wind conditions approaching or within the CAUTION band (21.6–27.0 knots). The empirical base for this rule is weaker than for R-CAUTION-002 and R-CAUTION-003; the studies are more geographically distant from Sabah and the wind evidence is partly inferential.

### RS(UNSAFE)

Confirmed empty. RS_candidate(UNSAFE) = ∅. The UNSAFE state disables Layer 3 entirely (G(UNSAFE) = 0). No rule specification is needed or appropriate.

### Rejected Candidates

Five candidate patterns were considered and rejected:

- **R-REJ-001** — "IF S == SAFE THEN Go": state restatement with no independent evidence
- **R-REJ-002** — "IF S == CAUTION THEN Delay": state restatement with no independent evidence  
- **R-REJ-003** — "IF wave > CAUTION threshold THEN Delay [in SAFE state]": structurally impossible — the antecedent implies CAUTION, not SAFE
- **R-REJ-004** — "IF sunrise THEN DepartureTime": sunrise is the Layer 2 g_t SAFE onset boundary; repurposing it as a departure time recommendation requires independent advisory-level evidence, which was not found
- **R-REJ-005** — "IF sunset THEN Duration": the daylight window (sunset minus departure) is not a trip duration recommendation without evidence that fishers should fill the daylight window — which was not found

---

## 6. What the Evidence Does Not Support

### DepartureTime — OPEN-L3-1C

The repository contains no scientific authority for recommending a specific departure time to Kota Kinabalu Zone A fishers. The clearest evidence about departure timing is actually negative: Gao (2024) rates tide as the highest decision factor (4.55/5) and notes tide-gated port access, which suggests departure timing is port-specific and tide-dependent — not sunrise-dependent. Tide is not in E vector. dataset-label-derivation.md Section 6.3 defers DepartureTime labeling to RQ5 fieldwork.

The gap is recorded as OPEN-L3-1C and GAP-01. Closing it requires domain expert elicitation from Kota Kinabalu Zone A fishers, or tidal almanac data for the site sufficient to derive tide-conditioned departure window recommendations.

### Duration — OPEN-L3-1D

No scientific authority for recommending a safe trip duration to Zone A fishers under SAFE state conditions was identified. The duration evidence in the repository (Rahim et al. 2024: 7–10 hours reduced to 3–5 hours under extreme weather) comes from UNSAFE-equivalent conditions when Layer 3 does not operate. No study provides duration guidance within SAFE state. dataset-label-derivation.md Section 6.3 explicitly defers Duration to RQ5 fieldwork.

The gap is recorded as OPEN-L3-1D and GAP-02.

### Go in CAUTION state

All three behavioral studies (Rahim, Gao, Yamin) map CAUTION-equivalent conditions to restricted or halted operations, not to full proceeding. The repository contains no evidence for a Go advisory under CAUTION conditions. A tension exists with appendix-c-formalisation.md line 791, which states "When S = CAUTION the Go recommendation is automatically presented by the system with a caution qualifier" — this conflicts with the empirical mapping and is recorded as GAP-03. That passage appears to be a presentation layer note rather than a rule specification, though the interpretation was not resolved in Batch 2.

---

## 7. Rule Conflict Analysis

The conflict analysis covered seven scenarios. No conclusion-type contradiction was identified in the current candidate rule set:

- No Delay rule exists in RS_candidate(SAFE), so Go + Delay within SAFE is not possible under the current candidate set
- Multiple Delay rules in RS_candidate(CAUTION) are compatible — they produce the same conclusion type with distinct explanations, giving the fisher more information about why delay is warranted
- Cross-state conflict (Go in SAFE, Delay in CAUTION) is architecturally impossible — each episode has exactly one S value and uses exactly one RS(S)

Note: when multiple CAUTION rules fire simultaneously, all produce Delay — no type-level conflict arises. Advisory aggregation policy (which Delay explanation to surface, whether multiple explanations are merged, how duplicate presentations are handled) is an implementation-level question not addressed by Batch 2.

One boundary condition worth recording: if a Delay rule is ever added to RS(SAFE) — for example, to handle sub-CAUTION wave conditions approaching the boundary — Go and Delay could fire simultaneously within the same episode, which would require an advisory conflict policy. No such rule exists in the current candidate set; CONF-005 records it for future reference.

---

## 8. Limitations of the Candidate Rules

Three limitations apply to the candidate set as a whole:

**Geographic adaptation required.** All Level C candidate rules (R-SAFE-001, R-CAUTION-002, R-CAUTION-003, R-CAUTION-004) draw on studies from Indonesia, Penang (West Malaysia), Terengganu (East Malaysia), Korea, Johor (South Malaysia), and Turkey. None directly studied Kota Kinabalu (Sabah, East Malaysia) Zone A fishers. The wave and weather regimes, vessel configurations, and operational practices may differ. These rules are conditionally supported, not locally validated.

**Marine warning data absent.** R-CAUTION-001 carries the strongest environmental-premise authority in the candidate set (P_ENV Level A — MET Malaysia Category 1) but is CONDITIONALLY SUPPORTED overall: the advisory mapping from MET's danger statement to the Delay recommendation requires an explicit inference step (P_ADV Level C inferred). R-CAUTION-001 cannot be empirically tested on the historical replay data. No marine warning archive exists for the study site; m is held at none throughout all 43,848 replay hours (D = {m}). The empirical binding rate of R-CAUTION-001 is unknown. All reported Level 2 binding rates are lower bounds.

**Classifier duplication risk.** The thresholds used in the antecedents of R-CAUTION-002, R-CAUTION-003, and R-CAUTION-004 coincide with the Layer 2 CAUTION classification boundaries. The risk is MODERATE rather than disqualifying, but it means the Layer 3 advisory rules at these thresholds do not add new environmental information — they confirm what Layer 2 already determined. The independent value comes from the explanation content and recommendation type, not from threshold novelty.

---

## 9. What Remains Open

After Batch 2, the following items remain open:

| Item | Status | What blocks it |
|---|---|---|
| OPEN-L3-1C | OPEN | DepartureTime — requires RQ5 fieldwork or tidal data |
| OPEN-L3-1D | OPEN | Duration — requires RQ5 fieldwork or DoF Malaysia guidelines |
| OPEN-L3-2 | OPEN (unchanged) | Predicate evaluation failure policy — blocks implementation, not specification |
| OPEN-L3-3 | **CLOSED (2026-09-11) — Resolution B** | CAUTION-Go presentation vs. rule semantics — RESOLVED (Interpretation B, presentation qualifier only). Appendix C §C.4 line 791 clarified under task §15 permission. Full evidence: `open-l3-3-resolution/`. |
| OPEN-B1-1 | OPEN (unchanged) | Freshness parameters (age_i) |
| OPEN-B1-6 | OPEN (unchanged) | Latency threshold H3 |

Batch 3 engine implementation is unblocked on the OPEN-L3-3 axis; other Batch 3 gating conditions (OPEN-L3-1C, OPEN-L3-1D, OPEN-L3-2) remain in force independently.

The current Batch 2 candidate set specifies conditionally supported Go/Delay rule candidates. RS_candidate(CAUTION) remains Delay-only under current scientific evidence — Go remains admissible in A_AI(CAUTION) but is not currently rule-supported. Presentation layer must attach a caution qualifier to any Go advisory produced when S = CAUTION. DepartureTime and Duration remain OPEN-L3-1C and OPEN-L3-1D respectively — both require additional domain evidence.

---

## 10. Closure

**Closure line:** JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 CLOSED — CAUTION-GO PRESENTATION SEMANTICS RESOLVED

*(Historical — superseded: JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN — CAUTION ADVISORY SEMANTICS REQUIRE AUTHORITY RESOLUTION. Superseded 2026-09-11 by OPEN-L3-3 Resolution B.)*

Semantic verification: 90 PASS / 0 FAIL / 0 OPEN / 90 checks total. The OPEN-L3-3 tracking check transitioned OPEN → PASS on 2026-09-11 after Resolution B — see §13 and `open-l3-3-resolution/verification.json` (which carries the resolution's own 23-check verification set, all PASS).

**RS_candidate(SAFE)** = {R-SAFE-001 (Go, CONDITIONALLY SUPPORTED, Level C)}  
**RS_candidate(CAUTION)** = {R-CAUTION-001 (Delay, CONDITIONALLY SUPPORTED, P_ENV Level A / P_ADV Level C), R-CAUTION-002 (Delay, CONDITIONALLY SUPPORTED, Level C), R-CAUTION-003 (Delay, CONDITIONALLY SUPPORTED, Level C), R-CAUTION-004 (Delay, CONDITIONALLY SUPPORTED, Level C)}  
**RS(UNSAFE)** = ∅

Full artefact set: `data/journal1-layer3-prototype/` (batch2 CSV files, semantic-verification-batch2.json, change-map-batch2.csv, closure-batch2.json).  
Authority document: `publications/active/journal-1/layer3-prototype-specification.md` §§16–27.

---

## 11. Evidence Decomposition by Rule (Final Repair §31)

| Rule | Environmental premise | P_ENV level | Advisory conclusion | P_ADV level | Inference bridge required | Overall status |
|---|---|---|---|---|---|---|
| **R-SAFE-001** | Favourable operating conditions are associated with fishers proceeding to sea (Rahim Fishing season, Gao go tier, Yamin SAFE-equivalent ops). The all-SAFE antecedent operationalises this broader empirical pattern. | Level C | Go advisory — behavioral analog of proceeding under favourable conditions | Level C | YES — broader favourable-conditions behaviour → canonical all-SAFE operationalisation → Go advisory candidate | CONDITIONALLY SUPPORTED |
| **R-CAUTION-001** | MET Category 1: 'berbahaya kepada bot-bot kecil' — conditions dangerous to small boats | Level A | Delay advisory — standard maritime response to active danger warning | Level C (inferred) | YES — danger warning → delay departure is standard maritime safety practice, not explicit MET text | CONDITIONALLY SUPPORTED |
| **R-CAUTION-002** | Wave height in CAUTION band causes capsizing risk (Jeong & Im) and seakeeping operability failure (Yaakob et al.) for small vessels | Level C | Delay advisory — operability restriction → delay departure inference | Level C | YES — departure restriction/operability concern ≠ Delay without explicit bridge | CONDITIONALLY SUPPORTED |
| **R-CAUTION-003** | Heavy rainfall causes restricted fishing operations, near-shore constraint, reduced trip frequency (Rahim East season) | Level C | Delay advisory — restricted behavior behavioral analog | Level C | YES — restricted behavior ≠ Delay departure advisory without inference | CONDITIONALLY SUPPORTED |
| **R-CAUTION-004** | Elevated wind associated with cautious-go behavior (Gao) and elevated accident risk (Atacan) | Level C | Delay advisory — elevated risk perception → delay inference (weakest bridge) | Level C | YES — cautious-go could map to either Go-with-qualifier or Delay; see OPEN-L3-3 | CONDITIONALLY SUPPORTED |

---

## 12. EV-08 Evidence Status (Final Repair §32)

EV-08 (dataset-label-derivation.md) is an internal project synthesis document. It synthesizes EV-02 (Rahim et al. 2024), EV-03 (Gao 2024), and EV-04 (Yamin et al. 2025) into Go/Delay label logic for the ML training dataset.

EV-08 is not a fourth independent empirical source. Any claim resting solely on EV-08 reduces to a claim from EV-02, EV-03, or EV-04. Earlier Batch 2 artefacts listed EV-08 alongside the three underlying studies as a primary evidence source, which gave the false impression that four independent sources converge on the Go and Delay mappings. This repair removes EV-08 from all primary evidence lists; it now appears only as internal design lineage.

**Corrected primary evidence after Final Repair:**
- R-SAFE-001: EV-02, EV-03, EV-04 (EV-08 removed)
- R-CAUTION-001: EV-01 (unchanged — EV-08 was not listed)
- R-CAUTION-002: EV-05, EV-06 (EV-08 removed)
- R-CAUTION-003: EV-02 (EV-08 removed)
- R-CAUTION-004: EV-03, EV-07 (EV-08 removed)

---

## 13. Appendix C CAUTION-Go Authority Resolution (Final Repair §33)

**Exact statement:** Appendix C §C.4, line 791 of `appendix-c-formalisation.md`:

> "When S = CAUTION, the **Go** recommendation is automatically presented by the system with a caution qualifier (e.g., 'Proceed with caution'). The recommendation type remains **Go**, but its presentation and explanation are modified by the safety state. This preserves set containment while allowing state‑dependent advisory messaging."

**Context:** The statement appears within the A_AI(S) set-definition section of Appendix C, immediately following the three-row A_AI table ({Go, Delay, DepartureTime, Duration} / {Go, Delay} / ∅). The surrounding section establishes that Go ∈ A_AI(CAUTION) — i.e., Go is in the admissible set for CAUTION state — and this statement elaborates on how Go would be presented if produced.

**Authority classification: B (UI/presentation guidance)** — the working interpretation. The statement describes how Go should be rendered at the presentation layer if produced by Layer 3 rules, not that Go is mandated in every CAUTION episode. Interpretation B is consistent with the set-definition context: A_AI(CAUTION) = {Go, Delay} establishes that Go is permitted but not mandatory.

**Residual ambiguity:** The phrase "automatically presented" is grammatically ambiguous. Under interpretation B (correct), it means "when Layer 3 rules produce Go in CAUTION state, the system presents it with a caution qualifier." Under interpretation A (normative), it means "the system always shows Go in CAUTION state regardless of rule engine output." Interpretation A would conflict with the empirical finding that all three behavioral studies map CAUTION conditions to Delay analogs, not Go.

**Normative impact on RS(CAUTION):** Under interpretation B, there is no normative impact — the statement is a UI rendering instruction and does not populate RS(CAUTION). Under interpretation A, a Go rule would be required in RS(CAUTION), which has no empirical basis in the repository.

**Resolution (2026-09-11):** OPEN-L3-3 CLOSED under Resolution B (Interpretation B — presentation qualifier only). The separate design decision Batch 2 deferred was executed as the OPEN-L3-3 resolution task, using provenance (line 791 predates the Layer 3 rule-based enforcement mechanism by 15 days but was retained through 8 subsequent §C.4 revisions), the parallel canonical text in `architecture-illustration.md` §202–204 (which frames the qualifier unambiguously as presentation-layer messaging), Algorithm 4's absence of any post-hoc emission branch, and Batch 2's own Go semantics ("no active Delay antecedent"). The minimal Appendix C clarification permitted by task §15 was applied: line 791 now reads *"any Go advisory generated by the active Layer 3 rule set is presented with a caution qualifier"* in place of *"the Go recommendation is automatically presented by the system with a caution qualifier"*. Formal semantics: `S = CAUTION ∧ Go ∈ AI(E) → Present(Go, caution_qualifier)`. No CAUTION-Go rule invented; RS_candidate(CAUTION) remains Delay-only; A_AI(CAUTION) = {Go, Delay} unchanged; Algorithm 3/4 and Safety Dominance unchanged.

**Resolution evidence set:** `data/journal1-layer3-prototype/open-l3-3-resolution/` — authority-trace.csv, semantic-decomposition.md, decision-matrix.csv, resolution.json, verification.json (23 checks all PASS), report.md.

**Remaining OPEN item:** none from OPEN-L3-3. OPEN-L3-1C, OPEN-L3-1D, OPEN-L3-2 remain OPEN independently as recorded in `layer3-prototype-specification.md` §26.

**Batch 3 implication:** OPEN-L3-3 blocks CAUTION advisory behaviour in Batch 3. A later task must resolve OPEN-L3-3 before Batch 3 engine implementation begins. Implementing SAFE-only or Delay-only paths does not route around this block without explicit authorisation.

---

## 14. CSV Integrity (Final Repair §30)

| File | header_width | data_row_count | min_row_width | max_row_width | Verdict |
|---|---|---|---|---|---|
| `rule-candidate-register-batch2.csv` | 23 | 10 | 23 | 23 | **PASS** |
| `rule-evidence-matrix-batch2.csv` | 13 | 9 | 13 | 13 | **PASS** |

The Final Repair rewrote both files using Python's `csv.writer` with `QUOTE_ALL` quoting. The prior repair had left R-CAUTION-001 at 18 columns (unescaped comma in `conflict_risk`) and R-REJ-003/004/005 at 14–15 columns (missing `limitation` column after a column shift). Both failures are now fixed. The candidate register grew from 16 to 23 columns with 7 new P_ENV/P_ADV distinction fields.
