# IPSCI 2026 Paper v4 Revision Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Address all major and minor reviewer issues to bring `ipsci-2026-paper-v4.md` to journal-ready quality, producing `ipsci-2026-paper-v5.md`.

**Architecture:** Seven targeted revision tasks applied sequentially to the paper. Each task targets a distinct structural or content weakness identified in the review. Tasks are ordered so that structural changes (Section 3, analytical framework) come before the tasks that depend on them (Section 4 subsection endings). The humanizer skill must be applied to every new passage before it is finalised.

**Tech Stack:** Markdown editing; humanizer skill for all new written passages; CLAUDE.md citation rule for any new paper references.

## Global Constraints

- All new text must pass through the humanizer skill before being inserted.
- Every corpus paper cited must carry a `[[notes]]` link per the Citation Reference Rule in CLAUDE.md.
- No formal variable (E, S, G(S), A_AI(S)) may be redefined — use canonical definitions from `docs/appendix-c-formalisation.md`.
- Output file: `ipsci-2026-paper-v5.md` (do not overwrite v4).
- The paper is a CS architecture thesis contribution — do not drift framing toward socio-technical theory.
- Strong universal claims ("no architecture exists") must be scoped to the reviewed corpus ("within the reviewed literature" / "among the 71 reviewed papers").

---

### Task 1: Hedge universal claims throughout the paper

**Files:**
- Modify: `ipsci-2026-paper-v4.md` — search and replace over-strong claim language
- Create: `ipsci-2026-paper-v5.md` — working copy for all subsequent tasks

**Why:** Reviewer flags that "none exists" and "no architecture implements" are difficult to defend scientifically. These must be scoped to the corpus before the paper is submitted.

**Interfaces:**
- Produces: `ipsci-2026-paper-v5.md` with hedged claims — all later tasks modify this file.

- [ ] **Step 1: Copy v4 to v5**

```bash
cp ipsci-2026-paper-v4.md ipsci-2026-paper-v5.md
```

- [ ] **Step 2: Locate all universal claim phrases**

Search for these exact strings in `ipsci-2026-paper-v5.md`:
- `none exists`
- `no architecture implements`
- `appears in none`
- `no mechanism`
- `no system`
- `no concept`
- `entirely absent`
- `remains entirely absent`

- [ ] **Step 3: Replace each with a corpus-scoped equivalent**

Use the following substitution pattern for every occurrence found:

| Original phrase | Replacement |
|---|---|
| `none exists` | `none has been identified in the reviewed literature` |
| `no architecture implements` | `no architecture in the reviewed corpus implements` |
| `appears in none of the reviewed architectures` | `has not appeared in any of the reviewed architectures` |
| `no mechanism` | `no mechanism in the reviewed corpus` |
| `no system in their review` | `no system in their review` *(this already scopes to Ramos et al. — leave as is)* |
| `contains no concept of` | `contains no concept of` *(already scoped to Attard-Frost — leave as is)* |
| `remains entirely absent` | `has not been identified in the reviewed literature` |

Apply edits directly in `ipsci-2026-paper-v5.md`. The three large-scale surveys already provide secondary coverage that supports strong claims within the corpus, so the language change is precision, not a weakening of the argument.

- [ ] **Step 4: Verify abstract and conclusion**

The abstract contains: *"The review finds that existing governance mechanisms are uniformly binary"* — this is correctly scoped to the review. Leave it.

The abstract also contains: *"Indykov et al. ... contain no mechanism"* — already scoped by attribution. Leave it.

Check the conclusion paragraph starting *"This paper establishes, from four independent bodies"* — no over-strong language detected; leave as is.

- [ ] **Step 5: Commit working copy**

```bash
git add ipsci-2026-paper-v5.md
git commit -m "init: create v5 working copy with hedged claim language"
```

---

### Task 2: Sharpen the novelty statement in the Introduction (Section 1)

**Files:**
- Modify: `ipsci-2026-paper-v5.md` — Section 1, paragraph 3 (the two-contribution paragraph)

