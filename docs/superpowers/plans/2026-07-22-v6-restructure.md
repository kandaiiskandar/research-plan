# v6 Paper Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure `ipsci-2026-paper-v6.md` to conference-paper norms: eliminate the standalone Key Concepts section, tighten Methodology by ~30%, trim the Literature Review by ~35–40%, and add one concrete scenario example to the Proposed Architecture.

**Architecture:** Four sequential edits to a single file. Each task produces a self-contained, reviewable change. No new files are created; all work stays in `ipsci-2026-paper-v6.md`.

**Tech Stack:** Plain Markdown editing only.

## Global Constraints

- Preserve all citations exactly — no reference numbers may change or be dropped.
- Preserve all three tables (Table I, II, III) and all three figures (Fig. 1, 2, 3) with their captions and diagrams.
- Do not alter formal notation (G(S), A_AI(S), AAI(S), E, S = f(E), Safety Dominance Property).
- Do not alter the Abstract, Conclusion, or References sections.
- The paper uses Roman numeral table labels (Table I, II, III) — maintain this convention.
- The paper uses "Fig. X" abbreviation style — never spell out "Figure".

---

### Task 1: Merge Key Concepts into Introduction

**Files:**
- Modify: `ipsci-2026-paper-v6.md` lines 7–45

**What to do:**

The `# Key Concepts` section (lines 19–45) is a standalone section with a one-sentence preamble, a definitional paragraph, and Fig. 1 with its diagram. Move its content into the Introduction and delete the section heading.

- [ ] **Step 1: Identify the insertion point in the Introduction**

  The Introduction currently ends at line 17 with a sentence listing all paper sections, including "the Key Concepts section defines the key concepts used throughout". The definitions belong after line 15 ("This paper takes up that third question.") and before the contributions paragraph (line 17). Place the definitional paragraph there.

- [ ] **Step 2: Move the Key Concepts definitional paragraph**

  Remove from Key Concepts:
  ```
  Five concepts recur throughout this review and are defined here to fix terminology.

  An AI decision support system generates recommendations...
  ```

  Insert after line 15 ("This paper takes up that third question."), with this lead-in rewrite:
  ```
  Five concepts are defined here to fix terminology. An AI decision support system generates recommendations for a human decision-maker who retains final decision authority; it is distinct from an autonomous agent, which executes actions directly. A safety-critical system is one in which incorrect or inappropriately scoped output can contribute to harm to human life, health, or property. Runtime governance refers to mechanisms that constrain AI behaviour during operation, as distinct from design-time controls such as training, fine-tuning, or static configuration. Within runtime governance, this paper separates two dimensions: participation gating (whether the AI participates in the decision at all) and advisory scope (the set of recommendation types the AI is permitted to generate while participating). Advisory scope restriction is the contraction of that set (dimension 2, Fig. 1). Finally, an environmental safety state is a classified summary S of an environmental observation vector E, produced by a classification function S = f (E) that is computed independently of the AI component; a low-resource environment is a deployment context lacking reliable connectivity, computing infrastructure, and institutional support, imposing offline-first and computationally lightweight requirements on any deployed system.
  ```

- [ ] **Step 3: Move Fig. 1 caption and diagram**

  Move the Fig. 1 caption and ASCII diagram immediately after the definitional paragraph (still within the Introduction, before the contributions paragraph). Keep the blank line separating the diagram from the text that follows.

- [ ] **Step 4: Update the contributions paragraph (line 17)**

  Remove the phrase "the Key Concepts section defines the key concepts used throughout;" from the paper-structure sentence in the contributions paragraph. The sentence should read naturally without it.

- [ ] **Step 5: Delete the `# Key Concepts` section heading and its preamble**

  Delete:
  ```
  # Key Concepts

  Five concepts recur throughout this review and are defined here to fix terminology.
  ```
  and the now-empty paragraph/diagram block that was moved.

- [ ] **Step 6: Verify**

  Read the Introduction from top to bottom. Confirm: (a) definitions appear before the contributions paragraph, (b) Fig. 1 and its diagram follow the definitions, (c) no `# Key Concepts` heading remains, (d) no orphaned blank lines.

---

### Task 2: Reduce Methodology by ~30%

**Files:**
- Modify: `ipsci-2026-paper-v6.md` (Methodology section, currently ~650 words → target ~450 words)

**What to cut and how:**

