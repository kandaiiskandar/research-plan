# Literature Review Extraction (Reduced)
## Paper: AI governance: a systematic literature review

> **DOI correction:** third-party summaries have circulated this paper with DOI 10.1007/s43681-024-00569-5 — that DOI belongs to **Attard-Frost & Lyons (2025)** (conference paper ref [22]). The correct DOI, verified from the PDF, is **10.1007/s43681-024-00653-w**.

---

## 1. Paper Identity (verified from PDF)

- **Full title:** AI governance: a systematic literature review
- **Authors:** Amna Batool, Didar Zowghi, Muneera Bano
- **Affiliation:** CSIRO's Data61, Melbourne, Australia
- **Year:** 2025 (received 21 Jul 2024; accepted 12 Dec 2024; published online 14 Jan 2025)
- **Venue:** *AI and Ethics* (Springer), vol. 5, pp. 3265–3279 — open access (CC BY)
- **DOI:** https://doi.org/10.1007/s43681-024-00653-w
- **Type:** Systematic literature review — 28 primary studies
- **Extraction category:** External evidence (institutional-layer governance SLR; complements Attard-Frost & Lyons and Reuel et al.)

---

## 2. Core Contribution

- **Method:** SLR of 28 articles analysing AI governance along four questions — **WHO** is accountable (stakeholders), **WHAT** is governed (data, systems, processes), **WHEN** governance occurs (**within the AI development life cycle**: pre-, during-, post-development), and **HOW** it is implemented (frameworks, tools, policies, models). Artifacts categorised into five governance levels adapted from Lu et al.: team, organization, industry, national, international.
- **Key findings (verified):**
  - **Only 3 of 28 studies** answer all four questions — governance coverage is fragmentary, not holistic.
  - The **largest share of governance solutions is organization-level**.
  - *"Many existing governance frameworks prioritize compliance and risk management, often focusing on technical and operational aspects such as performance, accuracy, and scalability"* — ethical guidelines are often unenforceable "suggestions."
  - **Lack of human involvement:** many governance approaches "focus on automating decision-making processes, often sidelining the role of human judgment and accountability," making them less human-centric.

---

## 3. Relevance to My Research

Governance theme at the **institutional layer**. Two specific values:

1. **Holistic-coverage gap:** 3/28 studies covering who/what/when/how corroborates, from a general governance SLR, the fragmentation the review documents at the architectural level.
2. **The WHEN dimension is the sharpest point for this research:** in this literature, the *temporal* dimension of governance is the **development life cycle** (pre-/during-/post-development). Even where the field asks *when* governance applies, the answer is design-lifecycle time — not runtime operational state. The concept of governance conditioned on the *current classified environmental state during operation* is absent from the SLR's entire analytical frame. This parallels, at the review level, the design-time vs. runtime finding in the conference paper §4.3.

**Extraction decision:** Reduced extraction, external evidence.

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- Corroboration in §4.6-style synthesis: a general AI-governance SLR finds coverage fragmentary (3/28 holistic), concentrated at the organization level, and oriented to compliance/risk management over enforceable principles — consistent with governance effort concentrating at layers other than runtime operation.
- The **WHEN-dimension observation** (our structural reading of their verified frame): the governance literature's own temporal axis is the development lifecycle; runtime state-conditioned governance sits outside its analytical categories entirely.
- The **human-involvement finding** supports the human-in-the-loop positioning of the architecture (Layer 4 as terminal decision authority), in motivation or discussion registers.

**What this paper CANNOT be cited for (overreach guard):**

- It does **not** identify, or come near, the advisory scope gap — its "how" artifacts are institutional (frameworks, policies, tools across team-to-international levels). The claim that it "directly supports" the advisory-scope argument overstates; it supports the *general* fragmentation/misdirection motivation only.
- The "lack of human involvement" finding concerns governance approaches sidelining human judgment — it is not evidence about decision-support systems or fisher-facing tools.
- Use the corrected DOI (10.1007/s43681-024-00653-w); the circulated 00569-5 is a different paper already cited as [22] — a duplicate-looking citation with two different papers on the same DOI would be a serious reference-list error.

---

## 5. Positioning for This Research

**Positioning paragraph:** Batool, Zowghi, and Bano (2025), systematically reviewing 28 AI governance studies, find coverage to be fragmentary — only three studies address who governs, what is governed, when, and how — with solutions concentrated at the organizational level and oriented toward compliance and risk management rather than enforceable principle. Notably, the review's temporal dimension of governance ("when") is defined entirely over the AI development life cycle (pre-, during-, and post-development): even where the governance literature explicitly asks when governance applies, the answer is design-lifecycle time, not runtime operational state. The concept of governance conditioned on a classified environmental state during operation falls outside the analytical frame of the field's own systematic reviews — consistent with this review's finding that runtime, state-conditioned advisory governance is a dimension the literature has yet to address.

---

## 6. Overall Relevance Score

### ⭐⭐ Low–Medium (external evidence)

**Justification:** Peer-reviewed, open-access SLR from CSIRO Data61 — a citable institutional-layer corroborant joining Attard-Frost & Lyons [22] and Reuel et al. [31]. Its distinctive value is the WHEN-dimension observation, which extends the design-time/runtime contrast to the level of the governance literature's own review categories. Best used as one sentence in the conference paper §4.6 or the thesis Chapter 2 governance synthesis. Not gap evidence for advisory scope specifically; not a comparator.