**Why:** The reviewer recommends a single tight paragraph that captures the novelty more precisely than the current multi-sentence description. The current framing buries the key distinction (participation ≠ advisory scope ≠ execution) inside the contributions paragraph.

**Interfaces:**
- Consumes: Task 1 output — `ipsci-2026-paper-v5.md`
- Produces: Sharpened novelty framing in Section 1, usable as a reference point for the Section 2 figure (Task 3) and the Section 4.6 gap synthesis (Task 5).

- [ ] **Step 1: Locate the target paragraph**

Find the paragraph in Section 1 that begins: *"This paper makes two contributions."*

- [ ] **Step 2: Insert a novelty-framing sentence before the two-contributions paragraph**

Insert the following block immediately **before** the sentence "This paper makes two contributions.":

> Existing runtime governance determines whether AI may operate. Existing autonomy research determines what autonomous agents may execute. Neither determines what AI may recommend to a human decision-maker under changing environmental risk. This paper addresses that third dimension.

- [ ] **Step 3: Run humanizer on the inserted text**

Invoke humanizer skill on the four-sentence insertion. Replace with humanized output.

- [ ] **Step 4: Verify the two-contributions paragraph still reads correctly after the insertion**

The transition from the new insertion into "This paper makes two contributions" should feel natural. Adjust the opening word of the contributions paragraph if needed (e.g., change "This paper makes two contributions. First, it establishes..." to "It does so through two contributions. First, it establishes...").

---

### Task 3: Add a governance-dimensions figure to Section 2

**Files:**
- Modify: `ipsci-2026-paper-v5.md` — Section 2 (Key Concepts), after the paragraph defining all five concepts

**Why:** The reviewer recommends a figure showing the three governance dimensions (Participation → Advisory Scope → Execution). This makes the paper's contribution immediately legible at a glance and strengthens Section 2's conceptual scaffolding.

**Interfaces:**
- Consumes: The five concept definitions already in Section 2.
- Produces: An ASCII/Markdown figure block appended to Section 2.

- [ ] **Step 1: Insert the figure block at the end of Section 2**

Add the following immediately after the closing sentence of Section 2 (after "...imposing offline-first and computationally lightweight requirements on any deployed system."):

```markdown
**Figure 1.** Three distinct governance dimensions in AI decision support systems. Existing literature addresses dimensions 1 and 3; this paper's contribution is dimension 2.

```
Governance Dimension 1 — Participation
Whether the AI may operate
(addressed by: shields, safety filters, binary gates)

          ↓

Governance Dimension 2 — Advisory Scope          ← this paper
What the AI is permitted to recommend
(the admissible recommendation space A_AI(S))

          ↓

Governance Dimension 3 — Execution
Which actions an autonomous agent may take
(addressed by: action-class restriction, autonomy levels)
```
```

- [ ] **Step 2: Add a forward reference**

Add a parenthetical at the end of the **advisory scope** definition sentence in Section 2 (the sentence ending "Advisory scope restriction is the contraction of that set.") to connect it to Figure 1:

> Advisory scope restriction is the contraction of that set (dimension 2, Figure 1).

- [ ] **Step 3: Run humanizer on any new prose inserted in this task**

Figure caption text should be humanized. The ASCII diagram itself does not need humanizing.

---

### Task 4: Expand Section 3 into a proper StLR methodology (2–3 pages)

**Files:**
- Modify: `ipsci-2026-paper-v5.md` — Section 3 (Methodology), full replacement

**Why:** This is the largest structural weakness. The current Section 3 is one paragraph (~120 words). A Structured Literature Review requires explicit description of: search strategy, screening criteria, inclusion/exclusion rules, paper coding scheme, theme emergence process, and synthesis method. Without these, reviewers cannot assess whether the gap identification is credible.

**Interfaces:**
- Produces: A 3-subsection methodology (3.1 Search Strategy, 3.2 Screening and Coding, 3.3 Theme Development and Synthesis) that explains the analytical framework used in Section 4.

