# Chapter 1 Introduction — Writing Plan

**Dissertation**: *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Comparative Evaluation in Coastal Fisheries*
**Output file**: `docs/chapter-1-draft.md` (to be written section by section)
**Framing**: CS-first — lead with the binary governance problem, introduce fisheries as the validation domain, not the research motivation

---

## Writing Rules

Carry over from Chapter 2 plan (`docs/chapter-2-writing-plan.md`):

- Synthesised prose — no bullet lists in running text
- One idea per sentence
- Simple and precise words
- Clear subject → verb → object structure
- APA 7th in-text citations: (Author, Year) or Author (Year)
- Every cited paper includes a `[[notes]]` link after the citation
- Light reasoning signals: *because*, *this means*, *this shows*
- Avoid AI-like transitions (*Furthermore*, *Moreover*, *Additionally*)

**Additional rules for Chapter 1:**

- Do not introduce socio-technical theory as a primary framework — it belongs in RQ5 discussion only
- Do not treat RQ5 as a co-equal contribution to RQ1/RQ2 in any framing
- Each section should be self-contained but hand off cleanly to the next
- The CAUTION mode is the architectural novelty — foreground it when introducing the proposed solution
- Never use "unique" or "novel" as stand-alone claims — always follow with a specific argument

---

## Target Length

Total: 2,500–3,500 words (excluding section headings and the thesis structure table)

| Section | Target words |
|---|---|
| 1.1 Opening — the governance problem | 250–350 |
| 1.2 The binary governance gap | 400–500 |
| 1.3 The application domain | 250–350 |
| 1.4 Research questions and objectives | 300–400 |
| 1.5 The proposed architecture | 300–400 |
| 1.6 Research contributions | 200–300 |
| 1.7 Methodology overview | 150–200 |
| 1.8 Scope and limitations | 150–200 |
| 1.9 Thesis structure | 150–200 |

---

## Section Plan

---

### 1.1 Opening — The governance problem

**Argument**: AI advisory systems are deployed in safety-critical contexts where operating conditions change, but the governance architectures that regulate them are static and binary — AI is either fully active or completely disabled.

**Do NOT open with the fisheries domain.** Open with the governance problem as a CS problem.

**Opening hook approach** (choose one when writing):

Option A — from practice: A fisher departs at dawn with a forecast that deteriorates by midday. At the point where conditions are dangerous but not prohibitive, the AI advisory system has no mode between full advice and silence — it either recommends or it does not.

Option B — from CS: AI governance mechanisms in safety-critical systems operate on a binary switch. An environmental safety state of elevated but non-prohibitive risk has no formal representation. The AI either participates fully or is blocked entirely.

Option B is more CS-aligned. Option A is more accessible. Consider a single-sentence version of Option A followed immediately by the CS framing.

**Key move**: By the end of 1.1, the reader should understand that there is a class of risk — elevated but non-prohibitive — for which no governance architecture has a formal response. This sets up 1.2.

**Source material**: `index.md` — Abstract (first paragraph); `index.md` — One sentence summary; `docs/justification-novelty-gap.md` — Section 1 (gap argument opening)

**Key citations**: Perez-Cerrolaza et al. (2024) [[notes]](../../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md), Ramos et al. (2024) [[notes]](../../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md)

---

### 1.2 The binary governance gap

**Argument**: Every existing safety-critical AI architecture implements governance at exactly one of two levels — participation control (whether AI acts) or output restriction (blocking specific actions) — but no architecture formally conditions both levels on the same classified environmental safety state. The result is that no existing architecture can formally express a CAUTION mode where AI participates within a restricted advisory scope because conditions are elevated but not prohibitive.

**Structure (three paragraphs)**:

**Paragraph 1 — Level 1 only: shields and participation gates**
Formal safety shields (Könighofer et al., 2025), safety filters (Bajcsy & Fisac, 2024), and runtime enforcement frameworks (Wang et al., 2026) implement Level 1 governance: whether AI may act. These are binary gates — safe/unsafe, permit/block. Within the permitted region, the AI produces its full advisory output without restriction. The governing function maps to {0, 1}, not {SAFE, CAUTION, UNSAFE}. No intermediate state exists where AI participates at reduced advisory scope.

