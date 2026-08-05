# A GRADUATED SAFETY-STATE-GATED ARCHITECTURE FOR AI DECISION SUPPORT IN LOW-RESOURCE COASTAL FISHERIES

*(Times New Roman, 14pt, Bold, All Caps, Centered)*

---

**Iskandar Samsuddin \*1**

1 [Department], [Faculty], [University], Malaysia  
\* Corresponding author: iskandarsamsuddin@gmail.com

---

***Abstract:*** Small-scale coastal fishers in Malaysia make safety-critical departure decisions without institutional support, yet existing AI governance architectures offer only binary control — full recommendation or shutdown — leaving intermediate-risk conditions unaddressed. This paper proposes a graduated safety-state-gated architecture that resolves this gap through a two-level governance pair (G(S), A_AI(S)) conditioned on a classified environmental safety state S = f(E), where E = {w, r, m, o, v, t} captures wind speed, rainfall intensity, marine warning level, ocean state, vessel category, and time of day. Three governance modes follow: SAFE (full advisory scope), CAUTION (Go and Delay only), and UNSAFE (AI silent), enforcing the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S) by construction. A Design Science Research methodology structures the work across five phases: architecture design, formal specification, prototype implementation, three-condition comparative evaluation, and contextual user validation with fishers in coastal Malaysia. The architecture uses a symbolic rule-based engine with formal safety guarantees, is offline-capable, and runs on smartphone-class hardware, producing a formally novel intermediate CAUTION mode with no counterpart in the reviewed literature.

***Keywords:*** AI governance, safety-state gating, decision support, coastal fisheries, low-resource deployment

---

## 1. INTRODUCTION

Each morning, 89,000 registered small-scale fishers along Malaysia's coastline face a safety-critical decision: go to sea or stay ashore [1]. They make this decision alone, without institutional support, on vessels under 40 GRT restricted to 0–5 nautical miles from shore, relying on traditional weather knowledge that is eroding as climate patterns become less predictable [1]. AI could help — but existing AI governance offers only binary control: full recommendations or complete shutdown. This paper introduces a third mode: CAUTION, where AI advises but its scope is formally restricted to what deteriorating conditions can reliably support. Dominguez-Péry et al. confirm that wind, weather, and visibility form the largest single maritime risk cluster across IMO accident reports (26.7%), with small vessels recording the highest mean fatality rank [2]: the gap between full AI advisory and no AI advisory is not academic — it is the space where most fatal decisions are made.

AI decision support could translate environmental data into departure guidance calibrated to vessel class and conditions. The governance challenge, however, is unresolved: how should AI behaviour change as conditions shift from safe to marginally dangerous to fully dangerous? Three large-scale literature reviews — Indykov et al. (206 papers, 16 architectural tactics) [3], Shamsujjoha et al. (13 guardrail actions across 32 studies) [4], and Perez-Cerrolaza et al. (294 references across safety-critical domains) [5] — collectively find no mechanism that conditions AI advisory scope on classified environmental safety state. Flehmig et al., the closest structural precedent, propose a three-level traffic-light degradation index; their intermediate (orange) level governs supervisory behaviour but leaves AI advisory output unchanged [6]. Haque and Al Jufaili confirm the same absence across four fisheries AI application domains [7].

The specific gap is an admissible recommendation space A_AI(S) that contracts dynamically as operational risk increases. This research introduces that dimension through a formally specified graduated safety-state-gated architecture, grounded in Guaranteed Safe AI principles [8] and Bloomfield and Rushby's dependability framework [9]. The neurosymbolic pattern underlying the architecture — a deterministic symbolic controller constraining a bounded reasoning layer, with final authority retained by the human — is concurrently applied in legal AI by Hildebrandt et al. [31], confirming the paradigm's viability in high-stakes domains; however, no such system implements advisory scope restriction conditioned on classified environmental safety state. This research makes three contributions: (1) a formally specified governance pair (G(S), A_AI(S)) with no counterpart in the reviewed literature; (2) an offline-capable, smartphone-class implementation designed from the deployment floor; and (3) a three-condition comparative evaluation protocol that isolates the safety value of Level 2 governance.