- [ ] **Step 1: Replace current Section 3 with the expanded version below**

Replace the entire current Section 3 block (from `## 3. METHODOLOGY` through the end of its single paragraph) with the following:

---

```markdown
## 3. METHODOLOGY

This review follows a structured literature review (StLR) protocol designed to answer one targeted question: does any existing architecture restrict an AI system's advisory scope as a function of classified environmental safety state? It is structured rather than systematic: the search and coding are disciplined, but the scope is purposive — covering the specific bodies of literature from which an answer could plausibly emerge, rather than attempting an exhaustive universal survey. This distinction matters: a systematic review promises reproducibility and completeness; a structured review promises analytical rigour and transparency of reasoning. Reviewers should apply the latter set of expectations here.

### 3.1 Search Strategy

Papers were retrieved from Scopus, IEEE Xplore, Web of Science, and ACM Digital Library using the following primary search strings: 'AI governance', 'runtime assurance', 'safety filter', 'advisory scope', 'decision support', 'human-AI collaboration', 'autonomy levels', 'guardrails', 'action restriction', and 'AI safety-critical'. Secondary searches targeting the application domain used 'fisheries AI', 'maritime decision support', and 'low-resource AI deployment'. Searches were not date-bounded but results were prioritised toward 2022–2026 to capture the contemporary state of the art.

An initial candidate set was assembled through iterative database search. Three large-scale systematic reviews within that set — Indykov et al. [5] (206 papers, 16 architectural tactics), Shamsujjoha et al. [6] (13 guardrail actions, 32 agent studies), and Perez-Cerrolaza et al. [24] (294 references, safety-critical domains) — were retained in full as secondary evidence; their own reviewed corpora extend effective coverage to several hundred additional primary studies without individually screening each. Papers were added iteratively through backward and forward citation tracing from high-relevance sources until no new governance mechanisms or architectural patterns emerged; 71 papers were carried through to full review.

### 3.2 Screening, Inclusion, and Coding

Papers were screened in two stages. Title and abstract screening applied the following inclusion criteria: (i) the paper addresses a mechanism that constrains or shapes AI system behaviour during operation; (ii) it targets a safety-critical or human-in-the-loop context; or (iii) it addresses AI deployment in low-resource or resource-constrained environments. Papers addressing purely training-time, fine-tuning, or static-configuration approaches with no runtime governance component were excluded. After screening, 71 papers were retained for full review.

Each retained paper was coded on the following four dimensions:

| Dimension | Values |
|---|---|
| **Governance target** | Participation / Advisory scope / Execution / Oversight |
| **Runtime adaptation** | Binary (on/off) / Graduated (3+ levels) / None |
| **Conditioning variable** | Environmental state / AI robustness / Task risk / Human authority / None |
| **Recommendation restriction** | Yes (bounded output set) / No |

The coding was performed by the author. The four dimensions were derived directly from the central research question — does any architecture restrict AI advisory scope as a function of classified environmental safety state? — by decomposing what such a mechanism would have to do: it would need to (a) target advisory scope rather than participation or execution, (b) implement graduated rather than binary adaptation, (c) condition restriction on the operator's environmental state rather than internal AI properties, and (d) produce a formally bounded output set. These requirements map one-to-one onto the four coding dimensions. A paper that codes Yes on all four dimensions would constitute a prior instance of the proposed mechanism; the coding exercise determines whether any such paper exists in the reviewed corpus. The **Primary governance target** label is used (rather than simply "governance target") because some papers implement multiple mechanisms; the code records only the mechanism most central to each paper's contribution.

### 3.3 Theme Development and Synthesis

Papers that shared a common governance topology — the same combination of governance target and conditioning variable — were grouped into themes. This produced three primary governance paradigms (deterministic safety constraints, authority allocation frameworks, adaptive risk-based systems) and one application-domain body (fisheries and low-resource deployment), reviewed in Sections 4.2–4.5 respectively.

Within each paradigm, papers were compared against the four coding dimensions to characterise the paradigm's collective governance posture. Section 4.6 synthesises across paradigms, noting where all four coding dimensions converge on the same absence, to characterise the research gap. Papers that constituted the closest structural precedents to the proposed mechanism — those that graduated some dimension of AI behaviour across three or more levels — were analysed in greater detail to establish precisely why they did not satisfy dimension (d) (recommendation restriction).

The mechanistic evidence reviewed in Section 4.7 is drawn from a separate, non-governance literature (LLM systems and cognition research) and was not subject to the same screening process; it is included to provide evidence on whether the gap could be closed within the AI component rather than through external governance.
```

