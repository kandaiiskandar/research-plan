# Viva Q&A — Novelty, Problem, and Gap

**Purpose:** Examiner-style questions and prepared answers for PhD viva defence.  
**Section:** Novelty, problem statement, and gap identification.  
**Research title:** *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Comparative Evaluation in Coastal Fisheries*

---

## Part 1 — What Is the Novelty?

---

**Q: What is the single most novel contribution of your research?**

The primary contribution is the governance pair **(G(S), A_AI(S))** — a two-level architecture that conditions both whether the AI participates and what the AI is permitted to recommend on a classified environmental safety state. The novel element is the second level: a formally specified AI-admissible recommendation space A_AI(S) that contracts as safety state worsens. No existing architecture implements this. Every reviewed system is binary at the governance level — AI either operates at full scope or is blocked. My architecture introduces a formally novel intermediate mode, CAUTION, where the AI remains active but its admissible output space is structurally restricted to recommendation types the current environmental conditions can reliably support.

---

**Q: Is this just a three-state on/off switch? How is that novel?**

No. A three-state switch would be G(S) ∈ {full, partial, off} — which is still just a participation gate. My contribution is at a different level. Under CAUTION, the gate is open (G(S) = 1) — the AI participates. What changes is the admissible recommendation space: A_AI(CAUTION) = {Go, Delay}, compared to A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}. The AI still reasons and still outputs a recommendation. It is structurally prevented — before reasoning begins — from generating recommendation types that the environmental data can no longer reliably support. This is pre-generation scope restriction, not a participation toggle.

---

**Q: What is the formal novelty? Can you state it precisely?**

Three formal elements together constitute the contribution:

1. **The governance pair (G(S), A_AI(S))** — two functions operating simultaneously on the classified safety state S. Level 1 controls participation; Level 2 controls advisory scope. No prior architecture formalises both.

2. **The containment property** — A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. The admissible recommendation space is strictly nested and contracts monotonically as safety state worsens.

3. **The Safety Dominance Property** — AI(E) ⊆ A_AI(S) for all E. Whatever the AI recommends is always within the admissible space determined by the current safety state. This holds by construction for the symbolic prototype via Rule-Set Starvation: the governance layer supplies only RS(CAUTION) to the inference engine before reasoning begins, so no rule exists in that configuration that can produce DepartureTime or Duration.

---

**Q: Why does the CAUTION mode matter? Why not just block the AI entirely under marginal conditions?**

Blocking entirely is the binary approach — and it has a cost. In real low-resource environments, marginal conditions are frequent. A system that goes silent every time conditions are ambiguous provides no decision support during the periods when fishers most need guidance. The CAUTION mode preserves advisory continuity — the AI still tells the fisher whether to go or delay — while withdrawing the recommendation types (precise departure time, trip duration) that depend on data precision the environment can no longer provide. The system communicates increased risk through what it withholds, not just what it displays. This is the specific behaviour that binary architectures cannot produce.

---

**Q: Is the Safety Dominance Property a theorem or just a definition?**

It is a proof by construction. I define RS(CAUTION) to contain only rules producing outputs in {Go, Delay}. The governance layer supplies only RS(CAUTION) to the inference engine when S = CAUTION. Since no rule in RS(CAUTION) can produce DepartureTime or Duration, AI(E) ⊆ {Go, Delay} = A_AI(CAUTION) holds by definition of the rule set. The property is non-trivial because it must hold for all possible inputs E — not just tested cases — and it holds structurally, not as a result of runtime filtering. The formal specification and proof in this thesis are scoped deliberately to the symbolic advisory reasoning engine. Because the Governance Layer runs before inference and is separated from the reasoning engine, the architectural pattern is not tied to a symbolic Layer 3 in principle; a probabilistic implementation would require an alternative pre-inference enforcement mechanism, and I treat that as future work outside the scope of the formal specification (O2), the prototype (O3), and the evaluation (O4).

---

**Q: Where does your architecture sit relative to existing safety AI frameworks?**