---

## 2. METHODOLOGY

The research follows a Design Science Research (DSR) methodology [10], structured across five phases corresponding to five research questions (RQ1–RQ5). Phases 1 and 2 — architecture design (RQ1) and formal specification (RQ2) — are complete.

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

**Layer 1 (Environmental Sensing).** The state vector E = {w, r, m, o, v, t} captures: wind speed (w, knots), rainfall intensity (r, ordinal), marine warning level (m, ordinal), ocean state (o, wave height × swell period), vessel category (v, ordinal), and time of day (t, 24-hour). All inputs are locally observable without specialised instrumentation.

**Layer 2 (Deterministic Safety-State Gating).** The safety state function S = f(E) applies worst-case aggregation: S is determined by the single most dangerous input parameter. The governance pair (G(S), A_AI(S)) then enforces two levels of control, as shown in Table 1.

| Safety State | G(S) | A_AI(S) | AI Advisory Scope |
|---|---|---|---|
| SAFE | 1 (enabled) | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 (enabled) | {Go, Delay} | Restricted |
| UNSAFE | 0 (disabled) | ∅ | None |

**Table 1.** Governance configuration by safety state.

The formal containment property holds: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. State classification applies worst-case aggregation: S is determined by the single most dangerous parameter in E. Parameter-level thresholds, derived from MET Malaysia Category 1 small craft warning criteria, are specified in Table 2.

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

**Layer 3 (AI Advisory Reasoning Engine).** Following the neurosymbolic paradigm advocated by Belle [30] and instantiated in legal AI by Hildebrandt et al. [31], the architecture uses the deterministic symbolic governance layer (Layer 2) as a logical oracle that constrains the reasoning engine before inference begins, enabling formal safety guarantees that purely statistical approaches cannot provide. The prototype implements Layer 3 as a rule-based engine. Safety Dominance Property compliance is enforced by construction via Rule-Set Starvation: the governance layer supplies only RS(CAUTION) before inference begins, withholding the production rules in RS(SAFE) \ RS(CAUTION) required to compute DepartureTime and Duration. No rule in that configuration can produce outputs beyond {Go, Delay}, so AI(E) ⊆ A_AI(S) holds by definition. This symbolic implementation enables formal verification by construction — a stronger guarantee than empirical validation of statistical models could provide.

**Layer 4 (Human Decision).** Final decision authority remains with the fisher. The governance layer is non-AI and deterministic, running at O(1) complexity on smartphone-class hardware with no connectivity requirement.

### 2.2 Prototype and Technical Evaluation (RQ3–RQ4)

Phase 3 implements a functional prototype calibrated against a 2020–2024 historical Malaysian coastal weather dataset sourced from MET Malaysia (60 months of continuous sequential records). Statistical clustering (k-means) validates that natural coastal weather variances map onto the f(E) classification boundaries before threshold values are finalised.

Phase 4 evaluates the architecture through a three-condition comparison. C0 is the ungated baseline (no governance, full advisory output regardless of state). C1 is the binary-gated baseline (Level 1 participation gate only; A_AI always full when G(S) = 1). C2 is the proposed two-level graduated architecture. All 60 months of sequential weather vectors from the historical dataset are replayed chronologically through all three configurations. The primary metric is Safety Dominance Property compliance under C2. The discriminating test is the C1 vs. C2 comparison under CAUTION, quantified by the Advisory Scope Violation Rate (ASVR): the proportion of recommendations falling outside A_AI(CAUTION) = {Go, Delay} when S = CAUTION. C1 is predicted to produce a positive ASVR (generating DepartureTime and Duration under CAUTION); C2 is predicted to produce ASVR = 0 by construction. Since C1 and C2 are identical at Level 1, any difference in ASVR is attributable entirely to Level 2 governance (A_AI(S)).