---

- [ ] **Step 2: Run humanizer on the full new Section 3**

Apply humanizer to the entire replacement Section 3 content (3.1, 3.2, 3.3). Replace with humanized output.

- [ ] **Step 3: Verify the coding table columns are consistent with their usage in Section 4**

The four coding dimensions introduced in 3.2 should match how papers are described in Sections 4.2–4.5. Spot-check:
- Shields/GS AI/safety filter: Participation / Binary / — / No ✓
- Flehmig et al.: Oversight / Graduated / AI degradation / No ✓
- Sahoo AMAGF: Execution / Graduated / Control quality / No ✓

No changes needed to Section 4 for consistency.

---

### Task 5: Make Section 4 subsection endings consistent

**Files:**
- Modify: `ipsci-2026-paper-v5.md` — Sections 4.2, 4.3, 4.4, 4.5

**Why:** The reviewer recommends that every subsection end with the same three-beat structure: what this paradigm does well (strength), what it cannot do (limitation), and what this tells us about the gap (contribution to gap). Currently each subsection ends differently; adding consistency makes the cross-paradigm synthesis in 4.6 feel like a natural payoff.

**Interfaces:**
- Consumes: Current Section 4 subsection endings.
- Produces: Each of 4.2–4.5 ending with a consistent three-beat closing sentence group.

- [ ] **Step 1: Add closing beat to Section 4.2**

Find the last sentence of Section 4.2: *"They say nothing about what the AI may recommend once active."*

Replace it with:

> The deterministic constraints paradigm is the most formally rigorous of the reviewed bodies: it delivers provable, by-construction participation-level safety. Its structural limitation is that the binary topology is not a design oversight but a consequence of the verification problem — safety guarantees require sharply bounded behaviour spaces. Within the 71 reviewed papers, no paper in this paradigm restricts the semantic content of AI output rather than its participation.

- [ ] **Step 2: Add closing beat to Section 4.3**

Find the last sentence of Section 4.3: *"Both bodies of work (safety constraints and authority allocation) address who or what acts; neither addresses what the AI may say once it does."*

Replace with:

> Authority allocation frameworks contribute a precise vocabulary for the human side of the loop and have produced the most empirically grounded accounts of human-AI collaboration in practice. Their limitation is that function allocation and autonomy levels are fixed at design time and do not respond to environmental conditions at runtime. Within the reviewed literature, no authority allocation framework conditions what the AI may recommend on a classified environmental state.

- [ ] **Step 3: Add closing beat to Section 4.4**

Find the last sentence of the main body of 4.4 (before Table 1): *"Across all three paradigms, the concept of a state-conditioned, formally bounded recommendation menu A_AI(S) for a human decision-maker facing escalating environmental risk remains entirely absent."*

Replace `remains entirely absent` with `has not been identified` (per Task 1 hedging), then add:

> Adaptive risk-based systems are the closest paradigm to the proposed architecture: they demonstrate that graduated operational posture is technically feasible and empirically useful. Their consistent limitation is that their intermediate governance levels are directed at human supervisory workflows, physical execution deferral, or agent action classes — never at the semantic content of an AI recommendation menu presented to a human operator.

- [ ] **Step 4: Add closing beat to Section 4.5**

