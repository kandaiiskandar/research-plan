# A GRADUATED SAFETY-STATE-GATED ARCHITECTURE FOR AI DECISION SUPPORT IN LOW-RESOURCE COASTAL FISHERIES

**Iskandar Samsuddin¹**

¹ Faculty of Computing and Informatics, Universiti Malaysia Sabah, Malaysia
* Corresponding author: iskandarsamsuddin@gmail.com

---

**Abstract:** Existing AI governance architectures for safety-critical systems provide binary participation control: the AI either generates its full recommendation set (departure times, trip durations) or shuts down entirely. This paper extends that binary model to graduated advisory scope restriction through a two-level governance pair (G(S), A_AI(S)) conditioned on a classified environmental safety state S = f(E). Three governance modes follow from the classification: SAFE (full advisory scope), CAUTION (go/no-go and delay only), and UNSAFE (AI silent), producing the formal containment A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. The Safety Dominance Property AI(E) ⊆ A_AI(S) is enforced by construction through state-conditioned rule sets supplied before any AI reasoning begins, not by filtering outputs after the fact. The architecture targets low-resource coastal fisheries deployment, where the governance layer runs offline on smartphone-class hardware from environmental inputs fishers already assess before every trip. A Design Science Research methodology guides the work across five research questions: architecture design, formal specification, prototype implementation, three-condition comparative evaluation (ungated, binary-gated, two-level graduated), and a contextual user study with small-scale fishers in coastal Malaysia. The CAUTION mode (AI active, advisory scope formally restricted) extends the binary participation model found across the reviewed literature [1][2][7].

**Keywords:** AI governance, safety-state classification, decision support, advisory scope restriction, coastal fisheries

---

## 1. INTRODUCTION

This paper examines how AI governance architectures handle intermediate-risk conditions, and extends existing binary participation models with a formally specified intermediate governance mode.

Consider a fisher using an AI decision support system before departure. Wind readings are elevated; a marine advisory is in effect, but no warning has been issued. Conditions are not safe, but they are not shutdown-level dangerous either. Under every governance architecture identified in this review, the system faces a choice it cannot make well: continue generating departure-time and trip-duration recommendations built on environmental data that is no longer stable, or go silent entirely. An intermediate option, one where the AI is active but restricted to advice the current conditions can actually support, does not exist in any reviewed architecture.

Fishers themselves already operate with an informal three-part decision structure: go, cautious-go, or don't-go [6]. Under intermediate conditions, Penang fishers shorten trips and stay near shore rather than cancelling entirely. However, Yamin et al. [9], surveying 136 fishers in Terengganu, found that traditional weather prediction is declining due to climate unpredictability, with fishers increasingly relying on generic weather apps that provide raw data without governance logic. The proposed architecture formalises the three-part mental model fishers already use and fills the decision support vacuum that traditional knowledge erosion has created.

Getting this governance right has direct safety consequences. Wen et al. [8], analysing 60 real-world accident reports across process control and autonomous vehicle domains, found that human intervention was ineffective in 83.3% of process control incidents where the AI acted autonomously and the human was expected to override. The proposed architecture reverses this relationship: the AI advises within a formally constrained scope, and the human makes the final decision. For small-scale coastal fishers operating without institutional safety infrastructure [5][6], this distinction is not theoretical.

Indykov et al. [1], reviewing 206 papers and 16 architectural tactics for ML-enabled systems, found no tactic demonstrating formal impact on safety through advisory scope restriction. Across the reviewed studies, existing architectures gate AI participation (on or off) but do not govern what the AI may recommend once participation is allowed. The practical consequence is direct: under intermediate-risk conditions, systems continue producing high-specificity outputs (departure times, trip durations) that depend on environmental data no longer reliable enough to support them.

At the theoretical level, Dalrymple et al. [7] propose Guaranteed Safe AI as a comprehensive framework for ensuring robust AI systems, with binary safety verification: a system either satisfies its specification or fails it. This paper extends the GS framework by adding an intermediate governance mode where the AI participates within a formally restricted advisory scope.

The closest structural precedent identified in this review is Flehmig et al. [2], whose three-level traffic-light degradation index (green / orange / red) classifies AI operational status in safety-critical industrial systems. Their intermediate level (orange) triggers heightened supervisory activity, but the AI's advisory scope is unchanged between Level 1 and Level 2; both produce identical recommendations. The three-level classification governs what the human supervisor does, not what the AI may say. Searching four fisheries application domains, Haque and Al Jufaili [3] found the same absence: no system identified in their review implements formal advisory scope restriction conditioned on environmental safety state.

