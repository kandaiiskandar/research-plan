# Literature Review Improvement Plan

**Date**: 2026-04-05
**Source**: Examiner & supervisor feedback (`review-comments/comments-1.md`)
**Scope**: Addressing 6 substantive concerns (C1–C6), 3 structural recommendations (R1–R3)

---

## Phase 1: New Paper Acquisition (C2, C5)

**Goal**: Convert PS4 and PS5 from "Unsupported" to "Methodologically grounded" and strengthen T4 (Low-resource) from 4 Yes papers to 7+.

### 1.1 Levels-of-Automation & Trust Literature (C2 — High)

The examiner specifically names these as essential for PS4/PS5 evaluation design:

| Paper | Why needed | Target PS |
|-------|-----------|-----------|
| Sheridan & Verplank (1978) — Levels of automation | Foundational framework for graduated automation — directly applicable to three-mode governance evaluation | PS4 |
| Parasuraman, Sheridan & Wickens (2000) — "A Model for Types and Levels of Human Interaction with Automation" | Defines 10 levels of automation across 4 information-processing stages — provides theoretical grounding for why governance should be graduated, not binary | PS4 |
| SAE J3016 — Levels of Driving Automation | Industry standard for graduated automation — demonstrates that graduated governance is established practice in automotive, undermining "is tripartite governance useful?" objection | PS4 |
| Lee & See (2004) — "Trust in Automation" | Foundational trust-in-automation framework — provides validated conceptual model for evaluating user trust across governance states | PS5 |
| Jian, Bisantz & Drury (2000) — Trust scale | Validated 12-item trust measurement instrument — essential for PS5 user study design | PS5 |
| Sarter & Woods (1995) — Automation mode confusion | Empirical studies of how users misunderstand intermediate automation modes in aviation — directly relevant to CAUTION mode comprehension | PS5 |

**Action**: Find PDFs, extract using `/extract-paper` or `/batch-extract`, then update tracker.

**Expected outcome**: PS4 moves to "Partially Supported" (methodological foundation exists, not yet applied to governance). PS5 moves to "Partially Supported" (validated instruments and mode confusion precedent exist).

### 1.2 Low-Resource AI Deployment Papers (C5 — Medium)

T4 has only 4 Yes papers for a theme in the dissertation title. Need 2–3 more covering:

| Search area | What to look for | Why |
|-------------|-----------------|-----|
| Edge AI / offline-first architectures | Systems designed for intermittent connectivity with safety considerations | Validates architecture's local state classification and pre-cached recommendation logic |
| Disaster response AI | Decision support under communication breakdown and resource scarcity | Similar constraint profile to coastal fisheries — analogous deployment context |
| Remote healthcare / telemedicine AI | Decision support under limited bandwidth and specialist scarcity | More mature literature with transferable design patterns for low-resource AI |

**Action**: Search, find 2–3 papers, extract, update tracker.

**Expected outcome**: T4 moves from "Partially Covered" (4 Yes) to "Well-Covered" (7+ Yes).

### 1.3 Search Keywords

For 1.1:
- `"levels of automation" safety-critical`
- `"trust in automation" calibration "decision support"`
- `"automation mode confusion" "mode awareness"`
- `"human factors" "graduated automation"`

For 1.2:
- `"edge AI" safety governance offline`
- `"disaster response" AI "decision support" "resource constrained"`
- `"telemedicine AI" "low resource" "decision support"`
- `"offline-capable" AI safety-critical`

---

## Phase 2: Document Edits (C1b, C3, C4, R1, R2, R3)

**Goal**: Strengthen the argumentative structure of `review-plan.md` based on examiner feedback.

### 2.1 First-Principles Argument for Graduated Governance (C1b — High)

**Where**: `papers/review-plan.md` — Section 4 (The Two-Level Governance Gap)

**What to add**: A subsection before the comparator analysis arguing why binary governance is structurally inadequate, not just absent. The argument:

