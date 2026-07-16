# Literature Review Extraction (Reduced)
## Paper: Responsible AI in the Global Context: Maturity Model and Survey

---

## 1. Paper Identity

- **Full title:** Responsible AI in the Global Context: Maturity Model and Survey
- **Authors:** Anka Reuel, Patrick Connolly, Kiana Jafari Meimandi, Shekhar Tewari, Jakub Wiatrak, Dikshita Venkatesh, Mykel Kochenderfer
- **Affiliations:** Stanford University (USA); Accenture (Ireland, India, Poland)
- **Year:** 2025
- **Venue:** Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT '25), Athens, Greece, pp. 2505– (37 pages)
- **DOI:** https://doi.org/10.1145/3715275.3732165
- **Type:** Empirical survey + conceptual maturity model (peer-reviewed conference paper)
- **Scale:** 1,000 organizations, 20 industries, 19 geographical regions (organizations with annual revenue > USD 499M)
- **Extraction category:** External evidence (institutional-level governance implementation gap — not a runtime architecture paper)

---

## 2. Core Contribution

- **What it builds:** A conceptual RAI maturity model with two main dimensions — **organizational** RAI maturity (governance, risk management, monitoring and control processes) and **operational** RAI maturity (system-level measures against risks such as discrimination, reliability, privacy) — with staged levels from Initial to Optimized. The authors are the first to apply such a model at scale.
- **Headline results:**
  - Most organizations sit at mid-level (Managed) organizational maturity; only **9%** reach Optimized organizational maturity.
  - Only **0.8%** reach Optimized *operational* maturity; **no organization** reached Optimized on both dimensions.
  - Operational scores are heavily skewed low (mean ≈ 35), indicating widespread difficulty translating RAI principles into operations.
  - The discrepancy "poses a societal risk. Organizations might appear more prepared to handle AI responsibly than they actually are in practice... a false sense of security among stakeholders and potentially inadequate safeguards."

**Key quote (Abstract):** *"The findings also reveal significant strides towards RAI maturity, but we also identify gaps in RAI implementation that could lead to increased (public) risks from AI systems."*

**Key quote (Discussion):** *"...indicating a gap between planning and execution of RAI practices. This suggests formal RAI structures and policies exist, but implementation lags."*

---

## 3. Relevance to My Research

Governance theme only, at the **institutional layer**: the paper provides large-scale empirical evidence that AI governance, where it exists, exists predominantly as organizational policy and principle rather than operationalized, enforced practice. It does not address runtime architecture, advisory scope, environmental states, decision support, or low-resource deployment.

**Extraction decision:** Reduced extraction, external evidence — same institutional-evidence role as Attard-Frost & Lyons (2025) [[notes]](../notes/AI%20governance%20systems-%20A%20multi-scale%20analysis%20framework%2C%20empirical%20findings%2C%20and%20future%20directions.%20AI%20and%20Ethics.md), which it complements: Attard-Frost & Lyons show a national governance system contains no runtime state-conditioned advisory concepts; Reuel et al. show that even the governance organizations *do* plan is not operationally executed.

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- Empirical confirmation, at unprecedented survey scale, that a **planning–execution gap** is the norm in AI governance: formal structures and principles exist, enforcement and operationalization lag. This strengthens the motivation for governance mechanisms that are **enforced by construction** — architectural properties that hold regardless of organizational follow-through — rather than governance that depends on policy, process, and training being faithfully executed. The Safety Dominance Property, enforced structurally by state-specific rule sets, is exactly the kind of mechanism that is immune to a planning–execution gap.
- Evidence that the governance gap the thesis documents at the architectural level has a counterpart at the institutional level: even mature organizations do not operationally implement the safeguards they plan, so waiting for organizational governance to close the runtime gap is not credible.

**What this paper CANNOT be cited for (overreach guard):**

- It says nothing about runtime governance architectures, advisory scope, safety states, or decision support — do not cite it as evidence about what *architectures* do or don't implement. The architectural absence rests on the four-layer gap argument.
- The sample is large organizations only (revenue > USD 499M); small operators and low-resource contexts — the thesis's deployment setting — are outside the sample. If anything this understates the gap for low-resource contexts, but that extrapolation is ours, and the authors themselves urge "cautious extrapolation."
- Self-reported survey data with acknowledged positive-response and social-desirability biases; the true operational gap is plausibly larger than measured, but cite the measured numbers only.

---

## 5. Positioning for This Research

**Positioning paragraph:** Reuel et al. (2025), surveying 1,000 organizations across 20 industries and 19 regions against a two-dimensional responsible-AI maturity model, find that while 9% of organizations reach the highest stage of organizational RAI maturity (policies, governance structures, risk processes), only 0.8% reach it operationally, and none reach it on both dimensions — a systematic gap between RAI planning and execution in which "formal RAI structures and policies exist, but implementation lags." This institutional-level evidence complements the architectural gap documented in this review: governance that depends on organizational processes being faithfully executed demonstrably under-delivers in practice. It thereby motivates a design principle of the proposed architecture — safety-relevant governance should be enforced by construction, as a structural property of the system (the Safety Dominance Property, guaranteed by state-specific rule sets supplied before inference), rather than left to organizational policy whose execution the best available evidence shows to be unreliable.

---

## 6. Overall Relevance Score

### ⭐⭐ Low–Medium (external evidence)

**Justification:** Institutional-layer evidence only — no runtime architecture content — but peer-reviewed at FAccT, exceptional survey scale, and directly quotable for the planning–execution gap. Best cited alongside Attard-Frost & Lyons (2025) in the motivation/problem statement and wherever the by-construction enforcement design decision is justified (e.g., discussion of `justification-layer3-enforcement`). Not a governance comparator; keep it out of the architectural gap argument proper.