This paper extends these binary participation models by adding a second governance level. The governance pair (G(S), A_AI(S)) conditions both AI participation and AI advisory scope on a classified environmental safety state S = f(E), producing a formally specified intermediate mode where AI participates but scope is restricted to what the current safety state can support.

---

## 2. METHODOLOGY

### 2.1 Research Design

A Design Science Research (DSR) methodology [4] structures the work across five research questions. The work spans architecture design and formal specification (the primary CS contribution reported here), prototype implementation, three-condition comparative evaluation, and a contextual user study with coastal fishers. This paper reports the design and specification phase.

### 2.2 Architecture Design and Formal Specification

The governance pipeline is defined as:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision**

The environmental state vector **E = {w, r, m, o, v, t}** captures six parameters: wind speed (w), rainfall intensity (r), marine warning level (m), ocean state (o), vessel category (v), and time of day (t). The safety state function **S = f(E)** applies worst-case aggregation (S is determined by the single most dangerous parameter), producing S ∈ {SAFE, CAUTION, UNSAFE}. Three states is the minimum partition that resolves the binary false dilemma (full scope or none) while remaining formally and operationally tractable; the tripartite structure also matches the go/cautious-go/don't-go classification documented empirically in small-scale fisher decision-making [6]. For example, wind speed below 22 knots classifies as SAFE, 22–27 knots as CAUTION, and above 27 knots as UNSAFE, with the CAUTION–UNSAFE boundary anchored to MET Malaysia's Category 1 warning threshold for small craft. Specific thresholds are parameters of the architecture, not structural features; the formal properties hold for any valid threshold assignment.

The governance pair (G(S), A_AI(S)) defines two levels of control:

- **Level 1 (Participation gate G(S)):** determines whether the AI operates. G(UNSAFE) = 0 (AI blocked); G(SAFE) = G(CAUTION) = 1 (AI participates).
- **Level 2 (Advisory scope A_AI(S)):** defines the admissible recommendation space per safety state.

**Table 1:** Governance configuration by safety state

| Safety State | G(S) | A_AI(S) | AI Advisory Scope |
|---|---|---|---|
| SAFE | 1 (enabled) | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 (enabled) | {Go, Delay} | Restricted |
| UNSAFE | 0 (disabled) | ∅ | None |

The formal containment property holds: **A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅**

The **Safety Dominance Property** (AI(E) ⊆ A_AI(S) for all E) is enforced by construction. The governance layer (Layer 2) supplies a state-conditioned rule set RS(S) to the AI reasoning layer (Layer 3) before any reasoning begins. RS(CAUTION) contains only rules producing recommendations within {Go, Delay}; no rule in that configuration can generate DepartureTime or Duration. The property holds by definition of the rule sets, not by runtime filtering of AI outputs.

The architecture is designed for low-resource deployment: the governance layer performs only threshold comparisons and lookup operations (O(1) complexity), requires no connectivity, runs on any smartphone-class hardware, and operates from environmental parameters that are locally observable without specialised instrumentation [5]. All six parameters in E are grounded in empirical studies of fisher decision-making: wind, rainfall, and ocean state are the dominant climate hazards reported by small-scale fishers across multiple studies [3][6], and each parameter is measurable through sensors independent of the AI system [5].

### 2.3 Evaluation Design

Three-condition technical evaluation compares C0 (ungated, no governance), C1 (binary-gated, Level 1 participation gate only), and C2 (the proposed two-level architecture). The design isolates the contribution of Level 2 governance through the CAUTION discriminator: under CAUTION, C1 and C2 are identical at Level 1 (G(S) = 1 for both), so any difference in recommendation output is attributable entirely to A_AI(S). Safety Dominance Property compliance under C2 is the primary metric, verified per scenario with 100% compliance required; any failure is an implementation defect, not a performance shortfall. Secondary metrics cover recommendation type accuracy, decision consistency, and boundary classification accuracy.

Contextual validation will be conducted with small-scale fishers and fisheries officers in coastal Malaysia, testing whether users correctly identify safety states, correctly interpret CAUTION scope restriction as a scope limitation rather than a display change, and make different decisions across the three governance modes.

---

## 3. RESULTS & DISCUSSION

### 3.1 The Governance Architecture as Design Artefact