Source: `docs/justification-novelty-gap.md` Section 2 (shields); `docs/justification-binary-governance-external-evidence.md` Section 2.1 (Zhang et al. binary formalisation)

Key citations: Könighofer et al. (2025) [[notes]](../../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md); Bajcsy & Fisac (2024) [[notes]](../../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md); Wang et al. (2026) [[notes]](../../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md); Newcomb & Ochoa (2026) [[notes]](../../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md)

**Paragraph 2 — Closest prior art: Flehmig et al. and the missing dimension**
The closest existing work to a three-mode governance structure is Flehmig et al. (2024), whose traffic-light degradation index classifies AI operational status into three levels. At Level 2 (orange), the AI stays active under elevated supervisory scrutiny. The architectural structure maps onto SAFE/CAUTION/UNSAFE. But the governance at Level 2 controls supervisory intensity, not AI advisory scope — the AI at Level 2 produces identical output to Level 1. There is no A_AI(CAUTION) ⊂ A_AI(SAFE). Flehmig et al. also condition their degradation index on AI model performance, not on the safety state of the operational environment. These two absences — environmental state conditioning and advisory scope restriction — define the gap this research fills.

Source: `docs/justification-novelty-gap.md` Section 3; `docs/research-alignment-table.md` (Primary comparators section)

Key citation: Flehmig et al. (2024) [[notes]](../../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md)

**Paragraph 3 — Scope of the gap: four independent confirmations**
The gap is confirmed across four independent bodies of literature: 91 collaborative intelligence papers (Ramos et al., 2024), 46 formal methods studies (Newcomb & Ochoa, 2026), 11 international AI safety frameworks (Bengio et al., 2026), and the cross-domain safety-critical AI survey (Perez-Cerrolaza et al., 2024). None identifies a mechanism that unifies participation governance and advisory scope governance under the same classified environmental state. The gap is the absence of a CAUTION mode — a formally defined intermediate state where AI participates within a restricted recommendation space because conditions are elevated but not yet prohibitive.

Source: `index.md` — Novelty section (gap confirmed independently across four bodies); `docs/justification-novelty-gap.md` — introduction and conclusion

