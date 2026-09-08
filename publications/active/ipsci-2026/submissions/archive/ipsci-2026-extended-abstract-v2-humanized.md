# A GRADUATED SAFETY-STATE-GATED ARCHITECTURE FOR AI DECISION SUPPORT IN LOW-RESOURCE COASTAL FISHERIES

*(Times New Roman, 14pt, Bold, All Caps, Centered)*

---

**Iskandar Samsuddin \*1**

1 [Department], [Faculty], [University], Malaysia  
\* Corresponding author: iskandarsamsuddin@gmail.com

---

***Abstract:*** Small-scale coastal fishers in Malaysia make safety-critical departure decisions without institutional support, yet every AI governance architecture identified in this review handles intermediate-risk conditions the same way: full output, or none. This paper proposes a graduated safety-state-gated architecture that fills this gap through a two-level governance pair: a participation gate G(S) that enables or disables the AI, and an admissible recommendation space A_AI(S) that defines what the AI may output. Both are conditioned on a classified safety state S = f(E), where E = {w, r, m, o, v, t} captures wind speed, rainfall intensity, marine warning level, ocean state, vessel category, and time of day. Three governance modes follow: SAFE (full advisory scope), CAUTION (Go and Delay only), and UNSAFE (AI silent). These enforce the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S) by construction. The work follows a Design Science Research methodology across five phases: architecture design, formal specification, prototype implementation, three-condition comparative evaluation, and contextual user validation with fishers in coastal Malaysia. The architecture uses a symbolic rule-based engine with formal safety guarantees, runs offline on smartphone-class hardware, and introduces a formally specified intermediate CAUTION mode with no identified precedent in the literature.

***Keywords:*** AI governance, safety-state gating, decision support, coastal fisheries, low-resource deployment

---

## 1. INTRODUCTION

Each morning, 89,000 registered small-scale fishers along Malaysia's coastline face a safety-critical decision: go to sea or stay ashore [1, 17]. They make this decision alone, without institutional support, on vessels under 40 GRT restricted to 0–5 nautical miles from shore, relying on traditional weather knowledge that is eroding as climate patterns become less predictable [1, 18]. AI could help, but existing governance offers only two settings: full recommendations or complete shutdown. This paper introduces a third mode, CAUTION, where AI advises within formally restricted scope. Dominguez-Péry et al. found that wind, weather, and visibility form the largest single maritime risk cluster across IMO accident reports (26.7%), with small vessels recording the highest mean fatality rank [2]. Atacan and Düzbastılar [13] found risk perception scores lowest among the smallest vessel operators — the same population Gao [14] identifies as relying primarily on peer weather knowledge when institutional forecasts are unavailable. The space between full AI advisory and no AI advisory is where most of those decisions happen.

Three independent surveys of AI governance literature confirm the pattern. Indykov et al. [3] reviewed 206 papers across 16 architectural tactics for machine-learning-enabled systems. Shamsujjoha et al. [4] mapped 13 guardrail actions across 32 studies. Perez-Cerrolaza et al. [5] examined 294 references from automotive, avionics, railway, and industrial domains. Across all three, no mechanism was identified that conditions AI advisory scope on classified environmental safety state. Flehmig et al. [6], the closest structural precedent, propose a three-level traffic-light degradation index; their intermediate (orange) level governs supervisory behaviour but leaves AI advisory output unchanged. Haque and Al Jufaili [7] confirmed the same absence across four fisheries AI application domains.

The gap is an admissible recommendation space A_AI(S) that contracts as operational risk increases. This research defines that space formally, through a graduated safety-state-gated architecture grounded in Guaranteed Safe AI principles [8] and Bloomfield and Rushby's dependability framework [9]. Belle [19] argues that symbolic reasoning is the right foundation for systems that require formal guarantees. Hildebrandt et al. [20] apply the same separation principle in legal AI, using a rule engine to govern what a bounded reasoning layer may output. Neither system, however, conditions advisory scope on classified environmental safety state. This research does, and makes three concrete contributions: a formally specified governance pair (G(S), A_AI(S)) with no identified precedent; an offline-capable, smartphone-class implementation designed from the constraints of low-resource deployment; and a three-condition comparative evaluation that isolates the safety value of Level 2 governance as a variable.

---

## 2. METHODOLOGY

The research follows a Design Science Research (DSR) methodology [10], structured across five phases. The five research questions guiding this work are:

RQ1: How can a three-mode hybrid AI decision architecture be designed such that AI participation is graduated based on classified environmental safety state?

RQ2: What formal specification ensures the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S)?

RQ3: How can a functional prototype be implemented under the constraints of small-scale coastal fisheries?

RQ4: How does the proposed graduated architecture compare to binary-gated and ungated baselines in terms of Safety Dominance Property compliance?