> Binary governance forces a false dilemma:
> - **Over-restriction**: Disabling AI entirely when environmental conditions are elevated but manageable wastes a scarce resource — particularly costly in low-resource settings where AI assistance is most valuable.
> - **Under-restriction**: Permitting full AI participation under elevated risk exposes users to recommendations that may not account for degraded conditions.
> - **The missing middle**: Graduated governance enables a CAUTION mode where AI operates under a restricted recommendation space — providing partial assistance calibrated to actual risk, rather than forcing an all-or-nothing choice.
>
> Empirical evidence: Gao (2024) documents that Penang fishers already make tripartite decisions (go / cautious-go / don't-go), demonstrating that practitioners naturally distinguish an intermediate risk state. The proposed architecture formalises this existing practice rather than imposing an artificial abstraction.

### 2.2 Baxi Comparative Analysis Table (C3 — Medium)

**Where**: `papers/review-plan.md` — Section 4 (The Two-Level Governance Gap), after Baxi discussion

**What to add**: A table contrasting environmental-state conditioning vs robustness conditioning:

| Dimension | Environmental state (proposed) | Agent robustness (Baxi) |
|-----------|-------------------------------|------------------------|
| **Observation mechanism** | Sensor inputs (weather, sea state, visibility) | Offline evaluation / benchmark testing |
| **Update frequency** | Continuous — changes during operation | Static — assessed at deployment or periodic review |
| **Governance response** | Real-time reclassification triggers immediate scope adjustment | Tier assignment persists until re-evaluation |
| **Failure mode** | Misclassification of environmental state → wrong governance mode applied in real-time | Overestimation of robustness → overly permissive tier assignment persists |
| **Dynamic environments** | Designed for — environmental variability is the primary use case | Not designed for — assumes relatively stable agent capability |
| **Applicability** | Operational environments with varying external risk (fisheries, maritime, disaster response) | Controlled environments where agent properties can be evaluated offline |

**Why this matters**: The distinction is not merely a change of input variable — it demands fundamentally different observation mechanisms, update dynamics, and failure handling, constituting a distinct architectural contribution.

### 2.3 Domain Justification Restructuring (C4 — Medium)

**Where**: `papers/review-plan.md` — Section 6 (Low-Resource Deployment and Domain Context)

**What to change**: Foreground Gao as the centrepiece and restructure the domain argument around three pillars:

1. **Environmental variability as first-class concern**: Unlike automotive/industrial domains with relatively controlled operating environments, fisheries face continuously varying conditions (weather, sea state, visibility, tidal patterns) that directly determine operational safety — making environment-state-conditioned governance particularly natural.

2. **Existing informal graduated decision-making**: Gao's empirical finding (go / cautious-go / don't-go) demonstrates that the proposed SAFE/CAUTION/UNSAFE classification formalises existing practice, not an imposed abstraction. Move Gao from "Motivates" to **centrepiece role**.

3. **Resource constraints make binary governance costly**: In low-resource environments where AI assistance is valuable but scarce, a binary gate that disables AI entirely under moderate risk wastes that resource. CAUTION mode is specifically designed for contexts where partial AI assistance > no AI assistance.

### 2.4 Merge Governance Sections 2 & 3 (R1 — Structural)

**Where**: `papers/review-plan.md` — Section 7 (Literature Review Outline)

**What to change**: Combine "Section 2: AI Governance — Level 1 Participation Control" and "Section 3: AI Governance — Level 2 Advisory Scope Control" into a single section:

> **Section 2: AI Safety Governance Mechanisms**
> - 2.1 Participation governance (Level 1) — binary on/off, well-established
> - 2.2 Advisory scope governance (Level 2) — exists but static/per-action
> - 2.3 The state-conditioned governance gap — neither level is conditioned on classified environmental state
> - 2.4 [Forward reference] Brief preview of proposed two-level governance pair

This creates a continuous escalation toward the gap rather than two separate stops.

### 2.5 Comparative Summary Table of Top Comparators (R2 — Structural)

**Where**: `papers/review-plan.md` — new subsection in Section 4 or as standalone Section 4.5

**What to add**: A 6–8 row table comparing top comparators across consistent dimensions:

| Architecture | Governance trigger | Governance level | Governance mode | Runtime vs design-time | Formal safety property |
|-------------|-------------------|-----------------|-----------------|----------------------|----------------------|
| Shields (Könighofer) | MDP state | L1 + partial L2 | Binary per-state | Runtime | Inductive winning region |
| Dalrymple | World model | L1 only | Binary | Runtime | Verifier pass/fail |
| Bajcsy/Fisac | System state z | L1 only | Binary | Runtime | Theorem 1 (HJ reachability) |
| Flehmig | AI performance | L1 only | Graduated (3-level) | Runtime | Weighted index threshold |
| Baxi | Agent robustness | L1 + L2 | Graduated (K-tier) | Design-time assessment | Bounded exposure theorem |
| Shamsujjoha | Per-artifact | Partial L1 + L2 | Binary per-layer | Runtime | None (defence-in-depth) |
| AgentSpec | Per-action rule | L1 + partial L2 | Binary per-action | Runtime | Soundness theorem |
| **Proposed** | **Environmental state** | **L1 + L2 unified** | **Graduated (3-mode)** | **Runtime** | **Safety Dominance Property** |

### 2.6 Forward Reference to Contribution (R3 — Structural)

**Where**: `papers/review-plan.md` — end of merged Section 2 (after 2.3)

**What to add**: A brief forward reference (2–3 sentences) previewing the proposed architecture so readers evaluate subsequent sections with the contribution in mind:

> *"The architecture proposed in this research addresses this gap through a two-level governance pair (G(S), A_AI(S)) conditioned on classified environmental safety state S = f(E), where AI participation and recommendation scope both narrow as operational risk increases. The following sections examine the formal, domain, and evaluation dimensions of this gap."*