- [ ] **Step 1: Compress the Search Strategy subsection**

  Current Search Strategy has two paragraphs (~200 words). Merge them into one:

  ```
  Papers were retrieved from Scopus, IEEE Xplore, Web of Science, and ACM Digital Library using search strings including AI governance, runtime assurance, safety filter, advisory scope, decision support, human-AI collaboration, autonomy levels, guardrails, action restriction, and AI safety-critical; secondary searches used fisheries AI, maritime decision support, and low-resource AI deployment. Three large-scale systematic reviews within the initial candidate set were retained as secondary evidence: Indykov et al. [5] (206 papers, 16 architectural tactics), Shamsujjoha et al. [6] (13 guardrail actions across 32 agent studies), and Perez-Cerrolaza et al. [24] (294 references). Papers were added through citation tracing until no new governance mechanisms emerged. 72 papers proceeded to full review.
  ```

- [ ] **Step 2: Compress the Screening, Inclusion, and Coding subsection**

  The paragraph explaining the coding dimension derivation logic (starting "The four dimensions were derived by decomposing...") is 130 words. Cut it to ~70 words by removing the step-by-step (a)–(d) restatement, since Table I already shows the dimensions. Replace with:

  ```
  The four dimensions were derived by decomposing the central research question: a mechanism that restricts AI advisory scope based on environmental safety state would need to target advisory scope, use graduated adaptation, condition on environmental state, and produce a formally bounded output set. Each requirement corresponds to one dimension; a paper coded Yes on all four would constitute a prior instance of the proposed mechanism.
  ```

- [ ] **Step 3: Compress the Theme Development and Synthesis subsection**

  Cut the third paragraph (lines 80–81, about the mechanistic basis evidence being from a separate literature) — this information already appears in the Mechanistic Basis section itself and is redundant here. The subsection should end after the second paragraph ("The closest structural precedents...").

- [ ] **Step 4: Verify**

  Word-count the Methodology section after edits. Confirm it is approximately 30% shorter than the original (~450 words). Confirm Table I and Fig. 2 remain in place with no orphaned blank lines.

---

### Task 3: Shorten Literature Review by ~35–40%

**Files:**
- Modify: `ipsci-2026-paper-v6.md` (Literature Review section)

**Guiding principle:** Preserve all evidence that directly establishes the gap (especially the Synthesis section and the Adaptive Risk-Based Systems section). Compress the introductory overview and the individual-paper detail in the Deterministic and Authority Allocation sections, since those paradigms are not the closest precedents.

- [ ] **Step 1: Compress the Overview of Existing Governance Paradigms paragraph**

  Current: ~130 words. Cut to ~60 words, keeping only the three-paradigm names and the key finding that none graduates advisory scope:

  ```
  Existing AI governance frameworks in safety-critical systems fall into three paradigms: deterministic safety constraints (provable runtime guarantees by blocking unsafe behaviour), authority allocation frameworks (distributing decision rights between human and AI), and adaptive risk-based systems (varying behaviour across graduated operational levels). Across all three, no framework graduates the AI's advisory scope. A fourth body (fisheries AI and low-resource deployment) is reviewed to establish whether the pattern persists in the application domain.
  ```

- [ ] **Step 2: Compress the Deterministic Safety Constraints subsection**

  Current: ~250 words. Cut to ~130 words. Retain Könighofer (shields), Dalrymple (GS AI), Bajcsy/Fisac (safety filter) as the three anchor papers and Pro2Guard as the proactive extension. Cut the detail on Corsi and Abella (shielding variants) — cite them briefly in a parenthetical or cut entirely since they add no new governance finding beyond "also binary":

  ```
  Könighofer et al. formalise shields: runtime mechanisms that intercept AI actions before they reach the environment [8]. Dalrymple et al. propose Guaranteed Safe AI, requiring formal proof certificates before AI output is deployed [9]. Bajcsy and Fisac implement a control-theoretic safety filter [10]. All three share the same governance topology: the AI either operates within its safety boundary or is replaced. The most recent extension, Pro2Guard, adds predictive foresight — learning a Markov Chain of agent behaviour to intervene before violations occur [34] — but the governance topology is unchanged: the object of governance remains execution, and nothing conditions what the AI may recommend. None of the 72 reviewed papers addresses the semantic content of AI output.
  ```