Key citations: Ramos et al. (2024) [[notes]](../../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Newcomb & Ochoa (2026) [[notes]](../../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Bengio et al. (2026) [[notes]](../../notes/International%20AI%20Safety%20Report%202026.md); Perez-Cerrolaza et al. (2024) [[notes]](../../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)

---

### 1.3 The application domain

**Argument**: Small-scale coastal fisheries in Malaysia provide a well-defined, operationally tractable domain to instantiate and evaluate the proposed governance architecture. The departure decision problem — whether a fisher should go to sea given current environmental conditions — has a natural three-mode risk structure, real low-resource constraints, and genuine safety stakes that make it an appropriate validation context. The domain motivates and validates the architecture; it is not the research contribution.

**Structure (two paragraphs)**:

**Paragraph 1 — The problem and why fisheries**
Small-scale coastal fisheries in Malaysia face a real AI governance problem: fisher departure decisions depend on environmental conditions (wind, sea state, rainfall, marine warnings), conditions change within trips, formal AI advisory systems are emerging in the domain, and the population they serve has constrained devices, intermittent connectivity, and limited digital literacy. No existing AI system for this domain formally governs how AI participation should change as conditions move from safe to dangerous. Haque and Al Jufaili (2026) review AI across four fisheries application domains and find no system implementing formal participation governance or advisory scope restriction conditioned on environmental safety state.

Source: `index.md` — PS3 problem statement; `docs/justification-low-resource-environments.md`

Key citation: Haque & Al Jufaili (2026) [[notes]](../../notes/AI%20in%20Fisheries%20and%20Aquaculture.md)

**Paragraph 2 — Why this domain is the right validation context**
The departure decision maps directly onto the three-mode governance structure. Safe conditions admit full AI advice; elevated but non-prohibitive conditions call for directional guidance without precision scheduling; prohibitive conditions require silence from the AI with a deterministic safety alert. The environmental state vector E = {w, r, m, o, v, t} is observable from independent sources. The low-resource constraints (TinyML-compatible hardware, offline operation after initial deployment) validate Layer 2's O(1) threshold classification and Layer 3's production rule engine, both of which are designed to run on constrained devices without cloud dependency.

Source: `index.md` — Proposed Architecture section; `docs/justification-low-resource-environments.md`; `docs/justification-layer3-enforcement.md` Section 2 (AgroNova deployment analogue)

---

### 1.4 Research questions and objectives

**Argument**: Five research questions, ordered from primary CS contribution (RQ1, RQ2) through implementation (RQ3) to evaluation (RQ4, RQ5). RQ1 and RQ2 are the primary contributions. RQ3–RQ5 are implementation, technical evaluation, and contextual validation.

**Presentation**: Brief framing paragraph (2–3 sentences), then a table or numbered list of RQs with objectives. A short paragraph after the table clarifying the CS/evaluation hierarchy.

**Source material**: `docs/research-alignment-table.md` — full table; `index.md` — Problem Statements PS1–PS5 with objectives O1–O5

**Key point to make in the framing paragraph**: The five RQs follow the Design Science Research cycle (Peffers et al.) — problem identification, design, development, evaluation, communication. RQ1 and RQ2 produce the primary design artefact. RQ3 instantiates it. RQ4 evaluates it technically. RQ5 validates it with users.

**Do NOT present RQ5 as a theoretical contribution.** It is contextual validation — testing whether the architecture functions as intended with the population it was designed for.

---

### 1.5 The proposed architecture

**Argument**: The proposed Graduated Safety-State-Gated Architecture introduces a two-level governance pair (G(S), A_AI(S)) conditioned on a classified environmental safety state S = f(E). The result is a formally defined CAUTION mode — the architectural novelty — that no existing single-level architecture can express.

**Structure (three paragraphs)**:

**Paragraph 1 — The formal pipeline**
The pipeline is: E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision. E is a vector of six independently observable environmental parameters. S = f(E) is a deterministic worst-case aggregation over a threshold table. The governance pair (G(S), A_AI(S)) consists of: G(S), the participation gate (1 if AI may act, 0 if not); and A_AI(S), the admissible recommendation space (what types of recommendation AI may generate). The Safety Dominance Property guarantees AI(E) ⊆ A_AI(S) for all E — proved by construction via the rule set RS(S) supplied to Layer 3 before any reasoning begins.

**Paragraph 2 — The three safety states and the CAUTION mode**
Three safety states are defined: SAFE (G(S) = 1, A_AI = {Go, Delay, DepartureTime, Duration}); CAUTION (G(S) = 1, A_AI = {Go, Delay}); UNSAFE (G(S) = 0, A_AI = ∅). The containment property holds: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. CAUTION is the architecturally novel state. Under CAUTION, AI remains active (G(S) = 1), so information continues to flow to the human decision-maker. But precision guidance — DepartureTime and Duration — is removed from the admissible space (A_AI(CAUTION) ⊂ A_AI(SAFE)), because such recommendations would be unreliable under elevated conditions. A binary architecture cannot express this: it has no level 2 governance to restrict advisory scope independently of the participation gate.

**Paragraph 3 — The four-layer implementation**
The architecture is implemented in four layers: Layer 1 observes E from sources independent of the AI; Layer 2 classifies S = f(E) deterministically (O(1), no AI); Layer 3 is a production rule system whose active rule set RS(S) is configured by Layer 2 before reasoning begins; and Layer 4 is the human decision-maker, who retains final authority in all three safety states. No actuator path exists from Layer 3 — AI output is advisory display only. The architecture runs without GPU, satisfies TinyML constraints, and operates offline after initial deployment.

**Source material**: `index.md` — Proposed Architecture and Novelty sections; `docs/architectural-layering-design.md`; `docs/justification-layer3-enforcement.md`; `docs/appendix-c-formalisation.md`

---

### 1.6 Research contributions

**Argument**: State the primary, secondary, and tertiary contributions clearly and in order of CS significance.

**Structure**: Brief framing sentence, then numbered list (acceptable here as it is a contributions enumeration).

**Primary contributions (RQ1, RQ2)**:
1. The Graduated Safety-State-Gated Architecture — the first governance architecture to formally unify participation governance (G(S)) and advisory scope governance (A_AI(S)) under the same classified environmental safety state S = f(E).
2. Formal specification of E, S = f(E), G(S), A_AI(S), RS(S), and the Safety Dominance Property AI(E) ⊆ A_AI(S) — proved by construction, not by runtime filtering.
3. The CAUTION mode — the first formally defined intermediate AI operational state in which AI participates within a restricted recommendation space conditioned on environmental safety state.

**Secondary contributions (RQ3, RQ4)**:
4. A prototype decision-support system for small-scale coastal fisheries, designed for low-resource deployment (offline, constrained hardware, limited connectivity).
5. A three-condition comparative evaluation (C0 ungated, C1 binary-gated, C2 two-level graduated) that isolates the contribution of Level 2 advisory scope governance beyond Level 1 participation governance, using the CAUTION mode as the discriminating condition.

**Tertiary contribution (RQ5)**:
6. A contextual validation study establishing whether fishers correctly perceive safety states, interpret advisory scope restriction under CAUTION, and make different decisions across the three governance modes.

**Source material**: `index.md` — Novelty section; `docs/justification-contribution-characterisation.md`

---

### 1.7 Methodology overview

**Argument**: Design Science Research (Peffers et al.) governs the research cycle. The design artefact is the governance architecture. The evaluation artefacts are the prototype, the comparative evaluation, and the contextual validation study.

**Keep this section short.** One paragraph only. The full methodology is in Chapter 3.

**Key sentence**: "This research follows the Design Science Research methodology (Peffers et al., 2007 [[notes]](../../notes/A%20Design%20Science%20Research%20Methodology%20for%20Information%20Systems%20Research.md)), which structures the research cycle as problem identification, design, development, demonstration, and evaluation."

**Do not detail the methodology here.** Mention DSR, state that the design artefact and the evaluation methods are detailed in Chapter 3, and move on.

---

### 1.8 Scope and limitations

**Argument**: The architecture is scoped to the departure decision problem for small-scale coastal fisheries. The formal proof covers the current recommendation type set. Extensions to other recommendation types would require separate enforcement arguments.

**Key limitations to state**:
- The recommendation set {Go, Delay, DepartureTime, Duration} is fixed by the current RS(S). Extensions require separate proofs.
- The contextual validation (RQ5) uses scenario-based tasks, not live deployment data.
- Threshold values in Layer 2 are domain-calibrated for Malaysian coastal fisheries; recalibration is required for other contexts.
- The architecture governs AI advisory scope but does not address the broader socio-technical context of fisher decision-making (automation bias, trust calibration). These appear as failure modes and are treated in the discussion, not as primary research contributions.

**Source material**: `docs/justification-layer3-enforcement.md` Section 6 (limitations of rule-based choice); `docs/rq5-study-design.md` (scope exclusions)

---

### 1.9 Thesis structure

**Format**: One short paragraph introducing the chapter overview, followed by a table mapping chapter to content.

| Chapter | Title | Content |
|---|---|---|
| 1 | Introduction | Problem, gap, proposed solution, RQs, contributions, methodology, scope |
| 2 | Literature Review | Binary governance in safety-critical AI; adaptive autonomy; low-resource AI; fisheries AI; formal synthesis of the gap |
| 3 | Research Design | DSR methodology; three-condition evaluation design; RQ5 user study design |
| 4 | Architecture Design and Formalisation | Formal specification of E, S = f(E), G(S), A_AI(S), RS(S); Safety Dominance Property proof; four-layer implementation |
| 5 | Prototype Implementation | Layer 1–4 implementation; low-resource deployment; rule set construction |
| 6 | Evaluation — Technical | Three-condition comparative analysis (C0 vs C1 vs C2); scenario results; CAUTION discriminator analysis |
| 7 | Evaluation — Contextual | User study with fishers; Q1/Q2/Q3 results; discussion of CAUTION mode perception |
| 8 | Discussion | Contributions situated in literature; limitations; future work |
| 9 | Conclusion | Summary of findings; formal properties revisited; practical significance |

*Note: Chapter numbers are provisional pending supervisor confirmation of structure.*

---

## Source Document Map

| Section | Primary sources |
|---|---|
| 1.1 | `index.md` (abstract, one-sentence summary); `docs/justification-novelty-gap.md` (Section 1) |
| 1.2 | `docs/justification-novelty-gap.md` (Sections 2–3); `docs/justification-binary-governance-external-evidence.md` (Section 2.1–2.2); `docs/research-alignment-table.md` (comparators) |
| 1.3 | `index.md` (PS3); `docs/justification-low-resource-environments.md` |
| 1.4 | `docs/research-alignment-table.md` (full table); `index.md` (PS1–PS5) |
| 1.5 | `index.md` (Proposed Architecture, Novelty); `docs/architectural-layering-design.md`; `docs/justification-layer3-enforcement.md` |
| 1.6 | `index.md` (Novelty); `docs/justification-contribution-characterisation.md` |
| 1.7 | `docs/research-alignment-table.md` (methodology column) |
| 1.8 | `docs/justification-layer3-enforcement.md` Section 6; `docs/rq5-study-design.md` |
| 1.9 | Chapter structure from thesis outline |

---

## Citation Checklist

The following papers are expected to appear in Chapter 1. All must include [[notes]] links:

| Paper | Section | Quick link |
|---|---|---|
| Perez-Cerrolaza et al. (2024) | 1.1, 1.2 | `[[notes]](../../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)` |
| Ramos et al. (2024) | 1.1, 1.2 | `[[notes]](../../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md)` |
| Könighofer et al. (2025) | 1.2 | `[[notes]](../../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md)` |
| Bajcsy & Fisac (2024) | 1.2 | `[[notes]](../../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md)` |
| Wang et al. (2026) | 1.2 | `[[notes]](../../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md)` |
| Flehmig et al. (2024) | 1.2 | `[[notes]](../../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md)` |
| Newcomb & Ochoa (2026) | 1.2 | `[[notes]](../../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md)` |
| Bengio et al. (2026) | 1.2 | `[[notes]](../../notes/International%20AI%20Safety%20Report%202026.md)` |
| Haque & Al Jufaili (2026) | 1.3 | `[[notes]](../../notes/AI%20in%20Fisheries%20and%20Aquaculture.md)` |
| Dalrymple et al. (2024) | 1.5 | `[[notes]](../../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md)` |
| Peffers et al. (2007) | 1.7 | *(check citation-notes-map.md for DSR paper link)* |

---

## Key Drafting Decisions

**Opening sentence**: Do not start with "This thesis..." or "This research...". Open with a claim about the world — the governance problem — not about the document.

**Contribution framing**: Always anchor the CAUTION mode as the specific novelty. "The architecture introduces a formally defined CAUTION mode" is more precise and defensible than "the architecture is novel because it has three states."

**Flehmig reference**: Flehmig et al. (2024) must appear in 1.2 as the closest prior art, with a precise statement of the two differences (trigger condition and governance target). This is the most important differentiation move in the introduction.

**Safety Dominance Property**: Introduce it in 1.5 as a named property with its formal statement: AI(E) ⊆ A_AI(S). Briefly note it is proved by construction. Full proof is in Chapter 4.

**Layer 4**: Do not describe Layer 4 as a software component. It is the human decision-maker. "No actuator path from Layer 3" is the key architectural property to state.