RQ5: How do small-scale fishers perceive, interpret, and respond to the three-state governance architecture?

Phases 1 and 2 — architecture design (RQ1) and formal specification (RQ2) — are complete.

### 2.1 Architecture Design (RQ1)

The governance pipeline is formalised as:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision**

```
┌──────────────────────────────────────────────────────┐
│  Layer 1: Environmental Sensing                      │
│  E = {w, r, m, o, v, t}                             │
└──────────────────────────────────────────────────────┘
                          ▼
┌──────────────────────────────────────────────────────┐
│  Layer 2: Deterministic Safety-State Gating          │
│  S = f(E) → (G(S), A_AI(S))                         │
│  States: SAFE / CAUTION / UNSAFE                     │
└──────────────────────────────────────────────────────┘
                          ▼
┌──────────────────────────────────────────────────────┐
│  Layer 3: AI Advisory Reasoning Engine               │
│  Rule-Set Starvation: RS(SAFE) or RS(CAUTION)        │
└──────────────────────────────────────────────────────┘
                          ▼
┌──────────────────────────────────────────────────────┐
│  Layer 4: Human Decision                             │
│  Fisher retains final authority                      │
└──────────────────────────────────────────────────────┘
```

**Figure 1.** Four-layer graduated safety-state-gated governance architecture.

**Environmental sensing (Layer 1).** The state vector E = {w, r, m, o, v, t} captures: wind speed (w, knots), rainfall intensity (r, ordinal), marine warning level (m, ordinal), ocean state (o, wave height × swell period), vessel category (v, ordinal), and time of day (t, 24-hour). All six inputs are locally observable without specialised instrumentation.

**Deterministic safety-state gating (Layer 2).** S = f(E) applies worst-case aggregation: the single most dangerous parameter determines S. The governance pair (G(S), A_AI(S)) enforces two levels of control, as shown in Table 1.

| Safety State | G(S) | A_AI(S) | AI Advisory Scope |
|---|---|---|---|
| SAFE | 1 (enabled) | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 (enabled) | {Go, Delay} | Restricted |
| UNSAFE | 0 (disabled) | ∅ | None |

**Table 1.** Governance configuration by safety state.

The containment property holds: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. Parameter-level thresholds, derived from MET Malaysia Category 1 small craft warning criteria, are in Table 2.

| Parameter | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| Wind speed (w) | ≤ 15 kn | 15–25 kn | > 25 kn |
| Rainfall intensity (r) | ≤ 5 mm/hr | 5–15 mm/hr | > 15 mm/hr |
| Marine warning (m) | None | Category 2 | Category 3+ |
| Wave height (o) | ≤ 1.0 m | 1.0–2.0 m | > 2.0 m |
| Vessel category (v) | ≥ 15 GRT | 5–15 GRT | < 5 GRT |
| Time of day (t) | 0600–1800 | Any | — |

**Table 2.** Per-parameter safety state thresholds (MET Malaysia Category 1 criteria).

RS(SAFE) contains production rules generating {Go, Delay, DepartureTime, Duration}; RS(CAUTION) is a strict subset containing only rules generating {Go, Delay}. Exact rule counts are established during Phase 3 prototype implementation.

**AI advisory reasoning (Layer 3).** Layer 2 acts as a logical oracle: it supplies only the rule set RS(S) to Layer 3 before any reasoning begins. Belle [19] argues that symbolic reasoning is the right foundation where formal guarantees are required, and this architecture exploits exactly that. Hildebrandt et al. [20] apply the same principle in legal AI, using a rule engine to control what a bounded interface may output. Layer 3 is a rule-based engine. Under CAUTION, Layer 2 supplies RS(CAUTION), which contains no production rules capable of generating DepartureTime or Duration. The engine fires only what is in its active rule set, so AI(E) ⊆ A_AI(S) holds not because output is filtered after generation, but because no rule generating a disallowed type exists in that configuration. That is what makes the guarantee architectural rather than empirical.

**Human decision (Layer 4).** Final decision authority remains with the fisher. The governance layer is non-AI and deterministic, running at O(1) complexity on smartphone-class hardware with no connectivity requirement — the design floor Katende [16] identifies as characteristic of low-resource deployment settings.

### 2.2 Prototype and Technical Evaluation (RQ3–RQ4)

The functional prototype (Phase 3) is calibrated against a 2020–2024 historical Malaysian coastal weather dataset sourced from MET Malaysia (60 months of continuous sequential records). k-means clustering confirms whether natural coastal weather variances map onto the f(E) classification boundaries before threshold values are finalised.