---

## Phase 3: Search Methodology Documentation (C1a)

**Goal**: Make the "0 papers" claim auditable by documenting the search protocol.

### 3.1 Create Search Protocol Document (C1a — High)

**Where**: New file — `papers/search-methodology.md`

**What to include**:

1. **Research questions driving the search** — mapped to RQ1–RQ5
2. **Databases searched** — Scopus, Web of Science, IEEE Xplore, ACM Digital Library, Google Scholar, arXiv
3. **Search strings** — primary and secondary, with Boolean operators
4. **Inclusion criteria** — language, date range, relevance to governance/safety/fisheries
5. **Exclusion criteria** — duplicates, non-English, purely theoretical with no architectural content
6. **Screening process** — title/abstract screening → full-text screening → extraction
7. **PRISMA flow diagram** — showing numbers at each stage (identified → screened → eligible → included)
8. **Snowball and citation chasing** — how additional papers were identified from reference lists
9. **Date of last search** — for reproducibility

**Note**: This documents the search *retrospectively* based on the actual process followed. The PRISMA numbers should reflect the real funnel (papers identified, screened, excluded, extracted).

---

## Phase 4: Housekeeping (C6)

**Goal**: Strengthen citation quality and regenerate analysis with new papers.

### 4.1 Check Peer-Reviewed Status of ArXiv Preprints (C6 — Low)

Check whether peer-reviewed versions exist for these core comparators:

| Paper | Current venue | Action |
|-------|--------------|--------|
| Bajcsy & Fisac (2024) | arXiv preprint | Search for conference/journal publication |
| Dalrymple et al. (2024) | arXiv preprint | Search for conference/journal publication |
| Baxi (2025) | arXiv preprint | Search for conference/journal publication |

If peer-reviewed versions exist: update `paper_tracker.md` venue field and notes files.
If not: add "(preprint)" qualifier when introducing each paper in the literature review.

### 4.2 Update Paper Tracker

After Phase 1 extractions complete:
- Add all new papers to `papers/paper_tracker.md`
- Update theme counts in Table 2

### 4.3 Re-run `/plan-review`

After all new papers are extracted and edits applied:
- Re-run `/plan-review` to regenerate `papers/review-plan.md` with updated corpus
- Verify PS4/PS5 status has improved
- Verify T4 coverage has improved
- Confirm all Phase 2 edits are preserved or re-integrated

---

## Execution Order & Dependencies

```
Phase 1 (New Papers)
├── 1.1 Levels-of-automation & trust papers ──┐
└── 1.2 Low-resource AI papers ───────────────┤
                                               ▼
Phase 2 (Document Edits) ◄── Can start in parallel with Phase 1
├── 2.1 First-principles argument             │
├── 2.2 Baxi comparative table                │
├── 2.3 Domain justification restructuring    │
├── 2.4 Merge governance sections             │
├── 2.5 Comparative summary table             │
└── 2.6 Forward reference                     │
                                               ▼
Phase 3 (Search Methodology) ◄── Requires Phase 1 complete (need final paper counts)
└── 3.1 Search protocol + PRISMA flow         │
                                               ▼
Phase 4 (Housekeeping) ◄── Requires Phases 1–3 complete
├── 4.1 ArXiv peer-review check               │
├── 4.2 Update tracker                        │
└── 4.3 Re-run /plan-review                   │
```

---

## Expected Outcomes

| Metric | Before | After |
|--------|--------|-------|
| PS4 coverage | Unsupported | Partially Supported |
| PS5 coverage | Unsupported | Partially Supported |
| T4 (Low-resource) | 4 Yes papers | 7+ Yes papers |
| Argumentative chain Links 8–9 | No papers | 4–6 papers providing methodological grounding |
| Baxi differentiator | Implied | Explicitly argued with comparative table |
| Domain justification | One paper among many | Centrepiece argument with three pillars |
| Search auditability | None | Full PRISMA flow + search protocol |
| ArXiv comparators | Unmarked | Peer-reviewed or explicitly flagged |
| Literature review outline | 7 sections | 6 sections (merged governance) with forward reference |
| Comparator positioning | Narrative only | Summary table + narrative |

---

## Severity Mapping (from examiner feedback)

| Priority | Actions | Phase |
|----------|---------|-------|
| **High** | C1a (search methodology), C1b (first-principles argument), C2 (PS4/PS5 papers) | Phases 1, 2.1, 3 |
| **Medium** | C3 (Baxi differentiator), C4 (domain justification), C5 (T4 papers) | Phases 1.2, 2.2, 2.3 |
| **Low** | C6 (ArXiv peer-review check) | Phase 4.1 |
| **Structural** | R1 (merge sections), R2 (comparator table), R3 (forward reference) | Phases 2.4, 2.5, 2.6 |