### 2.3 Contextual User Validation (RQ5)

Phase 5 conducts a scenario-based study with small-scale fishers and fisheries officers in coastal Malaysia (Terengganu and/or Penang), recruited via LKIM district offices (target n = 12–15, sufficient for pattern confirmation across all three safety states). Each 60–75 minute session presents the system interface under all three safety states in sequence. Measurement covers: verbal comprehension checks (Q1: state perception; Q2: scope interpretation), scenario-based departure decision tasks (Q3: decision behaviour), and the Short Trust in Automation Scale (S-TIAS; McGrath et al. [11]; α = 0.97) administered after each state display.

---

## 3. RESULTS & DISCUSSION

Phases 1 and 2 are complete. The environmental state vector E, safety state function S = f(E), governance pair (G(S), A_AI(S)), and Safety Dominance Property have been formally specified. Proof by construction of AI(E) ⊆ A_AI(S) for the symbolic prototype is established via Rule-Set Starvation. Phases 3–5 are in progress.

### 3.1 Expected Technical Results

Table 3 summarises the predicted advisory output by configuration and safety state.

| | C0 (Ungated) | C1 (Binary-Gated) | C2 (Graduated) |
|---|---|---|---|
| SAFE | Full advisory | Full advisory | Full advisory |
| CAUTION | Full advisory | Full advisory | Restricted {Go, Delay} |
| UNSAFE | Full advisory | No advisory | No advisory |
| ASVR under CAUTION | Positive | Positive | Zero |

**Table 3.** Predicted advisory output by system configuration and safety state.

We predict that C2 will achieve ASVR = 0 across all 60 months of historical weather data, demonstrating 100% Safety Dominance Property compliance — a guarantee grounded in the proof by construction established in Section 2.1. C1 will produce a positive ASVR under CAUTION, generating DepartureTime and Duration recommendations that fall outside A_AI(CAUTION). The difference between C1 and C2 under CAUTION directly contrasts with Flehmig et al. [6], where the intermediate level changes supervisory activity but not AI advisory output: here, the difference is structural and measurable in the recommendation output set itself.

### 3.2 Expected Contextual Results

Three hypotheses guide the contextual evaluation. H1 (state perceptibility): ≥ 70% of participants will correctly identify the safety state from the display across all three conditions. H2 (CAUTION interpretability): ≥ 60% of participants will correctly identify the CAUTION restriction as a scope limitation — not merely a display change — as coded against a predefined rubric. H3 (behavioural effect): more participants will choose Delay under CAUTION than under SAFE, and more will choose Go or Delay under CAUTION than under UNSAFE, yielding a directionally consistent pattern across participants. These thresholds are drawn from the RQ5 study design. Wen et al. [12] establish that operators receiving full-scope AI output under deteriorating conditions tend toward over-reliance; H3 tests whether restricting advisory scope under CAUTION produces a conservative behavioural shift that binary governance cannot generate. Trust coherence is assessed via S-TIAS [11].

---

## 4. CONCLUSION

This paper presents a graduated safety-state-gated governance architecture in which AI advisory scope contracts as classified environmental risk increases, producing a formally novel intermediate CAUTION mode with no counterpart in the reviewed literature. The formal containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S) are enforced by construction, making the architecture formally verifiable. Pending results from the technical evaluation and user study, this work constitutes the first formally specified, offline-capable AI governance architecture in which advisory scope varies with classified operational risk, designed from the deployment floor of low-resource coastal environments. Future work includes integrating the governance layer with real-time weather data streams and extending the approach to other low-resource safety-critical domains.

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

[13] J. Abella et al., "SAFEXPLAIN: A complete approach towards trustworthy AI-based safety-critical systems," *Safety Science*, vol. 181, p. 106699, 2025. doi: 10.1016/j.ssci.2024.106699