At this stage of the research, the architecture design is the primary deliverable. Table 1 presents the governance configuration. The CAUTION row is where the contribution sits: G(S) = 1 (AI participates, same as SAFE at Level 1) but A_AI(CAUTION) = {Go, Delay} (advisory scope restricted, unlike SAFE at Level 2). This configuration extends the binary participation model [1] and the three-level supervisory classification [2] by connecting the intermediate state to the AI's admissible output space.

The mechanism that produces this restriction is pre-hoc, not post-hoc: the governance layer supplies a state-conditioned rule set RS(S) to the reasoning layer before inference begins. Under CAUTION, no rule in RS(CAUTION) can produce DepartureTime or Duration. The restriction is structural and does not depend on output filtering.

### 3.2 Formal Properties and Evaluation Implications

The Safety Dominance Property (AI(E) ⊆ A_AI(S)) provides a binary, verifiable correctness criterion for evaluation. Under C2, every scenario either complies or fails; there is no acceptable partial compliance. This is the load-bearing test for the architecture's CS contribution: if the property holds across all test scenarios, the architecture delivers its formal safety guarantee. If it fails on any single scenario, there is an implementation defect.

The C1 vs C2 comparison under CAUTION is the direct empirical test of Level 2 governance's contribution. Under C1, a CAUTION-state scenario produces DepartureTime and Duration recommendations (full scope, G(S) = 1). Under C2, the same scenario produces only {Go, Delay} recommendations. The difference, attributable entirely to A_AI(S), demonstrates that Level 2 governance adds substantive safety value beyond what Level 1 alone provides. This comparison is made possible by the Level 2 extension, which existing binary and supervisory architectures [1][2] do not implement.

In low-resource deployment terms, the pre-hoc scope restriction in CAUTION mode also yields a computational efficiency advantage: the AI never expends inference cycles generating recommendation types that governance would suppress. Under connectivity-limited, battery-constrained conditions at sea, this efficiency is operationally significant [5].

---

## 4. CONCLUSION

AI governance for safety-critical systems has treated the intermediate-risk condition as architecturally invisible, a state where the formal response is to behave as though conditions were safe. The graduated architecture presented here gives that state a formal identity: CAUTION, where the AI remains active but advisory scope is restricted by construction to what the current environmental conditions can reliably support. The Safety Dominance Property (AI(E) ⊆ A_AI(S)) formalises this guarantee. The architecture has known limitations: worst-case aggregation on individual parameters does not capture interaction effects between sub-threshold conditions, and the SAFE–CAUTION boundary thresholds require domain expert calibration before deployment. Prototype implementation, three-condition comparative evaluation, and a contextual user study with coastal fishers in Malaysia follow as the next stages of this work.

---

## ACKNOWLEDGEMENT

[To be completed — include scholarship, grant, and institutional acknowledgements as applicable.]

---

## REFERENCES

[1] V. Indykov, D. Strüber, and R. Wohlrab, "Architectural tactics to achieve quality attributes of machine-learning-enabled systems: A systematic literature review," *Journal of Systems and Software*, vol. 223, p. 112373, 2025.

[2] N. Flehmig, M. A. Lundteigen, and S. Yin, "Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process," in *Proc. IEEE IECON 2024 — 50th Annual Conference of the IEEE Industrial Electronics Society*, 2024, DOI: 10.1109/IECON55916.2024.10906021.

[3] M. S. Haque and S. Al Jufaili, "Applications of artificial intelligence in fisheries: From data to decisions," *Reviews in Aquaculture*, 2026.

[4] K. Peffers, T. Tuunanen, M. A. Rothenberger, and S. Chatterjee, "A design science research methodology for information systems research," *Journal of Management Information Systems*, vol. 24, no. 3, pp. 45–77, 2007.

[5] A. Katende, "Rethinking data-efficient artificial intelligence for low-resource settings," *AI & Society*, 2026.

[6] P. K. Gao, "Mapping the decision-making factors of small-scale fishers: A case study of Penang," *Marine Policy*, 2024.

[7] D. Dalrymple et al., "Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems," *arXiv preprint arXiv:2405.06624*, 2024.

[8] H. Wen, Z. Sajid, and R. Arunthavanathan, "Risk perception in complex systems: A comparative analysis of process control and autonomous vehicle failures," *AI*, vol. 6, no. 8, p. 164, 2025, DOI: 10.3390/ai6080164.

[9] L. Yamin, T.-C. Kuo, and N. Aziz, "Interplay of traditional knowledge and adaptive capacity in climate change adaptation of small-scale fishers in central Terengganu, Malaysia," *Frontiers in Marine Science*, vol. 12, p. 1492131, 2025, DOI: 10.3389/fmars.2025.1492131.