- [ ] **Step 3: Compress the Authority Allocation subsection**

  Current: ~200 words. Cut to ~100 words. Keep Ramos (the 91-study review finding) and Mussi (the cross-domain scale confirmation), compress the Feng/McDonald/Zhang detail:

  ```
  Authority allocation frameworks ask who decides rather than what the AI may recommend. Ramos et al., reviewing 91 collaborative intelligence studies, find AI-assisted decision-making dominant across safety-critical industries, but no system varies advisory scope by safety state [13]. Feng, McDonald, and Zhang propose five autonomy levels, but both dimensions are configured at design time [14]. At cross-domain scale, Mussi et al. identify every ingredient of state-conditioned governance across power grids, railway networks, and air traffic management, yet assemble none into a runtime model: automation levels remain fixed at design time [33]. No framework in this body conditions what the AI may recommend on a classified environmental state.
  ```

- [ ] **Step 4: Compress the Adaptive Risk-Based Systems subsection**

  This is the closest precedents section — keep the three 2026 paradigm descriptions (Oversight intensification, Execution deferral, Action-class restriction) and the Flehmig/Baxi/Tumato 2.0 setup. Trim only the concluding transition sentences (lines 153–155) to one sentence.

  Remove the two-sentence block:
  ```
  Adaptive risk-based systems are the closest precedent the reviewed literature offers for the architecture proposed here. Graduated operational posture has been shown to be technically feasible and useful. The gap is in where the graduation is applied: intermediate governance levels across every reviewed system target human supervisory workflows, physical execution deferral, or agent action classes. The semantic content of the AI's recommendation output is left uncontracted at every tier. The next section examines whether this absence persists in the application domain.
  ```

  Replace with:
  ```
  Graduated operational posture is technically feasible; the gap is in where the graduation is applied. Intermediate governance levels target human workflows, execution deferral, or agent action classes — not the semantic content of AI output. The next section examines whether this pattern persists in the application domain.
  ```

- [ ] **Step 5: Compress the Fisheries and Low-Resource Deployment subsection**

  Current: ~200 words. Cut to ~120 words. The two risk statistics (Dominguez-Péry and Atacan) are important — keep both. Compress the five-paper governance-gap summary into three sentences:

  ```
  The application domain carries a measurable environmental risk profile. Dominguez-Péry et al., analysing 504 IMO maritime accident reports (2011–2021), found wind, weather, and visibility form the largest single risk cluster (26.7%), and small vessels record the highest mean fatality rank (p = 0.01) [2]. Atacan and Düzbastılar found that combined night navigation and heavy weather produces the highest accident consequence scores across all tested conditions (mean 37.03) [3].

  Against this risk profile, the domain's AI literature shows the same governance pattern. Haque and Al Jufaili confirm that no fisheries AI system implements formal advisory scope restriction conditioned on environmental state [17]. Rahim et al. document that the only external advisory available to coastal fishers is a binary government warning to stop fishing [18]. Katende identifies safety governance as a systematic gap in low-resource AI deployment — it has not been designed from the deployment floor [19]. The literature establishes deployment feasibility and documents the risk profile, but provides no formal runtime governance architecture.
  ```

- [ ] **Step 6: Compress the Synthesis section**

  The Synthesis section is load-bearing — it must be kept largely intact. Compress the conditioning-variable paragraph (lines 189–190, ~130 words) by cutting the Engin and Hand digression to a parenthetical and tightening:

  Remove:
  ```
  The contemporary literature also reveals a consistent misalignment in the variables used to condition runtime governance gates. Baxi conditions permissions on verified algorithmic robustness [15]; Flehmig et al. monitor AI degradation [7]; Kang classifies task regulatory impact [25]; Sahoo measures human-agent control quality [26]; Ghaleb et al. compute calibrated epistemic model uncertainty [27]; and Wang et al. predict the probability of the agent's own trajectory reaching an unsafe state [34]. All six gate behaviour on properties internal to the AI system or its software task. The same centring appears in governance theory itself: Engin and Hand's dimensional governance (the most adaptive strand of current governance thinking, arguing that static risk tiers and autonomy levels are insufficient and that governance categories should instead be explicit thresholds over continuously monitored dimensions) nonetheless defines its dimensions (decision authority, process autonomy, accountability) as properties of the human-AI relationship, not of the operator's physical environment [32]. The proposed architecture conditions its graduated constraints on an independently classified environmental safety state (S = f(E)).
  ```

  Replace with:
  ```
  A consistent misalignment appears in the variables used to condition runtime governance gates: Baxi conditions on AI robustness [15], Flehmig et al. on AI degradation [7], Kang on task regulatory impact [25], Sahoo on human-agent control quality [26], and Ghaleb et al. on epistemic model uncertainty [27]. All gate behaviour on properties internal to the AI system. Even the most adaptive strand of governance theory (Engin and Hand's dimensional governance [32]) defines its dimensions as properties of the human-AI relationship, not the operator's physical environment. The proposed architecture conditions its constraints on an independently classified environmental safety state (S = f(E)).
  ```