Technical evaluation (Phase 4) uses a three-condition comparison. C0 is the ungated baseline: no governance, full advisory output regardless of safety state. C1 is the binary-gated baseline: Level 1 participation gate only; A_AI is always full when G(S) = 1. C2 is the proposed two-level graduated architecture. All 60 months of weather vectors are replayed chronologically through all three configurations. The primary metric is Safety Dominance Property compliance under C2. The discriminating test is C1 vs. C2 under CAUTION, quantified by the Advisory Scope Violation Rate (ASVR): the proportion of recommendations falling outside A_AI(CAUTION) = {Go, Delay} when S = CAUTION. C1 is predicted to produce a positive ASVR; C2 is predicted to produce ASVR = 0 by construction. Since C1 and C2 are identical at Level 1, any difference in ASVR is attributable entirely to Level 2 governance.

### 2.3 Contextual User Validation (RQ5)

The user study (Phase 5) recruits small-scale fishers and fisheries officers in coastal Malaysia (Terengganu and/or Penang) via LKIM district offices (target n = 12–15, sufficient for pattern confirmation across all three safety states). Each session runs 60–75 minutes. Participants view the system interface under each safety state in sequence, then complete verbal comprehension checks (Q1: state perception; Q2: scope interpretation), scenario-based departure decision tasks (Q3: decision behaviour), and the Short Trust in Automation Scale (S-TIAS [11], derived from Jian et al. [15]; α = 0.97) after each state.

---

## 3. RESULTS & DISCUSSION

Phases 1 and 2 are complete. The environmental state vector E, safety state function S = f(E), governance pair (G(S), A_AI(S)), and Safety Dominance Property have all been formally specified. The proof by construction of AI(E) ⊆ A_AI(S) is established via Rule-Set Starvation. Phases 3–5 are in progress.

### 3.1 Expected Technical Results

Table 3 summarises the predicted advisory output by configuration and safety state.

| | C0 (Ungated) | C1 (Binary-Gated) | C2 (Graduated) |
|---|---|---|---|
| SAFE | Full advisory | Full advisory | Full advisory |
| CAUTION | Full advisory | Full advisory | Restricted {Go, Delay} |
| UNSAFE | Full advisory | No advisory | No advisory |
| ASVR under CAUTION | Positive | Positive | Zero |

**Table 3.** Predicted advisory output by system configuration and safety state.

C2 should achieve ASVR = 0 across all 60 months of historical weather data, demonstrating 100% Safety Dominance Property compliance. This prediction follows from the proof in Section 2.1, not from expected empirical behaviour. C1 will produce a positive ASVR under CAUTION, generating DepartureTime and Duration where A_AI(CAUTION) = {Go, Delay} forbids them. Flehmig et al. [6] found that their intermediate level changes supervisory activity but not AI advisory output. Here, the difference between C1 and C2 under CAUTION is structural and shows up directly in the recommendation set.

### 3.2 Expected Contextual Results

Three hypotheses guide the user study. H1 (state perceptibility): ≥ 70% of participants will correctly identify the safety state from the display across all three conditions. H2 (CAUTION interpretability): ≥ 60% will correctly identify the CAUTION restriction as a scope limitation rather than a display change, coded against a predefined rubric. H3 (behavioural effect): more participants will choose Delay under CAUTION than under SAFE, and more will choose Go or Delay under CAUTION than under UNSAFE. Wen et al. [12] found that operators receiving full-scope AI output under deteriorating conditions tend toward over-reliance. H3 tests whether restricting advisory scope produces a conservative shift, and whether that effect is detectable within the sample. It remains to be seen whether the CAUTION restriction is legible to fishers without formal technical background — that is precisely what H2 is designed to test. S-TIAS [11] measures trust coherence across states.

---

## 4. CONCLUSION

The graduated safety-state-gated architecture presented here restricts AI advisory scope as classified environmental risk increases, introducing a formally specified intermediate CAUTION mode with no identified precedent in this review. The containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S) hold by construction. Technical evaluation and user study are pending. When complete, the combined result should constitute the first formally verified, offline-capable governance architecture in which AI advisory scope varies with classified operational risk, built specifically for the constraints of low-resource deployment. Future work includes integrating with real-time weather data streams and testing whether the architecture generalises to other safety-critical domains under similar resource constraints.

---

## ACKNOWLEDGEMENT

[Research grant, institutional affiliation, and scholarship acknowledgement to be completed.]

---

## REFERENCES

[1] L. Yamin, T.-C. Kuo, and N. Aziz, "Interplay of traditional knowledge and adaptive capacity in climate change adaptation of small-scale fishers in central Terengganu, Malaysia," *Frontiers in Marine Science*, vol. 12, p. 1492131, 2025. doi: 10.3389/fmars.2025.1492131