Find the last sentence of Section 4.5: *"...Bhuvaneswari et al. show lightweight AI for safety-critical decisions is feasible in resource-constrained settings, also without one."*

Add after it:

> The fisheries and low-resource deployment body confirms deployment feasibility and documents the risk profile that motivates the governance question. Its limitation, from a governance architecture standpoint, is that it demonstrates what can be built without formal runtime governance rather than what a governance architecture should look like. The coding applied in Section 3.2 finds no paper in this body that scores Yes on any of the four governance dimensions.

- [ ] **Step 5: Run humanizer on all four new closing beats**

Apply humanizer to each inserted paragraph (4.2, 4.3, 4.4, 4.5 closings). Replace with humanized output.

---

### Task 6: Expand Table 1 with four additional columns

**Files:**
- Modify: `ipsci-2026-paper-v5.md` — Table 1 in Section 4.4

**Why:** The reviewer notes Table 1 is the best table in the paper and recommends adding: Governance Target, Decision Variable, Risk Variable, Output Restriction. These map directly to the coding dimensions introduced in the new Section 3.2, making the table a concrete output of the review methodology.

**Interfaces:**
- Consumes: Coding dimensions defined in Task 4 (Section 3.2).
- Produces: Expanded Table 1 with 9 columns (existing 5 + 4 new).

- [ ] **Step 1: Replace Table 1 with the expanded version**

Replace the entire current Table 1 markdown (from `| Framework |` through the last row `| **Proposed architecture** |`) with:

```markdown
| Framework | Governance target | Conditioning variable | Runtime adaptation | Intermediate mode variable | AI status at max risk | Output restriction |
|---|---|---|---|---|---|---|
| Shields [8], GS AI [9], safety filter [10] | Participation | Safety boundary | Binary (on/off) | None | Blocked | No |
| Tumato 2.0 [16] | Execution | Constraint predicate | Binary per action | None | — | No |
| Flehmig et al. traffic-light [7] | Oversight | AI degradation index | Graduated (3 levels) | **Human** supervisory intensity | Control → non-AI backup | No |
| Kang GAIE [25] | Oversight | Task regulatory impact | Graduated (3 tiers) | **Human** audit and approval | Full scope, HITL-gated | No |
| Ghaleb et al. safety gate [27] | Execution | Epistemic uncertainty | Graduated (3 regimes) | **System** re-sensing loop | Switched to classical planner | No |
| Sahoo AMAGF [26] | Execution | Control quality score | Graduated (5 bands) | **Agent** reversible actions only | Autonomy disablement | No (action classes only) |
| Baxi K-tier [15] | Execution | AI robustness (verified) | Graduated (K tiers) | **Agent** permission set | — | No (economic actions) |
| **Proposed architecture** | **Advisory scope** | **Environmental safety state** | **Graduated (3 states)** | **AI** admissible recommendation space | Disabled (G(S) = 0, A_AI = ∅) | **Yes** (A_AI(CAUTION) = {Go, Delay}) |
```

- [ ] **Step 2: Update the table caption**

Replace the current caption:

> **Table 1.** Governance patterns in the reviewed architectures, organised by the variable each framework graduates at its intermediate level.

With:

> **Table 1.** Coding of reviewed architectures against the four governance dimensions defined in Section 3.2. The proposed architecture is the only framework in the reviewed corpus that targets advisory scope, conditions governance on environmental safety state, and produces a formally bounded output restriction.

- [ ] **Step 3: Add a forward reference in Section 3.2**

At the end of the coding table in Section 3.2, add:

> Table 1 in Section 4.4 presents the full coding of all frameworks that implement graduated adaptation.

---

### Task 7: Add an architecture flow diagram to Section 5

**Files:**
- Modify: `ipsci-2026-paper-v5.md` — Section 5, between the opening paragraph and Section 5.1

**Why:** The reviewer recommends a diagram showing the full flow from environmental data through to recommendations. The architecture is simple — a diagram makes it immediately readable without requiring the reader to assemble it from prose.