It is a domain-specific, state-conditioned instantiation within the Guaranteed Safe AI framework (Dalrymple et al., 2024). GS AI requires formal proof certificates before AI output is deployed — but it is binary at the verification level: a policy either passes (AI operates) or fails (AI is blocked). My architecture extends GS principles into graduated governance by introducing a third mode where verification is conditioned on environmental safety state rather than applied globally to a policy. The Safety Dominance Property is the domain-specific safety specification in GS terms; the governance layer (Layer 2) is the verifier — deterministic, non-AI, and assurably guarded as per Bloomfield and Rushby (2025).

---

## Part 2 — What Is the Problem?

---

**Q: What problem does your research solve?**

Existing AI governance architectures for safety-critical decision support are binary: the AI either generates its full recommendation set or is blocked entirely. This binary structure creates a dangerous gap at intermediate-risk conditions. When environmental conditions are marginal — not fully safe, not fully dangerous — a binary-gated system with G(S) = 1 continues to generate high-specificity recommendations such as precise departure times and trip durations, even though the underlying environmental data can no longer reliably support that precision. The human decision-maker receives confident-looking advice without any architectural signal that advisory scope has become questionable. My research solves this by introducing a formally specified intermediate governance mode — CAUTION — that restricts what the AI may recommend under marginal conditions, rather than choosing between full output or silence.

---

**Q: Why is this specifically a problem in coastal fisheries?**

The fisheries context makes the problem concrete and consequential. Small-scale coastal fishers in Malaysia (Zone A, 0–5 nautical miles) make departure decisions three to six times per week without institutional safety support. Dominguez-Péry et al. (2023) found that wind, weather, and visibility account for 26.7% of maritime accident risk segments, with small vessels recording the highest fatality rank across size categories. Marginal environmental conditions — not fully safe, not fully dangerous — are the norm, not the exception. A binary-gated AI in this context is either giving full tactical advice under marginal conditions (the over-reliance risk documented by Wen et al., 2025) or going silent when the fisher still needs guidance. Neither is acceptable. The CAUTION mode addresses exactly this intermediate-risk regime.

---

**Q: Is the problem unique to fisheries, or is it general?**

The problem is general. The formal contribution — a governance pair (G(S), A_AI(S)) that contracts AI advisory scope as classified environmental safety state worsens — is domain-agnostic. The formal properties hold for any valid threshold assignment. The fisheries domain provides the motivation, the application context, and the validation population. It is not the contribution. The same architecture applies to any safety-critical domain where AI advisory scope should vary with classified operational risk: remote agricultural operations under extreme weather, maritime search-and-rescue coordination, disaster response triage, and remote mining in hazardous conditions.

---

**Q: What specifically goes wrong without your architecture?**

Without Level 2 governance, a binary-gated system (C1 in my evaluation) behaves identically to my proposed architecture (C2) under SAFE and UNSAFE conditions. The difference only appears under CAUTION. Under CAUTION, C1 allows the AI to generate the full recommendation set — including DepartureTime and Duration — because G(S) = 1 and there is no A_AI(S) restriction. C2 restricts the AI to {Go, Delay} under the same conditions. Wen et al. (2025) document the consequence: operators receiving high-specificity AI output under deteriorating conditions tend toward over-reliance, accepting recommendations the environmental data can no longer reliably support. My evaluation (RQ4) isolates this directly — the C1 vs. C2 comparison under CAUTION is the discriminating test, because the two architectures are identical at Level 1 under CAUTION. Any difference in output is attributable entirely to Level 2 governance.

---

## Part 3 — How Did You Find the Gap?

---

**Q: How did you establish that this gap exists? Could you have missed something?**

The gap is confirmed by four independent sources across different bodies of literature. I did not rely on a single review.

**Source 1 — The architecture literature directly.** I examined all primary safety-critical AI governance systems and found only binary governance in every case: shields (Könighofer et al., 2025), guaranteed safe AI (Dalrymple et al., 2024), safety filters (Bajcsy and Fisac, 2024), and supervision functions (Abella et al., 2025). All gate on a single boundary — safe or not safe.

