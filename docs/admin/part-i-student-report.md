# PART I — STUDENT'S REPORT

**Student Name:** Iskandar Samsuddin
**Reporting Period:** Six months (December 2025 – May 2026)
**Supervisor Meetings:** Twice every two weeks
**Research Title:** *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Comparative Evaluation in Coastal Fisheries*

Research progress is tracked at: **https://kandaiiskandar.github.io/research-plan/**

---

## Milestones Achieved

### Supervisor Meeting — Review of First Proposal Draft

The first draft of the research proposal was presented to the supervisor and reviewed in detail. The review covered the problem statement, research objectives, research gap, and research questions. The supervisor's feedback confirmed that the four elements needed to be more tightly linked to one another and that the literature review required deeper engagement with the formal AI safety architecture literature. Following this review, the problem statement was revised to focus precisely on the binary governance gap, the research questions were restructured around the architectural contribution, and the literature review was expanded accordingly.

---

### Formal Architecture

The first architecture draft was presented to the supervisor for review. The two-level governance pair (G(S), A_AI(S)) is fully designed and formally specified — where G(S) is the participation gate that controls whether the AI is allowed to operate at all, and A_AI(S) is the admissible recommendation space that defines what the AI is permitted to recommend, both conditioned on the classified environmental safety state S. The four-layer architecture is documented with the full governance table, advisory scope containment hierarchy, scenario walkthrough, and six-limitation analysis (L1–L6).

### Gap Argument

To establish the gap, the literature was surveyed across the formal AI safety architecture, ML systems quality, and guaranteed safe AI bodies of work. From this survey, four independent sources were identified that each confirm the same absence from a different direction: (1) no existing architecture formally restricts AI advisory scope based on classified environmental safety state; (2) Indykov et al. (2025), after reviewing 206 papers and 16 architectural tactics, found that no tactic demonstrates formal positive impact on the Safety quality attribute; (3) Dalrymple et al. (2024) show that Guaranteed Safe AI operates at a binary verification level with no intermediate CAUTION mode; and (4) Flehmig et al. (2024), the closest structural precedent found, implement a three-level traffic-light model but use the intermediate level to govern supervisory behaviour, not AI advisory scope. The identified gap in existing safety-critical AI architectures was then presented to the supervisor. The four-layer gap argument is complete, establishing the research gap from four independent sources across three bodies of literature. This forms the core of the Chapter 2 comparative analysis and viva preparation materials.

### Environmental State Vector

E = {w, r, m, o, v, t} is formally defined with full empirical justification for each parameter. Worst-case aggregation is justified from five independent sources. Illustrative threshold values are documented with their sources, pending domain expert calibration.

### Layer 3 Enforcement Mechanism

During the architecture review, the supervisor raised the possibility of using an Analytic Hierarchy Process (AHP) to weight environmental parameters and produce a composite safety score. This was examined and set aside: a weighted composite allows a dangerous reading in one parameter to be diluted by favourable readings in others, which is unacceptable in a safety-critical context. The discussion led to the adoption of the worst-case aggregation rule instead. Following that, the production rule system was selected for Layer 3, the enforcement mechanism was specified, and the Safety Dominance Property was proved by construction across all three safety state cases. This resolves the critical path item that blocked formal completion of the architecture.

### Literature Review (Chapter 2)

All nine sections are in complete draft form. The Chapter 2 comparative analysis table covers 17 systems across four governance dimensions. The closing bridge paragraph has been drafted. The chapter is ready for supervisor review.

### RQ4 Evaluation Design

Twenty-scenario evaluation design with three conditions (C0 ungated, C1 binary-gated, C2 two-level graduated), primary and secondary metrics, per-scenario verification protocol, and expected results table. Ready for implementation once the prototype is built.

### RQ5 Study Design

Full instrument design, participant specification, session format, and success criteria. Ethical approval application is the next step before field recruitment.

### Dataset Acquisition and Label Derivation

The dataset required for prototype implementation (RQ3) and evaluation (RQ4) was identified and its acquisition plan documented. The primary data source is **MET Malaysia's Kawasan Perairan** (Marine Waters Forecast) for Western Sabah and Labuan, which provides three of the six E vector variables directly — wind speed (w), wave height (o), and rainfall condition (r) — with the marine warning level (m) derived from the official MET warning bulletin. Vessel category (v) comes from fisher registration data and time of day (t) from the system clock.

The safety state thresholds used in S = f(E) were anchored to MET Malaysia's published **Kriteria Amaran Angin Kencang dan Laut Bergelora** (Rough Seas and Strong Winds Warning Criteria), giving the UNSAFE classification boundary formal institutional authority. For example, the wind UNSAFE threshold (>27 knots / >50 km/h) corresponds to MET Malaysia's Category 2 warning onset.

Advisory AI training labels (Go / Delay) were derived from three independent empirical studies of small-scale fisher departure decisions: Rahim et al. (2024) among 79 fishing households in coastal Indonesia, Gao (2024) from 25 semi-structured interviews with Penang fishers, and Yamin et al. (2025) from 136 Terengganu fishers. All three independently document the same tripartite decision pattern — full operations / restricted operations / no operations — which maps directly to the SAFE / CAUTION / UNSAFE governance states. This cross-study convergence provides the empirical grounding for the Delay recommendation type in CAUTION mode.

### Research Alignment Table

Full traceability from all five problem statements to gap evidence, research questions, objectives, and methodologies. All design decisions are linked to justification documents.

---

## Latest Proposal and Upcoming Dissemination

Following the supervisor's advice to sharpen the focus on the novelty and the specific problem being solved, the proposal went through several rounds of revision. Earlier versions were too broad, mixing architectural and socio-technical concerns without a clear primary contribution. With the supervisor's direction to identify precisely what problem the architecture solves and what makes it novel, the research was recentred on the binary governance gap and the two-level governance pair as the core CS contribution.

This process also led to a title revision — from *"Design and Socio-Technical Evaluation"* to *"Design and Comparative Evaluation"* — to accurately reflect the CS-first positioning of the research and the three-condition comparative evaluation at the centre of RQ4.

The finalised proposal covers the complete architecture design, formal model, five research questions, evaluation designs for RQ4 and RQ5, and the supporting justification documents. Progress and supporting documents are tracked at **https://kandaiiskandar.github.io/research-plan/**.

I will be presenting this research at the **International Postgraduate Symposium on Computing and Informatics (IPSCI 2026)**. The presentation will cover the proposed two-level governance architecture, the formal gap argument, and the comparative evaluation design.