**Interfaces:**
- Consumes: The formal structure already defined in Section 5.1 (G(S), A_AI(S), the three states).
- Produces: An ASCII flow diagram and a figure caption, inserted before Section 5.1.

- [ ] **Step 1: Insert the architecture diagram block before Section 5.1**

Add the following immediately before the `### 5.1 Formal Structure` heading:

```markdown
**Figure 3.** The graduated safety-state-gated architecture. The environmental safety state S = f(E) is computed by a deterministic external classifier before the AI component is consulted. The participation gate G(S) and advisory gate A_AI(S) are both conditioned on S; together they define the AI's admissible recommendation space for the current observation.

```
Environmental observation vector E = {w, r, m, o, v, t}
                    │
                    ▼
         ┌─────────────────────┐
         │  Safety Classifier  │  S = f(E)
         │  (deterministic,    │
         │   external to AI)   │
         └─────────┬───────────┘
                   │
         ┌─────────▼───────────┐
         │  S ∈ {SAFE,         │
         │       CAUTION,      │
         │       UNSAFE}       │
         └──┬──────┬───────────┘
            │      │
     ┌──────▼──┐ ┌─▼──────────────┐
     │ G(S) = 0│ │   G(S) = 1     │
     │ UNSAFE  │ │ SAFE / CAUTION │
     │ AI off  │ └────────┬───────┘
     └─────────┘          │
                 ┌────────▼───────────────────────┐
                 │  Advisory Gate A_AI(S)          │
                 │  SAFE:    {Go, Delay,           │
                 │            DepartureTime,       │
                 │            Duration}            │
                 │  CAUTION: {Go, Delay}           │
                 └────────┬───────────────────────┘
                          │
                 ┌────────▼───────────┐
                 │  Rule-based engine │
                 │  (RS(S) supplied   │
                 │   before inference)│
                 └────────┬───────────┘
                          │
                 ┌────────▼───────────┐
                 │  AI(E) ⊆ A_AI(S)   │
                 │  Recommendations   │
                 │  to human operator │
                 └────────────────────┘
```
```

- [ ] **Step 2: Run humanizer on the figure caption**

Apply humanizer to the Figure 2 caption text only (not the diagram). Replace with humanized output.

- [ ] **Step 3: Add a forward reference in Section 5 opening paragraph**

In the opening paragraph of Section 5, add a parenthetical after the first mention of "external governance":

> ...both AI participation and advisory scope are conditioned on a classified environmental safety state, by an architectural layer outside the AI component (Figure 3).

- [ ] **Step 4: Final commit**

```bash
git add ipsci-2026-paper-v5.md
git commit -m "revise: address reviewer issues — StLR methodology, analytical framework, novelty framing, figures, hedged claims, expanded Table 1"
```

---

### Task 8: Add a conceptual review-process figure to Section 3

**Files:**
- Modify: `ipsci-2026-paper-v5.md` — Section 3.3 (Theme Development and Synthesis), end of section

**Why:** An StLR paper benefits from a simple process figure that shows how the review progresses from research question to proposed architecture. This is not a PRISMA flowchart — it is a conceptual map showing the logical sequence of the methodology, which helps readers understand that the architecture emerges from the review process rather than being imposed on it.

**Interfaces:**
- Consumes: The three-subsection Section 3 produced in Task 4.
- Produces: Figure 0 (the review process), inserted at the end of Section 3.3, before Section 4.

- [ ] **Step 1: Insert the review-process figure at the end of Section 3.3**

Add the following immediately after the final paragraph of Section 3.3 (the paragraph ending "...it is included to provide evidence on whether the gap could be closed within the AI component rather than through external governance."):