**Source 2 — A systematic review of ML systems architecture.** Indykov et al. (2025) reviewed 206 papers and identified 16 architectural tactics for ML-enabled systems. In their trade-off matrix, AT11 (rule-based models) → Safety = 0: insufficient evidence of any formally demonstrated positive impact on the Safety attribute across the entire reviewed literature. If a mechanism like mine existed and had been studied, it would appear in this matrix.

**Source 3 — The theoretical safety AI framework.** Dalrymple et al. (2024) explicitly acknowledge that GS AI operates at the policy level and is binary at verification. They do not propose an intermediate mode. The gap is visible from within their own framework.

**Source 4 — The closest structural precedent.** Flehmig et al. (2024) is the most important paper for gap identification. They propose a three-level traffic-light degradation index for AI in safety-critical industrial systems — structurally almost identical to my three safety states. But at their intermediate level (Orange), the AI continues to operate with identical, unrestricted scope as at Level 1 (Green). The intermediate level governs human supervisory behaviour, not AI recommendation content. This is the binary governance problem appearing inside a three-level framework — the most precise available evidence that the CAUTION mode gap is real and remains unfilled even in the closest related work.

---

**Q: Why is Flehmig et al. (2024) the most important paper for your gap argument?**

Because it confirms the gap at maximum structural proximity. If any paper was going to fill the CAUTION mode gap, it would be Flehmig et al. — they have a three-level classification, a non-AI monitoring layer, a limiting logic for AI outputs, and a deterministic backup. Their system has almost every structural element of mine. But even they do not restrict what the AI may recommend at the intermediate level. They restrict what the *human supervisor does*. The AI gives identical outputs at Orange and Green. This means the gap is not an oversight in the broader literature — it persists even in the paper that came closest to filling it.

---

**Q: What distinguishes your architecture from Flehmig et al. (2024) precisely?**

Four dimensions:

| Dimension | Flehmig et al. (2024) | Proposed Architecture |
|---|---|---|
| Governance trigger | AI model performance degradation | Classified environmental safety state |
| Governance target | Human monitoring intensity | AI-admissible recommendation space |
| Intermediate mode effect | Supervisory activity increases; AI scope unchanged | AI scope formally restricted to A_AI(CAUTION) |
| Formal specification | Weighted degradation index | E → S = f(E) → (G(S), A_AI(S)) → AI(E) |

The critical difference is in the third row. Under Orange (their equivalent of CAUTION), the AI continues to generate DepartureTime and Duration. Under my CAUTION mode, the AI cannot generate those outputs — the rule set does not contain rules that produce them.

---

**Q: Why was this gap not filled earlier? Is there a reason no one did this before?**

Three structural reasons. First, most safety-critical AI literature focuses on autonomous agents (robotics, autonomous vehicles) where the output is an action, not an advisory recommendation. Restricting advisory scope by type is a distinction that only becomes visible when the AI produces structured, multi-type recommendations to a human decision-maker. Second, the deployment context matters — low-resource, offline-capable systems are underrepresented in the safety AI literature, which tends toward high-compute, always-connected systems. Third, the intermediate-risk problem is domain-sensitive: the frequency and consequences of marginal conditions vary by domain. In coastal fisheries, marginal conditions are the majority of operating time. In domains where conditions are either clearly safe or clearly dangerous, the gap is less visible.

---

**Q: How do you know your gap claim is still valid — could something have been published since your review?**

My gap argument rests on a structural absence: no reviewed architecture formally specifies a pre-generation advisory scope restriction conditioned on classified environmental state. A paper that fills this gap would need to introduce both a safety state classification function and an admissible recommendation space that contracts with that state — and formally prove a containment property. I have not found such a paper in the literature reviewed. The four-source confirmation across Indykov, Dalrymple, Flehmig, and the domain literature (Haque and Al Jufaili, 2026) makes it unlikely this was missed. If a new paper emerges during examination, my response would be to characterise exactly where it overlaps and where it differs — the gap argument is precise enough to survive a near-miss.

---

*Last updated: June 2026*  
*Cross-references: `docs/discussion-notes-governance-gap-precedents-and-formal-foundations.md`, `docs/research-alignment-table.md`, `docs/appendix-c-formalisation.md`*