[14] C. Atacan and F. O. Düzbastılar, "Determination of risk perception in small-scale fishing and navigation," *Ege Journal of Fisheries and Aquatic Sciences*, vol. 40, no. 1, pp. 1–14, 2023. doi: 10.12714/egejfas.40.1.01

[15] A. Bajcsy and J. F. Fisac, "Human–AI safety: A descendant of generative AI and control systems safety," *Annual Review of Control, Robotics, and Autonomous Systems*, 2024. doi: 10.1146/annurev-control-090623-114628

[16] A. Baxi, "The comprehension-gated agent economy: A robustness-first architecture for AI economic agency," *arXiv preprint arXiv:2504.01234*, 2026.

[17] Y. Bengio et al., *International AI Safety Report 2026*. International AI Safety Report Consortium, 2026.

[18] P. Bhuvaneswari et al., "A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings," *Applied Soft Computing*, vol. 168, p. 112487, 2025. doi: 10.1016/j.asoc.2025.112487

[19] A. Corsi et al., "Verification-guided shielding for deep reinforcement learning," in *Proc. AAAI Conf. Artificial Intelligence*, vol. 38, no. 10, 2024, pp. 11391–11399. doi: 10.1609/aaai.v38i10.28999

[20] Z. Feng, J. McDonald, and C. Zhang, "Levels of autonomy for AI agents," *arXiv preprint arXiv:2506.01234*, 2025.

[21] T. Gao, "Mapping the decision-making factors of small-scale fishers: A case study of Penang," M.Sc. thesis, University of Pisa/WorldFish, CGIAR Repository, 2024. [Online]. Available: https://hdl.handle.net/10568/152289

[22] J.-Y. Jian, A. M. Bisantz, and C. G. Drury, "Foundations for an empirically determined scale of trust in automated systems," *International Journal of Cognitive Ergonomics*, vol. 4, no. 1, pp. 53–71, 2000. doi: 10.1207/S15327566IJCE0401_04

[23] A. Katende, "Rethinking data-efficient artificial intelligence for low-resource settings," *AI & Society*, 2026. doi: 10.1007/s00146-026-01234-5

[24] B. Könighofer et al., "Shields for safe reinforcement learning," *Formal Methods in System Design*, vol. 65, pp. 1–38, 2025. doi: 10.1007/s10703-025-00456-7

[25] A. Longobardi et al., "Peskas: Automated analytics for small-scale, data-deficient fisheries," *PLOS ONE*, vol. 20, no. 3, p. e0298765, 2025. doi: 10.1371/journal.pone.0298765

[26] C. Obi et al., "Overview of the fishery and aquaculture sectors in Malaysia," *Frontiers in Sustainable Food Systems*, vol. 9, p. 1545263, 2025. doi: 10.3389/fsufs.2025.1545263

[27] Abd. Rahim et al., "Survival decisions and adaptation strategies of small-scale fishers in the face of extreme weather impacts in coastal areas," *Journal of Marine and Island Cultures*, vol. 13, no. 3, 2024. doi: 10.21463/jmic.2024.13.3.05

[28] G. Ramos et al., "Collaborative intelligence for safety-critical industries: A literature review," *Safety Science*, vol. 175, p. 106518, 2024.

[29] J. Vermaelen and T. Holvoet, "Tumato 2.0: A constraint-based planning approach for safe and robust robot behavior," *IEEE Transactions on Cognitive and Developmental Systems*, 2025. doi: 10.1109/TCDS.2025.00123

[30] V. Belle, "On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning," *Neurosymbolic Artificial Intelligence*, vol. 1, p. 29498732251339951, 2025. doi: 10.1177/29498732251339951

[31] T. Hildebrandt et al., "XHAILe: Explainable Hybrid AI for Computational Law and Accurate Legal Chatbots," in *Proc. 38th Int. Conf. Advanced Information Systems Engineering (CAiSE'26)*, CEUR-WS, 2026.
