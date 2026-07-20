# Literature Review Extraction (Reduced)
## Paper: Lessons from complex systems science for AI governance

---

## 1. Paper Identity

- **Full title:** Lessons from complex systems science for AI governance
- **Authors:** Noam Kolt, Michal Shur-Ofry, Reuven Cohen
- **Affiliations:** Faculty of Law + School of Computer Science and Engineering, Hebrew University, Jerusalem; Department of Mathematics, Bar-Ilan University
- **Year:** 2025
- **Venue:** *Patterns* (Cell Press), vol. 6, 101341, August 8, 2025 — Perspective, open access
- **DOI:** https://doi.org/10.1016/j.patter.2025.101341
- **Type:** Peer-reviewed perspective — conceptual/policy argument, no empirical study, no architecture
- **Extraction category:** External evidence (policy-layer complexity critique — peer-reviewed counterpart to, and replacement for, Paz 2025)

---

## 2. Core Contribution

- **Argument:** Contemporary AI systems and their environments exhibit the defining properties of complex adaptive systems — nonlinear growth, emergence (qualitatively new abilities past thresholds), feedback loops (e.g., training on synthetic data), interconnectedness with critical infrastructure, and cascading effects. Traditional governance approaches assume linear cause-and-effect and are "not up to the task."
- **Three desiderata for complexity-compatible AI governance:**
  1. **Early and scalable intervention** — in complex systems the case for intervention *declines* over time: early action on limited information can prevent harm; later action on complete information may no longer be effective (pandemic-containment analogy).
  2. **Adaptive institutional design** — institutions able to update as the system evolves.
  3. **Complexity-compatible risk thresholds** — regulators should not postpone action until a full evidentiary burden is met, because in complex systems the decisive information "may only become available at a time after which intervention has become more costly or less effective"; policymakers must "satisfice," acting on incomplete information at calibrated thresholds.

**Key quote (Bigger Picture):** *"Traditional governance approaches, which often assume linear cause-and-effect relationships, are not up to the task... [we propose] risk thresholds that reflect the nonlinearity of AI systems and their interactions with other sociotechnical structures."*

---

## 3. Relevance to My Research

Governance theme at the **policy/regulatory layer** — the peer-reviewed complexity critique. Serves the same argumentative role as Paz (2025) [[notes]](../notes/From%20Linear%20Risk%20to%20Emergent%20Harm-%20Complexity%20as%20the%20Missing%20Core%20of%20AI%20Governance.md) but from a citable venue (*Patterns*), with law + CS + mathematics authorship. **Where one complexity-critique citation is needed, cite Kolt et al., not Paz.**

**Extraction decision:** Reduced extraction, external evidence.

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- Peer-reviewed support that governance premised on **linear risk and static evidentiary thresholds is structurally mismatched** to systems with nonlinear, emergent dynamics — motivating governance that responds to current conditions at calibrated thresholds rather than waiting for full certainty.
- Two structural resonances with the architecture (as analogy, clearly flagged as ours):
  - **Calibrated risk thresholds acted on under incomplete information** — the CAUTION state is precisely a threshold-triggered response to conditions that do not yet constitute proven danger: intervention (scope contraction) before harm materialises, rather than a binary gate that waits for UNSAFE.
  - **Early intervention beats late certainty** — the graduated architecture operationalises this at runtime: contracting advisory scope early (CAUTION) is effective; blocking only when danger is certain (binary gating) intervenes at the point where, in Kolt et al.'s terms, intervention has become less effective.
- Completes the policy-layer triad: Kolt et al. (complexity critique of linear/static governance), Engin & Hand (constructive proposal: categories as thresholds over monitored dimensions) [[notes]](../notes/Towards%20Adaptive%20Categories-%20Dimensional%20Governance%20for%20Agentic%20AI.md), Reuel et al. (empirical planning–execution gap) [[notes]](../notes/Responsible%20AI%20in%20the%20Global%20Context-%20Maturity%20Model%20and%20Survey.md).

**What this paper CANNOT be cited for (overreach guard):**

- Its subject is **regulatory governance of AI as a technology in society** — policymakers, institutions, evidentiary standards — not runtime governance of an AI system's output. It contains no architecture, no runtime mechanism, and no advisory scope concept; the words "binary" and "graduated" do not appear. The mapping from regulatory thresholds to S = f(E) is *our* structural analogy and must be presented as such.
- Complex-systems vocabulary carries the same **project positioning caution** as Paz: sociotechnical framing stays out of Chapter 2's primary argument and the methodology; use in motivation or RQ5/discussion registers only.
- Do not use it as gap evidence — it says nothing about what architectures implement.

---

## 5. Positioning for This Research

**Positioning paragraph:** Kolt, Shur-Ofry, and Cohen (2025) argue from complex systems science that AI governance premised on linear cause-and-effect is structurally inadequate: because AI systems exhibit nonlinear growth, emergence, and cascading effects, governance must intervene early and at calibrated risk thresholds, acting on incomplete information — since by the time full evidence of danger is available, intervention "has become more costly or less effective." Although addressed to regulators and institutions rather than runtime systems, the argument translates structurally to the departure-decision setting: a binary gate that permits full-scope AI advice until danger is proven enacts, at runtime, exactly the wait-for-certainty policy Kolt et al. identify as failing in complex environments. The graduated architecture operationalises their prescription at the system level — the CAUTION state is an early, threshold-calibrated intervention that contracts advisory scope while conditions are still marginal, rather than deferring all restriction to the point where conditions are unambiguously unsafe.

---

## 6. Overall Relevance Score

### ⭐⭐ Low–Medium (external evidence)

**Justification:** No architecture or empirical content, but the authoritative, peer-reviewed version of the complexity critique — it supersedes Paz (2025) for citation purposes and completes the policy-layer motivation triad with Engin & Hand and Reuel et al. Best used in motivation or discussion for the early-intervention-at-calibrated-thresholds argument, which gives the CAUTION mode an independent theoretical rationale. Keep out of the architectural gap argument and out of the thesis's primary CS framing.