- [ ] **Step 7: Compress the Mechanistic Basis section**

  Cut the "Internal versus external governance" subsection (lines 209–213) — its content is a summary of the three preceding subsections and is already recapitulated in the Proposed Architecture section's opening paragraph. Replace the entire subsection with one bridging sentence at the end of the "Self-assessed uncertainty" subsection:

  ```
  The three limitations above — fixed pipeline, non-adaptive reasoning, unreliable self-assessment — establish that internal governance cannot be relied upon; the gap must be addressed through an external architectural layer.
  ```

- [ ] **Step 8: Compress the Objectives subsection**

  The three objectives are currently written as three separate unnumbered sentences/paragraphs (lines 219–223). Convert to a compact numbered list:

  ```
  This study has three objectives: (1) to determine whether existing architectures implement mechanisms that restrict AI advisory scope according to classified environmental safety state; (2) to characterise the advisory scope gap through a structured comparison across governance paradigms; and (3) to derive a graduated safety-state-gated governance architecture that addresses the gap through externally enforced governance.
  ```

  Remove the closing sentence ("The structured literature review addresses the first two objectives...") — this is implicit from the paper structure.

- [ ] **Step 9: Verify**

  Confirm Tables I and II remain in place. Confirm all citation numbers are intact. Confirm the section still contains the four-body structure (deterministic → authority → adaptive → fisheries) followed by synthesis, mechanistic basis, and objectives.

---

### Task 4: Expand Proposed Architecture with a concrete scenario

**Files:**
- Modify: `ipsci-2026-paper-v6.md` (Proposed Architecture section, Domain Instantiation subsection)

**What to add:** One concrete worked scenario illustrating the three states in practice, placed after the existing Domain Instantiation paragraph. This should be 120–150 words.

- [ ] **Step 1: Write and insert the scenario**

  After the existing Domain Instantiation paragraph (ending "...drawing on the empirically verified runtime-gating stability of Ghaleb et al. [27]."), insert:

  ```
  **Illustrative scenario.** A fisher prepares to depart at 0600. At SAFE state (wind 8 kt, no marine warning, calm swell), the system generates a full-scope recommendation: Go, with a suggested departure window of 0630–0700 and an estimated safe trip duration of four hours. Wind strengthens to 18 kt by mid-morning and the marine warning level rises to advisory; S = f(E) reclassifies the state to CAUTION. The AI remains engaged but its admissible space contracts to {Go, Delay}: it recommends Delay with a brief rationale, but withholds the departure time and duration it could no longer reliably support. By afternoon, sustained wind exceeds the UNSAFE threshold; G(S) = 0 disengages the AI entirely, and the system presents only the static government warning. The fisher receives calibrated guidance at each state rather than full-scope output until abrupt shutdown.
  ```

- [ ] **Step 2: Verify**

  Confirm the scenario references all three states (SAFE, CAUTION, UNSAFE), names the admissible recommendation sets at each, and is consistent with Table III.

---

### Task 5: Run humanizer on the revised paper

**Files:**
- Modify: `ipsci-2026-paper-v6.md` (full document, excluding References and formal notation blocks)

- [ ] **Step 1: Invoke the humanizer skill**

  Run `/humanizer` on `ipsci-2026-paper-v6.md`. Use Research Writing Mode (the input is academic writing). Apply all standard AI-pattern rules plus Rules R1–R7.

- [ ] **Step 2: Preserve off-limits content**

  The humanizer must not alter: formal notation (G(S), A_AI(S), AAI(S), E, S = f(E), containment expressions), citation numbers, table content, figure captions and diagrams, the Abstract, Conclusion, and References sections.

- [ ] **Step 3: Verify**

  Confirm no citation numbers changed, no formal symbols were rewritten, and all tables and figures remain intact.

---

## Self-Review Checklist

- [ ] Key Concepts content fully appears in the Introduction; `# Key Concepts` heading is gone
- [ ] Fig. 1 and diagram remain, now inside the Introduction
- [ ] Methodology is ~30% shorter; Table I and Fig. 2 remain in place
- [ ] Literature Review is ~35–40% shorter; Table II remains in place; all four paradigm bodies still covered
- [ ] Synthesis section retains the four-stream gap argument
- [ ] Proposed Architecture has a concrete scenario example
- [ ] All citation numbers [1]–[36] intact
- [ ] No orphaned headings, duplicate blank lines, or broken section references
- [ ] Humanizer applied; formal notation, citations, tables, and figures intact