```markdown
**Figure 2.** Conceptual review process: from research question to proposed architecture. The structured literature review (Sections 3.1–3.3 and 4.2–4.6) establishes the gap; Section 4.7 establishes why it cannot be closed within the AI component; Section 5 proposes the architecture the gap implies.

```
Research Question
(Does any architecture restrict AI advisory scope
 as a function of environmental safety state?)
                    │
                    ▼
         Database Search (Section 3.1)
         Scopus · IEEE Xplore · Web of Science · ACM DL
                    │
                    ▼
         Screening & Inclusion (Section 3.2)
         71 papers retained
                    │
                    ▼
         Four-dimension Coding (Section 3.2)
         Governance target · Runtime adaptation ·
         Conditioning variable · Output restriction
                    │
                    ▼
         Theme Development (Section 3.3)
         Three paradigms + application domain
         (Sections 4.2 – 4.5)
                    │
                    ▼
         Cross-paradigm Synthesis (Section 4.6)
         All four coding dimensions converge
         on the same absence
                    │
                    ▼
         Mechanistic Evidence (Section 4.7)
         Gap cannot be closed within the AI component
                    │
                    ▼
         Proposed Architecture (Section 5)
         G(S) + A_AI(S) — graduated governance pair
```
```

- [ ] **Step 2: Run humanizer on the figure caption only**

Apply humanizer to the Figure 0 caption text. The diagram itself does not need humanizing.

- [ ] **Step 3: Update the forward reference in Section 4.1**

Section 4.1 currently opens with: *"Existing AI governance frameworks in safety-critical systems fall into three main paradigms..."*

Add a parenthetical at the end of that paragraph's final sentence to point to Figure 0:

> The review methodology that produced this synthesis is described in Section 3 and summarised in Figure 2.

---

## Self-Review Checklist

### 1. Reviewer issue coverage

| Issue | Addressed in |
|---|---|
| Methodology not a true StLR | Task 4 — Section 3 expanded to 3 subsections, 2–3 pages |
| No explicit analytical framework | Task 4 — coding dimensions table in Section 3.2 |
| Four literature streams not justified | Task 4 — Section 3.3 explains purposive selection rationale |
| Strong universal claims | Task 1 — all instances hedged to corpus scope |
| No figure in Section 2 | Task 3 — Figure 1 (governance dimensions) |
| Section 3 too short | Task 4 — expanded from ~120 words to ~500 words |
| Section 4 subsections inconsistent | Task 5 — consistent three-beat endings added to 4.2–4.5 |
| Table 1 could be expanded | Task 6 — four new columns added; "Primary governance target" label used |
| No architecture diagram | Task 7 — Figure 2 added before Section 5.1 |
| Novelty statement not sharp enough | Task 2 — four-sentence novelty block added to Section 1 |
| **Supervisor correction 1:** No invented search statistics | Task 4 — "148 papers" removed; replaced with iterative saturation description |
| **Supervisor correction 2:** Must distinguish StLR from SLR | Task 4 — explicit StLR vs SLR distinction added to Section 3 opening |
| **Supervisor correction 3:** Coding dimensions must be derived from RQ | Task 4 — Section 3.2 explanation revised to derive all four dimensions from the research question |
| **Supervisor correction 4:** Add conceptual review-process figure | Task 8 — Figure 0 added at end of Section 3.3 |

### 2. Placeholder scan

- No "TBD" or "TODO" present in this plan.
- All new prose is shown in full with humanizer step following.
- All new table content is shown in full.

### 3. Consistency checks

- Coding dimensions in Section 3.2 (Task 4) match the column labels added to Table 1 (Task 6). ✓
- Figure 1 (Task 3) defines the three governance dimensions; Section 4.6 references them; Table 1 uses "Governance target" column. ✓
- Formal variables (G(S), A_AI(S), S = f(E)) unchanged from canonical definitions. ✓
- All Task 1 hedging applied before Tasks 5, 6, 7 reference the gap. ✓

---

**Plan complete and saved to `docs/superpowers/plans/2026-07-16-ipsci-paper-v4-revision.md`. Two execution options:**

**1. Subagent-Driven (recommended)** — fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** — execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**
