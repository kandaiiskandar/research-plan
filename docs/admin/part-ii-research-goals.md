# PART II — RESEARCH GOALS FOR THE NEXT 6 MONTHS

**Student Name:** Iskandar Samsuddin
**Planning Period:** June 2026 – November 2026
**Research Title:** *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Comparative Evaluation in Coastal Fisheries*

---

## Overview

The next six months transition the research from proposal and design into writing, implementation, and evaluation. The foundational work — the formal architecture, gap argument, literature review, and evaluation designs — is complete. The priorities for this period are writing the core thesis chapters, building the prototype, running the RQ4 technical evaluation, and preparing for the IPSCI 2026 presentation.

---

## Milestones

### 1. IPSCI 2026 — Presentation

The extended abstract for the **International Postgraduate Symposium on Computing and Informatics (IPSCI 2026)** will be finalised and submitted. The presentation will cover the proposed two-level governance architecture, the formal gap argument, and the comparative evaluation design. This is the first formal dissemination of the research and will provide an opportunity to receive external feedback before the core chapters are written.

---

### 2. Chapter 1 — Introduction

Chapter 1 will be written in full. The chapter opens with the binary governance problem as a CS problem, establishes the gap through the four-layer argument, introduces the fisheries domain as the validation context, and presents the five research questions, proposed architecture, and research contributions. The chapter concludes with the thesis structure.

**Target length:** 2,500–3,500 words

**Sections planned:**

| Section | Content |
|---|---|
| 1.1 | Opening — the governance problem |
| 1.2 | The binary governance gap |
| 1.3 | The application domain |
| 1.4 | Research questions and objectives |
| 1.5 | The proposed architecture |
| 1.6 | Research contributions |
| 1.7 | Methodology overview |
| 1.8 | Scope and limitations |
| 1.9 | Thesis structure |

---

### 3. Chapter 3 — Research Methodology

Chapter 3 will be written in full, covering the Design Science Research (DSR) framework (Peffers et al., 2007) as the governing methodology. The chapter maps each of the five research questions to its method: architecture design for RQ1, mathematical formalisation for RQ2, prototype development for RQ3, three-condition comparative analysis for RQ4, and the user study for RQ5. The justification for the DSR framework and the traceability from problem statement to methodology will be established here, drawing from the Research Alignment Table.

---

### 4. Chapter 4 — Architecture Design and Formal Model

Chapter 4 is the examination-critical chapter. It presents the primary CS contributions — the two-level governance pair (G(S), A_AI(S)) addressing RQ1, and the full formal specification addressing RQ2. The chapter covers the four-layer architecture, the environmental state vector E, the classification function S = f(E), the governance pair, the three safety states, and the Safety Dominance Property proof by construction via RS(S). This chapter draws directly from `docs/architecture-illustration.md` and `docs/appendix-c-formalisation.md`.

---

### 5. Prototype Implementation (RQ3)

The three-layer prototype will be implemented as a functional decision-support system suitable for mobile deployment. The implementation covers:

- **Layer 1** — Environmental input: reading the E vector from MET Malaysia's Kawasan Perairan data feed and the official warning bulletin
- **Layer 2** — Deterministic governance: computing S = f(E) via worst-case threshold aggregation, outputting G(S) and A_AI(S)
- **Layer 3** — Rule-based advisory engine: three distinct rule sets RS(SAFE), RS(CAUTION), and RS(UNSAFE), configured per safety state before reasoning begins

All three evaluation conditions will be implemented in the same codebase: C0 (ungated), C1 (binary-gated), and C2 (two-level graduated). This is a prerequisite for the RQ4 evaluation.

---

### 6. RQ4 Technical Evaluation

Once the prototype is complete, the twenty-scenario evaluation will be run across all three conditions. The evaluation will verify Safety Dominance Property compliance per scenario under C2, and produce the comparison results table showing how C0, C1, and C2 behave differently under CAUTION conditions. The primary finding expected is that C0 and C1 both produce DepartureTime and Duration under CAUTION, while C2 produces only {Go, Delay} — the direct empirical signature of the Level 2 governance contribution.

---

### 7. Ethical Approval Application (RQ5)

The ethical approval application for the RQ5 contextual validation study will be submitted to the institutional review board. The application covers the study purpose, participant population (fishers and fisheries officers in Terengganu and/or Penang), data collection methods, informed consent process, and data storage procedures. Allowing 4–8 weeks for review, approval is targeted before the end of this reporting period so that field recruitment can begin in the following period.

---

### 8. Chapter 2 — Literature Review (Finalisation)

Chapter 2 is currently in complete draft form across all nine sections. During this period it will be submitted to the supervisor for review and revised to final form. The comparative analysis table covering 17 systems across four governance dimensions, and the closing bridge paragraph leading into Chapter 3, will be confirmed and locked.

---

### 9. Dataset Analysis (2020–2024)

The environmental dataset covering the period 2020 to 2024 will be analysed. This dataset, sourced from MET Malaysia's Kawasan Perairan records for Western Sabah and Labuan, provides the real-world distribution of environmental conditions across the E vector parameters — wind speed, wave height, rainfall, and marine warning levels — over a five-year period spanning both monsoon and inter-monsoon seasons. The analysis will examine the frequency distribution of SAFE, CAUTION, and UNSAFE classifications under the proposed threshold values, identify the proportion of conditions falling in each safety state, and confirm that the threshold values produce a realistic and well-distributed classification. This analysis directly supports the threshold calibration for S = f(E) in RQ2, provides the scenario grounding for the RQ4 evaluation, and demonstrates that the CAUTION state occurs with meaningful frequency in real-world conditions — validating the practical relevance of the intermediate governance mode.

---

### 10. Paper 1 — Systematic Review (Draft)

Work will begin on the first publication: *Binary or Graduated? A Systematic Review of Safety Governance Mechanisms in AI Decision Support Systems*. The literature corpus (75+ papers) is already built and the comparison table and gap synthesis are substantially complete from the Chapter 2 work. The draft manuscript will be prepared for submission to *Safety Science* (Elsevier, Scopus Q1) by the end of this period, with supervisor review scheduled before submission.

---

## Chapters to be Written This Period

| Chapter / Document | Status at Start | Target Status at End |
|---|---|---|
| Chapter 1 — Introduction | Not started | Complete draft |
| Chapter 2 — Literature Review | Draft complete | Final (post-supervisor review) |
| Chapter 3 — Research Methodology | Not started | Complete draft |
| Chapter 4 — Architecture and Formal Model | Not started | Complete draft |
| Dataset Analysis (2020–2024) | Not started | Analysis complete |
| Paper 1 manuscript | Not started | Draft ready for supervisor review |

---

## Timeline

| Month | Priority Work |
|---|---|
| June 2026 | IPSCI 2026 abstract finalised; Chapter 1 draft begun; Chapter 2 submitted for supervisor review |
| July 2026 | Chapter 1 complete; Chapter 2 finalised; Chapter 3 begun; dataset analysis (2020–2024) started |
| August 2026 | Chapter 3 complete; dataset analysis complete; prototype development started |
| September 2026 | Prototype complete; RQ4 evaluation run; Chapter 4 begun |
| October 2026 | Chapter 4 complete; ethical approval application submitted; Paper 1 draft begun |
| November 2026 | Paper 1 draft ready for supervisor review; ethical approval awaited |