[2] C. Dominguez-Péry, R. Tassabehji, F. Corset, and Z. Chreim, "A holistic view of maritime navigation accidents and risk indicators: examining IMO reports from 2011 to 2021," *Journal of Shipping and Trade*, vol. 8, p. 11, 2023. doi: 10.1186/s41072-023-00135-y

[3] V. Indykov, D. Strüber, and R. Wohlrab, "Architectural tactics to achieve quality attributes of machine-learning-enabled systems: A systematic literature review," *Journal of Systems and Software*, vol. 223, p. 112373, 2025. doi: 10.1016/j.jss.2024.112373

[4] Md. Shamsujjoha, Q. Lu, D. Zhao, and L. Zhu, "Swiss cheese model for AI safety: A taxonomy and reference architecture for multi-layered guardrails of foundation model based agents," in *Proc. IEEE 22nd Int. Conf. Software Architecture (ICSA)*, 2025, pp. 37–48. doi: 10.1109/ICSA65012.2025.00014

[5] J. Perez-Cerrolaza et al., "Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey," *ACM Computing Surveys*, vol. 56, no. 7, Art. 176, 2024. doi: 10.1145/3626314

[6] N. Flehmig, M. A. Lundteigen, and S. Yin, "Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process," in *Proc. IEEE IECON 2024: 50th Annual Conf. IEEE Industrial Electronics Society*, 2024. doi: 10.1109/IECON55916.2024.10906021

[7] M. S. Haque and S. Al Jufaili, "Applications of artificial intelligence in fisheries: From data to decisions," *Reviews in Aquaculture*, 2026. doi: 10.1111/raq.12967

[8] D. Dalrymple et al., "Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems," *arXiv preprint arXiv:2405.06624*, 2024.

[9] R. Bloomfield and J. Rushby, *Assurance of AI Systems from a Dependability Perspective*, SRI Technical Report SRI-CSL-2024-02R3, SRI International, 2025. doi: 10.48550/arXiv.2407.13948

[10] K. Peffers, T. Tuunanen, M. A. Rothenberger, and S. Chatterjee, "A design science research methodology for information systems research," *Journal of Management Information Systems*, vol. 24, no. 3, pp. 45–77, 2007. doi: 10.2753/MIS0742-1222240302

[11] M. J. McGrath, O. Lack, J. Tisch, and A. Duenser, "Measuring trust in artificial intelligence: Validation of an established scale and its short form," *Frontiers in Artificial Intelligence*, vol. 8, p. 1582880, 2025. doi: 10.3389/frai.2025.1582880

[12] H. Wen, Z. Sajid, and R. Arunthavanathan, "Risk perception in complex systems: A comparative analysis of process control and autonomous vehicle failures," *AI*, vol. 6, no. 8, p. 164, 2025. doi: 10.3390/ai6080164

[13] C. Atacan and F. O. Düzbastılar, "Determination of risk perception in small-scale fishing and navigation," *Ege Journal of Fisheries and Aquatic Sciences*, vol. 40, no. 1, pp. 1–14, 2023. doi: 10.12714/egejfas.40.1.01

[14] T. Gao, "Mapping the decision-making factors of small-scale fishers: A case study of Penang," M.Sc. thesis, University of Pisa/WorldFish, CGIAR Repository, 2024. [Online]. Available: https://hdl.handle.net/10568/152289

[15] J.-Y. Jian, A. M. Bisantz, and C. G. Drury, "Foundations for an empirically determined scale of trust in automated systems," *International Journal of Cognitive Ergonomics*, vol. 4, no. 1, pp. 53–71, 2000. doi: 10.1207/S15327566IJCE0401_04

[16] A. Katende, "Rethinking data-efficient artificial intelligence for low-resource settings," *AI & Society*, 2026. doi: 10.1007/s00146-026-01234-5

[17] C. Obi et al., "Overview of the fishery and aquaculture sectors in Malaysia," *Frontiers in Sustainable Food Systems*, vol. 9, p. 1545263, 2025. doi: 10.3389/fsufs.2025.1545263

[18] Abd. Rahim et al., "Survival decisions and adaptation strategies of small-scale fishers in the face of extreme weather impacts in coastal areas," *Journal of Marine and Island Cultures*, vol. 13, no. 3, 2024. doi: 10.21463/jmic.2024.13.3.05

[19] V. Belle, "On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning," *Neurosymbolic Artificial Intelligence*, vol. 1, p. 29498732251339951, 2025. doi: 10.1177/29498732251339951

[20] T. Hildebrandt et al., "XHAILe: Explainable Hybrid AI for Computational Law and Accurate Legal Chatbots," in *Proc. 38th Int. Conf. Advanced Information Systems Engineering (CAiSE'26)*, CEUR-WS, 2026.
